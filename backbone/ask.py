"""Answers a question (piece 7 of the build list, R-47, R-48).

One model call returns a plan of up to five function calls. Code runs the
plan, and code writes the nine-part answer from the results. The plan is
saved under the question, so a repeated question calls no model.

The nine parts (R-32):

    1  the question as understood        6  what is not settled
    2  the answer                         7  assumptions
    3  figures and how they were worked out   8  documents not read
    4  what contributed, with sources     9  version
    5  what was excluded, and why
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone

from . import functions, reader, store, writing
from .logs import now
from .reading_schema import SECTION_KINDS, validate

PLAN_PROMPT = "plan.md"
MAX_CALLS = 5

DATE = {"type": ["string", "null"], "pattern": r"^\d{4}-\d{2}-\d{2}$"}
PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "patient_named": {"type": ["string", "null"]},
        "period": {
            "type": "object",
            "properties": {
                "start": DATE,
                "end": DATE,
                "basis": {"enum": ["as asked", "the episode", "last week of the episode", "not stated"]},
            },
            "required": ["start", "end", "basis"],
            "additionalProperties": False,
        },
        "reading": {"type": "string"},
        "other_readings": {"type": "array", "items": {"type": "string"}},
        "calls": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "function": {"enum": list(functions.CATALOGUE)},
                    "arguments": {
                        "type": "object",
                        "properties": {
                            "patient": {"type": ["string", "null"]},
                            "start": DATE,
                            "end": DATE,
                            "date": DATE,
                            "on": DATE,
                            "group_by": {"enum": ["week", "class", "day", "clinician", None]},
                            "instrument": {"type": ["string", "null"]},
                            "topic": {"type": ["string", "null"]},
                            "speaker": {"type": ["string", "null"]},
                            "weeks": {"type": ["integer", "null"]},
                            "first_start": DATE,
                            "first_end": DATE,
                            "second_start": DATE,
                            "second_end": DATE,
                        },
                        "additionalProperties": False,
                    },
                },
                "required": ["function", "arguments"],
                "additionalProperties": False,
            },
        },
        "no_function_fits": {"type": "boolean"},
        "document_kind": {"enum": SECTION_KINDS + [None]},
        "notes": {"type": ["string", "null"]},
    },
    "required": ["patient_named", "period", "reading", "other_readings", "calls", "no_function_fits", "document_kind", "notes"],
    "additionalProperties": False,
}



class Model:
    """The plan call, with its saved results."""

    def __init__(self, settings, log):
        self.settings = settings
        self.log = log

    def saved_path(self, question: str):
        digest = hashlib.sha256(" ".join(question.split()).encode("utf-8")).hexdigest()[:16]
        model = re.sub(r"[^A-Za-z0-9.-]+", "-", self.settings.model)
        return self.settings.answers / "plans" / f"{digest}__{model}__plan-v{self.settings.plan_prompt_version}.json"

    def plan(self, connection, question: str) -> dict:
        path = self.saved_path(question)
        if path.exists():
            record = json.loads(path.read_text(encoding="utf-8"))
            self.log.event("plan_reused", question=question, saved=path.name)
            return {**record, "reused": True}
        message = build_message(connection, question)
        attempts, plan, feedback = [], None, None
        for attempt in (1, 2):
            entry = {"attempt": attempt, "started_at": now()}
            try:
                text = message if not feedback else message + "\n\nYour previous plan was rejected:\n" + "\n".join(f"- {e}" for e in feedback) + "\n\nReturn a corrected plan."
                envelope = reader.call_model(self.settings, text, PLAN_PROMPT, PLAN_SCHEMA)
                entry["usage"] = reader.usage_of(envelope)
                candidate = reader.result_of(envelope)
                errors = validate(candidate, PLAN_SCHEMA)
                if not errors and len(candidate["calls"]) > MAX_CALLS:
                    errors = [f"result.calls: at most {MAX_CALLS} calls"]
            except reader.ModelCallError as error:
                candidate, errors = None, [str(error)]
            entry["errors"] = errors
            attempts.append(entry)
            self.log.event(
                "model_call", purpose="plan", question=question, model=self.settings.model, effort=self.settings.effort,
                plan_prompt_version=self.settings.plan_prompt_version, attempt=attempt, accepted=not errors, errors=errors[:10],
                **entry.get("usage", {}),
            )
            if not errors:
                plan = candidate
                break
            feedback = errors if candidate is not None else None
        record = {
            "question": question,
            "model": self.settings.model,
            "effort": self.settings.effort,
            "plan_prompt_version": self.settings.plan_prompt_version,
            "made_at": now(),
            "attempts": attempts,
            "plan": plan,
        }
        if plan is not None:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
        return {**record, "reused": False}


def build_message(connection, question: str) -> str:
    patients = functions.patients_in(connection)
    listed = "\n".join(
        f"- {p['patient']}: {p['name'] or 'name not printed'}; plan period "
        + (", ".join(f"{e['start']} to {e['end']}" for e in p["episodes"]) or "none")
        for p in patients
    ) or "- none"
    catalogue = "\n".join(
        f"- {name}: {entry['answers']} Arguments: " + ", ".join(f"{k} ({v})" for k, v in entry["arguments"].items())
        for name, entry in functions.CATALOGUE.items()
    )
    kinds = ", ".join(SECTION_KINDS)
    return (
        f"<question>\n{question}\n</question>\n\n<patients>\n{listed}\n</patients>\n\n"
        f"<functions>\n{catalogue}\n</functions>\n\nDocument kinds: {kinds}.\n\nReturn the plan."
    )


# --------------------------------------------------------------------------
# Running the plan
# --------------------------------------------------------------------------


def answer(connection, settings, log, question: str, question_id: str | None = None) -> dict:
    """The whole path: plan, run, write."""
    model = Model(settings, log)
    record = model.plan(connection, question)
    plan = record["plan"]
    built = {
        "question_id": question_id,
        "question": question,
        "plan": plan,
        "plan_source": "saved" if record["reused"] else "new",
        "plan_attempts": len(record.get("attempts", [])),
        "results": [],
        "parts": {},
    }
    if plan is None:
        built["parts"] = _parts_for_failure(record)
        built["text"] = writing.render(built)
        return built

    who = functions.resolve_patient(connection, plan["patient_named"])
    everyone = functions.patients_in(connection)
    if who["status"] == "none_named" and len(everyone) == 1:
        who = {"status": "found", **everyone[0], "assumed": True}
    built["patient"] = who

    if who["status"] in ("not_found", "several", "participant"):
        built["parts"] = _parts_for_patient(who, plan)
    elif plan["no_function_fits"]:
        built["parts"], built["lookup"] = _parts_for_no_function(connection, who, plan)
    else:
        for call in plan["calls"][:MAX_CALLS]:
            arguments = dict(call["arguments"])
            if who["status"] == "found":
                arguments["patient"] = who["patient"]
            elif "patient" in arguments:
                arguments.pop("patient")
            try:
                result = functions.call(connection, call["function"], arguments)
            except TypeError as error:
                result = {"function": call["function"], "arguments": arguments, "error": f"the call could not be run: {error}", "sources": [], "conflicts": [], "not_read": [], "calculation": []}
            built["results"].append(result)
        not_read = {}
        for result in built["results"]:
            for row in result.get("not_read", []):
                not_read[row["file"]] = row
        built["parts"] = writing.parts_from_results(_understood(who, plan), plan, built["results"], _not_read_lines(list(not_read.values())))
    built["parts"].setdefault("in short", [built["parts"]["2. the answer"][0]])
    built["parts"]["9. version"] = _version(connection, settings, record)
    built["text"] = writing.render(built)
    log.event("question_answered", question=question, question_id=question_id, plan_source=built["plan_source"], calls=len(built["results"]))
    return built


def _version(connection, settings, record) -> list[str]:
    read = connection.execute("SELECT MAX(read_at), COUNT(*) FROM documents WHERE read_status = 'read'").fetchone()
    return [
        f"Abstraction: {settings.store.name}, {read[1]} documents read, last read at {read[0]}.",
        f"Reading: model {settings.model}, effort {settings.effort}, prompt version {settings.prompt_version}.",
        f"Plan: model {record['model']}, plan prompt version {record['plan_prompt_version']}, made {record['made_at']}"
        + (" (saved plan reused)" if record.get("reused") else "") + ".",
        f"Answered: {datetime.now(timezone.utc).isoformat(timespec='seconds')}.",
    ]


def _parts_for_failure(record) -> dict:
    errors = [e for attempt in record["attempts"] for e in attempt["errors"]]
    return {
        "1. the question as understood": ["The plan call failed, so the question was not understood."],
        "2. the answer": ["No answer. The model did not return a plan that fits the schema."] + [f"- {e}" for e in errors[:5]],
        "3. figures": ["None."], "4. what contributed": ["Nothing."], "5. what was excluded": ["Nothing."],
        "6. not settled": ["Nothing."], "7. assumptions": ["None."], "8. documents not read": ["Not checked."],
    }


def _understood(who, plan) -> list[str]:
    lines = []
    if who["status"] == "found":
        lines.append(f"Patient: {who.get('name') or who['patient']} ({who['patient']})" + (", the only patient in the collection; the question names none." if who.get("assumed") else "."))
    elif who["status"] == "none_named":
        lines.append("Patient: none named.")
    else:
        lines.append(f"Patient as asked: {who.get('name')}.")
    period = plan["period"]
    if period["basis"] != "not stated" and period["start"] and period["end"]:
        lines.append(f"Period: {period['start']} to {period['end']} ({period['basis']}).")
    elif period["basis"] != "not stated":
        lines.append(f"Period: {period['basis']}, with no dates given.")
    lines.append(f"Reading: {plan['reading']}")
    for other in plan["other_readings"]:
        lines.append(f"Another reading: {other}")
    if plan.get("notes"):
        lines.append(f"Note: {plan['notes']}")
    return lines


def _parts_for_patient(who, plan) -> dict:
    parts = {"1. the question as understood": _understood(who, plan)}
    if who["status"] == "not_found":
        parts["2. the answer"] = [f"No patient named {who['name']} is in the collection. No figures are given for any other patient."]
    elif who["status"] == "several":
        names = "; ".join(f"{c['patient']}, {c['name']}" for c in who["candidates"])
        parts["2. the answer"] = [f"The name matches more than one patient: {names}. Say which one."]
    else:
        seen = ", ".join(f"{writing.day(a['date'])} ({a['class'].replace('_', ' ')}, as {a['role'].replace('_', ' ')})" for a in who["appearances"])
        parts["2. the answer"] = [
            f"{who['name']} appears in the record as a participant, not as a patient, and has no record of their own here.",
            f"They took part in contacts on: {seen}.",
        ]
    for name in ("3. figures", "4. what contributed", "5. what was excluded", "6. not settled"):
        parts[name] = ["Nothing." if name != "3. figures" else "None."]
    parts["7. assumptions"] = ["A patient is matched by name or record number as written. No near match is used."]
    parts["8. documents not read"] = ["Not checked, because no figure was worked out."]
    return parts


def _parts_for_no_function(connection, who, plan) -> dict:
    parts = {"1. the question as understood": _understood(who, plan)}
    kind = plan.get("document_kind")
    lines = ["Cannot answer. No function reads what the question asks for, so the abstraction holds no figure for it."]
    listed = []
    lookup = []  # What was looked up, for the check that every number in an answer has a source.
    if who["status"] == "found":
        period = plan["period"]
        if period["basis"] == "as asked" and period["start"] == period["end"] and period["start"]:
            rows = connection.execute(
                "SELECT c.quote, c.line, d.declared_id, d.file_name FROM claims c JOIN documents d USING (doc_hash)"
                " WHERE c.patient_key = ? AND c.service_date = ? ORDER BY d.declared_id, c.line, c.claim_id",
                (who["patient"], period["start"]),
            ).fetchall()
            lookup = [dict(r) for r in rows]
            listed = [f"- {r['declared_id'] or r['file_name']} line {r['line']}: \"{r['quote']}\"" for r in rows]
            lines.append(f"The stored passages for that patient and date, {period['start']}:" if listed else "No stored passage is dated that day.")
        elif kind:
            rows = connection.execute(
                "SELECT declared_id, file_name, kinds FROM documents WHERE patient_key = ? AND read_status = 'read' ORDER BY declared_id",
                (who["patient"],),
            ).fetchall()
            found = [r for r in rows if kind in (store.from_json(r["kinds"]) or [])]
            lookup = [dict(r) for r in found]
            listed = [f"- {r['declared_id'] or r['file_name']}: {r['file_name']}" for r in found]
            lines.append(f"Documents of the kind the question is about ({kind.replace('_', ' ')}), for this patient:" if listed else f"No document of that kind ({kind.replace('_', ' ')}) is in the record for this patient.")
    parts["2. the answer"] = lines + listed
    parts["3. figures"] = ["None. No figure is given."]
    parts["4. what contributed"] = ["Nothing. The documents above are named, not read."]
    parts["5. what was excluded"] = ["Nothing."]
    parts["6. not settled"] = ["Nothing."]
    parts["7. assumptions"] = ["None."]
    parts["8. documents not read"] = _not_read_lines(functions.not_read(connection, who["patient"]) if who["status"] == "found" else [])
    return parts, lookup


def _not_read_lines(rows) -> list[str]:
    if not rows:
        return ["None."]
    return [f"- {r['file']}: {r['reason']}. Any figure it would affect is not in this answer." for r in rows]
