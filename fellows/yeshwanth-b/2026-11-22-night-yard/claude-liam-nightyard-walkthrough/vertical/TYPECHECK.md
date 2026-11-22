# TYPECHECK.md — GATE T

Reel: `claude-liam-nightyard-walkthrough-vertical`  |  Checked: 2026-11-20T21:34  |  Overall: PASS  |  Beats checked: 48  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | — | no video | SKIP | — |
| B03 | ? | — | no video | SKIP | — |
| B04 | ? | — | no video | SKIP | — |
| B05 | ? | — | no video | SKIP | — |
| B06 | ? | — | no video | SKIP | — |
| B07 | ? | — | no video | SKIP | — |
| B08 | ? | — | no video | SKIP | — |
| B09 | ? | — | no video | SKIP | — |
| B10 | ? | — | no video | SKIP | — |
| B11 | ? | — | no video | SKIP | — |
| B12 | ? | — | no video | SKIP | — |
| B13 | ? | — | no video | SKIP | — |
| B14 | ? | — | no video | SKIP | — |
| B15 | ? | — | no video | SKIP | — |
| B16 | ? | — | no video | SKIP | — |
| B17 | ? | — | no video | SKIP | — |
| B18 | ? | — | no video | SKIP | — |
| B19 | ? | — | no video | SKIP | — |
| B20 | ? | — | no video | SKIP | — |
| B21 | ? | — | no video | SKIP | — |
| B22 | ? | — | no video | SKIP | — |
| B23 | ? | — | no video | SKIP | — |
| B24 | ? | — | no video | SKIP | — |
| B25 | ? | — | no video | SKIP | — |
| B26 | ? | — | no video | SKIP | — |
| B27 | ? | — | no video | SKIP | — |
| B28 | ? | — | no video | SKIP | — |
| B29 | ? | — | no video | SKIP | — |
| B30 | ? | — | no video | SKIP | — |
| B31 | ? | — | no video | SKIP | — |
| B32 | ? | — | no video | SKIP | — |
| B33 | ? | — | no video | SKIP | — |
| B34 | ? | — | no video | SKIP | — |
| B35 | ? | — | no video | SKIP | — |
| B36 | ? | — | no video | SKIP | — |
| B37 | ? | — | no video | SKIP | — |
| B38 | ? | — | no video | SKIP | — |
| B39 | ? | — | no video | SKIP | — |
| B40 | ? | — | no video | SKIP | — |
| B41 | ? | — | no video | SKIP | — |
| B42 | ? | — | no video | SKIP | — |
| B43 | ? | — | no video | SKIP | — |
| B44 | ? | — | no video | SKIP | — |
| B45 | ? | light | min-size §8.1: min text-run height 247px >= floor 72px | PASS | — |
| B46 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B47 | ? | light | min-size §8.1: min text-run height 73px >= floor 72px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 5 | 0 |
| overflow §8.2 | 5 | 0 |
| contrast §8.3 | 5 | 0 |
| contrast-local §8.3b | 5 | 0 |
| bbox-overlap §8.6b | 5 | 0 |
| card-clip §8.13 | 5 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
