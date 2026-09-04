# Beat 2 — Embed the Question

**Visual type:** Remotion
**Duration:** ~12 seconds

## What the viewer sees

**Question to vector (0-4s):**
The question text floats center screen: "Did Company A raise revenue guidance last quarter?"

Below it, an embedding model box appears (small, labeled "Embedding Model"). The question flows into it with a smooth animation.

Out the other side: a horizontal strip of colored cells, a visual representation of the vector. Each cell is a slightly different color. Label: "384 dimensions."

**Meaning space (4-12s):**
The vector floats upward into a 2D scatter plot representing embedding space. The plot has clusters of dots, each cluster labeled:

- "Revenue guidance" cluster (upper left, blue dots)
- "Margin commentary" cluster (lower right, teal dots)  
- "Capex outlook" cluster (center right, amber dots)
- "Earnings estimates" cluster (lower left, green dots)

The question's vector appears as a bright, pulsing dot that lands inside the "Revenue guidance" cluster. It belongs there because of meaning, not keywords.

Label: "Not searching for words. Searching for meaning."

## Technical notes

- The vector strip should look abstract and technical, like a barcode of meaning
- The scatter plot clusters should feel like neighborhoods on a map
- The question's dot landing in the right cluster is the visual insight
- Keep the plot simple, four clusters max, clear labels
- The embedding model box is a black box deliberately, we don't explain its internals here
