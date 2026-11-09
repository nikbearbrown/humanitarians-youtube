# TYPECHECK.md — GATE T

Reel: `how-your-phone-types-japanese`  |  Checked: 2026-11-06T07:37  |  Overall: PASS  |  Beats checked: 14  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [BVDT] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B01 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 47px >= floor 41px | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 66px >= floor 41px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 78px >= floor 41px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 78px >= floor 41px | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 606px >= floor 41px | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 68px >= floor 41px | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 42px >= floor 41px | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 48px >= floor 41px | PASS | — |
| B11 | ? | light | min-size §8.1: min text-run height 69px >= floor 41px | PASS | — |
| BVDT | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 14 | 0 |
| overflow §8.2 | 14 | 0 |
| contrast §8.3 | 14 | 0 |
| contrast-local §8.3b | 14 | 0 |
| bbox-overlap §8.6b | 14 | 0 |
| card-clip §8.13 | 14 | 0 |
| kerning §8.4 | 9 | 0 |
| redundancy §8.10 (advisory) | 1 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
