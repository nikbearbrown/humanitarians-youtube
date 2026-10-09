# SOURCES — *The Same Sunspot, Twice.*

Ep. 12 · `predicting-solar-storms` · AI in Astronomy & Space Science
Checked from primary sources on **2026-10-09**, during this build.

---

## Published — the stakes

**February 2022 Starlink loss.** SpaceX launched 49 Starlink satellites on
3 February 2022 into a low deployment orbit, during the main phase of a
**moderate** geomagnetic storm, with a second moderate storm the following
day. Solar plasma heated the upper atmosphere, denser gas expanded into the
satellites' altitude, drag rose, and **38 of the 49 reentered within days**.

- The peer-reviewed figure (*Space Weather*) and NASA's own visualization
  page both give **38 of 49**.
- **A correction applied, per DOUBLE-CHECK LAW.** SpaceX's initial
  announcement, and most contemporary press, said **"up to 40"**. That was an
  early estimate, superseded by the later count. **The reel says 38** and the
  40 appears nowhere.

What makes this the right anchor: the storm was *moderate*, not severe. The
episode is not about a once-a-century event.

---

## Published — the problem this episode measures

**Ahmadzadeh, Aydin, Georgoulis, Kempton, Mahajan & Angryk (2021), "How to
Train Your Flare Prediction Model: Revisiting Robust Sampling of Rare
Events", *The Astrophysical Journal Supplement Series*** (arXiv:2103.07542).

Verbatim from the abstract:

> "We showcase the general concept of temporal coherence"

> "lack of proper understanding of this effect may spuriously enhance models'
> performance"

> "with a 60:1 imbalance ratio for GOES M- and X-class flares and a 800:1 for
> X-class flares against flare-quiet instances"

> "a partitioned collection of multivariate time series of active region
> properties comprising 4075 regions"

That last figure describes **SWAN-SF**, the benchmark built specifically to
support unbiased flare forecasting — 4,075 active regions over nine years of
SDO operations.

**The mechanism, as the flare-forecasting literature states it.** A random
split puts samples from one active region on both sides, and that information
leaking into the test set gives an overly optimistic estimate of
generalisation performance; regions can appear dozens to hundreds of times in
these datasets while presenting no apparent change. The accepted fix is to
assign all rows of a region to one side — an active-region split.

**And the fix is not free**, which the reel also says:
- An AR-level split still leaks through **sympathetic flaring in co-temporal
  active regions**.
- **Chronological (year-based) splits** have their own problem: the splits
  may not share the same distribution, because of solar-cycle dependence, and
  some test periods contain no major flares at all.
- Resampling applied **before** splitting re-introduces leakage even when an
  AR split is used afterwards; split first, then sample each subset.

---

## What is NOT claimed

**No published paper measures how large the inflation is.** Searching the
flare-forecasting literature found the leakage problem stated clearly and
repeatedly, and the AR-split fix recommended, but no result quantifying the
gap between a random-split score and an honest one on the same data.

So the reel is explicit about the division of labour: **the literature
supplies the diagnosis; this reel supplies a measurement**, on a controlled
synthetic case where the ground truth is known by construction. The episode
does not claim the measurement is novel science, and it does not claim the
numbers transfer to any real dataset — only the direction and the rough size
of the effect are claimed, and every computed beat says "computed in this
reel" on its citation line.

---

## Computed in this reel

`assets/flares.py` — the simulator, two models, the metric.
`assets/gen_solar.py` — the experiment, the self-check and all six plates.

**Seed 1212**, logged here, used for every figure. 12 repeated runs; all
headline numbers are **medians** across those runs, with the full spread
shown on screen in `spread.png`.

| | |
|---|---|
| Catalogue | 350 active regions, observed hourly for 1–4 days → ~20,200 rows |
| Features | 4 per row: a constant per-region fingerprint + a slow random walk (σ 0.012/h) + measurement noise (σ 0.14) |
| Label | an M+ class flare within 24 h; a region either flares repeatedly or essentially never does |
| Base rate | ~1 in 58 — chosen to match SWAN-SF's reported 60:1 |
| Baseline model | logistic regression, class-weighted, gradient descent. LOW capacity |
| Flexible model | k-nearest-neighbour, k = 25. HIGH capacity |
| Metric | **TSS** (True Skill Statistic = TPR − FPR), the standard in flare forecasting, at the threshold that maximises it |
| Splits | random rows · by active region · chronological |

**Why these two models.** The point is not that kNN is good or bad; it is
that *capacity* is what converts region identity into an inflated score. A
model that can only draw one hyperplane cannot memorise which region a row
came from. A model that answers by finding the most similar row can, and
after a random split the most similar row is very often the same region an
hour earlier. Logistic regression and kNN are the clearest pair that differ
on exactly that axis while both being honest, legible methods.

**Why TSS and not accuracy.** At a 1-in-58 base rate, always predicting
"quiet" scores 98% accuracy. TSS scores it 0. The field uses TSS for this
reason, and so does the reel.

---

## Verified, then deliberately NOT used

| Fact | Why |
|---|---|
| Published TSS values for specific flare-prediction models | They are not comparable across papers precisely *because* of the splitting problem this episode is about. Quoting one as a benchmark would undercut the argument. |
| NOAA SWPC operational forecast verification statistics | Searched; no source found evaluating SWPC's operational products on SWAN-SF or giving comparable skill scores. Not used rather than approximated. |
| The 279% TSS increase reported from outlier removal in one SWAN-SF study | A different methodological knob, from a configuration chosen for best results. Adding it would blur which effect the episode is measuring. |
| Carrington 1859, Québec 1989, Halloween 2003 | The reel deliberately uses a *moderate* 2022 storm with a measured consequence instead of a historic extreme. The point is that this is routine, not apocalyptic. |
| Flare radiation reaching Earth in ~8 minutes, and L1 solar-wind warning times of ~15–60 minutes | A genuinely interesting constraint, but it is about *lead time*, a different limit from the one this episode measures. Cut to keep one spine. |

---

## Softened on purpose

- **"38 of 49"**, never "about 40". See the correction above.
- **The experiment is never presented as a model of the Sun**, of SWAN-SF, or
  of any published result. The region count, lifetimes, feature dimension and
  base rate are chosen to be illustrative of the mechanism.
- **The reel does not say published flare-forecast scores are wrong.** It says
  the literature names this failure mode, that the fix is known, and that the
  size of the error is worth seeing once. Which papers are affected is not a
  claim this reel makes or could support.
- **"The flexible model loses to the baseline"** is a statement about *this*
  synthetic case with *these* two models. It is not a claim that simple models
  beat flexible ones on real flare data.
- **Medians across 12 runs**, with the full spread on screen, because a single
  split is noisy — a point the flare literature makes about TSS specifically.
