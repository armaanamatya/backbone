# Reads compared. Baseline: opus at low.

Everything here is measured. The rules ran on each run's saved results with no model.

## Cost and time

| Run | Calls | Rejected | Cost | Seconds over the calls | Tokens out | Served by |
|---|---|---|---|---|---|---|
| opus at low | 31 | 0 | $1.62 | 486 | 60,078 | claude-opus-5-5 |
| opus at medium | 31 | 0 | $1.98 | 957 | 78,177 | claude-opus-5-5 |
| opus at high | 31 | 0 | $2.25 | 853 | 95,408 | claude-opus-5-5 |
| sonnet at low | 31 | 0 | $0.93 | 546 | 66,117 | claude-sonnet-5-5 |
| haiku at low | 60 | 29 | $2.46 | 4205 | 438,600 | claude-haiku-4-5-20251001 |
| fable at low | 31 | 0 | $5.06 | 985 | 81,836 | claude-fable-5-1 |

## What came back

| Run | Documents read | Claims | Quotes not found | Values not captured | Documents with the baseline's count-bearing facts |
|---|---|---|---|---|---|
| opus at low | 31 | 474 | 0 | 3 | 31 of 31 |
| opus at medium | 31 | 535 | 0 | 2 | 21 of 31 |
| opus at high | 31 | 563 | 0 | 2 | 20 of 31 |
| sonnet at low | 31 | 450 | 0 | 4 | 15 of 31 |
| haiku at low | 31 | 474 | 2 | 7 | 7 of 31 |
| fable at low | 31 | 626 | 0 | 2 | 13 of 31 |

## What the rules make of it

| Run | Encounters | Statuses and minutes | Weekly verdicts and minutes | Conflicts | Findings | Assessments | Totals |
|---|---|---|---|---|---|---|---|
| opus at low | 20 (same) | same | same | same | same | same | same |
| opus at medium | 20 (same) | same | same | same | same | same | same |
| opus at high | 20 (same) | same | same | same | same | same | same |
| sonnet at low | 20 (same) | same | same | same | same | same | same |
| haiku at low | 20 (same) | DIFFERS | DIFFERS | DIFFERS | DIFFERS | same | DIFFERS |
| fable at low | 20 (same) | same | same | same | same | same | same |

## Weekly verdicts

- opus at low, HG-M042: 2026-01-05: not met (140); 2026-01-12: not met (120); 2026-01-19: met (180); 2026-01-26: cannot determine (145 or 155)
- opus at medium, HG-M042: 2026-01-05: not met (140); 2026-01-12: not met (120); 2026-01-19: met (180); 2026-01-26: cannot determine (145 or 155)
- opus at high, HG-M042: 2026-01-05: not met (140); 2026-01-12: not met (120); 2026-01-19: met (180); 2026-01-26: cannot determine (145 or 155)
- sonnet at low, HG-M042: 2026-01-05: not met (140); 2026-01-12: not met (120); 2026-01-19: met (180); 2026-01-26: cannot determine (145 or 155)
- haiku at low, HG-M042: 2026-01-05: not met (140); 2026-01-12: not met (120); 2026-01-19: cannot determine (135); 2026-01-26: cannot determine (70 or 80)
- fable at low, HG-M042: 2026-01-05: not met (140); 2026-01-12: not met (120); 2026-01-19: met (180); 2026-01-26: cannot determine (145 or 155)

## Where a run differs from the baseline

- opus at medium: count-bearing facts differ in BH-D006, BH-D011, BH-D012, BH-D016, BH-D104, BH-D105, BH-D107, BH-D108, BH-D109, BH-D115
- opus at high: count-bearing facts differ in BH-D001, BH-D006, BH-D011, BH-D012, BH-D015, BH-D016, BH-D104, BH-D105, BH-D108, BH-D111, BH-D115
- sonnet at low: count-bearing facts differ in BH-D002, BH-D006, BH-D007, BH-D008, BH-D009, BH-D012, BH-D014, BH-D015, BH-D101, BH-D103, BH-D104, BH-D105, BH-D107, BH-D108, BH-D109, BH-D111
- haiku at low, HG-E113: baseline ('held', [45]), this run ('held', [])
- haiku at low, HG-E118: baseline ('held', [75]), this run ('held', [])
- haiku at low, HG-E120: baseline ('held', [20]), this run ('held', [])
- haiku at low, conflicts: baseline [('HG-M042/HG-E110:departure', 'settled', '8, then 9'), ('HG-M042/HG-E115:start', 'open', '11'), ('HG-M042/HG-E116:attendance', 'settled', '10')], this run [('HG-M042/HG-E110:departure', 'settled', '8, then 9'), ('HG-M042/HG-E115:start', 'open', '11')]
- haiku at low, findings: baseline ['charge_without_attendance', 'draft_made_before_the_service', 'note_signed_after_the_service_date'], this run ['charge_without_attendance', 'note_signed_after_the_service_date']
- haiku at low, totals: baseline [(12, 11, 585), (12, 11, 595)], this run [(12, 11, 465), (12, 11, 475)]
- haiku at low: count-bearing facts differ in BH-D001, BH-D002, BH-D003, BH-D005, BH-D006, BH-D008, BH-D010, BH-D011, BH-D012, BH-D013, BH-D014, BH-D015, BH-D016, BH-D101, BH-D103, BH-D104, BH-D105, BH-D106, BH-D107, BH-D108, BH-D111, BH-D113, BH-D114, BH-D115
- fable at low: count-bearing facts differ in BH-D001, BH-D002, BH-D007, BH-D009, BH-D011, BH-D012, BH-D013, BH-D014, BH-D015, BH-D016, BH-D103, BH-D104, BH-D105, BH-D107, BH-D108, BH-D111, BH-D112, BH-D115
