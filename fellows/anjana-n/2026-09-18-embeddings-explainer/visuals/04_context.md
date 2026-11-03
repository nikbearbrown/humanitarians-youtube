# B04 — Context Changes Everything

## Composition type
Remotion

## Layout
Dark stage. Two parallel sentences with the same word producing different embeddings.

## Elements

### Top sequence
- Sentence tokens in a horizontal row: "the," "river," "bank," "was," "steep."
- "bank" highlighted with a blue border.
- Arrow from "bank" leads to a vector dot that floats toward a nature cluster (small cluster of dots labeled "river," "shore," "water").

### Bottom sequence
- Sentence tokens: "the," "bank," "reported," "strong," "earnings."
- "bank" highlighted with a gold border.
- Arrow from "bank" leads to a different vector dot that floats toward a finance cluster (dots labeled "earnings," "revenue," "profit").

### Transformer blocks
- Between each "bank" token and its contextualized vector, a small stack of 3 rectangular blocks labeled "transformer layers."
- Arrows flow through the blocks, showing the embedding being reshaped.

### Center label
- Between the two paths: "same token, different vectors."

## Animation sequence
1. Top sentence appears, "bank" highlights blue (1.5s).
2. Arrow flows through transformer blocks, dot lands in nature cluster (2s).
3. Bottom sentence appears, "bank" highlights gold (1.5s).
4. Arrow flows through transformer blocks, dot lands in finance cluster (2s).
5. "same token, different vectors" label fades in between them (1.5s).
6. Both clusters and vectors glow to emphasize the contrast (1s).

## Palette
- Top "bank" highlight: #4A90D9 (blue)
- Bottom "bank" highlight: #F1C40F (gold)
- Nature cluster: #27AE60 (green)
- Finance cluster: #E67E22 (orange)
- Transformer blocks: #9B59B6 (purple)
- Label text: #EAEAEA
- Background: #1A1A2E
