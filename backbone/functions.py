"""The nine functions a question is answered with (R-18).

Each takes a patient and, where it applies, a period, and returns rows, the
calculation, the sources, and the open conflicts it depends on. They read the
saved abstraction and call no model, so they can be run directly (R-9).

    care_delivered        sessions, days, minutes and hours, grouped
    goal_status           the requirement in effect, totals, verdict and margin per week
    date_detail           everything known about one date, and what each document contributed
    assessments           distinct questionnaires and scores, with copies excluded
    observations          what was said about a topic, by whom, in date order
    not_counted           contacts and documents that did not count, with the reason
    conflicts_and_findings  what is unsettled, the alternatives, and what would settle it
    patients_below_goal   patients with consecutive weeks below the goal
    compare_periods       types and amounts of care in two periods
"""

from __future__ import annotations

from collections import defaultdict
from datetime import date, timedelta

from . import counting, quotes, store

CATALOGUE = {
    "care_delivered": {
        "arguments": {"patient": "patient", "start": "date", "end": "date", "group_by": "week | class | day | clinician"},
        "answers": "How many sessions, days, minutes and hours of therapy, in a period, grouped by week, class, day or clinician. Also the counts of encounters, of contacts held and of contacts with the patient present.",
    },
    "goal_status": {
        "arguments": {"patient": "patient", "start": "date", "end": "date"},
        "answers": "The goal in the plan, the plan itself and any change to it, and for each week the days, minutes, verdict and margin.",
    },
    "date_detail": {
        "arguments": {"patient": "patient", "date": "date"},
        "answers": "Everything known about one date: each contact, its status and minutes, and what each document says about it. Says when a date is not documented.",
    },
    "assessments": {
        "arguments": {"patient": "patient", "instrument": "text", "start": "date", "end": "date"},
        "answers": "The distinct questionnaire results with scores and dates, the change between them, and the copies and mentions that add none.",
    },
    "observations": {
        "arguments": {"patient": "patient", "topic": "one or more of mood, anxiety, sleep, safety, functioning, progress, reason_for_contact, medication, other, comma separated; leave out for all", "start": "date", "end": "date"},
        "answers": "What the notes say about the patient's condition on one or more topics, who said it, in date order, with the quote. One call covers several topics.",
    },
    "not_counted": {
        "arguments": {"patient": "patient", "start": "date", "end": "date"},
        "answers": "The contacts that did not count and why: no-shows, cancellations, contacts without the patient, excluded classes. The administrative records, and the documents that add no contact.",
    },
    "conflicts_and_findings": {
        "arguments": {"patient": "patient", "start": "date", "end": "date"},
        "answers": "Where documents disagree: the alternatives, whether a rule settled it, and what would settle it. Also the findings, such as a charge for a contact the patient missed. With dates, only the contacts in that period.",
    },
    "patients_below_goal": {
        "arguments": {"weeks": "number of consecutive weeks, default 2"},
        "answers": "Across the collection, the patients with that many consecutive weeks below the goal, and whether it depends on an open conflict.",
    },
    "compare_periods": {
        "arguments": {"patient": "patient", "first_start": "date", "first_end": "date", "second_start": "date", "second_end": "date"},
        "answers": "The types and amounts of care in two periods, side by side.",
    },
}

NOT_HELD = {"no_show", "cancelled_by_patient", "cancelled_by_clinic", "absent", "not_established"}


def words(text) -> str:
    return (text or "").replace("_", " ")


# --------------------------------------------------------------------------
# Shared pieces
# --------------------------------------------------------------------------


def patients_in(connection) -> list[dict]:
    rows = connection.execute(
        "SELECT patient_key, patient_name, patient_dob, COUNT(*) AS documents FROM documents"
        " WHERE patient_key IS NOT NULL GROUP BY patient_key, patient_name, patient_dob ORDER BY patient_key"
    ).fetchall()
    found = []
    for row in rows:
        rules = store.rows_of(connection, "plan_rules", row["patient_key"], "rule_id")
        plans = counting.plans(rules)
        found.append(
            {
                "patient": row["patient_key"],
                "name": row["patient_name"],
                "dob": row["patient_dob"],
                "documents": row["documents"],
                "episodes": [{"start": plan["start"], "end": plan["end"], "plan": plan["document"]} for plan in plans],
            }
        )
    return found


def resolve_patient(connection, asked: str | None) -> dict:
    """Who a question is about. Never falls through to another patient."""
    if not asked:
        return {"status": "none_named"}
    wanted = " ".join(asked.lower().split())
    everyone = patients_in(connection)
    exact = [p for p in everyone if p["patient"].lower() == wanted or (p["name"] or "").lower() == wanted]
    if len(exact) == 1:
        return {"status": "found", **exact[0]}
    parts = [p for p in everyone if wanted in (p["name"] or "").lower().split() or wanted in (p["name"] or "").lower()]
    if len(parts) == 1 and not exact:
        return {"status": "found", **parts[0]}
    if len(exact) > 1 or len(parts) > 1:
        return {"status": "several", "candidates": exact or parts}
    # A participant, such as a relative, is not a patient (P-2).
    appearances = []
    for row in connection.execute("SELECT * FROM contacts ORDER BY service_date, contact_id"):
        people = store.from_json(row["participants"]) or []
        if any(wanted == (person["name"] or "").lower() for person in people):
            appearances.append(
                {
                    "contact_id": row["contact_id"],
                    "patient": row["patient_key"],
                    "date": row["service_date"],
                    "class": row["service_class"],
                    "role": next(person["role"] for person in people if wanted == (person["name"] or "").lower()),
                }
            )
    if appearances:
        return {"status": "participant", "name": asked, "appearances": appearances}
    return {"status": "not_found", "name": asked}


def citations(connection, claim_ids) -> list[dict]:
    """The source lines behind claims, each checked again against the text."""
    result = []
    for claim_id in sorted(set(claim_ids)):
        row = connection.execute(
            "SELECT c.claim_id, c.type, c.line, c.quote, c.quote_status, d.declared_id, d.file_name, d.text"
            " FROM claims c JOIN documents d USING (doc_hash) WHERE c.claim_id = ?",
            (claim_id,),
        ).fetchone()
        if row is None:
            continue
        lines = quotes.split_lines(row["text"])
        at_line = 1 <= (row["line"] or 0) <= len(lines) and row["quote"] in lines[row["line"] - 1]
        result.append(
            {
                "claim": row["claim_id"],
                "type": row["type"],
                "document": row["declared_id"] or row["file_name"],
                "file": row["file_name"],
                "line": row["line"],
                "quote": row["quote"],
                "verified": bool(at_line),
            }
        )
    return result


def not_read(connection, patient: str) -> list[dict]:
    """Documents of the patient that failed to read (R-10). A document that
    failed has no patient recorded, so every failed document is listed."""
    rows = connection.execute(
        "SELECT file_name, declared_id, read_error FROM documents WHERE read_status = 'failed'"
        " AND (patient_key = ? OR patient_key IS NULL) ORDER BY file_name",
        (patient,),
    ).fetchall()
    return [{"file": row["file_name"], "document": row["declared_id"], "reason": row["read_error"]} for row in rows]


def _load(connection, patient: str) -> dict:
    rules = store.rows_of(connection, "plan_rules", patient, "rule_id")
    return {
        "copies": _copy_documents(connection, patient),
        "contacts": store.rows_of(connection, "contacts", patient, "service_date, contact_id"),
        "conflicts": store.rows_of(connection, "conflicts", patient, "conflict_id"),
        "findings": store.rows_of(connection, "findings", patient, "finding_id"),
        "assessments": store.rows_of(connection, "assessments", patient, "completed_date, assessment_id"),
        "weeks": store.rows_of(connection, "weekly_status", patient, "week_start"),
        "rules": rules,
        "plans": counting.plans(rules),
    }


def _period(data: dict, start, end) -> tuple[str | None, str | None, str]:
    """The period asked for, or the episode in the plan (D-20)."""
    if start and end:
        return start, end, "as asked"
    plans = data["plans"]
    if plans:
        return plans[0]["start"], plans[0]["end"], f"the episode in the plan {plans[0]['document']}"
    dates = [c["service_date"] for c in data["contacts"] if c["service_date"]]
    if dates:
        return min(dates), max(dates), "the dates of the record"
    return None, None, "no dates in the record"


def _contact_sources(connection, contact: dict) -> list[str]:
    """The claims a contact's status and minutes rest on."""
    ids = set()
    for option in contact["presence"]:
        ids.update(option.get("start_claims", []))
        ids.update(option.get("end_claims", []))
        if option.get("minutes_from"):
            ids.add(option["minutes_from"])
    for row in contact["removed"]:
        ids.add(row["claim"])
    marks = ",".join("?" * len(contact["claims"]))
    for row in connection.execute(
        f"SELECT claim_id, type FROM claims WHERE claim_id IN ({marks})", contact["claims"]
    ):
        if row["type"] in ("attendance", "contact", "stated_minutes", "correction", "charge"):
            ids.add(row["claim_id"])
    return sorted(ids)


def _open_conflicts(data: dict, contact_ids) -> list[dict]:
    wanted = set(contact_ids)
    return [c for c in data["conflicts"] if c["status"] == "open" and c["contact_id"] in wanted]


def _in(contact: dict, start, end) -> bool:
    return bool(contact["service_date"]) and (not start or start <= contact["service_date"]) and (not end or contact["service_date"] <= end)


def _copy_documents(connection, patient) -> set[str]:
    """The patient's documents that say they are copies of an earlier record.
    Worked out once per call, not once per contact."""
    found = set()
    for row in connection.execute("SELECT declared_id, file_name, sections FROM documents WHERE read_status = 'read' AND patient_key = ?", (patient,)):
        if any(section.get("is_copy") for section in store.from_json(row["sections"]) or []):
            found.add(row["declared_id"] or row["file_name"])
    return found


def _summary(connection, contact: dict, plan, copies: set[str] | None = None) -> dict:
    counted, why = counting.counts(contact, plan)
    if copies is None:
        copies = _copy_documents(connection, contact["patient_key"])
    return {
        "sources": _contact_sources(connection, contact),
        "copies": sorted(name for name in contact["documents"] if name in copies),
        "removed_rows": contact["removed"],
        "contact_id": contact["contact_id"],
        "encounter": contact["encounter_id"],
        "date": contact["service_date"],
        "class": contact["service_class"],
        "status": contact["status"],
        "partial": bool(contact["partial"]),
        "present": [[o["start"], o["end"]] for o in contact["presence"] if o.get("start")],
        "removed": sorted({(r["start"], r["end"]) for r in contact["removed"]}),
        "minutes": sorted({o["minutes"] for o in contact["minutes"] if o["minutes"] is not None}),
        "minutes_without_patient": contact["minutes_without_patient"],
        "clinicians": contact["clinicians"],
        "modality": contact["modality"],
        "counts": counted,
        "why_not": why,
        "notes": contact["notes"],
        "documents": contact["documents"],
    }


def _result(name, arguments, **parts) -> dict:
    return {"function": name, "arguments": arguments, **parts}


def _undocumented(data: dict, connection, patient, start, end) -> list[str]:
    sections = {}
    for row in connection.execute("SELECT doc_hash, sections FROM documents WHERE patient_key = ?", (patient,)):
        for section in store.from_json(row["sections"]) or []:
            sections[(row["doc_hash"], section["id"])] = section
    documented = counting.documented_dates(data["contacts"], sections)
    missing = []
    if start and end:
        current = date.fromisoformat(start)
        while current.isoformat() <= end:
            if current.isoformat() not in documented:
                missing.append(current.isoformat())
            current += timedelta(days=1)
    return missing


def _ranges(dates: list[str]) -> list[str]:
    """Dates as ranges, such as "2026-01-17 to 2026-01-18"."""
    out = []
    for on in dates:
        if out and (date.fromisoformat(out[-1][1]) + timedelta(days=1)).isoformat() == on:
            out[-1][1] = on
        else:
            out.append([on, on])
    return [a if a == b else f"{a} to {b}" for a, b in out]


# --------------------------------------------------------------------------
# 1. care_delivered
# --------------------------------------------------------------------------


def care_delivered(connection, patient, start=None, end=None, group_by=None):
    arguments = {"patient": patient, "start": start, "end": end, "group_by": group_by}
    data = _load(connection, patient)
    start, end, how = _period(data, start, end)
    plans = data["plans"]
    plan_of = lambda on: counting.plan_for(plans, on)  # noqa: E731
    inside = [c for c in data["contacts"] if _in(c, start, end)]
    totals = sorted(counting.tally(inside, plan_of), key=lambda row: row["minutes"])
    encounters = [c for c in inside if c["record_kind"] == "encounter"]
    counted = [c for c in encounters if counting.counts(c, plan_of(c["service_date"]))[0]]
    excluded = [c for c in encounters if not counting.counts(c, plan_of(c["service_date"]))[0]]
    counts = {
        "encounters": len(encounters),
        "held": sum(1 for c in encounters if c["status"] not in NOT_HELD),
        "with_patient_present": sum(1 for c in encounters if c["patient_present"] == "yes"),
        "therapy_sessions": sorted({row["sessions"] for row in totals}),
        "administrative_records": sum(1 for c in inside if c["record_kind"] != "encounter"),
    }

    groups = []
    if group_by == "week":
        seen = set()
        for contact in counted:
            week_start, week_end = counting.week_of(contact["service_date"], plans[0]["week_starts_on"] if plans else None)
            if week_start in seen:
                continue
            seen.add(week_start)
            members = [c for c in counted if counting.week_of(c["service_date"], plans[0]["week_starts_on"] if plans else None)[0] == week_start]
            rows = sorted(counting.tally(members, plan_of), key=lambda row: row["minutes"])
            groups.append({"group": f"{week_start} to {week_end}", "start": week_start, "end": week_end, "totals": rows})
    elif group_by == "day":
        for on in sorted({c["service_date"] for c in counted}):
            members = [c for c in counted if c["service_date"] == on]
            groups.append({"group": on, "totals": sorted(counting.tally(members, plan_of), key=lambda row: row["minutes"])})
    elif group_by == "class":
        for name in sorted({c["service_class"] for c in counted}):
            members = [c for c in counted if c["service_class"] == name]
            groups.append({"group": name, "totals": sorted(counting.tally(members, plan_of), key=lambda row: row["minutes"])})
    elif group_by == "clinician":
        names = sorted({name for c in counted for name in c["clinicians"]})
        for name in names:
            members = [c for c in counted if name in c["clinicians"]]
            groups.append({"group": name, "totals": sorted(counting.tally(members, plan_of), key=lambda row: row["minutes"])})

    calculation = []
    for row in totals:
        parts = [f"{c['encounter_id']} {counting.under(c, row['choices'])['minutes']}" for c in counted if counting.under(c, row["choices"]) and counting.under(c, row["choices"])["present"]]
        choice = ", ".join(f"{k.split('/')[-1]} = {v}" for k, v in row["choices"].items())
        calculation.append(
            f"{row['sessions']} sessions on {row['days']} days; minutes {' + '.join(p.split()[1] for p in parts)} = {row['minutes']}"
            + (f" ({choice})" if choice else "")
            + f"; hours {row['minutes']} / 60 = {row['hours']:.2f}"
        )
    sources = sorted({claim for c in counted for claim in _contact_sources(connection, c)})
    return _result(
        "care_delivered",
        arguments,
        period={"start": start, "end": end, "how": how},
        totals=totals,
        groups=groups,
        counts=counts,
        contributed=[_summary(connection, c, plan_of(c["service_date"]), data["copies"]) for c in counted],
        excluded=[_summary(connection, c, plan_of(c["service_date"]), data["copies"]) for c in excluded],
        calculation=calculation,
        sources=citations(connection, sources),
        conflicts=_open_conflicts(data, [c["contact_id"] for c in counted]),
        undocumented=_ranges(_undocumented(data, connection, patient, start, end)),
        not_read=not_read(connection, patient),
        plan={"document": plans[0]["document"], "counted_classes": sorted(plans[0]["counted_classes"])} if plans else None,
    )


# --------------------------------------------------------------------------
# 2. goal_status
# --------------------------------------------------------------------------


def goal_status(connection, patient, start=None, end=None):
    arguments = {"patient": patient, "start": start, "end": end}
    data = _load(connection, patient)
    start, end, how = _period(data, start, end)
    weeks = [w for w in data["weeks"] if (not end or w["week_start"] <= end) and (not start or w["week_end"] >= start)]
    rows = []
    for week in weeks:
        rows.append(
            {
                "week": f"{week['week_start']} to {week['week_end']}",
                "start": week["week_start"],
                "end": week["week_end"],
                "days": sorted({d["days"] for d in week["days"]}),
                "dates": week["days"][0]["dates"] if week["days"] else [],
                "minutes": sorted({m["minutes"] for m in week["minutes"]}),
                "hours": sorted({m["hours"] for m in week["minutes"]}),
                "verdict": week["verdict"],
                "margin": sorted(week["margin"], key=lambda m: m.get("minutes", 0)),
                "partial": bool(week["partial"]),
                "depends_on": week["conflicts"],
                "contacts": week["contacts"],
                "undocumented": _ranges(week["undocumented"]),
                "calculation": [
                    " + ".join(
                        str(counting.under(c, m["choices"])["minutes"])
                        for c in data["contacts"]
                        if c["contact_id"] in week["contacts"] and counting.under(c, m["choices"]) and counting.under(c, m["choices"])["present"]
                    )
                    + f" = {m['minutes']}"
                    for m in sorted(week["minutes"], key=lambda m: m["minutes"])
                ],
            }
        )
    plans = []
    for plan in data["plans"]:
        needs = [{"measure": r["measure"], "minimum": r["minimum"], "period": r["period"]} for r in plan["requirements"]]
        plans.append(
            {
                "document": plan["document"],
                "signed": plan["signed"],
                "episode": {"start": plan["start"], "end": plan["end"]},
                "requirements": needs,
                "week_starts_on": plan["week_starts_on"],
                "counted_classes": sorted(plan["counted_classes"]),
                "excluded_classes": sorted(plan["excluded_classes"]),
                "goals": plan["goals"],
                "sources": sorted({claim for claims in plan["sources"].values() for claim in claims}),
            }
        )
    counted_ids = sorted({c for w in weeks for c in w["contacts"]})
    counted = [c for c in data["contacts"] if c["contact_id"] in counted_ids]
    plan_of = lambda on: counting.plan_for(data["plans"], on)  # noqa: E731
    excluded = [c for c in data["contacts"] if c["record_kind"] == "encounter" and _in(c, start, end) and c["contact_id"] not in counted_ids]
    sources = sorted({claim for p in plans for claim in p["sources"]} | {claim for c in counted for claim in _contact_sources(connection, c)})
    return _result(
        "goal_status",
        arguments,
        period={"start": start, "end": end, "how": how},
        plans=plans,
        plan_changes=max(0, len(plans) - 1),
        weeks=rows,
        summary={verdict: sum(1 for w in rows if w["verdict"] == verdict) for verdict in ("met", "not_met", "cannot_determine")},
        contributed=[_summary(connection, c, plan_of(c["service_date"]), data["copies"]) for c in counted],
        excluded=[_summary(connection, c, plan_of(c["service_date"]), data["copies"]) for c in excluded],
        calculation=[f"{w['week']}: {'; '.join(w['calculation'])}" for w in rows],
        sources=citations(connection, sources),
        conflicts=_open_conflicts(data, counted_ids),
        not_read=not_read(connection, patient),
    )


# --------------------------------------------------------------------------
# 3. date_detail
# --------------------------------------------------------------------------


def date_detail(connection, patient, date: str):
    arguments = {"patient": patient, "date": date}
    data = _load(connection, patient)
    plan_of = lambda on: counting.plan_for(data["plans"], on)  # noqa: E731
    contacts = [c for c in data["contacts"] if c["service_date"] == date]
    rows = []
    for contact in contacts:
        summary = _summary(connection, contact, plan_of(date), data["copies"])
        by_document = defaultdict(list)
        marks = ",".join("?" * len(contact["claims"]))
        claims = connection.execute(
            f"SELECT c.*, d.declared_id, d.file_name, d.sections FROM claims c JOIN documents d USING (doc_hash)"
            f" WHERE c.claim_id IN ({marks}) ORDER BY c.claim_id",
            contact["claims"],
        ).fetchall()
        for claim in claims:
            section = next(
                (s for s in store.from_json(claim["sections"]) or [] if s["id"] == claim["section"]), {}
            )
            by_document[claim["declared_id"] or claim["file_name"]].append(
                {
                    "claim": claim["claim_id"],
                    "type": claim["type"],
                    "value": store.from_json(claim["value"]),
                    "label": claim["time_label"],
                    "line": claim["line"],
                    "quote": claim["quote"],
                    "kind": section.get("kind"),
                    "signed": section.get("signature"),
                    "copy": bool(section.get("is_copy")),
                }
            )
        effects = []
        for conflict in data["conflicts"]:
            if conflict["contact_id"] == contact["contact_id"]:
                effects.append(conflict)
        findings = [f for f in data["findings"] if f["contact_id"] == contact["contact_id"]]
        summary["documents_say"] = [
            {"document": name, "claims": found} for name, found in sorted(by_document.items())
        ]
        summary["conflicts"] = effects
        summary["findings"] = findings
        summary["record_kind"] = contact["record_kind"]
        rows.append(summary)

    encounters = [r for r in rows if r["record_kind"] == "encounter"]
    therapy = [r for r in encounters if r["counts"]]
    minutes = sorted(counting.tally([c for c in contacts], plan_of), key=lambda row: row["minutes"])
    dated = connection.execute(
        "SELECT declared_id, file_name, sections FROM documents WHERE patient_key = ? ORDER BY declared_id", (patient,)
    ).fetchall()
    documents_dated = []
    covered_by_view = []
    for row in dated:
        for section in store.from_json(row["sections"]) or []:
            view = {e["kind"]: e["date"] for e in section["dates"] if e["kind"] in ("period_start", "period_end")}
            if section["kind"] == "schedule_export" and len(view) == 2 and view["period_start"] <= date <= view["period_end"]:
                covered_by_view.append(row["declared_id"] or row["file_name"])
            for entry in section["dates"]:
                if entry["date"] == date and entry["kind"] != "service":
                    documents_dated.append({"document": row["declared_id"] or row["file_name"], "kind": entry["kind"], "quote": entry["quote"], "line": entry["line"]})
    if contacts:
        coverage = "documented"
    elif covered_by_view:
        coverage = "no_appointment_in_schedule"
    elif documents_dated:
        coverage = "document_dated_only"
    else:
        coverage = "not_documented"
    sources = sorted({claim for c in contacts for claim in _contact_sources(connection, c)})
    return _result(
        "date_detail",
        arguments,
        date=date,
        coverage=coverage,
        covered_by_schedule=sorted(set(covered_by_view)),
        documents_dated=documents_dated,
        contacts=rows,
        counts={"contacts": len(encounters), "therapy_contacts": len(therapy), "administrative_records": len(rows) - len(encounters)},
        totals=minutes,
        calculation=[
            " + ".join(str(counting.under(c, m["choices"])["minutes"]) for c in contacts if counting.under(c, m["choices"]) and counting.under(c, m["choices"])["present"] and counting.counts(c, plan_of(date))[0]) + f" = {m['minutes']}"
            for m in minutes
        ],
        sources=citations(connection, sources),
        conflicts=_open_conflicts(data, [c["contact_id"] for c in contacts]),
        not_read=not_read(connection, patient),
    )


# --------------------------------------------------------------------------
# 4. assessments
# --------------------------------------------------------------------------


def assessments(connection, patient, instrument=None, start=None, end=None, on=None):
    arguments = {"patient": patient, "instrument": instrument, "start": start, "end": end, "on": on}
    data = _load(connection, patient)
    found = data["assessments"]
    if instrument:
        wanted = "".join(ch for ch in instrument.upper() if ch.isalnum())
        found = [a for a in found if "".join(ch for ch in a["instrument"].upper() if ch.isalnum()) == wanted]
    if start or end:
        found = [a for a in found if a["completed_date"] and (not start or a["completed_date"] >= start) and (not end or a["completed_date"] <= end)]
    everything = found
    if on:
        found = [a for a in everything if a["completed_date"] == on]

    def dates_of(claim_id):
        row = connection.execute(
            "SELECT d.declared_id, d.file_name, d.sections, c.section FROM claims c JOIN documents d USING (doc_hash) WHERE c.claim_id = ?",
            (claim_id,),
        ).fetchone()
        section = next((s for s in store.from_json(row["sections"]) or [] if s["id"] == row["section"]), {})
        return row["declared_id"] or row["file_name"], [{"kind": e["kind"], "date": e["date"]} for e in section.get("dates", [])]

    rows = []
    for a in found:
        copies = []
        for claim_id in a["copies"]:
            document, dates = dates_of(claim_id)
            copies.append({"claim": claim_id, "document": document, "dates": dates})
        mentions = []
        for claim_id in a["mentions"]:
            document, dates = dates_of(claim_id)
            mentions.append({"claim": claim_id, "document": document, "dates": dates})
        rows.append(
            {
                "instrument": a["instrument"],
                "completed_date": a["completed_date"],
                "completed_time": a["completed_time"],
                "score": a["score"],
                "form_id": a["form_id"],
                "items": a["items"] or {},
                "sources": a["claims"],
                "copies": copies,
                "mentions": mentions,
            }
        )
    changes = []
    for earlier, later in zip(everything, everything[1:]):
        if earlier["score"] and later["score"] and len(earlier["score"]) == 1 and len(later["score"]) == 1:
            changes.append({"from": earlier["completed_date"], "to": later["completed_date"], "change": later["score"][0] - earlier["score"][0]})
    overall = None
    if len(everything) >= 2 and everything[0]["score"] and everything[-1]["score"]:
        overall = everything[-1]["score"][0] - everything[0]["score"][0]
    received_on = []
    if on:
        for a in everything:
            for claim_id in a["copies"] + a["mentions"]:
                document, dates = dates_of(claim_id)
                if any(d["date"] == on for d in dates):
                    received_on.append({"document": document, "of": {"instrument": a["instrument"], "completed_date": a["completed_date"], "score": a["score"]}, "dates": dates})
    sources = sorted({c for a in found for c in a["claims"] + a["copies"] + a["mentions"]})
    inside = [c for c in data["contacts"] if c["record_kind"] == "encounter" and (not start or not end or _in(c, start, end))]
    attendance = {}
    for contact in inside:
        attendance[contact["status"]] = attendance.get(contact["status"], 0) + 1
    # Contacts held without the patient, leaving out care coordination, which
    # is between professionals by its nature and says nothing about engagement.
    absent_from = sum(1 for c in inside if c["status"] == "held_without_patient" and c["service_class"] != "care_coordination")
    return _result(
        "assessments",
        arguments,
        rows=rows,
        distinct=len(found),
        held_classes=sorted({c["service_class"] for c in inside if c["patient_present"] == "yes"}),
        attendance=attendance,
        absent_from=absent_from,
        changes=changes,
        overall_change=overall,
        received_on=received_on,
        instruments=sorted({a["instrument"] for a in data["assessments"]}),
        calculation=[f"{c['from']} to {c['to']}: {c['change']:+d}" for c in changes] + ([f"overall {overall:+d}"] if overall is not None else []),
        sources=citations(connection, sources),
        conflicts=[c for c in data["conflicts"] if c["status"] == "open" and c["field"] == "score"],
        not_read=not_read(connection, patient),
    )


# --------------------------------------------------------------------------
# 5. observations
# --------------------------------------------------------------------------


def observations(connection, patient, topic=None, start=None, end=None, speaker=None):
    arguments = {"patient": patient, "topic": topic, "start": start, "end": end, "speaker": speaker}
    data = _load(connection, patient)
    rows = connection.execute(
        "SELECT c.*, d.declared_id, d.file_name, d.sections FROM claims c JOIN documents d USING (doc_hash)"
        " WHERE c.patient_key = ? AND c.type = 'observation' AND c.valid = 1 AND c.quote_status != 'unverified'"
        " ORDER BY c.claim_id",
        (patient,),
    ).fetchall()
    found = []
    seen = set()
    copies = drafts = 0
    wanted = {t.strip() for t in topic.split(",") if t.strip()} if topic and topic.strip() != "all" else set()
    for row in rows:
        value = store.from_json(row["value"])
        section = next((s for s in store.from_json(row["sections"]) or [] if s["id"] == row["section"]), {})
        if section.get("is_copy"):
            copies += 1
            continue  # A copy carries its original's statements (rule 9).
        if section.get("kind") == "draft_note":
            drafts += 1
            continue  # Template text says nothing about the patient.
        if wanted and value.get("topic") not in wanted:
            continue
        if speaker and value.get("speaker") != speaker:
            continue
        on = value.get("date") or row["service_date"]
        if (start and (not on or on < start)) or (end and (not on or on > end)):
            continue
        key = (on, value.get("speaker"), value.get("topic"), " ".join(row["quote"].lower().split()))
        if key in seen:
            continue  # The same words, from the same speaker, on the same date.
        seen.add(key)
        found.append(
            {
                "date": on,
                "speaker": value.get("speaker"),
                "speaker_name": value.get("speaker_name"),
                "topic": value.get("topic"),
                "summary": value.get("summary"),
                "quote": row["quote"],
                "document": row["declared_id"] or row["file_name"],
                "line": row["line"],
                "claim": row["claim_id"],
                "contact": row["encounter_id"],
            }
        )
    found.sort(key=lambda r: (r["date"] or "", r["document"], r["line"], r["claim"]))
    order = ["mood", "anxiety", "sleep", "safety", "functioning", "progress", "reason_for_contact", "medication", "other"]
    topics = defaultdict(int)
    for row in found:
        topics[row["topic"]] += 1
    return _result(
        "observations",
        arguments,
        rows=found,
        by_topic={name: topics[name] for name in order if name in topics},
        copies_left_out=copies,
        drafts_left_out=drafts,
        calculation=[f"{len(found)} statements" + (f" on {topic}" if topic else "") + ", in date order"],
        sources=citations(connection, [r["claim"] for r in found]),
        conflicts=[],
        not_read=not_read(connection, patient),
    )


# --------------------------------------------------------------------------
# 6. not_counted
# --------------------------------------------------------------------------


def not_counted(connection, patient, start=None, end=None):
    arguments = {"patient": patient, "start": start, "end": end}
    data = _load(connection, patient)
    start, end, how = _period(data, start, end)
    plan_of = lambda on: counting.plan_for(data["plans"], on)  # noqa: E731
    inside = [c for c in data["contacts"] if _in(c, start, end)]
    rows = []
    for contact in inside:
        counted, why = counting.counts(contact, plan_of(contact["service_date"]))
        if counted:
            continue
        summary = _summary(connection, contact, plan_of(contact["service_date"]), data["copies"])
        summary["record_kind"] = contact["record_kind"]
        summary["reason"] = why
        # The reason a document gives for a missed appointment.
        marks = ",".join("?" * len(contact["claims"]))
        reasons = connection.execute(
            f"SELECT claim_id, value, quote FROM claims WHERE claim_id IN ({marks}) AND type = 'attendance'", contact["claims"]
        ).fetchall()
        summary["reasons_given"] = sorted(
            {store.from_json(r["value"]).get("reason") for r in reasons if store.from_json(r["value"]).get("reason")}
        )
        rows.append(summary)
    missed = [r for r in rows if r["status"] in ("no_show", "cancelled_by_patient", "cancelled_by_clinic")]
    documents = []
    for row in connection.execute(
        "SELECT declared_id, file_name, kinds, doc_hash FROM documents WHERE patient_key = ? AND read_status = 'read' ORDER BY declared_id",
        (patient,),
    ):
        in_contact = any(row["declared_id"] in c["documents"] for c in data["contacts"] if c["record_kind"] == "encounter")
        if not in_contact:
            documents.append({"document": row["declared_id"], "file": row["file_name"], "kinds": store.from_json(row["kinds"])})
    by_reason = defaultdict(list)
    for row in rows:
        by_reason[row["reason"]].append(row["encounter"] or row["date"])
    sources = sorted({claim for r in rows for claim in r["sources"]})
    return _result(
        "not_counted",
        arguments,
        period={"start": start, "end": end, "how": how},
        rows=rows,
        missed=missed,
        by_reason=dict(sorted(by_reason.items())),
        documents_without_encounter=documents,
        calculation=[f"{len([r for r in rows if r['record_kind'] == 'encounter'])} encounters did not count; {len(rows) - len([r for r in rows if r['record_kind'] == 'encounter'])} administrative records"],
        sources=citations(connection, sources),
        conflicts=[],
        not_read=not_read(connection, patient),
    )


# --------------------------------------------------------------------------
# 7. conflicts_and_findings
# --------------------------------------------------------------------------


def conflicts_and_findings(connection, patient, start=None, end=None):
    arguments = {"patient": patient, "start": start, "end": end}
    data = _load(connection, patient)
    contacts = {c["contact_id"]: c for c in data["contacts"]}

    def inside(contact_id):
        contact = contacts.get(contact_id)
        return contact is None or _in(contact, start, end)

    conflicts = sorted((c for c in data["conflicts"] if inside(c["contact_id"])), key=lambda c: (c["status"] != "open", c["conflict_id"]))
    rows = []
    for conflict in conflicts:
        contact = contacts.get(conflict["contact_id"])
        rows.append(
            {
                **conflict,
                "encounter": contact["encounter_id"] if contact else None,
                "date": contact["service_date"] if contact else None,
                "effect": (
                    f"minutes {' or '.join(str(m['minutes']) for m in sorted(contact['minutes'], key=lambda m: m['minutes'] if m['minutes'] is not None else -1))}"
                    if contact and conflict["status"] == "open"
                    else None
                ),
                "weeks_affected": [w["week_start"] for w in data["weeks"] if conflict["conflict_id"] in w["conflicts"]],
            }
        )
    findings = []
    for finding in data["findings"]:
        if not inside(finding["contact_id"]):
            continue
        contact = contacts.get(finding["contact_id"])
        findings.append({**finding, "encounter": contact["encounter_id"] if contact else None, "date": contact["service_date"] if contact else None})
    sources = sorted({c for row in rows for alt in row["alternatives"] for c in alt.get("claims", [])} | {c for f in findings for c in f["claims"]})
    return _result(
        "conflicts_and_findings",
        arguments,
        open=[r for r in rows if r["status"] == "open"],
        settled=[r for r in rows if r["status"] != "open"],
        findings=findings,
        calculation=[f"{len([r for r in rows if r['status'] == 'open'])} open, {len([r for r in rows if r['status'] != 'open'])} settled, {len(findings)} findings"],
        sources=citations(connection, sources),
        conflicts=[r for r in rows if r["status"] == "open"],
        not_read=not_read(connection, patient),
    )


# --------------------------------------------------------------------------
# 8. patients_below_goal
# --------------------------------------------------------------------------


def patients_below_goal(connection, weeks=2):
    arguments = {"weeks": weeks}
    rows = []
    for patient in patients_in(connection):
        status = store.rows_of(connection, "weekly_status", patient["patient"], "week_start")
        run, best, depends = [], [], False
        for week in status:
            if week["verdict"] in ("not_met", "cannot_determine"):
                run.append(week)
            else:
                run = []
            definite = [w for w in run if w["verdict"] == "not_met"]
            if len(definite) >= weeks and len(definite) > len(best):
                best, depends = list(definite), False
            elif len(run) >= weeks and len(best) < weeks:
                best, depends = list(run), any(w["verdict"] == "cannot_determine" for w in run)
        if len(best) >= weeks:
            rows.append(
                {
                    "patient": patient["patient"],
                    "name": patient["name"],
                    "weeks": [f"{w['week_start']} to {w['week_end']}" for w in best],
                    "verdicts": [w["verdict"] for w in best],
                    "depends_on_open_conflict": depends,
                    "conflicts": sorted({c for w in best for c in w["conflicts"]}) if depends else [],
                }
            )
    return _result(
        "patients_below_goal",
        arguments,
        rows=rows,
        patients_checked=len(patients_in(connection)),
        calculation=[f"{len(rows)} of {len(patients_in(connection))} patients with {weeks} consecutive weeks below the goal"],
        sources=[],
        conflicts=[],
        not_read=[d for p in patients_in(connection) for d in not_read(connection, p["patient"])],
    )


# --------------------------------------------------------------------------
# 9. compare_periods
# --------------------------------------------------------------------------


def compare_periods(connection, patient, first_start, first_end, second_start, second_end):
    arguments = {"patient": patient, "first_start": first_start, "first_end": first_end, "second_start": second_start, "second_end": second_end}
    first = care_delivered(connection, patient, first_start, first_end, group_by="class")
    second = care_delivered(connection, patient, second_start, second_end, group_by="class")

    def shape(result):
        return {
            "period": result["period"],
            "sessions": sorted({r["sessions"] for r in result["totals"]}),
            "days": sorted({r["days"] for r in result["totals"]}),
            "minutes": sorted({r["minutes"] for r in result["totals"]}),
            "by_class": {g["group"]: {"sessions": sorted({t["sessions"] for t in g["totals"]}), "minutes": sorted({t["minutes"] for t in g["totals"]})} for g in result["groups"]},
        }

    a, b = shape(first), shape(second)
    difference = {
        "sessions": [y - x for x in a["sessions"] for y in b["sessions"]],
        "days": [y - x for x in a["days"] for y in b["days"]],
        "minutes": sorted({y - x for x in a["minutes"] for y in b["minutes"]}),
    }
    return _result(
        "compare_periods",
        arguments,
        first=a,
        second=b,
        difference=difference,
        calculation=[f"minutes {b['minutes']} less {a['minutes']} = {difference['minutes']}"],
        sources=first["sources"] + second["sources"],
        conflicts=first["conflicts"] + [c for c in second["conflicts"] if c not in first["conflicts"]],
        not_read=first["not_read"],
    )


FUNCTIONS = {
    "care_delivered": care_delivered,
    "goal_status": goal_status,
    "date_detail": date_detail,
    "assessments": assessments,
    "observations": observations,
    "not_counted": not_counted,
    "conflicts_and_findings": conflicts_and_findings,
    "patients_below_goal": patients_below_goal,
    "compare_periods": compare_periods,
}


def call(connection, name: str, arguments: dict) -> dict:
    """Runs one function by name, with only the arguments it takes."""
    if name not in FUNCTIONS:
        raise KeyError(f"no function named {name!r}")
    function = FUNCTIONS[name]
    allowed = function.__code__.co_varnames[1 : function.__code__.co_argcount]
    kept = {key: value for key, value in arguments.items() if key in allowed and value not in (None, "")}
    return function(connection, **kept)
