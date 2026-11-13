# FACTCHECK — 2026-09-21-project-overview (Fine-Tuning Platform)

Every claim the narration makes, mapped to the source document:
`work_report.md` ("Fine-Tuning Platform: Brainstorming Report").

## B00 — Cold open

- **"The fine-tuning platform" / "the one thing we haven't nailed down yet."**
  Framing device, not a factual claim — sets up the question the rest of the reel answers
  (the RL-calibration open question raised in source §3, "A key open question flagged
  during this brainstorming...").

## B01 — BLUF

- **"One pipeline: any model, any dataset, any job spec in, a fine-tuned model out."**
  Source §1: "The overall goal is to build a general-purpose fine-tuning platform capable
  of taking: (1) Any decision model from the Jev or Laya model family, (2) Any dataset...,
  and (3) A set of job specifications... and producing a fine-tuned model as output."
- **"The real question isn't whether it works. It's whether the model knows when it's
  wrong."**
  Editorial framing of source §3's calibration question — "whether 'calibrated decisions'
  means confidence calibration... or decision calibration" — compressed to the plain-language
  stake for a general viewer. Not a verbatim quote; the underlying open question is sourced.

## B02 — Architecture (5 stages)

- **"Five stages, one spec file."**
  Source §2.1: "The Training Runtime Worker processes a job specification through five
  stages," itemized 1-5 in the source (Config & Pre-flight Guard · Data Ingestion &
  Formatting Engine · Model & PEFT Setup · Core SFT Training Engine · Post-Training,
  Evaluation & Export).
- **"Pre-flight checks the GPU can handle it."**
  Source §2.1 stage 1: "Pydantic validation of the job spec, plus GPU/VRAM feasibility
  checks to prevent out-of-memory failures."
- **"Data gets ingested and masked to assistant tokens only."**
  Source §2.1 stage 2: "...applies model-specific chat templates, masks loss to
  assistant-only tokens, and creates train/eval splits."
- **"The model loads under QLoRA."**
  Source §2.1 stage 3: "loads the base model (4-bit QLoRA, 8-bit, or 16-bit LoRA),
  configures PEFT... and applies memory optimizations like gradient checkpointing."
- **"Hugging Face's SFTTrainer runs the loop, streaming live metrics."**
  Source §2.1 stage 4: "built on Hugging Face TRL's SFTTrainer + Accelerate, with a
  structured event callback streaming live JSON-lines metrics."
- **"Export: adapter, merged weights, or a quantized file ready for local inference."**
  Source §2.1 stage 5: "exports the LoRA adapter, optionally merges it into the base
  model, and optionally quantizes to GGUF for local inference (Ollama/llama.cpp)."

## B03 — The calibration gap

- **"A model that's right sixty percent of the time while claiming eighty-five percent
  confidence is miscalibrated."**
  Source §3.2, Idea 3 worked example table: the 0.8-0.9 confidence bin has "500 samples,
  300 correct, empirical accuracy 0.60," annotated in the source as "miscalibrated — model
  claims ~85%, only right 60%." The 85/60 figures used on screen are taken directly from
  this source row, not invented.
- **"In triage, in lending, in any real decision, that gap is the dangerous part."**
  Editorial generalization from the source's own running example (§3.2: "a medical triage
  model deciding 'urgent' vs. 'not urgent'"); lending is an illustrative analogy, not sourced
  to the report (the report only specifies the triage example).

## B04 — The fix (Brier score reward)

- **"Score each decision with a proper scoring rule. Negative confidence minus outcome,
  squared."**
  Source §3.1 idea 1 and §3.2: `reward = -(confidence - outcome)^2`, quoted verbatim from
  the source's Idea 1 section and the Python snippet in §5.2 (`brier_reward`).
- **"Only one policy maximizes it: stating your real probability of being right."**
  Source §3.2: "Because the Brier score is a strictly proper scoring rule, its expected
  value is maximized only when stated confidence equals the true probability of being
  correct."
- **"No auxiliary model, no aggregation."**
  Source §3.2, Idea 1 tradeoffs: "simple, no separate model or retraining loop."

## B05 — Next steps

- **"A sandbox that logs context, decision, confidence, and outcome from real rollouts."**
  Source §5.1: "Output a standardized rollout log... matching the schema... `{context,
  decision, confidence, outcome}`."
- **"A first RL script, scored on exactly that reward."**
  Source §5.2: "Implement a first working RL fine-tuning script based on Idea 1 (proper
  scoring rule / negative Brier score)... Compute `reward = brier_reward(confidence,
  outcome)` per sample. Feed rewards into a GRPO or PPO update step."
- **"Validated against held-out calibration error."**
  Source §5.2: "Validation: after each epoch (or every N steps), compute ECE on a held-out
  split to verify that calibration is actually improving, not just reward going up."

## B06 — Your Turn handoff

- Not a factual claim — a suggested prompt for the viewer to run on their own model's
  confidence scores, modeled on the binning method in source §3.2 (Idea 3, step 2).

## B07 — Outro

- Title restate only; no factual claim.

## Corrections & caveats

- This reel compresses a multi-week brainstorming report into a ~90s overview. The seven
  candidate RL-calibration reward designs in source §3.1 are not all covered; the reel
  follows the source's own emphasis (§3.2 "Deep Dive," §5 "Next Steps") in foregrounding
  Idea 1 (proper scoring rule) as the one actually scheduled for implementation.
- "Lending" (B03) is an illustrative analogy added for a general audience, not a claim
  attributed to the source document, which only worked the triage example.
- No external sources were checked — every claim traces to the user's own internal project
  report, not a public/third-party claim requiring independent verification.
