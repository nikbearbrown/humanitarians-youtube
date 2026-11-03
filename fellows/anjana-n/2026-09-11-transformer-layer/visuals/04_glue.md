# Beat 4 — The Glue: Residual + Layer Norm

**Visual type:** Remotion
**Duration:** ~12 seconds

## What the viewer sees

A side-view diagram showing the complete data flow through the layer with both bypass paths visible.

**Residual around attention (0-6s):**
The flow diagram shows:

Input → the path splits into two:
- **Main path** (top): goes through the "Self-Attention" block from Beat 2
- **Bypass path** (bottom): a curved arrow that goes around the block, unchanged

After attention, the two paths merge at a circle labeled "+". The original and the transformed are added together.

A brief visual demo: show what happens if attention learned nothing useful. The main path output is near-zero. But the bypass carries the original through untouched. The "+" produces the original, unchanged. Label: "If the layer learns nothing, no damage done."

After the "+", the sum passes through a small box labeled "Layer Norm." The vector strip's values visually stabilize: tall spikes shrink, low valleys grow. The range normalizes. Label: "Values rescaled."

**Residual around feed-forward (6-9s):**
The same pattern repeats: the output of the first Add & Norm splits again. Main path through "Feed-Forward" (Beat 3). Bypass around it. Merge at "+". Another "Layer Norm."

This second pass is shown faster, the viewer already understands the pattern.

**Full layer view (9-12s):**
The complete layer architecture is visible as a clean flow:

Input → [Self-Attention] → Add & Norm → [Feed-Forward] → Add & Norm → Output

The bypass arrows are visible around both blocks. The "revenue" token exits the right side of the layer, fully processed.

Label: "Residual protects. Layer norm stabilizes. That is why you can stack ninety-six of these."

## Technical notes

- The bypass arrows are the key visual element: a path that goes AROUND the operation
- The "+" merge node should feel like a safety net catching the original
- Layer norm's visual effect is values compressing toward a stable range
- The full-layer view at the end is the architectural summary the viewer takes away
- Show post-norm architecture (norm after add) matching the original Vaswani paper
