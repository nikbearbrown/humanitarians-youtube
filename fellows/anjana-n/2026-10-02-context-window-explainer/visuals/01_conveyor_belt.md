# B01 — The Conveyor Belt

## Composition type
Remotion

## Layout
Dark stage. Horizontal conveyor belt centered vertically.

## Elements

### Conveyor belt
- A long horizontal track spanning ~80% of screen width.
- Subtle animated texture (dashed lines moving left) to suggest motion.
- Belt color: #2C3E50 (dark slate) with #95A5A6 dashes.

### Text blocks on belt
- Rounded rectangles riding the belt, evenly spaced:
  - "system prompt" (blue, #4A90D9).
  - "user message 1" (green, #27AE60).
  - "assistant reply 1" (purple, #9B59B6).
  - "user message 2" (green, #27AE60).
  - "assistant reply 2" (purple, #9B59B6).
  - "user message 3" (green, #27AE60).
- White text on each block, small font.

### Overflow
- As new blocks slide in from the right, the leftmost block slides off the left edge and fades out with a subtle dissolve.
- A small "gone" label appears briefly where the block fell off.

### Context window bracket
- A glowing bracket (gold, #F1C40F) above the belt, spanning the visible portion.
- Label centered above bracket: "context window: 128K tokens."

### Model eye
- A simple stylized eye icon at center-top of the belt.
- Subtle pupil animation tracking the blocks.
- Color: #EAEAEA.

## Animation sequence
1. Belt appears, empty (0.5s).
2. Blocks slide on from right one by one (4s total, staggered).
3. Belt fills up — bracket glows to show it's full (1s).
4. New block arrives; leftmost block falls off left edge (2s).
5. "gone" label flashes where block disappeared (0.5s).
6. Hold with eye watching remaining blocks (2s).

## Palette
- Belt: #2C3E50 with #95A5A6 dashes
- System prompt block: #4A90D9
- User blocks: #27AE60
- Assistant blocks: #9B59B6
- Bracket: #F1C40F (gold)
- Eye: #EAEAEA
- "gone" label: #E74C3C
- Background: #1A1A2E
