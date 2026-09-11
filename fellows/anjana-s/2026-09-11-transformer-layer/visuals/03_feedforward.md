# Beat 3 — Feed-Forward Network

**Visual type:** Remotion
**Duration:** ~10 seconds

## What the viewer sees

The context-aware "revenue" vector from Beat 2 moves to the right inside the layer, entering a box labeled "Feed-Forward Network."

**Expansion (0-3s):**
Inside the box, the vector is visualized as a narrow vertical color strip (maybe 8 cells wide). It stretches horizontally to 4x its original width (32 cells). Each cell has a different color/intensity. Label: "Expand: d_model → 4x d_model"

The expansion should feel like zooming into detail, like magnifying the representation.

**Activation (3-6s):**
The expanded strip passes through a wave-shaped gate in the middle of the box, labeled "GELU." As it passes through:
- Some cells brighten (activated, kept)
- Some cells go dark/black (zeroed out, suppressed)

The result is a pattern of bright and dark, like a barcode. The non-linearity selectively keeps useful features and kills useless ones.

**Compression (6-10s):**
The activated strip compresses back to its original width (8 cells). Label: "Compress: 4x d_model → d_model"

The output vector exits the feed-forward box. It is the same size as the input but the colors are different. Transformed.

Label: "Attention gathers. Feed-forward processes."

## Technical notes

- The expand/activate/compress sequence should feel like a factory process: widen, filter, narrow
- The GELU gate should look like a physical filter or sieve
- Bright cells = activated features, dark cells = suppressed features
- The compression back to original size should feel like distillation
- Keep it clean, three distinct stages inside one box
