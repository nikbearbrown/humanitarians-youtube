# TYPECHECK.md — GATE T

Reel: `week-2-progress-vertical`  |  Checked: 2026-11-09T10:41  |  Overall: PASS  |  Beats checked: 9  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B01 | ? | light | min-size §8.1: min text-run height 113px >= floor 72px | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 98px >= floor 72px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 555px >= floor 72px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 882px >= floor 72px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 641px >= floor 72px | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 86px >= floor 72px | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 83px >= floor 72px | PASS | — |
| BOUT | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 9 | 0 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 0 |
| contrast-local §8.3b | 9 | 0 |
| bbox-overlap §8.6b | 9 | 0 |
| card-clip §8.13 | 9 | 0 |
| kerning §8.4 | 7 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
