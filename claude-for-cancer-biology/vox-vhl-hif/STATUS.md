# STATUS — vox-vhl-hif
## Why a Broken Oxygen Sensor Causes a Cancer to Act Permanently Starved

**Built:** 2026-07-08
**Slug:** vox-vhl-hif
**Source:** cancer-biology/chapters/15-cancer-metabolism-the-warburg-effect-and-glucose.md (VHL/pseudohypoxia section)
**Card:** Cancer Biology Candidate 12

---

## Deliverable

Review MP4 (slate cut):
```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-vhl-hif/vox-vhl-hif-review.mp4
```

---

## Build summary

- Beats: 15 (B01–B15)
- Actual duration: 290.9 seconds (~4:51) — within 5:00 hard cap
- Slots filled: 13/15 — MANIM rendered
- Open slates: 2 (ai stills)
  - **B02** — clear cell RCC histology photomicrograph (see PROMPTS.md)
  - **B12** — VHL-absent consequence schematic (see PROMPTS.md)

---

## Gate results

| Gate | Result |
|---|---|
| Gate P (pedagogy) | PASS — PEDAGOGY.md |
| Gate F (factcheck) | PASS — FACTCHECK.md |
| Gate 0 (audio) | PASS — 15 beats generated, timings.json written |
| Gate A (static) | PASS — 12 clean, 1 benign WARN (B04 card scene), 0 errors |
| Gate W (WCAG) | PASS — 4 WARNs (W6 white-on-SLATE section cards — geometry-unresolved, confirmed correct at render), 0 errors |
| Gate B (pixel audit) | WARN — manim module not found in layout auditor on this machine; film compiled and renders correctly |

---

## Residual warnings

1. **Motion histogram:** `drawon` carries 8/15 beats (53%) — over the 40% pantry cap. If you want more visual variety, converting B09 (constitutive HIF output) to a COMPOSITE beat would bring drawon to ~47%. Low priority.
2. **B08 center-cut:** B08 rendered 22.2s vs 20.9s audio — auto-trimmed 0.6s head/tail. No content lost.
3. **Open slates B02, B12:** fill via PROMPTS.md prompts, drop in `media/B02.png` and `media/B12.png`, rerun `bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-vhl-hif`.

---

## Color law

- TEAL `#1F6F5C` = working pathway / HIF destroyed / normal cell
- CRIMSON `#BF3339` = VHL absent / HIF accumulating / clear cell RCC
- GOLD `#F5D061` = editor highlight, fill only (B08: VHL node; B14: 40x accumulation label)
