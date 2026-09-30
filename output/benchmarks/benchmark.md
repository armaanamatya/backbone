# Benchmark, measured on 2026-09-30

Everything in this file is measured. Model: opus, effort low, reading prompt version 3, plan prompt version 2, 4 calls at a time. Estimates are in `estimates.md`.

## 1. Reading all the documents from empty

From the logs of the ingest runs that called the model under these settings. The run's wall time is the time from its first event to its last, with the calls running four at a time after the first. The sum of the call times is what one call at a time would take, each call measured on its own.

| Run | Documents read | Calls | Accepted | Run wall time | Sum of call times | Cost | Tokens in | Tokens out |
|---|---|---|---|---|---|---|---|---|
| 2026-09-29 13:14 | 31 | 31 | 31 | 138 s | 486 s | $1.62 | 339,418 | 60,078 |

Per document, over 31 accepted calls:

| Measure | Median | Mean | Min | Max |
|---|---|---|---|---|
| Seconds a call | 15.2 | 15.7 | 10.7 | 23.7 |
| Cost | $0.048 | $0.052 | $0.032 | $0.123 |
| Tokens in (prompt, document and cache) | 10,935 | 10,949 | 10,833 | 11,198 |
| Of which read from the cache | 9,817 | 9,500 | 0 | 9,817 |
| Tokens out | 1,818 | 1,938 | 1,088 | 3,367 |

Every model call in the logs, all purposes and all models: 283 calls, $17.10. By purpose: reading 250 calls, $16.27; plan 33 calls, $0.82.

## 2. Re-running from saved results, and adding one document

| Measure | Time | What runs |
|---|---|---|
| Fill an empty store from the saved results of 31 documents | 0.31 s (min 0.29, max 0.35, over 5 runs) | Hash, register, load each saved result, check every quote, rebuild the conclusions. No model |
| `ingest` again on the filled store | 0.055 s (min 0.047, max 0.176, over 5 runs) | Hash 31 files, find every one known, read nothing |
| Add one document to a store holding the other 30, code only | 0.079 s (min 0.047, max 0.139, over 5 runs) | Hash, register, load its saved result, check its quotes, rebuild the patient's conclusions (symptom_measure_review_jan16.txt) |
| Add one document, with its model call | 15.3 s | The code time above plus the median reading call from section 1 (15.2 s) |

## 3. Answering a question

Code time is measured here, from the saved plan, with the model switched off. The plan call's time and cost are from the logs of the calls that made the plans. A question with a saved plan calls no model; a new question makes one plan call.

| Question | Functions | Code time (median) | Plan call | Plan cost | Lines |
|---|---|---|---|---|---|
| DEV-01 | care_delivered, care_delivered, not_counted, conflicts_and_findings | 157 ms | 9.6 s | $0.037 | 250 |
| DEV-02 | care_delivered, care_delivered, not_counted, conflicts_and_findings | 148 ms | 7.6 s | $0.026 | 240 |
| DEV-03 | goal_status, care_delivered, conflicts_and_findings, not_counted | 152 ms | 7.4 s | $0.024 | 264 |
| DEV-04 | date_detail, date_detail, care_delivered, not_counted, conflicts_and_findings | 70 ms | 8.4 s | $0.027 | 96 |
| DEV-05 | observations, date_detail, assessments, conflicts_and_findings | 105 ms | 9.3 s | $0.028 | 357 |
| P-1 |  | 5 ms | 6.2 s | $0.020 | 48 |
| P-2 |  | 6 ms | 7.9 s | $0.023 | 49 |
| P-3 | date_detail, conflicts_and_findings | 28 ms | 7.4 s | $0.021 | 72 |
| P-4 | assessments, date_detail | 25 ms | 6.4 s | $0.021 | 61 |
| P-5 | goal_status, care_delivered, care_delivered | 141 ms | 12.7 s | $0.026 | 196 |
| P-6 | date_detail | 11 ms | 6.5 s | $0.020 | 49 |
| P-7 | care_delivered, not_counted | 82 ms | 6.4 s | $0.021 | 212 |
| P-8 | care_delivered, not_counted | 37 ms | 7.1 s | $0.023 | 103 |
| P-9 |  | 4 ms | 6.8 s | $0.021 | 50 |

New questions asked end to end, plan call included (the related questions in section 8 of the key). Their answers are in `output/answers/related/`. A row marked "plan reused" found its plan saved from an earlier run, so it called no model this time: its end-to-end figure is the code time measured now plus the plan call's time from the log of the run that made the plan.

| Question | Functions | End to end | Plan call | Plan cost | Tokens out |
|---|---|---|---|---|---|
| Q-1: How many sessions did Rowan attend from January 12 to January 25, 2026, by type, and on how many days? | care_delivered, care_delivered | 8.3 s (plan reused) | 8.3 s | $0.045 | 507 |
| Q-2: How many therapy sessions did Rowan attend in each week of the episode? | care_delivered | 7.4 s (plan reused) | 7.3 s | $0.020 | 429 |
| Q-7: Which of Rowan's therapy sessions had more than one clinician? | care_delivered, care_delivered, conflicts_and_findings | 9.2 s (plan reused) | 9.1 s | $0.028 | 792 |
| Q-9: Was Rowan's treatment plan goal met in the week of January 19, 2026, and by how much? | goal_status, not_counted, conflicts_and_findings | 6.6 s (plan reused) | 6.5 s | $0.024 | 600 |
| Q-13 (collection-wide): Which patients had two consecutive weeks below their treatment plan goal, and does any of them depend on unresolved documentation? | patients_below_goal | 6.0 s (plan reused) | 6.0 s | $0.020 | 396 |

## 4. Size of the saved abstraction

| Measure | Value |
|---|---|
| `output\abstraction.sqlite` | 503,808 bytes (492 KB) |
| Source text inside it | 50,106 bytes |
| Store bytes per document | 16,252 |
| Rows | documents 31, claims 474, contacts 26, conflicts 3, findings 3, plan_rules 10, assessments 3, weekly_status 4 |
| Saved reading results, these settings | 31 files, 205,136 bytes |
| Saved reading results, every model and effort tried | 1,547,890 bytes |
| Logs | 792,438 bytes |
| Answers | 1,997,816 bytes |

## 5. The same queries on a larger store

Measured on synthetic copies: the patient's rows copied under new record numbers, in a temporary store. Each figure is the median of three runs.

| Patients | Documents | Store | care_delivered, one patient | resolve_patient, by record number | patients_in, the list every plan call is given | build_message, the plan call's input | patients_below_goal, across the collection | known_hashes, the duplicate check at ingest |
|---|---|---|---|---|---|---|---|---|
| 1 | 31 | 0 MB | 50 ms | 1 ms | 1 ms | 1 ms, 2,671 chars | 4 ms | 0 ms |
| 10 | 310 | 4 MB | 63 ms | 9 ms | 9 ms | 11 ms, 3,283 chars | 54 ms | 1 ms |
| 100 | 3,100 | 39 MB | 85 ms | 96 ms | 152 ms | 162 ms, 9,403 chars | 496 ms | 17 ms |
| 1,000 | 31,000 | 391 MB | 44 ms | 1866 ms | 1917 ms | 1272 ms, 70,603 chars | 6252 ms | 76 ms |

