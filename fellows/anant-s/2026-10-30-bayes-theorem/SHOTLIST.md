# SHOTLIST: Bayes' Theorem: The Positive That's Usually Wrong

Current as built (ai-explainer, converted 2026-11-24 from tldr). Body rows are unchanged from the original shot list.

| Beat | Role | Lane | Component / scene | Shot type × source | Fill |
|---|---|---|---|---|---|
| B00 | ASK | Remotion | `ClaudeComposerAsk` (greeting "Hello, Liam"; the ask types in; three result lines) | GRAPHIC × own | machine |
| B01 | BLUF | Remotion | `BrutalistHesitantWriter` ("means you're probably sick" → "can still be a false alarm") | GRAPHIC × own | machine |
| B10 | HOOK | Manim | `B10_YouArePositive`: one "you" square, terracotta POSITIVE stamp, MathTex P(sick) = ? | GRAPHIC × own | machine |
| B11 | INSTANCE | Manim | `B11_TenThousand`: 125 × 80 isotype grid; 10 × 10 sick block scanned, 99 caught, 1 missed | GRAPHIC × own | machine |
| B12 | INSTANCE | Manim | `B12_FalseAlarms`: scan over the 9,900 healthy, 9,405 fade, 495 stay lit | GRAPHIC × own | machine |
| B13 | NAIVE | Manim | `B13_WrongCrowd`: box around the 10 × 10 sick block, MathTex 99/100, the 495 outside pulse | GRAPHIC × own | machine |
| B14 | SHIFT · predict | Manim | `B14_OnlyThePositives`: negatives fade, 594 positives regroup 27 × 22, hold ≥ 3 s | GRAPHIC × own | machine |
| B15 | TRANSFORM | Manim | `B15_OneInSix`: squares stack into 99/594, which reduces to 1/6 | GRAPHIC × own | machine |
| B16 | ABSTRACTION | Manim | `B16_BuildBayes`: counts ÷ 10,000 → P(+\ | D)P(D)/P(+) → P(A\ | B) = P(B\ | A)P(A)/P(B) | GRAPHIC × own | machine |
| B17 | TANGENT | Manim | `B17_ReadTheLine`: split stage, five zones, box spotlights | GRAPHIC × own | machine |
| B18 | PAYOFF | Manim | `B18_BackToYou`: B10's "you" square returns into the 594 block; 1/100 → 1/6 | GRAPHIC × own | machine |
| B19 | BOUNDARY | Manim | `B19_BaseRateDial`: P(D\ | +) vs base rate (log x); ValueTracker marker sweep | GRAPHIC × own | machine |
| BVDT | VERDICT | Remotion | `ClaudeVerdictArtifact` (4 lines) | GRAPHIC × remotion | machine |
| BHTF | YOUR TURN | Remotion | `ClaudeComposerAsk`: "Test Positive Twice" | GRAPHIC × remotion | machine |
| BOUT | OUTRO | Remotion | `ClaudeTitleOutro` (locked) | GRAPHIC × remotion | machine |

## History: original tldr shot list (2026-11-22, kept verbatim)

Beat ids in this history are the pre-conversion ones; the body ids did not change. Retired beats: B00, B01, B02, B03.

> # SHOTLIST — Bayes' Theorem: The Positive That's Usually Wrong
>
> | Beat | Role | Lane | Component / scene | Shot type × source | Fill |
> |---|---|---|---|---|---|
> | B00 | TL;DR · WHAT | Remotion | `ClaudeTldrWhat` ("Salaam, Liam") | GRAPHIC × remotion | machine |
> | B01 | TL;DR · WHY | Remotion | `ClaudeTldrWhy` | GRAPHIC × remotion | machine |
> | B02 | THE QUESTION | Remotion | `BrutalistHesitantWriter`: "the test" → "a positive" | GRAPHIC × remotion | machine |
> | B03 | TERMS | Remotion | `ClaudeDefinitions`: base rate, sensitivity, specificity | GRAPHIC × remotion | machine |
> | B10 | HOOK | Manim | `B10_YouArePositive`: one "you" square, terracotta POSITIVE stamp, MathTex P(sick) = ? | GRAPHIC × own | machine |
> | B11 | INSTANCE | Manim | `B11_TenThousand`: 125 × 80 isotype grid; 10 × 10 sick block scanned, 99 caught, 1 missed | GRAPHIC × own | machine |
> | B12 | INSTANCE | Manim | `B12_FalseAlarms`: scan over the 9,900 healthy, 9,405 fade, 495 stay lit | GRAPHIC × own | machine |
> | B13 | NAIVE | Manim | `B13_WrongCrowd`: box around the 10 × 10 sick block, MathTex 99/100, the 495 outside pulse | GRAPHIC × own | machine |
> | B14 | SHIFT · predict | Manim | `B14_OnlyThePositives`: negatives fade, 594 positives regroup 27 × 22, hold ≥ 3 s | GRAPHIC × own | machine |
> | B15 | TRANSFORM | Manim | `B15_OneInSix`: squares stack into 99/594, which reduces to 1/6 | GRAPHIC × own | machine |
> | B16 | ABSTRACTION | Manim | `B16_BuildBayes`: counts ÷ 10,000 → P(+\|D)P(D)/P(+) → P(A\|B) = P(B\|A)P(A)/P(B) | GRAPHIC × own | machine |
> | B17 | TANGENT | Manim | `B17_ReadTheLine`: split stage, five zones, box spotlights | GRAPHIC × own | machine |
> | B18 | PAYOFF | Manim | `B18_BackToYou`: B10's "you" square returns into the 594 block; 1/100 → 1/6 | GRAPHIC × own | machine |
> | B19 | BOUNDARY | Manim | `B19_BaseRateDial`: P(D\|+) vs base rate (log x); ValueTracker marker sweep | GRAPHIC × own | machine |
> | BVDT | VERDICT | Remotion | `ClaudeVerdictArtifact` (4 lines) | GRAPHIC × remotion | machine |
> | BHTF | YOUR TURN | Remotion | `ClaudeComposerAsk`: "Test Positive Twice" | GRAPHIC × remotion | machine |
> | BOUT | OUTRO | Remotion | `ClaudeTitleOutro` (locked) | GRAPHIC × remotion | machine |
>
> The pantry is empty by design. Every visual is computed (EXECUTABLE-EVIDENCE.md, and the tldr rule PURE MANIM IN THE LESSON). There are no stills, no AI footage and no shopping list.
>
> ## Library-first (GATE L), 2026-11-22
> All queries were run as `scene_search.py "<need>" --no-log`.
>
> **Queries tried**
> - "isotype grid of people"
> - "1000 dots population grid"
> - "bayes theorem probability tree"
> - "equation spotlight glossary"
>
> **Remotion hits.** All were film-specific figures (SycCurriculumStages, CwcDecompositionTree, HorrorEquation) that expose only `sparkLine`, or mascot and catalog grids. None can be reused for a filterable 10,000-mark grid. `ExecutedData` (probability comparison mode) was considered for B19. It was declined because tldr LEARN beats are pure Manim and the marker must persist from B15.
>
> **Manim leads to reuse in `scenes.py`.** These are copied into the reel's `scenes.py` as code, not imported from the toolkit, so GATE A's isolated copy stays self-contained.
> - `skills/make/explainer/manim/animated_graphics.py::IsotypeGrid`: one mark per unit in reading order, coloured by category, with `count_up(run_time)`.
>   - It builds one `Square` per mark. At 10,000 marks that is slow, so build one VMobject per category with many subpaths. Keep `IsotypeGrid` for the reading-order layout math and the count-up idea.
>   - It positions marks with `RIGHT*(i%per_row)*(size+gap)`. Built layout: per_row = 125 × 80 rows, size 0.058, gap 0.010 (pitch 0.068). The grid spans 8.5 × 5.44 u, centred near x = −1.4, with the counters in a column at x ≈ 4.3. That stays within ±6.0 × ±3.2 and fills more than 55% of the canvas. A 100 × 100 grid at this pitch would be 6.4 u tall, the whole ±3.2 band, so it was rejected. The sick are a 10 × 10 block (100 cells) in the top-left corner, so they read as countable squares; a 100-cell row read as a hairline at preview.
> - `animated_graphics.py::EquationTangent`, together with `EquationCard`, `SentencePair`, `GlossaryTable`, `WorkedExample` and `ValuesClaim`: the five-zone tangent template for B17.
> - `animated_graphics.py::HandRing`: optional ring for the 1 missed square in B11.
>
