# B02 — Sector Intelligence

## Layout
Dark stage. Three panels side by side: aggregation funnel (left), mood index (center), cross-sector heatmap (right).

## Elements

### Left panel: Sector Sentiment Aggregator

#### Funnel visualization
- Top: scattered dots in various colors representing individual company signals.
- Each dot is sized by market cap (larger = bigger company).
- Dots flow downward through a funnel shape.
- Bottom: a single wide horizontal bar emerges — the sector composite.
- Bar is colored by composite sentiment: blue-green gradient.
- Label above: "sector sentiment aggregator."
- Small text: "market-cap weighted."

### Center panel: Mood Index

#### Time-series chart
- X-axis: quarters (Q1 '23, Q2 '23, Q3 '23, Q4 '23, Q1 '24, Q2 '24).
- Y-axis: mood index value (0 to 100).
- A line chart in #4A90D9 (blue) trending across quarters.
- A horizontal dashed line at the historical mean (~55), labeled "historical mean."
- The line crosses below the mean at Q4 '23 — crossing point marked with a gold (#F1C40F) circle.
- Small flag at the crossing: "regime change."
- Label above: "sector mood index."

### Right panel: Cross-Sector Heatmap

#### Heatmap grid
- Rows: "Tech," "Healthcare," "Finance," "Energy."
- Columns: "sentiment," "hedging," "confidence."
- Each cell colored by z-score:
  - Strong positive (z > 1): #27AE60 (green).
  - Neutral (-0.5 to 0.5): #95A5A6 (grey).
  - Strong negative (z < -1): #E74C3C (red).
- Tech row: green, grey, green.
- Healthcare row: grey, red, grey.
- Finance row: red, green, grey.
- Energy row: grey, grey, red.
- Each cell shows the z-score value (e.g., "+1.4," "-0.8").
- Label above: "cross-sector heatmap."

## Animation sequence
1. Left: company dots scatter, then flow into funnel, composite bar emerges (3s).
2. Center: mood index line draws left to right, mean line appears, regime change flag pops (3.5s).
3. Right: heatmap grid appears, cells fill in with colors row by row (3.5s).
4. Hold all three panels (2s).

## Palette
- Company dots: various (#4A90D9, #1ABC9C, #9B59B6, #F39C12)
- Funnel: #2C3E50 outline
- Composite bar: #4A90D9 to #27AE60 gradient
- Mood index line: #4A90D9
- Historical mean: #95A5A6 (dashed)
- Regime change marker: #F1C40F (gold)
- Heatmap positive: #27AE60 (green)
- Heatmap neutral: #95A5A6 (grey)
- Heatmap negative: #E74C3C (red)
- Background: #1A1A2E
