# SOURCES — *The Universe You Can Afford.*

Ep. 07 · AI in Astronomy & Space Science

## Primary literature

| Short cite | Full source |
|---|---|
| Learning the Universe (2025) | *Learning the Universe: 3 h⁻¹Gpc Tests of a Field Level N-body Simulation Emulator* — [arXiv:2502.13242](https://arxiv.org/abs/2502.13242). **The episode's worked example.** Source of: the method (a machine-learned non-linear correction applied to the linear z=0 Zel'dovich field), the ~5% agreement on power spectrum, bispectrum and wavelet statistics at most scales, the test at (3 h⁻¹Gpc)³ across eight cosmologies, the halo-interior particle-position errors, and the "thousandth of the time" comparison. |
| Quijote (2020) | *The Quijote simulations*, Villaescusa-Navarro et al. — [arXiv:1909.05273](https://arxiv.org/pdf/1909.05273). Source of 44,100 full N-body simulations, >7,000 cosmological models in the {Ωm, Ωb, h, nₛ, σ₈, Mν, w} hyperplane, >8.5 trillion particles at a single redshift, a petabyte of data, and the explicitly stated purpose of providing enough data to train machine-learning algorithms. |
| AbacusSummit (2021) | *AbacusSummit: A Massive Set of High-Accuracy, High-Resolution N-Body Simulations* — [arXiv:2110.11398](https://arxiv.org/abs/2110.11398) · [MNRAS](https://academic.oup.com/mnras/article/508/3/4017/6366248) · [CfA project page](https://www.cfa.harvard.edu/research/abacussummit). 139 core simulations, ~60 trillion particles, 97 cosmologies, run with Abacus on Summit at the Oak Ridge Leadership Computing Facility. **Corroborating scale only — not on screen** (see `FACTCHECK.md`). |
| Zel'dovich (1970) | *Gravitational instability: an approximate theory for large density perturbations*, Astron. Astrophys. 5, 84. The approximation the whole episode turns on: one displacement per particle, x = q + D·ψ(q). |
| Field-level emulator (2023) | *Field-level Neural Network Emulator for Cosmological N-body Simulations* — the earlier emulator that arXiv:2502.13242 tests at larger volumes. |
| νGAN (2025) | *νGAN: A Deep Learning Emulator for Cosmic Web Simulations with Massive Neutrinos* — [IOPscience, ApJ](https://iopscience.iop.org/article/10.3847/1538-4357/ae3de4). Second data point for "generate a realisation in seconds"; not quoted on screen. |
| Super-resolution emulator (2020) | *Super-resolution emulator of cosmological simulations using deep physical models* — [MNRAS 495, 4227](https://academic.oup.com/mnras/article/495/4/4227/5843286). Reports a ~11× speedup; deliberately unused (see `FACTCHECK.md` § "Verified, then deliberately NOT used"). |

## Reel provenance

| Item | Value |
|---|---|
| Brief | `E:/NEU/Jobs/Humanitarians_AI/weekly_stem_videos/ideas.md` → Astronomy, topic **07** ("Simulating the universe") |
| Series | AI in Astronomy & Space Science, **Ep. 07** |
| Sibling episodes | `ai-vs-the-data-deluge` (01) · `exoplanet-hunting` (02) · `gravitational-wave-detection` (03) · `galaxy-classification` (04) · `fast-radio-bursts` (05) · `mars-rover-autonomy` (06, in the other `humanitarians-youtube` tree) |
| Fact-check date | 2026-08-28, from primary sources, during this build |
| Toolkit | `brutalist.art` · skill `ai-explainer` · channel `claude-hai` |
| Slug | `simulating-the-universe` — matches the folder |
| Deliverables | 16:9 at 3840×2160 **and** 9:16 at 2160×3840, both full length, same beats |

## Generated imagery — provenance and seed

Every plate is **computed**, not illustrated. `assets/gen_cosmos.py` runs, in 2D
at 512² on a single seed (**7717**), the two calculations the episode is about:

    initial field     Gaussian random field with a CDM-like P(k) (turnover at k_eq)
    Zel'dovich        psi = -i k / k^2 * delta_k, then x = q + D * psi   (one move)
    N-body            particle-mesh: CIC deposit -> FFT Poisson -> kick -> drift,
                      200 KDK leapfrog steps in the growth factor from a = 0.10

589,824 particles on a 512² mesh — **more particles than cells on purpose**, so
the initial Lagrangian lattice does not survive as moiré in the voids.

| Asset | What it is |
|---|---|
| `ic.png` | the starting field, rendered at low amplitude and the same polarity as the rest |
| `zeldovich.png` | the cheap guess at D = 1 |
| `nbody.png` | the particle-mesh result at D = 1, same seed |
| `residual.png` | N-body minus Zel'dovich, smoothed — terracotta where N-body piles up more mass, ink where less |
| `power.png` | the **measured** P(k) of both fields, log-log |
| `halo_zoom.png` | the same region in both, centred on the largest disagreement, wrapped periodically |

**Why the Zel'dovich growing mode is the N-body's initial condition.** The
integrator is written so that x = q + D·ψ is an *exact* solution in the linear
regime. The two plates therefore start identical by construction, and the
difference at D = 1 is genuinely the non-linear part rather than an artefact of
mismatched starting conditions. Getting that wrong is what the first version did:
see `FACTCHECK.md` § DOUBLE-CHECK LAW.

**Measured discrepancy** (median |ΔP/P|, Zel'dovich against particle-mesh):
**3.7% for k < 60** and **58.0% for k > 200**. Those are the two numbers B09
quotes, and they are labelled on screen as measured here.

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is that there is nothing to look at.** Eps. 01–06 all had AI
   inspecting observations. This is the first episode where the AI substitutes
   for the calculation, and B01 says so out loud so the pivot is visible.
2. **One worked example, not a survey of emulators.** Speedups in this literature
   range from ~11× to ~1000×; quoting the range would blur the mechanism.
3. **The generator reports its own error, and that is the point.** A picture that
   cannot be checked is decoration. The script prints the measured ΔP/P on every
   run, which is exactly how the first (wrong) integrator was caught.
4. **The 2D caveat is on screen, not just in the paperwork.** Every plate-bearing
   beat captions itself as a 2D toy at 512².
5. **My measured numbers are separated from published ones** in the narration and
   in the on-screen citation lines.
6. **No published figure is reproduced, redrawn or traced.**

## Not used

- No archival or licensed imagery. No AI-generated stills. No stock. No screen
  recordings. No figure from any of the cited papers reproduced or redrawn.
