# Beat 3 — The Fine-Tuning

**Visual type:** Remotion
**Duration:** ~15 seconds

## What the viewer sees

A simplified neural network diagram, vertical orientation. Three layers stacked:
- Bottom: "Embedding Layer"
- Middle: "Transformer Blocks" (shown as 3-4 stacked rectangles)
- Top: "Classification Head"

Label on the left: "BERT"

**Training data stream (0-5s):**
On "fine-tunes it on fifty thousand financial sentences" — a stream of text fragments flows upward into the bottom of the network from below. Readable fragments: "revenue growth," "margin pressure," "forward guidance," "operating leverage," "fiscal headwinds," "sequential improvement." They enter the network and disappear inside.

**Weight shift (5-8s):**
The transformer blocks pulse as data flows through. Their color gradually shifts from neutral grey to warm gold — the model is being reshaped by the financial data. A counter: "50,000 sentences" appears and holds.

**The insight (8-15s):**
Two small example boxes animate beside the network:

Box 1: "revenue decline" → red arrow pointing down. Below: "Negative"
Box 2: "expense decline" → green arrow pointing up. Below: "Positive"

Between them, the word "decline" is highlighted — same word, opposite meaning depending on context. The model label on the left updates from "BERT" to "FinBERT" with a subtle glow.

## Technical notes

- The neural network should be simplified — not anatomically accurate, just the three conceptual layers
- The training data stream should feel like feeding — sentences flowing in
- The grey-to-gold color shift is the visual metaphor for fine-tuning
- The "decline" insight is the key teaching moment — make the contrast clear
- The BERT → FinBERT label change is the payoff
