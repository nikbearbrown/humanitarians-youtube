# B01 — The Bottleneck

## Elements

### Neural network layer
- Left: a vertical column of 4 circles representing the input vector. Each circle contains a small number (e.g., 0.7, 0.3, 0.9, 0.1). Label: "inputs."
- Center: a 4x4 grid of small squares representing the weight matrix. Each cell has a tiny number. The entire grid glows gold (#F1C40F). Label: "weights."
- Right: a vertical column of 4 circles representing the output vector. Label: "outputs."
- Arrows from input column to weight matrix labeled "multiply."
- Arrows from weight matrix to output column labeled "add bias + activate."

### Operation counter
- Below the layer diagram, a rapidly ticking counter:
  - "matrix multiplications per training run:"
  - Number ticks up: "1B... 10B... 100B... 1T..."
  - Counter color: starts #EAEAEA (white), shifts to #F1C40F (gold) as numbers grow.

### Label
- Below the counter: "the dominant cost" in #F1C40F (gold).

## Animation sequence
1. Input vector appears (1s).
2. Weight matrix grid appears, glowing gold (1.5s).
3. "multiply" arrow draws, output vector appears (1.5s).
4. "add bias + activate" label fades in (1s).
5. Counter starts ticking rapidly (4s).
6. "the dominant cost" label fades in (2s).

## Palette
- Input/output circles: #4A90D9 (blue)
- Weight matrix: #F1C40F (gold)
- Arrows: #95A5A6 (grey)
- Counter: #EAEAEA transitioning to #F1C40F
- Label: #F1C40F (gold)
- Background: #1A1A2E
