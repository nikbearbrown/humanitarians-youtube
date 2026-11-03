# Beat 3 — The Architecture

**Visual type:** Manim  
**Duration:** ~28 seconds

## What the viewer sees

An animated flow diagram that builds from left to right as the narration progresses.

**Stage 1 (first 3 sec):** A document icon labeled "Transcript" enters from the left. It splits into small rectangular blocks labeled "chunks" that fan out slightly.

**Stage 2 (next 16 sec):** As each reader is named in the narration, a node appears on screen:

| Reader | Color | Shape | Appears when narrator says |
|--------|-------|-------|---------------------------|
| Keyword | blue | rectangle | "keyword reader scans for known guidance phrases" |
| FinBERT | teal | rectangle | "FinBERT, a financial sentiment model" |
| NER | orange | rectangle | "named entity recogniser extracts the hard numbers" |
| LLM | purple | rectangle | "large language model reasons through the passage" |

Each node animates in with a brief glow. Arrows draw from the chunk blocks to all four nodes simultaneously, showing parallel processing.

**Stage 3 (next 5 sec):** The LLM node briefly expands to show three sub-labels: "Chain-of-thought", "Self-consistency (3 passes)", "Verification". These appear as the narration describes them, then collapse back.

**Stage 4 (last 4 sec):** All four reader nodes draw arrows converging into a central diamond node labeled "Triangulator". The arrow thicknesses vary — the LLM arrow is thickest, keyword is thinnest — conveying dynamic weighting. A single output arrow exits right, ending at a signal block showing "direction: raised, confidence: 0.87".

## Mood

Systematic, precise, building complexity piece by piece. The viewer should understand the parallel multi-reader architecture by the end.

## Technical notes

- Manim's default dark background works well here
- Use smooth Create/FadeIn animations, not jarring transitions
- Arrow thickness represents weight: LLM (0.50) > FinBERT (0.20) > keyword (0.15)
- Keep text sizes large enough to read at 1080p export
- The diagram should be horizontally oriented: left-to-right data flow
