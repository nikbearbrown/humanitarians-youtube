# TYPECHECK.md — GATE T

Reel: `claude-liam-softmax-temperature`  |  Checked: 2026-11-23T04:40  |  Overall: PASS  |  Beats checked: 13  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [BVDT] narration recites the card (0.94) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | remotion | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | remotion | light | min-size §8.1: min text-run height 161px >= floor 41px | PASS | — |
| B02 | manim | light | min-size §8.1: min text-run height 45px >= floor 41px | PASS | — |
| B03 | manim | light | min-size §8.1: min text-run height 54px >= floor 41px | PASS | — |
| B04 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B05 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| B06 | manim | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| B07 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B08 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| B09 | manim | light | min-size §8.1: min text-run height 63px >= floor 41px | PASS | — |
| BVDT | remotion | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | remotion | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | remotion | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 13 | 0 |
| overflow §8.2 | 13 | 0 |
| contrast §8.3 | 13 | 0 |
| contrast-local §8.3b | 13 | 0 |
| bbox-overlap §8.6b | 13 | 0 |
| card-clip §8.13 | 13 | 0 |
| kerning §8.4 | 8 | 0 |
| redundancy §8.10 (advisory) | 1 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
