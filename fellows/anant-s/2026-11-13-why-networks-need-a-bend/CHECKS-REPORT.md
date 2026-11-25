# CHECKS-REPORT — written before the first slate (PROOF GATE)

The 14 beats break down as 12 SHOW, 0 HOLD, 2 CARD and 0 PUNT:
- **SHOW (12):** B00–B10 and BHTF.
- **CARD (2):** BVDT (verdict recap, exempt) and BOUT (locked outro).
- **HOLD and PUNT:** none.

| Beat | Class | On-screen artifact named in `shot.show` |
|---|---|---|
| B00 | SHOW | composer ask plus three result lines |
| B01 | SHOW | hesitant writer correcting the misconception (depth → the bend) |
| B02 | SHOW | one grid through a matrix (stays straight), then through ReLU (creases); 'bend' boxed |
| B03 | SHOW | typeset seeded matrices, two paths, both (7, 8), box on "=" |
| B04 | SHOW | 1,000-point clouds coinciding; gap counter 8.88×10⁻¹⁵; bias identity |
| B05 | SHOW | XOR square, line sweep, tally 115,560 / best 3 of 4, inequality proof |
| B06 | SHOW | executed loss curve flattening at ¼; output bars at ½ next to best-line bars |
| B07 | SHOW | typeset hand-set ReLU net, row-by-row table, the clip boxed |
| B08 | SHOW | points through the linear map and the fold; separating line; band in input space |
| B09 | SHOW | two 10×10 seed grids (18/100 vs 91/100), dead-unit inset |
| B10 | SHOW | diagonal trace with two kinks, continued straight to (3,3) → −4 |
| BVDT | CARD | verdict artifact (recap, exempt) |
| BHTF | SHOW | composer prompt plus three check lines |
| BOUT | CARD | locked title outro |

PPT test: no two consecutive body beats share a visual scheme. The sequence runs:
1. grid transform
2. equation paths
3. point cloud
4. square + sweep
5. curve + bars
6. table
7. fold geometry
8. seed grids
9. function trace

Motion languages also vary: transform, typeset, morph, sweep, plot, row-land, fold, resolve, trace. No language appears in more than about 40% of beats.

## Teaching arc

| Item | Status | Where |
|---|---|---|
| FRAMEWORK | ✓ | B02 (layer = matrix, bend = ReLU, network = alternation), before any example |
| WORKED EXAMPLE | ✓ | B03 (collapse, seeded integers) and B07 (hand-set ReLU solves XOR), each using the B02 framework visibly |
| FALSIFIABILITY | ✓ | B09 (the bend is necessary, not sufficient: 18/100 trained runs) and B10 (where the kinks show: straight pieces, linear extrapolation), each a full beat |
| SCAFFOLDED TASK | ✓ | BHTF, with a prompt plus a three-point rubric |
| BOOKENDS | ✓ | B00, BVDT, BHTF, BOUT; `bookend_check` PASS |
| NO-SOURCE-NO-VERDICT | ✓ | every numeric claim has an on-screen counter, table or plot from `evidence.json`; the B07 weights carry the textbook citation |

Legibility contract:
- Side-by-side comparisons are held for at least 2 s: B03 (two paths), B06 (net vs best line), B09 (two grids).
- Negative space should stay between 15 and 35%. That is verified at visual QC, not here.
