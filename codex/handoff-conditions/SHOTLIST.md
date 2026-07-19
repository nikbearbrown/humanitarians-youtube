# SHOTLIST — handoff-conditions

**Build Handoff Conditions with Claude: Why 'Looks Good' Fails Every Time** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/05-handoff-conditions.md
Series: CODEX FOR TEACHERS — Reel 03 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"Looks good is a feeling. Feelings don't catch broken links…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"A handoff condition must be specific, testable, and binary…"
Slate: problem statement — weak vs. strong conditions.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: 3 strong handoff conditions, weak vs. strong, bash one-liner.
runningText: "generating handoff conditions…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `check_handoff.sh`
Shows bash one-liner checking HTTP 200, git diff, html-validate.

## B04 — SLATE (~20s)
"Three conditions generated: weak vs. strong for each…"
Slate: output — all 3 PASS on correct build.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: introduce broken nav link; run check script.
runningText: "testing broken link detection…"

## B06 — SLATE (~14s)
"With deliberate broken link in nav: check script exits 1…"
Slate: condition 2 FAIL — caught what visual review would miss.

## B07 — SLATE (~12s)
"Handoff conditions catch what you know to specify…"
Slate: summary — bash script as the artifact, three properties rubric.

## B08 — SLATE (~8s)
"Next: build the first phase of a grading tool — survey before you grade."
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
