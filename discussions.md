# Discussions log

A record of what we have discussed on the Backbone take-home, what came out of each discussion, and what is still open.

**Related files**

| File | Holds |
|---|---|
| `review-notes.md` | The problem, the data, the traps, hand-worked answers, reasoning kinds, question catalog, design choices |
| `decisions.md` | Every interpretation used to count or calculate, with status |
| `discussions.md` | This file |
| `verification.md` | Findings from the seven-agent check of the three files above, with proposed corrections |

**Rule for this file:** each discussion gets an entry when it ends, and open items move to "Resolved" only when you have decided them.

---

## Open items

| # | Question | Raised in | Who decides |
|---|---|---|---|
| O-1 | Do we write our own test documents for a second patient and a plan amendment? | Discussion 7 | You |
| O-2 | What serves as the answer key, and who confirms it? | Discussion 6, 7 | You |
| O-3 | Which of the 25 Proposed decisions in `decisions.md` do you confirm, change, or want to discuss? | Discussion 6 | You |
| O-4 | Jan 26 conflict: leave open at 40–50, or resolve in favour of the second note? | Discussion 3 | You |
| O-5 | Final week: judge against the full requirement, or prorate? | Discussion 2 | You |
| O-6 | Where does the model work: per document, or per patient with the whole chart? | Discussion 4, 7 | You |
| O-7 | Which model for extraction? | Discussion 4, 7 | You, after an experiment |
| O-8 | Is there an Anthropic API key, or does the `claude` CLI stay as the backend? | Discussion 1 | You |
| O-9 | What are the five record types, and what does each hold? | Discussion 7 | Both |
| O-10 | How should category disagreements (attended or not) be represented, since ranges do not fit? | Discussion 7 | Both |
| O-11 | Where does a reviewer's ruling on a conflict get recorded? | Discussion 7 | Both |
| O-12 | Does a session on Jan 31 or Feb 1 count toward week 4? `review-notes.md` section 9 says yes; D-20 ends the review period on Jan 30 | Discussion 8 | You |
| O-13 | Which plan governs a week that contains a plan change, and does a plan take effect from its episode start or its signature? | Discussion 8 | You |
| O-14 | Which evidence can close an open conflict, and who may settle it? | Discussion 8 | Both |
| O-15 | What happens when a note's stated minutes and its clock times disagree? | Discussion 8 | You |
| O-16 | Do I apply the proposed corrections to `review-notes.md` and `decisions.md`, and add D-27 to D-34 as Proposed? | Discussion 8 | You |
| O-17 | Which of the items with no home in the five record types get stored: appointments not held, charges, authorizations, clinicians, intervals, documents, episodes? | Discussion 8 | Both |
| O-18 | How are patients identified, and how are documents that list several patients handled? | Discussion 8 | Both |
| O-19 | Within 2–5 hours, what is built, what is designed only, and what is left out? | Discussion 8 | You |
| O-20 | What format do answers take, and how precise must a citation be? | Discussion 8 | Both |
| O-21 | How are logs, benchmarks and measured cost produced, given the $0.07 figure cannot be used? | Discussion 8 | Both |
| O-22 | How do the interviewers run the code without your API key? | Discussion 8 | You |
| O-23 | What happens when the extraction prompt changes, and what does "repeated reviews" require? | Discussion 8 | Both |

## Resolved

| # | Question | Outcome | Discussion |
|---|---|---|---|
| R-1 | Keep or discard what was built unasked? | Discarded; start clean | 1 |
| R-2 | How do we work? | Discuss first; no code or model spend until you ask | 1 |
| R-3 | Are group breaks subtracted from patient minutes? | Yes (D-01, Confirmed) | 6 |
| R-4 | Are interpretations recorded? | Yes, in `decisions.md`, before they are used | 6 |
| R-5 | Should the 36 reasoning kinds drive the design? | No; they are a test checklist. The eight kinds drive the design | 7 |

---

## Discussion 1: Starting over

**What prompted it:** You pasted the interview email with no instruction. I assumed you wanted the take-home built and started building.

**What had happened**

- I created a code package, a copy of the documents, and an output folder.
- I installed the `anthropic` Python package.
- I ran about 36 model calls through your `claude` CLI, roughly $2.70 at list price.
- Nothing was sent outside your machine.

**What you said:** "wait what are you doing?" and "lets talk first about the problem, data and what context we have and what we can do."

**Outcome**

- Everything I built was deleted.
- `documents/` was kept, because the original extracted folder and zip were no longer in the project and it was the only copy of the source files.
- The `anthropic` package is still installed.
- We agreed to discuss before building.

**Still open:** O-8.

---

## Discussion 2: The problem, the data, and the traps

**What prompted it:** You asked for an explanation of the problem, the data, what Backbone wants from you, and what they want built, with a walkthrough of the documents and traps.

**Key points**

- Backbone wants an auditable abstraction of a patient's care, with arithmetic in code and every finding traceable to a source line.
- The data is 31 files for one patient, Rowan Mercer, Jan 5–30, 2026, in two visibly different batches.
- The governing rule is in the treatment plan: 3 therapy days and 150 patient-present minutes per Monday–Sunday week.
- Each trap changes a weekly verdict if handled wrongly.
- Two question types in the problem statement (cohort, plan change) cannot be tested on the supplied data.

**Hand-worked result**

| Week | Days | Minutes | Goal |
|---|---|---|---|
| Jan 5–11 | 3 | 140 | Not met |
| Jan 12–18 | 2 | 120 | Not met |
| Jan 19–25 | 3 | 180 | Met |
| Jan 26–Feb 1 | 3 | 145–155 | Cannot determine |

**Outcome:** Recorded in `review-notes.md`, sections 1–6.

**Still open:** O-5.

---

## Discussion 3: Why those three documents

**What prompted it:** I suggested you check D103, D110/D111, and D112 yourself. You asked why those.

**Key points**

- They are where my reading is a judgment call rather than arithmetic, and where being wrong changes an answer.
- Each is a different kind of problem:

| Document | Kind of problem |
|---|---|
| D103 | A signed correction that replaces an earlier value |
| D110 / D111 | Two equally valid records that disagree |
| D112 | A record that looks like evidence but is not |

- D103 is subtle: a later document overrides because it is an explicit signed correction, and an even later resend does not override because it is only a copy.
- D110/D111 is where you might disagree with me. The second note gives a first-hand arrival time.
- D113 (the Jan 30 family session) would be a fourth, since 30 versus 45 minutes also decides week 4.

**Outcome:** No decision taken.

**Still open:** O-4.

---

## Discussion 4: Other kinds of reasoning, scale, and design choices

**What prompted it:** You asked what other kinds of reasoning the system must do, what changes on larger document sets, and what other fundamental design choices exist.

**Key points**

- I listed reasoning kinds in five themes: assembling a record, calculating, negatives and gaps, narrative synthesis, and collection-wide reasoning.
- I checked the Word file for hidden content. It has no images or tables; the file size is embedded fonts.
- Things that get harder at scale: patient identity, multi-patient documents, missing identifiers, richer plan rules, extraction errors, re-processing, format.
- I listed design choices with options and my lean.
- Cost: about $0.07 per document measured on Opus, roughly $36K for 500K documents at list price (extrapolation).

**Outcome:** Recorded in `review-notes.md`, sections 7, 10, 11.

**Still open:** O-6, O-7.

---

## Discussion 5: Putting it all in one file

**What prompted it:** You asked for a markdown file holding the reasoning kinds and the questions that can arise, including unseen ones, plus everything discussed so far.

**Outcome**

- `review-notes.md` created with 14 sections.
- Questions are tagged by source: DEV (in `questions.json`), PS (named in the problem statement), Likely (my inference).
- One error caught and fixed while checking: sessions for Jan 12–25 are 6, not 7.

---

## Discussion 6: What "hand-derived" means

**What prompted it:** You asked what I meant by hand-derived, given most numbers are cited from documents, and how minutes are counted.

**Key points**

- Two kinds of numbers exist in the notes:

| Kind | Examples |
|---|---|
| Copied from a document | Clock times, PHQ-9 scores, plan thresholds, minutes for 7 of the 12 sessions |
| Calculated by me | Minutes for the 5 group sessions, weekly totals, overall total, hours, session counts, verdicts |

- Group minutes take three steps: take Rowan's presence from the roster, remove the break named in the group note, add what remains.
- Subtracting the break is an interpretation. Without it, week 1 becomes 155 minutes and meets the goal.
- For the 7 sessions with stated minutes, the stated figure matches the clock times in every case.

**What you said:** The break subtraction is good, and interpretations like it must be recorded as decisions.

**Outcome**

- `decisions.md` created with 26 decisions.
- D-01 (break subtraction) marked Confirmed. The other 25 are Proposed.

**Still open:** O-2, O-3.

---

## Discussion 7: Is the grouping principled, and are the design choices motivated

**What prompted it:** You asked how I arrived at 36 kinds in 6 groups, why not more or fewer, and whether the design choices are motivated by the reasoning kinds, the data and incoming data, the questions and incoming questions, and the system Backbone needs locally and at scale.

**Key points on the grouping**

- The 36 and 6 are not derived from anything. I listed items as I noticed them and sorted by theme.
- The list has overlaps, mixed sizes, and mixed categories.
- A principled test: two kinds differ only if they would be built differently. That gives eight kinds.
- The nature of each kind (language, logic, judgment) indicates whether a model or code should do it.

**Key points on motivation**

- My leans came from experience first; I had not traced them to requirements.
- When traced, seven are strongly motivated, two medium, two weak, and one unmotivated (Opus as the extraction model).
- Seven requirements have no design choice behind them. The most serious is evaluation.
- Working backwards from the questions gives five record types as the minimum the abstraction must hold.

**Proposals I introduced that we have not discussed**

- For category disagreements, store the alternatives rather than only a range.
- Keep a pointer from each range to the open conflict that caused it.

**Outcome:** Added to `review-notes.md`, sections 7 and 11.

**Still open:** O-1, O-2, O-6, O-7, O-9, O-10, O-11.

---

## Discussion 8: Verifying the three files

**What prompted it:** You asked for agents to verify the gaps and discussions in the three files, to be sure every gap and case the system needs has been thought about.

**What was done**

- Seven review agents ran in parallel, all read-only.

| # | Scope |
|---|---|
| 1 | Fact-check of batch 1 against the notes |
| 2 | Fact-check of batch 2 against the notes |
| 3 | Problem statement and `questions.json` coverage |
| 4 | Consistency across the three files, arithmetic, unlogged interpretations |
| 5 | Red team: unseen questions and documents |
| 6 | Scale, evaluation, operations |
| 7 | Clinical reviewer challenging every decision |

- I re-read the source for the findings that matter most and redid the arithmetic behind each proposed correction.
- You confirmed the change to `Problem Statement.docx` was highlighting. The agent's comparison found the text unchanged apart from one stray tab.

**What you said**

- On the modified `Problem Statement.docx`: "it was just hihglighting some sentences".
- "log all of this in discussions.md once the red team finishes".

**Summary**

- No weekly verdict and no headline number was wrong. Four agents derived the weekly minutes independently and matched the notes.
- All 26 decisions were judged sound. None was overturned.
- Several entries in `decisions.md` state the wrong effect of reversing them, and one contains a factual error.
- Eight interpretations were in use without being logged.
- Two agents disagree on Jan 26.
- The notes left out eight requirements from the problem statement.
- The five record types cannot hold several things the question catalog needs.
- Most of the documents and questions likely to be tested have no defined behaviour yet.

The findings below are grouped by agent. Where I re-read the source or redid the arithmetic myself, the finding is marked **(checked)**.

### Agents 1 and 2: fact-check against the source documents

**Confirmed correct**

| Item | Result |
|---|---|
| Week 1 | 50 + 45 + 45 = 140 minutes, 3 days, not met |
| Week 2 | 75 + 45 = 120 minutes, 2 days, not met |
| Week 3 | 60 + 30 + 45 + 45 = 180 minutes, 3 days, met |
| Week 4 | (40 or 50) + 75 + 30 = 145 or 155 minutes, 3 days |
| Totals | 12 sessions, 11 days, 585 or 595 minutes |
| PHQ-9 | 18, 14, 10; the Jan 26 import is a copy |
| Document index | All 31 rows |
| Patient identifiers | Identical in all 31 documents |

**Errors in the notes**

| Location | Notes say | Source says |
|---|---|---|
| D-07 | "Neither refers to the other" | Each note names the other clinician. Neither refers to the other's record **(checked)** |
| Section 6, DEV-05 | "every note describes [sleep] as inconsistent" | One note uses that word. The Jan 21 note records "one night of improved sleep" **(checked)** |
| Section 8.5 | "No medication change was made." | "No medication change was made today." **(checked)** |
| Section 5.10 | Quote attributed to the authorization letter | It is in the desk entry added on Jan 5 **(checked)** |
| Section 3 | D108 is a "Signed register" | Three entries are signed. The Jan 28 entry was "Entered by Ana Reed" **(checked)** |
| Section 8.2 | Partner-only time is 40 | 40 on Jan 16 plus 15 on Jan 30 **(checked)** |
| Section 8.5 work steps | Seven steps | Three are missing: Jan 6, Jan 12, Jan 23 **(checked)** |
| Section 8.7 | Seven people | Daniel Shaw, the outside social worker, is missing |
| Section 2 | Batch 1 uses one date style | Batch 1 mixes three |
| Mistakes table | Counting the Jan 27 charge makes week 4 met | The charge has no times. It adds a day and no minutes **(checked)** |

**Facts in the documents that the notes missed**

| Fact | Why it matters |
|---|---|
| Nothing covers Jan 17–18; the schedule export's view ends Jan 16 **(checked)** | Week 2 "not met" rests on silence |
| No schedule export exists for batch 2 | Scheduled times for Jan 19–30 are mostly unknown |
| The Jan 19 roster says arrival and departure "were entered at roster close" **(checked)** | The 10:00 arrival came from the same process as the wrong 11:30 |
| The correction cites a "room-transfer record" that was not supplied **(checked)** | Its key evidence is missing from the set |
| The authorization, received Jan 4, refers to a "submitted" plan; the only plan was signed Jan 5 **(checked)** | Bears on "one plan, no amendment" |
| The only source for Jan 6 and Jan 12 presence is an unsigned desk extract **(checked)** | A blunt "signed outranks unsigned" rule would weaken those minutes |
| The Jan 12 break note lacks the "whole group" wording **(checked)** | D-01's basis did not quote it |
| Casey Mercer, the partner, shares the patient's surname **(checked)** | A patient lookup on "Mercer" could match the wrong person |
| "Primary" and "second" appear only in the file names of the Jan 26 notes **(checked)** | A system that reads file names could wrongly prefer one |
| Accounts differ on who started the added Jan 19 session **(checked)** | The facilitator "arranged" it, or Rowan "requested additional help" |
| The Jan 30 questionnaire was completed at 12:42, yet Rowan was absent from the family session until 13:15 **(checked)** | The record does not explain this |
| Five sessions have a note but no attendance record | Presence rests on the clinician's note alone |
| The group's worked example about a work email was the facilitator's **(checked)** | It is not one of Rowan's steps |

**My one correction to an agent:** agent 1 suggested the Jan 6 arrival of 10:15 may be a desk time and not entry to the group. The roster also says the desk records arrival "when members enter or leave the scheduled group", so this is a minor caveat.

### Agent 3: problem statement and questions

**Requirements the notes did not capture** (all quotes **checked**)

| Requirement |
|---|
| "An organized representation of the patient's course of care... inspect it, understand how it represents the relevant evidence, and trace its contents back to their sources." |
| "Pay close attention to what the questions require: reconciling evidence across documents, calculating quantities over time, and distinguishing established conclusions from uncertainty." |
| "demonstrate how it reuses work across questions and runs" |
| "reliable, auditable, and straightforward to extend" |
| "State any assumptions that materially affect your answer." |
| "Document incomplete work and tradeoffs." |
| "You do not need to build a universal clinical review system." |
| "Prioritize a working end-to-end implementation, inspectable outputs, and meaningful checks." |

**Other findings**

- The problem statement says `questions.json` covers cohort and plan-change questions. It does not. Backbone's own test set probably has several patients and a plan change.
- `questions.json` gives no answer format. The format is ours to choose and is undecided.
- The notes say of retrieval that "the FAQ warns against it". The FAQ says "Retrieval may be useful" **(checked)**.
- One quote in section 1 is spliced from two separate sentences.

**Gaps in the hand-worked answers**

| Question | Gap |
|---|---|
| DEV-01 | No per-session source table |
| DEV-02 | Only Jan 26 is reported as unsettled |
| DEV-03 | The question says "State the goal". Section 6 never states it |
| DEV-04 | Does not say that no attendance record exists for Jan 21 |
| DEV-05 | No dated course of mood, anxiety and sleep. No source per claim. The plan's three clinical goals are never mentioned |

**Deliverables with no plan:** execution logs, benchmark results, the answer format, commands to process and ask and trace, setup the interviewers can run, the README's tested decision, and the first bottleneck at a million documents.

### Agent 4: consistency, arithmetic, decisions

**Arithmetic.** Every calculated figure is correct except two.

| Item | Notes say | Correct |
|---|---|---|
| Scheduled time for Jan 6 | Week 1 becomes 185 | 170. The 185 figure also leaves the break in **(checked)** |
| Cost for 500K documents | About $36K from $0.07 each | $35,000. The original run gives $0.075 per call **(checked)** |

**Decisions whose stated effect is wrong** (all **checked** by recomputing)

| Decision | Says | Should say |
|---|---|---|
| D-01 | Week 1 becomes met | Week 4 also becomes met, at 160 or 170 |
| D-02 | Week 1 only | Jan 19 and Jan 22 also rise to 75; total 660 or 670 |
| D-10 | Week 2 becomes met | Counting the Jan 30 medication visit also makes week 4 met |
| D-12 | Lists D008, D104, D112 | The risk is D108. Placed by its Jan 30 date, week 3 falls to 2 days and 135 minutes |
| D-13 | No answer changes | Totals become 11 sessions, 10 days, 535 or 545 minutes |
| D-14 | "Possibly" | Prorating gives a threshold near 107 minutes; week 4 is met either way |
| D-16 | No answer changes | Adds 3 sessions and 3 days. Also worded too broadly, since telephone therapy exists |
| D-11, D-12, D-14, D-15, D-20 | No "if reversed" line | One is needed |

**Contradictions between files**

| Contradiction |
|---|
| Section 11 says authorizations are "not needed by any question". Sections 5.10, 6 and 8.1 and D-26 all use them |
| Jan 16 is described three ways: a partner-only contact, a family session held without Rowan, and a session Rowan could not attend |
| "20 scheduled encounters" is a count of encounter IDs. One was added the same day and one had no patient |
| Section 9 says a session after Jan 30 raises week 4. D-20 ends the review period on Jan 30 |
| Section 9 says an addendum from either clinician settles Jan 26. One clinician restating 09:00 would not cancel the other's observation |
| Section 12 still lists the break as an open judgment call. D-01 is Confirmed |
| The motivation table rates "Opus for extraction" as a lean. The design table says "Decide by experiment" |
| Assessments are matched by form ID in one place and by completion date in another. Only two documents carry a form ID |

**Gaps that no open item tracked:** patient identity, documents listing several patients, the prompt change, "repeated reviews", which plan governs a week with a change, stated minutes against clock times, and the storage choice. These are now O-13, O-15, O-18 and O-23.

**Decisions written as facts about Rowan that need a general rule:** D-05, D-06, D-07, D-08, D-13, D-14 and D-20. D-20 fixes the review period at Jan 5–30, which fails for any second patient.

### Agent 7: clinical reviewer

**Verdict on the decisions:** all 26 sound. D-05, D-07, D-13, D-14, D-15, D-18 and D-21 need a stated caveat.

**Unlogged interpretations** (proposed as D-27 to D-34; effects **checked** by recomputing)

| Proposed ID | Interpretation | If reversed |
|---|---|---|
| D-27 | A video session counts as patient-present | Week 3 becomes 2 days and 135 minutes, not met |
| D-28 | Partial attendance still counts as a session and a therapy day | Weeks 1, 3 and 4 each fall to 2 days |
| D-29 | A session led by two clinicians counts the patient's minutes once | Week 1 becomes 185 and week 4 becomes 195, both met |
| D-30 | The added Jan 19 session is a separate session | 11 sessions; Jan 19 becomes one contact of 90 minutes |
| D-31 | Totals assume no therapy happened that is not in the record | Weeks 2 and 4 become "not met on the available record" |
| D-32 | Times equal to the scheduled times are accepted when the narrative supports them | Jan 12, 19 and 29 minutes become uncertain |
| D-33 | Jan 16 is a collateral contact, not an appointment Rowan missed | Missed or cancelled count rises by one |
| D-34 | Intervals exclude their end minute; a break is subtracted only where it overlaps presence | An 11:15 departure and 11:15 start would overlap |

The basis for D-27 is in the partner-contact note: "Rowan did not join in person, by telephone, or by video", which treats video as a form of presence **(checked)**.

**On the final week (O-5):** judge against the full requirement and label the week partial. No document records a discharge, and several say care continues. Show prorating only as a sensitivity.

**On DEV-05**

- "No conclusion on anxiety" is too strong. Anxiety is described in several notes; what is missing is a measured severity.
- "Continued engagement" needs qualifying by two no-shows, one cancellation and the Jan 16 absence.
- "44% reduction" invites a 50% threshold that is not in the record. The record's own words are "partial improvement".

**On the Jan 27 charge:** report it as an inconsistency between documentation and billing, not as improper billing. The record does not show whether the charge was later reversed.

### The disagreement on Jan 26 (O-4)

| | Keep open | Open, leaning 40 |
|---|---|---|
| Held by | Agent 7 | Agent 2 |
| Main argument | Both notes are signed and final, and nothing ranks them | The second note records an observed arrival and claims the whole encounter |
| Supporting point | The figures straddle 150 exactly | The Jan 19 roster shows a scheduled time entered in an "actual" field |
| Week 4 | Cannot determine | Not met at 145 if resolved |

**Both agree**

- 40 minutes is established. Only 09:00–09:10 is disputed.
- The value is "40 or 50", not "40–50".
- No scheduled time for the appointment exists in the record, so the idea that the first note recorded the booked start cannot be shown.
- "Equally valid" understates the difference between the two notes.

The second note reads: "Rowan entered the treatment room at 09:10, when we began the session. The full patient-contact interval for the encounter was 09:10–09:50." **(checked)**

### Agent 5: red team

**How the test authors build traps**

| Pattern | Example |
|---|---|
| One failure per document, tuned to flip a verdict by a small margin | 140 against 150; 145 and 155 straddling 150 |
| Each document states its own standing in one sentence | "no new clinician signature and records no additional visit" |
| A scheduled value leaks into an "actual" field | The 11:30 departure on Jan 19 |
| The format changes between batches | A third format is likely |
| The problem statement names things the data never exercises | Multiple patients, a plan change, authorizations |

**Structural problems with the five record types**

| Problem | Consequence |
|---|---|
| "Whether it counts" is stored on the contact but depends on the plan | An amendment that changes what counts leaves the stored value stale |
| Contacts store minutes, not intervals | No overlap detection and no break intersection |
| A document's standing is treated as its own property | It depends on other documents. The resent roster would be valid if the correction did not exist |
| Weekly status has no pointer to the conflict it depends on | "Which patients' inclusion depends on unresolved documentation" cannot be answered |
| Contacts hold only what happened | No-shows and cancellations have no home |

**New documents most likely to be tested and least covered**

| # | Document | Decision needed |
|---|---|---|
| 1 | Plan amendment taking effect mid-week | Which plan governs that week (O-13) |
| 2 | Second patient whose plan has a different shape | How plan rules are stored |
| 3 | Amendment that changes what counts | Stored, or evaluated at question time |
| 4 | Schedule export or check-in log for Jan 26 | Which evidence can close a conflict (O-14) |
| 5 | Signed note saying Rowan attended Jan 27 | How attended-or-not is represented (O-10) |
| 6 | Retraction of the added Jan 19 session | Week 3 becomes exactly 150, which tests "at least" |
| 7 | Multi-patient roster; a second "Rowan Mercer"; a missing record number | Identity rule (O-18) |
| 8 | Arrival during a break; two breaks; a break with no clock times | Store intervals |
| 9 | Discharge summary with its own totals | Summaries never override first-hand evidence |
| 10 | Billing extract that contradicts several notes | Charges never alter attendance |
| 11 | Session on Jan 31 or Feb 1 | O-12 |
| 12 | Stated minutes that disagree with clock times | O-15 |
| 13 | A service the plan never mentions | How unclassified services are handled |
| 14 | A note containing instructions aimed at the model | Must have no effect |

**Unseen questions most likely to be asked**

| Kind | Example | Correct behaviour |
|---|---|---|
| False premise | "How many minutes was the Jan 27 group?" | Rowan attended 0 |
| False premise | "What was the PHQ-9 on Jan 26?" | None; that document is an import |
| False premise | "How did care change after the plan change?" | No amendment exists |
| Not documented | "What care happened on Jan 24?" | "Not documented", which differs from "no care" |
| Not a patient | "How many sessions did Casey Mercer attend?" | Casey is a participant. Do not answer 0 |
| Unknown patient | A name not in the collection | Must not fall through to Rowan |
| Ambiguous | "How many visits did Rowan have?" | State the default: 12 therapy sessions |
| Relative date | "Sessions last week?" | Must not anchor on today's date |
| By clinician | "Therapy minutes by clinician" | Sums exceed the total because two sessions had two clinicians |

**Conflict types.** The notes handle four. The red team listed 25. Those not in the data but likely to be tested: a correction of a correction, a correction naming the wrong old value, a retraction, a late entry by the author, a late entry by someone who was not present, and the same document ID with different content.

**What extraction would need to capture, not yet planned:** for a correction, its target and old value; for every time, whether it is scheduled or actual; creation time apart from signature time; whether the author was present; markers for copy, retraction and late entry.

**My one correction to this agent:** it gave week 3 as 225 minutes if breaks were not subtracted. It is 210.

### Agent 6: scale, evaluation, operations

**Design decisions missing from section 11.** The agent listed 28. Those with the most effect:

| Decision | Why it matters |
|---|---|
| Standing per claim, not per document | One file holds a draft and a charge with different authority |
| Duplicate detection at two levels | A copy under a new ID passes a file check and would double-count |
| Extraction cache keyed on content and extractor version | Repeatable re-runs, restart proof, and the prompt-change answer |
| Matching encounter IDs by co-occurrence | Mapping HG-A112 to HG-E112 by pattern encodes this clinic's format |
| Citations located in the source by code | A quote that cannot be found is flagged |
| Alternatives in place of ranges | Attended-or-not moves days and minutes together |
| Failed extraction shown in answers | Otherwise accuracy is lost silently |
| Running without your API key | The interviewers run the code themselves |
| Opening every file as UTF-8 | The documents contain en dashes |

**Checks that need no answer key**

| Check | Passes when |
|---|---|
| Exact duplicate | Result unchanged; no model call |
| Same content under a new document ID | Contacts, assessments and observations unchanged |
| Order | Five arrival orders give the identical result |
| Incremental | Batch 1 then batch 2 equals both at once |
| Restart | A fresh process answers with no extraction calls |
| Citations | Every quote is found in its source |
| No patient in two sessions at once | Would catch the Jan 19 11:30 error |
| Totals | Weeks sum to the total |

**On the answer key:** it was made by the same reading that will shape the rules. The agent suggests writing a few test documents before tuning anything.

**Scale**

| Point | Detail |
|---|---|
| First bottleneck | The extraction loop: throughput under rate limits, and cost |
| Second | Human review. One open conflict per 31 documents extrapolates to about 32,000 at a million |
| Third | Any code that recomputes everything per document or per question |
| Making estimates defensible | Clone Rowan's records to large sizes and time the non-model stages |

**Scope.** The agent judged the notes are over-building: 26 decisions confirmed one at a time, a test per reasoning item, and more prose than a 30-minute call can use. It judged them under-building on automated checks, restart proof and the answer format.

**The line between a rule and an encoded fact.** The agent's test: would the rule be correct for another patient at another clinic, and would it exist if the answer were different?

### Claims I did not verify

| Claim | Source |
|---|---|
| Current model prices | Agent 6 |
| Temperature settings are rejected on the newest models | Agent 6 |
| PHQ-9 response and remission thresholds | Agent 7; outside knowledge |
| A billing convention that family therapy counts the full session | Agent 7; outside knowledge, and the plan's wording overrides it |
| Likelihood ratings for unseen questions and documents | Agent 5's judgment |

**What I attempted and did not complete**

- I wrote a script to apply the corrections to `decisions.md`. It was blocked before it ran, because the file is not under version control and the change could not be undone.
- As a result, `review-notes.md` and `decisions.md` are unchanged. The corrections and the eight new decisions are listed in `verification.md` as proposals.

**Outcome**

- This entry holds the findings grouped by agent.
- `verification.md` holds the same findings grouped by topic, in 16 sections, with each proposed correction set out as "says" and "should say".
- 12 open items added (O-12 to O-23).
- No item resolved. No decision's status changed.

**Still open:** O-12 to O-23. O-16 comes first, since it decides whether the notes are corrected.

---

## Suggested order for the next discussions

Each constrains the next.

1. Whether to apply the proposed corrections and new decisions (O-16).
2. Scope for the time budget, and how correctness will be checked (O-19, O-1, O-2).
3. The Proposed decisions, starting with those that change an answer (O-3, O-4, O-5, O-12, O-15).
4. The record types and conflict handling (O-9, O-10, O-11, O-13, O-14, O-17, O-18).
5. Where the model works, which model, and how the code is run and measured (O-6, O-7, O-8, O-20, O-21, O-22, O-23).
