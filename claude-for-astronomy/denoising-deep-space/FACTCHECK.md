# FACTCHECK — *The Sharpest Guess.*

Ep. 09 · `denoising-deep-space` · checked from primary sources on
**2026-09-17**, during this build. Every figure that reaches the screen or the
narration is in the table below with the source that supports it.

**Two kinds of number appear in this reel and they are never mixed.**
*Published* figures come from the two primary papers and are cited on screen.
*Computed here* figures come out of `assets/gen_deconv.py`, which runs the
calculation itself and asserts two of its own claims. B09 puts both on screen
**side by side with a tag separating them**, because that beat is precisely
about not confusing a measurement with a model output.

## Claims on screen or in the narration

| # | Claim | Where | Verdict | Source |
|---|---|---|---|---|
| 1 | Two different operations are both called "denoising" | B03, B11 | ✅ | Editorial framing, but a real and consequential distinction: NSClean removes a *measurable pattern*; deconvolution attempts to invert an operator with a null space. The two are not the same problem and the reel's spine is that conflating them is the mistake. |
| 2 | JWST's 1/f striping is driven by readout-electronics temperature variations and appears as banding in the fast-read direction | B03 cite | ✅ | [JWST User Documentation — 1/f Noise](https://jwst-docs.stsci.edu/known-issues/1-f-noise); Rauscher 2024 |
| 3 | It is removed by fitting a model in Fourier space to known-dark areas and subtracting | B03 | ✅ | *NSClean: An Algorithm for Removing Correlated Noise from JWST NIRSpec Images*, Rauscher, PASP **136**, 015001 (2024) — [arXiv:2306.03250](https://arxiv.org/abs/2306.03250) |
| 4 | It takes seconds, on a laptop, with **no network** | B03 narration | ✅ | Same: "computationally undemanding, requiring only a few seconds to clean an image on a typical laptop". It is a Fourier fit; no machine learning is involved. |
| 5 | The circular-aperture OTF is **exactly zero** above the cutoff | B04 cite, B04 narration, B11 | ✅ | Standard Fourier optics: the incoherent OTF is the autocorrelation of the pupil, `H(k) = (2/π)[arccos u − u√(1−u²)]` with `u = k/k_c`, identically zero for `k > k_c`. Implemented in closed form in `gen_deconv.py`, not approximated. |
| 6 | A diffusion prior trained on cosmological simulations supplies the missing structure | B07, B00 | ✅ | *Bayesian Deconvolution of Astronomical Images with Diffusion Models*, [arXiv:2411.19158](https://arxiv.org/html/2411.19158v2) — score-based DM trained on TNG100, deployed via Diffusion Posterior Sampling |
| 7 | **17,852** simulated galaxies in the training set | B07 counter, B07 cite | ✅ | Same: 17,852 images of 256×256 px from TNG100 at z = 0.1527, 0.1693, 0.1804, 0.4 kpc/pixel |
| 8 | **133 GPU-hours** to train, **~100 seconds** to sample | B07 (landscape only) | ✅ | Same: "133 hours on 32 V100 GPUs"; inference "∼100 seconds on a single A100 GPU". **Note the reel says "133 GPU-hours", which is wrong as an aggregate** — see § "Corrected before shipping". |
| 9 | The method reaches resolution comparable to HST from ground-based HSC data | B07 context | ✅ | Same, verbatim: "we reach resolutions comparable to those obtained by Hubble Space Telescope (HST) images". HSC-PDR3 at 0.17 arcsec/pixel. |
| 10 | The honest output is many samples, not one image | B08, B11 | ✅ | Both primary papers do this: arXiv:2411.19158 uses **256** posterior samples; the AJ paper uses **450** per source. |
| 11 | **256** posterior samples | B08 cite, B00 runningText | ✅ | arXiv:2411.19158 — posterior mean and variance computed over 256 samples in an r = 30 px aperture |
| 12 | A **variance ratio** (posterior variance ÷ prior variance) detects prior-driven features | B09, B11 | ✅ | Same. Lower = data-driven; higher = prior-dominated. |
| 13 | **0.0114** at SNR **699.3**, and **0.0685** at SNR **7.0** | B09 figures | ✅ | Same, Table 2: magnitude 18 → SNR 699.3 → variance ratio 0.0114; magnitude 23 → SNR 7.0 → 0.0685 |
| 14 | At high redshift "a high number of features are created (hallucinated) all around the galaxy" | B09 struck line | ✅ | Same, verbatim, at z = 0.8463. The paper also notes that above z ≈ 0.7 the cutout is < 80 px so the task becomes deconvolution *and* upsampling, and "an upscaling factor higher than a factor 2 is problematic". |
| 15 | HST reconstructions recovered structure later visible in JWST imaging of the same sources | B10, B10 cite | ✅ | *Echoes in the Noise: Posterior Samples of Faint Galaxy Surface Brightness Profiles…*, AJ — [10.3847/1538-3881/adb039](https://iopscience.iop.org/article/10.3847/1538-3881/adb039). HST F814W/F160W/F105W, COSMOS + SMACS 0723; "the skewed bar feature is recovered", "spiral arms are distinctly recovered". |
| 16 | That check is **qualitative only** | B10 narration + on-screen QUALITATIVELY + cite | ✅ | Same, verbatim: **"For this work, we only provide a qualitative comparison between our reconstruction and the JWST image."** This is the single most important caveat in the episode and it is spoken, shown and cited. |
| 17 | Nobody has published a rate for how often the guesses are wrong | B10 narration + landscape note | ✅ | Absence-of-evidence claim, stated as such. Neither primary paper reports a quantitative success/failure rate against independent truth; arXiv:2411.19158 offers the variance ratio as a *detector*, not a validated error rate. Phrased as "nobody has measured", not "it is unreliable". |
| 18 | 450 posterior samples per source; noise model trained on real HST noise cutouts | not on screen | ✅ | AJ paper: 450 samples via reverse-time SDEs; 39,254 cutouts of 64² from COSMOS and 8,747 of 32² from SMACS 0723. Verified, unused (see below). |

## Computed in this reel (`assets/gen_deconv.py`, seed 9109, 256²)

| Quantity | Value | How |
|---|---|---|
| Aperture cutoff | `k_c = 0.075` cycles/pixel | chosen to represent a seeing-limited ground-based system; the OTF above it is exactly 0 |
| Fraction of grid modes the telescope can see | **1,153 of 65,536 = 1.8%** | count of `k ≤ k_c`. The reel rounds the complement to "98% carry nothing". |
| Striping: pattern recovery | **3.58%** residual | per-row mean over 96 known-dark columns, compared against the true stripe profile |
| Information above the cutoff | **19.2%** of the truth, and **1.3×** the noise inside the source footprint (17,814 px) | ‖high-pass component‖ vs the per-pixel noise where the source is |
| **Null space: truth difference** | **52.4%** | ‖B − A‖ / ‖A‖, where B − A is projected entirely above the cutoff |
| **Null space: observation difference** | **0.0000 noise σ** | exactly zero, because `H` is identically zero there. **This is the reel's central claim and the script refuses to write a plate if it fails.** |
| Three priors, forced to equal data fit | χ²/N = **1.008, 1.007, 1.008** | regularisation strength bisected until each hits 1 |
| …yet they differ from each other by | **35.9%** | ‖rough − smooth‖ / ‖matched‖ |
| Posterior variance ÷ prior variance above the cutoff | **1.0000** | exact: where `H = 0` the posterior *is* the prior |
| Variance ratio over the observable band | **0.0006** at SNR ≈ 1000 → **0.0306** at SNR ≈ 3 (**53×**) | closed form, `var = 1/(|H|²/σ² + 1/P)` |

**The computed variance ratio and the published one are not the same
measurement and the reel never implies they are.** Mine is over Fourier modes
below the cutoff in a linear-Gaussian model; theirs is over an image-space
aperture with a diffusion prior. They span comparable ranges in the same
direction, which is why both appear in B09 — with a tag reading "published,
not measured here" under the published pair.

## Corrected before shipping

- **"133 GPU-hours" is wrong and was changed.** The paper says 133 *hours* on
  *32* V100s, which is ~4,256 GPU-hours. An earlier draft of B07 said "133
  GPU-hours", which understates the training cost by a factor of 32. The
  on-screen text now reads **"133 hours on 32 GPUs"**. This is exactly the
  class of error the DOUBLE-CHECK LAW exists to catch: a unit collapsed while
  paraphrasing.
- **The 98% figure is a rounding of 98.2%** (1 − 1153/65536). Stated as "98%".

## Verified, then deliberately NOT used

| Fact | Why it was dropped |
|---|---|
| The AJ paper's 450 samples, and its noise-score model trained on 39,254 real HST noise cutouts | A second sample count beside 256 invites the viewer to wonder which is right. One worked example per mechanism. |
| Noise ~0.04 e⁻/s against outskirt features ~0.01 e⁻/s and below | A good, concrete statement of "features below the noise", but it needs instrument-unit context the reel has no time to build. |
| The z > 0.7 upsampling limit ("factor higher than 2 is problematic") | Genuinely interesting and nearly made B09, but it introduces redshift and pixel-scale matching — a second failure mode competing with the one the episode teaches. |
| Score-based likelihood characterisation; Tweedie's formula | Mechanism detail below the resolution of a three-minute episode. |
| Richardson–Lucy deconvolution and its noise amplification | The classical baseline. Cut because the three-priors beat makes the same point more sharply and without a new named method. |
| HST/JWST diffraction limits (0.085″ at 814 nm on 2.4 m; 0.077″ at 2 µm on 6.5 m) | Computed and correct, but the episode's cutoff argument is about a *generic* aperture and specific numbers would imply the plates are of those telescopes. |

## Softened on purpose

- **"Tens of thousands"** in the narration, with **17,852** on screen. The
  voice carries the magnitude, the screen carries the figure.
- **"A real system"** rather than naming the paper in the voice. The citation
  line names it; the narration is about the mechanism, not the authors.
- **"One method's guesses held up. Qualitatively."** The sentence is
  deliberately built so the caveat cannot be skipped — it is its own sentence,
  and the word appears on screen in ink at full size.
- **"Nobody has measured how often they do not"** — an absence claim, phrased
  as an absence rather than as a defect.
- **The synthetic sky is captioned as synthetic** on B03, and no beat implies
  any plate is a real telescope image. There is no real HST, JWST or HSC image
  anywhere in this reel.

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is non-identifiability, not "AI lies".** The data genuinely has
   a null space; picking one element of it is a legitimate, useful thing to do.
   The failure is reporting the pick as a measurement.
2. **The centrepiece is a proof, not an anecdote.** B05 does not cite anyone —
   it constructs two skies and shows the observations are identical, and the
   generator asserts it.
3. **Published and computed-here are on screen together, tagged**, precisely
   because this episode is about that distinction.
4. **The strongest caveat is given the most emphasis.** "Qualitatively" is
   spoken as its own sentence and shown in ink at 22 pt — larger than most of
   the supporting text in the reel.
5. **No real observatory imagery, no reproduced figures, no redrawn plots.**
   B10's Hubble/Webb panels are empty cards standing for the comparison, not
   images of it, and they are never labelled as data.
6. **No claim that any specific published reconstruction is wrong.** The
   episode says the error rate is unmeasured, which is a different and true
   statement.
