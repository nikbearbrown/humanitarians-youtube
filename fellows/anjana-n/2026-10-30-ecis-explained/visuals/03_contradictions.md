# B03 — Signal Contradiction Detection

## Composition type
Remotion

## Layout
Dark stage. Center: earnings call card with signal bars and conflict lines. Below: interpretation branches.

## Elements

### Center: Earnings call card
- A rounded rectangle labeled "Company A — Q3 Call."
- Color: #EAEAEA border.

### Signal bars (extending from the card)
- Four horizontal signal bars extending right from the card:
  1. "bullish tone" — #27AE60 (green), strong fill.
  2. "rising hedging" — #E67E22 (orange), strong fill.
  3. "high confidence" — #4A90D9 (blue), strong fill.
  4. "high dodge score" — #E74C3C (red), strong fill.

### Conflict lines
- A red (#E74C3C) zigzag conflict line connecting "bullish tone" ↔ "rising hedging."
  - Small severity badge: "HIGH" in #E74C3C.
- A red zigzag conflict line connecting "high confidence" ↔ "high dodge score."
  - Small severity badge: "MED" in #F39C12 (amber).

### Conflict count
- Small counter near the card: "2 contradictions detected."
- Color: #E74C3C.

### Below: Interpretation branches

#### Diamond decision node
- Label: "what does this mean?"
- Color: #F1C40F (gold).

#### Three branches
1. "uncertainty" — #4A90D9 (blue). Small label: "genuine mixed signals."
2. "mixed outlook" — #E67E22 (orange). Small label: "positive on some metrics, negative on others."

## Animation sequence
1. Earnings call card appears (0.5s).
2. Four signal bars extend from the card (2s).
3. First conflict line zigzags between "bullish tone" and "rising hedging" with HIGH badge (1.5s).
4. Second conflict line zigzags between "high confidence" and "high dodge score" with MED badge (1.5s).
5. "2 contradictions detected" counter appears (0.5s).
6. Diamond decision node appears below (0.5s).
7. Three interpretation branches extend with labels (2s).

## Palette
- Bullish tone: #27AE60 (green)
- Rising hedging: #E67E22 (orange)
- High confidence: #4A90D9 (blue)
- High dodge score: #E74C3C (red)
- Conflict lines: #E74C3C (red)
- HIGH severity: #E74C3C (red)
- MED severity: #F39C12 (amber)
- Decision node: #F1C40F (gold)
- Uncertainty branch: #4A90D9 (blue)
- Mixed outlook branch: #E67E22 (orange)
=- Background: #1A1A2E
- Text: #EAEAEA
