"""Stages 4 and 5 against the answer key (checks 12 and 13 of the build plan).

The store is filled from the saved results of the full read. No model is
called. The key is `answer_key.json`, copied by hand from `answer-key.md`.
"""

import json
import random
from pathlib import Path

import pytest

from backbone import counting, store
from conftest import replay

KEY = json.loads((Path(__file__).parent / "answer_key.json").read_text(encoding="utf-8"))
PATIENT = KEY["patient"]


@pytest.fixture(scope="module")
def rows(full_read):
    return {table: store.rows_of(full_read, table, PATIENT) for table in store.CONCLUDES_TABLES}


@pytest.fixture(scope="module")
def encounters(rows):
    return {row["encounter_id"]: row for row in rows["contacts"] if row["record_kind"] == "encounter"}


# ---- Section 2 of the key: plan rules -----------------------------------------


def test_the_plan_is_read_from_the_plan_document(rows):
    plan = counting.plans(rows["plan_rules"])
    assert len(plan) == 1
    plan, expected = plan[0], KEY["plan"]
    assert plan["document"] == expected["document"]
    assert (plan["start"], plan["end"]) == (expected["episode"]["start"], expected["episode"]["end"])
    assert plan["signed"] == expected["signed"]
    assert plan["week_starts_on"] == expected["week_starts_on"]
    needed = {entry["measure"]: (entry["minimum"], entry["period"]) for entry in plan["requirements"]}
    assert needed == {
        "therapy_days": (expected["days_required"], "week"),
        "minutes": (expected["minutes_required"], "week"),
    }
    assert sorted(plan["counted_classes"]) == expected["counted_classes"]
    assert sorted(plan["day_classes"]) == expected["counted_classes"]
    assert sorted(plan["excluded_classes"]) == expected["excluded_classes"]
    assert len(plan["goals"]) == expected["goals"]


# ---- Section 3 of the key: contacts (check 12) -------------------------------


def test_there_are_twenty_encounters(encounters):
    assert sorted(encounters) == [entry["encounter"] for entry in KEY["contacts"]]


@pytest.mark.parametrize("expected", KEY["contacts"], ids=lambda entry: entry["encounter"])
def test_each_encounter_matches_the_key(encounters, rows, expected):
    contact = encounters[expected["encounter"]]
    assert contact["service_date"] == expected["date"]
    assert contact["service_class"] == expected["class"]
    assert contact["status"] == expected["status"]
    assert bool(contact["partial"]) == expected["partial"]
    assert sorted([entry["start"], entry["end"]] for entry in contact["presence"]) == expected["present"]
    assert sorted({(row["start"], row["end"]) for row in contact["removed"]}) == [
        tuple(entry) for entry in expected["removed"]
    ]
    assert sorted(entry["minutes"] for entry in contact["minutes"]) == expected["minutes"]
    assert contact["minutes_without_patient"] == expected.get("minutes_without_patient")
    if "modality" in expected:
        assert contact["modality"] == expected["modality"]
    plan = counting.plan_for(counting.plans(rows["plan_rules"]), contact["service_date"])
    assert counting.counts(contact, plan)[0] == expected["counts"]


def test_the_counts_of_contacts(encounters, rows):
    plans = counting.plans(rows["plan_rules"])
    not_held = {"no_show", "cancelled_by_patient", "cancelled_by_clinic", "absent", "not_established"}
    found = {
        "encounters": len(encounters),
        "held": sum(1 for row in encounters.values() if row["status"] not in not_held),
        "with_patient_present": sum(1 for row in encounters.values() if row["patient_present"] == "yes"),
        "therapy_sessions": sum(
            1 for row in encounters.values() if counting.counts(row, counting.plan_for(plans, row["service_date"]))[0]
        ),
    }
    assert found == KEY["counts_of_contacts"]


def test_sessions_with_two_clinicians(encounters):
    found = {number: row["clinicians"] for number, row in encounters.items() if len(row["clinicians"]) > 1}
    assert found == KEY["clinicians"]


def test_administrative_records_are_kept_apart(rows):
    kept = [row for row in rows["contacts"] if row["record_kind"] == "administrative"]
    assert kept
    assert {row["service_class"] for row in kept} <= {"scheduling_contact", "questionnaire_review"}
    assert all(row["minutes"] == [] for row in kept)


# ---- Section 4 of the key: conflicts and findings ----------------------------


def test_the_three_conflicts(rows):
    assert len(rows["conflicts"]) == len(KEY["conflicts"])
    for expected in KEY["conflicts"]:
        found = [
            row
            for row in rows["conflicts"]
            if row["contact_id"] == f"{PATIENT}/{expected['encounter']}" and row["field"] == expected["field"]
        ]
        assert len(found) == 1, expected["id"]
        conflict = found[0]
        assert conflict["status"] == expected["status"], expected["id"]
        assert conflict["outcome"] == expected["outcome"], expected["id"]
        assert conflict["rule"] == expected["rule"], expected["id"]
        values = {entry["value"]: entry["documents"] for entry in conflict["alternatives"]}
        assert values == expected["values"], expected["id"]
        assert bool(conflict["would_settle"]) == (expected["status"] == "open")


def test_the_findings(rows):
    found = {(row["kind"], row["contact_id"]) for row in rows["findings"]}
    for expected in KEY["findings"]:
        wanted = (expected["kind"], f"{PATIENT}/{expected['encounter']}")
        if expected["required"]:
            assert wanted in found, expected["id"]
    allowed = {(entry["kind"], f"{PATIENT}/{entry['encounter']}") for entry in KEY["findings"]}
    assert found <= allowed, "a finding the key does not list"


def test_the_charge_finding_is_not_called_improper_billing(rows):
    finding = next(row for row in rows["findings"] if row["kind"] == "charge_without_attendance")
    assert "inconsistency between documentation and billing" in finding["detail"]
    assert "not a finding of improper billing" in finding["detail"]


# ---- Section 5 of the key: assessments ------------------------------------------


def test_the_three_assessments(rows):
    found = [
        {
            "instrument": row["instrument"],
            "completed_date": row["completed_date"],
            "completed_time": row["completed_time"],
            "score": row["score"],
            "form_id": row["form_id"],
            "items": row["items"] or {},
        }
        for row in rows["assessments"]
    ]
    expected = [
        {
            "instrument": entry["instrument"],
            "completed_date": entry["completed_date"],
            "completed_time": entry["completed_time"],
            "score": [entry["score"]],
            "form_id": entry["form_id"],
            "items": entry.get("items", {}),
        }
        for entry in KEY["assessments"]
    ]
    assert found == expected


# ---- Section 6 of the key: weekly status and totals (check 13) -----------------


@pytest.mark.parametrize("expected", KEY["weeks"], ids=lambda entry: entry["start"])
def test_each_week_matches_the_key(rows, expected):
    week = next(row for row in rows["weekly_status"] if row["week_start"] == expected["start"])
    assert week["week_end"] == expected["end"]
    assert {entry["days"] for entry in week["days"]} == {expected["days"]}
    assert all(entry["dates"] == expected["dates"] for entry in week["days"])
    assert sorted(entry["minutes"] for entry in week["minutes"]) == expected["minutes"]
    assert week["verdict"] == expected["verdict"]
    assert sorted(entry["minutes"] for entry in week["margin"]) == expected["margin_minutes"]
    assert {entry["days"] for entry in week["margin"]} == {expected["margin_days"]}
    assert bool(week["partial"]) == expected["partial"]
    assert week["undocumented"] == expected["undocumented"]
    depends = [f"{PATIENT}/{expected['depends_on']}:start"] if "depends_on" in expected else []
    assert week["conflicts"] == depends


def test_there_are_four_weeks(rows):
    assert [row["week_start"] for row in rows["weekly_status"]] == [entry["start"] for entry in KEY["weeks"]]


def test_hours_by_week(rows):
    found = [sorted(entry["hours"] for entry in row["minutes"]) for row in rows["weekly_status"]]
    assert found == KEY["hours_by_week"]


def test_the_totals_for_the_period(rows):
    totals = counting.totals(rows["contacts"], rows["plan_rules"], KEY["period"]["start"], KEY["period"]["end"])
    expected = KEY["totals"]
    assert {row["sessions"] for row in totals} == {expected["sessions"]}
    assert {row["days"] for row in totals} == {expected["days"]}
    assert sorted(row["minutes"] for row in totals) == expected["minutes"]
    assert sorted(row["hours"] for row in totals) == expected["hours"]
    for name, wanted in expected["by_class"].items():
        assert {row["by_class"][name]["sessions"] for row in totals} == {wanted["sessions"]}
        assert sorted({row["by_class"][name]["minutes"] for row in totals}) == wanted["minutes"]


def test_weeks_sum_to_the_total(rows):
    """Check 9: for each way the open conflict could be settled, the weeks add
    up to the total, and so do the classes."""
    totals = counting.totals(rows["contacts"], rows["plan_rules"], KEY["period"]["start"], KEY["period"]["end"])
    for total in totals:
        by_week = 0
        for week in rows["weekly_status"]:
            fitting = [
                entry
                for entry in week["minutes"]
                if all(total["choices"].get(conflict) == value for conflict, value in entry["choices"].items())
            ]
            assert len(fitting) == 1
            by_week += fitting[0]["minutes"]
        assert by_week == total["minutes"]
        assert sum(entry["minutes"] for entry in total["by_class"].values()) == total["minutes"]
        assert sum(entry["sessions"] for entry in total["by_class"].values()) == total["sessions"]


# ---- Checks 3 and 4: the order of arrival ----------------------------------------


def test_any_order_of_arrival_gives_the_same_store(full_read, tmp_path):
    expected = store.dump(full_read)
    for seed in range(5):
        shuffled = {path.name: position for position, path in enumerate(_shuffled(seed))}
        other = replay(tmp_path / f"order{seed}", order=lambda path: shuffled[path.name])
        try:
            assert store.dump(other) == expected, f"order {seed}"
        finally:
            other.close()


def test_two_batches_give_the_same_store_as_one(full_read, tmp_path):
    def batches(files):
        first = [path for path in files if not path.name.startswith("BH-D1")]
        return [first, [path for path in files if path not in first]]

    other = replay(tmp_path / "batches", batches=batches)
    try:
        assert store.dump(other) == store.dump(full_read)
    finally:
        other.close()


def test_a_correction_that_arrives_before_its_roster_changes_nothing(full_read, tmp_path):
    def batches(files):
        first = [path for path in files if "BH-D103" in path.name or "BH-D104" in path.name]
        return [first, [path for path in files if path not in first]]

    other = replay(tmp_path / "correction_first", batches=batches)
    try:
        assert store.dump(other) == store.dump(full_read)
    finally:
        other.close()


def _shuffled(seed):
    from conftest import DOCUMENTS

    files = sorted(DOCUMENTS.iterdir())
    random.Random(seed).shuffle(files)
    return files


# ---- The same rules on the earlier read ------------------------------------------


def test_the_earlier_read_gives_the_same_figures(tmp_path):
    """The model gave some times and statuses other labels on its earlier read
    (prompt version 2). The rules must reach the same figures from it."""
    earlier = replay(tmp_path / "version2", prompt_version=2)
    try:
        versions = {row[0] for row in earlier.execute("SELECT DISTINCT prompt_version FROM claims")}
        assert versions == {2}
        rows = {table: store.rows_of(earlier, table, PATIENT) for table in store.CONCLUDES_TABLES}
    finally:
        earlier.close()
    encounters = {row["encounter_id"]: row for row in rows["contacts"] if row["record_kind"] == "encounter"}
    assert sorted(encounters) == [entry["encounter"] for entry in KEY["contacts"]]
    for expected in KEY["contacts"]:
        contact = encounters[expected["encounter"]]
        assert contact["status"] == expected["status"], expected["encounter"]
        assert sorted(entry["minutes"] for entry in contact["minutes"]) == expected["minutes"], expected["encounter"]
    for expected in KEY["weeks"]:
        week = next(row for row in rows["weekly_status"] if row["week_start"] == expected["start"])
        assert week["verdict"] == expected["verdict"]
        assert sorted(entry["minutes"] for entry in week["minutes"]) == expected["minutes"]
    assert [row["score"] for row in rows["assessments"]] == [[18], [14], [10]]
    assert len(rows["conflicts"]) == 3


def test_a_read_at_medium_effort_gives_the_same_figures(tmp_path):
    """The comparison run for O-44: the same rules on the medium-effort results."""
    other = replay(tmp_path / "medium", effort="medium")
    try:
        efforts = {row[0] for row in other.execute("SELECT DISTINCT effort FROM claims")}
        assert efforts == {"medium"}
        rows = {table: store.rows_of(other, table, PATIENT) for table in store.CONCLUDES_TABLES}
    finally:
        other.close()
    encounters = {row["encounter_id"]: row for row in rows["contacts"] if row["record_kind"] == "encounter"}
    assert sorted(encounters) == [entry["encounter"] for entry in KEY["contacts"]]
    for expected in KEY["contacts"]:
        contact = encounters[expected["encounter"]]
        assert contact["status"] == expected["status"], expected["encounter"]
        assert sorted(entry["minutes"] for entry in contact["minutes"]) == expected["minutes"], expected["encounter"]
    for expected in KEY["weeks"]:
        week = next(row for row in rows["weekly_status"] if row["week_start"] == expected["start"])
        assert week["verdict"] == expected["verdict"]
        assert sorted(entry["minutes"] for entry in week["minutes"]) == expected["minutes"]
    assert [row["score"] for row in rows["assessments"]] == [[18], [14], [10]]
    assert len(rows["conflicts"]) == 3

