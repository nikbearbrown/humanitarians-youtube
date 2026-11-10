# TYPECHECK.md — GATE T

Reel: `claude-liam-knife-throw-gamedev-vertical`  |  Checked: 2026-11-10T15:37  |  Overall: PASS  |  Beats checked: 31  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B04 | ? | — | no video | SKIP | — |
| B05 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B06 | ? | — | no video | SKIP | — |
| B07 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B08 | ? | — | no video | SKIP | — |
| B09 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B10 | ? | — | no video | SKIP | — |
| B11 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B12 | ? | — | no video | SKIP | — |
| B13 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B14 | ? | — | no video | SKIP | — |
| B15 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B16 | ? | — | no video | SKIP | — |
| B17 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B18 | ? | — | no video | SKIP | — |
| B19 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B20 | ? | — | no video | SKIP | — |
| B21 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B22 | ? | — | no video | SKIP | — |
| B23 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B24 | ? | — | no video | SKIP | — |
| B25 | ? | light | min-size §8.1: min text-run height 1085px >= floor 72px | PASS | — |
| B26 | ? | — | no video | SKIP | — |
| B27 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B28 | ? | light | min-size §8.1: min text-run height 424px >= floor 72px | PASS | — |
| B29 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B30 | ? | dark | min-size §8.1: min text-run height 74px >= floor 72px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 19 | 0 |
| overflow §8.2 | 19 | 0 |
| contrast §8.3 | 19 | 0 |
| contrast-local §8.3b | 19 | 0 |
| bbox-overlap §8.6b | 19 | 0 |
| card-clip §8.13 | 19 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
