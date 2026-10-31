# B02 — Confidence Calibration

## Composition type
Remotion

## Layout
Dark stage. Left: calibration curve (before/after). Right: ECE improvement table.

## Elements

### Left: Calibration Curve

#### Axes
- X-axis: "predicted probability" (0.0 to 1.0).
- Y-axis: "observed accuracy" (0.0 to 1.0).
- Color: #95A5A6 (grey).

#### Perfect calibration diagonal
- A dashed diagonal line from (0,0) to (1,1).
- Label: "perfect calibration."
- Color: #95A5A6 (grey dashed).

#### Before calibration curve
- A solid curve that deviates from the diagonal — overconfident at high values (curve bows below the diagonal on the right side).
- Color: #E74C3C (red).
- Label: "before."

#### After calibration curve
- A solid curve that closely follows the diagonal.
- Color: #4A90D9 (blue).
- Label: "after."

#### Decile dots
- Ten evenly spaced dots on the "after" curve, sitting near the diagonal.
- Color: #4A90D9 (blue).

### Right: ECE Improvement Table

#### Table
- Three columns: "signal type," "ECE before," "ECE after."
- Six rows:
  1. "hedging index" — 0.12 → 0.03. Green arrow ↓.
  2. "tone shift" — 0.09 → 0.02. Green arrow ↓.
  3. "confidence" — 0.15 → 0.04. Green arrow ↓.
  4. "dodge score" — 0.11 → 0.03. Green arrow ↓.
  5. "fwd-looking" — 0.08 → 0.02. Green arrow ↓.
  6. "mkt share" — 0.10 → 0.03. Green arrow ↓.
- Arrows color: #27AE60 (green).

#### Method labels
- Below the table, two small badges: "Platt scaling" and "isotonic regression."
- Color: #4A90D9 (blue).

## Animation sequence
1. Axes and diagonal appear (1s).
2. "Before" curve draws — deviating from diagonal (1.5s).
3. "After" curve draws — hugging diagonal (1.5s).
4. Decile dots appear on the after curve (0.5s).
5. ECE table fades in row by row with green arrows (3s).
6. Method badges appear (0.5s).

## Palette
- Before curve: #E74C3C (red)
- After curve: #4A90D9 (blue)
- Diagonal: #95A5A6 (grey dashed)
- ECE improvement arrows: #27AE60 (green)
- Method badges: #4A90D9 (blue)
- Background: #1A1A2E
- Text: #EAEAEA
