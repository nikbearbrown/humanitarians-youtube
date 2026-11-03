# B05 — The Latency Budget

## Composition type
Remotion

## Layout
Dark stage. Center: horizontal stacked bar chart. Below: final context arrow to LLM. Fade to title card.

## Elements

### Stacked bar chart

#### Bar segments (left to right)
1. "embed" — #1ABC9C (teal) — width proportional to 10ms. Label inside: "10ms."
2. "search" — #4A90D9 (blue) — width proportional to 40ms. Label inside: "40ms."
3. "rewrite" — #E67E22 (orange) — width proportional to ~150ms (shown as range). Label inside: "50–200ms." Dashed border (conditional). Slightly transparent to show it's not always present.
4. "rerank" — #9B59B6 (purple) — width proportional to 80ms. Label inside: "80ms."
5. "filter" — #E74C3C (red) — very thin sliver. Label outside (too narrow for inside): "5ms."
6. "overhead" — #95A5A6 (grey) — remaining space. Label inside: "network + retry."

#### Budget line
- Vertical gold line at the right end of the bar.
- Label above: "500ms budget."
- Color: #F1C40F (gold).

#### Total label
- Below the bar, centered: "total retrieval latency."

### Below: Final context to LLM

#### Context box
- Rounded rectangle below the bar chart.
- Label: "final context (5 chunks)."
- Color: #27AE60 (green) border.

#### Arrow to LLM
- Arrow from context box to a larger box labeled "LLM."
- LLM box color: #27AE60 (green).

### Title card
- Bar chart and context fade.
- Centered text: "What a Retrieval Pipeline Looks Like in Production."
- Color: #EAEAEA.
- Fade to dark.

## Animation sequence
1. Empty bar outline appears with 500ms budget line (1s).
2. "embed" segment fills from left (0.5s).
3. "search" segment extends (0.5s).
4. "rewrite" segment extends with dashed border, slightly transparent (1s).
5. "rerank" segment extends (0.5s).
6. "filter" sliver appears (0.3s).
7. "overhead" fills remaining gap to budget line (0.7s).
8. All labels fade in (0.5s).
9. Context box and arrow to LLM appear below (1.5s).
10. Scene fades, title card appears (2s).
11. Hold, fade to black (0.5s).

## Palette
- Embed: #1ABC9C (teal)
- Search: #4A90D9 (blue)
- Rewrite: #E67E22 (orange)
- Rerank: #9B59B6 (purple)
- Filter: #E74C3C (red)
- Overhead: #95A5A6 (grey)
- Budget line: #F1C40F (gold)
- Context/LLM: #27AE60 (green)
- Title text: #EAEAEA
- Background: #1A1A2E
