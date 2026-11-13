# B02 — Prediction Intervals & Uncertainty

## Composition type
Remotion

## Layout
Dark stage. Center: prediction point with expanding confidence band. Below: two additional uncertainty meters.

## Elements

### Probability axis (horizontal)
- A horizontal axis from 0% to 100%.
- Tick marks at 25%, 50%, 75%.
- Color: #EAEAEA.

### Prediction point
- A gold (#F1C40F) dot at the 72% mark.
- Label above: "72%."

### Conformal interval band
- A translucent blue (#3498DB, 30% opacity) band expanding from the dot.
- Left edge at 61%, right edge at 83%.
- Label: "conformal interval: 61%–83%."
- Thin blue border lines at 61% and 83%.

### MC dropout meter (below, left)
- A horizontal bar showing 50 small dots scattered along a range.
- Dots cluster near 72% but spread from ~65% to ~80%.
- Label: "MC dropout — 50 passes."
- Variance annotation: "σ = 4.2."
- Color: dots are #9B59B6 (purple).

### Ensemble disagreement meter (below, right)
- Six small model icons in a row.
- Each shows its own prediction as a small bar extending from a baseline.
- Four bars cluster near 72%, two deviate (one at 65%, one at 79%).
- Label: "ensemble disagreement."
- Color: model icons are #F39C12 (amber).

### Unified uncertainty score
- At the bottom center, a gauge or meter.
- Needle pointing to "moderate."
- Three zones: low (green #27AE60), moderate (amber #F39C12), high (red #E74C3C).
- Arrows from all three uncertainty sources feed into this gauge.

## Animation sequence
1. Probability axis appears (0.5s).
2. Gold prediction dot lands at 72% (1s).
3. Blue confidence band expands outward from the dot (2s).
4. "conformal interval" label appears (0.5s).
5. MC dropout meter appears below left — dots scatter (1.5s).
6. Ensemble disagreement meter appears below right — bars fan out (1.5s).
7. Arrows converge to unified uncertainty gauge (1.5s).
8. Gauge needle settles on "moderate" (0.5s).

## Palette
- Prediction point: #F1C40F (gold)
- Conformal band: #3498DB (blue, translucent)
- MC dropout dots: #9B59B6 (purple)
- Ensemble icons: #F39C12 (amber)
- Gauge zones: #27AE60 (low), #F39C12 (moderate), #E74C3C (high)
- Background: #1A1A2E
- Text: #EAEAEA
