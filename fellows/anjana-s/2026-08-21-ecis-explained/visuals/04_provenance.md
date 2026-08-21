# Beat 4 — Provenance

**Visual type:** Remotion
**Duration:** ~12 seconds

## What the viewer sees

A single signal card appears center screen — the familiar format: ticker (NVDA), direction (raised), confidence (0.84), supporting quote.

**The flip (0-5s):**
On "stores the exact prompt" — the signal card tilts backward slightly, revealing it has depth. Behind the front card, layers slide out like an accordion or a fanned stack of cards:

- Layer 1 (closest): **System Prompt** — a small text block preview, greyed, showing the first few lines of the extraction prompt
- Layer 2: **Few-Shot Examples** — three mini-cards fanned slightly, each showing a brief example extraction
- Layer 3: **Temporal Context** — a chunk preview labeled "Q3 2024 — prior quarter" with a date tag
- Layer 4 (deepest): **Source Chunk** — the original transcript text that was fed to the model, highlighted

Each layer slides out with a slight stagger — the stack builds depth behind the signal card.

**The seal (5-9s):**
All four layers are visible in a stacked arrangement. A dotted line connects each layer back to the signal card on top. A label appears: "Full provenance. Fully reproducible."

**The receipt (9-12s):**
On "Every decision has a receipt" — a receipt icon (a small paper slip with a checkmark) stamps onto the bottom of the stack. The entire provenance stack glows briefly — sealed and complete.

## Technical notes

- The accordion/stack effect is the signature visual of this beat — it should feel like opening a file to see everything behind it
- Each layer should be readable but not fully legible — the viewer sees that content exists, not the specific text
- The stagger animation should be smooth — each layer sliding out 0.2s after the previous
- The receipt icon is the emotional payoff — small, clean, definitive
- Dark background, the signal card and its layers are the only illuminated elements
