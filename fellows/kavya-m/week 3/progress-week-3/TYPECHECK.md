# TYPECHECK.md — GATE T

Reel: `kavya-brutalist-week3-progress`  |  Checked: 2026-10-28T19:29  |  Overall: **FAIL**  |  Beats checked: 8  |  FAILs: 1

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B05] narration recites the card (0.86) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| B02 | ? | light | min-size §8.1: smallest text run 8px < floor 27px (1.9% of 1440px logical); likely a capti… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B03 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B06 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B07 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |

---

## Failures requiring action before cut

### B02 (?)
- **min-size §8.1**: smallest text run 8px < floor 27px (1.9% of 1440px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 8 | 1 |
| overflow §8.2 | 8 | 0 |
| contrast §8.3 | 8 | 0 |
| contrast-local §8.3b | 8 | 0 |
| bbox-overlap §8.6b | 8 | 0 |
| card-clip §8.13 | 8 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 1 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
