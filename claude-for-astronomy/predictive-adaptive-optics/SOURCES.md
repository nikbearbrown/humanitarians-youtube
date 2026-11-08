# SOURCES — *Aim Where It's Going.*

Ep. 16 · `predictive-adaptive-optics` · AI in Astronomy & Space Science

Every claim on screen is either **PUBLISHED** (traceable to one of these) or
**COMPUTED HERE** (produced by `assets/gen_ao.py`, seed 1616, eight asserted
claims). The two are never blended in a single sentence.

---

## Primary — predictive wavefront control on sky

**van Kooten, Jensen-Clem, Cetre, Fowler, et al. (2022).** *Predictive
wavefront control on Keck II adaptive optics bench: on-sky coronagraphic
results.* **JATIS 8(2) 029006.** Preprint arXiv:2108.08932 (2021).
<https://arxiv.org/abs/2108.08932> · <https://doi.org/10.1117/1.JATIS.8.2.029006>

Used for:
- the loop timing — the system takes **"a total of 1 to 2 milli-seconds"** to
  measure and correct the wavefront;
- the contrast result — **"we find a contrast gain of 2.03 at separation of
  3"** (3 λ/D), with up to ~3 at larger separations, through NIRC2's L-band
  vortex coronagraph;
- the motivation — when the atmospheric coherence time is short relative to
  the AO speed, **"the servo-lag error becomes the dominate error term of the
  AO system."**

> **The separation ranges differ between the preprint and the journal
> version** (4–6 λ/D vs 3–7 λ/D). The episode says "close in" and puts only
> the 3 λ/D figure on screen, which both versions agree on.

**Fowler, Jensen-Clem, Cetre, van Kooten, Salama, Bouchez, Surendran,
Guthery, Marin, Cisse, Service, Bond, Por, Skaf, Gauvin (2026).** *Ground
control to major time-lag: on-sky results of data-driven predictive wavefront
control at Keck Observatory.* arXiv:2606.20838, submitted 18 Jun 2026 (SPIE).
<https://arxiv.org/abs/2606.20838>

Used for:
- **"a 20% performance improvement over a classic integrator"** in
  Shack-Hartmann wavefront residuals, on-sky engineering tests;
- the honest counterweight — **"NIRC2 imaging through the Brackett
  Gamma=2190nm filter shows comparable performance between an integrator and
  predictor"**, for both Strehl ratio and coronagraph-free contrast;
- the authors' own hedge — the principal-component gain is **"a modest
  improvement (on the order of 3% less area under the curve of component
  strength)"**.

> This is a **2026 preprint from engineering tests**, not a refereed
> performance paper. B09 dates both rows on screen for exactly that reason.

## Primary — the theory of the delay

**Doelman, N. J. (2020).** *The minimum of the time-delay wavefront error in
adaptive optics.* **MNRAS 491(4), 4719.** Preprint arXiv:1906.03128.
<https://arxiv.org/abs/1906.03128> · <https://doi.org/10.1093/mnras/stz3237>

Assuming von Kármán statistics and frozen flow, an optimal **temporal**
predictor reduces phase variance by **at most a factor of 1.77** versus the
zero-order prediction ordinary AO uses — equivalently it tolerates a delay
about **1.41×** longer for the same residual. Performance depends on the
product of time delay, wind speed and the reciprocal of the outer scale.

> **DELIBERATELY NOT PUT ON SCREEN, AND WHY.** This bound is for temporal
> prediction of the wavefront; the gains computed here are for the
> **band-limited** part a 60-mode deformable mirror can shape, which is a
> different quantity. The two are not in conflict and the episode does not
> claim to have beaten, confirmed or tested the 1.77 bound. See FACTCHECK.

## Primary — the EOF method, and where it runs

**Guyon, O. & Males, J. (2017).** *Adaptive optics predictive control with
empirical orthogonal functions (EOFs).* arXiv:1707.00570.
<https://arxiv.org/abs/1707.00570>

The data-driven predictor the Keck and Subaru work builds on. EOF predictive
control is in routine operation at **Subaru / SCExAO** and has been
demonstrated on **Keck II**.

**Fowler, J., van Kooten, M. A. M., Jensen-Clem, R. (2022).** *Battle of the
Predictive Wavefront Controls: Comparing Data and Model-Driven Predictive
Control for High Contrast Imaging.* arXiv:2208.00984.
<https://arxiv.org/abs/2208.00984>

Used for the stated range of the problem: **"AO lag of roughly 1 to 5
milliseconds"** lets the wavefront change before correction is applied,
creating speckles near the star.

## Secondary — the instrument

W. M. Keck Observatory adaptive optics documentation and the Keck II pyramid
wavefront sensor literature: a **349-actuator Xinetics deformable mirror**
(~249 illuminated through the hexagonal pupil), wavefront-sensor / DM spatial
sampling of **0.56 m**, 244 subapertures; the PyWFS real-time controller runs
the loop at **1 kHz**, and **the AO delay is determined to be 1.7 ms** at that
full frame rate.
<https://www2.keck.hawaii.edu/inst/ao/> · <https://arxiv.org/abs/2107.07601>

Used for: B03's `1 kHz · 1.7 ms` chip. **1.7 ms is the measured figure that
anchors the whole episode**, and it is the only delay number on screen.

## Secondary — reinforcement learning on sky, for context

**Nousiainen, Chambouleyron, Neichel, Cetre, Sauvage, Alagao, Kasper, Dray,
Fetick, Engler (2026).** *On-sky demonstration of reinforcement learning for
adaptive optics control.* A&A (accepted); arXiv:2606.10771.
<https://arxiv.org/abs/2606.10771>

First on-sky demonstration of an RL controller (PO4AO), on the Papyrus AO
system at the 1.52 m telescope at Observatoire de Haute-Provence. It
**"consistently outperformed the standard integrator in all tested
configurations"**, despite ~750 µs of added latency from an unoptimised Python
implementation.

> **NOT USED ON SCREEN.** It is a different telescope, a different control
> paradigm, and the abstract gives no quantitative margin. Logged because it
> is the most relevant 2026 result in the field and leaving it out of the
> record would be a selective reading.

## Textbook relations used

- Fried parameter and the **Kolmogorov phase structure function**
  D_φ(r) = 6.88 (r/r₀)^(5/3).
- The **von Kármán phase PSD**
  Φ(f) = 0.0229 r₀^(−5/3) (f² + 1/L₀²)^(−11/6), f in cycles/m.
- **Greenwood / atmospheric coherence time** τ₀ = 0.314 r₀ / v, and the
  servo-lag variance σ² = (τ/τ₀)^(5/3).
- **Maréchal** approximation, Strehl ≈ exp(−σ²).
- **Taylor frozen-flow hypothesis.**

Standard references: Roddier, *Adaptive Optics in Astronomy* (1999); Hardy,
*Adaptive Optics for Astronomical Telescopes* (1998); the Subaru/Guyon
astronomical-optics lecture notes
<https://subarutelescope.org/staff/guyon/15teaching.web/00AstrOptics.web/>

> **These are relations, not data.** The episode does not take any of them on
> faith: `gen_ao.py` integrates the PSD and recovers the 5/3 exponent and the
> 0.314 constant from scratch, and asserts both. That 6.88 × 0.314^(5/3) =
> 0.9980 is *why* the coherence time is defined the way it is, and the
> episode says so.

---

## Deliberately NOT used

| Source / idea | Why not |
|---|---|
| Doelman's 1.77× ceiling as an on-screen number | measures a different quantity than this episode's band-limited gain; stating them side by side would imply a comparison that was never run |
| The RL on-sky result (arXiv:2606.10771) | different telescope, different method, no quantitative margin in the abstract |
| The 2208.00984 EOF-vs-Fourier head-to-head verdict | the abstract states the study design, not a winner; no result to quote |
| "Wind-driven halo" imagery from VLT/SPHERE | would need a real instrument image, and REBUILD LAW forbids lifting figures |
| Mauna Kea site seeing statistics (r₀, τ₀) | not located in a citable form; the simulation's r₀ = 15 cm and v = 10 m/s are therefore presented as **stated parameters**, never as Mauna Kea values |
| Strehl figures from the simulation | the Maréchal conversion is implemented but a Strehl number here would describe a 60-mode toy, not a telescope |
| CNN / neural-net predictive control results | real, but the episode's argument is that the *limit* is the sensor, and a nonlinear model does not change that argument |

## Measured here but NOT claimed on screen

1. **The in-band share of total phase variance (~79%).** The 60 corrected
   modes hold most of the pupil's phase variance but only 16% of its
   *drift*. The drift share is stable; the variance share is not — a single
   screen's lowest modes scatter hard, and the measured pupil variance
   (202 rad²) sits well above the ideal-spectrum value (176 rad²) for exactly
   that reason. Only the 16% is on screen.
2. **The two-layer condition.** Gains of 195× clean and 5.24× at realistic
   noise sit within 10% of the three-layer numbers, so `noise.png` draws one
   layer and three. The full table is in FACTCHECK.md.

## Cost

**$0.00.** Kokoro `af_bella` locally for narration; Manim and Remotion for
picture; numpy/scipy/Pillow for the experiment. No image model, no
ElevenLabs, no API keys. Fellow Tier throughout.
