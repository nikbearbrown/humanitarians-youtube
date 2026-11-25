# SOURCES — Significant On Tuesday

Week ending 2026-11-06 · `ai-` track.

## Primary evidence — generated here

This reel's evidence is **not** a citation. Every number is produced by code
shipped in this folder and reproduces exactly from one seed.

| File | What it establishes |
|---|---|
| `peeking_evidence.py` | The whole argument: false-positive rates under fixed and repeated testing, the winner's curse, the two corrected boundaries, and the power/sample-size trade |
| `beat_data.py` | The exact arrays that appear on screen — the hero walk, the bar values, the density, the boundary table |
| `power_tradeoff.py` | Where group-sequential testing starts paying for itself, swept across power levels and two effect sizes |
| `peeking_results.json`, `beat_data.json` | Machine-readable output of the above; the beat sheet is populated **from these files**, never retyped by hand |

**Seed: `20261106`.** `numpy.random.default_rng`, no wall clock, no
environment dependence. `power_tradeoff.py` offsets the seed per condition
(`SEED + 1`, `+ 7`, `+ 99`) so the calibration sample, the null sample and the
power sample are independent rather than reused.

### Reproduce

```bash
python peeking_evidence.py && python beat_data.py && python power_tradeoff.py
```

Runtime is a few seconds each; `numpy` and `scipy` are the only dependencies.

## Method, stated plainly

- **Design:** A/A test. Two arms, both converting at 10%, 2,000 visitors per
  arm, 20,000 independent repetitions. Because the arms are identical, every
  significant result is a false positive by construction — no effect size has
  to be assumed and no prior is needed.
- **Test:** two-proportion z, pooled variance, equal arm sizes, two-sided at
  α = 0.05 (z = 1.95996). A look with zero conversions in both arms has no
  variance; it yields z = 0 rather than dividing by zero, which cannot create
  a false positive.
- **Peeking rule:** evaluate at each look, stop at the first crossing. This is
  the behaviour being measured, not a strawman — it is what "check it until
  it's significant" means operationally.
- **Calibrated boundary:** the 95th percentile of the maximum |z| across the
  20 looks, estimated on a *separate* simulated sample and then scored on the
  held-out one. This is a Pocock-style constant boundary obtained numerically
  rather than from a table.
- **Error bars:** Wilson 95% intervals on every simulated rate
  (`rate_ci`), so simulation noise is visible rather than implied.

## Prior work this result is consistent with

The phenomenon is long-established; the simulation re-derives it rather than
reporting it, and no figure in the reel is taken from any of these.

- **Armitage, McPherson & Rowe (1969)**, *Repeated significance tests on
  accumulating data*, J. Royal Statistical Society A — the original
  demonstration that repeated testing inflates the type I error rate.
- **Pocock (1977)**, *Group sequential methods in the conduct of clinical
  trials*, Biometrika — the constant-boundary correction the calibrated
  boundary here reconstructs numerically.
- **O'Brien & Fleming (1979)**, *A multiple testing procedure for clinical
  trials*, Biometrics — the alternative spending shape, mentioned in neither
  the narration nor on screen because the reel does not demonstrate it.

## Not used

- No screenshots, no lifted figures, no third-party chart images. REBUILD LAW:
  every graphic is a native Remotion scene driven by the arrays above.
- No published A/B platform's error-rate claims, no vendor benchmarks, and no
  estimate of how often real teams peek — see FACTCHECK, "Claims considered
  and cut".

## Components

New this reel, built against a GATE L punt and logged to
`TEMPLATE-MISSES.md`:

- `runtime/remotion/src/scenes/ThresholdWalk.tsx`
- `runtime/remotion/src/scenes/ThresholdWalk916.tsx`

Reused from the shared library: `ClaudeComposerAsk`,
`BrutalistHesitantWriter`, `ClaudeBarChart`, `DistributionShape`, `CardSet`,
`HaiTitleOutro` (and their `916` companions).
