# B03 — Gated Residual Networks

- Input flows through two dense layers
- A sigmoid gate decides how much of the transformation to keep
- Gate open: transformation passes through
- Gate closed: skip connection carries the original input unchanged
- The block can never make the signal worse than what came in
