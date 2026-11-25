# B02 — What's Inside a Time Series

## Composition type
Remotion / Manim

## Layout
Dark stage. Top: raw time series. Below: three decomposed layers stacking vertically.

## Elements

### Raw time series (top)
- A single line chart — wavy with an upward drift and periodic spikes.
- Color: #3498DB (blue).
- Label: "raw series."

### Decomposition layers (below, stacked vertically)

#### Trend
- A smooth upward-sloping line.
- Color: #E67E22 (orange).
- Label: "trend — long-term direction."

#### Seasonality
- A repeating sine-like wave with consistent amplitude.
- Color: #27AE60 (green).
- Label: "seasonality — repeating cycles."

#### Residual
- An irregular, jittery line hovering around zero.
- Color: #95A5A6 (grey).
- Label: "residual — noise."

### Equation annotation
- Between raw and decomposed: "= trend + seasonality + residual."
- Plus signs between the three layers.
- Color: #EAEAEA.

## Animation sequence
1. Raw time series draws (2s).
2. "raw series" label (0.5s).
3. Raw line splits — trend peels downward as a smooth line (2s).
4. Seasonality peels out below trend as a wave (2s).
5. Residual appears at the bottom as the leftover jitter (1.5s).
6. Labels appear on each: trend, seasonality, residual (1.5s).
7. Equation annotation fades in (1.5s).

## Palette
- Raw series: #3498DB (blue)
- Trend: #E67E22 (orange)
- Seasonality: #27AE60 (green)
- Residual: #95A5A6 (grey)
- Equation: #EAEAEA
- Background: #1A1A2E
- Text: #EAEAEA
