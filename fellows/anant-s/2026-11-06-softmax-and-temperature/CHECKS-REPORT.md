# CHECKS-REPORT — written before the first slate (PROOF GATE)

The 13 beats break down as 11 SHOW, 0 HOLD, 2 CARD and 0 PUNT:
- **SHOW (11):** B00–B09 and BHTF.
- **CARD (2):** BVDT (verdict recap, exempt) and BOUT (locked outro).
- **HOLD and PUNT:** none.

| Beat | Class | On-screen artifact named in `shot.show` |
|---|---|---|
| B00 | SHOW | composer ask plus three result lines with executed percentages |
| B01 | SHOW | hesitant writer correcting the misconception |
| B02 | SHOW | next-token loop diagram, five labelled constructed logits |
| B03 | SHOW | MathTex softmax with box spotlight and glossary per symbol |
| B04 | SHOW | arithmetic table (z, eᶻ, sum, p) from evidence, then bars |
| B05 | SHOW | five bars morphing with a temperature dial, rank badges fixed |
| B06 | SHOW | probability strip, seeded tick, 3 × 20 word chips |
| B07 | SHOW | predicted outlines vs counted bars, gap chips, 10,000 draws |
| B08 | SHOW | strip collapsing as T → 0, MathTex limit, 20 × "mat" |
| B09 | SHOW | constructed wrong-ranking bars, "wrong" counter, fixed ranks |
| BVDT | CARD | verdict artifact, 6 lines (recap, exempt) |
| BHTF | SHOW | composer prompt plus three check lines |
| BOUT | CARD | locked title outro |

## Teaching arc

| Item | Status | Where |
|---|---|---|
| FRAMEWORK | ✓ | B02 (the loop) and B03 (the formula), both before the example |
| WORKED EXAMPLE | ✓ | B04 applies the B03 formula column by column with executed numbers; the formula stays on screen |
| FALSIFIABILITY | ✓ | B07 (a prediction that could have failed, tested on 10,000 draws) and B09 (a failure mode: temperature cannot fix a wrong ranking). Each is a full beat. |
| SCAFFOLDED TASK | ✓ | BHTF: a paste-ready prompt plus a three-point rubric |
| BOOKENDS | ✓ | cold open, BVDT, BHTF, BOUT; `bookend_check` PASS |
| NO-SOURCE-NO-VERDICT | ✓ | every numeric claim has an on-screen counter, table or chip from `evidence.json`; constructed inputs are labelled on screen |

Legibility contract:
- Comparisons in B06 (three strips), B07 (predicted vs counted) and B09 (before and after the dial) are side by side and held for at least 2 s.
- Negative space stays between 15 and 35%, to be verified at visual QC.

**PPT test:** no beat is a headline over a paragraph. Every body beat has at least four timed `show` events that move on spoken words.

**Machine checks, 2026-11-22:** `bookend_check.py` PASS (exit 0); `beat_lint.py` clean (exit 0).
