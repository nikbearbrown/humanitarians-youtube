# B01 — Why One GPU Isn't Enough

## Composition type
Remotion

## Layout
Dark stage. Left: single GPU with memory overflow. Right: four GPUs with strategy question.

## Elements

### Left: Single GPU memory breakdown

#### GPU card
- A rounded rectangle labeled "GPU — 80 GB."
- Color: #4A90D9 (blue) border.

#### Memory bars (stacked vertically inside the GPU)
- Bar 1: "weights — 28 GB" — #9B59B6 (purple).
- Bar 2: "optimizer states — 56 GB" — #E67E22 (orange).
- Bar 3: "gradients — 28 GB" — #E67E22 (orange, lighter).
- Bar 4: "activations — variable" — #1ABC9C (teal).
- Total label: "> 100 GB."

#### Overflow
- Bars 3 and 4 extend beyond the GPU card boundary.
- The overflow region is tinted #E74C3C (red) with a dashed border.
- Label: "exceeds 80 GB."

### Right: Four GPUs with question

#### Four GPU cards
- Four smaller GPU rectangles in a row.
- Color: #4A90D9 (blue) border.
- The model is shown as a distributed element across them (faint, unresolved).

#### Strategy question
- Three labels with question marks between them:
  - "data parallel?"
  - "model parallel?"
  - "both?"
- Color: #F1C40F (gold) text.

## Animation sequence
1. Single GPU card appears (0.5s).
2. Memory bars stack up inside: weights, optimizer, gradients (2.5s).
3. Activations bar pushes beyond the card boundary (1s).
4. Overflow region highlights red with "exceeds 80 GB" (1s).
5. Four GPU cards appear on the right (1s).
6. Three strategy labels appear with question marks (1.5s).
7. Labels pulse gold (0.5s).

## Palette
- GPU border: #4A90D9 (blue)
- Weights: #9B59B6 (purple)
- Optimizer/gradients: #E67E22 (orange)
- Activations: #1ABC9C (teal)
- Overflow: #E74C3C (red)
- Strategy labels: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
