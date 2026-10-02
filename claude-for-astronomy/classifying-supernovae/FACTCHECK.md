# FACTCHECK — *What We Chased Before.*

Ep. 10 · `classifying-supernovae` · checked from primary sources on
**2026-09-25**, during this build.

**Two kinds of number appear and they are never mixed.** *Published* figures
come from the cited papers and carry a source line. *Computed here* figures
come out of `assets/gen_triage.py`, which runs a closed-loop experiment and
asserts its own central claim. B04 is published and says so on screen; B06,
B07, B08's enrichment figures and B10's trade-off are computed here and say so.

## Claims on screen or in the narration

| # | Claim | Where | Verdict | Source |
|---|---|---|---|---|
| 1 | A transient peaks and fades within about two weeks | B03 | ✅ | Standard transient phenomenology; the plate computes Bazin light curves (Bazin et al. 2009) whose peaks land at +5.7 d, +14.7 d and +0.8 d for the three shapes drawn. "About two weeks" describes the slowest of them. |
| 2 | A spectrum is only useful early | B03 | ✅ | The identifying features are strongest near peak; this is why brokers exist. Phrased as a usefulness window, not a hard cutoff. |
| 3 | Rubin/LSST will report **up to 10 million** changes a night | B03 counter, B00 | ✅ | arXiv:2502.19555 verbatim: "the Legacy Survey of Space and Time (LSST) at the Vera C. Rubin Observatory will detect up to 10 million time-changing events per night, and more than a million SNe during the whole survey." |
| 4 | About **1 in 10** transients ever gets a spectrum | B03 counter, B00, B11 | ✅ | Kulkarni (2020), analysing TNS demographics for 2019: only ~10% of transients were classified spectroscopically. Stated as "about". |
| 5 | Almost every transient brighter than ~mag 18 gets confirmed | B04 bars + narration | ✅ | ZTF Bright Transient Survey reports ~95% spectroscopic completeness for peaks brighter than 18.5 mag; historically ~80% of candidates brighter than V=17. The plate draws 80% and 95% for those two bands. |
| 6 | At 20–22 it is closer to **1 in 7** | B04 bars + narration | ✅ | Historical SN statistics: only 10–20% of SNe discovered with 20 < V < 22 have been spectroscopically confirmed. The plate draws 15%; "one in seven" is 14%. |
| 7 | The spectroscopic sample over-represents bright objects and SNe Ia | B05 cite | ✅ | Ishida et al. 2019, MNRAS **483**, 2 — verbatim: "the predomination of brighter objects" and "the predominance of SNe Ia over other SN types", attributed to "a follow-up strategy designed to maximize the number of spectroscopically confirmed SNe Ia". |
| 8 | Training on it gives a model best at what was already looked at | B05, B11 | ✅ | Same paper: "training algorithms rely on training being representative of the target", named as "a serious problem". The reel states the consequence rather than quoting. |
| 9 | Uncertainty sampling at the decision boundary is a **real deployed rule** | B08, B00 | ✅ | arXiv:2502.19555 — Fink selects "the closest 10 alerts to P_Ia=0.5" nightly from the ZTF public stream, Random Forest retrained nightly. |
| 10 | Fink's median filtering delay is 78 s; a whole night (~200,000 alerts) processes in under a minute | B00 runningText | ✅ | Same. The cold open's "ranking tonight's 200,000 alerts" uses that figure. |
| 11 | **92 spectra, not 127**, for the same performance — **25% fewer** | B09 | ✅ | Same, verbatim: "our follow-up strategy yields a training set that, with 25% less spectra, improves classification metrics when compared to publicly reported spectra." 92 events acquired at the ANU 2.3 m; compared against 127 public TNS spectra. |
| 12 | It turned up **microlensing events and flaring stars** not normally in training sets | B09 | ✅ | Same, verbatim: "not only supernovae types, but also microlensing events and flaring stars which are usually not incorporated on training sets." |
| 13 | Follow-up was at the ANU 2.3 m | B09 cite | ✅ | Same: ANU 2.3 m at Siding Spring, WiFeS spectrograph, Sept 2023 – Aug 2024. |
| 14 | Active learning can more than double purity for the same spectroscopic time | not on screen | ✅ | Ishida+2019: "2.3 times higher purity" after 180 days with 800 queries; 12% of the training objects doubles purity; 2.6× figure of merit. Verified, unused — see below. |

## Computed in this reel (`assets/gen_triage.py`, seed 1017)

The experiment: three classes (65% / 30% / 5%), overlapping 2-D features, a
magnitude per object, a **brightness-biased seed set of 30 labels**, then 12
seasons × 20 spectra, repeated **60 times**. Classifier: a hand-written
Gaussian naive Bayes, chosen because a class with no labels cannot be
predicted at all — so the mechanism is visible in the model.

| Quantity | Value |
|---|---|
| Greedy (most confident): overall accuracy | 0.883 → **0.897** — it rises |
| Greedy: rare-class recall, **median** | 0.000 → **0.000** |
| Greedy: runs ending with **no** rare-class recall | **48 of 60** |
| Canonical (brightest first): rare-class recall, median | **0.000**; 53 of 60 runs at zero |
| Uncertainty sampling: rare-class recall, median | **0.638**; **0 of 60** runs at zero |
| Uncertainty sampling: overall accuracy | **0.920** — higher than greedy too |
| Rare fraction of the labelled set at season 12 | greedy **0.19%** · uncertainty **16.8%** |
| Uncertainty picks, rare fraction vs a 5% base rate | season 1 **17% (3.6×)** → season 8 **39% (8.4×)** |
| Chance a survey ever recognises the rare class | **35%** at 0% exploration → **92%** at 10% → 100% at 20% |
| Cost of 10% exploration | confirmed-Ia count falls to **82%** of its peak (the reel says 18%) |

**The self-check asserts three things and the script writes nothing if any
fails**: greedy accuracy rises; greedy's median rare recall stays below 0.02
*and* at least half the runs end at zero; uncertainty ends at ≥ 0.40 with at
most 5% of runs at zero.

### Three errors this experiment caught, all mine

1. **I claimed rare-class recall "collapses" under greedy. It does not.** It
   starts at zero — a brightness-biased seed set contains no rare objects — and
   never leaves. The loop does not create the blind spot; it inherits it and
   preserves it. That is a different and better claim, and the assertion was
   rewritten to match the experiment rather than the other way round.
2. **I quoted a mean of a bimodal outcome.** A 12-repeat mean read 0.088 where
   the median is 0.000 and 48 of 60 runs end with no recall whatsoever. "Low
   recall" and "usually none at all" are different claims and only the second
   is true. Now 60 repeats, medians throughout.
3. **Two plates measured the same configuration with different statistics**,
   so pure-greedy read 0.281 in one and 0.000 in the other. Plus an off-by-one:
   the loop recorded metrics *before* each season's query, so its last point
   reflected eleven rounds, not twelve.

## Verified, then deliberately NOT used

| Fact | Why |
|---|---|
| Ishida+2019's headline numbers (2.3× purity, 12% of the training objects, 2.6× figure of merit, SNPCC's 20,216 SNe) | The paper is cited for the *diagnosis* (B05), not the result. Adding a second set of performance figures beside Fink's deployed ones would blur which is simulated and which is real. |
| ALeRCE: stamp classifier ~94% accuracy on a balanced test set; 1,273 of 4,495 TNS-confirmed SNe first reported by ALeRCE in 2021–22 (~28%) | A third system with its own metrics. The episode needs one deployed example, and Fink's is the one that ran the active-learning loop. |
| Nine brokers process the ZTF stream; ZTF alone streams >1 million alerts/night | The narration uses Rubin's 10 million as the forward-looking figure and Fink's 200,000/night as the operational one. A third volume figure adds nothing. |
| Fink's chronological metric series (accuracy 0.47 → …, efficiency 0.26, purity 0.87, FoM 0.18) | Four metrics with unfamiliar definitions; the 92-vs-127 comparison carries the same point in one line. |
| SNIascore, SNGuess and other automated classifiers | Not needed; the episode is about the selection loop, not a survey of classifiers. |

## Softened on purpose

- **"About one in ten"** — the published figure is an approximate demographic
  estimate, not a measured rate.
- **"Closer to one in seven"** for the faint band: the source gives 10–20%, the
  plate draws 15%, the voice says one in seven (14%).
- **"Nobody wrote that rule down."** An editorial line about an emergent
  selection function, not a claim that anyone acted improperly.
- **The simulation is never presented as a model of ZTF or Rubin.** B06–B08
  and B10 all carry "computed in this reel" on their citation lines. The class
  fractions, feature space and budget are invented to be *illustrative of the
  mechanism*; only the direction and robustness of the effect are claimed.
- **"A third becomes nine in ten"** is the computed 35% → 92%, stated in the
  voice as a ratio and shown on screen as the figures.

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is a feedback loop through human decisions and a scarce
   resource** — new to this series, and distinct from Ep. 07's circularity
   (which ran through simulations, not through people).
2. **The centrepiece is an experiment, not an anecdote**, and it asserts its
   own result.
3. **The fix is given as much room as the problem.** The episode ends on a
   number a reader can act on — one night in ten — rather than on a warning.
4. **Published and computed-here are separated** on screen and in the voice.
5. **No real survey imagery, no reproduced figures, no redrawn plots.** Every
   plate is generated here.
6. **No claim that any real survey team has made this mistake.** The loop is
   demonstrated in simulation and the published literature is cited for the
   *diagnosis* and the *fix*, both of which those authors state themselves.
