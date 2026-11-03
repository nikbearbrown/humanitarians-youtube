# B05 — Reaction Windows

## Layout
Full-width chart area with three cumulative abnormal return curves.

## Elements

### Chart axes

#### X-axis
- Label: "days after earnings call."
- Tick marks at: 0, 1, 2, 5, 10, 30.
- A vertical dashed line at day 0 labeled "earnings call" in #95A5A6 (grey).

#### Y-axis
- Label: "cumulative abnormal return (%)."
- Range: -1% to +4%.
- Gridlines at each 1% increment, very subtle (#2C3E50).

### Three reaction curves

#### Curve 1: Immediate Pricing (top)
- Color: #4A90D9 (blue).
- Sharp jump from 0% to ~3% between day 0 and day 1.
- Then flat line at ~3% from day 1 to day 30.
- Small label at right end: "immediate pricing."

#### Curve 2: Continued Drift (middle)
- Color: #27AE60 (green).
- Moderate jump from 0% to ~1.5% at day 0–1.
- Then steady upward slope from 1.5% to ~3.5% by day 30.
- Small label at right end: "continued drift."

#### Curve 3: Mean Reversion (bottom)
- Color: #E74C3C (red).
- Sharp jump from 0% to ~2.5% at day 0–1.
- Then curves downward, settling at ~0.5% by day 30.
- Small label at right end: "mean reversion."

### Filter toggle
- Top-right corner: a small pill-shaped toggle showing "confidence tier: high."
- Toggle color: #F1C40F (gold) fill.

### Chart label
- Centered below chart: "reaction window analysis."

## Animation sequence
1. Axes draw: x-axis with tick marks, y-axis with gridlines (1s).
2. Day-0 dashed line appears with "earnings call" label (0.5s).
3. Blue "immediate pricing" curve draws left to right (2s).
4. Green "continued drift" curve draws (2s).
5. Red "mean reversion" curve draws (2s).
6. Curve labels appear at right ends (1s).
7. Confidence tier filter toggle fades in (0.5s).
8. "reaction window analysis" label fades in (1s).

## Palette
- Immediate pricing curve: #4A90D9 (blue)
- Continued drift curve: #27AE60 (green)
- Mean reversion curve: #E74C3C (red)
- Earnings call line: #95A5A6 (grey, dashed)
- Gridlines: #2C3E50
- Filter toggle: #F1C40F (gold)
- Axis labels: #EAEAEA
- Background: #1A1A2E
