# B03 — When to Abstain

## Composition type
Remotion

## Layout
Dark stage. Two prediction cards side by side. Coverage-accuracy bar below.

## Elements

### Left card: Confident prediction
- A rounded rectangle with a green (#27AE60) border.
- Inside:
  - Probability: "72%."
  - Narrow confidence band (blue #3498DB, tight).
  - Variance: "low."
  - Ensemble: "5/6 agree."
- Bottom: green checkmark and label "predict."
- Color: green (#27AE60) glow.

### Right card: Uncertain prediction — abstained
- A rounded rectangle with a red (#E74C3C) border.
- Inside:
  - Probability: "58%."
  - Wide confidence band (blue #3498DB, very wide, spanning 35%–81%).
  - Variance: "high."
  - Ensemble: "3/6 agree."
- Bottom: red X icon and label "abstain — uncertainty too high."
- Color: red (#E74C3C) glow.
- Card slightly faded or desaturated compared to the left card.

### Coverage-accuracy bar (below both cards)
- A horizontal bar split into two segments:
  - Left segment (88%): green (#27AE60), labeled "predicted — 88%."
  - Right segment (12%): red (#E74C3C), labeled "abstained — 12%."
- Below the bar: "+8% accuracy on retained predictions."
- Color: #F1C40F (gold) for the accuracy label.

## Animation sequence
1. Left card appears with tight band, green checkmark (2s).
2. Right card appears with wide band, metrics diverging (2s).
3. Red abstention flag drops onto right card (1s).
4. Both cards settle side by side (0.5s).
5. Coverage-accuracy bar fills left to right below (2s).
6. "+8% accuracy" label appears in gold (1s).

## Palette
- Confident card: #27AE60 (green) border
- Abstained card: #E74C3C (red) border
- Confidence bands: #3498DB (blue)
- Checkmark: #27AE60 (green)
- Abstention X: #E74C3C (red)
- Coverage bar: #27AE60 (green) / #E74C3C (red)
- Accuracy label: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
