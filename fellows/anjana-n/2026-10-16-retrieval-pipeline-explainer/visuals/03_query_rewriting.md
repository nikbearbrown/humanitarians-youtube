# B03 — Query Rewriting

## Composition type
Remotion

## Layout
Dark stage. Three parallel technique paths across the top. Decision gate below. Latency annotation.

## Elements

### Original query
- Rounded rectangle at top center.
- Color: #EAEAEA text, #1ABC9C (teal) border.

### Three technique paths (arranged horizontally below original)

#### Path 1: HyDE
- Label: "HyDE."
- Arrow from original query to a paragraph block (hypothetical answer).
- Paragraph text (small, truncated)
- Arrow from paragraph to embed box.
- Color: #E67E22 (orange).

#### Path 2: Step-back
- Label: "step-back."
- Arrow from original query to a broader query.
- Broader query text: "What challenges did major tech companies face in 2024?"
- Color: #E67E22 (orange).

#### Path 3: Decomposition
- Label: "decomposition."
- Color: #E67E22 (orange).

### Decision gate
- Below the three paths, a diamond decision node.
- Label: "retrieval confidence < threshold?"
- "yes" arrow points up to the rewrite paths.
- "no" arrow bypasses right to "continue pipeline."
- Color: #F1C40F (gold) for the diamond.

### Latency annotation
- A dashed bracket spanning the three technique paths.
- Label: "+50–200ms (conditional)."
- Color: #F1C40F (gold).

### Bypass label
- On the "no" path: "skip — 0ms."
- Color: #27AE60 (green).

## Animation sequence
1. Original query appears (0.5s).
2. Decision gate appears below with "confidence < threshold?" (1s).
3. "yes" path activates — three technique paths grow upward (3s total):
   - HyDE: query → paragraph → embed (1s).
   - Step-back: query → broader query (1s).
   - Decomposition: query splits into three (1s).
4. Latency bracket appears: "+50–200ms" (0.5s).
5. "no" path highlights: "skip — 0ms" (1s).
6. Decision gate pulses gold (0.5s).

## Palette
- Original query: #1ABC9C (teal) border
- Technique paths: #E67E22 (orange)
- Decision gate: #F1C40F (gold)
- Bypass: #27AE60 (green)
- Latency bracket: #F1C40F (gold)
- Background: #1A1A2E
- Text: #EAEAEA
