# The saved abstraction

Written by the `export` command from `abstraction.sqlite`. No model is called to write it.

## Documents

| ID | File | Kinds | Patient | Read | Claims | Hash |
|---|---|---|---|---|---|---|
| BH-D001 | group_authorization_letter.txt | authorization, other | HG-M042 | read | 10 | d2240979a2de |
| BH-D002 | intake_and_individual_jan05.txt | clinical_note | HG-M042 | read | 29 | 7f5f7d4bbfc9 |
| BH-D003 | signed_treatment_plan_jan05.txt | plan | HG-M042 | read | 21 | 3b3f50db40b3 |
| BH-D004 | group_facilitator_jan06.txt | clinical_note | HG-M042 | read | 12 | 5edddc6b2093 |
| BH-D005 | early_group_attendance_roster.txt | attendance_record | HG-M042 | read | 27 | 6f205f89f8d3 |
| BH-D006 | early_appointment_status_export.txt | schedule_export | HG-M042 | read | 36 | 0bf056f3769e |
| BH-D007 | family_primary_jan09.txt | clinical_note | HG-M042 | read | 24 | 924dee06b05c |
| BH-D008 | family_cofacilitator_jan09.txt | clinical_note | HG-M042 | read | 17 | ad416fbda806 |
| BH-D009 | group_facilitator_jan12.txt | clinical_note | HG-M042 | read | 13 | d30d18d0335d |
| BH-D010 | medication_review_jan13.txt | clinical_note | HG-M042 | read | 24 | 95debafd3a72 |
| BH-D011 | individual_therapy_jan14.txt | clinical_note | HG-M042 | read | 24 | 8c2fbaf5bb45 |
| BH-D012 | partner_collateral_jan16.txt | clinical_note | HG-M042 | read | 25 | 432c973d1a4d |
| BH-D013 | symptom_measure_review_jan16.txt | questionnaire_review | HG-M042 | read | 17 | 300a30dbe42b |
| BH-D014 | imported_measure_summary_received_jan26.txt | import_receipt | HG-M042 | read | 10 | 85e2c780abde |
| BH-D015 | missed_visit_outreach_jan08.txt | scheduling_log | HG-M042 | read | 29 | 4521a120a4d7 |
| BH-D016 | group_cancellation_notice_jan15.txt | cancellation_notice | HG-M042 | read | 23 | 5f3375f11c85 |
| BH-D101 | BH-D101_group_content_2026-01-19.txt | clinical_note | HG-M042 | read | 15 | 05a234a8adc9 |
| BH-D102 | BH-D102_original_attendance_2026-01-19.txt | attendance_record | HG-M042 | read | 16 | 514ca20809f6 |
| BH-D103 | BH-D103_attendance_correction_2026-01-20.txt | correction | HG-M042 | read | 17 | 674440968b5d |
| BH-D104 | BH-D104_resent_roster_received_2026-01-26.txt | cover_sheet, attendance_record | HG-M042 | read | 15 | f3f25065559f |
| BH-D105 | BH-D105_individual_2026-01-19.txt | clinical_note | HG-M042 | read | 21 | 91fd8e8b1b31 |
| BH-D106 | BH-D106_telehealth_2026-01-21.txt | clinical_note, platform_export | HG-M042 | read | 20 | 09c946a2248a |
| BH-D107 | BH-D107_group_activity_records_2026-01-22_and_29.txt | clinical_note, clinical_note | HG-M042 | read | 20 | c5953bcb242e |
| BH-D108 | BH-D108_final_attendance_and_cancellation_register.txt | attendance_record | HG-M042 | read | 34 | 805b2c69c7fa |
| BH-D109 | BH-D109_care_coordination_2026-01-23.txt | clinical_note | HG-M042 | read | 18 | 069ea4112779 |
| BH-D110 | BH-D110_individual_primary_record_2026-01-26.txt | clinical_note | HG-M042 | read | 17 | 4b64c46a13b8 |
| BH-D111 | BH-D111_individual_second_record_2026-01-26.txt | clinical_note | HG-M042 | read | 21 | d03451942797 |
| BH-D112 | BH-D112_draft_note_and_charge_extract_2026-01-27.txt | cover_sheet, draft_note, billing_extract | HG-M042 | read | 14 | b4390ed6b672 |
| BH-D113 | BH-D113_family_therapy_2026-01-30.txt | clinical_note | HG-M042 | read | 21 | 36764827bcb3 |
| BH-D114 | BH-D114_medication_management_2026-01-30.txt | clinical_note | HG-M042 | read | 19 | 9942bd886fcd |
| BH-D115 | BH-D115_symptom_measure_review_2026-01-30.txt | questionnaire_review | HG-M042 | read | 17 | 4a3859fd81fc |

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
| HG-E110 | 2026-01-19 | group therapy | held, in part | 10:00–11:15 | 10:45–11:00 | 60 | yes | BH-D101, BH-D102, BH-D103, BH-D104, BH-D105 | left before the end |
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
| 2026-01-08 | scheduling contact | Outbound call placed to the patient's recorded number | telephone | BH-D015 |
| 2026-01-08 | scheduling contact | callback | telephone | BH-D015 |
| 2026-01-15 | scheduling contact | Portal notice | message | BH-D016 |
| 2026-01-15 | scheduling contact | called the desk | telephone | BH-D016 |
| 2026-01-16 | questionnaire review | Measurement review |  | BH-D013 |
| 2026-01-27 | scheduling contact | outreach message inviting the patient to contact scheduling | message | BH-D108 |
| 2026-01-28 | scheduling contact | Cancellation received from patient |  | BH-D108 |

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
| PHQ-9 | 2026-01-16 08:17 | 14 | HG-Q116 |  | 1 | 0 |
| PHQ-9 | 2026-01-30 12:42 | 10 |  | item 9: 0 | 0 | 0 |

#### Weekly status

| Week | Days | Dates | Minutes | Hours | Verdict | Margin | Depends on | Dates with no document |
|---|---|---|---|---|---|---|---|---|
| 2026-01-05 to 2026-01-11 | 3 | 2026-01-05, 2026-01-06, 2026-01-09 | 140 | 2.33 | not met | 10 minutes short |  |  |
| 2026-01-12 to 2026-01-18 | 2 | 2026-01-12, 2026-01-14 | 120 | 2.00 | not met | 1 day short, 30 minutes short |  | 2026-01-17, 2026-01-18 |
| 2026-01-19 to 2026-01-25 | 3 | 2026-01-19, 2026-01-21, 2026-01-22 | 180 | 3.00 | met | 30 minutes over |  | 2026-01-24, 2026-01-25 |
| 2026-01-26 to 2026-02-01 (partial) | 3 | 2026-01-26, 2026-01-29, 2026-01-30 | 145 or 155 | 2.42 or 2.58 | cannot determine | 5 minutes short or 5 minutes over | HG-M042/HG-E115:start | 2026-01-31, 2026-02-01 |

#### Totals, 2026-01-05 to 2026-01-30

| Measure | Value |
|---|---|
| Sessions | 12 |
| Therapy days | 11 |
| Minutes | 585 or 595 |
| Hours | 9.75 or 9.92 |
| family therapy | 2 sessions, 75 minutes |
| group therapy | 5 sessions, 300 minutes |
| individual therapy | 5 sessions, 210 or 220 minutes |

## What each document says

### BH-D001: group_authorization_letter.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-12 | authorization | Administrative correspondence | not_stated |  |  | received 2026-01-04 15:26; period_start 2026-01-05; period_end 2026-01-30 |
| 2 | 14-15 | other | Administrative entry | not_stated |  |  | entered 2026-01-05 08:05 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 2 | observation |  |  | date: 2026-01-05; speaker: staff; speaker_name: N. Ellis; summary: Patient informed office would send weekly appointment list; topic: other | 15 | "Rowan was informed that the office would send a weekly appointment list." |  |
| 002 | 1 | plan_rule |  |  | end_date: 2026-01-30; rule: episode_period; start_date: 2026-01-05 | 10 | "approved for the period January 5, 2026 through January 30, 2026" |  |
| 003 | 1 | plan_rule |  |  | measure: sessions; minimum: 8; period: episode; rule: requirement; text: Authorized quantity: 8 group sessions | 10 | "Authorized quantity: 8 group sessions." |  |
| 004 | 1 | plan_rule |  |  | rule: other; text: One authorization unit represents one scheduled group session | 10 | "One authorization unit represents one scheduled group session." |  |
| 005 | 1 | plan_rule |  |  | rule: counted_service; service_classes: group_therapy; text: outpatient therapeutic group work | 10 | "The service description is outpatient therapeutic group work supporting the submitted behavioral health treatment plan." |  |
| 006 | 1 | plan_rule |  |  | rule: excluded_service; service_classes: individual_therapy, family_therapy, medication_management | 10 | "This letter does not authorize individual therapy, family therapy, or medication appointments under the group service quantity." |  |
| 007 | 1 | statement |  |  | says: other | 12 | "The approved period permits the practice to arrange group appointments within the indicated dates." |  |
| 008 | 1 | statement |  |  | says: other | 12 | "Changes in appointment dates within the approved period may be made by the scheduling desk." |  |
| 009 | 2 | statement |  |  | says: not_an_attendance_record | 15 | "No service attendance record accompanies this letter." |  |
| 010 | 2 | statement |  |  | says: other | 15 | "Letter attached to the program account." |  |

Coverage: 10 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-A260104-88 | not captured |

### BH-D002: intake_and_individual_jan05.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-20 | clinical_note |  | signed by Mara Voss, 2026-01-05 12:18 | completed |  | service 2026-01-05; signed 2026-01-05 12:18 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E101 2026-01-05 | individual_therapy |  | 6 | "Encounter HG-E101 \| Service date 2026-01-05" |  |
| 002 | 1 | contact |  | family_therapy |  | 19 | "Rowan consented to involving their partner in a family visit focused on practical support." |  |
| 003 | 1 | modality | HG-E101 2026-01-05 | individual_therapy | modality: in_person | 13 | "Rowan arrived independently and participated throughout the appointment." |  |
| 004 | 1 | time | HG-E101 2026-01-05 | individual_therapy | end: 09:50; label: not_labelled; position: header; start: 09:00; what: patient_present | 8 | "Patient-present individual therapy: 09:00–09:50 local; completed, 50 minutes." |  |
| 005 | 1 | attendance | HG-E101 2026-01-05 | individual_therapy | status: completed; status_as_written: completed | 8 | "Patient-present individual therapy: 09:00–09:50 local; completed, 50 minutes." |  |
| 006 | 1 | attendance | HG-E101 2026-01-05 | individual_therapy | status: attended; status_as_written: participated throughout the appointment | 13 | "Rowan arrived independently and participated throughout the appointment." |  |
| 007 | 1 | participant | HG-E101 2026-01-05 | individual_therapy | name: Rowan Mercer; presence: present; role: patient; role_as_written: Patient | 13 | "Rowan arrived independently and participated throughout the appointment." |  |
| 008 | 1 | participant | HG-E101 2026-01-05 | individual_therapy | name: Mara Voss; presence: not_stated; role: clinician; role_as_written: Clinician | 7 | "Clinician: Mara Voss, LCSW" |  |
| 009 | 1 | participant |  | family_therapy | presence: not_stated; role: family_or_partner; role_as_written: partner | 19 | "Rowan consented to involving their partner in a family visit focused on practical support." |  |
| 010 | 1 | stated_minutes | HG-E101 2026-01-05 | individual_therapy | minutes: 50; of: patient_present | 8 | "Patient-present individual therapy: 09:00–09:50 local; completed, 50 minutes." |  |
| 011 | 1 | score |  |  | completed_date: 2026-01-05; instrument: PHQ-9; relation: completion; score: 18 | 15 | "PHQ-9 completed by Rowan on 2026-01-05: total score 18." |  |
| 012 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: patient; summary: several weeks of low mood, reduced interest; topic: mood | 11 | "Rowan describes several weeks of low mood, reduced interest in usual activities, fragmented sleep, and difficulty beginning ordinary tasks." |  |
| 013 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: patient; summary: fragmented sleep; topic: sleep | 11 | "fragmented sleep" |  |
| 014 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: patient; summary: difficulty beginning ordinary tasks; topic: functioning | 11 | "difficulty beginning ordinary tasks" |  |
| 015 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: worry about returning to work; topic: anxiety | 11 | "Worry increases when thinking about returning to work after a recent leave." |  |
| 016 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: postponing emails, avoiding conversations, isolating; topic: functioning | 11 | "Rowan has been postponing email replies, avoiding conversations about the return date, and spending more time alone at home." |  |
| 017 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: wants routine for work transition; topic: functioning | 11 | "They want a routine that makes the work transition feel manageable." |  |
| 018 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: speech clear and organized; topic: other | 13 | "Speech was clear and organized." |  |
| 019 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: affect subdued but responsive; topic: mood | 13 | "Affect was subdued but responsive, especially when discussing their partner's support." |  |
| 020 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: patient; summary: night waking, checking the time; topic: sleep | 13 | "Rowan described waking in the night and then checking the time repeatedly." |  |
| 021 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: fatigue increases avoidance; topic: functioning | 13 | "Daytime fatigue appears to make avoidance more likely." |  |
| 022 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: no immediate safety concern; can identify supports; topic: safety | 13 | "No immediate safety concern was identified in today's assessment; Rowan was able to discuss support contacts and ways to seek additional help if needed." |  |
| 023 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: depressive symptoms with anxiety and avoidance; topic: other | 15 | "Clinical impressions are depressive symptoms with anxiety and behavioral avoidance." |  |
| 024 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: chose to open work inbox five minutes; topic: functioning | 17 | "Rowan selected opening their work inbox for five minutes without requiring an immediate reply." |  |
| 025 | 1 | observation | HG-E101 2026-01-05 | individual_therapy | date: 2026-01-05; speaker: clinician; summary: consented to partner in family visit; topic: functioning | 19 | "Rowan consented to involving their partner in a family visit focused on practical support." |  |
| 026 | 1 | plan_rule |  |  | end_date: 2026-01-30; rule: episode_period; start_date: 2026-01-05 | 11 | "The current outpatient episode is planned for January 5 through January 30, with review as treatment progresses." |  |
| 027 | 1 | plan_rule |  |  | rule: other; text: Treatment goals and weekly schedule to be recorded in a separate plan | 19 | "Treatment goals and the proposed weekly schedule will be recorded in a separate plan." |  |
| 028 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |
| 029 | 1 | statement |  |  | says: other | 19 | "Treatment goals and the proposed weekly schedule will be recorded in a separate plan." |  |

Coverage: 13 times, dates and record numbers in the document. 13 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D003: signed_treatment_plan_jan05.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-21 | plan | Outpatient treatment plan | signed by Mara Voss, 2026-01-05 13:05 |  |  | signed 2026-01-05 13:05; other 2026-01-05 13:12; period_start 2026-01-05; period_end 2026-01-30 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: depressed mood; topic: mood | 10 | "Presenting needs: depressed mood, sleep disruption, anxiety about resuming work responsibilities, and avoidance of tasks and communication." |  |
| 002 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: sleep disruption; topic: sleep | 10 | "Presenting needs: depressed mood, sleep disruption, anxiety about resuming work responsibilities, and avoidance of tasks and communication." |  |
| 003 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: anxiety about resuming work; topic: anxiety | 10 | "Presenting needs: depressed mood, sleep disruption, anxiety about resuming work responsibilities, and avoidance of tasks and communication." |  |
| 004 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: avoidance of tasks and communication; topic: functioning | 10 | "Presenting needs: depressed mood, sleep disruption, anxiety about resuming work responsibilities, and avoidance of tasks and communication." |  |
| 005 | 1 | observation |  |  | date: 2026-01-05; speaker: patient; summary: wishes to improve follow-through despite anxiety; topic: functioning | 10 | "Rowan wishes to improve follow-through without waiting for anxiety to disappear." |  |
| 006 | 1 | observation |  |  | date: 2026-01-05; speaker: clinician; summary: partner support available; reminders may increase tension; topic: other | 10 | "Partner support is available but repeated reminders sometimes increase tension." |  |
| 007 | 1 | plan_rule |  |  | end_date: 2026-01-30; rule: episode_period; start_date: 2026-01-05 | 6 | "Episode dates: 2026-01-05 through 2026-01-30" |  |
| 008 | 1 | plan_rule |  |  | measure: therapy_days; minimum: 3; period: week; rule: requirement | 12 | "at least 3 therapy days and at least 150 minutes of patient-present therapy in each Monday–Sunday week" |  |
| 009 | 1 | plan_rule |  |  | measure: minutes; minimum: 150; patient_must_be_present: True; period: week; rule: requirement | 12 | "at least 3 therapy days and at least 150 minutes of patient-present therapy in each Monday–Sunday week" |  |
| 010 | 1 | plan_rule |  |  | rule: week_definition; week_starts_on: monday | 12 | "in each Monday–Sunday week" |  |
| 011 | 1 | plan_rule |  |  | patient_must_be_present: True; rule: therapy_day_definition; service_classes: individual_therapy, group_therapy, family_therapy | 12 | "A therapy day is a calendar day on which Rowan participates in individual, group, or family psychotherapy." |  |
| 012 | 1 | plan_rule |  |  | patient_must_be_present: True; rule: counted_service; service_classes: individual_therapy, group_therapy, family_therapy | 12 | "Patient-present individual, group, and family therapy contribute to the minute goal." |  |
| 013 | 1 | plan_rule |  |  | rule: excluded_service; service_classes: medication_management, collateral_contact, care_coordination | 12 | "Medication management, contacts with collateral informants only, and care coordination do not contribute." |  |
| 014 | 1 | plan_rule |  |  | rule: other; text: This is the program's individualized treatment-plan goal for Rowan. | 12 | "This is the program's individualized treatment-plan goal for Rowan." |  |
| 015 | 1 | plan_rule |  |  | goal_number: 1; rule: clinical_goal; text: improve daily activity and task initiation | 14 | "Goal 1: improve daily activity and task initiation." |  |
| 016 | 1 | plan_rule |  |  | goal_number: 2; rule: clinical_goal; text: improve coping with anxiety and disrupted sleep | 16 | "Goal 2: improve coping with anxiety and disrupted sleep." |  |
| 017 | 1 | plan_rule |  |  | goal_number: 3; rule: clinical_goal; text: support a workable return to employment | 18 | "Goal 3: support a workable return to employment." |  |
| 018 | 1 | plan_rule |  |  | rule: other; text: Family work counted when Rowan is present | 10 | "The treatment team will combine individual practice, therapeutic group activities, and family work when Rowan is present." |  |
| 019 | 1 | plan_rule |  |  | rule: other; text: Review participation, symptoms, functioning; adjust schedule when indicated | 20 | "Review: assess participation, symptoms, and practical functioning during the episode." |  |
| 020 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |
| 021 | 1 | statement |  |  | says: not_a_visit | 4 | "Harbor Grove Behavioral Health \| Outpatient treatment plan" |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D004: group_facilitator_jan06.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | clinical_note | Coping skills group | signed by Leena Park, LPC, 2026-01-06 12:02 |  |  | service 2026-01-06; signed 2026-01-06 12:02 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E102 2026-01-06 | group_therapy |  | 4 | "Harbor Grove Behavioral Health \| Coping skills group" |  |
| 002 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 5 | "Group scheduled 10:00–11:30 local" |  |
| 003 | 1 | time | HG-E102 2026-01-06 | group_therapy | detail: whole group took a break; end: 11:00; label: actual; position: body; start: 10:45; what: no_therapy_interval | 12 | "The whole group took a break from 10:45 to 11:00." |  |
| 004 | 1 | participant | HG-E102 2026-01-06 | group_therapy | name: Leena Park, LPC; presence: not_stated; role: clinician; role_as_written: Facilitator | 7 | "Facilitator: Leena Park, LPC" |  |
| 005 | 1 | participant | HG-E102 2026-01-06 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 14 | "Rowan was quiet initially and responded when invited to identify a situation involving avoidance." |  |
| 006 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: Quiet initially, responded when invited; topic: other | 14 | "Rowan was quiet initially and responded when invited to identify a situation involving avoidance." |  |
| 007 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: patient; summary: Delayed work reply out of fear of being asked for a return date; topic: anxiety | 14 | "They described delaying a reply to a work message because they feared being asked for a firm return date." |  |
| 008 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: Practiced breathing; chose reading the message as next step; topic: functioning | 14 | "Rowan practiced a breathing exercise and selected reading the message before deciding how to respond as a possible next step." |  |
| 009 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: clinician; summary: Participation relevant, receptive to peers; topic: other | 14 | "Their participation was relevant to the topic, and they appeared receptive to peer suggestions." |  |
| 010 | 1 | statement | HG-E102 2026-01-06 | group_therapy | says: no_therapy_provided | 12 | "No therapy was conducted during that interval." |  |
| 011 | 1 | statement | HG-E102 2026-01-06 | group_therapy | says: not_an_attendance_record | 14 | "The patient attendance roster is maintained by the group desk." |  |
| 012 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |

Coverage: 11 times, dates and record numbers in the document. 10 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E102 | captured on another line |

### BH-D005: early_group_attendance_roster.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | attendance_record | Group desk attendance extract | not_stated |  |  | exported_or_prepared 2026-01-12 15:10; service 2026-01-06; service 2026-01-12 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E102 2026-01-06 | group_therapy |  | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 002 | 1 | contact | HG-E105 2026-01-12 | group_therapy |  | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 003 | 1 | modality | HG-E102 2026-01-06 | group_therapy | modality: in_person | 13 | "Reception directed them to the group room after check-in." |  |
| 004 | 1 | modality | HG-E105 2026-01-12 | group_therapy | modality: in_person | 15 | "Rowan checked in before the group began and remained until the group was released." |  |
| 005 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 006 | 1 | time | HG-E102 2026-01-06 | group_therapy | label: actual; position: table; start: 10:15; what: patient_arrival | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 007 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:15; label: actual; position: table; what: patient_departure | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 008 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 009 | 1 | time | HG-E105 2026-01-12 | group_therapy | label: actual; position: table; start: 10:00; what: patient_arrival | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 010 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 011 | 1 | attendance | HG-E102 2026-01-06 | group_therapy | status: attended_part; status_as_written: Attended part | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 012 | 1 | attendance | HG-E102 2026-01-06 | group_therapy | reason: previously arranged ride; status: attended_part; status_as_written: would need to leave early for a previously arranged ride | 13 | "Rowan advised the facilitator that they would need to leave early for a previously arranged ride." |  |
| 013 | 1 | attendance | HG-E102 2026-01-06 | group_therapy | reason: difficulty finding parking; status: attended_part; status_as_written: running behind after difficulty finding parking | 13 | "Rowan called from the building entrance to say they were running behind after difficulty finding parking." |  |
| 014 | 1 | attendance | HG-E105 2026-01-12 | group_therapy | status: attended; status_as_written: Attended full | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 015 | 1 | attendance | HG-E105 2026-01-12 | group_therapy | status: attended; status_as_written: checked in before the group began and remained until the group was released | 15 | "Rowan checked in before the group began and remained until the group was released." |  |
| 016 | 1 | participant | HG-E102 2026-01-06 | group_therapy | name: Rowan Mercer; presence: present_part; role: patient | 10 | "2026-01-06 \| HG-E102   \| 10:00–11:30    \| 10:15           \| 11:15            \| Attended part" |  |
| 017 | 1 | participant | HG-E102 2026-01-06 | group_therapy | presence: not_stated; role: clinician; role_as_written: facilitator | 13 | "Rowan advised the facilitator that they would need to leave early for a previously arranged ride." |  |
| 018 | 1 | participant | HG-E105 2026-01-12 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 11 | "2026-01-12 \| HG-E105   \| 10:00–11:30    \| 10:00           \| 11:30            \| Attended full" |  |
| 019 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: patient; summary: Running late due to parking difficulty; topic: other | 13 | "Rowan called from the building entrance to say they were running behind after difficulty finding parking." |  |
| 020 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: patient; summary: Needed to leave early for a prearranged ride; topic: functioning | 13 | "Rowan advised the facilitator that they would need to leave early for a previously arranged ride." |  |
| 021 | 1 | observation | HG-E102 2026-01-06 | group_therapy | date: 2026-01-06; speaker: staff; summary: Did not re-enter group room after departing; topic: other | 13 | "Rowan did not re-enter the group room after departing." |  |
| 022 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: staff; summary: No transport concern reported; topic: other | 15 | "No transport concern was reported at that time." |  |
| 023 | 1 | statement |  |  | says: prepared_from_signed_record | 17 | "Prepared from the signed reception attendance sheet for the two dates listed." |  |
| 024 | 1 | statement |  |  | says: other | 17 | "The desk records arrival and departure when members enter or leave the scheduled group." |  |
| 025 | 1 | statement |  |  | says: other | 17 | "Session activities and room breaks are documented in the facilitator's record." |  |
| 026 | 1 | statement |  |  | says: other | 7 | "Patient entries shown below; other member rows omitted." |  |
| 027 | 1 | statement | HG-E102 2026-01-06 | group_therapy | says: other | 13 | "Departure was marked when Rowan returned their visitor badge." |  |

Coverage: 19 times, dates and record numbers in the document. 19 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D006: early_appointment_status_export.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-20 | schedule_export | Appointment desk | not_stated |  |  | exported_or_prepared 2026-01-16 16:50; period_start 2026-01-05; period_end 2026-01-16 |

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
| 009 | 1 | contact | HG-E109 2026-01-16 | collateral_contact |  | 18 | "HG-E109   \| Jan16 \| Family collateral      \| 14:00–14:40    \| Completed" |  |
| 010 | 1 | time | HG-E101 2026-01-05 | individual_therapy | end: 09:50; label: scheduled; position: table; start: 09:00; what: contact_interval | 10 | "HG-E101   \| Jan05 \| Individual therapy     \| 09:00–09:50    \| Completed" |  |
| 011 | 1 | time | HG-E102 2026-01-06 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 11 | "HG-E102   \| Jan06 \| Coping skills group    \| 10:00–11:30    \| Attended part" |  |
| 012 | 1 | time | HG-E103 2026-01-08 | individual_therapy | end: 11:45; label: scheduled; position: table; start: 11:00; what: contact_interval | 12 | "HG-E103   \| Jan08 \| Individual therapy     \| 11:00–11:45    \| No show" |  |
| 013 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: scheduled; position: table; start: 14:00; what: contact_interval | 13 | "HG-E104   \| Jan09 \| Family therapy         \| 14:00–14:45    \| Completed" |  |
| 014 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 14 | "HG-E105   \| Jan12 \| Coping skills group    \| 10:00–11:30    \| Completed" |  |
| 015 | 1 | time | HG-E106 2026-01-13 | medication_management | end: 09:25; label: scheduled; position: table; start: 09:00; what: contact_interval | 15 | "HG-E106   \| Jan13 \| Medication management  \| 09:00–09:25    \| Completed" |  |
| 016 | 1 | time | HG-E107 2026-01-14 | individual_therapy | end: 11:45; label: scheduled; position: table; start: 11:00; what: contact_interval | 16 | "HG-E107   \| Jan14 \| Individual therapy     \| 11:00–11:45    \| Completed" |  |
| 017 | 1 | time | HG-E108 2026-01-15 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 17 | "HG-E108   \| Jan15 \| Coping skills group    \| 10:00–11:30    \| Clinic cancelled" |  |
| 018 | 1 | time | HG-E109 2026-01-16 | collateral_contact | end: 14:40; label: scheduled; position: table; start: 14:00; what: contact_interval | 18 | "HG-E109   \| Jan16 \| Family collateral      \| 14:00–14:40    \| Completed" |  |
| 019 | 1 | attendance | HG-E101 2026-01-05 | individual_therapy | status: completed; status_as_written: Completed | 10 | "HG-E101   \| Jan05 \| Individual therapy     \| 09:00–09:50    \| Completed" |  |
| 020 | 1 | attendance | HG-E102 2026-01-06 | group_therapy | status: attended_part; status_as_written: Attended part | 11 | "HG-E102   \| Jan06 \| Coping skills group    \| 10:00–11:30    \| Attended part" |  |
| 021 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | status: no_show; status_as_written: No show | 12 | "HG-E103   \| Jan08 \| Individual therapy     \| 11:00–11:45    \| No show" |  |
| 022 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | status: no_show; status_as_written: remained unarrived at close of its appointment slot | 20 | "HG-E103 remained unarrived at close of its appointment slot on January 8." |  |
| 023 | 1 | attendance | HG-E104 2026-01-09 | family_therapy | status: completed; status_as_written: Completed | 13 | "HG-E104   \| Jan09 \| Family therapy         \| 14:00–14:45    \| Completed" |  |
| 024 | 1 | attendance | HG-E105 2026-01-12 | group_therapy | status: completed; status_as_written: Completed | 14 | "HG-E105   \| Jan12 \| Coping skills group    \| 10:00–11:30    \| Completed" |  |
| 025 | 1 | attendance | HG-E106 2026-01-13 | medication_management | status: completed; status_as_written: Completed | 15 | "HG-E106   \| Jan13 \| Medication management  \| 09:00–09:25    \| Completed" |  |
| 026 | 1 | attendance | HG-E107 2026-01-14 | individual_therapy | status: completed; status_as_written: Completed | 16 | "HG-E107   \| Jan14 \| Individual therapy     \| 11:00–11:45    \| Completed" |  |
| 027 | 1 | attendance | HG-E108 2026-01-15 | group_therapy | status: cancelled_by_clinic; status_as_written: Clinic cancelled | 17 | "HG-E108   \| Jan15 \| Coping skills group    \| 10:00–11:30    \| Clinic cancelled" |  |
| 028 | 1 | attendance | HG-E108 2026-01-15 | group_therapy | reason: staff illness was reported; status: cancelled_by_clinic; status_as_written: removed from the active room schedule | 20 | "HG-E108 was removed from the active room schedule after staff illness was reported." |  |
| 029 | 1 | attendance | HG-E109 2026-01-16 | collateral_contact | status: completed; status_as_written: Completed | 18 | "HG-E109   \| Jan16 \| Family collateral      \| 14:00–14:40    \| Completed" |  |
| 030 | 1 | attendance | HG-E109 2026-01-16 | collateral_contact | status: absent; status_as_written: Rowan could not attend | 20 | "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend." |  |
| 031 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Rowan Mercer; presence: absent; role: patient | 20 | "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend." |  |
| 032 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | presence: not_stated; role: family_or_partner; role_as_written: partner | 20 | "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend." |  |
| 033 | 1 | statement | HG-E103 2026-01-08 | individual_therapy | says: other | 20 | "Outreach was assigned to the individual therapist's support queue." |  |
| 034 | 1 | statement | HG-E108 2026-01-15 | group_therapy | says: other | 20 | "A cancellation message was released to all registered members." |  |
| 035 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: no_patient_contact | 20 | "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend." |  |
| 036 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |

Coverage: 47 times, dates and record numbers in the document. 43 captured, 4 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 20 | date | January 8 | captured on another line |
| 20 | number | HG-E103 | captured on another line |
| 20 | number | HG-E108 | captured on another line |
| 20 | number | HG-E109 | captured on another line |

### BH-D007: family_primary_jan09.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-19 | clinical_note | Family psychotherapy | signed by Mara Voss, 2026-01-09 16:24 |  |  | service 2026-01-09; signed 2026-01-09 16:24 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E104 2026-01-09 | family_therapy |  | 6 | "Encounter HG-E104 \| 2026-01-09, 14:00–14:45 local" |  |
| 002 | 1 | contact |  | individual_therapy |  | 18 | "review its effect at the next individual visit" |  |
| 003 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: not_labelled; position: header; start: 14:00; what: contact_interval | 6 | "Encounter HG-E104 \| 2026-01-09, 14:00–14:45 local" |  |
| 004 | 1 | attendance | HG-E104 2026-01-09 | family_therapy | status: attended; status_as_written: Present: Rowan and partner, Casey Mercer | 7 | "Present: Rowan and partner, Casey Mercer" |  |
| 005 | 1 | attendance | HG-E104 2026-01-09 | family_therapy | status: attended; status_as_written: remained present and engaged throughout the visit | 16 | "Rowan remained present and engaged throughout the visit." |  |
| 006 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Rowan Mercer; presence: present; role: patient | 7 | "Present: Rowan and partner, Casey Mercer" |  |
| 007 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Casey Mercer; presence: present; role: family_or_partner; role_as_written: partner | 7 | "Present: Rowan and partner, Casey Mercer" |  |
| 008 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Mara Voss; presence: not_stated; role: clinician; role_as_written: LCSW | 8 | "Clinicians: Mara Voss, LCSW; cofacilitator Leena Park, LPC" |  |
| 009 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Leena Park; presence: not_stated; role: clinician; role_as_written: cofacilitator, LPC | 8 | "Clinicians: Mara Voss, LCSW; cofacilitator Leena Park, LPC" |  |
| 010 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Rowan Mercer; presence: present; role: patient | 16 | "Rowan remained present and engaged throughout the visit." |  |
| 011 | 1 | stated_minutes | HG-E104 2026-01-09 | family_therapy | minutes: 45; of: patient_present | 9 | "Patient-present family therapy duration: 45 minutes" |  |
| 012 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Appointment focused on patterns of support at home while rebuilding routine; topic: reason_for_contact | 12 | "The appointment focused on patterns of support at home as Rowan attempts to rebuild a routine." |  |
| 013 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: Feels watched when asked repeatedly about contacting work; topic: other | 12 | "Rowan described feeling watched when asked repeatedly whether they had contacted work." |  |
| 014 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Partner worries giving space might leave patient isolated; topic: other | 12 | "Casey described worry that giving Rowan space might leave them isolated." |  |
| 015 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Both acknowledged intentions differed from how the other experienced the exchange; topic: progress | 12 | "Both were able to acknowledge that their intentions differed from how the other person experienced the exchange." |  |
| 016 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Patient practiced asking for one specific kind of help; topic: functioning | 14 | "Rowan practiced asking for one specific kind of help, and Casey practiced reflecting the request before offering suggestions." |  |
| 017 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Patient present and engaged throughout; topic: other | 16 | "Rowan remained present and engaged throughout the visit." |  |
| 018 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: More animated describing shared evening walk, identified as non-pressuring support; topic: mood | 16 | "They became more animated when describing a shared evening walk and identified this as support that did not feel like pressure." |  |
| 019 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Partner agreed to single planned check-in about work preparation; topic: functioning | 16 | "Casey agreed to use a single planned check-in about work preparation instead of repeated reminders." |  |
| 020 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Patient agreed to say when they want practical assistance vs quiet company; topic: functioning | 16 | "Rowan agreed to say when they wanted practical assistance versus quiet company." |  |
| 021 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Plan to try planned check-in and review at next individual visit; topic: progress | 18 | "Plan: try the planned check-in and review its effect at the next individual visit." |  |
| 022 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Continue small activity steps selected in treatment; topic: functioning | 18 | "Continue the small activity steps selected in treatment." |  |
| 023 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |
| 024 | 1 | statement | HG-E104 2026-01-09 | family_therapy | says: other | 18 | "Leena Park's accompanying entry is filed under encounter HG-E104." |  |

Coverage: 10 times, dates and record numbers in the document. 9 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 18 | number | HG-E104 | captured on another line |

### BH-D008: family_cofacilitator_jan09.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Accompanying clinical entry | signed by Leena Park, 2026-01-10 08:42 |  |  | service 2026-01-09; signed 2026-01-10 08:42 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E104 2026-01-09 | family_therapy |  | 4 | "Harbor Grove Behavioral Health \| Family service" |  |
| 002 | 1 | time | HG-E104 2026-01-09 | family_therapy | end: 14:45; label: not_labelled; position: header; start: 14:00; what: contact_interval | 6 | "Encounter HG-E104 \| Date 2026-01-09 \| 14:00–14:45 local" |  |
| 003 | 1 | attendance | HG-E104 2026-01-09 | family_therapy | status: attended; status_as_written: both present for the full 45 minutes | 8 | "Participants: Rowan Mercer and Casey Mercer; both present for the full 45 minutes" |  |
| 004 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Rowan Mercer; presence: present; role: patient | 8 | "Participants: Rowan Mercer and Casey Mercer; both present for the full 45 minutes" |  |
| 005 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Casey Mercer; presence: present; role: family_or_partner; role_as_written: partner | 8 | "Participants: Rowan Mercer and Casey Mercer; both present for the full 45 minutes" |  |
| 006 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Leena Park; presence: not_stated; role: clinician; role_as_written: LPC, cofacilitator | 7 | "Author: Leena Park, LPC, cofacilitator with Mara Voss, LCSW" |  |
| 007 | 1 | participant | HG-E104 2026-01-09 | family_therapy | name: Mara Voss; presence: not_stated; role: clinician; role_as_written: LCSW | 7 | "Author: Leena Park, LPC, cofacilitator with Mara Voss, LCSW" |  |
| 008 | 1 | stated_minutes | HG-E104 2026-01-09 | family_therapy | minutes: 45; of: patient_present | 8 | "both present for the full 45 minutes" |  |
| 009 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: Patient viewed partner reminders as evidence of falling behind; topic: anxiety | 11 | "Rowan initially described partner reminders as evidence that they were falling behind." |  |
| 010 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Partner said reminders were meant to help but increased tension; topic: other | 11 | "Casey explained that the reminders were an attempt to help, while also recognizing that repeated prompts increased tension." |  |
| 011 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Patient able to reflect partner's concern; topic: functioning | 13 | "Rowan was able to state that Casey wanted reassurance that some preparation was happening." |  |
| 012 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Rehearsal became less defensive with repetition; topic: progress | 13 | "The rehearsal became less defensive with repetition." |  |
| 013 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Both contributed ideas for a brief check-in; topic: functioning | 13 | "Both participants contributed ideas for a brief, predictable check-in." |  |
| 014 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: clinician; summary: Couple chose an evening walk as shared activity; topic: functioning | 15 | "The couple selected an evening walk as an activity they could share without making it a discussion about progress." |  |
| 015 | 1 | observation | HG-E104 2026-01-09 | family_therapy | date: 2026-01-09; speaker: patient; summary: Patient found the walk more acceptable than a task review; topic: functioning | 15 | "Rowan said this felt more acceptable than a lengthy review of unfinished tasks." |  |
| 016 | 1 | statement | HG-E104 2026-01-09 | family_therapy | says: other | 11 | "Accompanying clinical entry for the family appointment facilitated with Mara Voss." |  |
| 017 | 1 | statement | HG-E104 2026-01-09 | family_therapy | says: other | 15 | "The agreed home practice and ongoing treatment plan are recorded in Mara Voss's primary note for HG-E104." |  |

Coverage: 10 times, dates and record numbers in the document. 8 captured, 2 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E104 | captured on another line |
| 15 | number | HG-E104 | captured on another line |

### BH-D009: group_facilitator_jan12.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | clinical_note | Coping skills group | signed by None, 2026-01-12 12:20 |  |  | service 2026-01-12; signed 2026-01-12 12:20 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E105 2026-01-12 | group_therapy |  | 4 | "Harbor Grove Behavioral Health \| Coping skills group" |  |
| 002 | 1 | time | HG-E105 2026-01-12 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 6 | "Scheduled group 10:00–11:30 local" |  |
| 003 | 1 | time | HG-E105 2026-01-12 | group_therapy | detail: Group break; no therapeutic activity occurred during the break; end: 10:55; label: actual; position: body; start: 10:40; what: no_therapy_interval | 12 | "Group break: 10:40–10:55; no therapeutic activity occurred during the break." |  |
| 004 | 1 | participant | HG-E105 2026-01-12 | group_therapy | name: Leena Park, LPC; presence: not_stated; role: clinician; role_as_written: Facilitator | 7 | "Facilitator: Leena Park, LPC" |  |
| 005 | 1 | participant | HG-E105 2026-01-12 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 14 | "Rowan contributed an example about leaving work messages unopened." |  |
| 006 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: clinician; summary: Patient gave example of leaving work messages unopened; topic: functioning | 14 | "Rowan contributed an example about leaving work messages unopened." |  |
| 007 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: patient; summary: Identified looking at one message as a lower step than replying to all; topic: functioning | 14 | "They identified looking at one message as a lower step than replying to every outstanding message." |  |
| 008 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: patient; summary: Took a walk with Casey over the weekend; topic: functioning | 14 | "They also described taking a walk with Casey over the weekend" |  |
| 009 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: patient; summary: Walk helped evening feel less dominated by worry; topic: anxiety | 14 | "noted that it helped the evening feel less dominated by worry" |  |
| 010 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: clinician; summary: Wrote down an action to try after breakfast; asked how to respond if morning went poorly; topic: functioning | 14 | "During the planning exercise, Rowan wrote down an action to try after breakfast and asked how to respond if the morning went poorly." |  |
| 011 | 1 | observation | HG-E105 2026-01-12 | group_therapy | date: 2026-01-12; speaker: clinician; summary: Listened to peers and offered supportive comment to another member; topic: other | 16 | "Rowan listened to peers and offered a supportive comment to another member." |  |
| 012 | 1 | statement | HG-E105 2026-01-12 | group_therapy | says: no_therapy_provided | 12 | "no therapeutic activity occurred during the break." |  |
| 013 | 1 | statement | HG-E105 2026-01-12 | group_therapy | says: not_an_attendance_record | 16 | "Attendance is recorded on the group desk roster." |  |

Coverage: 11 times, dates and record numbers in the document. 10 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 5 | number | HG-E105 | captured on another line |

### BH-D010: medication_review_jan13.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | clinical_note | Prescriber visit | signed by Elias Brenner, NP, 2026-01-13 10:04 |  |  | service 2026-01-13; signed 2026-01-13 10:04 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E106 2026-01-13 | medication_management |  | 6 | "Encounter HG-E106 \| Date 2026-01-13" |  |
| 002 | 1 | time | HG-E106 2026-01-13 | medication_management | end: 09:25; label: actual; position: header; start: 09:00; what: contact_interval | 7 | "Actual visit 09:00–09:25 local; completed, 25 minutes" |  |
| 003 | 1 | attendance | HG-E106 2026-01-13 | medication_management | status: completed; status_as_written: completed | 7 | "Actual visit 09:00–09:25 local; completed, 25 minutes" |  |
| 004 | 1 | attendance | HG-E106 2026-01-13 | medication_management | status: attended; status_as_written: attended | 11 | "Rowan attended for medication management." |  |
| 005 | 1 | participant | HG-E106 2026-01-13 | medication_management | name: Rowan Mercer; presence: present; role: patient | 11 | "Rowan attended for medication management." |  |
| 006 | 1 | participant | HG-E106 2026-01-13 | medication_management | name: Elias Brenner; presence: not_stated; role: clinician; role_as_written: Clinician | 8 | "Clinician: Elias Brenner, NP" |  |
| 007 | 1 | stated_minutes | HG-E106 2026-01-13 | medication_management | minutes: 25; of: contact_total | 7 | "Actual visit 09:00–09:25 local; completed, 25 minutes" |  |
| 008 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: Attended for medication management; topic: reason_for_contact | 11 | "Rowan attended for medication management." |  |
| 009 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: Continuing sleep interruption and daytime tiredness; topic: sleep | 11 | "Rowan reported continuing sleep interruption and daytime tiredness." |  |
| 010 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: Mood somewhat less heavy on days with planned activity; topic: mood | 11 | "They described mood as somewhat less heavy on days with a planned activity" |  |
| 011 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: Remained concerned about work communication; topic: anxiety | 11 | "but remained concerned about work communication." |  |
| 012 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: Medication list reviewed and reconciled; topic: medication | 11 | "The medication list was reviewed with Rowan and reconciled with the active chart." |  |
| 013 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: patient; summary: Denied new urgent medication-related concern; topic: medication | 13 | "Rowan denied a new medication-related concern requiring urgent intervention." |  |
| 014 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: Attentive, asked questions, could restate next steps; topic: functioning | 13 | "Rowan was attentive, asked questions about the monitoring plan, and could restate the next steps." |  |
| 015 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: No new physical complaint; topic: other | 13 | "No new physical complaint was raised during this visit." |  |
| 016 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: Ongoing depressive symptoms; topic: mood | 15 | "Assessment: ongoing depressive and anxiety symptoms with sleep disruption." |  |
| 017 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: Ongoing anxiety symptoms; topic: anxiety | 15 | "Assessment: ongoing depressive and anxiety symptoms with sleep disruption." |  |
| 018 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: Sleep disruption; topic: sleep | 15 | "Assessment: ongoing depressive and anxiety symptoms with sleep disruption." |  |
| 019 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: Engaged with therapy program, intends to continue appointments; topic: progress | 15 | "Rowan is engaged with the therapy program and intends to continue the scheduled appointments." |  |
| 020 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: Medication monitoring will continue; topic: medication | 15 | "Medication monitoring will continue during the outpatient episode, with later follow-up arranged according to clinical response." |  |
| 021 | 1 | observation | HG-E106 2026-01-13 | medication_management | date: 2026-01-13; speaker: clinician; summary: Directed to bring concerns to treating therapist; topic: functioning | 17 | "Rowan was directed to bring activity and communication concerns to the treating therapist for continued work." |  |
| 022 | 1 | statement | HG-E106 2026-01-13 | medication_management | says: no_therapy_provided | 17 | "No separate psychotherapy component was provided or documented." |  |
| 023 | 1 | statement | HG-E106 2026-01-13 | medication_management | says: other | 17 | "Service documented: medication review and management only." |  |
| 024 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D011: individual_therapy_jan14.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | clinical_note | Individual psychotherapy | signed by Mara Voss, LCSW, 2026-01-14 13:16 |  |  | service 2026-01-14; signed 2026-01-14 13:16 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E107 2026-01-14 | individual_therapy |  | 6 | "Encounter HG-E107 \| Date 2026-01-14" |  |
| 002 | 1 | contact |  | individual_therapy |  | 11 | "since the prior individual appointment" |  |
| 003 | 1 | contact |  | family_therapy |  | 11 | "Rowan described the family appointment as helpful" |  |
| 004 | 1 | contact |  |  |  | 15 | "explored the missed appointment from the prior week" |  |
| 005 | 1 | contact |  | individual_therapy |  | 17 | "Rowan will review the result at the next individual visit." |  |
| 006 | 1 | time | HG-E107 2026-01-14 | individual_therapy | end: 11:45; label: not_labelled; position: header; start: 11:00; what: patient_present | 7 | "Patient-present session 11:00–11:45 local" |  |
| 007 | 1 | attendance | HG-E107 2026-01-14 | individual_therapy | status: completed; status_as_written: completed | 7 | "completed, 45 minutes" |  |
| 008 | 1 | attendance |  |  | status: absent; status_as_written: missed | 15 | "explored the missed appointment from the prior week" |  |
| 009 | 1 | participant | HG-E107 2026-01-14 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 7 | "Patient-present session 11:00–11:45 local" |  |
| 010 | 1 | participant | HG-E107 2026-01-14 | individual_therapy | name: Mara Voss; presence: not_stated; role: clinician; role_as_written: Clinician | 8 | "Clinician: Mara Voss, LCSW" |  |
| 011 | 1 | stated_minutes | HG-E107 2026-01-14 | individual_therapy | minutes: 45; of: patient_present | 7 | "completed, 45 minutes" |  |
| 012 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: Completed small activities: opened work message, two short walks; topic: functioning | 11 | "Rowan reported completing several small activities since the prior individual appointment, including opening a work message and taking two short walks." |  |
| 013 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: Has not replied to message; imagines being asked unanswerable questions; topic: anxiety | 11 | "They have not yet replied to the message and continue to imagine being asked questions they cannot answer." |  |
| 014 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: Family appointment helpful; check-in reduced reminders; topic: progress | 11 | "Rowan described the family appointment as helpful because the planned check-in with Casey reduced repeated reminders." |  |
| 015 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: Sleep remains interrupted; topic: sleep | 11 | "Sleep remains interrupted, and getting started in the morning continues to require effort." |  |
| 016 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: Starting the morning requires effort; topic: functioning | 11 | "getting started in the morning continues to require effort" |  |
| 017 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: Physical tension during rehearsal but stayed with task; topic: anxiety | 13 | "Rowan noticed physical tension during the rehearsal but was able to remain with the task." |  |
| 018 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: patient; summary: Message felt less overwhelming when limited in scope; topic: anxiety | 13 | "They said the message seemed less overwhelming when it did not need to solve the entire return-to-work question." |  |
| 019 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: Identified setting out appointment info evening before as preparation step; topic: functioning | 15 | "Rowan identified setting out appointment information the evening before as a helpful preparation step." |  |
| 020 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: Affect more varied than at intake; topic: mood | 15 | "Affect was more varied than at intake, although worry was evident when discussing employment." |  |
| 021 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: Worry evident discussing employment; topic: anxiety | 15 | "although worry was evident when discussing employment" |  |
| 022 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: Plan: send acknowledgment, track morning activity, practice breathing before avoided task; topic: functioning | 17 | "Plan: attempt the drafted acknowledgment, continue morning activity tracking, and practice the breathing skill before an avoided task." |  |
| 023 | 1 | observation | HG-E107 2026-01-14 | individual_therapy | date: 2026-01-14; speaker: clinician; summary: Continue group participation and family involvement; topic: progress | 17 | "Maintain planned group participation and family involvement as available." |  |
| 024 | 1 | statement |  |  | says: other | 2 | "SYNTHETIC TRAINING RECORD — Entirely fictional patient and organization." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D012: partner_collateral_jan16.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | clinical_note | Family collateral | signed by Mara Voss, 2026-01-16 16:08 |  |  | service 2026-01-16; signed 2026-01-16 16:08 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E109 2026-01-16 | collateral_contact |  | 6 | "Encounter HG-E109 \| Date 2026-01-16 \| 14:00–14:40 local" |  |
| 002 | 1 | contact |  | family_therapy |  | 15 | "reviewed supportive responses previously practiced in the family appointment" |  |
| 003 | 1 | contact |  | other |  | 17 | "Information from Casey will be incorporated into the next direct clinical review with Rowan." |  |
| 004 | 1 | time | HG-E109 2026-01-16 | collateral_contact | end: 14:40; label: not_labelled; position: header; start: 14:00; what: contact_interval | 6 | "Encounter HG-E109 \| Date 2026-01-16 \| 14:00–14:40 local" |  |
| 005 | 1 | attendance | HG-E109 2026-01-16 | collateral_contact | status: absent; status_as_written: Rowan was absent for the entire contact. | 8 | "Rowan was absent for the entire contact." |  |
| 006 | 1 | attendance | HG-E109 2026-01-16 | collateral_contact | reason: Rowan advised the office that they could not participate; status: other; status_as_written: could not participate | 11 | "Casey attended the arranged contact after Rowan advised the office that they could not participate." |  |
| 007 | 1 | attendance | HG-E109 2026-01-16 | collateral_contact | status: absent; status_as_written: did not join in person, by telephone, or by video | 17 | "Rowan did not join in person, by telephone, or by video." |  |
| 008 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Casey Mercer; presence: present; role: family_or_partner; role_as_written: partner | 8 | "Participant: Casey Mercer, partner." |  |
| 009 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Rowan Mercer; presence: absent; role: patient | 8 | "Rowan was absent for the entire contact." |  |
| 010 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Mara Voss; presence: not_stated; role: clinician; role_as_written: Clinician | 7 | "Clinician: Mara Voss, LCSW" |  |
| 011 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Casey Mercer; presence: present; role: family_or_partner | 11 | "Casey attended the arranged contact after Rowan advised the office that they could not participate." |  |
| 012 | 1 | participant | HG-E109 2026-01-16 | collateral_contact | name: Rowan Mercer; presence: absent; role: patient | 17 | "Rowan did not join in person, by telephone, or by video." |  |
| 013 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: Collateral discussion with partner only about home observations and supporting plan; topic: reason_for_contact | 11 | "This was a collateral discussion with Casey only, focused on observations at home and ways to support the treatment plan." |  |
| 014 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Patient taking short walks, more willing to discuss coming week; topic: functioning | 13 | "Casey reported that Rowan had been getting out for short walks and seemed more willing to discuss the coming week." |  |
| 015 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: Mornings remain difficult; topic: mood | 13 | "Mornings remain difficult" |  |
| 016 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Patient becomes quiet when conversation turns to work; topic: other | 13 | "Casey described Rowan becoming quiet when the conversation turns to work." |  |
| 017 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: Evening check-in has reduced unplanned reminders; topic: functioning | 13 | "The scheduled evening check-in has reduced unplanned reminders." |  |
| 018 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Less argument when asking what help patient wants; topic: other | 13 | "Casey said it takes effort to resist offering multiple solutions but has noticed less argument when asking what kind of help Rowan wants." |  |
| 019 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: Partner will offer walk or shared meal and use agreed check-in; topic: functioning | 15 | "Casey will continue to offer a walk or shared meal and will use the agreed check-in rather than repeated progress questions." |  |
| 020 | 1 | observation | HG-E109 2026-01-16 | collateral_contact | date: 2026-01-16; speaker: clinician; summary: No new treatment decision made with patient; topic: progress | 17 | "No new treatment decision was made with Rowan during this appointment." |  |
| 021 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: no_patient_contact | 8 | "Rowan was absent for the entire contact." |  |
| 022 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: other | 11 | "This was a collateral discussion with Casey only, focused on observations at home and ways to support the treatment plan." |  |
| 023 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: no_patient_contact | 17 | "Rowan did not join in person, by telephone, or by video." |  |
| 024 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: no_therapy_provided | 17 | "No patient-present psychotherapy occurred during this contact." |  |
| 025 | 1 | statement | HG-E109 2026-01-16 | collateral_contact | says: other | 17 | "No new treatment decision was made with Rowan during this appointment." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D013: symptom_measure_review_jan16.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | questionnaire_review | Measurement review | not_stated |  |  | completed 2026-01-16 08:17; reviewed 2026-01-16 09:10 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | 2026-01-16 | questionnaire_review |  | 4 | "Harbor Grove Behavioral Health \| Measurement review" |  |
| 002 | 1 | contact | 2026-01-05 | other |  | 11 | "the intake score of 18 recorded on January 5" |  |
| 003 | 1 | score |  |  | completed_date: 2026-01-16; completed_time: 08:17; form_id: HG-Q116; instrument: PHQ-9; relation: completion; score: 14 | 8 | "Total score: 14" |  |
| 004 | 1 | score |  |  | completed_date: 2026-01-05; instrument: PHQ-9; relation: mention; score: 18 | 11 | "the intake score of 18 recorded on January 5" |  |
| 005 | 1 | observation | 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; summary: Score lower than intake score; topic: progress | 11 | "The submitted score is lower than the intake score of 18 recorded on January 5." |  |
| 006 | 1 | observation | 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: patient; summary: Getting out of apartment a little easier; topic: functioning | 11 | "Rowan wrote that getting out of the apartment had become a little easier" |  |
| 007 | 1 | observation | 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: patient; summary: Thinking about work leads to procrastination; topic: functioning | 11 | "thinking about work continued to make them want to put things off" |  |
| 008 | 1 | observation | 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: patient; summary: Sleep inconsistent; topic: sleep | 11 | "Rowan also described sleep as inconsistent." |  |
| 009 | 1 | observation | 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; summary: Some improvement in depressive symptoms; topic: progress | 13 | "the score and recent individual-session material suggest some improvement in depressive symptoms" |  |
| 010 | 1 | observation | 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; summary: Persistent avoidance and difficulty initiating work communication; topic: functioning | 13 | "Persistent avoidance, difficulty initiating work communication" |  |
| 011 | 1 | observation | 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; summary: Sleep disruption remains clinically relevant; topic: sleep | 13 | "and sleep disruption remain clinically relevant" |  |
| 012 | 1 | observation | 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; summary: Attempted small activities and communication practice; no reliable routine yet; topic: functioning | 13 | "Rowan has attempted small activities and communication practice but has not yet established a reliable routine." |  |
| 013 | 1 | observation | 2026-01-16 | questionnaire_review | date: 2026-01-16; speaker: clinician; summary: Continue current therapeutic focus; topic: progress | 13 | "Continue the current therapeutic focus and review functioning alongside symptom change during the next direct appointment." |  |
| 014 | 1 | statement | 2026-01-16 | questionnaire_review | says: no_new_assessment | 11 | "No additional questionnaire was submitted with this update." |  |
| 015 | 1 | statement | 2026-01-16 | questionnaire_review | says: not_a_visit | 15 | "no clinical appointment occurred at the time of review" |  |
| 016 | 1 | statement | 2026-01-16 | questionnaire_review | says: other | 15 | "This entry records review of the portal submission" |  |
| 017 | 1 | statement | 2026-01-16 | questionnaire_review | says: other | 15 | "The form remains attached to the measurement tab with its original completion date." |  |

Coverage: 10 times, dates and record numbers in the document. 8 captured, 2 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | PHQ-9 | captured on another line |
| 6 | number | HG-Q116 | captured on another line |

### BH-D014: imported_measure_summary_received_jan26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-20 | import_receipt | Administrative import receipt | not_stated |  | copy; original signed by None, None | received 2026-01-26 07:44; completed 2026-01-16; reviewed 2026-01-16 09:10; received 2026-01-26 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | score |  |  | completed_date: 2026-01-16; form_id: HG-Q116; instrument: PHQ-9; relation: copy; score: 14 | 13 | "PHQ-9   \| 14     \| 2026-01-16     \| HG-Q116" |  |
| 002 | 1 | observation |  |  | date: 2026-01-16; speaker: clinician; speaker_name: Mara Voss; summary: some improvement in depressive symptoms; topic: mood | 15 | "some improvement in depressive symptoms" |  |
| 003 | 1 | observation |  |  | date: 2026-01-16; speaker: clinician; speaker_name: Mara Voss; summary: ongoing avoidance of work communication; topic: functioning | 15 | "ongoing avoidance of work communication" |  |
| 004 | 1 | observation |  |  | date: 2026-01-16; speaker: clinician; speaker_name: Mara Voss; summary: inconsistent sleep; topic: sleep | 15 | "inconsistent sleep" |  |
| 005 | 1 | observation |  |  | date: 2026-01-16; speaker: clinician; speaker_name: Mara Voss; summary: continue current therapeutic focus; topic: progress | 15 | "Continue current therapeutic focus and review practical functioning at the next direct appointment." |  |
| 006 | 1 | statement |  |  | says: is_copy_or_resend | 17 | "Import detail: copied result from the January 16 portal form." |  |
| 007 | 1 | statement |  |  | says: no_new_assessment | 17 | "No newly completed patient questionnaire is included in this batch." |  |
| 008 | 1 | statement |  |  | says: not_a_visit | 19 | "This receipt was entered by the administrative desk and does not document a visit with Rowan." |  |
| 009 | 1 | statement |  |  | says: other | 19 | "The measurement tab continues to hold the original patient submission." |  |
| 010 | 1 | statement |  |  | says: other | 17 | "The source form identifier and original completion date were retained in the imported row." |  |

Coverage: 13 times, dates and record numbers in the document. 11 captured, 1 captured on another line, 1 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-MEAS-0126 | not captured |
| 17 | date | January 16 | captured on another line |

### BH-D015: missed_visit_outreach_jan08.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | scheduling_log | Scheduling support log | not_stated |  |  | entered 2026-01-08 15:52; service 2026-01-08 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E103 2026-01-08 | individual_therapy |  | 6 | "Related appointment: HG-E103, 2026-01-08, 11:00–11:45 local" |  |
| 002 | 1 | contact | 2026-01-08 | scheduling_contact |  | 13 | "13:20: Outbound call placed to the patient's recorded number." |  |
| 003 | 1 | contact | 2026-01-08 | scheduling_contact |  | 15 | "15:36: Rowan returned the call." |  |
| 004 | 1 | contact | 2026-01-09 | family_therapy |  | 13 | "The next scheduled appointment remained the family visit on January 9." |  |
| 005 | 1 | modality | 2026-01-08 | scheduling_contact | modality: telephone | 13 | "Outbound call placed to the patient's recorded number." |  |
| 006 | 1 | modality | 2026-01-08 | scheduling_contact | modality: telephone | 15 | "Rowan returned the call." |  |
| 007 | 1 | time | HG-E103 2026-01-08 | individual_therapy | end: 11:45; label: scheduled; position: header; start: 11:00; what: contact_interval | 6 | "Related appointment: HG-E103, 2026-01-08, 11:00–11:45 local" |  |
| 008 | 1 | time | HG-E103 2026-01-08 | individual_therapy | detail: Reception notified the clinician that Rowan had not checked in; label: actual; position: body; start: 11:12; what: other | 9 | "11:12: Reception notified the clinician that Rowan had not checked in." |  |
| 009 | 1 | time | HG-E103 2026-01-08 | individual_therapy | detail: Appointment marked no show; label: actual; position: body; start: 11:45; what: other | 11 | "11:45: Appointment marked no show." |  |
| 010 | 1 | time | 2026-01-08 | scheduling_contact | detail: Outbound call placed; label: actual; position: body; start: 13:20; what: other | 13 | "13:20: Outbound call placed to the patient's recorded number." |  |
| 011 | 1 | time | 2026-01-08 | scheduling_contact | detail: Rowan returned the call; label: actual; position: body; start: 15:36; what: other | 15 | "15:36: Rowan returned the call." |  |
| 012 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | entry_entered_by: N. Ellis; entry_entered_date: 2026-01-08; entry_entered_time: 15:52; status: no_show; status_as_written: no show | 11 | "11:45: Appointment marked no show." |  |
| 013 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | status: absent; status_as_written: not seen | 11 | "Rowan was not seen for the scheduled individual visit." |  |
| 014 | 1 | attendance | HG-E103 2026-01-08 | individual_therapy | status: absent; status_as_written: had not checked in | 9 | "Reception notified the clinician that Rowan had not checked in." |  |
| 015 | 1 | participant | HG-E103 2026-01-08 | individual_therapy | name: Rowan Mercer; presence: absent; role: patient | 11 | "Rowan was not seen for the scheduled individual visit." |  |
| 016 | 1 | participant | HG-E103 2026-01-08 | individual_therapy | presence: not_stated; role: staff; role_as_written: Reception | 9 | "Reception notified the clinician that Rowan had not checked in." |  |
| 017 | 1 | participant | 2026-01-08 | scheduling_contact | name: Rowan Mercer; presence: present; role: patient | 15 | "15:36: Rowan returned the call." |  |
| 018 | 1 | participant | 2026-01-08 | scheduling_contact | presence: present; role: staff; role_as_written: Staff | 15 | "Staff verified the appointment time and location and offered to resend the existing appointment list." |  |
| 019 | 1 | participant | 2026-01-09 | family_therapy | name: Casey; presence: not_stated; role: family_or_partner | 15 | "confirmed that they still intended to attend the next day's visit with Casey" |  |
| 020 | 1 | observation | 2026-01-08 | scheduling_contact | date: 2026-01-08; speaker: patient; summary: Poor night of sleep; topic: sleep | 15 | "They said the morning had gotten away from them after a poor night of sleep" |  |
| 021 | 1 | observation | 2026-01-08 | scheduling_contact | date: 2026-01-08; speaker: patient; summary: Intends to attend next day's family visit; topic: functioning | 15 | "confirmed that they still intended to attend the next day's visit with Casey" |  |
| 022 | 1 | observation | 2026-01-08 | scheduling_contact | date: 2026-01-08; speaker: clinician; summary: Patient requested appointment list through portal; topic: functioning | 15 | "Rowan requested the list through the portal." |  |
| 023 | 1 | observation | 2026-01-08 | scheduling_contact | date: 2026-01-08; speaker: clinician; summary: Callback was about scheduling and contact information; topic: reason_for_contact | 17 | "The callback addressed scheduling and contact information." |  |
| 024 | 1 | observation | HG-E103 2026-01-08 | individual_therapy | date: 2026-01-08; speaker: clinician; summary: Clinician notified of missed appointment; barriers to be discussed next visit; topic: other | 17 | "The individual clinician was notified of the missed appointment so that barriers to attendance could be discussed at the next visit." |  |
| 025 | 1 | statement | 2026-01-08 | scheduling_contact | says: no_therapy_provided | 17 | "No therapy intervention was conducted." |  |
| 026 | 1 | statement | 2026-01-08 | scheduling_contact | says: no_patient_contact | 13 | "No answer; a brief callback request was left without clinical detail." |  |
| 027 | 1 | statement | HG-E103 2026-01-08 | individual_therapy | says: no_patient_contact | 11 | "Rowan was not seen for the scheduled individual visit." |  |
| 028 | 1 | statement | 2026-01-08 | scheduling_contact | says: other | 17 | "The callback addressed scheduling and contact information." |  |
| 029 | 1 | statement | HG-E103 2026-01-08 | individual_therapy | says: other | 9 | "There was no arrival call or cancellation message on the scheduling line." |  |

Coverage: 10 times, dates and record numbers in the document. 10 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D016: group_cancellation_notice_jan15.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | cancellation_notice | Notice | not_stated | Patient copy | copy; original signed by None, None | entered 2026-01-15 08:12; service 2026-01-15; other 2026-01-15 11:35 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E108 2026-01-15 | group_therapy |  | 9 | "The coping skills group scheduled for January 15 from 10:00 to 11:30 is cancelled by the clinic because of staff illness." |  |
| 002 | 1 | contact | 2026-01-15 | scheduling_contact |  | 11 | "08:15: Portal notice delivered to Rowan's account." |  |
| 003 | 1 | contact | 2026-01-15 | scheduling_contact |  | 13 | "08:37: Rowan called the desk and acknowledged receiving the notice." |  |
| 004 | 1 | contact | 2026-01-16 | family_therapy |  | 13 | "Staff confirmed that the family-related appointment on January 16 remained on the schedule and that later appointments would appear on the next weekly list." |  |
| 005 | 1 | modality | 2026-01-15 | scheduling_contact | modality: message | 11 | "08:15: Portal notice delivered to Rowan's account." |  |
| 006 | 1 | modality | 2026-01-15 | scheduling_contact | modality: telephone | 13 | "08:37: Rowan called the desk and acknowledged receiving the notice." |  |
| 007 | 1 | modality | 2026-01-15 | scheduling_contact | modality: telephone | 15 | "The telephone contact was limited to confirming the cancellation and upcoming appointment information." |  |
| 008 | 1 | time | HG-E108 2026-01-15 | group_therapy | end: 11:30; label: scheduled; position: body; start: 10:00; what: contact_interval | 9 | "The coping skills group scheduled for January 15 from 10:00 to 11:30 is cancelled by the clinic because of staff illness." |  |
| 009 | 1 | time | 2026-01-15 | scheduling_contact | detail: Portal notice delivered; label: actual; position: body; start: 08:15; what: other | 11 | "08:15: Portal notice delivered to Rowan's account." |  |
| 010 | 1 | time | 2026-01-15 | scheduling_contact | detail: Rowan called the desk; label: actual; position: body; start: 08:37; what: other | 13 | "08:37: Rowan called the desk and acknowledged receiving the notice." |  |
| 011 | 1 | attendance | HG-E108 2026-01-15 | group_therapy | entry_entered_by: N. Ellis; entry_entered_date: 2026-01-15; entry_entered_time: 08:12; reason: staff illness; status: cancelled_by_clinic; status_as_written: cancelled by the clinic | 9 | "The coping skills group scheduled for January 15 from 10:00 to 11:30 is cancelled by the clinic because of staff illness." |  |
| 012 | 1 | attendance | HG-E108 2026-01-15 | group_therapy | status: cancelled_by_clinic; status_as_written: the office initiated the cancellation | 11 | "The notice states that the office initiated the cancellation and that the participant should not come to the group room this morning." |  |
| 013 | 1 | attendance | HG-E108 2026-01-15 | group_therapy | status: cancelled_by_clinic; status_as_written: No group was held and no participants were seen | 15 | "No group was held and no participants were seen for HG-E108." |  |
| 014 | 1 | participant | HG-E108 2026-01-15 | group_therapy | name: Rowan Mercer; presence: absent; role: patient | 15 | "No group was held and no participants were seen for HG-E108." |  |
| 015 | 1 | participant | 2026-01-15 | scheduling_contact | name: Rowan Mercer; presence: present; role: patient | 13 | "08:37: Rowan called the desk and acknowledged receiving the notice." |  |
| 016 | 1 | participant | 2026-01-15 | scheduling_contact | presence: present; role: staff; role_as_written: Staff | 13 | "Staff confirmed that the family-related appointment on January 16 remained on the schedule and that later appointments would appear on the next weekly list." |  |
| 017 | 1 | observation | 2026-01-15 | scheduling_contact | date: 2026-01-15; speaker: staff; summary: Patient did not request changes to remaining appointments; topic: functioning | 13 | "Rowan did not request a change to the remaining appointments during this call." |  |
| 018 | 1 | statement |  |  | says: is_copy_or_resend | 5 | "Patient copy: Rowan Mercer \| DOB 1991-04-12 \| MRN HG-M042" |  |
| 019 | 1 | statement | HG-E108 2026-01-15 | group_therapy | says: no_patient_contact | 15 | "No group was held and no participants were seen for HG-E108." |  |
| 020 | 1 | statement | HG-E108 2026-01-15 | group_therapy | says: no_therapy_provided | 15 | "No replacement group was conducted in the January 15 slot." |  |
| 021 | 1 | statement | 2026-01-15 | scheduling_contact | says: no_clinical_service | 15 | "The telephone contact was limited to confirming the cancellation and upcoming appointment information." |  |
| 022 | 1 | statement | HG-E108 2026-01-15 | group_therapy | says: other | 9 | "A covering facilitator is unavailable for this morning's group." |  |
| 023 | 1 | statement | HG-E108 2026-01-15 | group_therapy | says: other | 9 | "The group room has been released from the schedule, and registered participants are being contacted before the planned start time." |  |

Coverage: 12 times, dates and record numbers in the document. 10 captured, 2 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 6 | number | HG-E108 | captured on another line |
| 15 | number | HG-E108 | captured on another line |

### BH-D101: BH-D101_group_content_2026-01-19.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-15 | clinical_note | Skills group clinical record | signed by Leah Chen, LCSW, 2026-01-19 12:08 |  |  | service 2026-01-19; signed 2026-01-19 12:08 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 4 | "Group encounter: HG-E110 \| Facilitator: Leah Chen, LCSW" |  |
| 002 | 1 | contact | 2026-01-19 | individual_therapy |  | 10 | "The facilitator offered grounding and arranged a same-day individual meeting with the treating clinician." |  |
| 003 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 6 | "Scheduled group: 10:00–11:30." |  |
| 004 | 1 | time | HG-E110 2026-01-19 | group_therapy | detail: Nontherapeutic break; end: 11:00; label: not_labelled; position: header; start: 10:45; what: no_therapy_interval | 6 | "Nontherapeutic break: 10:45–11:00." |  |
| 005 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Leah Chen, LCSW; presence: not_stated; role: clinician; role_as_written: Facilitator | 4 | "Facilitator: Leah Chen, LCSW" |  |
| 006 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 10 | "Rowan initially followed the exercise and identified postponing a message to a supervisor as a familiar pattern." |  |
| 007 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: Followed exercise; identified postponing message to supervisor as familiar pattern; topic: functioning | 10 | "Rowan initially followed the exercise and identified postponing a message to a supervisor as a familiar pattern." |  |
| 008 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: Became visibly tense when discussing return to workplace; topic: anxiety | 10 | "When discussion turned to returning to the workplace, Rowan became visibly tense" |  |
| 009 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: patient; summary: Said amount of discussion felt difficult to manage; topic: anxiety | 10 | "said the amount of discussion felt difficult to manage" |  |
| 010 | 1 | observation | 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Same-day individual meeting arranged after distress in group; topic: reason_for_contact | 10 | "The facilitator offered grounding and arranged a same-day individual meeting with the treating clinician." |  |
| 011 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: Continue practicing coping skills before approach task; coordinate with individual clinician; topic: progress | 12 | "Continue practicing brief coping skills before an approach task." |  |
| 012 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: no_therapy_provided | 8 | "there was no facilitated discussion, assigned therapeutic activity, or patient treatment during that interval." |  |
| 013 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: not_an_attendance_record | 10 | "Patient-specific arrival and departure are maintained on the attendance roster." |  |
| 014 | 1 | statement | 2026-01-19 | individual_therapy | says: separate_contact | 10 | "The facilitator offered grounding and arranged a same-day individual meeting with the treating clinician." |  |
| 015 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 12 | "without assuming that participation in a group exercise reflects completion of the patient's own work task." |  |

Coverage: 11 times, dates and record numbers in the document. 11 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D102: BH-D102_original_attendance_2026-01-19.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-20 | attendance_record | Patient-specific attendance roster extract | signed by Leah Chen, LCSW, 2026-01-19 12:14 | Final |  | service 2026-01-19; signed 2026-01-19 12:14 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 4 | "Group encounter: HG-E110" |  |
| 002 | 1 | modality | HG-E110 2026-01-19 | group_therapy | modality: in_person | 6 | "Location: Outpatient skills room B" |  |
| 003 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 8 | "Scheduled opening: 10:00 \| Scheduled closing: 11:30" |  |
| 004 | 1 | time | HG-E110 2026-01-19 | group_therapy | label: actual; position: header; start: 10:00; what: patient_arrival | 9 | "Patient arrival: 10:00" |  |
| 005 | 1 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: actual; position: header; what: patient_departure | 9 | "Patient departure: 11:30" |  |
| 006 | 1 | attendance | HG-E110 2026-01-19 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-19; entry_signed_time: 12:14; status: attended; status_as_written: Attended | 9 | "Status: Attended" |  |
| 007 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: present; role: patient; role_as_written: Patient | 14 | "Rowan was present for the opening check-in." |  |
| 008 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: patient; summary: Anxiety about reconnecting with work; topic: anxiety | 14 | "The patient identified anxiety about reconnecting with work and accepted an exercise handout." |  |
| 009 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: patient; summary: Accepted an exercise handout; topic: functioning | 14 | "The patient identified anxiety about reconnecting with work and accepted an exercise handout." |  |
| 010 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: Patient requested additional help; access to individual clinician arranged; topic: functioning | 14 | "Staff arranged access to the individual clinician after Rowan requested additional help." |  |
| 011 | 1 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: No transportation assistance requested; topic: other | 14 | "No transportation assistance was requested." |  |
| 012 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 12 | "This is the patient row from the facilitator's attendance sheet." |  |
| 013 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 12 | "Arrival and departure fields were entered at roster close." |  |
| 014 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 12 | "Group topics, exercises, and the scheduled break are recorded in the separate group clinical record." |  |
| 015 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 16 | "This roster is the original signed attendance entry for the listed service date." |  |
| 016 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 16 | "The staff member closing the roster certified the patient row as shown at the time of signing." |  |

Coverage: 11 times, dates and record numbers in the document. 11 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D103: BH-D103_attendance_correction_2026-01-20.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | correction | Attendance correction | signed by Leah Chen, LCSW, 2026-01-20 08:42 | Final |  | entered 2026-01-20; service 2026-01-19; signed 2026-01-20 08:42 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 5 | "Applies to group encounter HG-E110, service date January 19, 2026" |  |
| 002 | 1 | contact | 2026-01-19 | individual_therapy |  | 11 | "or the separate individual appointment" |  |
| 003 | 1 | time | HG-E110 2026-01-19 | group_therapy | detail: corrected departure; end: 11:15; label: actual; position: body; what: patient_departure | 7 | "Patient departure for HG-E110 is 11:15, replacing the original roster value of 11:30." |  |
| 004 | 1 | time | HG-E110 2026-01-19 | group_therapy | label: not_labelled; position: body; start: 10:00; what: patient_arrival | 7 | "Patient arrival remains 10:00." |  |
| 005 | 1 | time | HG-E110 2026-01-19 | group_therapy | detail: leaving skills room B; end: 11:15; label: actual; position: body; what: patient_departure | 9 | "The room-transfer record shows Rowan leaving skills room B at 11:15 and being received by the individual clinician at 11:15." |  |
| 006 | 1 | time | 2026-01-19 | individual_therapy | detail: received by the individual clinician; label: actual; position: body; start: 11:15; what: patient_arrival | 9 | "being received by the individual clinician at 11:15" |  |
| 007 | 1 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 9 | "The room-transfer record shows Rowan leaving skills room B at 11:15" |  |
| 008 | 1 | participant | 2026-01-19 | individual_therapy | presence: not_stated; role: clinician; role_as_written: individual clinician | 9 | "being received by the individual clinician at 11:15" |  |
| 009 | 1 | correction | HG-E110 2026-01-19 | group_therapy | field: departure; field_as_written: Patient departure; new_value: 11:15; old_value: 11:30; reason: original group roster was found to retain the scheduled group closing time in Rowan's departure field | 7 | "Patient departure for HG-E110 is 11:15, replacing the original roster value of 11:30." |  |
| 010 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 9 | "the original group roster was found to retain the scheduled group closing time in Rowan's departure field" |  |
| 011 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 9 | "The group continued for other members until its scheduled close." |  |
| 012 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 11 | "This correction applies only to Rowan Mercer's departure field on the January 19 group attendance roster." |  |
| 013 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 11 | "It does not change the group service date, scheduled opening or closing, the break recorded in the group clinical note, or the separate individual appointment." |  |
| 014 | 1 | statement | 2026-01-19 | individual_therapy | says: separate_contact | 11 | "or the separate individual appointment" |  |
| 015 | 1 | statement |  |  | says: other | 11 | "The original signed roster is retained in the chart with this correction attached to its attendance entry." |  |
| 016 | 1 | statement |  |  | says: no_clinical_service | 13 | "No additional clinical service was provided in making this correction." |  |
| 017 | 1 | statement |  |  | says: other | 13 | "The group discussion and the individual clinician's assessment remain documented in their respective service records." |  |

Coverage: 15 times, dates and record numbers in the document. 14 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-E110 | captured on another line |

### BH-D104: BH-D104_resent_roster_received_2026-01-26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-9 | cover_sheet | Records inbox cover sheet | not_stated |  |  | received 2026-01-26 16:22; service 2026-01-19 |
| 2 | 10-21 | attendance_record | ATTACHED ROSTER COPY | unsigned | Final, signed | copy; original signed by Leah Chen, LCSW, 2026-01-19 12:14 | service 2026-01-19; signed 2026-01-19 12:14; entered 2026-01-26 16:31 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E110 2026-01-19 | group_therapy |  | 11 | "Service date: January 19, 2026 \| Group encounter: HG-E110" |  |
| 002 | 2 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 13 | "Scheduled opening: 10:00 \| Scheduled closing: 11:30" |  |
| 003 | 2 | time | HG-E110 2026-01-19 | group_therapy | label: actual; position: header; start: 10:00; what: patient_arrival | 14 | "Patient arrival: 10:00" |  |
| 004 | 2 | time | HG-E110 2026-01-19 | group_therapy | end: 11:30; label: actual; position: header; what: patient_departure | 14 | "Patient departure: 11:30" |  |
| 005 | 2 | attendance | HG-E110 2026-01-19 | group_therapy | status: attended; status_as_written: Attended | 14 | "Status: Attended" |  |
| 006 | 2 | participant | HG-E110 2026-01-19 | group_therapy | name: Rowan Mercer; presence: present; role: patient; role_as_written: Patient | 14 | "Status: Attended" |  |
| 007 | 2 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: Attended opening check-in and accepted handout; topic: functioning | 18 | "Rowan attended the opening check-in, accepted the exercise handout, and requested additional help from the individual clinician." |  |
| 008 | 2 | observation | HG-E110 2026-01-19 | group_therapy | date: 2026-01-19; speaker: clinician; summary: Requested additional help from individual clinician; topic: functioning | 18 | "requested additional help from the individual clinician." |  |
| 009 | 1 | statement | HG-E110 2026-01-19 | group_therapy | says: is_copy_or_resend | 8 | "The attached attendance sheet was resent following a request for the original group roster." |  |
| 010 | 1 | statement |  |  | says: other | 8 | "No correction sheet was included in this transmission." |  |
| 011 | 1 | statement |  |  | says: other | 8 | "The receipt date is the inbox processing date." |  |
| 012 | 2 | statement | HG-E110 2026-01-19 | group_therapy | says: other | 18 | "Group content is recorded separately." |  |
| 013 | 2 | statement | HG-E110 2026-01-19 | group_therapy | says: is_copy_or_resend | 20 | "This is a retransmission of the January 19 roster for HG-E110." |  |
| 014 | 2 | statement | HG-E110 2026-01-19 | group_therapy | says: no_new_signature | 20 | "The received copy contains no new clinician signature and records no additional visit." |  |
| 015 | 2 | statement | HG-E110 2026-01-19 | group_therapy | says: not_a_visit | 20 | "records no additional visit." |  |

Coverage: 18 times, dates and record numbers in the document. 17 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 20 | number | HG-E110 | captured on another line |

### BH-D105: BH-D105_individual_2026-01-19.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Individual psychotherapy | signed by Mira Patel, LCSW, 2026-01-19 12:32 |  |  | service 2026-01-19; signed 2026-01-19 12:32 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E111 2026-01-19 | individual_therapy |  | 3 | "Individual psychotherapy \| Encounter HG-E111" |  |
| 002 | 1 | contact | 2026-01-19 | group_therapy |  | 9 | "This visit was added because Rowan became anxious during group and needed individual grounding and review of coping strategies." |  |
| 003 | 1 | contact |  | individual_therapy |  | 13 | "Continue the established outpatient plan and review how the smaller task went at the next individual visit." |  |
| 004 | 1 | modality | HG-E111 2026-01-19 | individual_therapy | modality: in_person | 5 | "January 19, 2026 \| In person" |  |
| 005 | 1 | time | HG-E111 2026-01-19 | individual_therapy | end: 11:45; label: not_labelled; position: header; start: 11:15; what: patient_present | 6 | "Patient contact: 11:15–11:45" |  |
| 006 | 1 | attendance | HG-E111 2026-01-19 | individual_therapy | status: attended; status_as_written: Rowan participated throughout the individual contact | 11 | "Rowan participated throughout the individual contact and reported that the immediate intensity of anxiety eased enough to discuss a next step." |  |
| 007 | 1 | participant | HG-E111 2026-01-19 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 11 | "Rowan participated throughout the individual contact and reported that the immediate intensity of anxiety eased enough to discuss a next step." |  |
| 008 | 1 | participant | HG-E111 2026-01-19 | individual_therapy | name: Mira Patel, LCSW; presence: not_stated; role: clinician; role_as_written: Clinician | 7 | "Clinician: Mira Patel, LCSW" |  |
| 009 | 1 | stated_minutes | HG-E111 2026-01-19 | individual_therapy | minutes: 30; of: contact_total | 6 | "Completed: 30 minutes" |  |
| 010 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Visit added because patient became anxious in group and needed individual grounding; topic: reason_for_contact | 9 | "This visit was added because Rowan became anxious during group and needed individual grounding and review of coping strategies." |  |
| 011 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: patient; summary: Felt overwhelmed by workplace discussion; worried about return to work; topic: anxiety | 9 | "The patient described feeling overwhelmed when other members discussed workplace demands and worried that returning to work would expose difficulties keeping up." |  |
| 012 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Identified muscle tension, rapid breathing, urge to leave as early activation signs; topic: anxiety | 9 | "Rowan was able to identify muscle tension, rapid breathing, and an urge to leave as early signs of activation." |  |
| 013 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: patient; summary: Anxiety intensity eased enough to discuss next step; topic: anxiety | 11 | "Rowan participated throughout the individual contact and reported that the immediate intensity of anxiety eased enough to discuss a next step." |  |
| 014 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Agreed task: draft two sentences to supervisor, not required to send today; topic: functioning | 11 | "We narrowed the work-related task to drafting two sentences to a supervisor, without requiring that the message be sent today." |  |
| 015 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: patient; summary: Denied current suicidal thoughts; future oriented; topic: safety | 13 | "Rowan denied current suicidal thoughts and remained future oriented in discussing the next appointment." |  |
| 016 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: No acute safety concern identified; topic: safety | 13 | "No acute safety concern was identified during this contact." |  |
| 017 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Avoidance interferes with resuming work routine; topic: functioning | 13 | "Persistent avoidance and disrupted sleep continue to interfere with resuming a usual work routine." |  |
| 018 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Disrupted sleep continues; topic: sleep | 13 | "Persistent avoidance and disrupted sleep continue to interfere with resuming a usual work routine." |  |
| 019 | 1 | observation | HG-E111 2026-01-19 | individual_therapy | date: 2026-01-19; speaker: clinician; summary: Continue established outpatient plan; review task at next visit; topic: progress | 13 | "Continue the established outpatient plan and review how the smaller task went at the next individual visit." |  |
| 020 | 1 | statement | HG-E111 2026-01-19 | individual_therapy | says: separate_contact | 9 | "This visit was added because Rowan became anxious during group and needed individual grounding and review of coping strategies." |  |
| 021 | 1 | statement | HG-E111 2026-01-19 | individual_therapy | says: other | 9 | "Rowan came directly from the group room." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D106: BH-D106_telehealth_2026-01-21.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-14 | clinical_note | Individual psychotherapy | signed by Mira Patel, LCSW, 2026-01-21 15:04 |  |  | service 2026-01-21; signed 2026-01-21 15:04 |
| 2 | 15-21 | platform_export | ATTACHED PLATFORM CONNECTION EXPORT | not_stated |  |  | exported_or_prepared 2026-01-21 14:06; service 2026-01-21 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E112 HG-A112 2026-01-21 | individual_therapy |  | 3 | "Individual psychotherapy \| Encounter HG-E112 \| Appointment HG-A112" |  |
| 002 | 1 | modality | HG-E112 HG-A112 2026-01-21 | individual_therapy | modality: video | 5 | "January 21, 2026 \| Video \| Clinician: Mira Patel, LCSW" |  |
| 003 | 1 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | end: 13:20; label: actual; position: body; start: 13:00; what: patient_present | 7 | "Patient contact occurred 13:00–13:20 and 13:30–13:55." |  |
| 004 | 1 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | end: 13:55; label: actual; position: body; start: 13:30; what: patient_present | 7 | "Patient contact occurred 13:00–13:20 and 13:30–13:55." |  |
| 005 | 1 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | detail: Connection was lost; no therapeutic contact; end: 13:30; label: actual; position: body; start: 13:20; what: no_therapy_interval | 7 | "Connection was lost from 13:20–13:30; there was no therapeutic contact during that interval." |  |
| 006 | 2 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | detail: Call VC-112A; end: 13:20; label: actual; position: table; start: 13:00; what: connection | 17 | "HG-A112 \| VC-112A \| January 21 13:00 \| January 21 13:20" |  |
| 007 | 2 | time | HG-E112 HG-A112 2026-01-21 | individual_therapy | detail: Call VC-112B; end: 13:55; label: actual; position: table; start: 13:30; what: connection | 18 | "HG-A112 \| VC-112B \| January 21 13:30 \| January 21 13:55" |  |
| 008 | 1 | participant | HG-E112 HG-A112 2026-01-21 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 7 | "Patient contact occurred 13:00–13:20 and 13:30–13:55." |  |
| 009 | 1 | participant | HG-E112 HG-A112 2026-01-21 | individual_therapy | name: Mira Patel, LCSW; presence: not_stated; role: clinician; role_as_written: Clinician | 5 | "January 21, 2026 \| Video \| Clinician: Mira Patel, LCSW" |  |
| 010 | 1 | stated_minutes | HG-E112 HG-A112 2026-01-21 | individual_therapy | minutes: 45; of: patient_present | 7 | "Total patient psychotherapy contact: 45 minutes." |  |
| 011 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: patient; summary: Drafted return-to-work message but did not send it; topic: functioning | 9 | "Rowan reported drafting a short message about a possible gradual return to work but stopping before sending it." |  |
| 012 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: patient; summary: Identified repeated checking of draft as delaying the task; topic: functioning | 9 | "The patient identified checking the draft repeatedly as another way the task was being delayed." |  |
| 013 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: clinician; summary: Practiced reading draft once and choosing a planned send time; topic: functioning | 9 | "Practiced reading the draft once and choosing a planned time to send it." |  |
| 014 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: patient; summary: One improved night then a night of prolonged wakefulness; topic: sleep | 11 | "Rowan described one night of improved sleep followed by a night of prolonged wakefulness." |  |
| 015 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: clinician; summary: Engaged and able to restate agreed task; topic: functioning | 11 | "Rowan was engaged and able to restate the agreed task." |  |
| 016 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: clinician; summary: No urgent safety concern reported; topic: safety | 11 | "No urgent safety concern was reported." |  |
| 017 | 1 | observation | HG-E112 HG-A112 2026-01-21 | individual_therapy | date: 2026-01-21; speaker: clinician; summary: Follow-up remains with established outpatient team; topic: progress | 11 | "Follow-up remains with the established outpatient team." |  |
| 018 | 1 | statement | HG-E112 HG-A112 2026-01-21 | individual_therapy | says: no_therapy_provided | 7 | "Connection was lost from 13:20–13:30; there was no therapeutic contact during that interval." |  |
| 019 | 1 | statement | HG-E112 HG-A112 2026-01-21 | individual_therapy | says: same_contact_continued | 7 | "The reconnection continued the same clinical encounter under original appointment HG-A112." |  |
| 020 | 2 | statement | HG-E112 HG-A112 2026-01-21 | individual_therapy | says: same_contact_continued | 19 | "Second call reason: Rejoin original appointment after network disconnect." |  |

Coverage: 29 times, dates and record numbers in the document. 24 captured, 5 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 7 | number | HG-A112 | captured on another line |
| 17 | number | HG-A112 | captured on another line |
| 18 | date | January 21 | captured on another line |
| 18 | date | January 21 | captured on another line |
| 18 | number | HG-A112 | captured on another line |

### BH-D107: BH-D107_group_activity_records_2026-01-22_and_29.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-10 | clinical_note | Skills group activity record extract | signed by Leah Chen, LCSW, 2026-01-22 12:06 |  |  | service 2026-01-22; signed 2026-01-22 12:06 |
| 2 | 12-17 | clinical_note | Skills group activity record extract | signed by Leah Chen, LCSW, 2026-01-29 12:11 |  |  | service 2026-01-29; signed 2026-01-29 12:11 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E113 2026-01-22 | group_therapy |  | 7 | "January 22, 2026 \| Encounter HG-E113" |  |
| 002 | 2 | contact | HG-E118 2026-01-29 | group_therapy |  | 12 | "January 29, 2026 \| Encounter HG-E118" |  |
| 003 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 8 | "Scheduled group 10:00–11:30." |  |
| 004 | 1 | time | HG-E113 2026-01-22 | group_therapy | detail: Nontherapeutic break; end: 11:00; label: not_labelled; position: header; start: 10:45; what: no_therapy_interval | 8 | "Nontherapeutic break 10:45–11:00." |  |
| 005 | 2 | time | HG-E118 2026-01-29 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 13 | "Scheduled group 10:00–11:30." |  |
| 006 | 2 | time | HG-E118 2026-01-29 | group_therapy | detail: Nontherapeutic break; end: 11:00; label: not_labelled; position: header; start: 10:45; what: no_therapy_interval | 13 | "Nontherapeutic break 10:45–11:00." |  |
| 007 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Rowan Mercer; presence: present_part; role: patient | 9 | "Rowan joined the discussion after it had begun;" |  |
| 008 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Leah Chen, LCSW; presence: not_stated; role: clinician; role_as_written: Facilitator | 9 | "Facilitator encouraged a limited, planned review period and a stopping point." |  |
| 009 | 2 | participant | HG-E118 2026-01-29 | group_therapy | name: Rowan Mercer; presence: not_stated; role: patient | 14 | "Rowan participated in the paired rehearsal and accepted feedback about keeping the request brief." |  |
| 010 | 2 | participant | HG-E118 2026-01-29 | group_therapy | name: Leah Chen, LCSW; presence: not_stated; role: clinician; role_as_written: Facilitator | 14 | "The facilitator helped identify a specific question to ask rather than trying to anticipate every possible concern." |  |
| 011 | 1 | observation | HG-E113 2026-01-22 | group_therapy | date: 2026-01-22; speaker: clinician; summary: Patient joined discussion late; topic: functioning | 9 | "Rowan joined the discussion after it had begun;" |  |
| 012 | 1 | observation | HG-E113 2026-01-22 | group_therapy | date: 2026-01-22; speaker: patient; summary: Concern that seeing outstanding calendar items would be overwhelming; topic: anxiety | 9 | "described concern that seeing outstanding items would become overwhelming." |  |
| 013 | 1 | observation | HG-E113 2026-01-22 | group_therapy | date: 2026-01-22; speaker: clinician; summary: Facilitator encouraged planned review period with stopping point; topic: functioning | 9 | "Facilitator encouraged a limited, planned review period and a stopping point." |  |
| 014 | 1 | observation | HG-E113 2026-01-22 | group_therapy | date: 2026-01-22; speaker: clinician; summary: Patient contributed example after the break; topic: functioning | 9 | "The patient contributed an example to the discussion after the break." |  |
| 015 | 2 | observation | HG-E118 2026-01-29 | group_therapy | date: 2026-01-29; speaker: patient; summary: Opened work calendar but delayed follow-up conversation; topic: functioning | 14 | "Rowan reported opening the work calendar but delaying a follow-up conversation." |  |
| 016 | 2 | observation | HG-E118 2026-01-29 | group_therapy | date: 2026-01-29; speaker: clinician; summary: Participated in paired rehearsal and accepted feedback; topic: functioning | 14 | "Rowan participated in the paired rehearsal and accepted feedback about keeping the request brief." |  |
| 017 | 1 | statement | HG-E113 2026-01-22 | group_therapy | says: not_an_attendance_record | 9 | "the arrival field is maintained in the attendance register." |  |
| 018 | 2 | statement | HG-E113 2026-01-22 | group_therapy | says: no_therapy_provided | 17 | "For both dates, the break was unstructured time without therapeutic activity or facilitator treatment." |  |
| 019 | 2 | statement | HG-E118 2026-01-29 | group_therapy | says: no_therapy_provided | 17 | "For both dates, the break was unstructured time without therapeutic activity or facilitator treatment." |  |
| 020 | 2 | statement |  |  | says: not_an_attendance_record | 17 | "Patient arrival, departure, and attendance status are entered in the separate attendance register." |  |

Coverage: 19 times, dates and record numbers in the document. 19 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D108: BH-D108_final_attendance_and_cancellation_register.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-23 | attendance_record | Outpatient attendance and appointment disposition extract | not_stated | Final |  | exported_or_prepared 2026-01-30 17:10; service 2026-01-22; service 2026-01-27; service 2026-01-28; service 2026-01-29 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E113 2026-01-22 | group_therapy |  | 9 | "January 22 \| HG-E113 \| Skills group" |  |
| 002 | 1 | contact | HG-E116 2026-01-27 | group_therapy |  | 10 | "January 27 \| HG-E116 \| Skills group" |  |
| 003 | 1 | contact | HG-E117 2026-01-28 | individual_therapy |  | 11 | "January 28 \| HG-E117 \| Individual" |  |
| 004 | 1 | contact | HG-E118 2026-01-29 | group_therapy |  | 12 | "January 29 \| HG-E118 \| Skills group" |  |
| 005 | 1 | contact | 2026-01-27 | scheduling_contact |  | 16 | "An outreach message inviting the patient to contact scheduling was left after the group; no clinical discussion occurred." |  |
| 006 | 1 | contact | 2026-01-28 | scheduling_contact |  | 18 | "Cancellation received from patient January 28, 08:12." |  |
| 007 | 1 | modality | 2026-01-27 | scheduling_contact | modality: message | 16 | "An outreach message inviting the patient to contact scheduling was left after the group; no clinical discussion occurred." |  |
| 008 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 9 | "January 22 \| HG-E113 \| Skills group \| 10:00–11:30 \| 10:30 \| 11:30 \| Attended, late arrival" |  |
| 009 | 1 | time | HG-E113 2026-01-22 | group_therapy | label: actual; position: table; start: 10:30; what: patient_arrival | 9 | "January 22 \| HG-E113 \| Skills group \| 10:00–11:30 \| 10:30 \| 11:30 \| Attended, late arrival" |  |
| 010 | 1 | time | HG-E113 2026-01-22 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 9 | "January 22 \| HG-E113 \| Skills group \| 10:00–11:30 \| 10:30 \| 11:30 \| Attended, late arrival" |  |
| 011 | 1 | time | HG-E116 2026-01-27 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 10 | "January 27 \| HG-E116 \| Skills group \| 10:00–11:30 \| — \| — \| No show; patient did not attend" |  |
| 012 | 1 | time | HG-E117 2026-01-28 | individual_therapy | end: 14:45; label: scheduled; position: table; start: 14:00; what: contact_interval | 11 | "January 28 \| HG-E117 \| Individual \| 14:00–14:45 \| — \| — \| Patient cancelled before appointment" |  |
| 013 | 1 | time | HG-E118 2026-01-29 | group_therapy | end: 11:30; label: scheduled; position: table; start: 10:00; what: contact_interval | 12 | "January 29 \| HG-E118 \| Skills group \| 10:00–11:30 \| 10:00 \| 11:30 \| Attended" |  |
| 014 | 1 | time | HG-E118 2026-01-29 | group_therapy | label: actual; position: table; start: 10:00; what: patient_arrival | 12 | "January 29 \| HG-E118 \| Skills group \| 10:00–11:30 \| 10:00 \| 11:30 \| Attended" |  |
| 015 | 1 | time | HG-E118 2026-01-29 | group_therapy | end: 11:30; label: actual; position: table; what: patient_departure | 12 | "January 29 \| HG-E118 \| Skills group \| 10:00–11:30 \| 10:00 \| 11:30 \| Attended" |  |
| 016 | 1 | time | HG-E113 2026-01-22 | group_therapy | detail: remained until the group closed; label: actual; position: body; start: 10:30; what: patient_arrival | 14 | "Rowan arrived at 10:30 and remained until the group closed." |  |
| 017 | 1 | time | 2026-01-28 | scheduling_contact | detail: Cancellation received from patient; label: actual; position: body; start: 08:12; what: other | 18 | "Cancellation received from patient January 28, 08:12." |  |
| 018 | 1 | attendance | HG-E113 2026-01-22 | group_therapy | status: attended_part; status_as_written: Attended, late arrival | 9 | "January 22 \| HG-E113 \| Skills group \| 10:00–11:30 \| 10:30 \| 11:30 \| Attended, late arrival" |  |
| 019 | 1 | attendance | HG-E116 2026-01-27 | group_therapy | status: no_show; status_as_written: No show; patient did not attend | 10 | "January 27 \| HG-E116 \| Skills group \| 10:00–11:30 \| — \| — \| No show; patient did not attend" |  |
| 020 | 1 | attendance | HG-E117 2026-01-28 | individual_therapy | status: cancelled_by_patient; status_as_written: Patient cancelled before appointment | 11 | "January 28 \| HG-E117 \| Individual \| 14:00–14:45 \| — \| — \| Patient cancelled before appointment" |  |
| 021 | 1 | attendance | HG-E118 2026-01-29 | group_therapy | status: attended; status_as_written: Attended | 12 | "January 29 \| HG-E118 \| Skills group \| 10:00–11:30 \| 10:00 \| 11:30 \| Attended" |  |
| 022 | 1 | attendance | HG-E113 2026-01-22 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-22; entry_signed_time: 12:09; status: attended_part; status_as_written: arrived at 10:30 and remained until the group closed | 14 | "Rowan arrived at 10:30 and remained until the group closed." |  |
| 023 | 1 | attendance | HG-E116 2026-01-27 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-27; entry_signed_time: 11:54; status: absent; status_as_written: absent for the entire group | 16 | "Final roster confirms Rowan was absent for the entire group." |  |
| 024 | 1 | attendance | HG-E117 2026-01-28 | individual_therapy | entry_entered_by: Ana Reed; entry_entered_date: 2026-01-28; entry_entered_time: 08:18; reason: personal scheduling conflict; status: cancelled_by_patient; status_as_written: Cancellation received from patient | 18 | "Cancellation received from patient January 28, 08:12." |  |
| 025 | 1 | attendance | HG-E118 2026-01-29 | group_therapy | entry_signed_by: Leah Chen, LCSW; entry_signed_date: 2026-01-29; entry_signed_time: 12:15; status: attended; status_as_written: present from opening through closing | 20 | "Rowan was present from opening through closing." |  |
| 026 | 1 | participant | HG-E113 2026-01-22 | group_therapy | name: Rowan Mercer; presence: present_part; role: patient | 14 | "Rowan arrived at 10:30 and remained until the group closed." |  |
| 027 | 1 | participant | HG-E116 2026-01-27 | group_therapy | name: Rowan Mercer; presence: absent; role: patient | 16 | "Final roster confirms Rowan was absent for the entire group." |  |
| 028 | 1 | participant | HG-E118 2026-01-29 | group_therapy | name: Rowan Mercer; presence: present; role: patient | 20 | "Rowan was present from opening through closing." |  |
| 029 | 1 | observation | HG-E117 2026-01-28 | individual_therapy | date: 2026-01-28; speaker: patient; summary: Patient reported a personal scheduling conflict; topic: other | 18 | "Rowan reported a personal scheduling conflict." |  |
| 030 | 1 | statement |  |  | says: other | 6 | "Group rows contain actual patient arrival and departure fields; the scheduled interval identifies the booked appointment." |  |
| 031 | 1 | statement | HG-E116 2026-01-27 | group_therapy | says: no_patient_contact | 16 | "No patient treatment contact occurred." |  |
| 032 | 1 | statement | 2026-01-27 | scheduling_contact | says: no_therapy_provided | 16 | "An outreach message inviting the patient to contact scheduling was left after the group; no clinical discussion occurred." |  |
| 033 | 1 | statement | HG-E117 2026-01-28 | individual_therapy | says: other | 18 | "Appointment HG-E117 was cancelled before the scheduled start; no replacement appointment was booked within January 2026." |  |
| 034 | 1 | statement |  |  | says: other | 22 | "Break details remain in the corresponding group activity records." |  |

Coverage: 41 times, dates and record numbers in the document. 40 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 18 | number | HG-E117 | captured on another line |

### BH-D109: BH-D109_care_coordination_2026-01-23.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Care coordination | signed by Mira Patel, LCSW, 2026-01-23 10:02 |  |  | service 2026-01-23; signed 2026-01-23 10:02 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E114 2026-01-23 | care_coordination |  | 3 | "Care coordination \| Encounter HG-E114" |  |
| 002 | 1 | modality | HG-E114 2026-01-23 | care_coordination | modality: telephone | 9 | "Neither participant made an employment determination during this call." |  |
| 003 | 1 | time | HG-E114 2026-01-23 | care_coordination | end: 09:20; label: not_labelled; position: header; start: 09:00; what: contact_interval | 5 | "January 23, 2026 \| 09:00–09:20" |  |
| 004 | 1 | attendance | HG-E114 2026-01-23 | care_coordination | status: absent; status_as_written: Patient participation: None. No patient contact occurred. | 7 | "Patient participation: None. No patient contact occurred." |  |
| 005 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Mira Patel, LCSW; presence: present; role: clinician; role_as_written: LCSW | 6 | "Participants: Mira Patel, LCSW, and Daniel Shaw, outside social worker" |  |
| 006 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Daniel Shaw; presence: present; role: outside_professional; role_as_written: outside social worker | 6 | "Participants: Mira Patel, LCSW, and Daniel Shaw, outside social worker" |  |
| 007 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Rowan Mercer; presence: absent; role: patient; role_as_written: Patient | 7 | "Patient participation: None. No patient contact occurred." |  |
| 008 | 1 | participant | HG-E114 2026-01-23 | care_coordination | name: Rowan Mercer; presence: absent; role: patient | 13 | "Rowan did not join by telephone or video, and no psychotherapy was delivered to the patient during the call." |  |
| 009 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: clinician; summary: Call to coordinate practical supports for return to work; topic: reason_for_contact | 9 | "With the patient's existing release on file, discussed coordination of practical supports related to returning to work." |  |
| 010 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: outside_professional; speaker_name: Daniel Shaw; summary: Patient asked for help understanding whom to contact about gradual return schedule; topic: functioning | 9 | "The outside social worker reported that Rowan had asked for help understanding whom to contact about a gradual return schedule." |  |
| 011 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: clinician; summary: Approach of breaking difficult task into manageable first step; topic: functioning | 11 | "Reviewed the current approach of helping Rowan break a difficult task into a manageable first step." |  |
| 012 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: clinician; summary: Avoidance and coping to continue being addressed in scheduled therapy; topic: progress | 11 | "I will continue to address avoidance and coping within scheduled therapy." |  |
| 013 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: clinician; summary: No change to medication; topic: medication | 11 | "No change to medication or psychotherapy frequency was made during the coordination call." |  |
| 014 | 1 | observation | HG-E114 2026-01-23 | care_coordination | date: 2026-01-23; speaker: clinician; summary: No change to psychotherapy frequency; topic: progress | 11 | "No change to medication or psychotherapy frequency was made during the coordination call." |  |
| 015 | 1 | statement | HG-E114 2026-01-23 | care_coordination | says: no_patient_contact | 7 | "Patient participation: None. No patient contact occurred." |  |
| 016 | 1 | statement | HG-E114 2026-01-23 | care_coordination | says: no_patient_contact | 13 | "This contact was between professionals only." |  |
| 017 | 1 | statement | HG-E114 2026-01-23 | care_coordination | says: no_therapy_provided | 13 | "Rowan did not join by telephone or video, and no psychotherapy was delivered to the patient during the call." |  |
| 018 | 1 | statement | HG-E114 2026-01-23 | care_coordination | says: other | 9 | "Neither participant made an employment determination during this call." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D110: BH-D110_individual_primary_record_2026-01-26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | clinical_note | Individual psychotherapy | signed by Mira Patel, LCSW, 2026-01-26 11:16 | Final |  | service 2026-01-26; signed 2026-01-26 11:16 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E115 HG-A115 2026-01-26 | individual_therapy |  | 3 | "Individual psychotherapy \| Encounter HG-E115 \| Appointment HG-A115" |  |
| 002 | 1 | modality | HG-E115 HG-A115 2026-01-26 | individual_therapy | modality: in_person | 5 | "January 26, 2026 \| In person" |  |
| 003 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | detail: patient psychotherapy contact; end: 09:50; label: actual; position: header; start: 09:00; what: patient_present | 7 | "Actual patient psychotherapy contact: 09:00–09:50, 50 minutes." |  |
| 004 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Mira Patel; presence: not_stated; role: clinician; role_as_written: LCSW | 6 | "Clinicians: Mira Patel, LCSW; Nora Ellis, LCSW" |  |
| 005 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Nora Ellis; presence: present; role: clinician; role_as_written: LCSW | 11 | "Nora Ellis participated directly in the clinical work and helped rehearse a grounding cue to use before sending the response." |  |
| 006 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 13 | "The patient remained attentive and collaborative, although hesitant about completing the task outside the office." |  |
| 007 | 1 | stated_minutes | HG-E115 HG-A115 2026-01-26 | individual_therapy | minutes: 50; of: patient_present | 7 | "Actual patient psychotherapy contact: 09:00–09:50, 50 minutes." |  |
| 008 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: Sent message to supervisor; asked to discuss next steps; topic: functioning | 9 | "Rowan described sending a short message to the supervisor and receiving a request to discuss possible next steps." |  |
| 009 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Reply reduced uncertainty but raised worry about commitments; topic: anxiety | 9 | "The reply reduced one uncertainty but also brought up worry about being asked for commitments the patient might not be able to meet." |  |
| 010 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Continued postponing choosing a time for the conversation; topic: functioning | 9 | "Rowan continued to postpone choosing a time for the conversation." |  |
| 011 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Sleep uneven, difficulty settling with repetitive work thoughts; topic: sleep | 9 | "Sleep remained uneven, with difficulty settling on nights when work-related thoughts became repetitive." |  |
| 012 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Able to return to main request with prompting; topic: progress | 11 | "Rowan was able to return to the main request with prompting." |  |
| 013 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Attentive and collaborative, hesitant about task outside office; topic: other | 13 | "The patient remained attentive and collaborative, although hesitant about completing the task outside the office." |  |
| 014 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: No current suicidal ideation reported; topic: safety | 13 | "No current suicidal ideation was reported." |  |
| 015 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Continue work on avoidance and bedtime routine; topic: progress | 13 | "Continue work on avoidance and the bedtime routine." |  |
| 016 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Maintain scheduled treatment contact; bring draft to next visit if stuck; topic: functioning | 13 | "Discussed maintaining scheduled treatment contact during the return-to-work planning period and bringing the response draft to the next visit if the patient remained stuck." |  |
| 017 | 1 | statement | HG-E115 HG-A115 2026-01-26 | individual_therapy | says: other | 11 | "Nora Ellis participated directly in the clinical work and helped rehearse a grounding cue to use before sending the response." |  |

Coverage: 10 times, dates and record numbers in the document. 10 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D111: BH-D111_individual_second_record_2026-01-26.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-18 | clinical_note | Participating clinician psychotherapy record | signed by Nora Ellis, LCSW, 2026-01-26 12:03 | Final |  | service 2026-01-26; signed 2026-01-26 12:03 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E115 HG-A115 2026-01-26 | individual_therapy |  | 4 | "Encounter HG-E115 \| Appointment HG-A115 \| Service date January 26, 2026" |  |
| 002 | 1 | modality | HG-E115 HG-A115 2026-01-26 | individual_therapy | modality: in_person | 6 | "Service: Individual psychotherapy, in person" |  |
| 003 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: header; start: 09:10; what: patient_present | 7 | "Actual patient psychotherapy contact: 09:10–09:50, 40 minutes." |  |
| 004 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | detail: entered the treatment room; label: actual; position: body; start: 09:10; what: patient_arrival | 10 | "Rowan entered the treatment room at 09:10, when we began the session." |  |
| 005 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: body; start: 09:10; what: patient_present | 10 | "The full patient-contact interval for the encounter was 09:10–09:50." |  |
| 006 | 1 | time | HG-E115 HG-A115 2026-01-26 | individual_therapy | end: 09:50; label: actual; position: body; what: patient_departure | 14 | "The session concluded with Rowan at 09:50." |  |
| 007 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Nora Ellis, LCSW; presence: present; role: clinician; role_as_written: Clinician | 10 | "I participated directly in this individual encounter." |  |
| 008 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Mira Patel, LCSW; presence: not_stated; role: clinician; role_as_written: participating with | 8 | "Clinician: Nora Ellis, LCSW, participating with Mira Patel, LCSW" |  |
| 009 | 1 | participant | HG-E115 HG-A115 2026-01-26 | individual_therapy | name: Rowan Mercer; presence: present; role: patient | 10 | "Rowan entered the treatment room at 09:10, when we began the session." |  |
| 010 | 1 | stated_minutes | HG-E115 HG-A115 2026-01-26 | individual_therapy | minutes: 40; of: patient_present | 7 | "Actual patient psychotherapy contact: 09:10–09:50, 40 minutes." |  |
| 011 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: Difficulty moving from supervisor's reply to arranging next conversation; topic: functioning | 10 | "Rowan discussed difficulty moving from a supervisor's reply to arranging the next conversation." |  |
| 012 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: Anticipated becoming overwhelmed if several work issues raised at once; topic: anxiety | 10 | "The patient anticipated becoming overwhelmed if several work issues were raised at once." |  |
| 013 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: Recognized tendency to keep editing a message after point was clear; topic: functioning | 12 | "Rowan recognized a tendency to keep editing a message after the essential point was already clear." |  |
| 014 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Could use cue in rehearsal but uncertain about using it independently when anxious; topic: anxiety | 12 | "The patient could use the cue during the rehearsal but remained uncertain about using it independently when anxious." |  |
| 015 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Repetitive planning at night affected settling for sleep; topic: sleep | 12 | "The discussion also addressed how repetitive planning at night affected settling for sleep." |  |
| 016 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Ongoing anxiety; topic: anxiety | 14 | "Clinical presentation remained consistent with ongoing anxiety, low mood, and functional difficulty around work demands." |  |
| 017 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Low mood; topic: mood | 14 | "Clinical presentation remained consistent with ongoing anxiety, low mood, and functional difficulty around work demands." |  |
| 018 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Functional difficulty around work demands; topic: functioning | 14 | "Clinical presentation remained consistent with ongoing anxiety, low mood, and functional difficulty around work demands." |  |
| 019 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: patient; summary: Engaged with team; wishes to resume steadier routine; topic: functioning | 14 | "Rowan was engaged with the treatment team and described a wish to resume a steadier routine." |  |
| 020 | 1 | observation | HG-E115 HG-A115 2026-01-26 | individual_therapy | date: 2026-01-26; speaker: clinician; summary: Continue individual and group work under existing outpatient plan; topic: progress | 14 | "Plan is to continue individual and group work under the existing outpatient plan." |  |
| 021 | 1 | statement | HG-E115 HG-A115 2026-01-26 | individual_therapy | says: other | 10 | "I participated directly in this individual encounter." |  |

Coverage: 14 times, dates and record numbers in the document. 14 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D112: BH-D112_draft_note_and_charge_extract_2026-01-27.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-5 | cover_sheet | Administrative chart extract | not_stated |  |  | exported_or_prepared 2026-01-30 17:25; service 2026-01-27 |
| 2 | 7-16 | draft_note | AUTOGENERATED PROGRESS NOTE | unsigned | DRAFT — UNSIGNED — system populated from scheduled group template |  | created 2026-01-27 09:45 |
| 3 | 18-28 | billing_extract | POSTED CHARGE EXTRACT | not_stated |  |  | service 2026-01-27; posted 2026-01-27 18:06; other 2026-01-30; exported_or_prepared 2026-01-30 17:25 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E116 2026-01-27 | group_therapy |  | 5 | "Service date January 27, 2026 \| Encounter HG-E116" |  |
| 002 | 2 | time | HG-E116 2026-01-27 | group_therapy | end: 11:30; label: scheduled; position: header; start: 10:00; what: contact_interval | 10 | "Scheduled service: Skills group, 10:00–11:30" |  |
| 003 | 2 | attendance | HG-E116 2026-01-27 | group_therapy | status: attended; status_as_written: Patient attended the full session | 11 | "Template attendance text: Patient attended the full session and participated in the skills discussion." |  |
| 004 | 2 | participant | HG-E116 2026-01-27 | group_therapy | name: Rowan Mercer; presence: present; role: patient; role_as_written: Patient | 11 | "Template attendance text: Patient attended the full session and participated in the skills discussion." |  |
| 005 | 2 | observation | HG-E116 2026-01-27 | group_therapy | date: 2026-01-27; speaker: other; speaker_name: system template; summary: Template text: patient participated in skills discussion; topic: functioning | 11 | "Template attendance text: Patient attended the full session and participated in the skills discussion." |  |
| 006 | 2 | observation | HG-E116 2026-01-27 | group_therapy | date: 2026-01-27; speaker: other; speaker_name: system template; summary: Template plan: continue outpatient skills group; topic: progress | 12 | "Template plan text: Continue outpatient skills group according to treatment plan." |  |
| 007 | 3 | charge | HG-E116 2026-01-27 | group_therapy | charge_id: CH-116; description: Group psychotherapy; posted_date: 2026-01-27; posted_time: 18:06; quantity: 1; status_as_written: Posted; unit_as_written: group session | 19 | "Charge ID: CH-116 \| Encounter: HG-E116" |  |
| 008 | 2 | statement | HG-E116 2026-01-27 | group_therapy | says: is_draft_or_unsigned | 9 | "Status: DRAFT — UNSIGNED — system populated from scheduled group template" |  |
| 009 | 2 | statement | HG-E116 2026-01-27 | group_therapy | says: no_new_signature | 13 | "Clinician signature: None" |  |
| 010 | 2 | statement | HG-E116 2026-01-27 | group_therapy | says: other | 14 | "Manual clinical entry: None" |  |
| 011 | 2 | statement | HG-E116 2026-01-27 | group_therapy | says: made_before_the_service | 16 | "It was generated from the appointment template before the scheduled group." |  |
| 012 | 2 | statement | HG-E116 2026-01-27 | group_therapy | says: other | 16 | "No clinician attestation or finalized patient-specific narrative appears in this draft." |  |
| 013 | 3 | statement | HG-E116 2026-01-27 | group_therapy | says: other | 25 | "This administrative extract preserves the draft document fields and posted charge fields as they appeared on January 30." |  |
| 014 | 3 | statement | HG-E116 2026-01-27 | group_therapy | says: not_an_attendance_record | 25 | "The signed group attendance register is maintained in the clinical attendance section of the chart." |  |

Coverage: 19 times, dates and record numbers in the document. 18 captured, 1 captured on another line, 0 not captured, 0 quoted only.

| Line | Kind | Value | Status |
|---|---|---|---|
| 19 | number | HG-E116 | captured on another line |

### BH-D113: BH-D113_family_therapy_2026-01-30.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Family psychotherapy | signed by Mira Patel, LCSW, 2026-01-30 14:18 |  |  | service 2026-01-30; signed 2026-01-30 14:18 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E119 2026-01-30 | family_therapy |  | 3 | "Family psychotherapy \| Encounter HG-E119" |  |
| 002 | 1 | modality | HG-E119 2026-01-30 | family_therapy | modality: in_person | 5 | "In person" |  |
| 003 | 1 | time | HG-E119 2026-01-30 | family_therapy | detail: Therapist session interval; end: 13:45; label: not_labelled; position: header; start: 13:00; what: contact_interval | 6 | "Therapist session interval: 13:00–13:45, 45 minutes." |  |
| 004 | 1 | time | HG-E119 2026-01-30 | family_therapy | detail: Partner only; end: 13:15; label: not_labelled; position: header; start: 13:00; what: patient_absent_interval | 7 | "Partner only: 13:00–13:15." |  |
| 005 | 1 | time | HG-E119 2026-01-30 | family_therapy | detail: Rowan present with partner; end: 13:45; label: not_labelled; position: header; start: 13:15; what: patient_present | 7 | "Rowan present with partner: 13:15–13:45, 30 minutes." |  |
| 006 | 1 | time | HG-E119 2026-01-30 | family_therapy | label: actual; position: body; start: 13:15; what: patient_arrival | 11 | "Rowan joined at 13:15 and participated through the end of the session." |  |
| 007 | 1 | attendance | HG-E119 2026-01-30 | family_therapy | status: attended_part; status_as_written: Rowan joined at 13:15 and participated through the end of the session. | 11 | "Rowan joined at 13:15 and participated through the end of the session." |  |
| 008 | 1 | participant | HG-E119 2026-01-30 | family_therapy | name: Rowan Mercer; presence: present_part; role: patient | 9 | "Rowan was not present for that portion." |  |
| 009 | 1 | participant | HG-E119 2026-01-30 | family_therapy | name: Casey Mercer; presence: present; role: family_or_partner; role_as_written: partner | 9 | "Rowan's partner, Casey Mercer, arrived first." |  |
| 010 | 1 | participant | HG-E119 2026-01-30 | family_therapy | name: Mira Patel, LCSW; presence: not_stated; role: clinician; role_as_written: Clinician | 5 | "Clinician: Mira Patel, LCSW" |  |
| 011 | 1 | stated_minutes | HG-E119 2026-01-30 | family_therapy | minutes: 45; of: contact_total | 6 | "Therapist session interval: 13:00–13:45, 45 minutes." |  |
| 012 | 1 | stated_minutes | HG-E119 2026-01-30 | family_therapy | minutes: 30; of: patient_present | 7 | "Rowan present with partner: 13:15–13:45, 30 minutes." |  |
| 013 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: family_or_partner; speaker_name: Casey Mercer; summary: Partner uncertain when reminders help vs increase pressure; topic: other | 9 | "Casey described uncertainty about when reminders helped and when they seemed to increase Rowan's sense of pressure." |  |
| 014 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Pattern: reminder about contacting work leads to withdrawal from task; topic: functioning | 11 | "Together, they identified a recurring pattern in which a reminder about contacting work led to a lengthy discussion, followed by Rowan withdrawing from the task." |  |
| 015 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Patient practiced requesting specific help; topic: functioning | 11 | "Rowan practiced requesting a specific kind of help and naming when a reminder felt overwhelming." |  |
| 016 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Agreed to one brief planned check-in; topic: functioning | 13 | "Both participants agreed to try one brief check-in at a planned time rather than repeated questions across the evening." |  |
| 017 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Remained anxious about work conversation; topic: anxiety | 13 | "Rowan remained anxious about the work conversation but could explain the intended first step." |  |
| 018 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Could explain intended first step; topic: functioning | 13 | "Rowan remained anxious about the work conversation but could explain the intended first step." |  |
| 019 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: patient; summary: Limited plan felt more manageable; topic: functioning | 13 | "The patient reported that having a limited plan felt more manageable." |  |
| 020 | 1 | observation | HG-E119 2026-01-30 | family_therapy | date: 2026-01-30; speaker: clinician; summary: Continue current outpatient treatment plan; topic: progress | 13 | "Continue the current outpatient treatment plan and revisit whether the agreed communication pattern was useful." |  |
| 021 | 1 | statement | HG-E119 2026-01-30 | family_therapy | says: other | 9 | "Rowan was not present for that portion." |  |

Coverage: 14 times, dates and record numbers in the document. 14 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D114: BH-D114_medication_management_2026-01-30.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-16 | clinical_note | Medication management | signed by Elena Ortiz, PMHNP, 2026-01-30 16:02 | Final |  | service 2026-01-30; signed 2026-01-30 16:02 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | HG-E120 2026-01-30 | medication_management |  | 3 | "Medication management \| Encounter HG-E120" |  |
| 002 | 1 | time | HG-E120 2026-01-30 | medication_management | end: 15:20; label: not_labelled; position: header; start: 15:00; what: contact_interval | 5 | "January 30, 2026 \| 15:00–15:20 \| Completed, 20 minutes" |  |
| 003 | 1 | attendance | HG-E120 2026-01-30 | medication_management | status: completed; status_as_written: Completed | 5 | "Completed, 20 minutes" |  |
| 004 | 1 | participant | HG-E120 2026-01-30 | medication_management | name: Elena Ortiz; presence: not_stated; role: clinician; role_as_written: Prescriber | 6 | "Prescriber: Elena Ortiz, PMHNP" |  |
| 005 | 1 | participant | HG-E120 2026-01-30 | medication_management | name: Rowan Mercer; presence: not_stated; role: patient | 8 | "Rowan reported taking the medication as prescribed and did not describe a new adverse effect." |  |
| 006 | 1 | stated_minutes | HG-E120 2026-01-30 | medication_management | minutes: 20; of: contact_total | 5 | "Completed, 20 minutes" |  |
| 007 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: patient; summary: Taking medication as prescribed, no new adverse effect; topic: medication | 8 | "Rowan reported taking the medication as prescribed and did not describe a new adverse effect." |  |
| 008 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Mood less persistently low than earlier in month; topic: mood | 8 | "Mood felt less persistently low than earlier in the month" |  |
| 009 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Anxiety noticeable when anticipating contact with work; topic: anxiety | 8 | "although anxiety remained noticeable when anticipating contact with work" |  |
| 010 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Sleep still variable; topic: sleep | 8 | "Sleep was still variable." |  |
| 011 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Alert, organized, able to describe follow-up plan; topic: functioning | 10 | "Rowan was alert, organized in conversation, and able to describe the follow-up plan." |  |
| 012 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: patient; summary: Denied current suicidal thoughts; topic: safety | 10 | "The patient denied current suicidal thoughts." |  |
| 013 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: No new acute safety issue; topic: safety | 10 | "No new acute safety issue emerged in this visit." |  |
| 014 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Continue current regimen, monitor sleep and tolerability; topic: medication | 10 | "Discussed continuing the current medication regimen, monitoring sleep and tolerability, and contacting the clinic if a concerning change occurred before the next prescriber appointment." |  |
| 015 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: No medication change made; topic: medication | 10 | "No medication change was made today." |  |
| 016 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Psychotherapy goals remain with treating therapist; topic: progress | 12 | "Ongoing psychotherapy goals and behavioral assignments remain with the treating therapist." |  |
| 017 | 1 | observation | HG-E120 2026-01-30 | medication_management | date: 2026-01-30; speaker: clinician; summary: Agreed to continue attending follow-up and bring medication questions; topic: functioning | 12 | "Rowan agreed to continue attending scheduled outpatient follow-up and to bring questions about the medication regimen to the next medication appointment." |  |
| 018 | 1 | statement | HG-E120 2026-01-30 | medication_management | says: no_therapy_provided | 12 | "No separately documented psychotherapy was provided." |  |
| 019 | 1 | statement | HG-E120 2026-01-30 | medication_management | says: other | 12 | "The service consisted of medication evaluation and management, including symptom review and medication counseling." |  |

Coverage: 9 times, dates and record numbers in the document. 9 captured, 0 captured on another line, 0 not captured, 0 quoted only.

### BH-D115: BH-D115_symptom_measure_review_2026-01-30.txt

- Patient: Rowan Mercer, born 1991-04-12, record number HG-M042
- Read by fable, effort low, prompt version 3

| Section | Lines | Kind | As written | Signature | Status | Copy | Dates |
|---|---|---|---|---|---|---|---|
| 1 | 1-17 | questionnaire_review | Symptom questionnaire and chart review | signed by Mira Patel, LCSW, 2026-01-30 16:20 |  |  | completed 2026-01-30 12:42; reviewed 2026-01-30; signed 2026-01-30 16:20 |

| # | Sec | Type | Contact | Class | Value | Line | Quote | Flags |
|---|---|---|---|---|---|---|---|---|
| 001 | 1 | contact | 2026-01-30 |  |  | 8 | "Rowan completed the questionnaire before the afternoon appointment." |  |
| 002 | 1 | score |  |  | completed_date: 2026-01-30; completed_time: 12:42; instrument: PHQ-9; relation: completion; score: 10 | 6 | "PHQ-9 total: 10." |  |
| 003 | 1 | score |  |  | completed_date: 2026-01-30; completed_time: 12:42; instrument: PHQ-9; item_number: 9; relation: completion; score: 0 | 6 | "Item 9: 0." |  |
| 004 | 1 | observation |  |  | date: 2026-01-30; speaker: patient; summary: Continued to endorse sleep difficulty; topic: sleep | 8 | "The patient continued to endorse sleep difficulty" |  |
| 005 | 1 | observation |  |  | date: 2026-01-30; speaker: patient; summary: Trouble sustaining usual activities; topic: functioning | 8 | "trouble sustaining usual activities" |  |
| 006 | 1 | observation |  |  | date: 2026-01-30; speaker: patient; summary: Fewer days of pervasive low mood than at intake; topic: mood | 8 | "with fewer days of pervasive low mood than reported at intake" |  |
| 007 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: Partial improvement; topic: progress | 10 | "Rowan shows partial improvement" |  |
| 008 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: Persistent avoidance and functional impact around returning to work; topic: functioning | 10 | "with persistent avoidance and meaningful functional impact around returning to work" |  |
| 009 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: Took initial steps (drafted and sent a message) but delays follow-up; topic: functioning | 10 | "The patient has taken some initial steps, including drafting and sending a message, but continues to delay follow-up" |  |
| 010 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: Becomes anxious when task expands beyond narrow action; topic: anxiety | 10 | "becomes anxious when a task expands beyond a narrowly defined action" |  |
| 011 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: Sleep disruption an intermittent barrier to daytime routine; topic: sleep | 10 | "Sleep disruption remains an intermittent barrier to establishing a steadier daytime routine." |  |
| 012 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: Continued treatment appropriate given remaining difficulties; topic: progress | 12 | "Continued treatment is appropriate given the remaining difficulties with follow-through and work-related functioning." |  |
| 013 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: Recommend continuing individual and group schedule and approach tasks; topic: progress | 12 | "Recommend continuity of the established individual and group schedule and continued use of small, observable approach tasks." |  |
| 014 | 1 | observation |  |  | date: 2026-01-30; speaker: clinician; summary: Family support may help with agreed tasks between appointments; topic: other | 12 | "Family support may help the patient carry out the agreed tasks between appointments." |  |
| 015 | 1 | statement |  |  | says: other | 8 | "The form was available to the treating clinician for review with the patient's account of functioning." |  |
| 016 | 1 | statement |  |  | says: not_a_visit | 14 | "This entry records questionnaire review within ongoing care and is not a separate treatment appointment." |  |
| 017 | 1 | statement |  |  | says: no_patient_contact | 14 | "No additional patient-contact interval is claimed in this entry." |  |

Coverage: 8 times, dates and record numbers in the document. 8 captured, 0 captured on another line, 0 not captured, 0 quoted only.

