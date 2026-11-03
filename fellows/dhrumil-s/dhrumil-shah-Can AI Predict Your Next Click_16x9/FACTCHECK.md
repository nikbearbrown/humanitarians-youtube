# FACTCHECK — Can AI Predict Your Next Click?

Date checked: **2026-09-12** · Checker: Claude (automated research) · Human sign-off: **pending**

Claim classes:
- **G** — GENERAL ML CLAIM (true of machine learning in general)
- **S** — SALESFORCE-SPECIFIC CLAIM (product documentation)
- **P** — PRIVACY / PLATFORM CLAIM (Apple)
- **D** — SYNTHETIC DEMONSTRATION (true of this project's generated data and models only)

Verdicts: SUPPORTED · QUALIFY · UNSUPPORTED · OUTDATED · VERIFY (needs human confirmation)

**Intro edition (2026-09-14).** B00 — *"Hi, I am Dhrumil Shah, and this video is about how AI
estimates which customers will click, buy, or leave, and why those scores are probabilities,
not certainties."* — makes no new factual claim. Its summary restates G01 (probabilities, not
certainties), already SUPPORTED. The presenter's name is the user's own identity. All other
claims and verdicts below are unchanged from the source film.

---

## General ML claims

| ID | Beat | Narration wording | Factual claim | Source | Evidence | Qualification | Verdict · approved wording |
|---|---|---|---|---|---|---|---|
| G01 | B02, B16 | "It estimates probabilities from past behavior." · "Prediction is not certainty." | A classifier outputs estimated conditional probabilities learned from historical examples. | Niculescu-Mizil & Caruana 2005 (ICML) | Paper evaluates predicted probabilities of supervised learners and their calibration. | Probabilities can be poorly calibrated; this is checked separately (G04). | SUPPORTED · as narrated |
| G02 | B04 | "Events become features, counted only before the prediction date." | Features must use only information available at prediction time, or leakage occurs. | Kaufman et al. 2012, ACM TKDD 6(4) | Defines leakage as target information not legitimately available; recommends learn–predict separation. | — | SUPPORTED · as narrated |
| G03 | B06 | "Earlier months train the model. A later month it never saw tests it, so the future can't leak in." | Time-based splits evaluate on later data and prevent temporal leakage. | Kaufman et al. 2012 | Learn–predict time separation. | A time split prevents *temporal* leakage; it does not guard against every leakage type. Other checks in `evaluation/leakage_checks.json`. | SUPPORTED · as narrated |
| G04 | B12 | "customers scored near fifty-five percent bought at fifty-six percent. That's calibration." | Calibration = predicted probabilities match observed frequencies in groups. | Niculescu-Mizil & Caruana 2005; scikit-learn calibration guide | Reliability diagrams compare mean predicted vs observed rate per bin. | Shown for one group (top decile) of one model; other bins in `evaluation/calibration_curve.png`. | SUPPORTED · as narrated |
| G05 | B13 | "prediction isn't causation … Only a holdout test shows whether the campaign caused anything." | Incremental campaign effect requires a treatment vs control comparison. | Gutierrez & Gérardy 2017, PMLR 67 | Uplift modelling framed as causal inference under the Rubin model. | "Only a holdout test" is slightly strong: well-designed quasi-experiments can also estimate effects. For marketing campaigns a randomised holdout is the standard. | QUALIFY · acceptable for a general audience; README notes quasi-experimental alternatives |
| G06 | B15 (on screen), evaluation docs | "association, not causation" (feature importance) | Permutation importance reflects model reliance, not intrinsic or causal effect. | scikit-learn User Guide §5.2 | "does not reflect the intrinsic predictive value of a feature by itself but how important this feature is for a particular model." | — | SUPPORTED |
| G07 | B10, B11 | "Those are business choices, not laws of nature." | Decision thresholds depend on costs, capacity, objectives; no universal cutoff. | Standard decision theory; scikit-learn *Tuning the decision threshold* guide | Threshold tuning to a cost/utility is documented practice. | — | SUPPORTED |
| G08 | B05 | "Churn, in this demo, means thirty days with no click, visit, or purchase. Real businesses define it differently." | Churn definitions vary (contractual vs non-contractual settings). | research.md §5 | Common distinction in customer-base analysis literature. | — | SUPPORTED |

## Salesforce-specific claims

| ID | Beat | Narration wording | Factual claim | Source | Evidence | Qualification | Verdict · approved wording |
|---|---|---|---|---|---|---|---|
| S01 | B14 | "Salesforce documents Einstein Engagement Scoring predicting opens, clicks, subscriber retention, and web conversion." | Official documentation lists these predicted outcomes. | Salesforce Help: *Einstein Engagement Scoring for Email Model Card*; Trailhead *Einstein Engagement Scoring in Marketing Cloud* | Model card: five engagement scores — opens, clicks, retention, web conversion, overall engagement. Trailhead: likelihood to open, click, stay subscribed, convert in the next 7 days. | Pages are JS-rendered; text was obtained via automated fetch. Documentation can change. | **VERIFY** — SUPPORTED by fetched text; human must open the model card and confirm before publishing |
| S02 | research / README only | 90-day lookback; weekly refresh; ≥1 send required; no demographic or third-party data | As stated | Model card | Fetched model-card text. | Not narrated. | VERIFY (not on screen) |
| S03 | research only | Personas Loyalist / Window Shopper / Selective Subscriber / Dormant-Winback | As stated | Trailhead module | Unit lists the four personas. | Not narrated. | VERIFY (not on screen) |

## Privacy / platform claims

| ID | Beat | Narration wording | Factual claim | Source | Evidence | Qualification | Verdict · approved wording |
|---|---|---|---|---|---|---|---|
| P01 | B14 | "But opens are noisy: Apple Mail can download email images in the background." | With Mail Privacy Protection, Apple Mail downloads remote content in the background regardless of engagement, so pixel opens can fire without a human open. | Apple — *Mail Privacy Protection & Privacy* (apple.com/legal); Apple Support Mail guide | "downloads remote content in the background by default — regardless of whether you engage with the email." | Earlier draft said "load emails automatically" — **rewritten** to "download email images in the background" (images/pixels are remote content). Applies when the user enables the feature. | SUPPORTED (after rewrite) · as narrated |

## Synthetic demonstration claims

All from generated files; reproducible with seed `20260912`.

| ID | Beat | Narration / on-screen | Value | File | Verdict |
|---|---|---|---|---|---|
| D01 | B01, B03, B06 | "Five thousand coffee-shop customers" · 1,217,852 events · 15,000 training rows | 5,000 · 1,217,852 · 15,000/5,000/5,000 | `data/generation_manifest.json`, `data/customer_features.csv` | SUPPORTED — labelled synthetic on screen |
| D02 | B04, B07 | 22 visits (30d), 6 email clicks (30d), 10 purchases (90d), active 1 day ago | C02661 on 2026-07-04 | `data/demo_customers.json` | SUPPORTED |
| D03 | B09 | "silent for seventy-four days. Click: two percent. Churn risk: seventy-three." | p_click 0.017 (1.7% → "two"), p_churn 0.7256 | `data/demo_customers.json` | SUPPORTED (rounded) |
| D04 | B01 | "eighty-nine, seventy, sixty-eight percent" | C02661 click 0.8891 · C01211 buy 0.6998 · C04293 churn 0.6783 | `data/demo_customers.json` | SUPPORTED — real model outputs; customers chosen by criteria in `05_score_customers.py` |
| D05 | B12 | "scored near fifty-five percent bought at fifty-six percent" · ROC-AUC 0.89 · PR-AUC 0.58 · base rate 0.12 | top bin 0.553 → 0.560; 0.8887; 0.5759; 0.1158 | `evaluation/calibration_bins.csv`, `evaluation/metrics.csv` | SUPPORTED |
| D06 | B10 | HIGH 966 · MEDIUM 2,535 · AT RISK 876 · LAPSED 623 | as stated | `data/demo_customers.json` | SUPPORTED — thresholds labelled business choices |
| D07 | B08 | "Click: eighty-nine percent. Buy: sixty-one. Churn risk: under one percent. That week, Customer A clicked, but didn't buy." | 0.8891 · 0.6116 · 0.0019; outcomes 1 / 0 / not churned | `data/demo_customers.json` | SUPPORTED |
| D08 | B14 | pre-fetch clients 8.4 opens vs 3.4; clicks 1.9 vs 1.8 (30d, test date) | 8.44 / 3.37; 1.85 / 1.78 | `evaluation/subgroup_check.csv` | SUPPORTED — labelled SYNTHETIC DEMO; not a real-world inflation estimate |
| D09 | B13 | Holdout diagram | no data | — | ILLUSTRATIVE plate on screen; no uplift experiment was run |

## Claims deliberately NOT made

- No real-world open-rate inflation percentage (blog figures unverified).
- No claim that logistic regression is generally better than boosting — only that it won on *this* validation set.
- No claim about Salesforce model accuracy, algorithms, or fairness beyond documentation.
- No claim that any campaign caused any purchase.

## Open items before publishing

1. **S01** — human opens the Salesforce model card and Trailhead unit and confirms the four outcomes are still listed.
2. **G05** — reviewer decides whether "Only a holdout test" should soften to "A holdout test"; changing it requires regenerating B13 audio.
