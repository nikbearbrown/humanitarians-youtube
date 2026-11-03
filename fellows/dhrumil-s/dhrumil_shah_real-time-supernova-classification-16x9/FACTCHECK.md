# FACTCHECK — Seven Million Alerts a Night

**16:9 cut.** Every claim, figure, qualification and source below is shared unchanged with the 9:16
cut: the two films speak the same narration and carry the same on-screen wording and source lines.
Only the layout differs, so this verification applies to both.

Verification against primary and official sources, performed before the narration was locked.
Every quantity spoken or shown in the film has a row here. Anything on screen that is *not* in this
table is labelled **ILLUSTRATIVE**, **DERIVED**, or **SYNTHETIC** in the picture itself.

**Verdict key:** ✅ SUPPORTED · ⚠️ QUALIFY (true only with the stated condition) · 🟦 DERIVED (the
film's own arithmetic, shown on screen) · 🟨 ILLUSTRATIVE (invented for teaching, labelled)

---

## B00 — presenter introduction (no claim)

> "Hi, I am Dhrumil Shah, and this video is about how artificial intelligence helps astronomers sort
> millions of nightly sky alerts, to find the exploding stars that are actually worth a telescope's
> time."

This beat names the presenter and summarises the film. It asserts no quantity and no result, and its
on-screen SOURCE line says so ("Presenter introduction — summarises the film; makes no factual
claim"). Two wording checks were still applied, because a summary can overclaim:

- **"millions of nightly sky alerts"** — kept deliberately vague ("millions", not "seven million")
  so the intro does not state the headline figure before B01 can qualify it. Consistent with row 1:
  800,000 on the first public night, ~7 million expected at full operations — "millions" is true of
  the steady-state expectation and makes no present-tense claim.
- **"helps astronomers sort … to find"** — the verb is *sort*, not *discover* or *identify*. The
  intro previews the film's thesis rather than contradicting it.

The on-screen six-stage preview uses plain-language glosses only ("Keep only what changed",
"Sort millions down to a few") — no figures, no sources required.

---

## Claim table

| # | Beat | Claim as used in the script | Wording on screen | Verification | Source | Verdict |
|---|---|---|---|---|---|---|
| 1 | B01 | "At full survey operations, that is about seven million alerts before morning." | `7,000,000` · `CHANGES REPORTED IN ONE NIGHT` · `AT FULL SURVEY OPERATIONS` | Rubin: "about seven million alerts are generated every single night"; first-alerts release: "up to seven million alerts per night" at full operations. Stated as an expectation — Rubin issued **800,000** on its first public-alert night, 2026-02-24. | [S2](https://rubinobservatory.org/explore/how-rubin-works/alerts), [S3](https://rubinobservatory.org/news/first-alerts) | ⚠️ QUALIFY — condition spoken *and* printed |
| 2 | B01 | "one telescope in Chile compares the sky to the way it looked before" | — | "Rubin Observatory automatically compares new images to older images to detect changes in an object's position or brightness, and it generates an alert for each change it observes." | [S2](https://rubinobservatory.org/explore/how-rubin-works/alerts) | ✅ |
| 3 | B02 | "One alert per second … eighty-one days." | `1 / sec` → `81 days` · `DERIVED` · `7,000,000 ÷ 86,400 s = 81.0 days` | 7,000,000 / 86,400 = 81.02 days. Division printed on screen. | Derived from [S2](https://rubinobservatory.org/explore/how-rubin-works/alerts) | 🟦 DERIVED |
| 4 | B03 | "the Legacy Survey of Space and Time … for ten years" | `LEGACY SURVEY OF SPACE AND TIME` · `TEN YEARS` | LSST is a ten-year survey by definition. | [S2](https://rubinobservatory.org/explore/how-rubin-works/alerts) | ✅ |
| 5 | B03, B08 | "a thousand pointings a night" | `~1,000` · `POINTINGS PER NIGHT` | DMTN-102 §2.2 derives the 10⁷/night figure "assuming an average of 1,000 visits per night." Approximate in narration and caption. | [S1 §2.2](https://dmtn-102.lsst.io/DMTN-102.pdf) | ✅ |
| 6 | B04 | "A deep template, stacked from everything seen at those coordinates before." | `TEMPLATE · DEEP REFERENCE STACK` · `ALIGNED · PIXEL FOR PIXEL` | Difference Image Analysis against a template of previous observations of the same field. | [S1 §1](https://dmtn-102.lsst.io/DMTN-102.pdf) | ✅ |
| 7 | B05 | "anything above five sigma counts as a detection, whether it got brighter or fainter" | `≥ 5σ` · `POSITIVE OR NEGATIVE FLUX — BOTH COUNT` | "all sources with a signal-to-noise ratio >5 (in positive or negative flux) will be considered 'detected' … and an alert generated." | [S1 §1](https://dmtn-102.lsst.io/DMTN-102.pdf) | ✅ |
| 8 | B06 | A residual "could be a supernova. A variable star. An asteroid. A feeding black hole. A cosmic ray striking the sensor. Or a flaw in the subtraction itself." | six labelled stamps | Maps to ALeRCE's deployed stamp-classifier label set (SN, AGN, variable star, asteroid, bogus); cosmic ray and subtraction flaw both fall under bogus. | [S5](https://iopscience.iop.org/article/10.3847/1538-3881/abe9bc) | ✅ |
| 9 | B06 | Supernova, variable-star and AGN residuals are indistinguishable from the stamp alone | `LOOK ALIKE` · "Three different causes. One indistinguishable dot." | An argument about the displayed synthetic stamps, which are identical PSF residuals by construction — and the reason a separate light-curve classifier exists. Not presented as a published measurement. | Reasoning from [S5](https://iopscience.iop.org/article/10.3847/1538-3881/abe9bc) | ⚠️ QUALIFY — argument, not citation |
| 10 | B07 | Packet carries "Position, brightness, timestamp, twelve months of previous measurements, and postage stamps of the template and the difference." | five labelled rows | Packet contains "coordinates, photometry, and image cutouts"; DIASource/DIAForcedSource records "from the previous 12 months"; "postage stamps of the difference image and template." | [S1 §1](https://dmtn-102.lsst.io/DMTN-102.pdf) | ✅ |
| 11 | B07 | "Requirement: out the door within sixty seconds." | `60 SECONDS` · `REQUIREMENT` · `≥98% OF A VISIT'S ALERTS, OUT OF THE DATA FACILITY` | "supporting the distribution of at least 98% of alerts for each visit within 60 seconds of the end of image readout." | [S1 §2.1](https://dmtn-102.lsst.io/DMTN-102.pdf) | ✅ — labelled REQUIREMENT, not performance |
| 12 | B08 | "The stream is public, and it is caught by seven independent community brokers." | seven broker names · `Public` | Seven full-stream brokers: ALeRCE, AMPEL, ANTARES, Babamul, Fink, Lasair, Pitt-Google. "Rubin's alerts are world-public." | [S4](https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers), [S2](https://rubinobservatory.org/explore/how-rubin-works/alerts) | ✅ |
| 13 | B09 | "In ALeRCE, one network reads the image stamps on the very first detection." | `MODEL 01 — STAMP CLASSIFIER` · `FIRES ON DETECTION #1` · `CONVOLUTIONAL NEURAL NETWORK` | CNN over science, reference and difference stamps from the first detection; five output classes. | [S5](https://iopscience.iop.org/article/10.3847/1538-3881/abe9bc) | ✅ — attributed by name |
| 14 | B09 | "A second model waits for six, and reads the light curve instead." | `NEEDS ≥ 6 DETECTIONS` · `BALANCED RANDOM FOREST` · `then 15 sub-classes` | Objects with six or more detections go to light-curve classification; balanced random forest; hierarchical taxonomy with 15 classes. | [S5](https://iopscience.iop.org/article/10.3847/1538-3881/abe9bc) | ✅ |
| 15 | B10 | "A supernova climbs over days and fades over weeks. A variable star repeats itself. An asteroid simply never comes back." | `ILLUSTRATIVE CURVE SHAPES — NOT FITTED TO ANY OBSERVED EVENT` | Qualitative basis of the transient / periodic / stochastic split. Drawn curves are analytic shapes, labelled. | [S5](https://iopscience.iop.org/article/10.3847/1538-3881/abe9bc) | 🟨 shapes over a ✅ distinction |
| 16 | B11 | Example output 86% / 7% / 4% / 3% | `ILLUSTRATIVE VALUES` · "Example output shape, not a published prediction for any real object." | Invented, to show a classifier returns a distribution. Flag animates in before the bars. | — | 🟨 ILLUSTRATIVE |
| 17 | B11 | "about ninety percent accurate on a balanced test set" | `~90%` · `Accuracy, balanced test set` | "90% accuracy on a balanced test set." Condition in the spoken line itself. | [S5](https://iopscience.iop.org/article/10.3847/1538-3881/abe9bc) | ✅ |
| 18 | B11 | 81% recall (shown, not spoken) | `81%` · `Recall, TNS-confirmed SNe` | "a recall of 81% among spectroscopically confirmed SNe from TNS." | [S5](https://iopscience.iop.org/article/10.3847/1538-3881/abe9bc) | ✅ |
| 19 | B12 | Brokers rank candidates so a few reach a human | `ILLUSTRATIVE QUEUE — IDS AND SCORES ARE SYNTHETIC` | Broker function: "filtering, cross-match, photometric classification, and prioritization for follow-up observations." Queue, IDs and scores are invented and labelled. | [S4](https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers), [S9](https://arxiv.org/pdf/1801.07323) | ✅ mechanism · 🟨 instance |
| 20 | B13 | "A spectrum splits the light into wavelengths and shows what is actually burning." | `ABSORPTION FEATURES → COMPOSITION · VELOCITY · REDSHIFT` · `ILLUSTRATIVE SPECTRUM` | Spectroscopy is the standard for determining transient type; photometric samples are contaminated without it. Trace is schematic and deliberately not labelled with any ion or object. | [S7](https://arxiv.org/html/2512.06319), [S9](https://arxiv.org/pdf/1801.07323) | ✅ mechanism · 🟨 trace |
| 21 | B14 | "Rubin may find close to a million supernovae." | `~1,000,000` · `SUPERNOVAE EXPECTED` | LSST "is expected to discover nearly a million Type Ia supernovae." The film says "supernovae" — a simplification in the conservative direction (the all-type total is larger, so the ratio is if anything understated). | [S7](https://arxiv.org/html/2512.06319) | ⚠️ QUALIFY — "~", errs conservative |
| 22 | B14 | "The overwhelming majority will never get a spectrum at all." | `~30,000` · `PLANNED SPECTRA (TiDES)` | TiDES plans spectroscopic follow-up for ~30,000 SNe; ~30,000 of ~1,000,000 is 3%, the fraction the dot field lights. | [S8](https://academic.oup.com/mnras/article/508/1/1/6352977), [S7](https://arxiv.org/html/2512.06319) | ✅ |
| 23 | B14–B15 | "A classification is a ranking. It is not a confirmation." | `A ranking is not a confirmation.` | Restatement of rows 20–22; the presenter's conclusion, labelled as such on the closing source line. | — | ✅ — argument from sourced parts |

---

## Numbers considered and deliberately NOT used

| Figure | Why it was dropped |
|---|---|
| **10 million alerts / night** | Real — DMTN-102's design requirement. Dropped as the headline because it describes what the system is rated for, not what it reports. |
| **800,000 (first night)** | The most defensible number in the set, and the reason B01 says "at full survey operations." Not the headline because the film is about the steady-state problem. |
| **~10 TB of raw images per night** | Ep. 01's figure; this film's scale beat is about alerts, not bytes. |
| **≥10,000 alerts per visit** | Verified; the per-visit form of a per-night number already stated, and needs "visit" defined. |
| **1.5 × 10⁸ ZTF alerts processed by ALeRCE; 6,162 SNe reported** | Verified; cut because a deployment-scale statistic invites the "so it works, then" reading the last beats exist to prevent. |
| **Alert packet size / stamp dimensions** | Too granular for a vertical cut. |
| **A named spectral feature (e.g. silicon for Type Ia)** | Labelling one trough on a synthetic spectrum edges toward presenting an invented trace as a real measurement. |

---

## Language rules enforced in the picture

1. **No "discovers."** The model never "discovers", "finds" or "identifies" a supernova. It sorts,
   filters, ranks, scores and prioritises. The intro uses *sort*; the one "find" in B00 ("to find
   the exploding stars … worth a telescope's time") has astronomers as its subject, and the one in
   B14 has the observatory as its subject.
2. **Every percentage carries its condition.** "~90%" never appears without "balanced test set".
3. **Illustrative before, not after.** The B11 flag animates in before the bars.
4. **Every image is captioned synthetic** wherever a viewer could mistake it for an observation.
5. **A SOURCE line is on screen for the whole of every beat**, including the intro, whose line
   states that it makes no claim.

---

## Sources

| ID | Reference |
|---|---|
| S1 | Graham, Bellm, Guy, Slater, Dubois-Felsmann & Jurić (2024), **DMTN-102: LSST Alerts: Key Numbers**. [dmtn-102.lsst.io](https://dmtn-102.lsst.io/DMTN-102.pdf) · [DOI 10.71929/rubin/2997858](https://doi.org/10.71929/rubin/2997858) |
| S2 | NSF–DOE Vera C. Rubin Observatory, **Alert Stream**. [rubinobservatory.org/explore/how-rubin-works/alerts](https://rubinobservatory.org/explore/how-rubin-works/alerts) |
| S3 | Rubin Observatory news release, 2026-02-25, **Launches Real-Time Discovery Machine for Monitoring the Night Sky**. [rubinobservatory.org/news/first-alerts](https://rubinobservatory.org/news/first-alerts) |
| S4 | Rubin Observatory, **Alerts and brokers**. [rubinobservatory.org/for-scientists/data-products/alerts-and-brokers](https://rubinobservatory.org/for-scientists/data-products/alerts-and-brokers) |
| S5 | Förster et al. (2021), **The ALeRCE Alert Broker**, AJ 161, 242. [IOPscience](https://iopscience.iop.org/article/10.3847/1538-3881/abe9bc) |
| S6 | NOIRLab, **NSF–DOE Rubin Observatory Celebrates First Public Alerts**. [noirlab.edu](https://noirlab.edu/science/news/announcements/sci26008) |
| S7 | **A Fully Photometric Approach to Type Ia Supernova Cosmology in the LSST Era**. [arXiv:2512.06319](https://arxiv.org/html/2512.06319) |
| S8 | **Optimizing a magnitude-limited spectroscopic training sample for photometric classification of supernovae**, MNRAS 508, 1. [Oxford Academic](https://academic.oup.com/mnras/article/508/1/1/6352977) |
| S9 | Narayan et al. (2018), **Machine Learning-based Brokers for Real-time Classification of the LSST Alert Stream**. [arXiv:1801.07323](https://arxiv.org/pdf/1801.07323) |

**Spend on verification and production: $0.00.**
