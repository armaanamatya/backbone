"""Writes the nine-part answer from the function results (R-32, R-47).

Code writes every sentence. Every number comes from a result, and every
citation was checked against its source line when the result was made.

The plan the model returned says which functions to run. What each result
does in the answer depends on its role:

    primary     the question asked for it: its headline and answer are part 2
    breakdown   a second cut of the same figures: it goes to part 3
    supporting  exclusions and disagreements: they go to parts 5 and 6
"""

from __future__ import annotations

import re
from datetime import date

ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ISO_DATE_ANYWHERE = re.compile(r"(?<!\d)\d{4}-\d{2}-\d{2}(?!\d)")

ANSWER_FUNCTIONS = {
    "care_delivered",
    "goal_status",
    "date_detail",
    "assessments",
    "observations",
    "patients_below_goal",
    "compare_periods",
}
SUPPORTING_FUNCTIONS = {"not_counted", "conflicts_and_findings"}

STATUS_WORDS = {
    "held": "held",
    "held_without_patient": "held with the patient absent",
    "no_show": "not held: no-show",
    "cancelled_by_patient": "not held: cancelled by the patient",
    "cancelled_by_clinic": "not held: cancelled by the clinic",
    "absent": "not held: the patient was absent",
    "not_established": "attendance not established",
    "unsettled": "attendance unsettled",
    "recorded": "recorded",
}
VERDICT_WORDS = {"met": "met", "not_met": "not met", "cannot_determine": "cannot be determined"}
KIND_WORDS = {
    "attendance_record": "The attendance record",
    "clinical_note": "The clinical note",
    "correction": "The correction",
    "platform_export": "The telehealth platform export",
    "draft_note": "The draft note",
    "billing_extract": "The charge extract",
    "schedule_export": "The schedule export",
    "scheduling_log": "The scheduling log",
    "cancellation_notice": "The cancellation notice",
    "questionnaire_review": "The questionnaire review",
    "import_receipt": "The import receipt",
    "plan": "The treatment plan",
    "authorization": "The authorization",
    "cover_sheet": "The cover sheet",
}
WHAT_WORDS = {
    "contact_interval": "the contact",
    "patient_present": "the patient present",
    "patient_arrival": "arrival",
    "patient_departure": "departure",
    "no_therapy_interval": "no therapy",
    "patient_absent_interval": "time without the patient",
    "connection": "a call",
    "other": "a time",
}
STATEMENT_WORDS = {
    "same_contact_continued": "says the second part continued the same contact",
    "separate_contact": "says this is a separate contact",
    "no_patient_contact": "says there was no contact with the patient",
    "no_therapy_provided": "says no therapy was provided",
    "is_copy_or_resend": "says it is a copy",
    "no_new_signature": "carries no new signature",
    "made_before_the_service": "was made before the service",
    "is_draft_or_unsigned": "is a draft, unsigned",
    "not_a_visit": "documents no visit",
    "no_clinical_service": "says no clinical service was provided",
    "prepared_from_signed_record": "was prepared from a signed record",
}
CANNOT_ESTABLISH = {"draft_note", "billing_extract", "schedule_export", "scheduling_log", "cancellation_notice"}
TOPIC_ORDER = ["mood", "anxiety", "sleep", "safety", "functioning", "progress", "reason_for_contact", "medication", "other"]


# --------------------------------------------------------------------------
# Small words
# --------------------------------------------------------------------------


def either(values) -> str:
    seen = []
    for value in values:
        if value not in seen:
            seen.append(value)
    return " or ".join(str(v) for v in seen)


def hours_of(values) -> str:
    return either(f"{value:.2f}" for value in values)


def plural(count, word) -> str:
    return f"{count} {word}{'' if count == 1 else 's'}"


def day(text) -> str:
    """2026-01-19 as "Jan 19"."""
    if not text:
        return "an unknown date"
    on = date.fromisoformat(text)
    return on.strftime("%b %d").replace(" 0", " ")


def span(start, end) -> str:
    return f"{day(start)} to {day(end)}" if start and end else "the record"


def words(text) -> str:
    return (text or "").replace("_", " ")


def cite(source) -> str:
    flag = "" if source["verified"] else " [quote not found at this line]"
    return f"{source['document']} line {source['line']}: \"{source['quote']}\"{flag}"


def time_words(value: dict, label: str | None) -> str:
    what = WHAT_WORDS.get(value.get("what"), "a time")
    start, end = value.get("start"), value.get("end")
    when = f"{start}–{end}" if start and end else (start or end or "")
    detail = value.get("detail")
    if label == "scheduled":
        what = "the scheduled contact" if what == "the contact" else f"scheduled {what}"
    text = f"{what} {when}".strip()
    if detail and value.get("what") in ("no_therapy_interval", "patient_absent_interval", "other"):
        text += f" ({detail})"
    return text


def claim_words(claim: dict) -> str | None:
    value, kind = claim["value"], claim["type"]
    if kind == "time":
        return time_words(value, claim.get("label"))
    if kind == "attendance":
        return f"marks it \"{value.get('status_as_written')}\""
    if kind == "correction":
        return f"replaces the {value.get('field')} {value.get('old_value')} with {value.get('new_value')}"
    if kind == "stated_minutes":
        of = {"patient_present": " with the patient", "contact_total": " for the contact", "without_patient": " without the patient"}.get(value.get("of"), "")
        return f"states {value.get('minutes')} minutes{of}"
    if kind == "charge":
        return f"posts charge {value.get('charge_id')} for {value.get('description')}"
    if kind == "statement":
        return STATEMENT_WORDS.get(value.get("says"))
    if kind == "participant" and value.get("role") == "patient" and value.get("presence") not in (None, "not_stated"):
        return f"has the patient {words(value.get('presence'))}"
    return None


def contact_line(row) -> str:
    status = STATUS_WORDS.get(row["status"], row["status"]) + (", attended in part" if row["partial"] else "")
    present = either(f"{a}–{b}" for a, b in row["present"]) or "no clock times"
    removed = ", ".join(f"{a}–{b}" for a, b in row["removed"])
    minutes = f"{either(row['minutes'])} minutes" if row["minutes"] else "no minutes"
    line = f"{row['encounter'] or row['date']}, {day(row['date'])}, {words(row['class'])}: {status}; present {present}"
    if removed:
        line += f"; removed {removed}"
    line += f"; {minutes}"
    if row.get("minutes_without_patient"):
        line += f" ({row['minutes_without_patient']} without the patient)"
    if row.get("modality") == "video":
        line += "; by video"
    if row.get("clinicians"):
        line += f"; with {' and '.join(row['clinicians'])}" if len(row["clinicians"]) > 1 else f"; with {row['clinicians'][0]}"
    if row.get("notes"):
        line += "; " + "; ".join(row["notes"])
    if len(row.get("documents", [])) > 1:
        line += f"; described by {len(row['documents'])} documents ({', '.join(row['documents'])}), counted once"
    if row.get("copies"):
        line += f"; {', '.join(row['copies'])} is a copy of an earlier record and adds nothing"
    return line


def cites(result, row) -> list[str]:
    seen, lines = set(), []
    for source in result["sources"]:
        if source["claim"] not in row.get("sources", []):
            continue
        key = (source["document"], source["line"], source["quote"])
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"  - {cite(source)}")
    return lines


def dedupe(lines: list[str]) -> list[str]:
    """Drops a repeated block: a line and the indented lines under it."""
    kept, seen, under, skipping = [], set(), set(), False
    for line in lines:
        indented = line.startswith("  ")
        if not indented:
            skipping = line in seen
            seen.add(line)
            under = set()
        elif line in under:
            continue
        under.add(line)
        if not skipping:
            kept.append(line)
    return kept


def conflict_words(conflict: dict) -> str:
    values = "; ".join(f"{a['value']} ({', '.join(a.get('documents') or []) or 'no document'})" for a in conflict["alternatives"])
    return f"{conflict['conflict_id'].split('/')[-1].split(':')[0]}, {conflict['field']}: {values}"


# --------------------------------------------------------------------------
# One block for each function
# --------------------------------------------------------------------------


def _block(**parts) -> dict:
    block = {
        "headline": [], "aside": [], "answer": [], "figures": [], "contributed": [], "excluded": [],
        # Contacts that did not count. Written once: `not_counted` writes them
        # with the reason a document gives, when it is in the plan.
        "excluded_contacts": [],
        "unsettled": [],
        # The open conflicts of `conflicts_and_findings`, by id, so that one the
        # figures depend on goes to part 6 and the rest are marked as elsewhere.
        "unsettled_by_id": {},
        "assumptions": [],
    }
    block.update(parts)
    return block


def short_dates(text: str) -> str:
    """Every ISO date in a code-written line as "Jan 19". Never applied to a quote."""
    return ISO_DATE_ANYWHERE.sub(lambda m: day(m.group(0)), text)


def ranges_in_words(ranges) -> str:
    """"2026-01-17 to 2026-01-18" as "Jan 17 to Jan 18"."""
    return ", ".join(" to ".join(day(part) for part in entry.split(" to ")) for entry in ranges)


def admin_line(row) -> str:
    """An administrative record, with its clock time where the record has one."""
    when = row["contact_id"].split("/")[-1]
    at = f" at {when}" if len(when) == 5 and when[2] == ":" else ""
    return f"{day(row['date'])}{at}, {words(row['class'])} ({row['modality'] or 'how not stated'})"


def _removed_lines(rows) -> list[str]:
    lines = []
    for row in rows:
        for removed in row.get("removed_rows", []):
            start, end = removed["start"], removed["end"]
            minutes = (int(end[:2]) * 60 + int(end[3:])) - (int(start[:2]) * 60 + int(start[3:]))
            lines.append(f"- Removed from the minutes: {row['encounter']} on {day(row['date'])}, {start}–{end}, {minutes} minutes ({removed['why']}).")
        if row.get("minutes_without_patient") and row["status"] == "held":
            lines.append(f"- Time without the patient: {row['encounter']} on {day(row['date'])}, {row['minutes_without_patient']} minutes, not the patient's.")
    return lines


def write_care(result, plan) -> dict:
    totals = result["totals"]
    counts = result["counts"]
    period = result["period"]
    headline, answer, figures = [], [], []
    if totals:
        sessions = either(t["sessions"] for t in totals)
        days = either(t["days"] for t in totals)
        minutes = either(t["minutes"] for t in totals)
        hours = either(f"{t['hours']:.2f}" for t in totals)
        classes = sorted({c for t in totals for c in t["by_class"]})
        by_class = ", ".join(f"{either(t['by_class'].get(c, {}).get('sessions', 0) for t in totals)} {words(c)}" for c in classes)
        first = f"{sessions} therapy session{'s' if sessions != '1' else ''} on {days} distinct days, {span(period['start'], period['end'])}" + (f": {by_class}." if by_class else ".")
        second = f"{minutes} minutes of therapy, which is {hours} hours, {span(period['start'], period['end'])}."
        headline += [second, first] if minutes_first(plan) else [first, second]
    aside = []
    if plan.get("other_readings"):
        aside.append(
            f"Under other readings of the question: {counts['held']} contacts held, {counts['with_patient_present']} with the patient present,"
            f" {counts['encounters']} encounters in the record."
        )
    for group in result["groups"]:
        rows = group["totals"]
        label = span(group["start"], group["end"]) if group.get("start") else (day(group["group"]) if ISO_DATE.match(group["group"]) else words(group["group"]))
        line = (
            f"- {label}: "
            f"{either(r['sessions'] for r in rows)} session{'s' if either(r['sessions'] for r in rows) != '1' else ''}, "
            f"{either(r['days'] for r in rows)} day{'s' if either(r['days'] for r in rows) != '1' else ''}, "
            f"{either(r['minutes'] for r in rows)} minutes ({hours_of(r['hours'] for r in rows)} hours)"
        )
        if group.get("start"):
            line += ", by class " + ", ".join(f"{words(c)} {either(r['by_class'].get(c, {}).get('minutes', 0) for r in rows)}" for c in sorted({c for r in rows for c in r["by_class"]}))
        answer.append(line + ".")
    figures += [f"- {short_dates(line)}" for line in result["calculation"]]
    for c in sorted({c for t in totals for c in t["by_class"]}):
        figures.append(f"- {words(c)}: {either(t['by_class'][c]['sessions'] for t in totals)} sessions, {either(t['by_class'][c]['minutes'] for t in totals)} minutes")
    figures.append(
        f"- Counts in the same period: {counts['encounters']} encounters in the record, {counts['held']} held, {counts['with_patient_present']} with the patient present,"
        f" {either(counts['therapy_sessions'])} therapy sessions, {counts['administrative_records']} administrative records (calls, messages, questionnaire reviews)."
    )
    if result["undocumented"]:
        figures.append(f"- Dates in the period with no document: {ranges_in_words(result['undocumented'])}.")
    contributed = []
    for row in result["contributed"]:
        contributed.append(f"- {contact_line(row)}")
        contributed += cites(result, row)
    excluded = _removed_lines(result["contributed"])
    excluded_contacts = [f"- {contact_line(row)}. Not counted: {row['why_not']}." for row in result["excluded"]]
    assumptions = []
    if any(r["modality"] == "video" for r in result["contributed"]):
        assumptions.append("A session by video counts as patient-present.")
    if any(r["partial"] for r in result["contributed"]):
        assumptions.append("A session the patient attended in part counts as a session and a therapy day; only its minutes are reduced.")
    if any(r["removed"] for r in result["contributed"]):
        assumptions.append("An interval a document says had no therapy, such as a group break or a lost connection, is removed from the minutes.")
    if result.get("plan"):
        assumptions.append(f"\"Therapy\" means the classes the plan {result['plan']['document']} counts: {', '.join(words(c) for c in result['plan']['counted_classes'])}, with the patient present.")
    return _block(headline=headline, aside=aside, answer=answer, figures=figures, contributed=contributed, excluded=excluded, excluded_contacts=excluded_contacts, assumptions=assumptions)


def minutes_first(plan) -> bool:
    """Whether the question is about minutes or hours before sessions."""
    reading = (plan.get("reading") or "").lower()
    positions = {word: reading.find(word) for word in ("minute", "hour", "session", "visit", "contact", "day")}
    found = {word: at for word, at in positions.items() if at >= 0}
    if not found:
        return False
    return min(found, key=found.get) in ("minute", "hour")


def write_goal(result, plan) -> dict:
    headline, answer = [], []
    summary = result["summary"]
    verdicts = ", ".join(f"{span(w['start'], w['end'])} {VERDICT_WORDS[w['verdict']]}" for w in result["weeks"])
    headline.append(
        f"Of {plural(len(result['weeks']), 'week')}, {summary['met']} met the goal, {summary['not_met']} did not, and {summary['cannot_determine']} cannot be determined: {verdicts}."
    )
    for p in result["plans"]:
        needs = " and ".join(f"at least {r['minimum']:g} {words(r['measure'])}" for r in p["requirements"])
        answer.append(
            f"The goal in the plan {p['document']}, signed {short_dates(p['signed']).replace('T', ' at ')}: {needs} in each week starting {p['week_starts_on']},"
            f" counting {', '.join(words(c) for c in p['counted_classes'])} with the patient present; not counting {', '.join(words(c) for c in p['excluded_classes'])}."
        )
    answer.append(f"The record holds {plural(len(result['plans']), 'plan')} and {plural(result['plan_changes'], 'change')} to it.")
    for week in result["weeks"]:
        margin = either(
            ", ".join(f"{abs(m[k]):g} {k if abs(m[k]) != 1 else k[:-1]} {'short' if m[k] < 0 else 'over'}" for k in ("days", "minutes") if k in m and m[k] != 0) or "exactly met"
            for m in week["margin"]
        )
        answer.append(
            f"- {span(week['start'], week['end'])}{' (partial: runs past the episode)' if week['partial'] else ''}: {either(week['days'])} therapy days ({', '.join(day(d) for d in week['dates']) or 'none'}),"
            f" {either(week['minutes'])} minutes ({hours_of(week['hours'])} hours): {VERDICT_WORDS[week['verdict']]} ({margin})."
            + (f" Depends on the open {', '.join(c.split('/')[-1].replace(':', ' ') for c in week['depends_on'])}." if week["depends_on"] else "")
        )
    figures = [f"- {short_dates(line)}" for line in result["calculation"]]
    for week in result["weeks"]:
        if week["undocumented"]:
            figures.append(f"- {span(week['start'], week['end'])}: dates with no document {ranges_in_words(week['undocumented'])}.")
    contributed = []
    for p in result["plans"]:
        contributed.append(f"- The plan {p['document']}:")
        contributed += [f"  - {cite(s)}" for s in result["sources"] if s["document"] == p["document"] and s["type"] == "plan_rule"]
    for row in result["contributed"]:
        contributed.append(f"- {contact_line(row)}")
        contributed += cites(result, row)
    excluded = _removed_lines(result["contributed"])
    excluded_contacts = [f"- {contact_line(row)}. Not counted: {row['why_not']}." for row in result["excluded"]]
    assumptions = []
    if any(w["partial"] for w in result["weeks"]):
        assumptions.append("A week that runs past the end of the episode is judged against the full requirement and labelled partial.")
    assumptions.append("A verdict is \"met\" only if every alternative meets the requirement, \"not met\" only if none does, and \"cannot be determined\" otherwise.")
    assumptions.append("The reason a week fell short, such as a cancellation, is context and does not change the verdict.")
    return _block(headline=headline, answer=answer, figures=figures, contributed=contributed, excluded=excluded, excluded_contacts=excluded_contacts, assumptions=assumptions)


def record_sentences(row: dict) -> list[str]:
    """One sentence for each kind of record about a contact, and its effect."""
    lines = []
    replaced = {}
    for conflict in row.get("conflicts", []):
        for alternative in conflict["alternatives"]:
            if alternative.get("note") and "replaced" in alternative["note"]:
                for document in alternative.get("documents", []):
                    replaced[document] = f"{conflict['field']} {alternative['value']}"
    open_values = {}
    for conflict in row.get("conflicts", []):
        if conflict["status"] == "open":
            for alternative in conflict["alternatives"]:
                for document in alternative.get("documents", []):
                    open_values[document] = f"{conflict['field']} {alternative['value']}"
    for said in row.get("documents_say", []):
        first = said["claims"][0]
        kind = first.get("kind") or "other"
        label = KIND_WORDS.get(kind, "The record")
        if first.get("copy"):
            label = "A later copy of the record"
        elif first.get("signed") == "signed":
            label += ", signed,"
        pieces = []
        for claim in said["claims"]:
            text = claim_words(claim)
            if text and text.lower() not in {piece.lower() for piece in pieces}:
                pieces.append(text)
        # "No therapy was provided" said beside a no-therapy interval is about
        # that interval, not about the contact (Discussion 32, defect 4).
        intervals = [c["value"] for c in said["claims"] if c["type"] == "time" and c["value"].get("what") == "no_therapy_interval" and c["value"].get("start") and c["value"].get("end")]
        if intervals and STATEMENT_WORDS["no_therapy_provided"] in pieces:
            when = ", ".join(f"{i['start']}–{i['end']}" for i in intervals)
            pieces[pieces.index(STATEMENT_WORDS["no_therapy_provided"])] = f"says no therapy was provided during {when}"
        effect = ""
        document = said["document"]
        if first.get("copy"):
            effect = " It changes nothing: a copy carries the date and authority of its original."
        elif kind == "correction" and any(piece.startswith("replaces") for piece in pieces):
            effect = " It replaces the value it names, because it is signed and names the contact, the field and the old value."
        elif kind in CANNOT_ESTABLISH:
            effect = " It cannot establish attendance, so it adds nothing to the minutes."
        if document in replaced:
            effect += f" Its {replaced[document]} was replaced by the correction."
        if document in open_values:
            effect += f" Its {open_values[document]} is one of two open alternatives."
        lines.append(f"- {label} {document} gives " + "; ".join(pieces) + "." + effect if pieces else f"- {label} {document} names the contact.{effect}")
    return lines


def write_date(result, plan) -> dict:
    on = result["date"]
    headline, answer = [], []
    if result["coverage"] == "not_documented":
        headline.append(f"{day(on)}: not documented. No document records a contact on this date, and none is dated on it. This does not say that no care took place.")
    elif result["coverage"] == "no_appointment_in_schedule":
        headline.append(f"{day(on)}: no contact is recorded. The schedule export {', '.join(result['covered_by_schedule'])} covers this date and lists no appointment on it.")
    elif result["coverage"] == "document_dated_only":
        headline.append(f"{day(on)}: no contact is recorded. Documents dated that day: " + "; ".join(f"{d['document']} ({words(d['kind'])})" for d in result["documents_dated"]) + ".")
    else:
        counts = result["counts"]
        headline.append(f"{day(on)}: {plural(counts['therapy_contacts'], 'therapy contact')} of {plural(counts['contacts'], 'encounter')}; patient therapy minutes {either(t['minutes'] for t in result['totals'])}.")
        for row in result["contacts"]:
            if row["record_kind"] != "encounter":
                continue
            line = f"- {contact_line(row)}" + ("" if row["counts"] else f". Not counted: {row['why_not']}")
            for finding in row["findings"]:
                line += f". {words(finding['kind']).capitalize()}"
            answer.append(line + ".")
            answer += ["  " + sentence for sentence in record_sentences(row)]
    figures = [f"- {line}" for line in result["calculation"] if line.strip() != "= 0"]
    contributed, excluded = [], []
    for row in result["contacts"]:
        line = f"- {contact_line(row)}" if row["record_kind"] == "encounter" else f"- {day(row['date'])}, {words(row['class'])}: an administrative record ({row['modality'] or 'how not stated'})"
        target = contributed if row["counts"] else excluded
        target.append(line if row["counts"] else line + f". Not counted: {row['why_not']}.")
        for said in row["documents_say"]:
            first = said["claims"][0]
            standing = f"{words(first['kind'])}{', signed' if first['signed'] == 'signed' else ''}{', a copy' if first['copy'] else ''}"
            target.append(f"  - {said['document']} ({standing}): " + "; ".join(f"line {c['line']}: \"{c['quote']}\"" for c in said["claims"][:6]))
        for conflict in row["conflicts"]:
            if conflict["status"] == "settled":
                target.append(f"  - {conflict_words(conflict)}. Settled by rule {conflict['rule']}: {conflict['outcome']}.")
        for finding in row["findings"]:
            target.append(f"  - Finding: {short_dates(finding['detail'])}")
    excluded = _removed_lines([r for r in result["contacts"] if r["counts"]]) + excluded
    assumptions = []
    if any(r["modality"] == "video" for r in result["contacts"]):
        assumptions.append("A session by video counts as patient-present.")
    if any(r["removed"] for r in result["contacts"]):
        assumptions.append("An interval a document says had no therapy, such as a group break or a lost connection, is removed from the minutes.")
    assumptions.append("\"Not documented\" is kept apart from \"did not happen\". The second is said only when a document says so.")
    return _block(headline=headline, answer=answer, figures=figures, contributed=contributed, excluded=excluded, assumptions=assumptions)


def write_assessments(result, plan) -> dict:
    on = result["arguments"].get("on")
    headline, answer = [], []
    rows = result["rows"]
    if on:
        if rows:
            headline.append(f"Completed on {day(on)}: " + "; ".join(f"{r['instrument']} {either(r['score'])}" for r in rows) + ".")
        else:
            headline.append(f"No questionnaire was completed on {day(on)}.")
        for received in result["received_on"]:
            of = received["of"]
            headline.append(f"A result received that day, in {received['document']}, is a copy of the {of['instrument']} of {day(of['completed_date'])}, score {either(of['score'])}. It is not a new assessment.")
    else:
        scores = " to ".join(either(r["score"]) for r in rows)
        dates = ", ".join(day(r["completed_date"]) for r in rows)
        instruments = ", ".join(sorted({r["instrument"] for r in rows}))
        headline.append(f"{instruments} {scores} across {plural(result['distinct'], 'distinct assessment')} ({dates})" + (f", {abs(result['overall_change'])} points {'lower' if result['overall_change'] < 0 else 'higher'} overall." if result["overall_change"] else "."))
        if result["changes"]:
            answer.append("Change between assessments: " + "; ".join(f"{day(c['from'])} to {day(c['to'])} {c['change']:+d}" for c in result["changes"]) + ".")
    figures = [f"- {short_dates(line)}" for line in result["calculation"]]
    contributed = []
    for row in rows:
        line = f"- {row['instrument']} {either(row['score'])}, completed {day(row['completed_date'])}" + (f" {row['completed_time']}" if row["completed_time"] else "") + (f", form {row['form_id']}" if row["form_id"] else "")
        if row["items"]:
            line += "; items: " + ", ".join(f"{k}: {v}" for k, v in row["items"].items())
        contributed.append(line)
        contributed += [f"  - {cite(s)}" for s in result["sources"] if s["claim"] in row["sources"]]
    excluded = []
    for row in rows:
        for copy in row["copies"]:
            dates = ", ".join(f"{d['kind']} {day(d['date'])}" for d in copy["dates"] if d["kind"] in ("received", "entered"))
            excluded.append(f"- {copy['document']}: a copy of the {row['instrument']} of {day(row['completed_date'])}" + (f" ({dates})" if dates else "") + ". Adds no assessment.")
            excluded += [f"  - {cite(s)}" for s in result["sources"] if s["claim"] == copy["claim"]]
        for mention in row["mentions"]:
            excluded.append(f"- {mention['document']}: a mention of the {row['instrument']} of {day(row['completed_date'])}. Adds no assessment.")
            excluded += [f"  - {cite(s)}" for s in result["sources"] if s["claim"] == mention["claim"]]
    assumptions = [
        "An assessment is identified by instrument and completion date, plus the form number where printed. Copies and mentions add none.",
        "Severity bands, and thresholds for response or remission, are outside knowledge and are not in the record.",
    ]
    return _block(headline=headline, answer=answer, figures=figures, contributed=contributed, excluded=excluded, assumptions=assumptions)


def latest_by_topic(rows) -> dict:
    latest = {}
    for row in rows:
        if row["topic"] not in latest or (row["date"] or "") >= (latest[row["topic"]]["date"] or ""):
            latest[row["topic"]] = row
    return latest


def write_observations(result, plan) -> dict:
    rows = result["rows"]
    headline, answer = [], []
    latest = latest_by_topic(rows)
    if "progress" in latest:
        row = latest["progress"]
        headline.append(f"The record's latest word on progress ({day(row['date'])}, {words(row['speaker'])}): \"{row['quote']}\" ({row['document']} line {row['line']}).")
    else:
        headline.append(f"{plural(len(rows), 'statement')} in the notes" + (f" on {', '.join(words(t) for t in result['by_topic'])}" if result["by_topic"] else "") + ".")
    for topic in [t for t in TOPIC_ORDER if t in result["by_topic"]]:
        found = [row for row in rows if row["topic"] == topic]
        answer.append(f"{plural(len(found), 'statement')} on {words(topic)}, in date order:")
        for row in found:
            who = words(row["speaker"]) + (f" ({row['speaker_name']})" if row.get("speaker_name") else "")
            answer.append(f"- {day(row['date'])}, {who}: \"{row['quote']}\" ({row['document']} line {row['line']})")
    if not rows:
        answer.append("No statement on that topic in the period.")
    figures = [f"- {line}" for line in result["calculation"]] + ["- By topic: " + ", ".join(f"{words(k)} {v}" for k, v in result["by_topic"].items())]
    contributed = [f"- {cite(s)}" for s in result["sources"]]
    excluded = []
    if result["copies_left_out"]:
        excluded.append(f"- {plural(result['copies_left_out'], 'statement')} in copies of other documents: a copy carries its original's statements.")
    if result.get("drafts_left_out"):
        excluded.append(f"- {plural(result['drafts_left_out'], 'statement')} in a draft: template text says nothing about the patient.")
    assumptions = ["The speaker of a statement is the person the sentence itself names as the source. Where it names none, the speaker is the author of the note; \"clinician\" means the clinician states it, not that the clinician observed it."]
    return _block(headline=headline, answer=answer, figures=figures, contributed=contributed, excluded=excluded, assumptions=assumptions)


def write_not_counted(result, plan) -> dict:
    encounters = [r for r in result["rows"] if r["record_kind"] == "encounter"]
    admin = [r for r in result["rows"] if r["record_kind"] != "encounter"]
    reasons = [f"{reason} ({', '.join(names)})" for reason, names in result["by_reason"].items() if not reason.startswith("an administrative record")]
    headline = []
    if encounters:
        headline.append(f"{plural(len(encounters), 'encounter')} did not count in {span(result['period']['start'], result['period']['end'])}: " + "; ".join(reasons) + ".")
    else:
        headline.append(f"Every encounter in {span(result['period']['start'], result['period']['end'])} counted.")
    if result["missed"]:
        headline.append(
            f"Appointments missed or cancelled: {len(result['missed'])}: "
            + "; ".join(f"{r['encounter']} on {day(r['date'])}, {STATUS_WORDS[r['status']].replace('not held: ', '')}" + (f" ({'; '.join(r['reasons_given'])})" if r["reasons_given"] else "") for r in result["missed"])
            + "."
        )
    if admin:
        headline.append(f"{plural(len(admin), 'administrative record')} kept and never counted: " + "; ".join(admin_line(r) for r in admin) + ".")
    figures = [f"- {line}" for line in result["calculation"]]
    for reason, names in result["by_reason"].items():
        figures.append(f"- {reason}: " + ", ".join(day(n) if ISO_DATE.match(n) else n for n in names))
    excluded = []
    for row in encounters:
        given = f" Reason given: {'; '.join(row['reasons_given'])}." if row["reasons_given"] else ""
        excluded.append(f"- {contact_line(row)}. Not counted: {row['reason']}.{given}")
        excluded += cites(result, row)
    for row in admin:
        excluded.append(f"- {admin_line(row)}, in {', '.join(row['documents'])}: an administrative record, never counted.")
    if result["documents_without_encounter"]:
        excluded.append("- Documents that describe no encounter: " + "; ".join(f"{d['document']} ({', '.join(words(k) for k in d['kinds'])})" for d in result["documents_without_encounter"]) + ".")
    return _block(headline=headline, figures=figures, excluded=excluded, assumptions=["A contact held without the patient is recorded as held with the patient absent, not as a missed appointment."])


def write_conflicts(result, plan) -> dict:
    headline, unsettled, excluded, contributed = [], [], [], []
    by_id = {}
    if result["open"]:
        headline.append(f"{plural(len(result['open']), 'open disagreement')}.")
        for c in result["open"]:
            unsettled.append(f"- {conflict_words(c)}. Effect: {c['effect']}." + (f" Weeks affected: {', '.join(day(w) for w in c['weeks_affected'])}." if c["weeks_affected"] else "") + f" What would settle it: {c['would_settle']}")
            by_id[c["conflict_id"]] = unsettled[-1]
            contributed.append(f"- {c['encounter'] or c['conflict_id']}, {c['field']}:")
            contributed += [f"  - {cite(s)}" for s in result["sources"] if any(s["claim"] in a.get("claims", []) for a in c["alternatives"])]
    else:
        headline.append("Nothing is open.")
    if result["settled"] or result["findings"]:
        headline.append(f"{plural(len(result['settled']), 'disagreement')} settled by a rule and {plural(len(result['findings']), 'finding')}; see part 5.")
    for c in result["settled"]:
        excluded.append(f"- {conflict_words(c)}. Settled by rule {c['rule']}: {c['outcome']}. The other value is not used.")
        excluded += [f"  - {cite(s)}" for s in result["sources"] if any(s["claim"] in a.get("claims", []) for a in c["alternatives"])]
    for f in result["findings"]:
        excluded.append(f"- Finding, {f['encounter'] or f['contact_id']}, {day(f['date'])}: {short_dates(f['detail'])}")
        excluded += [f"  - {cite(s)}" for s in result["sources"] if s["claim"] in f["claims"]]
    return _block(
        headline=headline, figures=[f"- {line}" for line in result["calculation"]], contributed=contributed, excluded=excluded, unsettled=unsettled, unsettled_by_id=by_id,
        assumptions=["Two records of equal standing that disagree stay open, as alternatives. A signed correction, a copy, or a record that cannot establish attendance is settled by rule."],
    )


def write_below(result, plan) -> dict:
    weeks = result["arguments"]["weeks"]
    headline = [f"{len(result['rows'])} of {plural(result['patients_checked'], 'patient')} with {weeks} consecutive weeks below the goal."]
    answer = []
    for row in result["rows"]:
        answer.append(f"- {row['name'] or row['patient']} ({row['patient']}): {ranges_in_words(row['weeks'])}; verdicts {', '.join(VERDICT_WORDS[v] for v in row['verdicts'])}" + ("; depends on an open conflict: " + ", ".join(c.split("/")[-1] for c in row["conflicts"]) if row["depends_on_open_conflict"] else "; does not depend on an open conflict") + ".")
    return _block(headline=headline, answer=answer, figures=[f"- {line}" for line in result["calculation"]], contributed=["- The weekly status of each patient, worked out from that patient's plan and contacts."], assumptions=["\"Below the goal\" means a week whose verdict is \"not met\". A week that cannot be determined is counted only where the run depends on it, and that is said."])


def write_compare(result, plan) -> dict:
    a, b = result["first"], result["second"]

    def one(name, side):
        classes = ", ".join(f"{words(c)} {either(v['sessions'])} sessions / {either(v['minutes'])} minutes" for c, v in side["by_class"].items())
        return f"{name} {span(side['period']['start'], side['period']['end'])}: {either(side['sessions'])} sessions on {either(side['days'])} days, {either(side['minutes'])} minutes" + (f": {classes}." if classes else ".")

    headline = [one("First period", a), one("Second period", b), f"Difference, second less first: sessions {either(result['difference']['sessions'])}, days {either(result['difference']['days'])}, minutes {either(result['difference']['minutes'])}."]
    return _block(headline=headline, figures=[f"- {line}" for line in result["calculation"]], contributed=[f"- {cite(s)}" for s in result["sources"]])


WRITERS = {
    "care_delivered": write_care,
    "goal_status": write_goal,
    "date_detail": write_date,
    "assessments": write_assessments,
    "observations": write_observations,
    "not_counted": write_not_counted,
    "conflicts_and_findings": write_conflicts,
    "patients_below_goal": write_below,
    "compare_periods": write_compare,
}


# --------------------------------------------------------------------------
# Roles, the progress block, and the lead
# --------------------------------------------------------------------------


def roles(results) -> list[str]:
    names = [r["function"] for r in results]
    has_answer = any(n in ANSWER_FUNCTIONS for n in names)
    seen, found = set(), []
    for result in results:
        name = result["function"]
        if name in SUPPORTING_FUNCTIONS and has_answer:
            role = "supporting"
        elif name == "care_delivered" and {"goal_status", "date_detail"} & set(names):
            role = "breakdown"
        else:
            role = "primary"
        seen.add(name)
        found.append(role)
    return found


def progress_block(results) -> list[str]:
    """What the record supports and what it does not settle, from general rules,
    when the answer holds both scores and statements."""
    scores = next((r for r in results if r["function"] == "assessments" and not r["arguments"].get("on")), None)
    said = next((r for r in results if r["function"] == "observations"), None)
    if not scores or not said:
        return []
    lines = ["What the record supports:"]
    rows = scores["rows"]
    if len(rows) >= 2 and scores["overall_change"] is not None:
        direction = "fall" if scores["overall_change"] < 0 else ("rise" if scores["overall_change"] > 0 else "no change")
        lines.append(f"- A {direction} in {', '.join(sorted({r['instrument'] for r in rows}))} of {abs(scores['overall_change'])} points across {plural(len(rows), 'distinct assessment')}, {day(rows[0]['completed_date'])} to {day(rows[-1]['completed_date'])}.")
    latest = latest_by_topic(said["rows"])
    for topic in [t for t in TOPIC_ORDER if t in latest and t != "reason_for_contact"]:
        row = latest[topic]
        lines.append(f"- {words(topic).capitalize()}, latest statement ({day(row['date'])}, {words(row['speaker'])}): \"{row['quote']}\" ({row['document']} line {row['line']}).")
    lines.append("What the record does not settle:")
    instruments = scores["instruments"]
    described = [words(t) for t in TOPIC_ORDER if t in said["by_topic"] and t not in ("progress", "reason_for_contact", "other", "medication")]
    named = ", ".join(instruments) if instruments else "no instrument"
    listed = described[0] if len(described) == 1 else ", ".join(described[:-1]) + " and " + described[-1] if described else "the symptoms"
    lines.append(
        f"- A measured level of anything beyond what the record's {plural(len(instruments), 'instrument').replace('1 instrument', 'one instrument')} ({named}) measures:"
        f" the record holds no other measure, so what the notes say on {listed} is description, not measurement."
    )
    lines.append("- A response, a remission or a change of severity band: the thresholds are outside the record.")
    if len(scores.get("held_classes", [])) > 1:
        lines.append(f"- Which care produced the change: {', '.join(words(c) for c in scores['held_classes'])} ran in the same period, and nothing in the record separates their effects.")
    attendance = scores.get("attendance", {})
    missed = sum(attendance.get(k, 0) for k in ("no_show", "cancelled_by_patient"))
    absent = scores.get("absent_from", 0)
    if missed or absent:
        lines.append(
            f"- Unbroken engagement: {plural(attendance.get('no_show', 0), 'no-show')} and {plural(attendance.get('cancelled_by_patient', 0), 'cancellation by the patient')} in the period"
            + (f", and {plural(absent, 'contact')} held without the patient, leaving out contacts between professionals" if absent else "")
            + "."
        )
    return lines


def lead(blocks, parts, results) -> list[str]:
    """Two to four sentences: the answer, the one open point, the one exclusion that matters.
    `blocks` and `results` are in the same order."""
    order = ["assessments", "goal_status", "care_delivered", "observations", "date_detail", "compare_periods", "patients_below_goal"]
    primary = [(block, result) for (block, role), result in zip(blocks, results) if role == "primary" and block["headline"]]
    primary.sort(key=lambda entry: order.index(entry[1]["function"]) if entry[1]["function"] in order else len(order))
    lines = []
    if len(primary) == 1:
        lines = primary[0][0]["headline"][:2]
    else:
        for block, _ in primary:
            if block["headline"][0] not in lines:
                lines.append(block["headline"][0])
            if len(lines) == 2:
                break
        if len(lines) == 1 and len(primary[0][0]["headline"]) > 1:
            lines.append(primary[0][0]["headline"][1])
    reason = _reason_for_contact(results)
    if reason:
        lines.append(reason)
    point = open_point(results)
    if point:
        lines.append(point)
    exclusion = _exclusion_that_matters(results)
    if exclusion:
        lines.append(exclusion)
    return lines[:4]


def _reason_for_contact(results) -> str | None:
    """Why a contact was arranged, for a date the plan asked about: a date
    `date_detail` was called on. The first statement on that date is given."""
    dates = {r["date"] for r in results if r["function"] == "date_detail"}
    if not dates:
        return None
    for result in results:
        if result["function"] != "observations":
            continue
        rows = [r for r in result["rows"] if r["topic"] == "reason_for_contact" and r["date"] in dates]
        if rows:
            row = rows[0]
            return f"Why the contact on {day(row['date'])} was arranged ({row['document']} line {row['line']}, {words(row['speaker'])}): \"{row['quote']}\""
    return None


def open_point(results) -> str | None:
    """The first open disagreement the figures depend on, and what it does."""
    for result in results:
        if result["function"] == "conflicts_and_findings":
            continue
        for conflict in result.get("conflicts", []):
            encounter = conflict["conflict_id"].split("/")[-1].split(":")[0]
            values = " or ".join(f"{a['value']} ({', '.join(a.get('documents') or [])})" for a in conflict["alternatives"])
            row = next(
                (r for other in results for r in other.get("contributed", []) + other.get("contacts", []) if isinstance(r, dict) and r.get("contact_id") == conflict["contact_id"]),
                None,
            )
            text = f"One point is open: the {conflict['field']} of {encounter}" + (f" on {day(row['date'])}" if row else "") + f", {values}"
            if row and row.get("minutes"):
                text += f", which makes its minutes {either(row['minutes'])}"
            goal = next((r for r in results if r["function"] == "goal_status"), None)
            week = next((w for w in goal["weeks"] if conflict["conflict_id"] in w["depends_on"]), None) if goal else None
            totals = next((r["totals"] for r in results if r["function"] == "care_delivered" and r.get("totals")), None)
            if week:
                text += f" and the week {span(week['start'], week['end'])} {either(week['minutes'])}, so that week cannot be determined"
            elif totals and len({t["minutes"] for t in totals}) > 1:
                text += f" and the total {either(sorted({t['minutes'] for t in totals}))}"
            return text + "."
    return None


def _exclusion_that_matters(results) -> str | None:
    rows = []
    findings = {}
    for result in results:
        for finding in result.get("findings", []):
            findings.setdefault(finding["contact_id"], []).append(finding)
        for row in result.get("excluded", []) + [r for r in result.get("rows", []) if isinstance(r, dict) and r.get("record_kind") == "encounter" and "why_not" in r] + [r for r in result.get("contacts", []) if isinstance(r, dict) and r.get("record_kind") == "encounter" and not r.get("counts")]:
            rows.append(row)
            for finding in row.get("findings", []):
                findings.setdefault(row["contact_id"], []).append(finding)
    if not rows:
        return None

    def rank(row):
        kinds = {f["kind"] for f in findings.get(row["contact_id"], [])}
        return (
            0 if "charge_without_attendance" in kinds else 1,
            0 if row["status"] == "held_without_patient" else 1,
            -(row.get("minutes_without_patient") or 0),
            -(max(row["minutes"]) if row["minutes"] else 0),
            row["date"] or "",
        )

    row = min(rows, key=rank)
    kinds = {f["kind"] for f in findings.get(row["contact_id"], [])}
    status = STATUS_WORDS.get(row["status"], row["status"])
    text = f"Not counted: {row['encounter'] or row['date']} on {day(row['date'])}, {words(row['class'])}, {status}"
    if "charge_without_attendance" in kinds:
        text += "; a charge is posted for it and a draft note says attended, and neither can establish attendance"
    elif row.get("minutes_without_patient"):
        text += f"; its {row['minutes_without_patient']} minutes were without the patient"
    elif row["minutes"]:
        text += f"; its {either(row['minutes'])} minutes are in a class the plan does not count"
    return text + "."


# --------------------------------------------------------------------------
# The nine parts
# --------------------------------------------------------------------------


def contacts_used(results) -> set[str]:
    """The contacts the figures of these results rest on or set aside."""
    used = set()
    for result in results:
        if result["function"] == "conflicts_and_findings":
            continue
        for row in result.get("contributed", []) + result.get("excluded", []) + result.get("contacts", []) + result.get("rows", []):
            if isinstance(row, dict) and row.get("contact_id"):
                used.add(row["contact_id"])
        for week in result.get("weeks", []):
            used.update(week.get("contacts", []))
    return used


def narrowed(result, used: set[str]) -> dict:
    """A supporting `conflicts_and_findings` result cut to the contacts the
    other results used. A question about scores and statements uses none, so
    it gets none (Discussion 32, defect 5)."""
    keep = lambda row: row.get("contact_id") in used  # noqa: E731
    return {**result, "open": [r for r in result["open"] if keep(r)], "settled": [r for r in result["settled"] if keep(r)], "findings": [f for f in result["findings"] if keep(f)],
            "conflicts": [r for r in result["conflicts"] if keep(r)],
            "calculation": [f"{len([r for r in result['open'] if keep(r)])} open, {len([r for r in result['settled'] if keep(r)])} settled, {len([f for f in result['findings'] if keep(f)])} findings, on the contacts behind these figures"]}


def parts_from_results(understood, plan, results, not_read_lines) -> dict:
    parts = {"1. the question as understood": understood}
    answer, figures, contributed, excluded, unsettled, assumptions = [], [], [], [], [], []
    blocks = []
    good = []
    assigned = roles(results)
    used = contacts_used(results)
    has_not_counted = any(r["function"] == "not_counted" and "error" not in r for r in results)
    depended = {c["conflict_id"] for r in results if r["function"] != "conflicts_and_findings" for c in r.get("conflicts", [])}
    from_conflicts = {}
    for result, role in zip(results, assigned):
        if "error" in result:
            answer.append(f"{result['function']}: {result['error']}")
            continue
        if result["function"] == "conflicts_and_findings" and role == "supporting":
            result = narrowed(result, used)
        block = WRITERS[result["function"]](result, plan)
        blocks.append((block, role))
        good.append(result)
        if role == "primary":
            answer += block["headline"] + block["aside"] + block["answer"]
        elif role == "breakdown":
            figures += [line if line.startswith("- ") else f"- {line}" for line in block["answer"]]
        else:
            excluded += block["headline"] if result["function"] == "not_counted" else []
        figures += block["figures"]
        contributed += block["contributed"]
        excluded += block["excluded"]
        if not (has_not_counted and result["function"] in ("care_delivered", "goal_status")):
            excluded += block["excluded_contacts"]
        if result["function"] == "conflicts_and_findings":
            for conflict_id, line in block["unsettled_by_id"].items():
                if conflict_id in depended or role == "primary":
                    from_conflicts[conflict_id] = line
                else:
                    # Open elsewhere in the record. Part 6 holds only what these figures depend on.
                    excluded.append(line.replace("- ", "- Open elsewhere in the record, not behind these figures: ", 1))
        else:
            unsettled += block["unsettled"]
        assumptions += block["assumptions"]
    for result in good:
        if result["function"] != "conflicts_and_findings":
            for conflict in result.get("conflicts", []):
                unsettled.append(from_conflicts.get(conflict["conflict_id"]) or f"- {conflict_words(conflict)}. What would settle it: {conflict['would_settle']}")
    for conflict_id, line in from_conflicts.items():
        if conflict_id not in depended:
            unsettled.append(line)
    answer += progress_block(good)
    seen = set()
    parts["2. the answer"] = dedupe(answer) or ["No result."]
    parts["3. figures"] = dedupe(figures) or ["None."]
    parts["4. what contributed"] = dedupe(contributed) or ["Nothing."]
    parts["5. what was excluded"] = dedupe(excluded) or ["Nothing."]
    parts["6. not settled"] = dedupe(unsettled) or ["Nothing."]
    standard = ["The figures cover the documented record. A date with no document is counted as a date with no contact, and is named where it falls in the period."]
    parts["7. assumptions"] = standard + [a for a in assumptions if not (a in seen or seen.add(a))]
    parts["8. documents not read"] = not_read_lines
    parts["in short"] = lead(blocks, parts, good)
    return parts


def render(built: dict) -> str:
    lines = [f"# {built.get('question_id') or 'Question'}", "", f"> {built['question']}", ""]
    short = built["parts"].get("in short")
    if short:
        lines += ["**In short.** " + " ".join(short), ""]
    for name, content in built["parts"].items():
        if name == "in short":
            continue
        lines += [f"## {name[0]}. {name[3:].capitalize()}", ""]
        lines += content
        lines.append("")
    return "\n".join(lines)
