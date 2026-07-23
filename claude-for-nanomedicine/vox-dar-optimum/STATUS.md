# STATUS — vox-dar-optimum

## Build: COMPLETE (slate cut)

Deliverable: `vox-dar-optimum-review.mp4` — 170.5s (~2:51)

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-nanomedicine/youtube/vox-dar-optimum/vox-dar-optimum-review.mp4
```

## Beat summary

| Beat | Type | Slot | Duration |
|------|------|------|----------|
| B01 | CARD title | MANIM | 9.2s |
| B02 | GRAPHIC accumulate | MANIM | 14.9s |
| B03 | CARD question | MANIM | 9.6s |
| B04 | GRAPHIC drawon | MANIM | 16.2s |
| B05 | STILL ai | **SLATE** | 13.1s |
| B06 | GRAPHIC accumulate | MANIM | 14.1s |
| B07 | GRAPHIC drawon | MANIM | 12.2s |
| B08 | CARD section | MANIM | 15.4s |
| B09 | GRAPHIC drawon | MANIM | 15.3s |
| B10 | GRAPHIC accumulate | MANIM | 17.6s |
| B11 | DOCUMENT highlight | MANIM | 21.0s |
| B12 | CARD endcard + outro | VIDEO | 11.8s |

## Open slot

- **B05**: STILL·ai — cell not internalizing enough payload. Generate with the prompt in PROMPTS.md; drop as `media/B05.png`, rerun `bash vox/scripts/vox_run.sh cancer-nanomedicine/youtube/vox-dar-optimum`.

## QC gates

- Gate A: all scenes clean (B11 has benign `_quote_scene` WARN)
- Gate W: all scenes clean
- Gate B: advisory-only warnings (manim import path in audit env); no layout errors found
- PEDAGOGY: PASS
- FACTCHECK: PASS

## Notes

- All DAR example numbers (68%, 11%, 2.4 µg/g, 0.3 µg/g, 3 mice) are illustrative, labeled in B11 narration and FACTCHECK
- Exclusions confirmed: no linker detail, no bystander effect, no five-step funnel, no site-specific conjugation
- Actual duration locked: 169.54s (audio) / 170.5s (compiled)
