# Weekly Report: Week 21 (Phase 21)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** November 15 – November 21, 2026
**Total hours:** 32.0

---

## Summary

Week 21 added three capabilities.

- **Advanced forecasting:** extends how far ahead the system can see.
  - a Temporal Fusion Transformer forecasting 1, 2, 5, and 10 quarters ahead
  - Prophet trend and seasonality decomposition
  - survival analysis that predicts when a company is likely to revise guidance, not just whether it will
- **Topic intelligence:** detects what earnings calls are about and when that changes.
  - BERTopic themes per sector and quarter
  - coreference resolution for Q&A
  - topic shift tracking
- **Agentic advanced queries:** the agent can now handle questions that need several steps.
  - multi-step reasoning chains
  - comparison queries
  - richer answers that combine forecasts, topics, signals, and uncertainty
- **Dashboard additions:**
  - survival curves
  - a topic trend heatmap
  - forecast fan charts
  - Prophet decomposition plots
  - multi-step support in the chat panel

---

## Work Completed

### Advanced Forecasting

#### 1. Temporal Fusion Transformer for Multi-Horizon Forecasting
*Development · Advanced Forecasting*
- Forecasts signals 1, 2, 5, and 10 quarters ahead.
- Uses variable selection and interpretable attention to show which inputs the model relied on.
- **Deliverable:** TFT model with multi-horizon forecast generation (1/2/5/10 quarters)
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/tft.py
- **Status:** Complete

#### 2. Prophet Trend & Seasonality Decomposition
*Development · Advanced Forecasting*
- Separates each signal's long-term trend from repeating seasonal patterns.
- Quarters that break the usual pattern stand out as residuals.
- **Deliverable:** Prophet decomposition module with trend/seasonality/residual outputs
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/prophet.py
- **Status:** Complete

#### 3. Survival Analysis for Time-to-Revision Prediction
*Development · Advanced Forecasting*
- Predicts when a company is likely to revise guidance, not just whether it will.
- **Deliverable:** survival analysis module with time-to-revision probability curves
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/survival.py
- **Status:** Complete

### NLP & Topic Intelligence

#### 4. BERTopic Topic Modeling
*Development · NLP & Topic Intelligence*
- Finds the themes discussed in earnings calls for each sector and quarter.
- Surfaces new topics and shifting strategic priorities.
- **Deliverable:** BERTopic topic modeling module with sector-quarter theme extraction
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/topics.py
- **Status:** Complete

#### 5. Coreference Resolution for Q&A
*Development · NLP & Topic Intelligence*
- Works out who or what pronouns refer to in Q&A exchanges.
- Makes sure statements are attributed to the right person or company.
- **Deliverable:** coreference resolution module for Q&A sections
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/coref.py
- **Status:** Complete

#### 6. Topic Shift Tracking
*Development · NLP & Topic Intelligence*
- Flags when new themes appear or established ones disappear from one quarter to the next.
- Detects changes in a company's or sector's narrative.
- **Deliverable:** topic shift detection module with emergence and disappearance alerts
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/topic_shift.py
- **Status:** Complete

### Agentic Advanced Queries

#### 7. Multi-Step Reasoning Chains
*Development · Agentic Advanced Queries*
- Lets the agent break complex questions into steps and run them in order.
- Example: "compare hedging trends across the sector, then explain the outlier".
- **Deliverable:** multi-step reasoning chain module for complex queries
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/reasoning.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/agent.py
- **Status:** Complete

#### 8. Comparison Queries
*Development · Agentic Advanced Queries*
- Handles side-by-side comparisons across companies or time periods.
- Retrieves the data for each side in parallel and presents the results as a table.
- **Deliverable:** comparison query module with parallel retrieval and formatting
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/compare.py
- **Status:** Complete

#### 9. Response Synthesis Refinement
*Development · Agentic Advanced Queries*
- Answers can now combine forecasts, topic analysis, signal data, and uncertainty estimates into one coherent explanation.
- **Deliverable:** enhanced response synthesis with multi-source answer composition
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/compare.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/forecasting/reasoning.py
- **Status:** Complete

### Dashboard

#### 10. Survival Curves per Company
*Development · Dashboard*
- Shows each company's time-to-revision probabilities
- **Deliverable:** survival curve dashboard view with time-to-revision probabilities
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 11. Topic Trend Heatmap
*Development · Dashboard*
- Shows themes by sector and quarter, highlighting topics that are emerging or disappearing.
- **Deliverable:** topic trend heatmap dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 12. TFT Multi-Horizon Forecast Viewer
*Development · Dashboard*
- Fan charts showing prediction intervals at 1, 2, 5, and 10 quarters ahead.
- **Deliverable:** TFT fan chart forecast dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 13. Prophet Decomposition Plots
*Development · Dashboard*
- Shows the trend, seasonality, and residual for each company's signal history.
- **Deliverable:** Prophet decomposition dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 14. Agentic Chat Panel with Multi-Step Support
*Development · Dashboard*
- The chat panel now shows each step of a multi-step query and its intermediate results.
- **Deliverable:** upgraded agentic chat panel with reasoning chain display
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

### Debugging

#### 15. Debugging & Testing
*Development · Debugging*
- Resolved issues across the forecasting models, topic intelligence, and multi-step reasoning. The main ones:
  - TFT training that would not converge
  - BERTopic producing a different number of topics on each run
- Ran integration testing across all the new components.
- **Deliverable:** resolved issues and verified fixes
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase21.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/intelligence/agent.py
- **Status:** Complete

### Research

#### 16. Temporal Fusion Transformer Architecture Study
*Research · Advanced Forecasting*
- Studied the TFT architecture for multi-horizon financial forecasting:
  - variable selection networks
  - gated residual networks
  - interpretable multi-head attention
- **Deliverable:** research notes on TFT architecture and applicability
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 17. Agentic Layer Advanced Query Research
*Research · Agentic Architecture*
- Researched approaches to multi-step reasoning chains, comparison queries, and response synthesis for querying financial analytics.
- **Deliverable:** research notes on agentic multi-step reasoning approaches
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Writing

#### 18. Substack Article: "Multi-Step Reasoning Chains: When One Call Is Not Enough"
*Writing · Substack Article*
- Explains why chaining several LLM calls, with routing logic between them, gives more reliable and auditable results than a single call, especially on complex financial text.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/multi-step-reasoning-chains-llm-routing-validation
- **Status:** Complete (published)

### Artifact

#### 19. Multi-Step Query Trace
*Artifact · Claude Artifact*
- Interactive artifact: type a complex question and see the agent's full reasoning chain.
- Shows each step's intent classification, tool routing, and intermediate results.
- **Deliverable:** Claude Artifact: Multi-Step Query Trace
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 20. Video: "ECIS Episode 16: Weekly Project Update"
*Documentation · Video Production*
- Weekly Mycroft ECIS project update. Covers:
  - multi-horizon fan chart forecasts
  - time-to-revision modeling
  - BERTopic theme tracking
  - multi-step agentic reasoning
- **Deliverable:** Video: ECIS Episode 16
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-20-ecis-explained
  - https://drive.google.com/drive/folders/1_gYuRX-K0r4SW9nhhYR-IZ00acrjkF4g
- **Status:** Complete

#### 21. Video: "What a Temporal Fusion Transformer Actually Does"
*Documentation · Video Production*
- STEM educational video on the Temporal Fusion Transformer.
- Explains how variable selection, gated residual networks, and interpretable attention help it outperform LSTMs on longer forecast horizons.
- **Deliverable:** Video: TFT Explainer
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-20-tft-explainer
  - https://drive.google.com/drive/folders/14KYNFReS6l4ElGfUVXzvT4VQ3tikk7sH
- **Status:** Complete