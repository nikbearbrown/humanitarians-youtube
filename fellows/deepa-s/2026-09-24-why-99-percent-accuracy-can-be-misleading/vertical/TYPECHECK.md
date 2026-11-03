# TYPECHECK.md — GATE T

Reel: `AccuracyExplainer_DeepaShenoy`  |  Checked: 2026-09-25T13:09  |  Overall: **FAIL**  |  Beats checked: 9  |  FAILs: 9

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B01 | ? | light | min-size §8.1: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B02 | ? | light | min-size §8.1: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B03 | ? | light | min-size §8.1: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B04 | ? | light | min-size §8.1: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B05 | ? | light | min-size §8.1: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B06 | ? | light | min-size §8.1: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B07 | ? | light | min-size §8.1: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B08 | ? | light | min-size §8.1: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |

---

## Failures requiring action before cut

### B00 (?)
- **min-size §8.1**: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B01 (?)
- **min-size §8.1**: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B02 (?)
- **min-size §8.1**: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B03 (?)
- **min-size §8.1**: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B04 (?)
- **min-size §8.1**: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B05 (?)
- **min-size §8.1**: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B06 (?)
- **min-size §8.1**: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B07 (?)
- **min-size §8.1**: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

### B08 (?)
- **min-size §8.1**: smallest text run 29px < floor 72px (1.9% of 3840px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 9 | 0 |
| min-size §8.1 | 9 | 9 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 0 |
| contrast-local §8.3b | 9 | 0 |
| bbox-overlap §8.6b | 9 | 0 |
| card-clip §8.13 | 9 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
