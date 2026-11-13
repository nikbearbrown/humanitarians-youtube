# B05 — The Agentic Layer

## Composition type
Remotion

## Layout
Dark stage. Right: chat panel with query. Left: three-node agent pipeline (plan → execute → synthesize).

## Elements

### Chat panel (right side)
- A dark rounded rectangle mimicking a chat interface.
- User message bubble: "Which companies show deterioration signals this quarter?"
- Color: user bubble #3498DB (blue) background.
- Agent response area below (initially empty, fills at the end).

### Agent pipeline (left side, compact flowchart)

#### Planning node
- Rounded rectangle labeled "plan."
- Inside: the query broken into sub-tasks:
  - "scan all tickers."
  - "check signal types: hedging, tone, dodge."
  - "filter for deterioration."
- Color: #9B59B6 (purple) border.

#### Execution node
- Rounded rectangle labeled "execute."
- Inside: tool icons routing to:
  - "signal DB" — database icon.
  - "cross-company analytics" — network icon.
  - "SHAP" — chart icon.
- Arrows from planning node to execution node.
- Color: #F39C12 (amber) border.

#### Synthesis node
- Rounded rectangle labeled "synthesize."
- Inside: "compose structured response."
- Arrow from execution node to synthesis node.
- Color: #1ABC9C (teal) border.

### Response in chat panel
- Agent response bubble appears:
  - "3 companies flagged: Company A (dodge ↑), Company C (hedging ↑), Company E (tone ↓)."
- Color: agent bubble #1A1A2E with #EAEAEA text and #1ABC9C (teal) left border.

## Animation sequence
1. Chat panel appears on right with user query (1.5s).
2. Planning node appears — sub-tasks list populates (1.5s).
3. Arrow to execution node — tool routing icons appear (1.5s).
4. Arrow to synthesis node — "compose response" (1s).
5. Arrow from synthesis to chat panel (0.5s).
6. Agent response bubble appears with results (2s).
7. Hold (0.5s).

## Palette
- User bubble: #3498DB (blue)
- Planning node: #9B59B6 (purple)
- Execution node: #F39C12 (amber)
- Synthesis node: #1ABC9C (teal)
- Agent response border: #1ABC9C (teal)
- Background: #1A1A2E
- Text: #EAEAEA
