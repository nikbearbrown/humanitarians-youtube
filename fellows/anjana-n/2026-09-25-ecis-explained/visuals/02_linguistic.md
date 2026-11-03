# B02 — Linguistic Analytics

## Composition type
Remotion

## Layout
Dark stage. Three horizontal gauges stacked vertically, feeding into a feature vector.

## Elements

### Top gauge: Readability
- Horizontal bar gauge labeled "readability."
- Left end: "simple." Right end: "complex."
- Needle swings and settles at a position (e.g., 70% toward complex).
- Color gradient: green (simple) to orange (complex).

### Middle gauge: Hedging Index
- Horizontal bar gauge labeled "hedging index."
- Left end: "definitive." Right end: "hedging."
- Needle settles at a moderate position.
- Color gradient: blue (definitive) to amber (hedging).

### Bottom gauge: Tone Shift
- A dual-bar comparison showing Q3 sentiment distribution vs Q4.
- Label: "tone shift."
- Q3 bar: mostly neutral (grey). Q4 bar: shifted toward positive (green).
- A delta arrow between them labeled with the shift magnitude.

### Feature vector (right side)
- Three values from the gauges feed into a small vertical column of cells.
- The column connects to the gold prediction node.
- Label: "linguistic features."

## Animation sequence
1. Top gauge appears and needle animates (2s).
2. Middle gauge appears and needle animates (2s).
3. Bottom gauge appears, Q3 and Q4 bars animate side by side (2s).
4. Lines from each gauge connect to the feature vector on the right (2s).
5. Feature vector glows, arrow to prediction node (1s).

## Palette
- Readability gradient: #27AE60 to #E67E22
- Hedging gradient: #4A90D9 to #F1C40F
- Q3 sentiment: #95A5A6 (grey)
- Q4 sentiment: #27AE60 (green)
- Feature vector: #F1C40F (gold)
- Background: #1A1A2E
