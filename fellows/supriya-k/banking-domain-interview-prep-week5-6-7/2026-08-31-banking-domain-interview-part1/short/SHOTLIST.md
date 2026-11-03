# SHOTLIST — banking-domain-interview-end-to-end-v2

GATE F requires this file to exist before `run.sh` will render anything. Same minimal pattern as
`banking-domain-sql-running-total-bug/SHOTLIST.md`: every beat resolves through an existing
Remotion pattern or a purpose-written Manim scene. No `pantry/` request, no archive search, no
AI-image prompt anywhere in the 16:9 build.

## Beat routing, 16:9 (12/12 resolved, 0 open)

| Beat | Act | Renders via | Slot |
|------|-----|-------------|------|
| B00 | INTRO | Remotion `ClaudeComposerAsk` | filled |
| B01 | PROBLEM | Manim `B01_TheSecondLanguage` | filled |
| B02 | MECHANISM | Manim `B02_SixPartMap` | filled |
| B03 | CLI | Remotion `ClaudeComposerAsk` | filled |
| B04 | CODE | Remotion `ClaudeCodeBeat` | filled |
| B05 | OUTPUT | Manim `B05_CorrectBalance` | filled |
| B06 | CLI (revision) | Remotion `ClaudeComposerAsk` | filled |
| B07 | CODE (revised) | Remotion `ClaudeCodeBeat` | filled |
| B08 | OUTPUT (revised) | Manim `B08_VintageCurve` | filled |
| B09 | SUMMARY | Manim `B09_TwoMoves` | filled |
| B10 | NEXT STEPS | Remotion `ClaudeComposerAsk` | filled |
| B11 | OUTRO | Remotion `ClaudeTitleOutro` | filled |

## Rhythm check

Manim/Remotion alternate in short runs: B01→B02 Manim, B03→B04 Remotion, B05 Manim, B06→B07
Remotion, B08→B09 Manim, B10→B11 Remotion — no single language carries more than 2 beats in a row.

## 9:16 Short — engineering dependency, not a shot gap

The 9:16 derivation (`./art shorts`) is NOT an open shot slot in the GATE F sense — every beat
still resolves through Remotion or Manim, none through pantry/archive/AI-image. It does depend on
one piece of Remotion infrastructure that does not exist yet: `ClaudeCodeBeat916` (see PLAN.md and
VISUAL-PLAN.md's 9:16 checklist). That component is built at Gate 3, alongside `scenes.py`, before
the 9:16 derivation runs — logged here so GATE F's paperwork check has a record of it, not because
it's a shot to fill later.

## Exclusions confirmed

- No archive/stock footage search — every beat is native motion.
- No AI-generated image or video slot — see `PROMPTS.md`.
- No screen-recording capture — CLI beats are reconstructed Claude-composer renders, per the
  skill's own Remotion-template convention.
