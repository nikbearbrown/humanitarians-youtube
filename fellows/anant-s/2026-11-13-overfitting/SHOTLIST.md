# SHOTLIST — Overfitting, When a Perfect Score Lies

| Beat | Act | Lane | Component / scene | Shot type × source | Fill |
|---|---|---|---|---|---|
| B00 | ASK | Remotion | `ClaudeComposerAsk` (Namaste, Liam), with three result lines | GRAPHIC × remotion | machine |
| B01 | BLUF | Remotion | `BrutalistHesitantWriter`: "means a perfect model" → "can mean memorized noise" | GRAPHIC × remotion | machine |
| B02 | FRAMEWORK | Manim | `B02_Setup`: hidden sin(πx) curve, 16 noisy training dots, a locked 1,000-point test box | GRAPHIC × own | machine |
| B03 | FRAMEWORK | Manim | `B03_ErrorMeasure`: MathTex MSE with box spotlights, glossary, and one real worked term | GRAPHIC × own | machine |
| B04 | WORKED_EXAMPLE | Manim | `B04_ThreeFits`: degree 1 / 3 / 15 panels on the same dots, train and test counters | GRAPHIC × own | machine |
| B05 | MECHANISM | Manim | `B05_TheU`: training and test error over degrees 0–15, noise-floor line, test curve exits the chart | GRAPHIC × own | machine |
| B06 | FALSIFIABILITY | Manim | `B06_MoreData`: one degree-15 model refit as n grows 16 → 1,000; train ↑ and test ↓ meet at the floor | GRAPHIC × own | machine |
| B07 | FALSIFIABILITY | Manim | `B07_PeekedScore`: train/validation/test strip; two 10×10 trial grids (70% vs 55%), control chip 53% | GRAPHIC × own | machine |
| BVDT | VERDICT | Remotion | `ClaudeVerdictArtifact`, six lines | GRAPHIC × remotion | machine |
| BHTF | YOUR_TURN | Remotion | `ClaudeComposerAsk` (Your turn.), prompt plus three check lines | GRAPHIC × remotion | machine |
| BOUT | OUTRO | Remotion | `ClaudeTitleOutro` (locked) | GRAPHIC × remotion | machine |

The pantry is empty by design: every visual is computed (EXECUTABLE-EVIDENCE.md). There are no stills and no AI footage.

**Motion languages** (budget: no single one in more than about 40% of beats):
- Type-on: B00, BHTF.
- Hesitant type: B01.
- Draw-on plus dots landing: B02, B05.
- Spotlight walk: B03.
- Three-panel simultaneous draw: B04.
- Live refit as data grows: B06.
- Trial grids filling: B07.
- Artifact-in: BVDT.
- Outro: BOUT.

**Library-first (GATE L), 2026-11-22.** Searched with `scene_search.py --no-log`, so nothing was written to TEMPLATE-MISSES.md.
- Queries:
  - "polynomial fit through noisy data points"
  - "training error versus test error curve"
  - "train test split of a dataset"
  - "three side-by-side panels comparing models"
  - "grid of trials colored by outcome"
  - "mean squared error equation with symbol glossary"
- **Hits:** film-specific figures with hard-coded content (WantFig1Scale, ConfluenceApiDesign, WebappTestingAnatomy, CadencesFig6Tide, HorrorEquation) that expose only a `sparkLine` prop, plus mascot grids. None is reusable.
- **Considered:** the generic `ExecutedData`. Manim was chosen instead because:
  - the curves must refit live (B06);
  - the series must land degree by degree on spoken cues (B05);
  - the equation needs box spotlights (B03).

  Plotted curves and morphing structure are Manim's lane (nopunt catalog: "A trend / scaling curve / non-monotonic" → Manim).
- **Recorded misses for the main session to log with `--reel` if wanted:** "training vs test error curve" and "train/validation/test split strip". Both are reusable shapes for later ML films (e.g. film 4+).
