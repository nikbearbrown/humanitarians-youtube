# Build Log — The Dataset With Zero Errors That's Still Poison

- **Reel Slug**: `dataset-with-zero-errors-thats-still-poison`
- **Course**: *Computational Skepticism for AI* by Professor Nik Bear Brown
- **Source**: Chapter 6 (*Bias: Where It Enters and Who Is Responsible*)
- **Candidate Card**: Candidate 06 (*The Dataset With Zero Errors That's Still Poison*)
- **Score**: 9/10
- **Narrator**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Chassis**: `course-skepticism` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757` single accent, EB Garamond + UI sans)
- **Visual Object**: The 5-Node Feedback Loop (Past World → Faithful Record → Trained Model → Automated Decisions → Future World)
- **Manim Move**: `trace`

---

## 1. Candidate Spec & Binding Exclusions Audit

| Candidate Item | Spec Requirement | Implementation & Verification | Status |
|---|---|---|---|
| **Hook** | Representative sample, accurate labels, no mistakes — model still harmful | Cold open and B01–B02 establish 10-year clean archive with 0 errors | **PASS** |
| **Core Idea** | Historical bias ((Y_{\text{historical}} \mid x)$) makes accuracy the harm | B06 & B07 establish historical distribution vs fair distribution | **PASS** |
| **Visual Object** | 5-node loop from past world to future world | B03 plants anchor loop; B07, B08, B09 trace through to completion | **PASS** |
| **Manim Move** | `trace` kinetic progression | B07–B09 trace glowing terracotta pulse through the feedback cycle | **PASS** |
| **Prerequisites** | Models learn from labeled data | No assumed advanced math; strictly follows labeled data foundation | **PASS** |
| **Exclusion 1** | No fairness-impossibility theorem | Zero mention of impossibility theorems / Chouldechova / Kleinberg | **PASS** |
| **Exclusion 2** | No COMPAS detail | Zero COMPAS or recidivism scoring details | **PASS** |
| **Exclusion 3** | Single-line fix taxonomy limit | B10 carries exactly one line on predictive fit vs inheritance trade-off | **PASS** |

---

## 2. Six-Move Pedagogical Audit (Plain Register)

1. **Move 1 — Stakes First (B00–B02)**:
   - Cold open with `BrutalistHesitantWriter` types naive assumption, pauses, and corrects "unbiased" to "poison".
   - B01 presents 10-year promotion archive with verified 0 data-entry errors and 100% accurate labels.
   - B02 shows model scorecard with 94.2% accuracy and converged diagnostics.
2. **Move 2 — Wrong Guess & Falsifying Case (B04–B05)**:
   - B04 articulates the naive Quality Reflex: *"The labels are clean, so the pipeline is clean."*
   - B05 falsifies it with historical reality: 3x promotion disparity for men vs equally qualified women faithfully recorded.
3. **Move 3 — Epistemic Mechanism (B06, B07, B10)**:
   - B06 contrasts (Y_{\text{historical}} \mid x)$ against (Y_{\text{fair}} \mid x)$.
   - B07 traces historical signal entering training data and loss function rewarding proxy features.
   - B10 (One Flag) states the fundamental trade-off: technical fixes spend predictive fit on past data to inherit less of the past.
4. **Move 4 — Anchor Planted & Paid Off (B03, B08, B09)**:
   - B03 plants the 5-node circular feedback loop.
   - B08 advances the trace to automated decisions rejecting qualified applicants from historically excluded groups.
   - B09 completes the loop: automated decisions shape the future world, generating the next round of biased training data.
5. **Move 5 — Both Directions (B11–B12)**:
   - Direction A (B11): Zero data-entry errors and clean labels do NOT guarantee an unbiased or safe model.
   - Direction B (B12): A biased outcome from such a model does NOT imply that data was corrupt, noisy, or mislabeled.
6. **Move 6 — Carry-Out Sentence (BCRY)**:
   - *"When a dataset faithfully records a discriminatory past, the model's accuracy is the harm — it projects what was into what will be, and calls the projection truth."*
   - Delivered in Remotion `WantQuote` serif typography.

---

## 3. Production Gates Verification

- **Audio Generation**: Kokoro `am_onyx` synthesized per-beat narration (197.44 s total duration).
- **Gate Audio**: PASS — `mean_volume: -23.9 dB`, `max_volume: -3.0 dB` (exceeds −40 dB threshold).
- **Gate T (Typography)**: PASS — line budgets, word ceilings, and bookend exemptions verified with `type_check.py`.
- **Gate V (Visual QC)**: PASS — verified safe margins ($\le 11.2$ width), contrast ratios, single terracotta accent moment per beat, readable serif/sans layout, and kinetic trace animations.
- **Composition & Assembly**: `compile.py` generated `dataset-with-zero-errors-thats-still-poison.mp4` (4K 3840×2160, 24fps) with all 16 slots filled.
- **4K Master**: `dataset-with-zero-errors-thats-still-poison-4k.mp4` staged and verified.

---

## 4. Delivery Status

- **Outbox**: `DELIVERY-course/dataset-with-zero-errors-thats-still-poison/` staged with 4K master and YouTube description.
- **Repository**: `humanitarians-youtube/computational-skepticism/dataset-with-zero-errors-thats-still-poison/` staged with all text artifacts (no media).
- **YouTube Metadata**: `dataset-with-zero-errors-thats-still-poison.md` with Playlist: *Computational Skepticism — Bias & Fairness* and code link.
