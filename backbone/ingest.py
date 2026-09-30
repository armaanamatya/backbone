"""Reads files as UTF-8, hashes them, skips duplicates, and has new documents read
(pieces 1 and 2 of the build list).

A file is known by the hash of its bytes. A file whose hash is already in the
store changes nothing and calls no model, whatever its name.
"""

from __future__ import annotations

import hashlib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import counting, quotes, reader, reconcile, store
from .logs import now


def hash_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def files_in(folder: Path) -> list[Path]:
    if folder.is_file():
        return [folder]
    return sorted(path for path in folder.iterdir() if path.is_file())


def register(connection, folder: Path, log) -> dict:
    """Adds files the store has not seen. Returns what happened to each file."""
    known = store.known_hashes(connection)
    outcome = {"new": [], "duplicate": [], "unreadable": []}
    for path in files_in(folder):
        data = path.read_bytes()
        doc_hash = hash_bytes(data)
        if doc_hash in known:
            outcome["duplicate"].append(path.name)
            log.event("file_skipped", file=path.name, doc_hash=doc_hash, reason="content already in the store")
            continue
        known.add(doc_hash)
        # Always UTF-8. The default on Windows would garble the dashes in times.
        try:
            text, problem = data.decode("utf-8"), None
        except UnicodeDecodeError as error:
            text, problem = data.decode("utf-8", errors="replace"), f"not UTF-8: {error}"
        text = text.removeprefix("﻿")
        store.register_document(
            connection,
            doc_hash=doc_hash,
            file_name=path.name,
            byte_size=len(data),
            line_count=len(quotes.split_lines(text)),
            text=text,
            registered_at=now(),
        )
        if problem:
            store.mark_failed(
                connection, doc_hash, problem, model=None, effort=None, prompt_version=None, read_at=now()
            )
            outcome["unreadable"].append(path.name)
            log.event("file_unreadable", file=path.name, doc_hash=doc_hash, reason=problem)
        else:
            outcome["new"].append(path.name)
            log.event("file_registered", file=path.name, doc_hash=doc_hash, bytes=len(data))
    connection.commit()
    return outcome


def waiting(connection, settings, only: list[str] | None = None) -> list:
    """Documents with no reading under the current model, effort and prompt version."""
    rows = connection.execute(
        "SELECT doc_hash, file_name, text, read_status, read_error, model, effort, prompt_version"
        " FROM documents ORDER BY file_name"
    ).fetchall()
    chosen = []
    for row in rows:
        if row["read_status"] == "failed" and row["model"] is None:
            continue  # The file itself could not be decoded. A model cannot help.
        current = (
            row["read_status"] == "read"
            and row["model"] == settings.model
            and row["effort"] == settings.effort
            and row["prompt_version"] == settings.prompt_version
        )
        if current:
            continue
        if only and not any(part.lower() in row["file_name"].lower() for part in only):
            continue
        chosen.append(row)
    return chosen


def read_waiting(connection, settings, log, only: list[str] | None = None) -> list[dict]:
    """Has each waiting document read, several at a time, and saves the claims."""
    rows = waiting(connection, settings, only)
    if not rows:
        return []

    def read(row):
        return reader.read_document(
            settings, log, doc_hash=row["doc_hash"], file_name=row["file_name"], text=row["text"]
        )

    # The prompt and the schema are the same in every call, and the service keeps
    # them ready once one call has sent them. So the first document that needs a
    # call is read alone, and the rest follow several at a time.
    records = {}
    fresh = [row for row in rows if not reader.saved_path(settings, row["doc_hash"]).exists()]
    if len(fresh) > 1:
        records[fresh[0]["doc_hash"]] = read(fresh[0])
    remaining = [row for row in rows if row["doc_hash"] not in records]
    with ThreadPoolExecutor(max_workers=max(1, settings.parallel_calls)) as pool:
        for row, record in zip(remaining, pool.map(read, remaining)):
            records[row["doc_hash"]] = record
    records = [records[row["doc_hash"]] for row in rows]

    stamp = {"model": settings.model, "effort": settings.effort, "prompt_version": settings.prompt_version}
    patients = set()
    summaries = []
    for row, record in zip(rows, records):
        if record["status"] != "read":
            errors = record["attempts"][-1]["errors"] if record["attempts"] else ["no attempt was made"]
            store.mark_failed(connection, row["doc_hash"], "; ".join(errors[:5]), read_at=now(), **stamp)
            log.event("document_not_read", file=row["file_name"], doc_hash=row["doc_hash"], errors=errors[:10])
            summaries.append({"file": row["file_name"], "status": "failed", "errors": errors})
            continue
        header, claims = reader.to_claims(record["reading"], row["doc_hash"], quotes.split_lines(row["text"]))
        store.save_reading(connection, row["doc_hash"], header, claims, read_at=record["read_at"], **stamp)
        patients.add(header["patient_key"])
        unverified = sum(1 for claim in claims if claim["quote_status"] == quotes.UNVERIFIED)
        invalid = sum(1 for claim in claims if not claim["valid"])
        summary = {
            "file": row["file_name"],
            "status": "read",
            "reused": record["reused"],
            "declared_id": header["declared_id"],
            "claims": len(claims),
            "unverified_quotes": unverified,
            "invalid_claims": invalid,
            "coverage": header["not_captured"]["counts"],
            "attempts": len(record["attempts"]),
            "usage": [attempt.get("usage") for attempt in record["attempts"]],
        }
        log.event("document_read", doc_hash=row["doc_hash"], **{k: v for k, v in summary.items() if k != "usage"})
        summaries.append(summary)
    for patient_key in sorted(patients):
        conclude(connection, patient_key, log)
    connection.commit()
    return summaries


def conclude(connection, patient_key: str, log) -> dict:
    """Rebuilds the conclusions for one patient, from all of that patient's
    claims. Nothing is carried over from the last build, so the order in which
    documents arrived cannot change the result."""
    claims, sections = store.load_claims(connection, patient_key)
    rows = reconcile.conclude(patient_key, claims, sections)
    rows["weekly_status"] = counting.weekly_status(rows["contacts"], rows["plan_rules"], sections)
    store.replace_conclusions(connection, patient_key, rows)
    sizes = {table: len(found) for table, found in rows.items()}
    log.event("conclusions_rebuilt", patient=patient_key, claims=len(claims), **sizes)
    return sizes
