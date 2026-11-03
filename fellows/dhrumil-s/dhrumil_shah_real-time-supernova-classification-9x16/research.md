# research.md — Real-Time Supernova Classification

*"Seven Million Alerts a Night"* · vertical 9:16 explainer · AI in Astronomy & Space Science ·
presented by Dhrumil Shah

Research performed against primary and official sources before the narration was locked. Every
number that reaches the script is carried into `FACTCHECK.md` with its source, its exact wording
on screen, and its qualification. Nothing in this brief is used uncited.

The film opens with a presenter introduction (B00: "Hi, I am Dhrumil Shah, and this video is
about…"). That beat summarises the film and makes no factual claim, so nothing in this brief
attaches to it.

---

## 1. The central question

> If an observatory reports millions of changes in the sky every night, how do astronomers find
> the one exploding star that actually matters?

The answer the film delivers, in one sentence: **machine learning does not identify supernovae —
it ranks candidates so that a scarce confirming measurement can be spent well.**

That distinction (detection → classification → confirmation) is the spine. It is also the most
common misconception in popular coverage of this topic, which routinely writes "AI discovered a
supernova" when what happened is "a broker ranked an alert highly and a spectrograph confirmed it."

---

## 2. The pipeline, as it actually runs

The educational framework used throughout the film, in the order the machinery performs it:

```
SCAN → SUBTRACT → ALERT → CLASSIFY → RANK → FOLLOW-UP
```

| Stage | What actually happens | Who does it |
|---|---|---|
| SCAN | Wide-field repeat imaging of the sky on a cadence | Rubin Observatory / LSST |
| SUBTRACT | Difference Image Analysis (DIA) against a deep template | Rubin Prompt Processing (Alert Production) |
| ALERT | Packet built per detected DIASource, distributed | Rubin Data Management System |
| CLASSIFY | Stamp and/or light-curve ML models annotate the alert | Community brokers |
| RANK | Filtering, scoring, prioritisation for follow-up | Brokers + science teams |
| FOLLOW-UP | Imaging and, decisively, spectroscopy | Other facilities entirely |

**No single institution owns the whole chain.** Rubin produces alerts and hands them off; brokers
are independent community software; confirmation happens on other telescopes. The film says this
explicitly, because "the AI pipeline" framing implies a single integrated machine that does not
exist.

---

## 3. Volume — the numbers, and which one to lead with

Three different numbers circulate, and they measure different things:

| Figure | What it actually is | Source |
|---|---|---|
| **800,000** | Measured — alerts issued on the first public-alert night, 2026-02-24 | Rubin news release, 2026-02-25 |
| **~7 million / night** | Rubin's announced expectation at full survey operations | Rubin Observatory (`how-rubin-works/alerts`, `news/first-alerts`) |
| **10⁷ (10 million) / night** | The *requirement* the Data Management System is built to sustain — a design ceiling, not a prediction of the sky | DMTN-102 §2.2 |

**Decision: lead with ~7 million, state it as the full-operations expectation, and never present it
as a present-tense measurement.**

1. It is Rubin's own public figure, in Rubin's own words ("about seven million alerts are generated
   every single night").
2. It is the operational number, not the engineering ceiling. Ep. 01 of the `claude-for-astronomy`
   collection (`ai-vs-the-data-deluge`) resolved the same 7M-vs-10M question the same way.
3. It is the harder figure to nitpick. The design ceiling invites "that's only the requirement";
   the requirement invites "it isn't doing that yet."

**Derived arithmetic used on screen:** 7,000,000 alerts ÷ 86,400 seconds = **81.0 days** of
continuous work at one alert per second. The film's own arithmetic, labelled as a derivation.

---

## 4. How an alert is actually made

From DMTN-102 §1 and the Rubin alert-stream pages:

- Difference Image Analysis is performed on every new visit against a template built from previous
  observations of the same field.
- **Every source with signal-to-noise ratio > 5, in positive *or* negative flux, is considered
  "detected."** Negative matters: something that got *fainter* also trips the threshold — the
  cleanest proof that "detection" is a statistical trigger, not recognition of anything.
- One alert packet is instantiated per detected source.

**Alert packet contents** (DMTN-102 / LSE-163 / Rubin Prompt Products):

- the DIASource record that triggered it — coordinates, photometry, time
- the associated DIAObject / SSObject record, including variability metrics
- all DIASource and DIAForcedSource records from the **previous 12 months**
- **postage stamps** of the difference image and the template at that position

**Latency requirement:** at least 98% of a visit's alerts distributed within **60 seconds** of the
end of image readout (DMTN-102 §2.1). Rubin's public release describes this to a general audience
as a two-minute window; the film uses the 60-second requirement and attributes it to the
requirement document.

**Per-visit volume:** ≥10,000 alerts per standard visit on average; ~1,000 visits per night
(DMTN-102 §2.2). The "thousand pointings a night" line comes from here.

---

## 5. What a residual dot can be

The film must not imply every transient is a supernova. The disposition classes used on screen:

- **supernova** — the thing being hunted
- **variable star** — intrinsically changes brightness, repeats
- **asteroid / solar-system object** — moves, never returns to the same pixel
- **active galactic nucleus** — accreting supermassive black hole, stochastic variability
- **cosmic ray** — a particle striking the sensor, not light at all
- **bogus** — subtraction residual from imperfect alignment or PSF matching

These map directly to ALeRCE's deployed stamp-classifier labels (SN, AGN, variable star, asteroid,
bogus), with cosmic rays falling under bogus in that taxonomy.

---

## 6. Brokers and their models

**Seven full-stream community brokers** are selected for Rubin: **ALeRCE, AMPEL, ANTARES, Babamul,
Fink, Lasair, Pitt-Google** (plus two downstream brokers, SNAPS and POI Broker). Rubin's own
description of their function: *"filtering, cross-match, photometric classification, and
prioritization for follow-up observations."* The alerts are world-public.

The film uses **ALeRCE** as its worked example — the best-documented deployed two-model design in
the peer-reviewed literature (Förster et al. 2021, AJ 161, 242):

**Stamp classifier** — a convolutional neural network reading the *science, reference and
difference* stamps from the **first** detection. Five classes. Reported: **90% accuracy on a
balanced test set** and **81% recall on spectroscopically confirmed supernovae from TNS.**

**Light-curve classifier** — a balanced random forest over features of the multiband flux
evolution, hierarchical (transient / periodic / stochastic, then 15 sub-classes). It requires
**≥6 detections**, so it is strictly later and strictly better-informed.

That split is the film's most teachable mechanism: **the trade between "now" and "sure" is a design
decision, not a limitation.** Brokers run both.

**Caution carried into the script:** brokers do *not* all use the same features or architecture.
The film attributes the two-model design to ALeRCE by name, in narration and on screen.

---

## 7. Why ranking is the entire point — the confirmation bottleneck

- Spectroscopy is what actually determines what a transient *is*: it splits the light into
  wavelengths and shows composition, expansion velocity and redshift.
- Rubin/LSST is expected to discover **close to a million Type Ia supernovae.**
- Spectroscopic capacity is nothing like that: 4MOST's TiDES survey plans spectroscopic follow-up
  for **~30,000 supernovae at all redshifts**, so the vast majority of LSST supernovae will never
  receive a spectroscopic classification.

The honest framing is therefore not "AI finds supernovae." It is: **the confirming measurement is
the scarce resource, and machine learning is how you decide where to spend it.** A classifier that
is 90% accurate is a triage decision about a telescope's night, not a discovery.

---

## 8. Verified, then deliberately NOT used

- **SN 1987A, Tycho, Kepler's supernova** — the film is about a detection system, not about
  supernovae themselves.
- **Kepler-90i / AstroNet** — covered by Ep. 01 of the `claude-for-astronomy` collection.
- **Mechanism detail for brokers other than ALeRCE** — all seven are named once; describing all
  seven would be a directory, not an explanation.
- **The "10 TB per night" raw-data figure** — Ep. 01's number; this film's scale beat is about
  *alerts*, not *bytes*.
- **Real Rubin / ZTF image cutouts** — every visual is synthetic and captioned as such, so nothing
  has to be passed off as an observation. See `ASSETS.md`.

---

## 9. Source list

| # | Source | Used for |
|---|---|---|
| S1 | [DMTN-102, *LSST Alerts: Key Numbers*](https://dmtn-102.lsst.io/DMTN-102.pdf) (Graham, Bellm, Guy, Slater, Dubois-Felsmann, Jurić 2024) | 60 s latency, ≥10,000 alerts/visit, 10⁷/night design figure, SNR > 5, packet contents, ~1,000 visits/night |
| S2 | [Rubin — *Alert Stream*](https://rubinobservatory.org/explore/how-rubin-works/alerts) | "about seven million alerts … every single night"; image comparison; broker role; world-public |
| S3 | [Rubin — *Launches Real-Time Discovery Machine*](https://rubinobservatory.org/news/first-alerts) (2026-02-25) | first alerts 2026-02-24; 800,000 that night; up to 7M at full operations |
| S4 | [Rubin — *Alerts and brokers*](https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers) | seven full-stream brokers; broker functions |
| S5 | [Förster et al. 2021, *The ALeRCE Alert Broker*, AJ 161, 242](https://iopscience.iop.org/article/10.3847/1538-3881/abe9bc) | stamp and light-curve classifiers; accuracy and recall; ≥6 detections |
| S6 | [NOIRLab — *Rubin Celebrates First Public Alerts*](https://noirlab.edu/science/news/announcements/sci26008) | corroborates S3 |
| S7 | [Fully photometric SN Ia cosmology in the LSST era, arXiv:2512.06319](https://arxiv.org/html/2512.06319) | ~1M SNe Ia expected; most without spectroscopic classification |
| S8 | [Magnitude-limited spectroscopic training sample, MNRAS 508, 1](https://academic.oup.com/mnras/article/508/1/1/6352977) | TiDES/4MOST ~30,000 spectroscopic SNe |
| S9 | [Narayan et al. 2018, *ML-based Brokers for Real-time Classification of the LSST Alert Stream*](https://arxiv.org/pdf/1801.07323) | brokers as the mechanism for sifting and prioritising for follow-up |

---

## 10. Terminology the film defines on first use

- **template / reference image** — "a deep template, stacked from everything seen at those coordinates before"
- **difference image** — shown as subtraction: what is left when you remove normal from now
- **alert** — five concrete fields: where, how bright, when, what it looked like before, the pixels
- **broker** — "independent community brokers" catching the public stream
- **light curve** — brightness plotted against time
- **spectrum** — "splits the light into wavelengths and shows what is actually burning"
