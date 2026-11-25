# B04 — Analyst Intelligence

## Composition type
Remotion

## Layout
Dark stage. Left: analyst profile card. Right: two dodge score comparison cards showing raw vs normalized.

## Elements

### Analyst profile card (left)
- A rounded rectangle styled as a profile card.
- Name: "Analyst 1."
- Difficulty rating bar: 4 out of 5 filled segments.
  - Color: #E67E22 (orange) for filled, #555555 for empty.
- Question type distribution: three small horizontal bars:
  - "forward-looking" — longest bar, #3498DB (blue).
  - "backward-looking" — medium bar, #9B59B6 (purple).
  - "confrontational" — short bar, #E74C3C (red).
- Alignment score: a small gauge at "0.72."
  - Color: #F1C40F (gold).

### Dodge comparison (right, two cards stacked)

#### Top card: Tough analyst, hard question
- Label: "Analyst 1 — difficulty: high."
- Dodge icon (evasion symbol).
- Raw dodge score: "0.8."
- Normalized dodge score: "0.4" — lower, labeled "expected evasion."
- Color: #27AE60 (green) for normalized (low signal).

#### Bottom card: Friendly analyst, routine question
- Label: "Analyst 2 — difficulty: low."
- Same dodge icon.
- Raw dodge score: "0.8" — identical.
- Normalized dodge score: "0.9" — higher, labeled "unusual evasion."
- Color: #E74C3C (red) for normalized (high signal).

### Divergence annotation
- Arrow between the two normalized scores.
- Label: "same raw score, different signal."
- Color: #F1C40F (gold).

## Animation sequence
1. Analyst profile card appears (2s).
2. Difficulty bar fills, question type bars extend (1.5s).
3. Alignment gauge appears (0.5s).
4. Top dodge card appears — raw 0.8, normalized drops to 0.4 (1.5s).
5. Bottom dodge card appears — raw 0.8, normalized rises to 0.9 (1.5s).
6. Divergence arrow and "same raw score, different signal" label (1.5s).

## Palette
- Profile card: #E67E22 (orange) accents
- Difficulty bar: #E67E22 (filled), #555555 (empty)
- Question types: #3498DB, #9B59B6, #E74C3C
- Alignment gauge: #F1C40F (gold)
- Low signal (expected): #27AE60 (green)
- High signal (unusual): #E74C3C (red)
- Divergence label: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
