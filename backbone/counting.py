"""Counts minutes, days, weeks and goal verdicts, carrying alternatives
(piece 6 of the build list).

Everything here is code. The thresholds, the counted classes, the week and the
episode are read from the patient's plan. None is written here.

The rules applied in this file:

     2  a contact belongs to the week of its service date
     4  any counted minutes make a session and a therapy day
    12  a verdict is "met" only if every alternative meets the requirement,
        "not met" only if none does, and "cannot determine" otherwise
"""

from __future__ import annotations

import itertools
from collections import defaultdict
from datetime import date, timedelta

WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

MET = "met"
NOT_MET = "not_met"
CANNOT_DETERMINE = "cannot_determine"
NO_PLAN = "no_plan"


def day(text: str) -> date:
    return date.fromisoformat(text)


def plans(plan_rules: list[dict]) -> list[dict]:
    """One plan for each plan document, in the shape the counting needs."""
    by_document = defaultdict(list)
    for row in plan_rules:
        by_document[row["doc_hash"]].append(row)
    result = []
    for doc_hash, rows in sorted(by_document.items()):
        plan = {
            "doc_hash": doc_hash,
            "document": rows[0]["value"].get("document"),
            "signed": rows[0]["value"].get("signed"),
            "start": rows[0]["effective_from"],
            "end": rows[0]["effective_to"],
            "requirements": [],
            "week_starts_on": None,
            "day_classes": set(),
            "counted_classes": set(),
            "excluded_classes": set(),
            "goals": [],
            "sources": {},
        }
        for row in rows:
            value = row["value"]
            rule = row["rule"]
            plan["sources"].setdefault(rule, []).append(row["claim_id"])
            if rule == "requirement" and value.get("minimum") is not None:
                plan["requirements"].append(
                    {
                        "measure": value.get("measure"),
                        "minimum": value["minimum"],
                        "period": value.get("period"),
                        "claim": row["claim_id"],
                    }
                )
            elif rule == "week_definition":
                plan["week_starts_on"] = value.get("week_starts_on")
            elif rule == "therapy_day_definition":
                plan["day_classes"] |= set(value.get("service_classes", []))
            elif rule == "counted_service":
                plan["counted_classes"] |= set(value.get("service_classes", []))
            elif rule == "excluded_service":
                plan["excluded_classes"] |= set(value.get("service_classes", []))
            elif rule == "clinical_goal":
                plan["goals"].append({"number": value.get("goal_number"), "text": value.get("text"), "claim": row["claim_id"]})
        # Where a plan names the counted classes and gives no separate list for
        # a therapy day, or the reverse, the one list serves for both.
        plan["counted_classes"] = plan["counted_classes"] or set(plan["day_classes"])
        plan["day_classes"] = plan["day_classes"] or set(plan["counted_classes"])
        plan["counted_classes"] -= plan["excluded_classes"]
        plan["day_classes"] -= plan["excluded_classes"]
        plan["requirements"].sort(key=lambda entry: (str(entry["measure"]), entry["minimum"]))
        plan["goals"].sort(key=lambda entry: (entry["number"] is None, entry["number"]))
        result.append(plan)
    return result


def plan_for(all_plans: list[dict], on: str) -> dict | None:
    """The plan in effect on a date. With more than one, the one that took
    effect last. Which plan governs a week that holds a change is open (O-13)."""
    fitting = [
        plan
        for plan in all_plans
        if plan["start"] and plan["end"] and plan["start"] <= on <= plan["end"]
    ]
    if not fitting:
        return None
    return max(fitting, key=lambda plan: (plan["start"], plan["signed"] or "", plan["doc_hash"]))


def week_of(on: str, starts_on: str | None) -> tuple[str, str]:
    """Rule 2: the week a service date falls in."""
    first = WEEKDAYS.index(starts_on or "monday")
    current = day(on)
    start = current - timedelta(days=(current.weekday() - first) % 7)
    return start.isoformat(), (start + timedelta(days=6)).isoformat()


def counts(contact: dict, plan: dict | None) -> tuple[bool, str]:
    """Whether a contact counts toward the goal, and why not when it does not.
    This is worked out each time from the plan and is never stored (R-20)."""
    if contact["record_kind"] != "encounter":
        return False, "an administrative record, not an encounter"
    if contact["patient_present"] == "no":
        return False, {
            "no_show": "no-show",
            "cancelled_by_patient": "cancelled by the patient",
            "cancelled_by_clinic": "cancelled by the clinic",
            "held_without_patient": "held with the patient absent",
            "absent": "the patient was absent",
            "not_established": "attendance is not established",
        }.get(contact["status"], contact["status"])
    if plan is None:
        return False, "no plan is in effect on that date"
    if contact["service_class"] in plan["excluded_classes"]:
        return False, "a class of service the plan excludes"
    if contact["service_class"] not in plan["counted_classes"]:
        return False, "a class of service the plan does not count"
    return True, ""


def scenarios(contacts: list[dict]) -> list[dict]:
    """Every way the open conflicts behind these contacts could be settled.

    Each scenario is a choice for each open conflict. With nothing open there
    is one scenario, with no choices in it.
    """
    options: dict[str, set] = defaultdict(set)
    for contact in contacts:
        for entry in contact["minutes"]:
            for conflict, value in entry["choices"].items():
                options[conflict].add(value)
    names = sorted(options)
    return [dict(zip(names, chosen)) for chosen in itertools.product(*(sorted(options[name]) for name in names))]


def under(contact: dict, scenario: dict) -> dict | None:
    """The contact's minutes under one scenario."""
    for entry in contact["minutes"]:
        if all(scenario.get(conflict) == value for conflict, value in entry["choices"].items()):
            return entry
    return None


def tally(contacts: list[dict], plan_of) -> list[dict]:
    """Sessions, days and minutes of the contacts that count, for each scenario.

    `plan_of` gives the plan in effect on a date.
    """
    counted = [contact for contact in contacts if counts(contact, plan_of(contact["service_date"]))[0]]
    rows = []
    for scenario in scenarios(counted):
        sessions, dates, minutes, unknown = [], set(), 0, []
        by_class: dict[str, dict] = defaultdict(lambda: {"sessions": 0, "minutes": 0})
        for contact in counted:
            entry = under(contact, scenario)
            if entry is None or not entry["present"]:
                continue
            sessions.append(contact["contact_id"])
            plan = plan_of(contact["service_date"])
            if contact["service_class"] in plan["day_classes"]:
                dates.add(contact["service_date"])
            by_class[contact["service_class"]]["sessions"] += 1
            if entry["minutes"] is None:
                unknown.append(contact["contact_id"])
                continue
            minutes += entry["minutes"]
            by_class[contact["service_class"]]["minutes"] += entry["minutes"]
        rows.append(
            {
                "choices": scenario,
                "sessions": len(sessions),
                "contacts": sorted(sessions),
                "days": len(dates),
                "dates": sorted(dates),
                "minutes": minutes,
                "hours": round(minutes / 60, 2),
                "minutes_unknown_for": sorted(unknown),
                "by_class": {name: dict(values) for name, values in sorted(by_class.items())},
            }
        )
    return rows


def verdict(rows: list[dict], requirements: list[dict]) -> tuple[str, list[dict]]:
    """Rule 12, over every scenario."""
    if not requirements:
        return CANNOT_DETERMINE, []
    outcomes, margins = [], []
    for row in rows:
        margin = {"choices": row["choices"]}
        results = []
        for requirement in requirements:
            measure = {"therapy_days": "days", "minutes": "minutes", "sessions": "sessions"}.get(requirement["measure"])
            if measure is None:
                results.append(None)
                continue
            margin[measure] = row[measure] - requirement["minimum"]
            if row[measure] >= requirement["minimum"]:
                results.append(True)
            elif measure == "minutes" and row["minutes_unknown_for"]:
                # Minutes that are not known could only add to the total.
                results.append(None)
            else:
                results.append(False)
        outcomes.append(False if False in results else (None if None in results else True))
        margins.append(margin)
    if all(outcome is True for outcome in outcomes):
        return MET, margins
    if all(outcome is False for outcome in outcomes):
        return NOT_MET, margins
    return CANNOT_DETERMINE, margins


def documented_dates(contacts: list[dict], sections: dict) -> set[str]:
    """Dates the record says something about: a contact falls on it, a document
    is dated on it, or the view of a schedule export covers it (D-31)."""
    dates = {contact["service_date"] for contact in contacts if contact["service_date"]}
    for section in sections.values():
        view = {}
        for entry in section.get("dates", []):
            if not entry.get("date"):
                continue
            dates.add(entry["date"])
            if entry["kind"] in ("period_start", "period_end"):
                view[entry["kind"]] = entry["date"]
        if section["kind"] == "schedule_export" and len(view) == 2:
            current, last = day(view["period_start"]), day(view["period_end"])
            while current <= last:
                dates.add(current.isoformat())
                current += timedelta(days=1)
    return dates


def weekly_status(contacts: list[dict], plan_rules: list[dict], sections: dict) -> list[dict]:
    """One row for each week of each plan's episode."""
    all_plans = plans(plan_rules)
    documented = documented_dates(contacts, sections)
    rows = {}
    for plan in all_plans:
        if not plan["start"] or not plan["end"]:
            continue
        weekly = [entry for entry in plan["requirements"] if entry["period"] == "week"]
        start, _ = week_of(plan["start"], plan["week_starts_on"])
        while start <= plan["end"]:
            end = (day(start) + timedelta(days=6)).isoformat()
            low, high = max(start, plan["start"]), min(end, plan["end"])
            inside = [
                contact
                for contact in contacts
                if contact["service_date"]
                and low <= contact["service_date"] <= high
                and plan_for(all_plans, contact["service_date"]) is plan
            ]
            tallies = tally(inside, lambda on: plan_for(all_plans, on))
            outcome, margins = verdict(tallies, weekly)
            conflicts = sorted({conflict for row in tallies for conflict in row["choices"]})
            every_day = [(day(start) + timedelta(days=offset)).isoformat() for offset in range(7)]
            rows[start] = {
                "week_start": start,
                "week_end": end,
                "requirement": {
                    "plan": plan["document"],
                    "requirements": weekly,
                    "week_starts_on": plan["week_starts_on"],
                    "counted_classes": sorted(plan["counted_classes"]),
                    "excluded_classes": sorted(plan["excluded_classes"]),
                },
                "days": [{"days": row["days"], "dates": row["dates"], "choices": row["choices"]} for row in tallies],
                "minutes": [
                    {
                        "minutes": row["minutes"],
                        "hours": row["hours"],
                        "choices": row["choices"],
                        "unknown_for": row["minutes_unknown_for"],
                        "by_class": row["by_class"],
                    }
                    for row in tallies
                ],
                "verdict": outcome,
                "margin": margins,
                # D-14: a week that runs past the episode is judged in full, and labelled.
                "partial": start < plan["start"] or end > plan["end"],
                "conflicts": conflicts,
                "contacts": sorted({contact for row in tallies for contact in row["contacts"]}),
                "undocumented": [on for on in every_day if on not in documented],
            }
            start = (day(start) + timedelta(days=7)).isoformat()
    return [rows[start] for start in sorted(rows)]


def totals(contacts: list[dict], plan_rules: list[dict], start: str, end: str) -> list[dict]:
    """Sessions, days and minutes between two dates, for each scenario."""
    all_plans = plans(plan_rules)
    inside = [c for c in contacts if c["service_date"] and start <= c["service_date"] <= end]
    return tally(inside, lambda on: plan_for(all_plans, on))
