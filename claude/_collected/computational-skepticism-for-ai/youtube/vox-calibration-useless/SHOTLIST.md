# SHOTLIST — vox-calibration-useless

## Rhythm check
13 beats | estimated ~185s ≈ 3:05 | under 5:00 cap ✓
CARD · GRAPHIC · CARD · GRAPHIC · GRAPHIC · STILL · GRAPHIC · DOCUMENT · GRAPHIC · DOCUMENT · GRAPHIC · GRAPHIC · CARD
Max run: 2 consecutive same type ✓

## Act map

| Beat | Act | Type | Source | Motion | Notes |
|------|-----|------|--------|--------|-------|
| B01 | COLD OPEN | CARD | own | title | "COMPUTATIONAL SKEPTICISM" eyebrow |
| B02 | COLD OPEN | GRAPHIC | own | compare | ECE=0 vs same 30% output for every patient |
| B03 | THE QUESTION | CARD | own | question | On screen + in narration ✓ |
| B04 | THE PROBLEM | GRAPHIC | own | compare | What calibration actually measures |
| B05 | THE PROBLEM | GRAPHIC | own | compare | Calibration vs discrimination: separate axes |
| B06 | THE MECHANISM | STILL | ai | kenburns | Slate — reliability diagram, all dots piled on one point (see PROMPTS.md) |
| B07 | THE MECHANISM | GRAPHIC | own | compare | Reliability diagram: discriminating vs base-rate model |
| B08 | THE MECHANISM | DOCUMENT | own | highlight | Quote: "perfect calibration…useless for triage" |
| B09 | THE IMPLICATION | GRAPHIC | own | compare | Both required: calibration + discrimination |
| B10 | THE IMPLICATION | DOCUMENT | own | highlight | Quote: "honest about uncertainty but useless for triage" |
| B11 | THE IMPLICATION | GRAPHIC | own | trace | What to report: plot diagram, check spread |
| B12 | THE EXAMPLE | GRAPHIC | own | compare | Fraud model: ECE=0, every transaction = 2.1%, no signal |
| B13 | RECAP | CARD | own | endcard | "Calibration = honesty. Discrimination = usefulness. Separate axes." |

## Color semantics
- TEAL = good calibration / on the diagonal / honest zone
- CRIMSON = fails to discriminate / useless for decisions / base-rate output
- GOLD = the key insight / axis labels / both axes together
- SLATE = neutral axis background
- Never swapped mid-film ✓

## STILL economy
~185s → 1–2 stills allowed (1 per 90s); used: 1 (B06, THE MECHANISM entry) ✓

## Exclusions honored
- No Brier score formula or three-term decomposition algebra ✓
- No ECE binning math ✓
- No AUROC definition ✓
- No temperature scaling ✓
- Two dot-patterns carry the visual argument ✓

---

## Slots YOU fill (prompts in PROMPTS.md, beat-id-prefixed)

### B06 — STILL · ai · kenburns (THE MECHANISM entry)
The content IS the reliability diagram with all predictions collapsed to one point.
Wrong = generic data science dashboard, any scatterplot without the pile-up visible.
Real-asset alternatives (check first):
- https://commons.wikimedia.org/w/index.php?search=calibration+reliability+diagram&title=Special:MediaSearch&type=image
Drop the result in `pantry/` as `B06-<anything>.jpg`; set `shot.focus` toward
the piled-up dot cluster after intake.
