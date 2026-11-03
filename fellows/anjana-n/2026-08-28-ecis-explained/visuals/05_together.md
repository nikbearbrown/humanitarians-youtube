# Beat 5 — All Together

**Visual type:** Remotion
**Duration:** ~8 seconds

## What the viewer sees

The triangulator node sits at the center, same style as all previous episodes.

Three inputs flow in from the left, stacked vertically with connecting arrows:

1. **Reader confidence: 0.85** — white text, neutral
2. **Speaker weight: 0.8 (CEO)** — green text
3. **Chunk quality: 0.92** — green text

An equation animates step by step:
0.85 × 0.8 = 0.68
0.68 × 0.92 = **0.63**

The output signal exits the triangulator to the right with confidence 0.63. Attached to it like a tag on a piece of luggage: a trend label reading "consecutive_raise" in a green band.

Below the triangulator, a label appears:
"What. Who. How clean. What came before."

Each word in the label corresponds to an input above it — a visual mapping from the four concepts to the four inputs.

## Technical notes

- This beat ties the entire episode together — it should feel like a summary diagram, not a new concept
- The step-by-step equation should be readable and paced to the narration
- The trend tag attached to the output signal is a nice visual touch — it rides alongside, not inside
- The label is the episode's thesis statement — give it a beat to land
- Reuse the triangulator node style from all previous episodes
