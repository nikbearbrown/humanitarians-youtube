# B02 — Consensus Integration

## Composition type
Remotion

## Layout
Dark stage. Split view with extracted guidance on the left, consensus estimate on the right, and delta measurement in the center.

## Elements

### Left panel: Extracted guidance
- A signal badge showing direction "raised" and a guidance value.
- Label: "extracted guidance."
- Blue fill (#4A90D9).

### Right panel: Consensus estimate
- A similar badge showing the analyst consensus estimate value.
- Label: "consensus estimate."
- Warm grey fill (#7F8C8D).

### Delta measurement
- An animated horizontal gap measurement bar between the two values.
- Label: "delta" with the computed difference.
- Color: gold (#F1C40F).

### Feature vector
- The delta value animates downward, sliding into a vertical feature vector (column of cells).
- The vector feeds into the prediction model (gold node at bottom).

## Animation sequence
1. Left badge (extracted guidance) fades in.
2. Right badge (consensus) fades in.
3. Gap measurement bar stretches between them, delta value appears.
4. Delta slides down into the feature vector.
5. Feature vector lights up, arrow points to the gold prediction node.

## Palette
- Extracted guidance: #4A90D9 (blue)
- Consensus: #7F8C8D (warm grey)
- Delta: #F1C40F (gold)
- Prediction node: #F1C40F (gold)
- Background: #1A1A2E
