# The saved abstraction

Written by the `export` command from `abstraction.sqlite`. No model is called to write it.

## Documents

| ID | File | Kinds | Patient | Read | Claims | Hash |
|---|---|---|---|---|---|---|
| BH-D001 | group_authorization_letter.txt | authorization | HG-M042 | read | 2 | d2240979a2de |
| BH-D002 | intake_and_individual_jan05.txt | clinical_note | HG-M042 | read | 16 | 7f5f7d4bbfc9 |
| BH-D003 | signed_treatment_plan_jan05.txt | plan | HG-M042 | read | 14 | 3b3f50db40b3 |
| BH-D004 | group_facilitator_jan06.txt | clinical_note | HG-M042 | read | 11 | 5edddc6b2093 |
| BH-D005 | early_group_attendance_roster.txt | attendance_record | HG-M042 | read | 16 | 6f205f89f8d3 |
| BH-D006 | early_appointment_status_export.txt | schedule_export | HG-M042 | read | 34 | 0bf056f3769e |
| BH-D007 | family_primary_jan09.txt | clinical_note | HG-M042 | read | 16 | 924dee06b05c |
| BH-D008 | family_cofacilitator_jan09.txt | clinical_note | HG-M042 | read | 14 | ad416fbda806 |
| BH-D009 | group_facilitator_jan12.txt | clinical_note | HG-M042 | read | 11 | d30d18d0335d |
| BH-D010 | medication_review_jan13.txt | clinical_note | HG-M042 | read | 15 | 95debafd3a72 |
| BH-D011 | individual_therapy_jan14.txt | clinical_note | HG-M042 | read | 16 | 8c2fbaf5bb45 |
| BH-D012 | partner_collateral_jan16.txt | clinical_note | HG-M042 | read | 15 | 432c973d1a4d |
| BH-D013 | symptom_measure_review_jan16.txt | questionnaire_review | HG-M042 | read | 14 | 300a30dbe42b |
| BH-D014 | imported_measure_summary_received_jan26.txt | import_receipt | HG-M042 | read | 10 | 85e2c780abde |
| BH-D015 | missed_visit_outreach_jan08.txt | scheduling_log | HG-M042 | read | 11 | 4521a120a4d7 |
| BH-D016 | group_cancellation_notice_jan15.txt | cancellation_notice | HG-M042 | read | 11 | 5f3375f11c85 |
| BH-D101 | BH-D101_group_content_2026-01-19.txt | clinical_note | HG-M042 | read | 14 | 05a234a8adc9 |
| BH-D102 | BH-D102_original_attendance_2026-01-19.txt | attendance_record | HG-M042 | read | 10 | 514ca20809f6 |
| BH-D103 | BH-D103_attendance_correction_2026-01-20.txt | correction | HG-M042 | read | 12 | 674440968b5d |
| BH-D104 | BH-D104_resent_roster_received_2026-01-26.txt | cover_sheet, attendance_record | HG-M042 | read | 12 | f3f25065559f |
| BH-D105 | BH-D105_individual_2026-01-19.txt | clinical_note | HG-M042 | read | 17 | 91fd8e8b1b31 |
| BH-D106 | BH-D106_telehealth_2026-01-21.txt | clinical_note, platform_export | HG-M042 | read | 18 | 09c946a2248a |
| BH-D107 | BH-D107_group_activity_records_2026-01-22_and_29.txt | clinical_note | HG-M042 | read | 15 | c5953bcb242e |
| BH-D108 | BH-D108_final_attendance_and_cancellation_register.txt | attendance_record | HG-M042 | read | 27 | 805b2c69c7fa |
| BH-D109 | BH-D109_care_coordination_2026-01-23.txt | clinical_note | HG-M042 | read | 11 | 069ea4112779 |
| BH-D110 | BH-D110_individual_primary_record_2026-01-26.txt | clinical_note | HG-M042 | read | 15 | 4b64c46a13b8 |
| BH-D111 | BH-D111_individual_second_record_2026-01-26.txt | clinical_note | HG-M042 | read | 18 | d03451942797 |
| BH-D112 | BH-D112_draft_note_and_charge_extract_2026-01-27.txt | draft_note, billing_extract | HG-M042 | read | 9 | b4390ed6b672 |
| BH-D113 | BH-D113_family_therapy_2026-01-30.txt | clinical_note | HG-M042 | read | 17 | 36764827bcb3 |
| BH-D114 | BH-D114_medication_management_2026-01-30.txt | clinical_note | HG-M042 | read | 15 | 9942bd886fcd |
| BH-D115 | BH-D115_symptom_measure_review_2026-01-30.txt | questionnaire_review | HG-M042 | read | 14 | 4a3859fd81fc |

## What the record establishes

Worked out by code from the claims further down. No model takes part.

### Patient HG-M042, Rowan Mercer

#### Plan

| Value | Read from the plan |
|---|---|
| Document | BH-D003 |
| Signed | 2026-01-05T13:05 |
| In effect | 2026-01-05 to 2026-01-30 |
| Required | at least 150 minutes each week, at least 3 therapy days each week |
| Week starts on | monday |
| Counted classes | family therapy, group therapy, individual therapy |
| Excluded classes | care coordination, collateral contact, medication management |

#### Encounters

| Encounter | Date | Class | Status | Present | Removed | Minutes | Counts | Documents | Notes |
|---|---|---|---|---|---|---|---|---|---|
| HG-E101 | 2026-01-05 | individual therapy | held | 09:00–09:50 |  | 50 | yes | BH-D002, BH-D006 |  |
| HG-E102 | 2026-01-06 | group therapy | held, in part | 10:15–11:15 | 10:45–11:00 | 45 | yes | BH-D004, BH-D005, BH-D006 | arrived after the start; left before the end |
| HG-E103 | 2026-01-08 | individual therapy | no show |  |  |  | no: no-show | BH-D006, BH-D015 |  |
| HG-E104 | 2026-01-09 | family therapy | held | 14:00–14:45 |  | 45 | yes | BH-D006, BH-D007, BH-D008, BH-D015 |  |
| HG-E105 | 2026-01-12 | group therapy | held | 10:00–11:30 | 10:40–10:55 | 75 | yes | BH-D005, BH-D006, BH-D009 |  |
| HG-E106 | 2026-01-13 | medication management | held | 09:00–09:25 |  | 25 | no: a class of service the plan excludes | BH-D006, BH-D010 |  |
| HG-E107 | 2026-01-14 | individual therapy | held | 11:00–11:45 |  | 45 | yes | BH-D006, BH-D011 |  |
| HG-E108 | 2026-01-15 | group therapy | cancelled by clinic |  |  |  | no: cancelled by the clinic | BH-D006, BH-D016 |  |
| HG-E109 | 2026-01-16 | collateral contact | held without patient |  |  | 40 without the patient | no: held with the patient absent | BH-D006, BH-D012 |  |
| HG-E110 | 2026-01-19 | group therapy | held, in part | 10:00–11:15 |  | 75 | yes | BH-D101, BH-D102, BH-D103, BH-D104 | left before the end |
| HG-E111 | 2026-01-19 | individual therapy | held | 11:15–11:45 |  | 30 | yes | BH-D101, BH-D103, BH-D105 |  |
| HG-E112 | 2026-01-21 | individual therapy | held | 13:00–13:55 | 13:20–13:30 | 45 | yes | BH-D106 |  |
| HG-E113 | 2026-01-22 | group therapy | held, in part | 10:30–11:30 | 10:45–11:00 | 45 | yes | BH-D107, BH-D108 | arrived after the start |
| HG-E114 | 2026-01-23 | care coordination | held without patient |  |  | 20 without the patient | no: held with the patient absent | BH-D109 |  |
| HG-E115 | 2026-01-26 | individual therapy | held | 09:00–09:50 or 09:10–09:50 |  | 50 or 40 | yes | BH-D110, BH-D111 |  |
| HG-E116 | 2026-01-27 | group therapy | no show |  |  |  | no: no-show | BH-D108, BH-D112 |  |
| HG-E117 | 2026-01-28 | individual therapy | cancelled by patient |  |  |  | no: cancelled by the patient | BH-D108 |  |
| HG-E118 | 2026-01-29 | group therapy | held | 10:00–11:30 | 10:45–11:00 | 75 | yes | BH-D107, BH-D108 |  |
| HG-E119 | 2026-01-30 | family therapy | held, in part | 13:15–13:45 |  | 30; 15 without the patient | yes | BH-D113 | joined after the start |
| HG-E120 | 2026-01-30 | medication management | held | 15:00–15:20 |  | 20 | no: a class of service the plan excludes | BH-D114 | the patient's presence is taken from the interval of the contact |

#### Administrative records

Kept, and not counted as encounters.

| Date | Class | As written | How | Documents |
|---|---|---|---|---|
| 2026-01-08 | scheduling contact | Outbound call / returned call | telephone | BH-D015 |
| 2026-01-15 | scheduling contact | Rowan called the desk | telephone | BH-D016 |
| 2026-01-30 | questionnaire review | questionnaire review within ongoing care |  | BH-D115 |

#### Conflicts

| Conflict | Field | Values | Outcome | Rule | What would settle it |
|---|---|---|---|---|---|
| HG-M042/HG-E110:departure | departure | 11:15 (BH-D103); 11:30 (BH-D102, BH-D104) | settled: 11:15 | 8, then 9 |  |
| HG-M042/HG-E115:start | start | 09:00 (BH-D110); 09:10 (BH-D111) | open | 11 | An arrival or check-in record, or a correction by the author of the record being changed. |
| HG-M042/HG-E116:attendance | attendance | attended (BH-D112); did not attend (BH-D108) | settled: did not attend | 10 |  |

#### Findings

| Finding | Contact | Detail |
|---|---|---|
| note signed after the service date | HG-M042/HG-E104 | The note in BH-D008 was signed on 2026-01-10, after the service date 2026-01-09. |
| charge without attendance | HG-M042/HG-E116 | A charge (CH-116, Group psychotherapy) is posted for a contact whose status is no show. This is an inconsistency between documentation and billing. The record does not show whether the charge was later reviewed or reversed. It is not a finding of improper billing. |
| draft made before the service | HG-M042/HG-E116 | A draft note for this contact was made before the service it describes. |

#### Assessments

| Instrument | Completed | Score | Form | Items | Copies | Mentions |
|---|---|---|---|---|---|---|
| PHQ-9 | 2026-01-05 | 18 |  |  | 0 | 1 |
| PHQ-9 | 2026-01-16 08:17 | 14 | HG-Q116 |  | 2 | 0 |
| PHQ-9 | 2026-01-30 12:42 | 10 |  | item 9: 0 | 0 | 0 |

#### Weekly status

| Week | Days | Dates | Minutes | Hours | Verdict | Margin | Depends on | Dates with no document |
|---|---|---|---|---|---|---|---|---|
| 2026-01-05 to 2026-01-11 | 3 | 2026-01-05, 2026-01-06, 2026-01-09 | 140 | 2.33 | not met | 10 minutes short |  | 2026-01-07, 2026-01-11 |
| 2026-01-12 to 2026-01-18 | 2 | 2026-01-12, 2026-01-14 | 120 | 2.00 | not met | 1 day short, 30 minutes short |  | 2026-01-17, 2026-01-18 |
| 2026-01-19 to 2026-01-25 | 3 | 2026-01-19, 2026-01-21, 2026-01-22 | 195 | 3.25 | met | 45 minutes over |  | 2026-01-24, 2026-01-25 |
| 2026-01-26 to 2026-02-01 (partial) | 3 | 2026-01-26, 2026-01-29, 2026-01-30 | 145 or 155 | 2.42 or 2.58 | cannot determine | 5 minutes short or 5 minutes over | HG-M042/HG-E115:start | 2026-01-31, 2026-02-01 |

#### Totals, 2026-01-05 to 2026-01-30

| Measure | Value |
|---|---|
| Sessions | 12 |
| Therapy days | 11 |
| Minutes | 600 or 610 |
| Hours | 10.00 or 10.17 |
| family therapy | 2 sessions, 75 minutes |
| group therapy | 5 sessions, 315 minutes |
| individual therapy | 5 sessions, 210 or 220 minutes |

## What each document says

### BH-D001: group_authorization_letter.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | authorization | Administrative correspondence | not_stated |  |  | received 2026-01-04 15:26; entered 2026-01-05 08:05; period_start 2026-01-05; period_end 2026-01-30 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | statement |  |  | says: not_an_attendance_record | 15 | "No service attendance record accompanies this letter." |  |
| 002 | 1 | statement |  |  | says: not_a_visit | 12 | "Scheduling remains the responsibility of Harbor Grove Behavioral Health and the member." |  |

Coverage: 10 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-A260104-88 | not captured |

### BH-D002: intake_and_individual_jan05.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-19 | clinical_note |  | signed by Mara Voss, 2026-01-05 12:18 |  |  | service 2026-01-05; signed 2026-01-05 12:18 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E101 2026-01-05 | individual_therapy |  | 8 | "Patient-present individual therapy: 09:00–09:50 local; completed, 50 minutes." |  |
| 002 | 1 | time | HG-E101 2026-01-05 | individual_therapy | end: 09:50; label: not_labelled; position: header; start: 09:00; what: patient_present | 8 | "Patient-present individual therapy: 09:00–09:50 local; completed, 50 minutes." |  |
| 003 | 1 | attendance | HG-E101 2026-01-05 | individual_therapy | status: completed; status_as_written: completed | 8 | "Patient-present individual therapy: 09:00–09:50 local; completed, 50 minutes." |  |
| 004 | 1 | participant | HG-E101 2026-01-05 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 13 | "Rowan arrived independently and participated throughout the appointment." |  |
| 005 | 1 | participant | HG-E101 2026-01-05 | individual_therapy | name: Mara Voss; presence: not_stated; role: clinician | 7 | "Clinician: Mara Voss, LCSW" |  |
| 006 | 1 | stated_minutes | HG-E101 2026-01-05 | individual_therapy | minutes: 50; of: patient_present | 8 | "Patient-present individual therapy: 09:00–09:50 local; completed, 50 minutes." |  |
| 007 | 1 | score |  |  | completed_date: 2026-01-05; instrument: PHQ-9; relation: completion; score: 18 | 15 | "PHQ-9 completed by Rowan on 2026-01-05: total score 18." |  |
| 008 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: several weeks of low mood, reduced interest; topic: mood | 11 | "Rowan describes several weeks of low mood, reduced interest in usual activities, fragmented sleep, and difficulty beginning ordinary tasks." |  |
| 009 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: fragmented sleep; topic: sleep | 11 | "Rowan describes several weeks of low mood, reduced interest in usual activities, fragmented sleep, and difficulty beginning ordinary tasks." |  |
| 010 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: worry about returning to work; topic: anxiety | 11 | "Worry increases when thinking about returning to work after a recent leave." |  |
| 011 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: postponing emails, avoiding conversations, more time alone; topic: functioning | 11 | "Rowan has been postponing email replies, avoiding conversations about the return date, and spending more time alone at home." |  |
| 012 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: no immediate safety concern identified; topic: safety | 13 | "No immediate safety concern was identified in today's assessment;" |  |
| 013 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: affect subdued but responsive; topic: mood | 13 | "Affect was subdued but responsive, especially when discussing their partner's support." |  |
| 014 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: waking at night, checking time; topic: sleep | 13 | "Rowan described waking in the night and then checking the time repeatedly." |  |
| 015 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Rowan chose to open work inbox for five minutes; topic: functioning | 17 | "Rowan selected opening their work inbox for five minutes without requiring an immediate reply." |  |
| 016 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: consented to partner in family visit; topic: functioning | 19 | "Rowan consented to involving their partner in a family visit focused on practical support." |  |

Coverage: 13 times, dates and record numbers in the document. 11 captured, 1 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E101 | captured on another line |
| 11 | date | January 30 | not captured |

### BH-D003: signed_treatment_plan_jan05.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 4-20 | plan | Outpatient treatment plan | signed by Mara Voss, LCSW, 2026-01-05 13:05 |  |  | signed 2026-01-05 13:05; other 2026-01-05 13:12; period_start 2026-01-05; period_end 2026-01-30 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: depressed mood; topic: mood | 10 | "Presenting needs: depressed mood, sleep disruption, anxiety about resuming work responsibilities, and avoidance of tasks and communication." |  |
| 002 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: sleep disruption; topic: sleep | 10 | "Presenting needs: depressed mood, sleep disruption, anxiety about resuming work responsibilities, and avoidance of tasks and communication." |  |
| 003 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: anxiety about returning to work; topic: anxiety | 10 | "Presenting needs: depressed mood, sleep disruption, anxiety about resuming work responsibilities, and avoidance of tasks and communication." |  |
| 004 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: avoidance of tasks and communication; topic: functioning | 10 | "Presenting needs: depressed mood, sleep disruption, anxiety about resuming work responsibilities, and avoidance of tasks and communication." |  |
| 005 | 1 | plan_rule |  |  | end_date: 2026-01-30; rule: episode_period; start_date: 2026-01-05 | 6 | "Episode dates: 2026-01-05 through 2026-01-30" |  |
| 006 | 1 | plan_rule |  |  | measure: therapy_days; minimum: 3; period: week; rule: requirement | 12 | "at least 3 therapy days" |  |
| 007 | 1 | plan_rule |  |  | measure: minutes; minimum: 150; period: week; rule: requirement | 12 | "at least 150 minutes of patient-present therapy in each Monday–Sunday week" |  |
| 008 | 1 | plan_rule |  |  | rule: week_definition; week_starts_on: monday | 12 | "each Monday–Sunday week" |  |
| 009 | 1 | plan_rule |  |  | patient_must_be_present: True; rule: therapy_day_definition; service_classes: individual_therapy, group_therapy, family_therapy | 12 | "A therapy day is a calendar day on which Rowan participates in individual, group, or family psychotherapy." |  |
| 010 | 1 | plan_rule |  |  | patient_must_be_present: True; rule: counted_service; service_classes: individual_therapy, group_therapy, family_therapy | 12 | "Patient-present individual, group, and family therapy contribute to the minute goal." |  |
| 011 | 1 | plan_rule |  |  | rule: excluded_service; service_classes: medication_management, collateral_contact, care_coordination | 12 | "Medication management, contacts with collateral informants only, and care coordination do not contribute." |  |
| 012 | 1 | plan_rule |  |  | goal_number: 1; rule: clinical_goal; text: improve daily activity and task initiation | 14 | "Goal 1: improve daily activity and task initiation." |  |
| 013 | 1 | plan_rule |  |  | goal_number: 2; rule: clinical_goal; text: improve coping with anxiety and disrupted sleep | 16 | "Goal 2: improve coping with anxiety and disrupted sleep." |  |
| 014 | 1 | plan_rule |  |  | goal_number: 3; rule: clinical_goal; text: support a workable return to employment | 18 | "Goal 3: support a workable return to employment." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D004: group_facilitator_jan06.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-14 | clinical_note |  | signed by Leena Park, 2026-01-06 12:02 |  |  | service 2026-01-06; signed 2026-01-06 12:02 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E102 2026-01-06 | group_therapy |  | 4 | "Harbor Grove Behavioral Health \| Coping skills group" |  |
| 002 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 5 | "Service date 2026-01-06 \| Group scheduled 10:00–11:30 local" |  |
| 003 | 1 | time | HG-E102 2026-01-06 | group_therapy | detail: break, whole group; end: 11:00; label: actual; position: body; start: 10:45; what: no_therapy_interval | 12 | "The whole group took a break from 10:45 to 11:00." |  |
| 004 | 1 | participant | HG-E102 2026-01-06 | group_therapy | name: Leena Park; presence: not_stated; role: clinician; role_as_written: Facilitator | 7 | "Facilitator: Leena Park, LPC" |  |
| 005 | 1 | participant | HG-E102 2026-01-06 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 14 | "Rowan was quiet initially and responded when invited to identify a situation involving avoidance." |  |
| 006 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: Rowan delayed replying to work message, fearing firm return date question; topic: functioning | 14 | "They described delaying a reply to a work message because they feared being asked for a firm return date." |  |
| 007 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: Rowan chose reading the message before deciding response as next step; topic: functioning | 14 | "Rowan practiced a breathing exercise and selected reading the message before deciding how to respond as a possible next step." |  |
| 008 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: Participation relevant, receptive to peers; topic: progress | 14 | "Their participation was relevant to the topic, and they appeared receptive to peer suggestions." |  |
| 009 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: Group focus on early physical anxiety signs and coping response; topic: reason_for_contact | 10 | "Group focus: recognizing early physical signs of anxiety and choosing a coping response before withdrawing from a task." |  |
| 010 | 1 | statement | HG-E102 2026-01-06 | group_therapy | says: no_therapy_provided | 12 | "No therapy was conducted during that interval." |  |
| 011 | 1 | statement | HG-E102 2026-01-06 | group_therapy | says: not_an_attendance_record | 14 | "The patient attendance roster is maintained by the group desk." |  |

Coverage: 11 times, dates and record numbers in the document. 10 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E102 | captured on another line |

### BH-D005: early_group_attendance_roster.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 4-17 | attendance_record | Group desk attendance extract | not_stated |  |  | exported_or_prepared 2026-01-12 15:10 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E102 2026-01-06 | group_therapy |  | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 002 | 1 | contact | HG-E105 2026-01-12 | group_therapy |  | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 003 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 004 | 1 | time | HG-E102 2026-01-06 | group_therapy | label: actual; position: table; start: 10:15; what: patient_arrival | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 005 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:15; label: actual; position: table; what: patient_departure | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 006 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 007 | 1 | time | HG-E105 2026-01-12 | group_therapy | label: actual; position: table; start: 10:00; what: patient_arrival | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 008 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 009 | 1 | attendance | HG-E102 2026-01-06 | group_therapy | status: attended_part; status_as_written: Attended part | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 010 | 1 | attendance | HG-E105 2026-01-12 | group_therapy | status: attended; status_as_written: Attended full | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 011 | 1 | participant |  |  | name: Rowan Mercer; presence: not_stated; role: patient | 5 | "Patient: Rowan Mercer \| DOB 1991-04-12 \| MRN HG-M042" |  |
| 012 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: staff; summary: Running behind after parking difficulty; topic: reason_for_contact | 13 | "Rowan called from the building entrance to say they were running behind after difficulty finding parking." |  |
| 013 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: staff; summary: Advised they would leave early for arranged ride; topic: functioning | 13 | "Rowan advised the facilitator that they would need to leave early for a previously arranged ride." |  |
| 014 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: staff; summary: No transport concern reported; topic: other | 15 | "No transport concern was reported at that time." |  |
| 015 | 1 | statement |  |  | says: prepared_from_signed_record | 17 | "Prepared from the signed reception attendance sheet for the two dates listed." |  |
| 016 | 1 | statement |  |  | says: other | 17 | "Session activities and room breaks are documented in the facilitator's record." |  |

Coverage: 19 times, dates and record numbers in the document. 19 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D006: early_appointment_status_export.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-20 | schedule_export | Appointment desk export | not_stated |  |  | exported_or_prepared 2026-01-16 16:50 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E101 2026-01-05 | individual_therapy |  | 10 | "HG-E101   \| Jan05 \| Individual therapy     \| 09:00–09:50    \| Completed" |  |
| 002 | 1 | contact | HG-E102 2026-01-06 | group_therapy |  | 11 | "HG-E102   \| Jan06 \| Coping skills group    \| 10:00–11:30    \| Attended part" |  |
| 003 | 1 | contact | HG-E103 2026-01-08 | individual_therapy |  | 12 | "HG-E103   \| Jan08 \| Individual therapy     \| 11:00–11:45    \| No show" |  |
| 004 | 1 | contact | HG-E104 2026-01-09 | family_therapy |  | 13 | "HG-E104   \| Jan09 \| Family therapy         \| 14:00–14:45    \| Completed" |  |
| 005 | 1 | contact | HG-E105 2026-01-12 | group_therapy |  | 14 | "HG-E105   \| Jan12 \| Coping skills group    \| 10:00–11:30    \| Completed" |  |
| 006 | 1 | contact | HG-E106 2026-01-13 | medication_management |  | 15 | "HG-E106   \| Jan13 \| Medication management  \| 09:00–09:25    \| Completed" |  |
| 007 | 1 | contact | HG-E107 2026-01-14 | individual_therapy |  | 16 | "HG-E107   \| Jan14 \| Individual therapy     \| 11:00–11:45    \| Completed" |  |
| 008 | 1 | contact | HG-E108 2026-01-15 | group_therapy |  | 17 | "HG-E108   \| Jan15 \| Coping skills group    \| 10:00–11:30    \| Clinic cancelled" |  |
| 009 | 1 | contact | HG-E109 HG-E109 2026-01-16 | collateral_contact |  | 18 | "HG-E109   \| Jan16 \| Family collateral      \| 14:00–14:40    \| Completed" |  |
| 010 | 1 | time | HG-E101 2026-01-05 | individual_therapy | end: 09:50; label: scheduled; position: table; start: 09:00; what: contact_interval | 10 | "HG-E101   \| Jan05 \| Individual therapy     \| 09:00–09:50    \| Completed" |  |
| 011 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 11 | "HG-E102   \| Jan06 \| Coping skills group    \| 10:00–11:30    \| Attended part" |  |
| 012 | 1 | time | HG-E103 2026-01-08 | individual_therapy | end: 11:45; label: scheduled; position: table; start: 11:00; what: contact_interval | 12 | "HG-E103   \| Jan08 \| Individual therapy     \| 11:00–11:45    \| No show" |  |
| 013 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: scheduled; position: table; start: 14:00; what: contact_interval | 13 | "HG-E104   \| Jan09 \| Family therapy         \| 14:00–14:45    \| Completed" |  |
| 014 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 14 | "HG-E105   \| Jan12 \| Coping skills group    \| 10:00–11:30    \| Completed" |  |
| 015 | 1 | time | HG-E106 2026-01-13 | medication_management | end: 09:25; label: scheduled; position: table; start: 09:00; what: contact_interval | 15 | "HG-E106   \| Jan13 \| Medication management  \| 09:00–09:25    \| Completed" |  |
| 016 | 1 | time | HG-E107 2026-01-14 | individual_therapy | end: 11:45; label: scheduled; position: table; start: 11:00; what: contact_interval | 16 | "HG-E107   \| Jan14 \| Individual therapy     \| 11:00–11:45    \| Completed" |  |
| 017 | 1 | time | HG-E108 2026-01-15 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 17 | "HG-E108   \| Jan15 \| Coping skills group    \| 10:00–11:30    \| Clinic cancelled" |  |
| 018 | 1 | time | HG-E109 HG-E109 2026-01-16 | collateral_contact | end: 14:40; label: scheduled; position: table; start: 14:00; what: contact_interval | 18 | "HG-E109   \| Jan16 \| Family collateral      \| 14:00–14:40    \| Completed" |  |
| 019 | 1 | attendance | HG-E101 2026-01-05 | individual_therapy | status: completed; status_as_written: Completed | 10 | "HG-E101   \| Jan05 \| Individual therapy     \| 09:00–09:50    \| Completed" |  |
| 020 | 1 | attendance | HG-E102 2026-01-06 | group_therapy | status: attended_part; status_as_written: Attended part | 11 | "HG-E102   \| Jan06 \| Coping skills group    \| 10:00–11:30    \| Attended part" |  |
| 021 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | status: no_show; status_as_written: No show | 12 | "HG-E103   \| Jan08 \| Individual therapy     \| 11:00–11:45    \| No show" |  |
| 022 | 1 | attendance | HG-E104 2026-01-09 | family_therapy | status: completed; status_as_written: Completed | 13 | "HG-E104   \| Jan09 \| Family therapy         \| 14:00–14:45    \| Completed" |  |
| 023 | 1 | attendance | HG-E105 2026-01-12 | group_therapy | status: completed; status_as_written: Completed | 14 | "HG-E105   \| Jan12 \| Coping skills group    \| 10:00–11:30    \| Completed" |  |
| 024 | 1 | attendance | HG-E106 2026-01-13 | medication_management | status: completed; status_as_written: Completed | 15 | "HG-E106   \| Jan13 \| Medication management  \| 09:00–09:25    \| Completed" |  |
| 025 | 1 | attendance | HG-E107 2026-01-14 | individual_therapy | status: completed; status_as_written: Completed | 16 | "HG-E107   \| Jan14 \| Individual therapy     \| 11:00–11:45    \| Completed" |  |
| 026 | 1 | attendance | HG-E108 2026-01-15 | group_therapy | reason: staff illness; status: cancelled_by_clinic; status_as_written: Clinic cancelled | 17 | "HG-E108   \| Jan15 \| Coping skills group    \| 10:00–11:30    \| Clinic cancelled" |  |
| 027 | 1 | attendance | HG-E109 HG-E109 2026-01-16 | collateral_contact | status: completed; status_as_written: Completed | 18 | "HG-E109   \| Jan16 \| Family collateral      \| 14:00–14:40    \| Completed" |  |
| 028 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | status: other; status_as_written: remained unarrived at close of its appointment slot | 20 | "Desk comments: HG-E103 remained unarrived at close of its appointment slot on January 8." |  |
| 029 | 1 | attendance | HG-E109 HG-E109 2026-01-16 | collateral_contact | reason: could not attend; status: absent; status_as_written: Rowan could not attend | 20 | "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend." |  |
| 030 | 1 | participant | HG-E109 HG-E109 2026-01-16 | collateral_contact | name: Rowan Mercer; presence: absent; role: patient | 20 | "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend." |  |
| 031 | 1 | observation | HG-E108 2026-01-15 | group_therapy | date: 2026-01-15; speaker: staff; summary: staff illness reported, group removed from schedule; topic: other | 20 | "HG-E108 was removed from the active room schedule after staff illness was reported." |  |
| 032 | 1 | observation | HG-E109 HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: staff; summary: retained as partner collateral contact after patient could not attend; topic: reason_for_contact | 20 | "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend." |  |
| 033 | 1 | statement | HG-E109 HG-E109 2026-01-16 | collateral_contact | says: separate_contact | 20 | "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend." |  |
| 034 | 1 | statement |  |  | says: not_an_attendance_record | 7 | "View: appointments January 5–16, 2026; times local" |  |

Coverage: 47 times, dates and record numbers in the document. 41 captured, 6 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | date | January 5–16, 2026 | captured on another line |
| 7 | date | January 5–16, 2026 | captured on another line |
| 20 | date | January 8 | captured on another line |
| 20 | number | HG-E103 | captured on another line |
| 20 | number | HG-E108 | captured on another line |
| 20 | number | HG-E109 | captured on another line |

### BH-D007: family_primary_jan09.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 4-18 | clinical_note | Family psychotherapy | signed by Mara Voss, 2026-01-09 16:24 |  |  | service 2026-01-09 14:00; signed 2026-01-09 16:24 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E104 2026-01-09 | family_therapy |  | 4 | "Harbor Grove Behavioral Health \| Family psychotherapy" |  |
| 002 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: not_labelled; position: header; start: 14:00; what: contact_interval | 6 | "Encounter HG-E104 \| 2026-01-09, 14:00–14:45 local" |  |
| 003 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Rowan Mercer; presence: present; role: patient | 7 | "Present: Rowan and partner, Casey Mercer" |  |
| 004 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Casey Mercer; presence: present; role: family_or_partner | 7 | "Present: Rowan and partner, Casey Mercer" |  |
| 005 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Mara Voss; presence: not_stated; role: clinician | 8 | "Clinicians: Mara Voss, LCSW; cofacilitator Leena Park, LPC" |  |
| 006 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Leena Park; presence: not_stated; role: clinician | 8 | "Clinicians: Mara Voss, LCSW; cofacilitator Leena Park, LPC" |  |
| 007 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Rowan Mercer; presence: present; role: patient | 16 | "Rowan remained present and engaged throughout the visit." |  |
| 008 | 1 | stated_minutes | HG-E104 2026-01-09 | family_therapy | minutes: 45; of: patient_present | 9 | "Patient-present family therapy duration: 45 minutes" |  |
| 009 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: Rowan felt watched when asked repeatedly about contacting work; topic: mood | 12 | "Rowan described feeling watched when asked repeatedly whether they had contacted work." |  |
| 010 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Casey worried space might leave Rowan isolated; topic: anxiety | 12 | "Casey described worry that giving Rowan space might leave them isolated." |  |
| 011 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Rowan rebuilding a routine; topic: functioning | 12 | "as Rowan attempts to rebuild a routine" |  |
| 012 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Rowan present and engaged throughout; topic: functioning | 16 | "Rowan remained present and engaged throughout the visit." |  |
| 013 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Casey agreed to a single planned check-in; topic: functioning | 16 | "Casey agreed to use a single planned check-in about work preparation instead of repeated reminders." |  |
| 014 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Rowan agreed to say when wanting practical help versus quiet company; topic: functioning | 16 | "Rowan agreed to say when they wanted practical assistance versus quiet company." |  |
| 015 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Plan to review check-in at next individual visit and continue activity steps; topic: progress | 18 | "Plan: try the planned check-in and review its effect at the next individual visit." |  |
| 016 | 1 | statement | HG-E104 2026-01-09 | family_therapy | says: other | 18 | "Leena Park's accompanying entry is filed under encounter HG-E104." |  |

Coverage: 10 times, dates and record numbers in the document. 8 captured, 2 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E104 | captured on another line |
| 18 | number | HG-E104 | captured on another line |

### BH-D008: family_cofacilitator_jan09.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 4-15 | clinical_note | Accompanying clinical entry | signed by Leena Park, 2026-01-10 08:42 |  |  | service 2026-01-09; signed 2026-01-10 08:42 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E104 2026-01-09 | family_therapy |  | 11 | "Accompanying clinical entry for the family appointment facilitated with Mara Voss." |  |
| 002 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: not_labelled; position: header; start: 14:00; what: contact_interval | 6 | "Encounter HG-E104 \| Date 2026-01-09 \| 14:00–14:45 local" |  |
| 003 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Rowan Mercer; presence: present; role: patient | 8 | "Participants: Rowan Mercer and Casey Mercer; both present for the full 45 minutes" |  |
| 004 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Casey Mercer; presence: present; role: family_or_partner | 8 | "Participants: Rowan Mercer and Casey Mercer; both present for the full 45 minutes" |  |
| 005 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Leena Park; presence: not_stated; role: clinician | 7 | "Author: Leena Park, LPC, cofacilitator with Mara Voss, LCSW" |  |
| 006 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Mara Voss; presence: not_stated; role: clinician | 7 | "Author: Leena Park, LPC, cofacilitator with Mara Voss, LCSW" |  |
| 007 | 1 | stated_minutes | HG-E104 2026-01-09 | family_therapy | minutes: 45; of: patient_present | 8 | "both present for the full 45 minutes" |  |
| 008 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: Rowan described partner reminders as evidence of falling behind; topic: anxiety | 11 | "Rowan initially described partner reminders as evidence that they were falling behind." |  |
| 009 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Reminders meant to help; repeated prompts increased tension; topic: other | 11 | "Casey explained that the reminders were an attempt to help" |  |
| 010 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Rehearsal became less defensive with repetition; topic: progress | 13 | "The rehearsal became less defensive with repetition." |  |
| 011 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Both contributed ideas for a brief check-in; topic: functioning | 13 | "Both participants contributed ideas for a brief, predictable check-in." |  |
| 012 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Couple selected a shared evening walk; topic: functioning | 15 | "The couple selected an evening walk as an activity they could share without making it a discussion about progress." |  |
| 013 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: Rowan said walk felt more acceptable than lengthy review of tasks; topic: functioning | 15 | "Rowan said this felt more acceptable than a lengthy review of unfinished tasks." |  |
| 014 | 1 | statement | HG-E104 2026-01-09 | family_therapy | says: other | 15 | "The agreed home practice and ongoing treatment plan are recorded in Mara Voss's primary note for HG-E104." |  |

Coverage: 10 times, dates and record numbers in the document. 8 captured, 2 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E104 | captured on another line |
| 15 | number | HG-E104 | captured on another line |

### BH-D009: group_facilitator_jan12.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Coping skills group | signed by Leena Park, 2026-01-12 12:20 |  |  | service 2026-01-12; signed 2026-01-12 12:20 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E105 2026-01-12 | group_therapy |  | 4 | "Harbor Grove Behavioral Health \| Coping skills group" |  |
| 002 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 6 | "Scheduled group 10:00–11:30 local" |  |
| 003 | 1 | time | HG-E105 2026-01-12 | group_therapy | detail: Group break; end: 10:55; label: actual; position: body; start: 10:40; what: no_therapy_interval | 12 | "Group break: 10:40–10:55; no therapeutic activity occurred during the break." |  |
| 004 | 1 | participant | HG-E105 2026-01-12 | group_therapy | name: Leena Park; presence: not_stated; role: clinician; role_as_written: Facilitator | 7 | "Facilitator: Leena Park, LPC" |  |
| 005 | 1 | participant | HG-E105 2026-01-12 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 14 | "Rowan contributed an example about leaving work messages unopened." |  |
| 006 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: clinician; summary: identified looking at one message as lower step; topic: functioning | 14 | "They identified looking at one message as a lower step than replying to every outstanding message." |  |
| 007 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: clinician; summary: took a walk with Casey over weekend; topic: functioning | 14 | "They also described taking a walk with Casey over the weekend" |  |
| 008 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: clinician; summary: walk helped evening feel less dominated by worry; topic: anxiety | 14 | "noted that it helped the evening feel less dominated by worry" |  |
| 009 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: clinician; summary: wrote down action to try after breakfast; topic: functioning | 14 | "Rowan wrote down an action to try after breakfast" |  |
| 010 | 1 | statement | HG-E105 2026-01-12 | group_therapy | says: no_therapy_provided | 12 | "no therapeutic activity occurred during the break" |  |
| 011 | 1 | statement | HG-E105 2026-01-12 | group_therapy | says: not_an_attendance_record | 16 | "Attendance is recorded on the group desk roster." |  |

Coverage: 11 times, dates and record numbers in the document. 10 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 5 | number | HG-E105 | captured on another line |

### BH-D010: medication_review_jan13.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 4-17 | clinical_note | Prescriber visit | signed by None, 2026-01-13 10:04 |  |  | service 2026-01-13; signed 2026-01-13 10:04 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E106 2026-01-13 | medication_management |  | 6 | "Encounter HG-E106 \| Date 2026-01-13" |  |
| 002 | 1 | time | HG-E106 2026-01-13 | medication_management | end: 09:25; label: actual; position: header; start: 09:00; what: contact_interval | 7 | "Actual visit 09:00–09:25 local; completed, 25 minutes" |  |
| 003 | 1 | attendance | HG-E106 2026-01-13 | medication_management | status: completed; status_as_written: completed | 7 | "Actual visit 09:00–09:25 local; completed, 25 minutes" |  |
| 004 | 1 | attendance | HG-E106 2026-01-13 | medication_management | status: attended; status_as_written: Rowan attended for medication management. | 11 | "Rowan attended for medication management." |  |
| 005 | 1 | participant | HG-E106 2026-01-13 | medication_management | name: Rowan Mercer; presence: present; role: patient | 11 | "Rowan attended for medication management." |  |
| 006 | 1 | participant | HG-E106 2026-01-13 | medication_management | name: Elias Brenner; presence: not_stated; role: clinician; role_as_written: NP | 8 | "Clinician: Elias Brenner, NP" |  |
| 007 | 1 | stated_minutes | HG-E106 2026-01-13 | medication_management | minutes: 25; of: contact_total | 7 | "Actual visit 09:00–09:25 local; completed, 25 minutes" |  |
| 008 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: continuing sleep interruption and daytime tiredness; topic: sleep | 11 | "Rowan reported continuing sleep interruption and daytime tiredness." |  |
| 009 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: mood somewhat less heavy on days with planned activity; topic: mood | 11 | "They described mood as somewhat less heavy on days with a planned activity" |  |
| 010 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: concerned about work communication; topic: functioning | 11 | "remained concerned about work communication" |  |
| 011 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: denied new medication-related concern requiring urgent intervention; topic: safety | 13 | "Rowan denied a new medication-related concern requiring urgent intervention." |  |
| 012 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: ongoing depressive and anxiety symptoms with sleep disruption; topic: progress | 15 | "Assessment: ongoing depressive and anxiety symptoms with sleep disruption." |  |
| 013 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: intends to continue scheduled appointments; topic: functioning | 15 | "intends to continue the scheduled appointments" |  |
| 014 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: medication monitoring will continue; topic: medication | 15 | "Medication monitoring will continue during the outpatient episode" |  |
| 015 | 1 | statement | HG-E106 2026-01-13 | medication_management | says: no_therapy_provided | 17 | "No separate psychotherapy component was provided or documented." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D011: individual_therapy_jan14.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 4-17 | clinical_note | Individual psychotherapy | signed by Mara Voss, 2026-01-14 13:16 |  |  | service 2026-01-14; signed 2026-01-14 13:16 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E107 2026-01-14 | individual_therapy |  | 4 | "Harbor Grove Behavioral Health \| Individual psychotherapy" |  |
| 002 | 1 | time | HG-E107 2026-01-14 | individual_therapy | end: 11:45; label: not_labelled; position: header; start: 11:00; what: patient_present | 7 | "Patient-present session 11:00–11:45 local; completed, 45 minutes" |  |
| 003 | 1 | attendance | HG-E107 2026-01-14 | individual_therapy | status: completed; status_as_written: completed | 7 | "Patient-present session 11:00–11:45 local; completed, 45 minutes" |  |
| 004 | 1 | participant | HG-E107 2026-01-14 | individual_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 5 | "Rowan Mercer \| DOB 1991-04-12 \| MRN HG-M042" |  |
| 005 | 1 | participant | HG-E107 2026-01-14 | individual_therapy | name: Mara Voss; presence: not_stated; role: clinician | 8 | "Clinician: Mara Voss, LCSW" |  |
| 006 | 1 | stated_minutes | HG-E107 2026-01-14 | individual_therapy | minutes: 45; of: patient_present | 7 | "Patient-present session 11:00–11:45 local; completed, 45 minutes" |  |
| 007 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: completed small activities: opened work message, two walks; topic: functioning | 11 | "Rowan reported completing several small activities since the prior individual appointment, including opening a work message and taking two short walks." |  |
| 008 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: continues to imagine being asked unanswerable questions; topic: anxiety | 11 | "continue to imagine being asked questions they cannot answer" |  |
| 009 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: sleep interrupted; topic: sleep | 11 | "Sleep remains interrupted" |  |
| 010 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: getting started in morning requires effort; topic: functioning | 11 | "getting started in the morning continues to require effort." |  |
| 011 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: family appointment helpful; topic: progress | 11 | "Rowan described the family appointment as helpful because the planned check-in with Casey reduced repeated reminders." |  |
| 012 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: noticed physical tension but remained with task; topic: anxiety | 13 | "Rowan noticed physical tension during the rehearsal but was able to remain with the task." |  |
| 013 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: message less overwhelming when not solving whole question; topic: anxiety | 13 | "They said the message seemed less overwhelming when it did not need to solve the entire return-to-work question." |  |
| 014 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: identified preparing appointment info evening before; topic: functioning | 15 | "Rowan identified setting out appointment information the evening before as a helpful preparation step." |  |
| 015 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: affect more varied than intake; worry about employment; topic: mood | 15 | "Affect was more varied than at intake, although worry was evident when discussing employment." |  |
| 016 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: plan to attempt drafted acknowledgment, track activity, practice breathing; topic: functioning | 17 | "Plan: attempt the drafted acknowledgment, continue morning activity tracking, and practice the breathing skill before an avoided task." |  |

Coverage: 9 times, dates and record numbers in the document. 8 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E107 | captured on another line |

### BH-D012: partner_collateral_jan16.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 4-17 | clinical_note | Family collateral | signed by Mara Voss, 2026-01-16 16:08 |  |  | service 2026-01-16; signed 2026-01-16 16:08 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E109 2026-01-16 | collateral_contact |  | 4 | "Harbor Grove Behavioral Health \| Family collateral" |  |
| 002 | 1 | time | HG-E109 2026-01-16 | collateral_contact | end: 14:40; label: not_labelled; position: header; start: 14:00; what: contact_interval | 6 | "Encounter HG-E109 \| Date 2026-01-16 \| 14:00–14:40 local" |  |
| 003 | 1 | attendance | HG-E109 2026-01-16 | collateral_contact | reason: Rowan advised the office that they could not participate; status: absent; status_as_written: Rowan was absent for the entire contact. | 8 | "Rowan was absent for the entire contact." |  |
| 004 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Casey Mercer; presence: present; role: family_or_partner; role_as_written: partner | 11 | "Casey attended the arranged contact" |  |
| 005 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Rowan Mercer; presence: absent; role: patient | 8 | "Rowan was absent for the entire contact." |  |
| 006 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Mara Voss; presence: not_stated; role: clinician | 7 | "Clinician: Mara Voss, LCSW" |  |
| 007 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Rowan getting out for short walks; topic: functioning | 13 | "Casey reported that Rowan had been getting out for short walks" |  |
| 008 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey Mercer; summary: more willing to discuss coming week; topic: progress | 13 | "seemed more willing to discuss the coming week" |  |
| 009 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: mornings remain difficult; topic: mood | 13 | "Mornings remain difficult" |  |
| 010 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Rowan quiet when talk turns to work; topic: functioning | 13 | "Casey described Rowan becoming quiet when the conversation turns to work." |  |
| 011 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: evening check-in reduced reminders; topic: functioning | 13 | "The scheduled evening check-in has reduced unplanned reminders." |  |
| 012 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: Casey will offer walk/meal and use check-in; topic: functioning | 15 | "Casey will continue to offer a walk or shared meal and will use the agreed check-in rather than repeated progress questions." |  |
| 013 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: Casey attended arranged contact as Rowan could not participate; topic: reason_for_contact | 11 | "Casey attended the arranged contact after Rowan advised the office that they could not participate." |  |
| 014 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: no_therapy_provided | 17 | "No patient-present psychotherapy occurred during this contact." |  |
| 015 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: no_patient_contact | 17 | "Rowan did not join in person, by telephone, or by video." |  |

Coverage: 9 times, dates and record numbers in the document. 8 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E109 | captured on another line |

### BH-D013: symptom_measure_review_jan16.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 4-15 | questionnaire_review | Measurement review | not_stated |  |  | completed 2026-01-16 08:17; reviewed 2026-01-16 09:10 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | 2026-01-16 | questionnaire_review |  | 4 | "Harbor Grove Behavioral Health \| Measurement review" |  |
| 002 | 1 | score |  |  | completed_date: 2026-01-16; completed_time: 08:17; form_id: HG-Q116; instrument: PHQ-9; relation: completion; score: 14 | 8 | "Total score: 14" |  |
| 003 | 1 | score |  |  | completed_date: 2026-01-05; instrument: PHQ-9; relation: mention; score: 18 | 11 | "The submitted score is lower than the intake score of 18 recorded on January 5." |  |
| 004 | 1 | observation |  |  | date: 2026-01-16; speaker: patient; speaker_name: Rowan; summary: getting out of apartment a little easier; topic: functioning | 11 | "Rowan wrote that getting out of the apartment had become a little easier" |  |
| 005 | 1 | observation |  |  | date: 2026-01-16; speaker: patient; speaker_name: Rowan; summary: thinking about work makes them want to put things off; topic: functioning | 11 | "thinking about work continued to make them want to put things off" |  |
| 006 | 1 | observation |  |  | date: 2026-01-16; speaker: patient; speaker_name: Rowan; summary: sleep inconsistent; topic: sleep | 11 | "Rowan also described sleep as inconsistent." |  |
| 007 | 1 | observation |  |  | date: 2026-01-16; speaker: clinician; summary: some improvement in depressive symptoms; topic: progress | 13 | "suggest some improvement in depressive symptoms" |  |
| 008 | 1 | observation |  |  | date: 2026-01-16; speaker: clinician; summary: persistent avoidance and difficulty initiating work communication; topic: functioning | 13 | "Persistent avoidance, difficulty initiating work communication, and sleep disruption remain clinically relevant." |  |
| 009 | 1 | observation |  |  | date: 2026-01-16; speaker: clinician; summary: sleep disruption remains relevant; topic: sleep | 13 | "Persistent avoidance, difficulty initiating work communication, and sleep disruption remain clinically relevant." |  |
| 010 | 1 | observation |  |  | date: 2026-01-16; speaker: clinician; summary: attempted small activities and communication practice; no reliable routine yet; topic: functioning | 13 | "Rowan has attempted small activities and communication practice but has not yet established a reliable routine." |  |
| 011 | 1 | observation |  |  | date: 2026-01-16; speaker: clinician; summary: continue current therapeutic focus; topic: progress | 13 | "Continue the current therapeutic focus" |  |
| 012 | 1 | statement |  |  | says: no_new_assessment | 11 | "No additional questionnaire was submitted with this update." |  |
| 013 | 1 | statement |  |  | says: not_a_visit | 15 | "no clinical appointment occurred at the time of review" |  |
| 014 | 1 | statement |  |  | says: no_clinical_service | 15 | "This entry records review of the portal submission; no clinical appointment occurred at the time of review." |  |

Coverage: 10 times, dates and record numbers in the document. 8 captured, 2 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | PHQ-9 | captured on another line |
| 6 | number | HG-Q116 | captured on another line |

### BH-D014: imported_measure_summary_received_jan26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 4-19 | import_receipt | Administrative import receipt | not_stated |  | copy; original signed by None, None | received 2026-01-26 07:44; completed 2026-01-16; reviewed 2026-01-16 09:10 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | score |  |  | completed_date: 2026-01-16; form_id: HG-Q116; instrument: PHQ-9; relation: copy; score: 14 | 13 | "PHQ-9   \| 14     \| 2026-01-16     \| HG-Q116" |  |
| 002 | 1 | score |  |  | completed_date: 2026-01-16; form_id: HG-Q116; instrument: PHQ-9; relation: copy; score: 14 | 17 | "Import detail: copied result from the January 16 portal form." |  |
| 003 | 1 | observation |  |  | date: 2026-01-16; speaker: outside_professional; speaker_name: Mara Voss, LCSW; summary: some improvement in depressive symptoms; topic: progress | 15 | "some improvement in depressive symptoms" |  |
| 004 | 1 | observation |  |  | date: 2026-01-16; speaker: outside_professional; speaker_name: Mara Voss, LCSW; summary: ongoing avoidance of work communication; topic: functioning | 15 | "ongoing avoidance of work communication" |  |
| 005 | 1 | observation |  |  | date: 2026-01-16; speaker: outside_professional; speaker_name: Mara Voss, LCSW; summary: inconsistent sleep; topic: sleep | 15 | "inconsistent sleep" |  |
| 006 | 1 | observation |  |  | date: 2026-01-16; speaker: outside_professional; speaker_name: Mara Voss, LCSW; summary: continue current therapeutic focus; topic: progress | 15 | "Continue current therapeutic focus" |  |
| 007 | 1 | statement |  |  | says: is_copy_or_resend | 17 | "Import detail: copied result from the January 16 portal form." |  |
| 008 | 1 | statement |  |  | says: no_new_assessment | 17 | "No newly completed patient questionnaire is included in this batch." |  |
| 009 | 1 | statement |  |  | says: not_a_visit | 19 | "does not document a visit with Rowan" |  |
| 010 | 1 | statement |  |  | says: no_new_signature | 19 | "This receipt was entered by the administrative desk" |  |

Coverage: 13 times, dates and record numbers in the document. 11 captured, 1 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-MEAS-0126 | not captured |
| 17 | date | January 26 | captured on another line |

### BH-D015: missed_visit_outreach_jan08.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | scheduling_log | Scheduling support log | not_stated |  |  | entered 2026-01-08 15:52 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E103 2026-01-08 | individual_therapy |  | 6 | "Related appointment: HG-E103, 2026-01-08, 11:00–11:45 local" |  |
| 002 | 1 | contact | 2026-01-09 | family_therapy |  | 13 | "The next scheduled appointment remained the family visit on January 9." |  |
| 003 | 1 | contact | 2026-01-08 | scheduling_contact |  | 15 | "15:36: Rowan returned the call." |  |
| 004 | 1 | modality | 2026-01-08 | scheduling_contact | modality: telephone | 15 | "Rowan returned the call." |  |
| 005 | 1 | time | HG-E103 2026-01-08 | individual_therapy | end: 11:45; label: scheduled; position: header; start: 11:00; what: contact_interval | 6 | "Related appointment: HG-E103, 2026-01-08, 11:00–11:45 local" |  |
| 006 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | reason: morning had gotten away from them after a poor night of sleep; status: no_show; status_as_written: Appointment marked no show | 11 | "11:45: Appointment marked no show." |  |
| 007 | 1 | participant | HG-E103 2026-01-08 | individual_therapy | name: Rowan Mercer; presence: absent; role: patient | 11 | "Rowan was not seen for the scheduled individual visit." |  |
| 008 | 1 | observation | 2026-01-08 | scheduling_contact | date: 2026-01-08; speaker: patient; summary: poor night of sleep; topic: sleep | 15 | "They said the morning had gotten away from them after a poor night of sleep" |  |
| 009 | 1 | observation | 2026-01-09 | family_therapy | date: 2026-01-08; speaker: patient; summary: still intends to attend next day's visit; topic: functioning | 15 | "confirmed that they still intended to attend the next day's visit with Casey" |  |
| 010 | 1 | statement | 2026-01-08 | scheduling_contact | says: no_therapy_provided | 17 | "No therapy intervention was conducted." |  |
| 011 | 1 | statement | 2026-01-08 | scheduling_contact | says: separate_contact | 17 | "The callback addressed scheduling and contact information." |  |

Coverage: 10 times, dates and record numbers in the document. 10 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D016: group_cancellation_notice_jan15.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | cancellation_notice | Patient copy | not_stated |  |  | entered 2026-01-15 08:12 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E108 2026-01-15 | group_therapy |  | 9 | "The coping skills group scheduled for January 15 from 10:00 to 11:30 is cancelled by the clinic because of staff illness." |  |
| 002 | 1 | contact | 2026-01-15 | scheduling_contact |  | 13 | "08:37: Rowan called the desk and acknowledged receiving the notice." |  |
| 003 | 1 | contact | 2026-01-16 | family_therapy |  | 13 | "the family-related appointment on January 16 remained on the schedule" |  |
| 004 | 1 | modality | 2026-01-15 | scheduling_contact | modality: telephone | 13 | "Rowan called the desk" |  |
| 005 | 1 | time | HG-E108 2026-01-15 | group_therapy | end: 11:30; label: scheduled; position: body; start: 10:00; what: contact_interval | 9 | "scheduled for January 15 from 10:00 to 11:30" |  |
| 006 | 1 | time | 2026-01-15 | scheduling_contact | label: actual; position: body; start: 08:37; what: other | 13 | "08:37: Rowan called the desk" |  |
| 007 | 1 | attendance | HG-E108 2026-01-15 | group_therapy | reason: staff illness; status: cancelled_by_clinic; status_as_written: cancelled by the clinic | 9 | "is cancelled by the clinic because of staff illness." |  |
| 008 | 1 | observation | HG-E108 2026-01-15 | group_therapy | date: 2026-01-15; speaker: clinician; summary: group cancelled due to staff illness; topic: reason_for_contact | 9 | "A covering facilitator is unavailable for this morning's group." |  |
| 009 | 1 | statement | HG-E108 2026-01-15 | group_therapy | says: no_therapy_provided | 15 | "No group was held and no participants were seen for HG-E108." |  |
| 010 | 1 | statement | HG-E108 2026-01-15 | group_therapy | says: no_therapy_provided | 15 | "No replacement group was conducted in the January 15 slot." |  |
| 011 | 1 | statement | 2026-01-15 | scheduling_contact | says: no_clinical_service | 15 | "The telephone contact was limited to confirming the cancellation and upcoming appointment information." |  |

Coverage: 12 times, dates and record numbers in the document. 9 captured, 3 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E108 | captured on another line |
| 15 | date | January 15 | captured on another line |
| 15 | number | HG-E108 | captured on another line |

### BH-D101: BH-D101_group_content_2026-01-19.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-14 | clinical_note | Skills group clinical record | signed by Leah Chen, LCSW, 2026-01-19 12:08 |  |  | service 2026-01-19; signed 2026-01-19 12:08 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 4 | "Group encounter: HG-E110 \| Facilitator: Leah Chen, LCSW" |  |
| 002 | 1 | contact | 2026-01-19 | individual_therapy |  | 10 | "arranged a same-day individual meeting with the treating clinician" |  |
| 003 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 6 | "Scheduled group: 10:00–11:30." |  |
| 004 | 1 | time | HG-E110 2026-01-19 | group_therapy | detail: Nontherapeutic break; end: 11:00; label: scheduled; position: header; start: 10:45; what: no_therapy_interval | 6 | "Nontherapeutic break: 10:45–11:00." |  |
| 005 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Leah Chen; presence: not_stated; role: clinician; role_as_written: Facilitator | 4 | "Facilitator: Leah Chen, LCSW" |  |
| 006 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 10 | "Rowan initially followed the exercise" |  |
| 007 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: identified postponing message to supervisor as familiar pattern; topic: functioning | 10 | "identified postponing a message to a supervisor as a familiar pattern" |  |
| 008 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: became visibly tense discussing return to workplace; topic: anxiety | 10 | "Rowan became visibly tense" |  |
| 009 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: patient; summary: said amount of discussion felt difficult to manage; topic: functioning | 10 | "said the amount of discussion felt difficult to manage" |  |
| 010 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: members selected a small approach behavior to attempt during the week; topic: functioning | 8 | "selected a small approach behavior they could attempt during the week" |  |
| 011 | 1 | observation | 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: same-day individual meeting arranged after difficulty in group; topic: reason_for_contact | 10 | "arranged a same-day individual meeting with the treating clinician" |  |
| 012 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: no_therapy_provided | 8 | "there was no facilitated discussion, assigned therapeutic activity, or patient treatment during that interval" |  |
| 013 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: not_an_attendance_record | 10 | "Patient-specific arrival and departure are maintained on the attendance roster." |  |
| 014 | 1 | statement | 2026-01-19 | individual_therapy | says: separate_contact | 10 | "arranged a same-day individual meeting with the treating clinician" |  |

Coverage: 11 times, dates and record numbers in the document. 11 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D102: BH-D102_original_attendance_2026-01-19.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-19 | attendance_record | Patient-specific attendance roster extract | signed by Leah Chen, LCSW, 2026-01-19 12:14 | Final |  | service 2026-01-19; signed 2026-01-19 12:14 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 4 | "Service date: January 19, 2026 \| Group encounter: HG-E110" |  |
| 002 | 1 | modality | HG-E110 2026-01-19 | group_therapy | modality: in_person | 6 | "Location: Outpatient skills room B" |  |
| 003 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 8 | "Scheduled opening: 10:00 \| Scheduled closing: 11:30" |  |
| 004 | 1 | time | HG-E110 2026-01-19 | group_therapy | label: actual; position: header; start: 10:00; what: patient_arrival | 9 | "Patient arrival: 10:00" |  |
| 005 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: actual; position: header; what: patient_departure | 9 | "Patient departure: 11:30" |  |
| 006 | 1 | attendance | HG-E110 2026-01-19 | group_therapy | status: attended; status_as_written: Attended | 9 | "Status: Attended" |  |
| 007 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 14 | "Rowan was present for the opening check-in." |  |
| 008 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: patient identified anxiety about reconnecting with work; topic: anxiety | 14 | "The patient identified anxiety about reconnecting with work and accepted an exercise handout." |  |
| 009 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: staff arranged access to individual clinician after patient requested help; topic: reason_for_contact | 14 | "Staff arranged access to the individual clinician after Rowan requested additional help." |  |
| 010 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 16 | "This roster is the original signed attendance entry for the listed service date." |  |

Coverage: 11 times, dates and record numbers in the document. 11 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D103: BH-D103_attendance_correction_2026-01-20.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | correction | Attendance correction | signed by Leah Chen, LCSW, 2026-01-20 08:42 | Final |  | entered 2026-01-20; service 2026-01-19; signed 2026-01-20 08:42 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 5 | "Applies to group encounter HG-E110, service date January 19, 2026" |  |
| 002 | 1 | contact | 2026-01-19 | individual_therapy |  | 11 | "the separate individual appointment" |  |
| 003 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:15; label: actual; position: body; what: patient_departure | 7 | "Patient departure for HG-E110 is 11:15, replacing the original roster value of 11:30." |  |
| 004 | 1 | time | HG-E110 2026-01-19 | group_therapy | label: actual; position: body; start: 10:00; what: patient_arrival | 7 | "Patient arrival remains 10:00." |  |
| 005 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:15; label: actual; position: body; what: patient_departure | 9 | "The room-transfer record shows Rowan leaving skills room B at 11:15" |  |
| 006 | 1 | time | 2026-01-19 | individual_therapy | label: actual; position: body; start: 11:15; what: patient_arrival | 9 | "being received by the individual clinician at 11:15" |  |
| 007 | 1 | time | HG-E110 2026-01-19 | group_therapy | detail: original roster departure value 11:30; end: 11:30; label: scheduled; position: body; what: other | 9 | "retain the scheduled group closing time in Rowan's departure field" |  |
| 008 | 1 | participant |  |  | name: Rowan Mercer; presence: not_stated; role: patient | 4 | "Patient: Rowan Mercer \| DOB: 1991-04-12 \| MRN: HG-M042" |  |
| 009 | 1 | participant |  |  | name: Leah Chen; presence: not_stated; role: clinician | 15 | "Electronically signed: Leah Chen, LCSW \| January 20, 2026, 08:42" |  |
| 010 | 1 | correction | HG-E110 2026-01-19 | group_therapy | field: departure; new_value: 11:15; old_value: 11:30; reason: original roster retained the scheduled group closing time in the departure field | 7 | "Patient departure for HG-E110 is 11:15, replacing the original roster value of 11:30." |  |
| 011 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: no_clinical_service | 13 | "No additional clinical service was provided in making this correction." |  |
| 012 | 1 | statement | 2026-01-19 | individual_therapy | says: separate_contact | 11 | "the separate individual appointment" |  |

Coverage: 15 times, dates and record numbers in the document. 14 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-E110 | captured on another line |

### BH-D104: BH-D104_resent_roster_received_2026-01-26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-8 | cover_sheet | Records inbox cover sheet | not_stated |  |  | received 2026-01-26 16:22 |
| 2 | 10-21 | attendance_record | ATTACHED ROSTER COPY | unsigned | Final, signed | copy; original signed by Leah Chen, LCSW, 2026-01-19 12:14 | service 2026-01-19; signed 2026-01-19 12:14; entered 2026-01-26 16:31 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 2 | contact | HG-E110 2026-01-19 | group_therapy |  | 11 | "Service date: January 19, 2026 \| Group encounter: HG-E110" |  |
| 002 | 2 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 13 | "Scheduled opening: 10:00 \| Scheduled closing: 11:30" |  |
| 003 | 2 | time | HG-E110 2026-01-19 | group_therapy | label: actual; position: header; start: 10:00; what: patient_arrival | 14 | "Patient arrival: 10:00" |  |
| 004 | 2 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: actual; position: header; what: patient_departure | 14 | "Patient departure: 11:30" |  |
| 005 | 2 | attendance | HG-E110 2026-01-19 | group_therapy | status: attended; status_as_written: Attended | 14 | "Status: Attended" |  |
| 006 | 2 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 18 | "Rowan attended the opening check-in" |  |
| 007 | 2 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: accepted the exercise handout; topic: functioning | 18 | "accepted the exercise handout" |  |
| 008 | 2 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: requested additional help from individual clinician; topic: reason_for_contact | 18 | "requested additional help from the individual clinician" |  |
| 009 | 1 | statement |  |  | says: is_copy_or_resend | 8 | "The attached attendance sheet was resent following a request for the original group roster." |  |
| 010 | 2 | statement |  |  | says: is_copy_or_resend | 20 | "This is a retransmission of the January 19 roster for HG-E110." |  |
| 011 | 2 | statement |  |  | says: no_new_signature | 20 | "The received copy contains no new clinician signature and records no additional visit." |  |
| 012 | 2 | statement |  |  | says: not_a_visit | 20 | "records no additional visit" |  |

Coverage: 18 times, dates and record numbers in the document. 17 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 20 | number | HG-E110 | captured on another line |

### BH-D105: BH-D105_individual_2026-01-19.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | clinical_note | Individual psychotherapy | signed by Mira Patel, LCSW, 2026-01-19 12:32 |  |  | service 2026-01-19; signed 2026-01-19 12:32 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E111 2026-01-19 | individual_therapy |  | 3 | "Individual psychotherapy \| Encounter HG-E111" |  |
| 002 | 1 | modality | HG-E111 2026-01-19 | individual_therapy | modality: in_person | 5 | "January 19, 2026 \| In person" |  |
| 003 | 1 | time | HG-E111 2026-01-19 | individual_therapy | end: 11:45; label: not_labelled; position: header; start: 11:15; what: patient_present | 6 | "Patient contact: 11:15–11:45" |  |
| 004 | 1 | attendance | HG-E111 2026-01-19 | individual_therapy | status: completed; status_as_written: Completed: 30 minutes | 6 | "Completed: 30 minutes" |  |
| 005 | 1 | participant | HG-E111 2026-01-19 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 11 | "Rowan participated throughout the individual contact" |  |
| 006 | 1 | participant | HG-E111 2026-01-19 | individual_therapy | name: Mira Patel; presence: not_stated; role: clinician; role_as_written: LCSW | 7 | "Clinician: Mira Patel, LCSW" |  |
| 007 | 1 | stated_minutes | HG-E111 2026-01-19 | individual_therapy | minutes: 30; of: patient_present | 6 | "Completed: 30 minutes" |  |
| 008 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: added because anxious in group; topic: reason_for_contact | 9 | "This visit was added because Rowan became anxious during group and needed individual grounding and review of coping strategies." |  |
| 009 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: patient; summary: felt overwhelmed by workplace talk; topic: anxiety | 9 | "The patient described feeling overwhelmed when other members discussed workplace demands" |  |
| 010 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: identified early activation signs; topic: anxiety | 9 | "Rowan was able to identify muscle tension, rapid breathing, and an urge to leave as early signs of activation." |  |
| 011 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: patient; summary: anxiety intensity eased; topic: anxiety | 11 | "reported that the immediate intensity of anxiety eased enough to discuss a next step" |  |
| 012 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: agreed task: draft two sentences to supervisor; topic: functioning | 11 | "We narrowed the work-related task to drafting two sentences to a supervisor, without requiring that the message be sent today." |  |
| 013 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: patient; summary: denied suicidal thoughts; topic: safety | 13 | "Rowan denied current suicidal thoughts" |  |
| 014 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: no acute safety concern; topic: safety | 13 | "No acute safety concern was identified during this contact." |  |
| 015 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: disrupted sleep interferes with work; topic: sleep | 13 | "Persistent avoidance and disrupted sleep continue to interfere with resuming a usual work routine." |  |
| 016 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: continue established plan; topic: progress | 13 | "Continue the established outpatient plan" |  |
| 017 | 1 | statement | HG-E111 2026-01-19 | individual_therapy | says: separate_contact | 9 | "This visit was added because Rowan became anxious during group" |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D106: BH-D106_telehealth_2026-01-21.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-13 | clinical_note | Individual psychotherapy | signed by Mira Patel, LCSW, 2026-01-21 15:04 |  |  | service 2026-01-21; signed 2026-01-21 15:04 |
| 2 | 15-20 | platform_export | ATTACHED PLATFORM CONNECTION EXPORT | not_stated |  |  | exported_or_prepared 2026-01-21 14:06 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E112 HG-A112 2026-01-21 | individual_therapy |  | 3 | "Individual psychotherapy \| Encounter HG-E112 \| Appointment HG-A112" |  |
| 002 | 1 | modality | HG-E112 HG-A112 2026-01-21 | individual_therapy | modality: video | 5 | "January 21, 2026 \| Video \| Clinician: Mira Patel, LCSW" |  |
| 003 | 1 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | end: 13:20; label: actual; position: body; start: 13:00; what: patient_present | 7 | "Patient contact occurred 13:00–13:20 and 13:30–13:55." |  |
| 004 | 1 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | end: 13:55; label: actual; position: body; start: 13:30; what: patient_present | 7 | "Patient contact occurred 13:00–13:20 and 13:30–13:55." |  |
| 005 | 1 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | detail: connection lost; end: 13:30; label: actual; position: body; start: 13:20; what: no_therapy_interval | 7 | "Connection was lost from 13:20–13:30; there was no therapeutic contact during that interval." |  |
| 006 | 2 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | detail: VC-112A; end: 13:20; label: actual; position: table; start: 13:00; what: connection | 17 | "HG-A112 \| VC-112A \| January 21 13:00 \| January 21 13:20" |  |
| 007 | 2 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | detail: VC-112B; end: 13:55; label: actual; position: table; start: 13:30; what: connection | 18 | "HG-A112 \| VC-112B \| January 21 13:30 \| January 21 13:55" |  |
| 008 | 1 | participant | HG-E112 HG-A112 2026-01-21 | individual_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 4 | "Rowan Mercer \| DOB: 1991-04-12 \| MRN: HG-M042" |  |
| 009 | 1 | participant | HG-E112 HG-A112 2026-01-21 | individual_therapy | name: Mira Patel; presence: not_stated; role: clinician; role_as_written: LCSW | 5 | "Clinician: Mira Patel, LCSW" |  |
| 010 | 1 | stated_minutes | HG-E112 HG-A112 2026-01-21 | individual_therapy | minutes: 45; of: patient_present | 7 | "Total patient psychotherapy contact: 45 minutes." |  |
| 011 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: patient; summary: drafted message about return to work, did not send; topic: functioning | 9 | "Rowan reported drafting a short message about a possible gradual return to work but stopping before sending it." |  |
| 012 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: patient; summary: checking draft repeatedly delays task; topic: functioning | 9 | "The patient identified checking the draft repeatedly as another way the task was being delayed." |  |
| 013 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: patient; summary: one night improved sleep then prolonged wakefulness; topic: sleep | 11 | "Rowan described one night of improved sleep followed by a night of prolonged wakefulness." |  |
| 014 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: clinician; summary: engaged, able to restate agreed task; topic: functioning | 11 | "Rowan was engaged and able to restate the agreed task." |  |
| 015 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: clinician; summary: no urgent safety concern reported; topic: safety | 11 | "No urgent safety concern was reported." |  |
| 016 | 1 | statement | HG-E112 HG-A112 2026-01-21 | individual_therapy | says: no_therapy_provided | 7 | "there was no therapeutic contact during that interval" |  |
| 017 | 1 | statement | HG-E112 HG-A112 2026-01-21 | individual_therapy | says: same_contact_continued | 7 | "The reconnection continued the same clinical encounter under original appointment HG-A112." |  |
| 018 | 2 | statement | HG-E112 HG-A112 2026-01-21 | individual_therapy | says: other | 19 | "Second call reason: Rejoin original appointment after network disconnect." |  |

Coverage: 29 times, dates and record numbers in the document. 22 captured, 7 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-A112 | captured on another line |
| 17 | date | January 21 | captured on another line |
| 17 | date | January 21 | captured on another line |
| 17 | number | HG-A112 | captured on another line |
| 18 | date | January 21 | captured on another line |
| 18 | date | January 21 | captured on another line |
| 18 | number | HG-A112 | captured on another line |

### BH-D107: BH-D107_group_activity_records_2026-01-22_and_29.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | clinical_note | Skills group activity record extract | signed by Leah Chen, LCSW, 2026-01-22 12:06 |  |  | service 2026-01-22; signed 2026-01-22 12:06; service 2026-01-29; signed 2026-01-29 12:11 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E113 2026-01-22 | group_therapy |  | 7 | "January 22, 2026 \| Encounter HG-E113" |  |
| 002 | 1 | contact | HG-E118 2026-01-29 | group_therapy |  | 12 | "January 29, 2026 \| Encounter HG-E118" |  |
| 003 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:30; label: scheduled; position: body; start: 10:00; what: contact_interval | 8 | "Scheduled group 10:00–11:30." |  |
| 004 | 1 | time | HG-E113 2026-01-22 | group_therapy | detail: Nontherapeutic break; end: 11:00; label: not_labelled; position: body; start: 10:45; what: no_therapy_interval | 8 | "Nontherapeutic break 10:45–11:00." |  |
| 005 | 1 | time | HG-E118 2026-01-29 | group_therapy | end: 11:30; label: scheduled; position: body; start: 10:00; what: contact_interval | 13 | "Scheduled group 10:00–11:30." |  |
| 006 | 1 | time | HG-E118 2026-01-29 | group_therapy | detail: Nontherapeutic break; end: 11:00; label: not_labelled; position: body; start: 10:45; what: no_therapy_interval | 13 | "Nontherapeutic break 10:45–11:00." |  |
| 007 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Leah Chen; presence: not_stated; role: clinician; role_as_written: Facilitator | 5 | "Facilitator: Leah Chen, LCSW" |  |
| 008 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Rowan Mercer; presence: present_part; role: patient | 9 | "Rowan joined the discussion after it had begun;" |  |
| 009 | 1 | participant | HG-E118 2026-01-29 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 14 | "Rowan participated in the paired rehearsal" |  |
| 010 | 1 | observation | HG-E113 2026-01-22 | group_therapy | date: 2026-01-22; speaker: clinician; summary: concern that seeing outstanding items would be overwhelming; topic: anxiety | 9 | "described concern that seeing outstanding items would become overwhelming" |  |
| 011 | 1 | observation | HG-E113 2026-01-22 | group_therapy | date: 2026-01-22; speaker: clinician; summary: used opening work calendar as example; contributed example after break; topic: functioning | 9 | "The patient contributed an example to the discussion after the break." |  |
| 012 | 1 | observation | HG-E118 2026-01-29 | group_therapy | date: 2026-01-29; speaker: clinician; summary: opened work calendar but delayed follow-up conversation; topic: functioning | 14 | "Rowan reported opening the work calendar but delaying a follow-up conversation." |  |
| 013 | 1 | observation | HG-E118 2026-01-29 | group_therapy | date: 2026-01-29; speaker: clinician; summary: participated in paired rehearsal, accepted feedback; topic: functioning | 14 | "Rowan participated in the paired rehearsal and accepted feedback about keeping the request brief." |  |
| 014 | 1 | statement |  |  | says: no_therapy_provided | 17 | "the break was unstructured time without therapeutic activity or facilitator treatment." |  |
| 015 | 1 | statement |  |  | says: not_an_attendance_record | 17 | "Patient arrival, departure, and attendance status are entered in the separate attendance register." |  |

Coverage: 19 times, dates and record numbers in the document. 19 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D108: BH-D108_final_attendance_and_cancellation_register.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-22 | attendance_record | Outpatient attendance and appointment disposition extract | not_stated | Final |  | exported_or_prepared 2026-01-30 17:10 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E113 2026-01-22 | group_therapy |  | 9 | "January 22 \| HG-E113 \| Skills group \| 10:00–11:30 \| 10:30 \| 11:30 \| Attended, late arrival" |  |
| 002 | 1 | contact | HG-E116 2026-01-27 | group_therapy |  | 10 | "January 27 \| HG-E116 \| Skills group \| 10:00–11:30 \| — \| — \| No show; patient did not attend" |  |
| 003 | 1 | contact | HG-E117 HG-E117 2026-01-28 | individual_therapy |  | 11 | "January 28 \| HG-E117 \| Individual \| 14:00–14:45 \| — \| — \| Patient cancelled before appointment" |  |
| 004 | 1 | contact | HG-E118 2026-01-29 | group_therapy |  | 12 | "January 29 \| HG-E118 \| Skills group \| 10:00–11:30 \| 10:00 \| 11:30 \| Attended" |  |
| 005 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 9 | "January 22 \| HG-E113 \| Skills group \| 10:00–11:30 \| 10:30 \| 11:30 \| Attended, late arrival" |  |
| 006 | 1 | time | HG-E113 2026-01-22 | group_therapy | label: actual; position: table; start: 10:30; what: patient_arrival | 9 | "January 22 \| HG-E113 \| Skills group \| 10:00–11:30 \| 10:30 \| 11:30 \| Attended, late arrival" |  |
| 007 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 9 | "January 22 \| HG-E113 \| Skills group \| 10:00–11:30 \| 10:30 \| 11:30 \| Attended, late arrival" |  |
| 008 | 1 | time | HG-E116 2026-01-27 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 10 | "January 27 \| HG-E116 \| Skills group \| 10:00–11:30 \| — \| — \| No show; patient did not attend" |  |
| 009 | 1 | time | HG-E117 HG-E117 2026-01-28 | individual_therapy | end: 14:45; label: scheduled; position: table; start: 14:00; what: contact_interval | 11 | "January 28 \| HG-E117 \| Individual \| 14:00–14:45 \| — \| — \| Patient cancelled before appointment" |  |
| 010 | 1 | time | HG-E118 2026-01-29 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 12 | "January 29 \| HG-E118 \| Skills group \| 10:00–11:30 \| 10:00 \| 11:30 \| Attended" |  |
| 011 | 1 | time | HG-E118 2026-01-29 | group_therapy | label: actual; position: table; start: 10:00; what: patient_arrival | 12 | "January 29 \| HG-E118 \| Skills group \| 10:00–11:30 \| 10:00 \| 11:30 \| Attended" |  |
| 012 | 1 | time | HG-E118 2026-01-29 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 12 | "January 29 \| HG-E118 \| Skills group \| 10:00–11:30 \| 10:00 \| 11:30 \| Attended" |  |
| 013 | 1 | time | HG-E113 2026-01-22 | group_therapy | label: actual; position: body; start: 10:30; what: patient_arrival | 14 | "Rowan arrived at 10:30 and remained until the group closed." |  |
| 014 | 1 | attendance | HG-E113 2026-01-22 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-22; entry_signed_time: 12:09; status: attended_part; status_as_written: Attended, late arrival | 9 | "January 22 \| HG-E113 \| Skills group \| 10:00–11:30 \| 10:30 \| 11:30 \| Attended, late arrival" |  |
| 015 | 1 | attendance | HG-E116 2026-01-27 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-27; entry_signed_time: 11:54; status: no_show; status_as_written: No show; patient did not attend | 10 | "January 27 \| HG-E116 \| Skills group \| 10:00–11:30 \| — \| — \| No show; patient did not attend" |  |
| 016 | 1 | attendance | HG-E116 2026-01-27 | group_therapy | status: absent; status_as_written: Rowan was absent for the entire group | 16 | "Final roster confirms Rowan was absent for the entire group." |  |
| 017 | 1 | attendance | HG-E117 HG-E117 2026-01-28 | individual_therapy | entry_entered_by: Ana Reed; entry_entered_date: 2026-01-28; entry_entered_time: 08:18; reason: personal scheduling conflict; status: cancelled_by_patient; status_as_written: Patient cancelled before appointment | 11 | "January 28 \| HG-E117 \| Individual \| 14:00–14:45 \| — \| — \| Patient cancelled before appointment" |  |
| 018 | 1 | attendance | HG-E118 2026-01-29 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-29; entry_signed_time: 12:15; status: attended; status_as_written: Attended | 12 | "January 29 \| HG-E118 \| Skills group \| 10:00–11:30 \| 10:00 \| 11:30 \| Attended" |  |
| 019 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Rowan Mercer; presence: present_part; role: patient | 14 | "Rowan arrived at 10:30 and remained until the group closed." |  |
| 020 | 1 | participant | HG-E116 2026-01-27 | group_therapy | name: Rowan Mercer; presence: absent; role: patient | 16 | "Final roster confirms Rowan was absent for the entire group." |  |
| 021 | 1 | participant | HG-E118 2026-01-29 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 20 | "Rowan was present from opening through closing." |  |
| 022 | 1 | observation | HG-E117 HG-E117 2026-01-28 | individual_therapy | date: 2026-01-28; speaker: clinician; summary: patient reported a personal scheduling conflict; topic: other | 18 | "Rowan reported a personal scheduling conflict." |  |
| 023 | 1 | observation | HG-E116 2026-01-27 | group_therapy | date: 2026-01-27; speaker: clinician; summary: outreach message left inviting patient to contact scheduling; topic: reason_for_contact | 16 | "An outreach message inviting the patient to contact scheduling was left after the group" |  |
| 024 | 1 | statement | HG-E116 2026-01-27 | group_therapy | says: no_patient_contact | 16 | "No patient treatment contact occurred." |  |
| 025 | 1 | statement | HG-E116 2026-01-27 | group_therapy | says: no_clinical_service | 16 | "no clinical discussion occurred" |  |
| 026 | 1 | statement | HG-E117 HG-E117 2026-01-28 | individual_therapy | says: other | 18 | "no replacement appointment was booked within January 2026" |  |
| 027 | 1 | statement |  |  | says: other | 22 | "Break details remain in the corresponding group activity records." |  |

Coverage: 41 times, dates and record numbers in the document. 31 captured, 9 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 14 | date | January 22 | captured on another line |
| 14 | date | January 22 | captured on another line |
| 14 | time | 12:09 | captured on another line |
| 16 | time | 11:54 | captured on another line |
| 18 | time | 08:12 | not captured |
| 18 | time | 08:18 | captured on another line |
| 18 | number | HG-E117 | captured on another line |
| 20 | date | January 29 | captured on another line |
| 20 | date | January 29 | captured on another line |
| 20 | time | 12:15 | captured on another line |

### BH-D109: BH-D109_care_coordination_2026-01-23.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | clinical_note | Care coordination | signed by Mira Patel, LCSW, 2026-01-23 10:02 |  |  | service 2026-01-23; signed 2026-01-23 10:02 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E114 2026-01-23 | care_coordination |  | 3 | "Care coordination \| Encounter HG-E114" |  |
| 002 | 1 | time | HG-E114 2026-01-23 | care_coordination | end: 09:20; label: not_labelled; position: header; start: 09:00; what: contact_interval | 5 | "January 23, 2026 \| 09:00–09:20" |  |
| 003 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Mira Patel; presence: not_stated; role: clinician; role_as_written: LCSW | 6 | "Participants: Mira Patel, LCSW, and Daniel Shaw, outside social worker" |  |
| 004 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Daniel Shaw; presence: not_stated; role: outside_professional; role_as_written: outside social worker | 6 | "Participants: Mira Patel, LCSW, and Daniel Shaw, outside social worker" |  |
| 005 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Rowan Mercer; presence: absent; role: patient | 7 | "Patient participation: None. No patient contact occurred." |  |
| 006 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: outside_professional; speaker_name: Daniel Shaw; summary: Patient asked for help on whom to contact about gradual return schedule; topic: reason_for_contact | 9 | "The outside social worker reported that Rowan had asked for help understanding whom to contact about a gradual return schedule." |  |
| 007 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: clinician; summary: Approach of breaking difficult task into manageable first step; topic: functioning | 11 | "Reviewed the current approach of helping Rowan break a difficult task into a manageable first step." |  |
| 008 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: clinician; summary: No change to medication or therapy frequency; topic: medication | 11 | "No change to medication or psychotherapy frequency was made during the coordination call." |  |
| 009 | 1 | statement | HG-E114 2026-01-23 | care_coordination | says: no_patient_contact | 7 | "Patient participation: None. No patient contact occurred." |  |
| 010 | 1 | statement | HG-E114 2026-01-23 | care_coordination | says: no_therapy_provided | 13 | "no psychotherapy was delivered to the patient during the call" |  |
| 011 | 1 | statement | HG-E114 2026-01-23 | care_coordination | says: other | 13 | "This contact was between professionals only." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D110: BH-D110_individual_primary_record_2026-01-26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Individual psychotherapy | signed by Mira Patel, LCSW, 2026-01-26 11:16 | Final |  | service 2026-01-26; signed 2026-01-26 11:16 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E115 HG-A115 2026-01-26 | individual_therapy |  | 3 | "Individual psychotherapy \| Encounter HG-E115 \| Appointment HG-A115" |  |
| 002 | 1 | modality | HG-E115 HG-A115 2026-01-26 | individual_therapy | modality: in_person | 5 | "January 26, 2026 \| In person" |  |
| 003 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: header; start: 09:00; what: patient_present | 7 | "Actual patient psychotherapy contact: 09:00–09:50, 50 minutes." |  |
| 004 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 4 | "Rowan Mercer \| DOB: 1991-04-12 \| MRN: HG-M042" |  |
| 005 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Mira Patel; presence: not_stated; role: clinician; role_as_written: LCSW | 6 | "Clinicians: Mira Patel, LCSW; Nora Ellis, LCSW" |  |
| 006 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Nora Ellis; presence: present; role: clinician; role_as_written: LCSW | 11 | "Nora Ellis participated directly in the clinical work" |  |
| 007 | 1 | stated_minutes | HG-E115 HG-A115 2026-01-26 | individual_therapy | minutes: 50; of: patient_present | 7 | "Actual patient psychotherapy contact: 09:00–09:50, 50 minutes." |  |
| 008 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: worry about commitments after supervisor's reply; topic: anxiety | 9 | "but also brought up worry about being asked for commitments the patient might not be able to meet" |  |
| 009 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: continued to postpone choosing a time for conversation; topic: functioning | 9 | "Rowan continued to postpone choosing a time for the conversation." |  |
| 010 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: sleep uneven, difficulty settling; topic: sleep | 9 | "Sleep remained uneven, with difficulty settling on nights when work-related thoughts became repetitive." |  |
| 011 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: able to return to main request with prompting; topic: functioning | 11 | "Rowan was able to return to the main request with prompting." |  |
| 012 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: attentive and collaborative, hesitant about task outside office; topic: mood | 13 | "The patient remained attentive and collaborative, although hesitant about completing the task outside the office." |  |
| 013 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: no current suicidal ideation reported; topic: safety | 13 | "No current suicidal ideation was reported." |  |
| 014 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: continue work on avoidance and bedtime routine; topic: progress | 13 | "Continue work on avoidance and the bedtime routine." |  |
| 015 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: plan to bring response draft to next visit if stuck; topic: functioning | 13 | "bringing the response draft to the next visit if the patient remained stuck" |  |

Coverage: 10 times, dates and record numbers in the document. 10 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D111: BH-D111_individual_second_record_2026-01-26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | clinical_note | Participating clinician psychotherapy record | signed by Nora Ellis, LCSW, 2026-01-26 12:03 | Final |  | service 2026-01-26; signed 2026-01-26 12:03 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E115 HG-A115 2026-01-26 | individual_therapy |  | 4 | "Encounter HG-E115 \| Appointment HG-A115 \| Service date January 26, 2026" |  |
| 002 | 1 | modality | HG-E115 HG-A115 2026-01-26 | individual_therapy | modality: in_person | 6 | "Service: Individual psychotherapy, in person" |  |
| 003 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: header; start: 09:10; what: patient_present | 7 | "Actual patient psychotherapy contact: 09:10–09:50, 40 minutes." |  |
| 004 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | label: actual; position: body; start: 09:10; what: patient_arrival | 10 | "Rowan entered the treatment room at 09:10, when we began the session." |  |
| 005 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: body; start: 09:10; what: patient_present | 10 | "The full patient-contact interval for the encounter was 09:10–09:50." |  |
| 006 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: body; what: patient_departure | 14 | "The session concluded with Rowan at 09:50." |  |
| 007 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 10 | "Rowan entered the treatment room at 09:10, when we began the session." |  |
| 008 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Nora Ellis; presence: present; role: clinician; role_as_written: LCSW | 10 | "I participated directly in this individual encounter." |  |
| 009 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Mira Patel; presence: not_stated; role: clinician; role_as_written: LCSW | 8 | "Clinician: Nora Ellis, LCSW, participating with Mira Patel, LCSW" |  |
| 010 | 1 | stated_minutes | HG-E115 HG-A115 2026-01-26 | individual_therapy | minutes: 40; of: patient_present | 7 | "Actual patient psychotherapy contact: 09:10–09:50, 40 minutes." |  |
| 011 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: difficulty moving from supervisor's reply to arranging next conversation; topic: functioning | 10 | "Rowan discussed difficulty moving from a supervisor's reply to arranging the next conversation." |  |
| 012 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: anticipated becoming overwhelmed by several work issues; topic: anxiety | 10 | "The patient anticipated becoming overwhelmed if several work issues were raised at once." |  |
| 013 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: tendency to keep editing a message; topic: functioning | 12 | "Rowan recognized a tendency to keep editing a message after the essential point was already clear." |  |
| 014 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: uncertain using cue independently when anxious; topic: anxiety | 12 | "remained uncertain about using it independently when anxious" |  |
| 015 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: repetitive night planning affected settling for sleep; topic: sleep | 12 | "The discussion also addressed how repetitive planning at night affected settling for sleep." |  |
| 016 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: ongoing anxiety, low mood, functional difficulty; topic: mood | 14 | "Clinical presentation remained consistent with ongoing anxiety, low mood, and functional difficulty around work demands." |  |
| 017 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: wish to resume steadier routine; topic: functioning | 14 | "described a wish to resume a steadier routine" |  |
| 018 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: continue individual and group work under existing plan; topic: progress | 14 | "Plan is to continue individual and group work under the existing outpatient plan." |  |

Coverage: 14 times, dates and record numbers in the document. 14 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D112: BH-D112_draft_note_and_charge_extract_2026-01-27.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 7-16 | draft_note | AUTOGENERATED PROGRESS NOTE | unsigned | DRAFT — UNSIGNED — system populated from scheduled group template |  | created 2026-01-27 09:45; service 2026-01-27 |
| 2 | 18-27 | billing_extract | POSTED CHARGE EXTRACT | not_stated |  |  | posted 2026-01-27 18:06; exported_or_prepared 2026-01-30 17:25; service 2026-01-27 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E116 2026-01-27 | group_therapy |  | 10 | "Scheduled service: Skills group, 10:00–11:30" |  |
| 002 | 1 | time | HG-E116 2026-01-27 | group_therapy | end: 11:30; label: scheduled; position: body; start: 10:00; what: contact_interval | 10 | "Scheduled service: Skills group, 10:00–11:30" |  |
| 003 | 1 | attendance | HG-E116 2026-01-27 | group_therapy | status: attended; status_as_written: Patient attended the full session and participated in the skills discussion. | 11 | "Template attendance text: Patient attended the full session and participated in the skills discussion." |  |
| 004 | 1 | participant | HG-E116 2026-01-27 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 11 | "Template attendance text: Patient attended the full session and participated in the skills discussion." |  |
| 005 | 2 | charge | HG-E116 2026-01-27 | group_therapy | charge_id: CH-116; description: Group psychotherapy; posted_date: 2026-01-27; posted_time: 18:06; quantity: 1; status_as_written: Posted; unit_as_written: group session | 21 | "Description: Group psychotherapy" |  |
| 006 | 1 | statement | HG-E116 2026-01-27 | group_therapy | says: is_draft_or_unsigned | 9 | "Status: DRAFT — UNSIGNED — system populated from scheduled group template" |  |
| 007 | 1 | statement | HG-E116 2026-01-27 | group_therapy | says: made_before_the_service | 16 | "It was generated from the appointment template before the scheduled group." |  |
| 008 | 1 | statement | HG-E116 2026-01-27 | group_therapy | says: no_clinical_service | 16 | "No clinician attestation or finalized patient-specific narrative appears in this draft." |  |
| 009 | 2 | statement | HG-E116 2026-01-27 | group_therapy | says: not_an_attendance_record | 25 | "The signed group attendance register is maintained in the clinical attendance section of the chart." |  |

Coverage: 19 times, dates and record numbers in the document. 13 captured, 6 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 3 | date | January 30, 2026 | captured on another line |
| 3 | time | 17:25 | captured on another line |
| 5 | number | HG-E116 | captured on another line |
| 19 | number | CH-116 | captured on another line |
| 19 | number | HG-E116 | captured on another line |
| 25 | date | January 30 | captured on another line |

### BH-D113: BH-D113_family_therapy_2026-01-30.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | clinical_note | Family psychotherapy | signed by Mira Patel, LCSW, 2026-01-30 14:18 |  |  | service 2026-01-30; signed 2026-01-30 14:18 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E119 2026-01-30 | family_therapy |  | 3 | "Family psychotherapy \| Encounter HG-E119" |  |
| 002 | 1 | modality | HG-E119 2026-01-30 | family_therapy | modality: in_person | 5 | "January 30, 2026 \| In person \| Clinician: Mira Patel, LCSW" |  |
| 003 | 1 | time | HG-E119 2026-01-30 | family_therapy | end: 13:45; label: not_labelled; position: header; start: 13:00; what: contact_interval | 6 | "Therapist session interval: 13:00–13:45, 45 minutes." |  |
| 004 | 1 | time | HG-E119 2026-01-30 | family_therapy | detail: Partner only; end: 13:15; label: not_labelled; position: header; start: 13:00; what: patient_absent_interval | 7 | "Partner only: 13:00–13:15." |  |
| 005 | 1 | time | HG-E119 2026-01-30 | family_therapy | detail: Rowan present with partner; end: 13:45; label: not_labelled; position: header; start: 13:15; what: patient_present | 7 | "Rowan present with partner: 13:15–13:45, 30 minutes." |  |
| 006 | 1 | time | HG-E119 2026-01-30 | family_therapy | label: actual; position: body; start: 13:15; what: patient_arrival | 11 | "Rowan joined at 13:15 and participated through the end of the session." |  |
| 007 | 1 | attendance | HG-E119 2026-01-30 | family_therapy | status: attended_part; status_as_written: Rowan was not present for that portion | 9 | "Rowan was not present for that portion." |  |
| 008 | 1 | participant | HG-E119 2026-01-30 | family_therapy | name: Rowan Mercer; presence: present_part; role: patient | 11 | "Rowan joined at 13:15 and participated through the end of the session." |  |
| 009 | 1 | participant | HG-E119 2026-01-30 | family_therapy | name: Casey Mercer; presence: present; role: family_or_partner | 9 | "Rowan's partner, Casey Mercer, arrived first." |  |
| 010 | 1 | participant | HG-E119 2026-01-30 | family_therapy | name: Mira Patel; presence: not_stated; role: clinician | 5 | "Clinician: Mira Patel, LCSW" |  |
| 011 | 1 | stated_minutes | HG-E119 2026-01-30 | family_therapy | minutes: 45; of: contact_total | 6 | "Therapist session interval: 13:00–13:45, 45 minutes." |  |
| 012 | 1 | stated_minutes | HG-E119 2026-01-30 | family_therapy | minutes: 30; of: patient_present | 7 | "Rowan present with partner: 13:15–13:45, 30 minutes." |  |
| 013 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Rowan remained anxious about work conversation; topic: anxiety | 13 | "Rowan remained anxious about the work conversation but could explain the intended first step." |  |
| 014 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: patient; summary: Limited plan felt more manageable; topic: progress | 13 | "The patient reported that having a limited plan felt more manageable." |  |
| 015 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Continue current treatment plan; topic: progress | 13 | "Continue the current outpatient treatment plan and revisit whether the agreed communication pattern was useful." |  |
| 016 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Both agreed to try one brief planned check-in; topic: functioning | 13 | "Both participants agreed to try one brief check-in at a planned time rather than repeated questions across the evening." |  |
| 017 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Uncertain when reminders help or add pressure; topic: other | 9 | "Casey described uncertainty about when reminders helped and when they seemed to increase Rowan's sense of pressure." |  |

Coverage: 14 times, dates and record numbers in the document. 14 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D114: BH-D114_medication_management_2026-01-30.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | clinical_note | Medication management | signed by Elena Ortiz, PMHNP, 2026-01-30 16:02 | Final |  | service 2026-01-30; signed 2026-01-30 16:02 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E120 2026-01-30 | medication_management |  | 3 | "Medication management \| Encounter HG-E120" |  |
| 002 | 1 | time | HG-E120 2026-01-30 | medication_management | end: 15:20; label: not_labelled; position: header; start: 15:00; what: contact_interval | 5 | "January 30, 2026 \| 15:00–15:20 \| Completed, 20 minutes" |  |
| 003 | 1 | attendance | HG-E120 2026-01-30 | medication_management | status: completed; status_as_written: Completed | 5 | "January 30, 2026 \| 15:00–15:20 \| Completed, 20 minutes" |  |
| 004 | 1 | participant | HG-E120 2026-01-30 | medication_management | name: Elena Ortiz; presence: not_stated; role: clinician; role_as_written: Prescriber | 6 | "Prescriber: Elena Ortiz, PMHNP" |  |
| 005 | 1 | participant | HG-E120 2026-01-30 | medication_management | name: Rowan Mercer; presence: not_stated; role: patient | 4 | "Rowan Mercer \| DOB: 1991-04-12 \| MRN: HG-M042" |  |
| 006 | 1 | stated_minutes | HG-E120 2026-01-30 | medication_management | minutes: 20; of: contact_total | 5 | "January 30, 2026 \| 15:00–15:20 \| Completed, 20 minutes" |  |
| 007 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: patient; summary: took medication as prescribed, no new adverse effect; topic: medication | 8 | "Rowan reported taking the medication as prescribed and did not describe a new adverse effect." |  |
| 008 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: mood less persistently low; topic: mood | 8 | "Mood felt less persistently low than earlier in the month" |  |
| 009 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: anxiety remained noticeable anticipating work contact; topic: anxiety | 8 | "anxiety remained noticeable when anticipating contact with work" |  |
| 010 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: sleep variable; topic: sleep | 8 | "Sleep was still variable." |  |
| 011 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: patient; summary: denied current suicidal thoughts; topic: safety | 10 | "The patient denied current suicidal thoughts." |  |
| 012 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: no new acute safety issue; topic: safety | 10 | "No new acute safety issue emerged in this visit." |  |
| 013 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: no medication change made; topic: medication | 10 | "No medication change was made today." |  |
| 014 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: agreed to continue follow-up and bring medication questions; topic: functioning | 12 | "Rowan agreed to continue attending scheduled outpatient follow-up and to bring questions about the medication regimen to the next medication appointment." |  |
| 015 | 1 | statement | HG-E120 2026-01-30 | medication_management | says: no_therapy_provided | 12 | "No separately documented psychotherapy was provided." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D115: BH-D115_symptom_measure_review_2026-01-30.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by sonnet, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | questionnaire_review | Symptom questionnaire and chart review | signed by Mira Patel, LCSW, 2026-01-30 16:20 |  |  | completed 2026-01-30 12:42; reviewed 2026-01-30; signed 2026-01-30 16:20 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | 2026-01-30 | questionnaire_review |  | 14 | "This entry records questionnaire review within ongoing care and is not a separate treatment appointment." |  |
| 002 | 1 | score |  |  | completed_date: 2026-01-30; completed_time: 12:42; instrument: PHQ-9; relation: completion; score: 10 | 6 | "PHQ-9 total: 10." |  |
| 003 | 1 | score |  |  | completed_date: 2026-01-30; completed_time: 12:42; instrument: PHQ-9; item_number: 9; relation: completion; score: 0 | 6 | "Item 9: 0." |  |
| 004 | 1 | observation | 2026-01-30 | questionnaire_review | date: 2026-01-30; speaker: clinician; summary: continued sleep difficulty; topic: sleep | 8 | "The patient continued to endorse sleep difficulty and trouble sustaining usual activities" |  |
| 005 | 1 | observation | 2026-01-30 | questionnaire_review | date: 2026-01-30; speaker: clinician; summary: trouble sustaining usual activities; topic: functioning | 8 | "The patient continued to endorse sleep difficulty and trouble sustaining usual activities" |  |
| 006 | 1 | observation | 2026-01-30 | questionnaire_review | date: 2026-01-30; speaker: clinician; summary: fewer days of pervasive low mood than at intake; topic: mood | 8 | "with fewer days of pervasive low mood than reported at intake" |  |
| 007 | 1 | observation | 2026-01-30 | questionnaire_review | date: 2026-01-30; speaker: clinician; summary: partial improvement; topic: progress | 10 | "Rowan shows partial improvement" |  |
| 008 | 1 | observation | 2026-01-30 | questionnaire_review | date: 2026-01-30; speaker: clinician; summary: functional impact around returning to work; avoidance; topic: functioning | 10 | "persistent avoidance and meaningful functional impact around returning to work" |  |
| 009 | 1 | observation | 2026-01-30 | questionnaire_review | date: 2026-01-30; speaker: clinician; summary: took initial steps, drafted and sent message; topic: functioning | 10 | "The patient has taken some initial steps, including drafting and sending a message" |  |
| 010 | 1 | observation | 2026-01-30 | questionnaire_review | date: 2026-01-30; speaker: clinician; summary: anxious when task expands; topic: anxiety | 10 | "becomes anxious when a task expands beyond a narrowly defined action" |  |
| 011 | 1 | observation | 2026-01-30 | questionnaire_review | date: 2026-01-30; speaker: clinician; summary: sleep disruption intermittent barrier; topic: sleep | 10 | "Sleep disruption remains an intermittent barrier to establishing a steadier daytime routine." |  |
| 012 | 1 | observation | 2026-01-30 | questionnaire_review | date: 2026-01-30; speaker: clinician; summary: continued treatment appropriate; topic: progress | 12 | "Continued treatment is appropriate given the remaining difficulties" |  |
| 013 | 1 | statement | 2026-01-30 | questionnaire_review | says: not_a_visit | 14 | "is not a separate treatment appointment" |  |
| 014 | 1 | statement | 2026-01-30 | questionnaire_review | says: no_patient_contact | 14 | "No additional patient-contact interval is claimed in this entry." |  |

Coverage: 8 times, dates and record numbers in the document. 8 captured, 0 captured on another line, 0 not captured, 0 quoted only.

