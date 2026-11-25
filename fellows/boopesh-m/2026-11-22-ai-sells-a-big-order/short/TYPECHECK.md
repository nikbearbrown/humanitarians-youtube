# TYPECHECK.md — GATE T

Reel: `ai-sells-a-big-order-short`  |  Checked: 2026-11-23T20:03  |  Overall: PASS  |  Beats checked: 6  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B20 | ? | light | min-size §8.1: min text-run height 81px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B30 | ? | light | min-size §8.1: min text-run height 81px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B40 | ? | light | min-size §8.1: min text-run height 74px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B50 | ? | dark | min-size §8.1: min text-run height 74px >= floor 72px | PASS | — |
| B90 | ? | light | min-size §8.1: min text-run height 82px >= floor 72px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 6 | 0 |
| overflow §8.2 | 6 | 0 |
| contrast §8.3 | 6 | 0 |
| contrast-local §8.3b | 6 | 0 |
| bbox-overlap §8.6b | 6 | 0 |
| card-clip §8.13 | 6 | 0 |
| kerning §8.4 | 5 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
