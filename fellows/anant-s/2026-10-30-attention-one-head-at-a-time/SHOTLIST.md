# SHOTLIST: Attention, One Head at a Time

Current as built (ai-explainer, converted 2026-11-24 from tldr). Body rows are unchanged from the original shot list.

| Beat | Role | Lane | Component / scene | Shot type × source | Fill |
|---|---|---|---|---|---|
| B00 | ASK | Remotion | `ClaudeComposerAsk` (greeting "Hello, Liam"; the ask types in; three result lines) | GRAPHIC × own | machine |
| B01 | BLUF | Remotion | `BrutalistHesitantWriter` ("picks the one word it needs" → "blends every word around it") | GRAPHIC × own | machine |
| B10 | HOOK | Manim | `B10_ChaseMoves`: sentence and embeddings, head box, chase's dot lands, then moves when cats → kids | GRAPHIC × own | machine |
| B11 | INSTANCE | Manim | `B11_MixingPoints`: value points; two-point blend sweep; four-point blend gliding inside the hull | GRAPHIC × own | machine |
| B12 | INSTANCE | Manim | `B12_RequestMeetsOffer`: chase's request docks against each offer; products → score chips; then small asks | GRAPHIC × own | machine |
| B13 | NAIVE | Manim | `B13_EqualWeights`: ¼ weights; all four blend dots collapse onto (0.5, 0.75) | GRAPHIC × own | machine |
| B14 | SHIFT · predict | Manim | `B14_HeatMap`: score grid → ÷2 → row softmax → heat map; HOLD for the prediction | GRAPHIC × own | machine |
| B15 | TRANSFORM | Manim | `B15_LetTheMatchMix`: heat-map row → masses on the value points → dot lands on B10's ghost; other rows fire | GRAPHIC × own | machine |
| B16 | ABSTRACTION | Manim | `B16_NameIt`: requests/offers/points → Q/K/V; objects morph into the MathTex equation | GRAPHIC × own | machine |
| B17 | TANGENT | Manim | `B17_Tangent`: five-zone equation tangent on the split stage, with a box spotlight | GRAPHIC × own | machine |
| B18 | PAYOFF | Manim | `B18_Payoff`: B10's dot with weighted pull lines; cats → kids replayed with the re-weighting visible | GRAPHIC × own | machine |
| B19 | BOUNDARY | Manim | `B19_OrderBlind`: dogs ↔ cats swap, heat-map cells permute, outputs stay still; + position moves cats | GRAPHIC × own | machine |
| BVDT | VERDICT | Remotion | `ClaudeVerdictArtifact` (six lines) | REMOTION × own | machine |
| BHTF | YOUR TURN | Remotion | `ClaudeComposerAsk` (Your turn.; prompt read verbatim; three checks) | REMOTION × own | machine |
| BOUT | OUTRO | Remotion | `ClaudeTitleOutro` (locked) | REMOTION × own | machine |

## History: original tldr shot list (2026-11-22, kept verbatim)

Beat ids in this history are the pre-conversion ones; the body ids did not change. Retired beats: B00, B01, B02, B03.

> # SHOTLIST: Attention, One Head at a Time
>
> | Beat | Role | Lane | Component / scene | Shot type × source | Fill |
> |---|---|---|---|---|---|
> | B00 | TL;DR · WHAT | Remotion | `ClaudeTldrWhat` | REMOTION × own | machine |
> | B01 | TL;DR · WHY | Remotion | `ClaudeTldrWhy` | REMOTION × own | machine |
> | B02 | THE QUESTION | Remotion | `BrutalistHesitantWriter` ("pick the word it needs" → "blend the words around it") | REMOTION × own | machine |
> | B03 | TERMS | Remotion | `ClaudeDefinitions` (embedding, dot product, softmax) | REMOTION × own | machine |
> | B10 | HOOK | Manim | `B10_ChaseMoves`: sentence and embeddings, head box, chase's dot lands, then moves when cats → kids | GRAPHIC × own | machine |
> | B11 | INSTANCE | Manim | `B11_MixingPoints`: value points; two-point blend sweep; four-point blend gliding inside the hull | GRAPHIC × own | machine |
> | B12 | INSTANCE | Manim | `B12_RequestMeetsOffer`: chase's request docks against each offer; products → score chips; then small asks | GRAPHIC × own | machine |
> | B13 | NAIVE | Manim | `B13_EqualWeights`: ¼ weights; all four blend dots collapse onto (0.5, 0.75) | GRAPHIC × own | machine |
> | B14 | SHIFT · predict | Manim | `B14_HeatMap`: score grid → ÷2 → row softmax → heat map; HOLD for the prediction | GRAPHIC × own | machine |
> | B15 | TRANSFORM | Manim | `B15_LetTheMatchMix`: heat-map row → masses on the value points → dot lands on B10's ghost; other rows fire | GRAPHIC × own | machine |
> | B16 | ABSTRACTION | Manim | `B16_NameIt`: requests/offers/points → Q/K/V; objects morph into the MathTex equation | GRAPHIC × own | machine |
> | B17 | TANGENT | Manim | `B17_Tangent`: five-zone equation tangent on the split stage, with a box spotlight | GRAPHIC × own | machine |
> | B18 | PAYOFF | Manim | `B18_Payoff`: B10's dot with weighted pull lines; cats → kids replayed with the re-weighting visible | GRAPHIC × own | machine |
> | B19 | BOUNDARY | Manim | `B19_OrderBlind`: dogs ↔ cats swap, heat-map cells permute, outputs stay still; + position moves cats | GRAPHIC × own | machine |
> | BVDT | VERDICT | Remotion | `ClaudeVerdictArtifact` (six lines) | REMOTION × own | machine |
> | BHTF | YOUR TURN | Remotion | `ClaudeComposerAsk` (Your turn.; prompt read verbatim; three checks) | REMOTION × own | machine |
> | BOUT | OUTRO | Remotion | `ClaudeTitleOutro` (locked) | REMOTION × own | machine |
>
> The pantry is empty by design. A lesson is entirely drawable (tldr PURE-MANIM law), and every number comes from `demo/evidence.json`. There are no stills, no AI footage and no shopping list.
>
> ## Persistent objects (transform, don't cut, within section 1)
> - **Sentence row** (B10, B18, B19): "cats chase small dogs". The word "cats" morphs to "kids" (B10, B18) and swaps places with "dogs" (B19).
> - **Value plane** (B10 → B19): x −2…3, y −3…3, with four labelled value points. Kids' point appears only in B10 and B18.
> - **Chase's output dot and its two ghost landings** (B10 → B15 → B18): the HOOK's object, returned by the PAYOFF.
> - **Score grid → heat map** (B14 → B15 → B16 → B18 → B19).
> - **Request and offer rows** (B12 → B14 → B16, where they become Q and K).
>
> ## Library-first (GATE L), 2026-11-22, `scene_search.py --no-log`
> - **Queries:** "attention heat map", "query key value attention", "weighted average of points", "dot product two vectors", "softmax row of scores", "matrix grid of numbers animated", "equation with symbol glossary", "word order shuffle".
> - **Result: no reusable hit.** Every hit was a film-specific figure with hard-coded content that exposes only `sparkLine`/`phase` props (BrandAgentMapper, BigQueryApi*, TeachClaudeFig3, BrandSignalMatrix, HorrorEquation, …). LEARN beats must be Manim anyway (tldr law), so Remotion compositions were only checked for bookends.
> - **Manim lead for B17:** `skills/make/explainer/manim/animated_graphics.py` already has `EquationTangent`, `SentencePair`, `GlossaryTable`, `WorkedExample` and `ValuesClaim` (the EQT_* fixtures). Adapt them to the Claude palette rather than writing the zones from scratch. They are imported by copy into `scenes.py`, never edited in the toolkit.
> - **Bookend props confirmed:** `--check ClaudeTldrWhat ClaudeTldrWhy ClaudeDefinitions BrutalistHesitantWriter ClaudeComposerAsk ClaudeVerdictArtifact ClaudeTitleOutro` all RENDERABLE 16:9. The zod schemas were read in `runtime/remotion/src/scenes/ClaudeTldrWhat.tsx`, `ClaudeTldrWhy.tsx` and `ClaudeDefinitions.tsx`. lines ≤ 4 ✓, terms 1–5 ✓, term ≤ 22 chars ✓, meaning ≤ ~80 chars ✓ (longest is 74), durationSeconds ≥ 3 / ≥ 2 ✓.
>
