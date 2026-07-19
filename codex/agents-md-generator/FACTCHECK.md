# FACTCHECK — agents-md-generator

## Claims Table

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B01 | AGENTS.md is a communication protocol between you and a stateless collaborator; Codex starts every session with no memory | ✓ | Ch07: "AGENTS.md is a communication protocol between you and a stateless collaborator. Codex starts every session with no memory of the last." Verbatim. | — |
| B01 | 20 minutes to write AGENTS.md; repaid at start of every subsequent session | ✓ | Ch07: "The 20 minutes it takes to write AGENTS.md is repaid at the start of every subsequent session." Verbatim. | — |
| B01 | Only if file contains what Codex can't infer from code, not what it already knows | ✓ | Ch07: "only if the file contains what Codex can't infer from the code, not what it already knows." Verbatim. | — |
| B04 | 23 entries in draft; 14 INFERABLE, 9 NEEDS HUMAN INPUT | Illustrative | Synthetic count illustrating the INFERABLE/NEEDS HUMAN INPUT split from Ch07. Numbers are illustrative. | Marked synthetic. |
| B04 | INFERABLE examples: GDScript snake_case, Godot 4.x API, standard scene structure | Illustrative | Constructed from Ch07 examples of what Codex can infer from code. | Marked synthetic. |
| B04 | Cleaned final: 9 entries, under 40 lines | Illustrative | Synthetic result illustrating the pruning step. | Marked synthetic. |
| B06 | Lessons learned grows with 4 entries; Stack/Style/Architecture/Environment unchanged | Illustrative | Illustrates the design of the Lessons learned section from Ch07. | Marked synthetic. |

## Illustrative Scenarios
- B04: Entry counts (23 draft, 14 INFERABLE, 9 NEEDS HUMAN INPUT) — SYNTHETIC. Illustrates the tagging discipline from Ch07.
- B06: Lessons learned entries (packed scenes, export key, AnimationPlayer, delta accumulation) — SYNTHETIC. Consistent with Godot development patterns referenced in Ch07.
- All code outputs are synthetic demonstrations.
