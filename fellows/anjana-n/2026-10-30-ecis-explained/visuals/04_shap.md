# B04 — SHAP Explainability

## Composition type
Remotion

## Layout
Dark stage. Left: SHAP waterfall chart. Right: natural language explanation box. Arrow connecting them.

## Elements

### Left: SHAP Waterfall Chart

#### Base value line
- A vertical dashed line near the center of the chart.
- Label at top: "base value: 0.45."
- Color: #95A5A6 (grey).

#### Positive contribution bars (extending right from base)
- Bar 1: "hedging index +0.18" — #E74C3C (red), longest bar.
- Bar 2: "CEO-CFO divergence +0.12" — #E67E22 (orange).
- Bar 3: "dodge score +0.08" — #E74C3C (red, shorter).

#### Negative contribution bars (extending left from accumulated position)
- Bar 4: "confidence −0.05" — #4A90D9 (blue).
- Bar 5: "sector mood −0.03" — #4A90D9 (blue, shorter).

#### Final prediction
- A vertical line at the accumulated end position.
- Label: "prediction: 0.75."
- Color: #F1C40F (gold).

#### Chart label
- Below: "SHAP feature contributions."

### Connecting arrow
- A horizontal arrow from the waterfall chart to the explanation box.
- Label on arrow: "template generation."
- Color: #27AE60 (green).

### Right: Natural Language Explanation

#### Text box
- Rounded rectangle with readable text:
  - "Company A flagged: hedging rose 40% while CEO-CFO divergence hit a 4-quarter high and dodge score exceeded sector average."
- Color: #27AE60 (green) border.

#### Audit badge
- Small badge below: "stored for audit."
- Color: #95A5A6 (grey).

## Animation sequence
1. Base value line appears (0.5s).
2. Positive bars grow right from base: hedging, CEO-CFO, dodge (2.5s).
3. Negative bars grow left: confidence, sector mood (1.5s).
4. Final prediction line and label appear (1s).
5. Arrow draws to explanation box (0.5s).
6. Explanation text fades in (2s).
7. Audit badge appears (0.5s).

## Palette
- Positive contribution bars: #E74C3C (red), #E67E22 (orange)
- Negative contribution bars: #4A90D9 (blue)
- Base value: #95A5A6 (grey)
- Final prediction: #F1C40F (gold)
- Template arrow: #27AE60 (green)
- Explanation box: #27AE60 (green) border
- Audit badge: #95A5A6 (grey)
- Background: #1A1A2E
- Text: #EAEAEA
