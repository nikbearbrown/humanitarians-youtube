# PEDAGOGY — claude-liam-diagram-redraw
# "Claude, Redrawn." | diagram-redraw skill teardown

## Learning goal
Viewer leaves knowing: (1) diagram-redraw mines Wikipedia media refs for editorial usefulness signal, classifies them (doable/logo/photo), and redraws the doable ones in house style; (2) the 3-stage pipeline: classify → human select → redraw; (3) the two hard rules: never copy a source image (redraw the idea), and only draw what the book actually needs.

## Prediction beat
B03 asks: given a page with 12 images, how many will be doable diagrams? Viewer predicts before B04 shows the actual classification split (doable ≈ 40%, logos + photos skipped).

## Concrete before abstract
B04 shows the Stage 1 candidate plan for a real topic (quantum mechanics) before B05/B06/B07 state the abstract laws.

## Self-demo check
B04 is genuinely free: Stage 1 (harvest.mjs) is deterministic, no AI, no API. Shows the classification table and ranked candidates as they would appear in the output JSON/MD.

## ILLUSTRATE LAW
- UI beats (5): B00, B03, BVDT, BHTF, BOUT
- Illustration beats (6): B01, B02, B04, B05, B06, B07

## VERDICT: PASS
