# Reading effort: low against medium

Superseded by `models-and-efforts.md`, which adds Opus at high, Sonnet, Haiku and Fable. Kept as the first comparison.

The comparison run for O-44. The 31 documents were read a second time with the same model (Opus) and the same prompt (version 3), with the tool's effort set to medium instead of low. Everything below is measured; nothing is estimated.

Run on 2026-09-30. The medium results are saved in `output/readings/*__opus__medium__v3.json` and the store built from them is `output/comparison/medium.sqlite`. The check `test_a_read_at_medium_effort_gives_the_same_figures` replays them with no model.

## Cost and time

| Measure | Low | Medium | Change |
|---|---|---|---|
| Calls | 31 | 31 | |
| Rejected | 0 | 0 | |
| Cost, as the tool reports it | $1.62 | $1.98 | +22% |
| Time summed over the calls | 486 s | 957 s | +97% |
| Time from start to finish, four at a time | 2 min 18 s | about 5 min | |
| Tokens out | 60,078 | 78,177 | +30% |

## What came back

| Measure | Low | Medium |
|---|---|---|
| Claims | 474 | 535 |
| Observations | 140 | 175 |
| Quotes found at the stated line | 474 of 474 | 535 of 535 |
| Values not captured, of 448 | 3 | 2 |
| Documents whose count-bearing facts are identical between the two reads | 20 of 31 | |

The 11 documents that differ do so in labels and in details returned by one read and not the other. Examples: D109 gives the patient's status as "absent" at low and "other" at medium; D105 gives its 30 minutes as "with the patient" at low and "for the contact" at medium; D015 prints the encounter number in the appointment field at medium.

## What the rules make of it

| Conclusion | Low | Medium |
|---|---|---|
| Encounters | 20 | 20 |
| Statuses and minutes of the 20 | As the key | As the key |
| Weekly verdicts | Not met, not met, met, cannot determine | The same |
| Weekly minutes | 140, 120, 180, 145 or 155 | The same |
| Conflicts | 3, the same rules | The same |
| Findings | 3 | The same |
| Assessments | 18, 14, 10 | The same |
| Administrative records | 6 | 7: the portal notice of Jan 15 is a record of its own at medium |

## The key's citations in section 7

| Result | Low | Medium |
|---|---|---|
| A claim holds it, with the same speaker | 40 of 42 | 41 of 42 |
| No claim holds it | 1: D009 line 14 | 0 |
| A claim holds it with a different speaker | 1: D105 line 9 | 1: D105 line 9 |

The speaker of D105 line 9 is "clinician" at both efforts. The key has "patient". That is a reading of the sentence, not an effect of effort.

## Two things the comparison found in the code

- D015 at medium printed the encounter number in the appointment field. Rule 1 matched numbers only within the same field, so two contacts got the same id and the rebuild failed. Rule 1 now matches a number in either field, and the store never reuses an id.
- D011 at medium returned a reference to "the missed appointment from the prior week" with no number and no date, and an attendance status for it. It became an encounter with no date. A reference with no number and no date is now a mention (D-41).

Neither changes a figure at low effort. Both are in the checks.
