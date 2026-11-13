# Friction Log: Week 7 (Phase 7)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** August 9 – August 15, 2026

---

## 1. Focus of the week

- **Model optimization:**
  - targeted QLoRA fine-tuning of Llama 3.1 8B on the maintained-vs-none boundary
  - before/after Scorecard comparison on held-out data
  - Mistral-7B routing for hedged-language chunks
- **Pipeline enhancement:**
  - maintained/none prompt boundary
  - temporal retrieval edge cases
  - exemplar collection
  - boilerplate detection
  - batch-level consistency checking
  - ticker registry
- **Scaling:** Mistral-7B extraction across additional companies.
- **Scoring:**
  - full Scorecard evaluation and recalibration
  - per-ticker reader comparison
- **Dashboard:** RAG interface improvements and a per-ticker view.
- **Research:**
  - QLoRA fine-tuning study
  - Mistral-7B exploration
  - routing reassessment after fine-tuning
- **Outputs:**
  - Fine-Tuning Data Reviewer (Claude artifact)
  - "Tokenizer Alignment Across Models" (Substack)
  - two videos: "FinBERT Explainer" and "ECIS Explained (EP2)"

## 2. What was tried, and what was expected

- **Fine-tuning:** expected targeted fine-tuning to fix the maintained-vs-none errors identified by the Week 5 error taxonomy. Success threshold: Brier skill score improvement above 0.05.
- **Training run:** expected the Colab training run to complete in one pass with the configured checkpointing.
- **Adapter:** expected the fine-tuned adapter to slot into the existing pipeline without changing anything other than extraction quality.
- **Routing:** expected routing hedged-language chunks to Mistral-7B to remain clearly beneficial after fine-tuning.

## 3. Points of resistance, and next steps taken

### Fine-tuning gains hit a ceiling (load-bearing)
- **Result:** Brier skill score improved by 0.07, above the 0.05 threshold.
  - Gains were concentrated in maintained-vs-none, as predicted.
  - The fine-tuned model now classifies soft reaffirmation language as maintained rather than none, for example "we continue to expect results in line with prior outlook".
- **What resisted:** Murphy decomposition showed calibration improved but resolution stayed flat.
  - Fine-tuning corrected confidence estimates on boundary cases.
  - It did not improve the model's ability to tell genuinely ambiguous text from clear maintained guidance.
- **Next step:** concluded that further fine-tuning iterations would likely not help, because the resolution plateau suggests a representation ceiling at 8B parameters.

### Training data composition
- **What resisted:** the composition of the training data, not the run itself, decides whether fine-tuning generalizes or memorizes.
- **Next step:** deliberate decisions on example selection, boundary balancing, and whether to correct reasoning traces alongside labels.
- Memorization risks were reviewed with the Fine-Tuning Data Reviewer artifact.

### QLoRA Colab disconnect with no intermediate checkpoint
- **What happened:**
  - Training disconnected at step 380 of 500.
  - Checkpoint-to-Drive was configured, but the interval was set to every 500 steps, so no intermediate checkpoint existed.
  - The full run had to restart from scratch.
- **Next step:** checkpoint interval reduced to every 100 steps.
- **Lesson:** the failure was not the disconnect, which is expected on Colab. It was the assumption that the run would complete uninterrupted. The checkpoint interval is a reliability decision disguised as a configuration parameter.

### Fine-tuned adapter tokenization drift
- **What happened:**
  - The adapter loaded correctly via Unsloth but tokenized 3–4% of chunks slightly differently from the base model.
  - Its modified attention patterns changed whitespace handling in the JSON output.
  - The same chunk text therefore produced different content hashes, breaking signal alignment.
- **Next step:** whitespace normalized before hashing.
- **Lesson:** fine-tuning changed output formatting, not just extraction quality, and the alignment logic couldn't tell the two apart.

### Routing benefit narrowed
- **What resisted:** after fine-tuning, Llama handles the maintained/none boundary well, but Mistral still outperforms on hedged downgrades.
  - Routing remains warranted for Category B hedged-language chunks.
  - Fine-tuning reduced the number of chunks where routing makes a difference.
- **Next step:** routing kept for hedged language. Whether the narrower benefit justifies running two models in production is carried forward as an explicit design trade-off.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos, using the video generation tool created by Humanitarians AI.

### Claude (artifact)
- Built the Fine-Tuning Data Reviewer.
- It visualizes the training example distribution across the maintained/none boundary, provides an example review interface, and flags memorization risks.

### Gru (SDD session)
- Documented the fine-tuning decisions, routing logic, and per-ticker analysis.

### Eddy
- Reviewed "Tokenizer Alignment Across Models" before publication.

## 5. Understood now, and still unresolved

### Understood
- **Error taxonomy:** the Week 5 error taxonomy was predictive. Targeting the identified boundary produced gains exactly where expected.
- **What fine-tuning fixes:** calibration, not resolution. A flat resolution component signals the limit of what fine-tuning at this model size can do.
- **Training reliability:** checkpoint intervals are reliability decisions, not defaults.
- **Fine-tuning side effects:** fine-tuning can change model behavior in ways unrelated to its target, such as output formatting, so downstream alignment needs to be robust to it.
- **Tokenization:** FinBERT-defined chunks don't map cleanly onto Llama tokens, which affects extraction consistency in multi-model pipelines.

### Unresolved
- **Routing complexity:** whether the narrowed routing benefit justifies the operational complexity of two models in production. Carried forward as an explicit design trade-off.
- **Per-ticker routing:** whether the per-ticker reader patterns should feed into ticker-specific routing or weighting.
