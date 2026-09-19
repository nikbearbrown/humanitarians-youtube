# SOURCES — *The Sharpest Guess.*

Ep. 09 · AI in Astronomy & Space Science

## Primary literature

| Short cite | Full source |
|---|---|
| Bayesian deconvolution with diffusion models (2024) | *Bayesian Deconvolution of Astronomical Images with Diffusion Models: Quantifying Prior-Driven Features in Reconstructions* — [arXiv:2411.19158](https://arxiv.org/html/2411.19158v2). **The episode's worked example for the prior.** Source of: the method (score-based diffusion model + Diffusion Posterior Sampling), the training set (17,852 images of 256² from TNG100 at z = 0.1527/0.1693/0.1804, 0.4 kpc/pixel), the HSC-PDR3 test data at 0.17″/pixel, "resolutions comparable to those obtained by Hubble Space Telescope (HST) images", the training and inference cost (133 hours on 32 V100s; ~100 s on one A100), the **variance ratio** as a prior-dominance metric over 256 posterior samples in an r = 30 px aperture, the two published values (0.0114 at SNR 699.3; 0.0685 at SNR 7.0), and the hallucination statement at z = 0.8463 — "a high number of features are created (hallucinated) all around the galaxy". |
| Echoes in the Noise (2025) | *Echoes in the Noise: Posterior Samples of Faint Galaxy Surface Brightness Profiles with Score-based Likelihoods and Priors*, AJ — [10.3847/1538-3881/adb039](https://iopscience.iop.org/article/10.3847/1538-3881/adb039). **The episode's external check.** HST F814W/F160W/F105W on WFC3, three COSMOS and three SMACS 0723 targets, 450 posterior samples per source via reverse-time SDEs, prior trained on PROBES/SKIRT-TNG and likelihood on real HST noise cutouts (39,254 of 64²; 8,747 of 32²). Recovers structure "which have otherwise only become visible in next-generation James Webb Space Telescope imaging" — and states plainly: **"For this work, we only provide a qualitative comparison between our reconstruction and the JWST image."** |
| NSClean (2024) | *NSClean: An Algorithm for Removing Correlated Noise from JWST NIRSpec Images*, Rauscher, PASP **136**, 015001 — [arXiv:2306.03250](https://arxiv.org/abs/2306.03250). **The contrast case.** Fits a background model in Fourier space to known-dark areas and subtracts it; "computationally undemanding, requiring only a few seconds to clean an image on a typical laptop". No machine learning is involved. |
| JWST 1/f noise | [JWST User Documentation — 1/f Noise](https://jwst-docs.stsci.edu/known-issues/1-f-noise). The physical origin: unstable reference-voltage fluctuations in the ASIC readout electronics, temporally 1/f, appearing as striping along the fast-read direction. |
| ATLAS CNN retrain (2024) | *Training a convolutional neural network for real–bogus classification in the ATLAS survey*, RASTI **3**, 385. Not used here — listed because Ep. 08 drew on it and this reel deliberately does not reuse it. |

## Reel provenance

| Item | Value |
|---|---|
| Brief | `E:/NEU/Jobs/Humanitarians_AI/weekly_stem_videos/ideas.md` → Astronomy, topic **09** ("Denoising deep space images — how AI reconstructs sharper JWST/Hubble images from noisy raw sensor data") |
| Series | AI in Astronomy & Space Science, **Ep. 09** |
| Sibling episodes | `ai-vs-the-data-deluge` (01) · `exoplanet-hunting` (02) · `gravitational-wave-detection` (03) · `galaxy-classification` (04) · `fast-radio-bursts` (05) · `mars-rover-autonomy` (06, in the other `humanitarians-youtube` tree) · `simulating-the-universe` (07) · `asteroid-impact-warning` (08) |
| Fact-check date | 2026-09-17, from primary sources, during this build |
| Toolkit | `brutalist.art` · skill `ai-explainer` · channel `claude-hai` |
| Slug | `denoising-deep-space` — matches the folder |
| Deliverables | 16:9 at 3840×2160 **and** 9:16 at 2160×3840, both full length, same beats |

## Generated imagery — provenance and seed

Every plate is **computed**, not illustrated. `assets/gen_deconv.py` runs on one
seed (**9109**) at 256² and prints its own diagnostics on every run.

    optics        the incoherent OTF of a circular pupil, in closed form:
                  H(k) = (2/pi)[arccos u - u sqrt(1-u^2)],  u = k/k_c
                  and IDENTICALLY ZERO for k > k_c.  k_c = 0.075 cycles/px
    observation   PSF convolution -> Poisson photons -> Gaussian read noise
    striping      a 1/f profile along the slow-read axis, constant per row,
                  estimated from 96 known-dark columns and subtracted
    posterior     exact: a linear-Gaussian problem with a circulant PSF is
                  DIAGONAL in Fourier space, so
                      var(k)  = 1 / ( |H(k)|^2/sigma^2 + 1/P(k) )
                      mean(k) = var(k) conj(H(k)) Y(k) / sigma^2
                  and the samples are exact, not approximate

| Asset | What it is |
|---|---|
| `twokinds.png` | striped frame · cleaned frame · blurred truth · the truth. The left pair is removable, the right pair is not. |
| `forward.png` | the chain: sky, blurred, photons, plus read noise |
| `nullspace.png` | two skies · how they differ · the one image they share |
| `threeanswers.png` | three posterior samples under three different priors, each forced to χ²/N = 1 |
| `posterior.png` | three samples · their mean · the fractional disagreement map |
| `varratio.png` | posterior variance ÷ prior variance over the observable band, against SNR |

### The two assertions that certify the plates

**1. The two kinds of denoising behave differently.** The stripe pattern is
recovered to **3.58%**; the information above the cutoff is **19.2%** of the
truth and **1.3× the noise inside the source footprint**, and no estimator
recovers it. The script raises `SystemExit` if the stripe residual exceeds 5%
or if the lost information falls below the noise.

**2. Two different skies produce the same image.** Truths differing by
**52.4%** yield observations differing by **0.0000 noise σ** — exactly zero,
because `H` is identically zero above the cutoff. The perturbation is
projected above the cutoff, concentrated on the source with an envelope, and
then *projected again*, so it remains exactly in the null space after being
made legible. The script writes nothing if this fails.

### Five errors this script caught, four of them mine

1. **The stripe residual measured the wrong thing.** It compared the cleaned
   frame against the noiseless scene, folding in the Gaussian read noise that
   stripe removal never claimed to touch, and reported 22% for a method
   recovering the pattern to 3.6%.
2. **An arbitrary threshold.** "Lost information > 20% of the truth" was a
   number chosen before any measurement; it then read 19.2%. Replaced with a
   comparison against the noise, which is what the claim actually means.
3. **The wrong comparison region.** That noise comparison was first made over
   the whole frame, where noise fills 65,536 pixels and the galaxy occupies a
   few thousand, so empty sky dominated and it reported 0.5×. Restricted to
   the source footprint: 1.3×.
4. **A prior 255× too weak.** `P *= truth.var()*size/P.sum()` gets numpy's
   unnormalised-FFT factor wrong by N. Nothing crashed — a too-weak prior just
   stops contributing, so posterior samples collapsed onto the mean, the
   "three answers" plate showed three nearly identical pictures (2.8% apart
   instead of 35.9%), and the variance ratio was computed against a mis-scaled
   prior. Found by measuring a draw's standard deviation against the galaxy's.
   Now derived: `std = sqrt(sum(spec))/N`, asserted over 24 draws.
5. **A self-check noisier than the effect it checked.** The null-space and
   peak checks were first done by Monte Carlo; at the smallest disc the
   probability is ~10⁻⁵, so 800,000 samples left ~8 hits per point and `argmax`
   returned noise. Replaced with exact quadrature and closed-form variance.

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is non-identifiability, not dishonesty.** Choosing one element
   of the null space is a legitimate and useful thing to do. Reporting the
   choice as a measurement is the failure.
2. **The centrepiece is a proof, not a citation.** B05 constructs two skies and
   shows the images are identical; the generator asserts it.
3. **Published and computed-here appear together, tagged**, because the episode
   is about that distinction.
4. **The strongest caveat gets the most emphasis.** The JWST comparison is
   qualitative, and "QUALITATIVELY" is spoken as its own sentence and shown at
   22 pt in ink — larger than most supporting text in the reel.
5. **A unit error was caught and corrected before shipping**: "133 GPU-hours"
   collapsed 133 hours × 32 GPUs by a factor of 32. See `FACTCHECK.md`.

## Not used

- No archival or licensed imagery. No AI-generated stills. No stock. No screen
  recordings. **No real HST, JWST or HSC image anywhere in this reel**, and no
  figure from any cited paper reproduced or redrawn. B10's Hubble/Webb panels
  are schematic cards — a soft blob against a tighter shape with structure —
  and are never labelled as data.
