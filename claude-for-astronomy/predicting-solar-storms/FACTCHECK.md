# FACTCHECK — *The Same Sunspot, Twice.*

Ep. 12 · `predicting-solar-storms` · checked from primary sources on
**2026-10-09**, during this build.

**Two kinds of number appear and they are never mixed.** *Published* figures
come from the cited sources and carry a source line. *Computed here* figures
come out of `assets/gen_solar.py`, which runs the experiment and asserts
three claims. B03 is published and says so on screen; B04–B10 are computed
here and say so.

**And a third distinction this episode needs.** The *diagnosis* — that random
splits leak through repeated observations of one active region — is
published and well established. The *measurement* of how large the resulting
inflation is, is not: searching the flare-forecasting literature found the
problem stated clearly and the fix recommended, but no paper quantifying the
gap on the same data. The reel says the literature names this, and presents
its own number as a measurement on a controlled synthetic case, never as a
new scientific result about the Sun.

## Claims on screen or in the narration

| # | Claim | Where | Verdict | Source |
|---|---|---|---|---|
| 1 | SpaceX launched **49** Starlink satellites on 3 February 2022 | B03 | ✅ | NASA visualization page; *Space Weather* study. |
| 2 | They launched into a **moderate** geomagnetic storm | B03 | ✅ | Deployment took place during the main phase of a moderate storm, with another moderate storm the next day. "Moderate" is the sources' own word, and the reel leans on it. |
| 3 | Heated atmosphere → denser gas at altitude → more drag | B03 | ✅ | NASA: solar plasma heated the atmosphere, denser gases expanded into the satellites' orbit, drag increased, the satellites de-orbited. |
| 4 | **38 of the 49** reentered within days | B03 counter + narration | ✅ | *Space Weather* (peer-reviewed) and NASA both give 38. See the correction below. |
| 5 | A flare-prediction dataset has a base rate near **1 in 60** | B04 chip, B00 | ✅ | Ahmadzadeh et al. 2021, verbatim: "with a 60:1 imbalance ratio for GOES M- and X-class flares and a 800:1 for X-class flares against flare-quiet instances". The simulation is tuned to ~1 in 58 to match. |
| 6 | One active region contributes many near-identical rows | B02, B04 | ✅ | Flare-forecasting literature: regions can appear dozens to hundreds of times in these datasets while presenting no apparent change. SWAN-SF is built from "4075 regions" of multivariate time series (Ahmadzadeh et al. 2021). |
| 7 | Shuffling rows before splitting leaks information and inflates the score | B02, B05, B10, B11 | ✅ | Same literature: a random split puts samples from one region on both sides, and that leakage gives an overly optimistic estimate of generalisation performance. Ahmadzadeh et al. 2021, verbatim: "lack of proper understanding of this effect may spuriously enhance models' performance". |
| 8 | The fix is to assign whole regions to one side | B10, B11 | ✅ | Active-region splitting is the standard recommendation in this literature. |
| 9 | TSS is the field's metric, and accuracy is not | not spoken; B07 axis label | ✅ | TSS is standard in flare forecasting precisely because it is insensitive to the base rate. At 1 in 58, always predicting "quiet" is 98% accurate and scores TSS 0. |

## Computed in this reel (`assets/gen_solar.py`, seed 1212)

350 simulated active regions observed hourly for 1–4 days (~20,200 rows,
4 features), base rate ~1 in 58. Two models chosen to differ on **capacity**:
class-weighted logistic regression, and 25-nearest-neighbour. Metric: TSS at
its best threshold. **12 repeats; every headline number is a median**, and
the full spread is on screen in B09.

| Quantity | Value |
|---|---|
| Test regions also present in training — random split | **100%** |
| Test regions also present in training — by-region split | **0%** |
| Median distance to nearest training row — random split | **0.13** |
| Median distance to nearest training row — by-region split | **0.38** |
| **Random split**: plain model · flexible model | 0.356 · **0.484** — the flexible model wins by +0.128 |
| **By-region split**: plain model · flexible model | **0.374** · 0.121 — the ordering reverses |
| The flexible model's score, random → by-region | **−75%** |
| The plain model's score, random → by-region | 0.356 → 0.374 — it does not fall |
| Chronological split: plain · flexible | 0.322 · 0.129 |
| Control: inflation at fingerprint 0.00 → 1.00 | **+0.000 → +0.306** |

**The self-check asserts three things and the script writes nothing if any
fails**: the flexible model beats the baseline under a random split; the
ordering reverses under a by-region split, with the flexible model's drop
more than 3× the baseline's movement; and the inflation vanishes when the
region fingerprint is removed.

### Two simulators discarded before this one, both my errors

1. **I simulated the leak away.** The first version used a within-region
   random walk of σ 0.12/hour on top of a unit fingerprint. Over a 72-hour
   lifetime that walk wanders further than the fingerprint itself, so rows of
   one region ended up no more alike than rows of different regions — and the
   nearest-neighbour distance came out at 0.18 under *every* split, which is
   how it showed up. A real active region's parameters barely move hour to
   hour; that is exactly why its rows are near-duplicates. Now σ 0.012.
2. **I inflated a bad number.** The second version used k=5, where the
   flexible model was simply worse than logistic regression under every
   split (0.16 against 0.31). Its "inflation" was then the inflation of a
   model nobody would ship, and proved nothing. At k=25 the model estimates a
   region's flare *rate* rather than echoing one neighbour's coin flip, and
   is genuinely competitive when evaluated honestly — which is the situation
   the episode is actually about.

Both were caught by reading the diagnostics rather than the headline: in (1)
the nearest-neighbour distances were identical across splits, and in (2) the
flexible model lost to the baseline everywhere.

## Verified, then deliberately NOT used

| Fact | Why |
|---|---|
| Published TSS values for named flare-prediction models | Not comparable across papers *because* of the splitting problem this episode is about. Quoting one as a benchmark would undercut the argument. |
| NOAA SWPC operational verification statistics | Searched; nothing found evaluating SWPC products on SWAN-SF or giving comparable skill scores. Not approximated. |
| A reported 279% TSS increase from outlier removal on SWAN-SF | A different methodological knob, from a best-case configuration. It would blur which effect is being measured. |
| Carrington 1859, Québec 1989, Halloween 2003 | The reel deliberately uses a *moderate* 2022 storm with a measured consequence. The point is that this is routine. |
| Flare X-rays arriving in ~8 minutes; L1 solar-wind warning of ~15–60 minutes | A real and interesting limit, but it is about *lead time* — a different failure from the one measured here. Cut to keep one spine. |
| Sympathetic flaring in co-temporal regions, which leaks past an AR split | True, and in SOURCES.md, but it is a second-order caveat that would complicate the fix the episode recommends. Named in the paperwork, not in the voice. |

## Softened on purpose

- **"38 of 49"**, never "about 40". SpaceX's initial announcement said up to
  40 and most contemporary press repeated it; the peer-reviewed and NASA
  figure is 38. This is the same class of correction as Ep. 11's ESA bracket,
  where the vendor's 40% was really 33%.
- **The experiment is never presented as a model of the Sun**, of SWAN-SF, or
  of any published result. Region count, lifetimes, feature dimension and
  base rate are illustrative; only the direction and rough size are claimed.
- **The reel does not say published flare scores are wrong.** It says the
  literature names this failure mode, the fix is known, and the size of the
  error is worth seeing once. Which papers are affected is not claimed.
- **"The flexible model loses to the plain one"** is about *this* synthetic
  case with *these* two models. It is not a claim that simple models beat
  flexible ones on real flare data.
- **Medians over 12 runs**, with the full spread shown, because a single
  split is noisy — a point the flare literature makes about TSS specifically.

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is the EVALUATION**, which is new to this series. Ep. 10 was a
   training set produced by past decisions; Ep. 11 an objective that omitted
   the failure. Here the model, the data and the objective can all be fine
   and the number still be wrong, because of how the test set was built. It
   is the earliest possible failure — before deployment is even a question.
2. **The centrepiece is an experiment, not an anecdote**, and it asserts its
   own result over repeated runs.
3. **The control beat is what makes it an experiment.** B10 removes the
   suspected cause and shows the effect vanish. Without it the episode would
   only be a correlation.
4. **The fix is given as much room as the problem**, and it is free — one
   line of the split changed. The episode ends on something a student can do
   today, not on a warning.
5. **Published and computed-here are separated**, and so are *diagnosis* and
   *measurement*, because the literature supplies the first and this reel
   only the second.
6. **No real solar imagery, no reproduced figures, no redrawn plots.** Every
   plate is generated here; the Starlink beat is an isotype count of 49
   squares, never a satellite picture.
7. **No claim that any named team made this mistake.** The mechanism is
   demonstrated in simulation and the literature is cited for the diagnosis
   and the fix, both of which those authors state themselves.
