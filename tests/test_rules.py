"""Stages 4 and 5, one rule at a time, on made-up claims.

No model and no supplied document is used. Each check names the rule in
`decisions.md` that it tries.
"""

from backbone import counting, reconcile
from made_up import DAY, PATIENT, Record


def conclude(record, claims=None):
    rows = reconcile.conclude(record.patient, claims if claims is not None else record.claims, record.sections)
    rows["weekly_status"] = counting.weekly_status(rows["contacts"], rows["plan_rules"], record.sections)
    return rows


def only(rows, table="contacts"):
    assert len(rows[table]) == 1, rows[table]
    return rows[table][0]


def minutes_of(contact):
    return sorted(entry["minutes"] for entry in contact["minutes"])


def roster_and_correction(record):
    roster = record.document("roster", kind="attendance_record", signed=f"{DAY}T12:00")
    roster.contact("NF-E1").scheduled("10:00", "11:30").arrived("10:00").left("11:30").attendance("attended")
    fix = record.document("correction", kind="correction", signed="2025-03-05T09:00")
    fix.contact("NF-E1").correction("departure", "11:30", "11:10").left("11:10")
    return roster, fix


# ---- Rule 8 and rule 9 ------------------------------------------------------


def test_rule_8_a_signed_correction_replaces_the_value_it_names():
    record = Record()
    roster_and_correction(record)
    rows = conclude(record)
    contact = only(rows)
    assert contact["presence"][0]["end"] == "11:10"
    assert minutes_of(contact) == [70]
    conflict = only(rows, "conflicts")
    assert (conflict["field"], conflict["status"], conflict["rule"], conflict["outcome"]) == (
        "departure", "settled", "8", "11:10")


def test_rule_8_does_not_depend_on_the_order_the_documents_arrive_in():
    record = Record()
    roster_and_correction(record)
    record.document("copy", kind="attendance_record", signed=None, is_copy=True, copy_signed=f"{DAY}T12:00") \
        .contact("NF-E1").arrived("10:00").left("11:30")
    first = conclude(record)
    for seed in range(8):
        assert conclude(record, record.shuffled(seed)) == first


def test_rule_9_a_copy_received_after_the_correction_does_not_bring_the_old_value_back():
    record = Record()
    roster_and_correction(record)
    record.document(
        "copy", kind="attendance_record", signed=None, is_copy=True, copy_signed=f"{DAY}T12:00",
        dates=[("received", "2025-03-11")],
    ).contact("NF-E1").arrived("10:00").left("11:30").attendance("attended")
    rows = conclude(record)
    contact = only(rows)
    assert contact["service_date"] == DAY, "the date it was received places nothing (rule 2)"
    assert minutes_of(contact) == [70]
    conflict = only(rows, "conflicts")
    assert (conflict["status"], conflict["rule"], conflict["outcome"]) == ("settled", "8, then 9", "11:10")
    old = next(entry for entry in conflict["alternatives"] if entry["value"] == "11:30")
    assert old["documents"] == ["copy", "roster"]


def test_a_new_signed_record_after_the_correction_reopens_the_question():
    record = Record()
    roster_and_correction(record)
    record.document("later note", signed="2025-03-06T10:00").contact("NF-E1").left("11:30")
    rows = conclude(record)
    conflict = only(rows, "conflicts")
    assert conflict["status"] == "open"
    assert minutes_of(only(rows)) == [70, 90]


def test_a_correction_of_a_field_no_rule_covers_stays_open():
    record = Record()
    note = record.document("note")
    note.contact("NF-E1").present("10:00", "10:50")
    record.document("fix", kind="correction", signed="2025-03-05T09:00").contact("NF-E1").correction(
        "other", "in person", "video")
    rows = conclude(record)
    assert only(rows, "conflicts")["status"] == "open"


# ---- Rule 10 ------------------------------------------------------------------


def draft_charge_and_register(record, register=True):
    draft = record.document("draft", kind="draft_note", signed=None)
    draft.contact("NF-E2").scheduled("10:00", "11:30").attendance("attended").participant("patient", "present")
    draft.statement("made_before_the_service")
    record.document("charge", kind="billing_extract", signed=None).contact("NF-E2").charge("CH-9")
    if register:
        record.document("register", kind="attendance_record", signed=None).contact("NF-E2").scheduled(
            "10:00", "11:30").attendance("no_show", entry_signed_by="Dana Ortiz", entry_signed_date=DAY)


def test_rule_10_a_draft_and_a_charge_cannot_establish_attendance():
    record = Record()
    draft_charge_and_register(record)
    rows = conclude(record)
    contact = only(rows)
    assert (contact["status"], contact["patient_present"], contact["minutes"]) == ("no_show", "no", [])
    conflict = only(rows, "conflicts")
    assert (conflict["field"], conflict["status"], conflict["rule"], conflict["outcome"]) == (
        "attendance", "settled", "10", "did not attend")
    kinds = {finding["kind"] for finding in rows["findings"]}
    assert "charge_without_attendance" in kinds


def test_rule_10_a_draft_and_a_charge_alone_leave_attendance_not_established():
    record = Record()
    draft_charge_and_register(record, register=False)
    rows = conclude(record)
    contact = only(rows)
    assert (contact["status"], contact["patient_present"], contact["minutes"]) == ("not_established", "no", [])
    assert "charge_without_attendance" in {finding["kind"] for finding in rows["findings"]}


def test_rule_10_a_schedule_status_is_not_attendance():
    record = Record()
    record.document("schedule", kind="schedule_export", signed=None).contact("NF-E3").scheduled(
        "09:00", "09:50").attendance("completed")
    contact = only(conclude(record))
    assert contact["patient_present"] == "no"
    assert contact["minutes"] == []


def test_d42_a_no_show_is_taken_from_a_scheduling_record():
    record = Record()
    record.document("log", kind="scheduling_log", signed=None).contact("NF-E3", service="individual_therapy") \
        .time("contact_interval", "09:00", "09:50", "not_labelled", "header").attendance("no_show")
    contact = only(conclude(record))
    assert contact["status"] == "no_show"
    assert contact["presence"] == [], "a time in a scheduling log is the booked slot, not presence"


# ---- Rule 11 and rule 12 ------------------------------------------------------


def two_notes_that_disagree(record, first="09:00", second="09:10"):
    stated = {"09:00": 50, "09:10": 40}
    record.document("note A", signed=f"{DAY}T11:00").contact("NF-E4", service="individual_therapy").present(
        first, "09:50").minutes(stated[first])
    record.document("note B", signed=f"{DAY}T12:00").contact("NF-E4", service="individual_therapy").present(
        second, "09:50").minutes(stated[second])


def test_rule_11_two_signed_notes_that_disagree_stay_open():
    record = Record()
    two_notes_that_disagree(record)
    rows = conclude(record)
    assert minutes_of(only(rows)) == [40, 50]
    conflict = only(rows, "conflicts")
    assert (conflict["field"], conflict["status"], conflict["rule"], conflict["outcome"]) == (
        "start", "open", "11", None)
    assert [entry["value"] for entry in conflict["alternatives"]] == ["09:00", "09:10"]
    assert conflict["would_settle"]


def test_rule_1_two_notes_for_one_session_count_once():
    record = Record()
    two_notes_that_disagree(record, "09:00", "09:00")
    rows = conclude(record)
    assert minutes_of(only(rows)) == [50]
    assert rows["conflicts"] == []


def week(record):
    rows = conclude(record)
    return next(row for row in rows["weekly_status"] if row["week_start"] == "2025-03-03"), rows


def test_rule_12_verdicts_under_an_open_conflict():
    for minimum, expected in ((30, "met"), (45, "cannot_determine"), (60, "not_met")):
        record = Record()
        record.document("plan", kind="plan").plan(days=1, minutes=minimum, counted=("individual_therapy",))
        two_notes_that_disagree(record)
        status, _ = week(record)
        assert status["verdict"] == expected, minimum
        assert sorted(entry["minutes"] for entry in status["minutes"]) == [40, 50]
        assert status["conflicts"] == [f"{PATIENT}/NF-E4:start"]


# ---- Rules 3, 4, 5, 6 -----------------------------------------------------------


def test_rule_3_a_scheduled_time_is_never_counted():
    record = Record()
    record.document("register", kind="attendance_record", signed=None).contact("NF-E5").scheduled(
        "10:00", "11:30").arrived("10:20").left("11:30").attendance("attended_part")
    contact = only(conclude(record))
    assert minutes_of(contact) == [70]
    assert contact["partial"]


def test_rule_5_and_6_a_break_is_removed_only_where_it_overlaps_presence():
    record = Record()
    record.document("register", kind="attendance_record", signed=None).contact("NF-E5").arrived("10:50").left("11:30")
    record.document("group note").contact("NF-E5").scheduled("10:00", "11:30").no_therapy("10:45", "11:00")
    contact = only(conclude(record))
    assert contact["presence"][0]["intervals"] == [["11:00", "11:30"]]
    assert minutes_of(contact) == [30]


def test_rule_6_an_interval_does_not_include_its_end_minute():
    record = Record()
    record.document("note").contact("NF-E5", service="individual_therapy").present("10:00", "11:15")
    assert minutes_of(only(conclude(record))) == [75]


def test_rule_4_time_without_the_patient_is_not_the_patients():
    record = Record()
    note = record.document("family note").contact("NF-E6", service="family_therapy")
    note.time("contact_interval", "13:00", "13:45", "not_labelled", "header")
    note.time("patient_absent_interval", "13:00", "13:15", "not_labelled", "header")
    note.present("13:15", "13:45", label="not_labelled").minutes(30).minutes(45, of="contact_total")
    rows = conclude(record)
    contact = only(rows)
    assert minutes_of(contact) == [30]
    assert contact["minutes_without_patient"] == 15
    assert contact["partial"]
    assert rows["conflicts"] == []


def test_rule_4_a_contact_held_without_the_patient_is_not_a_missed_appointment():
    record = Record()
    note = record.document("collateral note").contact("NF-E7", service="collateral_contact")
    note.time("contact_interval", "14:00", "14:40", "not_labelled", "header")
    note.attendance("absent").participant("patient", "absent").participant("family_or_partner", "present", "Robin Hale")
    contact = only(conclude(record))
    assert (contact["status"], contact["patient_present"]) == ("held_without_patient", "no")
    assert contact["minutes_without_patient"] == 40
    assert contact["minutes"] == []


def test_rule_4_two_calls_of_one_video_session_are_one_contact():
    record = Record()
    note = record.document("video note").contact("NF-E8", service="individual_therapy", appointment="NF-A8")
    note.modality("video").present("13:00", "13:20", position="body").present("13:30", "13:55", position="body")
    note.no_therapy("13:20", "13:30", detail="connection lost").minutes(45)
    export = record.document("platform", kind="platform_export", signed=None).contact(appointment="NF-A8", service=None)
    export.time("connection", "13:00", "13:20").time("connection", "13:30", "13:55")
    rows = conclude(record)
    contact = only(rows)
    assert (contact["encounter_id"], contact["appointment_id"], contact["modality"]) == ("NF-E8", "NF-A8", "video")
    assert minutes_of(contact) == [45]
    assert [(row["start"], row["end"]) for row in contact["removed"]] == [("13:20", "13:30")]
    assert rows["conflicts"] == []


def test_d39_with_no_times_for_the_patient_the_interval_of_the_contact_is_used():
    record = Record()
    record.document("medication note").contact("NF-E9", service="medication_management").time(
        "contact_interval", "15:00", "15:20", "not_labelled", "header").minutes(20, of="contact_total")
    contact = only(conclude(record))
    assert (contact["status"], contact["patient_present"]) == ("held", "yes")
    assert minutes_of(contact) == [20]


# ---- Rule 14 --------------------------------------------------------------------


def test_rule_14_stated_minutes_that_differ_from_the_clock_open_a_conflict():
    record = Record()
    record.document("note").contact("NF-E10", service="individual_therapy").present("11:00", "11:45").minutes(50)
    rows = conclude(record)
    assert minutes_of(only(rows)) == [45, 50]
    conflict = only(rows, "conflicts")
    assert (conflict["field"], conflict["status"]) == ("minutes", "open")


def test_rule_14_stated_minutes_stand_where_no_clock_time_is_given():
    record = Record()
    record.document("note").contact("NF-E10", service="individual_therapy").attendance("attended").minutes(45)
    assert minutes_of(only(conclude(record))) == [45]


# ---- Rule 1 and D-41 ----------------------------------------------------------


def test_rule_1_a_reference_with_no_number_matches_on_date_class_and_time():
    record = Record()
    record.document("note").contact("NF-E11", service="individual_therapy").present("11:15", "11:45")
    record.document("other note").contact(None, service="individual_therapy").arrived("11:15")
    record.document("morning note").contact(None, service="individual_therapy").present("08:00", "08:30")
    rows = conclude(record)
    assert sorted(contact["encounter_id"] or "none" for contact in rows["contacts"]) == ["NF-E11", "none"]
    assert rows["conflicts"] == []


def test_d41_a_mention_makes_no_contact():
    record = Record()
    record.document("note").contact("NF-E11", service="individual_therapy").present("11:15", "11:45")
    record.document("log", kind="scheduling_log", signed=None).contact(None, service="family_therapy", date="2025-03-07")
    assert len(conclude(record)["contacts"]) == 1


def test_d40_a_call_about_scheduling_is_kept_and_is_not_an_encounter():
    record = Record()
    record.document("log", kind="scheduling_log", signed=None).contact(None, service="scheduling_contact").time(
        "connection", "13:20").modality("telephone").participant("patient", "present")
    contact = only(conclude(record))
    assert (contact["record_kind"], contact["status"]) == ("administrative", "recorded")
    assert counting.counts(contact, None) == (False, "an administrative record, not an encounter")


def test_rule_15_names_are_not_merged_on_likeness():
    record = Record()
    note = record.document("note").contact("NF-E12", service="individual_therapy").present("09:00", "09:50")
    note.participant("clinician", name="N. Ortiz").participant("clinician", name="Nina Ortiz, LPC")
    assert only(conclude(record))["clinicians"] == ["N. Ortiz", "Nina Ortiz"]


# ---- Counting: rules 2 and 4, D-37, R-29 -------------------------------------


def planned(record, **plan):
    record.document("plan", kind="plan", signed="2025-03-03T13:00").plan(**plan)


def session(record, name, number, date, start, end, service="individual_therapy", signed=None):
    record.document(name, signed=signed or f"{date}T17:00").contact(number, date=date, service=service).present(start, end)


def test_rule_2_a_session_belongs_to_the_week_of_its_service_date():
    record = Record()
    planned(record)
    session(record, "late note", "NF-E13", "2025-03-07", "10:00", "10:50", signed="2025-03-12T09:00")
    rows = conclude(record)
    weeks = {row["week_start"]: row for row in rows["weekly_status"]}
    assert weeks["2025-03-03"]["minutes"][0]["minutes"] == 50
    assert weeks["2025-03-10"]["minutes"][0]["minutes"] == 0


def test_d11_two_sessions_on_one_date_make_one_therapy_day():
    record = Record()
    planned(record)
    session(record, "first", "NF-E14", DAY, "10:00", "11:00", service="group_therapy")
    session(record, "second", "NF-E15", DAY, "11:00", "11:30")
    status, rows = week(record)
    assert status["days"][0]["days"] == 1
    assert status["minutes"][0]["minutes"] == 90
    total = only({"totals": counting.totals(rows["contacts"], rows["plan_rules"], "2025-03-03", "2025-03-28")}, "totals")
    assert (total["sessions"], total["days"], total["minutes"], total["hours"]) == (2, 1, 90, 1.5)


def test_d10_a_class_the_plan_excludes_adds_nothing():
    record = Record()
    planned(record)
    session(record, "therapy", "NF-E16", DAY, "10:00", "11:00")
    session(record, "medication", "NF-E17", "2025-03-05", "09:00", "09:25", service="medication_management")
    session(record, "unlisted", "NF-E18", "2025-03-06", "09:00", "09:25", service="care_coordination")
    status, rows = week(record)
    assert (status["days"][0]["days"], status["minutes"][0]["minutes"]) == (1, 60)
    plan = counting.plans(rows["plan_rules"])[0]
    reasons = {c["encounter_id"]: counting.counts(c, plan)[1] for c in rows["contacts"]}
    assert reasons["NF-E17"] == "a class of service the plan excludes"
    assert reasons["NF-E18"] == "a class of service the plan does not count"


def test_r29_a_session_after_the_episode_ends_does_not_count():
    record = Record()
    planned(record, end="2025-03-06")
    session(record, "inside", "NF-E19", DAY, "10:00", "11:00")
    session(record, "after", "NF-E20", "2025-03-07", "10:00", "11:00")
    status, _ = week(record)
    assert status["minutes"][0]["minutes"] == 60
    assert status["partial"], "the week runs past the end of the episode (D-14)"


def test_d37_plan_rules_come_only_from_a_plan():
    record = Record()
    planned(record)
    record.document("authorization", kind="authorization", signed=None).rule(
        "requirement", measure="sessions", minimum=8, period="episode")
    rows = conclude(record)
    assert {row["value"]["document"] for row in rows["plan_rules"]} == {"plan"}
    assert [entry["measure"] for entry in counting.plans(rows["plan_rules"])[0]["requirements"]] == [
        "minutes", "therapy_days"]


def test_with_no_plan_nothing_is_judged():
    record = Record()
    session(record, "therapy", "NF-E21", DAY, "10:00", "11:00")
    rows = conclude(record)
    assert rows["weekly_status"] == []
    assert counting.totals(rows["contacts"], rows["plan_rules"], "2025-03-03", "2025-03-09")[0]["sessions"] == 0


def test_d31_a_date_is_documented_when_a_schedule_view_covers_it():
    record = Record()
    planned(record, end="2025-03-09")
    session(record, "therapy", "NF-E22", DAY, "10:00", "11:00")
    record.document(
        "schedule", kind="schedule_export", signed=None,
        dates=[("period_start", "2025-03-03"), ("period_end", "2025-03-07")],
    )
    status, _ = week(record)
    assert status["undocumented"] == ["2025-03-08", "2025-03-09"]


# ---- Rule 13 --------------------------------------------------------------------


def test_rule_13_a_copy_and_a_mention_add_no_assessment():
    record = Record()
    record.document("review", kind="questionnaire_review").score(14, "2025-03-10", form="NF-Q1", time="08:17") \
        .score(18, "2025-03-03", relation="mention")
    record.document("intake").score(18, "2025-03-03")
    record.document("import", kind="import_receipt", signed=None, is_copy=True).score(14, "2025-03-10", form="NF-Q1")
    rows = conclude(record)
    found = [(row["completed_date"], row["score"], len(row["copies"]), len(row["mentions"])) for row in rows["assessments"]]
    assert found == [("2025-03-03", [18], 0, 1), ("2025-03-10", [14], 1, 0)]


def test_rule_13_two_forms_on_one_date_are_two_assessments():
    record = Record()
    record.document("review", kind="questionnaire_review").score(14, "2025-03-10", form="NF-Q1") \
        .score(9, "2025-03-10", form="NF-Q2").score(7, "2025-03-10", instrument="PHQ-9")
    assert len(conclude(record)["assessments"]) == 3


def test_rule_13_a_score_that_two_records_give_differently_stays_open():
    record = Record()
    record.document("review", kind="questionnaire_review").score(14, "2025-03-10", form="NF-Q1")
    record.document("note").score(15, "2025-03-10", form="NF-Q1")
    rows = conclude(record)
    assert only(rows, "assessments")["score"] == [14, 15]
    assert only(rows, "conflicts")["field"] == "score"
