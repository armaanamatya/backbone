"""Checks that run on a filled store and on written answers (stage 8).

Each function returns a list of problems, empty when the check passes. The
`check` command runs them on the store and answers on disk; the tests run
them on a store replayed from the saved results. None calls a model, and
none reads the answer key.

    overlaps                  check 8: no patient is in two contacts at once
    stated_minutes_disagree   check 7: stated minutes equal the clock times, or a conflict is open
    quotes_not_at_line        check 6: every quote is at its cited line
    numbers_not_in_results    check 11: every number in an answer comes from a result
    part_5_contradicts_part_6 a conflict part 6 lists is not called "not behind these figures" in part 5
    long_dates                dates in parts 2 to 6 are written as "Jan 19", not "2026-01-19"
    repeated_contacts         no contact is listed twice in part 5
"""

from __future__ import annotations

import re

from . import quotes, store

NUMBER = re.compile(r"\d+(?:[.:]\d+)*")
ISO_DATE = re.compile(r"(?<!\d)\d{4}-\d{2}-\d{2}(?!\d)")
CHECKED_PARTS = ("in short", "2. the answer", "3. figures", "4. what contributed", "5. what was excluded", "6. not settled", "7. assumptions", "8. documents not read")


def _clock(text: str) -> int:
    return int(text[:2]) * 60 + int(text[3:])


# --------------------------------------------------------------------------
# On the store
# --------------------------------------------------------------------------


def overlaps(connection, patient: str | None = None) -> list[dict]:
    """Check 8. Two contacts of one patient on one date whose presence
    intervals overlap, under any way the open conflicts could be settled.
    The end of an interval is not inside it (D-34)."""
    found = []
    for who in [patient] if patient else store.patients(connection):
        rows = [r for r in store.rows_of(connection, "contacts", who, "service_date, contact_id") if r["record_kind"] == "encounter"]
        for index, first in enumerate(rows):
            for second in rows[index + 1 :]:
                if first["service_date"] != second["service_date"]:
                    continue
                for a in first["presence"]:
                    for b in second["presence"]:
                        if not (a.get("start") and a.get("end") and b.get("start") and b.get("end")):
                            continue
                        if _clock(a["start"]) < _clock(b["end"]) and _clock(b["start"]) < _clock(a["end"]):
                            found.append(
                                {
                                    "patient": who,
                                    "date": first["service_date"],
                                    "first": first["encounter_id"] or first["contact_id"],
                                    "first_present": f"{a['start']}–{a['end']}",
                                    "second": second["encounter_id"] or second["contact_id"],
                                    "second_present": f"{b['start']}–{b['end']}",
                                }
                            )
    return found


def stated_minutes_disagree(connection, patient: str | None = None) -> list[dict]:
    """Check 7. Where a document states the patient's minutes for a contact,
    the figure is one of the contact's alternatives, or a conflict on its
    minutes is recorded."""
    found = []
    for who in [patient] if patient else store.patients(connection):
        conflicts = {(c["contact_id"], c["field"]) for c in store.rows_of(connection, "conflicts", who)}
        for contact in store.rows_of(connection, "contacts", who, "service_date, contact_id"):
            if not contact["claims"]:
                continue
            marks = ",".join("?" * len(contact["claims"]))
            stated = connection.execute(
                f"SELECT claim_id, value FROM claims WHERE claim_id IN ({marks}) AND type = 'stated_minutes'"
                " AND valid = 1 AND quote_status != 'unverified'",
                contact["claims"],
            ).fetchall()
            minutes = {m["minutes"] for m in contact["minutes"] if m["minutes"] is not None}
            for row in stated:
                value = store.from_json(row["value"])
                if value.get("of") != "patient_present" or not value.get("minutes"):
                    continue
                if value["minutes"] in minutes or (contact["contact_id"], "minutes") in conflicts:
                    continue
                found.append({"patient": who, "contact": contact["encounter_id"] or contact["contact_id"], "stated": value["minutes"], "from_clock": sorted(minutes), "claim": row["claim_id"]})
    return found


def quotes_not_at_line(connection) -> list[dict]:
    """Check 6, on the store: every claim whose quote was marked found is at its line."""
    found = []
    rows = connection.execute(
        "SELECT c.claim_id, c.quote, c.line, c.quote_status, d.text, d.file_name FROM claims c JOIN documents d USING (doc_hash)"
    ).fetchall()
    for row in rows:
        if row["quote_status"] == quotes.UNVERIFIED:
            continue
        lines = quotes.split_lines(row["text"])
        at = 1 <= (row["line"] or 0) <= len(lines) and row["quote"] in lines[row["line"] - 1]
        if not at:
            found.append({"claim": row["claim_id"], "file": row["file_name"], "line": row["line"], "quote": row["quote"]})
    return found


# --------------------------------------------------------------------------
# On a written answer
# --------------------------------------------------------------------------


def _tokens(text: str) -> set[str]:
    found = set(NUMBER.findall(text))
    # "05" in a date is "5" in a sentence.
    return found | {str(int(token)) for token in found if token.isdigit()}


def _numbers_of(value, into: set) -> None:
    """Every number a result holds: as a value, inside a string, or as the
    length of a list, which is what a count in a sentence is."""
    if isinstance(value, bool) or value is None:
        return
    if isinstance(value, int):
        into.add(str(abs(value)))
    elif isinstance(value, float):
        into.add(f"{abs(value):.2f}")
        into.add(f"{abs(value):g}")
    elif isinstance(value, str):
        into |= _tokens(value)
    elif isinstance(value, dict):
        into.add(str(len(value)))
        for item in value.values():
            _numbers_of(item, into)
    elif isinstance(value, (list, tuple)):
        into.add(str(len(value)))
        for item in value:
            _numbers_of(item, into)


def _minutes_between(results) -> set[str]:
    """The length of every removed interval, which an answer writes as minutes."""
    found = set()
    for result in results:
        for row in result.get("contributed", []) + result.get("excluded", []) + result.get("contacts", []) + result.get("rows", []):
            if not isinstance(row, dict):
                continue
            for a, b in row.get("removed", []) or []:
                found.add(str(_clock(b) - _clock(a)))
    return found


def numbers_not_in_results(built: dict) -> list[dict]:
    """Check 11. Every number in the answer text, outside part 1 and part 9,
    is a value from a function result, a number inside a quoted line, the
    length of a list in a result, or the length of a removed interval."""
    allowed: set[str] = set()
    for result in built.get("results", []):
        _numbers_of(result, allowed)
    _numbers_of(built.get("patient"), allowed)
    _numbers_of(built.get("lookup"), allowed)
    allowed |= _minutes_between(built.get("results", []))
    # Part 9 names the version; part 1 is the plan the model returned.
    found = []
    for part in CHECKED_PARTS:
        for line in built["parts"].get(part, []):
            for token in sorted(_tokens(line)):
                if token in allowed:
                    continue
                # 9.75 hours may be stored as 9.75 and written as 9.75; 2.0 is written 2.00.
                try:
                    if f"{float(token):.2f}" in allowed or f"{float(token):g}" in allowed:
                        continue
                except ValueError:
                    pass
                found.append({"question": built.get("question_id"), "part": part, "number": token, "line": line[:160]})
    return found


def part_5_contradicts_part_6(built: dict) -> list[dict]:
    """A conflict that part 6 lists as not settled is not also called "not
    behind these figures" in part 5 (Discussion 32)."""
    unsettled = "\n".join(built["parts"].get("6. not settled", []))
    found = []
    for line in built["parts"].get("5. what was excluded", []):
        if "not behind these figures" not in line:
            continue
        name = line.split("figures: ", 1)[-1].split(",")[0].strip()
        if name and name in unsettled:
            found.append({"question": built.get("question_id"), "conflict": name, "line": line[:160]})
    return found


def long_dates(built: dict) -> list[dict]:
    """Dates in the written parts are in the short form, "Jan 19", except
    inside a quoted line from a document (choice 15 of O-51)."""
    found = []
    for part in ("in short", "2. the answer", "3. figures", "5. what was excluded", "6. not settled"):
        for line in built["parts"].get(part, []):
            outside = re.sub(r'"[^"]*"', "", line)
            for on in ISO_DATE.findall(outside):
                found.append({"question": built.get("question_id"), "part": part, "date": on, "line": line[:160]})
    return found


def repeated_contacts(built: dict) -> list[dict]:
    """No encounter opens two top-level lines of part 5."""
    seen, found = {}, []
    for line in built["parts"].get("5. what was excluded", []):
        if line.startswith("  "):
            continue
        match = re.match(r"- ([A-Z]{2}-[A-Z]\d+), [A-Z][a-z]{2} \d{1,2}, ", line)
        if not match:
            continue
        name = match.group(1)
        if name in seen:
            found.append({"question": built.get("question_id"), "contact": name, "line": line[:160]})
        seen[name] = line
    return found


ANSWER_CHECKS = {
    "numbers in the text come from the results (check 11)": numbers_not_in_results,
    "part 5 does not contradict part 6": part_5_contradicts_part_6,
    "dates are in the short form": long_dates,
    "no contact is listed twice in part 5": repeated_contacts,
}
STORE_CHECKS = {
    "no patient is in two contacts at once (check 8)": overlaps,
    "stated minutes equal the clock times, or a conflict is open (check 7)": stated_minutes_disagree,
    "every quote is at its cited line (check 6)": quotes_not_at_line,
}
