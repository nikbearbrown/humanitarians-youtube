# B02 — Sequence Models — LSTM and GRU

## Composition type
Remotion

## Layout
Dark stage. Left: tree model seeing a single snapshot. Right: LSTM unrolled across quarters with hidden state.

## Elements

### Left: Tree model (snapshot)
- A single feature vector column (vertical bar with feature labels).
- Label: "Q4 only."
- A tree icon below processing it.
- Color: #F39C12 (amber) for the feature vector, #EAEAEA for the tree.

### Right: LSTM unrolled

#### Quarter cells
- Four to eight cells in a horizontal chain: "Q1," "Q2," "Q3," "Q4," etc.
- Each cell is a rounded rectangle with a feature vector inside.
- Color: #3498DB (blue) border.

#### Hidden state arrows
- Arrows connecting each cell to the next, labeled "h."
- Color: #9B59B6 (purple) for hidden state.
- The hidden state grows richer (thicker arrow) moving right.

#### Hedging ramp highlight
- A line graph overlaying the cells showing hedging increasing gradually over four quarters.
- Color: #E67E22 (orange) line.
- Label: "gradual ramp — sequence pattern."

#### Output
- From the final cell, an arrow to a prediction node.
- Label: "next-quarter forecast."
- Color: #F1C40F (gold).

### GRU annotation
- Small text below the LSTM: "GRU variant: 30% faster, comparable accuracy."
- Color: #1ABC9C (teal).

### Side-by-side label
- Between the two sides: "snapshot vs sequence."

## Animation sequence
1. Tree model appears with single feature vector (1.5s).
2. "Q4 only" label (0.5s).
3. LSTM cells unroll left to right, hidden state arrows connecting them (3s).
4. Hedging ramp line draws over the cells (1.5s).
5. "gradual ramp — sequence pattern" label (0.5s).
6. Prediction node appears at end (1s).
7. GRU annotation fades in below (1s).
8. "snapshot vs sequence" label appears (1s).

## Palette
- Tree/snapshot: #F39C12 (amber)
- LSTM cells: #3498DB (blue)
- Hidden state: #9B59B6 (purple)
- Hedging ramp: #E67E22 (orange)
- Prediction: #F1C40F (gold)
- GRU text: #1ABC9C (teal)
- Background: #1A1A2E
- Text: #EAEAEA
