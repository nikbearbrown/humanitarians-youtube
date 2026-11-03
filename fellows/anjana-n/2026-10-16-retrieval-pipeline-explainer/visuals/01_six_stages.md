# B01 — The Six Stages

## Composition type
Remotion

## Layout
Dark stage. Six blocks in a horizontal pipeline left to right. Gold timeline bar below.

## Elements

### Query input
- Small rounded rectangle on the far left.
- Text: "user question."
- Color: #EAEAEA text, thin #95A5A6 border.

### Six pipeline blocks (left to right)
1. "embed" — #1ABC9C (teal).
2. "search" — #4A90D9 (blue).
3. "rewrite" — #E67E22 (orange). Dashed border (conditional stage).
4. "rerank" — #9B59B6 (purple).
5. "filter" — #E74C3C (red).
6. "assemble" — #27AE60 (green).
- Each block is a rounded rectangle with centered label.
- Arrows connect each block to the next.

### Output
- Small rounded rectangle on the far right.
- Text: "final context."
- Color: #27AE60 (green) border.

### Latency timeline
- A thin horizontal gold bar (#F1C40F) running below all six blocks.
- Left end: "0ms."
- Right end: "< 500ms."
- Small tick marks below each block showing cumulative time.

## Animation sequence
1. Query input appears (0.5s).
2. Blocks appear one by one left to right, each with a small pop (3s total, 0.5s each).
3. Arrows draw between blocks (1s).
4. "rewrite" block border animates to dashed (0.5s).
5. Output box appears (0.5s).
6. Gold timeline bar draws left to right below (2s).
7. "< 500ms" label fades in at right end (0.5s).

## Palette
- Embed: #1ABC9C (teal)
- Search: #4A90D9 (blue)
- Rewrite: #E67E22 (orange)
- Rerank: #9B59B6 (purple)
- Filter: #E74C3C (red)
- Assemble: #27AE60 (green)
- Timeline: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
