# Weekly report — week ending 16 October 2026

**Author:** Amos Jaimes · **Branch:** `amosj`

## Summary

- **Paper preparation.** We checked the proposed paper outline (plain 1D CNNs
  vs. 1D ResNets on the Ho et al. 2019 bacteria-ID data) against our data and
  code. A LaTeX template is now ready in Overleaf format. Most of the outline
  can be done. One section had to be redesigned, because the dataset has no
  1 s / 2 s / 3 s exposure splits. The core experiment needs new code before
  it can run.
- **Hybrid model rerun at a larger size.** Our pretrained hybrid model
  (multi-scale CNN stem + transformer, "model A") was trained only at the
  `small` size (5.0 M parameters). The choice of size rests on a trial that
  ran *before* the masked-GroupNorm fix, so `base` (14.6 M) has never been
  tested on the current model. Configs for a base-size rerun are now in
  place. Nothing has been launched yet.
- **What to expect.** A bigger model will most likely give a small
  improvement (0–2 points) rather than a large one. Section 3 explains why,
  and sets out the decision rules for judging the rerun.

---

## 1. Paper preparation

### 1.1 Outline review

We checked the proposed outline section by section against the repository
and against Ho et al., *Nat. Commun.* 10, 4927 (2019)
(doi:10.1038/s41467-019-12898-9).

| Outline section | Status | Notes |
|---|---|---|
| 6.1 30-isolate classification | ✅ Ready | Data, training and metrics code exist |
| 6.2 Treatment grouping (8 classes) | ✅ Small addition | Isolate → group map taken from the authors' `config.py`; the clinical files are already labelled by treatment group |
| 6.3 MRSA vs. MSSA (ROC-AUC) | ✅ Small addition | Use the S. aureus isolates (MRSA 16, 17 vs. MSSA 14, 15, 18); needs saved probabilities + ROC code |
| 6.4 Noise across 1 s / 2 s / 3 s | ⚠ Redesigned | The data has no such splits: the reference set is 1 s, and fine-tune/test are 2 s at about the same SNR. Replaced by a **simulated SNR sweep** plus the **real 1 s → 2 s instrument shift** |
| 6.5 Training dynamics and cost | ✅ Mostly ready | Loss curves and parameter counts already logged; still need gradient-norm logging and a latency benchmark |
| §4 "5-fold CV across samples" | ⚠ Changed | No sample IDs in the release. Use the original protocol instead: 5 random 90/10 fine-tune splits, then the separately cultured test set |
| Core ResNet-vs-plain contrast | ❌ Needs new code | Our current "ResNet" is not the paper's architecture, and it differs from our CNN in about seven ways at once, so the effect of skip connections cannot yet be isolated |

**Current evidence (3 seeds each, before any controlled comparison):** our
small plain CNN (40 k parameters) reaches **83.9%**; our ResNet (262 k)
reaches **79.6%**; Ho et al. report **82.2%**. So the paper should be framed
neutrally ("Do residual connections matter?"), not assume the ResNet wins.

### 1.2 What was built

- **`paper/overleaf/`**: the Overleaf project (`main.tex`, `references.bib`,
  `figures/`), with an upload-ready zip at `paper/overleaf.zip`.
  - IEEE journal class, full-page single-column layout. Switching to two
    columns is a one-word change.
  - All sections of the outline, with red `\TBD` placeholders for every
    number still to be measured and blue `\NOTE` writing hints.
  - Worked examples of every figure and table type, and back matter (data
    availability, author contributions, conflicts of interest).
  - 14 references. These still need checking against publisher records
    before submission.
- **Fig. 1 from real data**: `paper/scripts/make_fig_spectra.py`.
- **Onboarding guide for new collaborators**: `paper/overleaf_guide.png`, an
  annotated Overleaf screenshot with 17 marked spots, plus `paper/README.md`.

### 1.3 Next steps for the paper

1. Build the controlled experiment code:
   - a faithful port of the paper's 25-layer ResNet (64→100 filters, kernel
     5, strided convolutions, no pooling);
   - a depth- and width-matched plain twin;
   - one-factor-at-a-time variants for depth, pooling vs. stride, and kernel
     size.
2. Add the treatment-group metric, the MRSA/MSSA task with ROC-AUC, the
   SNR-sweep tool, gradient-norm logging and a latency benchmark.
3. Run the grid: about 15–20 configurations × 3–5 seeds, roughly 1–2 GPU-days.
4. Fill in the `\TBD` placeholders, then write the Discussion from the
   results.

---

## 2. Hybrid model (model A) rerun with more parameters

### 2.1 Why rerun

Model A is a **hybrid**: a multi-scale CNN stem (kernels 3/9/25) feeds 101
spectral tokens into a transformer. It is pretrained with masked
reconstruction on 242,156 public spectra. The size was chosen in a 50-epoch
trial:

| Trial (50 epochs) | Params | Probe score | Note |
|---|---|---|---|
| tiny | 0.92 M | 0.636 | |
| small | 4.99 M | 0.672 | |
| base | 14.57 M | 0.672 | tied with small → the smaller one was picked |
| **small + masked GroupNorm** | 4.99 M | **0.742** | the stem fix added +0.07 |
| base + masked GroupNorm | 14.57 M | **never run** | ← the gap |

The tie between small and base was measured on the **old** stem. The fix that
mattered most (masked GroupNorm, +0.07) was only ever applied to `small`, and
the main run then went straight to small. So we do not know whether `base`
would pull ahead on the current architecture.

Results with small A, for reference (test sets, mean ± sd over 5 seeds):

| Arm | T1 (30 isolates) | T2 (2018 → 2019 clinical) |
|---|---|---|
| S: from scratch | 80.9 ± 0.7 | 87.8 ± 0.7 |
| LP: frozen A + head | 78.2 ± 0.2 | 86.8 ± 0.6 |
| B1: fine-tune A | **83.1 ± 0.6** | 89.6 ± 0.5 |
| B2: LoRA on frozen A (4.4% trainable) | 81.9 ± 0.6 | **91.9 ± 0.6** |

The pre-registered reuse test (Q3) **narrowly failed**: B2 was 1.23 points
behind B1 on T1, against a 1.0-point margin. A larger A is the most direct way
to give LoRA more to work with.

### 2.2 What is set up

Three new configs. Each is identical to the one used for small, except for
the size and the output folders.

| File | Purpose |
|---|---|
| `foundation/configs/pretrain_trial_base_mgn.yaml` | Base, 50 epochs: a like-for-like trial against `small_trial_mgn` |
| `foundation/configs/pretrain_main_base.yaml` | Base, up to 200 epochs: the full pretraining run |
| `foundation/configs/adapt_base.yaml` | Adaptation of base A; writes to `foundation/runs/adapt_base/` so the finished small results and their locked test pass stay untouched |

Run order (nothing has been started):

```bash
# 1. Trial (gate)
venv/Scripts/python.exe -m foundation.pretrain --config foundation/configs/pretrain_trial_base_mgn.yaml
venv/Scripts/python.exe -m foundation.analysis.report foundation/runs/pretrain/20261003-111809_small_trial_mgn foundation/runs/pretrain/<base_trial_mgn run> --out foundation/results/pretrain_trials_base_mgn.md

# 2. Full pretraining (only if the gate in 3.3 passes)
venv/Scripts/python.exe -m foundation.pretrain --config foundation/configs/pretrain_main_base.yaml

# 3. Adaptation (first set a_ckpt in adapt_base.yaml to <base main run>/ckpt_best.pt)
venv/Scripts/python.exe -m foundation.adapt sweep --config foundation/configs/adapt_base.yaml
venv/Scripts/python.exe -m foundation.adapt seeds --config foundation/configs/adapt_base.yaml
venv/Scripts/python.exe -m foundation.adapt curve --config foundation/configs/adapt_base.yaml

# 4. One test pass, written to its own results folder
venv/Scripts/python.exe -m foundation.evaluate --config foundation/configs/adapt_base.yaml --results foundation/results/base
```

### 2.3 Compute estimate (RTX 3060)

Estimates are scaled from the measured small and base runs. Base has about
3× the transformer compute of small (width 384 vs. 256, 8 vs. 6 layers).

| Step | Small (measured) | Base (estimate) |
|---|---|---|
| 50-epoch trial | 1.3 h | ≈ 2.2–2.4 h |
| Main pretraining | 4.5 h (stopped at epoch 180) | ≈ 9–10 h for 200 epochs; less if it stops early |
| Adaptation: sweep + seeds + curve | 4.6 h | ≈ 12–14 h |
| **Total** | ≈ 10 h | **≈ 24–26 h (about one GPU-day)** |

The model A file grows from 20 MB to about 58 MB. Each LoRA add-on grows from
about 1 MB to about 2 MB.

---

## 3. What to expect when the full training is done

### 3.1 Pretraining (model A itself)

- **Probe score:** small reached 0.742 at 50 epochs and **0.796** after the
  main run. A reasonable expectation for base is **0.80–0.83**. It could also
  tie again: on the old stem, base matched small at 50 epochs and peaked
  earlier (epoch 30 vs. 40). That suggests our 242 k-spectrum corpus may not
  be large enough to use the extra capacity.
- **Representation richness** (RankMe) should rise. Base already scored 125
  vs. 99 on the old stem.
- **Watch the source-ID probe.** Base was slightly higher (0.950 vs. 0.941),
  so it may encode more "which instrument/lab" information. That is not
  helpful for transfer to our data.

### 3.2 Downstream (our tasks)

- **Most likely gains are small, 0–2 points.** The main limit on our tasks is
  domain shift, not model capacity. Validation accuracy is already 95–99%,
  while test accuracy is 83–92%. That 7–12 point gap comes from measuring
  new cultures and a later clinical year, which a bigger encoder does not
  directly fix.
- **Where base could help most:**
  - **B2 (LoRA) on T1.** More capacity in the frozen model gives the
    adapters more to steer. This is the arm that missed the Q3 margin by
    0.23 points, so base could turn Q3 into a pass.
  - **The low-data curve** (5–10 spectra per class), where pretraining
    already gave about +4 points over scratch.
- **Where base may not help, or could hurt:**
  - **B1 (full fine-tune) on T2.** That is 9,000 training spectra for a
    14.6 M-parameter model, so overfitting is more likely.
  - **LP (frozen + head).** It was already 5 points behind and is unlikely to
    close the gap.

### 3.3 Decision rules (fix these before running)

1. **Gate after the trial.** Adopt base only if `base_trial_mgn` beats
   `small_trial_mgn` (0.742) by **more than 0.03** on the probe score. That
   is the same tie rule used in the original size trial.
2. **Downstream comparison.** Compare base vs. small per arm with the same
   paired bootstrap and McNemar tests, selecting only on validation.
3. **Test-set reuse.** The test sets were already scored once for small.
   Scoring them again for base is a **second, declared comparison**, and the
   report must say so. To stay strict, freeze every base setting before that
   single pass.
4. **Known limit.** Both A models use one pretraining seed. A difference
   under about 1 point between small and base may be pretraining-seed noise
   rather than size. If the result is close, a second small seed (≈ 4.5 h)
   would settle it.

---

## 4. Plan for next week

1. Run the base trial (≈ 2.3 h) and apply the gate in 3.3.
2. If the gate passes, start the base main pretraining overnight (≈ 9–10 h).
3. In parallel on CPU, start the paper's controlled experiment code (§1.3).
4. Share the Overleaf project with co-authors, and verify the references.
