"""Stages 6 and 7: the functions, and the answers written from the saved plans.

No model is called. The plans the model returned are read from
`output/answers/plans`, the same way saved reading results are.
"""

from backbone import functions

PATIENT = "HG-M042"


def text_of(answer, part):
    return "\n".join(answer["parts"][part])


# ---- Stage 6: the functions run without a model ----------------------------------


def test_every_function_runs_directly(full_read):
    for name in functions.CATALOGUE:
        arguments = {"patient": PATIENT, "date": "2026-01-19", "first_start": "2026-01-05", "first_end": "2026-01-16", "second_start": "2026-01-19", "second_end": "2026-01-30"}
        result = functions.call(full_read, name, arguments)
        assert result["function"] == name
        assert "sources" in result and "conflicts" in result and "not_read" in result


def test_a_function_result_cites_lines_that_hold_the_quote(full_read):
    result = functions.care_delivered(full_read, PATIENT)
    assert result["sources"]
    assert all(source["verified"] for source in result["sources"])


def test_a_patient_is_never_swapped_for_another(full_read):
    assert functions.resolve_patient(full_read, "Jordan Blake")["status"] == "not_found"
    assert functions.resolve_patient(full_read, "Casey Mercer")["status"] == "participant"
    assert functions.resolve_patient(full_read, "Rowan Mercer")["status"] == "found"
    assert functions.resolve_patient(full_read, "HG-M042")["status"] == "found"


# ---- Stage 7: the five answers -----------------------------------------------------


def test_every_answer_has_nine_parts_and_used_a_saved_plan(answers):
    for question_id, answer in answers.items():
        assert answer["plan_source"] == "saved", question_id
        assert len([name for name in answer["parts"] if name[0].isdigit()]) == 9, question_id
        assert "[quote not found" not in answer["text"], question_id
        assert 1 <= len(answer["parts"]["in short"]) <= 4, question_id


def test_dev_01_sessions_by_type_and_days(answers):
    text = text_of(answers["DEV-01"], "2. the answer")
    assert "12 therapy sessions on 11 distinct days" in text
    assert "2 family therapy, 5 group therapy, 5 individual therapy" in text
    assert "20 encounters in the record, 16 held, 14 with the patient present" in text_of(answers["DEV-01"], "3. figures")
    lead = " ".join(answers["DEV-01"]["parts"]["in short"])
    assert lead.startswith("12 therapy sessions on 11 distinct days")
    assert "One point is open: the start of HG-E115" in lead
    assert "Not counted: HG-E116" in lead
    contributed = text_of(answers["DEV-01"], "4. what contributed")
    assert "counted once" in contributed
    assert "BH-D104 is a copy" in contributed


def test_dev_02_minutes_and_hours(answers):
    text = text_of(answers["DEV-02"], "2. the answer")
    assert "585 or 595 minutes of therapy, which is 9.75 or 9.92 hours" in text
    for week in ("140 minutes (2.33 hours)", "120 minutes (2.00 hours)", "180 minutes (3.00 hours)", "145 or 155 minutes (2.42 or 2.58 hours)"):
        assert week in text
    assert answers["DEV-02"]["parts"]["in short"][0].startswith("585 or 595 minutes")
    assert "HG-E115" in text_of(answers["DEV-02"], "6. not settled")
    excluded = text_of(answers["DEV-02"], "5. what was excluded")
    assert "Removed from the minutes: HG-E112 on Jan 21, 13:20–13:30, 10 minutes" in excluded
    assert "Time without the patient: HG-E119 on Jan 30, 15 minutes" in excluded
    assert excluded.count("Removed from the minutes") == 6


def test_dev_03_verdicts(answers):
    text = text_of(answers["DEV-03"], "2. the answer")
    assert "at least 150 minutes and at least 3 therapy days" in text
    assert "140 minutes (2.33 hours): not met" in text
    assert "120 minutes (2.00 hours): not met" in text
    assert "180 minutes (3.00 hours): met" in text
    assert "145 or 155 minutes (2.42 or 2.58 hours): cannot be determined" in text
    assert "partial" in text
    assert "Of 4 weeks, 1 met the goal, 2 did not, and 1 cannot be determined" in answers["DEV-03"]["parts"]["in short"][0]
    assert "HG-E115" in text_of(answers["DEV-03"], "6. not settled")


def test_dev_04_two_dates(answers):
    text = text_of(answers["DEV-04"], "2. the answer")
    assert "Jan 19: 2 therapy contacts of 2 encounters; patient therapy minutes 90" in text
    assert "Jan 21: 1 therapy contact of 1 encounter; patient therapy minutes 45" in text
    assert "by video" in text
    for sentence in (
        "The attendance record, signed, BH-D102 gives",
        "Its departure 11:30 was replaced by the correction",
        "The correction, signed, BH-D103 gives",
        "A later copy of the record BH-D104 gives",
        "It changes nothing: a copy carries the date and authority of its original",
        "The telehealth platform export" if "platform" in text else "The clinical note, signed, BH-D106 gives",
        "says the second part continued the same contact",
    ):
        assert sentence in text, sentence
    # The plan asked for the disagreements of Jan 19 to Jan 21, and none there is open.
    assert text_of(answers["DEV-04"], "6. not settled") == "Nothing."
    excluded = text_of(answers["DEV-04"], "5. what was excluded")
    assert "11:30 (BH-D102, BH-D104)" in excluded and "Settled by rule 8, then 9: 11:15" in excluded


def test_dev_05_assessments_and_course(answers):
    text = text_of(answers["DEV-05"], "2. the answer")
    assert "PHQ-9 18 to 14 to 10 across 3 distinct assessments (Jan 5, Jan 16, Jan 30), 8 points lower overall" in text
    assert "What the record supports:" in text and "What the record does not settle:" in text
    assert "A fall in PHQ-9 of 8 points across 3 distinct assessments" in text
    assert "thresholds are outside the record" in text
    lead = answers["DEV-05"]["parts"]["in short"]
    assert lead[0].startswith("PHQ-9 18 to 14 to 10")
    assert "latest word on progress" in lead[1]
    for topic in ("on mood", "on anxiety", "on sleep", "on safety", "on functioning", "on progress"):
        assert topic in text, topic
    assert "This visit was added because Rowan became anxious during group" in text
    # Nothing these figures depend on is open. What is open elsewhere in the record is labelled.
    assert all("not behind these figures" in line for line in answers["DEV-05"]["parts"]["6. not settled"])
    excluded = text_of(answers["DEV-05"], "5. what was excluded")
    assert "BH-D014: a copy of the PHQ-9 of Jan 16" in excluded
    assert "BH-D013: a mention of the PHQ-9 of Jan 5" in excluded


# ---- Stage 7: the nine problem questions (section 8 of the key) ----------------------


def test_p1_unknown_patient(answers):
    text = answers["P-1"]["text"]
    assert "No patient named Jordan Blake" in text
    assert "12" not in text_of(answers["P-1"], "2. the answer")
    assert answers["P-1"]["results"] == []


def test_p2_participant_not_patient(answers):
    text = text_of(answers["P-2"], "2. the answer")
    assert "participant, not as a patient" in text
    for on in ("Jan 9", "Jan 16", "Jan 30"):
        assert on in text
    assert " 0 " not in text


def test_p3_false_premise_group_not_attended(answers):
    text = text_of(answers["P-3"], "2. the answer")
    assert "patient therapy minutes 0" in text
    assert "no-show" in text
    whole = answers["P-3"]["text"]
    assert "BH-D108 line 16" in whole
    assert "draft" in whole.lower() and "CH-116" in whole


def test_p4_no_score_that_day(answers):
    text = text_of(answers["P-4"], "2. the answer")
    assert "No questionnaire was completed on Jan 26" in text
    assert "copy of the PHQ-9 of Jan 16, score 14" in text


def test_p5_no_plan_change(answers):
    text = text_of(answers["P-5"], "2. the answer")
    assert "1 plan and 0 changes" in text


def test_p6_date_with_no_document(answers):
    text = text_of(answers["P-6"], "2. the answer")
    assert "not documented" in text
    assert "does not say that no care took place" in text


def test_p7_ambiguous_term(answers):
    understood = text_of(answers["P-7"], "1. the question as understood")
    assert "Reading:" in understood
    text = text_of(answers["P-7"], "2. the answer")
    assert "12 therapy sessions" in text
    assert "Under other readings of the question: 16 contacts held, 14 with the patient present, 20 encounters in the record" in text


def test_p8_relative_date(answers):
    understood = text_of(answers["P-8"], "1. the question as understood")
    assert "last week of the episode" in understood
    assert "2026-01-26" in understood
    assert "3 therapy sessions" in text_of(answers["P-8"], "2. the answer")


def test_p9_no_function_fits(answers):
    text = text_of(answers["P-9"], "2. the answer")
    assert "Cannot answer" in text
    assert "BH-D001" in text
    assert answers["P-9"]["results"] == []
    assert "units" not in text_of(answers["P-9"], "3. figures")
