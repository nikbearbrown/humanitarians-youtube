# Weekly Report: Week 22 (Phase 22)

**Project:** Mycroft — ECIS (Earnings Call Intelligence System) + Decision Scorecard
**Week:** November 22 – November 28, 2026
**Total hours:** 29.75

---

## Summary

Week 22 added structural reasoning and deeper language analysis.

- **Graph models:** the first tools for reasoning about relationships and unusual transcripts.
  - a graph neural network that learns how influence flows between companies
  - a variational autoencoder that flags transcripts unlike the usual pattern
- **Language enhancement:** makes the language layer more financially aware.
  - a language model fine-tuned on the earnings call corpus
  - entity linking from company mentions to tickers
  - automatic call summaries
  - argument mining that pairs management's claims with their evidence
- **Signal processing:** wavelet decomposition separating lasting trends from short-term noise.
- **Dashboard additions:**
  - a company relationship map
  - an entity graph viewer
  - an auto-summary panel
  - an argument structure view
  - anomaly scores per transcript

---

## Work Completed

### Graph Models

#### 1. Graph Neural Network for Cross-Company Modeling
*Development · Graph Models*
- Represents companies as nodes, with contagion and supply chain links as weighted edges.
- Learns how strongly a change at one company carries over to another, using message passing with attention.
- Limited to two hops, because deeper message passing blurred individual company signals together.
- **Deliverable:** GNN module with company graph and edge weight learning
- **Links:**
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graph_models/graph.py
  - https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graph_models/gat.py
- **Status:** Complete

#### 2. Variational Autoencoder for Transcript Anomaly Detection
*Development · Graph Models*
- Learns what a typical transcript's features look like and flags transcripts that don't fit.
- Catches unusual combinations of features, not just single extreme values.
- Trained on a curated 20-feature subset after the full 40+ feature set proved unstable.
- **Deliverable:** VAE anomaly detection module with per-transcript anomaly scoring
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graph_models/vae.py
- **Status:** Complete

### Language Enhancement

#### 3. Domain-Specific Language Model Fine-Tuning
*Development · Language Enhancement*
- Fine-tuned a language model on the full earnings call corpus.
- Improves downstream NLP tasks by teaching the model financial vocabulary and phrasing.
- **Deliverable:** domain-tuned language model on earnings call corpus
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graph_models/domain_lm.py
- **Status:** Complete

#### 4. Named Entity Linking
*Development · Language Enhancement*
- Resolves company mentions in transcripts to their tickers.
- Handles aliases, subsidiaries, and informal references.
- Checks the surrounding text before linking short strings, so a word like "AI" isn't mistaken for a ticker.
- **Deliverable:** named entity linking module with ticker resolution
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graph_models/entity_link.py
- **Status:** Complete

#### 5. Earnings Call Summarization Model
*Development · Language Enhancement*
- Generates a concise summary of each earnings call.
- Uses a two-stage pipeline: key sentences are selected first, then rewritten into a summary.
- **Deliverable:** earnings call auto-summarization module
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graph_models/summarize.py
- **Status:** Complete

#### 6. Argument Mining
*Development · Language Enhancement*
- Extracts claims made by management and the evidence offered for them.
- Shows whether management supports its statements or simply asserts them.
- **Deliverable:** argument mining module with claim-evidence extraction
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graph_models/arguments.py
- **Status:** Complete

### Signal Processing

#### 7. Wavelet Decomposition on Signal Time-Series
*Development · Signal Processing*
- Separates each signal's trend from noise at several time scales.
- Distinguishes lasting structural shifts from call-to-call volatility.
- **Deliverable:** wavelet decomposition module with multi-scale trend separation
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/graph_models/wavelet.py
- **Status:** Complete

### Dashboard

#### 8. GNN Network Graph
*Development · Dashboard*
- Interactive company relationship map showing learned influence and contagion strength between companies.
- **Deliverable:** interactive GNN network graph dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 9. Entity Graph Viewer
*Development · Dashboard*
- Shows resolved company mentions linked across calls, and how companies reference one another in analyst and management dialogue.
- **Deliverable:** entity graph viewer dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 10. Auto-Summary Panel
*Development · Dashboard*
- Shows the generated summary for each call, with key topics and guidance highlights.
- **Deliverable:** auto-summary dashboard panel per earnings call
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 11. Argument Structure View
*Development · Dashboard*
- Shows management's claims linked to their supporting evidence.
- **Deliverable:** argument structure dashboard view with claim-evidence linking
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

#### 12. VAE Anomaly Scores per Transcript
*Development · Dashboard*
- Shows an anomaly score for each transcript and flags unusual calls, with details on what didn't fit.
- **Deliverable:** VAE anomaly score dashboard view
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/src/ecis/dashboard/views.py
- **Status:** Complete

### Debugging

#### 13. Debugging & Testing
*Development · Debugging*
- Resolved issues across the graph models, language enhancement, and signal processing. The main ones:
  - GNN signals blurring together beyond two hops
  - VAE training instability on the full feature set
  - entity linking matching short words like "AI" as tickers
- Ran integration testing across all the new components.
- **Deliverable:** resolved issues and verified fixes
- **Link:** https://github.com/nikbearbrown/mycroft/blob/main/projects/ecis/tests/test_phase22.py
- **Status:** Complete

### Research

#### 14. Graph Attention Networks in Financial Prediction
*Research · Graph Models*
- Researched graph attention network designs for financial prediction, where the importance of each connection depends on context.
- **Deliverable:** research notes on GAT architectures for financial modeling
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 15. VAE vs Alternative Anomaly Detection Approaches
*Research · Anomaly Detection*
- Compared variational autoencoders with other anomaly detection methods for text features, including reconstruction-based and density-based approaches.
- **Deliverable:** research notes on VAE and anomaly detection method comparison
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 16. Extractive-Abstractive Summarization Benchmarks
*Research · Summarization*
- Reviewed summarization benchmarks and current approaches suited to earnings call transcripts.
- **Deliverable:** research notes on summarization benchmarks and methods
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

#### 17. Argument Mining Frameworks Study
*Research · Argument Mining*
- Studied frameworks for extracting claims and evidence from text, and how well they fit management statements.
- **Deliverable:** research notes on argument mining frameworks
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/research
- **Status:** Complete

### Writing

#### 18. Substack Article: "How Graph Attention Networks Learn Which Neighbors Matter"
*Writing · Substack Article*
- Explains how graph attention networks decide how much weight each neighbor gets based on content.
- Applies the idea to modeling influence between companies.
- **Deliverable:** published Substack article
- **Link:** https://mycroftproject.substack.com/p/graph-attention-networks-learned-neighbor-weighting
- **Status:** Complete (published)

### Artifact

#### 19. Auto-Summary Comparison
*Artifact · Claude Artifact*
- Interactive side-by-side view of a full earnings call transcript and its generated summary.
- Highlights the sentences chosen in the first stage and why they were chosen.
- **Deliverable:** Claude Artifact: Auto-Summary Comparison
- **Link:** https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis/docs/artifacts
- **Status:** Complete

### Video

Both videos follow the same split.
- **Concept, ideas, narration, and direction:** original work.
- **Assembly:** Claude, using the video generation tool created by Humanitarians AI.

#### 20. Video: "ECIS Episode 17: Weekly Project Update"
*Documentation · Video Production*
- Weekly Mycroft ECIS project update. Covers:
  - graph-based cross-company modeling
  - domain-tuned language processing
  - argument mining
  - wavelet signal decomposition
- **Deliverable:** Video: ECIS Episode 17
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-27-ecis-explained
  - https://drive.google.com/drive/folders/1Iry0drBjXAoFGKaaxGuccqAq6RGCO_c_
- **Status:** Complete

#### 21. Video: "Fine-Tuning Explainer"
*Documentation · Video Production*
- STEM educational video on fine-tuning.
- Explains how continued pre-training, task fine-tuning, and LoRA adapters reshape a language model's weights to specialize it for a domain.
- **Deliverable:** Video: Fine-Tuning Explainer
- **Links:**
  - https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/anjana-n/2026-11-27-finetuning-explainer
  - https://drive.google.com/drive/folders/1gqdgH8vstfYRKv32iWxdidjYEw9182vf
- **Status:** Complete