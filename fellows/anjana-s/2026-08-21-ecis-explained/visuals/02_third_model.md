# Beat 2 — The Third Model

**Visual type:** Remotion
**Duration:** ~15 seconds

## What the viewer sees

**Qwen arrives (0-4s):**
A third node animates into the empty slot from Beat 1. "Qwen 14B" in warm amber. It is noticeably larger than Llama and Mistral — maybe 30-40% bigger — reflecting the parameter count difference. The dotted outline from the recap fills in solid.

The three nodes now sit in a row:
- Llama 3.1 8B (purple, smaller)
- Mistral 7B (teal, smaller)
- Qwen 14B (amber, larger)

All three connect down to the triangulator with arrows of varying thickness.

**Architecture rework (4-8s):**
A pipeline state bar appears below the nodes — a horizontal strip labeled "Pipeline State." Inside it, three colored dots appear: purple, teal, amber. A label: "Model identity flows through state." This conveys that multi-model is now native, not an afterthought.

The triangulator node briefly opens to show three internal weight bars — purple, teal, amber — each at a different height. Label: "Weighted independently."

**Three-way agreement (8-15s):**
A chunk card flows in from the left. It splits into three paths, one to each model. All three process simultaneously:
- Llama: "raised 0.81"
- Mistral: "raised 0.77"
- Qwen: "raised 0.84"

Green agreement lines connect all three. The triangulator absorbs the three signals and outputs: "raised 0.86" — confidence boosted by three-way consensus.

A label appears: "Multi-model native. Not bolted on."

## Technical notes

- Amber for Qwen is the new series color — keep it consistent from here on
- The size difference between Qwen and the other two should be visible but not cartoonish
- The pipeline state bar is a new visual element — keep it simple, just colored dots in a strip
- Reuse the triangulator node from Episodes 1 and 2
- The three-way flow should feel like Episode 2's dual flow, extended naturally to three
