# B03 — Management Behavior

## Layout
Split view: confidence gauge (left), CEO-CFO divergence (right).

## Elements

### Left side: Management Confidence Score

#### Vertical gauge
- A tall vertical gauge styled like a thermometer, scaled 0–100.
- Fill level at 72, color gradient: red at bottom (#E74C3C), gold in middle (#F1C40F), green at top (#27AE60).
- Marker at 72.
- Large number "72" beside the marker.

#### Input arrows
- Four thin arrows entering the gauge from the left, each labeled:
  - "hedging (inv)" — #E74C3C (red, inverted).
  - "fwd-looking" — #4A90D9 (blue).
  - "definitive" — #27AE60 (green).
  - "specificity" — #F1C40F (gold).

#### Trend sparkline
- Below the gauge: a small sparkline across 4 quarters (Q1–Q4).
- The line shows 68 → 71 → 72 → 72. Slight upward trend.
- Label: "confidence trend."

### Right side: CEO vs CFO Divergence

#### Speaker icons
- Two simplified person icons side by side.
- Left icon labeled "CEO," right icon labeled "CFO."

#### Horizontal score bars
- Below CEO icon: a horizontal bar filled to 78%. Color: #27AE60 (green). Label: "78."
- Below CFO icon: a horizontal bar filled to 51%. Color: #E67E22 (orange). Label: "51."

#### Divergence highlight
- A red bracket (#E74C3C) spanning the gap between the right edge of the CFO bar and the right edge of the CEO bar.
- Inside the bracket: "27 pts."
- A small alert triangle icon (#E74C3C) pulses beside the bracket.
- Label below: "divergence flagged."

#### Historical context
- Small text below: "threshold: >15 pts."

## Animation sequence
1. Left: gauge appears, fill animates from 0 to 72 (2s).
2. Input arrows draw in one by one with labels (2s).
3. Sparkline draws below (1s).
4. Right: CEO and CFO icons appear (0.5s).
5. Score bars grow: CEO to 78, CFO to 51 (1.5s).
6. Red bracket and "27 pts" appear, alert icon pulses (2s).
7. "divergence flagged" label fades in (1s).

## Palette
- Gauge fill: gradient #E74C3C → #F1C40F → #27AE60
- Hedging input: #E74C3C (red)
- Forward-looking input: #4A90D9 (blue)
- Definitive input: #27AE60 (green)
- Specificity input: #F1C40F (gold)
- CEO bar: #27AE60 (green)
- CFO bar: #E67E22 (orange)
- Divergence bracket: #E74C3C (red)
- Alert icon: #E74C3C (red)
- Sparkline: #4A90D9 (blue)
- Background: #1A1A2E
