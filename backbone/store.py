"""Creates and writes the saved abstraction: two layers, eight tables (R-20).

"Says" holds what each document states: documents and claims.
"Concludes" holds what code works out from the claims: contacts, conflicts,
findings, plan_rules, assessments and weekly_status.

Every row carries the patient, so a question about one patient never reads
another patient's rows.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path

SAYS_TABLES = ("documents", "claims")
CONCLUDES_TABLES = (
    "contacts",
    "conflicts",
    "findings",
    "plan_rules",
    "assessments",
    "weekly_status",
)
TABLES = SAYS_TABLES + CONCLUDES_TABLES

# Raised when a table changes shape. An older store is then emptied of claims
# and conclusions, and the next `ingest` fills it again from the saved results.
SCHEMA_VERSION = 3

# Columns that record when something was done. They are left out when two
# stores are compared, because they differ between runs by design.
VOLATILE_COLUMNS = {"registered_at", "read_at"}

SCHEMA = """
CREATE TABLE IF NOT EXISTS documents (
    doc_hash              TEXT PRIMARY KEY,
    file_name             TEXT NOT NULL,
    byte_size             INTEGER NOT NULL,
    line_count            INTEGER NOT NULL,
    text                  TEXT NOT NULL,
    declared_id           TEXT,
    kinds                 TEXT,
    patient_key           TEXT,
    patient_name          TEXT,
    patient_dob           TEXT,
    patient_record_number TEXT,
    sections              TEXT,
    read_status           TEXT NOT NULL DEFAULT 'pending',
    read_error            TEXT,
    not_captured          TEXT,
    model                 TEXT,
    effort                TEXT,
    prompt_version        INTEGER,
    registered_at         TEXT NOT NULL,
    read_at               TEXT
);
DROP INDEX IF EXISTS documents_by_patient;
DROP INDEX IF EXISTS documents_by_status;
CREATE INDEX IF NOT EXISTS documents_by_patient_and_status ON documents(patient_key, read_status);
CREATE INDEX IF NOT EXISTS documents_by_status_and_patient ON documents(read_status, patient_key);

CREATE TABLE IF NOT EXISTS claims (
    claim_id           TEXT PRIMARY KEY,
    doc_hash           TEXT NOT NULL REFERENCES documents(doc_hash),
    section            INTEGER,
    patient_key        TEXT NOT NULL,
    type               TEXT NOT NULL,
    contact_ref        TEXT,
    encounter_id       TEXT,
    appointment_id     TEXT,
    service_date       TEXT,
    service_class      TEXT,
    service_as_written TEXT,
    value              TEXT NOT NULL,
    time_label         TEXT,
    quote              TEXT,
    line               INTEGER,
    quote_status       TEXT NOT NULL,
    valid              INTEGER NOT NULL DEFAULT 1,
    invalid_reason     TEXT,
    model              TEXT,
    effort             TEXT,
    prompt_version     INTEGER
);
CREATE INDEX IF NOT EXISTS claims_by_patient ON claims(patient_key, type);
CREATE INDEX IF NOT EXISTS claims_by_document ON claims(doc_hash);

CREATE TABLE IF NOT EXISTS contacts (
    contact_id             TEXT PRIMARY KEY,
    patient_key            TEXT NOT NULL,
    record_kind            TEXT NOT NULL,
    encounter_id           TEXT,
    appointment_id         TEXT,
    service_date           TEXT,
    service_class          TEXT,
    service_as_written     TEXT,
    status                 TEXT NOT NULL,
    patient_present        TEXT NOT NULL,
    partial                INTEGER NOT NULL DEFAULT 0,
    modality               TEXT,
    clinicians             TEXT,
    participants           TEXT,
    session                TEXT,
    presence               TEXT,
    removed                TEXT,
    minutes                TEXT,
    minutes_without_patient INTEGER,
    notes                  TEXT,
    documents              TEXT,
    claims                 TEXT
);
CREATE INDEX IF NOT EXISTS contacts_by_patient ON contacts(patient_key, service_date);

CREATE TABLE IF NOT EXISTS conflicts (
    conflict_id  TEXT PRIMARY KEY,
    patient_key  TEXT NOT NULL,
    contact_id   TEXT,
    field        TEXT NOT NULL,
    alternatives TEXT NOT NULL,
    status       TEXT NOT NULL,
    rule         TEXT,
    outcome      TEXT,
    would_settle TEXT
);
CREATE INDEX IF NOT EXISTS conflicts_by_patient ON conflicts(patient_key);

CREATE TABLE IF NOT EXISTS findings (
    finding_id  TEXT PRIMARY KEY,
    patient_key TEXT NOT NULL,
    kind        TEXT NOT NULL,
    contact_id  TEXT,
    detail      TEXT,
    claims      TEXT
);
CREATE INDEX IF NOT EXISTS findings_by_patient ON findings(patient_key);

CREATE TABLE IF NOT EXISTS plan_rules (
    rule_id        TEXT PRIMARY KEY,
    patient_key    TEXT NOT NULL,
    doc_hash       TEXT NOT NULL,
    rule           TEXT NOT NULL,
    value          TEXT NOT NULL,
    effective_from TEXT,
    effective_to   TEXT,
    claim_id       TEXT
);
CREATE INDEX IF NOT EXISTS plan_rules_by_patient ON plan_rules(patient_key);

CREATE TABLE IF NOT EXISTS assessments (
    assessment_id  TEXT PRIMARY KEY,
    patient_key    TEXT NOT NULL,
    instrument     TEXT NOT NULL,
    score          TEXT,
    completed_date TEXT,
    completed_time TEXT,
    form_id        TEXT,
    items          TEXT,
    claims         TEXT,
    copies         TEXT,
    mentions       TEXT
);
CREATE INDEX IF NOT EXISTS assessments_by_patient ON assessments(patient_key);

CREATE TABLE IF NOT EXISTS weekly_status (
    patient_key  TEXT NOT NULL,
    week_start   TEXT NOT NULL,
    week_end     TEXT NOT NULL,
    requirement  TEXT NOT NULL,
    days         TEXT NOT NULL,
    minutes      TEXT NOT NULL,
    verdict      TEXT NOT NULL,
    margin       TEXT,
    partial      INTEGER NOT NULL DEFAULT 0,
    conflicts    TEXT,
    contacts     TEXT,
    undocumented TEXT,
    PRIMARY KEY (patient_key, week_start)
);
"""


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    version = connection.execute("PRAGMA user_version").fetchone()[0]
    has_tables = connection.execute("SELECT COUNT(*) FROM sqlite_master WHERE type = 'table'").fetchone()[0]
    if has_tables and version != SCHEMA_VERSION:
        for table in CONCLUDES_TABLES + ("claims",):
            connection.execute(f"DROP TABLE IF EXISTS {table}")
        connection.execute("UPDATE documents SET read_status = 'pending' WHERE read_status = 'read'")
    connection.executescript(SCHEMA)
    connection.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
    connection.commit()
    return connection


def to_json(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def from_json(text):
    return None if text is None else json.loads(text)


def known_hashes(connection: sqlite3.Connection) -> set[str]:
    return {row["doc_hash"] for row in connection.execute("SELECT doc_hash FROM documents")}


def patients(connection: sqlite3.Connection) -> list[str]:
    rows = connection.execute(
        "SELECT DISTINCT patient_key FROM documents WHERE patient_key IS NOT NULL ORDER BY patient_key"
    )
    return [row["patient_key"] for row in rows]


def register_document(connection, *, doc_hash, file_name, byte_size, line_count, text, registered_at):
    connection.execute(
        "INSERT INTO documents (doc_hash, file_name, byte_size, line_count, text, registered_at)"
        " VALUES (?, ?, ?, ?, ?, ?)",
        (doc_hash, file_name, byte_size, line_count, text, registered_at),
    )


def mark_failed(connection, doc_hash, error, *, model, effort, prompt_version, read_at):
    connection.execute("DELETE FROM claims WHERE doc_hash = ?", (doc_hash,))
    connection.execute(
        "UPDATE documents SET read_status = 'failed', read_error = ?, model = ?, effort = ?,"
        " prompt_version = ?, read_at = ? WHERE doc_hash = ?",
        (error, model, effort, prompt_version, read_at, doc_hash),
    )


def save_reading(connection, doc_hash, header, claims, *, model, effort, prompt_version, read_at):
    """Replaces what the store holds for one document with a new reading."""
    connection.execute("DELETE FROM claims WHERE doc_hash = ?", (doc_hash,))
    connection.execute(
        "UPDATE documents SET declared_id = ?, kinds = ?, patient_key = ?, patient_name = ?,"
        " patient_dob = ?, patient_record_number = ?, sections = ?, not_captured = ?,"
        " read_status = 'read', read_error = NULL, model = ?, effort = ?, prompt_version = ?,"
        " read_at = ? WHERE doc_hash = ?",
        (
            header["declared_id"],
            to_json(header["kinds"]),
            header["patient_key"],
            header["patient_name"],
            header["patient_dob"],
            header["patient_record_number"],
            to_json(header["sections"]),
            to_json(header["not_captured"]),
            model,
            effort,
            prompt_version,
            read_at,
            doc_hash,
        ),
    )
    connection.executemany(
        "INSERT INTO claims (claim_id, doc_hash, section, patient_key, type, contact_ref, encounter_id,"
        " appointment_id, service_date, service_class, service_as_written, value, time_label,"
        " quote, line, quote_status, valid, invalid_reason, model, effort, prompt_version)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                claim["claim_id"],
                doc_hash,
                claim["section"],
                header["patient_key"],
                claim["type"],
                claim["contact_ref"],
                claim["encounter_id"],
                claim["appointment_id"],
                claim["service_date"],
                claim["service_class"],
                claim["service_as_written"],
                to_json(claim["value"]),
                claim["time_label"],
                claim["quote"],
                claim["line"],
                claim["quote_status"],
                1 if claim["valid"] else 0,
                claim["invalid_reason"],
                model,
                effort,
                prompt_version,
            )
            for claim in claims
        ],
    )


def load_claims(connection, patient_key: str) -> tuple[list[dict], dict]:
    """The claims of one patient, and the sections they came from.

    Only valid claims whose quote was found in the source are returned. The
    others stay in the store, and are not used in any conclusion.
    """
    sections = {}
    documents = {}
    for row in connection.execute(
        "SELECT doc_hash, declared_id, file_name, sections FROM documents"
        " WHERE patient_key = ? AND read_status = 'read'",
        (patient_key,),
    ):
        documents[row["doc_hash"]] = row["declared_id"] or row["doc_hash"][:12]
        for section in from_json(row["sections"]) or []:
            sections[(row["doc_hash"], section["id"])] = section
    claims = []
    for row in connection.execute(
        "SELECT * FROM claims WHERE patient_key = ? AND valid = 1 AND quote_status != 'unverified'"
        " ORDER BY claim_id",
        (patient_key,),
    ):
        claim = dict(row)
        claim["value"] = from_json(claim["value"])
        claim["document"] = documents.get(claim["doc_hash"], claim["doc_hash"][:12])
        claims.append(claim)
    return claims, sections


def replace_conclusions(connection, patient_key: str, rows: dict[str, list[dict]]) -> None:
    """Rebuilds the conclusions for one patient from scratch, so the order in
    which documents arrived cannot change them."""
    for table in CONCLUDES_TABLES:
        connection.execute(f"DELETE FROM {table} WHERE patient_key = ?", (patient_key,))
        for row in rows.get(table, []):
            row = {**row, "patient_key": patient_key}
            names = list(row)
            values = [
                to_json(value) if isinstance(value, (dict, list)) else (int(value) if isinstance(value, bool) else value)
                for value in row.values()
            ]
            connection.execute(
                f"INSERT INTO {table} ({', '.join(names)}) VALUES ({', '.join('?' * len(names))})",
                values,
            )


def rows_of(connection, table: str, patient_key: str, order: str = "") -> list[dict]:
    """The rows of one conclusions table for one patient, with their JSON opened."""
    query = f"SELECT * FROM {table} WHERE patient_key = ?" + (f" ORDER BY {order}" if order else "")
    result = []
    for row in connection.execute(query, (patient_key,)):
        opened = {}
        for name, value in dict(row).items():
            if isinstance(value, str) and value[:1] in "[{":
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    pass
            opened[name] = value
        result.append(opened)
    return result


def dump(connection: sqlite3.Connection, tables=TABLES) -> dict:
    """The content of the store in a fixed order, for comparing two stores."""
    result = {}
    for table in tables:
        columns = [
            row["name"]
            for row in connection.execute(f"PRAGMA table_info({table})")
            if row["name"] not in VOLATILE_COLUMNS
        ]
        rows = connection.execute(f"SELECT {', '.join(columns)} FROM {table}").fetchall()
        result[table] = sorted((tuple(row) for row in rows), key=repr)
    return result
