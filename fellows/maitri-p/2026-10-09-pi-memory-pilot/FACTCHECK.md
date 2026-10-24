# FACTCHECK — pi-memory-pilot

Source: recorded pilot `multihop_a9aff89630`, audited report v3.0.1, read-only. No experiment
re-run, no API calls. Only the values below were copied (see `evidence.json`).

| # | Claim on screen / in narration | Verdict | Source field |
|---|---|---|---|
| 1 | Mean tool calls: none 6.00 · procedural 4.33 · metacognitive 5.00 · both 6.83 | TRUE (asserted in build) | `summary.*.mean_tool_calls` |
| 2 | 6 test questions per condition, 1 repetition | TRUE | `summary.*.runs` = 6; experiment notes: one repetition |
| 3 | Three practice questions; lessons frozen; fresh sessions for evaluation | TRUE | experiment notes |
| 4 | Every numeric answer correct | TRUE | experiment notes: "All numeric answers were correct" |
| 5 | One combined ("both") run cited the wrong rule | TRUE — citation-compliance failure, not a wrong answer | `both.passed` = 5/6; experiment notes |
| 6 | Metacognitive lesson text (WHEN / DO / INSTEAD OF) | VERBATIM fragments, trimmed with "…"; asserted against stored lesson | `memories.json` metacognitive `trigger` / `lesson` |
| 7 | Lesson saved after repeated KeyErrors in practice | TRUE | experiment notes: "repeated path-key lookup errors" |
| 8 | Metacognitive condition logged zero tool errors | TRUE — descriptive only, no causal claim | `metacognitive.tool_errors` = 0 |
| 9 | (4.33 − 6.00)/6.00 ≈ −28% | TRUE — −0.278 | arithmetic on #1 |
| 10 | "Early signal, not proven improvement"; next: 3 repetitions | TRUE | report limits; `--repeats 3` in experiment notes |

Lower tool calls = more efficient search, not higher accuracy. Wilson intervals overlap; no
difference between conditions is claimed.
