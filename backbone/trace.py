"""Follows a figure back to the contacts, the claims and the source lines it rests on.

Calls no model. This is how a conclusion is inspected without the setup that
read the documents (R-9).
"""

from __future__ import annotations

from . import quotes, store


def _claims(connection, claim_ids) -> list[str]:
    lines = []
    for claim_id in claim_ids:
        row = connection.execute(
            "SELECT c.*, d.declared_id, d.file_name, d.text FROM claims c JOIN documents d USING (doc_hash)"
            " WHERE c.claim_id = ?",
            (claim_id,),
        ).fetchone()
        if row is None:
            lines.append(f"    {claim_id}: not in the store")
            continue
        text = quotes.split_lines(row["text"])
        found = row["quote"] in text[row["line"] - 1] if 1 <= (row["line"] or 0) <= len(text) else False
        value = store.from_json(row["value"])
        value = {k: v for k, v in value.items() if v not in (None, "", [])}
        lines.append(
            f"    {claim_id} [{row['type']}] {row['declared_id']} ({row['file_name']}) line {row['line']}"
            f"{'' if found else ' [QUOTE NOT AT THIS LINE]'}"
        )
        lines.append(f"        says: {value}")
        lines.append(f"        \"{row['quote']}\"")
    return lines


def _contact(connection, row) -> list[str]:
    lines = [
        f"Contact {row['contact_id']}: {row['encounter_id'] or ''} {row['service_date']} {row['service_class']},"
        f" status {row['status']}, patient present {row['patient_present']}"
        + (", attended in part" if row["partial"] else ""),
    ]
    for option in row["presence"]:
        choice = ", ".join(f"{k.split('/')[-1]} = {v}" for k, v in option["choices"].items())
        lines.append(
            f"  presence {option['start']}–{option['end']} less removed = {option['intervals']} = {option['minutes']} minutes"
            + (f"  [if {choice}]" if choice else "")
        )
        lines += _claims(connection, option.get("start_claims", []) + option.get("end_claims", []))
    for removed in row["removed"]:
        lines.append(f"  removed {removed['start']}–{removed['end']} ({removed['why']})")
        lines += _claims(connection, [removed["claim"]])
    if row["notes"]:
        lines.append(f"  notes: {'; '.join(row['notes'])}")
    conflicts = connection.execute("SELECT * FROM conflicts WHERE contact_id = ? ORDER BY conflict_id", (row["contact_id"],)).fetchall()
    for conflict in conflicts:
        lines += _conflict(connection, dict(conflict), indent="  ")
    lines.append(f"  all claims about this contact: {len(row['claims'])}")
    return lines


def _conflict(connection, row, indent="") -> list[str]:
    alternatives = store.from_json(row["alternatives"]) if isinstance(row["alternatives"], str) else row["alternatives"]
    lines = [f"{indent}Conflict {row['conflict_id']} on {row['field']}: {row['status']}, rule {row['rule']}" + (f", outcome {row['outcome']}" if row["outcome"] else "")]
    for alternative in alternatives:
        lines.append(f"{indent}  value {alternative['value']} from {', '.join(alternative.get('documents') or [])}" + (f" ({alternative['note']})" if alternative.get("note") else ""))
        lines += [indent + line for line in _claims(connection, alternative.get("claims", []))]
    if row.get("would_settle"):
        lines.append(f"{indent}  what would settle it: {row['would_settle']}")
    return lines


def follow(connection, what: str, value: str) -> str:
    lines = []
    if what == "contact":
        rows = [r for r in _all(connection, "contacts") if value in (r["encounter_id"], r["appointment_id"], r["contact_id"]) or r["contact_id"].endswith("/" + value)]
        if not rows:
            return f"No contact {value}."
        for row in rows:
            lines += _contact(connection, row)
    elif what == "week":
        rows = [r for r in _all(connection, "weekly_status") if r["week_start"] == value]
        if not rows:
            return f"No week starting {value}."
        for week in rows:
            lines.append(f"Week {week['week_start']} to {week['week_end']} for {week['patient_key']}: {week['verdict']}")
            for entry in week["minutes"]:
                choice = ", ".join(f"{k.split('/')[-1]} = {v}" for k, v in entry["choices"].items())
                lines.append(f"  minutes {entry['minutes']}" + (f" [if {choice}]" if choice else ""))
            lines.append(f"  days {', '.join(week['days'][0]['dates']) if week['days'] else 'none'}")
            for contact_id in week["contacts"]:
                row = next(r for r in _all(connection, "contacts") if r["contact_id"] == contact_id)
                lines += ["  " + line for line in _contact(connection, row)]
    elif what == "conflict":
        rows = [r for r in _all(connection, "conflicts") if r["conflict_id"] == value or r["conflict_id"].endswith("/" + value)]
        if not rows:
            return f"No conflict {value}."
        for row in rows:
            lines += _conflict(connection, row)
    elif what == "claim":
        lines += _claims(connection, [value])
    elif what == "assessment":
        rows = [r for r in _all(connection, "assessments") if r["completed_date"] == value or r["assessment_id"] == value]
        if not rows:
            return f"No assessment {value}."
        for row in rows:
            lines.append(f"Assessment {row['assessment_id']}: {row['instrument']} {row['score']} completed {row['completed_date']} {row['completed_time'] or ''}")
            lines.append("  completion:")
            lines += _claims(connection, row["claims"])
            if row["copies"]:
                lines.append("  copies, which add nothing:")
                lines += _claims(connection, row["copies"])
            if row["mentions"]:
                lines.append("  mentions, which add nothing:")
                lines += _claims(connection, row["mentions"])
    elif what == "finding":
        rows = [r for r in _all(connection, "findings") if r["finding_id"] == value or value in r["finding_id"]]
        if not rows:
            return f"No finding {value}."
        for row in rows:
            lines.append(f"Finding {row['finding_id']}: {row['detail']}")
            lines += _claims(connection, row["claims"])
    return "\n".join(lines)


def _all(connection, table) -> list[dict]:
    return [row for patient in store.patients(connection) for row in store.rows_of(connection, table, patient)]
