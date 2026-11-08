# FACTCHECK — *Aim Where It's Going.*

Ep. 16 · `predictive-adaptive-optics`

Every number that appears on screen, with its status. **PUBLISHED** means it
comes from a source in `SOURCES.md`. **COMPUTED** means `assets/gen_ao.py`
produced it on seed 1616 and asserts it — the generator writes no plate if any
of its eight claims fails.

---

## On-screen claims

| # | Claim | Where | Status | Check |
|---|---|---|---|---|
| 1 | Keck II runs its pyramid sensor at **1 kHz** and its measured AO delay is **1.7 ms** | B03 chip | **PUBLISHED** | Keck PyWFS literature; "the AO delay is determined to be 1.7 milli-seconds when running the PyWFS at its full frame-rate" |
| 2 | At 10 m/s, 1.7 ms of delay is **1.7 cm** of sideways travel | B03, B00 | **COMPUTED** (arithmetic) | 10 × 0.0017 = 0.017 m |
| 3 | r₀ = **15 cm**, so that slide is ~11% of a coherence cell | B03 rules | **STATED PARAMETER** + arithmetic | 0.017/0.15 = 0.113 |
| 4 | The servo-lag exponent is **5/3 exactly** (fitted 1.666667) | B04 chip | **COMPUTED** | spectral integral, 4 delays, log-log fit |
| 5 | The coherence time **4.71 ms** is where lag costs **1 rad²** | B04 | **COMPUTED** | τ₀ = 0.314·r₀/v = 4.71 ms; σ²(τ₀) = 0.9972 rad² |
| 6 | Only **16%** of the servo-lag error lies in modes a mirror can shape | B04, B00 | **COMPUTED** | 0.0321 / 0.2031 rad² at 2 ms |
| 7 | A **24-frame** linear filter, no physics in it | B05 | **COMPUTED** (method) | ridge on 60 Zernike modes |
| 8 | ACROSS the pupil buys **1.2×**; BACK in time buys **5.1×**; both **11.2×** | B06 | **COMPUTED** | at 0.05 rad RMS per mode, one layer |
| 9 | Quiet sensor **331×**; realistic sensor **11.2×**; three layers **4.8×** | B07, B10, B00 | **COMPUTED** | gains over the zero-order hold |
| 10 | Servo lag is about **a fifth (22%)** of the error budget | B08 | **DERIVED** from 9 + 11 | φ = 0.20/(1 − 1/11.2) = 0.2194 |
| 11 | Keck reports **20%** better Shack-Hartmann residuals | B08, B09 | **PUBLISHED** | arXiv:2606.20838 abstract |
| 12 | 2021, vortex coronagraph: contrast **2.03×** close in | B09 | **PUBLISHED** | arXiv:2108.08932, at 3 λ/D |
| 13 | 2026, Brackett gamma: Strehl and contrast **comparable** | B09 | **PUBLISHED** | arXiv:2606.20838 |
| 14 | Three layers in clean air still gave **183×** | B10 | **COMPUTED** | the refused expectation |

---

## The eight asserted claims

`gen_ao.py` writes nothing unless all eight hold. Reproduced on seed 1616:

```
  translation operator is exact                  ok   rel err 2.2e-07
  Kolmogorov lag exponent is 5/3                 ok   1.666667
  sigma^2(tau0) = 1 rad^2                        ok   0.9972 rad^2
  screens reproduce the spectral integral        ok   ratio 1.0205
  in-band lag error goes as tau^2, not tau^(5/3) ok   1.990
  prediction still wins at realistic noise       ok   11.20x (1 layer) 4.82x (3 layers)
  more layers cost the predictor                 ok   11.20 > 5.24 > 4.82
  looking BACK beats looking ACROSS              ok   L1 5.1/1.2  L2 3.7/1.0  L3 3.7/1.1
```

### Why the exponent claim is worth asserting

σ²_lag(τ) = (τ/τ₀)^(5/3) with τ₀ = 0.314 r₀/v is usually quoted as two
separate facts. They are one fact. The lag error is the structure function
evaluated at the displacement v·τ:

```
  D(vτ) = 6.88 (vτ/r0)^(5/3) = 6.88 · 0.314^(5/3) · (τ/τ0)^(5/3)
        = 0.9980 · (τ/τ0)^(5/3)
```

**The constant 0.314 exists precisely so that 6.88 × 0.314^(5/3) = 1.** The
coherence time is the structure function in disguise, and the episode says so.
The generator recovers both from the spectrum without assuming either.

---

## The full measured table

Gains are over the zero-order hold, at a 2 ms delay, 24 taps, λ chosen on a
held-out validation split and scored once on held-out test atmospheres.
8 train / 2 validation / 2 test, each an independent 8192-frame atmosphere.

| layers | noise (rad RMS/mode) | zero-order | space only | time only | both |
|---|---|---|---|---|---|
| 1 | 0.00 | 0.0321 | 17.7× | 292× | **331×** |
| 1 | 0.01 | 0.0381 | 4.9× | 10.6× | 24.4× |
| 1 | 0.02 | 0.0561 | 2.2× | 6.1× | 14.3× |
| 1 | **0.05** | 0.1821 | **1.2×** | **5.1×** | **11.2×** |
| 1 | 0.10 | 0.6319 | 1.1× | 5.3× | 11.6× |
| 2 | 0.00 | 0.0608 | 0.9× | 123× | 195× |
| 2 | **0.05** | 0.2108 | 1.0× | 3.7× | 5.2× |
| 3 | 0.00 | 0.0488 | 1.9× | 118× | **183×** |
| 3 | **0.05** | 0.1988 | 1.2× | 3.7× | **4.8×** |

Split robustness, four rotations of the train/validation/test assignment, at
noise 0.05: **1 layer 11.31 ± 0.10 · 2 layers 5.28 ± 0.08 · 3 layers
4.89 ± 0.05.** The on-screen numbers are rounded from the canonical split.

---

## Claims considered and REFUSED

**1 · "Prediction beats a faster loop."** Checked and false in this setup.
Halving the delay from 2 ms to 1 ms cuts the in-band lag error 0.0321 → 0.0081
(**4.0×**); prediction at 2 ms with a realistic sensor is **11.2×**. The draft
verdict line claiming otherwise was rewritten before it reached the beat
sheet.

**2 · "More atmospheric layers break the predictor."** This was the working
hypothesis. It is **wrong in clean air**: three layers still gave 183×,
because a sum of frozen translations is still a linear time-invariant process
and a linear filter handles any number of them. Layers only cost once the
sensor is noisy (11.2× → 4.8×). B10 states the refusal out loud.

**3 · "Spatial prediction from one frame is worth having."** Measured at
**1.2×** with one layer and **1.0×** with two opposed layers — i.e. nothing.
A single snapshot carries no direction. Reported as the measured near-zero it
is, not inflated.

**4 · "This simulation beats / confirms / tests Doelman's 1.77× bound."**
Refused. That bound is on temporal prediction of the wavefront; the gains here
are on the band-limited part a 60-mode mirror can shape. **Different
quantities.** The bound is in SOURCES.md and nowhere on screen.

**5 · "The in-band share of phase variance is 79%."** Refused as unstable:
the measured pupil variance (202 rad²) and the ideal-spectrum value
(176 rad²) differ by 15% because a single screen's lowest modes scatter hard.
Only the **16% drift share** — whose numerator averages 12 atmospheres and
whose denominator is an exact integral — goes on screen.

**6 · "r₀ = 15 cm and v = 10 m/s describe Mauna Kea."** Refused. No citable
site statistic was located, so they are presented as **stated simulation
parameters** in the citation line of B03 and B04, never as measurements.

**7 · "Keck's predictive control gives a 2–3× contrast gain."** Narrowed. The
preprint and the journal version disagree on the separations for the ~3×
figure (4–6 λ/D vs 3–7 λ/D). Only **2.03× at 3 λ/D**, which both agree on,
goes on screen, and B09 says "close in" rather than naming a range.

**8 · "AI forecasts the turbulence."** The predictor here is ridge regression
— linear, 1,440 parameters, fitted once. B05 says "one linear filter" and
"no physics inside". The episode does not dress it up, and the narration's
word for what it does is *fit*, not *learn to understand*.

---

## Known limitations, stated plainly

- **One wind direction family.** Layers differ in speed and may blow in
  **opposite** directions along one axis; genuinely two-dimensional direction
  diversity is not simulated. Opposed layers already defeat single-frame
  spatial prediction, which is the effect the episode uses.
- **No boiling.** Every layer is strictly frozen. Real turbulence has a finite
  lifetime, which would reduce every gain reported here. The episode's claim
  is therefore an **upper bound** on what frozen flow allows, and it says the
  limit comes from the sensor *within that model*.
- **No closed loop.** This measures open-loop prediction error, not a servo
  with its own transfer function. A real integrator has memory and sits
  somewhere between the zero-order hold and the predictor.
- **Noise is white and modal.** Real wavefront-sensor noise is correlated
  across subapertures and depends on guide-star magnitude.
- **The 60-mode band is a stand-in** for a deformable mirror's influence
  functions, not a model of a specific DM.
- **Screens are finite.** 81.92 × 40.96 m at 2 cm against L₀ = 25 m, so the
  lowest spatial frequencies are under-represented. This is why the headline
  lag numbers are integrated off the spectrum instead, and why the screens are
  only used as a cross-check (ratio 1.02) and for the modal telemetry, where
  ratios are robust.

## Two numbers corrected during the build

- A comment in `ao.py` asserted the screen generator was verified; it was
  **off by exactly 2** in variance (a spurious √2), caught by comparing
  against the exact discrete PSD rather than by eye. The comment now records
  the bug.
- The spectral integral's recovered exponent was **1.6637**, not 5/3, until
  the low-frequency cut-off was lowered from 1e-5 to 1e-8: for Kolmogorov the
  structure function's low-f tail falls only as fmin^(1/3), and the truncation
  is τ-dependent, so it bends the fitted slope. At 1e-8 it is 1.666667.
