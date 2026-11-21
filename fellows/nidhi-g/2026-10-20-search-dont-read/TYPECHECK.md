# TYPECHECK.md — GATE T

Reel: `search-dont-read`  |  Checked: 2026-10-20T17:24  |  Overall: PASS  |  Beats checked: 11  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | min-size §8.1: min text-run height 154px >= floor 41px | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 90px >= floor 41px | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 70px >= floor 41px | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B09 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 89px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 11 | 0 |
| overflow §8.2 | 11 | 0 |
| contrast §8.3 | 11 | 0 |
| contrast-local §8.3b | 11 | 0 |
| bbox-overlap §8.6b | 11 | 0 |
| card-clip §8.13 | 11 | 0 |
| kerning §8.4 | 8 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
