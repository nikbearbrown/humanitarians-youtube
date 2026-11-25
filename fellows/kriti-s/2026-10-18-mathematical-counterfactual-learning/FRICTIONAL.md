# Frictional Log — counterfactual-learning


## 2026-10-16 — Build Explainer Video on Mathematical Counterfactual Learning in 16:9 and 9:16 format

Drafted by Optimus(AI) from videos folders and reviewed by me 

- **Work and expectation:** In the scenario, I review and verify the mathematical architecture of counterfactual agent learning and expect its foundational proofs—trajectory pairing, prefix invariance, divergence index $k^*$, and lesson tuple synthesis to be clear and verifiable within ~68 seconds.
- **What I try:** Formalize state-action sequences $\tau$, binary outcome verification $V(\tau)$, sequence prefix equivalence $\forall j < k^*$, divergence detection across (hypothesis, tool, arguments), and synthesis of the dual constraint $\langle \mathcal{W}_{\text{invariant}}, \mathcal{P}_{\text{prescription}} \rangle$.
- **Where it resists:** 
  - *Mathematical Notation in Video:* Rendering mathematical subscripts, superscripts, and Greek letters cleanly within Remotion components without visual clipping or font kerning artifacts.
  - *Outro Pattern Compliance:* The review cut flagged an outro warning (B11 palette styling vs. stock outro conventions), requiring alignment with the Brutalist OUTRO LAW before final release.
  - *Credit Assignment Precision:* Ensuring the explanation clearly bounds blame to post-divergence steps, preventing the model from falsely attributing downstream failures to valid early steps.
- **AI and other contributions:** Claude Code compiled the beat sheet, constructed custom presentation layouts (`FormBCard`, `CwcConceptCard`), verified mathematical definitions against causal literature, and executed the Brutalist video build pipeline. Audio voiced via Kokoro `am_onyx` (Liam in for Kriti). Human fellow authored the mathematical formalisms, designed the lesson schema, and approved the review cut.
- **What I understand:** Understanding causal counterfactual mechanics is the knowledge required to transform errors into durable architectural guardrails.
- **Evidence:** [beat_sheet.json](beat_sheet.json)
