# Build Log — Why Three Reasonable Fairness Definitions Cannot All Be True

- **Reel Slug**: `why-three-reasonable-fairness-definitions-cannot-all-be`
- **Course**: *Computational Skepticism for AI* by Professor Nik Bear Brown
- **Source**: Chapter 7 (*Fairness Metrics: Choosing a Definition and Defending It*)
- **Candidate Card**: Candidate 18 (*Why Three Reasonable Fairness Definitions Cannot All Be True*)
- **Score**: 8/10
- **Narrator**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Chassis**: `course-skepticism` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757` single accent, EB Garamond + UI sans)
- **Visual Object**: The odds identity balance $v/(1-v) = p/(1-p) \cdot t/f$ as a balance whose base-rate weight, once moved, forces the error-rate side to tilt
- **Manim Move**: `transform`
- **Cut Duration**: 192.1 s (master video: 3840×2160 4K UHD @ 24fps)

---

## 1. Candidate Spec & Binding Exclusions Audit

| Candidate Item | Spec Requirement | Implementation & Verification | Status |
|---|---|---|---|
| **Hook** | ProPublica said COMPAS was biased; its maker said it was fair — and both were arithmetically correct. | Cold open (B00) and B01 establish both sides and their simultaneous mathematical validity. | **PASS** |
| **Core Idea** | Bayes' rule ties precision to base rate times the error-rate ratio, so enforcing calibrated scores across groups with different base rates forces their error rates apart — a four-line theorem, not a tooling gap. | B05–B09 formulate Bayes' rule into odds form and prove the impossibility theorem. | **PASS** |
| **Visual Object** | The odds identity balance as a balance whose base-rate weight forces the error-rate side to tilt | B06 plants the balance, B07 transforms to 2 groups, B08 demonstrates tilt. | **PASS** |
| **Manim Move** | `transform` kinetic progression | B07 implements `transform` morphing single-group balance into the ratio of error rates vs base rates. | **PASS** |
| **Prerequisites** | Conditional probability, TPR/FPR, base rate | Only plain conditional probabilities, rates, and base rates assumed. | **PASS** |
| **Exclusion 1** | No demographic-parity extension | Zero demographic parity / statistical parity formulas introduced. | **PASS** |
| **Exclusion 2** | No Kleinberg three-way proof | Focuses strictly on Chouldechova's odds formulation (calibration vs error rates). | **PASS** |
| **Exclusion 3** | No COMPAS history beyond one line | Limited strictly to one-line context in B01; no deep historical dive. | **PASS** |
| **Exclusion 4** | No debiasing toolkit | Explains the epistemic impossibility and stops; zero tooling recommendations. | **PASS** |

---

## 2. Six-Move Pedagogical Audit (Plain Register)

1. **Move 1 — Stakes First (B00–B03)**:
   - Cold open (B00) with `BrutalistHesitantWriter` types naive assumption (*"If an AI model has calibrated scores, shouldn't its error rates be equal across groups?"*), hesitates on "be equal across groups?", corrects to "diverge across groups?". Liam reads over typing.
   - B01 presents the COMPAS dispute: ProPublica (diverging false positives) vs Northpointe (calibrated risk scores); both arithmetically correct.
   - B02 formalizes Definition 1: Calibration Parity (predictive parity / score honesty).
   - B03 formalizes Definitions 2 & 3: Equalized Odds (FPR parity and TPR parity).
2. **Move 2 — Wrong Guess & Falsifying Case (B04)**:
   - Articulates the Tooling Fallacy: the assumption that a larger dataset, better features, or cleaner optimization could reconcile both definitions. Falsified: no algorithm can satisfy both.
3. **Move 3 — Epistemic Mechanism (B05–B08)**:
   - B05 defines the four fundamental Bayes quantities: base rate $p$, true positive rate $t$, false positive rate $f$, precision $v$.
   - B06 derives the Odds Identity: $v/(1-v) = [p/(1-p)] \cdot (t/f)$.
   - B07 applies the MANIM MOVE `transform`: compares Group A and Group B, calibration locks precision ratio to 1, tying error-rate ratio directly to base rates.
   - B08 illustrates the tilted balance: when base rates differ, error-rate ratio must tilt in compensation.
4. **Move 4 — Anchor Planted & Paid Off (B06, B09)**:
   - B06 plants the balance scale.
   - B09 pays off the four-line impossibility theorem: equalized odds forces error ratio to 1.0, which contradicts unequal base rates. One definition must break.
5. **Move 5 — One Flag & Degenerate Escapes (B10)**:
   - Explicitly flags the arithmetic's only two escapes: identical base rates across groups, or zero prediction errors ($t=1, f=0$). Notes that in real-world social evaluations, neither ever happens.
6. **Move 6 — Both Directions (B11–B12)**:
   - Direction A (B11): Calibration ⇏ Equal Error Rates (calibrated scores across unequal base rates guarantee diverging false-positive rates).
   - Direction B (B12): Equal Error Rates ⇏ Calibration (equalizing error rates across unequal base rates guarantees that identical scores mean different probabilities).
7. **Move 7 — Carry-Out Sentence (BCRY)**:
   - *"Calibrating scores across groups with different base rates forces their error rates apart — the conflict is Bayes' rule, not a tooling gap."*
   - Rendered in Remotion `WantQuote` serif typography.
8. **Move 8 — Your Turn (BHTF)**:
   - Interactive prompt for Claude / AI assistants challenging the viewer to inspect base rates, FPRs, and PPVs in their organization's models to see which definition was chosen and who signed off on the one that broke.
9. **Move 9 — Outro (BOUT)**:
   - `OutroCTA` with "@HumanitariansAI", "Why Three Reasonable Fairness Definitions Cannot All Be True. Liam, in for Bear."

---

## 3. Production Gates Verification

- **Audio Generation**: Kokoro `am_onyx` synthesized per-beat narration (192.1 s total runtime).
- **Gate Audio**: PASS — `mean_volume: -23.9 dB`, `max_volume: -1.7 dB` (audible, clear, passes > −40 dB gate).
- **Gate T (Typography)**: PASS — checked via `type_check.py`, 16 beats checked, 0 FAILs, min text height, margins, contrast, no wordy cards.
- **Gate V (Visual QC)**: PASS — verified 19 sample frames across timeline; clear EB Garamond serif titles, UI sans labels, safe margins (>10%), humanitarians palette (`#FAF9F5`, `#3D3929`, `#D97757`), no overlapping text, clean balance illustrations.
- **Composition & Assembly**: `compile.py` generated `why-three-reasonable-fairness-definitions-cannot-all-be.mp4` (4K 3840×2160, 24fps) with all 16 slots filled.
- **4K Master**: `why-three-reasonable-fairness-definitions-cannot-all-be-4k.mp4` verified and hardlinked.

---

## 4. Delivery Status

- **Outbox**: `DELIVERY-course/why-three-reasonable-fairness-definitions-cannot-all-be/` staged with 4K master and YouTube description.
- **Repository**: `humanitarians-youtube/computational-skepticism/why-three-reasonable-fairness-definitions-cannot-all-be/` staged with all text artifacts (no media).
- **YouTube Metadata**: `why-three-reasonable-fairness-definitions-cannot-all-be.md` with Playlist: *Computational Skepticism — Bias & Fairness* and code link.
