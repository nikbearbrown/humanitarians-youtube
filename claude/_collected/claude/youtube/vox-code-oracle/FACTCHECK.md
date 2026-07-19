# FACTCHECK — vox-code-oracle

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | Developer copied AI-fixed code; tests failed in a new way; bug lived three files away | ✓ | Chapter 04: "A developer pastes a broken function into Claude chat. Claude produces a corrected version. The developer copies it back in. Thirty seconds later the tests fail in a new way — because the function was broken for a reason that lived three files away, and Claude chat had no idea those files existed." | — |
| B05 | Code correctness established by external verification: tests, builds, type-checkers, linters | ✓ | Chapter 04: "Code is not done when it is written. It is not done when it reads correctly. It is done when it passes external verification: tests run, builds complete, type checks pass, linters clear." | — |
| B05 | Mark Chen and colleagues introduced HumanEval because code cannot be judged by appearance | ✓ | Chapter 04: "Mark Chen and colleagues (2021) introduced HumanEval, the field's foundational code-evaluation benchmark, precisely because code cannot be judged by appearance." | — |
| B07 | Practitioner rule: trust the oracle, not the output | ✓ | Chapter 04: "This is the practitioner rule: trust the oracle, not the output." — verbatim | — |
| B08 | Productivity research found speedups on well-defined tasks with clear oracle; gains shrink without one | ✓ | Chapter 04: "Studies of AI coding assistance have found speedups on well-defined, self-contained tasks (Dohmke, et al., 2023). The key variable is whether the task has clear scope and a clear oracle. Without those, the gains shrink and the review burden grows." | — |
| B09 | Off-by-one error on empty input; zero exceptions, zero alerts, wrong output shipped | Illustrative | Constructed example per card spec. Derived from chapter 04 framing. | None needed |
| B11 | Paste into chat = no oracle; agent with test runner = oracle | ✓ | Chapter 04: "When you paste code into chat and Claude improves it, you have no oracle. When you use Claude Code to fix a failing test, you have an oracle: does the test now pass?" | — |

## Terms Table
| Term | Debut beat | Prior beat |
|---|---|---|
| oracle | B05 | B04 established naive appearance model is wrong; viewer wants mechanism |
| HumanEval | B05 | B05 itself (citation for oracle necessity, not a standalone defined term) |

## Exclusion Confirmation
- NO formal verification or proof-based methods: PASS (absent)
- NO extended test coverage metric discussion: PASS (oracle concept only)
- NO fuzzing or property-based testing: PASS (absent)

## Illustrative Examples
- B09: off-by-one, 40 clients, empty dataset — ILLUSTRATIVE (from card spec)
