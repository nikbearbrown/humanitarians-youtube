# B04 — Pre-Signal Drift

## Composition type
Remotion

## Layout
Dark stage. A stylized price chart centered on the earnings call date.

## Elements

### Price chart
- A smooth line chart showing stock price over ~30 days.
- A vertical dashed line in the center marks the earnings call date, labeled "earnings call."

### Pre-call window (left of the line)
- A shaded amber region covering the 10 trading days before the call.
- The price line trends upward within this region.
- Label: "already moving (+5%)" in amber (#F1C40F).

### Post-call window (right of the line)
- The price line continues upward.
- Label: "signal confirmed (+3%)" in green (#27AE60).

### Verdict badge
- Below the chart, a badge: "correct but already priced in."
- Badge fill: amber with white text.

## Animation sequence
1. Price chart line draws from left to right (3s).
2. Vertical dashed line appears at the earnings call date (0.5s).
3. Pre-call shaded region highlights, "+5%" label fades in (2s).
4. Post-call "+3%" label fades in (1.5s).
5. Verdict badge slides up from below (1.5s).

## Palette
- Price line: #EAEAEA (white)
- Pre-call region: #F1C40F at 20% opacity (amber)
- Pre-call label: #F1C40F (amber)
- Post-call label: #27AE60 (green)
- Earnings call line: #E74C3C (red, dashed)
- Verdict badge: #F1C40F fill, #1A1A2E text
- Background: #1A1A2E
