**Repository:** [https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis](https://github.com/nikbearbrown/mycroft/tree/main/projects/ecis)

# Mycroft ECIS — Phase 22 — Graph Models, Language Enhancement, and Signal Processing

**Timeline:** November 22, 2026 – November 28, 2026

**Scope:** Phase 22 covers three areas:
- learning how influence flows between companies
- detecting unusual transcripts
- deepening the language layer with financially aware NLP

---

## Graph Models
- **Graph neural network:** companies are nodes, and contagion and supply chain links are weighted edges.
  - Message passing with attention learns how strongly each company influences the others.
  - Limited to two hops to avoid over-smoothing.
- **Variational autoencoder:** learns the normal distribution of transcript features and scores each transcript by reconstruction error.
  - Trained on a curated 20-feature subset for stability.

## Language Enhancement
- **Domain fine-tuning:** a language model fine-tuned on the full earnings call corpus.
- **Named entity linking:** resolves company mentions, aliases, and subsidiaries to tickers.
  - Context-window checks prevent short strings like "AI" from being linked as tickers.
- **Summarization:** a two-stage extractive-abstractive pipeline that generates a summary of each call.
- **Argument mining:** extracts management's claims and links them to their supporting evidence.

## Signal Processing
- **Wavelet decomposition:** separates each signal's trend from noise at several time scales, matched to quarterly and annual cadence.

## Dashboard
- **GNN network graph:** an interactive company relationship map with learned influence strengths.
- **Entity graph viewer:** resolved company mentions linked across calls.
- **Auto-summary panel:** the generated summary for each call.
- **Argument structure view:** claims linked to their evidence.
- **VAE anomaly scores:** a score for each transcript, with flagged outliers.

## Validation
- **Integration testing:** run across all new modules (`tests/test_phase22.py`).

## Open Items
- None