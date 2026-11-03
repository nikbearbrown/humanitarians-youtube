# B02 — Signal Decay and Half-Lives

## Composition type
Remotion

## Layout
Dark stage. A chart area with six decay curves on shared axes. Half-life markers where each curve crosses the threshold.

## Elements

### Axes
- X-axis: "time horizon" with tick marks at 1d, 2d, 5d, 10d, 20d, 30d, 60d.
- Y-axis: "correlation with excess returns" from 0.0 to 0.5.
- Color: #95A5A6 (grey) for axis lines and labels.

### Significance threshold
- Horizontal dashed line at ~0.05 correlation level.
- Label: "significance threshold."
- Color: #95A5A6 (grey dashed).

### Six decay curves
1. "hedging index" — #E67E22 (orange). Slow decay. Crosses threshold around 20d.
2. "tone shift" — #9B59B6 (purple). Medium decay. Crosses around 15d.
3. "confidence score" — #27AE60 (green). Medium decay. Crosses around 12d.
4. "dodge score" — #E74C3C (red). Fast decay. Crosses around 5d.
5. "fwd-looking density" — #4A90D9 (blue). Slow decay. Crosses around 25d.
6. "market share language" — #1ABC9C (teal). Medium decay. Crosses around 10d.

### Half-life markers
- Where each curve crosses the threshold, a small vertical line with a dot.
- Label beside each: "t½ = Xd."
- Color matches the curve.

### Title
- Top: "signal decay by type."
- Color: #EAEAEA.

## Animation sequence
1. Axes and threshold line draw (1s).
2. Curves draw left to right simultaneously, each at its own decay rate (3s).
3. Half-life markers appear where curves cross the threshold (2s).
4. Labels fade in beside each marker (1.5s).
5. "hedging index" and "fwd-looking density" curves highlighted briefly as slow decayers (1s).
6. "dodge score" highlighted briefly as fast decayer (0.5s).

## Palette
- Hedging index: #E67E22 (orange)
- Tone shift: #9B59B6 (purple)
- Confidence score: #27AE60 (green)
- Dodge score: #E74C3C (red)
- Forward-looking density: #4A90D9 (blue)
- Market share language: #1ABC9C (teal)
- Threshold/axes: #95A5A6 (grey)
- Background: #1A1A2E
- Text: #EAEAEA
