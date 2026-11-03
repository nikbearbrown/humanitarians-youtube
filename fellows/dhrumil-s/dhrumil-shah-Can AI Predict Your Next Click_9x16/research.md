# Research notes — predictive customer analytics

Research date: **2026-09-12**. Primary and official sources were preferred;
marketing blogs were used only to locate primary sources and are not cited for claims.

## 1. The central question

*Can AI really predict what a customer will do next?* In the defensible sense, a
supervised classifier estimates **P(event within a window | features observed before a
prediction date)**. It outputs a probability, not knowledge of an individual's choice.
Two further questions are separate: whether the probability is **calibrated**, and
whether acting on it **causes** a different outcome.

## 2. Industry example — Salesforce Einstein Engagement Scoring

| Finding | Source |
|---|---|
| Einstein Engagement Scoring for email produces five engagement scores per contact: opens, clicks, retention, web conversion, and overall engagement. | Salesforce Help — *Einstein Engagement Scoring for Email Model Card* (`help.salesforce.com/s/articleView?id=sf.mc_anb_EES_email_model_card.htm`) |
| Trailhead describes the predictions as the likelihood to open, click, stay subscribed, and convert (purchase or download) **in the next 7 days**. | Trailhead — *Einstein Engagement Scoring in Marketing Cloud* module, "Explore Engagement Scoring" unit |
| The model uses up to **90 days** of historical engagement. | Model card |
| Scores and models are updated **weekly**; cadence varies by one to several days per business unit. | Model card |
| At least **one email send** is required for a contact to be scored. | Model card |
| The model card states it does **not** include demographic data or third-party data. | Model card |
| Scores are grouped into four personas: Loyalist, Window Shopper, Selective Subscriber, Dormant/Winback. | Trailhead — same module |

**Caveats.** Salesforce Help pages are rendered client-side; content was retrieved through
automated fetches on 2026-09-12. A human reviewer should open the model card directly and
confirm the wording before publishing (flagged in `FACTCHECK.md`). Salesforce is used as
one example; it is not presented as the only implementation.

## 3. Email opens are a noisy signal

| Finding | Source |
|---|---|
| With Mail Privacy Protection / Protect Mail Activity, Apple Mail downloads remote content in the background by default, regardless of whether the user engages with the email. | Apple — *Mail Privacy Protection & Privacy* (`apple.com/legal/privacy/data/en/mail-privacy-protection/`) |
| The feature hides the user's IP address; remote content is routed through two relays. | Same Apple page; Apple Support — *Use Mail Privacy Protection on Mac* |

Implication: a tracking pixel can load without a person opening the email, so "open"
events overstate engagement. The project excludes opens from features and from the
churn definition. Industry blogs report large inflation percentages; none were verified
against primary data, so **no inflation figure is stated in the video**. The on-screen
open/click comparison is from the synthetic simulation and is labelled as such.

## 4. Machine-learning method

| Topic | Key point | Source |
|---|---|---|
| Leakage | Leakage is information about the target that would not legitimately be available at prediction time; avoided by a learn–predict separation in time. | Kaufman, Rosset, Perlich & Stitelman (2012), *Leakage in data mining: Formulation, detection, and avoidance*, ACM TKDD 6(4), doi:10.1145/2382577.2382579 |
| Calibration | Different learners produce differently calibrated probabilities; reliability diagrams and Platt/isotonic calibration are standard checks and fixes. | Niculescu-Mizil & Caruana (2005), *Predicting good probabilities with supervised learning*, ICML, doi:10.1145/1102351.1102430 |
| Feature importance | Permutation importance measures how much a *particular model* relies on a feature, not the feature's intrinsic value or a causal effect. | scikit-learn User Guide, *Permutation feature importance* (§5.2, v1.9) |
| Causal impact | Estimating a campaign's incremental effect is a causal-inference problem (uplift modelling), requiring treatment/control comparison — distinct from response prediction. | Gutierrez & Gérardy (2017), *Causal Inference and Uplift Modelling: A Review of the Literature*, PMLR 67:1–13 |
| Imbalanced evaluation | PR-AUC should be read against the positive base rate; accuracy alone is misleading for rare events. | Standard practice; see scikit-learn *Model evaluation* guide |

## 5. Churn definitions

There is no universal churn definition. Contractual businesses observe cancellation;
non-contractual retailers (like a coffee e-shop) must infer inactivity. This project uses
a stated demonstration definition — no click, visit, or purchase for 30 days — and says
on screen that real businesses define churn differently.

## 6. Credible disagreements and limits

- Engagement scores can reinforce existing patterns (customers never emailed look disengaged).
- Suppressing "low" segments may reduce data on them, weakening future models.
- Fairness: even without protected attributes, proxies can exist; this demo contains no
  demographic data, and the only subgroup audit is by (synthetic) mail client.
- Prediction quality in a simulation is easier than in reality: the synthetic generator
  has a clean latent structure, so real-world metrics will usually be lower.

## 7. Visual evidence suitable for animation

Event logs, point-in-time feature windows, chronological split diagram, probability rings,
reliability diagram, segmentation scatter with threshold lines, holdout comparison schematic.
