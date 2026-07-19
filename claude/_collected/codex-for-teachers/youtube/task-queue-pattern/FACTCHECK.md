# FACTCHECK — task-queue-pattern
**Build the Task Queue Pattern with Claude: Parallel Work Without Context Bloat**
Source: `codex-for-teachers/chapters/10-task-queue.md`

---

## Claims audit

| # | Beat | Claim | Verdict | Source / Note |
|---|------|-------|---------|---------------|
| 1 | B00 | The task queue is a third option between breaking focus and losing the idea | ✓ | Chapter thesis: the task queue pattern enables parallel investigation without contaminating the main session context. |
| 2 | B01 | The task queue relocates supervision — it does not eliminate it | ✓ | Chapter: the pattern moves supervisory work to the evaluation step, not away from it. |
| 3 | B01 | Two rules: only fire what you will return to; evaluate every return before the next session ends | ✓ | Chapter names these as the two governing rules of the task queue pattern. |
| 4 | B01 | Unevaluated task queue returns are ambient debt | ✓ | Chapter uses the debt metaphor for unevaluated returns — they accumulate and compound into the next session's context. |
| 5 | B04 | Task queue return: No recommendation with 2 reasons, ~15 lines implementation estimate | SYNTHETIC | Illustrative return consistent with the chapter's description of a well-formed task queue return. Specific content is synthetic. |
| 6 | B04 | Evaluation: REVISE — implement line-count variance, not average | SYNTHETIC | Illustrative evaluation consistent with the chapter's USE/REVISE/REVERT framework. |
| 7 | B06 | Unevaluated return leads Codex to implement a feature AGENTS.md explicitly excludes | ✓ | Chapter: unevaluated returns become ambient permission in the next session's context. The failure mode is described explicitly in the chapter. |
| 8 | B07 | Evaluation labels: USE, REVISE, REVERT | ✓ | Chapter names these three evaluation labels as the required vocabulary for task queue returns. |

---

## Exclusions confirmed
- No discussion of task queue for longer-running investigations (multi-session)
- No discussion of task queue item prioritization
- No discussion of concurrent multiple task queue items

## Synthetic scenarios
Task queue item content (investigation topic, specific recommendation, implementation line count) and evaluation outcomes are illustrative examples consistent with the source chapter's pattern description. Not transcripts of actual Claude sessions.
