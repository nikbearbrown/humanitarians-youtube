# B04 — Concept Drift

## Composition type
Remotion

## Layout
Dark stage. Split view: concept drift on the left, prediction decay on the right.

## Elements

### Left side: Concept Drift Detection
- Two overlapping distribution curves (kernel density style).
- First curve: blue (#4A90D9), labeled "Q1-Q2" (the baseline window).
- Second curve: orange (#E67E22), labeled "Q3-Q4" (the recent window), shifted right.
- The gap between the curves is shaded in light orange.
- A metric badge in the shaded gap: "PSI = 0.31."

### Right side: Prediction Decay Tracking
- A rolling accuracy line chart over ~30 data points.
- The line starts above a horizontal dashed baseline labeled "naive momentum baseline."
- Over the last 10 points, the line trends downward, crossing below the baseline.
- The 10 consecutive below-baseline points are highlighted with red dots.

## Animation sequence
1. Left: blue curve draws (1s).
2. Orange curve draws, shifted right (1s).
3. Gap shading fills in, "PSI = 0.31" badge appears (1s).
4. Icon pulses (0.5s).
5. Right: accuracy line draws left to right (2s).
6. Baseline dashed line appears (0.5s).
7. Last 10 points below baseline highlight, alert badge appears (2s).

## Palette
- Baseline distribution: #4A90D9 (blue)
- Shifted distribution: #E67E22 (orange)
- Drift shading: #E67E22 at 20% opacity
- PSI badge: #E67E22 fill, white text
- Accuracy line: #27AE60 (green) above baseline, #E74C3C (red) below
- Baseline: #95A5A6 (grey, dashed)
- Alert badge: #E74C3C (red)
