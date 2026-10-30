# Frictional Log

## 2026-10-25 — Week 5 Entry

**Record provenance:** Reflecting on the Week 5 ablation matrix, leakage audit, and Carry the Couch update. 

- **Work and expectation:** In the scenario, I review and verify the Week 5 ablation findings, expecting the complete E1–E7 ablation progression (climbing from 6.5% to 63.0% on 200 tasks), the leakage resolution, and the handoff to Carry the Couch modules to be rigorously and concisely conveyed within ~60 seconds.
- **What I try:** Investigate and eliminate test patch leakage in the evaluation harness; evaluate the clean E1–E7 ablation matrix on 200 defect tasks; implement 5-phase applicability filtering (Planning, Editing, Testing, Recovery, Verification); apply novelty dampening via access-count penalties to prevent template collapse; test selective interception (hard constraints vs. soft recommendations); formalize paired statistical significance via McNemar's test; and initialize Carry the Couch embodied agent modules under a strict 1,000-token budget ceiling.
- **Where it resists:** 
  - *Evaluation Leakage Investigation:* Uncovering an anomalous 100% Pass@1 signal caused by test patch solutions lingering in runtime context; enforced absolute physical separation between evaluation ground-truth and agent runtime environments.
  - *Template Collapse & Over-Reliance:* Agents repeatedly retrieved and over-applied high-frequency memory patterns; engineered a novelty dampening formula ($S_{\text{final}} = S_{\text{retrieval}} \cdot \exp(-\lambda \cdot N_{\text{access}})$) to penalize over-accessed traces and force exploration.
  - *Isolating Memory vs. Upstream Reasoning Lift:* In-memory enhancements (E2–E6) improved Pass@1 incrementally from 6.5% to 34.5%, but the decisive breakthrough (63.0% in E7) stemmed from upstream fault-localization branching and scoped Best-of-N patch generation, confirming that memory cannot compensate for misidentified fault locations.
- **AI and other contributions:** Claude Code compiled the beat sheet, built custom Remotion scenes (`ClaudeComposerAsk`, `ClaudeTitleOutro`), validated ablation metrics against test outputs, and executed the review cut build. Audio voiced via Kokoro `am_onyx` (persona: Kriti). Human fellow investigated the 100% leakage anomaly, designed the 5-phase applicability filter and novelty dampening formula, executed the E1–E7 ablation runs, formalized McNemar's test, and initiated Carry the Couch module design.
- **What I understand:**  Ablation frameworks, token budget enforcers, and paired tests are measurement equipment; a 100% Pass@1 metric produced by test-patch leakage is artifactual delusion. True knowledge requires clean ablation isolation and recognizing that memory retrieval operates downstream of upstream fault localization.
- **Evidence:** [beat_sheet.json](beat_sheet.json), [report.md](report.md), [weekly_hours.md](weekly_hours.md)
