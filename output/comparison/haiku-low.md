# The saved abstraction

Written by the `export` command from `abstraction.sqlite`. No model is called to write it.

## Documents

| ID | File | Kinds | Patient | Read | Claims | Hash |
|---|---|---|---|---|---|---|
| BH-D001 | group_authorization_letter.txt | authorization | HG-M042 | read | 5 | d2240979a2de |
| BH-D002 | intake_and_individual_jan05.txt | clinical_note | HG-M042 | read | 28 | 7f5f7d4bbfc9 |
| BH-D003 | signed_treatment_plan_jan05.txt | plan | HG-M042 | read | 18 | 3b3f50db40b3 |
| BH-D004 | group_facilitator_jan06.txt | clinical_note | HG-M042 | read | 14 | 5edddc6b2093 |
| BH-D005 | early_group_attendance_roster.txt | attendance_record | HG-M042 | read | 19 | 6f205f89f8d3 |
| BH-D006 | early_appointment_status_export.txt | schedule_export | HG-M042 | read | 30 | 0bf056f3769e |
| BH-D007 | family_primary_jan09.txt | clinical_note | HG-M042 | read | 17 | 924dee06b05c |
| BH-D008 | family_cofacilitator_jan09.txt | clinical_note | HG-M042 | read | 17 | ad416fbda806 |
| BH-D009 | group_facilitator_jan12.txt | clinical_note | HG-M042 | read | 10 | d30d18d0335d |
| BH-D010 | medication_review_jan13.txt | clinical_note | HG-M042 | read | 17 | 95debafd3a72 |
| BH-D011 | individual_therapy_jan14.txt | clinical_note | HG-M042 | read | 21 | 8c2fbaf5bb45 |
| BH-D012 | partner_collateral_jan16.txt | clinical_note | HG-M042 | read | 13 | 432c973d1a4d |
| BH-D013 | symptom_measure_review_jan16.txt | questionnaire_review | HG-M042 | read | 13 | 300a30dbe42b |
| BH-D014 | imported_measure_summary_received_jan26.txt | import_receipt | HG-M042 | read | 6 | 85e2c780abde |
| BH-D015 | missed_visit_outreach_jan08.txt | scheduling_log | HG-M042 | read | 16 | 4521a120a4d7 |
| BH-D016 | group_cancellation_notice_jan15.txt | cancellation_notice | HG-M042 | read | 12 | 5f3375f11c85 |
| BH-D101 | BH-D101_group_content_2026-01-19.txt | clinical_note | HG-M042 | read | 9 | 05a234a8adc9 |
| BH-D102 | BH-D102_original_attendance_2026-01-19.txt | attendance_record | HG-M042 | read | 9 | 514ca20809f6 |
| BH-D103 | BH-D103_attendance_correction_2026-01-20.txt | correction | HG-M042 | read | 8 | 674440968b5d |
| BH-D104 | BH-D104_resent_roster_received_2026-01-26.txt | cover_sheet, attendance_record | HG-M042 | read | 10 | f3f25065559f |
| BH-D105 | BH-D105_individual_2026-01-19.txt | clinical_note | HG-M042 | read | 16 | 91fd8e8b1b31 |
| BH-D106 | BH-D106_telehealth_2026-01-21.txt | clinical_note, platform_export | HG-M042 | read | 18 | 09c946a2248a |
| BH-D107 | BH-D107_group_activity_records_2026-01-22_and_29.txt | clinical_note, clinical_note | HG-M042 | read | 18 | c5953bcb242e |
| BH-D108 | BH-D108_final_attendance_and_cancellation_register.txt | schedule_export | HG-M042 | read | 25 | 805b2c69c7fa |
| BH-D109 | BH-D109_care_coordination_2026-01-23.txt | clinical_note | HG-M042 | read | 12 | 069ea4112779 |
| BH-D110 | BH-D110_individual_primary_record_2026-01-26.txt | clinical_note | HG-M042 | read | 14 | 4b64c46a13b8 |
| BH-D111 | BH-D111_individual_second_record_2026-01-26.txt | clinical_note | HG-M042 | read | 21 | d03451942797 |
| BH-D112 | BH-D112_draft_note_and_charge_extract_2026-01-27.txt | draft_note, billing_extract | HG-M042 | read | 7 | b4390ed6b672 |
| BH-D113 | BH-D113_family_therapy_2026-01-30.txt | clinical_note | HG-M042 | read | 18 | 36764827bcb3 |
| BH-D114 | BH-D114_medication_management_2026-01-30.txt | clinical_note | HG-M042 | read | 17 | 9942bd886fcd |
| BH-D115 | BH-D115_symptom_measure_review_2026-01-30.txt | questionnaire_review | HG-M042 | read | 16 | 4a3859fd81fc |

## What the record establishes

Worked out by code from the claims further down. No model takes part.

### Patient HG-M042, Rowan Mercer

#### Plan

| Value | Read from the plan |
|---|---|
| Document | BH-D003 |
| Signed | 2026-01-05T13:05 |
| In effect | 2026-01-05 to 2026-01-30 |
| Required | at least 150 minutes each week |
| Week starts on | monday |
| Counted classes | family therapy, group therapy, individual therapy |
| Excluded classes | care coordination, collateral contact, medication management |

#### Encounters

| Encounter | Date | Class | Status | Present | Removed | Minutes | Counts | Documents | Notes |
|---|---|---|---|---|---|---|---|---|---|
| HG-E101 | 2026-01-05 | individual therapy | held | 09:00–09:50 |  | 50 | yes | BH-D002, BH-D006 |  |
| HG-E102 | 2026-01-06 | group therapy | held, in part | 10:15–11:15 | 10:45–11:00 | 45 | yes | BH-D004, BH-D005, BH-D006 | arrived after the start; left before the end |
| HG-E103 | 2026-01-08 | individual therapy | no show |  |  |  | no: no-show | BH-D006, BH-D015 |  |
| HG-E104 | 2026-01-09 | family therapy | held | 14:00–14:45 |  | 45 | yes | BH-D006, BH-D007, BH-D008 |  |
| HG-E105 | 2026-01-12 | group therapy | held | 10:00–11:30 | 10:40–10:55 | 75 | yes | BH-D005, BH-D006, BH-D009 |  |
| HG-E106 | 2026-01-13 | medication management | held | 09:00–09:25 |  | 25 | no: a class of service the plan excludes | BH-D006, BH-D010 |  |
| HG-E107 | 2026-01-14 | individual therapy | held | 11:00–11:45 |  | 45 | yes | BH-D006, BH-D011 |  |
| HG-E108 | 2026-01-15 | group therapy | cancelled by clinic |  |  |  | no: cancelled by the clinic | BH-D006, BH-D016 |  |
| HG-E109 | 2026-01-16 | collateral contact | held without patient |  |  |  | no: held with the patient absent | BH-D006, BH-D012 |  |
| HG-E110 | 2026-01-19 | group therapy | held | 10:00–11:30 | 10:45–11:00 | 75 | yes | BH-D101, BH-D102, BH-D103, BH-D104 |  |
| HG-E111 | 2026-01-19 | individual therapy | held | 11:15–11:45 |  | 30 | yes | BH-D105 |  |
| HG-E112 | 2026-01-21 | individual therapy | held | 13:00–13:55 | 13:20–13:30 | 45 | yes | BH-D106 |  |
| HG-E113 | 2026-01-22 | group therapy | held, in part |  | 10:45–11:00 | None | yes | BH-D107, BH-D108 | no clock times are given for the patient's presence |
| HG-E114 | 2026-01-23 | care coordination | held without patient |  |  | 20 without the patient | no: held with the patient absent | BH-D109 |  |
| HG-E115 | 2026-01-26 | individual therapy | held | 09:00–09:50 or 09:10–09:50 |  | 50 or 40 | yes | BH-D110, BH-D111 |  |
| HG-E116 | 2026-01-27 | group therapy | no show |  |  |  | no: no-show | BH-D108, BH-D112 |  |
| HG-E117 | 2026-01-28 | individual therapy | cancelled by patient |  |  |  | no: cancelled by the patient | BH-D108 |  |
| HG-E118 | 2026-01-29 | group therapy | held |  | 10:45–11:00 | None | yes | BH-D107, BH-D108 | no clock times are given for the patient's presence |
| HG-E119 | 2026-01-30 | family therapy | held, in part | 13:15–13:45 |  | 30; 15 without the patient | yes | BH-D113 | joined after the start |
| HG-E120 | 2026-01-30 | medication management | held |  |  | None | no: a class of service the plan excludes | BH-D114 | no clock times are given for the patient's presence |

#### Administrative records

Kept, and not counted as encounters.

| Date | Class | As written | How | Documents |
|---|---|---|---|---|
| 2026-01-08 | scheduling contact | Outbound call | message | BH-D015 |
| 2026-01-08 | scheduling contact | callback | telephone | BH-D015 |
| 2026-01-15 | scheduling contact | telephone contact | telephone | BH-D016 |
| 2026-01-16 | questionnaire review | Measurement review |  | BH-D013 |

#### Conflicts

| Conflict | Field | Values | Outcome | Rule | What would settle it |
|---|---|---|---|---|---|
| HG-M042/HG-E115:start | start | 09:00 (BH-D110); 09:10 (BH-D111) | open | 11 | An arrival or check-in record, or a correction by the author of the record being changed. |

#### Findings

| Finding | Contact | Detail |
|---|---|---|
| note signed after the service date | HG-M042/HG-E104 | The note in BH-D008 was signed on 2026-01-10, after the service date 2026-01-09. |
| charge without attendance | HG-M042/HG-E116 | A charge (CH-116, Group psychotherapy) is posted for a contact whose status is no show. This is an inconsistency between documentation and billing. The record does not show whether the charge was later reviewed or reversed. It is not a finding of improper billing. |

#### Assessments

| Instrument | Completed | Score | Form | Items | Copies | Mentions |
|---|---|---|---|---|---|---|
| PHQ-9 | 2026-01-05 | 18 |  |  | 0 | 1 |
| PHQ-9 | 2026-01-16 08:17 | 14 | HG-Q116 |  | 1 | 0 |
| PHQ-9 | 2026-01-30 12:42 | 10 |  | item 9: 0 | 0 | 0 |

#### Weekly status

| Week | Days | Dates | Minutes | Hours | Verdict | Margin | Depends on | Dates with no document |
|---|---|---|---|---|---|---|---|---|
| 2026-01-05 to 2026-01-11 | 3 | 2026-01-05, 2026-01-06, 2026-01-09 | 140 | 2.33 | not met | 10 minutes short |  | 2026-01-07, 2026-01-11 |
| 2026-01-12 to 2026-01-18 | 2 | 2026-01-12, 2026-01-14 | 120 | 2.00 | not met | 30 minutes short |  | 2026-01-17, 2026-01-18 |
| 2026-01-19 to 2026-01-25 | 3 | 2026-01-19, 2026-01-21, 2026-01-22 | 150 | 2.50 | met | exactly met |  | 2026-01-24, 2026-01-25 |
| 2026-01-26 to 2026-02-01 (partial) | 3 | 2026-01-26, 2026-01-29, 2026-01-30 | 70 or 80 | 1.17 or 1.33 | cannot determine | 80 minutes short or 70 minutes short | HG-M042/HG-E115:start | 2026-01-31, 2026-02-01 |

#### Totals, 2026-01-05 to 2026-01-30

| Measure | Value |
|---|---|
| Sessions | 12 |
| Therapy days | 11 |
| Minutes | 480 or 490 |
| Hours | 8.00 or 8.17 |
| family therapy | 2 sessions, 75 minutes |
| group therapy | 5 sessions, 195 minutes |
| individual therapy | 5 sessions, 210 or 220 minutes |

## What each document says

### BH-D001: group_authorization_letter.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | authorization |  | unsigned |  |  | received 2026-01-04 15:26; entered 2026-01-05 08:05; period_start 2026-01-05; period_end 2026-01-30 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | plan_rule |  |  | end_date: 2026-01-30; rule: episode_period; start_date: 2026-01-05 | 10 | "approved for the period January 5, 2026 through January 30, 2026" |  |
| 002 | 1 | plan_rule |  |  | measure: sessions; minimum: 8; period: episode; rule: requirement | 10 | "Authorized quantity: 8 group sessions" |  |
| 003 | 1 | plan_rule |  |  | rule: counted_service; service_classes: group_therapy | 10 | "One authorization unit represents one scheduled group session" |  |
| 004 | 1 | plan_rule |  |  | rule: excluded_service; service_classes: individual_therapy, family_therapy, medication_management | 10 | "This letter does not authorize individual therapy, family therapy, or medication appointments under the group service quantity" |  |
| 005 | 1 | statement |  |  | says: not_an_attendance_record | 15 | "No service attendance record accompanies this letter" |  |

Coverage: 10 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-A260104-88 | not captured |

### BH-D002: intake_and_individual_jan05.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-19 | clinical_note |  | signed by Mara Voss, LCSW, 2026-01-05 12:18 |  |  | service 2026-01-05; signed 2026-01-05 12:18; period_start 2026-01-05; period_end 2026-01-30 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E101 2026-01-05 | individual_therapy |  | 8 | "Patient-present individual therapy: 09:00–09:50 local" |  |
| 002 | 1 | modality | HG-E101 2026-01-05 | individual_therapy | modality: in_person | 13 | "Rowan arrived independently and participated throughout the appointment" |  |
| 003 | 1 | time | HG-E101 2026-01-05 | individual_therapy | end: 09:50; label: not_labelled; position: header; start: 09:00; what: contact_interval | 8 | "09:00–09:50 local" |  |
| 004 | 1 | attendance | HG-E101 2026-01-05 | individual_therapy | status: completed; status_as_written: completed | 8 | "completed, 50 minutes" |  |
| 005 | 1 | participant | HG-E101 2026-01-05 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 13 | "Rowan arrived independently and participated throughout the appointment" |  |
| 006 | 1 | participant | HG-E101 2026-01-05 | individual_therapy | name: Mara Voss; presence: not_stated; role: clinician; role_as_written: LCSW | 7 | "Clinician: Mara Voss, LCSW" |  |
| 007 | 1 | stated_minutes | HG-E101 2026-01-05 | individual_therapy | minutes: 50; of: patient_present | 8 | "50 minutes" |  |
| 008 | 1 | score |  |  | completed_date: 2026-01-05; instrument: PHQ-9; relation: completion; score: 18 | 15 | "PHQ-9 completed by Rowan on 2026-01-05: total score 18" |  |
| 009 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: patient; summary: Several weeks of low mood; topic: mood | 11 | "Rowan describes several weeks of low mood" |  |
| 010 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: patient; summary: Reduced interest in usual activities; topic: functioning | 11 | "reduced interest in usual activities" |  |
| 011 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: patient; summary: Fragmented sleep; topic: sleep | 11 | "fragmented sleep" |  |
| 012 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: patient; summary: Difficulty beginning ordinary tasks; topic: functioning | 11 | "difficulty beginning ordinary tasks" |  |
| 013 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Worry increases when thinking about work return; topic: anxiety | 11 | "Worry increases when thinking about returning to work after a recent leave" |  |
| 014 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Postponing email replies, avoiding conversations, spending more time alone; topic: functioning | 11 | "Rowan has been postponing email replies, avoiding conversations about the return date, and spending more time alone at home" |  |
| 015 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Wants a routine to make work transition feel manageable; topic: functioning | 11 | "They want a routine that makes the work transition feel manageable" |  |
| 016 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Speech clear and organized; topic: other | 13 | "Speech was clear and organized" |  |
| 017 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Affect subdued but responsive; topic: mood | 13 | "Affect was subdued but responsive" |  |
| 018 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: patient; summary: Wakes in the night and checks the time repeatedly; topic: sleep | 13 | "Rowan described waking in the night and then checking the time repeatedly" |  |
| 019 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Daytime fatigue appears to make avoidance more likely; topic: functioning | 13 | "Daytime fatigue appears to make avoidance more likely" |  |
| 020 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: No immediate safety concern identified; topic: safety | 13 | "No immediate safety concern was identified in today's assessment" |  |
| 021 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Able to discuss support contacts and seeking help if needed; topic: functioning | 13 | "Rowan was able to discuss support contacts and ways to seek additional help if needed" |  |
| 022 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Depressive symptoms; topic: mood | 15 | "Clinical impressions are depressive symptoms with anxiety and behavioral avoidance" |  |
| 023 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Anxiety; topic: anxiety | 15 | "Clinical impressions are depressive symptoms with anxiety and behavioral avoidance" |  |
| 024 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Behavioral avoidance; topic: functioning | 15 | "Clinical impressions are depressive symptoms with anxiety and behavioral avoidance" |  |
| 025 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Selected opening work inbox for five minutes without requiring immediate reply; topic: functioning | 17 | "Rowan selected opening their work inbox for five minutes without requiring an immediate reply" |  |
| 026 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: Consented to involving partner in family visit focused on practical support; topic: functioning | 19 | "Rowan consented to involving their partner in a family visit focused on practical support" |  |
| 027 | 1 | plan_rule |  |  | end_date: 2026-01-30; rule: episode_period; start_date: 2026-01-05 | 11 | "The current outpatient episode is planned for January 5 through January 30" |  |
| 028 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization" |  |

Coverage: 13 times, dates and record numbers in the document. 12 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E101 | captured on another line |

### BH-D003: signed_treatment_plan_jan05.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-21 | plan | Outpatient treatment plan | signed by Mara Voss, 2026-01-05 13:05 |  |  | period_start 2026-01-05; period_end 2026-01-30; signed 2026-01-05 13:05; created 2026-01-05 13:12 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | stated_minutes |  |  | minutes: 150; of: patient_present | 12 | "at least 150 minutes of patient-present therapy in each Monday–Sunday week" |  |
| 002 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: depressed mood; topic: mood | 10 | "depressed mood" |  |
| 003 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: sleep disruption; topic: sleep | 10 | "sleep disruption" |  |
| 004 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: anxiety about resuming work responsibilities; topic: anxiety | 10 | "anxiety about resuming work responsibilities" |  |
| 005 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: avoidance of tasks and communication; topic: functioning | 10 | "avoidance of tasks and communication" |  |
| 006 | 1 | observation |  |  | date: 2026-01-05; speaker: patient; summary: wants to improve follow-through without waiting for anxiety to disappear; topic: functioning | 10 | "Rowan wishes to improve follow-through without waiting for anxiety to disappear" |  |
| 007 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: repeated reminders increase tension; topic: anxiety | 10 | "repeated reminders sometimes increase tension" |  |
| 008 | 1 | plan_rule |  |  | end_date: 2026-01-30; rule: episode_period; start_date: 2026-01-05 | 6 | "Episode dates: 2026-01-05 through 2026-01-30" |  |
| 009 | 1 | plan_rule |  |  | measure: therapy_days; minimum: 3; period: week; rule: requirement | 12 | "at least 3 therapy days in each Monday–Sunday week" | unverified |
| 010 | 1 | plan_rule |  |  | measure: minutes; minimum: 150; period: week; rule: requirement | 12 | "at least 150 minutes of patient-present therapy in each Monday–Sunday week" |  |
| 011 | 1 | plan_rule |  |  | rule: week_definition; week_starts_on: monday | 12 | "each Monday–Sunday week" |  |
| 012 | 1 | plan_rule |  |  | patient_must_be_present: True; rule: therapy_day_definition; service_classes: individual_therapy, group_therapy, family_therapy | 12 | "A therapy day is a calendar day on which Rowan participates in individual, group, or family psychotherapy" |  |
| 013 | 1 | plan_rule |  |  | patient_must_be_present: True; rule: counted_service; service_classes: individual_therapy, group_therapy, family_therapy | 12 | "Patient-present individual, group, and family therapy contribute to the minute goal" |  |
| 014 | 1 | plan_rule |  |  | rule: excluded_service; service_classes: medication_management, collateral_contact, care_coordination | 12 | "Medication management, contacts with collateral informants only, and care coordination do not contribute" |  |
| 015 | 1 | plan_rule |  |  | goal_number: 1; rule: clinical_goal; text: improve daily activity and task initiation | 14 | "improve daily activity and task initiation" |  |
| 016 | 1 | plan_rule |  |  | goal_number: 2; rule: clinical_goal; text: improve coping with anxiety and disrupted sleep | 16 | "improve coping with anxiety and disrupted sleep" |  |
| 017 | 1 | plan_rule |  |  | goal_number: 3; rule: clinical_goal; text: support a workable return to employment | 18 | "support a workable return to employment" |  |
| 018 | 1 | plan_rule |  |  | rule: other; text: assess participation, symptoms, and practical functioning during the episode. Adjust the schedule when clinically indicated or when access barriers arise | 20 | "assess participation, symptoms, and practical functioning during the episode. Adjust the schedule when clinically indicated or when access barriers arise" |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D004: group_facilitator_jan06.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | clinical_note | Coping skills group | signed by None, 2026-01-06 12:02 |  |  | service 2026-01-06; signed 2026-01-06 12:02 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E102 2026-01-06 | group_therapy |  | 4 | "Harbor Grove Behavioral Health \| Coping skills group" |  |
| 002 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 5 | "Group scheduled 10:00–11:30 local" |  |
| 003 | 1 | time | HG-E102 2026-01-06 | group_therapy | detail: break; end: 11:00; label: actual; position: body; start: 10:45; what: no_therapy_interval | 12 | "took a break from 10:45 to 11:00" |  |
| 004 | 1 | participant | HG-E102 2026-01-06 | group_therapy | name: Leena Park; presence: present; role: clinician; role_as_written: Facilitator | 10 | "The facilitator demonstrated paced breathing" |  |
| 005 | 1 | participant | HG-E102 2026-01-06 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 14 | "Rowan was quiet initially and responded when invited to identify a situation involving avoidance" |  |
| 006 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: was quiet initially; topic: functioning | 14 | "Rowan was quiet initially" |  |
| 007 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: responded when invited to identify avoidance situation; topic: functioning | 14 | "responded when invited to identify a situation involving avoidance" |  |
| 008 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: patient; summary: feared being asked for a firm return date; topic: anxiety | 14 | "feared being asked for a firm return date" |  |
| 009 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: patient; summary: delayed replying to work message; topic: functioning | 14 | "delaying a reply to a work message" |  |
| 010 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: practiced a breathing exercise; topic: functioning | 14 | "Rowan practiced a breathing exercise" |  |
| 011 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: selected reading message before deciding how to respond as next step; topic: functioning | 14 | "selected reading the message before deciding how to respond as a possible next step" |  |
| 012 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: participation was relevant to topic; topic: functioning | 14 | "Their participation was relevant to the topic" |  |
| 013 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: appeared receptive to peer suggestions; topic: functioning | 14 | "they appeared receptive to peer suggestions" |  |
| 014 | 1 | statement | HG-E102 2026-01-06 | group_therapy | says: no_therapy_provided | 12 | "No therapy was conducted during that interval" |  |

Coverage: 11 times, dates and record numbers in the document. 10 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E102 | captured on another line |

### BH-D005: early_group_attendance_roster.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | attendance_record | Group desk attendance extract | not_stated |  | copy; original signed by None, None | exported_or_prepared 2026-01-12 15:10; service 2026-01-06; service 2026-01-12 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E102 2026-01-06 | group_therapy |  | 10 | "HG-E102" |  |
| 002 | 1 | contact | HG-E105 2026-01-12 | group_therapy |  | 11 | "HG-E105" |  |
| 003 | 1 | modality | HG-E102 2026-01-06 | group_therapy | modality: in_person | 13 | "group room" |  |
| 004 | 1 | modality | HG-E105 2026-01-12 | group_therapy | modality: in_person | 15 | "group began" |  |
| 005 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 10 | "10:00–11:30" |  |
| 006 | 1 | time | HG-E102 2026-01-06 | group_therapy | label: actual; position: table; start: 10:15; what: patient_arrival | 10 | "10:15" |  |
| 007 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:15; label: actual; position: table; what: patient_departure | 10 | "11:15" |  |
| 008 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 11 | "10:00–11:30" |  |
| 009 | 1 | time | HG-E105 2026-01-12 | group_therapy | label: actual; position: table; start: 10:00; what: patient_arrival | 11 | "10:00" |  |
| 010 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 11 | "11:30" |  |
| 011 | 1 | attendance | HG-E102 2026-01-06 | group_therapy | reason: Late arrival after difficulty finding parking; early departure for previously arranged ride; status: attended_part; status_as_written: Attended part | 10 | "Attended part" |  |
| 012 | 1 | attendance | HG-E105 2026-01-12 | group_therapy | status: attended; status_as_written: Attended full | 11 | "Attended full" |  |
| 013 | 1 | participant | HG-E102 2026-01-06 | group_therapy | name: Rowan; presence: present_part; role: patient | 10 | "Attended part" |  |
| 014 | 1 | participant | HG-E105 2026-01-12 | group_therapy | name: Rowan; presence: present; role: patient | 11 | "Attended full" |  |
| 015 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: patient; summary: Called from building entrance saying running behind after difficulty finding parking; topic: functioning | 13 | "Rowan called from the building entrance to say they were running behind after difficulty finding parking." |  |
| 016 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: patient; summary: Advised needing to leave early for previously arranged ride; topic: functioning | 13 | "Rowan advised the facilitator that they would need to leave early for a previously arranged ride." |  |
| 017 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: staff; summary: No transport concern reported; topic: functioning | 15 | "No transport concern was reported at that time." |  |
| 018 | 1 | statement |  |  | says: is_copy_or_resend | 17 | "Prepared from the signed reception attendance sheet for the two dates listed." |  |
| 019 | 1 | statement |  |  | says: other | 17 | "The desk records arrival and departure when members enter or leave the scheduled group. Session activities and room breaks are documented in the facilitator's record." |  |

Coverage: 19 times, dates and record numbers in the document. 19 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D006: early_appointment_status_export.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-21 | schedule_export | Export | not_stated |  |  | exported_or_prepared 2026-01-16 16:50 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E101 2026-01-05 | individual_therapy |  | 10 | "HG-E101   \| Jan05 \| Individual therapy     \| 09:00–09:50" |  |
| 002 | 1 | contact | HG-E102 2026-01-06 | group_therapy |  | 11 | "HG-E102   \| Jan06 \| Coping skills group    \| 10:00–11:30" |  |
| 003 | 1 | contact | HG-E103 2026-01-08 | individual_therapy |  | 12 | "HG-E103   \| Jan08 \| Individual therapy     \| 11:00–11:45" |  |
| 004 | 1 | contact | HG-E104 2026-01-09 | family_therapy |  | 13 | "HG-E104   \| Jan09 \| Family therapy         \| 14:00–14:45" |  |
| 005 | 1 | contact | HG-E105 2026-01-12 | group_therapy |  | 14 | "HG-E105   \| Jan12 \| Coping skills group    \| 10:00–11:30" |  |
| 006 | 1 | contact | HG-E106 2026-01-13 | medication_management |  | 15 | "HG-E106   \| Jan13 \| Medication management  \| 09:00–09:25" |  |
| 007 | 1 | contact | HG-E107 2026-01-14 | individual_therapy |  | 16 | "HG-E107   \| Jan14 \| Individual therapy     \| 11:00–11:45" |  |
| 008 | 1 | contact | HG-E108 2026-01-15 | group_therapy |  | 17 | "HG-E108   \| Jan15 \| Coping skills group    \| 10:00–11:30" |  |
| 009 | 1 | contact | HG-E109 2026-01-16 | collateral_contact |  | 18 | "HG-E109   \| Jan16 \| Family collateral      \| 14:00–14:40" |  |
| 010 | 1 | time | HG-E101 2026-01-05 | individual_therapy | end: 09:50; label: scheduled; position: table; start: 09:00; what: contact_interval | 10 | "09:00–09:50" |  |
| 011 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 11 | "10:00–11:30" |  |
| 012 | 1 | time | HG-E103 2026-01-08 | individual_therapy | end: 11:45; label: scheduled; position: table; start: 11:00; what: contact_interval | 12 | "11:00–11:45" |  |
| 013 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: scheduled; position: table; start: 14:00; what: contact_interval | 13 | "14:00–14:45" |  |
| 014 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 14 | "10:00–11:30" |  |
| 015 | 1 | time | HG-E106 2026-01-13 | medication_management | end: 09:25; label: scheduled; position: table; start: 09:00; what: contact_interval | 15 | "09:00–09:25" |  |
| 016 | 1 | time | HG-E107 2026-01-14 | individual_therapy | end: 11:45; label: scheduled; position: table; start: 11:00; what: contact_interval | 16 | "11:00–11:45" |  |
| 017 | 1 | time | HG-E108 2026-01-15 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 17 | "10:00–11:30" |  |
| 018 | 1 | time | HG-E109 2026-01-16 | collateral_contact | end: 14:40; label: scheduled; position: table; start: 14:00; what: contact_interval | 18 | "14:00–14:40" |  |
| 019 | 1 | attendance | HG-E101 2026-01-05 | individual_therapy | status: completed; status_as_written: Completed | 10 | "Completed" |  |
| 020 | 1 | attendance | HG-E102 2026-01-06 | group_therapy | status: attended_part; status_as_written: Attended part | 11 | "Attended part" |  |
| 021 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | reason: remained unarrived at close of its appointment slot; status: no_show; status_as_written: No show | 12 | "No show" |  |
| 022 | 1 | attendance | HG-E104 2026-01-09 | family_therapy | status: completed; status_as_written: Completed | 13 | "Completed" |  |
| 023 | 1 | attendance | HG-E105 2026-01-12 | group_therapy | status: completed; status_as_written: Completed | 14 | "Completed" |  |
| 024 | 1 | attendance | HG-E106 2026-01-13 | medication_management | status: completed; status_as_written: Completed | 15 | "Completed" |  |
| 025 | 1 | attendance | HG-E107 2026-01-14 | individual_therapy | status: completed; status_as_written: Completed | 16 | "Completed" |  |
| 026 | 1 | attendance | HG-E108 2026-01-15 | group_therapy | reason: staff illness was reported; status: cancelled_by_clinic; status_as_written: Clinic cancelled | 17 | "Clinic cancelled" |  |
| 027 | 1 | attendance | HG-E109 2026-01-16 | collateral_contact | reason: Rowan could not attend; status: completed; status_as_written: Completed | 18 | "Completed" |  |
| 028 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Rowan Mercer; presence: absent; role: patient | 20 | "Rowan could not attend" |  |
| 029 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |
| 030 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: no_patient_contact | 20 | "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend." |  |

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
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | clinical_note | Family psychotherapy | signed by Mara Voss, 2026-01-09 16:24 |  |  | service 2026-01-09; signed 2026-01-09 16:24 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E104 2026-01-09 | family_therapy |  | 6 | "Encounter HG-E104 \| 2026-01-09, 14:00–14:45 local" |  |
| 002 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: not_labelled; position: header; start: 14:00; what: contact_interval | 6 | "14:00–14:45" |  |
| 003 | 1 | attendance | HG-E104 2026-01-09 | family_therapy | status: attended; status_as_written: remained present and engaged throughout the visit | 16 | "Rowan remained present and engaged throughout the visit." |  |
| 004 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Rowan; presence: present; role: patient | 7 | "Present: Rowan and partner, Casey Mercer" |  |
| 005 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Casey Mercer; presence: present; role: family_or_partner; role_as_written: partner | 7 | "Present: Rowan and partner, Casey Mercer" |  |
| 006 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Mara Voss; presence: present; role: clinician; role_as_written: LCSW | 8 | "Clinicians: Mara Voss, LCSW; cofacilitator Leena Park, LPC" |  |
| 007 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Leena Park; presence: present; role: clinician; role_as_written: cofacilitator Leena Park, LPC | 8 | "cofacilitator Leena Park, LPC" |  |
| 008 | 1 | stated_minutes | HG-E104 2026-01-09 | family_therapy | minutes: 45; of: patient_present | 9 | "Patient-present family therapy duration: 45 minutes" |  |
| 009 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Appointment addressed patterns of support as patient rebuilds routine; topic: reason_for_contact | 12 | "The appointment focused on patterns of support at home as Rowan attempts to rebuild a routine." |  |
| 010 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: Felt watched when asked repeatedly about work contact; topic: other | 12 | "Rowan described feeling watched when asked repeatedly whether they had contacted work." |  |
| 011 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: family_or_partner; speaker_name: Casey; summary: Worry that space might leave patient isolated; topic: functioning | 12 | "Casey described worry that giving Rowan space might leave them isolated." |  |
| 012 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Both acknowledged intentions differed from how other experienced exchange; topic: progress | 12 | "Both were able to acknowledge that their intentions differed from how the other person experienced the exchange." |  |
| 013 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: More animated when describing shared evening walk; topic: mood | 16 | "They became more animated when describing a shared evening walk" |  |
| 014 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Identified shared activity as support without pressure; topic: functioning | 16 | "identified this as support that did not feel like pressure" |  |
| 015 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Partner agreed to single planned check-in instead of repeated reminders; topic: functioning | 16 | "Casey agreed to use a single planned check-in about work preparation instead of repeated reminders." |  |
| 016 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Agreed to communicate when wanting practical assistance versus quiet company; topic: functioning | 16 | "Rowan agreed to say when they wanted practical assistance versus quiet company." |  |
| 017 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |

Coverage: 10 times, dates and record numbers in the document. 9 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 18 | number | HG-E104 | captured on another line |

### BH-D008: family_cofacilitator_jan09.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Accompanying clinical entry | signed by Leena Park, LPC, 2026-01-10 08:42 |  |  | service 2026-01-09; signed 2026-01-10 08:42 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E104 2026-01-09 | family_therapy |  | 6 | "Encounter HG-E104" |  |
| 002 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: scheduled; position: header; start: 14:00; what: contact_interval | 6 | "14:00–14:45" |  |
| 003 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: actual; position: body; start: 14:00; what: patient_present | 8 | "for the full 45 minutes" |  |
| 004 | 1 | attendance | HG-E104 2026-01-09 | family_therapy | status: attended; status_as_written: both present for the full 45 minutes | 8 | "both present for the full 45 minutes" |  |
| 005 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Rowan Mercer; presence: present; role: patient | 8 | "Rowan Mercer and Casey Mercer; both present for the full 45 minutes" |  |
| 006 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Casey Mercer; presence: present; role: family_or_partner | 8 | "Rowan Mercer and Casey Mercer; both present for the full 45 minutes" |  |
| 007 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Leena Park; presence: not_stated; role: clinician; role_as_written: LPC, cofacilitator | 7 | "Author: Leena Park, LPC, cofacilitator with Mara Voss, LCSW" |  |
| 008 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Mara Voss; presence: not_stated; role: clinician; role_as_written: LCSW | 7 | "Author: Leena Park, LPC, cofacilitator with Mara Voss, LCSW" |  |
| 009 | 1 | stated_minutes | HG-E104 2026-01-09 | family_therapy | minutes: 45; of: contact_total | 8 | "for the full 45 minutes" |  |
| 010 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: described partner reminders as evidence of falling behind; topic: functioning | 11 | "Rowan initially described partner reminders as evidence that they were falling behind." |  |
| 011 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: family_or_partner; speaker_name: Casey Mercer; summary: reminders were attempt to help but repeated prompts increased tension; topic: other | 11 | "Casey explained that the reminders were an attempt to help, while also recognizing that repeated prompts increased tension." |  |
| 012 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: stated that partner wanted reassurance about preparation happening; topic: functioning | 13 | "Rowan was able to state that Casey wanted reassurance that some preparation was happening." |  |
| 013 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: family_or_partner; speaker_name: Casey Mercer; summary: reflected partner's wish to keep ownership of return-to-work process; topic: functioning | 13 | "Casey reflected Rowan's wish to keep ownership of the return-to-work process." |  |
| 014 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: rehearsal became less defensive with repetition; topic: progress | 13 | "The rehearsal became less defensive with repetition." |  |
| 015 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: both contributed ideas for a brief, predictable check-in; topic: functioning | 13 | "Both participants contributed ideas for a brief, predictable check-in." |  |
| 016 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: selected evening walk as shared activity without focusing on progress discussion; topic: functioning | 15 | "The couple selected an evening walk as an activity they could share without making it a discussion about progress." |  |
| 017 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: evening walk more acceptable than lengthy review of unfinished tasks; topic: functioning | 15 | "Rowan said this felt more acceptable than a lengthy review of unfinished tasks." |  |

Coverage: 10 times, dates and record numbers in the document. 9 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 15 | number | HG-E104 | captured on another line |

### BH-D009: group_facilitator_jan12.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | clinical_note |  | signed by None, 2026-01-12 12:20 |  |  | service 2026-01-12; signed 2026-01-12 12:20 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E105 2026-01-12 | group_therapy |  | 4 | "Coping skills group" |  |
| 002 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 6 | "Scheduled group 10:00–11:30 local" |  |
| 003 | 1 | time | HG-E105 2026-01-12 | group_therapy | detail: Group break; no therapeutic activity occurred; end: 10:55; label: not_labelled; position: body; start: 10:40; what: no_therapy_interval | 12 | "Group break: 10:40–10:55; no therapeutic activity occurred during the break." |  |
| 004 | 1 | participant | HG-E105 2026-01-12 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 14 | "Rowan contributed an example about leaving work messages unopened." |  |
| 005 | 1 | participant | HG-E105 2026-01-12 | group_therapy | name: Leena Park; presence: present; role: clinician; role_as_written: Facilitator | 16 | "The facilitator reinforced restarting with a smaller step and reviewing what interfered." |  |
| 006 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: patient; summary: Took a walk with Casey over the weekend; topic: functioning | 14 | "taking a walk with Casey over the weekend" |  |
| 007 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: patient; summary: Walk helped evening feel less dominated by worry; topic: mood | 14 | "helped the evening feel less dominated by worry" |  |
| 008 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: patient; summary: Identified looking at one message as a lower step than replying to all outstanding messages; topic: functioning | 14 | "identified looking at one message as a lower step than replying to every outstanding message" |  |
| 009 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: patient; summary: Wrote down action to try after breakfast and asked how to respond if morning went poorly; topic: functioning | 14 | "wrote down an action to try after breakfast and asked how to respond if the morning went poorly" |  |
| 010 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: clinician; summary: Listened to peers and offered supportive comment to another member; topic: functioning | 16 | "Rowan listened to peers and offered a supportive comment to another member." |  |

Coverage: 11 times, dates and record numbers in the document. 10 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 5 | number | HG-E105 | captured on another line |

### BH-D010: medication_review_jan13.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | clinical_note | Prescriber visit | signed by Elias Brenner, 2026-01-13 10:04 | completed |  | service 2026-01-13; signed 2026-01-13 10:04 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E106 2026-01-13 | medication_management |  | 11 | "Rowan attended for medication management" |  |
| 002 | 1 | modality | HG-E106 2026-01-13 | medication_management | modality: in_person | 7 | "Actual visit 09:00–09:25 local" |  |
| 003 | 1 | time | HG-E106 2026-01-13 | medication_management | end: 09:25; label: actual; position: header; start: 09:00; what: contact_interval | 7 | "Actual visit 09:00–09:25 local" |  |
| 004 | 1 | attendance | HG-E106 2026-01-13 | medication_management | status: attended; status_as_written: attended | 11 | "Rowan attended for medication management" |  |
| 005 | 1 | participant | HG-E106 2026-01-13 | medication_management | name: Rowan Mercer; presence: present; role: patient | 11 | "Rowan attended for medication management" |  |
| 006 | 1 | participant | HG-E106 2026-01-13 | medication_management | name: Elias Brenner; presence: not_stated; role: clinician; role_as_written: Clinician | 8 | "Clinician: Elias Brenner, NP" |  |
| 007 | 1 | stated_minutes | HG-E106 2026-01-13 | medication_management | minutes: 25; of: contact_total | 7 | "completed, 25 minutes" |  |
| 008 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: continuing sleep interruption and daytime tiredness; topic: sleep | 11 | "Rowan reported continuing sleep interruption and daytime tiredness" |  |
| 009 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: mood somewhat less heavy on days with planned activity; topic: mood | 11 | "They described mood as somewhat less heavy on days with a planned activity" |  |
| 010 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: concerned about work communication; topic: functioning | 11 | "remained concerned about work communication" |  |
| 011 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: denied new medication-related concern requiring urgent intervention; topic: medication | 13 | "Rowan denied a new medication-related concern requiring urgent intervention" |  |
| 012 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: no new physical complaint raised; topic: other | 13 | "No new physical complaint was raised during this visit" |  |
| 013 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: ongoing depressive symptoms; topic: mood | 15 | "ongoing depressive and anxiety symptoms" |  |
| 014 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: ongoing anxiety symptoms; topic: anxiety | 15 | "ongoing depressive and anxiety symptoms" |  |
| 015 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: ongoing sleep disruption; topic: sleep | 15 | "sleep disruption" |  |
| 016 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: engaged with therapy program and intends to continue scheduled appointments; topic: progress | 15 | "Rowan is engaged with the therapy program and intends to continue the scheduled appointments" |  |
| 017 | 1 | statement |  |  | says: other | 17 | "No separate psychotherapy component was provided or documented" |  |

Coverage: 9 times, dates and record numbers in the document. 8 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E106 | captured on another line |

### BH-D011: individual_therapy_jan14.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | clinical_note | Individual psychotherapy | signed by Mara Voss, 2026-01-14 13:16 | completed |  | service 2026-01-14; signed 2026-01-14 13:16 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E107 2026-01-14 | individual_therapy |  | 6 | "Encounter HG-E107 \| Date 2026-01-14" |  |
| 002 | 1 | modality | HG-E107 2026-01-14 | individual_therapy | modality: in_person | 7 | "Patient-present session" |  |
| 003 | 1 | time | HG-E107 2026-01-14 | individual_therapy | end: 11:45; label: actual; position: body; start: 11:00; what: contact_interval | 7 | "Patient-present session 11:00–11:45 local" |  |
| 004 | 1 | time | HG-E107 2026-01-14 | individual_therapy | end: 11:45; label: actual; position: body; start: 11:00; what: patient_present | 7 | "Patient-present session 11:00–11:45 local" |  |
| 005 | 1 | attendance | HG-E107 2026-01-14 | individual_therapy | status: completed; status_as_written: completed | 7 | "completed" |  |
| 006 | 1 | participant | HG-E107 2026-01-14 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 7 | "Patient-present session" |  |
| 007 | 1 | participant | HG-E107 2026-01-14 | individual_therapy | name: Mara Voss; presence: not_stated; role: clinician; role_as_written: Clinician | 8 | "Clinician: Mara Voss, LCSW" |  |
| 008 | 1 | stated_minutes | HG-E107 2026-01-14 | individual_therapy | minutes: 45; of: patient_present | 7 | "45 minutes" |  |
| 009 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: completed several small activities including opening work message and taking two short walks; topic: functioning | 11 | "Rowan reported completing several small activities since the prior individual appointment, including opening a work message and taking two short walks." |  |
| 010 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: has not yet replied to message; topic: functioning | 11 | "have not yet replied to the message" |  |
| 011 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: continues to imagine being asked questions unable to answer; topic: anxiety | 11 | "continue to imagine being asked questions they cannot answer" |  |
| 012 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: family appointment helpful because planned check-in with Casey reduced repeated reminders; topic: functioning | 11 | "Rowan described the family appointment as helpful because the planned check-in with Casey reduced repeated reminders." |  |
| 013 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: sleep remains interrupted; topic: sleep | 11 | "Sleep remains interrupted" |  |
| 014 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: getting started in morning continues to require effort; topic: functioning | 11 | "getting started in the morning continues to require effort" |  |
| 015 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: noticed physical tension during rehearsal; topic: other | 13 | "Rowan noticed physical tension during the rehearsal" |  |
| 016 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: was able to remain with task; topic: functioning | 13 | "was able to remain with the task" |  |
| 017 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: message seemed less overwhelming when it did not need to solve entire return-to-work question; topic: anxiety | 13 | "They said the message seemed less overwhelming when it did not need to solve the entire return-to-work question." |  |
| 018 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: identified setting out appointment information evening before as helpful preparation step; topic: functioning | 15 | "Rowan identified setting out appointment information the evening before as a helpful preparation step." |  |
| 019 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: affect more varied than at intake; topic: mood | 15 | "Affect was more varied than at intake" |  |
| 020 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: worry evident when discussing employment; topic: anxiety | 15 | "worry was evident when discussing employment" |  |
| 021 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D012: partner_collateral_jan16.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | clinical_note | Family collateral | signed by Mara Voss, 2026-01-16 16:08 |  |  | service 2026-01-16; signed 2026-01-16 16:08 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E109 2026-01-16 | collateral_contact |  | 6 | "Encounter HG-E109 \| Date 2026-01-16 \| 14:00–14:40 local" |  |
| 002 | 1 | time | HG-E109 2026-01-16 | collateral_contact | end: 14:40; label: scheduled; position: header; start: 14:00; what: contact_interval | 6 | "14:00–14:40 local" |  |
| 003 | 1 | attendance | HG-E109 2026-01-16 | collateral_contact | status: absent; status_as_written: absent for the entire contact | 8 | "Rowan was absent for the entire contact" |  |
| 004 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Casey Mercer; presence: present; role: family_or_partner; role_as_written: partner | 11 | "Casey attended the arranged contact" |  |
| 005 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Rowan Mercer; presence: absent; role: patient | 8 | "Rowan was absent for the entire contact" |  |
| 006 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Mara Voss; presence: not_stated; role: clinician | 7 | "Clinician: Mara Voss, LCSW" |  |
| 007 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey; summary: Getting out for short walks and more willing to discuss the coming week; topic: functioning | 13 | "Casey reported that Rowan had been getting out for short walks and seemed more willing to discuss the coming week" |  |
| 008 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey; summary: Mornings remain difficult; topic: mood | 13 | "Mornings remain difficult," |  |
| 009 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey; summary: Becomes quiet when conversation turns to work; topic: functioning | 13 | "Casey described Rowan becoming quiet when the conversation turns to work" |  |
| 010 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: Scheduled evening check-in has reduced unplanned reminders; topic: progress | 13 | "The scheduled evening check-in has reduced unplanned reminders" |  |
| 011 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey; summary: Less argument when Casey asks what kind of help Rowan wants; topic: progress | 13 | "Casey said it takes effort to resist offering multiple solutions but has noticed less argument when asking what kind of help Rowan wants" |  |
| 012 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: no_patient_contact | 8 | "Rowan was absent for the entire contact" |  |
| 013 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: no_therapy_provided | 17 | "No patient-present psychotherapy occurred during this contact" |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D013: symptom_measure_review_jan16.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | questionnaire_review | Measurement review | unsigned |  |  | completed 2026-01-16 08:17; reviewed 2026-01-16 09:10 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-Q116 2026-01-16 | questionnaire_review |  | 4 | "Measurement review" |  |
| 002 | 1 | modality | HG-Q116 2026-01-16 | questionnaire_review | modality: other | 6 | "patient portal form HG-Q116" | unverified |
| 003 | 1 | score |  |  | completed_date: 2026-01-16; completed_time: 08:17; form_id: HG-Q116; instrument: PHQ-9; relation: completion; score: 14 | 8 | "Total score: 14" |  |
| 004 | 1 | score |  |  | completed_date: 2026-01-05; instrument: PHQ-9; relation: mention; score: 18 | 11 | "The submitted score is lower than the intake score of 18 recorded on January 5." |  |
| 005 | 1 | observation | HG-Q116 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: patient; speaker_name: Rowan; summary: Getting out of the apartment had become easier; topic: functioning | 11 | "getting out of the apartment had become a little easier" |  |
| 006 | 1 | observation | HG-Q116 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: patient; speaker_name: Rowan; summary: Thinking about work made them want to put things off; topic: functioning | 11 | "thinking about work continued to make them want to put things off" |  |
| 007 | 1 | observation | HG-Q116 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: patient; speaker_name: Rowan; summary: Sleep is inconsistent; topic: sleep | 11 | "Rowan also described sleep as inconsistent" |  |
| 008 | 1 | observation | HG-Q116 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; speaker_name: Mara Voss; summary: Some improvement in depressive symptoms; topic: progress | 13 | "some improvement in depressive symptoms" |  |
| 009 | 1 | observation | HG-Q116 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; speaker_name: Mara Voss; summary: Persistent avoidance remains clinically relevant; topic: functioning | 13 | "Persistent avoidance" |  |
| 010 | 1 | observation | HG-Q116 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; speaker_name: Mara Voss; summary: Difficulty initiating work communication remains clinically relevant; topic: functioning | 13 | "difficulty initiating work communication" |  |
| 011 | 1 | observation | HG-Q116 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; speaker_name: Mara Voss; summary: Sleep disruption remains clinically relevant; topic: sleep | 13 | "sleep disruption remain clinically relevant" |  |
| 012 | 1 | observation | HG-Q116 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; speaker_name: Mara Voss; summary: Has attempted small activities and communication practice but has not yet established a reliable routine; topic: functioning | 13 | "Rowan has attempted small activities and communication practice but has not yet established a reliable routine" |  |
| 013 | 1 | statement |  |  | says: not_a_visit | 15 | "no clinical appointment occurred at the time of review" |  |

Coverage: 10 times, dates and record numbers in the document. 8 captured, 2 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | PHQ-9 | captured on another line |
| 6 | number | HG-Q116 | captured on another line |

### BH-D014: imported_measure_summary_received_jan26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-19 | import_receipt | Administrative import receipt | not_stated |  | copy; original signed by None, None | received 2026-01-26 07:44; other 2026-01-16 09:10 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | score |  |  | completed_date: 2026-01-16; form_id: HG-Q116; instrument: PHQ-9; relation: copy; score: 14 | 13 | "PHQ-9   \| 14     \| 2026-01-16     \| HG-Q116" |  |
| 002 | 1 | observation |  |  | date: 2026-01-16; speaker: outside_professional; speaker_name: Mara Voss; summary: some improvement in depressive symptoms; topic: progress | 15 | "some improvement in depressive symptoms" |  |
| 003 | 1 | observation |  |  | date: 2026-01-16; speaker: outside_professional; speaker_name: Mara Voss; summary: ongoing avoidance of work communication; topic: functioning | 15 | "ongoing avoidance of work communication" |  |
| 004 | 1 | observation |  |  | date: 2026-01-16; speaker: outside_professional; speaker_name: Mara Voss; summary: inconsistent sleep; topic: sleep | 15 | "inconsistent sleep" |  |
| 005 | 1 | statement |  |  | says: no_new_assessment | 17 | "No newly completed patient questionnaire is included in this batch." |  |
| 006 | 1 | statement |  |  | says: not_a_visit | 19 | "does not document a visit with Rowan" |  |

Coverage: 13 times, dates and record numbers in the document. 10 captured, 2 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-MEAS-0126 | not captured |
| 17 | date | January 16 | captured on another line |
| 17 | date | January 26 | captured on another line |

### BH-D015: missed_visit_outreach_jan08.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | scheduling_log | Scheduling support log | not_stated |  |  | entered 2026-01-08 15:52 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E103 2026-01-08 | individual_therapy |  | 11 | "scheduled individual visit" |  |
| 002 | 1 | contact | 2026-01-08 | scheduling_contact |  | 13 | "Outbound call placed to the patient's recorded number" |  |
| 003 | 1 | contact | 2026-01-08 | scheduling_contact |  | 15 | "Rowan returned the call" |  |
| 004 | 1 | modality | HG-E103 2026-01-08 | individual_therapy | modality: in_person | 9 | "The appointment remained on the room schedule" |  |
| 005 | 1 | modality | 2026-01-08 | scheduling_contact | modality: message | 13 | "a brief callback request was left" |  |
| 006 | 1 | modality | 2026-01-08 | scheduling_contact | modality: telephone | 15 | "Rowan returned the call" |  |
| 007 | 1 | time | HG-E103 2026-01-08 | individual_therapy | end: 11:45; label: scheduled; position: header; start: 11:00; what: contact_interval | 6 | "11:00–11:45 local" |  |
| 008 | 1 | time | 2026-01-08 | scheduling_contact | label: actual; position: body; start: 13:20; what: connection | 13 | "13:20: Outbound call placed to the patient's recorded number" |  |
| 009 | 1 | time | 2026-01-08 | scheduling_contact | label: actual; position: body; start: 15:36; what: connection | 15 | "15:36: Rowan returned the call" |  |
| 010 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | status: no_show; status_as_written: no show | 11 | "Appointment marked no show" |  |
| 011 | 1 | participant | HG-E103 2026-01-08 | individual_therapy | name: Rowan Mercer; presence: absent; role: patient | 11 | "Rowan was not seen for the scheduled individual visit" |  |
| 012 | 1 | participant | 2026-01-08 | scheduling_contact | name: Rowan Mercer; presence: present; role: patient | 15 | "Rowan returned the call" |  |
| 013 | 1 | participant | 2026-01-08 | scheduling_contact | presence: present; role: staff; role_as_written: Staff | 15 | "Staff verified the appointment time and location" |  |
| 014 | 1 | observation | 2026-01-08 | scheduling_contact | date: 2026-01-08; speaker: patient; summary: poor night of sleep; topic: sleep | 15 | "They said the morning had gotten away from them after a poor night of sleep" |  |
| 015 | 1 | observation | 2026-01-08 | scheduling_contact | date: 2026-01-08; speaker: patient; summary: confirmed intention to attend next day's family visit; topic: functioning | 15 | "confirmed that they still intended to attend the next day's visit with Casey" |  |
| 016 | 1 | statement | 2026-01-08 | scheduling_contact | says: no_therapy_provided | 17 | "No therapy intervention was conducted" |  |

Coverage: 10 times, dates and record numbers in the document. 7 captured, 2 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | date | 2026-01-08 | captured on another line |
| 6 | number | HG-E103 | captured on another line |
| 13 | date | January 9 | not captured |

### BH-D016: group_cancellation_notice_jan15.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | cancellation_notice | Notice | not_stated |  |  | entered 2026-01-15 08:12; other 2026-01-15 08:15; other 2026-01-15 11:35 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E108 2026-01-15 | group_therapy |  | 9 | "The coping skills group scheduled for January 15 from 10:00 to 11:30" |  |
| 002 | 1 | contact | 2026-01-15 | scheduling_contact |  | 13 | "Rowan called the desk and acknowledged receiving the notice." |  |
| 003 | 1 | modality | HG-E108 2026-01-15 | group_therapy | modality: in_person | 9 | "The group room has been released from the schedule" |  |
| 004 | 1 | modality | 2026-01-15 | scheduling_contact | modality: telephone | 13 | "Rowan called the desk" |  |
| 005 | 1 | time | HG-E108 2026-01-15 | group_therapy | end: 11:30; label: scheduled; position: body; start: 10:00; what: contact_interval | 9 | "from 10:00 to 11:30" |  |
| 006 | 1 | time | 2026-01-15 | scheduling_contact | label: actual; position: body; start: 08:37; what: connection | 13 | "08:37: Rowan called the desk" |  |
| 007 | 1 | attendance | HG-E108 2026-01-15 | group_therapy | reason: staff illness; status: cancelled_by_clinic; status_as_written: cancelled by the clinic | 9 | "cancelled by the clinic because of staff illness" |  |
| 008 | 1 | attendance | 2026-01-15 | scheduling_contact | status: attended; status_as_written: called | 13 | "Rowan called the desk and acknowledged receiving the notice." |  |
| 009 | 1 | participant | HG-E108 2026-01-15 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 9 | "registered participants" |  |
| 010 | 1 | participant | 2026-01-15 | scheduling_contact | name: Rowan Mercer; presence: present; role: patient | 13 | "Rowan called the desk" |  |
| 011 | 1 | participant | 2026-01-15 | scheduling_contact | presence: present; role: staff | 13 | "Staff confirmed that" |  |
| 012 | 1 | statement | HG-E108 2026-01-15 | group_therapy | says: no_patient_contact | 15 | "No group was held and no participants were seen for HG-E108." |  |

Coverage: 12 times, dates and record numbers in the document. 9 captured, 2 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E108 | captured on another line |
| 13 | date | January 16 | not captured |
| 15 | number | HG-E108 | captured on another line |

### BH-D101: BH-D101_group_content_2026-01-19.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-14 | clinical_note | Skills group clinical record | signed by Leah Chen, LCSW, 2026-01-19 12:08 |  |  | service 2026-01-19; signed 2026-01-19 12:08 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 4 | "Group encounter: HG-E110" |  |
| 002 | 1 | modality | HG-E110 2026-01-19 | group_therapy | modality: in_person | 6 | "Scheduled group: 10:00–11:30. Nontherapeutic break: 10:45–11:00." |  |
| 003 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 6 | "Scheduled group: 10:00–11:30" |  |
| 004 | 1 | time | HG-E110 2026-01-19 | group_therapy | detail: Restroom use and refreshments; end: 11:00; label: not_labelled; position: header; start: 10:45; what: no_therapy_interval | 6 | "Nontherapeutic break: 10:45–11:00" |  |
| 005 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 10 | "Rowan initially followed the exercise" |  |
| 006 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Leah Chen, LCSW; presence: not_stated; role: clinician; role_as_written: Facilitator | 4 | "Facilitator: Leah Chen, LCSW" |  |
| 007 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: patient; summary: Identified postponing message to supervisor as familiar pattern; topic: functioning | 10 | "identified postponing a message to a supervisor as a familiar pattern" |  |
| 008 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: Became visibly tense when discussion turned to workplace matters; topic: anxiety | 10 | "became visibly tense" |  |
| 009 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: patient; summary: Found the amount of discussion difficult to manage; topic: anxiety | 10 | "said the amount of discussion felt difficult to manage" |  |

Coverage: 11 times, dates and record numbers in the document. 11 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D102: BH-D102_original_attendance_2026-01-19.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-20 | attendance_record | Patient-specific attendance roster extract | signed by Leah Chen, LCSW, 2026-01-19 12:14 | Final |  | service 2026-01-19; signed 2026-01-19 12:14 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 4 | "Group encounter: HG-E110" |  |
| 002 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 8 | "Scheduled opening: 10:00 \| Scheduled closing: 11:30" |  |
| 003 | 1 | time | HG-E110 2026-01-19 | group_therapy | label: actual; position: header; start: 10:00; what: patient_arrival | 9 | "Patient arrival: 10:00" |  |
| 004 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: actual; position: header; what: patient_departure | 9 | "Patient departure: 11:30" |  |
| 005 | 1 | attendance | HG-E110 2026-01-19 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-19; entry_signed_time: 12:14; status: attended; status_as_written: Attended | 9 | "Status: Attended" |  |
| 006 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 14 | "Rowan was present for the opening check-in" |  |
| 007 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: patient; summary: The patient reported anxiety about reconnecting with work; topic: anxiety | 14 | "The patient identified anxiety about reconnecting with work" |  |
| 008 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: patient; summary: The patient accepted an exercise handout; topic: functioning | 14 | "accepted an exercise handout" |  |
| 009 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: patient; summary: The patient requested additional help, which prompted staff to arrange individual clinician access; topic: reason_for_contact | 14 | "Rowan requested additional help" |  |

Coverage: 11 times, dates and record numbers in the document. 11 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D103: BH-D103_attendance_correction_2026-01-20.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | correction | Attendance correction | signed by Leah Chen, LCSW, 2026-01-20 08:42 | Final |  | entered 2026-01-20; service 2026-01-19; signed 2026-01-20 08:42 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 5 | "group encounter HG-E110, service date January 19, 2026" |  |
| 002 | 1 | modality |  |  | modality: in_person | 9 | "Rowan leaving skills room B at 11:15" |  |
| 003 | 1 | time |  |  | label: actual; position: body; start: 10:00; what: patient_arrival | 7 | "Patient arrival remains 10:00" |  |
| 004 | 1 | time |  |  | end: 11:15; label: actual; position: body; what: patient_departure | 7 | "Patient departure for HG-E110 is 11:15" |  |
| 005 | 1 | participant |  |  | name: Rowan Mercer; presence: not_stated; role: patient | 7 | "Patient departure for HG-E110 is 11:15" |  |
| 006 | 1 | correction |  |  | field: departure; new_value: 11:15; old_value: 11:30; reason: the original group roster was found to retain the scheduled group closing time in Rowan's departure field | 7 | "Patient departure for HG-E110 is 11:15, replacing the original roster value of 11:30" |  |
| 007 | 1 | statement |  |  | says: no_clinical_service | 13 | "No additional clinical service was provided in making this correction" |  |
| 008 | 1 | statement |  |  | says: other | 11 | "This correction applies only to Rowan Mercer's departure field on the January 19 group attendance roster" |  |

Coverage: 15 times, dates and record numbers in the document. 11 captured, 4 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-E110 | captured on another line |
| 9 | time | 11:15 | captured on another line |
| 9 | time | 11:15 | captured on another line |
| 11 | date | January 19 | captured on another line |

### BH-D104: BH-D104_resent_roster_received_2026-01-26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-9 | cover_sheet |  | unsigned |  |  | received 2026-01-26 16:22 |
| 2 | 10-21 | attendance_record | ATTACHED ROSTER COPY | unsigned |  | copy; original signed by Leah Chen, LCSW, 2026-01-19 12:14 | service 2026-01-19; signed 2026-01-19 12:14; entered 2026-01-26 16:31 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 2 | contact | HG-E110 2026-01-19 | group_therapy |  | 11 | "Service date: January 19, 2026 \| Group encounter: HG-E110" |  |
| 002 | 2 | modality | HG-E110 2026-01-19 | group_therapy | modality: in_person | 12 | "Location: Outpatient skills room B" |  |
| 003 | 2 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 13 | "Scheduled opening: 10:00 \| Scheduled closing: 11:30" |  |
| 004 | 2 | time | HG-E110 2026-01-19 | group_therapy | label: actual; position: table; start: 10:00; what: patient_arrival | 14 | "Patient arrival: 10:00" |  |
| 005 | 2 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 14 | "Patient departure: 11:30" |  |
| 006 | 2 | attendance | HG-E110 2026-01-19 | group_therapy | status: attended; status_as_written: Attended | 14 | "Status: Attended" |  |
| 007 | 2 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 14 | "Patient arrival: 10:00 \| Patient departure: 11:30 \| Status: Attended" |  |
| 008 | 2 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: attended opening check-in, accepted exercise handout, requested additional help from individual clinician; topic: functioning | 18 | "Rowan attended the opening check-in, accepted the exercise handout, and requested additional help from the individual clinician." |  |
| 009 | 2 | statement |  |  | says: is_copy_or_resend | 20 | "This is a retransmission of the January 19 roster for HG-E110." |  |
| 010 | 2 | statement |  |  | says: no_new_signature | 20 | "The received copy contains no new clinician signature" |  |

Coverage: 18 times, dates and record numbers in the document. 17 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 20 | number | HG-E110 | captured on another line |

### BH-D105: BH-D105_individual_2026-01-19.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | clinical_note | Individual psychotherapy | signed by Mira Patel, LCSW, 2026-01-19 12:32 |  |  | service 2026-01-19; signed 2026-01-19 12:32 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E111 2026-01-19 | individual_therapy |  | 3 | "Individual psychotherapy \| Encounter HG-E111" |  |
| 002 | 1 | modality | HG-E111 2026-01-19 | individual_therapy | modality: in_person | 5 | "In person" |  |
| 003 | 1 | time | HG-E111 2026-01-19 | individual_therapy | end: 11:45; label: not_labelled; position: header; start: 11:15; what: patient_present | 6 | "Patient contact: 11:15–11:45" |  |
| 004 | 1 | participant | HG-E111 2026-01-19 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 11 | "Rowan participated throughout the individual contact" |  |
| 005 | 1 | participant | HG-E111 2026-01-19 | individual_therapy | name: Mira Patel; presence: not_stated; role: clinician; role_as_written: LCSW | 7 | "Clinician: Mira Patel, LCSW" |  |
| 006 | 1 | stated_minutes | HG-E111 2026-01-19 | individual_therapy | minutes: 30; of: contact_total | 6 | "Completed: 30 minutes" |  |
| 007 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Patient became anxious during group and needed individual grounding and review of coping strategies; topic: reason_for_contact | 9 | "Rowan became anxious during group and needed individual grounding and review of coping strategies." |  |
| 008 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: patient; summary: Patient described feeling overwhelmed by workplace demands and worried about returning to work; topic: anxiety | 9 | "The patient described feeling overwhelmed when other members discussed workplace demands and worried that returning to work would expose difficulties keeping up." |  |
| 009 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Patient identified muscle tension, rapid breathing, and urge to leave as early signs of activation; topic: anxiety | 9 | "Rowan was able to identify muscle tension, rapid breathing, and an urge to leave as early signs of activation." |  |
| 010 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: patient; summary: Intensity of anxiety eased enough to discuss next step; topic: anxiety | 11 | "reported that the immediate intensity of anxiety eased enough to discuss a next step." |  |
| 011 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Narrowed work-related task to drafting two sentences to a supervisor; topic: functioning | 11 | "We narrowed the work-related task to drafting two sentences to a supervisor, without requiring that the message be sent today." |  |
| 012 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Discussed allowing an incomplete draft to exist rather than abandoning the task due to perfectionism; topic: functioning | 11 | "Discussed allowing an incomplete draft to exist rather than abandoning the task because the wording felt imperfect." |  |
| 013 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: patient; summary: Patient denied current suicidal thoughts and remained future oriented; topic: safety | 13 | "Rowan denied current suicidal thoughts and remained future oriented in discussing the next appointment." |  |
| 014 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: No acute safety concern identified; topic: safety | 13 | "No acute safety concern was identified during this contact." |  |
| 015 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Disrupted sleep continues to interfere with resuming usual work routine; topic: sleep | 13 | "Persistent avoidance and disrupted sleep continue to interfere with resuming a usual work routine." |  |
| 016 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Persistent avoidance and disrupted sleep interfere with resuming usual work routine; topic: functioning | 13 | "Persistent avoidance and disrupted sleep continue to interfere with resuming a usual work routine." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D106: BH-D106_telehealth_2026-01-21.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-13 | clinical_note |  | signed by Mira Patel, LCSW, 2026-01-21 15:04 |  |  | service 2026-01-21; signed 2026-01-21 15:04 |
| 2 | 15-20 | platform_export |  | not_stated |  |  | exported_or_prepared 2026-01-21 14:06 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E112 HG-A112 2026-01-21 | individual_therapy |  | 3 | "Individual psychotherapy \| Encounter HG-E112 \| Appointment HG-A112" |  |
| 002 | 1 | modality | HG-E112 HG-A112 2026-01-21 | individual_therapy | modality: video | 5 | "Video" |  |
| 003 | 1 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | end: 13:20; label: actual; position: body; start: 13:00; what: patient_present | 7 | "Patient contact occurred 13:00–13:20 and 13:30–13:55" |  |
| 004 | 1 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | detail: Connection was lost; end: 13:30; label: actual; position: body; start: 13:20; what: no_therapy_interval | 7 | "Connection was lost from 13:20–13:30" |  |
| 005 | 1 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | end: 13:55; label: actual; position: body; start: 13:30; what: patient_present | 7 | "Patient contact occurred 13:00–13:20 and 13:30–13:55" |  |
| 006 | 2 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | end: 13:20; label: not_labelled; position: table; start: 13:00; what: connection | 17 | "January 21 13:00 \| January 21 13:20" |  |
| 007 | 2 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | end: 13:55; label: not_labelled; position: table; start: 13:30; what: connection | 18 | "January 21 13:30 \| January 21 13:55" |  |
| 008 | 1 | attendance | HG-E112 HG-A112 2026-01-21 | individual_therapy | status: attended; status_as_written: Patient contact occurred 13:00–13:20 and 13:30–13:55 | 7 | "Patient contact occurred 13:00–13:20 and 13:30–13:55" |  |
| 009 | 1 | participant | HG-E112 HG-A112 2026-01-21 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 7 | "Patient contact occurred 13:00–13:20 and 13:30–13:55" |  |
| 010 | 1 | participant | HG-E112 HG-A112 2026-01-21 | individual_therapy | name: Mira Patel; presence: present; role: clinician; role_as_written: Clinician: Mira Patel, LCSW | 5 | "Clinician: Mira Patel, LCSW" |  |
| 011 | 1 | stated_minutes | HG-E112 HG-A112 2026-01-21 | individual_therapy | minutes: 45; of: patient_present | 7 | "Total patient psychotherapy contact: 45 minutes" |  |
| 012 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: patient; summary: Drafted a message about possible gradual return to work and stopped before sending it; topic: functioning | 9 | "Rowan reported drafting a short message about a possible gradual return to work but stopping before sending it" |  |
| 013 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: patient; summary: Identified checking draft repeatedly as way the task was being delayed; topic: functioning | 9 | "The patient identified checking the draft repeatedly as another way the task was being delayed" |  |
| 014 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: patient; summary: One night of improved sleep followed by prolonged wakefulness; topic: sleep | 11 | "Rowan described one night of improved sleep followed by a night of prolonged wakefulness" |  |
| 015 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: clinician; summary: Engaged and able to restate the agreed task; topic: functioning | 11 | "Rowan was engaged and able to restate the agreed task" |  |
| 016 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: clinician; summary: No urgent safety concern reported; topic: safety | 11 | "No urgent safety concern was reported" |  |
| 017 | 1 | statement | HG-E112 HG-A112 2026-01-21 | individual_therapy | says: same_contact_continued | 7 | "The reconnection continued the same clinical encounter under original appointment HG-A112" |  |
| 018 | 2 | statement | HG-E112 HG-A112 2026-01-21 | individual_therapy | says: same_contact_continued | 19 | "Second call reason: Rejoin original appointment after network disconnect" |  |

Coverage: 29 times, dates and record numbers in the document. 20 captured, 7 captured on another line, 2 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-A112 | captured on another line |
| 17 | date | January 21 | captured on another line |
| 17 | date | January 21 | captured on another line |
| 17 | number | HG-A112 | captured on another line |
| 17 | number | VC-112A | not captured |
| 18 | date | January 21 | captured on another line |
| 18 | date | January 21 | captured on another line |
| 18 | number | HG-A112 | captured on another line |
| 18 | number | VC-112B | not captured |

### BH-D107: BH-D107_group_activity_records_2026-01-22_and_29.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-10 | clinical_note | Skills group activity record extract | signed by Leah Chen, LCSW, 2026-01-22 12:06 |  |  | signed 2026-01-22 12:06; service 2026-01-22 |
| 2 | 12-18 | clinical_note | Skills group activity record extract | signed by Leah Chen, LCSW, 2026-01-29 12:11 |  |  | signed 2026-01-29 12:11; service 2026-01-29 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E113 2026-01-22 | group_therapy |  | 7 | "Encounter HG-E113" |  |
| 002 | 2 | contact | HG-E118 2026-01-29 | group_therapy |  | 12 | "Encounter HG-E118" |  |
| 003 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 8 | "Scheduled group 10:00–11:30" |  |
| 004 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:00; label: not_labelled; position: header; start: 10:45; what: no_therapy_interval | 8 | "Nontherapeutic break 10:45–11:00" |  |
| 005 | 2 | time | HG-E118 2026-01-29 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 13 | "Scheduled group 10:00–11:30" |  |
| 006 | 2 | time | HG-E118 2026-01-29 | group_therapy | end: 11:00; label: not_labelled; position: header; start: 10:45; what: no_therapy_interval | 13 | "Nontherapeutic break 10:45–11:00" |  |
| 007 | 1 | attendance | HG-E113 2026-01-22 | group_therapy | status: attended_part; status_as_written: Rowan joined the discussion after it had begun | 9 | "Rowan joined the discussion after it had begun" |  |
| 008 | 2 | attendance | HG-E118 2026-01-29 | group_therapy | status: attended; status_as_written: Rowan reported opening the work calendar but delaying a follow-up conversation | 14 | "Rowan reported opening the work calendar but delaying a follow-up conversation" |  |
| 009 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Rowan Mercer; presence: present_part; role: patient | 9 | "Rowan joined the discussion after it had begun" |  |
| 010 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Leah Chen; presence: present; role: clinician; role_as_written: Facilitator | 9 | "Facilitator encouraged a limited, planned review period and a stopping point" |  |
| 011 | 2 | participant | HG-E118 2026-01-29 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 14 | "Rowan participated in the paired rehearsal and accepted feedback about keeping the request brief" | verified_line_corrected |
| 012 | 2 | participant | HG-E118 2026-01-29 | group_therapy | name: Leah Chen; presence: present; role: clinician; role_as_written: Facilitator | 14 | "The facilitator helped identify a specific question to ask" |  |
| 013 | 1 | observation | HG-E113 2026-01-22 | group_therapy | date: 2026-01-22; speaker: patient; summary: Used opening a work calendar as an example; topic: functioning | 9 | "Rowan used opening a work calendar as an example" |  |
| 014 | 1 | observation | HG-E113 2026-01-22 | group_therapy | date: 2026-01-22; speaker: patient; summary: Concern that seeing outstanding items would become overwhelming; topic: anxiety | 9 | "described concern that seeing outstanding items would become overwhelming" |  |
| 015 | 1 | observation | HG-E113 2026-01-22 | group_therapy | date: 2026-01-22; speaker: clinician; summary: Contributed an example to discussion after break; topic: functioning | 9 | "The patient contributed an example to the discussion after the break" | verified_line_corrected |
| 016 | 2 | observation | HG-E118 2026-01-29 | group_therapy | date: 2026-01-29; speaker: patient; summary: Opened work calendar but delayed follow-up conversation; topic: functioning | 14 | "Rowan reported opening the work calendar but delaying a follow-up conversation" |  |
| 017 | 2 | observation | HG-E118 2026-01-29 | group_therapy | date: 2026-01-29; speaker: clinician; summary: Participated in paired rehearsal and accepted feedback about keeping request brief; topic: functioning | 14 | "Rowan participated in the paired rehearsal and accepted feedback about keeping the request brief" | verified_line_corrected |
| 018 | 2 | statement |  |  | says: not_an_attendance_record | 17 | "Patient arrival, departure, and attendance status are entered in the separate attendance register" |  |

Coverage: 19 times, dates and record numbers in the document. 19 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D108: BH-D108_final_attendance_and_cancellation_register.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-23 | schedule_export | Outpatient attendance and appointment disposition extract | not_stated | Final |  | exported_or_prepared 2026-01-30 17:10 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E113 2026-01-22 | group_therapy |  | 9 | "January 22 \| HG-E113 \| Skills group" |  |
| 002 | 1 | contact | HG-E116 2026-01-27 | group_therapy |  | 10 | "January 27 \| HG-E116 \| Skills group" |  |
| 003 | 1 | contact | HG-E117 2026-01-28 | individual_therapy |  | 11 | "January 28 \| HG-E117 \| Individual" |  |
| 004 | 1 | contact | HG-E118 2026-01-29 | group_therapy |  | 12 | "January 29 \| HG-E118 \| Skills group" |  |
| 005 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 9 | "10:00–11:30" |  |
| 006 | 1 | time | HG-E113 2026-01-22 | group_therapy | label: actual; position: table; start: 10:30; what: patient_arrival | 9 | "10:30" |  |
| 007 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 9 | "11:30" |  |
| 008 | 1 | time | HG-E113 2026-01-22 | group_therapy | label: actual; position: body; start: 10:30; what: patient_arrival | 14 | "Rowan arrived at 10:30 and remained until the group closed" |  |
| 009 | 1 | time | HG-E116 2026-01-27 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 10 | "10:00–11:30" |  |
| 010 | 1 | time | HG-E117 2026-01-28 | individual_therapy | end: 14:45; label: scheduled; position: table; start: 14:00; what: contact_interval | 11 | "14:00–14:45" |  |
| 011 | 1 | time | HG-E118 2026-01-29 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 12 | "10:00–11:30" |  |
| 012 | 1 | time | HG-E118 2026-01-29 | group_therapy | label: actual; position: table; start: 10:00; what: patient_arrival | 12 | "10:00" |  |
| 013 | 1 | time | HG-E118 2026-01-29 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 12 | "11:30" |  |
| 014 | 1 | attendance | HG-E113 2026-01-22 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-22; entry_signed_time: 12:09; status: attended_part; status_as_written: Attended, late arrival | 9 | "Attended, late arrival" |  |
| 015 | 1 | attendance | HG-E116 2026-01-27 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-27; entry_signed_time: 11:54; status: no_show; status_as_written: No show; patient did not attend | 10 | "No show; patient did not attend" |  |
| 016 | 1 | attendance | HG-E117 2026-01-28 | individual_therapy | entry_entered_by: Ana Reed; entry_entered_date: 2026-01-28; entry_entered_time: 08:18; reason: personal scheduling conflict; status: cancelled_by_patient; status_as_written: Patient cancelled before appointment | 11 | "Patient cancelled before appointment" |  |
| 017 | 1 | attendance | HG-E118 2026-01-29 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-29; entry_signed_time: 12:15; status: attended; status_as_written: Attended | 12 | "Attended" |  |
| 018 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Rowan; presence: present_part; role: patient | 9 | "Attended, late arrival" |  |
| 019 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Leah Chen; presence: not_stated; role: clinician; role_as_written: LCSW | 14 | "Signed: Leah Chen, LCSW" |  |
| 020 | 1 | participant | HG-E116 2026-01-27 | group_therapy | name: Rowan; presence: absent; role: patient | 16 | "Rowan was absent for the entire group" |  |
| 021 | 1 | participant | HG-E116 2026-01-27 | group_therapy | name: Leah Chen; presence: not_stated; role: clinician; role_as_written: LCSW | 16 | "Signed: Leah Chen, LCSW" |  |
| 022 | 1 | participant | HG-E117 2026-01-28 | individual_therapy | name: Rowan; presence: not_stated; role: patient | 11 | "Patient cancelled before appointment" |  |
| 023 | 1 | participant | HG-E118 2026-01-29 | group_therapy | name: Rowan; presence: present; role: patient | 20 | "Rowan was present from opening through closing" |  |
| 024 | 1 | participant | HG-E118 2026-01-29 | group_therapy | name: Leah Chen; presence: not_stated; role: clinician; role_as_written: LCSW | 20 | "Signed: Leah Chen, LCSW" |  |
| 025 | 1 | statement | HG-E116 2026-01-27 | group_therapy | says: no_patient_contact | 16 | "No patient treatment contact occurred" |  |

Coverage: 41 times, dates and record numbers in the document. 26 captured, 14 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 14 | date | January 22 | captured on another line |
| 14 | date | January 22 | captured on another line |
| 14 | time | 12:09 | captured on another line |
| 16 | date | January 27 | captured on another line |
| 16 | date | January 27 | captured on another line |
| 16 | time | 11:54 | captured on another line |
| 18 | date | January 28 | captured on another line |
| 18 | date | January 28 | captured on another line |
| 18 | date | January 28 | captured on another line |
| 18 | time | 08:12 | not captured |
| 18 | time | 08:18 | captured on another line |
| 18 | number | HG-E117 | captured on another line |
| 20 | date | January 29 | captured on another line |
| 20 | date | January 29 | captured on another line |
| 20 | time | 12:15 | captured on another line |

### BH-D109: BH-D109_care_coordination_2026-01-23.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | clinical_note | Care coordination | signed by Mira Patel, LCSW, 2026-01-23 10:02 |  |  | service 2026-01-23; signed 2026-01-23 10:02 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E114 2026-01-23 | care_coordination |  | 3 | "Encounter HG-E114" |  |
| 002 | 1 | modality | HG-E114 2026-01-23 | care_coordination | modality: telephone | 9 | "during this call" |  |
| 003 | 1 | time | HG-E114 2026-01-23 | care_coordination | end: 09:20; label: not_labelled; position: header; start: 09:00; what: contact_interval | 5 | "January 23, 2026 \| 09:00–09:20" |  |
| 004 | 1 | attendance | HG-E114 2026-01-23 | care_coordination | status: absent; status_as_written: None. No patient contact occurred. | 7 | "Patient participation: None. No patient contact occurred." |  |
| 005 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Mira Patel; presence: present; role: clinician; role_as_written: LCSW | 6 | "Mira Patel, LCSW" |  |
| 006 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Daniel Shaw; presence: present; role: outside_professional; role_as_written: outside social worker | 6 | "Daniel Shaw, outside social worker" |  |
| 007 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Rowan Mercer; presence: absent; role: patient | 7 | "Patient participation: None" |  |
| 008 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: outside_professional; speaker_name: Daniel Shaw; summary: Patient needed help understanding whom to contact about gradual return to work; topic: reason_for_contact | 9 | "Rowan had asked for help understanding whom to contact about a gradual return schedule" |  |
| 009 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: clinician; summary: Patient's current approach involves breaking difficult tasks into manageable steps; topic: functioning | 11 | "Reviewed the current approach of helping Rowan break a difficult task into a manageable first step" |  |
| 010 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: clinician; summary: Patient has avoidance issues to be addressed in scheduled therapy; topic: functioning | 11 | "I will continue to address avoidance and coping within scheduled therapy" |  |
| 011 | 1 | statement | HG-E114 2026-01-23 | care_coordination | says: no_patient_contact | 7 | "No patient contact occurred." |  |
| 012 | 1 | statement | HG-E114 2026-01-23 | care_coordination | says: no_therapy_provided | 13 | "no psychotherapy was delivered to the patient during the call" |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D110: BH-D110_individual_primary_record_2026-01-26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | clinical_note |  | signed by Mira Patel, LCSW, 2026-01-26 11:16 | Final |  | service 2026-01-26; signed 2026-01-26 11:16 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E115 HG-A115 2026-01-26 | individual_therapy |  | 3 | "Individual psychotherapy \| Encounter HG-E115 \| Appointment HG-A115" |  |
| 002 | 1 | modality | HG-E115 HG-A115 2026-01-26 | individual_therapy | modality: in_person | 5 | "In person" |  |
| 003 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: body; start: 09:00; what: patient_present | 7 | "Actual patient psychotherapy contact: 09:00–09:50, 50 minutes." |  |
| 004 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 7 | "Actual patient psychotherapy contact: 09:00–09:50" |  |
| 005 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Mira Patel; presence: not_stated; role: clinician; role_as_written: LCSW | 6 | "Mira Patel, LCSW" |  |
| 006 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Nora Ellis; presence: present; role: clinician; role_as_written: LCSW | 11 | "Nora Ellis participated directly in the clinical work" |  |
| 007 | 1 | stated_minutes | HG-E115 HG-A115 2026-01-26 | individual_therapy | minutes: 50; of: patient_present | 7 | "Actual patient psychotherapy contact: 09:00–09:50, 50 minutes." |  |
| 008 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: patient worried about being asked for commitments they might not be able to meet; topic: anxiety | 9 | "brought up worry about being asked for commitments the patient might not be able to meet" |  |
| 009 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: patient continued to postpone choosing time for conversation; topic: functioning | 9 | "Rowan continued to postpone choosing a time for the conversation" |  |
| 010 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: sleep uneven with difficulty settling when work-related thoughts repetitive; topic: sleep | 9 | "Sleep remained uneven, with difficulty settling on nights when work-related thoughts became repetitive" |  |
| 011 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: patient able to return to main request with prompting; topic: functioning | 11 | "Rowan was able to return to the main request with prompting" |  |
| 012 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: patient remained attentive and collaborative; topic: functioning | 13 | "The patient remained attentive and collaborative" |  |
| 013 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: patient hesitant about completing task outside office; topic: functioning | 13 | "although hesitant about completing the task outside the office" |  |
| 014 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: no current suicidal ideation; topic: safety | 13 | "No current suicidal ideation was reported" |  |

Coverage: 10 times, dates and record numbers in the document. 10 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D111: BH-D111_individual_second_record_2026-01-26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | clinical_note | Participating clinician psychotherapy record | signed by Nora Ellis, LCSW, 2026-01-26 12:03 | Final |  | service 2026-01-26; signed 2026-01-26 12:03 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E115 HG-A115 2026-01-26 | individual_therapy |  | 4 | "Encounter HG-E115 \| Appointment HG-A115 \| Service date January 26, 2026" |  |
| 002 | 1 | modality | HG-E115 HG-A115 2026-01-26 | individual_therapy | modality: in_person | 6 | "Service: Individual psychotherapy, in person" |  |
| 003 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: header; start: 09:10; what: contact_interval | 7 | "Actual patient psychotherapy contact: 09:10–09:50, 40 minutes." |  |
| 004 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | label: actual; position: body; start: 09:10; what: patient_arrival | 10 | "Rowan entered the treatment room at 09:10" |  |
| 005 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: body; what: patient_departure | 14 | "The session concluded with Rowan at 09:50" |  |
| 006 | 1 | attendance | HG-E115 HG-A115 2026-01-26 | individual_therapy | status: attended; status_as_written: Rowan entered the treatment room at 09:10 | 10 | "Rowan entered the treatment room at 09:10" |  |
| 007 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Rowan; presence: present; role: patient | 10 | "Rowan entered the treatment room at 09:10" |  |
| 008 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Nora Ellis; presence: present; role: clinician; role_as_written: LCSW | 10 | "I participated directly in this individual encounter" |  |
| 009 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Mira Patel; presence: not_stated; role: clinician; role_as_written: LCSW | 8 | "participating with Mira Patel, LCSW" |  |
| 010 | 1 | stated_minutes | HG-E115 HG-A115 2026-01-26 | individual_therapy | minutes: 40; of: patient_present | 7 | "40 minutes" |  |
| 011 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: discussed difficulty moving from a supervisor's reply to arranging the next conversation; topic: functioning | 10 | "Rowan discussed difficulty moving from a supervisor's reply to arranging the next conversation" |  |
| 012 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: anticipated becoming overwhelmed if several work issues were raised at once; topic: anxiety | 10 | "The patient anticipated becoming overwhelmed if several work issues were raised at once" |  |
| 013 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: recognized a tendency to keep editing a message after the essential point was already clear; topic: functioning | 12 | "Rowan recognized a tendency to keep editing a message after the essential point was already clear" |  |
| 014 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: could use the cue during the rehearsal but remained uncertain about using it independently when anxious; topic: functioning | 12 | "The patient could use the cue during the rehearsal but remained uncertain about using it independently when anxious" |  |
| 015 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: repetitive planning at night affected settling for sleep; topic: sleep | 12 | "The discussion also addressed how repetitive planning at night affected settling for sleep" |  |
| 016 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: ongoing anxiety; topic: anxiety | 14 | "Clinical presentation remained consistent with ongoing anxiety, low mood, and functional difficulty around work demands" |  |
| 017 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: low mood; topic: mood | 14 | "Clinical presentation remained consistent with ongoing anxiety, low mood, and functional difficulty around work demands" |  |
| 018 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: functional difficulty around work demands; topic: functioning | 14 | "Clinical presentation remained consistent with ongoing anxiety, low mood, and functional difficulty around work demands" |  |
| 019 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: was engaged with the treatment team; topic: functioning | 14 | "Rowan was engaged with the treatment team" |  |
| 020 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: described a wish to resume a steadier routine; topic: functioning | 14 | "described a wish to resume a steadier routine" |  |
| 021 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: plan to continue individual and group work under existing outpatient plan; topic: progress | 14 | "Plan is to continue individual and group work under the existing outpatient plan" |  |

Coverage: 14 times, dates and record numbers in the document. 13 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 10 | time | 09:50 | captured on another line |

### BH-D112: BH-D112_draft_note_and_charge_extract_2026-01-27.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 7-16 | draft_note | AUTOGENERATED PROGRESS NOTE | unsigned | DRAFT — UNSIGNED — system populated from scheduled group template |  | service 2026-01-27; created 2026-01-27 09:45 |
| 2 | 18-27 | billing_extract | POSTED CHARGE EXTRACT | not_stated |  |  | service 2026-01-27; posted 2026-01-27 18:06; exported_or_prepared 2026-01-30 17:25 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E116 2026-01-27 | group_therapy |  | 10 | "Skills group" |  |
| 002 | 1 | time | HG-E116 2026-01-27 | group_therapy | end: 11:30; label: scheduled; position: body; start: 10:00; what: contact_interval | 10 | "Skills group, 10:00–11:30" |  |
| 003 | 1 | attendance | HG-E116 2026-01-27 | group_therapy | status: attended; status_as_written: Patient attended the full session and participated in the skills discussion. | 11 | "Patient attended the full session and participated in the skills discussion." |  |
| 004 | 1 | participant | HG-E116 2026-01-27 | group_therapy | presence: present; role: patient | 11 | "Patient attended the full session and participated in the skills discussion." |  |
| 005 | 2 | charge | HG-E116 2026-01-27 | group_therapy | charge_id: CH-116; description: Group psychotherapy; posted_date: 2026-01-27; posted_time: 18:06; quantity: 1; status_as_written: Posted; unit_as_written: group session | 21 | "Group psychotherapy" |  |
| 006 | 1 | statement |  |  | says: made_before_the_service | 16 | "It was generated from the appointment template before the scheduled group." |  |
| 007 | 1 | statement |  |  | says: is_draft_or_unsigned | 9 | "Status: DRAFT — UNSIGNED — system populated from scheduled group template" |  |

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
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Family psychotherapy | signed by Mira Patel, LCSW, 2026-01-30 14:18 |  |  | service 2026-01-30; signed 2026-01-30 14:18 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E119 2026-01-30 | family_therapy |  | 3 | "Family psychotherapy \| Encounter HG-E119" |  |
| 002 | 1 | modality | HG-E119 2026-01-30 | family_therapy | modality: in_person | 5 | "In person" |  |
| 003 | 1 | time | HG-E119 2026-01-30 | family_therapy | end: 13:45; label: actual; position: header; start: 13:00; what: contact_interval | 6 | "Therapist session interval: 13:00–13:45, 45 minutes." |  |
| 004 | 1 | time | HG-E119 2026-01-30 | family_therapy | detail: Partner only; end: 13:15; label: actual; position: header; start: 13:00; what: patient_absent_interval | 7 | "Partner only: 13:00–13:15." |  |
| 005 | 1 | time | HG-E119 2026-01-30 | family_therapy | detail: with partner; end: 13:45; label: actual; position: header; start: 13:15; what: patient_present | 7 | "Rowan present with partner: 13:15–13:45, 30 minutes." |  |
| 006 | 1 | attendance | HG-E119 2026-01-30 | family_therapy | status: attended_part; status_as_written: Rowan joined at 13:15 and participated through the end of the session | 9 | "Rowan was not present for that portion" |  |
| 007 | 1 | participant | HG-E119 2026-01-30 | family_therapy | name: Rowan Mercer; presence: present_part; role: patient | 11 | "Rowan joined at 13:15 and participated through the end of the session" |  |
| 008 | 1 | participant | HG-E119 2026-01-30 | family_therapy | name: Casey Mercer; presence: present; role: family_or_partner | 9 | "Casey Mercer, arrived first" |  |
| 009 | 1 | participant | HG-E119 2026-01-30 | family_therapy | name: Mira Patel, LCSW; presence: not_stated; role: clinician | 5 | "Clinician: Mira Patel, LCSW" |  |
| 010 | 1 | stated_minutes | HG-E119 2026-01-30 | family_therapy | minutes: 45; of: contact_total | 6 | "Therapist session interval: 13:00–13:45, 45 minutes." |  |
| 011 | 1 | stated_minutes | HG-E119 2026-01-30 | family_therapy | minutes: 30; of: patient_present | 7 | "Rowan present with partner: 13:15–13:45, 30 minutes." |  |
| 012 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Described uncertainty about when reminders helped versus when they increased patient's sense of pressure; topic: anxiety | 9 | "Casey described uncertainty about when reminders helped and when they seemed to increase Rowan's sense of pressure." |  |
| 013 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: A reminder about work led to lengthy discussion followed by patient withdrawing from the task; topic: functioning | 11 | "a reminder about contacting work led to a lengthy discussion, followed by Rowan withdrawing from the task." |  |
| 014 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Patient practiced requesting specific kind of help and naming when reminder felt overwhelming; topic: functioning | 11 | "Rowan practiced requesting a specific kind of help and naming when a reminder felt overwhelming." |  |
| 015 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Both participants agreed to try one brief check-in at planned time rather than repeated questions; topic: functioning | 13 | "Both participants agreed to try one brief check-in at a planned time rather than repeated questions across the evening." |  |
| 016 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Patient remained anxious about work conversation; topic: anxiety | 13 | "Rowan remained anxious about the work conversation" |  |
| 017 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Patient could explain the intended first step; topic: functioning | 13 | "could explain the intended first step." |  |
| 018 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: patient; summary: Patient reported that having a limited plan felt more manageable; topic: functioning | 13 | "The patient reported that having a limited plan felt more manageable." |  |

Coverage: 14 times, dates and record numbers in the document. 13 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 11 | time | 13:15 | captured on another line |

### BH-D114: BH-D114_medication_management_2026-01-30.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Medication management | signed by Elena Ortiz, PMHNP, 2026-01-30 16:02 | Final |  | service 2026-01-30; signed 2026-01-30 16:02 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E120 2026-01-30 | medication_management |  | 3 | "Medication management \| Encounter HG-E120" |  |
| 002 | 1 | time | HG-E120 2026-01-30 | medication_management | end: 15:20; label: scheduled; position: header; start: 15:00; what: contact_interval | 5 | "15:00–15:20" |  |
| 003 | 1 | attendance | HG-E120 2026-01-30 | medication_management | status: completed; status_as_written: Completed, 20 minutes | 5 | "Completed, 20 minutes" |  |
| 004 | 1 | participant | HG-E120 2026-01-30 | medication_management | name: Rowan Mercer; presence: present; role: patient | 8 | "Rowan reported taking the medication as prescribed" |  |
| 005 | 1 | participant | HG-E120 2026-01-30 | medication_management | name: Elena Ortiz; presence: not_stated; role: clinician; role_as_written: Prescriber | 6 | "Prescriber: Elena Ortiz, PMHNP" |  |
| 006 | 1 | stated_minutes | HG-E120 2026-01-30 | medication_management | minutes: 20; of: contact_total | 5 | "20 minutes" |  |
| 007 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: patient; summary: Taking medication as prescribed; topic: medication | 8 | "Rowan reported taking the medication as prescribed" |  |
| 008 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: patient; summary: Did not describe new adverse effects; topic: medication | 8 | "did not describe a new adverse effect" |  |
| 009 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Mood less persistently low than earlier in month; topic: mood | 8 | "Mood felt less persistently low than earlier in the month" |  |
| 010 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Anxiety remains noticeable when anticipating work contact; topic: anxiety | 8 | "anxiety remained noticeable when anticipating contact with work" |  |
| 011 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Sleep still variable; topic: sleep | 8 | "Sleep was still variable" |  |
| 012 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Alert and organized in conversation; topic: functioning | 10 | "Rowan was alert, organized in conversation" |  |
| 013 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Able to describe the follow-up plan; topic: functioning | 10 | "able to describe the follow-up plan" |  |
| 014 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: patient; summary: Denied current suicidal thoughts; topic: safety | 10 | "The patient denied current suicidal thoughts" |  |
| 015 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: No new acute safety issues; topic: safety | 10 | "No new acute safety issue emerged in this visit" |  |
| 016 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: patient; summary: Agreed to continue outpatient follow-up and bring medication questions; topic: functioning | 12 | "Rowan agreed to continue attending scheduled outpatient follow-up and to bring questions about the medication regimen to the next medication appointment" |  |
| 017 | 1 | statement | HG-E120 2026-01-30 | medication_management | says: no_therapy_provided | 12 | "No separately documented psychotherapy was provided" |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D115: BH-D115_symptom_measure_review_2026-01-30.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by haiku, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | questionnaire_review | Symptom questionnaire and chart review | signed by Mira Patel, LCSW, 2026-01-30 16:20 |  |  | completed 2026-01-30 12:42; signed 2026-01-30 16:20 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | 2026-01-30 |  |  | 8 | "the afternoon appointment" |  |
| 002 | 1 | score |  |  | completed_date: 2026-01-30; completed_time: 12:42; instrument: PHQ-9; relation: completion; score: 10 | 6 | "PHQ-9 total: 10." |  |
| 003 | 1 | score |  |  | completed_date: 2026-01-30; completed_time: 12:42; instrument: PHQ-9; item_number: 9; relation: completion; score: 0 | 6 | "Item 9: 0." |  |
| 004 | 1 | observation |  |  | date: 2026-01-30; speaker: patient; summary: continued to endorse sleep difficulty; topic: sleep | 8 | "The patient continued to endorse sleep difficulty" |  |
| 005 | 1 | observation |  |  | date: 2026-01-30; speaker: patient; summary: trouble sustaining usual activities; topic: functioning | 8 | "trouble sustaining usual activities" |  |
| 006 | 1 | observation |  |  | date: 2026-01-30; speaker: patient; summary: fewer days of pervasive low mood than at intake; topic: mood | 8 | "fewer days of pervasive low mood than reported at intake" |  |
| 007 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: shows partial improvement; topic: progress | 10 | "Rowan shows partial improvement" |  |
| 008 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: persistent avoidance; topic: functioning | 10 | "persistent avoidance" |  |
| 009 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: meaningful functional impact around returning to work; topic: functioning | 10 | "meaningful functional impact around returning to work" |  |
| 010 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: has taken some initial steps including drafting and sending a message; topic: functioning | 10 | "The patient has taken some initial steps, including drafting and sending a message" |  |
| 011 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: continues to delay follow-up; topic: functioning | 10 | "continues to delay follow-up" |  |
| 012 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: becomes anxious when task expands beyond narrowly defined action; topic: anxiety | 10 | "becomes anxious when a task expands beyond a narrowly defined action" |  |
| 013 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: sleep disruption remains intermittent barrier to establishing steadier daytime routine; topic: sleep | 10 | "Sleep disruption remains an intermittent barrier to establishing a steadier daytime routine" |  |
| 014 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: continued treatment is appropriate; topic: progress | 12 | "Continued treatment is appropriate" |  |
| 015 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: remaining difficulties with follow-through and work-related functioning; topic: functioning | 12 | "remaining difficulties with follow-through and work-related functioning" |  |
| 016 | 1 | statement |  |  | says: not_a_visit | 14 | "is not a separate treatment appointment" |  |

Coverage: 8 times, dates and record numbers in the document. 8 captured, 0 captured on another line, 0 not captured, 0 quoted only.

