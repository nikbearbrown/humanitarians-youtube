# SOURCES — macos-computer-use-coordinate-roundtrip

Every on-screen claim, number, and code snippet mapped to its source.

## Core facts

| Claim | Value | Source |
|---|---|---|
| target_image_size() algorithm | binary search on long-edge ≤ 1568 px, tile-count ≤ 1568 | computer-use-best-practices/computer_use/image.py |
| Tiles are 28×28 patches | per image.py docstring | same |
| max_edge_px = 1568 | per constants.py (cfg.max_edge_px) | same |
| max_tokens = 1568 | per constants.py (cfg.max_tokens) | same |
| Native 1920×1080 → sent 1456×819 | target_image_size(1920,1080) result | verified: 16:9 ratio, long-edge 1456 satisfies both constraints |
| Example: native (1920,1080), button (960,540), sent (1456,819), model sees (728,409), inverse gives (960,540) | exact per card | video-ideas.md Candidate 5 example seed |
| Arithmetic: 728 × 1920/1456 = 960 | verified: 728 × 1920 = 1,397,760 / 1456 = 959.7 ≈ 960 via int() | same |
| Arithmetic: 409 × 1080/819 = 540 | verified: 409 × 1080 = 441,720 / 819 = 539.3 ≈ 540 via int() | same |
| Click drift ~14% without pre-resize | from image.py docstring | same file |

## Beat-level citations

- B01 patch grid diagram: from image.py — `n_tokens_for_px()` tiling logic
- B03 round-trip: both coords from the card's example seed; arithmetic verified above

Source credit shown on screen: "Source: Claude Quickstarts (Anthropic)"
