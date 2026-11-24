# TYPECHECK.md — GATE T

Reel: `show-tell-how-rag-works`  |  Checked: 2026-11-24T11:10  |  Overall: PASS  |  Beats checked: 18  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | remotion | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | remotion | light | min-size §8.1: min text-run height 122px >= floor 41px | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B11 | manim | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| B12 | manim | light | min-size §8.1: min text-run height 239px >= floor 41px | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 60px >= floor 41px | PASS | — |
| B14 | manim | light | min-size §8.1: min text-run height 112px >= floor 41px | PASS | — |
| B15 | manim | light | min-size §8.1: min text-run height 112px >= floor 41px | PASS | — |
| B16 | manim | light | min-size §8.1: min text-run height 60px >= floor 41px | PASS | — |
| B17 | manim | light | min-size §8.1: min text-run height 64px >= floor 41px | PASS | — |
| B18 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B19 | card | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B21 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B22 | manim | light | min-size §8.1: min text-run height 120px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BVDT | remotion | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |

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
| kerning §8.4 | 12 | 0 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
