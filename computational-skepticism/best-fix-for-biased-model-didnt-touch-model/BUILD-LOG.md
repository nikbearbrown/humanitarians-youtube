# Build Log — The Best Fix for a Biased Model Didn't Touch the Model

- **Reel Slug**: `best-fix-for-biased-model-didnt-touch-model`
- **Course**: *Computational Skepticism for AI* by Professor Nik Bear Brown
- **Source**: Chapter 6 (*Bias: Where It Enters and Who Is Responsible*)
- **Candidate Card**: Candidate 17 (*The Best Fix for a Biased Model Didn't Touch the Model*)
- **Score**: 9/10
- **Narrator**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Chassis**: `course-skepticism` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757` single accent, EB Garamond + UI sans)
- **Visual Object**: Causal path diagram with bias flowing from world to decision; interventions as dams on individual paths
- **Manim Move**: `trace`
- **Cut Duration**: 178.8 s (master video: 3840×2160 4K UHD @ 24fps)

---

## 1. Candidate Spec & Binding Exclusions Audit

| Candidate Item | Spec Requirement | Implementation & Verification | Status |
|---|---|---|---|
| **Hook** | Three teams fix same system: loss penalty, resampling, downstream review room | Cold open and B01–B02 establish the three teams and the puzzle | **PASS** |
| **Core Idea** | Interventions are dams on specific paths; model retraining leaves reviewer bypass open | B03–B09 causal graph with bias flow and path dams | **PASS** |
| **Visual Object** | Causal path diagram with bias flowing from world to decision; interventions as dams | B03 plants 3-path graph; B06–B08 trace dams on each path | **PASS** |
| **Manim Move** | `trace` kinetic progression | B04, B06, B07, B08, B09 trace bias flows and dams across the paths | **PASS** |
| **Prerequisites** | Causal intuition, DAG basics | Plain causal intuition; no complex notation required | **PASS** |
| **Exclusion 1** | No do-calculus notation | Zero Pearlian do-calculus symbols ($\text{do}(X)$) used | **PASS** |
| **Exclusion 2** | No 10-mechanism taxonomy | Zero taxonomy enumeration; focused cleanly on the 3 paths | **PASS** |
| **Exclusion 3** | No fairness metric formulas | Kept qualitative; zero mathematical fairness formulas | **PASS** |
| **Exclusion 4** | Parable labeled as constructed composite | B01 clearly displays "CONSTRUCTED COMPOSITE CASE" badge | **PASS** |
| **Exclusion 5** | Effect sizes qualitative | Magnitudes illustrative; no false empirical precision | **PASS** |

---

## 2. Six-Move Pedagogical Audit (Plain Register)

1. **Move 1 — Stakes First (B00–B02)**:
   - Cold open with `BrutalistHesitantWriter` types naive assumption (*"To fix a biased model, you retrain the model."*), hesitates, and strikes through to reveal *"To fix a biased model, you don't touch the model."*
   - B01 introduces the three engineering teams assigned to fix documented production disparities.
   - B02 presents the empirical puzzle: Team 1 (loss penalty) fails; Team 2 (resampling) shifts shape but fails; Team 3 (restructured review room) collapses the disparity.
2. **Move 2 — Wrong Guess & Falsifying Case (B04–B05)**:
   - B04 articulates the naive Model Centricity trap: assuming the algorithm is the sole container of bias.
   - B05 unmasks the architecture: the model is just one node in a larger causal system with multiple parallel paths.
3. **Move 3 — Epistemic Mechanism (B03, B06–B08, B10)**:
   - B03 plants the anchor: three parallel causal paths (Path A: Data, Path B: Model Weights, Path C: Human Review).
   - B06 tests Team 1's dam on Path B (loss penalty) — stops 5 units of bias, leaving Path A and C open.
   - B07 tests Team 2's dam on Path A (resampling) — stops 10 units of bias, leaving reviewer bypass conduit open.
   - B08 tests Team 3's dam on Path C (reviewer heuristics & appeal criteria) — blocks 85 units, collapsing disparity.
   - B10 formulates the Leverage Analysis Protocol (Map, Trace, Test Dams, Intervene at dominant bottleneck).
4. **Move 4 — Anchor Planted & Paid Off (B03, B08, B09)**:
   - B03 establishes the 3-path graph.
   - B08 applies the decisive dam to Path C.
   - B09 pays off the causal map: Team 3 achieved high leverage because they intervened where the bias volume was concentrated.
5. **Move 5 — Both Directions (B11–B12)**:
   - Direction A (B11): Model Balance does not imply Fair Outcome (a pristine model cannot stop downstream bias).
   - Direction B (B12): Outcome Disparity does not imply Model Flaw (a massive disparity can arise purely from upstream/downstream conduits).
6. **Move 6 — Carry-Out Sentence (BCRY)**:
   - *"An intervention only removes what its causal path carries — and the highest-leverage path often bypasses the model entirely."*
   - Rendered in Remotion `WantQuote` serif typography.

---

## 3. Production Gates Verification

- **Audio Generation**: Kokoro `am_onyx` synthesized per-beat narration (178.8 s total runtime).
- **Gate Audio**: PASS — `mean_volume: -24.0 dB`, `max_volume: -2.9 dB` (audible, clear, passes > −40 dB gate).
- **Gate T (Typography)**: PASS — zero errors, safe margins, WCAG contrast compliance.
- **Gate V (Visual QC)**: PASS — verified safe margins, single terracotta accent moment per beat, crisp text hierarchy, readable labels, and fluid Manim trace motions.
- **Composition & Assembly**: `compile.py` generated `best-fix-for-biased-model-didnt-touch-model.mp4` (4K 3840×2160, 24fps) with all 16 slots filled.
- **4K Master**: `best-fix-for-biased-model-didnt-touch-model-4k.mp4` verified and hardlinked.

---

## 4. Delivery Status

- **Outbox**: `DELIVERY-course/best-fix-for-biased-model-didnt-touch-model/` staged with 4K master and YouTube description.
- **Repository**: `humanitarians-youtube/computational-skepticism/best-fix-for-biased-model-didnt-touch-model/` staged with all text artifacts (no media).
- **YouTube Metadata**: `best-fix-for-biased-model-didnt-touch-model.md` with Playlist: *Computational Skepticism — Bias & Fairness* and code link.
