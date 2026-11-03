# B04 — Tensor Cores

## Elements

### Left side: CUDA core

#### Core icon
- A single green circle (#27AE60), larger than the grid dots in B02.
- Label above: "CUDA core."

#### Scalar operation
- Two small numbers float in from the left (e.g., "3.2" and "4.7").
- They enter the core.
- One number floats out to the right: "15.04."
- A small "x" symbol between the inputs.

#### Label
- Below: "scalar multiply-add."

### Right side: Tensor core

#### Core icon
- A larger square, purple (#9B59B6), with an inner grid pattern suggesting matrix structure.
- Label above: "tensor core."

#### Matrix operation
- Two small 4x4 grids float in from the left.
- Grid A color: #4A90D9 (blue). Grid B color: #27AE60 (green).
- They enter the tensor core.
- One 4x4 grid floats out to the right, colored #F1C40F (gold) — the result.

#### Label
- Below: "matrix multiply-accumulate."

### Bottom: Mixed precision diagram

#### Precision blocks
- Left: a compact block labeled "FP16 inputs" (#9B59B6).
- Arrow pointing right.
- Right: a wider block labeled "FP32 accumulation" (#4A90D9).
- Label below arrow: "reduced memory, maintained accuracy."

### Count badge
- Top right corner: "432 tensor cores per A100."
- Badge: #9B59B6 text on dark card.

## Animation sequence
1. CUDA core appears, two numbers flow in, product flows out (2.5s).
2. "scalar multiply-add" label (0.5s).
3. Tensor core square appears with inner grid pattern (1s).
4. Two 4x4 matrices flow in, result matrix flows out (3s).
5. "matrix multiply-accumulate" label (0.5s).
6. Precision diagram appears: FP16 block, arrow, FP32 block (2s).
7. "reduced memory, maintained accuracy" label (1s).
8. "432 tensor cores" badge fades in (1s).

## Palette
- CUDA core: #27AE60 (green)
- Tensor core: #9B59B6 (purple)
- Input matrix A: #4A90D9 (blue)
- Input matrix B: #27AE60 (green)
- Result matrix: #F1C40F (gold)
- FP16 block: #9B59B6 (purple)
- FP32 block: #4A90D9 (blue)
- Scalar numbers: #EAEAEA
- Background: #1A1A2E
