# SHOTLIST — dangerous-middle-research

**Research the Dangerous Middle: What the Bias Literature Actually Says** · 16:9 · ~118s est. (10 beats)
Source: codex-for-teachers/chapters/09-dangerous-middle.md
Series: CODEX FOR TEACHERS — Reel 10 of 10

All beats are SLATE or Remotion motion graphics. No Manim scenes. No AI image generation.

---

## B00 — SLATE (~8s)
"LLM grading accuracy jumped from 55% to 93% between 2022 and 2025…"
Slate: intro hook text on teardown ground.

## B01 — SLATE (~12s)
"The improvement makes the problem worse, not better…"
Slate: problem statement — narrowing principle, concentration in ESL/AAVE populations.

## B02 — REMOTION: NikBearBrownTerminalAsk (~12s)
Command: synthesize 2024-2026 bias literature — ESL, AAVE, arXiv:2601.16724, Anthropic Ed. Report 2025.
runningText: "synthesizing bias literature…"

## B03 — REMOTION: NikBearBrownCodeBlock (~14s)
filename: `bias_brief.md`
Shows 3-row summary table: Study / Key Finding / Implication. UNVERIFIED markers present.

## B04 — SLATE (~20s)
"Brief generated: 694 words, sourced. Claude flags 2 unverified statistics…"
Slate: output — UNVERIFIED markers confirmed in chapter sources, mitigation correctly stated as 40% not elimination.

## B05 — REMOTION: NikBearBrownTerminalAsk (~10s)
Command: produce one-page plain-language version for parents and administrators.
runningText: "generating plain-language version…"

## B06 — SLATE (~14s)
"Plain-language version: 380 words, no jargon. What gets lost in translation…"
Slate: comparison shows what teacher must add back for technical vs. policy audience.

## B07 — SLATE (~12s)
"The narrowing principle is what makes the dangerous middle genuinely dangerous…"
Slate: summary — 10% disagreement is systematic, not random; human must audit that 10%.

## B08 — SLATE (~8s)
"That's the full Codex for Teachers series — ten tools for conducting AI responsibly in the classroom."
Slate: series close card.

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
