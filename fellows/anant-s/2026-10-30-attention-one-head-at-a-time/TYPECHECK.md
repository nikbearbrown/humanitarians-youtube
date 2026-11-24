# TYPECHECK.md — GATE T

Reel: `tldr-attention`  |  Checked: 2026-11-24T10:21  |  Overall: PASS  |  Beats checked: 15  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [BVDT] narration recites the card (0.84) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | remotion | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | remotion | light | min-size §8.1: min text-run height 122px >= floor 41px | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B11 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B12 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B14 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B15 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B16 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| B17 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B18 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B19 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| BVDT | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | dark | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 15 | 0 |
| overflow §8.2 | 15 | 0 |
| contrast §8.3 | 15 | 0 |
| contrast-local §8.3b | 15 | 0 |
| bbox-overlap §8.6b | 15 | 0 |
| card-clip §8.13 | 15 | 0 |
| kerning §8.4 | 10 | 0 |
| redundancy §8.10 (advisory) | 1 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
