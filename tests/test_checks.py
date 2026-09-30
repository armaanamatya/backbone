"""Stage 8: the checks in section 9 of the build plan that the other files
do not already hold: 7, 8 and 11, plus the answer checks Discussion 32 asked
for. No model is called, and no check here reads the answer key.
"""

import pytest

from backbone import checks, ingest, store
from conftest import replay
from made_up import DAY, Record
from test_patients import put

PATIENT = "HG-M042"


# ---- Check 8: no patient is in two contacts at once ---------------------------------


def test_no_patient_is_in_two_contacts_at_once(full_read):
    assert checks.overlaps(full_read) == []


def test_without_the_correction_the_overlap_on_jan_19_is_caught(tmp_path):
    """The check the plan names: with BH-D103 missing, the roster's 11:30
    departure puts the patient in the group and the individual session at once."""
    other = replay(tmp_path / "no_correction", batches=lambda files: [[f for f in files if "BH-D103" not in f.name]])
    try:
        found = checks.overlaps(other)
    finally:
        other.close()
    assert len(found) == 1
    assert (found[0]["first"], found[0]["second"], found[0]["date"]) == ("HG-E110", "HG-E111", "2026-01-19")
    assert found[0]["first_present"] == "10:00–11:30" and found[0]["second_present"] == "11:15–11:45"


def test_an_overlap_in_a_made_up_record_is_found(connection, log):
    record = Record()
    record.document("plan", kind="plan", signed="2025-03-03T13:00").plan(days=1, minutes=45)
    record.document("group note").contact("NF-E1", service="group_therapy").present("10:00", "11:30")
    record.document("individual note").contact("NF-E2", service="individual_therapy").present("11:15", "11:45")
    put(connection, record, "first")
    ingest.conclude(connection, record.patient, log)
    found = checks.overlaps(connection)
    assert [(f["first"], f["second"]) for f in found] == [("NF-E1", "NF-E2")]


def test_contacts_that_meet_end_to_end_do_not_overlap(connection, log):
    """The end minute is not inside the interval (D-34)."""
    record = Record()
    record.document("plan", kind="plan", signed="2025-03-03T13:00").plan(days=1, minutes=45)
    record.document("group note").contact("NF-E1", service="group_therapy").present("10:00", "11:15")
    record.document("individual note").contact("NF-E2", service="individual_therapy").present("11:15", "11:45")
    put(connection, record, "first")
    ingest.conclude(connection, record.patient, log)
    assert checks.overlaps(connection) == []
    assert DAY


# ---- Check 7: stated minutes agree with the clock, or a conflict is open ------------


def test_stated_minutes_equal_the_clock_times_or_a_conflict_exists(full_read):
    assert checks.stated_minutes_disagree(full_read) == []


def test_stated_minutes_that_disagree_without_a_conflict_are_caught(connection, log):
    record = Record()
    record.document("plan", kind="plan", signed="2025-03-03T13:00").plan(days=1, minutes=45)
    record.document("note").contact("NF-E1", service="individual_therapy").present("10:00", "10:50").minutes(50)
    put(connection, record, "first")
    ingest.conclude(connection, record.patient, log)
    assert checks.stated_minutes_disagree(connection) == []
    # Tamper with the conclusion, as a fault in the rules would.
    connection.execute("UPDATE contacts SET minutes = ? WHERE patient_key = ?", ('[{"minutes": 40, "present": true, "choices": {}}]', record.patient))
    found = checks.stated_minutes_disagree(connection)
    assert [(f["contact"], f["stated"], f["from_clock"]) for f in found] == [("NF-E1", 50, [40])]


# ---- Check 6 on the store ----------------------------------------------------------


def test_every_stored_quote_is_at_its_line(full_read):
    assert checks.quotes_not_at_line(full_read) == []


# ---- Check 11 and the answer checks ---------------------------------------------------


def test_every_number_in_an_answer_comes_from_the_results(answers):
    for question_id, built in answers.items():
        assert checks.numbers_not_in_results(built) == [], question_id


def test_a_number_from_nowhere_is_caught(answers):
    built = dict(answers["DEV-01"])
    built["parts"] = {**built["parts"], "2. the answer": built["parts"]["2. the answer"] + ["There were 999 sessions."]}
    assert [p["number"] for p in checks.numbers_not_in_results(built)] == ["999"]


def test_part_5_never_contradicts_part_6(answers):
    for question_id, built in answers.items():
        assert checks.part_5_contradicts_part_6(built) == [], question_id


def test_the_open_conflict_behind_the_minutes_is_in_part_6_and_not_called_elsewhere(answers):
    for question_id in ("DEV-01", "DEV-02", "DEV-03"):
        parts = answers[question_id]["parts"]
        assert any("HG-E115, start" in line for line in parts["6. not settled"]), question_id
        assert not any("not behind these figures" in line for line in parts["5. what was excluded"]), question_id


def test_dates_in_answers_are_in_the_short_form(answers):
    for question_id, built in answers.items():
        assert checks.long_dates(built) == [], question_id


def test_no_contact_is_listed_twice_in_part_5(answers):
    for question_id, built in answers.items():
        assert checks.repeated_contacts(built) == [], question_id


def test_the_six_administrative_records_are_each_listed(answers):
    lines = [line for line in answers["DEV-01"]["parts"]["5. what was excluded"] if line.endswith("an administrative record, never counted.")]
    assert len(lines) == 6
    assert sum(1 for line in lines if line.startswith("- Jan 8 at ")) == 2


def test_a_conflict_on_no_contact_behind_the_figures_is_left_out(answers):
    """DEV-05 is about scores and statements. The Jan 26 start and the Jan 27
    charge concern contacts that are behind none of its figures."""
    text = answers["DEV-05"]["text"]
    assert "HG-E115" not in text
    assert "charge" not in text.lower()
    assert answers["DEV-05"]["parts"]["6. not settled"] == ["Nothing."]


def test_the_group_note_says_no_therapy_during_the_break_not_in_the_group(answers):
    text = "\n".join(answers["DEV-04"]["parts"]["2. the answer"])
    assert "says no therapy was provided during 10:45–11:00" in text
    assert "says no therapy was provided." not in text


def test_the_lead_of_dev_05_gives_the_reason_for_the_added_contact(answers):
    lead = answers["DEV-05"]["parts"]["in short"]
    assert any(line.startswith("Why the contact on Jan 19 was arranged") for line in lead)
    assert 2 <= len(lead) <= 4


def test_engagement_leaves_out_contacts_between_professionals(answers):
    line = next(l for l in answers["DEV-05"]["parts"]["2. the answer"] if l.startswith("- Unbroken engagement"))
    assert "1 contact held without the patient" in line
    assert "between professionals" in line
