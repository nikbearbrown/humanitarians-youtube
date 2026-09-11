# FACTCHECK — *The Number Went Up.*

Ep. 08 · `asteroid-impact-warning` · checked from primary sources on
**2026-09-11**, during this build. Every figure that reaches the screen or the
narration is in the table below with the source that supports it.

**Two kinds of number appear in this reel and they are never mixed.**
*Published* figures are the real 2024 YR4 record and the real ATLAS/Chyba
Rabeendran results, cited on screen. *Computed here* figures come out of
`assets/gen_neo.py`, which runs the calculation itself, and every beat showing
one captions it as such. B07 and B09 are published. B08 is computed here.

## Claims on screen or in the narration

| # | Claim | Where | Verdict | Source |
|---|---|---|---|---|
| 1 | ATLAS uses 0.5 m f/2.0 Schmidt telescopes | B03 cite | ✅ | Tonry et al. 2018, *ATLAS: A High-cadence All-sky Survey System*, PASP — 0.5 m Schmidt corrector, 0.65 m spherical primary, f/2.0 |
| 2 | Four 30 s exposures per field per night | B03 narration + cite | ✅ | Tonry+ 2018 — four observations per field per night over a ~1 hour interval, 30 s typical |
| 3 | ~26,000 sq deg of sky per night | B03 cite | ✅ | Tonry+ 2018 — ~26,000 deg², ~900 images per night |
| 4 | "Four telescopes" | B03 narration | ✅ | ATLAS operates units at Haleakalā and Mauna Loa (Hawai'i), Sutherland (South Africa) and Río Hurtado (Chile). The project page now describes five; **the narration says four**, which is the funded core and is never stated as a total. See § "Softened on purpose". |
| 5 | ~100,000 candidate alerts a night | B03 chip, B00 output, B11 | ✅ | ATLAS alert-stream documentation: ≈10⁵ alerts/night, the majority classified bogus. Tonry+ 2018 separately gives 10⁵–2×10⁶ *star* detections per image — a different quantity, not used. |
| 6 | Eight postage-stamp classes, sorted by a CNN | B04, B00, B11 | ✅ | Chyba Rabeendran & Denneau 2021, [arXiv:2101.08912](https://arxiv.org/abs/2101.08912) — "classify small 'postage-stamp' images … into eight classes" |
| 7 | A second network scores a sequence of four detections | B05, B11 | ✅ | Same — "a multi-layered perceptron that provides a probability that a temporal sequence of four candidate detections represents a real astronomical source" |
| 8 | **99.6%** accuracy on real asteroids | B05 counter, B00 output | ✅ | Same, verbatim: "the model reaches 99.6% accuracy on real asteroids in ATLAS data" |
| 9 | **0.4%** false negative rate | B05 counter | ✅ | Same, verbatim: "with a 0.4% false negative rate" |
| 10 | Screening load cut by **90%** | B05 counter, B00, B11 | ✅ | Same, verbatim: "has reduced the amount of NEO candidates that astronomers must screen by 90%" |
| 11 | The purpose was reducing delay to the Minor Planet Center | B05 closer ("speed, not cleverness") | ✅ | Same: "The goal of this work is to reduce the time delay between NEO detections and submission to the Minor Planet Center" |
| 12 | A cosmic ray has no point-spread function; a bad subtraction is two lobes | B04 | ✅ | Standard difference-imaging artefact taxonomy; both are among the eight classes in arXiv:2101.08912. Both are **synthesised from their own physical model** in `gen_neo.py`, not asserted. |
| 13 | Impact probability is **not** learned — it is orbit determination | B06, B10, B11 | ✅ | The impact-monitoring systems are Sentry (JPL), Aegis (ESA NEOCC) and NEODyS (SpaceDyS/Pisa); Aegis and NEODyS use Line-of-Variations sampling, Sentry the impact-observation method. No neural network is involved in any of them. |
| 14 | 2024 YR4 discovered by ATLAS, Río Hurtado, Chile, 27 Dec 2024 | B07 cite | ✅ | *The Impact Hazard Assessment for Near-Earth Asteroid 2024 YR4*, [PMC12963224](https://pmc.ncbi.nlm.nih.gov/articles/PMC12963224/) — discovery 27 Dec 2024, o-band 16.5, ATLAS; pre-discovery Catalina data folded into the initial designation |
| 15 | Size **60 ± 7 m** | B07 cite, B07 narration ("a sixty-metre rock") | ✅ | Same — JWST infrared refinement, March 2025. The earlier photometric range was 40–90 m; the narration uses the refined figure. |
| 16 | Probability track 0.6% → 1.8% → 1.1% → **3.1%** → 0.9% → <0.1% | B07 plotted points | ✅ | Same, Sentry column of Table 1: 29 Dec 0.6, 8 Jan 1.8, 22 Jan 1.1, **18 Feb 3.1 (peak)**, 20 Feb <1, 23 Feb <0.1 |
| 17 | Peak was the highest ever recorded for an object of this size | B07 narration | ✅ | Same; and Torino 3 has been reached by no object other than Apophis. |
| 18 | **Torino 3 — only Apophis ever matched it** | B07 chip | ✅ | CNEOS news 210; corroborated by PMC12963224's Torino column |
| 19 | Five days from peak to essentially zero | B07 narration | ✅ | 18 Feb peak → 23 Feb Torino 0 / <0.1% = five days |
| 20 | Would-be impact date 22 Dec 2032, impact speed 17.3 km/s | used to derive `b_cap` | ✅ | PMC12963224 |
| 21 | The rise happened because Earth sat in the **core** of the uncertainty region and later moved to the tail and outside it | B08 | ✅ | Same, paraphrasing its own explanation: "the Earth remained within the core of the uncertainty region", then "moved towards the tail and eventually outside of the uncertainty region". **B08 then derives this from scratch rather than asserting it.** |
| 22 | Lunar impact probability peaked at **4.3%** | B09 counter | ✅ | PMC12963224 gives 4.3% for 22 Dec 2032 at the end of the discovery apparition; EarthSky dates the peak to 3 June 2025 (1-in-23) |
| 23 | Lunar impact **ruled out 5 Mar 2026**, from JWST data of 18 & 26 Feb 2026 | B09 cite | ✅ | NASA statement quoted by EarthSky, 5 Mar 2026: "Using data from NASA's James Webb Space Telescope observations collected on February 18 and 26, 2026 … ruling out a chance of lunar impact on December 22, 2032." Object passes the Moon at ~21,200 km. |
| 24 | **11** impactors ever discovered before impact | B10 counter, B00, B11 | ✅ | *Predictions of Imminent Earth Impactors Discovered by LSST*, [arXiv:2603.05587](https://arxiv.org/html/2603.05587v1) — "As of January 1, 2026, 11 imminent impactors have been discovered before impact", 2008 TC3 first |
| 25 | ~**40%** of the ≥140 m population catalogued, against a **90%** mandate | B10 plate + cite, B00 | ✅ | *The Near-Earth Object Surveyor Mission*, [arXiv:2310.12918](https://arxiv.org/pdf/2310.12918) — "perhaps 40% of all 140-meter and larger objects have been discovered"; the 90% figure is the George E. Brown Jr. survey mandate |
| 26 | >90% of the ≥1 km population found | B10 plate (bar at 0.90) | ✅ | NASA NEO Program — "over 90% of the near-Earth objects larger than one kilometre already discovered". **The bar is drawn at exactly 0.90, not higher**, because 0.90 is what the source supports. |
| 27 | NEO Surveyor closes the gap | B10 cite | ✅ | arXiv:2310.12918 — ~76% of ≥140 m catalogued after the 5-year nominal survey; 90% within 10 years of launch |

## Computed in this reel (`assets/gen_neo.py`, seed 8801)

| Quantity | Value | How |
|---|---|---|
| v∞ for 2024 YR4 | **13.20 km/s** | from the published 17.3 km/s impact speed: v∞² = v_imp² − v_esc². Using the impact speed directly here understates the capture radius by ~12%, and the script comments on that trap. |
| Earth's capture radius on the target plane | **8352 km = 1.311 R_E** | b_cap = R⊕·√(1 + (v_esc/v∞)²) — gravitational focusing |
| Peak of the computed probability curve | **3.86%**, at σ/d = 0.78 | target-plane quadrature over the capture disc |
| Analytic prediction for the peak | **σ → d/√2 = 0.7071 d** | maximise b_cap²σ⁻²·exp(−d²/2σ²) |
| Self-check result | **PASS** — converged to 0.7063, Δ = −0.0008 | the script asserts this and raises `SystemExit` if it fails |
| Tracklet straight-line RMS residual | real **0.040** vs artefacts **1.456** (36×) | least-squares fit through four positions |
| Naive 5σ detections in the difference frame | **4 blobs — 1 real, 3 artefacts** | connected-component count on the real difference image |

**The computed peak (3.86%) is close to the published peak (3.1%) by
construction, not by coincidence, and the reel never implies otherwise.** The
nominal miss distance `d` was set to 8·b_cap to put the curve's maximum in a
plausible few-per-cent range; that is a choice of *illustration scale*, stated
in the script. What is NOT a choice is the curve's SHAPE and the location of
its peak — those follow from the geometry and are checked analytically. B08's
on-screen chip reads "computed in this reel, not redrawn" for exactly this
reason, and its x-axis is the width of the uncertainty region, **not a date**.

## Verified, then deliberately NOT used

| Fact | Why it was dropped |
|---|---|
| A later ATLAS CNN retrain reports a median 0.72% false-positive rate at a 1.00% missed-detection rate (RASTI 3, 385, 2024) | A second, differently-defined pair of rates beside 99.6%/0.4% would blur the one mechanism the beat has time to teach. One worked example, per the DOUBLE-CHECK LAW habit set in Ep. 07. |
| 2024 BX1: discovered <3 h before impact, Scout gave **95 minutes** of warning from three observations over 27 minutes | Genuinely striking, and it was in an earlier draft of B10. Cut because the episode's spine is *why a probability moves*, and a second worked example pulled against it. Kept here because it is the best single illustration of Scout's short-arc job. |
| Most 50 m asteroids are detected 3–9 days before impact; most 140 m, 10–40 days | Same reason — warning-time statistics are a different episode. |
| LSST/Rubin should find ~1–2 imminent impactors >1 m per year, median 1.57 days before impact, and can link ~78% of the metre-size impactors it observes (arXiv:2603.05587) | Forward-looking; the reel ends on the search being unfinished and does not need a roadmap beat. |
| AbacusSummit, Quijote and other simulation suites | Ep. 07's material. |
| Torino scale definition in detail | The chip says what matters: only Apophis ever matched it. |

## Softened on purpose

- **"Four telescopes."** ATLAS's telescope count has grown over time and is
  described variously as two, four and five depending on date and on whether
  partner units are included. The narration says "four telescopes photograph
  the same field four times a night" — a description of the survey's operating
  pattern, not a claim about the current total. No number of telescopes appears
  on screen.
- **"About 100,000 alerts a night."** Stated as "about", because the published
  figure is an order-of-magnitude description of the alert stream (≈10⁵) and
  varies with galactic latitude and conditions.
- **"A sixty-metre rock."** 60 ± 7 m; the uncertainty is on the citation line,
  not in the voice.
- **"Much older arithmetic"** rather than a specific number of years. Orbit
  determination by least squares dates to Gauss in 1801; "two hundred years"
  was in the first draft and was cut as both imprecise and expensive to speak.
- **B08's probability curve is not a redraw of 2024 YR4's history.** Its
  horizontal axis is the width of the uncertainty region and it is labelled
  "the region shrinks →". No date axis, no published curve reproduced.

## DOUBLE-CHECK LAW — editorial decisions

1. **The spine is that a rising number was the system working.** That is the
   transferable lesson and the reason this topic is worth an episode. The
   mechanism beats exist to earn it, not the other way round.
2. **The learned/computed split is the design tell.** Every prior episode in
   this series asked what AI does. This one asks where AI *stops*, which is
   why the colour contract makes the terracotta halt at a boundary in B06.
3. **Published and computed are visibly separated** — in the narration, in the
   citation lines, and in B08's own on-screen chip.
4. **The synthetic sky is captioned as synthetic** on every beat that shows it
   ("the mechanism is real, the stars are not").
5. **No published figure is reproduced, redrawn or traced.** B07 rebuilds the
   *published numbers* as a native animated plot, which is what REBUILD LAW
   requires; the numbers are in row 16 above.
6. **No claim about what would happen if an impact occurred.** No casualty
   figures, no blast comparisons, no "city killer" language in the narration —
   the phrase appears nowhere on screen. The episode is about measurement, and
   sensationalising the hazard would be the easy, dishonest version.
