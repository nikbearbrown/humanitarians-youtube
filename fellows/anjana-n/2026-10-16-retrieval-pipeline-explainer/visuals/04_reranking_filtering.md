# B04 — Reranking and Filtering

## Composition type
Remotion

## Layout
Dark stage. Left: bi-encoder ranked list. Center: cross-encoder reranker. Right: filter gate and final list.

## Elements

### Left: Bi-encoder ranked candidates

#### Card column
- Twenty small cards in a vertical column (only top 8 visible, rest implied by "..." and count).
- Each card has a short label and a similarity score.
- Order: roughly by score but not perfectly relevant.
- Cards 3 and 7 are highlighted with a faint red tint — they'll drop after reranking.
- Label above: "bi-encoder ranked (top 20)."
- Color: #4A90D9 (blue) borders.

### Center: Cross-encoder reranker

#### Reranker block
- Large rounded rectangle labeled "cross-encoder."
- Color: #9B59B6 (purple).

#### Pair processing
- Inside the block, a visual showing: [query] + [candidate] → score.
- Three pairs shown flowing through simultaneously.
- Small text: "processes each pair independently."

#### Reordered output
- Cards emerge on the right side in a new order.
- Previously rank-3 and rank-7 cards are now at bottom / removed.
- Previously lower-ranked cards have moved up.
- Visible shuffling of positions.

#### Latency tag
- Pill badge below: "+80ms."
- Color: #F1C40F (gold).

### Right: Filter gate

#### Gate icon
- A vertical bar with three small icons:
  - Calendar icon: "date range." (#95A5A6).
  - File icon: "document type." (#95A5A6).
  - Lock icon: "access permissions." (#95A5A6).

#### Filtering action
- Three cards from the reranked list hit the gate.
- Two cards pass through (turn green border).
- One card is blocked (turns red, slides out with fade).

#### Final list
- Five remaining cards with green (#27AE60) borders.
- Label: "final candidates."

#### Latency tag
- Pill badge below: "+5ms."
- Color: #F1C40F (gold).

## Animation sequence
1. Bi-encoder ranked column appears with scores (1.5s).
2. Cards flow into cross-encoder block as pairs (2s).
3. Cards emerge reordered — visible position shuffling (2s).
4. "+80ms" tag appears (0.5s).
5. Filter gate appears with three icons (0.5s).
6. Cards pass through gate — one rejected (fades red, slides out) (2s).
7. Final candidates highlighted green (1s).
8. "+5ms" tag appears (0.5s).

## Palette
- Bi-encoder cards: #4A90D9 (blue)
- Cross-encoder block: #9B59B6 (purple)
- Filter icons: #95A5A6 (grey)
- Rejected card: #E74C3C (red)
- Final candidates: #27AE60 (green)
- Latency tags: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
