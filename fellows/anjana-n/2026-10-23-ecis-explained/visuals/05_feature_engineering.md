# B05 — Feature Engineering

## Composition type
Remotion

## Layout
Dark stage. Three sections left to right: feature selection list, interaction Venn diagram, embedding drift chart.

## Elements

### Left: Feature Selection

#### Ranked feature list
- Ten rows in a vertical list, each a small bar:
  - Top 6 rows: green (#27AE60) bar, label "keep."
  - Rows 7–8: yellow (#F1C40F) bar, label "monitor."
  - Rows 9–10: red (#E74C3C) bar, label "drop."
- Feature names beside each row (abbreviated): "hedging idx," "dodge score," "tone shift," "fwd-looking," "confidence," "mkt share," "specificity Δ," "sarcasm freq," "metaphor ratio," "formatting score."

#### Three method labels
- Below the list, three small badges: "RFE," "permutation," "LASSO."
- Color: #95A5A6 (grey).

#### Label above: "automated feature selection."

### Center: Feature Interaction

#### Three overlapping circles (Venn)
- Circle 1: "dodge score" — #E74C3C (red), semi-transparent.
- Circle 2: "rising hedging" — #E67E22 (orange), semi-transparent.
- Circle 3: "defensive language" — #9B59B6 (purple), semi-transparent.

#### Intersection
- Center overlap highlighted in #F1C40F (gold).
- Label: "interaction feature."
- Small text below: "synergy > individual signals."

### Right: Embedding Drift

#### Time-series chart
- X-axis: quarters (Q1 through Q6).
- Y-axis: "cosine distance from centroid" (0.00 to 0.15).
- Line plot showing drift values per quarter.
- Most quarters below 0.05.
- One quarter (Q5) spikes to ~0.12.

#### Threshold line
- Horizontal red dashed line at 0.10.
- Label: "PSI > 0.1 — retrain flag."

#### Alert flag
- At Q5, a small red flag icon with "⚠ drift detected."

#### Label above: "embedding drift."

## Animation sequence
1. Feature list appears, bars growing from left (2s).
2. "keep/monitor/drop" labels color-code the rows (1s).
3. Three method badges fade in (0.5s).
4. Venn circles appear, overlapping (1.5s).
5. Intersection highlights gold with label (1s).
6. Embedding drift chart draws: line plots quarter by quarter (2s).
7. Threshold line appears, Q5 flag triggers (1s).

## Palette
- Keep: #27AE60 (green)
- Monitor: #F1C40F (gold)
- Drop: #E74C3C (red)
- Dodge score circle: #E74C3C (red)
- Hedging circle: #E67E22 (orange)
- Defensive language circle: #9B59B6 (purple)
- Interaction highlight: #F1C40F (gold)
- Drift line: #4A90D9 (blue)
- Drift threshold: #E74C3C (red dashed)
- Method badges: #95A5A6 (grey)
- Background: #1A1A2E
- Text: #EAEAEA
