# TYPECHECK.md — GATE T

Reel: `backtest-mirage-short`  |  Checked: 2026-11-08T02:16  |  Overall: PASS  |  Beats checked: 5  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 78px >= floor 72px | PASS | — |
| B20 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px | PASS | — |
| B30 | ? | light | min-size §8.1: min text-run height 80px >= floor 72px | PASS | — |
| B90 | ? | light | min-size §8.1: min text-run height 239px >= floor 72px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 5 | 0 |
| overflow §8.2 | 5 | 0 |
| contrast §8.3 | 5 | 0 |
| contrast-local §8.3b | 5 | 0 |
| bbox-overlap §8.6b | 5 | 0 |
| card-clip §8.13 | 5 | 0 |
| kerning §8.4 | 4 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
