# B04 — Forecasting Approaches

## Composition type
Remotion

## Layout
Dark stage. Three columns — one per method. Tradeoff bars below. Gold forecast line extending from a time series.

## Elements

### Time series baseline (top, spanning all columns)
- A short time series line ending at a "now" marker.
- Color: #3498DB (blue).
- A gold (#F1C40F) dashed line extends forward from "now" — the forecast.

### Column 1: ARIMA (left)
- A compact equation: "ARIMA(p, d, q)."
- Small icon: a regression line with lag terms.
- Label: "classical statistics."
- Color: #E67E22 (orange) accent.

### Column 2: Prophet (center)
- A small decomposition diagram: trend line + seasonal wave + holiday spikes.
- Label: "structured decomposition."
- Color: #27AE60 (green) accent.

### Column 3: LSTM (right)
- Three unrolled recurrent cells connected by arrows.
- Label: "recurrent neural network."
- Color: #9B59B6 (purple) accent.

### Tradeoff bars (below all three columns)

#### Interpretability bar
- A gradient bar: high (left/orange) → low (right/purple).
- Label: "interpretability."
- ARIMA marked high, Prophet mid, LSTM low.

#### Data requirement bar
- A gradient bar: low (left/orange) → high (right/purple).
- Label: "data needed."
- ARIMA marked low, Prophet mid, LSTM high.

### Bottom annotation
- "No single method wins everywhere."
- Color: #EAEAEA.

## Animation sequence
1. Time series draws with "now" marker (1.5s).
2. Gold forecast dashed line extends (1s).
3. ARIMA column appears — equation and label (1.5s).
4. Prophet column appears — decomposition diagram (1.5s).
5. LSTM column appears — recurrent cells (1.5s).
6. Interpretability bar fills (1.5s).
7. Data requirement bar fills (1.5s).
8. Bottom annotation (1s).

## Palette
- Time series: #3498DB (blue)
- Forecast: #F1C40F (gold, dashed)
- ARIMA: #E67E22 (orange)
- Prophet: #27AE60 (green)
- LSTM: #9B59B6 (purple)
- Tradeoff bars: gradient from orange → purple
- Background: #1A1A2E
- Text: #EAEAEA
