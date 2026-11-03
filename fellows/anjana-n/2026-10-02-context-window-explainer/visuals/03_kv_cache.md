# B03 — The KV Cache

## Composition type
Remotion

## Layout
Dark stage. Left side: quadratic scaling grid. Right side: KV cache and GPU memory bar.

## Elements

### Left side: Quadratic scaling visualization

#### Grid animation
- A square grid where rows = tokens, columns = tokens.
- Phase 1: 4x4 grid (small, labeled "1K tokens"). 16 cells visible.
- Phase 2: grid doubles to 8x8 (labeled "2K tokens"). 64 cells — 4x the area.
- Phase 3: grid doubles again to 16x16 (labeled "4K tokens"). 256 cells — 16x the original.
- Each cell is a small square, color transitioning from blue (#4A90D9) at top-left to purple (#9B59B6) at bottom-right.
- Label below: "double tokens = 4x compute."

### Right side: KV cache diagram

#### Cache blocks
- Two stacked horizontal rectangles:
  - Top: labeled "K cache" (blue, #4A90D9).
  - Bottom: labeled "V cache" (purple, #9B59B6).
- Small text: "one pair per layer, per token."

#### GPU memory bar
- A vertical bar on the far right, styled like a thermometer.
- Bottom label: "GPU VRAM."
- As the context length slider increases, the bar fills upward:
  - 4K: ~10% full (green, #27AE60).
  - 32K: ~40% full (gold, #F1C40F).
  - 128K: ~85% full (red, #E74C3C).
- Label at the 128K mark: "~40 GB VRAM (KV cache alone)."

#### Context length slider
- A horizontal slider below the cache blocks.
- Knob slides from left (4K) to right (128K).
- As it moves, the GPU bar fills and changes color.

## Animation sequence
1. Left: 4x4 grid appears (1s).
2. Grid doubles to 8x8 — "4x compute" (1.5s).
3. Grid doubles to 16x16 — "16x compute" (1.5s).
4. Right: K and V cache blocks appear (1s).
5. Slider moves from 4K to 128K, GPU bar fills progressively (3s).
6. "~40 GB" label appears at peak (1s).

## Palette
- Grid cells: gradient #4A90D9 to #9B59B6
- K cache: #4A90D9 (blue)
- V cache: #9B59B6 (purple)
- GPU bar low: #27AE60 (green)
- GPU bar mid: #F1C40F (gold)
- GPU bar high: #E74C3C (red)
- Slider track: #95A5A6 (grey)
- Slider knob: #EAEAEA
- Background: #1A1A2E
