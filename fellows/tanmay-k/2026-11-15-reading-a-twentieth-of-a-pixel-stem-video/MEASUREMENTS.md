# Week 31 — Measurements (our own simulations, 2026-11-16)

Everything here is code in `experiment/`, run on one laptop with numpy. No telescope data was used and none is claimed.

## 1. How well a line centre is read from counted photons (`experiment/photon_precision.py`, seed 31)
Setup: one Gaussian emission line, width (FWHM) 100 km/s (line sigma 42.47 km/s), detector pixel 0.05 nm = 22.84 km/s at H-alpha (656.28 nm, air; 1 km/s = 0.0022 nm). Each photon lands at a random wavelength drawn from the line and is binned into a pixel; the line centre is recovered from the **binned counts only** (a weighted centroid refined three times). Error is the root-mean-square miss of the recovered centre over repeated trials. No sky background, no calibration error: the ideal case.

| Photons | Measured error (km/s) | Rule: sigma / sqrt(N) (km/s) | Ratio | Error as share of one pixel |
|---|---|---|---|---|
| 10 | 14.615 | 13.429 | 1.09 | 64.0% |
| 30 | 8.449 | 7.753 | 1.09 | 37.0% |
| 100 | 4.598 | 4.247 | 1.08 | 20.1% |
| 300 | 2.679 | 2.452 | 1.09 | 11.7% |
| 1,000 | 1.449 | 1.343 | 1.08 | 6.3% |
| 3,000 | 0.836 | 0.775 | 1.08 | 3.7% |
| 10,000 | 0.459 | 0.425 | 1.08 | 2.0% |
| 100,000 | 0.142 | 0.134 | 1.06 | 0.6% |

Reading it: over four decades of light the measured error follows **width / sqrt(photons)** within 6 to 9% (the small excess is the cost of sorting photons into pixels). A hundred times the light buys ten times the precision. At 1,000 photons the error is about 6% of one pixel, which is the sense of "a twentieth of a pixel".

The exercise in the film's last beat: for a line of width 100 km/s (sigma 42.5 km/s) and a target error of 5 km/s the rule gives N = (42.5 / 5)^2 = 72 photons; the same simulation needed about 85 (the binning cost). See `FACTCHECK.md`.

## 2. Sky glow (`experiment/sky_glow.py`, seed 31, 2,000 trials each)
Same line, pixels and estimator, plus a flat background spread uniformly over the +/-600 km/s window, **no background subtraction**.

| Line photons | Glow photons | Measured error (km/s) | Rule (km/s) | Times the rule |
|---|---|---|---|---|
| 100 | 0 | 4.69 | 4.25 | 1.1 |
| 100 | 100 | 5.24 | 4.25 | 1.23 |
| 100 | 1,000 | 7.31 | 4.25 | 1.72 |
| 1,000 | 0 | 1.44 | 1.34 | 1.07 |
| 1,000 | 1,000 | 1.67 | 1.34 | 1.24 |
| 1,000 | 10,000 | 3.37 | 1.34 | 2.51 |

Reading it: ten times as many glow photons as line photons took the error at 1,000 line photons from 1.44 to 3.37 km/s (more than double); the rule still gives the clean-case number, so it bends when the sky is bright. Real pipelines subtract background; the film says only what this simulation did. Not tested: blended neighbouring lines, calibration error.

## 3. Toy rotating disk (`experiment/rotation_bars.py`; assumptions, not a measured galaxy)
Assumed: exponential disk, scale length 3 kpc; the centre ring collects 100,000 line photons, and each ring's photons scale as exp(-R / 3 kpc); line width 100 km/s everywhere; error = sigma / sqrt(N) x 1.08 (the binning factor measured in section 1).

| Ring radius (kpc) | Photons | Error bar (km/s) |
|---|---|---|
| 1 | 71,653 | 0.17 |
| 3 | 36,787 | 0.24 |
| 5 | 18,887 | 0.33 |
| 8 | 6,948 | 0.55 |
| 11 | 2,556 | 0.91 |
| 15 | 673 | 1.77 |

The edge ring's error bar is about ten times the inner ring's (1.77 against 0.17 km/s). The film labels this "toy disk: assumed. Not a measured galaxy."

## Limits
Ideal Gaussian line; flat glow; estimator fixed in advance; one laptop, one seed per experiment. These numbers show how counting photons limits precision in a simulation we built; they say nothing about what any real survey achieves.
