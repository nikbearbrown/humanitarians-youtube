# B03 — Data Quality

## Composition type
Remotion

## Layout
Dark stage. Three columns: data profiling (left), lineage chain (center), completeness monitor (right).

## Elements

### Left column: Data Profiling
- A small card with three mini-visualizations stacked:
  - A mini histogram showing confidence score distribution (5-6 bars, roughly bell-shaped).
  - A text line: "missing values: 2 / 850."
  - A text line with a warning icon: "outliers: 1 detected (IQR method)."
- Label above: "data profiling."
- The histogram bars are blue (#4A90D9), the outlier flag is orange (#E67E22).

### Center column: Data Lineage
- A vertical chain of 6 connected boxes, top to bottom:
  1. "raw transcript" (grey box).
  2. "cleaned text" (grey box).
  3. "chunk 47" (blue box).
  4. "FinBERT + LLM outputs" (purple box).
  5. "triangulated signal" (gold box).
  6. "validated signal" (green box).
- Thin arrows connecting each box downward.
- Label above: "data lineage."
- A dotted line traces the full path from top to bottom, glowing gold.

### Right column: Completeness Monitor
- A small grid table. Rows: Company A, B, C, D. Columns: consensus, prices, outcomes.
- Most cells have green checkmarks (#27AE60).
- Two cells marks (#E74C3C): Company B/consensus and Company D/outcomes.
- Label above: "completeness monitor."

## Animation sequence
1. Left column fades in: histogram draws, missing/outlier text appears (2.5s).
2. Center column: boxes appear top to bottom with connecting arrows (3s).
3. Gold trace line flows from top box to bottom box (1.5s).
4. Right column: grid appears, checks and X marks fill in (2s).

## Palette
- Profiling histogram: #4A90D9 (blue)
- Outlier flag: #E67E22 (orange)
- Lineage boxes: gradient from #95A5A6 (grey, raw) through #4A90D9 (blue) to #27AE60 (green, validated)
- Lineage trace: #F1C40F (gold)
- Completeness checks: #27AE60 (green)
- Completeness gaps: #E74C3C (red)
- Background: #1A1A2E
