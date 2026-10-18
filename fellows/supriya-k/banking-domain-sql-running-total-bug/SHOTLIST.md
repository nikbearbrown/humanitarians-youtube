# SHOTLIST — banking-sql-running-total-bug
*The Running-Balance Bug Hiding in a Correct-Looking SQL Query*

---

GATE F requires this file to exist before `run.sh` will render anything. Unlike a shotlist for a
video with archive footage or AI-generated stills, this project has **zero open shot slots**:
every one of the 12 beats resolves either through an existing Remotion pattern
(`ClaudeComposerAsk`, `ClaudeCodeBeat`, `ClaudeTitleOutro` — all already registered components) or
a purpose-written Manim scene in `scenes.py`. There is no `pantry/` request, no archive search, no
AI-image prompt anywhere in this video.

This file exists to satisfy GATE F's paperwork check, not to log shot prompts that don't apply
here — same minimal pattern the structural reference
(`projects/data-analyst-book/hai-sql-window-functions-tie-bug/SHOTLIST.md`) used for the same
reason.

## Beat routing (12/12 resolved, 0 open)

| Beat | Act | Renders via | Slot |
|------|-----|-------------|------|
| B00 | INTRO | Remotion `ClaudeComposerAsk` | filled |
| B01 | PROBLEM | Manim `B01_RunningBalanceStakes` | filled |
| B02 | MECHANISM | Manim `B02_FilterOrderSplit` | filled |
| B03 | CLI | Remotion `ClaudeComposerAsk` | filled |
| B04 | CODE | Remotion `ClaudeCodeBeat` | filled |
| B05 | OUTPUT | Manim `B05_TruncatedBalance` | filled |
| B06 | CLI (revision) | Remotion `ClaudeComposerAsk` | filled |
| B07 | CODE (fixed) | Remotion `ClaudeCodeBeat` | filled |
| B08 | OUTPUT (fixed) | Manim `B08_CorrectedBalance` | filled |
| B09 | SUMMARY | Manim `B09_TheLesson` | filled |
| B10 | NEXT STEPS | Remotion `ClaudeComposerAsk` | filled |
| B11 | OUTRO | Remotion `ClaudeTitleOutro` | filled |

## Rhythm check

Manim/Remotion alternate in short runs (max 2 consecutive of either kind: B01→B02 Manim, then
B03→B04 Remotion, B05 Manim, B06→B07 Remotion, B08→B09 Manim, B10→B11 Remotion) — no single
rendering language carries more than 2 beats in a row, consistent with the MOTION.md pantry cap
spirit even though this video has no pantry footage to cap.

## Exclusions confirmed

- No archive/stock footage search — not needed, every beat is native motion.
- No AI-generated image or video slot — see `PROMPTS.md` (same "not applicable" pattern).
- No screen-recording capture — the CLI beats are reconstructed Claude-composer renders, not a
  literal terminal recording, per the skill's own Remotion-template convention.
