# FACTCHECK — Can You Trust Your AI? How We Test Large Language Models

Every factual claim in the narration or on screen, with its source. The paper was read in full (arXiv HTML v1, sections 1–26) on 2026-11-20.

**Paper:** Nik Bear Brown, "Enhancing Trust in LLMs: Algorithms for Comparing and Interpreting LLMs", arXiv 2406.01943, v1, 4 June 2024 (cs.CL). It is a literature survey: it reports no experiments, results or model rankings of its own.

| Beat | Claim | Source | Status |
|---|---|---|---|
| B00 | Researchers measure models (scores, benchmarks, bias tests), look inside them (embeddings, attention, explanations) and keep people in the loop | Paper §3 list, §§4–5, 10, 13, 20, 22, 23, 25 | ✓ (answer labelled illustrative) |
| B02 | Water boils at about 70 °C at the summit of Everest, not 100 °C | `evidence/boiling.txt`: Antoine equation at 253 mmHg gives 71.9 °C | ✓ ("about 70") |
| B02 | A confident answer that isn't true is called a hallucination | Common usage; paper §16 defines a Hallucination Score over "hallucinated content" | ✓ |
| B02 | The model answer shown | Invented for the film | Labelled "Illustrative answer, not from a specific model" |
| B03 | Models can learn unfair patterns from training data (bias) | Paper §10 | ✓ |
| B03 | Black box: no easy way to see why a model said what it said | Paper §§1–2 (transparency) | ✓ |
| B04 | Researchers' toolbox: metrics, benchmarks, head-to-head comparisons, bias tests, interpretability, human review | Paper §§4–5, 13, 10, 19–23, 25; A/B testing is **not** in the paper | ✓ with on-screen footnote: "Five of the six are covered in the survey; head-to-head A/B testing is common industry practice" |
| B05 | BLEU and ROUGE score an answer by words shared with a reference | Paper §5.1–5.2 (n-gram overlap; ROUGE emphasises recall) | ✓ |
| B05 | The wrong answer scores 0.87; a correct answer in other words scores 0.25 | `evidence/overlap.json` (ROUGE-1 F1, computed locally by `overlap.py`) | ✓ real computation |
| B05 | "these metrics have been found to have low correlation with human judgment" | Paper §5 introduction, verbatim | ✓ |
| B06 | Benchmarks: every model takes the same test, scored the same way; leaderboards rank them | Paper §13 | ✓ |
| B06 | A/B testing compares two versions on the same prompts | General industry practice; not attributed to the paper | ✓ (narration does not credit the survey for it) |
| B06 | "over-optimization for specific benchmarks" | Paper §13.3, verbatim phrase | ✓ |
| B06 | Bars, ranks and A/B votes | Invented layout | Labelled "Illustrative bars and choices · no real models or scores" |
| B07 | Swap one sensitive detail (name, gender, region) and compare: a quality shift is a bias signal | Paper §21.1: counterfactuals "that alter demographic or contextually sensitive aspects of the input" to uncover bias. The paper's fairness section (§10) has no name-swap test, so the film credits §21 | ✓ |
| B07 | The two letters' comparison rows | Invented | Labelled "Illustrative comparison: how the test works, not a real model's output" |
| B08 | Models represent words as points in a space with hundreds of dimensions (embeddings); similar ideas cluster | Paper §23 (embedding space analysis: t-SNE/PCA, cosine similarity, clusters); all-MiniLM-L6-v2 has 384 dimensions | ✓ |
| B08 | The plotted points, clusters, kitten ~ cat 0.79, kitten ~ guitar 0.25 | `evidence/embed.json`: all-MiniLM-L6-v2 (rev 1110a24) run locally, PCA to 2-D, cosine on full vectors | ✓ real computation. The word set was chosen from four candidates as the one that separates most clearly in 2-D (BUILD-LOG) |
| B09 | Asking a model to explain its reasoning helps engineers spot errors | Paper §22 (language-based explanations) | ✓ |
| B09 | The three reasoning steps | Invented | Labelled "Illustrative explanation" |
| B09 | "High attention does not always equate to causal importance" | Paper §20.3, verbatim | ✓ |
| B10 | Metrics miss tone, context and subtle errors; people judge coherence, helpfulness, real-world fit | Paper §5 (low correlation with human judgment), §25.1 (quality, relevance, coherence) | ✓ |
| B10 | The survey calls human evaluation "indispensable" | Paper §25: "an indispensable method" | ✓ |
| B10 | The strongest evaluations combine both | Paper §5.9, §25.3 (integrate human assessment with automated metrics) | ✓ |
| B11 | The four-question checklist | Supplied script; practical advice, not a paper claim | ✓ |
| B12 | Title, author, arXiv 2406.01943, June 2024; a survey with no experiments of its own | arXiv abs page; full text | ✓ |
| B14 | Suggested prompt | Written for the film | — |

## Not claimed

- That the paper runs experiments, ranks models or proves any trust gain.
- That the paper describes A/B testing or a name-swap test in its fairness section.
- That the Hallucination Score has a formula (the paper gives none). The film does not mention the score by name.
- That Nik Bear Brown invented LLMMaps (the paper credits Puchert, 2023). The film does not mention LLMMaps.
- Any model names, versions, prices or usage statistics.
