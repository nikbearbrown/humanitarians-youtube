# B02 — Dodge Detection

## Composition type
Remotion

## Layout
Dark stage. Left: Q&A flow with cross-encoder. Right: dodge meter and question type weights.

## Elements

### Left side: Q&A Flow

#### Analyst question
- An analyst icon (person silhouette, #4A90D9).
- Speech bubble extending right: "What drove the margin decline?"
- A type badge on the bubble: "confrontational" (#E74C3C, red).

#### Cross-encoder block
- A rounded rectangle between analyst and management, labeled "cross-encoder reranker."
- Color: #9B59B6 (purple) outline.
- The question text and answer text both feed into the block as arrows.
- Output arrow pointing right with score: "relevance: 0.31."

#### Management answer
- A management icon (person silhouette, #95A5A6).
- Speech bubble: ellipsis or vague text ("We continue to focus on operational excellence...").

#### Relevance verdict
- Below the cross-encoder output: "low relevance — dodge detected" in #E67E22 (orange).

### Right side: Dodge Scoring

#### Dodge meter
- A vertical bar gauge, 0–100.
- Fill at ~78, colored in gradient: green at bottom, orange at top.
- Label: "call dodge score: 78."

#### Question type weights
- Four small badges stacked vertically:
  - "confrontational: 2.0x" (#E74C3C).
  - "forward-looking: 1.5x" (#4A90D9).
  - "backward-looking: 1.0x" (#95A5A6).
  - "clarification: 0.5x" (#27AE60).

#### Quarterly trend
- Small sparkline below the meter showing dodge scores across 4 quarters.
- Line trends upward. Label: "dodge trend."

## Animation sequence
1. Analyst icon and question bubble appear with type badge (1.5s).
2. Management icon and vague answer appear (1.5s).
3. Cross-encoder block appears, arrows feed in, relevance score outputs (2s).
4. "dodge detected" verdict appears (1s).
5. Dodge meter fills to 78 (1.5s).
6. Question type weight badges appear (1.5s).
7. Sparkline draws below (1s).

## Palette
- Analyst icon: #4A90D9 (blue)
- Management icon: #95A5A6 (grey)
- Confrontational badge: #E74C3C (red)
- Cross-encoder: #9B59B6 outline (purple)
- Dodge detected: #E67E22 (orange)
- Dodge meter gradient: #27AE60 → #E67E22
- Forward-looking: #4A90D9, backward: #95A5A6, clarification: #27AE60
- Sparkline: #E67E22 (orange)
- Background: #1A1A2E
