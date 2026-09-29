# Answer key

What the system's output is compared against. Written by hand from the 31 source documents, the 36 confirmed decisions and the 16 rules in `decisions.md`. No code and no model run produced anything in this file.

**Status:** fixed on 2026-09-29. You checked the six marked rows and confirmed the key (R-44 in `discussions.md`). Any later change is logged in `discussions.md` before it is made.

**Verification, 2026-09-29:**

- All 136 quotes were compared with their cited lines and match exactly.
- You checked the six rows marked **Check**.
- Six speaker labels in section 7 follow D-35, which you confirmed.
- P-9, the Jan 19 reason, the safety table and the header times (D-36) were changed as you decided. See Discussion 19 in `discussions.md`.
- The three points of wording were changed as you decided. No point from the verification is open.

**How to check it**

- Rows marked **Check** decide a weekly verdict. There are six. Compare each against the cited lines.
- Every citation gives the document ID and the line number. Where a quote follows, it is the exact wording on that line.
- File names for each document ID are in section 1.

**Limit:** this key was made by the same reading that shaped the rules. It cannot catch a mistake that both share.

Contents

1. Documents
2. Plan rules
3. Contacts
4. Conflicts and findings
5. Assessments
6. Weekly status and totals
7. The five answers
8. Problem questions and related questions
9. What this key does not cover

---

## 1. Documents

| ID | File | Kind | Signed |
|---|---|---|---|
| D001 | group_authorization_letter.txt | Authorization, with a desk entry added | No |
| D002 | intake_and_individual_jan05.txt | Clinical note | Yes, Jan 5, 12:18 |
| D003 | signed_treatment_plan_jan05.txt | Plan | Yes, Jan 5, 13:05 |
| D004 | group_facilitator_jan06.txt | Clinical note | Yes, Jan 6, 12:02 |
| D005 | early_group_attendance_roster.txt | Attendance record (desk extract) | No; prepared from a signed sheet |
| D006 | early_appointment_status_export.txt | Schedule export | No |
| D007 | family_primary_jan09.txt | Clinical note | Yes, Jan 9, 16:24 |
| D008 | family_cofacilitator_jan09.txt | Clinical note | Yes, Jan 10, 08:42 |
| D009 | group_facilitator_jan12.txt | Clinical note | Yes, Jan 12, 12:20 |
| D010 | medication_review_jan13.txt | Clinical note | Yes, Jan 13, 10:04 |
| D011 | individual_therapy_jan14.txt | Clinical note | Yes, Jan 14, 13:16 |
| D012 | partner_collateral_jan16.txt | Clinical note | Yes, Jan 16, 16:08 |
| D013 | symptom_measure_review_jan16.txt | Questionnaire review | Reviewed, Jan 16, 09:10 |
| D014 | imported_measure_summary_received_jan26.txt | Import | No |
| D015 | missed_visit_outreach_jan08.txt | Scheduling log | No |
| D016 | group_cancellation_notice_jan15.txt | Cancellation notice | No |
| D101 | BH-D101_group_content_2026-01-19.txt | Clinical note | Yes, Jan 19, 12:08 |
| D102 | BH-D102_original_attendance_2026-01-19.txt | Attendance record | Yes, Jan 19, 12:14 |
| D103 | BH-D103_attendance_correction_2026-01-20.txt | Correction | Yes, Jan 20, 08:42 |
| D104 | BH-D104_resent_roster_received_2026-01-26.txt | Copy of D102 | No new signature |
| D105 | BH-D105_individual_2026-01-19.txt | Clinical note | Yes, Jan 19, 12:32 |
| D106 | BH-D106_telehealth_2026-01-21.txt | Clinical note, with a platform export | Yes, Jan 21, 15:04 |
| D107 | BH-D107_group_activity_records_2026-01-22_and_29.txt | Clinical notes for two dates | Yes, Jan 22, 12:06 and Jan 29, 12:11 |
| D108 | BH-D108_final_attendance_and_cancellation_register.txt | Attendance record (extract) | Three entries signed; one entered by desk staff |
| D109 | BH-D109_care_coordination_2026-01-23.txt | Clinical note | Yes, Jan 23, 10:02 |
| D110 | BH-D110_individual_primary_record_2026-01-26.txt | Clinical note | Yes, Jan 26, 11:16 |
| D111 | BH-D111_individual_second_record_2026-01-26.txt | Clinical note | Yes, Jan 26, 12:03 |
| D112 | BH-D112_draft_note_and_charge_extract_2026-01-27.txt | Draft note, and a billing extract | No |
| D113 | BH-D113_family_therapy_2026-01-30.txt | Clinical note | Yes, Jan 30, 14:18 |
| D114 | BH-D114_medication_management_2026-01-30.txt | Clinical note | Yes, Jan 30, 16:02 |
| D115 | BH-D115_symptom_measure_review_2026-01-30.txt | Questionnaire review | Yes, Jan 30, 16:20 |

Patient in all 31: Rowan Mercer, date of birth 1991-04-12, record number HG-M042.

---

## 2. Plan rules

All read from D003. None is typed into code.

| Value | Expected | Source |
|---|---|---|
| Episode | 2026-01-05 to 2026-01-30 | D003 line 6: "Episode dates: 2026-01-05 through 2026-01-30" |
| Signed | Jan 5, 13:05, by Mara Voss | D003 line 7: "signed 2026-01-05, 13:05 local" |
| Patient agreement | Jan 5, 13:12 | D003 line 8: "Patient agreement recorded 2026-01-05, 13:12 local" |
| Days required | At least 3 therapy days each week | D003 line 12: "at least 3 therapy days and at least 150 minutes of patient-present therapy in each Monday–Sunday week" |
| Minutes required | At least 150 each week | Same line |
| Week | Monday to Sunday | Same line |
| Therapy day | A calendar day with individual, group or family therapy | D003 line 12: "A therapy day is a calendar day on which Rowan participates in individual, group, or family psychotherapy." |
| Counted classes | Individual, group and family therapy, with the patient present | D003 line 12: "Patient-present individual, group, and family therapy contribute to the minute goal." |
| Excluded classes | Medication management, collateral-only contacts, care coordination | D003 line 12: "Medication management, contacts with collateral informants only, and care coordination do not contribute." |
| Amendments | None in the record | |

**The plan's three clinical goals** (used in the answer to DEV-05)

| Goal | Source |
|---|---|
| 1. Daily activity and task initiation | D003 line 14: "Goal 1: improve daily activity and task initiation." |
| 2. Coping with anxiety and disrupted sleep | D003 line 16: "Goal 2: improve coping with anxiety and disrupted sleep." |
| 3. A workable return to employment | D003 line 18: "Goal 3: support a workable return to employment." |

---

## 3. Contacts

20 encounters, HG-E101 to HG-E120. 16 were held. Rowan was present at 14. 12 count as therapy.

**Columns**

| Column | Meaning |
|---|---|
| Present | The interval Rowan was present, from actual times |
| Removed | Intervals a document says had no therapy |
| Minutes | Rowan's counted minutes |
| Counts | Whether the contact counts toward the goal under the plan |

### Week 1: Jan 5 to Jan 11

| Encounter | Date | Class | Status | Present | Removed | Minutes | Counts | |
|---|---|---|---|---|---|---|---|---|
| HG-E101 | Jan 5 | Individual therapy | Held | 09:00–09:50 | None | 50 | Yes | |
| HG-E102 | Jan 6 | Group therapy | Held, attended in part | 10:15–11:15 | 10:45–11:00 | 45 | Yes | **Check** |
| HG-E103 | Jan 8 | Individual therapy | Not held: no-show | None | | 0 | No | |
| HG-E104 | Jan 9 | Family therapy | Held | 14:00–14:45 | None | 45 | Yes | |

Calculation for HG-E102: 10:15 to 10:45 is 30, and 11:00 to 11:15 is 15. Total 45.

**Sources**

- HG-E101
  - D002 line 8: "Patient-present individual therapy: 09:00–09:50 local; completed, 50 minutes."
  - D002 line 7: "Clinician: Mara Voss, LCSW"
  - D006 line 10: "Individual therapy"
- HG-E102
  - D005 line 10: "Attended part". The same line gives arrival 10:15 and departure 11:15.
  - D004 line 12: "The whole group took a break from 10:45 to 11:00. No therapy was conducted during that interval."
  - D005 line 13: "Departure was marked when Rowan returned their visitor badge."
  - D004 line 7: "Facilitator: Leena Park, LPC"
  - D004 does not mention the late arrival or the early departure.
- HG-E103
  - D015 line 11: "Appointment marked no show. Rowan was not seen for the scheduled individual visit."
  - D015 line 17: "No therapy intervention was conducted."
  - D006 line 12: "No show"
- HG-E104
  - D007 line 9: "Patient-present family therapy duration: 45 minutes"
  - D008 line 8: "both present for the full 45 minutes"
  - D007 line 8: "Clinicians: Mara Voss, LCSW; cofacilitator Leena Park, LPC"
  - Two notes, one session (rule 1). Both carry encounter HG-E104.

### Week 2: Jan 12 to Jan 18

| Encounter | Date | Class | Status | Present | Removed | Minutes | Counts | |
|---|---|---|---|---|---|---|---|---|
| HG-E105 | Jan 12 | Group therapy | Held | 10:00–11:30 | 10:40–10:55 | 75 | Yes | |
| HG-E106 | Jan 13 | Medication management | Held | 09:00–09:25 | None | 25, not counted | No | |
| HG-E107 | Jan 14 | Individual therapy | Held | 11:00–11:45 | None | 45 | Yes | |
| HG-E108 | Jan 15 | Group therapy | Not held: cancelled by the clinic | None | | 0 | No | |
| HG-E109 | Jan 16 | Collateral contact | Held, patient absent | None | | 0 for Rowan; 40 with the partner | No | **Check** |

Calculation for HG-E105: 10:00 to 10:40 is 40, and 10:55 to 11:30 is 35. Total 75.

**Sources**

- HG-E105
  - D005 line 11: "Attended full". The same line gives arrival 10:00 and departure 11:30.
  - D005 line 15: "Rowan checked in before the group began and remained until the group was released."
  - D009 line 12: "Group break: 10:40–10:55; no therapeutic activity occurred during the break."
- HG-E106
  - D010 line 7: "Actual visit 09:00–09:25 local; completed, 25 minutes"
  - D010 line 17: "No separate psychotherapy component was provided or documented."
  - D006 line 15 marks it "Completed". A schedule status does not make it therapy.
- HG-E107
  - D011 line 7: "Patient-present session 11:00–11:45 local; completed, 45 minutes"
- HG-E108
  - D016 line 9: "cancelled by the clinic because of staff illness"
  - D016 line 15: "No group was held and no participants were seen for HG-E108."
- HG-E109
  - D012 line 8: "Rowan was absent for the entire contact."
  - D012 line 17: "No patient-present psychotherapy occurred during this contact."
  - D006 line 20: "Appointment HG-E109 was retained as a partner collateral contact after Rowan could not attend."
  - D006 line 18 marks it "Completed". It is recorded as held with the patient absent, not as a missed appointment (rule 4).
  - D012 line 6: "14:00–14:40 local". The note states no duration. The header time is taken as actual (D-36).

### Week 3: Jan 19 to Jan 25

| Encounter | Date | Class | Status | Present | Removed | Minutes | Counts | |
|---|---|---|---|---|---|---|---|---|
| HG-E110 | Jan 19 | Group therapy | Held, left early | 10:00–11:15 | 10:45–11:00 | 60 | Yes | |
| HG-E111 | Jan 19 | Individual therapy | Held; added the same day | 11:15–11:45 | None | 30 | Yes | |
| HG-E112 | Jan 21 | Individual therapy, by video | Held | 13:00–13:20 and 13:30–13:55 | 13:20–13:30 | 45 | Yes | **Check** |
| HG-E113 | Jan 22 | Group therapy | Held, arrived late | 10:30–11:30 | 10:45–11:00 | 45 | Yes | |
| HG-E114 | Jan 23 | Care coordination | Held, no patient | None | | 0 for Rowan; 20 between professionals | No | |

Calculations:

- HG-E110: 10:00 to 10:45 is 45, and 11:00 to 11:15 is 15. Total 60.
- HG-E112: 13:00 to 13:20 is 20, and 13:30 to 13:55 is 25. Total 45.
- HG-E113: 10:30 to 10:45 is 15, and 11:00 to 11:30 is 30. Total 45.

**Sources**

- HG-E110
  - D103 line 7: "Patient departure for HG-E110 is 11:15, replacing the original roster value of 11:30. Patient arrival remains 10:00."
  - D102 line 9: "Patient departure: 11:30". Replaced by the correction (rule 8).
  - D104 line 20: "This is a retransmission of the January 19 roster for HG-E110. The received copy contains no new clinician signature and records no additional visit."
  - D101 line 6: "Scheduled group: 10:00–11:30. Nontherapeutic break: 10:45–11:00."
  - Four documents, one session (rule 1).
- HG-E111
  - D105 line 6: "Patient contact: 11:15–11:45"
  - D105 line 9: "This visit was added because Rowan became anxious during group and needed individual grounding and review of coping strategies."
  - D105 line 7: "Clinician: Mira Patel, LCSW"
  - A separate session from the group: its own encounter number and a different clinician (rule 1).
- HG-E112
  - D106 line 7: "Patient contact occurred 13:00–13:20 and 13:30–13:55."
  - D106 line 7: "there was no therapeutic contact during that interval"
  - D106 line 7: "Total patient psychotherapy contact: 45 minutes."
  - D106 line 7: "The reconnection continued the same clinical encounter under original appointment HG-A112."
  - D106 line 19: "Second call reason: Rejoin original appointment after network disconnect."
  - Two calls, one session (rule 1). Video counts as present (rule 4).
- HG-E113
  - D108 line 14: "Rowan arrived at 10:30 and remained until the group closed."
  - D107 line 8: "Scheduled group 10:00–11:30. Nontherapeutic break 10:45–11:00."
- HG-E114
  - D109 line 7: "Patient participation: None. No patient contact occurred."
  - D109 line 6: "Participants: Mira Patel, LCSW, and Daniel Shaw, outside social worker"
  - D109 line 5: "09:00–09:20". The note states no duration. The header time is taken as actual (D-36).

### Week 4: Jan 26 to Feb 1

| Encounter | Date | Class | Status | Present | Removed | Minutes | Counts | |
|---|---|---|---|---|---|---|---|---|
| HG-E115 | Jan 26 | Individual therapy | Held | 09:00–09:50 or 09:10–09:50 | None | 50 or 40 | Yes | **Check** |
| HG-E116 | Jan 27 | Group therapy | Not held for Rowan: no-show | None | | 0 | No | **Check** |
| HG-E117 | Jan 28 | Individual therapy | Not held: cancelled by the patient | None | | 0 | No | |
| HG-E118 | Jan 29 | Group therapy | Held | 10:00–11:30 | 10:45–11:00 | 75 | Yes | |
| HG-E119 | Jan 30 | Family therapy | Held, patient present for part | 13:15–13:45 | None | 30 | Yes | **Check** |
| HG-E120 | Jan 30 | Medication management | Held | 15:00–15:20 | None | 20, not counted | No | |

Calculation for HG-E118: 10:00 to 10:45 is 45, and 11:00 to 11:30 is 30. Total 75.

**Sources**

- HG-E115
  - D110 line 7: "Actual patient psychotherapy contact: 09:00–09:50, 50 minutes."
  - D111 line 7: "Actual patient psychotherapy contact: 09:10–09:50, 40 minutes."
  - D111 line 10: "Rowan entered the treatment room at 09:10, when we began the session."
  - D110 line 6: "Clinicians: Mira Patel, LCSW; Nora Ellis, LCSW"
  - Two notes, one session (rule 1). The start time is an open conflict (section 4).
- HG-E116
  - D108 line 16: "Final roster confirms Rowan was absent for the entire group. No patient treatment contact occurred."
  - D108 line 10: "No show; patient did not attend"
  - D112 line 9: "Status: DRAFT — UNSIGNED — system populated from scheduled group template"
  - D112 line 11: "Template attendance text: Patient attended the full session and participated in the skills discussion."
  - A draft and a charge cannot establish attendance (rule 10).
- HG-E117
  - D108 line 11: "Patient cancelled before appointment"
  - D108 line 18: "Cancellation received from patient January 28, 08:12."
  - D108 line 18: "Entered by Ana Reed, January 28, 08:18."
- HG-E118
  - D108 line 20: "Rowan was present from opening through closing."
  - D107 line 13: "Scheduled group 10:00–11:30. Nontherapeutic break 10:45–11:00."
- HG-E119
  - D113 line 7: "Partner only: 13:00–13:15. Rowan present with partner: 13:15–13:45, 30 minutes."
  - D113 line 6: "Therapist session interval: 13:00–13:45, 45 minutes."
  - D113 line 9: "Rowan was not present for that portion."
- HG-E120
  - D114 line 5: "Completed, 20 minutes"
  - D114 line 12: "No separately documented psychotherapy was provided."

### Records that are not contacts

| Record | Date | Why it is not a contact | Source |
|---|---|---|---|
| Questionnaire review | Jan 16 | No appointment took place | D013 line 15: "no clinical appointment occurred at the time of review" |
| Questionnaire review | Jan 30 | Not a separate appointment | D115 line 14: "not a separate treatment appointment" |
| Import of a result | Received Jan 26 | Administrative | D014 line 19: "does not document a visit with Rowan" |
| Two phone calls | Jan 8 | Scheduling only | D015 line 17: "The callback addressed scheduling and contact information." |
| One phone call | Jan 15 | Confirming the cancellation | D016 line 15: "The telephone contact was limited to confirming the cancellation and upcoming appointment information." |
| Outreach message | Jan 27 | No clinical discussion | D108 line 16: "no clinical discussion occurred" |
| Attendance correction | Entered Jan 20 | No service | D103 line 13: "No additional clinical service was provided in making this correction." |
| Authorization | Received Jan 4 | Not a record of attendance | D001 line 15: "No service attendance record accompanies this letter." |

---

## 4. Conflicts and findings

### Conflicts

| # | Contact | Field | Values | Outcome | Rule |
|---|---|---|---|---|---|
| C-1 | HG-E110, Jan 19 | Departure | 11:30 (D102, and its copy D104); 11:15 (D103) | Settled: 11:15 | 8, then 9 |
| C-2 | HG-E115, Jan 26 | Start | 09:00 (D110); 09:10 (D111) | Open: 40 or 50 minutes | 11 |
| C-3 | HG-E116, Jan 27 | Attendance | Absent (D108, signed); attended (D112 draft) | Settled: did not attend | 10 |

**C-1 in detail**

- D103 is signed, names the contact, the field and the old value, and gives the reason.
  - D103 line 9: "the original group roster was found to retain the scheduled group closing time in Rowan's departure field"
  - D103 line 15: "Electronically signed: Leah Chen, LCSW | January 20, 2026, 08:42"
- D104 is a copy of D102. Its only signature is the original one.
  - D104 line 8: "No correction sheet was included in this transmission."
- D105 supports 11:15 independently. It has a different author and was signed on Jan 19, before the correction.
  - D105 line 9: "Rowan came directly from the group room."
- The order in which the four documents arrive must not change the result.
- Limit: D103 line 9 relies on a "room-transfer record" that is not among the supplied documents.

**C-2 in detail**

- Both notes are signed and final. Neither corrects the other.
- Established: Rowan was in session from 09:10 to 09:50. 40 minutes is agreed.
- In dispute: 09:00 to 09:10.
- D111 records an observed arrival. D110 names no arrival or start event.
- No document gives a scheduled time for this appointment.
- What would settle it: an arrival or check-in record, or a correction by the author of the note being changed.

**C-3 in detail**

- The draft was created before the session it describes.
  - D112 line 8: "Creation time: January 27, 2026, 09:45"
  - D112 line 10: "Scheduled service: Skills group, 10:00–11:30"
  - D112 line 16: "No clinician attestation or finalized patient-specific narrative appears in this draft."
- The signed attendance entry is D108 line 16, signed by Leah Chen on Jan 27 at 11:54.

### Findings

| # | Finding | Required | Source |
|---|---|---|---|
| F-1 | A group therapy charge (CH-116) is posted for HG-E116, which the signed attendance entry records as a no-show | Yes | D112 line 22: "Quantity charged: 1 group session" |
| F-2 | A draft note for HG-E116 was created before the session began | No | D112 line 8 |
| F-3 | The second note for HG-E104 was signed the day after the service | No | D008 line 9: "Signed 2026-01-10, 08:42 local" |

Wording expected for F-1: an inconsistency between documentation and billing. The record does not show whether the charge was later reviewed or reversed. It is not a finding of improper billing.

"Required: No" means the system may report it, and the key does not fail the system if it does not.

---

## 5. Assessments

Three distinct assessments, all PHQ-9.

| # | Completed | Score | Form ID | Source |
|---|---|---|---|---|
| A-1 | Jan 5, time not stated | 18 | None | D002 line 15: "PHQ-9 completed by Rowan on 2026-01-05: total score 18." |
| A-2 | Jan 16, 08:17 | 14 | HG-Q116 | D013 line 7: "Completed by patient: 2026-01-16, 08:17 local" and D013 line 8: "Total score: 14" |
| A-3 | Jan 30, 12:42 | 10 | None | D115 line 6: "PHQ-9 total: 10. Item 9: 0." |

| Measure | Value |
|---|---|
| Change, A-1 to A-2 | 4 points lower |
| Change, A-2 to A-3 | 4 points lower |
| Change overall | 8 points lower |
| Item scores | Only item 9 on Jan 30, which is 0 |

**Records that are not assessments**

| Record | Why | Source |
|---|---|---|
| The score of 18 mentioned in D013 | A mention of A-1 | D013 line 11: "lower than the intake score of 18 recorded on January 5" |
| The score of 14 in D014 | A copy of A-2, received Jan 26 | D014 line 17: "No newly completed patient questionnaire is included in this batch." |
| The questionnaire mentioned in D114 | A reference to A-3 | D114 line 8: "the symptom questionnaire available in the chart" |

Counting D014 as a fourth assessment would give 18, 14, 14, 10, which is wrong.

No anxiety measure exists in the record.

---

## 6. Weekly status and totals

### Weekly status

| Week | Therapy days | Dates | Minutes | Calculation | Verdict | Margin |
|---|---|---|---|---|---|---|
| Jan 5–11 | 3 | Jan 5, 6, 9 | 140 | 50 + 45 + 45 | Not met | 10 minutes short |
| Jan 12–18 | 2 | Jan 12, 14 | 120 | 75 + 45 | Not met | 1 day and 30 minutes short |
| Jan 19–25 | 3 | Jan 19, 21, 22 | 180 | 60 + 30 + 45 + 45 | Met | 30 minutes over |
| Jan 26–Feb 1 | 3 | Jan 26, 29, 30 | 145 or 155 | (40 or 50) + 75 + 30 | Cannot determine | 5 short or 5 over |

- Week 4 depends on conflict C-2.
- Week 4 is partial. The episode ends on Friday Jan 30, and the full requirement still applies.
- No document covers Jan 17–18, Jan 24–25 or Jan 31–Feb 1. Verdicts are on the documented record.

### Totals for Jan 5 to Jan 30

| Measure | Value | Calculation |
|---|---|---|
| Sessions | 12 | 3 + 2 + 4 + 3 |
| Individual | 5 | Jan 5, 14, 19, 21, 26 |
| Group | 5 | Jan 6, 12, 19, 22, 29 |
| Family | 2 | Jan 9, 30 |
| Therapy days | 11 | Jan 19 has two sessions |
| Minutes | 585 or 595 | 140 + 120 + 180 + (145 or 155) |
| Hours | 9.75 or 9.92 | Minutes divided by 60 |
| Individual minutes | 210 or 220 | 50 + 45 + 30 + 45 + (40 or 50) |
| Group minutes | 300 | 45 + 75 + 60 + 45 + 75 |
| Family minutes | 75 | 45 + 30 |

### Hours by week

| Week | Minutes | Hours |
|---|---|---|
| Jan 5–11 | 140 | 2.33 |
| Jan 12–18 | 120 | 2.00 |
| Jan 19–25 | 180 | 3.00 |
| Jan 26–Feb 1 | 145 or 155 | 2.42 or 2.58 |

### The 8 encounters that did not count

| Reason | Encounters |
|---|---|
| No-show | HG-E103 (Jan 8), HG-E116 (Jan 27) |
| Cancelled by the patient | HG-E117 (Jan 28) |
| Cancelled by the clinic | HG-E108 (Jan 15) |
| Medication management | HG-E106 (Jan 13), HG-E120 (Jan 30) |
| Held with the patient absent | HG-E109 (Jan 16) |
| Professionals only | HG-E114 (Jan 23) |

---

## 7. The five answers

Each answer has the nine parts agreed in Discussion 18. Part 9, the version, is set when the system runs and is not in this key. Source lines for every contact are in section 3.

### DEV-01

> For January 5–30, 2026, how many therapy sessions did Rowan attend, by service type and in total, and on how many distinct days? Provide a reviewable abstraction with source support and explain records that could lead to duplicate or ineligible counts.

| Part | Expected |
|---|---|
| 1. Question as understood | Rowan Mercer, HG-M042. Jan 5 to Jan 30, 2026. "Therapy session" means individual, group or family therapy with Rowan present, as the plan defines it |
| 2. Answer | 12 sessions on 11 distinct days: 5 individual, 5 group, 2 family |
| 3. Figures | 3 + 2 + 4 + 3 = 12 sessions. Jan 19 has two sessions, so 11 days |
| 4. What contributed | The 12 counted contacts in section 3, each with its sources |
| 5. What was excluded | The 8 encounters in section 6, and the records in the table below |
| 6. Not settled | Nothing that changes a count. The Jan 26 start time is open, and it affects minutes only |
| 7. Assumptions | The count covers the documented record. Partial attendance still counts as a session. Video counts as present. The Jan 5 session counts although the plan was signed later that day |
| 8. Documents not read | None |

**Records that could lead to a duplicate count**

| Record | Risk |
|---|---|
| D007 and D008 | Two notes for one family session on Jan 9 |
| D110 and D111 | Two notes for one individual session on Jan 26 |
| D101, D102, D103, D104 | Four documents for one group session on Jan 19 |
| D104 | A copy received on Jan 26. It records no new visit |
| D106 | Two video calls under one appointment on Jan 21 |
| D005, D006, D107, D108 | Each covers several dates, so the same session appears in more than one document |
| D013 and D014 | The same questionnaire result in two documents |

**Records that could lead to an ineligible count**

| Record | Risk |
|---|---|
| D112, draft | Says "attended the full session", but is unsigned and was created before the session |
| D112, charge | A charge for a session the patient did not attend |
| D006 | Marks the medication visit and the partner-only contact "Completed" |
| D006, D108 | Hold rows for a no-show, a clinic cancellation, a second no-show and a patient cancellation |
| D010, D114 | Medication visits, which the plan excludes |
| D012 | A contact with the partner only |
| D109 | A call between professionals only |
| D015, D016 | Phone calls about scheduling |
| D013, D115 | Questionnaire reviews, not appointments |
| D001 | An authorization for 8 group sessions, which is not a record of attendance |

### DEV-02

> How many therapy minutes and hours did Rowan actually receive during the review period, overall and for each Monday–Sunday week? Show calculations or supporting detail, and report any conclusion the available documents do not settle.

| Part | Expected |
|---|---|
| 1. Question as understood | Rowan Mercer. "The review period" is taken as the episode in the plan, Jan 5 to Jan 30. "Actually receive" means minutes with Rowan present, less any interval a document says had no therapy |
| 2. Answer | 585 or 595 minutes, which is 9.75 or 9.92 hours. By week: 140, 120, 180, and 145 or 155 |
| 3. Figures | The weekly and total tables in section 6, and the per-session calculations in section 3 |
| 4. What contributed | The 12 counted contacts in section 3 |
| 5. What was excluded | Group breaks, 15 minutes in each of 5 groups. The 10 minutes of lost connection on Jan 21. The partner-only 15 minutes on Jan 30. The 8 encounters in section 6 |
| 6. Not settled | The Jan 26 start time (C-2). The two totals differ by 10 minutes because of it |
| 7. Assumptions | Totals cover the documented record. On Jan 6 both times were recorded at the desk, so 45 is the most that session can be |
| 8. Documents not read | None |

### DEV-03

> For each week, did the delivered therapy meet the goal documented in Rowan’s treatment plan? State the goal, the relevant therapy-day and minute totals, and whether it was met, not met, or cannot be determined from the current record.

| Part | Expected |
|---|---|
| 1. Question as understood | Rowan Mercer. Each Monday to Sunday week of the episode. The goal is the participation goal in the plan signed Jan 5 |
| 2. Answer | Not met, not met, met, cannot determine |
| 3. Figures | The weekly status table in section 6 |
| 4. What contributed | The 12 counted contacts in section 3 |
| 5. What was excluded | The 8 encounters in section 6 |
| 6. Not settled | Week 4. Days are met. Minutes are 145 or 155 against 150, and depend on the Jan 26 start time |
| 7. Assumptions | Week 4 runs past the end of the episode and is judged against the full requirement. Verdicts are on the documented record |
| 8. Documents not read | None |

**The goal, as the answer must state it**

D003 line 12: "at least 3 therapy days and at least 150 minutes of patient-present therapy in each Monday–Sunday week"

**Context the answer may give, without changing a verdict**

| Week | Context |
|---|---|
| Jan 5–11 | A no-show on Jan 8, and partial attendance on Jan 6 |
| Jan 12–18 | The clinic cancelled the group on Jan 15. Rowan could not attend on Jan 16 |
| Jan 26–Feb 1 | A no-show on Jan 27, and a cancellation by Rowan on Jan 28 |

### DEV-04

> Reconstruct the care on January 19 and January 21. How many therapy contacts and patient therapy minutes occurred on each date, and how do the attendance records, clinical notes, later documents, and telehealth records affect your answer?

| Part | Expected |
|---|---|
| 1. Question as understood | Rowan Mercer. Two dates: Jan 19 and Jan 21, 2026 |
| 2. Answer | Jan 19: 2 therapy contacts, 90 minutes. Jan 21: 1 therapy contact, 45 minutes |
| 3. Figures | Jan 19: group 60 and individual 30. Jan 21: 20 + 25 |
| 4. What contributed | HG-E110, HG-E111 and HG-E112 in section 3 |
| 5. What was excluded | The group break on Jan 19. The 10 minutes of lost connection on Jan 21. The old departure value of 11:30 |
| 6. Not settled | Nothing |
| 7. Assumptions | Video counts as present. The added individual session is a separate session |
| 8. Documents not read | None |

**How each kind of record affects the answer**

| Kind | Document | Effect |
|---|---|---|
| Attendance record | D102 | Gives arrival 10:00 and departure 11:30. The departure is replaced |
| Attendance record, corrected | D103 | Replaces the departure with 11:15 and keeps the arrival |
| Clinical note | D101 | Gives the break, and records that Rowan became tense and a same-day meeting was arranged |
| Clinical note | D105 | Gives the individual session from 11:15, and says Rowan came directly from the group room |
| Later document | D104 | Arrives Jan 26 showing 11:30. It is a copy and changes nothing |
| Telehealth record | D106 | The note and the platform export agree: two calls, one appointment |

**What the record does not hold**

- No attendance or schedule record exists for Jan 21. Presence rests on the clinician's note and the platform export.
- No schedule export covers Jan 19 or Jan 21.
- The room-transfer record that D103 relies on was not supplied.

Without the correction, Rowan would be recorded in two sessions at once from 11:15 to 11:30.

### DEV-05

> Summarize the documented symptom course during the episode and the reason for the additional individual contact on January 19. Which symptom assessments are distinct, and what conclusions about progress can and cannot be supported?

| Part | Expected |
|---|---|
| 1. Question as understood | Rowan Mercer. The episode, Jan 5 to Jan 30. "Symptom assessments" means completed questionnaires. Clinicians' written assessments are given as supporting observations |
| 2. Answer | PHQ-9 scores fell from 18 to 14 to 10 across three distinct assessments. The record calls this partial improvement. Sleep stayed disrupted, and anxiety about work persisted |
| 3. Figures | 18 to 14 is 4 lower. 14 to 10 is 4 lower. Overall 8 lower |
| 4. What contributed | The three assessments in section 5, and the observations below |
| 5. What was excluded | The copy in D014 and the two mentions in section 5 |
| 6. Not settled | Nothing. The three accounts of the added Jan 19 session supply different details and do not disagree (rule 7) |
| 7. Assumptions | Severity bands and thresholds for the PHQ-9 are outside knowledge and are labelled as such if shown |
| 8. Documents not read | None |

**The "Who" column** (D-35, rule 16)

| Value | Meaning |
|---|---|
| Patient | The sentence itself names the patient as the source, as in "Rowan reported" or "They described" |
| Clinician | The clinician who signed the note states it, and the sentence names no other source. It does not mean the clinician observed it |

A sentence is not marked Patient because of the paragraph around it.

**Mood**

| Date | Who | What | Source |
|---|---|---|---|
| Jan 5 | Patient | Low mood for several weeks | D002 line 11: "several weeks of low mood, reduced interest in usual activities" |
| Jan 5 | Clinician | Subdued affect | D002 line 13: "Affect was subdued but responsive" |
| Jan 13 | Patient | Somewhat better on active days | D010 line 11: "mood as somewhat less heavy on days with a planned activity" |
| Jan 14 | Clinician | More varied affect | D011 line 15: "Affect was more varied than at intake" |
| Jan 16 | Clinician | Some improvement | D013 line 13: "suggest some improvement in depressive symptoms" |
| Jan 26 | Clinician | Low mood continues | D111 line 14: "ongoing anxiety, low mood, and functional difficulty around work demands" |
| Jan 30 | Clinician | Less persistently low | D114 line 8: "Mood felt less persistently low than earlier in the month" |
| Jan 30 | Clinician | Partial improvement | D115 line 10: "Rowan shows partial improvement" |

**Anxiety**

| Date | Who | What | Source |
|---|---|---|---|
| Jan 5 | Clinician | Worry about returning to work | D002 line 11: "Worry increases when thinking about returning to work after a recent leave." |
| Jan 14 | Clinician | Worry when discussing employment | D011 line 15: "worry was evident when discussing employment" |
| Jan 19 | Clinician | Visibly tense in group | D101 line 10: "Rowan became visibly tense" |
| Jan 19 | Patient | Early signs of anxiety named | D105 line 9: "muscle tension, rapid breathing, and an urge to leave" |
| Jan 30 | Clinician | Anxious about the work conversation | D113 line 13: "Rowan remained anxious about the work conversation" |
| Jan 30 | Clinician | Anxiety when anticipating work contact | D114 line 8: "anxiety remained noticeable when anticipating contact with work" |

**Sleep**

| Date | Who | What | Source |
|---|---|---|---|
| Jan 5 | Patient | Fragmented | D002 line 11: "fragmented sleep" |
| Jan 8 | Patient | A poor night | D015 line 15: "a poor night of sleep" |
| Jan 13 | Patient | Interrupted | D010 line 11: "continuing sleep interruption and daytime tiredness" |
| Jan 14 | Clinician | Interrupted | D011 line 11: "Sleep remains interrupted" |
| Jan 16 | Patient | Inconsistent | D013 line 11: "Rowan also described sleep as inconsistent." |
| Jan 21 | Patient | One better night, then a poor one | D106 line 11: "one night of improved sleep followed by a night of prolonged wakefulness" |
| Jan 26 | Clinician | Uneven | D110 line 9: "Sleep remained uneven" |
| Jan 30 | Clinician | Still variable | D114 line 8: "Sleep was still variable." |
| Jan 30 | Clinician | An intermittent barrier | D115 line 10: "Sleep disruption remains an intermittent barrier" |

**Steps toward returning to work**

| Date | Step | Source |
|---|---|---|
| Jan 5 | Chose opening the work inbox for five minutes | D002 line 17: "Rowan selected opening their work inbox for five minutes" |
| Jan 6 | Chose reading the message as a possible next step | D004 line 14: "selected reading the message before deciding how to respond as a possible next step" |
| Jan 12 | Identified looking at one message as a smaller step | D009 line 14: "They identified looking at one message as a lower step" |
| Jan 14 | Had opened a work message; not yet replied; drafted a response in session | D011 line 11: "They have not yet replied to the message" |
| Jan 19 | Task narrowed to drafting two sentences | D105 line 11: "drafting two sentences to a supervisor" |
| Jan 21 | Had drafted a message; stopped before sending | D106 line 9: "stopping before sending it" |
| Jan 23 | Had asked whom to contact about a gradual return; reported by the outside social worker | D109 line 9: "Rowan had asked for help understanding whom to contact about a gradual return schedule" |
| Jan 26 | Had sent the message and received a reply; postponing a time to talk | D110 line 9: "Rowan continued to postpone choosing a time for the conversation." |
| Jan 29 | Had opened the work calendar; delaying the follow-up conversation | D107 line 14: "Rowan reported opening the work calendar but delaying a follow-up conversation." |
| Jan 30 | Still delaying follow-up | D115 line 10: "continues to delay follow-up" |

The worked example about a work email on Jan 19 was the facilitator's, not one of Rowan's steps (D101 line 8).

**Safety**

| Date | Statement | Source |
|---|---|---|
| Jan 5 | No immediate concern | D002 line 13: "No immediate safety concern was identified in today's assessment" |
| Jan 19 | Denied suicidal thoughts | D105 line 13: "Rowan denied current suicidal thoughts" |
| Jan 21 | No urgent concern | D106 line 11: "No urgent safety concern was reported." |
| Jan 26 | No suicidal ideation reported | D110 line 13: "No current suicidal ideation was reported." |
| Jan 30 | Denied suicidal thoughts | D114 line 10: "The patient denied current suicidal thoughts." |
| Jan 30 | Item 9 is 0 | D115 line 6 |

No safety statement appears in the week of Jan 12 to Jan 18.

One sentence in that week is left out of the table because it is about medication:

- D010 line 13: "Rowan denied a new medication-related concern requiring urgent intervention."
- The system may report it if it labels it as medication-related. The key does not fail the system either way.

**The reason for the added contact on Jan 19**

| Source | What it says |
|---|---|
| D105 line 9 | "This visit was added because Rowan became anxious during group and needed individual grounding and review of coping strategies." |
| D101 line 10 | "The facilitator offered grounding and arranged a same-day individual meeting with the treating clinician." |
| D102 line 14 | "Staff arranged access to the individual clinician after Rowan requested additional help." |

Read together (rule 7): Rowan became anxious during the group and asked for additional help, and the facilitator arranged an individual session the same day. This is not a conflict.

**What the record supports**

| Conclusion | Basis |
|---|---|
| Partial improvement in depressive symptoms | Three falling scores, and the clinician's words on Jan 16 and Jan 30 |
| First steps on work tasks | A message drafted and sent, a reply received |
| No acute safety concern at any point where safety was recorded | The safety table above |
| Treatment continues | D115 line 12: "Continued treatment is appropriate" |

**What the record does not support**

| Conclusion | Why |
|---|---|
| Remission or resolution | The last score is 10, and the clinician writes "partial improvement" |
| A measured level of anxiety | No anxiety questionnaire exists. Anxiety is described in notes only |
| Stable sleep | No note describes sleep as stable |
| A return to work | Not achieved within the episode. Rowan is still delaying the follow-up conversation |
| That treatment or medication caused the improvement | Therapy and medication ran together, and nothing in the record separates them |
| Unbroken engagement | Two no-shows, one cancellation by Rowan, and absence on Jan 16 |

**Progress against the plan's goals**

| Goal | What the record shows |
|---|---|
| 1. Activity and task initiation | Small activities attempted. No reliable routine yet (D013 line 13: "has not yet established a reliable routine") |
| 2. Coping with anxiety and sleep | Breathing and grounding practised in session. Sleep still disrupted on Jan 30 |
| 3. Return to employment | A message sent and a reply received. The follow-up conversation is delayed |

---

## 8. Problem questions and related questions

### Problem questions

At least one per case agreed in Discussion 18, except the case that waits on a second patient.

| # | Case | Question | Expected behaviour |
|---|---|---|---|
| P-1 | Unknown patient | "How many sessions did Jordan Blake attend?" | No patient by that name in the collection. No figures for any other patient |
| P-2 | A participant, not a patient | "How many sessions did Casey Mercer attend?" | Casey Mercer appears as a participant, not as a patient. Casey took part in contacts on Jan 9, Jan 16 and Jan 30. The answer is not 0 |
| P-3 | False premise | "How many minutes was Rowan in the Jan 27 group?" | 0. Rowan did not attend. Cites the signed attendance entry, and reports the draft and the charge |
| P-4 | False premise | "What was Rowan's PHQ-9 score on Jan 26?" | No questionnaire was completed on Jan 26. A result received that day is a copy of the Jan 16 score of 14 |
| P-5 | False premise | "How did Rowan's care change after the treatment plan was changed?" | The record holds one plan and no change to it. The change of staff on Jan 19 is not a plan change |
| P-6 | A date with no document | "What care did Rowan receive on Jan 24?" | Not documented. The answer does not say no care took place |
| P-7 | An ambiguous term | "How many visits did Rowan have?" | States the reading used: 12 therapy sessions. Gives the others beside it: 14 contacts with Rowan present, 16 contacts held, 20 encounters in the record |
| P-8 | A relative date | "How many sessions did Rowan attend last week?" | Uses the last week of the episode, Jan 26 to Feb 1, and says so: 3 sessions. Does not use today's date |
| P-9 | No function fits | "How many group authorization units does Rowan have left?" | Says the abstraction cannot answer it, because authorizations are not stored. Gives no figure for units left. Names D001 as the document that holds the authorization. Quoting the passage is not required |

The case "a name that matches two patients" cannot be tested on one patient. It waits on the second patient, which is on hold.

Figures in P-7: 20 encounters, less 2 no-shows and 2 cancellations, gives 16 held. Less the partner-only contact and the call between professionals gives 14 with Rowan present. Less 2 medication visits gives 12 therapy sessions.

### Related questions

| # | Question | Expected answer |
|---|---|---|
| Q-1 | Sessions from Jan 12 to Jan 25, by type, and on how many days | 6 sessions on 5 days: group 3 (Jan 12, 19, 22), individual 3 (Jan 14, 19, 21) |
| Q-2 | Sessions in each week | 3, 2, 4, 3 |
| Q-3 | Minutes by type in each week | Week 1: individual 50, group 45, family 45. Week 2: group 75, individual 45. Week 3: group 105, individual 75. Week 4: individual 40 or 50, group 75, family 30 |
| Q-4 | Days with more than one session | Jan 19 |
| Q-5 | Appointments missed or cancelled, and why | Jan 8 no-show. Jan 15 cancelled by the clinic, staff illness. Jan 27 no-show. Jan 28 cancelled by Rowan, a personal scheduling conflict. Also Jan 16, held with the partner after Rowan could not attend |
| Q-6 | Time in contacts that do not count | Medication 45 (25 + 20). Partner only 55 (40 on Jan 16, 15 on Jan 30). Care coordination 20. The 40 and the 20 come from header times (D-36) |
| Q-7 | Sessions with more than one clinician | Jan 9 (Mara Voss, Leena Park) and Jan 26 (Mira Patel, Nora Ellis) |
| Q-8 | Sessions by video | 1, on Jan 21 |
| Q-9 | Was the goal met in the week of Jan 19, and by how much | Met. 3 days and 180 minutes, 30 over |
| Q-10 | How many weeks met the goal | 1 met, 2 not met, 1 cannot be determined. So 1 or 2 of 4 |
| Q-11 | What changes if the Jan 26 start is settled at 09:10 | Week 4 becomes 145 minutes, not met. The total becomes 585 |
| Q-12 | What changes if the Jan 26 start is settled at 09:00 | Week 4 becomes 155 minutes, met. The total becomes 595 |
| Q-13 | Which patients had two consecutive weeks below the goal | Rowan, on weeks 1 and 2. This does not depend on the open conflict |
| Q-14 | Group sessions attended, against scheduled | 5 attended of 7 scheduled (Jan 6, 12, 15, 19, 22, 27, 29), on the documented record. No schedule export covers Jan 19 to Jan 30 |

---

## 9. What this key does not cover

| Not covered | Why |
|---|---|
| A second patient | On hold (O-1) |
| A plan change | On hold (O-1, O-13) |
| A document that lists several patients | No such document is supplied |
| The exact wording of a written answer | The key fixes figures, sources and behaviour. Wording may vary |
| Every observation in every note | Section 7 lists the observations the five answers need |
