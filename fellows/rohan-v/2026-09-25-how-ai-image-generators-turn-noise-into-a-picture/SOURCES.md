# SOURCES — How AI Image Generators Turn Noise Into a Picture

## First-party: Midjourney

| Source | Used for |
|---|---|
| Midjourney documentation, **"Seeds"** — docs.midjourney.com/hc/en-us/articles/32604356340877-Seeds (read 2026-09-25 in the browser; the page refuses automated fetches) | every image starts from random noise "like the random noise you see on a TV screen"; seeds are whole numbers 0–4294967295; a new random seed is used unless you set one; lock a seed "like having a control in an experiment"; seeds only influence "the initial layout of noise"; seeds "have the least impact on the final image"; for consistency use "style references, omni references, and personalization" |

Midjourney does **not** publish its model architecture. The reel never claims
it does: everything about *how* the noise becomes a picture is shown on an
open, reproducible toy model and labelled as such.

## The method

| Source | Used for |
|---|---|
| J. Ho, A. Jain, P. Abbeel, *Denoising Diffusion Probabilistic Models*, NeurIPS 2020 — arXiv:2006.11239 | the forward process x_t = √ᾱ_t·x₀ + √(1−ᾱ_t)·ε (eq. 4), the linear β schedule 10⁻⁴ → 0.02 over T = 1000 (§4), the ε-prediction loss ‖ε − ε_θ(x_t, t)‖² (eq. 14), the ancestral sampling step (Algorithm 2) |
| J. Ho, T. Salimans, *Classifier-Free Diffusion Guidance*, 2022 — arXiv:2207.12598 | how one model follows a prompt: train with the prompt randomly dropped, then mix the prompted and unprompted noise guesses at sampling time (guidance weight 3 here) |

## Executable evidence (this folder)

| File | What it is |
|---|---|
| `train_toy_diffusion.py` | the toy model, trained from scratch in plain numpy on 12,000 procedurally drawn 16×16 pictures (hearts, music notes). No GPU, no downloads, no pretrained weights. Seeded throughout |
| `evidence/run.log`, `evidence/toy_diffusion.json` | the training run's full output and every number the reel shows (SHA-256 in the log) |
| `evidence/weights.npz` | the trained weights (EMA), so any picture can be regenerated |
| `scan_seeds.py`, `evidence/seed_scan.{log,json}` | the logged rule that chose B05's fork seed, with all 40 seeds' scores kept |
| `export_toy_data.py`, `evidence/export.log` | replays the runs from the weights, verifies them against the record, typesets the equations, writes the scenes' data module |

Environment: Python 3.12.10, numpy 2.5.2, Windows 11, CPU only.
