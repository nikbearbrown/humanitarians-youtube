# B04 — Signal Value

## Layout
Two panels: feature importance ranking (left), surprise score matrix (right).

## Elements

### Left panel: Signal-to-Price Feature Importance

#### Ranked horizontal bar chart
- Four horizontal bars, sorted by length (longest at top):
  1. "tone shift magnitude" — longest bar, #F1C40F (gold). Small label: "r = 0.34."
  2. "confidence level" — medium bar, #4A90D9 (blue). Label: "r = 0.28."
  3. "hedging index" — medium bar, #27AE60 (green). Label: "r = 0.22."
  4. "direction signal" — shorter bar, #9B59B6 (purple). Label: "r = 0.15."
- Each bar has three small dots at its right end representing time horizons:
  - Filled dot = significant at that horizon.
  - Empty dot = not significant.
  - Labeled "1d · 5d · 30d" above the dot row.
- Label above: "feature importance (signal → price)."

### Right panel: Surprise Score Matrix

#### 2x2 grid
- Rows labeled on left: "NLP: raised" (top), "NLP: lowered" (bottom).
- Columns labeled on top: "consensus: raised" (left), "consensus: lowered" (right).
- Four cells with counts:
  - Top-left (NLP raised, consensus raised): "142" — grey (#95A5A6). Label: "agreement."
  - Top-right (NLP raised, consensus lowered): "23" — gold (#F1C40F), glowing. Label: "model saw it first."
  - Bottom-left (NLP lowered, consensus raised): "18" — #E67E22 (orange). Label: "model disagrees."
  - Bottom-right (NLP lowered, consensus lowered): "117" — grey (#95A5A6). Label: "agreement."

#### Highlight
- The top-right "model saw it first" cell has a thicker gold border and a subtle radial glow.
- A small star icon beside it.

#### Badge
- Below the matrix: "surprise score analytics."

## Animation sequence
1. Left: bars grow from left to right, top to bottom (3s).
2. Correlation labels and horizon dots fade in (1.5s).
3. Right: 2x2 grid appears (0.5s).
4. Cells fill with counts one by one (2s).
5. Top-right cell glows gold, "model saw it first" label appears (2s).
6. "surprise score analytics" badge fades in (1s).

## Palette
- Tone shift bar: #F1C40F (gold)
- Confidence bar: #4A90D9 (blue)
- Hedging bar: #27AE60 (green)
- Direction bar: #9B59B6 (purple)
- Agreement cells: #95A5A6 (grey)
- "Model saw it first" cell: #F1C40F (gold, glowing)
- "Model disagrees" cell: #E67E22 (orange)
- Horizon dots: #EAEAEA (filled), #3A3A4E (empty)
- Background: #1A1A2E
