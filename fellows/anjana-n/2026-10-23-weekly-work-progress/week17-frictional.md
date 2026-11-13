# Friction Log: Week 17 (Phase 17)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** October 18 – October 24, 2026

---

## 1. Focus of the week

- **Signal quality and coverage:**
  - decay analysis by type
  - false positive analysis
  - multi-quarter signal chaining
  - earnings call quality gates
- **Linguistic depth:**
  - speech act classification (DeBERTa)
  - discourse structure analysis
  - metaphor tracking
  - sarcasm detection
- **Feature engineering:**
  - automated feature selection
  - interaction discovery
  - embedding drift monitoring
- **Dashboard:** signal chain, quality gate, speech act, and feature importance views.
- **Research:**
  - temporal chaining
  - speech acts and discourse
  - feature selection and embedding stability
- **Outputs:**
  - two  artifacts
  - one Substack article
  - two videos

## 2. What was tried, and what was expected

- **Sarcasm detection:** expected a context-aware detector to catch genuine sarcasm in Q&A without flagging ordinary phrasing.
- **Speech acts:** expected a DeBERTa classifier trained on labelled earnings call sentences to separate assertions, promises, hedged intentions, and deflections.
- **Discourse structure:** expected sentence-level sentiment to reveal where bad news sits in a call.
- **Feature evaluation:** expected that evaluating features independently would show which ones matter.
- **Feature count:** expected more features to mean better predictions.

## 3. Points of resistance, and next steps taken

### Features that matter only in combination (load-bearing)
- **What happened:** dodge score, rising hedging, and defensive language each have a moderate effect on their own. Combined, they predict negative guidance revisions at 2x the base rate.
- **What resisted:** this three-way interaction was invisible while features were evaluated independently.
- **Next step:** the interaction was promoted to the feature vector.
  - A second candidate, metaphor density + declining numerical specificity, was statistically significant but barely beat the individual features.
  - It was placed on monitoring rather than promoted.
- **Lesson:** statistical significance alone doesn't justify promotion when the lift is marginal.

### More features made the model worse
- **What happened:** four low-value features were adding noise:
  - raw transcript length
  - absolute Q&A word count
  - a hedging variant correlated at r = 0.91 with the primary index
  - a superseded keyword density score
- **Next step:** dropped all four. LightGBM AUC improved from 0.72 to 0.74 through noise reduction alone.

### Sarcasm detection: "That's a great question" (unresolved)
- **What happened:** the phrase was flagged as sarcastic 40% of the time. In earnings calls it is almost never sarcasm; it is filler.
- **Next step:** built a financial-idiom exclusion list, but it keeps growing as new edge cases surface.
- **Still open:** where to draw the line between idiom and genuine sarcasm when the same phrase is used both ways.
  - The exclusion list is a stopgap.
  - The underlying problem is that the model lacks social context, such as a CEO flattering an analyst vs. dismissing a question.

### DeBERTa speech act class imbalance
- **What happened:** training data was 60%+ assertions, with under 5% deflections and hedged intentions. The model classified everything as assertion by default.
- **Next step:** class-weighted loss plus synthetic oversampling by paraphrasing. About 45 minutes of retraining.
- **Still to watch:** whether the paraphrased deflections are realistic enough for the model to generalize to real ones.

### Discourse structure window size
- **What happened:** raw sentence-level sentiment was too noisy to detect discourse structure.
- **Next step:** tested three sliding-window sizes:
  - **3 sentences:** too reactive; a single positive sentence flipped the assessment.
  - **7 sentences:** too smooth; buried bad news got averaged away.
  - **5 sentences:** captured paragraph-level shifts without over-smoothing.
- **Still to decide:** 5 is an empirical choice, so it should stay a tunable hyperparameter. Short vs. long and scripted vs. extemporaneous calls may need different windows.

### False positives have causes, not just categories
- **What resisted:** high-confidence wrong predictions clustered into root causes, each with its own mechanism. Three of the clusters:
  - ambiguous language whose meaning shifts with context
  - sarcasm misreads, where surface sentiment contradicts the speaker's intent
  - context-dependent meaning: language that signals "raised" for a growth company signals "maintained" for a mature one
- **Next step:** each cluster is encoded as a confidence modifier, applied to signals that match a known pattern.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifacts)
- **Interactive System Architecture Map:** the full 17-phase ECIS pipeline, with clickable nodes showing data flow, inputs, and outputs.
- **Earnings Call Quality Scorecard:** shows how a transcript is graded before analysis, with pass/fail quality gate thresholds.

### Gru (SDD session)
- Documented this week's architecture changes.

### Eddy
- Reviewed "Quantizing the Readers Nobody Thinks About" before publication.

## 5. Understood now, and still unresolved

### Understood
- **Distinct signals compound:** building separate but complementary NLP signals pays off in combination, even when each is only moderately predictive alone.
- **Pruning helps:** removing noise features can improve a model more than adding new ones.
- **Language form carries intent:** "We will deliver" and "we hope to approach" score the same on sentiment but imply very different follow-through.
- **Rare classes are informative:** deflections are rare because they carry information, so class imbalance has to be handled deliberately.
- **Smoothing is a trade-off:** window size decides whether buried bad news stays visible.

### Unresolved
- **Sarcasm vs. idiom:** where the boundary sits; the exclusion list keeps growing.
- **Discourse window size:** may need to adapt to the call's style.
- **Metaphor + specificity interaction:** held on monitoring.
- **NLP vs. consensus value:** carried from Week 15.
- **Power analysis:** n≈45 is still insufficient. Carried from Week 14.
- **ChromaDB versioning and operational tooling:** carried from Weeks 13–14.
