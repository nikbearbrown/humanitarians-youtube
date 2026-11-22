# Friction Log: Week 21 (Phase 21)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** November 15 – November 21, 2026

---

## 1. Focus of the week

- **Advanced forecasting:**
  - Temporal Fusion Transformer (1/2/5/10-quarter horizons)
  - Prophet decomposition
  - survival analysis for time-to-revision
- **Topic intelligence:** BERTopic themes, coreference resolution for Q&A, and topic shift tracking.
- **Agentic advanced queries:** multi-step reasoning chains, comparison queries, and refined response synthesis.
- **Dashboard:**
  - survival curves
  - topic heatmap
  - forecast fan charts
  - Prophet plots
  - multi-step chat panel

## 2. What was tried, and what was expected

- **TFT training:** expected to converge with its default settings.
- **BERTopic:** expected to produce a set of topics from run to run.
- **Guidance revision:** expected to be well served by asking "will they revise?" as a yes/no question.
- **Attention weights:** expected the TFT's to show why the model made each forecast.

## 3. Points of resistance, and next steps taken

### "Will they revise?" was the wrong question (load-bearing)
- **What resisted:** a yes/no answer misses the more useful information, which is when a revision is likely.
- **Next step:**
  - Guidance revision was reframed as a time-to-event problem, using survival analysis.
  - The model now estimates how revision changes over time, given the current signal trajectory.
  - Companies that haven't revised yet are handled correctly rather than counted as "no revision".
- **Lesson:** changing how a problem is framed can matter more than changing the model.

### TFT training would not converge
- **What happened:** with the default learning rate, the loss kept oscillating and never settled.
- **Next step:**
  - Learning rate reduced to 1e-4, with a cosine annealing schedule and gradient clipping at 0.5.
  - About 40 minutes of training runs before it stabilized.
- **Lesson:** a similar fix to Week 20's LSTM. These settings are worth keeping as the default starting configuration for future neural models.

### BERTopic produced a different number of topics each run
- **What happened:** the clustering step was too sensitive to its minimum cluster size, so different runs found different numbers of topics.
- **Next step:**
  - The minimum cluster size is now set relative to the corpus: 2% of documents.
  - Topics with more than 0.85 similarity are merged.
- **Lesson:** a similar problem to Week 20's HMM regimes. Unsupervised clustering needs settings that scale with the data and a step that removes near-duplicates.
  - The merge trades some topic detail for stability.

### Attention shows what the model looked at, not why
- **What resisted:** the TFT's attention weights show which past quarters the model focused on. That is easy to misread as which quarters caused the forecast.
- **Next step:** TFT explanations are presented as what the model relied on, not as causes.

### Sector narratives as context
- **What resisted:** a company's themes mean more when compared with what the rest of its sector is saying.
- **Next step:** topic shift tracking flags companies that break from their sector's common narrative. For example, one company talks about expansion while its peers talk about cost cutting.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifact)
- **Multi-Step Query Trace:** shows the agent's full reasoning chain for a complex question: each step, the tools it used, and the intermediate results.

### Gru (SDD session)
- Documented this week's architecture changes.

### Eddy
- Reviewed "Multi-Step Reasoning Chains: When One Call Is Not Enough" before publication.

## 5. Understood now, and still unresolved

### Understood
- **When matters as much as whether.** Survival analysis answers a more useful question than yes/no classification.
- **Neural models need stable training settings.** A lower learning rate, a schedule, and gradient clipping now look like the default.
- **Clustering settings should scale with the data.** Otherwise results change from run to run.
- **Order matters in multi-step reasoning.** An outlier can't be explained before it has been identified.

### Unresolved
- None