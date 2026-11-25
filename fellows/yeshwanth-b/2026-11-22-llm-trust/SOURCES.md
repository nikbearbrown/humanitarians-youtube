# SOURCES — Can You Trust Your AI? How We Test Large Language Models

**Source script:** supplied by Yeshwanth Balaji on 2026-11-20 (topic, audience, four learning goals, six sections, recap, closing, six required visuals). It was fact-checked against the paper and rewritten in the channel's Plain register, not read verbatim.

**Paper:** Nik Bear Brown, "Enhancing Trust in LLMs: Algorithms for Comparing and Interpreting LLMs", arXiv:2406.01943 [cs.CL], v1, 4 June 2024. https://arxiv.org/abs/2406.01943 · full text https://arxiv.org/html/2406.01943 (read 2026-11-20).

**Model used for the embedding beat:** sentence-transformers/all-MiniLM-L6-v2 (Apache-2.0), ONNX export, revision `1110a243fdf4706b3f48f1d95db1a4f5529b4d41`, run locally with onnxruntime. Downloaded free from the Hugging Face Hub, no account.

**Physics check:** Antoine equation constants for water (A 8.07131, B 1730.63, C 233.426; mmHg, °C); Everest summit pressure about 253 mmHg (West et al., 1983).

## Corrections and changes to the supplied script

| Where | Supplied | Film | Why |
|---|---|---|---|
| Section 2 | A/B testing presented with the paper's toolbox | Kept, but the footnote says A/B testing is industry practice and not in the survey | DOUBLE-CHECK LAW: the paper never mentions A/B testing |
| Section 3 | Swap names/genders/regions as a fairness test | Kept, credited to the survey's counterfactual explanations (§21.1) | The paper's fairness section (§10) uses disaggregated metrics; the swap idea is in §21.1 |
| Section 4 | "Explanations help engineers spot errors" | Kept, plus the survey's own caution (§20.3) that attention is not proof | Teardown honesty: the survey hedges this itself |
| Section 2 | "Automated metrics score outputs against reference answers" | Shown with a real ROUGE-1 calculation in which a wrong answer outscores a right one | SHOW-DON'T-TELL; "one score never tells the whole story" demonstrated, not asserted |
| Section 4 | "Similar ideas cluster together" | Shown with real embeddings from a small open model | EXECUTABLE-EVIDENCE: run the model instead of drawing a picture of one |
| Credit | "Credit slide: Nik Bear Brown, arXiv 2406.01943" | Credit beat adds that the paper is a survey and the examples are ours | So no example is mistaken for a result from the paper |
| Hook | "a confident-sounding wrong answer" | Everest boiling point (100 °C vs about 70 °C) | Needed a concrete, checkable example; the physics is verified in `evidence/boiling.txt` |

## Verbatim quotes on screen

- §5: "these metrics have been found to have low correlation with human judgment"
- §13.3: "over-optimization for specific benchmarks"
- §20.3: "High attention does not always equate to causal importance"
- §25 (spoken, paraphrased as "indispensable"): "Human Evaluation stands as an indispensable method for appraising Large Language Models"
