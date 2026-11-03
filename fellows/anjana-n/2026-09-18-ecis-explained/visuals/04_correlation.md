# B04 — Cross-Company Correlation

## Composition type
Remotion

## Layout
Dark stage. Correlation heatmap with cluster highlighting and leading indicator animation.

## Elements

### Correlation heatmap
- Grid with rows and columns labeled Company A through Company H (anonymous).
- Cell shading: cool blue (#3498DB) for low correlation, warm orange (#E67E22) for high correlation, neutral grey for near-zero.
- Diagonal is always max (self-correlation).

### Co-moving cluster
- A bounding box highlights a 4x4 subgrid of companies (A, C, E, G) with high mutual correlation.
- Label: "co-moving cluster."

### Leading indicator animation
- Within the cluster, Company A pulses first (bright glow).
- After a beat (representing one quarter lag), Companies C, E, G pulse.
- A small arrow from A to the others labeled "leads by 1 quarter."

## Animation sequence
1. Heatmap grid appears, cells fill in with color from top-left to bottom-right.
2. High-correlation cluster highlights with bounding box (2s).
3. Company A within the cluster pulses bright gold.
4. Quarter-lag beat, then C, E, G pulse in response.
5. "leads by 1 quarter" label and arrows fade in.

## Palette
- Low correlation: #3498DB (blue)
- High correlation: #E67E22 (orange)
- Cluster border: #F1C40F (gold)
- Leading indicator pulse: #F1C40F (gold)
- Labels: #EAEAEA
- Background: #1A1A2E
