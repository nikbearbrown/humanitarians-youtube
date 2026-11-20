**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 21 — Advanced Forecasting, Topic Intelligence, and Multi-Step Agentic Queries

**Timeline:** November 15, 2026 – November 21, 2026

**Scope:** Phase 21 covers three areas:
- multi-horizon and time-to-event forecasting
- topic and narrative tracking across sectors
- an agent that can answer questions requiring several steps

---

## Advanced Forecasting
- **Temporal Fusion Transformer:** forecasts at 1, 2, 5, and 10 quarters ahead.
  - Uses variable selection and interpretable attention.
  - Trained at a learning rate of 1e-4 with cosine annealing and gradient clipping at 0.5.
- **Prophet:** splits each signal history into trend, seasonality, and residual. Residuals flag quarters that break the usual pattern.
- **Survival analysis:** predicts when a company is likely to revise guidance
  - Companies that haven't revised yet are handled as censored observations.

## Topic Intelligence
- **BERTopic:** finds themes per sector and quarter.
  - The minimum cluster size is set to 2% of the corpus.
  - Topics with more than 0.85 similarity are merged.
- **Coreference resolution:** links pronouns in Q&A exchanges to the right speaker or entity.
- **Topic shift tracking:** flags themes that appear or disappear, and companies that break from their sector's narrative.

## Agentic Advanced Queries
- **Multi-step reasoning chains:** break a question into steps, run them in order, and combine the results.
  - Example: "compare hedging trends across the sector, then explain the outlier."
- **Comparison queries:** side-by-side analytics across companies or periods, with data retrieved in parallel and results shown as a table.
- **Response synthesis:** combines forecasts, topics, signals, and uncertainty into one answer.

## Dashboard
- **Survival curves:** each company's time-to-revision probabilities.
- **Topic trend heatmap:** themes by sector and quarter.
- **TFT fan charts:** forecast intervals at 1, 2, 5, and 10 quarters ahead.
- **Prophet decomposition plots.**
- **Chat panel:** now shows each step of a multi-step query.

## Validation
- **Integration testing:** (`tests/test_phase21.py`).