# B03 — All-Reduce: The Communication Pattern

## Composition type
Remotion

## Layout
Dark stage. Top: ring all-reduce diagram with four GPUs. Bottom: contrasted centralized pattern.

## Elements

### Top: Ring All-Reduce

#### Four GPUs in a ring
- Four GPU nodes arranged in a circle (top, right, bottom, left).
- Color: #4A90D9 (blue) border.
- Each GPU labeled "GPU 0," "GPU 1," "GPU 2," "GPU 3."

#### Stage 1 arrows
- Each GPU sends a gradient chunk (small colored block) to the next GPU clockwise.
- Arrow from GPU 0 → GPU 1, GPU 1 → GPU 2, GPU 2 → GPU 3, GPU 3 → GPU 0.
- Chunk color: #E67E22 (orange).
- Small label: "send chunk."

#### Stage 2 arrows
- Same ring pattern. Each GPU now sends the accumulated sum.
- Chunk grows slightly (sum of two).
- Label: "accumulate + send."

#### Completion
- After two full rounds, each GPU shows "complete average" with a gold (#F1C40F) checkmark.
- Small label per GPU: "✓ all gradients averaged."

### Bottom: Centralized Pattern (contrasted)

#### Hub-spoke layout
- One central node labeled "parameter server."
- Four GPU nodes around it, all arrows pointing inward to the hub.
- Return arrows from hub back to each GPU.

#### Bottleneck indicator
- The central hub has a red (#E74C3C) bottleneck icon (hourglass or congestion symbol).
- Label: "bandwidth chokepoint."
- Small text: "gets worse with more GPUs."

### Comparison labels
- Top section label: "ring all-reduce — scales." Color: #27AE60 (green).
- Bottom section label: "centralized — bottleneck." Color: #E74C3C (red).

## Animation sequence
1. Four GPUs appear in ring formation (1s).
2. Stage 1: gradient chunks pass clockwise simultaneously (2s).
3. Stage 2: accumulated chunks pass clockwise (2s).
4. Gold checkmarks appear on all GPUs (0.5s).
5. Scene splits: centralized pattern appears below (1.5s).
6. All arrows converge on hub, bottleneck icon pulses red (1.5s).
7. Comparison labels appear (0.5s).

## Palette
- GPU nodes: #4A90D9 (blue)
- Gradient chunks: #E67E22 (orange)
- Complete checkmarks: #F1C40F (gold)
- Ring label: #27AE60 (green)
- Hub/bottleneck: #E74C3C (red)
- Centralized label: #E74C3C (red)
- Background: #1A1A2E
- Text: #EAEAEA
