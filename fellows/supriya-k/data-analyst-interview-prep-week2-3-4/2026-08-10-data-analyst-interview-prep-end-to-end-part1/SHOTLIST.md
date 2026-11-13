# SHOTLIST — hai-interview-end-to-end (v2, 2026-10-15)

GATE F requires this file before `run.sh` renders. Every beat resolves through an existing Remotion
pattern or a purpose-written Manim scene. There are no `pantry/`, archive, or AI-image slots; the
0%-VOX lane decision (accepted at GATE P, 2026-07-24, carried into v2) still holds.

## Beat routing (24/24 planned, 0 open)

| Beat | Act | 16:9 | 9:16 (`short/`) |
|------|-----|------|------|
| B00 | OPEN | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B01 | I — The Six Stages | `StateCardPair` | `StateCardPair916` |
| B02 | I — The Six Stages | Manim `B02_SixStageChips` (`scenes.py`) | portrait class, `short/scenes.py` |
| B03 | I — The Six Stages | `StateCardPair` | `StateCardPair916` |
| B04 | I — The Six Stages | `QuoteCard` | `QuoteCard916` |
| B05 | II — What's Tested Where | `StateCardPair` | `StateCardPair916` |
| B06 | II — What's Tested Where | Manim `B06_MatrixRows12` (`scenes.py`) | portrait class, `short/scenes.py` |
| B07 | II — What's Tested Where | Manim `B07_MatrixRows34` (`scenes.py`) | portrait class, `short/scenes.py` |
| B08 | II — What's Tested Where | Manim `B08_MatrixRows56` (`scenes.py`) | portrait class, `short/scenes.py` |
| B09 | II — What's Tested Where | `QuoteCard` | `QuoteCard916` |
| B11 | III — What Changed by 2026 | `StateCardPair` | `StateCardPair916` |
| B12 | III — What Changed by 2026 | `StateCardPair` | `StateCardPair916` |
| B13 | III — What Changed by 2026 | Manim `B13_LineByLineCheck` (`scenes.py`) | portrait class, `short/scenes.py` |
| B14 | III — What Changed by 2026 | `StateCardPair` | `StateCardPair916` |
| B15 | III — What Changed by 2026 | `StateCardPair` | `StateCardPair916` |
| B17 | IV — The Worked Plan | `StateCardPair` | `StateCardPair916` |
| B18 | IV — The Worked Plan | Manim `B18_MayaProfile` (`scenes.py`) | portrait class, `short/scenes.py` |
| B20 | IV — The Worked Plan | Manim `B20_Week1Block` (`scenes.py`) | portrait class, `short/scenes.py` |
| B21 | IV — The Worked Plan | Manim `B21_Week2Block` (`scenes.py`) | portrait class, `short/scenes.py` |
| B22 | IV — The Worked Plan | Manim `B22_Week3Block` (`scenes.py`) | portrait class, `short/scenes.py` |
| B23 | IV — The Worked Plan | Manim `B23_LopsidedHours` (`scenes.py`) | portrait class, `short/scenes.py` |
| B_VERDICT | CLOSE | `ClaudeVerdictArtifact` | `ClaudeVerdictArtifact916` |
| B_YOURTURN | CLOSE | `ClaudeComposerAsk` | `ClaudeComposerAsk916` |
| B_OUTRO | CLOSE | `ClaudeTitleOutroFilled` | `ClaudeTitleOutroFilled916` |

The 9:16 cut also appends the silent 4.5s endcard (`shorts.py --handle Supriya`).
v2 changes vs v1: B10/B16/B19 dropped; B23 moved from Remotion `StateCardPair` to Manim
`B23_LopsidedHours`; B12/B14 moved from `LabelChip` to `StateCardPair`.
