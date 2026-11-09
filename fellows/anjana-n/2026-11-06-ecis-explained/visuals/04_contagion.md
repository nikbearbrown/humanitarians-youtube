# B04 — Cross-Company Contagion

## Composition type
Remotion

## Layout
Dark stage. Top: sector network graph with propagation animation. Bottom: supply chain link.

## Elements

### Sector network graph (top)
- Six company nodes arranged in a loose cluster:
  - "Company A" (center-left, larger — sector leader).
  - "Company B" through "Company F" (surrounding).
- Nodes are circles with labels inside.
- Color: #EAEAEA border initially, then change as contagion spreads.

### Contagion propagation
- Company A pulses green (#27AE60) first — small label: "hedging ↑."
- Directed arrows from Company A to Company B and Company C.
- Arrow label: "Q+1."
- Company B and C turn green (#27AE60).
- Arrows from B and C to Company D and E.
- Arrow label: "Q+2."
- Company D and E turn green (#27AE60).
- Company F remains grey — no contagion link.

### Granger causality annotation
- Small text near the arrows: "Granger causality."
- Subtle, not dominant.

### Supply chain link (bottom)
- Two nodes connected by a horizontal arrow:
  - Left node: "Supplier X" — #9B59B6 (purple) border.
  - Right node: "Customer Y" — #F39C12 (amber) border.
  - Arrow between them: labeled "language deterioration → 1–2 quarter lag."
  - Arrow color: #E74C3C (red).
- Small label below: "upstream signal → downstream early warning."

## Animation sequence
1. Six company nodes appear in cluster (1s).
2. Company A pulses green — "hedging ↑" (1.5s).
3. Arrows animate from A to B and C — "Q+1" — B and C turn green (2s).
4. Arrows animate from B/C to D and E — "Q+2" — D and E turn green (1.5s).
5. Supply chain link appears below (1.5s).
6. Red arrow animates from Supplier X to Customer Y (1.5s).
7. "upstream signal → downstream early warning" label appears (1s).

## Palette
- Company nodes (inactive): #EAEAEA border
- Company nodes (contagion): #27AE60 (green)
- Arrows (sector): #27AE60 (green)
- Supplier: #9B59B6 (purple)
- Customer: #F39C12 (amber)
- Supply chain arrow: #E74C3C (red)
- Background: #1A1A2E
- Text: #EAEAEA
