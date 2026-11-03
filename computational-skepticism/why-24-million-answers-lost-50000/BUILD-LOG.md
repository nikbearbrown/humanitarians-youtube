# Build Log — Why 2.4 Million Answers Lost to 50,000

- **Reel Slug**: `why-24-million-answers-lost-50000`
- **Course**: *Computational Skepticism for AI* by Professor Nik Bear Brown
- **Source**: Chapter 6 (*Bias: Where It Enters and Who Is Responsible*)
- **Candidate Card**: Candidate 07 (*Why 2.4 Million Answers Lost to 50,000*)
- **Score**: 9/10
- **Narrator**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Chassis**: `course-skepticism` (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757` single accent, EB Garamond + UI sans)
- **Visual Object**: The Estimation Target / Off-Center Distribution (Responses accumulating tightly around biased center $\theta + \text{Bias}$ vs True Parameter $\theta$)
- **Manim Move**: `accumulate`

---

## 1. Candidate Spec & Binding Exclusions Audit

| Candidate Item | Spec Requirement | Implementation & Verification | Status |
|---|---|---|---|
| **Hook** | 1936 Literary Digest poll: 2.4M responses vs Gallup's 50,000 | B00 hesitancy open and B01–B02 establish 2.4M poll vs 50k election outcome | **PASS** |
| **Core Idea** | Bias is property of estimator & frame; more data narrows scatter around wrong answer | B06–B07 introduce formal bias $\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$ and sampling frame error | **PASS** |
| **Visual Object** | Target with responses accumulating tightly off-center | B03 plants anchor target; B08–B09 accumulate 2.4M points around biased point | **PASS** |
| **Manim Move** | `accumulate` kinetic progression | B08–B09 animate kinetic accumulation of points tightening variance around biased mean | **PASS** |
| **Prerequisites** | Averages, basic sampling concept | Follows plain intuitive setup; formal definition grounded in expected value | **PASS** |
| **Exclusion 1** | No 10-mechanism taxonomy | Zero taxonomy enumeration; focus kept squarely on sampling frame bias | **PASS** |
| **Exclusion 2** | No formula beyond $\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$ | Formula restricted strictly to $\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$ | **PASS** |
| **Exclusion 3** | No inverse probability weighting | Zero mention of IPW or reweighting schemes | **PASS** |

---

## 2. Six-Move Pedagogical Audit (Plain Register)

1. **Move 1 — Stakes First (B00–B02)**:
   - Cold open with `BrutalistHesitantWriter` types naive premise (*"If we collect millions of responses, won't big data always beat smaller samples?"*), deletes and corrects to *"When 2.4 Million Answers Lost to 50,000"*.
   - B01 presents the 1936 Literary Digest poll: 10 million ballots mailed, 2.4 million returned, predicting Landon by 57%.
   - B02 shows the actual election: Roosevelt won by 60.8% in a 46-state landslide, correctly called by George Gallup with only 50,000 respondents.
2. **Move 2 — Wrong Guess & Falsifying Case (B04–B05)**:
   - B04 articulates the Volume Reflex: *"Surely two point four million answers cancel out any small sample errors."*
   - B05 delivers the falsifying statistical breakdown: The poll had near-zero variance, yet suffered a massive 16.2% systematic offset.
3. **Move 3 — Epistemic Mechanism (B06, B07, B10)**:
   - B06 defines statistical bias rigorously: $\text{Bias}(\hat{\theta}) = E[\hat{\theta}] - \theta$.
   - B07 exposes the sampling frame: telephone directories, car registrations, and magazine subscriber lists systematically skewed toward affluent anti-New Deal voters.
   - B10 (One Flag) delivers the critical limitation: Larger sample size $N \to \infty$ reduces standard error $\sigma/\sqrt{N} \to 0$, but leaves systematic bias $\text{Bias}(\hat{\theta})$ completely untouched.
4. **Move 4 — Anchor Planted & Paid Off (B03, B08, B09)**:
   - B03 plants the estimation target visual comparing True Parameter $\theta$ with Biased Estimator Center $\theta + \text{Bias}$.
   - B08 applies the `accumulate` move: dots flood onto the target, clustering tightly away from the true center.
   - B09 pays off the anchor: 2.4 million points collapse into a dense cluster around the wrong answer, visualizing that volume only buys confidence in an error.
5. **Move 5 — Both Directions (B11–B12)**:
   - Direction A (B11): Massive dataset scale ($N$) does NOT guarantee an unbiased or representative estimator.
   - Direction B (B12): A small dataset ($N$) with representative sampling does NOT mean low precision or poor validity.
6. **Move 6 — Carry-Out Sentence (BCRY)**:
   - *"More data only narrows the scatter around the wrong answer — when your sampling frame is biased, volume gives you convergence to an error with absolute confidence."*
   - Delivered in Remotion `WantQuote` serif typography with terracotta quotation marks.

---

## 3. Production Gates Verification

- **Audio Generation**: Kokoro `am_onyx` synthesized per-beat narration across 16 beats (178.4 s total duration).
- **Gate Audio**: PASS — `mean_volume: -23.9 dB`, `max_volume: -2.9 dB` (exceeds −40 dB threshold).
- **Gate T (Typography)**: PASS — line budgets, word ceilings, and bookend exemptions verified with `type_check.py`.
- **Gate V (Visual QC)**: PASS — verified safe margins, contrast ratios, single terracotta accent per beat, crisp serif/sans typography, and kinetic `accumulate` point distribution animations.
- **Composition & Assembly**: `compile.py` generated `why-24-million-answers-lost-50000.mp4` (4K 3840×2160, 24fps) with all 16 slots filled.
- **4K Master**: `why-24-million-answers-lost-50000-4k.mp4` created and verified.

---

## 4. Delivery Status

- **Outbox**: `DELIVERY-course/why-24-million-answers-lost-50000/` staged with 4K master and YouTube description.
- **Repository**: `humanitarians-youtube/computational-skepticism/why-24-million-answers-lost-50000/` staged with all text artifacts (no media).
- **YouTube Metadata**: `why-24-million-answers-lost-50000.md` with Playlist: *Computational Skepticism — Bias & Fairness* and code link.
