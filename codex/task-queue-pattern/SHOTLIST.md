# SHOTLIST — task-queue-pattern

**Build the Task Queue Pattern with Claude: Parallel Work Without Context Bloat** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/10-task-queue.md
Series: CODEX FOR TEACHERS — Reel 07 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"Every tangential idea that fires during a focused build is a choice…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"The task queue relocates supervision — it does not eliminate it…"
Slate: problem statement — two rules, ambient debt of unevaluated returns.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: TASK QUEUE ITEM — investigate average submission length, return yes/no with reasons.
runningText: "running background task…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `task_queue.sh`
Shows pattern: main session in left pane, background claude call in right, evaluation labels.

## B04 — SLATE (~20s)
"Task queue return: No — average submission length is noisy…"
Slate: output — REVISE evaluation, implement line-count variance. Main session unaffected.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: fire-and-forget failure — skip evaluation, next session starts with unevaluated item.
runningText: "simulating unevaluated return…"

## B06 — SLATE (~14s)
"Unevaluated return becomes ambient permission — Codex begins implementing excluded feature…"
Slate: task queue items are inputs to the next session, not decoration.

## B07 — SLATE (~12s)
"Two rules: only fire what you will return to, evaluate every return…"
Slate: summary — USE/REVISE/REVERT labels, one-line rationale.

## B08 — SLATE (~8s)
"Next: write the post-build document that converts build experience into teaching capacity."
Slate: next-steps bridge card.

## B09 — REMOTION: NikBearBrownOutro (~8s)
Standard outro props.

---

## Slot inventory

| Slot | Need | Status |
|------|------|--------|
| B00 | Intro slate | vox_compile auto-generates |
| B01 | Problem slate | vox_compile auto-generates |
| B02 | Remotion: NikBearBrownTerminalAsk | Remotion render needed |
| B03 | Remotion: NikBearBrownCodeBlock | Remotion render needed |
| B04 | Output slate | vox_compile auto-generates |
| B05 | Remotion: NikBearBrownTerminalAsk | Remotion render needed |
| B06 | Output slate | vox_compile auto-generates |
| B07 | Summary slate | vox_compile auto-generates |
| B08 | Next-steps slate | vox_compile auto-generates |
| B09 | Remotion: NikBearBrownOutro | Remotion render needed |

All open Remotion slots → `media/<BID>.mp4` via `vox_remotion.py`.
