# Week 13 Summary: Residual Shortcuts vs. Downsampling Ablation in 1D Bacterial Raman Spectroscopy

In this technical teardown, we summarize our **Controlled Architectural Ablation Study** (`data/week13/14_ARCHITECTURAL_ABLATION_RESULTS.md`), designed to answer Reviewer Feedback §3.2 (`paper/feedback/01.md`): *Why does a 6-layer Plain 1D CNN (`legacy_cnn`, 40,446 parameters) outperform a 17-layer 1D ResNet (`resnet`, 262,510 parameters) by $+4.33 \pm 1.72$ percentage points ($83.89 \pm 0.33\%$ vs. $79.56 \pm 1.78\%$) on the 30-isolate `bacteria-ID` benchmark?*

## Video Links

- [16:9 video](https://drive.google.com/file/d/1uNN2vWuHy8nNSy7S_QxzXGjLJ7RA698H/view?usp=sharing)
- [9:16 video](https://drive.google.com/file/d/1bSmvaRyTY73gheAMUxgqcVh3bgr2LTeo/view?usp=sharing)
- [GitHub commit](https://github.com/hspgit/RAMAN-Effect/commit/2278251cf9ef8973edc6db9fe34e777353f75c28)

---

## Key Architectural, Experimental & Statistical Takeaways

- **Four Confounded Baseline Factors (§1)**:
  - The baseline Plain 1D CNN and 17-layer 1D ResNet differ simultaneously in:
    1. **Residual shortcut connections**: none vs. 5 identity + 3 projection ($1\times 1$) shortcuts.
    2. **Network depth & capacity**: 6 convolutions (`40,446` parameters) vs. 17 main-path convolutions (`262,510` parameters).
    3. **Downsampling mechanism**: 5 stages of `AvgPool1d(kernel=3, stride=3)` vs. strided convolutions (`stride=2`) + stem `MaxPool1d`.
    4. **Theoretical receptive field**: `971` vs. `435` points out of `1,000` spectral points.

- **Four Single-Factor Control Architectures (§2.1)**:
  - Exposed via `--model-type` in `main.py` (`src/model.py` and `legacy_baseline/model.py`):
    - **Control 1 — `resnet_no_shortcuts` (`251,310` params)**: 17-layer 1D ResNet with all 5 identity and 3 projection shortcuts removed (`use_shortcuts=False`).
    - **Control 2 — `legacy_cnn_shortcuts` (`51,830` params)**: 6-layer Plain CNN with residual shortcuts added around each block (identity on Block 4; $1\times 1$ projection + BN on blocks 1, 2, 3, 5, 6).
    - **Control 3 — `legacy_cnn_strided` (`40,446` params)**: 6-layer Plain CNN with `AvgPool1d(k=3, s=3)` replaced by `Conv1d(k=3, stride=3)`.
    - **Control 4 — `resnet_avgpool` (`262,510` params)**: 17-layer 1D ResNet with strided convolutions and `MaxPool1d` replaced by `stride=1` convolutions + `AvgPool1d(stride=2)` (`use_avgpool=True`).

- **Canonical 18-Run Protocol (§2.2)**:
  - `6` architectures $\times$ `3` independent random seeds (`seeds 1, 2, 3`) = `18` total canonical runs under `minmax_only` (per-spectrum `[0, 1]` min–max normalization via RamanSPy).
  - **Pre-training**: `60,000` reference spectra (1 s exposure, `40,200` train / `19,800` val), Adam ($\text{lr}=10^{-3}$, weight decay $0.01$), cosine annealing ($T_{\max}=100$), early stopping (patience 10), on-the-fly physical augmentation (circular shift $\in [-5, 5]$ pts, Gaussian noise $\sigma=0.01$, multiplicative scale $\in [0.95, 1.05]$).
  - **Fine-tuning & Evaluation**: `3,000` fine-tuning spectra (100/isolate, 2 s exposure, 20 epochs, Adam $\text{lr}=10^{-4}$, no weight decay), evaluated in a single pass on the held-out `3,000`-spectrum test set (100/isolate, 2 s).

- **3-Seed Empirical Results & Pooled McNemar Tests (§3–§4)**:
  - `legacy_cnn`: **$83.89 \pm 0.33\%$** (Macro-F1 $83.37 \pm 0.31\%$, 8-class treatment $96.78 \pm 0.13\%$, MRSA $84.20 \pm 1.56\%$)
  - `legacy_cnn_strided`: **$83.64 \pm 0.42\%$** (Macro-F1 $83.32 \pm 0.31\%$, 8-class treatment **$97.09 \pm 0.08\%$**, MRSA $82.93 \pm 1.75\%$)
  - `legacy_cnn_shortcuts`: **$82.60 \pm 0.44\%$** (Macro-F1 $82.17 \pm 0.49\%$, 8-class treatment $97.00 \pm 0.22\%$, MRSA $83.27 \pm 0.81\%$)
  - `resnet_avgpool`: **$80.12 \pm 1.85\%$** (Macro-F1 $79.86 \pm 1.76\%$, 8-class treatment $94.51 \pm 0.39\%$, MRSA $80.60 \pm 2.60\%$)
  - `resnet`: **$79.56 \pm 1.78\%$** (Macro-F1 $79.24 \pm 1.83\%$, 8-class treatment $93.86 \pm 1.03\%$, MRSA $79.33 \pm 3.72\%$)
  - `resnet_no_shortcuts`: **$77.93 \pm 0.82\%$** (Macro-F1 $77.66 \pm 0.73\%$, 8-class treatment $94.23 \pm 0.41\%$, MRSA $78.33 \pm 1.80\%$)
  - **Conclusion 1 (Shortcuts Flip Sign with Depth)**: Beneficial at 17 layers ($+1.62$ pp, $\chi^2 = 16.85, p = 4.05 \times 10^{-5}$), actively counterproductive at 6 layers ($-1.29 \pm 0.20$ pp, $\chi^2 = 16.25, p = 5.56 \times 10^{-5}$).
  - **Conclusion 2 (Downsampling Is Secondary)**: Strided vs. AvgPool in 6-layer CNN is statistically indistinguishable ($-0.24 \pm 0.40\%$, $\chi^2 = 0.47, p = 0.4948$ NS); AvgPool in 17-layer ResNet adds $+0.57 \pm 1.60\%$ ($\chi^2 = 2.11, p = 0.1460$ NS), closing only $\sim 13\%$ of the baseline gap.
  - **Conclusion 3 (Compact 6-Layer Hierarchy Dominates)**: Holding shortcuts fixed, 6 layers beat 17 layers by **$+5.96 \pm 1.13\%$ without shortcuts** ($\chi^2 = 207.71, p = 4.34 \times 10^{-47}$) and **$+3.04 \pm 1.40\%$ with shortcuts** ($\chi^2 = 57.33, p = 3.68 \times 10^{-14}$).
