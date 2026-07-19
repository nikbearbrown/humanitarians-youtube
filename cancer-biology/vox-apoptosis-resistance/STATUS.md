# STATUS — vox-apoptosis-resistance

**Built:** 2026-07-08
**Card:** Cancer Biology Candidate 09

## Deliverable

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-apoptosis-resistance/vox-apoptosis-resistance-review.mp4
```

## Build summary

- Beats: 15
- Duration: 163.9s (~2:44)
- Act structure: COLD OPEN (B01–B02) → THE QUESTION (B03) → THE PROBLEM (B04–B05) → Section card (B06) → THE MECHANISM / five sabotage points (B07–B11) → THE IMPLICATION (B12) → THE EXAMPLE / illustrative (B13–B14) → RECAP (B15)

## Gate results

| Gate | Result |
|------|--------|
| P (Pedagogy) | PASS |
| 0 (Audio) | PASS — 15 mp3s, 162.96s actual |
| A (Static / per-class) | 14/14 CLEAN |
| W (WCAG margins) | 14/14 CLEAN |
| B (Pixel audit) | Warning only — `manim` not installed in audit env; renders completed |

## Motion histogram

accumulate:7  hold:5  drawon:2  kenburns:1

Note: accumulate at 46% is slightly over the 40% advisory cap. The card's manim_move is `accumulate` — the five-block sabotage mechanism IS the film's visual through-line. Advisory only, not a gate failure.

## Slots

| Beat | Status |
|------|--------|
| B01 | MANIM — title card |
| B02 | SLATE — awaiting ai still (CLL bone marrow histology). Prompt in PROMPTS.md. |
| B03 | MANIM — question card |
| B04 | MANIM — intact circuit drawon |
| B05 | MANIM — blocked circuit |
| B06 | MANIM — section card |
| B07 | MANIM — sabotage 1 (BCL-2 HIGH) |
| B08 | MANIM — sabotage 2 (BAX LOST) |
| B09 | MANIM — sabotage 3 (XIAP) |
| B10 | MANIM — sabotage 4 (AKT-BAD) |
| B11 | MANIM — sabotage 5 (p53 MUT) |
| B12 | MANIM — five-block static + gold signal arrow |
| B13 | MANIM — clonal selection step 1 |
| B14 | MANIM — clonal selection steps 2-3 |
| B15 | VIDEO — recap + outro (bear mascot) |

## Open slots (human fill)

- **B02**: STILL ai — CLL bone marrow biopsy. See PROMPTS.md for generative prompt and Wikimedia archive link. After filling: drop in `media/B02.png`, run `bash vox/scripts/vox_run.sh cancer-biology/youtube/vox-apoptosis-resistance` (only B02 slot recompiles).

## Exclusions confirmed

No extrinsic pathway, no venetoclax mechanism, no necroptosis/pyroptosis/ferroptosis, no p53 transcriptional detail (PUMA/NOXA absent), no IAP biochemistry beyond XIAP naming.
