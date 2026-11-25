# TYPECHECK.md — GATE T

Reel: `tldr-attention-scaling-vertical`  |  Checked: 2026-11-23T23:50  |  Overall: PASS  |  Beats checked: 16  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B00] narration recites the card (0.85) — discuss it, don't read it
> - §8.10 [B01] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [BVDT] narration recites the card (0.83) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 101px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B11 | manim | light | min-size §8.1: min text-run height 90px >= floor 72px | PASS | — |
| B12 | manim | light | min-size §8.1: min text-run height 101px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 84px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B14 | manim | light | min-size §8.1: min text-run height 125px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B15 | manim | light | min-size §8.1: min text-run height 85px >= floor 72px | PASS | — |
| B16 | manim | light | min-size §8.1: min text-run height 108px >= floor 72px | PASS | — |
| B17 | manim | light | min-size §8.1: min text-run height 85px >= floor 72px | PASS | — |
| B18 | manim | light | min-size §8.1: min text-run height 113px >= floor 72px | PASS | — |
| BVDT | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact916) — §8.1 hachure/crossbar fragm… | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| BOUT | bookend | dark | min-size §8.1: min text-run height 75px >= floor 72px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 16 | 0 |
| overflow §8.2 | 16 | 0 |
| contrast §8.3 | 16 | 0 |
| contrast-local §8.3b | 16 | 0 |
| bbox-overlap §8.6b | 16 | 0 |
| card-clip §8.13 | 16 | 0 |
| kerning §8.4 | 9 | 0 |
| redundancy §8.10 (advisory) | 3 | 3 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
