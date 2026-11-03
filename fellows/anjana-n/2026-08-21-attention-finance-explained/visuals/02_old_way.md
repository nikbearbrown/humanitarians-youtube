# Beat 2 — The Old Way

**Visual type:** Remotion
**Duration:** ~12 seconds

## What the viewer sees

The same sentence from Beat 1, same layout, same word blocks.

**Left-to-right cursor (0-7s):**
A glowing highlight cursor appears on "We" at the far left. It moves word by word, left to right, at a steady pace.

As the cursor passes each word, it gets colored:
- "We" → neutral
- "expect" → neutral
- "revenue" → turns **green** — the model registers a financial keyword
- "to remain" → neutral
- "broadly in line" → turns **green** — sounds stable/positive
- "with prior guidance" → turns **green** — reaffirmation language

The model is building a positive picture. A verdict bar starts forming above the sentence: filling green, labeled "POSITIVE."

The cursor continues:
- "despite" → turns **amber** — a hedge word, but the verdict bar barely moves
- "near-term headwinds" → turns **amber/red** — negative signal

But the verdict bar is already mostly filled green. The late amber words don't have enough weight to change the verdict.

**Wrong answer (7-12s):**
The verdict locks in: "POSITIVE ✓" in green above the sentence.

A red **✗** stamps over it. Wrong.

A label appears below: "Left-to-right. Made up its mind too early."

The green-colored early words and the amber-colored late words are still visible — the visual shows the imbalance.

## Technical notes

- The cursor movement should feel mechanical and rigid — left to right, no going back
- The green coloring of early words should feel confident — the model is committing
- The verdict bar filling green before the cursor reaches "despite" is the key visual — the decision is already made
- The red X should feel definitive — a clear wrong answer
- Same word block layout as Beat 1 — exact positioning
