# SHOTLIST — ab-testing-can-lie-to-you

GATE F requires this file before `run.sh` renders. Every beat resolves through an existing Remotion
pattern or a purpose-written Manim scene. There are no `pantry/`, archive, or AI-image slots.

## Beat routing (12/12 planned, 0 open)

| Beat | Act | 16:9 | 9:16 |
|------|-----|------|------|
| B00 | INTRO | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B01 | PROBLEM | Manim `B01_DontShip` | portrait class, `short/scenes.py` |
| B02 | CLI | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B03 | CODE | `ClaudeCodeBeat` (`py/carousel_v1.py` excerpt) | `ClaudeCodeBeat916` |
| B04 | OUTPUT | Manim `B04_LooksWorse` | portrait class |
| B05 | CLI (revision) | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B06 | CODE (revised) | `ClaudeCodeBeat` (`py/carousel_v2.py` excerpt) | `ClaudeCodeBeat916` |
| B07 | OUTPUT (revised) | Manim `B07_TheFlip` | portrait class |
| B08 | SECOND LIE (peeking) | Manim `B08_Peeking` | portrait class |
| B09 | SUMMARY | Manim `B09_ThreeChecks` | portrait class |
| B10 | NEXT STEPS | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B11 | OUTRO | `ClaudeTitleOutroFilled` (scale 1.8) | `ClaudeTitleOutroFilled916` (scale 1.3) |

## Rhythm

B00 Remotion · B01 Manim · B02–B03 Remotion · B04 Manim · B05–B06 Remotion · B07–B09 Manim ·
B10–B11 Remotion. B07–B09 is three Manim beats in a row: flip → second lie → lesson.

## Data receipt

Manim beats parse every simulated number from `py/*.out` at render time and tag it "SIMULATION".
Code beats show `py/*.py` excerpts verbatim (line ranges in each beat's `role_note`).
