# Paper report: 1D ResNet vs. plain CNN on bacteria-ID

Date: 2026-10-23
Paper source: [`paper/overleaf/main.tex`](../paper/overleaf/main.tex),
bibliography: [`paper/overleaf/references.bib`](../paper/overleaf/references.bib).
Nothing described here is committed to git yet.

## 1. What the paper is

An IEEE-style journal paper (IEEEtran, single-column) titled *"Do Residual
Connections Matter? Evaluating 1D Residual Networks versus Plain
Convolutional Networks for Low-SNR Bacterial Raman Spectroscopy"*. It
compares a 1D ResNet against a plain 1D CNN for classifying bacterial Raman
spectra from the public bacteria-ID dataset (Ho et al., *Nat. Commun.*
2019): 60,000 reference spectra from 30 isolates, plus 3,000 fine-tuning
and 3,000 test spectra measured on independently cultured samples.

Outline: abstract, introduction, dataset, models and experimental setup,
results, discussion, conclusion, back matter and appendix.

## 2. Work done in this session

The section written in this session is **Section III, "Model Architectures
and Experimental Setup"**, plus a few small follow-up edits. The work was
split between subagents (gathering facts, verifying references, drafting)
and the main agent, which checked every claim against the code, the run
records and the original sources.

### 2.1 Fact-finding: what the code actually contains

The old Section III text described work that does not exist in the repo:

| Old paper claim | What the code and runs show |
|---|---|
| A faithful reimplementation of Ho et al.'s 25-layer ResNet | Not in the repo. The model called `resnet` is `Raman1DCNN` (`src/model.py`), a smaller network with the ResNet-18 stage layout |
| Plain-5, Plain-10 and Plain-25 networks; pooling and kernel-width ablations | None implemented, none run |
| Batch size 10, Adam betas (0.5, 0.999) | Batch size 64, default betas (0.9, 0.999), weight decay 0.01 |
| 10% held-out validation split | 67/33 random split (40,200 / 19,800) |
| Five 90/10 fine-tuning splits, checkpoint chosen on validation accuracy | One fine-tuning run, last-epoch weights kept, no validation |
| Holm–Bonferroni correction | Not implemented |
| RTX 3060 with 12 GB | RTX 3060 is confirmed by the run manifests; the 12 GB is not |

The `bacteria-ID/` folder in the repo is empty, so Ho et al.'s original
code was downloaded from GitHub (`csho33/bacteria-ID`) and checked
directly.

Verified model facts, from the code and by instantiating the models:

| | 1D ResNet (ours) | Plain CNN (ours) | Ho et al. ResNet-25 (reference only) |
|---|---|---|---|
| Code | `src/model.py` (`Raman1DCNN`) | `legacy_baseline/model.py` (`LegacyCNN`) | `resnet.py` in csho33/bacteria-ID |
| Layout | stem + 4 stages × 2 basic blocks | 6 conv blocks | stem + 6 stages × 2 basic blocks |
| Channels | 16, 32, 64, 128 | 8, 16, 32, 32, 64, 128 | 64 stem, then 100 |
| Kernel | 3 (stem 7) | 3 | 5 |
| Main-path convolutions | 17 (+3 projection shortcuts) | 6 | 25 (+6 projection shortcuts) |
| Downsampling | strided stem, max-pool, stride 2 | average pool 3, stride 3 | stride 2, no pooling |
| Head | GAP, FC 128, dropout 0.4, FC 30 | GAP, dropout 0.3, FC 30 | flatten 3,200, FC 30 |
| Receptive field (points) | 435 | 971 | 889 |
| Trainable parameters | 262,510 | 40,446 | 1,340,878 |

Shared training protocol, from `main.py` and the run manifests
`runs/20260917-*_{resnet,legacy_cnn}_abl-minmax_only_*`:

- **Pre-training:** Adam, learning rate 1e-3, weight decay 0.01, batch
  size 64, cosine schedule, at most 100 epochs, early stopping on
  validation loss with patience 10.
- **Augmentation (pre-training only):** shift by up to ±5 points, Gaussian
  noise with σ = 0.01, scale in [0.95, 1.05].
- **Fine-tuning:** all layers, learning rate 1e-4, 20 epochs, no weight
  decay.
- **Testing:** one pass over the 3,000-spectrum test set, seeds 1–3.

### 2.2 Bibliography verification

All 14 existing references were checked against Crossref and the
publishers' records. Two were wrong and are fixed (citation keys
unchanged):

- `pan2021review` was cited as an arXiv preprint. It is actually a
  *J. Raman Spectrosc.* 53(1):6–19 (2022) article, and its fifth author
  was missing.
- `paszke2019pytorch` had a page range the official NeurIPS record does not
  support, and an incomplete author list.

New references were added and verified the same way: LeCun 1998, He 2016
(identity mappings), Nair & Hinton 2010, Srivastava 2014, Lin 2014 (NiN),
Bengio 1994, Luo 2016, Prechelt 1998, Loshchilov & Hutter 2017 and 2019,
Szegedy 2016, Zhang 2018, Harris 2020 (NumPy), Acquarelli 2017, Deng 2022,
Georgiev 2024 (RamanSPy), Edwards 1948, the authors' bacteria-ID code
repository, and the PyTorch MPS documentation. The bibliography has 33
entries, all cited. The Liu et al. (2017) augmentation claim was checked
against the paper's text.

### 2.3 Section III, as rewritten

| Subsection | Content |
|---|---|
| Intro | Two architecture families, the shared input (1×1000, min–max normalised), PyTorch |
| A. 1D ResNet | Layer-by-layer description, the residual block equation, parameter count, receptive field |
| B. Plain 1D CNN | Layer-by-layer description, BN placed after ReLU, parameter count, receptive field |
| C. Scope of the comparison | The seven factors in which the two models differ (shortcuts, depth, receptive field, downsampling, BN placement, head, capacity). It states plainly that this is a family-vs-family comparison, not a single-factor ablation of residual connections. Ho's ResNet-25 appears only as a reference |
| D. Training protocol | Pre-training, fine-tuning, testing, seeds and software |
| E. Evaluation metrics and statistics | Accuracy, macro-F1, McNemar's test with continuity correction, mean ± s.d. and a paired t-interval over seeds |
| F. Computing hardware | Two machines: an NVIDIA GeForce RTX 3060 (CUDA) for all reported runs, and a Mac M3 (PyTorch MPS backend) for earlier development runs |

New figures and tables, all drawn from scratch in TikZ inside `main.tex`
(no image files; they read in greyscale):

- **Fig. 2:** both networks layer by layer, with the tensor shape after
  every layer and the shortcut connections drawn in.
- **Fig. 3:** a residual basic block next to a plain CNN block.
- **Fig. 4:** the experimental pipeline (split → pre-train → fine-tune →
  single test pass → metrics and McNemar).
- **Table II:** architecture comparison, including Ho's ResNet-25 marked
  "not trained here".
- **Table III:** the shared training hyper-parameters.

The old architecture diagram, which showed a model that was never run, was
removed. The text says "GPU" in general terms, and Section III-F names the
hardware.

### 2.4 Table IV (results)

The three placeholder rows (ResNet-25 (ours), Plain-25, Plain-10) were
replaced with the two models that were actually trained:

| Model | 30-isolate (%) | Treatment (%) | MRSA AUC |
|---|---|---|---|
| 1D ResNet (ours) | 79.6 ± 1.8 | n.e. | n.e. |
| Plain CNN (ours) | 83.9 ± 0.3 | n.e. | n.e. |

Values are the mean ± s.d. over seeds 1–3, with one test pass each.
"n.e." means not evaluated: the repo has no treatment-group mapping and no
MRSA/MSSA classifier.

### 2.5 Checks

- The paper compiles with MiKTeX (pdflatex → bibtex → pdflatex ×2) to 10
  pages, with no errors, no undefined references or citations and no
  overfull boxes.
- The rendered pages were inspected to confirm the diagrams are legible
  and correct.

## 3. Current results

Test accuracy and macro-F1 from the run records, three seeds each:

| Model | Accuracy per seed (%) | Mean ± s.d. (%) | Macro-F1 (mean) |
|---|---|---|---|
| 1D ResNet | 78.00, 79.17, 81.50 | 79.6 ± 1.8 | 0.792 |
| Plain CNN | 83.57, 84.23, 83.87 | 83.9 ± 0.3 | 0.834 |

The plain CNN currently beats the 1D ResNet by about 4 points, with 6.5×
fewer parameters. Run time per run was 9.7–25.8 min for the ResNet and
8.2–14.6 min for the CNN, on the RTX 3060.

## 4. Still open

Other sections were deliberately left unchanged, so they still disagree
with Section III:

- **Abstract and contributions** claim a faithful ResNet-25
  reimplementation and Plain-N depth, downsampling and kernel ablations.
  Either run those experiments or remove the claims.
- **Section II-C (evaluation protocol)** still mentions five 90/10
  fine-tuning splits, checkpoint selection on validation accuracy, and 3–5
  seeds.
- **Section II-B (pre-processing)** says no further steps are applied, but
  the code re-applies min–max normalisation.
- **Results text** says Table IV shows macro-F1 (it has no macro-F1
  column), and a note still refers to a ResNet-25 vs. Plain-25 contrast.
- **Missing results:** the treatment-group and MRSA AUC results, the
  confusion matrices, ROC curves, noise robustness and cost tables are
  still placeholders.
- **Reproducibility:** the 2026-09-17 runs were made from uncommitted code
  (`git_dirty: true` at fb58ad3), so they cannot be reproduced exactly
  from a commit.
- **Ho's 82.2%** is not directly comparable to our rows, because his
  network and training settings differ from ours.
