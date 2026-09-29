# Verification findings

Produced 2026-09-28. Seven independent review agents (Opus) checked `review-notes.md`, `decisions.md` and `discussions.md` against the 31 source documents, the problem statement and `questions.json`. This file is the merged result.

**Nothing in `review-notes.md` or `decisions.md` has been changed.** Every correction and every new decision below is proposed and waits for your approval.

**How to read the "Checked" column**

| Mark | Meaning |
|---|---|
| Source | I read the source line myself after the agent reported it |
| Recomputed | I redid the arithmetic myself |
| 2+ agents | Two or more agents reported it independently; I did not re-read the source |
| Agent only | One agent reported it; not re-checked |

**Agents**

| # | Scope |
|---|---|
| 1 | Fact-check of batch 1 (D001–D016), weeks 1–2 |
| 2 | Fact-check of batch 2 (D101–D115), weeks 3–4 |
| 3 | Problem statement and `questions.json` coverage |
| 4 | Consistency across the three files; arithmetic; unlogged interpretations |
| 5 | Red team: unseen questions and documents |
| 6 | Scale, evaluation, operations |
| 7 | Clinical reviewer acting as devil's advocate on every decision |

Contents

1. What held up
2. Errors found, and proposed corrections
3. Interpretations that were never logged
4. The one real disagreement: Jan 26
5. Facts in the documents that the notes missed
6. Problem statement requirements the notes did not capture
7. Gaps in the hand-worked answers
8. What the five record types cannot hold
9. Conflict types, and what extraction must capture
10. New documents with no defined behaviour
11. Unseen questions most likely to be asked
12. Design decisions missing from section 11
13. Evaluation: checks that need no answer key
14. Scale
15. Scope against the 2–5 hour budget
16. Claims not verified

---

## 1. What held up

| Item | Result | Checked |
|---|---|---|
| Weekly minutes 140, 120, 180, 145 or 155 | Correct | 4 agents derived them independently |
| Weekly verdicts: not met, not met, met, cannot determine | Correct under the logged decisions | 4 agents |
| 12 sessions (5 individual, 5 group, 2 family) on 11 days | Correct | 4 agents |
| Totals 585 or 595 minutes; 9.75 or 9.92 hours | Correct | 3 agents |
| PHQ-9: 18, 14, 10; three distinct assessments | Correct | 3 agents |
| Document index (section 3), all 31 rows | Correct, one wording issue on D108 | Agents 1, 2 |
| Quotes attributed to source documents | All verbatim except three (section 2) | Agents 1, 2 |
| Counts in prose: 26 decisions, 36 reasoning items, eight kinds | Correct; each of the 36 is assigned exactly once | Agent 4 |
| Problem statement text after your highlighting | Unchanged apart from one stray tab | Agent 3 |
| All 26 decisions | Judged sound; none overturned | Agent 7 |

No weekly verdict and no headline number was wrong.

---

## 2. Errors found, and proposed corrections

None of these has been applied. "Says" is the current wording in the file. "Should say" is the proposed correction.

### In `decisions.md`

| Decision | Says | Should say | Checked |
|---|---|---|---|
| D-01 | Reversing makes week 1 met | Also makes week 4 met (160 or 170) and lifts weeks 2 and 3 to 135 and 210 | Recomputed |
| D-02 | Reversal effect listed for week 1 only | Also raises Jan 19 and Jan 22 to 75 each; total 660 or 670 | Recomputed |
| D-07 | "Neither refers to the other" | Each note names the other clinician. Neither refers to the other's record or explains the ten minutes | Source |
| D-07 | Alternative argued that D110 "may have recorded the scheduled start" | No scheduled time for that appointment exists in the record, so this cannot be shown | Source |
| D-08 | Draft or charge would make week 4 met | The draft would (75 minutes). The charge alone adds a day and no minutes | Source |
| D-10 | Reversal effect listed for week 2 only | Counting the Jan 30 medication visit makes week 4 met (165 or 175) | Recomputed |
| D-12 | Listed D008, D104, D112 | None of those can move a session to another week. The risk is D108 (dated Jan 30, carries Jan 22) and D104 | Recomputed |
| D-13 | "No" change if reversed | Weekly verdict holds; totals become 11 sessions, 10 days, 535 or 545 minutes | Recomputed |
| D-14 | "Possibly" | Prorating gives a threshold near 107 minutes, so week 4 is met either way | Recomputed |
| D-14 | Supporting fact: no replacement booked in January | That sentence is about one cancelled appointment. The real basis is the plan's episode end | Source |
| D-16 | "No" change if reversed; worded as "phone calls are not therapy" | Counting them adds 3 sessions and 3 days. The basis is each document's own statement, not the channel | Source |
| D-21 | Covers departure only; summary "Possibly" | Cover arrival too; effect is on minutes only | Source |
| D-11, D-15, D-20 | No "if reversed" line | Add one to each | Recomputed |

### In `review-notes.md`

| Location | Says | Should say | Checked |
|---|---|---|---|
| Section 5 mistakes table | Scheduled time for Jan 6 gives 185 | 170. It is 185 only if the break is also left in | Recomputed |
| Section 5 mistakes table | Medication visit gives 3 days | Add: minutes stay at 120, so still not met | Recomputed |
| Section 5 mistakes table | Seven verdict-flipping mistakes are missing | Add them (listed below) | Recomputed |
| Section 6, DEV-05 | "every note describes [sleep] as inconsistent" | Never described as stable. One note uses "inconsistent"; one records a single improved night | Source |
| Section 8.5 | "No medication change was made." | "No medication change was made today." | Source |
| Section 8.5 work steps | Seven rows | Add three steps: Jan 6, Jan 12, Jan 23 | Source |
| Section 8.2 | Partner-only time 40 | 40 on Jan 16 plus 15 on Jan 30 | Source |
| Section 8.3 | "Which weeks depend on unresolved documentation" tagged PS | Tagged Likely. The problem statement asks about patients, which is in 8.6 | Agent 3 |
| Section 8.7 | Seven people | Add Daniel Shaw (outside social worker) and Leah Chen's correction | Agent 2 |
| Section 5.10 | Quote attributed to the authorization letter | It is in the desk entry added to the letter on Jan 5 | Source |
| Section 3 | D108 "Signed register" | Register extract with three signed attendance entries and one unsigned scheduling entry | Source |
| Section 2 | Batch 1 date style "2026-01-05" | Batch 1 mixes three styles | Agent 1 |
| Section 9 | Session after Jan 30 "may raise" week 4 | Undecided; conflicts with D-20. Open item O-12 | Agents 2, 4, 5 |
| Section 9 | New 11:30 record makes Jan 19 unresolved | Add: week 3 is met either way, and D105 independently supports 11:15 | Recomputed |
| Section 9 | Addendum "from either clinician" settles Jan 26 | Who may settle it is undecided. Open item O-14 | Agents 4, 5 |
| Section 10 | "$0.07 per document measured... about $36K" | Label as unusable: from the deleted build, per call not per document, arithmetic gives $35K | Recomputed |
| Section 11 | RAG: "the FAQ warns against it" | The FAQ says "Retrieval may be useful" and recommends thinking beyond it | Source |
| Section 11 | Authorizations "not needed by any question" | Remove. Contradicted by sections 5.10, 6, 8.1 and D-26 | 2+ agents |
| Section 12 | Break alternative: "None reasonable" | Some programs count breaks; rejected here on the documents' own wording | Agent 7 |
| Section 1 | Quote spliced from two sentences | Quote both sentences separately | Source |
| Section 1 | Eight requirements missing | Add them (section 6 of this file) | Source |

### Mistakes missing from the section 5 table

| Mistake | Effect | Checked |
|---|---|---|
| Counting both Jan 9 notes as two sessions | Week 1 becomes 185, wrongly met | Recomputed |
| Counting the Jan 8 no-show at its scheduled 45 minutes | Week 1 becomes 4 days and 185, wrongly met | Recomputed |
| Counting the cancelled Jan 15 group from the schedule | Week 2 becomes 3 days and 195, wrongly met | Recomputed |
| Summing both Jan 26 notes | 13 sessions; week 4 becomes 195, wrongly met | Recomputed |
| Placing the Jan 22 group by the register's Jan 30 date | Week 3 becomes 2 days and 135, wrongly not met | Recomputed |
| Placing the resent roster on its Jan 26 receipt date | Week 4 gains a phantom group, wrongly met | Recomputed |
| Treating the video session as not patient-present | Week 3 becomes 2 days and 135, wrongly not met | Recomputed |

---

## 3. Interpretations that were never logged

Each is being used in a number without a decision behind it. They are proposed for `decisions.md` with status Proposed, and have not been added.

| Proposed ID | Interpretation | If reversed | Found by |
|---|---|---|---|
| D-27 | A video session counts as patient-present | Week 3 becomes 2 days and 135 minutes, not met | Agents 2, 5, 7 |
| D-28 | Partial attendance still counts as a session and a therapy day | Under a full-attendance rule, weeks 1, 3 and 4 each fall to 2 days | Agents 4, 7 |
| D-29 | A session led by two clinicians counts the patient's minutes once | Week 1 becomes 185 and week 4 becomes 195, both met | Agents 2, 7 |
| D-30 | The added Jan 19 individual session is a separate session | 11 sessions; Jan 19 becomes one contact of 90 minutes | Agents 4, 7 |
| D-31 | Totals assume no therapy happened that is not in the record | Weeks 2 and 4 become "not met on the available record" | Agents 1, 7 |
| D-32 | Arrival and departure times that equal the scheduled times are accepted when the narrative supports them | Jan 12, 19 and 29 minutes become uncertain | Agents 2, 7 |
| D-33 | Jan 16 is a collateral contact, not an appointment Rowan missed | Missed or cancelled count rises by one | Agents 1, 4 |
| D-34 | Intervals exclude their end minute; a break is subtracted only where it overlaps presence | An 11:15 departure and 11:15 start would overlap | Agent 4 |

Interpretations noted but not logged, because they cannot change a number on this data: percentage rounding, a single local time zone, the partner treated as a "collateral informant", "20 scheduled encounters" being a count of encounter IDs, and the unnamed "treating clinician" on Jan 19 taken to be Mira Patel.

---

## 4. The one real disagreement: Jan 26

Two agents read both notes closely and reached different conclusions. This is open item O-4 and is yours to decide.

| | Keep open | Open, leaning 40 |
|---|---|---|
| Held by | Agent 7 (clinical reviewer) | Agent 2 (batch 2 fact-check) |
| Main argument | Both notes are signed and final. Nothing in the record ranks one above the other | The second note records an observed event and claims the whole encounter; the first gives a slot-shaped time and no event |
| Supporting point | The figures straddle 150 exactly. The Jan 19 correction shows how the authors write a conflict they mean to be resolved | The Jan 19 roster already shows a scheduled time entered in an "actual" field |
| Week 4 | Cannot determine | Not met at 145 if resolved |

**What both agree on**

- 40 minutes is established: both notes place Rowan in session from 09:10 to 09:50. Only 09:00–09:10 is disputed.
- The value is "40 or 50", not "40–50". No document supports 45.
- No scheduled time for this appointment exists in the record. Batch 1 has a schedule export; batch 2 does not.
- The notes' description of the two records as "equally valid" understates the difference between them.
- "Primary" and "second" appear only in the file names, not in either document.

**What would settle it:** an arrival or check-in record, or a correction by the author of the note being changed. A schedule export would not, since it shows the booked slot and not the arrival.

---

## 5. Facts in the documents that the notes missed

### Could affect an answer

| Fact | Source | Why it matters | Checked |
|---|---|---|---|
| Nothing covers Jan 17–18. The schedule export's view is "January 5–16" | D006 | Week 2 "not met" rests on silence. One 45-minute session would meet the goal | Source |
| No schedule export exists for batch 2 | — | Scheduled times for Jan 19–30 are mostly unknown | 2+ agents |
| The Jan 19 roster says "Arrival and departure fields were entered at roster close" | D102 | The 10:00 arrival came from the same process as the wrong 11:30 | Source |
| The correction cites a "room-transfer record" that was not supplied | D103 | The correction's key evidence is missing from the set | Source |
| The authorization, received Jan 4, refers to a "submitted" treatment plan; the only plan was signed Jan 5 | D001, D003 | Bears on "one plan, no amendment" | Source |
| The Jan 28 register entry was "Entered by Ana Reed", not signed by a clinician | D108 | The register is not uniformly signed | Source |
| The only source for Jan 6 and Jan 12 presence is an unsigned desk extract | D005 | A blunt "signed outranks unsigned" rule would weaken those minutes | Source |
| The Jan 12 break note lacks the "whole group" wording | D009 | D-01's basis did not quote it | Source |
| Five sessions have a note but no attendance record | D105, D106, D110/D111, D113, D114 | Presence for those rests on the clinician's note alone | Agent 2 |

### Bear on narrative answers

| Fact | Source | Checked |
|---|---|---|
| Accounts differ on who started the added Jan 19 session: the facilitator "arranged" it, or Rowan "requested additional help" | D101, D102 | Source |
| The group's "worked example involving an unanswered work email" was the facilitator's, not Rowan's | D101 | Source |
| The Jan 30 questionnaire was completed at 12:42, "before the afternoon appointment", yet Rowan was absent from the family session until 13:15 | D115, D113 | Source |
| Week 2 has no explicit safety statement | — | Agent 5 |
| The treatment plan's three clinical goals appear nowhere in the notes | D003 | Source |
| The plan says "Adjust the schedule when clinically indicated or when access barriers arise" | D003 | Source |
| No diagnosis code, drug name or dose appears anywhere | — | Agent 1 |

### Identity

| Fact | Source | Checked |
|---|---|---|
| The partner, Casey Mercer, shares the patient's surname and appears in six documents | D007, D008, D012, D113 and others | Source |
| N. Ellis imported the PHQ-9 summary at 07:44 on Jan 26, the same morning Nora Ellis co-led a session | D014, D111 | Agent 2 |

---

## 6. Problem statement requirements the notes did not capture

All quotes confirmed against the extracted text.

| Requirement | Status in the notes |
|---|---|
| "An organized representation of the patient's course of care... We should be able to inspect it, understand how it represents the relevant evidence, and trace its contents back to their sources." | Absent from section 1 |
| "Pay close attention to what the questions require: reconciling evidence across documents, calculating quantities over time, and distinguishing established conclusions from uncertainty." | Dropped |
| "demonstrate how it reuses work across questions and runs" | Only reuse across questions was captured |
| "reliable, auditable, and straightforward to extend" | "Extend" never mentioned |
| "State any assumptions that materially affect your answer." | Absent |
| "Document incomplete work and tradeoffs." | Absent |
| "You do not need to build a universal clinical review system." | Absent |
| "Prioritize a working end-to-end implementation, inspectable outputs, and meaningful checks." | Absent |

Two of these are passages you highlighted.

**A mismatch in the materials.** The problem statement says the questions in `questions.json` cover cohort and plan-change questions. They do not. This suggests Backbone's own test set has several patients and a plan change.

**Deliverables with no plan behind them**

| Deliverable | Status |
|---|---|
| Execution logs | No plan |
| Benchmark results | No plan |
| Measured figures kept separate from estimates | The only cost figure cannot be submitted as measured |
| Format of the five answers | Undecided |
| Commands to process, add documents, ask, and trace | Not designed |
| Setup the interviewers can run themselves | Blocked by O-8 |
| README: the tested design decision | No experiment defined |
| README: first bottleneck at a million documents | Not named |

---

## 7. Gaps in the hand-worked answers

| Question | Gap |
|---|---|
| DEV-01 | No per-session source table. The list of records that could distort the count omits the no-show and cancellation rows and the Jan 5 timing |
| DEV-02 | Only Jan 26 is reported as unsettled. The Jan 6 desk times and the closed-record assumption are not stated |
| DEV-03 | The question says "State the goal". Section 6 never states it |
| DEV-04 | Does not say that no attendance record exists for Jan 21, or that the room-transfer record is missing |
| DEV-05 | Gives PHQ-9 scores but no dated course of mood, anxiety and sleep. No source per claim. Progress is not set against the plan's three goals |
| DEV-05 | "No conclusion on anxiety" is too strong. Anxiety is described in several notes; what is missing is a measured severity |
| DEV-05 | "Continued engagement" needs qualifying: two no-shows, one cancellation, and absence on Jan 16 |
| DEV-05 | "44% reduction" invites comparison with a 50% threshold that is not in the record. Use the record's own words: "partial improvement" |

---

## 8. What the five record types cannot hold

Section 11 of the notes derived five record types from the questions already named. The agents found four structural problems and a list of things with no home.

**Structural problems**

| Problem | Consequence |
|---|---|
| "Whether it counts" is stored on the contact, but it depends on the plan | A plan amendment that changes what counts leaves the stored flag stale |
| Contacts store minutes, not intervals | No overlap detection, no break intersection, no "what if breaks were not subtracted" |
| A document's standing is treated as its own property | It is relational: the resent roster would be valid evidence if the correction did not exist. Computing it per document breaks order independence |
| Weekly status has no pointer to the conflict it depends on | "Which patients' inclusion depends on unresolved documentation" cannot be answered |

**Things with no home**

| Missing | Needed by |
|---|---|
| Appointments that did not happen, with initiator and reason | Missed and cancelled counts; attendance rate; why a week fell short |
| Charges | Charge without attendance |
| Authorizations | Attended against authorized; units used |
| Clinicians and roles per contact | Minutes by clinician; sessions with two clinicians |
| Participants per interval | Partner-only time; questions about Casey |
| Video or in person | Goal status if video did not count |
| The documents themselves: hash, kind, dates, signature | Duplicates; unsigned documents; late signatures |
| Patient registry | Unknown patient; two patients with one name |
| Episode: start, end, extension | Review period; sessions after Jan 30 |
| Reviewer rulings | O-11 |

This is input to open item O-9. It is not a recommendation to build all of them.

---

## 9. Conflict types, and what extraction must capture

The notes handle four conflict types, each written as an outcome for Rowan. The red team listed 25. Those not seen in the supplied data but likely to be tested:

| Type | Example |
|---|---|
| Correction of a correction | "Departure 11:20, replaces corrected value 11:15" |
| Correction that does not bind | Names the wrong old value or the wrong encounter |
| Retraction | "Entered in error, wrong chart" |
| Late entry or addendum | Author corrects their own note days later |
| Late entry by someone who was not there | Records staff asserting a start time |
| Same document ID, different content | An integrity problem, not a duplicate |
| Summary document with its own totals | A discharge summary saying "13 sessions" |
| Stated minutes disagree with clock times | "09:00–09:50, 45 minutes" |
| Two signed records disagree on attendance | A signed note saying Rowan attended Jan 27 |

**Properties the extraction step would need to capture, not yet planned**

- For a correction: the target, the field, the old value, the new value
- For every time: whether it is scheduled or actual
- Creation time as separate from signature time
- Whether the author was present at the event
- Markers for copy, retraction, late entry, template
- Which documents support which others
- Participants per interval
- Video or in person

---

## 10. New documents with no defined behaviour

Ranked by the red team as most likely to be tested and least covered. Likelihoods are the agent's judgment.

| # | Document | Decision needed |
|---|---|---|
| 1 | Plan amendment taking effect mid-week | Which plan governs that week |
| 2 | Second patient whose plan has a different shape ("2 groups and 1 individual weekly") | How plan rules are stored; D-20 cannot stay fixed at Jan 5–30 |
| 3 | Amendment that changes what counts | Whether counting is stored or evaluated at question time |
| 4 | Schedule export or check-in log for Jan 26 | Which evidence can close an open conflict |
| 5 | Signed note saying Rowan attended Jan 27 | How attended-or-not is represented (O-10) |
| 6 | Retraction of the added Jan 19 session | Week 3 becomes exactly 150, which tests "at least" |
| 7 | Multi-patient roster; a second "Rowan Mercer"; a missing record number | Identity rule |
| 8 | Arrival during a break; two breaks; a break with no clock times | Store intervals |
| 9 | Discharge summary with its own totals | Summaries never override first-hand evidence |
| 10 | Billing extract that contradicts several notes | Charges never alter attendance |
| 11 | Session on Jan 31 or Feb 1 | Whether the plan applies after the episode ends |
| 12 | Stated minutes that disagree with clock times | D-19's open point |
| 13 | Service the plan never mentions: peer support, a crisis call with intervention | How unclassified services are handled |
| 14 | A note containing instructions aimed at the model | Must have no effect |

---

## 11. Unseen questions most likely to be asked

| Kind | Example | Correct behaviour for Rowan |
|---|---|---|
| False premise | "How many minutes was the Jan 27 group?" | Rowan attended 0. The group ran for others |
| False premise | "What was the PHQ-9 on Jan 26?" | None. The Jan 26 document is an import of the Jan 16 score |
| False premise | "How did care change after the plan change?" | No amendment exists. The change of staff is not a plan change |
| Not documented | "What care happened on Jan 24?" | "Not documented", which is different from "no care" |
| Not a patient | "How many sessions did Casey Mercer attend?" | Casey is a participant, not a patient. Do not answer 0 |
| Unknown patient | A name not in the collection | "No such patient". Must not fall through to Rowan |
| Ambiguous | "How many visits did Rowan have?" | State the default: 12 therapy sessions. Also 14 contacts with Rowan present |
| Relative date | "Sessions last week?" | Must not anchor on today's date |
| What if | "If video did not count?" | Week 3: 2 days, 135 minutes, not met |
| By clinician | "Therapy minutes by clinician" | Sums exceed the total because two sessions had two clinicians; say so |
| Integrity | "Which patients have a charge without attendance?" | Rowan, CH-116 |
| Evidence | "Which documents were excluded, and why?" | Needs a record of documents that produced no counted contact |

---

## 12. Design decisions missing from section 11

Agent 6 listed 28. Those with the most effect on scoring or on the follow-up run:

| Decision | Why it matters |
|---|---|
| Standing per claim, not per document | D112 holds a draft and a charge with different authority |
| Duplicate detection at two levels | A copy under a new ID passes a file check and would double-count assessments and observations |
| Extraction cache keyed on content and extractor version | Repeatable re-runs, restart proof, duplicate skipping, and an answer to the prompt-change question |
| Matching encounter IDs by co-occurrence, never by pattern | Mapping HG-A112 to HG-E112 by prefix encodes this clinic's format |
| Citations as quotes located in the source by code | A quote that cannot be found is flagged, not kept |
| Alternatives in place of ranges | Attended-or-not moves days and minutes together |
| Failed extraction shown in answers as a coverage gap | Otherwise it is a silent loss of accuracy |
| Running without your API key | The interviewers run the code themselves |
| Opening every file as UTF-8 | The documents contain en dashes; the Windows default would garble them |
| Version stamp on every answer | Supports repeated reviews and "what changed" |

**The line between a general rule and an encoded fact** (agent 6's test: would the rule be correct for another patient at another clinic, and would it exist if the answer were different?)

| Encoded fact | General rule |
|---|---|
| Break at 10:45–11:00 as a constant | Read the break from the group note |
| 150 minutes as a constant | Read thresholds from the plan |
| A list of document IDs that are copies | A retransmission carries the authority of its original |
| Prompt examples copied from these documents | Synthetic examples |
| "Prefer the later note when it states an arrival time" | Equal-standing disagreement stays open |

---

## 13. Evaluation: checks that need no answer key

| Check | Passes when |
|---|---|
| Exact duplicate | Result unchanged; no model call |
| Same content under a new document ID | Contacts, assessments and observations unchanged |
| Order | Five random arrival orders give the identical result |
| Incremental | Batch 1 then batch 2 equals both at once |
| Restart | A fresh process answers with no extraction calls |
| Citations | Every quote is found in its source |
| Stated against computed minutes | Equal, or a conflict is raised |
| No patient in two sessions at once | Would catch the Jan 19 11:30 error |
| Totals | Weeks sum to the total; types sum to the total |
| Coverage | Every document contributes a claim or has a stated reason for contributing none |

**Problem with the hand answer key:** it was made by the same reading that will shape the rules. Agent 6 suggests writing a few test documents before tuning anything, so they are held out.

**Candidate experiments for the README's tested decision**

| Experiment | Question | Model calls (agent's estimate) |
|---|---|---|
| Model choice | Does a smaller model match a larger one except on subtle standing? | 93–186 |
| Per document against whole chart | Does whole-chart reading break duplicate invariance? | About 37 |
| Rules against model adjudication | Is the model stable on Jan 26 across five runs? | About 20 |

---

## 14. Scale

| Point | Detail |
|---|---|
| First bottleneck | The extraction loop: model throughput under rate limits, and cost |
| Second | Human review. One open conflict per 31 documents extrapolates to about 32,000 at a million |
| Third | Any code that recomputes everything per document or per question |
| Missing from section 10 | Review volume; late documents changing verdicts already reported; long documents that need splitting |
| The problem statement says "inpatient" | Inpatient charts could run to hundreds of documents per patient |
| Making estimates defensible | Clone Rowan's records to 10K, 100K and 1M to time the non-model stages with no model calls |

---

## 15. Scope against the 2–5 hour budget

Agent 6's judgment, not a decision.

| Over-building | Under-building |
|---|---|
| Confirming 26 decisions one at a time | Automated checks |
| A test per reasoning item | Proof of restart |
| Hand answers for every likely question | Coverage gaps in answers |
| More notes prose | Running without your key |
| | The answer format |

It recommends confirming the decisions that change an answer and accepting the rest as a batch, and settling O-8 first because nothing can be measured without it.

---

## 16. Claims not verified

| Claim | Source | Status |
|---|---|---|
| Current model prices | Agent 6 | Not checked. Confirm before any cost estimate |
| Temperature settings are rejected on the newest models | Agent 6 | Not checked |
| Response and remission thresholds for the PHQ-9 | Agent 7 | Outside knowledge; not in the record |
| Billing-code convention that family therapy counts the full session when the patient is present for part | Agent 7 | Outside knowledge; the plan's wording overrides it |
| Likelihood ratings for unseen questions and documents | Agent 5 | The agent's judgment |

**One agent figure I corrected:** the red team gave week 3 as 225 if breaks were not subtracted. It is 210.
