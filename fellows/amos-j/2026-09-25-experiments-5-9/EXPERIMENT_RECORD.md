# RAMAN Effect — complete experiment record

Every experiment run, with full per-seed data, statistics, and chart specifications
for building visualisations.

**Model:** LegacyCNN, 40,446 parameters, unless stated otherwise
**Test set:** 3,000 spectra, 100 per class, 30 classes, perfectly balanced
**Environment:** torch 2.11.0+cu128, RTX 3060, Python 3.12.10, ramanspy 0.2.10
**Protocol:** 100 pre-train epochs, 20 fine-tune epochs, `--val-split 0.33`, 3 or 6 seeds
**Statistics:** paired per-seed differences + McNemar on per-sample correctness

---

## 0. Headline

| Stage | Accuracy | Note |
|---|---|---|
| Documented starting point | 76.50% | single run, unreproducible, old code |
| Measured baseline, current code | 74.78% ± 1.04 | 3 seeds |
| After removing ASPLS | 83.89% ± 0.33 | 3 seeds |
| 3-model probability ensemble | 85.03% | single measurement |

**Net: +10.25 points over the measured baseline.** 9.11 of those came from one
deletion. Nine experiments; one moved accuracy materially.

---

## 1. Experiment summary — impact flags

| # | Experiment | Effect | p (pooled McNemar) | Impact |
|---|---|---|---|---|
| 1 | Seed-noise floor | 0.00 | n/a | ⬜ Infrastructure |
| 2 | Variance attribution by stage | 0.00 | n/a | ⬜ Diagnostic |
| **3** | **Preprocessing ablation (drop ASPLS)** | **+7.61 pts** | **2.5e-57** | 🟩 **MAJOR** |
| **3b** | **Also drop despike + SavGol** | **+1.50 pts** | **7.3e-06** | 🟩 **MINOR-REAL** |
| 4 | Architecture re-test (5 designs) | 0.00 | n/a | ⬜ Confirmatory |
| 5 | Phase-2 tuning (3 remedies) | +0.02 / −0.03 / +0.16 | 0.95 / 0.91 / 0.47 | ⬛ NULL |
| 6 | Longer fine-tuning (60 vs 20) | **−1.01 pts** | 3.4e-05 | 🟥 **NEGATIVE** |
| 7 | Incremental learning (new classes) | n/a | n/a | ⬜ Engineering result |
| **8** | **3-model ensemble** | **+0.80 pts** | **0.059** | 🟨 **MARGINAL** |
| 9 | Stage-1 augmentation on/off | +0.16 pts | 0.53 | ⬛ NULL (n=6) |

**Only experiments 3, 3b and 8 changed the deployed model.**

Legend: 🟩 adopted · 🟨 adopted with caveats · 🟥 rejected · ⬛ no effect · ⬜ no accuracy change by design

---

## 2. Noise floor — read this before interpreting any effect size

| Measurement | Seeds | sd | Notes |
|---|---|---|---|
| legacy_full pipeline | 3 | 1.04 | pre-ASPLS-removal |
| minmax_only pipeline | 3 | 0.33 | post-removal |
| minmax_only, augmented | 6 | **0.76** | revised upward at n=6 |
| minmax_only, no augment | 6 | **0.56** | revised upward at n=6 |
| Binomial floor at n=3000, p=0.84 | — | 0.67 | irreducible sampling error |

**Use 0.6–0.8 points as the working noise floor.** The 0.33 figure came from three
seeds and did not survive six. Any effect below ~1 point needs ≥6 paired seeds and a
per-sample test.

---

## 3. Experiment 1 — seed-noise floor

**Question:** how much does the result move with nothing changed but the random seed?

**Data (legacy_full pipeline):**

| Seed | Accuracy |
|---|---|
| 1 | 74.67 |
| 2 | 73.80 |
| 3 | 75.87 |

mean 74.78 · sd 1.04 · spread 2.07

**Determinism check:** two runs at seed 7 with `--augment` matched to full float
precision (val loss 1.1417966807683309 on both).

**Invalidated by this:** the documented "+1.40 from augmentation" claim and the
"73.23% ± 0.11%" cross-validation margin.

### Chart spec
- **Type:** horizontal bar, 3 bars
- **Axis:** x from 70 to 78 (full 0–100 hides the effect)
- **Series:** `[74.67, 73.80, 75.87]`, labels `Run 1/2/3`
- **Colour:** single neutral grey `#5A6B76`
- **Annotation:** shaded band or bracket spanning 73.80–75.87 labelled "2.07 pt spread"
- **Caption:** "Same settings, different seed. Anything smaller than this band is luck."

---

## 4. Experiment 2 — variance attribution by stage

**Question:** does stage 1 or stage 2 cause the wobble?

**Data:**

| Seed | After stage 1 | After stage 2 | Gain |
|---|---|---|---|
| 1 | 50.20 | 74.67 | +24.47 |
| 2 | 49.20 | 73.80 | +24.60 |
| 3 | 55.50 | 75.87 | +20.37 |
| **mean** | **51.63** | **74.78** | **+23.14** |
| **spread** | **6.30** | **2.07** | 4.23 |

Ratio spread(after)/spread(before) = **0.33**. Stage 2 *reduces* variance threefold.

**Prediction that failed:** I argued stage 2 was adding instability. It damps it.

**Secondary result:** fine-tuning is worth ~23 points for this model, not the 43
claimed in the docs (that figure came from one ResNet run).

### Chart spec
- **Type:** grouped horizontal bar, 3 categories × 2 series, or slope chart
- **Series A "After stage 1":** `[50.20, 49.20, 55.50]`, colour `#C05A3C`
- **Series B "After stage 2":** `[74.67, 73.80, 75.87]`, colour `#3F9E86`
- **Axis:** 40–80
- **Annotations:** "spread 6.30" on group A, "spread 2.07" on group B
- **Alternative:** slope chart with three lines converging left-to-right, which
  shows the damping more directly than bars

---

## 5. Experiment 3 — preprocessing ablation 🟩 THE ONE THAT MATTERED

**Question:** are the four ramanspy cleaning steps helping?

**Hypothesis:** the distributed arrays already lie in [0.0, 1.0] and are already
baseline-corrected, so ASPLS fits and subtracts the peak envelope rather than a
fluorescence baseline.

**Code change (`src/dataset.py`):**

```python
# before
DEFAULT_PIPELINE = (WhitakerHayes, SavGol(9,3), ASPLS, MinMax)
# after
DEFAULT_PIPELINE = (MinMax,)
```

### Full per-seed data

| Arm | Steps | Seed 1 | Seed 2 | Seed 3 | Mean | sd |
|---|---|---|---|---|---|---|
| legacy_full | WH + SG + ASPLS + MM | 74.67 | 73.80 | 75.87 | 74.78 | 1.04 |
| no_despike | SG + ASPLS + MM | 74.73 | 72.57 | 74.83 | 74.04 | 1.28 |
| no_savgol | WH + ASPLS + MM | 75.03 | 76.13 | 75.77 | 75.64 | 0.56 |
| no_aspls | WH + SG + MM | 82.37 | 82.93 | 81.87 | 82.39 | 0.53 |
| none | (nothing) | 83.27 | 84.17 | 83.23 | 83.56 | 0.53 |
| **minmax_only** | **MM** | **83.57** | **84.23** | **83.87** | **83.89** | **0.33** |

**The grouping is by ASPLS, not by step count.** Every arm with it: 74.0–75.6.
Every arm without: 82.4–83.9.

### Paired comparisons

| Comparison | Δ mean | 95% CI | McNemar b / c | pooled p |
|---|---|---|---|---|
| no_aspls − legacy_full | **+7.61** | [+3.71, +11.51] | 576 / 1261 | **2.5e-57** |
| minmax_only − no_aspls | **+1.50** | [+0.42, +2.58] | 379 / 514 | **7.3e-06** |
| none − no_aspls | +1.17 | [+0.57, +1.76] | 444 / 549 | 9.7e-04 |
| no_despike − no_aspls | −8.34 | [−12.76, −3.93] | 1331 / 580 | 5.6e-66 ⚠ |
| no_savgol − no_aspls | −6.74 | [−8.28, −5.21] | 1222 / 615 | 2.2e-45 ⚠ |

⚠ **Design flaw:** `no_despike` and `no_savgol` retain ASPLS, so these two rows
differ from the baseline by two steps, not one. The numbers are correct; the
comparison is not a clean single-step ablation.

Per-seed differences for the headline comparison: `+7.70, +9.13, +6.00`

**Side effect:** sd fell 1.04 → 0.33 at n=3. ASPLS injected instability as well as error.

**Prediction that failed:** I estimated +2 to +5 points. Actual +7.61.

### Chart spec — primary
- **Type:** horizontal bar, 6 arms, sorted ascending
- **Values:** `[74.04, 74.78, 75.64, 82.39, 83.56, 83.89]`
- **Labels:** `no_despike, legacy_full, no_savgol, no_aspls, none, minmax_only`
- **Colour by group:** contains-ASPLS `#C05A3C`, no-ASPLS `#3F9E86`
- **Axis:** 70–86
- **Error bars:** ± sd `[1.28, 1.04, 0.56, 0.53, 0.53, 0.33]`
- **Annotation:** horizontal divider between the two colour groups labelled
  "with / without ASPLS", plus a brace showing the ~8 point gap
- **Caption:** "p = 2.5e-57, three paired seeds"

### Chart spec — mechanism (recommended, not yet produced)
- **Type:** line overlay, one spectrum, three traces
- **Traces:** raw spectrum · after full 4-step pipeline · after minmax_only
- **Axis:** x = Raman shift 381.98–1792.40 cm⁻¹ (**descending in the file**,
  step −1.2; reverse for plotting), y = normalised intensity
- **Purpose:** shows the band area ASPLS removes. This is the single most
  persuasive figure available and has not been made yet.
- **Source:** `data/wavenumbers.npy` + one row of `data/X_reference.npy`

---

## 6. Experiment 4 — architecture re-test

**Question:** does the "smaller model wins" finding survive the corrected pipeline?

### Data (minmax_only, 3 seeds)

| Design | Params | Seed 1 | Seed 2 | Seed 3 | Mean | sd | Old (legacy_full, 1 seed) | Δ |
|---|---|---|---|---|---|---|---|---|
| **LegacyCNN** | 40,446 | 83.57 | 84.23 | 83.87 | **83.89** | **0.33** | 76.50 | +7.4 |
| Raman1DCNN | 262,510 | 78.00 | 79.17 | 81.50 | 79.56 | 1.78 | 69.90 | +9.7 |
| MultiscaleCNN | 193,358 | 75.20 | 73.53 | 75.07 | 74.60 | 0.89 | 63.73 | +10.9 |
| Transformer1D | 109,726 | 66.23 | 76.10 | 75.93 | 72.76 | **5.65** | 54.73 | +18.0 |
| FusionNet | 75,694 | 67.97 | 64.40 | 67.03 | 66.47 | 1.84 | 60.87 | +5.6 |

### Stage-1-only accuracy (reference checkpoint, before fine-tuning)

| Design | Seed 1 | Seed 2 | Seed 3 | Mean |
|---|---|---|---|---|
| LegacyCNN | 55.47 | 58.10 | 56.13 | 56.57 |
| Raman1DCNN | 47.83 | 51.30 | 51.30 | 50.14 |
| Transformer1D | 44.07 | 47.33 | 52.93 | 48.11 |
| MultiscaleCNN | 48.07 | 44.33 | 47.33 | 46.58 |
| FusionNet | 39.77 | 42.60 | 43.90 | 42.09 |

Fine-tuning gain is 24–29 points for **every** design. The domain gap is a property
of the data, not the model.

**Prediction that failed:** I argued twice that the capacity finding was an ASPLS
artifact. It survived, and is now supported by 15 runs instead of 5 single runs.

**Ordering change:** MultiscaleCNN now clearly beats FusionNet, so capacity does not
monotonically predict accuracy either. The real pattern is *pure CNN beats anything
with a transformer component; among CNNs the smallest wins*.

### Chart spec — primary
- **Type:** horizontal bar, 5 designs, sorted descending
- **Values:** `[83.89, 79.56, 74.60, 72.76, 66.47]`
- **Error bars:** `[0.33, 1.78, 0.89, 5.65, 1.84]`
- **Axis:** 60–88
- **Colour:** winner `#3F9E86`, rest `#5A6B76`
- **Secondary label:** parameter count under each design name

### Chart spec — capacity vs accuracy (the interesting one)
- **Type:** scatter, x = log parameters, y = accuracy, error bars = sd
- **Points:** `(40446, 83.89), (75694, 66.47), (109726, 72.76), (193358, 74.60), (262510, 79.56)`
- **Annotation:** mark the three pure CNNs vs the two transformer-containing designs
  in different markers. The CNN subset is the one showing the inverse trend.

### Chart spec — stability
- **Type:** horizontal bar of sd alone
- **Values:** `[0.33, 0.89, 1.78, 1.84, 5.65]`
- **Caption:** "LegacyCNN is 17× steadier than Transformer1D"

---

## 7. Experiment 5 — phase-2 tuning ⬛ NULL

**Question:** does instrumenting the fine-tuning stage help?

Fine-tuning previously: 20 epochs, no validation, no augmentation, weight decay
silently 0, last epoch saved.

### Data (3 seeds)

| Arm | Seed 1 | Seed 2 | Seed 3 | Mean | sd | Δ vs base | 95% CI | pooled p |
|---|---|---|---|---|---|---|---|---|
| p2_base | 83.57 | 84.23 | 83.87 | 83.89 | 0.33 | — | — | — |
| p2_val | 83.13 | 84.97 | 83.63 | 83.91 | 0.95 | +0.02 | [−1.53, +1.57] | 0.95 |
| p2_valaug | 83.37 | 84.30 | 83.90 | 83.86 | 0.47 | −0.03 | [−0.39, +0.33] | 0.91 |
| p2_valaugwd | 83.77 | 84.37 | 84.00 | 84.04 | 0.30 | +0.16 | [+0.06, +0.25] | 0.47 |

**⚠ Statistical trap worth documenting:** `p2_valaugwd`'s t-interval *excludes* zero
while its McNemar p is 0.47. The interval is narrow only because three per-seed
differences happened to land close (+0.20, +0.13, +0.13). At df=2 a t-interval
estimates its own spread from three numbers. Trust McNemar. Treat as zero.

**Best fine-tune epoch (of 20):** `[20, 17, 20]` — always at or near the maximum.

### Chart spec
- **Type:** horizontal bar, 4 arms
- **Values:** `[83.89, 83.91, 83.86, 84.04]`
- **Axis:** 80–86 (so the bars fill; at 0–100 they are indistinguishable anyway,
  which is arguably the honest presentation)
- **Colour:** all identical grey `#5A6B76` — the point is that nothing differs
- **Annotation:** "largest difference 0.18 pts = 5 samples of 3,000"

---

## 8. Experiment 6 — longer fine-tuning 🟥 NEGATIVE

**Question:** best-epoch was always last; is 20 epochs too few?

### Data

| Config | Seed 1 | Seed 2 | Seed 3 | Mean | sd |
|---|---|---|---|---|---|
| 20 epochs (base) | 83.57 | 84.23 | 83.87 | **83.89** | **0.33** |
| 60 epochs (base) | 83.13 | 83.87 | 81.63 | 82.88 | 1.14 |
| 60 epochs (+ val selection) | 83.20 | 84.43 | 81.50 | 83.04 | 1.47 |

**Paired, 60 vs 20:** Δ = **−1.01** pts, CI [−3.64, +1.62]
Per-seed: `−0.43, −0.37, −2.23`
McNemar per seed: `86/73 p=0.34`, `81/70 p=0.42`, `114/47 p=2.0e-07`
**Pooled: 281 / 190, χ² = 17.20, p = 3.4e-05**

**Best fine-tune epoch (of 60):** `[54, 56, 57]`

**The diagnosis, corrected:** best epoch tracks ~90% of whatever budget it is given
(17–20 of 20; 54–57 of 60). That is not a model still converging. It is a 300-sample
validation set unable to discriminate late epochs, picking one near the end at random.

**Prediction that failed:** I gave this a 40% chance of helping. It lost a point.

### Chart spec
- **Type:** two paired bars, or a dumbbell/slope chart with 3 seed lines
- **Panel 1 accuracy:** `[83.89, 82.88]`, axis 78–86, colours `#3F9E86` / `#C05A3C`
- **Panel 2 stability:** sd `[0.33, 1.14]`, axis 0–1.5, same colours
- **Annotation:** "best epoch = 17–20 of 20, and 54–57 of 60 → tracks the budget,
  not convergence"

---

## 9. Experiment 7 — incremental learning (new classes arrive)

**Setup:** 5 of 30 classes held out (labels **2, 10, 11, 21, 26**, holdout-seed 0).
Stage A model trained on the remaining 25 → **87.32%** on those 25.

### Config A — 100 new spectra per class (realistic)

| Strategy | Overall (30) | Old kept | New learned | Forgetting | Minutes |
|---|---|---|---|---|---|
| **retrain** | **83.97** | 86.28 | 72.4 | +1.04 | 3.24 |
| replay (20/class) | 74.60 | 84.88 | 23.2 | +2.44 | 0.042 |
| frozen backbone | 71.40 | 85.68 | 0.0 | +1.64 | 0.015 |
| naive (new only) | 66.87 | 79.24 | 5.0 | +8.08 | 0.037 |

### Config B — 2,000 new spectra per class

| Strategy | Overall | Old kept | New learned | Forgetting | Minutes |
|---|---|---|---|---|---|
| naive | 9.60 | 0.60 | 54.6 | **+86.72** | 0.80 |
| replay (20/class) | 71.63 | 82.76 | 16.0 | +4.56 | 0.81 |
| frozen backbone | 29.53 | 26.12 | 46.6 | +61.20 | 0.46 |

### Config C — 2,000 new per class, replay buffer 400/class

| Strategy | Overall | Old kept | New learned | Forgetting | Minutes |
|---|---|---|---|---|---|
| **retrain** | **83.97** | 86.28 | 72.4 | +1.04 | 3.37 |
| naive | 13.83 | 2.76 | 69.2 | +84.56 | 0.78 |
| replay (2,500 samples) | 73.00 | 85.88 | 8.6 | +1.44 | 0.96 |
| frozen backbone | 27.43 | 23.80 | 45.6 | +63.52 | 0.46 |

### Key findings

1. **Retrain wins in every configuration.** Best incremental result across all three
   is 74.60%; retrain is 83.97%. A 9.4-point gap for 2.4 extra minutes.
2. **The failure mode depends on new-data volume.** With 100/class, nothing much
   happens either way. With 2,000/class, naive collapses to 2.8% on old classes.
3. **🔬 Mechanistic result:** the frozen arm lost 63.5 points with *every* backbone
   parameter locked (36,576 frozen, 3,870 trainable). Classes 2 and 17 fell to
   exactly zero recall while their features were bit-identical. **Forgetting here is
   logit competition in the classifier head, not representation drift.** Points at
   head normalisation as an untested cheap fix.
4. **Retrain's own "forgetting" of +1.04 is the noise floor** for that metric — it is
   two independently trained models compared per class. Replay's +1.44 is therefore
   indistinguishable from zero.

**Predictions that failed:** I predicted catastrophic forgetting in Config A (got
plasticity failure); I predicted a larger replay buffer would help (new-class recall
fell 23.2 → 8.6).

### Chart spec — primary
- **Type:** grouped horizontal bar, 4 strategies × 2 series
- **Series "Old kept":** `[86.3, 85.9, 85.7, 79.2]` colour `#1C7293`
- **Series "New learned":** `[72.4, 23.2, 0.0, 5.0]` colour `#3F9E86`
- **Axis:** 0–100
- **Caption:** "Only retrain does both. It takes 3.4 minutes."

### Chart spec — stability/plasticity scatter (better for a technical audience)
- **Type:** scatter, x = new-class recall, y = old-class recall
- **Points (Config A):** `(72.4, 86.3) retrain`, `(23.2, 84.9) replay`,
  `(0.0, 85.7) frozen`, `(5.0, 79.2) naive`
- **Overlay Config C** as hollow markers: `(72.4, 86.3)`, `(8.6, 85.9)`,
  `(45.6, 23.8)`, `(69.2, 2.8)`
- **Annotation:** top-right corner labelled "ideal"; retrain is alone there
- **Purpose:** shows the trade-off curve and that only retrain escapes it

### Chart spec — accuracy vs wall-clock
- **Type:** scatter, x = minutes (log), y = overall accuracy
- **Points:** `(3.24, 83.97)`, `(1.0, 74.60)`, `(0.5, 71.40)`, `(0.8, 66.87)`
- **Caption:** "The shortcuts save 2.4 minutes and cost 9 to 17 points"

---

## 10. Experiment 8 — seed ensemble 🟨 MARGINAL

**Question:** do three models differing only by seed make different mistakes?

### Diversity diagnostics (compute these before the result)

| Metric | Value |
|---|---|
| Pairwise disagreement | 11.20%, 11.30%, 11.63% (mean 11.38%) |
| Oracle (≥1 member correct) | 90.23% |
| Unanimous and correct | 77.00% |

Oracle is the hard ceiling. At 90.23% vs a best member of 84.23% there was ~6 points
of headroom; the ensemble captured 0.8 of it.

### Results

| Method | Accuracy | macro-F1 | vs best member | McNemar b/c | p |
|---|---|---|---|---|---|
| member seed 1 | 83.57 | — | — | — | — |
| member seed 2 | **84.23** | — | — | — | — |
| member seed 3 | 83.87 | — | — | — | — |
| logit mean | 84.93 | 0.8442 | +0.70 | 65 / 86 | 0.104 |
| **probability mean** | **85.03** | **0.8451** | **+0.80** | 62 / 86 | **0.059** |
| majority vote | 84.80 | 0.8425 | +0.57 | 61 / 78 | 0.175 |

**Caveats to report with this number:**
- Compare against the **best** member (84.23), not the mean (83.89). You would ship
  one model and pick a good one.
- p = 0.059 is outside conventional significance.
- Three combination rules were tried and the best reported: mild selection effect.
- One measurement, no error bar. Nine models in three groups of three would be needed.
- Costs 3× storage and 3× inference.

### Chart spec
- **Type:** horizontal bar, 3 members + 3 combination rules, with a gap between groups
- **Values:** `[83.57, 84.23, 83.87]` then `[84.93, 85.03, 84.80]`
- **Reference line:** dashed vertical at 84.23 labelled "best single model"
- **Second reference line:** dashed at 90.23 labelled "oracle ceiling"
- **Axis:** 80–92
- **Colour:** members `#5A6B76`, ensembles `#3F9E86`

---

## 11. Experiment 9 — stage-1 augmentation ⬛ NULL (and a methodology lesson)

**Question:** does `--augment` help under the corrected pipeline?

Augmentations: circular shift ±5 index positions (≤6 cm⁻¹), additive Gaussian noise
σ=0.01, multiplicative scale U(0.95, 1.05). All three always applied, per `__getitem__`.

### Full data, 6 paired seeds

| Seed | No augment | Augment | Δ | McNemar b/c | p |
|---|---|---|---|---|---|
| 1 | 83.27 | 83.57 | +0.30 | 142 / 151 | 0.640 |
| 2 | 82.27 | 84.23 | **+1.97** | 115 / 174 | **6.5e-04** |
| 3 | 83.60 | 83.87 | +0.27 | 148 / 156 | 0.688 |
| 4 | 83.87 | 83.00 | −0.87 | 183 / 157 | 0.175 |
| 5 | 83.00 | 82.07 | −0.93 | 174 / 146 | 0.131 |
| 6 | 83.40 | 83.60 | +0.20 | 154 / 160 | 0.778 |
| **mean** | **83.23** | **83.39** | **+0.16** | **916 / 944** | **0.531** |
| **sd** | **0.56** | **0.76** | CI [−0.95, +1.26] | χ² = 0.39 | |

### ⚠ The n=3 vs n=6 reversal — worth a chart on its own

| | n = 3 | n = 6 |
|---|---|---|
| Mean difference | **+0.84** | **+0.16** |
| Pooled p | **0.012** | **0.531** |
| sd, no augment | 0.69 | 0.56 |
| sd, augment | **0.33** | **0.76** |

At three seeds this looked like a real +0.84 with a significant p and a halved
variance. All three signals were small-sample artifacts driven by seed 2. **Three
seeds is not enough for sub-point effects.**

### Chart spec — primary
- **Type:** paired slope chart, 6 lines (one per seed), two x positions
- **Left:** no augment, **Right:** augment
- **Colour:** upward slopes `#3F9E86`, downward `#C05A3C`
- **Overlay:** thick line for the mean, 83.23 → 83.39
- **Caption:** "4 of 6 seeds up, 2 down, mean +0.16, p = 0.53"

### Chart spec — the methodology lesson
- **Type:** two-panel bar, n=3 vs n=6
- **Panel values:** `[+0.84, +0.16]` for mean difference; `[0.012, 0.531]` for p
- **Caption:** "The same experiment, three more seeds, opposite conclusion"

---

## 12. Benchmark context — all on this dataset and test protocol

| Source | Species (30-class) | Antibiotic (8-group) | Model |
|---|---|---|---|
| Project start (documented) | 76.50 | — | LegacyCNN, 40k |
| Project start (measured) | 74.78 ± 1.04 | — | LegacyCNN, 40k |
| RamanSPy paper | 79.63 | 94.63 | logistic regression |
| Ho et al. 2019 | >82 | 97.0 ± 0.3 | 25-layer ResNet |
| **This work** | **83.89 ± 0.33** | not run | LegacyCNN, 40k |
| **This work (ensemble)** | **85.03** | not run | 3 × LegacyCNN |
| Published best (U-Net) | 86.30 | 97.84 | U-Net |

### Chart spec
- **Type:** horizontal bar, sorted ascending, 7 entries
- **Values:** `[74.78, 76.50, 79.63, 82.00, 83.89, 85.03, 86.30]`
- **Colour:** this work `#3F9E86`, published references `#1C7293`, start `#C05A3C`
- **Axis:** 70–88
- **Annotation:** bracket from 74.78 to 85.03 labelled "+10.25 pts"

---

## 13. Per-class behaviour — consistent targets

Classes that fail across **every** architecture and **every** seed:

| Class | Recall range | Note |
|---|---|---|
| 11 | 0.24 – 0.43 | worst; not rescued by fine-tuning |
| 8 | 0.44 – 0.68 | consistently poor |
| 6 | 0.23 – 0.54 | |
| 9 | 0.27 – 0.36 | fails on test, looks fine on validation |
| 2 | 0.47 – 0.58 | |
| 4 | 0.53 – 0.63 | |

High-seed-variance classes (fate decided by initialisation, **not** worth targeting):
16 (sd 0.121), 24 (0.068), 13 (0.064).

Accuracy 83.89% vs macro-F1 0.8442 — the gap exists because error is concentrated.

### Chart spec
- **Type:** horizontal bar of per-class recall, 30 bars sorted ascending, with error
  bars = sd across seeds
- **Colour:** below 0.6 in `#C05A3C`, rest `#5A6B76`
- **Alternative:** 30×30 confusion matrix heatmap from
  `runs/<id>/metrics.json` → `test.confusion` (already recorded for every run)
- **Note:** the existing `results/heatmaps/*.png` are from a 5-epoch model with no
  pre-training and should **not** be reused.

---

## 14. Data sources for plotting

All per-run data is machine-readable:

```
runs/<run_id>/manifest.json   # all args, git SHA, device, library versions
runs/<run_id>/metrics.json    # per-epoch history + test.{accuracy, macro_f1,
                              #   per_class_recall, per_class_precision,
                              #   support, confusion (30x30)}
runs/<run_id>/test_y_pred.npy # 3000 predictions (for McNemar / custom analysis)
runs/<run_id>/test_y_true.npy # 3000 ground-truth labels
results/ablation/*.json       # paired comparison outputs
results/ensemble_p2base20.json
```

**Training curves:** `metrics.json` → `history[]`, each entry has `phase`
(`pretrain` / `finetune`), `epoch`, `train_loss`, `train_acc`, `val_loss`,
`val_acc`, `val_macro_f1`, `val_per_class_recall`, `lr`.

**Tags for selecting runs:**
`abl-full` / `noise100` = legacy_full baseline (6 runs total) ·
`abl-minmax_only` = the 5-architecture grid ·
`p2_base` / `p2_val` / `p2_valaug` / `p2_valaugwd` = phase-2 arms ·
`noaug` = augmentation-off arm

---

## 15. Corrections and known defects

| Item | Status |
|---|---|
| `docs/3_PREPROCESSING.md` rationale | **Falsified** — ASPLS costs 8 points here |
| `docs/4` 78.70% figure | Not a test number (validation split of reference set) |
| `docs/10` master results table | All 18 entries used ASPLS; invalid |
| "Augmentation worth +1.40" | **Falsified** at n=6: +0.16, p=0.53 |
| "73.23% ± 0.11%" | Last-epoch number; folds overlapped; margin ~10× too small |
| "torch is CPU-only" (§0.3) | **Stale** — torch 2.11.0+cu128, CUDA available |
| Wavenumber axis direction | Descending (1792.40 → 381.98), docs said ascending |
| Clinical split labels | **Antibiotic-treatment**, not isolate. Guard added. |
| `no_despike` / `no_savgol` arms | Retain ASPLS; two-step comparisons, not clean |
| `compare_runs.py` summary stats | Pool across model types; meaningless multi-model |
| Cache wall-clock benefit | Claimed, never measured |
| Ensemble error bar | Single measurement, no replication |

---

## 16. Open, ranked by expected value

1. **Head normalisation / logit calibration** for the new-class case — follows
   directly from the frozen-backbone result, untested.
2. **Antibiotic-treatment task** (8 groups, published 97%) — a label remap; never run.
3. **12,500 clinical spectra** — 4× the current test set, untouched; requires (2) first.
4. **Per-class work on classes 11 and 8** — consistent across all designs and seeds.
5. **Mechanism figure** — raw vs full-pipeline vs minmax_only spectrum overlay.
6. **Transformer1D init fix** — unscaled `torch.randn` for `cls_token` / `pos_embedding`
   at d_model 64; suspected cause of sd 5.65, unconfirmed. Same pattern in FusionNet.
