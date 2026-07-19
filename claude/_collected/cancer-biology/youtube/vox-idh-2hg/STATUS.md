# STATUS — vox-idh-2hg

**Built:** 2026-07-08
**Slug:** vox-idh-2hg
**Title:** Why a Metabolic Enzyme Mutation Can Lock Cells Into an Immature State
**Topic:** CANCER BIOLOGY
**Source:** cancer-biology/chapters/07-epigenetics-in-cancer-the-methylation-and-histone-code.md

---

## Deliverable

`open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-idh-2hg/vox-idh-2hg-review.mp4`

---

## Stats

- Beats: 13
- Actual duration: 272.4 s (4:32)
- Slots filled: 11/13 (MANIM) — B02, B10 are SLATE (ai media pending)

## Slot status

| Beat | Type | Status |
|---|---|---|
| B01 | CARD / MANIM | filled |
| B02 | STILL · ai | SLATE — needs image (AML bone marrow histology) |
| B03 | CARD / MANIM | filled |
| B04 | GRAPHIC / MANIM | filled |
| B05 | GRAPHIC / MANIM | filled |
| B06 | GRAPHIC / MANIM | filled |
| B07 | GRAPHIC / MANIM | filled |
| B08 | GRAPHIC / MANIM | filled |
| B09 | GRAPHIC / MANIM | filled |
| B10 | STILL · ai | SLATE — needs image (hematopoiesis diagram) |
| B11 | GRAPHIC / MANIM | filled |
| B12 | GRAPHIC / MANIM | filled |
| B13 | VIDEO / outro | filled (bearbrown mascot) |

## Open slots (ai stills)

Generate images using the prompts in PROMPTS.md, drop into `media/` with the beat id prefix (e.g. `B02-aml-marrow.png`), then rerun `bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-idh-2hg`.

## Gate results

- Gate A (static pre-flight): 11/11 CLEAN
- Gate W (WCAG + margins): 11/11 CLEAN
- Gate 0 (audio): PASS — 13 beats, 272.4 s total
- Gate B (pixel audit): warnings only (manim not importable as module in qc path — benign; scenes slotted successfully)

## Compiler notes

- `drawon` carries 6/13 beats (46%) — slightly over the 40% pantry cap; soft warning only. If the human requests a revision, consider varying 1–2 GRAPHIC beats to annotate or composite motion language.

## Exclusions honored

- No full TCA cycle chemistry
- No TET1/2/3 isoforms
- No IDH-mutant glioma vs AML distinction
- No histone demethylase mechanism detail
- No DNMT inhibitor comparison
