# SHOTLIST — generate-evaluate-select

**Generate-Evaluate-Select with Claude: Three Responses, One Real Decision** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/07-best-of-n.md
Series: CODEX FOR TEACHERS — Reel 05 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"One Claude response is a default. Three responses are a choice…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"Generate-evaluate-select is not a workaround…"
Slate: problem statement — default vs. deliberate choice, Interpretive Judgment.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: feedback paragraph, 80 words, second person, 2 rubric criteria. Run 3 times.
runningText: "generating 3 candidates…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `compare_responses.py`
Shows comparison script: word count, criteria, framing, equity flags.

## B04 — SLATE (~20s)
"Three candidates: Response A deficit-first, B strength-first, C equity flag…"
Slate: output — Response B selected, reasoning logged.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: generate 4th response explicitly leading with a strength.
runningText: "forcing strength-first framing…"

## B06 — SLATE (~14s)
"Response D strength-first but one fewer rubric criterion…"
Slate: forced framing did not improve output; selection still Response B.

## B07 — SLATE (~12s)
"Generate-evaluate-select is a dangerous-middle detector…"
Slate: summary — when all three share a pattern, fix the specification.

## B08 — SLATE (~8s)
"Next: build the three-file system — AGENTS.md, DESIGN.md, and PROJECT.md together."
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
