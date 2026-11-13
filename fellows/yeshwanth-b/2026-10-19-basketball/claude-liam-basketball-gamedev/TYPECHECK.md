# TYPECHECK.md — GATE T

Reel: `claude-liam-basketball-gamedev`  |  Checked: 2026-10-19T10:05  |  Overall: PASS  |  Beats checked: 33  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | ? | light | min-size §8.1: min text-run height 81px >= floor 41px | PASS | — |
| B02 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B04 | ? | — | no video | SKIP | — |
| B05 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B06 | ? | — | no video | SKIP | — |
| B07 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B08 | ? | — | no video | SKIP | — |
| B09 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B10 | ? | — | no video | SKIP | — |
| B11 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B12 | ? | — | no video | SKIP | — |
| B13 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B14 | ? | — | no video | SKIP | — |
| B15 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B16 | ? | — | no video | SKIP | — |
| B17 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B18 | ? | — | no video | SKIP | — |
| B19 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B20 | ? | — | no video | SKIP | — |
| B21 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B22 | ? | — | no video | SKIP | — |
| B23 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B24 | ? | — | no video | SKIP | — |
| B25 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B26 | ? | — | no video | SKIP | — |
| B27 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B28 | ? | — | no video | SKIP | — |
| B29 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B31 | ? | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B32 | ? | light | min-size §8.1: min text-run height 43px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 15 | 0 |
| min-size §8.1 | 20 | 0 |
| overflow §8.2 | 20 | 0 |
| contrast §8.3 | 20 | 0 |
| contrast-local §8.3b | 20 | 0 |
| bbox-overlap §8.6b | 20 | 0 |
| card-clip §8.13 | 20 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
