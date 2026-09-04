# Beat 3 — Retrieve

**Visual type:** Remotion
**Duration:** ~15 seconds

## What the viewer sees

**Vector search (0-6s):**
The question vector (bright dot from Beat 2) enters from the left. On the right, a large cylindrical database icon labeled "Vector Store" pulses gently. Inside it, thousands of tiny dots represent stored chunk embeddings.

The question vector sends out a ripple that washes through the database. Dots near it in meaning space light up bright. Distant dots stay dim. Three dots glow brightest.

Similarity score lines connect the question vector to the top three matches: 0.94, 0.91, 0.87.

**Retrieved chunks (6-11s):**
Three chunk cards slide out from the database, ranked by similarity:

Card 1 (0.94): Preview text: "We are raising our full-year revenue outlook to twelve point five billion..."
Metadata tags: Company A | Q3 2024 | Prepared Remarks | CFO

Card 2 (0.91): Preview text: "The increase reflects stronger than expected demand across..."
Metadata tags: Company A | Q3 2024 | Prepared Remarks | CEO

Card 3 (0.87): Preview text: "Prior guidance of twelve billion has been revised upward..."
Metadata tags: Company A | Q3 2024 | Q&A | CFO

Each card appears with a slight stagger. The metadata tags are small but readable.

**Handoff (11-15s):**
The three cards stack together into a neat bundle. An arrow carries the bundle to the right toward a new node: the LLM icon (not yet active, just waiting).

Label: "Context assembled. Three chunks. Ready for the model."

## Technical notes

- The ripple effect through the database should feel like sonar, searching by proximity
- The similarity scores on the connecting lines should be readable
- Chunk card text should be partially visible, enough to see it is real transcript language
- Metadata tags distinguish the sources and reinforce that these are real documents
- The handoff animation should feel like passing a file folder to someone
