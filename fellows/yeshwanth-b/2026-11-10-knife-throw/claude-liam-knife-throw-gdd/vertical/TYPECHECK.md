# TYPECHECK.md — GATE T

Reel: `claude-liam-knife-throw-gdd-vertical`  |  Checked: 2026-11-10T15:14  |  Overall: PASS  |  Beats checked: 27  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 424px >= floor 72px | PASS | — |
| B04 | ? | — | no video | SKIP | — |
| B05 | ? | light | min-size §8.1: min text-run height 424px >= floor 72px | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 424px >= floor 72px | PASS | — |
| B07 | ? | — | no video | SKIP | — |
| B08 | ? | light | min-size §8.1: min text-run height 424px >= floor 72px | PASS | — |
| B09 | ? | — | no video | SKIP | — |
| B10 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B11 | ? | — | no video | SKIP | — |
| B12 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B13 | ? | — | no video | SKIP | — |
| B14 | ? | light | min-size §8.1: min text-run height 247px >= floor 72px | PASS | — |
| B15 | ? | — | no video | SKIP | — |
| B16 | ? | — | no video | SKIP | — |
| B17 | ? | light | min-size §8.1: min text-run height 424px >= floor 72px | PASS | — |
| B18 | ? | — | no video | SKIP | — |
| B19 | ? | light | min-size §8.1: min text-run height 424px >= floor 72px | PASS | — |
| B20 | ? | — | no video | SKIP | — |
| B21 | ? | light | min-size §8.1: min text-run height 247px >= floor 72px | PASS | — |
| B22 | ? | light | min-size §8.1: min text-run height 247px >= floor 72px | PASS | — |
| B23 | ? | light | min-size §8.1: min text-run height 424px >= floor 72px | PASS | — |
| B24 | ? | light | min-size §8.1: min text-run height 247px >= floor 72px | PASS | — |
| B25 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B26 | ? | dark | min-size §8.1: min text-run height 74px >= floor 72px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 18 | 0 |
| overflow §8.2 | 18 | 0 |
| contrast §8.3 | 18 | 0 |
| contrast-local §8.3b | 18 | 0 |
| bbox-overlap §8.6b | 18 | 0 |
| card-clip §8.13 | 18 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
