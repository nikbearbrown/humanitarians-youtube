# TYPECHECK.md — GATE T

Reel: `claude-liam-cross-entropy-vertical`  |  Checked: 2026-11-24T02:40  |  Overall: PASS  |  Beats checked: 11  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | min-size §8.1: min text-run height 111px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B03 | ? | light | min-size §8.1: min text-run height 92px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 114px >= floor 72px | PASS | — |
| B05 | ? | light | min-size §8.1: min text-run height 111px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B06 | ? | light | min-size §8.1: min text-run height 76px >= floor 72px (individual-char fallback at 4×) | PASS | — |
| B07 | ? | light | min-size §8.1: min text-run height 133px >= floor 72px | PASS | — |
| BVDT | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact916) — §8.1 hachure/crossbar fragm… | PASS | — |
| BHTF | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk916) — §8.1 hachure/crossbar fragments… | PASS | — |
| BOUT | ? | dark | min-size §8.1: min text-run height 75px >= floor 72px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 1 | 0 |
| min-size §8.1 | 11 | 0 |
| overflow §8.2 | 11 | 0 |
| contrast §8.3 | 11 | 0 |
| contrast-local §8.3b | 11 | 0 |
| bbox-overlap §8.6b | 11 | 0 |
| card-clip §8.13 | 11 | 0 |
| kerning §8.4 | 6 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
