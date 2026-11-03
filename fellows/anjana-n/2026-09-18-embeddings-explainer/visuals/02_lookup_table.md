# B02 — The Lookup Table

## Composition type
Remotion

## Layout
Dark stage. Large embedding matrix with a row lookup animation.

## Elements

### Embedding matrix
- A grid with 6-8 visible rows and 8-10 visible columns.
- Row labels (left side): "the," "revenue," "decline," "forecast," "grew," "margin," "beat."
- Column headers: "dim 1," "dim 2," ... "dim 768" (with ellipsis between dim 3 and dim 768).
- Cells contain small floating point numbers.

### Row highlight
- The row for "revenue" highlights with a blue glow.
- The highlighted row slides out of the matrix and becomes the standalone embedding vector from B01.

### Training timeline
- A horizontal bar at the bottom.
- Left end: "before training" with matrix cells showing random static noise.
- Right end: "after training" with structured, meaningful values.
- An animated transition sweeps left to right, transforming noise into structure.

### Label
- "embedding matrix" in muted text above the grid.

## Animation sequence
1. Matrix fades in with all rows visible (2s).
2. "revenue" row highlights blue (1s).
3. Highlighted row slides out to the right, becoming the vector (2s).
4. Matrix fades slightly, training timeline appears at bottom (1s).
5. Timeline animates: noise transforms to structure, left to right sweep (3s).

## Palette
- Matrix border: #2C3E50 (dark slate)
- Row highlight: #4A90D9 (blue)
- Noise state: random greys
- Trained state: blue gradient values
- Timeline bar: #27AE60 (green sweep)
- Background: #1A1A2E
