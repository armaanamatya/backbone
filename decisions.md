# Decisions log

Every interpretation made in order to count or calculate something. A decision is recorded here when the documents alone do not dictate the number and a different reading would be defensible or would change an answer.

**Status values**

- **Confirmed**: you have agreed to it.
- **Proposed**: my reading, waiting for your review.

**Confirmed 2026-09-29:** you confirmed all 34 decisions. D-07 and D-14 were confirmed last, when you decided the Jan 26 conflict (O-4) and the final week (O-5). The section "How the decisions go into code" at the end shows where each decision lands.

**Added 2026-09-29:** D-35 and D-36 were added while the answer key was being verified, and you confirmed both the same day. There are now 36 decisions and 16 rules.

**Rule for this file:** any new interpretation made while calculating gets added here before it is used.

**Verification, 2026-09-28:** seven review agents checked this file against the source documents. Entries whose content was wrong carry a "Corrected" line. Six others gained a missing "if reversed" line or a cross-reference. D-27 to D-34 were added because they were in use without being logged. No status was changed. Details are in `verification.md`.

## Summary

| ID | Decision | Changes an answer if reversed | Status | Goes in code as |
|---|---|---|---|---|
| D-01 | Group breaks are subtracted from Rowan's minutes | Yes: weeks 1 and 4 become met | Confirmed | Rule 5 |
| D-02 | Minutes use Rowan's actual presence, not the scheduled slot | Yes: week 1 becomes met | Confirmed | Rule 3 |
| D-03 | Only time with the patient present counts | Yes: week 4 becomes met | Confirmed | Rule 4 |
| D-04 | A lost connection is excluded; two calls are one session | Yes: session count and minutes | Confirmed | Rules 1, 5 |
| D-05 | A signed correction replaces the value it names | Yes: Jan 19 minutes | Confirmed | Rule 8 |
| D-06 | A resent copy does not reinstate the old value | Yes: Jan 19 minutes | Confirmed | Rule 9 |
| D-07 | The Jan 26 conflict stays open as 40 or 50 minutes | Yes: week 4 verdict | Confirmed | Rule 11 |
| D-08 | A signed register outranks an unsigned draft and a charge | Yes: week 4 becomes met | Confirmed | Rule 10 |
| D-09 | One session per contact, however many documents describe it | Yes: session count | Confirmed | Rule 1 |
| D-10 | What counts as therapy follows the plan's definition | Yes: weeks 2 and 4 become met | Confirmed | Plan value |
| D-11 | A therapy day is a calendar day with at least one counted session | Yes: day counts | Confirmed | Plan value |
| D-12 | Sessions are placed in weeks by service date | Yes: week 3 becomes not met, week 4 met | Confirmed | Rule 2 |
| D-13 | The Jan 5 session counts, though the plan was signed later that day | Yes: totals change; the week 1 verdict does not | Confirmed | Plan value |
| D-14 | Week 4 is judged against the full requirement | Yes: week 4 becomes met if prorated | Confirmed | Convention |
| D-15 | Verdicts under uncertainty use the lowest and highest possible totals | Yes: week 4 verdict | Confirmed | Rule 12 |
| D-16 | Scheduling calls and outreach messages are not therapy | Yes: session and day counts | Confirmed | Plan value |
| D-17 | Questionnaire reviews are not appointments | Yes: session and day counts | Confirmed | Plan value |
| D-18 | Assessments are distinct by completion date, not by document | Yes: symptom course | Confirmed | Rules 9, 13 |
| D-19 | Where a note states patient minutes, the stated figure is used | No: all match the clock times | Confirmed | Rule 14 |
| D-20 | "The review period" means Jan 5–30 | No, for Rowan; it cannot be fixed for other patients | Confirmed | Plan value |
| D-21 | The Jan 6 desk times are accepted as arrival and departure | Minutes only | Confirmed | Rule 3 |
| D-22 | Hours are minutes divided by 60, to two decimals | No | Confirmed | Convention |
| D-23 | PHQ-9 severity bands are labelled as outside knowledge | No | Confirmed | Convention |
| D-24 | "N. Ellis" and "Nora Ellis, LCSW" are not assumed to be one person | No | Confirmed | Rule 15 |
| D-25 | The reason a week fell short is reported as context only | No | Confirmed | Convention |
| D-26 | Authorization units used are not calculated | No | Confirmed | Left out |
| D-27 | A video session counts as patient-present | Yes: week 3 becomes not met | Confirmed | Rule 4 |
| D-28 | Partial attendance still counts as a session and a therapy day | Yes: weeks 1, 3 and 4 fall to 2 days | Confirmed | Rule 4 |
| D-29 | A session led by two clinicians counts the patient's minutes once | Yes: weeks 1 and 4 become met | Confirmed | Rule 1 |
| D-30 | The added Jan 19 individual session is a separate session | Yes: session count | Confirmed | Rule 1 |
| D-31 | Totals assume no therapy happened that is not in the record | Yes: weeks 2 and 4 | Confirmed | Convention |
| D-32 | Times equal to the scheduled times are accepted when the narrative supports them | Minutes only | Confirmed | Rule 3 |
| D-33 | Jan 16 is a collateral contact, not an appointment Rowan missed | Yes: missed-appointment count | Confirmed | Rule 4 |
| D-34 | Intervals exclude their end minute; breaks are subtracted only where they overlap presence | No, on this data | Confirmed | Rule 6 |
| D-35 | The speaker of an observation is the patient only when the sentence names the patient as its source | No figure or verdict. Six speaker labels in DEV-05 | Confirmed | Rule 16 |
| D-36 | A time in the header of a signed note is taken as actual, unless the note labels it scheduled | No verdict. The minutes of two contacts that do not count | Confirmed | Rule 3 |

---

## Minutes

### D-01: Group breaks are subtracted from Rowan's minutes

- **Status:** Confirmed
- **Decision:** For group sessions, the break is removed from Rowan's presence before counting minutes.
- **Basis:**
  - D004: "The whole group took a break from 10:45 to 11:00. No therapy was conducted during that interval."
  - D101: "there was no facilitated discussion, assigned therapeutic activity, or patient treatment during that interval."
  - D009 (Jan 12): "Group break: 10:40–10:55; no therapeutic activity occurred during the break."
  - D107 (Jan 22 and 29): "For both dates, the break was unstructured time without therapeutic activity or facilitator treatment."
  - D003 counts "patient-present therapy".
- **What is interpretation:** No document states Rowan's group minutes. The subtraction is my reading of the plan's wording.
- **Applies to:** Jan 6, 12, 19, 22, 29.
- **If reversed:** Every group gains 15 minutes. Group minutes rise from 300 to 375.

| Week | With breaks subtracted | Without | Verdict without |
|---|---|---|---|
| Jan 5–11 | 140 | 155 | Met |
| Jan 12–18 | 120 | 135 | Not met |
| Jan 19–25 | 180 | 210 | Met |
| Jan 26–Feb 1 | 145 or 155 | 160 or 170 | Met |

- **Corrected 2026-09-28:** the earlier entry gave the effect on week 1 only. Week 4 also changes. The Jan 12, 22 and 29 notes were added to the basis, since only the Jan 6 note says "whole group".

### D-02: Minutes use Rowan's actual presence, not the scheduled slot

- **Status:** Confirmed
- **Decision:** Arrival and departure from the attendance record define presence. The scheduled slot is used only to identify the appointment.
- **Basis:** D108: "Group rows contain actual patient arrival and departure fields; the scheduled interval identifies the booked appointment."
- **Applies to:** Jan 6 (10:15–11:15), Jan 19 (10:00–11:15), Jan 22 (10:30–11:30).
- **If reversed:** Jan 6, Jan 19 and Jan 22 each become 75 after the break. Week 1 becomes 170, which meets the goal. Week 3 becomes 225. The total becomes 660 or 670.
- **Corrected 2026-09-28:** the earlier entry gave Jan 6 only. `review-notes.md` had said 185 for the same mistake; that figure also left the break in.

### D-03: Only time with the patient present counts

- **Status:** Confirmed
- **Decision:** When the clinician's session is longer than the patient's presence, only the patient's portion counts.
- **Basis:**
  - D113: "Partner only: 13:00–13:15. Rowan present with partner: 13:15–13:45, 30 minutes."
  - D003: "contacts with collateral informants only... do not contribute."
- **Applies to:** Jan 30 family session: 30 minutes, not 45.
- **If reversed:** Week 4 becomes 160 or 170, which meets the goal.

### D-04: A lost connection is excluded; two calls are one session

- **Status:** Confirmed
- **Decision:** The Jan 21 video visit is one session of 45 minutes.
- **Basis:**
  - D106: "Connection was lost from 13:20–13:30; there was no therapeutic contact during that interval."
  - D106: "The reconnection continued the same clinical encounter under original appointment HG-A112."
- **Calculation:** 13:00–13:20 (20) + 13:30–13:55 (25) = 45.
- **If reversed:** Counting the gap gives 55 minutes. Counting each call gives 13 sessions.

### D-19: Where a note states patient minutes, the stated figure is used

- **Status:** Confirmed
- **Decision:** For the 7 sessions whose notes state the patient's minutes, that figure is used, after checking it against the clock times in the same note.
- **Check performed:**

| Date | Clock times | Computed | Stated |
|---|---|---|---|
| Jan 5 | 09:00–09:50 | 50 | 50 |
| Jan 9 | 14:00–14:45 | 45 | 45 |
| Jan 14 | 11:00–11:45 | 45 | 45 |
| Jan 19 | 11:15–11:45 | 30 | 30 |
| Jan 21 | 13:00–13:20, 13:30–13:55 | 45 | 45 |
| Jan 26 | 09:00–09:50 / 09:10–09:50 | 50 / 40 | 50 / 40 |
| Jan 30 | 13:15–13:45 | 30 | 30 |

- **If they disagree:** both figures are kept as alternatives and a conflict is opened, under rule 11. Decided 2026-09-29 (was O-15). It has not happened in this data.

### D-21: The Jan 6 desk times are accepted as arrival and departure

- **Status:** Confirmed
- **Decision:** 10:15 is used as Rowan's arrival and 11:15 as the departure on Jan 6.
- **Basis:**
  - D005: "Departure was marked when Rowan returned their visitor badge."
  - D005: "Reception directed them to the group room after check-in."
  - D005: "The desk records arrival and departure when members enter or leave the scheduled group."
- **What is interpretation:** Both times were recorded at the desk. Rowan may have entered the room slightly after 10:15 and left it slightly before 11:15. The group note (D004) does not mention the late arrival or the early departure.
- **If reversed:** Jan 6 could be a few minutes below 45, so 45 is the most it can be. Week 1 stays not met.
- **Corrected 2026-09-28:** the earlier entry covered the departure only.

### D-22: Hours are minutes divided by 60, to two decimals

- **Status:** Confirmed
- **Decision:** 585 or 595 minutes is reported as 9.75 or 9.92 hours.

---

## Conflicts between documents

### D-05: A signed correction replaces the value it names

- **Status:** Confirmed
- **Decision:** Rowan's Jan 19 group departure is 11:15.
- **Basis:**
  - D103: "Patient departure for HG-E110 is 11:15, replacing the original roster value of 11:30."
  - D103 is signed, names the field, names the old value, and gives the cause.
  - D105 starts the individual session at 11:15 and says Rowan "came directly from the group room".
- **Why this is not "latest wins":** The correction wins because it is an explicit, signed replacement of one field, not because of its date.
- **If reversed:** Group minutes become 75, and Rowan is recorded in two sessions at once from 11:15 to 11:30.

### D-06: A resent copy does not reinstate the old value

- **Status:** Confirmed
- **Decision:** D104, received Jan 26 and showing 11:30, changes nothing.
- **Basis:**
  - D104: "No correction sheet was included in this transmission."
  - D104: "The received copy contains no new clinician signature and records no additional visit."
  - Its only signature is the original one from Jan 19, 12:14, which predates the correction.
- **If reversed:** Same effect as reversing D-05.

### D-07: The Jan 26 conflict stays open as 40 or 50 minutes

- **Status:** Confirmed
- **Decision:** Neither note is preferred. The session is carried as two alternatives: 40 minutes (D111) or 50 minutes (D110).
- **Basis:**
  - D110 (Mira Patel, signed 11:16): "09:00–09:50, 50 minutes."
  - D111 (Nora Ellis, signed 12:03): "Rowan entered the treatment room at 09:10, when we began the session."
  - Both are signed and final. No correction exists.
  - Each note names the other clinician, so both describe the same encounter. Neither refers to the other's record, the scheduled time, a late arrival, or the ten minutes.
- **What is established:** Both notes place Rowan in session from 09:10 to 09:50. 40 minutes is agreed. Only 09:00–09:10 is disputed.
- **How the value is carried:** as "40 or 50", each figure tied to its note. No document supports a value in between. You confirmed this form on 2026-09-28.
- **Why it is not resolved toward D111:** that would need a rule such as "a note that records an arrival outranks one that does not". The rule would have been suggested by this one case. The answer still states that D111 records an observed arrival and D110 does not. You confirmed on 2026-09-29 that the conflict stays open (was O-4).
- **Argument for the alternative:**
  - D111 records an observed event: "Rowan entered the treatment room at 09:10".
  - D111 claims the whole encounter: "The full patient-contact interval for the encounter was 09:10–09:50."
  - D110 names no arrival or start event.
  - The Jan 19 roster (D102) shows a scheduled time entered in an "actual" field.
- **Limit of that argument:** No scheduled time for this appointment exists in the record, so it cannot be shown that D110's 09:00 was the booked start.
- **If reversed in favour of D111:** Week 4 is 145 minutes, not met.
- **If reversed in favour of D110:** Week 4 is 155 minutes, met.
- **What would settle it:** An independent arrival or check-in record, or a correction by the author of the note being changed. A schedule export would not, because it shows the booked slot and not the arrival. Who may settle a conflict is open item O-14.
- **Corrected 2026-09-28:** the earlier entry said "Neither refers to the other", which is wrong as worded, and suggested D110 "may have recorded the scheduled start", which the record cannot show.

### D-08: A signed register outranks an unsigned draft and a charge

- **Status:** Confirmed
- **Decision:** Rowan did not attend the Jan 27 group. It contributes 0 minutes and no therapy day.
- **Basis:**
  - D108, signed Jan 27, 11:54: "Final roster confirms Rowan was absent for the entire group. No patient treatment contact occurred."
  - D112 draft: unsigned, created at 09:45, before the 10:00 session. "No clinician attestation or finalized patient-specific narrative appears in this draft."
  - D112 charge: a billing row, not a record of attendance.
- **Also recorded:** The charge for a no-show is reported as a finding.
- **What counts as an attendance record:** a desk extract counts, even if the extract itself is unsigned. D005 says it was "Prepared from the signed reception attendance sheet". Decided 2026-09-29.
- **If reversed:**
  - Crediting the draft: week 4 gains a day and 75 minutes (the full session less the break), giving 220 or 230, which meets the goal. Sessions become 13 on 12 days.
  - Crediting the charge alone: week 4 gains a day and no minutes, because the charge carries no times. Week 4 stays "cannot determine".
- **Wording for the finding:** A group psychotherapy charge is posted for an encounter the signed attendance entry records as a no-show. The record does not show whether the charge was later reviewed or reversed. This is an inconsistency between documentation and billing, not a finding of improper billing.
- **Corrected 2026-09-28:** the earlier entry did not separate the draft from the charge.

---

## Counting sessions and days

### D-09: One session per contact, however many documents describe it

- **Status:** Confirmed
- **Decision:** Documents are evidence about a contact. They are never counted as contacts themselves.
- **Applies to:**
  - Jan 9 family: D007 and D008, one session.
  - Jan 26 individual: D110 and D111, one session.
  - Jan 19 group: D101, D102, D103, D104, one session.
- **Basis:** Matching encounter numbers (HG-E104, HG-E115, HG-E110).
- **If reversed:** Session count rises above 12. Minutes also double wherever each document carries its own minutes (see D-29).

### D-10: What counts as therapy follows the plan's definition

- **Status:** Confirmed
- **Decision:** Individual, group, and family psychotherapy with Rowan present count. Nothing else does.
- **Basis:** D003: "Medication management, contacts with collateral informants only, and care coordination do not contribute."
- **Excluded:**

| Date | Contact | Minutes | Document |
|---|---|---|---|
| Jan 13 | Medication visit | 25 | D010 |
| Jan 16 | Partner only | 40 | D012 |
| Jan 23 | Care coordination | 20 | D109 |
| Jan 30 | Medication visit | 20 | D114 |

- **If reversed:**
  - Counting the partner-only contact makes week 2 three days and 160 minutes, which meets the goal.
  - Counting the Jan 30 medication visit makes week 4 165 or 175 minutes, which meets the goal.
  - Counting the Jan 13 medication visit makes week 2 three days and 145 minutes, still not met.
  - Counting the Jan 23 coordination call makes week 3 200 minutes. It adds no day, because Rowan was not on the call.
- **Further basis:**
  - D012: "No patient-present psychotherapy occurred during this contact."
  - D003: "family work when Rowan is present".
- **Corrected 2026-09-28:** the earlier entry gave the partner-only effect only.

### D-11: A therapy day is a calendar day with at least one counted session

- **Status:** Confirmed
- **Decision:** Jan 19 is one therapy day with two sessions.
- **Basis:** D003: "A therapy day is a calendar day on which Rowan participates in individual, group, or family psychotherapy."
- **Result:** 12 sessions on 11 days.
- **If reversed:** Counting each session as a day gives 12 days, and week 3 has 4. No verdict changes.

### D-16: Scheduling calls and outreach messages are not therapy

- **Status:** Confirmed
- **Decision:** The calls on Jan 8 and Jan 15 and the message on Jan 27 are not sessions.
- **Why:** Each document says no therapy took place. The reason is what happened on the call, not that it was a call. A telephone contact in which psychotherapy was delivered would need its own decision.
- **Basis:**
  - D015: "No therapy intervention was conducted."
  - D016: "The telephone contact was limited to confirming the cancellation and upcoming appointment information."
  - D108: "no clinical discussion occurred."
- **If reversed:** Three sessions and three days are added (Jan 8, 15, 27). Week 2 reaches 3 days. The documents give no call durations, so minutes could not be calculated.
- **Corrected 2026-09-28:** the earlier entry said reversal changed nothing, and was worded as a rule about phone calls in general.

### D-17: Questionnaire reviews are not appointments

- **Status:** Confirmed
- **Decision:** The PHQ-9 reviews on Jan 16 and Jan 30 add no session, day, or minutes.
- **Basis:**
  - D013: "no clinical appointment occurred at the time of review."
  - D115: "not a separate treatment appointment. No additional patient-contact interval is claimed in this entry."
- **If reversed:** Jan 16 would become a therapy day in week 2.

---

## Weeks and goals

### D-12: Sessions are placed in weeks by service date

- **Status:** Confirmed
- **Decision:** The date the service happened decides the week. Signature, receipt, and export dates do not.
- **Applies to:**

| Document | Its own date | Service date it carries | Moves to another week if misread |
|---|---|---|---|
| D108 | Jan 30 | Jan 22, 27, 28, 29 | Yes: Jan 22 would move from week 3 to week 4 |
| D104 | Received Jan 26 | Jan 19 | Yes: a phantom group in week 4 |
| D014 | Received Jan 26 | Jan 16 (PHQ-9) | Yes: a false assessment in week 4 |
| D005 | Jan 12 | Jan 6, Jan 12 | Yes: Jan 6 would move from week 1 to week 2 |
| D008 | Signed Jan 10 | Jan 9 | No: same week |
| D112 | Jan 30 | Jan 27 | No: same week |

- **If reversed:** Placing the Jan 22 group by D108's date makes week 3 two days and 135 minutes, not met. Placing D104 by its receipt date adds a group to week 4, which then meets the goal.
- **Corrected 2026-09-28:** the earlier entry listed only documents that could not change a week.

### D-13: The Jan 5 session counts, though the plan was signed later that day

- **Status:** Confirmed
- **Decision:** The 09:00 session on Jan 5 counts toward week 1.
- **Basis:** D003 gives the episode as "2026-01-05 through 2026-01-30". The plan was signed at 13:05.
- **What is interpretation:** The note covers intake as well as therapy. It labels all 50 minutes as patient-present individual therapy and gives no split.
- **If reversed:** Week 1 becomes 2 days and 90 minutes, still not met. Totals change: 11 sessions, 4 individual, 10 days, and 535 or 545 minutes.
- **Corrected 2026-09-28:** the earlier summary said reversal changed no answer. It changes the answers to DEV-01 and DEV-02. Whether a plan takes effect from its episode start or its signature is open item O-13.

### D-14: Week 4 is judged against the full requirement

- **Status:** Confirmed
- **Decision:** The week of Jan 26–Feb 1 must reach 3 days and 150 minutes, although the episode ends on Friday Jan 30.
- **Basis:** The plan states the requirement per Monday–Sunday week and says nothing about partial weeks.
- **Alternative:** Prorate to 5 of 7 days, or report partial weeks separately.
- **Confirmed 2026-09-29 (was O-5):** the full requirement applies, and the week is labelled partial in the answer.
- **Supporting facts:**
  - D003 gives the episode as ending on Jan 30 and has no clause on partial weeks.
  - No record covers Jan 31 or Feb 1.
- **If reversed:** Prorating gives thresholds of about 107 minutes and 2.14 days. Week 4, at 3 days and 145 or 155 minutes, would be met whichever Jan 26 value is used.
- **A session after the episode ends:** it does not count toward the goal. It is reported separately and flagged. Decided 2026-09-29 (was O-12).
- **Corrected 2026-09-28:** the earlier entry had no reversal effect, and cited a sentence in D108 that is about one cancelled appointment.

### D-15: Verdicts under uncertainty use the lowest and highest possible totals

- **Status:** Confirmed
- **Decision:**

| Condition | Verdict |
|---|---|
| Even the highest possible total is below the requirement | Not met |
| Even the lowest possible total reaches the requirement | Met |
| Anything else | Cannot determine |

- **Applies to:** Week 4: days are 3 either way; minutes are 145 or 155 against 150.
- **If reversed:** Using the lower value gives not met. Using the higher value or a midpoint gives met.
- **Limit:** The lowest and highest totals assume the record is complete (see D-31).

### D-20: "The review period" means Jan 5–30

- **Status:** Confirmed
- **Decision:** When a question says "the review period" without dates, the episode dates are used.
- **Basis:** DEV-01 states "January 5–30, 2026". D003 gives the same episode dates.
- **If reversed:** No effect on this data. For any other patient the period must come from that patient's own episode dates, so this cannot be a fixed value in the system.

### D-25: The reason a week fell short is reported as context only

- **Status:** Confirmed
- **Decision:** Week 2 is not met. The clinic's cancellation on Jan 15 is reported alongside but does not change the verdict.
- **Basis:** DEV-03 asks whether delivered therapy met the goal, not who was responsible.

---

## Symptoms and assessments

### D-18: Assessments are distinct by completion date, not by document

- **Status:** Confirmed
- **Decision:** There are three PHQ-9 assessments: Jan 5 (18), Jan 16 (14), Jan 30 (10).
- **Basis:**
  - D014: "copied result from the January 16 portal form... No newly completed patient questionnaire is included in this batch."
  - D013 mentions the score of 18 only as a comparison with intake.
- **If reversed:** The course reads 18, 14, 14, 10.

### D-23: PHQ-9 severity bands are labelled as outside knowledge

- **Status:** Confirmed
- **Decision:** Bands such as "moderate", and thresholds for response and remission, are general conventions for the instrument. They are shown with a label saying they do not come from the record.
- **Basis:** No document in the set states a severity band.

---

## People and authorizations

### D-24: "N. Ellis" and "Nora Ellis, LCSW" are not assumed to be one person

- **Status:** Confirmed
- **Decision:** They are kept as separate names.
- **Basis:** N. Ellis appears as desk staff in batch 1. Nora Ellis, LCSW appears as a clinician on Jan 26. No document links them.
- **Effect on numbers:** None.

### D-26: Authorization units used are not calculated

- **Status:** Confirmed
- **Decision:** The notes report 8 authorized, 7 scheduled, 5 attended. No "units used" figure is given.
- **Basis:** D001 defines a unit as "one scheduled group session", and no document says whether a no-show or a clinic cancellation uses a unit.
- **Possible values:** 5 if only attended groups use a unit, 6 if the no-show also does, 7 if every scheduled group does. Read literally, D001's definition points to 7.

---

## Added after verification

These eight were in use in the numbers without being logged. All were confirmed on 2026-09-29.

### D-27: A video session counts as patient-present

- **Status:** Confirmed
- **Decision:** The Jan 21 video session counts toward therapy days and minutes. As a rule: presence does not depend on how the patient attends, unless the plan says otherwise.
- **Basis:**
  - D003 counts "patient-present" therapy and does not say how the patient must attend.
  - D106 records the session as "Individual psychotherapy" by video and states "Total patient psychotherapy contact: 45 minutes."
  - D012: "Rowan did not join in person, by telephone, or by video." This treats video as one way of being present.
- **If reversed:** Week 3 becomes 2 days (Jan 19, 22) and 135 minutes, not met. Sessions become 11. The total becomes 540 or 550.

### D-28: Partial attendance still counts as a session and a therapy day

- **Status:** Confirmed
- **Decision:** A session Rowan attended for part of its length counts as one session and makes that date a therapy day. Only the minutes are reduced. As a rule: any counted minutes make a session and a therapy day, unless the plan sets a minimum.
- **Basis:** D003: "A therapy day is a calendar day on which Rowan participates in individual, group, or family psychotherapy." The plan sets no minimum length.
- **Applies to:**

| Date | Session | Rowan's minutes | Full session |
|---|---|---|---|
| Jan 6 | Group | 45 | 75 |
| Jan 19 | Group | 60 | 75 |
| Jan 22 | Group | 45 | 75 |
| Jan 30 | Family | 30 | 45 |

- **If reversed:** Under a rule requiring full attendance, those four sessions drop out. Weeks 1, 3 and 4 each fall to 2 days and are not met. Sessions become 8.

### D-29: A session led by two clinicians counts the patient's minutes once

- **Status:** Confirmed
- **Decision:** When two clinicians each write a note for the same session, Rowan's minutes are counted once.
- **Basis:** The plan counts the patient's therapy minutes. Both notes in each pair carry the same encounter number.
- **Applies to:** Jan 9 (D007, D008) and Jan 26 (D110, D111).
- **If reversed:** Jan 9 becomes 90 and week 1 becomes 185, which meets the goal. Jan 26 becomes 90 and week 4 becomes 195, which meets the goal.

### D-30: The added Jan 19 individual session is a separate session

- **Status:** Confirmed
- **Decision:** Jan 19 has two sessions: the group and the individual session that followed it.
- **Basis:**
  - D105 has its own encounter number (HG-E111), a different clinician, and says "This visit was added".
  - D103 calls it "the separate individual appointment".
- **What is interpretation:** D105 says Rowan "came directly from the group room", so the two could be read as one continuous contact.
- **If reversed:** 11 sessions, 4 individual. Jan 19 becomes one contact of 90 minutes. Minutes and verdicts do not change.

### D-31: Totals assume no therapy happened that is not in the record

- **Status:** Confirmed
- **Decision:** A date with no document is counted as a date with no therapy. Verdicts are stated as "on the available record".
- **Basis:** None in the documents. This is an assumption.
- **What the record does not cover:**
  - D006 is the only schedule export. Its view is "appointments January 5–16, 2026".
  - No schedule export exists for Jan 19–30.
  - No document covers Jan 17–18, Jan 24–25, or Jan 31–Feb 1.
- **If reversed:** Week 2 could not be called "not met" with certainty. One 45-minute session on Jan 17 or 18 would give 3 days and 165 minutes, which meets the goal.
- **Tension:** `review-notes.md` lists "silence is not a negative" as a kind of reasoning the system must do. This decision is where the hand answers depart from it.

### D-32: Times equal to the scheduled times are accepted when the narrative supports them

- **Status:** Confirmed
- **Decision:** Where an arrival or departure equals the scheduled opening or closing, it is accepted if the document's own wording supports it.
- **Applies to:**

| Date | Time | Support |
|---|---|---|
| Jan 12 | 10:00–11:30 | D005: "Rowan checked in before the group began and remained until the group was released." |
| Jan 19 | Arrival 10:00 | D102: "Rowan was present for the opening check-in." D103: "Patient arrival remains 10:00." |
| Jan 29 | 10:00–11:30 | D108: "Rowan was present from opening through closing." |

- **What is interpretation:** D102 says "Arrival and departure fields were entered at roster close." That process produced the wrong 11:30 departure on Jan 19.
- **If reversed:** Minutes for those dates become uncertain. No verdict can be recalculated without other evidence.

### D-33: Jan 16 is a collateral contact, not an appointment Rowan missed

- **Status:** Confirmed
- **Decision:** The Jan 16 contact is counted as a partner-only contact. It is not counted among Rowan's no-shows or cancellations. It is reported separately as an appointment that went ahead without Rowan.
- **Basis:**
  - D006 lists the appointment type as "Family collateral" and says it "was retained as a partner collateral contact after Rowan could not attend."
  - D012: "Casey attended the arranged contact after Rowan advised the office that they could not participate."
- **If reversed:** Patient cancellations become 2. Therapy minutes and verdicts do not change.

### D-34: Intervals exclude their end minute; breaks are subtracted only where they overlap presence

- **Status:** Confirmed
- **Decision:**
  - A session from 10:00 to 11:15 covers the minutes up to 11:15 and not 11:15 itself. A departure at 11:15 and a start at 11:15 do not overlap.
  - Only the part of a break that falls inside Rowan's presence is subtracted.
- **Basis:** Convention. Nothing in the record states it.
- **If reversed:** No change on this data, because every break falls wholly inside Rowan's presence. With an arrival at 10:50 during a 10:45–11:00 break, 10 minutes would be subtracted and not 15.

---

## Added while verifying the answer key

### D-35: The speaker of an observation is the patient only when the sentence names the patient as its source

- **Status:** Confirmed 2026-09-29
- **Decision:**
  - The speaker of an observation is the person the sentence itself names as the source, as in "Rowan reported" or "They described".
  - Where the sentence names no one, the speaker is the author of the note.
  - "Clinician" as a speaker means the clinician who signed the note states it and the sentence names no other source. It does not mean the clinician observed it.
- **Basis:** Paragraphs in this record change speaker partway, so the sentence that opens a paragraph does not settle the sentences after it.
  - D105 opens a paragraph with "Rowan denied current suicidal thoughts" and ends it with the clinician's judgment: "Persistent avoidance and disrupted sleep continue to interfere with resuming a usual work routine."
  - D002 has "Rowan described waking in the night" followed by the clinician's inference: "Daytime fatigue appears to make avoidance more likely."
- **What is interpretation:** For the six sentences below, the patient is the likelier source of the information. Sleep at home is something a clinician learns from the patient. D114 also calls its content "the patient's report". The record does not attribute the sentences, so the label follows the sentence and not the likelier source.
- **Applies to:**

| Table in DEV-05 | Date | Sentence | Speaker |
|---|---|---|---|
| Anxiety | Jan 5 | D002: "Worry increases when thinking about returning to work after a recent leave." | Clinician |
| Sleep | Jan 14 | D011: "Sleep remains interrupted" | Clinician |
| Sleep | Jan 26 | D110: "Sleep remained uneven" | Clinician |
| Mood | Jan 30 | D114: "Mood felt less persistently low than earlier in the month" | Clinician |
| Anxiety | Jan 30 | D114: "anxiety remained noticeable when anticipating contact with work" | Clinician |
| Sleep | Jan 30 | D114: "Sleep was still variable." | Clinician |

- **Alternative:** An unattributed sentence takes the speaker of the paragraph around it. This asks the reader to judge where the patient's account stops.
- **If reversed:** All six rows become Patient. No figure or verdict changes. Observations are matched by patient, date, speaker and wording, so the key and the system must use the same reading.

### D-36: A time in the header of a signed note is taken as actual, unless the note labels it scheduled

- **Status:** Confirmed 2026-09-29
- **Decision:** Where a signed note for a contact that was held gives an interval in its header without calling it scheduled or actual, the interval is taken as the actual time.
- **Basis:** Notes in this record label a scheduled time when they give one.
  - D004: "Group scheduled 10:00–11:30 local"
  - D009: "Scheduled group 10:00–11:30 local"
  - D101: "Scheduled group: 10:00–11:30."
- **Applies to:**

| Date | Contact | Header | Used for |
|---|---|---|---|
| Jan 16 | HG-E109, partner only | D012: "14:00–14:40 local" | 40 minutes with the partner |
| Jan 23 | HG-E114, care coordination | D109: "09:00–09:20" | 20 minutes between professionals |
| Jan 9 | HG-E104, family therapy | D007: "14:00–14:45 local" | The interval only. The 45 minutes are stated in the note |

- **What is interpretation:** D012 states no duration, and its interval equals the scheduled slot in D006. D109 has no schedule to compare with.
- **Limit:** The rule covers signed notes of a contact that was held. D015 is a scheduling log for a no-show, and its header interval, 11:00–11:45, is the booked slot.
- **If reversed:** Jan 16 and Jan 23 have no minutes. No counted session depends on a time of this kind, so no total or verdict changes. The time in contacts that do not count could not be given in full.

---

## How the decisions go into code

The problem statement forbids "manually encoding patient facts or answers". Each decision is therefore sorted into one of four bins. Confirmed 2026-09-29.

| Bin | Count | Goes in code |
|---|---|---|
| General rule | 24 decisions, which reduce to 16 rules | Yes |
| Value read from a document | 6 | Yes, as data read from the plan |
| Reporting convention | 5 | Yes |
| Left out | 1 | No |

Facts about Rowan are in none of these bins. "The Jan 19 departure is 11:15" is never typed into code. It is what the rules produce when they run on the documents.

**The test for a rule:** would it be right for another patient at another clinic, and would it exist if the answer were different?

### The 16 rules

| # | Rule | From |
|---|---|---|
| 1 | Documents describe the same contact when they share an encounter or appointment number. Failing that, they match on patient, date, service class and overlapping time. One contact is one session, however many documents or calls describe it | D-04, D-09, D-29, D-30 |
| 2 | A contact belongs to the week of its service date. Signature, receipt and export dates never place it | D-12 |
| 3 | Minutes come from actual times. A scheduled time identifies the appointment and is never counted. A time in the header of a signed note is taken as actual, unless the note labels it scheduled | D-02, D-21, D-32, D-36 |
| 4 | Only intervals with the patient present count. Presence does not depend on how the patient attends, and any counted minutes make a session and a therapy day, unless the plan says otherwise. A contact held without the patient is recorded as held with the patient absent, not as a missed appointment | D-03, D-27, D-28, D-33 |
| 5 | An interval that a document says had no therapy is removed, and only where it overlaps the patient's presence | D-01, D-04 |
| 6 | An interval runs up to its end time and does not include it | D-34 |
| 7 | Different documents can each supply a different detail of one contact, and the details are combined | New |
| 8 | A signed correction that names the contact, the field and the old value replaces that value | D-05 |
| 9 | A copy, resend or import carries the authority and date of its original | D-06, D-18 |
| 10 | Attendance is established by an attendance record or a signed clinical note. A draft, a schedule status or a charge cannot establish it. A charge without established attendance is reported as a finding | D-08 |
| 11 | When two records of equal standing disagree and neither corrects the other, both values are kept as alternatives and the conflict stays open. Anything the rules do not recognize also stays open | D-07 |
| 12 | A verdict is "met" only if every alternative meets the requirement, "not met" only if none does, and "cannot determine" otherwise | D-15 |
| 13 | An assessment is identified by patient, instrument and completion time, plus the form ID where present. Mentions of an earlier score add nothing | D-18 |
| 14 | Minutes are calculated from clock times. Stated minutes are checked against them, and a mismatch opens a conflict | D-19 |
| 15 | Two names are treated as one person only when a document links them | D-24 |
| 16 | The speaker of an observation is the person the sentence names as its source. Where it names no one, the speaker is the author of the note | D-35 |

Rules 8 to 11 are the conflict rules, applied in that order. Retractions, chained corrections and summary documents are not recognized, so under rule 11 they stay open.

### Values read from the plan

| Value | From |
|---|---|
| The thresholds: 3 days and 150 minutes | D-10 |
| Which classes of service count, and which are excluded | D-10, D-16, D-17 |
| What makes a therapy day | D-11 |
| The week definition: Monday to Sunday | D-12 |
| The episode dates, used as the default review period | D-20 |
| The date the plan takes effect | D-13 |

D-16 and D-17 are not separate rules. A scheduling call and a questionnaire review are classes the plan does not count.

### Reporting conventions

| Convention | From |
|---|---|
| Hours are minutes divided by 60, to two decimals | D-22 |
| Anything not from the record is labelled as outside knowledge | D-23 |
| The reason a week fell short is given as context and does not change the verdict | D-25 |
| Every answer says its totals cover the documented record, and names any period with no document | D-31 |
| A week that runs past the end of the episode is labelled partial | D-14 |

### Left out

D-26, authorization units. Authorizations are not stored.

### Duplicates

| Level | How they are caught |
|---|---|
| The file | Identical content is skipped before any model call |
| The facts | Contacts by rule 1, assessments by rule 13, observations by patient, date, speaker and wording |
