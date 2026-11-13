# Friction Log: Week 8 (Phase 8)

**Project:** Mycroft — ECIS + Decision Scorecard
**Week:** August 16 – August 22, 2026

---

## 1. Focus of the week

- **Model experimentation:** Qwen2.5-14B (AWQ 4-bit) configured and run on a representative subset, followed by:
  - Qwen-specific prompt adjustments
  - Scorecard evaluation
  - cross-tier error comparison (7B/8B vs. 14B)
- **Scaling:** extraction completed across the remaining tickers, plus full batch outcome resolution.
- **Pipeline hardening:**
  - input validation
  - confidence gating
  - JSON retry logic
  - signal provenance tracking
- **Infrastructure:** ticker registry and outcome caching improvements.
- **Architecture rework:**
  - per-chunk model identity
  - model tier as a triangulator weight
- **Dashboard:** three-model comparison view and Qwen metrics.
- **Research:** Qwen architecture and quantization; architecture review.
- **Outputs:**
  - Parameter Budget Calculator and Three-Model Arena (Claude artifacts)
  - two videos: "Attention in Finance Explained" and "ECIS Explained (EP3)"

## 2. What was tried, and what was expected

- **Model size:** open question going in was whether moving from 7B/8B to 14B would lift the Week 7 resolution plateau.
- **Inference speed:** expected Qwen2.5-14B at AWQ 4-bit to run at normal speed once loaded.
- **Provenance:** expected full prompt provenance per signal to be affordable to store.
- **Validation:** expected a single minimum token threshold to work across all tickers.
- **Weighting:** expected the Scorecard data to show how to weigh signals from different model tiers.

## 3. Points of resistance, and next steps taken

### More parameters didn't lift the plateau (load-bearing)
- **What happened:**
  - Qwen at 14B improved calibration on the maintained/none boundary compared with both 8B models.
  - It produced fewer false "maintained" signals on soft reaffirmation language.
- **What resisted:** resolution stayed flat. All three models struggle equally on genuinely ambiguous text, where "maintained" and "none" are both defensible readings.
- **Diagnosis:** the boundary problem is linguistic ambiguity in the taxonomy, not model capacity.
- **Next step:** strategy shifted away from bigger models toward better taxonomy definitions and prompt boundaries.
  - It took care not to read Qwen's calibration gain as an overall improvement.

### Qwen AWQ kernel compatibility
- **What happened:** the model loaded successfully, but inference ran 40% slower than expected.
- **Cause:** profiling showed Ollama falling back to CPU for attention operations the AWQ kernel didn't support on the Colab GPU configuration.
- **Next step:** switched to a different AWQ checkpoint with compatible kernel implementations.
- **Lesson:** the failure was not in the model or the quantization. It came from how one AWQ implementation interacted with one GPU, which only shows up when the model actually runs.

### Signal provenance storage inflation
- **What happened:** storing the full prompt per signal, including few-shot examples and temporal context, inflated the signals database by 3x.
- **Next step:** switched from raw text to compressed JSON blobs, bringing storage down to 1.4x baseline.
- **The trade-off:**
  - At 1.4x, provenance is still fully reconstructable.
  - Heavier compression would force decompression for field-level access, degrading the audit trail for debugging.
  - 1.4x was a deliberate balance between storage cost and audit trail integrity.

### Input validation false positives
- **What happened:** validation rejected legitimate chunks from one ticker whose transcripts use unusually short paragraphs. Valid content fell below the minimum token threshold.
- **Next step:** lowered the threshold and added a per-ticker override capability.
  - The exceptions are systematic (stored in the registry), not ad hoc manual fixes.
- **Lesson:** a recurring theme. Universal rules applied to heterogeneous financial data always produce edge cases that need company-specific exceptions.

### Weighting across model tiers
- **What resisted:** when a high-confidence 8B signal and a low-confidence 14B signal disagree on the same chunk, the Scorecard data can't yet say which should win.
- **Next step:**
  - Weight by model tier initially.
  - Let vindication aggregation adjust the weights over time.
  - Start from a reasonable prior rather than wait for data that doesn't yet exist.

## 4. AI and other contributions: accepted, changed, rejected

### Claude + Humanitarians AI video generation tool
- **Original work:** the concept, ideas, narration, and direction for both videos.
- **Claude's part:** assembled the videos, using the video generation tool created by Humanitarians AI.

### Claude (artifacts)
- **Parameter Budget Calculator:** estimates VRAM, inference time, and compute units from model size, quantization, and chunk count. Used to check whether a configuration fits the available hardware before running it.
- **Three-Model Arena:** shows Llama, Mistral, and Qwen extractions side by side, with disagreement highlighting and the triangulator's resolution view.

### Gru (SDD session)
- Documented the multi-model architecture decisions and the provenance tracking design.

## 5. Understood now, and still unresolved

### Understood
- **The resolution plateau is structural:** the same ceiling appeared across three models at three parameter scales. It is a property of the task's ambiguity, not of any one model.
- **Calibration vs. resolution:** calibration gains are real and meaningful, but they are a different thing from resolution gains.
- **Hardware compatibility:** a model that loads is not necessarily running as intended. Profiling caught a silent CPU fallback.
- **Audit trails:** they have a cost, and the right compression level is the one that keeps them usable.
- **Exceptions:** heterogeneous sources need systematic, registry-based exceptions, not one-off fixes.

### Unresolved
- **Taxonomy work:** turning the "better definitions, not bigger models" conclusion into implementation work.
- **Routing:** whether the narrowed benefit justifies the operational complexity of multiple models in production.
- **Tier weights:** whether tier-based weighting converges to the right values as vindication data accumulates.
