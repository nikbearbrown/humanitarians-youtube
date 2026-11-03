# B05 — Working Around It

## Composition type
Remotion

## Layout
Dark stage. Three columns at top. Conveyor belt callback at bottom.

## Elements

### Three strategy columns

#### Left column: Chunking
- A tall rectangle representing a long document (outlined, #95A5A6).
- The rectangle splits into 4 smaller pieces with dotted cut lines.
- Each piece is a different shade of blue (#4A90D9 variants).
- Small arrows show each chunk sliding down toward the conveyor belt below.
- Label above: "chunking."

#### Center column: Summarization
- A tall stack of text blocks representing conversation turns (6-7 blocks, alternating green and purple).
- The stack compresses downward — an animation squishing it — into a single compact block labeled "summary."
- The summary block is gold (#F1C40F).
- Label above: "summarization."

#### Right column: RAG
- A small search icon (magnifying glass, #EAEAEA) at the top.
- Below it, a cylinder representing a database/knowledge base (#2C3E50 with a blue outline).
- The search icon sends a query line into the database.
- Two small snippet blocks (#27AE60) fly out of the database upward, then arc down toward the conveyor belt.
- Label above: "RAG."

### Bottom: Conveyor belt callback
- The same conveyor belt from B01 reappears at the bottom of the screen.
- This time it's efficiently loaded:
  - A chunk block (blue) from the left column.
  - A summary block (gold) from the center column.
  - Two RAG snippet blocks (green) from the right column.
- Plenty of empty space on the belt — it's not overflowing.
- The gold bracket from B01 reappears above: "context window."

### Closing text
- The belt and columns fade.
- Centered text: "The context window is a budget. Spend it on what matters."
- Text color: #EAEAEA, slightly larger than other labels.
- Fade to dark.

## Animation sequence
1. Three column labels appear (0.5s).
2. Left: document splits into chunks (1.5s).
3. Center: conversation stack compresses into summary (1.5s).
4. Right: search queries database, snippets fly out (1.5s).
5. Conveyor belt appears at bottom (0.5s).
6. Chunks, summary, and snippets land on the belt (2s).
7. Bracket appears, belt looks balanced and efficient (1s).
8. Everything fades, closing text appears (2s).
9. Fade to dark (1s).

## Palette
- Document/chunks: #4A90D9 shades (blue)
- Summary block: #F1C40F (gold)
- RAG snippets: #27AE60 (green)
- Search icon: #EAEAEA
- Database: #2C3E50 with #4A90D9 outline
- Conveyor belt: #2C3E50 with #95A5A6 dashes
- Bracket: #F1C40F (gold)
- Closing text: #EAEAEA
- Background: #1A1A2E
