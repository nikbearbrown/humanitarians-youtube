# B03 — Querying by Distance

## Composition type
Remotion

## Layout
Dark stage. Same vector space from B02, now with a query dot and ranked results.

## Elements

### Query dot
- A gold dot (#F1C40F) appears in the upper right area, labeled "query: strong revenue growth."

### Distance rings
- Concentric circles radiate outward from the query dot like ripples.
- Inner ring is bright, outer rings fade.

### Nearest neighbor highlights
- First nearest: "quarterly revenue rose" glows bright (white outline). Rank #1.
- Second nearest: "sales beat expectations" glows medium. Rank #2.
- Third nearest: "exceeded guidance" glows softer. Rank #3.
- Far-away dots (negative cluster) stay dim and unhighlighted.

### Results list (right side)
- A ranked list builds vertically:
  - #1: "quarterly revenue rose" — 0.94
  - #2: "sales beat expectations" — 0.89
  - #3: "exceeded guidance" — 0.83
- Each entry appears as its corresponding dot highlights.

## Animation sequence
1. Query dot drops in with a pulse (1s).
2. Distance rings ripple outward (1.5s).
3. First nearest dot highlights, #1 result appears on right (1.5s).
4. Second nearest highlights, #2 appears (1.5s).
5. Third nearest highlights, #3 appears (1.5s).
6. Far-away dots visibly stay dim (1s).

## Palette
- Query dot: #F1C40F (gold)
- Distance rings: #F1C40F at decreasing opacity
- Highlighted dots: #EAEAEA (white glow)
- Results scores: #27AE60 (green)
- Dim dots: #3A3A4E (dark grey)
- Background: #1A1A2E
