# TYPECHECK.md — GATE T

Reel: `what-got-in-the-way`  |  Checked: 2026-11-15T01:10  |  Overall: PASS  |  Beats checked: 9  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B20 | ? | light | min-size §8.1: min text-run height 103px >= floor 41px | PASS | — |
| B30 | ? | light | min-size §8.1: min text-run height 45px >= floor 41px | PASS | — |
| B40 | ? | dark | min-size §8.1: min text-run height 67px >= floor 41px | PASS | — |
| B50 | ? | light | min-size §8.1: min text-run height 103px >= floor 41px | PASS | — |
| B60 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |
| B80 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B90 | ? | light | min-size §8.1: min text-run height 198px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 9 | 0 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 0 |
| contrast-local §8.3b | 9 | 0 |
| bbox-overlap §8.6b | 9 | 0 |
| card-clip §8.13 | 9 | 0 |
| kerning §8.4 | 6 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
