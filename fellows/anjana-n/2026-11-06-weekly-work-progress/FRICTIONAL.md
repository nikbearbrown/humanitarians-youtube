# Friction Log: Week 19 (Phase 19)

**Project:** Mycroft — ECIS + Decision Scorecard

**Week:** November 1 – November 7, 2026

---

## 1. Focus of the week

- **Uncertainty quantification:**
  - conformal prediction intervals
  - Monte Carlo dropout on the MLP
  - ensemble disagreement
  - selective prediction with abstention
- **Cross-company intelligence:**
  - contagion modeling
  - supply chain language propagation
  - temporal lag modeling
  - leading indicator identification
- **Agentic foundation:** a LangGraph conversational agent with intent parsing, tool routing, query execution, and response synthesis.
- **Dashboard:**
  - interval bands
  - uncertainty indicators
  - contagion network graph
  - lag curves
  - chat interface prototype

## 2. What was tried, and what was expected

- **Granger causality:** expected to reveal which companies' language shifts genuinely lead their peers.
- **Conformal prediction:** expected to give reliable coverage guarantees for every signal type.
- **Entity extraction:** expected to be enough for the intent parser to tell retrieval questions from comparison questions.
- **Uncertainty sources:** Monte Carlo dropout and ensemble disagreement were expected to agree on which predictions are uncertain.

## 3. Points of resistance, and next steps taken

### "Everything causes everything" (load-bearing)
- **What happened:** Granger causality flagged nearly every company pair as causally linked.
- **Cause:** companies in the same sector respond to the same macroeconomic conditions at the same time, so shared exposure looked like one company influencing another.
- **Next step:** signals were residualized against sector averages before testing. Diagnosing the problem took about 40 minutes.
- **Lesson:** a second layer of the same challenge as the Week 12 multiple-comparisons problem. Cross-company analysis is easily fooled because companies in a sector share so many common drivers.

### Coverage guarantees broke down on sparse signal types
- **What happened:** for signal types with fewer than 30 samples, the conformal calibration sets were too small and the coverage guarantees no longer held.
- **Next step:**
  - Switched to cross-conformal prediction, a K-fold variant.
  - It held coverage but ran about 5x slower, so caching was added.
  - About 35 minutes.
- **Lesson:** the third time a statistical method has hit too few samples:
  - Week 13: the KS test on short transcripts
  - Week 18: isotonic regression on small subsets
  - this week: conformal calibration on sparse signal types

  Falling back to a slower but valid method is now a design principle. The root cause, thin data for some signal types, remains.

### Intent parser misrouted comparison questions (open)
- **What happened:** when a question contained two ticker names, the parser assumed a lookup instead of a comparison.
- **Next step:** syntactic pattern detection was layered on top of entity extraction. It still fails on implicit comparisons.
- **Status:** a genuine unsolved problem, acknowledged rather than hidden.

### Choosing coverage and abstention levels
- **What resisted:** wider intervals are statistically safe but less useful.
  - At 95% coverage, a forecast like "between −8% and +12%" is true but tells the user very little.
- **Next step:**
  - 90% coverage was chosen as the balance between being correct and being useful.
  - At that level, the system abstains on about 12% of predictions.
  - Lower would overcommit; higher would refuse too often to be useful.

### When uncertainty measures disagree
- **What resisted:** Monte Carlo dropout and ensemble disagreement sometimes point in different directions.
  - Dropout variance captures uncertainty inside one model.
  - Ensemble disagreement captures uncertainty across different models.
- **Next step:** both are kept as separate indicators. They can diverge when a model is confident but wrong, and that divergence is informative.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifact)
- **Agentic Query Demo:** accepts plain-English questions about ECIS and shows the intent classification, the tool routing decision, and the structured response.

### Gru (SDD session)
- Documented this week's architecture changes.

### Eddy
- Reviewed "Mixture of Experts" before publication.

## 5. Understood now, and still unresolved

### Understood
- **"I don't know" is a feature.** Abstaining on about one prediction in eight is better than outputting numbers the system can't support.
- **Causation in correlated data needs care.** In financial data, apparent causation is often shared exposure. Raw Granger tests overfit unless common drivers are removed first.
- **Coverage and usefulness pull against each other.** The right interval width is a judgment call, not a formula.
- **Every statistical method needs a small-sample fallback.**
- **Turning plain-English questions into the right analysis is a judgment problem.** It can't be solved by keyword matching alone.

### Unresolved
- **Implicit comparisons:** the intent parser is still fragile on questions.
- **Residualization:** whether removing sector averages also removes genuine cross-company signal.

### Resolved this week
Six items carried from earlier weeks:
- **Pre-calibration confidence thresholds** (Week 18): reviewed and updated.
- **CatBoost integration cost** (Week 18).
- **Sarcasm vs. idiom boundary** (Week 17).
- **NLP vs. consensus value** (Week 15).
- **Power analysis, n≈45** (Week 14).
- **ChromaDB versioning and operational tooling** (Weeks 13–14).
