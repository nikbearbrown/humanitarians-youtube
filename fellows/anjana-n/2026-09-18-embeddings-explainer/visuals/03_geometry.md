# B03 — Geometry of Meaning

## Composition type
Remotion

## Layout
Dark stage. 2D scatter plot showing token clusters in embedding space.

## Elements

### Scatter plot
- A 2D space (no axis labels, just clean coordinates) representing a projection of the embedding space.
- Dots represent tokens, each with a small label.

### Positive cluster (upper right)
- Green dots (#27AE60): "growth," "raised," "exceeded," "beat," "sales increase."
- Dashed green circle enclosing the cluster.

### Negative cluster (lower left)
- Red dots (#E74C3C): "decline," "missed," "write-down," "impairment."
- Dashed red circle enclosing the cluster.

### Distance measurements
- A short dashed line between "growth" and "raised" with label: "similar" (short distance).
- A long dashed line between "growth" and "decline" with label: "distant" (long distance).

## Animation sequence
1. Empty 2D space appears (0.5s).
2. Positive cluster dots appear one by one with labels (2s).
3. Dashed green circle encloses them (0.5s).
4. Negative cluster dots appear one by one (2s).
5. Dashed red circle encloses them (0.5s).
6. Short distance line between "growth" and "raised," "similar" label (1.5s).
7. Long distance line between "growth" and "decline," "distant" label (1.5s).

## Palette
- Positive cluster: #27AE60 (green)
- Negative cluster: #E74C3C (red)
- Distance lines: #F1C40F (gold, dashed)
- Labels: #EAEAEA (white)
- Background: #1A1A2E
