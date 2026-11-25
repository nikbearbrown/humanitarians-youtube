**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 19 — Uncertainty Quantification, Cross-Company Intelligence, and Agentic Foundation

**Timeline:** November 1, 2026 – November 7, 2026

**Scope:** Phase 19 covers three areas:
- calibrated uncertainty around every forecast
- tracking how language shifts move between companies
- the first version of a conversational agent for querying ECIS in plain English

---

## Uncertainty Quantification
- **Conformal prediction:** distribution-free prediction intervals around each point estimate.
- **Monte Carlo dropout:** the MLP runs N times with dropout active, and the variance of the results is the uncertainty estimate.
- **Ensemble disagreement:** the spread across the six guidance revision models, used as an explicit uncertainty feature.
- **Selective prediction:** the system abstains from forecasting when uncertainty exceeds a configurable threshold.
- **Storage:** intervals, variance, disagreement scores, and abstention flags are stored with each forecast in PostgreSQL.

## Cross-Company Intelligence
- **Contagion modeling:** detects when one company's language shift comes before similar shifts at its sector peers.
- **Supply chain propagation:** tracks supplier hedging patterns that predict customer guidance revisions.
- **Temporal lag modeling:** measures the delay between a language signal and the price reaction, for each signal type.
- **Leading indicators:** ranks companies by how far ahead their language shifts predict sector-wide moves.
- **Storage:** contagion scores, lag estimates, and propagation links are stored in PostgreSQL.

## Agentic Foundation
- **Agent architecture:** a LangGraph conversational agent with state management for multi-turn questions.
- **Intent parser:** sorts each question into one of four types:
  - retrieval
  - comparison
  - analysis
  - explanation
- **Tool routing:** connects the agent to the signal database, prediction engine, and analytics modules.
- **Query execution:** turns plain-English questions into structured database and analytics calls.
- **Response synthesis:** combines tables, computed metrics, and short explanations into one answer.

## Dashboard
- **Forecast timeline:** shows prediction interval bands.
- **Per-prediction indicators:** variance, disagreement, and abstention status.
- **Contagion network graph:** arrows show the direction of influence between companies.
- **Temporal lag curves:** shown by signal type and by company.
- **Chat interface prototype:** displays how each question was classified and which tools were used.

## Validation
- **Integration testing:** across all the new modules (`tests/test_phase19.py`).
