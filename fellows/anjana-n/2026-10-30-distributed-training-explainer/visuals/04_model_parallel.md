# B04 — Model Parallelism

## Composition type
Remotion

## Layout
Dark stage. Two sections stacked. Top: tensor parallelism. Bottom: pipeline parallelism with micro-batching.

## Elements

### Top: Tensor Parallelism

#### Large matrix
- A wide rectangular matrix labeled "layer weight matrix."
- Color: #9B59B6 (purple).

#### Split into four slices
- The matrix is divided by vertical dashed lines into four equal slices.
- Each slice is assigned to a GPU:
  - Slice 1 → "GPU 0" — #4A90D9 (blue).
  - Slice 2 → "GPU 1" — #4A90D9 (blue).
  - Slice 3 → "GPU 2" — #4A90D9 (blue).
  - Slice 4 → "GPU 3" — #4A90D9 (blue).

#### Combine step
- Arrows from all four slices converge to a result block.
- Label: "combine partial results."
- Color: #F1C40F (gold).

#### Section label
- "tensor parallelism — splits individual layers."

### Bottom: Pipeline Parallelism

#### Four GPUs in sequence
- Four GPU cards in a horizontal line, each containing a group of layers:
  - GPU 0: "layers 1–12" — #9B59B6 (purple).
  - GPU 1: "layers 13–24" — #9B59B6 (purple, slightly different shade).
  - GPU 2: "layers 25–36" — #9B59B6 (purple, slightly different shade).
  - GPU 3: "layers 37–48" — #9B59B6 (purple, slightly different shade).

#### Sequential flow (without micro-batching)
- A single batch arrow flows left to right through all four GPUs.
- GPUs 1–3 show red (#E74C3C) "idle" zones while waiting.
- Label on the idle zones: "pipeline bubble."

#### Micro-batching overlay
- The same pipeline, but now with four micro-batches shown as overlapping:
  - Micro-batch 1 on GPU 1 while micro-batch 2 enters GPU 0.
  - Micro-batch 1 on GPU 2 while micro-batch 2 on GPU 1 while micro-batch 3 enters GPU 0.
- The red idle zones shrink significantly.
- Label: "micro-batching reduces the bubble."

#### Section label
- "pipeline parallelism — splits layer groups."

## Animation sequence
1. Large matrix appears (0.5s).
2. Matrix splits into four slices, each moves to a GPU (2s).
3. Combine arrows converge to result (1s).
4. "tensor parallelism" label appears (0.5s).
5. Scene shifts to bottom: four GPUs with layer groups (1s).
6. Single batch flows through — red idle bubbles appear (2s).
7. Micro-batches overlay: multiple batches overlap, idle zones shrink (2s).
8. "pipeline parallelism" label and "micro-batching" label appear (1s).

## Palette
- Weight matrix: #9B59B6 (purple)
- GPU nodes: #4A90D9 (blue)
- Layer groups: #9B59B6 (purple shades)
- Combine result: #F1C40F (gold)
- Idle bubbles: #E74C3C (red)
- Micro-batch arrows: #27AE60 (green), #1ABC9C (teal), #F39C12 (amber), #4A90D9 (blue)
- Background: #1A1A2E
- Text: #EAEAEA
