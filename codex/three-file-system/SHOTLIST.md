# SHOTLIST — three-file-system

**Build the Three-File System with Claude: AGENTS + DESIGN + PROJECT** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/12-three-file-system.md
Series: CODEX FOR TEACHERS — Reel 06 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"The simulation Codex builds without three files is generic…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"The three-file system constrains Codex before Code Mode runs…"
Slate: problem statement — AGENTS.md, DESIGN.md, PROJECT.md defined.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: generate DESIGN.md for bubble-sort simulator. 6 CSS variables, 2 typefaces, 4 allowed, 5 never.
runningText: "generating DESIGN.md…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `DESIGN.md`
Shows 6 color variables with hex/purpose, 2 typefaces, 4 allowed, 5 never interactions.

## B04 — SLATE (~20s)
"DESIGN.md generated: exactly 6 CSS variables, 2 typefaces, 4 allowed / 5 never…"
Slate: output — 74 lines, under 80. Three-file system complete under 45 minutes.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: intentionally violate DESIGN.md constraint then catch and correct it.
runningText: "testing constraint enforcement…"

## B06 — SLATE (~14s)
"Claude generates a 7th color variable, catches it, substitutes closest defined variable…"
Slate: DESIGN.md acted as a constraint, not a suggestion.

## B07 — SLATE (~12s)
"Six colors is not a limitation — it is the decision that makes the simulation coherent…"
Slate: summary — specifying the small set that matters, not everything.

## B08 — SLATE (~8s)
"Next: the task queue pattern — file ideas without breaking focus."
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
