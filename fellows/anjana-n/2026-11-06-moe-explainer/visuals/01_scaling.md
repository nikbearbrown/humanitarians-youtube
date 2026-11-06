# B01 — The Scaling Problem

## Composition type
Remotion

## Layout
Dark stage. Center: a dense transformer FFN block with tokens flowing through. Right: parameter and compute counters climbing in lockstep.

## Elements

### Dense FFN block
- A large rounded rectangle labeled "feed-forward network."
- Color: #9B59B6 (purple) fill.
- The entire block is solidly lit — all parameters active.

### Token stream
- A row of orange (#E67E22) dots entering from the left, passing through the entire FFN, exiting right.
- Every dot touches every part of the block.
- Label above: "every token → every parameter."

### Parameter counter (right, top)
- A vertical counter ticking up: "7B → 13B → 70B."
- Color: #27AE60 (green) text.

### Compute counter (right, bottom)
- A second counter climbing in lockstep: "7B ops → 13B ops → 70B ops."
- Color: #E74C3C (red) text.
- A thin line connects the two counters — they move together.
- Label: "parameters = compute."

### Question text
- Appears at the bottom after counters climb.
- "What if most parameters could sit this one out?"
- Color: #F1C40F (gold).

## Animation sequence
1. Dense FFN block appears, fully lit purple (1s).
2. Token stream flows through — all dots pass through entire block (2s).
3. "every token → every parameter" label (1s).
4. Parameter counter ticks: 7B → 13B → 70B (3s).
5. Compute counter ticks in sync below it (same 3s).
6. "parameters = compute" label appears (1s).
7. Question text fades in at bottom in gold (2s).

## Palette
- FFN block: #9B59B6 (purple)
- Tokens: #E67E22 (orange)
- Parameter count: #27AE60 (green)
- Compute count: #E74C3C (red)
- Question: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
