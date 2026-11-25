# B05 — Why It Works

## Composition type
Remotion

## Layout
Dark stage. A parameter-vs-compute chart showing dense models plateauing and MoE breaking through. Title card at the end.

## Elements

### Parameter-compute chart

#### Axes
- X-axis: "total parameters" — labeled 10B, 50B, 100B, 150B.
- Y-axis: "performance" — unlabeled, just an upward arrow.
- Color: #EAEAEA.

#### Dense model curve
- A curve rising steeply at first, then flattening.
- Color: #9B59B6 (purple).
- Label at the plateau: "dense — compute wall."
- A data point at 70B labeled "dense 70B."

#### MoE model curve
- A curve that continues rising past where the dense curve flattens.
- Color: #3498DB (blue).
- Arrow extending further right.
- A data point at 141B total labeled "MoE 8×22B (141B total)."
- Annotation below that point: "~39B active per token."

### Cost comparison callout
- A small box between the two data points.
- "≈ half the inference cost."
- Arrow from MoE point down to dense performance level, showing it matches or exceeds.
- Color: #F1C40F (gold).

### Title card
- Chart fades.
- Centered text: "Mixture of Experts."
- Sub-text: "Massive Capacity, Sparse Compute."
- Color: #EAEAEA for title, #F1C40F (gold) for sub-text.
- Fade to dark.

## Animation sequence
1. Axes appear (0.5s).
2. Dense curve draws from left to right, flattening (2.5s).
3. "dense 70B" data point and "compute wall" label (1s).
4. MoE curve draws, continuing upward past the plateau (2.5s).
5. "MoE 8×22B" data point with "~39B active" annotation (1.5s).
6. Cost comparison callout appears in gold (1.5s).
7. Chart fades (0.5s).
8. Title card: "Mixture of Experts" (1.5s).
9. Sub-text: "Massive Capacity, Sparse Compute" in gold (1s).
10. Fade to dark (0.5s).

## Palette
- Dense curve: #9B59B6 (purple)
- MoE curve: #3498DB (blue)
- Cost callout: #F1C40F (gold)
- Axes: #EAEAEA
- Title: #EAEAEA
- Sub-text: #F1C40F (gold)
- Background: #1A1A2E
