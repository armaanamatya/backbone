"""Writes the saved abstraction in readable form. Calls no model."""

from __future__ import annotations

from . import export_conclusions, store


def _cell(value) -> str:
    if value is None or value == "":
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ")


def _table(headers: list[str], rows: list[list]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    lines += ["| " + " | ".join(_cell(value) for value in row) + " |" for row in rows]
    return lines


def _value(value: dict) -> str:
    parts = []
    for name, content in value.items():
        if content is None or content == [] or name == "ref":
            continue
        if isinstance(content, list):
            content = ", ".join(str(entry) for entry in content)
        parts.append(f"{name}: {content}")
    return "; ".join(parts)


def _contact(claim) -> str:
    parts = [claim["encounter_id"], claim["appointment_id"], claim["service_date"]]
    return " ".join(part for part in parts if part)


def documents_part(connection) -> list[str]:
    lines = ["## Documents", ""]
    rows = connection.execute(
        "SELECT d.*, (SELECT COUNT(*) FROM claims c WHERE c.doc_hash = d.doc_hash) AS claim_count"
        " FROM documents d ORDER BY COALESCE(d.declared_id, 'zz'), d.file_name"
    ).fetchall()
    table = []
    for row in rows:
        kinds = store.from_json(row["kinds"]) or []
        table.append(
            [
                row["declared_id"],
                row["file_name"],
                ", ".join(kinds),
                row["patient_key"],
                row["read_status"],
                row["claim_count"],
                row["doc_hash"][:12],
            ]
        )
    lines += _table(["ID", "File", "Kinds", "Patient", "Read", "Claims", "Hash"], table)
    not_read = [row for row in rows if row["read_status"] == "failed"]
    if not_read:
        lines += ["", "### Documents not read", ""]
        lines += _table(["File", "Reason"], [[row["file_name"], row["read_error"]] for row in not_read])
    return lines + [""]


def claims_part(connection) -> list[str]:
    lines = ["## What each document says", ""]
    documents = connection.execute(
        "SELECT * FROM documents WHERE read_status = 'read'"
        " ORDER BY COALESCE(declared_id, 'zz'), file_name"
    ).fetchall()
    for document in documents:
        title = document["declared_id"] or document["doc_hash"][:12]
        lines += [f"### {title}: {document['file_name']}", ""]
        lines += [
            f"- Patient: {document['patient_name']}, born {document['patient_dob']},"
            f" record number {document['patient_record_number']}",
            f"- Read by {document['model']}, effort {document['effort']},"
            f" prompt version {document['prompt_version']}",
            "",
        ]
        sections = store.from_json(document["sections"]) or []
        table = []
        for section in sections:
            signed = section["signature"]
            if signed == "signed":
                signed = f"signed by {section.get('signed_by')}, {section.get('signed_date')} {section.get('signed_time') or ''}".strip()
            original = ""
            if section.get("is_copy"):
                original = f"copy; original signed by {section.get('original_signed_by')}, {section.get('original_signed_date')} {section.get('original_signed_time') or ''}".strip()
            dates = "; ".join(
                f"{entry['kind']} {entry['date']} {entry.get('time') or ''}".strip() for entry in section["dates"]
            )
            table.append(
                [
                    section["id"],
                    f"{section['first_line']}-{section['last_line']}",
                    section["kind"],
                    section.get("kind_as_written"),
                    signed,
                    section.get("status_as_written"),
                    original,
                    dates,
                ]
            )
        lines += _table(["Section", "Lines", "Kind", "As written", "Signature", "Status", "Copy", "Dates"], table)
        lines.append("")
        claims = connection.execute(
            "SELECT * FROM claims WHERE doc_hash = ? ORDER BY claim_id", (document["doc_hash"],)
        ).fetchall()
        table = []
        for claim in claims:
            flags = []
            if claim["quote_status"] != "verified":
                flags.append(claim["quote_status"])
            if not claim["valid"]:
                flags.append(f"invalid: {claim['invalid_reason']}")
            table.append(
                [
                    claim["claim_id"].split(":")[1],
                    claim["section"],
                    claim["type"],
                    _contact(claim),
                    claim["service_class"],
                    _value(store.from_json(claim["value"])),
                    claim["line"],
                    f"\"{claim['quote']}\"",
                    ", ".join(flags),
                ]
            )
        lines += _table(["#", "Sec", "Type", "Contact", "Class", "Value", "Line", "Quote", "Flags"], table)
        lines.append("")
        coverage = store.from_json(document["not_captured"]) or {}
        counts = coverage.get("counts", {})
        lines.append(
            f"Coverage: {coverage.get('values', 0)} times, dates and record numbers in the document. "
            + ", ".join(f"{count} {status.replace('_', ' ')}" for status, count in counts.items())
            + "."
        )
        listed = coverage.get("listed", [])
        if listed:
            lines.append("")
            lines += _table(
                ["Line", "Kind", "Value", "Status"],
                [[row["line"], row["kind"], row["value"], row["status"].replace("_", " ")] for row in listed],
            )
        lines.append("")
    return lines


def write(connection, path) -> None:
    lines = [
        "# The saved abstraction",
        "",
        "Written by the `export` command from `abstraction.sqlite`. No model is called to write it.",
        "",
    ]
    lines += documents_part(connection)
    lines += export_conclusions.part(connection)
    lines += claims_part(connection)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
