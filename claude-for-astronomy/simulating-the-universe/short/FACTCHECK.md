# FACTCHECK — *The Universe You Can Afford.*

Ep. 07 · AI in Astronomy & Space Science · checked 2026-08-28 against the sources
in `SOURCES.md`. Every number that reaches the screen or the narration is here.

| # | Claim (beat) | Verdict | Source | Note |
|---|---|---|---|---|
| 1 | You cannot run an experiment on the universe, so a theory is tested by simulating it (B02, B11) | **VERIFIED** — framing, not a number | Standard cosmological practice; the whole rationale for the Quijote and AbacusSummit suites | Stated as method, not as a quotation |
| 2 | Testing a theory properly needs thousands of simulations, because you are searching a parameter space (B02, B03, B11) | **VERIFIED** | Quijote spans >7,000 cosmological models in a 7-parameter hyperplane, explicitly to enable inference and ML | |
| 3 | Quijote is 44,100 N-body simulations (B03, B00 props) | **VERIFIED** | *The Quijote simulations*, arXiv:1909.05273 — abstract: "a set of 44,100 full N-body simulations" | Narration says "forty-four thousand"; the on-screen counter carries 44,100 |
| 4 | Across more than 7,000 cosmological models (B03) | **VERIFIED** | Same — "spanning more than 7,000 cosmological models" | |
| 5 | More than 8.5 trillion particles (B03) | **VERIFIED** | Same — "more than 8.5 trillions of particles" at a single redshift | |
| 6 | Built as training data for machine learning (B03) | **VERIFIED** | Same — stated purpose is to "provide enough data to train machine learning algorithms" | |
| 7 | N-body has no shortcut: deposit mass, solve the field, kick, drift, repeat hundreds of times (B04, B11) | **VERIFIED** | The standard particle-mesh loop; it is also literally the loop implemented in `assets/gen_cosmos.py` | The on-screen loop labels are the four stages of that implementation |
| 8 | The Zel'dovich approximation moves every particle once, in a straight line (B05) | **VERIFIED** | Zel'dovich 1970; x = q + D·ψ(q), a single displacement with a fixed direction | The displacement field in the plates is computed from the relation, not drawn |
| 9 | It is accurate while the field is smooth and wrong once structures collapse (B05) | **VERIFIED** | Standard result (shell crossing); also **measured here** — see #14 | |
| 10 | The emulator applies a learned non-linear correction to the linear Zel'dovich field rather than integrating gravity (B06, B08, B11) | **VERIFIED** | *Learning the Universe: 3 h⁻¹Gpc Tests of a Field Level N-body Simulation Emulator*, arXiv:2502.13242 — "uses machine learning to apply a non-linear correction to the linear z=0 Zeldovich approximation (ZA) fields" | |
| 11 | Agreement within ~5% on power spectrum, bispectrum and wavelet statistics at most scales (B07, B00 props, B11) | **VERIFIED** | Same — "the power spectrum, bispectrum and wavelet statistics of the raw particle fields agree with the N-body simulations within ~5% at most scales" | "at most scales" is load-bearing and is preserved in the narration's scoping |
| 12 | A thousandth of the N-body time (B07, B00 props, B11) | **VERIFIED** | Same — "the emulator can create z=0 particle fields in a thousandth of the time required for N-body simulations" | At (3 h⁻¹Gpc)³ volumes specifically |
| 13 | Reported errors sit in the highly non-linear interiors of haloes (B09) | **VERIFIED** | Same — "the emulator has slight errors in the positions of particles in the highly non-linear interior of the halo" | The reel says "inside dense haloes" |
| 14 | The Zel'dovich approximation is ~4% off on large scales and ~58% off on small ones (B09) | **MEASURED HERE, not published** | `assets/gen_cosmos.py` — median \|ΔP/P\| between the Zel'dovich field and the particle-mesh N-body field on the same seed: 3.7% for k<60, 58.0% for k>200 | **Flagged in PEDAGOGY §4.** Narration says "in my own two-D run"; the citation line says "percentages measured here". A 2D toy at 512², one dimension short and at the wrong scale — it shows the *shape* of the error, not a literature value |
| 15 | An emulator can only be trusted inside the box of cosmologies it was trained on (B10, B11) | **VERIFIED — general property** | Standard out-of-distribution limitation of surrogate models; arXiv:2502.13242 itself motivates its own test set by noting the emulator was trained at (h⁻¹Gpc)³ and had to be re-tested at (3 h⁻¹Gpc)³ | Framed as a property of the method, not as a quoted claim |
| 16 | The training set is N-body output, so the emulator is a compression of simulations already paid for (B10, B11) | **VERIFIED — inference, labelled** | Follows directly from #10 and #3 | Stated as reasoning on screen, and the citation line says the cost is already paid |

## Verified, then deliberately NOT used

- **AbacusSummit's 139 simulations, ~60 trillion particles, 97 cosmologies on
  Summit** (arXiv:2110.11398). Real and impressive, and a second suite on screen
  would have made B03 a list instead of a point. It stays in `SOURCES.md` as the
  corroborating second data point for "thousands of runs".
- **A node-hours or core-hours figure for a flagship run.** Several are quoted in
  secondary write-ups (e.g. ~350,000 node-hours for AbacusSummit; ~130 million
  core-hours for TNG50) and I could not confirm either from the primary paper
  text I could reach. Following the Ep. 05 and Ep. 06 precedent, a figure whose
  provenance will not check comes out entirely rather than being softened. The
  episode makes the cost argument with the **relative** number (1/1000), which is
  both verified and the one that matters.
- **Other emulator speedups** — ~11× for a super-resolution emulator, ~600× for a
  GPU modified-gravity emulator, "seconds on a GPU" for a GAN cosmic-web
  generator. All real; quoting a range would blur the single worked example.
- **The 2LPT improvement over Zel'dovich.** Correct and relevant, and one more
  approximation than a three-minute reel can introduce.

## Imagery

**No published figure is reproduced anywhere in this reel.** Every plate is
computed by `assets/gen_cosmos.py`, which runs a Gaussian random field, a
Zel'dovich displacement and a particle-mesh N-body solve in 2D at 512². The
"cheap guess versus the real thing" comparison, the residual, the measured power
spectra and the halo zoom are all outputs of that run on one shared seed. Every
beat that shows a plate captions it as a 2D toy.

## DOUBLE-CHECK LAW — the fact-check of the fact-check

1. **The first version of the generator was wrong, and it would have shipped a
   false picture.** Its particle-mesh integrator omitted the Hubble drag term and
   mis-scaled the initial velocity, so the two calculations disagreed by a factor
   of twenty on the largest scales — where they should agree almost exactly. It
   was caught because the script prints the measured ΔP/P and the number was
   absurd (1841%). The equation of motion was then derived properly, fixed by
   requiring the Zel'dovich growing mode to be an exact solution in the linear
   regime, and the numbers moved to 3.7% / 58% — which is the physically expected
   behaviour. **A generator that reports its own diagnostics catches this; one
   that only draws pictures does not.**
2. **The temptation was to call the emulator "wrong".** It is not: 5% on the
   statistics people actually use, at a thousandth of the cost, is a good trade.
   B07 lands the win before B09 and B10 price it.
3. **The second temptation was to imply the emulator removes the need for
   N-body.** It cannot — it is trained on N-body. B10 exists to say so.
4. **My own measured numbers are labelled as mine**, in the narration and in the
   on-screen citation, precisely because they sit next to published ones.
