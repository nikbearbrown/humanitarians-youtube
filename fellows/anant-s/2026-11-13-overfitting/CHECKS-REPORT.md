# CHECKS-REPORT — written before the first slate (PROOF GATE)

The 11 beats break down as 9 SHOW, 0 HOLD, 2 CARD and 0 PUNT:
- **SHOW (9):** B00–B07 and BHTF.
- **CARD (2):** BVDT (verdict recap, exempt) and BOUT (locked outro).
- **HOLD and PUNT:** none.

| Beat | Class | On-screen artifact named in `shot.show` |
|---|---|---|
| B00 | SHOW | composer ask plus three result lines (degree 15: 0 / 9,882.6; degree 3: 0.0586 / 0.0471) |
| B01 | SHOW | hesitant writer correcting "means a perfect model" → "can mean memorized noise" |
| B02 | SHOW | hidden true curve, 16 dots displaced by noise, locked test box |
| B03 | SHOW | typeset MSE, box spotlights, worked term −1.032² = 1.065, 4.546 ÷ 16 = 0.284 |
| B04 | SHOW | three fits side by side with executed train/test counters |
| B05 | SHOW | train/test error across degrees 0–15, floor line, exit chips |
| B06 | SHOW | degree-15 refit as n grows, ladder of executed errors |
| B07 | SHOW | trial grids 69.6% vs 55.2%, control 53.3%, median counters |
| BVDT | CARD | verdict artifact (recap, exempt) |
| BHTF | SHOW | composer prompt plus three check lines |
| BOUT | CARD | locked title outro |

## Teaching arc

| Item | Status | Where |
|---|---|---|
| FRAMEWORK | ✓ | B02 (the setup: hidden truth, train/test split) and B03 (the grade: MSE), both before any example |
| WORKED EXAMPLE | ✓ | B04 runs three models through the B02/B03 framework, with the train and test grades on screen. B05 extends it to all 16 degrees. |
| FALSIFIABILITY | ✓ | B06: the "complex = bad" story bends, because more data tames the same degree-15 model. B07: the "held-out score = honest" story bends, because choosing by it makes it optimistic. Each is a full beat. |
| SCAFFOLDED TASK | ✓ | BHTF: a paste-ready prompt plus a three-point rubric. The third check tests the B07 lesson. |
| BOOKENDS | ✓ | cold open, BVDT, BHTF, BOUT; `bookend_check` PASS |
| NO-SOURCE-NO-VERDICT | ✓ | every spoken number has an on-screen counter, chip or grid from `evidence.json`; `make_sheet.py` asserts the spoken values |

**Legibility contract:**
- Comparisons in B04 (three panels) and B07 (two grids) are side by side and held for at least 2 s.
- The B06 ladder keeps all rungs visible at once.
- Negative space should stay between 15 and 35%; this is verified at visual QC.
- Un-highlighted elements never drop below 40% opacity. The B02 truth-curve fade stops at 40%.

**PPT test:** no body beat is a static slide. Every body beat has a mover that enacts the sentence:
- B02: dots jump off the curve.
- B03: the spotlight walks the formula.
- B04: curves draw.
- B05: series land.
- B06: the model refits.
- B07: grids fill.
