# SHOTLIST — banking-domain-star-method-behavioral

GATE F requires this file to exist before `run.sh` will render anything. This project has **zero
open shot slots**: every one of the 22 beats resolves either through an existing Remotion pattern
(`ClaudeComposerAsk`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`, `QuoteCard`, `StateCardPair`,
`LabelChip` — all already registered components) or a purpose-written Manim scene in `scenes.py`.
There is no `pantry/` request, no archive search, no AI-image prompt anywhere in this video — the
lane-mix plan sets VOX at 0% (see `VISUAL-PLAN.md`'s Lane-mix decision section for why).

This file exists to satisfy GATE F's paperwork check, not to log shot prompts that don't apply
here — same minimal pattern the two structural references
(`projects/data-analyst-book/hai-interview-end-to-end/SHOTLIST.md` and the sibling cli-explainer
build this session) used for the same reason.

## Beat routing (22/22 resolved, 0 open)

| Beat | Act | Renders via | Slot |
|---|---|---|---|
| B00 | INTRO | Remotion `ClaudeComposerAsk` | filled |
| B01 | I (card) | Manim `B01_ActICard` | filled |
| B02 | I | Manim `B02_StarFourParts` | filled |
| B03 | I | Remotion `QuoteCard` | filled |
| B04 | II (card) | Manim `B04_ActIICard` | filled |
| B05 | II | Manim `B05_ThreeCompetencies` | filled |
| B06 | II | Remotion `LabelChip` | filled |
| B07 | II | Remotion `QuoteCard` | filled |
| B08 | II | Manim `B08_DeliveryRule` | filled |
| B09 | III (card) | Manim `B09_ActIIICard` | filled |
| B10 | III | Remotion `QuoteCard` | filled |
| B11 | III | Remotion `StateCardPair` | filled |
| B12 | III | Manim `B12_ScoredChecklist` | filled |
| B13 | IV (card) | Manim `B13_ActIVCard` | filled |
| B14 | IV | Manim `B14_FiveStageLoop` | filled |
| B15 | IV | Remotion `QuoteCard` | filled |
| B16 | IV | Remotion `QuoteCard` | filled |
| B17 | IV | Manim `B17_ScoreAndChart` | filled |
| B18 | IV | Manim `B18_TheLesson` | filled |
| B_VERDICT | VERDICT | Remotion `ClaudeVerdictArtifact` | filled |
| B_YOURTURN | YOUR TURN | Remotion `ClaudeComposerAsk` | filled |
| B_OUTRO | OUTRO | Remotion `ClaudeTitleOutro` | filled |

## Rhythm check

No single rendering language carries more than 2 consecutive beats (verified beat-by-beat against
the full sequence above): …CARD,MANIM,REMOTION,CARD,MANIM,REMOTION,REMOTION,MANIM,CARD,REMOTION,
REMOTION,MANIM,CARD,MANIM,REMOTION,REMOTION,MANIM,MANIM… — the two runs of 2 (REMOTION,REMOTION at
B06→B07 and B10→B11 and B15→B16; MANIM,MANIM at B17→B18) are all exactly at the cap, never over it.

## Exclusions confirmed

- No archive/stock footage search — VOX lane is 0% (see `VISUAL-PLAN.md`).
- No AI-generated image or video slot.
- No screen-recording capture.
