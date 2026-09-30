# Estimates at 500,000 documents

Every figure in this file is an estimate: a measured figure from `benchmark.md` multiplied out. Nothing here was run at this size.

## Reading every document once

| Estimate | Figure | From |
|---|---|---|
| Cost of reading 500,000 documents with opus at low | $26,100 | $0.052 a document, the mean over 31 calls, times 500,000 |
| Time, at 4 calls at a time as now | 544 hours | 15.7 s a call, times 500,000, over 4 |
| Time, at 64 calls at a time | 34 hours | The same, over 64. The service's rate limits, not the code, would set the true figure |
| Daily arrivals of 1,000 documents | $52 and 65 minutes a day | The same figures, times 1,000 |

## Storage

| Estimate | Figure | From |
|---|---|---|
| The store | 8.1 GB | 16,252 bytes a document, which includes the document's text |
| The saved reading results | 3.3 GB | 6,617 bytes a document |

## Where the code slows first

Section 5 of `benchmark.md` measures the queries on a store of the patient copied over. Read along a row: the timing that grows with the number of patients is the one that limits a collection, and the one that stays flat is fine. The reading of these figures is in the README.

