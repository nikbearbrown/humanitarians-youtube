# FACTCHECK — pi-memory-task-review (Week 4)

**This is a re-analysis of saved pilot runs (`multihop_a9aff89630`, audited). No new Pi runs, no API calls.**
Every number below was recomputed from the per-run records (`run.json` call lists, `tool_errors`,
`evaluation.audited.json`) and asserted at build time. Only the resulting numbers are in `evidence.json`.

| # | Claim | Verdict | Derivation |
|---|---|---|---|
| 1 | Procedural: fewer calls than no memory on 4/6, equal 1, more 1 | TRUE | per-task call counts |
| 2 | Metacognitive: fewer 3, more 3 | TRUE | per-task call counts |
| 3 | Both: fewer 2, equal 1, more 3 | TRUE | per-task call counts |
| 4 | One task (routing_2): no memory 12 calls, 2 KeyErrors | TRUE | `calls` length 12; `tool_errors` 2; labels KeyError ×2 |
| 5 | Same task, metacognitive: 3 calls, 0 tool errors | TRUE | `calls` length 3; `tool_errors` 0 |
| 6 | Means: none 6.00, procedural 4.33 | TRUE | 36/6, 26/6 |
| 7 | Without that task: none 4.80, procedural 4.40 (gap 1.67 → 0.40) | TRUE — re-analysis arithmetic, added by Claude, approved for inclusion pending fellow review | 24/5, 22/5 |
| 8 | Metacognitive 0 tool errors vs 2 without memory (whole pilot) | TRUE | summed `tool_errors` |
| 9 | All numeric answers correct; one combined-memory run failed the evidence check | TRUE | `evaluation.audited.json`: both = 5/6 (aliases_2) |
| 10 | Next steps: repeat with frozen memories; selective retrieval; stale/conflicting lessons | Fellow's plan | WEEK3_ANALYSIS next milestone |

One repetition per condition. No claim of general improvement.
