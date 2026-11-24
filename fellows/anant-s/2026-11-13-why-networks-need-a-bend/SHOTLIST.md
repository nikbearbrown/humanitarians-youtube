# SHOTLIST — Why Neural Networks Need a Bend

| Beat | Act | Lane | Component / scene | Shot type × source | Fill |
|---|---|---|---|---|---|
| B00 | ASK | Remotion | `ClaudeComposerAsk` ("Jambo, Liam") | GRAPHIC × remotion | machine |
| B01 | BLUF | Remotion | `BrutalistHesitantWriter` ("Stacking more layers" → "A bend between layers") | GRAPHIC × remotion | machine |
| B02 | FRAMEWORK | Manim | `B02_TwoMoves`: one grid through a matrix (stays straight), then through ReLU (creases); 'bend' boxed | GRAPHIC × own | machine |
| B03 | WORKED_EXAMPLE | Manim | `B03_Collapse`: MathTex matrices, two computation paths, both give (7, 8); box on "=" | GRAPHIC × own | machine |
| B04 | MECHANISM | Manim | `B04_TenLayers`: 1,000-point cloud through ten layers vs one matrix; gap counter; bias identity | GRAPHIC × own | machine |
| B05 | MECHANISM | Manim | `B05_NoLine`: XOR square, sweeping line, "best 3 of 4" tally, four-inequality proof | GRAPHIC × own | machine |
| B06 | MECHANISM | Manim | `B06_StuckAtHalf`: deep-linear loss curve flattens at ¼; output bars at ½ next to best-line bars | GRAPHIC × own | machine |
| B07 | WORKED_EXAMPLE | Manim | `B07_ReluFix`: MathTex h = ReLU(Wx + c), y = wᵀh; row-by-row table; box on the −1 → 0 clip | GRAPHIC × own | machine |
| B08 | MECHANISM | Manim | `B08_Fold`: points move to z-space, ReLU fold, separating line, unfold to a band | GRAPHIC × own | machine |
| B09 | FALSIFIABILITY | Manim | `B09_HundredSeeds`: two 10×10 seed grids (2 units: 18/100, 8 units: 91/100); dead-unit inset | GRAPHIC × own | machine |
| B10 | FALSIFIABILITY | Manim | `B10_StraightAgain`: diagonal trace with two kinks, straight past the data to (3,3) → −4 | GRAPHIC × own | machine |
| BVDT | VERDICT | Remotion | `ClaudeVerdictArtifact`, 6 lines | GRAPHIC × remotion | machine |
| BHTF | YOUR_TURN | Remotion | `ClaudeComposerAsk` ("Your turn.") | GRAPHIC × remotion | machine |
| BOUT | OUTRO | Remotion | `ClaudeTitleOutro` (locked) | GRAPHIC × remotion | machine |

The pantry is empty by design. Every visual is computed (EXECUTABLE-EVIDENCE.md); there are no stills and no AI footage.

**REBUILD note.** B08's fold is our own executed geometry, not a copy of *Deep Learning* Fig. 6.1, but it shows the same idea. Caption it once, small: "Weights and idea: Goodfellow, Bengio & Courville (2016), §6.1". B07 carries the same citation for its weights.

**Math.** Every matrix and equation is Manim `MathTex`, and each beat's TeX strings are listed in `shot.manim.mathtex`. No TeX goes into any Remotion prop. The BVDT lines are plain sentences with no notation.

**Library-first (GATE L), 2026-11-22.** All queries were run with `scene_search.py --no-log`, so nothing was written to TEMPLATE-MISSES.md. The queries:
- "matrix multiplication worked example"
- "grid transformed by a matrix linear map"
- "relu activation function graph"
- "xor points no line separates"
- "neural network layer diagram"
- "training loss curve flattens"
- "grid of trials success failure"
- "piecewise linear function kinks"

Every hit was a film-specific figure with hard-coded content and only a `sparkLine` prop: ExampleSkill*, Graphing*, Cadences*, Sleeper*, Brand*, LinearApi*. None is reusable here. `ClaudeScienceLayerStack` (props `layers`, `caption`) was considered for the B02 network strip. It was rejected because B02's point is the grid transform performing itself, and that is Manim's lane: "moving mechanism / math / geometry → Manim" (nopunt). The genuine misses (matrix-grid transform, XOR sweep, seed-grid outcome) are candidate library components. They were not logged, because this planning session must not write into the toolkit; the main session can log them with `--reel`.
