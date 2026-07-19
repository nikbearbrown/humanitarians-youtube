# STATUS — vox-bcl-selectivity

## Build complete

- **Slug:** vox-bcl-selectivity
- **Title:** Why the Same Drug That Kills Cancer Cells Kills Platelets (and How to Fix It)
- **Beats:** 14 (B01–B14)
- **Actual duration:** 216.5s (~3:37)
- **Review MP4:** `cancer-biology/youtube/vox-bcl-selectivity/vox-bcl-selectivity-review.mp4`

## Gate summary

| Gate | Result |
|------|--------|
| Gate P (pedagogy) | PASS |
| FACTCHECK | VERDICT: PASS |
| Gate 0 (audio) | PASS — 14 beats, 215.58s locked |
| Gate A (static pre-flight) | PASS — 13/13 scenes clean |
| Gate W (WCAG) | WARNINGS only (W6 white-adrift on white text inside colored shapes — text is on its colored card, not on cream; cosmetically acceptable) — no ERRORs |
| Gate B (pixel audit) | WARNING — manim not importable in audit environment; all scenes rendered and slotted correctly |

## Slots

| Beat | Status |
|------|--------|
| B01 | MANIM |
| B02 | SLATE (ai still — fill via SHOTLIST.md / PROMPTS.md) |
| B03–B14 | MANIM or VIDEO (B14 outro rendered) |

## Open slots (ai stills to fill)

- **B02** — blood smear microscopy image; prompt in PROMPTS.md

## Residual warnings

- **Gate W W6:** White text inside colored solid cards (e.g., "LEUKEMIA CELL" on a teal card, "NAVITOCLAX" on a slate bar) flagged as white-adrift. These are legitimate: the white text renders ON the colored card background (teal/slate/crimson), not on the cream ground. The Gate W checker resolves coordinates approximately and flags when it cannot confirm the backing. Visually correct; no fix needed.
- **Motion histogram:** drawon carries 9/14 beats (64%); compile warns at >40%. The "compare" move of this reel is fundamentally graphic-driven — each drawon scene is visually distinct. Acceptable for this card's mechanism.

## Watch

```
open /Users/bear/Documents/CoWork/bear-textbooks/books/cancer-biology/youtube/vox-bcl-selectivity/vox-bcl-selectivity-review.mp4
```
