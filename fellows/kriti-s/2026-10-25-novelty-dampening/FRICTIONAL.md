# Frictional Log — novelty-dampening

## 2026-10-25 — Build Explainer Video on Novelty Dampening in 16:9 and 9:16 format

Drafted by Optimus(AI) from videos folders and reviewed by me.

- **Work and expectation:** In the scenario, I review and verify the novelty dampening explainer, expecting its core premise—that repetitive memory recall can be resolved via logarithmic access penalties without deleting core memories—to be intuitively demonstrated and verifiable within ~60 seconds.
- **What I try:** Present the retrieval trap of naive cosine similarity, illustrate memory crowding-out by generic episodes, formulate the novelty dampening equation ($\text{Sim}(q, m) / [1 + \alpha \log(1 + N_{\text{access}}(m))]$), calibrate $\alpha = 0.15$, demonstrate how long-tail memories surface, and confirm that no memories are permanently excluded.
- **Where it resists, and what I do next:** 
  - *Mathematical Formula Rendering:* Rendering math fractions and logarithms cleanly within Remotion components without kerning collisions or visual overlap across widescreen (16:9) and portrait (9:16) layouts.
  - *Alpha Calibration Sensitivity:* Explaining why linear penalties cause ranking thrashing, whereas logarithmic scaling ($\ln(1 + N)$) provides stable, sub-linear degradation that preserves highly relevant episodes under extreme query similarity.
  - *Visualizing Rank Inversion:* Creating animated bar charts showing how top-ranked generic episodes slide down while specialized secondary candidates elevate into top-$k$ positions.
- **AI and other contributions:** Claude Code compiled the 12-beat sheet, generated Remotion scenes, validated factcheck claims against mathematical definitions and retrieval logs, and executed the video build pipeline. Audio voiced via Kokoro `am_onyx` (Liam in for Kriti). Human fellow formulated the dampening equation, calibrated $\alpha = 0.15$, audited retrieval entropy metrics, and approved the review cut.
- **What I understand:** Vector databases and dense embeddings are for retrieval. When an agent repeats mistakes, the flaw is often retrieval monopolization rather than representation failure. Soft access friction restores diversity without destroying historical knowledge.
- **Evidence:** [beat_sheet.json](beat_sheet.json)
