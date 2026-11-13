# Friction Log: Week 6 (Phase 6)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** August 2 – August 8, 2026

---

## 1. Focus of the week

- **Model experimentation:** Mistral-7B-Instruct configured alongside Llama 3.1 8B. Extraction run on a representative subset, then compared in three ways:
  - Scorecard comparison
  - self-consistency and hallucination comparison
  - Mistral-specific prompt adjustments
- **Pipeline scaling:** additional tickers ingested, followed by full extraction, batch outcome resolution, and Scorecard evaluation.
- **Feedback loops:** first full production cycle of the watchdog and learning graph.
- **Dashboard:** model comparison view and per-model reader metrics.
- **Research:** Mistral-7B architecture and configuration.
- **Outputs:**
  - the Model Comparison Dashboard (Claude artifact)
  - two Substack articles
  - two videos: "Why AI Dominates the Crypto Market" and "ECIS Explained"

## 2. What was tried, and what was expected

- **Prompts:** expected the Llama-optimized prompt templates to transfer to Mistral-7B with little change.
- **Pipeline code:** expected the self-consistency comparison logic and chunk handling to work unchanged for a second model.
- **Comparison:** expected the side-by-side Scorecard to show which model is better.
- **Thresholds:** expected the thresholds set in Week 5 to hold during the first full feedback loop cycle.

## 3. Points of resistance, and next steps taken

### Aggregate scores hid the real difference (load-bearing)
- **What resisted:** the headline Scorecard metrics did not surface the important distinction between the two models. Interpreting the error decomposition did.
  - **Llama:** calibration-heavy errors. It reads signals correctly but states confidence poorly, which recalibration can fix.
  - **Mistral:** resolution-heavy errors. It misreads signals at a structural level, which needs architectural intervention.
- **Supporting evidence:** Mistral's higher hallucination rate under temperature variation. Its extractions are less grounded in the source text, which fits the resolution diagnosis.
- **Next step:** a new design question for the next phase. Either route chunks to different models by signal type, to exploit the complementary error profiles, or fine-tune a single model on its failure mode.

### Mistral truncated JSON output
- **What happened:** ~10–15% of extractions using the Llama-optimized prompts came back as truncated JSON.
  - The partial JSON was valid, so it passed initial parsing.
  - It was missing fields the signal schema requires.
- **Diagnosis:** output format sensitivity, not a content problem. The information was often present in the reasoning trace but never serialized into the structured output.
- **Next step:** Mistral-specific prompt templates.

### Type mismatches in self-consistency vote comparison
- **What happened:** one model produced string confidence values, the other floats.
- **Why:** the comparison logic assumed uniform types because it had only ever seen one model's output.
- **Next step:** type normalization in the comparison layer.

### Non-deterministic chunk ordering
- **What happened:** the same transcript could produce chunks in different orders between runs.
- **Why it mattered:** cross-model alignment matches signals by source chunk. With unstable order, a signal difference could be a model difference or an alignment artifact, and there was no way to tell which.
- **Next step:** content hashing to give chunks stable IDs, independent of processing order.

### First feedback loop cycle
- **What resisted:** the system now modifies its own thresholds within bounds, and whether those bounds are right had to be checked.
- **Next step:** the cycle was observed, and the learning graph's automated threshold adjustments were checked for overcorrection.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos are original work.
- **Claude's part:** Claude assembled the videos, using the video generation tool created by Humanitarians AI.

### Claude (artifact)
- Built the Model Comparison Dashboard.
- It visualizes Brier scores, error decomposition, self-consistency behavior, and hallucination rates across both models.

### Gru (SDD session)
- Documented the model comparison architecture and the routing-vs-fine-tuning analysis.

### Eddy
- Reviewed both Week 6 articles before publication.

## 5. Understood now, and still unresolved

### Understood
- **Error type matters more than score:** the kind of error decides what to do next. Calibration-heavy errors call for recalibration; resolution-heavy errors call for architecture.
- **A second model tests the pipeline:** it exposed hidden single-model assumptions (output format, value types, chunk ordering) that one model never would have.
- **Self-consistency works across models:** the Week 3 framework, applied to a second model, revealed differences in grounding.
- **vLLM is now sequenced:** finish the model comparison on Ollama, then move the chosen configuration to vLLM for production batch inference. This was open since Week 3.

### Unresolved
- **Routing vs. fine-tuning:** informed by this week's data but not decided. Current data can't fully answer the generalization risk.
- **Threshold bounds:** whether the Week 5 thresholds stay right as the feedback loops keep adjusting them.
