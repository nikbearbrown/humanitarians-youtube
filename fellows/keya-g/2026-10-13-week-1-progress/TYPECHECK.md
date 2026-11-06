# TYPECHECK.md — GATE T

Reel: `week-1-progress`  |  Checked: 2026-11-03T19:44  |  Overall: PASS  |  Beats checked: 8  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | min-size §8.1: min text-run height 52px >= floor 41px | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 89px >= floor 41px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 82px >= floor 41px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 92px >= floor 41px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 45px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 75px >= floor 41px | PASS | — |
| BOUT | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 8 | 0 |
| overflow §8.2 | 8 | 0 |
| contrast §8.3 | 8 | 0 |
| contrast-local §8.3b | 8 | 0 |
| bbox-overlap §8.6b | 8 | 0 |
| card-clip §8.13 | 8 | 0 |
| kerning §8.4 | 6 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
