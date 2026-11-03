# Beat 2 — Fine-Tuning

**Visual type:** Remotion
**Duration:** ~15 seconds

## What the viewer sees

**The boundary problem (0-5s):**
Two quote cards side by side:
- Left: "We are comfortable with our current outlook." Tagged: "MAINTAINED" (blue)
- Right: "We remain focused on execution." Tagged: "NONE" (grey)

A red pulsing zone between them labeled "Decision boundary." Red X marks scatter in the zone, representing past misclassifications. This is where the model kept getting it wrong.

**Training (5-10s):**
The two cards shrink and join a stream of training examples (200+ small cards) flowing into a simplified neural network diagram from below. Counter: "200+ reviewed extractions."

The network is the base model. Beside it, a small rectangular block highlights: the QLoRA adapter. It glows as the training data flows through, absorbing the corrections. Labels on the adapter: "Rank 16. 4-bit. 5 epochs."

The adapter block is visually small compared to the base model, reinforcing that it is a targeted refinement, not a full retrain.

**Result (10-15s):**
The adapter locks into the side of the base model with a click. The combined model re-reads the two boundary quotes. Both are now tagged correctly with higher confidence badges. The red X marks in the decision boundary zone clear out, replaced by green checkmarks.

Label: "Same model. Sharper edge."

## Technical notes

- The boundary zone with red X marks is the visual problem statement
- The adapter block should look like a small attachment, not a replacement
- The clearing of red X marks to green checkmarks is the payoff
- No specific company names in the example quotes
