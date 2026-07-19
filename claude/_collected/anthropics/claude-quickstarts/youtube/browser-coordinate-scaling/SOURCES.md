# SOURCES — browser-coordinate-scaling

Every on-screen claim, number, and code snippet mapped to its source.

## Core facts

| Claim | Value | Source |
|---|---|---|
| Claude API width for 16:9 screenshots | 1456 px | `browser-use-demo/browser_use_demo/tools/coordinate_scaling.py` — `CLAUDE_ACTUAL_WIDTH = 1456` |
| Claude API height for 16:9 screenshots | 819 px | same file — `CLAUDE_ACTUAL_HEIGHT = 819` |
| Scale formula | `real_x = int(x * viewport_w / 1456)` | same file — `CoordinateScaler.get_scale_factors()` |
| Example: original 2560×1440, Claude sees 1456×819, Claude returns (728,409), scaled result (1280,720) | exact per card | video-ideas.md Candidate 1 example seed |
| Aspect ratio for 16:9 | `(16,9): (1456, 819)` | `coordinate_scaling.py` — `DOCUMENTED_SIZES` dict |
| Threshold check: if scale_x/scale_y near 1.0 no scaling | `abs(scale_x - 1.0) < 0.05` | same file — `scale_coordinates()` |
| Bounds clamp | `min(scaled_x, viewport_w - 1)` | same file |

## Beat-level citations

- B02 formula: direct from `CoordinateScaler.scale_coordinates()` in source file
- B03 split-screen: numbers 728, 409 → 1280, 720 are the card's example seed, verified against source arithmetic: 728 × 2560/1456 = 1280 exactly; 409 × 1440/819 = 719.9 ≈ 720 via int()

Source credit shown on screen: "Source: Claude Quickstarts (Anthropic)"
