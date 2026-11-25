# B03 — Sparse Activation

## Composition type
Remotion

## Layout
Dark stage. Side-by-side comparison: dense model (left) vs MoE model (right). Capacity circle below the MoE side.

## Elements

### Left: Dense model
- A single solid rectangle labeled "dense — 13B."
- Fully lit in purple (#9B59B6).
- Below: "13B total = 13B active."
- A meter bar: fully filled green (#27AE60).

### Right: MoE model
- Eight smaller rectangles in a grid.
- Two are lit blue (#3498DB), six are dim grey (#555555).
- Label: "MoE — 8 × 6.5B."
- Below: "52B total, 13B active."

### Capacity circle (below MoE)
- A large circle representing 52B total parameters.
- Color: #27AE60 (green) outline.
- A smaller highlighted slice (about 25% of the circle) in blue (#3498DB).
- Label on slice: "13B active."
- Label on full circle: "52B total."

### Comparison annotation
- Centered between the two sides:
  - "4× capacity."
  - "same compute."
- Color: #F1C40F (gold).

### Throughput bar (bottom)
- Two horizontal bars:
  - Dense: green bar at full width, labeled "13B ops/token."
  - MoE: identical green bar at same width, labeled "13B ops/token."
- Label below: "per-token cost: identical."

## Animation sequence
1. Dense model block appears, fully lit (1.5s).
2. "13B total = 13B active" label (1s).
3. MoE model grid appears — two light up, six stay dim (2s).
4. "52B total, 13B active" label (1s).
5. Capacity circle appears below MoE — slice highlights (2s).
6. "4× capacity, same compute" annotation in gold (1.5s).
7. Throughput bars appear — both identical length (2s).
8. "per-token cost: identical" label (1s).

## Palette
- Dense block: #9B59B6 (purple)
- Active experts: #3498DB (blue)
- Inactive experts: #555555 (dim grey)
- Capacity circle: #27AE60 (green) outline, #3498DB (blue) slice
- Comparison text: #F1C40F (gold)
- Throughput bars: #27AE60 (green)
- Background: #1A1A2E
- Text: #EAEAEA
