# B04 — Speech Acts and Discourse Structure

## Composition type
Remotion

## Layout
Dark stage. Left: stacked bar of speech act distribution. Right: four discourse structure pattern diagrams.

## Elements

### Left: Speech Act Distribution

#### Stacked horizontal bar
- One wide horizontal bar divided into six colored segments:
  1. "promises" — #4A90D9 (blue), ~10%.
  2. "commitments" — #1ABC9C (teal), ~15%.
  3. "hedged intentions" — #E67E22 (orange), ~25%.
  4. "predictions" — #F1C40F (gold), ~20%.
  5. "deflections" — #E74C3C (red), ~15%.
  6. "assertions" — #27AE60 (green), ~15%.
- Each segment labeled with its name and percentage.
- Label above: "speech act distribution — Q3 call."

#### DeBERTa label
- Small text below bar: "fine-tuned DeBERTa classifier."
- Color: #95A5A6.

### Right: Discourse Structure Patterns

#### Four small diagrams arranged in 2×2 grid
Each is a miniature sentiment trajectory line across a horizontal axis (start to end of prepared remarks):

1. "front-loading"
   - Line starts low (negative), rises steadily to end high.
   - Small "−" at start, "+" at end.
   - Color: #4A90D9 (blue).

2. "burying"
   - Line starts high, dips in the middle, returns high.
   - "+" at start, "−" in middle, "+" at end.
   - Color: #E67E22 (orange).

3. "progressive disclosure"
   - Line starts low/flat, gradually builds upward.
   - Small steps, each higher.
   - Color: #27AE60 (green).

4. "deflection"
   - Line starts flat, dips, then pivots to flat again (doesn't recover, just stops declining).
   - Arrow at the pivot point.
   - Color: #E74C3C (red).

- Each diagram is a small card with the pattern name below it.
- Label above the 2×2 grid: "narrative patterns."

## Animation sequence
1. Speech act bar draws left to right, segments filling (2.5s).
2. Segment labels fade in (1s).
3. "DeBERTa" label appears (0.5s).
4. Four discourse diagrams appear one by one (3s, 0.75s each):
   - Front-loading line draws.
   - Burying line draws.
   - Progressive disclosure line draws.
   - Deflection line draws with pivot arrow.
5. "narrative patterns" label fades in (0.5s).
6. "deflection" diagram border briefly highlights red (0.5s).

## Palette
- Promises: #4A90D9 (blue)
- Commitments: #1ABC9C (teal)
- Hedged intentions: #E67E22 (orange)
- Predictions: #F1C40F (gold)
- Deflections: #E74C3C (red)
- Assertions: #27AE60 (green)
- Front-loading line: #4A90D9 (blue)
- Burying line: #E67E22 (orange)
- Progressive disclosure line: #27AE60 (green)
- Deflection line: #E74C3C (red)
- DeBERTa label: #95A5A6 (grey)
- Background: #1A1A2E
- Text: #EAEAEA
