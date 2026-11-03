# B01 — Cold Open

## Composition type
Remotion

## Layout
Dark stage. SQL queries on the left, one succeeds, one fails.

## Elements

### Successful query
- A code block in monospace: `SELECT * FROM products WHERE status = 'active'`
- Green checkmark to the right.
- A small results table fades in below: three matching rows.

### Failed query
- Below the first, another code block: `SELECT * FROM products WHERE ??? similar to this`
- The operator position shows a red "???" pulsing.
- Red question mark to the right. No results table.

### Right side (empty space)
- Empty dark area, suggesting the answer has not arrived yet.
- A faint dotted outline of a box with a question mark inside, hinting at what comes next.

## Animation sequence
1. First query types in character by character (2s).
2. Green checkmark, results table fades in (1.5s).
3. Second query types in, "???" pulses red (2s).
4. Red question mark appears, no results (1.5s).
5. Hold on the contrast (2s).

## Palette
- Code text: #EAEAEA (white) on #2C2C3E (dark block)
- Success: #27AE60 (green)
- Failure: #E74C3C (red)
- Background: #1A1A2E
