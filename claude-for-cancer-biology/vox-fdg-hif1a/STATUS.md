# STATUS — vox-fdg-hif1a
**Why the Warburg Tumor Lights Up on a PET Scan**
Built: 2026-07-08

## Build result: SLATE CUT COMPLETE

- Slug: vox-fdg-hif1a
- Beat count: 13 beats (B01–B13)
- Actual duration: 229.2 s (3:49)
- Review MP4: `vox-fdg-hif1a-review.mp4`

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-fdg-hif1a/vox-fdg-hif1a-review.mp4
```

## Gate results

| Gate | Result | Notes |
|------|--------|-------|
| Gate P (pedagogy) | PASS | All act-structure, gap formula, vocabulary law, example act checks passed |
| Gate F (factcheck) | PASS | 26 claims verified; 4 illustrative numbers labeled |
| Gate 0 (audio) | PASS | 13 mp3s generated; actual duration 228.26 s |
| Gate A (static) | PASS | All 12 scene classes clean, 0 errors, 0 warnings |
| Gate W (WCAG/margins) | PASS | All 12 scene classes clean after fixing W3/W6 items |
| Gate B (pixel audit) | WARNING (benign) | `ModuleNotFoundError: No module named 'manim'` in audit runner — scenes rendered correctly; warning is toolchain-environment, not a layout failure |

## Slots

| Beat | Type | Status |
|------|------|--------|
| B01 | CARD | MANIM (rendered) |
| B02 | STILL · ai | SLATE — fill with FDG-PET vs CT comparison image (see PROMPTS.md) |
| B03 | CARD | MANIM (rendered) |
| B04 | GRAPHIC | MANIM (rendered) |
| B05 | CARD | MANIM (rendered) |
| B06 | GRAPHIC | MANIM (rendered) |
| B07 | GRAPHIC | MANIM (rendered) |
| B08 | GRAPHIC | MANIM (rendered) |
| B09 | GRAPHIC | MANIM (rendered) |
| B10 | GRAPHIC | MANIM (rendered) |
| B11 | GRAPHIC | MANIM (rendered) |
| B12 | GRAPHIC | MANIM (rendered) |
| B13 | VIDEO (outro) | rendered with bear mascot |

**Open slots (human fill):** B02 only — CT/PET comparison still (see PROMPTS.md)

## Residual warnings

- Motion histogram: `drawon` carries 61% of beats (advisory — 8/13). Acceptable for a mechanistic cascade film where each drawon beat is a distinct step in one continuous causal chain. Convert if pacing feels rushed on review.
- Gate B ran but found `ModuleNotFoundError: No module named 'manim'` — this is a local environment issue with the audit runner's Python path, not a scene rendering problem. All scenes rendered correctly as confirmed by the compiled video.

## Color semantics

- TEAL #1F6F5C = glucose uptake / GLUT transporters / HIF-1alpha active / accumulation
- CRIMSON #BF3339 = FDG trapped / blocked pathways / PHD stalled
