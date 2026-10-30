# Week 5: Novelty Dampening in Agent Memory — Diversity Without Deletion

**Group:** RL Environment · **Reporting week:** 2026-10-19 through 2026-10-25

## Executive Summary

This report covers the production and delivery of a dual-format explainer video (16:9 widescreen and 9:16 portrait) investigating the retrieval monopolization trap in agent memory systems, where standard cosine similarity repeatedly recalls generic episodes and crowds out specialized task solutions. To restore retrieval diversity without destructive pruning, the architecture introduces **Novelty Dampening**, a dynamic stateful penalty mechanism formulated as:
$$\text{Score}_{\text{dampened}}(m) = \frac{\text{Sim}(q, m)}{1 + \alpha \log(1 + N_{\text{access}}(m))}$$
With hyperparameter $\alpha = 0.15$, the logarithmic penalty applies gentle friction to initial recalls while progressively dampening chronic high-frequency hits. Crucially, useful memories are never deleted—their bar to surface simply rises—naturally exposing relevant long-tail episodes, increasing retrieval entropy, and preventing repetitive failure loops. Produced through human research direction and AI-assisted Remotion video generation voiced by Kokoro `am_onyx` (Liam in for Kriti). The film is credited to original production.

## Evidence — Open Directly

- [Adapted beat sheet (12 beats)](beat_sheet.json).
- [Frictional log](Frictional.md).
- [Explainer video](https://drive.google.com/file/d/1pkT49De-_GHOBI-F6t6xB9HxS_LeuFn1/view?usp=drive_link).
- [Progress video](https://drive.google.com/file/d/1JIj6hXEDv8WmXZKlges4AIuMUXBfKcXT/view?usp=drive_link).

## Attribution and Contribution

Work by Kriti S.: technical mechanism structured into a 12-beat teardown (`claude-liam-novelty-dampening`), custom Remotion scenes constructed (`ClaudeComposerAsk`, `ClaudeTitleOutro`, logarithmic decay curve animations, rank-shift distribution tables), and narration script written, then voiced via Kokoro `am_onyx` (Liam in for Kriti). Research and review by Kriti S.: mathematical formulation of the dampening equation, tuning the $\alpha = 0.15$ penalty parameter, verifying the non-destructive retention guarantee, and approving the video review cut.

## Folder Contents

- README.md: result, evidence status, and attribution.
- beat_sheet.json: 12-beat novelty dampening production plan and cues.
- Frictional.md: process reflection and build friction log.
