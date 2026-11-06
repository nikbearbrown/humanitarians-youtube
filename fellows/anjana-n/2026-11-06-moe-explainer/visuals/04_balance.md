# B04 — Load Balancing and Routing Collapse

## Composition type
Remotion

## Layout
Dark stage. Two states: collapsed routing (top/first) → balanced routing (bottom/after). Transition triggered by balancing loss.

## Elements

### State 1: Routing collapse

#### Eight expert boxes in a row
- Expert 1 and expert 2: bright blue (#3498DB), overflowing with token dots.
  - Token dots piled up, some spilling over the top.
  - Label: "overloaded."
- Experts 3–8: dim grey (#555555), empty.
  - Label: "starved."

#### Collapse label
- "routing collapse" in red (#E74C3C), centered above.

#### Token flow
- All orange (#E67E22) tokens funnel into experts 1 and 2.
- No tokens reach experts 3–8.

### Transition: Balancing loss

#### Loss term icon
- A small shield or balance-scale icon.
- Label: "auxiliary load-balancing loss."
- Color: #F1C40F (gold).
- Appears between the two states.

### State 2: Balanced routing

#### Eight expert boxes in a row
- All eight are lit blue (#3498DB) at roughly equal brightness.
- Each holds a roughly equal number of token dots.
- Label: "balanced routing."

#### Capacity factor annotation
- A small cap icon on each expert.
- Label: "capacity factor — max tokens per expert per batch."
- Color: #F39C12 (amber).

#### Overflow routing
- One token exceeds expert 3's cap → arrow redirects to expert 5 (second choice).
- Small label: "overflow → second choice."

## Animation sequence
1. Eight expert boxes appear (0.5s).
2. Tokens flood into experts 1 and 2 — others empty (2.5s).
3. "routing collapse" label appears in red (1s).
4. Balancing loss icon appears in gold (1s).
5. Token distribution animates — tokens redistribute evenly (2.5s).
6. All experts light up blue equally (1s).
7. "balanced routing" label replaces collapse label (0.5s).
8. Capacity factor annotation appears (1.5s).
9. One overflow redirect animates (1.5s).

## Palette
- Overloaded experts: #3498DB (blue, bright)
- Starved experts: #555555 (dim grey)
- Balanced experts: #3498DB (blue, even)
- Tokens: #E67E22 (orange)
- Collapse label: #E74C3C (red)
- Balancing loss icon: #F1C40F (gold)
- Capacity factor: #F39C12 (amber)
- Background: #1A1A2E
- Text: #EAEAEA
