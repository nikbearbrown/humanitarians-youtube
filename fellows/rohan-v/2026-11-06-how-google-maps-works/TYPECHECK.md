# TYPECHECK.md — GATE T

Reel: `google-maps-explainer`  |  Checked: 2026-11-09T18:37  |  Overall: PASS  |  Beats checked: 10  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | dark | min-size §8.1: min text-run height 81px >= floor 41px | PASS | — |
| B02 | ? | dark | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B03 | ? | dark | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B04 | ? | dark | min-size §8.1: diegetic-palette pattern (HyperFrames:traffic) — geometric ink markers are … | PASS | — |
| B05 | ? | dark | min-size §8.1: min text-run height 42px >= floor 41px | PASS | — |
| B06 | ? | dark | min-size §8.1: diegetic-palette pattern (HyperFrames:busy) — geometric ink markers are not… | PASS | — |
| B07 | ? | dark | min-size §8.1: min text-run height 58px >= floor 41px | PASS | — |
| B08 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 10 | 0 |
| overflow §8.2 | 10 | 0 |
| contrast §8.3 | 10 | 0 |
| contrast-local §8.3b | 10 | 0 |
| bbox-overlap §8.6b | 10 | 0 |
| card-clip §8.13 | 10 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
