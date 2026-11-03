# Data dictionary — BrewBox synthetic customer analytics

**Every row in this project is synthetic.** BrewBox is a fictional online coffee shop.
There are no names, email addresses, phone numbers, postal addresses, device IDs, or
protected demographic attributes anywhere in the data. Identifiers are sequential
synthetic codes (`C00001` … `C05000`).

| Setting | Value |
|---|---|
| Generator | `src/01_generate_data.py` |
| Random seed | `20260912` |
| Customers | 5,000 |
| Simulated history | 240 days, starting `2026-01-05` (day 0) |
| Event rows | 1,217,852 |
| Feature rows | 25,000 (5 prediction dates × 5,000 customers, minus customers with < 14 days tenure) |

---

## 1. `data/customer_events.csv` — raw event log

One row per behavioural event. This is the **only** file `02_prepare_features.py` reads.

| Field | Type | Definition | Generation logic |
|---|---|---|---|
| `customer_id` | string | Synthetic customer code, `C00001`–`C05000` | Sequential |
| `timestamp` | string `YYYY-MM-DD HH:MM` | When the event happened (synthetic calendar) | Day from the simulation; intraday time synthetic but causally ordered (send 09:00 → open → click → visit → view → cart → purchase) |
| `event_type` | category | One of the nine types below | Latent-engagement simulation |
| `session_minutes` | float, nullable | Minutes on site; only on `web_visit` rows | Gamma-distributed, longer for more engaged customers |

### Event types

| `event_type` | Count | Meaning | Simulation rule (simplified) |
|---|---:|---|---|
| `email_sent` | 280,294 | BrewBox newsletter delivered | Tuesdays and Fridays to every subscribed customer who has signed up |
| `email_open` | 184,865 | An open was *recorded* | Human open **or** a privacy pre-fetch (see note) |
| `email_click` | 56,799 | Link in the newsletter clicked | Only after a human open; probability rises with engagement |
| `web_visit` | 199,960 | Site session | Poisson rate rising with engagement; boosted on click days |
| `search` | 70,171 | On-site search | ~35% of visits |
| `product_view` | 340,455 | Product page viewed | ~1.7 per visit |
| `add_to_cart` | 56,355 | Item added to cart | Per-visit probability rising with engagement |
| `purchase` | 28,201 | Order placed | ~50% of cart adds |
| `unsubscribe` | 752 | Left the newsletter | Rare; more likely for disengaged customers |

> **Open-tracking note.** Half of the synthetic customers use a mail client that
> pre-fetches remote content, modelled on Apple Mail Privacy Protection. For them,
> ~90% of sends record an "open" whether or not a person read the email. Opens
> are therefore excluded from the model inputs and from "meaningful activity".

## 2. `data/customers.csv`

| Field | Type | Definition |
|---|---|---|
| `customer_id` | string | Synthetic code |
| `signup_date` | date | First day the customer can generate events (days 0–60) |

## 3. `data/simulation_truth.csv` — audit only

Latent simulation state (`latent_base_affinity`, `latent_engagement_final`,
`dormant_at_end`, `dormant_days`, `apple_mail_prefetch_client`, `unsubscribed_at_end`).
**Never read by scripts 02–05.** Used only by `04_evaluate_models.py` for the subgroup
audit, which a real business could not run because it would not observe this state.

---

## 4. `data/customer_features.csv` — point-in-time features and targets

One row per (customer, prediction date). For prediction date *s*, feature code
receives only event matrices sliced to days `[0, s)`; target code receives only
`[s, s + 30)`. This slicing is enforced with an `assert` in `02_prepare_features.py`.

### Keys and bookkeeping

| Field | Type | Status | Definition |
|---|---|---|---|
| `customer_id` | string | key | Synthetic code — **not** a model input |
| `snapshot_day` | int | key | Prediction date as a day index (75, 90, 105, 135, 180) |
| `prediction_date` | date | key | Calendar date of the prediction |
| `split` | category | bookkeeping | `train` (days 75, 90, 105) · `validate` (135) · `test` (180) |

### Features (model inputs)

| Field | Type | Window | Definition |
|---|---|---|---|
| `emails_sent_30d` | int | `[s−30, s)` | Newsletters delivered |
| `email_clicks_30d` | int | `[s−30, s)` | Newsletter clicks |
| `click_rate_30d` | float | `[s−30, s)` | `email_clicks_30d / max(emails_sent_30d, 1)` |
| `web_visits_30d` | int | `[s−30, s)` | Site sessions |
| `product_views_30d` | int | `[s−30, s)` | Product page views |
| `searches_30d` | int | `[s−30, s)` | On-site searches |
| `cart_adds_30d` | int | `[s−30, s)` | Add-to-cart events |
| `purchases_90d` | int | `[s−90, s)` | Orders |
| `past_purchase_count` | int | `[0, s)` | Lifetime orders before the prediction date (the brief's `past_conversion_count`) |
| `days_since_last_activity` | int | `[0, s)` | Days since the last click, visit, or purchase; days since signup if none |
| `avg_session_minutes_30d` | float | `[s−30, s)` | Mean session minutes; 0 if no visits |
| `engagement_trend_14d` | int | `[s−28, s)` | (clicks + visits in last 14 days) − (clicks + visits in the 14 days before) |
| `tenure_days` | int | `[0, s)` | `s − signup day` |
| `is_unsubscribed` | 0/1 | `[0, s)` | Unsubscribed before the prediction date |

### Diagnostic column — excluded from every model

| Field | Type | Window | Why excluded |
|---|---|---|---|
| `email_opens_30d` | int | `[s−30, s)` | Contaminated by privacy pre-fetch opens; kept only to demonstrate the problem |

### Eligibility flags (who each model scores)

| Field | Definition |
|---|---|
| `eligible_click` | Tenure ≥ 14 days **and** still subscribed (unsubscribed customers receive no emails, so "click" is undefined) |
| `eligible_convert` | Tenure ≥ 14 days |
| `eligible_churn` | Tenure ≥ 14 days **and** activity in the prior 90 days (you cannot "churn" if you already left) |

### Targets — future outcomes, never model inputs

| Field | Type | Window | Definition |
|---|---|---|---|
| `click_next_7d` | 0/1 | `[s, s+7)` | At least one newsletter click |
| `convert_next_7d` | 0/1 | `[s, s+7)` | At least one purchase |
| `churn_next_30d` | 0/1 | `[s, s+30)` | **No** click, visit, or purchase for 30 days. *Demonstration definition — real businesses define churn differently (contract cancellation, subscription lapse, no order in N days, etc.).* |

A guard in `02_prepare_features.py` asserts that no target column and no diagnostic
column appears in `MODEL_FEATURES`.

---

## 5. `data/scored_customers.csv` — test-date scores

All customers on the test prediction date (`2026-07-04`).

| Field | Type | Definition |
|---|---|---|
| features | — | As above |
| `p_click_7d` | float, nullable | Click model probability; empty if not `eligible_click` |
| `p_convert_7d` | float | Purchase model probability |
| `p_churn_30d` | float, nullable | Churn model probability; empty if not `eligible_churn` |
| `segment` | category | `HIGH ENGAGEMENT` (click ≥ 0.60 or buy ≥ 0.30) · `AT RISK` (churn ≥ 0.50) · `MEDIUM ENGAGEMENT` · `LAPSED` (outside the churn population). **Thresholds are business choices for this demo.** |
| `suggested_test_action` | string | A test to consider — not an automatic treatment |
| `outcome_click_next_7d` · `outcome_convert_next_7d` · `outcome_churn_next_30d` | 0/1 | What actually happened after each window closed — used only for the MEASURE step |

## 6. `data/demo_customers.json`

Customers featured on screen, picked by documented criteria in `05_score_customers.py`
(not hand-picked for a desired number): Customer A `C02661`, Customer B `C03887`,
hook customers `C01211` (buy) and `C04293` (leave).
