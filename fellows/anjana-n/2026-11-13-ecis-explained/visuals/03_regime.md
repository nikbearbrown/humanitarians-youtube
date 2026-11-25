# B03 — Market Regime Detection

## Composition type
Remotion

## Layout
Dark stage. Top: HMM state diagram. Middle: quarterly timeline with colored regime zones. Bottom: regime label feeding into prediction.

## Elements

### HMM state diagram (top)
- Three circular nodes arranged in a triangle:
  - "bullish" — #27AE60 (green).
  - "bearish" — #E74C3C (red).
  - "transitional" — #F39C12 (amber).
- Curved transition arrows between all pairs with small probability labels.
- Label above: "Hidden Markov Model."

### Quarterly timeline (middle)
- A horizontal bar divided into quarters (Q1 through Q8).
- Colored zones:
  - Q1–Q3: green (#27AE60) — bullish.
  - Q4–Q5: amber (#F39C12) — transitional.
  - Q6–Q8: red (#E74C3C) — bearish.
- Small labels above each zone: "bullish," "transitional," "bearish."

### Regime label drop (bottom)
- Arrows dropping from the timeline into a prediction layer block.
- Label: "regime as context feature."
- Color: #F1C40F (gold) for the prediction layer.

### Interpretation annotation
- Text at bottom: "same signal, different meaning depending on the regime."
- Color: #EAEAEA.

## Animation sequence
1. HMM state diagram appears — three nodes with transitions (2s).
2. Timeline appears below with quarters (1s).
3. Regime colors fill in left to right: green → amber → red (3s).
4. Arrows drop from timeline into prediction layer (1.5s).
5. "regime as context feature" label (0.5s).
6. Interpretation annotation fades in (1s).

## Palette
- Bullish: #27AE60 (green)
- Bearish: #E74C3C (red)
- Transitional: #F39C12 (amber)
- HMM label: #EAEAEA
- Prediction layer: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
