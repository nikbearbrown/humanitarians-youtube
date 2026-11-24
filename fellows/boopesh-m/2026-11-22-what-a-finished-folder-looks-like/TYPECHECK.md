# TYPECHECK.md — GATE T

Reel: `finished-folder-master`  |  Checked: 2026-11-23T19:32  |  Overall: PASS  |  Beats checked: 10  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 86px >= floor 41px | PASS | — |
| B20 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B30 | manim | light | min-size §8.1: min text-run height 86px >= floor 41px | PASS | — |
| B40 | manim | light | min-size §8.1: min text-run height 52px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B50 | manim | light | min-size §8.1: min text-run height 86px >= floor 41px | PASS | — |
| B60 | manim | light | min-size §8.1: min text-run height 42px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B70 | manim | dark | min-size §8.1: min text-run height 150px >= floor 41px | PASS | — |
| B80 | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B90 | manim | light | min-size §8.1: min text-run height 55px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 10 | 0 |
| overflow §8.2 | 10 | 0 |
| contrast §8.3 | 10 | 0 |
| contrast-local §8.3b | 10 | 0 |
| bbox-overlap §8.6b | 10 | 0 |
| card-clip §8.13 | 10 | 0 |
| kerning §8.4 | 8 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
