# SHOTLIST — five-element-specification

**Build a Five-Element Specification with Claude: Stop Prompting, Start Conducting** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/04-prompts-to-specifications.md
Series: CODEX FOR TEACHERS — Reel 02 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"A request gives Codex a target. A specification gives it constraints…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"The five-element specification is not bureaucracy…"
Slate: problem statement — Codex defaults vs. your decisions.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: full SPECIFICATION with all five elements for src/syllabus.html.
runningText: "running specification version…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `src/syllabus.html`
Shows generated file: semantic HTML5, nav copied, no new CSS, no JS, empty section blocks.

## B04 — SLATE (~20s)
"Specification version: 1 file created, 0 files modified…"
Slate: output comparison — specification vs. vague prompt results.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: Same specification with STOP block added.
runningText: "adding STOP block…"

## B06 — SLATE (~14s)
"With the STOP block, Codex pauses before touching any file outside src/…"
Slate: STOP block as handoff condition in the specification.

## B07 — SLATE (~12s)
"The five elements: specific task, invariants, context, output format, negative constraints…"
Slate: summary — specification vs. average project defaults.

## B08 — SLATE (~8s)
"Next: write handoff conditions that catch what tests miss."
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
