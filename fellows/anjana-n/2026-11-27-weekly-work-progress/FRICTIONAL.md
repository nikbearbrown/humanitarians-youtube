# Friction Log: Week 22 (Phase 22)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** November 22 – November 28, 2026

---

## 1. Focus of the week

- **Graph models:**
  - a graph neural network (GNN) for influence between companies
  - a variational autoencoder (VAE) for spotting unusual transcripts
- **Language enhancement:**
  - domain fine-tuning on the earnings call corpus
  - named entity linking to tickers
  - call summarization
  - argument mining
- **Signal processing:** wavelet decomposition into trend and noise at several time scales.
- **Dashboard:**
  - company relationship map
  - entity graph viewer
  - auto-summary panel
  - argument structure view
  - anomaly scores per transcript


## 2. What was tried, and what was expected

- **GNN:** expected deeper message passing (three or more hops) to capture longer chains of influence, such as supplier → manufacturer → retailer.
- **VAE:** expected to train on the full 40+ feature set and learn what a normal transcript looks like across all features.
- **Entity linking:** expected fuzzy matching to resolve company mentions to tickers reliably.

## 3. Points of resistance, and next steps taken

### GNN signals blurred together beyond two hops (load-bearing)
- **What happened:** beyond two hops, each company's signal washed out into an average of its neighbors. Every company ended up looking the same.
- **What was tried:** skip connections around the message-passing layers. These kept some of each company's identity, but results still degraded at three or more hops.
- **Next step:** the GNN is limited to two hops. About 35 minutes went into diagnosing and testing fixes.
- **Lesson:** there is a real trade-off. Looking further across the network captures longer chains of influence but erases what makes each company distinct.
  - The cost: the model can learn that A affects B and that B affects C, but not the full A → B → C path in one pass.

### VAE training was unstable on the full feature set
- **What happened:** with all 40+ features, the model learned to ignore the high-variance features and reconstruct only the stable ones.
- **Next step:** training was moved to a curated 20-feature subset, which stabilized it. About 30 minutes went into diagnosing the problem.
- **Lesson:** stability came at the cost of coverage. The detector can only flag unusual patterns in the features it sees.
  - The dropped high-variance features may include the newer signals, such as dodge scores and hedging measures, which are among the most worth watching.

### Wavelet scales matched to earnings call cadence
- **What resisted:** a wavelet decomposition is only useful if its time scales match how often the data arrives.
- **Next step:** scales were chosen to reflect quarterly and annual patterns. This separates lasting shifts from call-to-call volatility.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos using the video generation tool created by Humanitarians AI.

### Claude (artifact)
- **Auto-Summary Comparison:** shows a full transcript next to its generated summary, highlighting which sentences were selected and why.

### Gru (SDD session)
- Documented this week's architecture changes.

### Eddy
- Reviewed "How Graph Attention Networks Learn Which Neighbors Matter" before publication.

## 5. Understood now, and still unresolved

### Understood
- **Deeper isn't always better in graph models.** Past two hops, the GNN loses the individual company signals it exists to compare.
- **Generative models can catch combined anomalies.** The VAE flags transcripts that look normal feature by feature but are unusual in combination. This complements the distance-based out-of-distribution check from Week 18.
- **Ambiguous short strings need context.** The same lesson applies to entity linking as to analyst name matching.
- **Established methods still need domain fitting.** The value of the language work is in adapting it to financial text, not in the methods themselves.

### Unresolved
- None