# FACTCHECK — claude-liam-convolution

Verdicts: PASS · CORRECTED · EXEMPT. "Run" = recomputed by `experiment.py` (numpy; deterministic). Image: 6×6, every row [0,0,0,9,9,9]. Kernel: every row [−1,0,1] (3×3). "Convolution" is computed as cross-correlation (no kernel flip), as in deep-learning libraries.

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B02 | Edge sits between columns 3 and 4 of the 6×6 image | PASS | image definition | — |
| 2 | B03 | Window at top-left (columns 1–3) sums to 0 | PASS | run | — |
| 3 | B04 | Window positions 2, 3, 4 give 27, 27, 0 | PASS | run: 27, 27, 0; position 4: −27 + 27 = 0 | "nine minus nine" per pixel; three rows give −27 + 27 |
| 4 | B04, B05 | Every output row reads 0, 27, 27, 0 | PASS | run | — |
| 5 | B06 | Fully connected 6×6 → 4×4 needs 36 × 16 = 576 weights | PASS | arithmetic (ignores biases) | said "weights" |
| 6 | B06 | The convolution uses 9 weights | PASS | kernel size | — |
| 7 | B06 | Edge moved one column left gives 27, 0, 0, 0 | PASS | run | — |
| 8 | B07 | Unpadded 3×3 layers: 6 → 4 → 2, a third does not fit | PASS | run: 6, 4, 2, 0 | — |
| 9 | B07 | One pixel of zero padding keeps size 6 | PASS | run | — |
| 10 | B00, BVDT | Convolution in deep learning slides the kernel without flipping (cross-correlation) | EXEMPT | convention | narration says "slide, multiply and add" |
