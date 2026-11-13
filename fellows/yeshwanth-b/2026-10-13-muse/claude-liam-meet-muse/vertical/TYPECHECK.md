# TYPECHECK.md — GATE T

Reel: `claude-liam-meet-muse-vertical`  |  Checked: 2026-10-13T12:51  |  Overall: PASS  |  Beats checked: 16  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 222px >= floor 72px | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 222px >= floor 72px | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 222px >= floor 72px | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B11 | ? | light | min-size §8.1: min text-run height 77px >= floor 72px | PASS | — |
| B12 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B14 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B15 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B16 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 16 | 0 |
| overflow §8.2 | 16 | 0 |
| contrast §8.3 | 16 | 0 |
| contrast-local §8.3b | 16 | 0 |
| bbox-overlap §8.6b | 16 | 0 |
| card-clip §8.13 | 16 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
