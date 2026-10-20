# SHOTLIST — claude-code-explained

GATE F requires this file before `run.sh` renders. Every beat resolves through an existing Remotion
pattern or a purpose-written Manim scene — no `pantry/`, archive, or AI-image slot.

## Beat routing (12/12 planned, 0 open)

| Beat | Act | 16:9 | 9:16 |
|------|-----|------|------|
| B00 | INTRO | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B01 | PROBLEM | Manim `B01_CannotWatch` | portrait class, `short/scenes.py` |
| B02 | MECHANISM | Manim `B02_TheLoop` | portrait class |
| B03 | CLI | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B04 | CODE | `ClaudeCodeBeat` | `ClaudeCodeBeat916` |
| B05 | OUTPUT | Manim `B05_FillBefore_After` | portrait class |
| B06 | CLI (revision) | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B07 | CODE (revised) | `ClaudeCodeBeat` | `ClaudeCodeBeat916` |
| B08 | OUTPUT (revised) | Manim `B08_WholeFrame` | portrait class |
| B09 | SUMMARY | Manim `B09_FourMoves` | portrait class |
| B10 | NEXT STEPS | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B11 | OUTRO | `ClaudeTitleOutroFilled` | `ClaudeTitleOutroFilled916` |

All 9:16 Remotion ids are already registered in `Root.tsx`, so `shorts.py`'s ONDA CHECK can rewire
every beat.

## Rhythm

B01–B02 Manim · B03–B04 Remotion · B05 Manim · B06–B07 Remotion · B08–B09 Manim · B10–B11 Remotion.
No more than two beats in a row in one engine.

## Engineering dependencies (Gate 3, not shot gaps)

`ClaudeCodeBeat`/`ClaudeCodeBeat916` optional `handle` + `lang` props; `compile.py --vbitrate`.
