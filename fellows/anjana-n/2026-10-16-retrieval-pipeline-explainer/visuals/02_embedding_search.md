# B02 — Embedding and Search

## Composition type
Remotion

## Layout
Dark stage. Left: query-to-vector transformation. Center: ANN index cylinder. Right: candidate cards. Cumulative latency bar below.

## Elements

### Left: Embedding

#### Query text
- Color: #EAEAEA.

#### Embed box
- Rounded rectangle labeled "embedding model."
- Color: #1ABC9C (teal).

#### Vector output
- A row of numbers in monospace: "[0.23, -0.81, 0.44, 0.12, ...]"
- Enclosed in a small bracket.
- Color: #1ABC9C (teal) text.

#### Latency tag
- Small pill badge below the embed box: "~10ms."
- Color: #F1C40F (gold).

### Center: ANN Index

#### Index cylinder
- A database cylinder, larger than other elements.
- Label: "ANN index."
- Color: #4A90D9 (blue).

#### Internal structure sketch
- Faint HNSW-style graph inside the cylinder: nodes connected by edges at multiple layers.
- Labels on two layers: "HNSW" and small text "~2M vectors."

#### Latency tag
- Small pill badge below: "~40ms."
- Color: #F1C40F (gold).

### Right: Candidate cards

#### Cards
- Eight small document cards in a column, numbered 1–8.
- Each card has a one-line label: "risk factor section," "supply chain note," "revenue summary," etc.
- Top cards have higher similarity scores displayed: "0.89," "0.84," "0.81," descending.
- Color: #4A90D9 (blue) borders.

### Bottom: Cumulative bar
- Horizontal bar showing: embed segment (teal, 10ms) + search segment (blue, 40ms).
- Right end label: "50ms."
- Color: #F1C40F (gold) border.

## Animation sequence
1. Query text appears (0.5s).
2. Text flows into embed box (0.5s).
3. Vector output emerges with "~10ms" tag (1.5s).
4. Vector arrow flies into index cylinder (1s).
5. HNSW graph inside cylinder briefly highlights search path (1.5s).
6. Candidate cards emerge from cylinder, stacking with scores (2s).
7. "~40ms" tag appears (0.5s).
8. Cumulative bar fills: teal + blue = "50ms" (1.5s).

## Palette
- Embed box/vector: #1ABC9C (teal)
- Index: #4A90D9 (blue)
- Candidate borders: #4A90D9 (blue)
- Latency tags: #F1C40F (gold)
- HNSW graph: #95A5A6 (grey, faint)
- Background: #1A1A2E
- Text: #EAEAEA
