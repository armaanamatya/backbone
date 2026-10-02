# Backbone take-home: a clinical abstraction that answers questions

A prototype that reads the 31 documents in `documents/`, builds a saved abstraction of one patient's course of care, and answers the five questions in `questions.json` from that abstraction, with every figure calculated in code and every citation checked against its source line.

Everything below is measured unless it says "estimate". Every decision about how the record is read and counted, with its status, is in `decisions.md`.

## 1. What is built

**The idea.** The model reads one document at a time and reports what that document *says*: contacts, times, attendance, stated minutes, corrections, charges, scores, plan rules, and observations, each with a quote copied from the document. Code does everything after that: it checks each quote is in the source, matches documents to contacts, applies the conflict rules, counts minutes, days and weeks, and writes the answer. The model never decides which document is right and never adds two numbers.

**The abstraction** is one SQLite file, `output/abstraction.sqlite`, in two layers:

| Layer | Tables | Holds |
|---|---|---|
| Says | `documents`, `claims` | Each document, and each thing it states, with the quote, the line, the model and the prompt version that read it |
| Concludes | `contacts`, `conflicts`, `findings`, `plan_rules`, `assessments`, `weekly_status` | What code works out from the claims, rebuilt per patient from scratch whenever a document of that patient arrives |

Every row carries the patient. The readable form of the same store is `output/abstraction.md`.

**How a question is answered.** One model call returns a plan: the patient as written, the period, how the terms are read, and up to five calls to the nine functions in `backbone/functions.py`. Code runs the calls and writes the nine-part answer from the results. The plan is saved under the question, so a repeated question calls no model. The nine functions can also be called directly, with no model at all.

**The 16 rules** that code applies (a signed correction replaces the value it names; a copy carries the authority of its original; a draft or a charge cannot establish attendance; two records of equal standing that disagree stay open, and so on) are listed with their sources in `decisions.md`. Nothing about the patient is typed into code. The thresholds, the counted classes, and the week definition are read from the treatment plan document.

## 2. Setup and how to run

Needs Python 3.11 or later. The code uses the standard library only; the checks need `pytest`. Clone with git rather than downloading the files through an editor: `.gitattributes` keeps every file's bytes as committed, because a document is known by the hash of its bytes and the saved reading results are keyed by it. Reading a *new* document needs the `claude` command-line tool on the PATH and an Anthropic account; everything else runs with no model and no key.

```
python -m backbone ingest documents/          # read new documents (calls the model only for documents with no saved result)
python -m backbone ask --file questions.json  # answer the five questions (plans are saved, so this calls no model)
python -m backbone ask "How many sessions did Rowan attend in the week of January 19?"   # a new question: one plan call
python -m backbone call goal_status --patient HG-M042         # run one function directly; no model
python -m backbone trace contact HG-E110                      # follow a figure to its claims and source lines; no model
python -m backbone trace week 2026-01-26
python -m backbone export                                     # write output/abstraction.md; no model
python -m backbone check                                      # the checks on the store and answers, then the 157 tests
python -m backbone benchmark                                  # times, sizes, tokens and cost; no model unless --live
python -m backbone compare settings.toml output/comparison/settings-sonnet-low.toml   # compare two reads
```

**Processing new documents.** Drop the files in a folder and run `ingest` on it. A file whose content is already in the store is skipped before any model call, whatever its name. A new file is hashed, read once, and its result saved under `output/readings/` keyed by hash, model, effort and prompt version. The patient's conclusions are then rebuilt from all of that patient's claims, so the order in which documents arrive cannot change the result. A document that fails to read twice is recorded as not read, and every answer it would affect says so.

**Answering new questions from the saved abstraction.** `ask` reads the store on disk and calls no reading model. It makes one plan call for a question it has not seen, and none for one it has. To answer with no model at all, call the functions directly with `call`, or run `ask` after the plan is saved.

**Settings** are in `settings.toml`: the model, the reading effort, the prompt versions, a spending cap per call, and how many documents are read at a time. Nothing in it is a fact about a patient.

## 3. What is in `output/`

| Path | Holds |
|---|---|
| `abstraction.sqlite`, `abstraction.md` | The saved abstraction, and the same in readable form |
| `answers/DEV-01.md` to `DEV-05.md` | The five answers, each in nine parts with a short lead, with the JSON beside each holding the plan and the function results |
| `answers/P-1.md` to `P-9.md` | Nine problem questions: an unknown patient, a participant who is not a patient, three false premises, a date with no document, an ambiguous term, a relative date, and a question no function fits |
| `answers/related/Q-*.md` | Five related questions from the answer key, asked end to end during the benchmark |
| `answers/plans/` | The saved plan for every question asked |
| `readings/` | The saved result of every reading call, for every model and effort tried |
| `logs/` | One JSON-lines file per run: every call, its tokens, its cost, and what was accepted or rejected |
| `benchmarks/benchmark.md` | The measured figures. `estimates.md` beside it holds the estimates, and nothing else |
| `comparison/` | Six reads of the 31 documents by different models and efforts, each in its own store, and the report comparing them |

**Reading an answer.** Each answer opens with "In short": the figure, the one open point if any, and the one exclusion that matters most. Then nine parts: the question as understood, the answer, the figures and how they were worked out, what contributed with a source line for each, what was excluded and why, what is not settled, the assumptions, the documents not read, and the version. A citation is the document ID, the line number and the quote, and code confirms the quote is at that line before it is shown. Where the plan asks for the record's disagreements, one on a contact the figures do not use is still stated: an open one in part 6, marked "not behind these figures", and the settled ones and findings in one line of part 5.

**Following a conclusion back.** `trace week 2026-01-26` prints the week's verdict, the contacts behind it, each contact's presence intervals and the claims they rest on, and each claim's document, line and quote. `trace conflict HG-M042/HG-E115:start` prints the two alternatives and what would settle them.

## 4. The answers, in one line each

| Question | Answer |
|---|---|
| DEV-01 | 12 therapy sessions on 11 distinct days, Jan 5 to Jan 30: 5 individual, 5 group, 2 family. 20 encounters in the record, 16 held, 14 with the patient present |
| DEV-02 | 585 or 595 minutes (9.75 or 9.92 hours). By week: 140, 120, 180, and 145 or 155. The two totals differ because two signed notes give the Jan 26 start as 09:00 and 09:10, and nothing settles it |
| DEV-03 | Against at least 3 therapy days and 150 minutes a week: not met, not met, met, cannot be determined |
| DEV-04 | Jan 19: 2 therapy contacts, 90 minutes. Jan 21: 1 contact, 45 minutes. The signed correction replaces the roster's 11:30 departure with 11:15; the later copy changes nothing; the platform export agrees with the note |
| DEV-05 | PHQ-9 18 to 14 to 10 across three distinct assessments, 8 points lower. The copy of the Jan 16 result and two mentions add none. The Jan 19 individual session was added because Rowan became anxious during group |

The problem questions behave as intended: no figure is given for a patient not in the collection, a participant is not mistaken for a patient, a false premise is answered with what the record holds, a date with no document is "not documented" and never "no care took place", and a question no function fits says so and names the document that holds the answer without quoting a figure.

## 5. Checks

`python -m backbone check` runs the store and answer checks, then the 157 tests in `tests/`. None calls a model: the tests replay the saved reading results and the saved plans into an empty store. The 16 checks, and where each lives:

| # | Check | Where |
|---|---|---|
| 1 | A copy of a file changes nothing and calls no model | `test_ingest.py` |
| 2 | The same content under a new document ID changes no conclusion | `test_key.py`, the correction-first batch |
| 3 | Five random orders of arrival give the identical store | `test_key.py` |
| 4 | Two batches equal one | `test_key.py` |
| 5 | A restart answers with no reading call | `test_saved_readings.py` |
| 6 | Every quote is at its cited line | `test_saved_readings.py`, `test_checks.py`, `check` |
| 7 | Stated minutes equal the clock times, or a conflict is open | `test_checks.py`, `check` |
| 8 | No patient is in two contacts at once | `test_checks.py`, `check`. Replaying without the correction BH-D103 shows the overlap it would catch |
| 9 | Weeks sum to the total, classes sum to the total | `test_key.py` |
| 10 | Every document gives at least one claim | `test_saved_readings.py` |
| 11 | Every number in an answer comes from a function result. It catches a figure from nowhere, such as a wrong total. It cannot catch a wrong small count: in DEV-01, 39 of the 61 whole numbers from 0 to 60 occur somewhere in the results, as a day, a clock time or a line number, against 47 of the 939 from 61 to 999. Small counts are held by checks 12 to 15 | `test_checks.py`, `check` |
| 12 | The 20 contacts match the key | `test_key.py` |
| 13 | The four weeks match the key | `test_key.py` |
| 14 | The five answers match the key by figure and source | `test_key_answers.py` |
| 15 | The nine problem questions behave as the key says | `test_answers.py` |
| 16 | Every time, date and record number in a document is in a claim or listed as not captured | `coverage.py`, shown in `abstraction.md` |

Checks 1 to 11 do not use the answer key. The key, `answer-key.md`, was worked by hand and verified against the documents before the build, and it is copied into `tests/answer_key.json` for checks 12 to 15. The 16 rules are also each tried on made-up records that exercise one rule at a time (`test_rules.py`), and two made-up patients share a store in `test_patients.py` to show that one patient's rows never reach the other's answer.

## 6. Measurements

From `output/benchmarks/benchmark.md`. Model alias `opus` in the `claude` tool, which the logs show served as `claude-opus-5-5`; effort low; reading prompt version 3.

| Measure | Figure |
|---|---|
| Reading all 31 documents from empty, four calls at a time | 138 s wall time, $1.62 |
| The same, one call at a time | 486 s, the sum of the 31 measured call times |
| One reading call | median 15.2 s, $0.048, 10,935 tokens in (9,817 of them read from the cache) and 1,818 out |
| Filling an empty store from the saved results, no model | 0.29 s |
| `ingest` again on a filled store | 0.04 s |
| Adding one document | 0.06 s of code, plus one reading call, so about 15 s |
| Answering a question about one patient, plan saved | 3 to 156 ms of code, no model |
| Answering a new question about one patient | 6.6 to 9.3 s end to end, of which the plan call is all but 0.2 s; $0.020 to $0.045 |
| Answering a new question across the collection (which patients had two consecutive weeks below the goal) | 6.0 s end to end, on one patient, which shows little |
| The store | 492 KB for 31 documents, 16 KB a document including the document's own text; 474 claims |
| Model use over the whole build | 278 calls, $16.96: 250 reading calls (including 153 for the model comparison) and 28 plan calls |

**Estimates**, in `output/benchmarks/estimates.md` and nowhere else: reading 500,000 documents once would cost about $26,000 with this model at this effort and take about 34 hours at 64 calls at a time; the store would be about 8 GB and the saved results about 3 GB. A day's 1,000 new documents would cost about $52.

## 7. The design decision tested: which model reads the documents

The reading step is the only place the model's judgement enters, so the question was whether the rules make the answer robust to it. All 31 documents were read six times, with the same prompt, and the rules run on each read: Opus at low, medium and high effort; Sonnet at low; Haiku at low; Fable at low. The report is `output/comparison/models-and-efforts.md`.

| Read | Cost | Reaches the key's figures |
|---|---|---|
| Opus, low (the setting used) | $1.62 | Yes |
| Opus, medium | $1.98 | Yes |
| Opus, high | $2.25 | Yes |
| Sonnet, low | $0.93 | Yes |
| Fable, low | $5.06 | Yes |
| Haiku, low | $2.46 | No: three contacts lose their minutes, week 3 becomes "cannot be determined", and one finding is missing |

**What was learned.** Five of the six reads reach identical conclusions: the same 20 contacts with the same statuses and minutes, the same four verdicts, the same three conflicts settled the same way, the same scores. They do so although the readings themselves differ: only 7 to 21 of the 31 documents came back with the same count-bearing facts as the baseline. The rules absorb the differences, because they act on what a document states and not on how the model labelled it. Two of those rules were tightened by the comparison: a no-therapy interval is now removed whatever label the model gave it, and a claim about "the contact" in a document that refers to one contact is attached to that contact. Neither changed a figure at the baseline. The practical result is that Sonnet at $0.93 and Opus at $1.62 are interchangeable on this record, and effort above low buys one more of the key's 42 cited observation lines for 22 to 39 percent more cost.

## 8. An observed limitation, and how to investigate it next

**The rules can only work with what the reading returns.** Haiku called the attendance register BH-D108 a schedule export. A schedule status cannot establish attendance (rule 10), so the Jan 22 and Jan 29 groups lost their minutes and week 3 fell to "cannot be determined". The code does not override a model's reading of what kind of document it has, and it has no second opinion to compare against.

A smaller instance of the same thing is on the record at the setting used: the key's DEV-05 table marks seven statements as the patient's that Opus at low effort attributed to the clinician ("Rowan selected...", "Rowan agreed..."). Six models and efforts read one of them, BH-D105 line 9, the same way as each other and differently from the key. No figure depends on it, but it shows the reading step is where variance lives.

**Next.** Read each document twice, with two different models, and compare the two readings' section kinds and count-bearing facts. Where they disagree, either read a third time or mark the document for review, and let the answer say that a document's kind is disputed. The saved-result mechanism and the `compare` command already make this cheap to try: the second read is one more settings file, and the comparison is a command. The measured cost of the second read with Sonnet is $0.03 a document.

## 9. The first bottleneck at a million documents

Section 5 of `benchmark.md` runs the same queries on a store holding the patient copied 10, 100 and 1,000 times over (31,000 documents), on synthetic copies.

| Patients | One patient's `care_delivered` | The plan call's input (`ask.build_message`) | `patients_below_goal` |
|---|---|---|---|
| 1 | 50 ms | 1 ms, 2,671 characters | 4 ms |
| 100 | 85 ms | 162 ms, 9,403 characters | 496 ms |
| 1,000 | 44 ms | 1,272 ms, 70,603 characters | 6,252 ms |

**The constraint is `functions.patients_in`**, called by `ask.build_message` for every question. It lists every patient in the collection, with one query each for their plan rules, and puts the whole list into the plan call's prompt so that the model can say which patient the question names. At 1,000 patients that is 1.3 seconds and 70,000 characters per question, while a question about one patient stays at 44 ms. At a million documents, about 32,000 patients at this record's size, it is an estimated 40 seconds and 2 MB of prompt per question, before the model is called. The same walk is in `patients_below_goal`, which loads each patient's weeks one query at a time: an estimated three and a half minutes at 32,000 patients.

**What I would change.** Keep a `patients` table with an index on the record number and on the name, written at ingest. Resolve the patient the question names by lookup, in code, before the plan call, and give the model only the matching patient (or the few candidates for an ambiguous name). For the collection-wide question, store each patient's run of weeks below the goal as a column of `weekly_status` at ingest, so the question is one indexed query. Both are changes to two functions; the store's shape and the rules stay as they are. Reading, which is one call per document and parallel, does not slow with the collection; it costs money, not time, and the estimate for that is in section 6.

Three smaller ones were found and fixed by the same measurement: the copies check ran one full scan of the documents table per contact; the `documents` table had no index on the patient; and once it had one, SQLite preferred a status index to it and scanned every read document, until both indexes were made composite. A question about one patient now takes the same time on 31,000 documents as on 31.

## 10. Not built, and tradeoffs

| Item | Treatment |
|---|---|
| A second patient, and a plan change | The rules and the store carry the patient on every row and carry the plan's dates, and both are tested on made-up records (`test_patients.py`, `test_rules.py`). No supplied document holds a second patient or a plan change, and no test document was written for them. The collection-wide question therefore runs on one patient. Which plan governs a week that contains a change is not decided |
| A question whose second step depends on the first result | Not handled. One plan call, no tool loop. The answer says which part it could not do |
| Near matches on patient identity | A patient is matched by record number or by name as written, and a first name that matches exactly one patient. Nothing fuzzier |
| Reviewer rulings on an open conflict | Not built. Each open conflict says what would settle it; a ruling would be one more claim of a new kind, with the same standing as a signed correction |
| Retractions, chained corrections, summary documents | Stay open under rule 11 and are reported as such |
| Re-reading after a prompt change | The version stamp is on every claim and every saved result. Raising `prompt_version` in `settings.toml` makes `ingest` read every document again; the old results stay on disk. The process is not automated beyond that |
| The model's summary paragraph | Not built. Every sentence of an answer is written by code from the results. The cost is that the "what the record supports and does not settle" block of DEV-05 is built from general rules and never judges: it quotes the latest statement on sleep rather than saying sleep is not stable |
| Batch processing, a smaller model, a different database | Described in section 9. Sonnet reaches the same figures at 57 percent of the cost |
| A user interface, search by similarity, probabilities, authorization units, time zones, scanned documents | Left out. Authorizations are read but not stored, so a question about units left is answered "cannot answer" with the document named |

**Tradeoffs made on purpose.** The reading prompt was adjusted while looking at eleven of the 31 documents only, so the other twenty test it fairly; examples in the prompt are made up. The answer key was fixed before the build and shares the reading that shaped the rules, so checks 1 to 11 do not use it. Answers are long, because parts 4 and 5 carry a citation for every figure; the lead at the top is there so the figure can be read in one line.

## 11. Models, settings and assistance

| Item | Value |
|---|---|
| Reading | The `claude` command-line tool, one call per document, no tools given to the model, our own system prompt (`prompts/reading.md`, version 3), output constrained to a JSON schema, `--effort low`, a $0.50 cap per call, four calls at a time. Model alias `opus`, served as `claude-opus-5-5` |
| Planning a question | The same tool and model, `prompts/plan.md` version 2, one call per new question |
| Comparison reads | `sonnet` (`claude-sonnet-5-5`), `haiku` (`claude-haiku-4-5-20251001`), `fable` (`claude-fable-5-1`), and `opus` at medium and high effort. Settings files in `output/comparison/` |
| Coding assistance | Claude Code (Anthropic), model Claude Fable 5.1, in several sessions. The design was discussed and decided before any code was written; the decisions are in `decisions.md`. The code, the tests and this README were written in those sessions and checked by the tests and by a second session reading the answers against the key |
| Runtime | Reading all 31 documents: 2 min 18 s. The whole test suite: about 15 s. Answering the fourteen saved questions: under 2 s |
| Model cost | $16.96 over the build, of which $1.62 is the read used, $10.70 the model comparison, and $0.69 the 28 plan calls |
