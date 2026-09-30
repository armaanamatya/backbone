"""Calls the model on one document and returns claims (piece 2 of the build list).

The model reads one document at a time and reports what it says (R-12). It is
given no tools, and the document is passed in as data. The result is saved under
the file's hash, the model, the effort and the prompt version, so a second run
reads the saved result and calls nothing.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from . import coverage, quotes
from .logs import now
from .reading_schema import CLAIM_LISTS, READING_SCHEMA, validate

READING_PROMPT = "reading.md"
MAX_ATTEMPTS = 2

# Fields that identify the contact an item is about. They become columns of the
# claim; everything else the model returned for the item goes into its value.
COMMON_FIELDS = ("section", "contact", "quote", "line")
CONTACT_FIELDS = (
    "encounter_id",
    "appointment_id",
    "service_date",
    "service_class",
    "service_as_written",
)


class ModelCallError(Exception):
    pass


def find_claude(configured: str = "") -> str:
    """The `claude` program. On Windows the npm command is a batch file that
    mangles long arguments, so the program behind it is called directly."""
    found = configured or shutil.which("claude")
    if not found:
        raise ModelCallError("the `claude` command-line tool was not found on the PATH")
    path = Path(found)
    if os.name == "nt" and path.suffix.lower() != ".exe":
        behind = path.parent / "node_modules" / "@anthropic-ai" / "claude-code" / "bin" / "claude.exe"
        if behind.exists():
            return str(behind)
    return str(path)


def saved_path(settings, doc_hash: str) -> Path:
    model = re.sub(r"[^A-Za-z0-9.-]+", "-", settings.model)
    name = f"{doc_hash[:16]}__{model}__{settings.effort}__v{settings.prompt_version}.json"
    return settings.readings / name


def build_message(lines: list[str], feedback: list[str] | None = None) -> str:
    numbered = "\n".join(f"{number}| {text}" for number, text in enumerate(lines, start=1))
    message = f"<document>\n{numbered}\n</document>\n\nReport what this document says."
    if feedback:
        listed = "\n".join(f"- {error}" for error in feedback[:40])
        message += (
            "\n\nYour previous result for this document was rejected for these reasons:\n"
            f"{listed}\n\nReturn a complete, corrected result."
        )
    return message


def call_model(settings, message: str, prompt: str = READING_PROMPT, schema: dict = READING_SCHEMA) -> dict:
    """One call. Returns what the tool printed, with the time the call took.

    `prompt` names a file in the prompts folder, and `schema` is what the
    result must fit. The reading step uses the defaults; the plan call for a
    question passes its own.
    """
    command = [
        find_claude(settings.claude_path),
        "--print",
        "--model", settings.model,
        "--effort", settings.effort,
        "--system-prompt-file", str(settings.prompts / prompt),
        "--json-schema", json.dumps(schema, separators=(",", ":")),
        "--output-format", "json",
        "--tools", "",
        "--strict-mcp-config",
        "--disable-slash-commands",
        "--safe-mode",
        "--no-session-persistence",
        "--max-budget-usd", f"{settings.spending_cap_usd:.2f}",
    ]
    started = time.perf_counter()
    # An empty working folder, so nothing from this project reaches the model.
    with tempfile.TemporaryDirectory() as folder:
        try:
            done = subprocess.run(
                command,
                input=message.encode("utf-8"),
                capture_output=True,
                cwd=folder,
                timeout=settings.timeout_seconds,
            )
        except subprocess.TimeoutExpired as error:
            raise ModelCallError(f"no result after {settings.timeout_seconds} seconds") from error
    seconds = round(time.perf_counter() - started, 3)
    printed = done.stdout.decode("utf-8", errors="replace").strip()
    try:
        envelope = json.loads(printed)
    except json.JSONDecodeError as error:
        problem = done.stderr.decode("utf-8", errors="replace").strip() or printed[:500]
        raise ModelCallError(f"the tool did not print JSON (exit {done.returncode}): {problem}") from error
    if isinstance(envelope, list):
        results = [entry for entry in envelope if isinstance(entry, dict) and entry.get("type") == "result"]
        if not results:
            raise ModelCallError("the tool printed no result entry")
        envelope = results[-1]
    envelope["wall_seconds"] = seconds
    return envelope


def usage_of(envelope: dict) -> dict:
    """Tokens, time and cost of one call, as the tool reports them (R-23)."""
    usage = envelope.get("usage") or {}
    return {
        "wall_seconds": envelope.get("wall_seconds"),
        "api_seconds": None if envelope.get("duration_api_ms") is None else envelope["duration_api_ms"] / 1000,
        "input_tokens": usage.get("input_tokens"),
        "output_tokens": usage.get("output_tokens"),
        "cache_creation_input_tokens": usage.get("cache_creation_input_tokens"),
        "cache_read_input_tokens": usage.get("cache_read_input_tokens"),
        "cost_usd": envelope.get("total_cost_usd"),
        "turns": envelope.get("num_turns"),
        "models": envelope.get("modelUsage"),
    }


def result_of(envelope: dict) -> dict:
    """The structured result inside what the tool printed."""
    if envelope.get("is_error"):
        raise ModelCallError(f"the tool reported an error: {envelope.get('subtype')}: {envelope.get('result')}")
    result = envelope.get("structured_output")
    if result is None:
        text = (envelope.get("result") or "").strip()
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text)
        try:
            result = json.loads(text)
        except json.JSONDecodeError as error:
            raise ModelCallError("the result is not JSON") from error
    if not isinstance(result, dict):
        raise ModelCallError("the result is not a JSON object")
    return result


def problems_in(reading: dict, line_count: int) -> list[str]:
    """Schema failures, and references inside the result that point nowhere."""
    errors = validate(reading)
    if errors:
        return errors
    sections = {section["id"] for section in reading["sections"]}
    if not sections:
        errors.append("result.sections: a document has at least one section")
    refs = [contact["ref"] for contact in reading["contacts"]]
    for ref in sorted({ref for ref in refs if refs.count(ref) > 1}):
        errors.append(f"result.contacts: ref {ref!r} is used for more than one contact")
    for name in CLAIM_LISTS:
        for index, item in enumerate(reading[name]):
            where = f"result.{name}[{index}]"
            if item["section"] not in sections:
                errors.append(f"{where}.section: no section has id {item['section']}")
            if item.get("contact") is not None and item["contact"] not in refs:
                errors.append(f"{where}.contact: no contact has ref {item['contact']!r}")
            if not 1 <= item["line"] <= line_count:
                errors.append(f"{where}.line: the document has lines 1 to {line_count}")
    return errors


def read_document(settings, log, *, doc_hash: str, file_name: str, text: str) -> dict:
    """Reads one document, from the saved result if there is one.

    Returns a record with status "read" or "failed". A failed read is not saved,
    so the next run tries again.
    """
    path = saved_path(settings, doc_hash)
    if path.exists():
        with open(path, encoding="utf-8") as handle:
            record = json.load(handle)
        log.event("reading_reused", file=file_name, doc_hash=doc_hash, saved=path.name)
        record["reused"] = True
        return record

    lines = quotes.split_lines(text)
    attempts = []
    feedback = None
    reading = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        entry = {"attempt": attempt, "started_at": now()}
        try:
            envelope = call_model(settings, build_message(lines, feedback))
            entry["usage"] = usage_of(envelope)
            entry["session_id"] = envelope.get("session_id")
            candidate = result_of(envelope)
            errors = problems_in(candidate, len(lines))
        except ModelCallError as error:
            candidate, errors = None, [str(error)]
        entry["errors"] = errors
        attempts.append(entry)
        log.event(
            "model_call",
            purpose="reading",
            file=file_name,
            doc_hash=doc_hash,
            model=settings.model,
            effort=settings.effort,
            prompt_version=settings.prompt_version,
            attempt=attempt,
            accepted=not errors,
            errors=errors[:10],
            **entry.get("usage", {}),
        )
        if not errors:
            reading = candidate
            break
        # The error is shown to the model only when there is a result to correct.
        feedback = errors if candidate is not None else None

    record = {
        "doc_hash": doc_hash,
        "file_name": file_name,
        "model": settings.model,
        "effort": settings.effort,
        "prompt_version": settings.prompt_version,
        "read_at": now(),
        "status": "read" if reading is not None else "failed",
        "attempts": attempts,
        "reading": reading,
        "reused": False,
    }
    if reading is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(record, handle, ensure_ascii=False, indent=1)
    return record


UNIDENTIFIED = "unidentified"


def patient_key(document: dict) -> str:
    """The record number where the document prints one. Failing that, the name
    and date of birth. How patients are identified beyond this is open (O-18)."""
    if document.get("patient_record_number"):
        return document["patient_record_number"].strip()
    if document.get("patient_name"):
        name = " ".join(document["patient_name"].lower().split())
        return f"{name}|{document.get('patient_dob') or ''}"
    return UNIDENTIFIED


def _minutes(clock: str) -> int:
    return int(clock[:2]) * 60 + int(clock[3:])


def _invalid_reason(kind: str, item: dict) -> str | None:
    if kind != "time":
        return None
    start, end = item.get("start"), item.get("end")
    if start is None and end is None:
        return "no time given"
    if start is not None and end is not None and _minutes(end) < _minutes(start):
        return "the end is before the start"
    return None


def to_claims(reading: dict, doc_hash: str, lines: list[str]) -> tuple[dict, list[dict]]:
    """Turns a result into the document's header fields and its claims.

    Each quote is looked up in the source here, and each time is checked.
    """
    document = reading["document"]
    contacts = {contact["ref"]: contact for contact in reading["contacts"]}
    sections = []
    for section in reading["sections"]:
        section = dict(section)
        dates = []
        for entry in section["dates"]:
            line, status = quotes.locate(lines, entry["quote"], entry["line"])
            dates.append({**entry, "quote": quotes.clean(entry["quote"]), "line": line, "quote_status": status})
        section["dates"] = dates
        sections.append(section)

    # A claim about a contact that names none, in a document that refers to
    # exactly one contact, is taken to be about that contact.
    sole = next(iter(contacts)) if len(contacts) == 1 else None
    about_contacts = {"modality", "time", "attendance", "participant", "stated_minutes", "correction", "charge"}

    claims = []
    for name, kind in CLAIM_LISTS.items():
        for item in reading[name]:
            if kind in about_contacts and item.get("contact") is None and sole is not None:
                item = {**item, "contact": sole}
            about = item if kind == "contact" else contacts.get(item.get("contact")) or {}
            line, status = quotes.locate(lines, item["quote"], item["line"])
            reason = _invalid_reason(kind, item)
            skip = COMMON_FIELDS + (CONTACT_FIELDS if kind == "contact" else ())
            value = {field: content for field, content in item.items() if field not in skip}
            claims.append(
                {
                    "claim_id": f"{doc_hash[:12]}:{len(claims) + 1:03d}",
                    "section": item["section"],
                    "type": kind,
                    "contact_ref": item.get("ref") if kind == "contact" else item.get("contact"),
                    "encounter_id": about.get("encounter_id"),
                    "appointment_id": about.get("appointment_id"),
                    "service_date": about.get("service_date"),
                    "service_class": about.get("service_class"),
                    "service_as_written": about.get("service_as_written"),
                    "value": value,
                    "time_label": item.get("label") if kind == "time" else None,
                    "quote": quotes.clean(item["quote"]),
                    "line": line,
                    "quote_status": status,
                    "valid": reason is None,
                    "invalid_reason": reason,
                }
            )

    header = {
        "declared_id": document.get("declared_id"),
        "kinds": [section["kind"] for section in sections],
        "patient_key": patient_key(document),
        "patient_name": document.get("patient_name"),
        "patient_dob": document.get("patient_dob"),
        "patient_record_number": document.get("patient_record_number"),
        "sections": sections,
        "not_captured": coverage.check(lines, reading),
    }
    return header, claims
