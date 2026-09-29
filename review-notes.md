# Backbone take-home: review notes

Status of everything in this file: worked out by hand from reading the problem statement, `questions.json`, and all 31 documents. No code produced these numbers. Items marked **(judgment)** are interpretations you should agree or disagree with before we design anything.

Contents

1. What Backbone is asking
2. The data at a glance
3. Document index
4. Timeline: every contact, week by week
5. The traps
6. Hand-worked answers to the five development questions
7. Kinds of reasoning the system must do
8. Question catalog: asked, and likely to be asked
9. New documents that could arrive, and what should happen
10. What gets harder at 500K+ documents
11. Fundamental design choices
12. Judgment calls and open decisions
13. Oddities in the materials
14. Questions to expect in the design call

---



## 1. What Backbone is asking

Backbone reviews clinical records to establish what care a patient received and whether the documentation supports the conclusions drawn about it. The exercise is a small version of that job.

### What must be built


| Requirement                  | Wording in the problem statement                                                                                           |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| A clinical abstraction       | "an accurate, auditable clinical abstraction", used to answer questions about individual patients and the whole collection |
| Persistence                  | "retain its work so that it can answer new questions after restarting"                                                     |
| Reuse                        | "New questions should use the existing abstraction... should not rebuild the abstraction for each question"                |
| Source checks allowed        | "you may check relevant source passages"                                                                                   |
| Duplicates harmless          | "Duplicate copies of a document should not change clinical results"                                                        |
| No recency rule              | "A later document does not automatically override an earlier one"                                                          |
| Multiple sources per contact | "A scheduled appointment, a clinician's note, and an attendance entry can each contribute different information"           |
| Arithmetic in code           | "Calculate numerical answers in code from the abstraction"                                                                 |
| Traceability                 | "trace a finding across patients to the individual patients, services, calculations, and source passages"                  |
| Generalization               | works on "related unseen questions and additional documents without manually encoding patient facts or answers"            |
| Scale                        | assume 500,000+ documents, repeated reviews, new documents daily                                                           |




### What must be measured and reported

- Initial processing time
- Latency for individual-patient questions and collection-wide questions
- Model usage and cost
- Size of the saved abstraction
- Where it becomes slow or expensive at 500K+ documents, which part of the code causes it, and what you would change
- Measured results kept separate from estimates



### What must be submitted

- Runnable code and setup instructions, including how to process documents and how to answer new questions from the saved abstraction
- The abstraction, answers to the five questions, execution logs, benchmark results, all with supporting sources
- A short README covering:
  - approach
  - one design decision you tested and what you learned
  - one observed limitation and how you would investigate it
  - the first bottleneck you expect at a million documents
  - model names and settings
  - coding assistance used
  - approximate runtime and model cost
- Sent to [manan@backbonesystems.ai](mailto:manan@backbonesystems.ai) and [andrew@backbonesystems.ai](mailto:andrew@backbonesystems.ai) as a ZIP or GitHub link
- Time budget: 2–5 hours



### What happens after

A 30-minute system design call. They will review the abstraction, follow conclusions back to sources, and run related questions and additional documents through the submitted code.

### What they score

Completeness, accuracy, reproducible calculations, evidence quality, handling of uncertainty, performance on follow-up questions, research judgment.

### Guidance from the FAQ

- Think beyond vector search plus answer.
- When documents conflict or information is missing, make it explicit. If you resolve a conflict, explain the basis and keep the evidence. If the record cannot settle something, say what can be established and what documentation would be needed.
- References must be specific enough to locate the evidence within a document.
- For calculated answers, show which records contributed and any consequential inclusion or exclusion decisions.
- A command line or notebook is enough. No UI needed.

---



## 2. The data at a glance


| Fact                   | Value                                        |
| ---------------------- | -------------------------------------------- |
| Files                  | 31 text files, about 50 KB in total          |
| Exact duplicate files  | None in the supplied set                     |
| Patients               | 1: Rowan Mercer, DOB 1991-04-12, MRN HG-M042 |
| Organization           | Harbor Grove Behavioral Health (fictional)   |
| Episode                | 2026-01-05 to 2026-01-30, outpatient         |
| Treatment plans        | 1 (BH-D003), no amendment                    |
| Scheduled encounters   | 20 (HG-E101 to HG-E120)                      |
| Counted as therapy     | 12                                           |
| Symptom questionnaires | 3 PHQ-9 administrations                      |




### The governing rule (BH-D003)

- At least **3 therapy days** and at least **150 minutes** of patient-present therapy in each Monday–Sunday week.
- A therapy day is a calendar day on which Rowan participates in individual, group, or family psychotherapy.
- Counts toward minutes: patient-present individual, group, and family therapy.
- Does not count: medication management, contacts with collateral informants only, care coordination.



### Two batches


|               | Batch 1                          | Batch 2                           |
| ------------- | -------------------------------- | --------------------------------- |
| Document IDs  | BH-D001 to BH-D016               | BH-D101 to BH-D115                |
| Service dates | Jan 5–16                         | Jan 19–30                         |
| File names    | descriptive, no ID               | start with the ID                 |
| Date style    | 2026-01-05                       | January 19, 2026                  |
| Header        | "SYNTHETIC TRAINING RECORD" line | none                              |
| Therapists    | Mara Voss, Leena Park            | Mira Patel, Leah Chen, Nora Ellis |
| Prescriber    | Elias Brenner, NP                | Elena Ortiz, PMHNP                |
| Group name    | Coping skills group              | Skills group                      |
| Desk staff    | N. Ellis                         | Ana Reed                          |


The problem statement says "supplied datasets" (plural), which fits two batches. It may also be how they intend to test incremental processing.

---



## 3. Document index


| ID      | File                                       | What it is                                     | Service date(s)    | Document date  |
| ------- | ------------------------------------------ | ---------------------------------------------- | ------------------ | -------------- |
| BH-D001 | group_authorization_letter                 | Authorization: 8 group sessions, Jan 5–30      | none               | Jan 4          |
| BH-D002 | intake_and_individual_jan05                | Individual therapy note and intake; PHQ-9 = 18 | Jan 5              | Jan 5          |
| BH-D003 | signed_treatment_plan_jan05                | Treatment plan with the weekly goal            | none               | Jan 5, 13:05   |
| BH-D004 | group_facilitator_jan06                    | Group note; break 10:45–11:00                  | Jan 6              | Jan 6          |
| BH-D005 | early_group_attendance_roster              | Desk roster extract: arrival and departure     | Jan 6, Jan 12      | Jan 12         |
| BH-D006 | early_appointment_status_export            | Schedule export, 9 appointment rows            | Jan 5–16           | Jan 16         |
| BH-D007 | family_primary_jan09                       | Family therapy note, primary clinician         | Jan 9              | Jan 9          |
| BH-D008 | family_cofacilitator_jan09                 | Family therapy note, cofacilitator             | Jan 9              | Jan 10         |
| BH-D009 | group_facilitator_jan12                    | Group note; break 10:40–10:55                  | Jan 12             | Jan 12         |
| BH-D010 | medication_review_jan13                    | Medication visit, 25 min                       | Jan 13             | Jan 13         |
| BH-D011 | individual_therapy_jan14                   | Individual therapy note, 45 min                | Jan 14             | Jan 14         |
| BH-D012 | partner_collateral_jan16                   | Partner-only contact; Rowan absent             | Jan 16             | Jan 16         |
| BH-D013 | symptom_measure_review_jan16               | PHQ-9 = 14, form HG-Q116; review only          | Jan 16             | Jan 16         |
| BH-D014 | imported_measure_summary_received_jan26    | Import of the Jan 16 PHQ-9 result              | none               | Jan 26         |
| BH-D015 | missed_visit_outreach_jan08                | Scheduling log: no-show and phone calls        | Jan 8              | Jan 8          |
| BH-D016 | group_cancellation_notice_jan15            | Clinic cancelled the group                     | Jan 15             | Jan 15         |
| BH-D101 | group_content_2026-01-19                   | Group note; break 10:45–11:00                  | Jan 19             | Jan 19         |
| BH-D102 | original_attendance_2026-01-19             | Original signed roster: departure 11:30        | Jan 19             | Jan 19, 12:14  |
| BH-D103 | attendance_correction_2026-01-20           | Signed correction: departure 11:15             | Jan 19             | Jan 20, 08:42  |
| BH-D104 | resent_roster_received_2026-01-26          | Resent copy of the original roster             | Jan 19             | Jan 26, 16:22  |
| BH-D105 | individual_2026-01-19                      | Added individual session 11:15–11:45           | Jan 19             | Jan 19         |
| BH-D106 | telehealth_2026-01-21                      | Video session in two calls, plus platform log  | Jan 21             | Jan 21         |
| BH-D107 | group_activity_records_2026-01-22_and_29   | Group notes for two dates                      | Jan 22, Jan 29     | Jan 22, Jan 29 |
| BH-D108 | final_attendance_and_cancellation_register | Signed register, 4 appointment rows            | Jan 22, 27, 28, 29 | Jan 30         |
| BH-D109 | care_coordination_2026-01-23               | Professional-only call, 20 min                 | Jan 23             | Jan 23         |
| BH-D110 | individual_primary_record_2026-01-26       | Individual note: 09:00–09:50                   | Jan 26             | Jan 26, 11:16  |
| BH-D111 | individual_second_record_2026-01-26        | Second clinician's note: 09:10–09:50           | Jan 26             | Jan 26, 12:03  |
| BH-D112 | draft_note_and_charge_extract_2026-01-27   | Unsigned draft note and a posted charge        | Jan 27             | Jan 30         |
| BH-D113 | family_therapy_2026-01-30                  | Family therapy; Rowan present 30 of 45 min     | Jan 30             | Jan 30         |
| BH-D114 | medication_management_2026-01-30           | Medication visit, 20 min                       | Jan 30             | Jan 30         |
| BH-D115 | symptom_measure_review_2026-01-30          | PHQ-9 = 10, item 9 = 0; review only            | Jan 30             | Jan 30         |


---



## 4. Timeline: every contact, week by week

"Minutes" means patient-present therapy minutes that count toward the goal.

### Week 1: Jan 5–11


| Date  | Encounter | What happened                                                   | Documents        | Counts | Minutes |
| ----- | --------- | --------------------------------------------------------------- | ---------------- | ------ | ------- |
| Jan 5 | HG-E101   | Individual therapy 09:00–09:50                                  | D002, D006       | yes    | 50      |
| Jan 6 | HG-E102   | Group 10:00–11:30; Rowan present 10:15–11:15; break 10:45–11:00 | D004, D005, D006 | yes    | 45      |
| Jan 8 | HG-E103   | Individual no-show; two scheduling phone calls                  | D015, D006       | no     | 0       |
| Jan 9 | HG-E104   | Family therapy 14:00–14:45; two clinicians each wrote a note    | D007, D008, D006 | yes    | 45      |


- Jan 6 arithmetic: 10:15–10:45 (30) + 11:00–11:15 (15) = 45
- **Week total: 3 therapy days, 140 minutes. Not met, 10 minutes short.**



### Week 2: Jan 12–18


| Date   | Encounter | What happened                                             | Documents        | Counts | Minutes  |
| ------ | --------- | --------------------------------------------------------- | ---------------- | ------ | -------- |
| Jan 12 | HG-E105   | Group, full attendance; break 10:40–10:55                 | D009, D005, D006 | yes    | 75       |
| Jan 13 | HG-E106   | Medication visit 09:00–09:25                              | D010, D006       | no     | excluded |
| Jan 14 | HG-E107   | Individual therapy 11:00–11:45                            | D011, D006       | yes    | 45       |
| Jan 15 | HG-E108   | Group cancelled by clinic, staff illness                  | D016, D006       | no     | 0        |
| Jan 16 | HG-E109   | Partner-only contact 14:00–14:40; Rowan absent            | D012, D006       | no     | excluded |
| Jan 16 | none      | PHQ-9 completed 08:17, reviewed 09:10; not an appointment | D013             | no     | 0        |


- **Week total: 2 therapy days, 120 minutes. Not met, 1 day and 30 minutes short.**



### Week 3: Jan 19–25


| Date   | Encounter | What happened                                                        | Documents              | Counts | Minutes  |
| ------ | --------- | -------------------------------------------------------------------- | ---------------------- | ------ | -------- |
| Jan 19 | HG-E110   | Group; Rowan present 10:00–11:15 after correction; break 10:45–11:00 | D101, D102, D103, D104 | yes    | 60       |
| Jan 19 | HG-E111   | Added individual session 11:15–11:45                                 | D105                   | yes    | 30       |
| Jan 21 | HG-E112   | Video session 13:00–13:20 and 13:30–13:55                            | D106                   | yes    | 45       |
| Jan 22 | HG-E113   | Group; Rowan arrived 10:30, stayed to 11:30                          | D107, D108             | yes    | 45       |
| Jan 23 | HG-E114   | Care coordination between professionals, 09:00–09:20                 | D109                   | no     | excluded |


- Jan 19 group arithmetic: 10:00–10:45 (45) + 11:00–11:15 (15) = 60
- Jan 22 arithmetic: 10:30–10:45 (15) + 11:00–11:30 (30) = 45
- **Week total: 3 therapy days, 180 minutes. Met.**



### Week 4: Jan 26–Feb 1


| Date   | Encounter | What happened                                                          | Documents  | Counts | Minutes  |
| ------ | --------- | ---------------------------------------------------------------------- | ---------- | ------ | -------- |
| Jan 26 | HG-E115   | Individual; notes disagree: 09:00–09:50 vs 09:10–09:50                 | D110, D111 | yes    | 40 or 50 |
| Jan 27 | HG-E116   | Group no-show per signed register; draft note and charge say otherwise | D108, D112 | no     | 0        |
| Jan 28 | HG-E117   | Individual cancelled by Rowan at 08:12                                 | D108       | no     | 0        |
| Jan 29 | HG-E118   | Group, full attendance                                                 | D107, D108 | yes    | 75       |
| Jan 30 | HG-E119   | Family therapy 13:00–13:45; Rowan present 13:15–13:45                  | D113       | yes    | 30       |
| Jan 30 | HG-E120   | Medication visit 15:00–15:20                                           | D114       | no     | excluded |
| Jan 30 | none      | PHQ-9 completed 12:42; review is not an appointment                    | D115       | no     | 0        |


- **Week total: 3 therapy days, 145–155 minutes. Cannot be determined.**



### Totals for Jan 5–30


| Measure               | Value                        |
| --------------------- | ---------------------------- |
| Sessions              | 12                           |
| Individual            | 5 (Jan 5, 14, 19, 21, 26)    |
| Group                 | 5 (Jan 6, 12, 19, 22, 29)    |
| Family                | 2 (Jan 9, 30)                |
| Distinct therapy days | 11 (Jan 19 has two sessions) |
| Minutes               | 585–595                      |
| Hours                 | 9.75–9.92                    |
| Individual minutes    | 210–220                      |
| Group minutes         | 300                          |
| Family minutes        | 75                           |




### Scheduled contacts that did not count (8 of 20)


| Reason                       | Encounters                                         |
| ---------------------------- | -------------------------------------------------- |
| No-show                      | HG-E103 (Jan 8), HG-E116 (Jan 27)                  |
| Cancelled by patient         | HG-E117 (Jan 28)                                   |
| Cancelled by clinic          | HG-E108 (Jan 15)                                   |
| Medication management        | HG-E106 (Jan 13, 25 min), HG-E120 (Jan 30, 20 min) |
| Partner only, patient absent | HG-E109 (Jan 16, 40 min)                           |
| Professionals only           | HG-E114 (Jan 23, 20 min)                           |


---



## 5. The traps



### 5.1 Jan 19 group: correction, then a resent original


| Document | Signed or received | Departure time | Nature                                                  |
| -------- | ------------------ | -------------- | ------------------------------------------------------- |
| D102     | Jan 19, 12:14      | 11:30          | Original signed roster                                  |
| D103     | Jan 20, 08:42      | 11:15          | Signed correction naming the field and old value        |
| D104     | Jan 26, 16:22      | 11:30          | Resent copy of D102; "no correction sheet was included" |


- D103 explains the error: the scheduled closing time was left in the departure field.
- D105 corroborates 11:15: Rowan "came directly from the group room" to a session starting at 11:15.
- With 11:30, Rowan would be in two sessions at once from 11:15 to 11:30.
- D104 says of itself that it has "no new clinician signature and records no additional visit".
- Result: 60 minutes, not 75.



### 5.2 Jan 21 video: two calls, one session

- Calls VC-112A (13:00–13:20) and VC-112B (13:30–13:55), both under appointment HG-A112.
- Connection lost 13:20–13:30, "no therapeutic contact during that interval".
- Result: one session, 45 minutes. Not two sessions, not 55 minutes.



### 5.3 Jan 26 individual: two signed notes disagree


| Document | Author     | Signed | Patient contact     |
| -------- | ---------- | ------ | ------------------- |
| D110     | Mira Patel | 11:16  | 09:00–09:50, 50 min |
| D111     | Nora Ellis | 12:03  | 09:10–09:50, 40 min |


- Both are final. No correction exists.
- D111 is later and more specific: "Rowan entered the treatment room at 09:10, when we began the session."
- Result **(judgment)**: left open at 40–50 minutes.



### 5.4 Jan 27 group: no-show against a draft and a charge


| Source         | Says                                         | Standing                                                        |
| -------------- | -------------------------------------------- | --------------------------------------------------------------- |
| D108 register  | No show; "absent for the entire group"       | Signed by Leah Chen, Jan 27, 11:54                              |
| D112 section A | "Patient attended the full session"          | Unsigned draft, auto-generated at 09:45, before the 10:00 group |
| D112 section B | Charge CH-116, 1 group session, posted 18:06 | Billing row                                                     |


- Result: not attended, 0 minutes.
- The charge for a no-show is a finding a reviewer would want surfaced.



### 5.5 Jan 30 family: clinician time is not patient time

- Therapist interval 13:00–13:45 (45 minutes).
- Partner only 13:00–13:15. Rowan present 13:15–13:45.
- Result: 30 minutes.



### 5.6 Group breaks, late arrivals, early departures


| Date   | Scheduled   | Rowan present | Break       | Minutes |
| ------ | ----------- | ------------- | ----------- | ------- |
| Jan 6  | 10:00–11:30 | 10:15–11:15   | 10:45–11:00 | 45      |
| Jan 12 | 10:00–11:30 | 10:00–11:30   | 10:40–10:55 | 75      |
| Jan 19 | 10:00–11:30 | 10:00–11:15   | 10:45–11:00 | 60      |
| Jan 22 | 10:00–11:30 | 10:30–11:30   | 10:45–11:00 | 45      |
| Jan 29 | 10:00–11:30 | 10:00–11:30   | 10:45–11:00 | 75      |


- The break is in the group note; arrival and departure are in a separate roster.
- The Jan 12 break is at a different time from the others, so it cannot be hardcoded.



### 5.7 Two notes for one session

- Jan 9 family: D007 (primary) and D008 (cofacilitator, signed Jan 10). One session of 45 minutes.
- Jan 26 individual: D110 and D111. One session.



### 5.8 "Completed" in the schedule export

- D006 marks HG-E106 (medication) and HG-E109 (partner-only) as "Completed".
- Completed means the appointment took place, not that the patient received therapy.
- D006 also shows only scheduled times, never actual presence.



### 5.9 PHQ-9 copies and references


| Document | Score | Completed | Nature                                                             |
| -------- | ----- | --------- | ------------------------------------------------------------------ |
| D002     | 18    | Jan 5     | Original                                                           |
| D013     | 14    | Jan 16    | Original (form HG-Q116)                                            |
| D013     | 18    | Jan 5     | Mention of the earlier score                                       |
| D014     | 14    | Jan 16    | Import received Jan 26; "no newly completed patient questionnaire" |
| D115     | 10    | Jan 30    | Original                                                           |


- Three distinct assessments. Counting D014 as a Jan 26 result gives 18, 14, 14, 10, a false plateau.



### 5.10 Authorization is not attendance

- D001 authorizes 8 group sessions. It says "No service attendance record accompanies this letter."
- 7 groups were scheduled, 5 attended, 1 cancelled by the clinic, 1 no-show.



### 5.11 Phone calls and messages

- Jan 8: outbound call (no answer) and Rowan's callback, "No therapy intervention was conducted."
- Jan 15: Rowan called the desk to acknowledge the cancellation.
- Jan 27: outreach message left after the group.
- None are therapy.



### What each mistake does to the weekly verdict


| Mistake                                        | Effect                                                    |
| ---------------------------------------------- | --------------------------------------------------------- |
| Using scheduled time for Jan 6                 | Week 1 becomes 185 min, wrongly met                       |
| Not subtracting the break on Jan 6             | Week 1 becomes 155 min, wrongly met                       |
| Counting the partner-only contact              | Week 2 becomes 3 days and 160 min, wrongly met            |
| Counting the medication visit as a therapy day | Week 2 reaches 3 days                                     |
| Using 11:30 on Jan 19                          | Week 3 becomes 195 min (verdict unchanged, minutes wrong) |
| Counting two video calls as two sessions       | Session count becomes 13                                  |
| Counting the Jan 27 draft or charge            | Week 4 wrongly met                                        |
| Using 45 for the Jan 30 family session         | Week 4 becomes 160–170, wrongly met                       |
| Choosing one Jan 26 note                       | Week 4 looks certain when it is not                       |


---



## 6. Hand-worked answers to the five development questions



### DEV-01: sessions, types, distinct days, duplicate or ineligible records

- 12 sessions: 5 individual, 5 group, 2 family.
- 11 distinct days.
- Records that could inflate or distort the count:


| Record                 | Risk                                                  |
| ---------------------- | ----------------------------------------------------- |
| D007 and D008          | Two notes, one family session                         |
| D110 and D111          | Two notes, one individual session                     |
| D104                   | Resent roster, not a new visit                        |
| D106 platform log      | Two calls, one session                                |
| D112 draft             | Unsigned, generated before the session                |
| D112 charge            | Billing row for a no-show                             |
| D006 "Completed" rows  | Include a medication visit and a partner-only contact |
| D010, D114             | Medication visits                                     |
| D012                   | Partner only                                          |
| D109                   | Professionals only                                    |
| D015, D016             | Phone contacts                                        |
| D013, D115             | Questionnaire reviews, not appointments               |
| D014                   | Imported result                                       |
| D001                   | Authorization                                         |
| D107, D108, D005, D006 | One document covering several dates                   |




### DEV-02: minutes and hours, overall and by week


| Week         | Calculation          | Minutes | Hours     |
| ------------ | -------------------- | ------- | --------- |
| Jan 5–11     | 50 + 45 + 45         | 140     | 2.33      |
| Jan 12–18    | 75 + 45              | 120     | 2.00      |
| Jan 19–25    | 60 + 30 + 45 + 45    | 180     | 3.00      |
| Jan 26–Feb 1 | (40 or 50) + 75 + 30 | 145–155 | 2.42–2.58 |
| Total        |                      | 585–595 | 9.75–9.92 |


- Not settled by the record: the Jan 26 start time.



### DEV-03: weekly goal


| Week         | Days | Minutes | Status           | Reason                                 |
| ------------ | ---- | ------- | ---------------- | -------------------------------------- |
| Jan 5–11     | 3    | 140     | Not met          | Minutes 10 short                       |
| Jan 12–18    | 2    | 120     | Not met          | 1 day and 30 minutes short             |
| Jan 19–25    | 3    | 180     | Met              | Both thresholds reached                |
| Jan 26–Feb 1 | 3    | 145–155 | Cannot determine | Days reached; minutes depend on Jan 26 |




### DEV-04: Jan 19 and Jan 21


| Date   | Therapy contacts | Minutes | How                             |
| ------ | ---------------- | ------- | ------------------------------- |
| Jan 19 | 2                | 90      | Group 60 + individual 30        |
| Jan 21 | 1                | 45      | 20 + 25, disconnection excluded |


- Attendance records: D102 original (11:30), D103 correction (11:15).
- Clinical notes: D101 supplies the break and the reason for the transfer; D105 supplies the 11:15 start.
- Later documents: D104 arrives Jan 26 with the old value but is a copy.
- Telehealth records: the platform log confirms two calls under one appointment.



### DEV-05: symptom course, reason for the Jan 19 contact, progress

**Distinct assessments**


| Date   | PHQ-9 | Change | Band (general convention) |
| ------ | ----- | ------ | ------------------------- |
| Jan 5  | 18    |        | moderately severe         |
| Jan 16 | 14    | −4     | moderate                  |
| Jan 30 | 10    | −4     | moderate                  |


- Overall change: −8 points, a 44% reduction.
- Item 9 = 0 on Jan 30. Item-level scores are not recorded for the other two dates.
- The bands and thresholds are general conventions for the instrument, not statements in the record.

**Reason for the added Jan 19 session**

- D105: "added because Rowan became anxious during group and needed individual grounding and review of coping strategies."
- D101: Rowan "became visibly tense" when discussion turned to returning to work; the facilitator "arranged a same-day individual meeting".

**What the record supports**

- Partial improvement in depressive symptoms (three scores, and the clinician's Jan 30 assessment).
- Some first steps on work tasks (see 8.5).
- Continued engagement with treatment.

**What the record does not support**

- Remission or resolution.
- Any conclusion about anxiety severity: no anxiety measure exists.
- Stable sleep: every note describes it as inconsistent.
- Return to work: not achieved within the episode.
- That the improvement was caused by treatment or medication.

---



## 7. Kinds of reasoning the system must do



### Group A: conflict between documents


| #   | Reasoning                                               | Example                       |
| --- | ------------------------------------------------------- | ----------------------------- |
| 1   | A signed correction replaces a specific earlier value   | D103 over D102                |
| 2   | A copy carries no new authority, whatever its date      | D104, D014                    |
| 3   | Two equally valid records disagree and stay open        | D110 vs D111                  |
| 4   | What kind of record it is decides what it can establish | D112 draft and charge vs D108 |




### Group B: assembling one record from many documents


| #   | Reasoning                                                | Example                                                            |
| --- | -------------------------------------------------------- | ------------------------------------------------------------------ |
| 5   | Matching documents to the same contact                   | D007 and D008; HG-A112 and HG-E112                                 |
| 6   | Matching documents to the same patient                   | MRN, name, DOB                                                     |
| 7   | Matching records to the same assessment                  | Form HG-Q116 in D013 and D014                                      |
| 8   | Combining complementary facts                            | Break from the note, times from the roster, slot from the schedule |
| 9   | Telling dates apart: service, signature, receipt, export | D008, D014, D104, D112                                             |
| 10  | Splitting one document into several contacts             | D006 (9 rows), D108 (4 rows), D107 (2 dates)                       |
| 11  | Exact duplicate files                                    | Same content twice must change nothing                             |




### Group C: calculating


| #   | Reasoning                                   | Example                                                    |
| --- | ------------------------------------------- | ---------------------------------------------------------- |
| 12  | Interval arithmetic                         | Presence minus breaks; split calls                         |
| 13  | Patient time versus clinician time          | Jan 30 family: 30 of 45                                    |
| 14  | Classifying what counts                     | Therapy versus medication, collateral, coordination        |
| 15  | Rules that come from the record             | Thresholds and definitions from D003                       |
| 16  | Rules in effect for a period                | Which plan version governs which week                      |
| 17  | Calendar bucketing                          | Monday–Sunday weeks; weeks that cross the episode boundary |
| 18  | Carrying ranges through sums and thresholds | 40–50 becomes 145–155 becomes "cannot determine"           |
| 19  | Patterns over time                          | Two consecutive weeks below                                |
| 20  | Before and after comparison                 | Around a plan change, normalized for period length         |




### Group D: negatives, gaps, and consistency


| #   | Reasoning                                        | Example                                           |
| --- | ------------------------------------------------ | ------------------------------------------------- |
| 21  | Stated negatives are evidence                    | "No patient contact occurred"                     |
| 22  | Silence is not a negative                        | A week with no documents is not proof of no care  |
| 23  | Internal consistency                             | Stated duration against the computed interval     |
| 24  | Cross-record consistency                         | Overlapping sessions; a charge without attendance |
| 25  | What documentation would settle an open question | For Jan 26: a signed addendum or an arrival log   |




### Group E: narrative synthesis


| #   | Reasoning                          | Example                                      |
| --- | ---------------------------------- | -------------------------------------------- |
| 26  | Who said it                        | Patient, clinician, partner, questionnaire   |
| 27  | Observation versus assessment      | "Visibly tense" versus "partial improvement" |
| 28  | Linking cause across documents     | D101 explains D105                           |
| 29  | Limits of a conclusion             | Direction versus remission                   |
| 30  | Keeping outside knowledge labelled | PHQ-9 severity bands are not in the record   |




### Group F: across the collection and over time


| #   | Reasoning                          | What it means                                                                             |
| --- | ---------------------------------- | ----------------------------------------------------------------------------------------- |
| 31  | Cohort aggregation with drill-down | From a list of patients down to the source line                                           |
| 32  | Sensitivity                        | Would the conclusion flip under each resolution of an open conflict                       |
| 33  | Revision                           | A new document changes an earlier conclusion                                              |
| 34  | Order independence                 | The same documents in a different arrival order give the same result                      |
| 35  | Question interpretation            | Mapping an unseen question to the right calculation; defaults such as "the review period" |
| 36  | Patient reference resolution       | "Rowan" to one patient, or an error if ambiguous                                          |

### How this list was produced, and its limits

The 36 items and 6 groups are not derived from anything. I listed items as I noticed them in the traps and the problem statement, then sorted them by theme. Known flaws:

- **Overlaps.** Items 5, 6, 7 are all matching. Items 23 and 24 are both consistency checks.
- **Mixed sizes.** "Interval arithmetic" is a broad technique; "patient reference resolution" is one narrow task.
- **Mixed categories.** Items 33 and 34 are properties of the system, not kinds of reasoning.
- **Not exhaustive.** Nothing guarantees the list is complete.

Use the 36 as a **test checklist**: each should have a test case. Do not use them to drive the design.

### The eight kinds that drive the design

Test for whether two kinds are different: would they be built differently? That depends on what the reasoning looks at, whether it is language or logic, and when it runs.

| Kind | Looks at | Nature | Runs | Items from the 36 |
|---|---|---|---|---|
| Reading a document | One document | Language | Once per document | 9, 10, 26, 27 |
| Weighing the source | One document | Language | Once per document | 2, 4 |
| Matching | One patient's documents | Exact lookup | When a document arrives | 5, 6, 7, 11 |
| Reconciling a contact | Documents about one contact | Logic | When a document arrives | 1, 3, 8, 21–25 |
| Counting and measuring | One patient | Arithmetic | When a document arrives | 12–17 |
| Evaluating | One patient or the collection | Logic over ranges | At question time | 18, 19, 20, 31, 32 |
| Writing a narrative | One patient | Judgment | At question time | 28, 29, 30 |
| Understanding the question | The question | Language | At question time | 35, 36 |

System properties, outside the table: 33 (revision), 34 (order independence).

What the "Nature" column implies:

| Nature | Suited to |
|---|---|
| Language | A model |
| Exact lookup, logic, arithmetic | Code |
| Judgment | A model, restricted to evidence already in the abstraction |


---



## 8. Question catalog: asked, and likely to be asked

Source key: **DEV** = in `questions.json`. **PS** = named in the problem statement but not testable on the supplied data. **Likely** = my inference of a related question.

### 8.1 Counting sessions


| Question                                           | Source | Hand answer for Rowan                                                                          |
| -------------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------- |
| Sessions by type, total, distinct days, Jan 5–30   | DEV-01 | 12; 5/5/2; 11 days                                                                             |
| Sessions in a different date range, e.g. Jan 12–25 | Likely | 6 (group 3, individual 3)                                                                      |
| Sessions per week                                  | Likely | 3, 2, 4, 3                                                                                     |
| Sessions by clinician                              | Likely | See 8.7                                                                                        |
| In-person versus video                             | Likely | 1 video (Jan 21). Modality is not stated in every note                                         |
| Days with more than one session                    | Likely | Jan 19                                                                                         |
| Appointments missed or cancelled, and why          | Likely | 2 no-shows, 1 patient cancellation, 1 clinic cancellation, 1 family session held without Rowan |
| Group sessions attended against authorized         | Likely | 5 attended, 7 scheduled, 8 authorized                                                          |




### 8.2 Minutes and hours


| Question                                       | Source | Hand answer for Rowan                                           |
| ---------------------------------------------- | ------ | --------------------------------------------------------------- |
| Minutes and hours overall and per week         | DEV-02 | 585–595; 140, 120, 180, 145–155                                 |
| Minutes by service type                        | Likely | Individual 210–220, group 300, family 75                        |
| Minutes on a given day                         | Likely | See section 4                                                   |
| Time in non-therapy contacts                   | Likely | Medication 45, partner-only 40, coordination 20                 |
| Scheduled time against delivered time          | Likely | Groups: 450 scheduled across 5 attended, 300 delivered          |
| Time lost to breaks, lateness, early departure | Likely | Breaks 75; late or early 75 (Jan 6: 30, Jan 19: 15, Jan 22: 30) |




### 8.3 Goal compliance


| Question                                       | Source | Hand answer for Rowan                                                         |
| ---------------------------------------------- | ------ | ----------------------------------------------------------------------------- |
| Was the goal met each week                     | DEV-03 | Not met, not met, met, cannot determine                                       |
| By how much did each week miss                 | Likely | Week 1: 10 min. Week 2: 1 day, 30 min. Week 4: between 5 short and 5 over     |
| Which weeks depend on unresolved documentation | PS     | Week 4                                                                        |
| What would settle week 4                       | Likely | A signed addendum from either clinician, or an arrival record for Jan 26      |
| Was the requirement in effect for that period  | PS     | One plan covers Jan 5–30                                                      |
| Why was a week missed                          | Likely | Week 2: clinic cancelled the group; Rowan could not attend the family session |




### 8.4 Reconstructing a date


| Date   | Source | Therapy contacts | Minutes | Points to explain                                           |
| ------ | ------ | ---------------- | ------- | ----------------------------------------------------------- |
| Jan 19 | DEV-04 | 2                | 90      | Correction, resent copy, same-day transfer                  |
| Jan 21 | DEV-04 | 1                | 45      | Two calls, one appointment                                  |
| Jan 6  | Likely | 1                | 45      | Late arrival, early departure, break                        |
| Jan 9  | Likely | 1                | 45      | Two notes; one signed the next day                          |
| Jan 16 | Likely | 0                | 0       | Partner only; PHQ-9 review is not a visit                   |
| Jan 22 | Likely | 1                | 45      | Late arrival                                                |
| Jan 26 | Likely | 1                | 40–50   | Unresolved conflict                                         |
| Jan 27 | Likely | 0                | 0       | Signed no-show against draft and charge                     |
| Jan 30 | Likely | 1                | 30      | Partial presence; medication visit excluded; PHQ-9 at 12:42 |




### 8.5 Progress and symptoms


| Question                                     | Source | Hand answer for Rowan                                                 |
| -------------------------------------------- | ------ | --------------------------------------------------------------------- |
| Symptom course and distinct assessments      | DEV-05 | 18, 14, 10; three distinct                                            |
| Reason for the Jan 19 added session          | DEV-05 | Became anxious in group                                               |
| What conclusions can and cannot be supported | DEV-05 | See section 6                                                         |
| Course of sleep                              | Likely | Disrupted throughout; never described as stable                       |
| Steps toward return to work                  | Likely | See below                                                             |
| Safety statements                            | Likely | See below                                                             |
| Medication changes                           | Likely | None. Jan 30: "No medication change was made." Drug name never stated |
| Family involvement                           | Likely | Jan 9 session, Jan 16 partner contact, Jan 30 session                 |


**Work-related steps in date order**


| Date   | Document   | Step                                                                          |
| ------ | ---------- | ----------------------------------------------------------------------------- |
| Jan 5  | D002       | Chose opening the work inbox for five minutes                                 |
| Jan 14 | D011       | Had opened a work message; not yet replied; drafted a response in session     |
| Jan 19 | D105       | Task narrowed to drafting two sentences to a supervisor                       |
| Jan 21 | D106       | Had drafted a message; stopped before sending                                 |
| Jan 26 | D110       | Had sent the message and received a reply; postponing choosing a time to talk |
| Jan 29 | D107       | Had opened the work calendar; delaying the follow-up conversation             |
| Jan 30 | D113, D115 | Still anxious; "continues to delay follow-up"                                 |


**Safety statements**


| Date   | Document | Statement                              |
| ------ | -------- | -------------------------------------- |
| Jan 5  | D002     | No immediate safety concern identified |
| Jan 19 | D105     | Denied current suicidal thoughts       |
| Jan 21 | D106     | No urgent safety concern reported      |
| Jan 26 | D110     | No current suicidal ideation reported  |
| Jan 30 | D114     | Denied current suicidal thoughts       |
| Jan 30 | D115     | PHQ-9 item 9 = 0                       |




### 8.6 Collection-wide questions

None of these can be tested on the supplied data. They need more patients.


| Question                                                      | Source | Answer with only Rowan                                             |
| ------------------------------------------------------------- | ------ | ------------------------------------------------------------------ |
| Which patients had two consecutive weeks below requirements   | PS     | Rowan, on weeks 1 and 2                                            |
| Which patients' inclusion depends on unresolved documentation | PS     | None. Rowan qualifies regardless of week 4, because week 3 was met |
| How many patients met the goal every week                     | Likely | 0 of 1                                                             |
| Which patients have unresolved conflicts                      | Likely | Rowan (Jan 26)                                                     |
| Totals or averages across patients                            | Likely | Trivial with one patient                                           |
| Trace a cohort finding to its sources                         | PS     | Patient, then week, then session, then calculation, then line      |


Note on the second row: if Jan 26 were resolved to 40 minutes, week 4 becomes not met. Weeks 3 and 4 still do not form a pair because week 3 was met.

### 8.7 Clinicians and services


| Clinician          | Role                       | Contacts                                                                              |
| ------------------ | -------------------------- | ------------------------------------------------------------------------------------- |
| Mara Voss, LCSW    | Therapist, batch 1         | Individual Jan 5, 14; family Jan 9; partner contact Jan 16; plan; PHQ-9 review Jan 16 |
| Leena Park, LPC    | Group facilitator, batch 1 | Groups Jan 6, 12; cofacilitator Jan 9                                                 |
| Elias Brenner, NP  | Prescriber, batch 1        | Medication Jan 13                                                                     |
| Mira Patel, LCSW   | Therapist, batch 2         | Individual Jan 19, 21, 26; family Jan 30; coordination Jan 23; PHQ-9 review Jan 30    |
| Leah Chen, LCSW    | Group facilitator, batch 2 | Groups Jan 19, 22, 29; register entries                                               |
| Nora Ellis, LCSW   | Participating clinician    | Individual Jan 26                                                                     |
| Elena Ortiz, PMHNP | Prescriber, batch 2        | Medication Jan 30                                                                     |




### 8.8 Treatment-plan change

Not testable on the supplied data. There is one plan and no amendment.


| Question                                                     | Source | Needs                                  |
| ------------------------------------------------------------ | ------ | -------------------------------------- |
| How did types and amounts of care change after a plan change | PS     | A plan amendment document              |
| Did care meet the requirement in effect for each period      | PS     | Two plan versions with effective dates |
| Which plan governs a week that contains the change           | Likely | A stated rule **(judgment)**           |




### 8.9 Record integrity


| Question                                     | Source | Hand answer for Rowan            |
| -------------------------------------------- | ------ | -------------------------------- |
| Charges without supporting attendance        | Likely | CH-116 for Jan 27                |
| Documents that are copies                    | Likely | D104, D014                       |
| Values that were corrected                   | Likely | Jan 19 departure, 11:30 to 11:15 |
| Open conflicts and what would resolve them   | Likely | Jan 26 start time                |
| Unsigned or draft documents                  | Likely | D112 section A                   |
| Notes signed on a later day than the service | Likely | D008 (Jan 10 for Jan 9)          |


---



## 9. New documents that could arrive, and what should happen


| New document                                                       | Expected behaviour                                  |
| ------------------------------------------------------------------ | --------------------------------------------------- |
| Exact duplicate of an existing file                                | Nothing changes                                     |
| Same document with different whitespace or line endings            | Nothing changes                                     |
| Signed addendum settling Jan 26 at 09:10                           | Week 4 becomes 145, not met                         |
| Signed addendum settling Jan 26 at 09:00                           | Week 4 becomes 155, met                             |
| Another resend of the Jan 19 original roster                       | Nothing changes                                     |
| A new signed record, written after the correction, that says 11:30 | A real conflict; Jan 19 becomes unresolved          |
| Signed note for Jan 27 saying Rowan attended                       | Conflict between two signed records                 |
| A second patient                                                   | Appears in collection-wide answers; Rowan unchanged |
| A plan amendment                                                   | Later weeks are judged against the new requirement  |
| Documents for a session after Jan 30                               | Week 4 totals may rise                              |
| A multi-patient roster                                             | Each patient gets only their own row                |
| Same documents, different arrival order                            | Identical result                                    |


---



## 10. What gets harder at 500K+ documents


| Concern                 | Why                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------- |
| Patient identity        | Shared names, typos, missing record numbers                                                             |
| Multi-patient documents | Real rosters list every group member                                                                    |
| Missing encounter IDs   | Matching falls back to date, time, type, clinician                                                      |
| Richer plan rules       | "2 groups and 1 individual weekly", tapering schedules                                                  |
| Extraction errors       | 1% wrong is 5,000 documents; needs validation, sampling, review queue                                   |
| Re-processing           | A prompt or model change means re-extracting everything                                                 |
| Extraction cost         | Measured earlier at about $0.07 per document on Opus; about $36K for 500K at list price (extrapolation) |
| Throughput              | Rate limits on model calls set the ceiling on initial processing                                        |
| Format                  | Scans, tables, long documents                                                                           |
| Time zones              | "All times local" breaks with several facilities                                                        |
| Provisional conclusions | Documents arrive daily, so any answer is "as of" a date                                                 |


---



## 11. Fundamental design choices


| Choice                | Options                                                                              | My lean                                                         |
| --------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| Unit of abstraction   | Per-document summaries; claims plus a reconciled layer; one merged timeline          | Two layers: what each document says, and what we conclude       |
| Where the model works | Per document; per patient with the whole chart; none (rules only)                    | Per document; code reconciles                                   |
| Conflict policy       | Fixed precedence rules; model adjudication; leave open for a human                   | Rules for clear cases; leave the rest open                      |
| Uncertainty           | Min–max ranges; enumerated scenarios; probabilities                                  | Ranges                                                          |
| Storage               | SQLite; JSON files per patient; Postgres                                             | SQLite plus a readable export                                   |
| Answering questions   | Fixed reports; model picks from coded functions; model writes SQL; RAG over raw text | Model plans, code computes, model narrates                      |
| Plan rules            | Hardcoded; extracted as data with effective dates                                    | Extracted as data                                               |
| Time model            | One date per fact; service time plus record time                                     | Both                                                            |
| Citations             | Trust the model's references; verify quotes in code                                  | Verify in code                                                  |
| Extraction cost       | One strong model; small model with escalation; batch processing                      | Decide by experiment                                            |
| Schema                | Fixed typed fields; open-ended facts                                                 | Typed for contacts, measures, plans; free text for observations |
| Incremental updates   | Rebuild everything; rebuild only affected patients                                   | Affected patients only                                          |




### Trade-offs on the three that matter most

**Where the model works**


| Option                  | For                                                              | Against                                                                        |
| ----------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Per document            | Cacheable, parallel, incremental, cheap to re-run reconciliation | Extractor never sees other documents; rules must anticipate conflict types     |
| Whole chart per patient | Handles novel conflicts flexibly                                 | Re-runs when any document arrives; harder to audit; model does the reconciling |
| Rules only, no model    | Free and deterministic                                           | Breaks on format changes; the two batches already differ                       |


**Conflict policy**


| Option             | For                       | Against                                         |
| ------------------ | ------------------------- | ----------------------------------------------- |
| Fixed rules        | Reproducible, explainable | Only covers anticipated cases                   |
| Model adjudication | Flexible                  | Can vary between runs; reasoning must be stored |
| Leave open         | Never wrong               | Less useful if too much stays open              |


**Answering questions**


| Option                      | For                                   | Against                                                      |
| --------------------------- | ------------------------------------- | ------------------------------------------------------------ |
| Fixed reports               | Fully reproducible                    | Cannot handle unseen questions                               |
| Model picks coded functions | Numbers from code; handles variations | Limited to what the functions cover                          |
| Model writes SQL            | Most flexible                         | Query errors; harder to guarantee correctness                |
| RAG over raw text           | Simple                                | Re-derives everything per question; the FAQ warns against it |

### What motivates each choice

The leans in the table above came from experience first. This traces each one back to a requirement, the data, or the questions.

| Design choice | What motivates it | Strength |
|---|---|---|
| Two layers: what documents say, what we conclude | "Retain the supporting evidence"; conflicts need both sides kept | Strong |
| Model reads one document at a time | Duplicates cost nothing; new documents are cheap; formats vary between batches | Strong, with a gap |
| Code reconciles, counts, and evaluates | "Calculate numerical answers in code"; logic must be reproducible | Strong |
| Plan rules stored as data with dates | "Requirements in effect for each period"; other patients will have other plans | Strong |
| Two dates per fact (service and record) | D008, D014, D104 each have a record date that differs from the service date | Strong |
| Citations checked in code | Evidence quality is scored; nobody can hand-check 500K documents | Strong |
| Rebuild only affected patients | Documents arrive daily | Strong |
| Model plans, code computes, model narrates | Unseen questions need flexibility; numbers must come from code | Medium |
| Rules for clear conflicts, rest left open | Uncertainty handling is scored | Medium |
| Uncertainty as ranges | "Cannot be determined" is an explicit answer option | Weak |
| SQLite | Survives restart, inspectable, no setup | Weak |
| Opus for extraction | None: it was a default | Unmotivated |

### Known gaps in the motivated choices

| Choice | Gap | Mitigation |
|---|---|---|
| Per-document reading | Which facts get extracted is fixed in advance; an unseen question may need one we skipped | The problem statement allows checking source passages |
| Ranges | Work for minutes, not for category disagreements such as attended or not | Store the alternatives, not only a range |
| Ranges | Lose the link to the conflict that caused them; the cohort question needs it | Keep a pointer from each range to its open conflict |
| Conflict rules | Only cover conflict types anticipated in advance | Anything unrecognized stays open rather than being resolved |
| SQLite | A prototype convenience | The requirement is only persistent, queryable, inspectable |

### Requirements with no design choice behind them

| Requirement or driver | Why it is missing |
|---|---|
| How we know extraction is correct | Evaluation was never listed as a design choice |
| Testing cohort and plan-change questions | No supplied data exercises them |
| Patient identity across many patients | Invisible with one patient |
| Documents that list several patients | The supplied rosters are single-patient extracts |
| Where a reviewer's ruling goes | If someone settles Jan 26, nothing records it |
| What happens when the extraction prompt changes | Not considered |
| "Repeated reviews" | Not considered |

Evaluation is the most serious gap. Accuracy is scored, and the README must describe a decision that was tested.

### Deriving the abstraction from the questions

Working backwards from each question type gives the minimum the abstraction must hold.

| Question type | What it needs stored |
|---|---|
| Sessions, minutes, goals | One record per contact: date, type, whether it counts, minutes, sources |
| Goals per period | Plan rules with effective dates |
| Cohort | One row per patient per week, with a status |
| Reconstructing a date | What each document claimed, its standing, and the reasoning applied |
| Progress | Distinct assessments; observations tagged with who said them |

That gives five record types. Anything beyond them needs its own justification. Authorizations, for example, are not needed by any question Backbone has named.

### Suggested order of decisions

Each constrains the next.

1. How correctness will be checked, including whether to write test documents for a second patient and a plan change.
2. The five record types and what each holds.
3. Where the model works and which model, settled by a small experiment.


---



## 12. Judgment calls and open decisions


| #   | Question                                                                  | My reading                                    | Alternative                                                              |
| --- | ------------------------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------ |
| 1   | Does the Jan 5 session count, given the plan was signed at 13:05 that day | Yes; the plan's episode starts Jan 5          | Exclude it; week 1 becomes 2 days, 90 min (still not met)                |
| 2   | Is week 4 judged in full, although the episode ends Friday Jan 30         | Yes, without prorating                        | Prorate, or mark partial weeks separately                                |
| 3   | Should Jan 26 be resolved in favour of D111                               | No; leave at 40–50                            | Yes; D111 gives a first-hand arrival time. Week 4 becomes not met at 145 |
| 4   | Does the group break apply to Rowan                                       | Yes; the notes say the whole group stopped    | None reasonable                                                          |
| 5   | Is the Jan 6 departure time reliable                                      | Yes, though it is when the badge was returned | Treat as approximate                                                     |
| 6   | Are "N. Ellis" and "Nora Ellis, LCSW" the same person                     | Not assumed                                   | Assume the same                                                          |
| 7   | Does a no-show use an authorization unit                                  | Not stated in the record                      | D001 defines a unit as "one scheduled group session"                     |
| 8   | Should week 2 be flagged as partly caused by the clinic                   | Yes, as context; verdict stays not met        | Report the verdict only                                                  |


---



## 13. Oddities in the materials

- The problem statement says "inpatient"; every document is outpatient.
- The problem statement says "multiple patients"; the supplied data has one.
- Therapists and prescribers change between batches with no handoff documented.
- The unsigned draft for Jan 27 was created at 09:45, before the session it describes.
- A charge was posted for a session the signed register records as a no-show.
- Appointment IDs (HG-A112) and the authorization number (HG-A260104-88) share a prefix.
- Group breaks are at 10:45–11:00 except Jan 12, which is 10:40–10:55.

---



## 14. Questions to expect in the design call

**About the abstraction**

- Show me how you got 60 minutes for the Jan 19 group.
- Why is week 4 "cannot determine" rather than "not met"?
- Where is the evidence that Rowan did not attend on Jan 27?
- What happens to this answer if I add this document?

**About the design**

- Why this representation and not plain retrieval?
- What does the model do, and what does code do?
- How do you know the extraction is right?
- What did you test, and what did you learn?
- What conflict types would your rules miss?

**About scale**

- What is the first bottleneck at a million documents, and which part of the code causes it?
- What does initial processing cost, and what does a new document cost?
- What is measured and what is estimated?
- How do collection-wide questions stay fast?
- What happens when you change the extraction prompt?

