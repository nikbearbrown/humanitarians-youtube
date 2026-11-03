# PROOF review (pre-Gate P): long film and Short, after the intro and sign-off were added

Method: every claim in both scripts was read against the committed report, the agent log and the recipe in `nikbearbrown/mycroft` `main`.

## Defects found and fixed in the scripts
| # | Where | Found | Fix |
|---|---|---|---|
| 1 | Long B02 | "two customers, twice" is three words, narration said four | "three words" |
| 2 | Long B03, Short S2 | "nothing in it is prose" / "no prose": the log carries evidence and condition strings | "built for a script, not a reader" |
| 3 | Long B04 | "without opening a single other file": the report points to files | "written as sentences a person can act on" |
| 4 | Long B05, Short S4 | "taken from the log's" / "a check compares every time": both pages are computed from the same files and the counts are compared before writing | "both computed from the same files"; "compared before the report is written" |
| 5 | Long B12 | "the report says that plainly too" had no precise referent | the report's source list gives status DRAFT and version 0.3.1 (verified) |
| 6 | Short S5 | "Approve the next phase: yes" dropped "sample mode only", which the report states | restored |

## Scores (after fixes)
| Criterion | Long | Short |
|---|---|---|
| Purpose: one actionable takeaway | 2 | 2 |
| Accuracy: every claim traced | 2 | 2 |
| Structure: its own shape | 2 | 2 |
| Tone: positive, humble, first person | 2 | 2 |
| Clarity: one idea per beat, numbers in words | 2 | 2 |
| Distinctness from W24 to W28 | 2 | 2 |

Length: long 748 words (about 4.6 min); Short 259 words (about 86 s).

## For your read at Gate P (judgement calls)
1. B08 admits "my check matched its own line": the method working, but it is your voice.
2. B10 "same bytes" holds with the clock pinned, as narrated.
3. The introduction says "public repository where work is written as recipes"; the sign-off line is yours verbatim.
4. Short S5 reads out both "Approve (sample mode only): yes" and "Block live execution: yes"; both are the report's own lines (verified).
