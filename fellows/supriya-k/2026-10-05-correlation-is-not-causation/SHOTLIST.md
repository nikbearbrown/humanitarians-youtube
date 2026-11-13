# SHOTLIST — correlation-is-not-causation

GATE F requires this file before `run.sh` renders. Every beat resolves through an existing Remotion
pattern or a purpose-written Manim scene. There are no `pantry/`, archive, or AI-image slots.

## Beat routing (12/12 planned, 0 open)

| Beat | Act | 16:9 | 9:16 |
|------|-----|------|------|
| B00 | INTRO | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B01 | PROBLEM | Manim `B01_PickOne` | portrait class, `short/scenes.py` |
| B02 | CLI | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B03 | CODE | `ClaudeCodeBeat` (`sql/q1_by_treatment.sql`) | `ClaudeCodeBeat916` |
| B04 | OUTPUT | Manim `B04_KeyholeWins` | portrait class |
| B05 | CLI (revision) | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B06 | CODE (revised) | `ClaudeCodeBeat` (`sql/q2_by_size.sql`) | `ClaudeCodeBeat916` |
| B07 | OUTPUT (revised) | Manim `B07_TheFlip` | portrait class |
| B08 | MECHANISM | Manim `B08_WhoGotWhat` | portrait class |
| B09 | SUMMARY | Manim `B09_ThreeQuestions` | portrait class |
| B10 | NEXT STEPS | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B11 | OUTRO | `ClaudeTitleOutroFilled` (scale 1.8) | `ClaudeTitleOutroFilled916` (scale 1.2) |

All 9:16 Remotion ids are already registered in `Root.tsx`, so `shorts.py`'s ONDA CHECK can rewire
every beat.

## Rhythm

B00 Remotion · B01 Manim · B02–B03 Remotion · B04 Manim · B05–B06 Remotion · B07–B09 Manim ·
B10–B11 Remotion. B07–B09 is three Manim beats in a row. It's deliberate: flip → why → lesson is
one continuous argument over the same data.

## Data receipt

Manim beats parse every number from `sql/*.out` at render time. Code beats show `sql/*.sql`
verbatim.
