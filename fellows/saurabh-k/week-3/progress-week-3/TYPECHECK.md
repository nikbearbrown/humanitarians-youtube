# TYPECHECK.md — GATE T

Reel: `hai-repo-sensei-v2`  |  Checked: 2026-10-26T18:50  |  Overall: PASS  |  Beats checked: 20  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | min-size §8.1: min text-run height 135px >= floor 41px | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 91px >= floor 41px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 72px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 170px >= floor 41px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 42px >= floor 41px | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 412px >= floor 41px | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 62px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 414px >= floor 41px | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 385px >= floor 41px | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| B11 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | ? | light | min-size §8.1: min text-run height 133px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B13 | ? | light | min-size §8.1: min text-run height 73px >= floor 41px | PASS | — |
| B14 | ? | light | min-size §8.1: min text-run height 72px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B15 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | ? | light | min-size §8.1: min text-run height 46px >= floor 41px | PASS | — |
| B17 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | ? | light | min-size §8.1: min text-run height 170px >= floor 41px | PASS | — |
| B19 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 20 | 0 |
| overflow §8.2 | 20 | 0 |
| contrast §8.3 | 20 | 0 |
| contrast-local §8.3b | 20 | 0 |
| bbox-overlap §8.6b | 20 | 0 |
| card-clip §8.13 | 20 | 0 |
| kerning §8.4 | 13 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
