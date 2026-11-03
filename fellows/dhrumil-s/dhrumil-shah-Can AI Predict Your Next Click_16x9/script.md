# Script — Can AI Predict Your Next Click?

**How Customer Engagement Scoring Works** · 9:16 vertical · voice: Kokoro `af_kore` (Pragmatist register)

Alternative titles: *Click. Convert. Leave. — How AI Predicts Customer Behavior* ·
*Predictive Customer Analytics — How AI Scores Engagement*

Central question: **Can AI really predict what a customer will do next?**
Answer: **It estimates probabilities from past behavior — prediction is not certainty.**

Measured durations are in `audio/timings.json` and `BUILD-LOG.md`. Every number below
is a real output of this project's models on synthetic data (see `FACTCHECK.md`).

---

| Beat | Section | Narration |
|---|---|---|
| B00 | INTRO | Hi, I am Dhrumil Shah, and this video is about how AI estimates which customers will click, buy, or leave, and why those scores are probabilities, not certainties. |
| B01 | HOOK | Five thousand coffee-shop customers. Will this one click? Will this one buy? Is this one about to leave? A model answers: eighty-nine, seventy, sixty-eight percent. But how does it know? |
| B02 | THE QUESTION | It doesn't know. It estimates probabilities from past behavior. |
| B03 | EVENTS | It starts with events: emails, clicks, visits, product views, carts, purchases, each with a customer ID and a timestamp. |
| B04 | FEATURES | Events become features, counted only before the prediction date. Visits in thirty days. Purchases in ninety. Days since last activity. |
| B05 | TARGET | Then define the target. Click within seven days? Buy within seven? Churn, in this demo, means thirty days with no click, visit, or purchase. Real businesses define it differently. |
| B06 | TRAINING | Training pairs past features with what happened next. Earlier months train the model. A later month it never saw tests it, so the future can't leak in. |
| B07 | CUSTOMER A | Customer A: twenty-two visits this month, ten purchases in ninety days, active yesterday. |
| B08 | PROBABILITY | Click: eighty-nine percent. Buy: sixty-one. Churn risk: under one percent. That week, Customer A clicked, but didn't buy. A probability is not a promise. |
| B09 | CUSTOMER B | Customer B: silent for seventy-four days. Click: two percent. Churn risk: seventy-three. |
| B10 | SEGMENT | Scores rank everyone. The team sets cutoffs for high, medium, and at risk. Those are business choices, not laws of nature. |
| B11 | ACTION | Each segment gets something to test: a new-roast email, an offer, a win-back message, or fewer emails. Consent and human review still apply. |
| B12 | MEASURE | Does it work? On the unseen month, customers scored near fifty-five percent bought at fifty-six percent. That's calibration. |
| B13 | LIMITS | But prediction isn't causation. A high scorer might have bought anyway. Only a holdout test shows whether the campaign caused anything. |
| B14 | LIMITS | Salesforce documents Einstein Engagement Scoring predicting opens, clicks, subscriber retention, and web conversion. But opens are noisy: Apple Mail can download email images in the background. And bad data makes confident, wrong scores. |
| B15 | HUMAN DECISION | Claude isn't the predictor here. It explains scores in plain language, flags leakage, and drafts the next experiment. People decide what's fair. |
| B16 | ENDING | So, can AI predict your next click? It turns past behavior into probabilities that people can test. Events. Features. Model. Probability. Action. Measure. Prediction is not certainty. |

**End card (2.5 s hold, no narration):** Prediction ≠ Certainty ·
EVENTS → FEATURES → MODEL → PROBABILITY → ACTION → MEASURE ·
"BrewBox is fictional. All customers and events are synthetic." · DHRUMIL SHAH · CLAUDE FOR MARKETING

## Revision notes

- v1 draft ran 476 words (~3:10) — cut to 346 words to fit 2:20–2:50 without speeding speech.
- v2: B14 "Apple Mail can load emails automatically" → "Apple Mail can download email images in the background" (accuracy, see FACTCHECK P01).
- No channel introduction at the top: the film opens on the problem.

## Suggested YouTube description

Can AI predict which customer will click, buy, or leave? Not with certainty — it estimates
probabilities from past behavior. This short walks through a real, reproducible ML
pipeline on a fictional coffee shop with 5,000 synthetic customers:
EVENTS → FEATURES → MODEL → PROBABILITY → ACTION → MEASURE.

• Point-in-time features and a chronological train/validate/test split (no leakage)
• Logistic regression vs gradient boosting, chosen on validation log loss
• Test-month ROC-AUC 0.89, calibration checked with a reliability diagram
• Why prediction ≠ causation, and why email opens are a noisy signal
• Where Claude fits: explaining scores, not producing them

All data is synthetic. Salesforce Einstein Engagement Scoring is referenced from its
official documentation as one industry example.

#MachineLearning #MarketingAnalytics #CustomerChurn #Claude #DataScience
