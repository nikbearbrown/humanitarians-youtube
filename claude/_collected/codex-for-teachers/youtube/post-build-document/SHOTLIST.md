# SHOTLIST — post-build-document

**Write the Post-Build Document with Claude: Account for Every Decision** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/16-post-build-document.md
Series: CODEX FOR TEACHERS — Reel 08 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"Without the post-build document, the lesson evaporates…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"The post-build document is the Feynman test applied to your own build…"
Slate: problem statement — 5 sections as teaching artifact, Section 5 as load-bearer.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: write 5-section post-build document. Section 5: 4 specific reversible decisions.
runningText: "generating post-build document…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `post-build.md`
Shows five sections including 4 specific reversible decisions in Section 5.

## B04 — SLATE (~20s)
"Generated document: Section 5 has 4 specific reversible decisions…"
Slate: output — each decision actionable by a future teacher.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: evaluate Section 5 — could a future teacher act on each decision without background?
runningText: "evaluating specificity…"

## B06 — SLATE (~14s)
"Decision 2 flagged: column count not specified — revised to 'max 4 columns'…"
Slate: Plausibility Audit caught gap in Claude's own output.

## B07 — SLATE (~12s)
"Section 5 is the load-bearing section. Vague self-criticism is not actionable…"
Slate: summary — specificity is the teaching.

## B08 — SLATE (~8s)
"Next: build a plausibility audit checklist that names which supervisory capacity fired."
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
