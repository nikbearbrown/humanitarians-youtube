# B04 — Making It Fast

## Composition type
Remotion

## Layout
Dark stage. Split view: brute force on the left, graph-based ANN on the right.

## Elements

### Left panel: Brute force
- A query dot in the center with hundreds of thin lines radiating to every stored dot.
- A counter ticks up rapidly: "1,000,000 comparisons."
- A small clock icon below, spinning slowly. Label: "slow."

### Right panel: HNSW graph
- Dots connected by edges to their nearby neighbors only (sparse graph structure).
- A query dot enters at a random node on the edge of the graph.
- A glowing gold path hops along edges: 4 hops, each moving closer to the target dot.
- Hop 1: far from target. Hop 2: closer. Hop 3: nearby. Hop 4: at the nearest neighbor.
- Counter: "47 comparisons."
- Clock icon below, spinning fast. Label: "fast."

### Bottom label
- Centered: "approximate nearest neighbor."

## Animation sequence
1. Left panel: query dot appears, lines radiate outward rapidly (2s).
2. Counter ticks to 1,000,000 (1s).
3. "slow" label (0.5s).
4. Right panel: graph structure fades in (1.5s).
5. Query dot enters, first hop highlights (1s).
6. Three more hops along the glowing path (2s).
7. Counter shows 47, "fast" label (1s).
8. "approximate nearest neighbor" fades in at bottom (1s).

## Palette
- Brute force lines: #E74C3C at 20% opacity (red, thin)
- Graph edges: #3A3A4E (dark grey)
- Hop path: #F1C40F (gold, glowing)
- Query dot: #F1C40F (gold)
- Target dot: #27AE60 (green)
- Slow label: #E74C3C (red)
- Fast label: #27AE60 (green)
- Background: #1A1A2E
