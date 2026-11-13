# B04 — Guidance Revision Predictor

## Composition type
Remotion

## Layout
Dark stage. Left: feature vector. Center: six model blocks. Right: comparison table.

## Elements

### Left: Feature Vector

#### Stacked bars
- Nine small horizontal bars stacked vertically, each labeled and colored:
  1. "hedging index" (#E74C3C).
  2. "mgmt confidence" (#27AE60).
  3. "specificity change" (#4A90D9).
  4. "CEO-CFO divergence" (#E67E22).
  5. "dodge score" (#E67E22).
  6. "market share shift" (#9B59B6).
  7. "fwd-looking delta" (#4A90D9).
  8. "sentiment delta" (#1ABC9C).
  9. "sector mood" (#F1C40F).
- Each bar has a different fill length representing the feature value.
- Label above: "feature vector."

### Center: Six Model Blocks

#### 2x3 grid
- Row 1: "logistic regression" (#4A90D9), "XGBoost" (#27AE60), "Random Forest" (#1ABC9C).
- Row 2: "LightGBM" (#F39C12), "MLP" (#9B59B6), "CatBoost" (#E74C3C).
- Each block is a small rounded rectangle with the model name.
- Arrows from the feature vector enter each block.

### Right: Comparison Table

#### Performance table
- Three columns: "model," "F1," "Brier."
- Six rows ranked by performance.
- Top row highlighted with gold (#F1C40F) border. Small badge: "primary."
- Second row with silver (#95A5A6) border. Small badge: "fallback."
- Remaining rows in default styling.
- Label above: "model comparison."

#### Evaluation badges
- Below the table: two small badges: "bootstrap CIs" and "permutation tests" in #95A5A6.

## Animation sequence
1. Feature vector bars appear, growing from left (2s).
2. Arrows extend from feature vector to model grid (1s).
3. Six model blocks appear in grid (2s).
4. Arrows from models converge to comparison table (1s).
5. Table rows fill in, top model highlighted gold (2.5s).
6. "primary" and "fallback" badges appear (1s).
7. Evaluation badges fade in below (1s).

## Palette
- Feature bars: various as listed
- Model blocks: #4A90D9, #27AE60, #1ABC9C, #F39C12, #9B59B6, #E74C3C
- Primary highlight: #F1C40F (gold)
- Fallback highlight: #95A5A6 (grey)
- Evaluation badges: #95A5A6
- Arrows: #95A5A6
- Background: #1A1A2E
