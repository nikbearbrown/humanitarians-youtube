# FACTCHECK — cli-int8-mash

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | affine int8 formula: q = clip(round(x/scale) + zp, -128, 127) | ✓ | standard affine quantization; matches quantize_demo.py |
| B01 | x-hat = scale * (q - zp) | ✓ | standard affine dequantization |
| B01 | weights in [-1.5, 1.5] | ✓ | quantize_demo.py weights = np.clip(randn*0.6, -1.5, 1.5) |
| B01 | activations in [0.001, 0.01] | ✓ | quantize_demo.py activations = 0.0055 + 0.0045*sin(t) |
| B02 | scale = (hi - lo) / 255 | ✓ | q_params function in quantize_demo.py |
| B02 | zp = clip(round(-128 - lo/scale), -128, 127) | ✓ | q_params function |
| B03 | weight scale ≈ 0.0118 | ✓ | 3.0/255 = 0.01176... printed by script |
| B03 | 249 distinct dequantised levels for weights | ✓ | script output: "distinct dequant levels = 249" |
| B03 | activation range narrower than one step | ✓ | range = 0.009; step = 0.0118; 0.009 < 0.0118 |
| B03 | 4095 floats collapse to 2 levels | ✓ | script output: "distinct dequant levels = 2, collapse 4095/2" |
| B03 | "the sine is gone" | ✓ | quantised values {0, 0.0118} bracket the sine range [0.001, 0.01] without representing it |
| B05 | per-channel scale ≈ 3x10^-5 (300x finer than weight scale) | ✓ | 0.009/255 = 0.0000353; 0.0118/0.0000353 ≈ 334x finer; "three hundred times" is a valid rounded figure |
| B05 | 255 levels available with per-channel scale | ✓ | (0.01-0.001)/0.0000353 ≈ 255 by construction |
| B05 | "bigger quantization table" at inference | ✓ | per-channel quantization requires one (scale, zp) pair per channel vs one pair for the whole tensor |
| B05 | "more memory at inference" | ✓ | storing per-channel scale tables adds overhead proportional to channel count |

## Terms table

| Term | Debuts beat | Need created by |
|------|-------------|-----------------|
| affine int8 quantization | B01 | B01 (the prompt establishes the task) |
| scale | B02 | B01 (introduced in the prompt) |
| zero-point | B02 | B01 (introduced in the prompt) |
| staircase | B03 | B02 (code shows the step structure) |
| mash zone | B03 | B03 (visual shows the collapse) |
| per-channel | B05 | B04 (the change prompt names it) |

## Illustrative items
None — all numbers are computed from the actual script (quantize_demo.py) with np.random.seed(0).

## Exclusions honored
- No equations on screen (narration carries the formulas) ✓
- No chapter references in on-screen text ✓
- No forbidden phrases (obviously, clearly, revolutionary, important to understand) ✓
- No → ✓ ≠ × in on-screen Manim strings ✓
