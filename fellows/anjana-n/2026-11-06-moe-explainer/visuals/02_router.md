# B02 — The Router and the Experts

## Composition type
Remotion

## Layout
Dark stage. Left: router diamond. Right: eight expert blocks in a 2×4 grid. Token flows from left through router to selected experts.

## Elements

### Router
- A diamond shape labeled "router."
- Color: #F1C40F (gold) fill.
- Small text inside: "learned gating."

### Eight expert blocks
- Eight rounded rectangles in a 2×4 grid:
  - "expert 1" through "expert 8."
- Color: #555555 (dim grey) initially.

### Incoming token
- An orange (#E67E22) dot arriving from the left.
- Label: "token."

### Softmax bar chart
- Below the router, a small horizontal bar chart showing probability over 8 experts.
- Expert 3 and expert 7 have the tallest bars.
- Other bars are short.
- Label: "softmax probabilities."

### Routing arrows
- Two arrows from the router to expert 3 and expert 7.
- Those two experts light up blue (#3498DB).
- The remaining six stay dim grey (#555555).
- Arrow labels: probability weights (e.g., "0.62" and "0.38").

### Weighted sum
- Outputs from expert 3 and expert 7 merge into a single output node.
- Label: "weighted sum."
- Color: #3498DB (blue) with gold (#F1C40F) border.

## Animation sequence
1. Eight expert blocks appear in grid, all dim grey (1s).
2. Router diamond appears at left in gold (0.5s).
3. Token arrives from left (1s).
4. Softmax bar chart appears below router — bars animate (2s).
5. Two arrows extend to expert 3 and expert 7 — they light up blue (2s).
6. Weight labels appear on arrows (0.5s).
7. Outputs merge at weighted sum node (1.5s).
8. "8 experts, 2 active" label appears below (1s).

## Palette
- Router: #F1C40F (gold)
- Active experts: #3498DB (blue)
- Inactive experts: #555555 (dim grey)
- Token: #E67E22 (orange)
- Softmax bars: #3498DB (blue) for top 2, #555555 for rest
- Weighted sum: #3498DB border, #F1C40F accent
- Background: #1A1A2E
- Text: #EAEAEA
