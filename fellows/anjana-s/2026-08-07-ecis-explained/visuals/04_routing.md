# Beat 4 — Smart Routing

**Visual type:** Manim or Remotion  
**Duration:** ~22 seconds

## What the viewer sees

An animated decision tree / routing diagram. Chunks enter from the top and flow through the orchestration agent.

**Layout:**

```
        ┌──────────┐
        │  Chunks  │
        └────┬─────┘
             │
      ┌──────┴──────┐
      │ Orchestrator │
      └──┬──┬──┬──┬─┘
         │  │  │  │
         A  B  C  D
         │  │  │  │
         ▼  ▼  ▼  ▼
       LLM Full Conflict ✕
      confirm pipeline resolve SKIP
```

**Animation sequence:**

1. Chunks stream in from the top as small rectangles
2. The orchestrator node classifies each chunk — a brief label flashes (A, B, C, or D)
3. Chunks route down their respective branches:
   - **Cat A** chunks glow green, flow to "LLM confirm"
   - **Cat B** chunks glow amber, flow to "Full pipeline"
   - **Cat C** chunks glow red, flow to "Conflict resolution"
   - **Cat D** chunks grey out, dissolve, and disappear
4. A counter in the bottom-right tallies: "LLM calls saved: 60-80%" — the number ticks up as D chunks dissolve

The D branch should be visually dominant — lots of chunks disappearing there — to sell the efficiency story.

## Mood

Efficient, smart. The viewer should feel the elegance of not doing unnecessary work.

## Technical notes

- This can be Manim (consistent style with Beat 3) or Remotion (if animation needs are simpler)
- Category colors: A=green, B=amber, C=red, D=grey
- The counter is the key visual payoff — make it prominent
- Speed up the chunk flow as it continues, showing the system at scale
