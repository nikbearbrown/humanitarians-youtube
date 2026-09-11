# SOURCES — *The Number Went Up.*

Ep. 08 · AI in Astronomy & Space Science

## Primary literature

| Short cite | Full source |
|---|---|
| Chyba Rabeendran & Denneau (2021) | *A Two-Stage Deep Learning Detection Classifier for the ATLAS Asteroid Survey* — [arXiv:2101.08912](https://arxiv.org/abs/2101.08912). **The episode's worked example for the learned half.** Source of: the two-stage architecture (a CNN over eight postage-stamp classes, then a multi-layer perceptron scoring a temporal sequence of four detections), 99.6% accuracy on real asteroids, the 0.4% false-negative rate, the 90% reduction in candidates astronomers must screen, and the stated goal of cutting the delay between detection and submission to the Minor Planet Center. |
| Tonry et al. (2018) | *ATLAS: A High-cadence All-sky Survey System*, PASP 130, 064505 — [IOPscience](https://iopscience.iop.org/article/10.1088/1538-3873/aabadf). Source of the instrument: 0.5 m Schmidt corrector on a 0.65 m spherical primary at f/2.0, STA-1600 10560² CCD, 5.375° × 5.375° (28.9 deg²) per exposure, four 30 s frames per field per night over ~1 hour, ~26,000 deg² and ~900 images a night, limiting magnitude ~19.5 in *o*-band. |
| Impact hazard assessment for 2024 YR4 (2026) | *The Impact Hazard Assessment for Near-Earth Asteroid 2024 YR4* — [PMC12963224](https://pmc.ncbi.nlm.nih.gov/articles/PMC12963224/). **The episode's worked example for the computed half.** Source of: the discovery record (ATLAS, 27 Dec 2024, *o* = 16.5), the day-by-day Sentry/Aegis/NEODyS probability tracks and the 3.1% peak on 18 Feb 2025, the Torino history, the 60 ± 7 m JWST size, the 22 Dec 2032 date and 17.3 km/s impact speed, the 4.3% lunar figure, 504 observations from 63 observatories, and the uncertainty-region explanation this reel then derives independently. |
| Predictions of imminent impactors from LSST (2026) | *Predictions of Imminent Earth Impactors Discovered by LSST* — [arXiv:2603.05587](https://arxiv.org/html/2603.05587v1). Source of "11 imminent impactors discovered before impact as of 1 January 2026", 2008 TC3 first. Its forecasts for Rubin were verified and deliberately not used (see `FACTCHECK.md`). |
| NEO Surveyor mission (2023) | *The Near-Earth Object Surveyor Mission*, PSJ — [arXiv:2310.12918](https://arxiv.org/pdf/2310.12918). Source of "perhaps 40% of all 140-metre and larger objects have been discovered", and of the mission's projected ~76% after five years and 90% within ten years of launch. |
| 2024 YR4 lunar impact ruled out (2026) | NASA statement of **5 March 2026**, reported by [EarthSky](https://earthsky.org/space/asteroid-2024-yr4-odds-hit-earth-torino-scale-2032/): Webb observations of 18 and 26 February 2026 rule out a lunar impact on 22 December 2032; the object passes the Moon at ~21,200 km. Peak lunar probability 4.3% (1-in-23) as of 3 June 2025. |
| CNEOS Torino announcement | *Asteroid 2024 YR4 reaches level 3 on the Torino Scale* — [cneos.jpl.nasa.gov/news/news210.html](https://cneos.jpl.nasa.gov/news/news210.html). Corroborates Torino 3 and the IAWN notification. |
| Scout / 2024 BX1 | *NASA System Predicts Impact of a Very Small Asteroid Over Germany* — [JPL](https://www.jpl.nasa.gov/news/nasa-system-predicts-impact-of-a-very-small-asteroid-over-germany/). Verified, **not on screen** (see `FACTCHECK.md` § "Verified, then deliberately NOT used"). |
| ATLAS CNN retrain (2024) | *Training a convolutional neural network for real–bogus classification in the ATLAS survey*, RAS Techniques and Instruments 3, 385 — [Oxford Academic](https://academic.oup.com/rasti/article/3/1/385/7713043). Corroborating only; its 0.72% FPR / 1.00% MDR pair is deliberately unused. |

## Reel provenance

| Item | Value |
|---|---|
| Brief | `E:/NEU/Jobs/Humanitarians_AI/weekly_stem_videos/ideas.md` → Astronomy, topic **08** ("Asteroid/comet tracking — automated detection and orbit prediction for planetary defense (NASA's ATLAS system)") |
| Series | AI in Astronomy & Space Science, **Ep. 08** |
| Sibling episodes | `ai-vs-the-data-deluge` (01) · `exoplanet-hunting` (02) · `gravitational-wave-detection` (03) · `galaxy-classification` (04) · `fast-radio-bursts` (05) · `mars-rover-autonomy` (06, in the other `humanitarians-youtube` tree) · `simulating-the-universe` (07) |
| Fact-check date | 2026-09-11, from primary sources, during this build |
| Toolkit | `brutalist.art` · skill `ai-explainer` · channel `claude-hai` |
| Slug | `asteroid-impact-warning` — matches the folder |
| Deliverables | 16:9 at 3840×2160 **and** 9:16 at 2160×3840, both full length, same beats |

## Generated imagery — provenance and seed

Every plate is **computed**, not illustrated. `assets/gen_neo.py` runs on a
single seed (**8801**) and prints its own diagnostics on every run.

| Asset | What it is |
|---|---|
| `detect.png` | two epochs of a synthetic star field and their real difference, with the one mover ringed. The subtraction is deliberately imperfect — a 0.35-pixel registration error — so bright stars leave dipole residuals, which is why the artefact classes exist at all. |
| `stamps.png` | the eight postage-stamp classes, each **synthesised from its own physical model**: a trailed NEO, a point source, a 1–2 pixel cosmic ray with no PSF, a subtraction dipole, a diffraction spike, a satellite streak, a saturated-column bleed, and pure noise. All eight share one physical stretch so they are genuinely comparable. |
| `tracklet.png` | four detections over one hour, with the least-squares straight-line fit drawn, plus four unrelated artefacts. The RMS residual is printed: 0.040 vs 1.456. |
| `bplane.png` | the target plane at three uncertainty widths, rendering the actual 2-D Gaussian density. Earth's disc is the real capture radius and its offset is the real nominal miss distance, to scale. |
| `impactprob.png` | the impact probability against the width of the uncertainty region, by exact quadrature. **The x-axis is a width, not a date.** |
| `completeness.png` | the catalogued fraction by size class against the 90% mandate. A ledger of published fractions, not a computation. |

### The self-check that certifies `impactprob.png`

The plate's claim is that the rise-then-collapse is forced by geometry. That is
testable, so the script tests it. For a capture disc small compared with the
uncertainty region, the probability goes as the disc area times the 2-D density
at the Earth,

    P  ~  b_cap² / σ²  ·  exp( −d² / 2σ² )

and maximising that gives **σ_peak → d/√2 = 0.7071 d**. The script drives
`b_cap/d` down through 0.125, 0.025, 0.005 and 0.001 and asserts convergence:

```
b_cap/d=0.1250  ->  peak at sigma/d=0.7788
b_cap/d=0.0250  ->  peak at sigma/d=0.7106
b_cap/d=0.0050  ->  peak at sigma/d=0.7063
b_cap/d=0.0010  ->  peak at sigma/d=0.7063
PASS: converged to 0.7063 vs predicted 0.7071 (delta -0.0008)
```

On failure it raises `SystemExit` and writes no plate.

**Two errors were caught by this check, and both were mine, not the code's.**
The first version of the derivation used the one-dimensional argument and
predicted σ_peak = d; the Monte Carlo said 0.67 and the Monte Carlo was right,
because the uncertainty shrinks in *both* target-plane directions at once. The
second version had the correct prediction but estimated P by sampling, and at
`b_cap/d = 0.001` the peak probability is ~10⁻⁵ — so even 800,000 samples left
about eight hits per point and `argmax` over the noisy curve returned noise.
Replacing the estimator with exact quadrature made the check mean something.

**Measured discrepancy used on screen:** the capture radius
**b_cap = 8352 km = 1.311 R_E**, from v∞ = 13.20 km/s recovered from the
published 17.3 km/s impact speed.

## DOUBLE-CHECK LAW — editorial decisions

1. **A rising probability is not a worsening situation.** That is the episode,
   and it is the one thing a viewer can carry into any risk number they meet.
2. **One worked example on each side of the handoff** — ATLAS's classifier for
   the learned half, 2024 YR4 for the computed half. Not a survey of surveys.
3. **The generator reports its own error, and refuses to run when it is
   wrong.** A picture that cannot be checked is decoration.
4. **The synthetic sky says it is synthetic**, on screen, on every beat that
   shows it.
5. **Published numbers and numbers computed here are separated** in the
   narration and in the on-screen citation lines. B08 captions itself.
6. **No published figure is reproduced, redrawn or traced.** B07 rebuilds the
   published *numbers* as a native animated plot per REBUILD LAW.
7. **The hazard is not sensationalised.** No casualty estimates, no blast
   comparisons, and the phrase "city killer" — common in the sources — appears
   nowhere in the narration or on screen.

## Not used

- No archival or licensed imagery. No AI-generated stills. No stock. No screen
  recordings. No figure from any cited paper reproduced or redrawn. No real
  telescope image of 2024 YR4 or of any other object.
