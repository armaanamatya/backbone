# Build plan

How the system gets built, in what order, and how each stage is checked. Written 2026-09-29, while `answer-key.md` was being verified.

**Status:** built. You gave the go-ahead on 2026-09-29, and for stages 8 to 10 on 2026-09-30. All ten stages are built, and stage 11, the model comparison, was run early. All 31 documents are read at prompt version 3, the contacts and weekly verdicts match the key, the five answers and nine problem questions are answered, 155 checks pass, the benchmark is measured, and the README is written. The build is stopped at the last review point, after stage 10: whether to send it. What was built and measured is in Discussions 22, 24 to 26, 29, 31, 33 and 34 of `discussions.md`.

**What this plan rests on**

| Source | What it supplies |
|---|---|
| `discussions.md`, R-8 to R-53 | The decisions taken: what is built, the functions, the tables, the capture list, the answer format, and the changes made while the key was verified |
| `decisions.md` | The 36 confirmed decisions and the 16 rules |
| `answer-key.md` | What the output is compared against. Verified on 2026-09-29 (Discussion 19) |

Contents

1. The principle
2. What is built
3. Layout
4. Settings
5. Commands
6. Stages
7. The reading step
8. The store
9. Checks
10. Measurements
11. Model usage
12. Points where you review
13. Risks and unknowns
14. Not built

---

## 1. The principle

Build one thin path from a document to an answer first, then widen it. The problem statement asks for this: "Prioritize a working end-to-end implementation, inspectable outputs, and meaningful checks."

In practice, stage 2 reads three documents and stage 5 already produces weekly verdicts. Nothing is polished before the whole path works.

---

## 2. What is built

The 11 pieces accepted in R-11, with the two additions in R-9 and R-10.

| # | Piece | Stage |
|---|---|---|
| 1 | Read files, hash them, skip exact duplicates | 1 |
| 2 | Model reads one document and returns claims, each with a quote | 2, 3 |
| 3 | Code checks every quote exists in its source | 3 |
| 4 | Saved store with patient on every row | 1 |
| 5 | Code matches documents to contacts and applies the conflict rules | 4 |
| 6 | Code counts minutes, days, weeks and goal verdicts, carrying alternatives | 5 |
| 7 | Questions: the model returns a plan of function calls, code runs them, and code writes the answer (R-47, R-48) | 6, 7 |
| 8 | The five answers, with sources and calculations | 7 |
| 9 | Logs and a benchmark script | 1 onward, 9 |
| 10 | Automated checks | 8, and alongside each stage |
| 11 | README | 10 |
| + | Functions can be called directly, without a model | 6 |
| + | A document that fails to read is shown in every answer it affects | 3, 7 |

---

## 3. Layout

| Path | Holds |
|---|---|
| `README.md` | The write-up Backbone asks for |
| `documents/` | The 31 source files, unchanged |
| `questions.json` | The five questions, unchanged |
| `backbone/` | The code, one file per stage |
| `prompts/` | The three prompts: reading, choosing functions, and the optional summary of observations |
| `tests/` | The checks |
| `settings.toml` | Model, prompt version, spending cap |
| `output/abstraction.sqlite` | The saved abstraction |
| `output/abstraction.md` | The same abstraction in readable form |
| `output/answers/` | The five answers, as data and as text |
| `output/logs/` | One log file per run |
| `output/benchmarks/` | Measured figures, and estimates in a separate file |
| `answer-key.md` | The key |

**Code files**

| File | Does |
|---|---|
| `ingest.py` | Reads files as UTF-8, hashes them, skips duplicates |
| `reader.py` | Calls the model on one document and returns claims |
| `quotes.py` | Finds each quote in its source and records the line |
| `coverage.py` | Lists every time, date and encounter number in a document, and checks each appears in a claim |
| `store.py` | Creates and writes the tables |
| `reconcile.py` | Matches documents to contacts and applies rules 1 and 7 to 11 |
| `counting.py` | Intervals, minutes, days, weeks, verdicts: rules 2 to 6 and 12 |
| `functions.py` | The nine functions |
| `ask.py` | Gets a plan of function calls from the model, runs it, and writes the nine-part answer in code. Handles a question no function fits |
| `logs.py` | Writes one line per event |
| `cli.py` | The commands |

The system uses Python's standard library only, so the interviewers install nothing beyond Python. The checks use `pytest`.

---

## 4. Settings

One file, `settings.toml`. Nothing in it is a fact about a patient.

| Setting | Value at the start | Why it is a setting |
|---|---|---|
| Model | Opus (R-17) | Swapping models later is a one-line change (R-23) |
| Effort | Low for reading, confirmed at stage 2 (R-49) | Affects cost and accuracy |
| Prompt version | 1 at the start, 2 after stage 2, 3 after stage 3 | Stamped on every claim |
| Spending cap per call | $0.50, set at stage 2 | A guard against a runaway call |
| Calls in parallel | 4 | Sets how long reading takes |

---

## 5. Commands

| Command | Does | Needs a model |
|---|---|---|
| `ingest documents/` | Reads new documents and updates the abstraction | Yes, one call per new document |
| `ask "question"` | Answers a question in the nine-part format | One call for a new question. None for a repeated one, because its plan is saved |
| `call goal_status --patient HG-M042` | Runs one function and prints its result | No |
| `trace` | Follows a figure back to contacts, claims and source lines | No |
| `export` | Writes the abstraction in readable form | No |
| `check` | Runs the checks on the store and the answers, then the tests | No |
| `benchmark` | Measures times and sizes | Only with `--live`, for new questions end to end |

Five of the eight commands run with no model, and `benchmark` calls one only with `--live`. That is how the interviewers can inspect the abstraction and follow a conclusion to its source without your setup (R-9).

---

## 6. Stages

Each stage ends with something that can be checked.

| # | Stage | Builds | Done when | Model calls |
|---|---|---|---|---|
| 1 | Skeleton | Settings, logs, the store with its eight tables, reading and hashing files | 31 documents are registered. A copy of a file is skipped. A restart finds the same store | 0 |
| 2 | Read three documents | The reading prompt, the output schema, the model call, the coverage check | D103, D108 and D112 each return the claims the capture list names. The coverage check shows what low effort misses, if anything. The call reports its tokens and cost, or we learn that it does not | About 3 to 10 |
| 3 | Trial on eleven, then read all 31 | The trial set, parallel calls, a saved copy of each result, the quote check, handling of a failed read | The trial set passes the quote check and the coverage check. All 31 are then read once. Every claim has a quote found in its source. A failed document is recorded as not read | About 40 to 65 |
| 4 | Reconcile | Contacts, conflicts, findings, plan rules, assessments | Matches sections 2 to 5 of the key: 20 contacts, 3 conflicts, finding F-1, 3 assessments | 0 |
| 5 | Count | Intervals, minutes, days, weekly status | Matches section 6 of the key: 140, 120, 180, 145 or 155, and the four verdicts | 0 |
| 6 | Functions | The nine functions and the `call` command | Each function returns rows, the calculation, the sources and the conflicts it depends on | 0 |
| 7 | Questions | The plan call, the saved plans, the nine-part answer written by code, the five answers | The five answers match section 7 of the key. The nine problem questions behave as in section 8 | About 14 to 25 |
| 8 | Checks | The checks in section 9 of this plan | All pass, or each failure is understood and written down. Built: 155 pass (Discussion 34) | 0 |
| 9 | Measure | The benchmark script, which replays saved results and logs | The measured figures in section 10 exist, with estimates kept in a separate file. Built: 5 calls (Discussion 34) | About 5 |
| 10 | Write up | The README, the readable export | Every item the problem statement asks for is present. Built (Discussion 34) | 0 |
| 11 | After the build | The model comparison (O-36) | On your go-ahead only. Run early, on your ask: 153 calls (Discussion 33) | About 31 per model |

**Why this order**

- Stages 4 to 6 cost nothing to repeat, because they run on saved results from stage 3.
- Stage 2 comes before stage 3 so that a mistake in the prompt costs three calls, not 31.
- In stage 3 the prompt is adjusted on eleven documents only. All 31 are read once, when those eleven pass (R-50, R-53).
- Stage 5 produces the verdicts early. If the numbers are wrong, that shows before any work on questions.

**How stages 4 and 5 are developed**

Against two things: the saved results of stage 3, and small hand-written sets of claims that exercise one rule each. For example: a correction arriving before the roster it corrects, or a copy arriving after the correction. These need no model and no document.

**How stage 7 answers a question** (R-47, R-48)

1. One model call returns a plan of up to five function calls. There is no tool loop.
2. Code runs the plan.
3. Code writes the nine-part answer from the function results.
4. The plan is saved under the question text, stamped with the model and prompt version. A repeated question calls no model.

- The model writes one thing only: an optional summary paragraph for the observations function.
- Limit: a question whose second step depends on the result of the first is not handled. This narrows R-22.

**How stage 7 handles a question no function fits**

| The question | What the system shows | From |
|---|---|---|
| Names a date | "Cannot answer", and the stored passages for that patient and date | R-33 |
| Names no date | "Cannot answer", and the documents of a matching kind for that patient, by document ID and file name | R-42 |

- In the plan call, the model says that no function fits and names the kind of document the question is about, from the list of kinds. Code looks the kind up in the `documents` table. The model does not search the text.
- No figure is given, and no passage is quoted.
- If no document of that kind exists for the patient, the answer is "cannot answer" alone.
- The list of kinds gains "authorization", which the capture list did not name.
- Example: a question about authorization units left names D001, the authorization letter, and gives no count of units (D-26).

---

## 7. The reading step

### The call

| Part | Choice | Why |
|---|---|---|
| Tool | The `claude` command-line tool, run once per document | R-16 |
| Tools given to the model | None | The model only reads. A document cannot make it act |
| System prompt | Our own, replacing the default | Keeps the call close to a direct one |
| Output | Checked against a schema by the tool, then again by our code | A malformed result is caught twice |
| Document text | Passed in as data, clearly marked | Instructions inside a note are treated as text, not as orders |
| Saved result | Kept under the file's hash, the model and the prompt version | A re-run reads the saved result and calls nothing |

### What the prompt tells the model

| Instruction | Reason |
|---|---|
| Report what the document says. Do not decide which document is right | Code reconciles (R-12) |
| Do not calculate minutes | Code counts |
| Give every claim a short quote, copied exactly | Code checks it |
| Say whether each time is labelled scheduled, labelled actual, or not labelled, and where in the document it appears | Rule 3. Code treats an unlabelled time in the header of a signed note as actual (D-36) |
| For an observation, take the speaker from the sentence itself. Where the sentence names no one, give the author of the note. Do not take the speaker from the paragraph around it | Rule 16 (D-35) |
| For a correction, give the target, the field, the old value and the new value | Rule 8 |
| Say what the document says about itself | Rules 9 and 10 |
| Split a file that holds several records | D112 holds a draft and a charge |
| Put each service into one of seven general classes | R-21 |
| Leave a field empty when the document does not state it | No guessing |

Examples in the prompt are made up. None is taken from the 31 documents, so the prompt holds no fact about Rowan.

### The trial set (R-50, R-53)

The prompt is adjusted while looking at these eleven documents and no others.

| Document | Kind | Why it is in the set |
|---|---|---|
| D003 | Plan | The thresholds and what counts |
| D006 | Schedule export | Scheduled times and statuses, which must not be read as attendance |
| D014 | Import | A questionnaire score in a table, and a received date that is not a completion date |
| D103 | Correction | Target, field, old value and new value |
| D104 | Copy | What a copy says about itself, and an attached roster |
| D106 | Clinical note, with a platform export | Two intervals, and an interruption |
| D107 | Clinical notes for two dates | A group break with its times, and two dates in one file |
| D108 | Attendance record, register | Four dates, three signed entries and one desk entry |
| D111 | Clinical note | An observed arrival, and a second clinician |
| D112 | Draft note, and a billing extract | Two sections in one file, neither of which is attendance |
| D113 | Clinical note, family session | An interval with the partner and without the patient |

- D103, D108 and D112 are the three documents of stage 2.
- The set holds documents from both batches, which write dates and times differently.
- The other 20 documents are read once, after the set passes. The prompt was not adjusted on them, so they test it fairly.
- The set was eight documents under R-52. A check of the 31 files found no score, no group break, no partner-only interval and no copy in it (Discussion 21). D107, D113, D014 and D104 were added, and D005 was taken out because D006 and D108 cover its shape.
- Three kinds are in no trial document: the authorization (D001), the scheduling log (D015) and the cancellation notice (D016).
- If the full read exposes a problem, the prompt changes, the version number rises, and all 31 are read again.

### When the result fails our checks

| Failure | Action |
|---|---|
| The result does not fit the schema | One retry, with the error shown to the model |
| A quote is not found in the source | The claim is kept and marked unverified. It is not used in a count |
| A time, date or encounter number in the document appears in no claim | It is listed as not captured for that document. The list is shown at the reviews after stages 2 and 3. The read is not blocked (R-51) |
| A time does not parse, or an end is before a start | The claim is marked invalid |
| The second attempt also fails | The document is recorded as not read, and every answer it affects says so (R-10) |

---

## 8. The store

SQLite, in one file. Two layers, eight tables (R-20).

| Layer | Table | Key columns |
|---|---|---|
| Says | `documents` | Hash, file name, declared ID, kind, dates, signature, read or not |
| Says | `claims` | Document, section, patient, contact reference, type, value, scheduled or actual, quote, line, model, prompt version |
| Concludes | `contacts` | Patient, date, class, status, clinicians, in person or video, presence intervals, removed intervals |
| Concludes | `conflicts` | Contact, field, alternatives, claims behind each, rule applied or open, what would settle it |
| Concludes | `findings` | Kind, contact, claims behind it |
| Concludes | `plan_rules` | Patient, thresholds, counted classes, week definition, dates in effect |
| Concludes | `assessments` | Patient, instrument, score, completion time, form ID, original or copy |
| Concludes | `weekly_status` | Patient, week, days, minutes as alternatives, verdict, conflicts it depends on |

**How a new document is handled**

1. The file is hashed. If the hash is known, nothing more happens.
2. The model reads it and the claims are saved.
3. The "concludes" tables are rebuilt for that patient only, from all of that patient's claims.

Step 3 rebuilds from scratch for the patient, so the order in which documents arrive cannot change the result.

---

## 9. Checks

| # | Check | Passes when | Needs the key |
|---|---|---|---|
| 1 | Exact duplicate | Adding a copy of a file changes nothing and calls no model | No |
| 2 | Same content under a new document ID | Contacts, assessments and weekly status are unchanged | No |
| 3 | Order | Five random orders give the identical store | No |
| 4 | In two batches | Batch 1 then batch 2 equals both at once | No |
| 5 | Restart | A new process answers with no reading calls | No |
| 6 | Quotes | Every quote used in an answer is found at its cited line | No |
| 7 | Stated minutes | Where a note states minutes, they equal the clock times, or a conflict exists | No |
| 8 | Overlap | No patient is in two sessions at once | No |
| 9 | Totals | Weeks sum to the total. Types sum to the total | No |
| 10 | Coverage | Every document gives at least one claim, or has a stated reason for giving none | No |
| 11 | Numbers in text | Every number in a written answer appears in the function results | No |
| 12 | Contacts | The 20 contacts match section 3 of the key | Yes |
| 13 | Weekly status | The four weeks match section 6 of the key | Yes |
| 14 | The five answers | Figures and sources match section 7 of the key | Yes |
| 15 | Problem questions | The nine behave as in section 8 of the key | Yes |
| 16 | Coverage of values | Every time, date and encounter number in a document appears in a claim, or is listed as not captured | No |

Check 8 is the one that would catch the 11:30 departure on Jan 19 if the correction were missing.

For checks 12 to 15, the verified key is copied by hand into a data file, `tests/answer_key.json`, so that code can compare against it.

---

## 10. Measurements

The problem statement asks for these, with measured figures kept apart from estimates.

| Measure | How | Measured or estimated |
|---|---|---|
| Time to read all 31 documents, from empty | Timed, one call at a time and four at a time | Measured |
| Time to re-run with saved results | Timed | Measured |
| Time to add one new document | Timed | Measured |
| Time to answer a question about one patient | Code time is timed over five runs. Model time is taken from the logs of calls already made | Measured |
| Time to answer a question across the collection | Timed | Measured on one patient, which shows little. See section 13 |
| Tokens and cost per document | From what the tool reports | Measured, if the tool reports them |
| Size of the saved abstraction | File size and rows per table | Measured |
| Cost and time at 500,000 documents | Measured cost per document, multiplied | Estimated |
| Where it slows first at a million documents | From the timings per stage | Estimated, naming the function |

---

## 11. Model usage

| Stage | Calls | Note |
|---|---|---|
| 2 | 3 to 10 | Three documents, with a few tries at the prompt |
| 3 | 40 to 65 | The prompt is tried on eleven documents, then all 31 are read once |
| 7 | 14 to 25 | Five questions and nine problem questions, one plan call each, with some repeats |
| 9 | About 5 | Question timings. The rest replay saved results and logs |
| Total | About 60 to 105 | Was 80 to 175 before R-47, R-48 and R-50 |

These are estimates. I have no reliable cost per call: the only figure on record is $2.70 for 36 calls, from the build that was deleted. Stage 2 gives the first real figure, and I will report it before stage 3 begins.

---

## 12. Points where you review

| After stage | What you see | What you decide |
|---|---|---|
| 2 | The claims from three documents, what the coverage check found, and the cost of a call | Whether the capture list is working, whether low effort is accurate enough, and whether to read all 31 |
| 5 | The contacts and weekly verdicts beside the key | Whether the numbers are right before work on questions begins |
| 7 | The five answers | Whether they say what you would say in the call |
| 10 | The whole submission | Whether to send it |

I stop at each of these and wait for you.

---

## 13. Risks and unknowns

| Risk | Effect | What the plan does |
|---|---|---|
| The `claude` tool may not report tokens and cost per call | "Model usage and cost" could not be measured | Found out at stage 2. If it does not, cost is estimated from the length of the text and labelled an estimate |
| The interviewers may not have the `claude` tool | They could not read a new document | The saved abstraction and the saved reading results are in the submission. Four commands need no model. The README says what reading a new document needs. Revisited under O-36 |
| One patient in the data | Collection-wide timing shows little, and the cohort function is tested on one patient | Patient is on every row from stage 1. The second patient is on hold (O-1) and should return before stage 9 |
| No plan change in the data | The plan in effect for a period is untested | Plan rules carry dates from stage 4. On hold (O-13) |
| The model reads a document differently on a second run | Results could differ between runs | Saved results make re-runs identical. How much the model varies is a candidate for the README's observed limitation |
| The prompt is adjusted while looking at the documents | It may fit them too well | The prompt is adjusted on eleven documents only, so the other 20 test it fairly. Examples in the prompt are made up. The README says so |
| The trial set lacks a kind of document. The authorization, the scheduling log and the cancellation notice are not in it | The full read exposes a problem the trial did not | The prompt changes and all 31 are read again. The saving is lost for that round |
| The key shares the reading that shaped the rules | A shared mistake would pass every check | Checks 1 to 11 do not use the key. The key was verified against the documents on 2026-09-29, and you checked the six rows that decide a verdict |
| A question needs a second step that depends on the first result | The one plan call cannot express it | The answer says which part it could not do. Described in the README as a limit |
| Low effort makes the reading less accurate | Claims are missed | The coverage check lists what was missed. Effort is raised if stage 2 shows a loss |
| Windows reads text files in a different encoding by default | The en dashes in times would be garbled and line numbers could shift | Every file is opened as UTF-8 |

---

## 14. Not built

From Discussion 12.

| Item | Treatment |
|---|---|
| Near matches on patient identity | Described in the README |
| The process for re-reading after a prompt change | The version stamp is built. The process is described |
| Reviewer rulings | Described |
| Retractions, chained corrections, summary documents | They stay open under rule 11. Described |
| Batch processing, a smaller model, a different database | Described under scale |
| A user interface, search by similarity, probabilities, authorization units, time zones, scanned documents | Left out |
