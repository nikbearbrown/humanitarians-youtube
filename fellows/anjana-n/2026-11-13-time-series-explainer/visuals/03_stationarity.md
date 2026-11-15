# B03 — Stationarity

## Composition type
Remotion / Manim

## Layout
Dark stage. Two time series side by side. Differencing arrow between them.

## Elements

### Left: Non-stationary series
- A line chart trending upward with widening variance.
- Color: #E74C3C (red) line.
- A dashed horizontal mean line that shifts upward over time (three positions, each higher).
- Label: "non-stationary — mean drifts."
- Variance cone widens as the series progresses.

### Right: Stationary series
- A line chart oscillating around a flat constant mean.
- Color: #1ABC9C (teal) line.
- A dashed horizontal mean line that stays perfectly flat.
- Consistent variance throughout.
- Label: "stationary — stable mean & variance."

### Differencing arrow (between the two)
- A curved arrow from the non-stationary series to the stationary one.
- Label on arrow: "differencing — subtract previous value."
- Small formula: "y'(t) = y(t) − y(t−1)."
- Color: #F1C40F (gold) arrow.

### Bottom annotation
- "Make it stationary first, then fit the model."
- Color: #EAEAEA.

## Animation sequence
1. Non-stationary series draws — mean line drifts up (2.5s).
2. "non-stationary — mean drifts" label (0.5s).
3. Differencing arrow appears with formula (2s).
4. Stationary series draws — flat mean line (2.5s).
5. "stationary — stable mean & variance" label (0.5s).
6. Bottom annotation fades in (1.5s).

## Palette
- Non-stationary: #E74C3C (red)
- Stationary: #1ABC9C (teal)
- Mean lines: #EAEAEA (dashed)
- Differencing arrow: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
