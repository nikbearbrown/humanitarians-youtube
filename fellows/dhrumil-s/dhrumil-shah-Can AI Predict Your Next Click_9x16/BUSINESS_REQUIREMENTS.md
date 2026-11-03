# Business requirements — predictive engagement scoring (BrewBox demonstration)

*Prepared in the style of a Business Analyst requirements document. BrewBox is a
fictional online coffee shop; all data is synthetic.*

## 1. Problem

The marketing team sends the same newsletter cadence to every customer. With
5,000 customers and more than a million behavioural events, nobody can manually
judge who is likely to engage, who is likely to buy, and who is drifting away.
Campaigns are therefore either too broad (wasted sends, unsubscribes) or reactive
(win-back effort starts after a customer has already gone quiet).

## 2. Business objective

Prioritise audiences using calibrated, predictive engagement scores, and measure
whether actions taken on those scores change outcomes.

**Success is not "the model is accurate."** Success is: scores are reliable
enough to rank audiences, and at least one score-driven campaign is evaluated
against a holdout group.

## 3. Stakeholders and users

| Role | Needs |
|---|---|
| Marketing analyst | Understand drivers of each score; export audiences |
| Campaign manager | Choose which segment receives which test, and when |
| CRM team | Load scores into the campaign platform on a schedule |
| Business analyst | Requirements, acceptance criteria, traceability |
| Data scientist / ML engineer | Build, evaluate, monitor, retrain the models |
| Privacy / legal reviewer | Confirm consent, data minimisation, permitted use |

## 4. Scope

**In scope:** click (7-day), purchase (7-day) and churn (30-day) probability models;
segmentation; audience export; outcome tracking; plain-language explanations.

**Out of scope:** automatic sending without human approval; individual price
discrimination; use of protected demographic attributes; causal uplift modelling
(recommended as a follow-up — see §9).

## 5. Functional requirements

| ID | Requirement |
|---|---|
| FR-01 | **Ingest events.** Load timestamped behavioural events (email sent/open/click, visit, search, product view, cart add, purchase, unsubscribe) keyed by a pseudonymous customer ID. |
| FR-02 | **Engineer features.** Compute point-in-time features using only events strictly before the prediction date. |
| FR-03 | **Define targets explicitly.** Each model has a written target and window: click ≤ 7 days, purchase ≤ 7 days, churn = no click/visit/purchase for 30 days. |
| FR-04 | **Train and select models** on earlier prediction dates; select on a later validation date; report on an even later test date. |
| FR-05 | **Calculate scores.** Produce a probability between 0 and 1 per customer per model, with the model version and prediction date. |
| FR-06 | **Display probability** with its definition (event + window), not as a bare number. |
| FR-07 | **Classify segments** using thresholds stored as configuration and owned by the campaign manager. |
| FR-08 | **Export audience** as a CSV of customer IDs, segment, scores, and suggested test. |
| FR-09 | **Track outcomes.** After each window closes, record the observed outcome against the score. |
| FR-10 | **Explain.** Provide feature-level drivers (coefficients / permutation importance) and a plain-language summary (Claude), labelled as association, not causation. |
| FR-11 | **Holdout support.** Every score-driven campaign export can reserve a random holdout share. |

## 6. Non-functional requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-01 | Reproducibility | Fixed random seed; one command per pipeline stage; outputs regenerate identically. |
| NFR-02 | Privacy | No direct identifiers in model inputs or exports; pseudonymous IDs; no protected attributes; data minimisation. |
| NFR-03 | Interpretability | A transparent baseline (logistic regression) is always trained; a more complex model is adopted only if it is clearly better on validation. |
| NFR-04 | Performance | Scoring 5,000 customers completes in seconds on a laptop; full pipeline in under two minutes. |
| NFR-05 | Auditability | Model selection, metrics, leakage checks, and thresholds are written to versioned files (`models/model_selection.json`, `evaluation/*`). |
| NFR-06 | Calibration | Probabilities are checked with reliability curves and Brier score before being shown as percentages. |
| NFR-07 | Governance | Actions require human approval; consent and suppression lists are applied before any send. |

## 7. Acceptance criteria

| ID | Given / When / Then | Status in this build |
|---|---|---|
| AC-01 | **Given** a prediction date *s*, **when** features are computed, **then** no event on or after *s* contributes to any feature. | ✅ Enforced by `assert` on history slice |
| AC-02 | **Given** the feature list, **when** the pipeline runs, **then** no target column, customer ID, or email-open count is a model input. | ✅ `evaluation/leakage_checks.json` |
| AC-03 | **Given** training labels, **when** the split is built, **then** every training label window closes on or before the validation date, and every validation window before the test date. | ✅ |
| AC-04 | **Given** the test date, **when** models are evaluated, **then** ROC-AUC, PR-AUC with base rate, Brier score, calibration curve, and precision/recall/F1 at a validation-chosen threshold are reported — not accuracy alone. | ✅ `evaluation/metrics.csv` |
| AC-05 | **Given** models trained on shuffled labels, **when** scored on test data, **then** mean ROC-AUC ≈ 0.5. | ✅ 0.52 ± 0.13 over 20 runs (real model: 0.89) |
| AC-06 | **Given** a score shown as a percentage, **when** customers are grouped by score, **then** observed rates track predicted rates (expected calibration error < 0.03). | ✅ 0.010–0.020 |
| AC-07 | **Given** segment thresholds, **when** they change, **then** only configuration changes — no retraining. | ✅ constants in `05_score_customers.py` |
| AC-08 | **Given** an audience export, **when** it is produced, **then** it contains no names, emails, phones, or addresses. | ✅ synthetic IDs only |
| AC-09 | **Given** a campaign on a segment, **when** results are reported, **then** a holdout comparison is required before claiming impact. | ⏳ Process requirement — no campaign was run |

## 8. Risks

| Risk | Mitigation |
|---|---|
| Opens inflated by privacy pre-fetch | Opens excluded from features and from "activity" |
| Label leakage via overlapping windows | Chronological split with window-closure rule (AC-03) |
| Scores treated as certainty | UI shows event + window; outcome tracking (FR-09) |
| Prediction mistaken for causal impact | Holdout requirement (FR-11, AC-09) |
| Segment treatment feels unfair or manipulative | Human approval; no protected attributes; frequency caps |
| Model drift | Re-evaluate calibration on each new prediction date |

## 9. Recommended next steps

1. Run one holdout-controlled win-back test on the AT RISK segment.
2. Add uplift modelling to target customers whose behaviour *changes* because of a campaign.
3. Monitor calibration monthly; retrain when ECE exceeds 0.05.
