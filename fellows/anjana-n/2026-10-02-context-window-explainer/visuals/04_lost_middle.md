# B04 — Lost in the Middle

## Composition type
Remotion

## Layout
Dark stage. Full-width context bar at center. U-shaped attention curve above.

## Elements

### Context bar
- A long horizontal bar representing the full context window.
- Divided into many thin vertical segments.
- Color gradient by attention intensity:
  - Left edge (first ~15% of tokens): bright blue (#4A90D9).
  - Middle (~70% of tokens): faded grey (#3A3A4E, barely visible).
  - Right edge (last ~15% of tokens): bright blue (#4A90D9).
- Small labels at edges: "beginning" (left), "end" (right).
- Small label at center: "middle" in dim grey.

### U-shaped attention curve
- A smooth curve plotted above the context bar.
- Y-axis: "recall accuracy" (0% to 100%).
- The curve starts high on the left (~90%), dips sharply in the middle (~40%), and rises again on the right (~85%).
- The dip region is shaded in light red (#E74C3C at 15% opacity).
- The curve line color follows the bar: blue at edges, grey in the dip.


### Label
- Centered below the bar: "lost in the middle."
- Text color: #E74C3C (red), pulsing softly.

## Animation sequence
1. Context bar appears with gradient coloring (1.5s).
2. U-shaped attention curve draws from left to right (2s).
3. Dip region shading fills in (1s).
4. drops into the middle of the bar (1.5s).
5. "?" appears, dotted line connects to curve dip (2s).
6. "lost in the middle" label fades in below (1.5s).

## Palette
- High-attention segments: #4A90D9 (blue)
- Low-attention segments: #3A3A4E (dim)
- Attention curve: #4A90D9 fading to #95A5A6 in dip
- Dip shading: #E74C3C at 15% opacity
- Question mark: #F1C40F (gold)
- "lost in the middle" label: #E74C3C (red)
- Background: #1A1A2E
