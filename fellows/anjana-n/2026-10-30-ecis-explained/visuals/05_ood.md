# B05 — Out-of-Distribution Detection

## Composition type
Remotion

## Layout
Dark stage. Center: 2D scatter plot with training cluster and outliers. Right: confidence penalty scale.

## Elements

### Scatter plot

#### Training distribution cluster
- A dense cluster of small dots in the center of the plot.
- Color: #4A90D9 (blue), slightly varied opacity.
- ~40 dots clustered together.

#### Boundary ellipse
- A dashed ellipse enclosing the training cluster.
- Label on the boundary: "Mahalanobis boundary."
- Color: #95A5A6 (grey dashed).

#### Isolation forest label
- A small badge near the boundary: "+ isolation forest."
- Color: #95A5A6 (grey).

#### Outlier dots (outside the ellipse)
1. **Marginal outlier** — just outside the ellipse.
   - Color: #E67E22 (orange).
   - Small label: "new CEO style."
   - Penalty tag: "−5%."
2. **Moderate outlier** — further from the ellipse.
   - Color: #E67E22 (orange), darker.
   - Small label: "unusual structure."
   - Penalty tag: "−15%."
3. **Extreme outlier** — far from the ellipse.
   - Color: #E74C3C (red).
   - Small label: "crisis call."
   - Penalty tag: "−40%."

#### Axes
- Faint axes labeled "feature dimension 1" and "feature dimension 2."
- Color: #95A5A6 (grey, faint).

### Right: Confidence Penalty Scale

#### Vertical scale
- A vertical bar showing penalty magnitude.
- Top: "0% (in-distribution)" — #27AE60 (green).
- Middle: "−15%" — #E67E22 (orange).
- Bottom: "−40%+" — #E74C3C (red).
- Gradient from green to red.

#### Connecting arrows
- Dashed arrows from each outlier dot to its position on the penalty scale.

## Animation sequence
1. Training cluster dots appear (1.5s).
2. Boundary ellipse draws around cluster (1s).
3. "Mahalanobis boundary" and "isolation forest" labels fade in (0.5s).
4. Marginal outlier appears with "−5%" tag (1s).
5. Moderate outlier appears with "−15%" tag (1s).
6. Extreme outlier appears with "−40%" tag (1s).
7. Penalty scale appears on right (1s).
8. Dashed arrows connect outliers to scale positions (1s).

## Palette
- Training cluster: #4A90D9 (blue)
- Boundary ellipse: #95A5A6 (grey dashed)
- Marginal outlier: #E67E22 (orange)
- Moderate outlier: #E67E22 (orange, darker)
- Extreme outlier: #E74C3C (red)
- In-distribution: #27AE60 (green)
- Penalty scale gradient: #27AE60 → #E67E22 → #E74C3C
- Background: #1A1A2E
- Text: #EAEAEA
