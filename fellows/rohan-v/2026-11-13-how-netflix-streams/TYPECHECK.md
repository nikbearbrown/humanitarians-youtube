# TYPECHECK.md — GATE T

Reel: `netflix-streaming-explainer`  |  Checked: 2026-11-10T03:33  |  Overall: PASS  |  Beats checked: 9  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | dark | min-size §8.1: diegetic-palette pattern (HyperFrames:ladder) — geometric ink markers are n… | PASS | — |
| B02 | ? | dark | min-size §8.1: diegetic-palette pattern (HyperFrames:vmaf) — geometric ink markers are not… | PASS | — |
| B03 | ? | dark | min-size §8.1: diegetic-palette pattern (HyperFrames:pertitle) — geometric ink markers are… | PASS | — |
| B04 | ? | dark | min-size §8.1: diegetic-palette pattern (HyperFrames:player) — geometric ink markers are n… | PASS | — |
| B05 | ? | dark | min-size §8.1: diegetic-palette pattern (HyperFrames:cdn) — geometric ink markers are nota… | PASS | — |
| B06 | ? | dark | min-size §8.1: diegetic-palette pattern (HyperFrames:scale) — geometric ink markers are no… | PASS | — |
| B07 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 9 | 0 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 0 |
| contrast-local §8.3b | 9 | 0 |
| bbox-overlap §8.6b | 9 | 0 |
| card-clip §8.13 | 9 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
