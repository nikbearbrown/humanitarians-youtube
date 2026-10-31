# B02 — Data Parallelism

## Composition type
Remotion

## Layout
Dark stage. Four GPU nodes in a row, each with a model copy and data batch. Gradient convergence below.

## Elements

### Four GPU nodes (horizontal row)

#### Each GPU contains:
- A purple (#9B59B6) block labeled "model copy."
- All four model blocks are identical in size and shape.

#### Data batches above each GPU
- Four mini-batch blocks, each a slightly different shade of green (#27AE60 variations):
  - GPU 1: "batch 1."
  - GPU 2: "batch 2."
  - GPU 3: "batch 3."
  - GPU 4: "batch 4."
- Arrows from each batch into its GPU.

#### Forward/backward arrows
- Inside each GPU, small internal arrows: "fwd →" and "← bwd."
- Color: #EAEAEA (faint).

### Gradient convergence

#### Gradient arrows
- From each GPU, an orange (#E67E22) arrow labeled "∇" points downward to a central node.

#### Average node
- A circle labeled "average."
- Color: #F1C40F (gold).

#### Return arrows
- From the average node, four gold (#F1C40F) arrows return to each GPU.
- Label on return arrows: "synchronized update."

### Timeline bar
- Below everything, a horizontal bar.
- Label: "4× data throughput."
- Four segments, each colored to match a GPU's batch.
- Color: #27AE60 (green) shades.

## Animation sequence
1. Four GPU nodes appear with model copies (1.5s).
2. Four different-colored batches drop into their GPUs (1.5s).
3. Forward/backward arrows animate inside each GPU simultaneously (1.5s).
4. Orange gradient arrows emerge from all four GPUs (1s).
5. Arrows converge at the average node (1s).
6. Gold return arrows flow back to all GPUs (1.5s).
7. Timeline bar fills: "4× data throughput" (1s).

## Palette
- GPU nodes: #4A90D9 (blue) border
- Model copies: #9B59B6 (purple)
- Data batches: #27AE60 (green, varied shades)
- Gradient arrows: #E67E22 (orange)
- Average node: #F1C40F (gold)
- Return arrows: #F1C40F (gold)
- Timeline: #27AE60 (green)
- Background: #1A1A2E
- Text: #EAEAEA
