# QC STATUS — Muse, Doing The Errands.

Build date: 2026-10-28 · 10 beats · 2:06 measured audio · Kokoro `am_onyx` · $0.00

| File | Spec | Duration |
|---|---|---|
| `hussain-meta-muse-agent-4k-16x9.mp4` | 3840×2160, 24fps, AAC | 125.67s |
| `hussain-meta-muse-agent-4k-9x16.mp4` | 2160×3840, 24fps, AAC | 125.67s |

Both masters were promoted through `compile.py`'s full final path (GATE F paperwork, beat lint, GATE V).
**GATE V: 0 BLOCKER / 0 MAJOR in both aspects.** The 9:16 is a native reflowed render: every beat
uses a `*916` composition, not a crop.

## Defects found and fixed by looking at frames

1. Body scenes underfilled the canvas. Type was enlarged in all four Muse scenes. B02 got placeholder
   list rows and B06 portrait cards now stretch the full safe height.
2. Portrait B00: the segment title "Muse, The Personal Agent" crossed the right safe edge (2 BLOCKERs).
   The 9:16 sheet now uses "The Personal Agent". 16:9 is unchanged.
3. B01 (hesitant writer) was flagged underfill at 50% and 85%, because the text is still typing at
   those samples. It is declared `qc.sparse_by_design` with a written reason. That waives only
   underfill/clustered. The final frame was checked: all three lines and both corrections are on screen.

## Known lint warning

`SKIN LINT: outro is CortexTitleOutro, OUTRO LAW wants ClaudeTitleOutro`. This is intentional:
ClaudeTitleOutro is locked to @NikBearBrown, and this reel is narrated by Hussain as himself.

## Human review

Both masters were watched and approved by Mohammed Hussain on 2026-10-28. The record is in `metadata.approvals.final_cut` in each beat sheet, with the master's sha256.
