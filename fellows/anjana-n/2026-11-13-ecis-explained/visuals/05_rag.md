# B05 — The Agent Learns to Read

## Composition type
Remotion

## Layout
Dark stage. Center: agentic chat panel. Left: two retrieval source icons (ChromaDB, PostgreSQL). Dual paths merge into the response.

## Elements

### Chat panel (center-right)
- Dark rounded rectangle mimicking chat interface.
- User query bubble: "Why was Company A flagged for deterioration?"
- Color: user bubble #3498DB (blue).

### Retrieval sources (left)

#### ChromaDB (transcript corpus)
- A cylinder icon labeled "ChromaDB — transcripts."
- Color: #9B59B6 (purple).
- Arrow labeled "semantic search" extending to the agent.

#### PostgreSQL (signal database)
- A cylinder icon labeled "PostgreSQL — signals."
- Color: #F39C12 (amber).
- Arrow labeled "structured query" extending to the agent.

### Hybrid retrieval merge
- Both arrows converge at a small merge node before entering the chat panel.
- Label: "hybrid retrieval."
- Color: #F1C40F (gold).

### Agent response
- Two result elements in the response area:
  - A quote bubble: an excerpt from a transcript (italic text, quotation marks).
    - Label: "transcript excerpt."
    - Color: #9B59B6 (purple) left border.
  - A data card: signal metric (e.g., "hedge index: 0.73 ↑").
    - Label: "signal metric."
    - Color: #F39C12 (amber) left border.
- Below both: synthesized response text.
- Agent bubble border: #1ABC9C (teal).

## Animation sequence
1. Chat panel appears with user query (1.5s).
2. ChromaDB icon appears with "semantic search" arrow (1s).
3. PostgreSQL icon appears with "structured query" arrow (1s).
4. Arrows converge at merge node — "hybrid retrieval" (1s).
5. Quote bubble appears in response area (1.5s).
6. Data card appears below the quote (1.5s).
7. Synthesized response text fills in (1.5s).

## Palette
- User query: #3498DB (blue)
- ChromaDB: #9B59B6 (purple)
- PostgreSQL: #F39C12 (amber)
- Merge node: #F1C40F (gold)
- Transcript excerpt border: #9B59B6 (purple)
- Signal metric border: #F39C12 (amber)
- Agent response: #1ABC9C (teal) border
- Background: #1A1A2E
- Text: #EAEAEA
