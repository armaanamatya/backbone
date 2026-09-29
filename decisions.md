# Decisions log

Every interpretation made in order to count or calculate something. A decision is recorded here when the documents alone do not dictate the number and a different reading would be defensible or would change an answer.

**Status values**

- **Confirmed**: you have agreed to it.
- **Proposed**: my reading, waiting for your review.

**Rule for this file:** any new interpretation made while calculating gets added here before it is used.

## Summary

| ID | Decision | Changes an answer if reversed | Status |
|---|---|---|---|
| D-01 | Group breaks are subtracted from Rowan's minutes | Yes: week 1 becomes met | Confirmed |
| D-02 | Minutes use Rowan's actual presence, not the scheduled slot | Yes: week 1 becomes met | Proposed |
| D-03 | Only time with the patient present counts | Yes: week 4 becomes met | Proposed |
| D-04 | A lost connection is excluded; two calls are one session | Yes: session count and minutes | Proposed |
| D-05 | A signed correction replaces the value it names | Yes: Jan 19 minutes | Proposed |
| D-06 | A resent copy does not reinstate the old value | Yes: Jan 19 minutes | Proposed |
| D-07 | The Jan 26 conflict stays open as 40–50 minutes | Yes: week 4 verdict | Proposed |
| D-08 | A signed register outranks an unsigned draft and a charge | Yes: week 4 becomes met | Proposed |
| D-09 | One session per contact, however many documents describe it | Yes: session count | Proposed |
| D-10 | What counts as therapy follows the plan's definition | Yes: week 2 becomes met | Proposed |
| D-11 | A therapy day is a calendar day with at least one counted session | Yes: day counts | Proposed |
| D-12 | Sessions are placed in weeks by service date | Yes: possible misplacement | Proposed |
| D-13 | The Jan 5 session counts, though the plan was signed later that day | No: week 1 is not met either way | Proposed |
| D-14 | Week 4 is judged against the full requirement | Possibly | Proposed |
| D-15 | Verdicts under uncertainty use the lowest and highest possible totals | Yes: week 4 verdict | Proposed |
| D-16 | Phone calls and outreach messages are not therapy | No | Proposed |
| D-17 | Questionnaire reviews are not appointments | Yes: session and day counts | Proposed |
| D-18 | Assessments are distinct by completion date, not by document | Yes: symptom course | Proposed |
| D-19 | Where a note states patient minutes, the stated figure is used | No: all match the clock times | Proposed |
| D-20 | "The review period" means Jan 5–30 | Possibly | Proposed |
| D-21 | The Jan 6 badge-return time is accepted as departure | Possibly | Proposed |
| D-22 | Hours are minutes divided by 60, to two decimals | No | Proposed |
| D-23 | PHQ-9 severity bands are labelled as outside knowledge | No | Proposed |
| D-24 | "N. Ellis" and "Nora Ellis, LCSW" are not assumed to be one person | No | Proposed |
| D-25 | The reason a week fell short is reported as context only | No | Proposed |
| D-26 | Authorization units used are not calculated | No | Proposed |

---

## Minutes

### D-01: Group breaks are subtracted from Rowan's minutes

- **Status:** Confirmed
- **Decision:** For group sessions, the break is removed from Rowan's presence before counting minutes.
- **Basis:**
  - D004: "The whole group took a break from 10:45 to 11:00. No therapy was conducted during that interval."
  - D101: "there was no facilitated discussion, assigned therapeutic activity, or patient treatment during that interval."
  - D003 counts "patient-present therapy".
- **What is interpretation:** No document states Rowan's group minutes. The subtraction is my reading of the plan's wording.
- **Applies to:** Jan 6, 12, 19, 22, 29.
- **If reversed:** Jan 6 becomes 60 and week 1 becomes 155, which meets the goal. Group minutes rise from 300 to 375.

### D-02: Minutes use Rowan's actual presence, not the scheduled slot

- **Status:** Proposed
- **Decision:** Arrival and departure from the attendance record define presence. The scheduled slot is used only to identify the appointment.
- **Basis:** D108: "Group rows contain actual patient arrival and departure fields; the scheduled interval identifies the booked appointment."
- **Applies to:** Jan 6 (10:15–11:15), Jan 19 (10:00–11:15), Jan 22 (10:30–11:30).
- **If reversed:** Jan 6 becomes 75 after the break and week 1 becomes 170, which meets the goal.

### D-03: Only time with the patient present counts

- **Status:** Proposed
- **Decision:** When the clinician's session is longer than the patient's presence, only the patient's portion counts.
- **Basis:**
  - D113: "Partner only: 13:00–13:15. Rowan present with partner: 13:15–13:45, 30 minutes."
  - D003: "contacts with collateral informants only... do not contribute."
- **Applies to:** Jan 30 family session: 30 minutes, not 45.
- **If reversed:** Week 4 becomes 160–170, which meets the goal.

### D-04: A lost connection is excluded; two calls are one session

- **Status:** Proposed
- **Decision:** The Jan 21 video visit is one session of 45 minutes.
- **Basis:**
  - D106: "Connection was lost from 13:20–13:30; there was no therapeutic contact during that interval."
  - D106: "The reconnection continued the same clinical encounter under original appointment HG-A112."
- **Calculation:** 13:00–13:20 (20) + 13:30–13:55 (25) = 45.
- **If reversed:** Counting the gap gives 55 minutes. Counting each call gives 13 sessions.

### D-19: Where a note states patient minutes, the stated figure is used

- **Status:** Proposed
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

- **Open point:** What to do if a stated figure and the clock times disagree. It has not happened in this data.

### D-21: The Jan 6 badge-return time is accepted as departure

- **Status:** Proposed
- **Decision:** 11:15 is used as Rowan's departure on Jan 6.
- **Basis:** D005: "Departure was marked when Rowan returned their visitor badge."
- **What is interpretation:** The badge was returned at the desk, so Rowan may have left the room slightly earlier.
- **If reversed:** Jan 6 could be a few minutes below 45. Week 1 stays not met.

### D-22: Hours are minutes divided by 60, to two decimals

- **Status:** Proposed
- **Decision:** 585–595 minutes is reported as 9.75–9.92 hours.

---

## Conflicts between documents

### D-05: A signed correction replaces the value it names

- **Status:** Proposed
- **Decision:** Rowan's Jan 19 group departure is 11:15.
- **Basis:**
  - D103: "Patient departure for HG-E110 is 11:15, replacing the original roster value of 11:30."
  - D103 is signed, names the field, names the old value, and gives the cause.
  - D105 starts the individual session at 11:15 and says Rowan "came directly from the group room".
- **Why this is not "latest wins":** The correction wins because it is an explicit, signed replacement of one field, not because of its date.
- **If reversed:** Group minutes become 75, and Rowan is recorded in two sessions at once from 11:15 to 11:30.

### D-06: A resent copy does not reinstate the old value

- **Status:** Proposed
- **Decision:** D104, received Jan 26 and showing 11:30, changes nothing.
- **Basis:**
  - D104: "No correction sheet was included in this transmission."
  - D104: "The received copy contains no new clinician signature and records no additional visit."
  - Its only signature is the original one from Jan 19, 12:14, which predates the correction.
- **If reversed:** Same effect as reversing D-05.

### D-07: The Jan 26 conflict stays open as 40–50 minutes

- **Status:** Proposed
- **Decision:** Neither note is preferred. The session is carried as a range.
- **Basis:**
  - D110 (Mira Patel, signed 11:16): "09:00–09:50, 50 minutes."
  - D111 (Nora Ellis, signed 12:03): "Rowan entered the treatment room at 09:10, when we began the session."
  - Both are signed and final. Neither refers to the other. No correction exists.
- **Argument for the alternative:** D111 gives a first-hand arrival time, and D110 may have recorded the scheduled start.
- **If reversed in favour of D111:** Week 4 is 145 minutes, not met.
- **If reversed in favour of D110:** Week 4 is 155 minutes, met.
- **What would settle it:** A signed addendum from either clinician, or an independent arrival record.

### D-08: A signed register outranks an unsigned draft and a charge

- **Status:** Proposed
- **Decision:** Rowan did not attend the Jan 27 group. It contributes 0 minutes and no therapy day.
- **Basis:**
  - D108, signed Jan 27, 11:54: "Final roster confirms Rowan was absent for the entire group. No patient treatment contact occurred."
  - D112 draft: unsigned, created at 09:45, before the 10:00 session. "No clinician attestation or finalized patient-specific narrative appears in this draft."
  - D112 charge: a billing row, not a record of attendance.
- **Also recorded:** The charge for a no-show is reported as a finding.
- **If reversed:** Week 4 gains a day and up to 75 minutes, which meets the goal.

---

## Counting sessions and days

### D-09: One session per contact, however many documents describe it

- **Status:** Proposed
- **Decision:** Documents are evidence about a contact. They are never counted as contacts themselves.
- **Applies to:**
  - Jan 9 family: D007 and D008, one session.
  - Jan 26 individual: D110 and D111, one session.
  - Jan 19 group: D101, D102, D103, D104, one session.
- **Basis:** Matching encounter numbers (HG-E104, HG-E115, HG-E110).
- **If reversed:** Session count rises above 12.

### D-10: What counts as therapy follows the plan's definition

- **Status:** Proposed
- **Decision:** Individual, group, and family psychotherapy with Rowan present count. Nothing else does.
- **Basis:** D003: "Medication management, contacts with collateral informants only, and care coordination do not contribute."
- **Excluded:**

| Date | Contact | Minutes | Document |
|---|---|---|---|
| Jan 13 | Medication visit | 25 | D010 |
| Jan 16 | Partner only | 40 | D012 |
| Jan 23 | Care coordination | 20 | D109 |
| Jan 30 | Medication visit | 20 | D114 |

- **If reversed:** Counting the partner-only contact makes week 2 three days and 160 minutes, which meets the goal.

### D-11: A therapy day is a calendar day with at least one counted session

- **Status:** Proposed
- **Decision:** Jan 19 is one therapy day with two sessions.
- **Basis:** D003: "A therapy day is a calendar day on which Rowan participates in individual, group, or family psychotherapy."
- **Result:** 12 sessions on 11 days.

### D-16: Phone calls and outreach messages are not therapy

- **Status:** Proposed
- **Decision:** The calls on Jan 8 and Jan 15 and the message on Jan 27 are not sessions.
- **Basis:**
  - D015: "No therapy intervention was conducted."
  - D016: "The telephone contact was limited to confirming the cancellation and upcoming appointment information."
  - D108: "no clinical discussion occurred."

### D-17: Questionnaire reviews are not appointments

- **Status:** Proposed
- **Decision:** The PHQ-9 reviews on Jan 16 and Jan 30 add no session, day, or minutes.
- **Basis:**
  - D013: "no clinical appointment occurred at the time of review."
  - D115: "not a separate treatment appointment. No additional patient-contact interval is claimed in this entry."
- **If reversed:** Jan 16 would become a therapy day in week 2.

---

## Weeks and goals

### D-12: Sessions are placed in weeks by service date

- **Status:** Proposed
- **Decision:** The date the service happened decides the week. Signature, receipt, and export dates do not.
- **Applies to:** D008 (signed Jan 10 for Jan 9), D104 (received Jan 26 for Jan 19), D112 (produced Jan 30 for Jan 27).

### D-13: The Jan 5 session counts, though the plan was signed later that day

- **Status:** Proposed
- **Decision:** The 09:00 session on Jan 5 counts toward week 1.
- **Basis:** D003 gives the episode as "2026-01-05 through 2026-01-30". The plan was signed at 13:05.
- **If reversed:** Week 1 becomes 2 days and 90 minutes. Still not met.

### D-14: Week 4 is judged against the full requirement

- **Status:** Proposed
- **Decision:** The week of Jan 26–Feb 1 must reach 3 days and 150 minutes, although the episode ends on Friday Jan 30.
- **Basis:** The plan states the requirement per Monday–Sunday week and says nothing about partial weeks.
- **Alternative:** Prorate to 5 of 7 days, or report partial weeks separately.
- **Supporting fact:** D108 says no replacement appointment was booked within January.

### D-15: Verdicts under uncertainty use the lowest and highest possible totals

- **Status:** Proposed
- **Decision:**

| Condition | Verdict |
|---|---|
| Even the highest possible total is below the requirement | Not met |
| Even the lowest possible total reaches the requirement | Met |
| Anything else | Cannot determine |

- **Applies to:** Week 4: days are 3 either way; minutes are 145–155 against 150.

### D-20: "The review period" means Jan 5–30

- **Status:** Proposed
- **Decision:** When a question says "the review period" without dates, the episode dates are used.
- **Basis:** DEV-01 states "January 5–30, 2026". D003 gives the same episode dates.

### D-25: The reason a week fell short is reported as context only

- **Status:** Proposed
- **Decision:** Week 2 is not met. The clinic's cancellation on Jan 15 is reported alongside but does not change the verdict.
- **Basis:** DEV-03 asks whether delivered therapy met the goal, not who was responsible.

---

## Symptoms and assessments

### D-18: Assessments are distinct by completion date, not by document

- **Status:** Proposed
- **Decision:** There are three PHQ-9 assessments: Jan 5 (18), Jan 16 (14), Jan 30 (10).
- **Basis:**
  - D014: "copied result from the January 16 portal form... No newly completed patient questionnaire is included in this batch."
  - D013 mentions the score of 18 only as a comparison with intake.
- **If reversed:** The course reads 18, 14, 14, 10.

### D-23: PHQ-9 severity bands are labelled as outside knowledge

- **Status:** Proposed
- **Decision:** Bands such as "moderate", and thresholds for response and remission, are general conventions for the instrument. They are shown with a label saying they do not come from the record.
- **Basis:** No document in the set states a severity band.

---

## People and authorizations

### D-24: "N. Ellis" and "Nora Ellis, LCSW" are not assumed to be one person

- **Status:** Proposed
- **Decision:** They are kept as separate names.
- **Basis:** N. Ellis appears as desk staff in batch 1. Nora Ellis, LCSW appears as a clinician on Jan 26. No document links them.
- **Effect on numbers:** None.

### D-26: Authorization units used are not calculated

- **Status:** Proposed
- **Decision:** The notes report 8 authorized, 7 scheduled, 5 attended. No "units used" figure is given.
- **Basis:** D001 defines a unit as "one scheduled group session", and no document says whether a no-show or a clinic cancellation uses a unit.
