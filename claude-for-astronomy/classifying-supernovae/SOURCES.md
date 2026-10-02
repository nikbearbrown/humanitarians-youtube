# SOURCES — *What We Chased Before.*

Ep. 10 · AI in Astronomy & Space Science

## Primary literature

| Short cite | Full source |
|---|---|
| Fink real-time active learning (2025) | *Real-Time Active Learning for optimised spectroscopic follow-up: Enhancing early SN Ia classification with the Fink broker* — [arXiv:2502.19555](https://arxiv.org/html/2502.19555). **The episode's deployed example.** Source of: the uncertainty rule (the 10 alerts closest to P_Ia = 0.5), nightly Random Forest retraining, the 78 s median filtering delay, ~200,000 alerts processed in under a minute, follow-up at the ANU 2.3 m with WiFeS over Sept 2023 – Aug 2024, **92 spectra reaching the performance of 127 public ones (25% fewer)**, a median candidate magnitude of 19.5 ± 0.7, the discovery of **microlensing events and flaring stars "usually not incorporated on training sets"**, and Rubin/LSST's **up to 10 million events per night**. |
| Ishida et al. (2019) | *Optimizing spectroscopic follow-up strategies for supernova photometric classification with active learning*, MNRAS **483**, 2 — [Oxford Academic](https://academic.oup.com/mnras/article/483/1/2/5162860). **The episode's diagnosis.** Source of the non-representativeness statement: "the predomination of brighter objects" and "the predominance of SNe Ia over other SN types", attributed to "a follow-up strategy designed to maximize the number of spectroscopically confirmed SNe Ia"; and of the framing that "training algorithms rely on training being representative of the target". Its headline results (2.3× purity, 12% of training objects, 2.6× figure of merit, SNPCC's 20,216 SNe) were verified and deliberately unused — see `FACTCHECK.md`. |
| Kulkarni (2020) | Demographics of astronomical transients and TNS classification statistics for 2019: **only ~10% of transients are classified spectroscopically**. |
| ZTF Bright Transient Survey | *The Zwicky Transient Facility Bright Transient Survey I* — [arXiv:1910.12973](https://arxiv.org/pdf/1910.12973), and the [BTS pages](https://sites.astro.caltech.edu/ztf/bts/bts.php). ~95% spectroscopic completeness for peaks brighter than 18.5 mag. |
| Historical magnitude-dependent completeness | ~80% of SN candidates brighter than V = 17 spectroscopically confirmed; only **10–20% for 20 < V < 22**. |
| ALeRCE (2021) | *The Automatic Learning for the Rapid Classification of Events (ALeRCE) Alert Broker*, AJ **161**, 242, and *The Real-time Stamp Classifier* — [arXiv:2008.03309](https://arxiv.org/pdf/2008.03309). Corroborating only; ~94% accuracy on a balanced test set, and 1,273 of 4,495 TNS-confirmed SNe first reported by ALeRCE in 2021–22. Not on screen. |
| Bazin et al. (2009) | The analytic transient light-curve shape used to compute `deadline.png`. |

## Reel provenance

| Item | Value |
|---|---|
| Brief | `weekly_stem_videos/ideas.md` → Astronomy, topic **10** ("Classifying supernovae in real time") |
| Series | AI in Astronomy & Space Science, **Ep. 10** |
| Fact-check date | 2026-09-25, from primary sources, during this build |
| Toolkit | `brutalist.art` · skill `ai-explainer` · channel `claude-hai` |
| Slug | `classifying-supernovae` — matches the folder |
| Deliverables | 16:9 at 3840×2160 **and** 9:16 at 2160×3840, both full length, same beats |

## Generated imagery — provenance and seed

Every plate is **computed**. `assets/gen_triage.py`, seed **1017**, numpy +
Pillow only (no sklearn).

The experiment: three classes (65 / 30 / 5%), overlapping 2-D features, a
magnitude per object, a brightness-biased seed set of 30 labels, then 12
seasons × 20 spectra, repeated **60 times**, under three strategies —
canonical (brightest), greedy (most confident) and uncertainty (smallest
margin between the top two classes). The classifier is a hand-written Gaussian
naive Bayes, chosen because **a class with no labelled examples cannot be
predicted at all**, which puts the feedback mechanism in plain view.

| Asset | What it is |
|---|---|
| `selection.png` | published confirmation fraction by peak magnitude — a ledger |
| `deadline.png` | three computed Bazin light curves with the useful window marked |
| `loop.png` | accuracy and rare-class recall against season, all three strategies |
| `composition.png` | what the labelled set is made of, season by season |
| `boundary.png` | where doubt lives in season 1, and where it has moved by season 8 |
| `budget.png` | exploration fraction against P(rare class ever found) and Ia count |

### The self-check

The script asserts, and writes nothing if any fails: greedy accuracy **rises**;
greedy's median rare-class recall stays **below 0.02** *and* at least half the
runs end at zero; uncertainty sampling ends at **≥ 0.40** with at most 5% of
runs at zero. It refused three times before passing, each time for a real
error — see `FACTCHECK.md` and `PROMPTS.md`.

**Headline results.** Greedy: accuracy 0.883 → 0.897, median rare recall
0.000 → **0.000**, with **48 of 60** runs never recognising the class once.
Canonical: median 0.000, 53 of 60 at zero. Uncertainty: median **0.638**,
accuracy **0.920**, **0 of 60** at zero. Rare fraction of the labelled set at
season 12: **0.19%** against **16.8%**. And the trade-off: **35% → 92%** chance
of ever finding the class for a 10% exploration quota, costing 18% of the
confirmed-Ia count.

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is a feedback loop through human decisions and a scarce
   resource.** Distinct from Ep. 07's circularity, which ran through
   simulations rather than through people.
2. **The centrepiece is an experiment that asserts its own result**, and the
   claim was rewritten when the experiment disagreed with it.
3. **Medians, not means.** The outcome is bimodal and the mean describes
   neither mode.
4. **The fix gets as much room as the problem**, and the episode ends on a
   number rather than a warning.
5. **No claim that any real survey team has made this mistake.** The loop is
   shown in simulation; the literature is cited for the diagnosis and the fix,
   both of which those authors state themselves.

## Not used

No archival or licensed imagery. No AI-generated stills. No stock. No screen
recordings. **No real survey image, alert stamp or published figure appears
anywhere in this reel**, and nothing is reproduced or redrawn.
