# SHOTLIST — vox-calibration-curve

## Rhythm check
14 beats | estimated ~116s ≈ 1:56 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · DOCUMENT · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow |
| B02 | COLD OPEN | GRAPHIC | own | trace | Dashboard: 94% accuracy, all green, sign off |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | Accuracy vs. confidence: different claims |
| B05 | THE PROBLEM | GRAPHIC | own | trace | 99% promise: 99 of 100 should be positive |
| B06 | THE MECHANISM | STILL | ai | kenburns | Slate — prediction stream, high-confidence labels (see PROMPTS.md) |
| B07 | THE MECHANISM | GRAPHIC | own | drawon | Reliability diagram: axes + perfect diagonal |
| B08 | THE MECHANISM | GRAPHIC | own | accumulate | Sort predictions into confidence bins |
| B09 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "70% confident on 1000 cases → 700 should be positive" |
| B10 | THE MECHANISM | GRAPHIC | own | accumulate | Count positives per bin; high-confidence bins fall short |
| B11 | THE IMPLICATION | GRAPHIC | own | drawon | Calibration curve peels away from diagonal at top |
| B12 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "A net will say 99% when it should say 85%, fluently" |
| B13 | THE EXAMPLE | GRAPHIC | own | compare | Medical: 400 patients at 99%, only 310 (77%) actually positive |
| B14 | RECAP | CARD | own | endcard | "Accuracy measures correct calls. Calibration measures honest ones." |

## Color semantics
- TEAL = calibrated region / diagonal / honest zone
- CRIMSON = overconfident tail / peel / overclaiming
- GOLD = key insight / axis labels
- Never swapped mid-film ✓

## STILL economy
~116s → 1–2 stills allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- No ECE or Brier formulas ✓
- No temperature-scaling or softmax mechanics ✓
- No human-forecaster calibration tangent ✓
- One model, one curve ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS the high-confidence output stream — predictions each labeled 97%, 99%, 98%.
Wrong = generic data center, any screenshot without confidence percentages visible.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=machine+learning+predictions+output&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B06-<anything>.jpg`; set `shot.focus` toward
the percentage labels after intake.
