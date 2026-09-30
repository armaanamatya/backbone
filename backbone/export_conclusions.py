"""The part of the readable export that shows what the record establishes."""

from __future__ import annotations

from . import counting, store


def cell(value) -> str:
    if value is None or value == "":
        return ""
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers: list[str], rows: list[list]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    lines += ["| " + " | ".join(cell(value) for value in row) + " |" for row in rows]
    return lines


def either(values) -> str:
    """Alternatives, written as "40 or 50"."""
    seen = []
    for value in values:
        if value not in seen:
            seen.append(value)
    return " or ".join(str(value) for value in seen) if seen else ""


def words(text) -> str:
    return (text or "").replace("_", " ")


def margin_of(entry: dict) -> str:
    parts = [
        f"{abs(entry[name]):g} {name if abs(entry[name]) != 1 else name[:-1]} {'short' if entry[name] < 0 else 'over'}"
        for name in ("days", "minutes", "sessions")
        if name in entry and entry[name] != 0
    ]
    return ", ".join(parts) or "exactly met"


def plan_part(plans: list[dict]) -> list[str]:
    lines = ["#### Plan", ""]
    if not plans:
        return lines + ["No plan is in the record.", ""]
    for plan in plans:
        needs = ", ".join(
            f"at least {entry['minimum']:g} {words(entry['measure'])} each {entry['period']}"
            for entry in plan["requirements"]
        )
        lines += table(
            ["Value", "Read from the plan"],
            [
                ["Document", plan["document"]],
                ["Signed", plan["signed"]],
                ["In effect", f"{plan['start']} to {plan['end']}"],
                ["Required", needs],
                ["Week starts on", plan["week_starts_on"]],
                ["Counted classes", ", ".join(words(name) for name in sorted(plan["counted_classes"]))],
                ["Excluded classes", ", ".join(words(name) for name in sorted(plan["excluded_classes"]))],
            ],
        )
        lines.append("")
    return lines


def encounters_part(contacts: list[dict], plans: list[dict]) -> list[str]:
    rows = []
    for contact in contacts:
        if contact["record_kind"] != "encounter":
            continue
        plan = counting.plan_for(plans, contact["service_date"]) if contact["service_date"] else None
        counted, why = counting.counts(contact, plan)
        minutes = either(entry["minutes"] for entry in contact["minutes"])
        if contact["minutes_without_patient"]:
            minutes = (minutes + "; " if minutes else "") + f"{contact['minutes_without_patient']} without the patient"
        rows.append(
            [
                contact["encounter_id"] or contact["appointment_id"],
                contact["service_date"],
                words(contact["service_class"]),
                words(contact["status"]) + (", in part" if contact["partial"] else ""),
                either(f"{entry['start']}–{entry['end']}" for entry in contact["presence"] if entry["start"]),
                ", ".join(sorted({f"{row['start']}–{row['end']}" for row in contact["removed"]})),
                minutes,
                "yes" if counted else f"no: {why}",
                ", ".join(contact["documents"]),
                "; ".join(contact["notes"]),
            ]
        )
    headers = ["Encounter", "Date", "Class", "Status", "Present", "Removed", "Minutes", "Counts", "Documents", "Notes"]
    return ["#### Encounters", ""] + table(headers, rows) + [""]


def administrative_part(contacts: list[dict]) -> list[str]:
    kept = [contact for contact in contacts if contact["record_kind"] != "encounter"]
    if not kept:
        return []
    rows = [
        [c["service_date"], words(c["service_class"]), c["service_as_written"], c["modality"], ", ".join(c["documents"])]
        for c in kept
    ]
    lines = ["#### Administrative records", "", "Kept, and not counted as encounters.", ""]
    return lines + table(["Date", "Class", "As written", "How", "Documents"], rows) + [""]


def conflicts_part(conflicts: list[dict]) -> list[str]:
    rows = []
    for conflict in conflicts:
        values = "; ".join(
            f"{entry['value']} ({', '.join(entry.get('documents') or []) or 'no document'})"
            for entry in conflict["alternatives"]
        )
        outcome = f"settled: {conflict['outcome']}" if conflict["status"] == "settled" else "open"
        rows.append(
            [conflict["conflict_id"], conflict["field"], values, outcome, conflict["rule"], conflict["would_settle"]]
        )
    headers = ["Conflict", "Field", "Values", "Outcome", "Rule", "What would settle it"]
    return ["#### Conflicts", ""] + table(headers, rows) + [""]


def findings_part(findings: list[dict]) -> list[str]:
    rows = [[words(row["kind"]), row["contact_id"], row["detail"]] for row in findings]
    return ["#### Findings", ""] + table(["Finding", "Contact", "Detail"], rows) + [""]


def assessments_part(assessments: list[dict]) -> list[str]:
    rows = [
        [
            row["instrument"],
            f"{row['completed_date']} {row['completed_time'] or ''}".strip(),
            either(row["score"]),
            row["form_id"],
            ", ".join(f"item {number}: {score}" for number, score in (row["items"] or {}).items()),
            len(row["copies"]),
            len(row["mentions"]),
        ]
        for row in assessments
    ]
    headers = ["Instrument", "Completed", "Score", "Form", "Items", "Copies", "Mentions"]
    return ["#### Assessments", ""] + table(headers, rows) + [""]


def weeks_part(weeks: list[dict]) -> list[str]:
    rows = []
    for week in weeks:
        week = {**week, "minutes": sorted(week["minutes"], key=lambda entry: entry["minutes"])}
        week["margin"] = sorted(week["margin"], key=lambda entry: entry.get("minutes", 0))
        rows.append(
            [
                f"{week['week_start']} to {week['week_end']}" + (" (partial)" if week["partial"] else ""),
                either(entry["days"] for entry in week["days"]),
                ", ".join(week["days"][0]["dates"]) if week["days"] else "",
                either(entry["minutes"] for entry in week["minutes"]),
                either(f"{entry['hours']:.2f}" for entry in week["minutes"]),
                words(week["verdict"]),
                either(margin_of(entry) for entry in week["margin"]),
                ", ".join(week["conflicts"]),
                ", ".join(week["undocumented"]),
            ]
        )
    headers = ["Week", "Days", "Dates", "Minutes", "Hours", "Verdict", "Margin", "Depends on", "Dates with no document"]
    return ["#### Weekly status", ""] + table(headers, rows) + [""]


def totals_part(contacts: list[dict], rules: list[dict], plans: list[dict]) -> list[str]:
    lines = []
    for plan in plans:
        totals = sorted(counting.totals(contacts, rules, plan["start"], plan["end"]), key=lambda row: row["minutes"])
        rows = [
            ["Sessions", either(row["sessions"] for row in totals)],
            ["Therapy days", either(row["days"] for row in totals)],
            ["Minutes", either(row["minutes"] for row in totals)],
            ["Hours", either(f"{row['hours']:.2f}" for row in totals)],
        ]
        for name in sorted({name for row in totals for name in row["by_class"]}):
            sessions = either(row["by_class"][name]["sessions"] for row in totals)
            minutes = either(row["by_class"][name]["minutes"] for row in totals)
            rows.append([words(name), f"{sessions} sessions, {minutes} minutes"])
        lines += [f"#### Totals, {plan['start']} to {plan['end']}", ""] + table(["Measure", "Value"], rows) + [""]
    return lines


def part(connection) -> list[str]:
    lines = ["## What the record establishes", ""]
    lines += ["Worked out by code from the claims further down. No model takes part.", ""]
    for patient in store.patients(connection):
        name = connection.execute(
            "SELECT patient_name FROM documents WHERE patient_key = ? AND patient_name IS NOT NULL LIMIT 1",
            (patient,),
        ).fetchone()
        lines += [f"### Patient {patient}" + (f", {name[0]}" if name else ""), ""]
        rules = store.rows_of(connection, "plan_rules", patient, "rule_id")
        plans = counting.plans(rules)
        contacts = store.rows_of(connection, "contacts", patient, "service_date, contact_id")
        lines += plan_part(plans)
        lines += encounters_part(contacts, plans)
        lines += administrative_part(contacts)
        lines += conflicts_part(store.rows_of(connection, "conflicts", patient, "conflict_id"))
        lines += findings_part(store.rows_of(connection, "findings", patient, "finding_id"))
        lines += assessments_part(store.rows_of(connection, "assessments", patient, "completed_date"))
        lines += weeks_part(store.rows_of(connection, "weekly_status", patient, "week_start"))
        lines += totals_part(contacts, rules, plans)
    return lines
