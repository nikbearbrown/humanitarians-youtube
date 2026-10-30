# Week 5: Pi Memory Ablations (E1–E7), Leakage Audits, and Carry the Couch Modules

**Group:** RL Environment · **Reporting week:** 2026-10-19 through 2026-10-25

## Executive Summary

The week centered on comprehensive empirical ablation testing across 200 software defect tasks to isolate memory components and eliminate evaluation contamination. Following an investigation of an anomalous 100% Pass@1 signal that traced to ground-truth patch leakage, strict runtime isolation was established. The resulting clean ablation matrix demonstrated progressive architectural gains across seven experiments: baseline E1 (6.5%), episode quality guard E2 (30.0%), multi-phase applicability filtering across five execution phases (planning, code editing, test execution, recovery, verification) with novelty dampening access penalties E3 (32.5%), phase-aware retrieval with fixed token budgets E4 (29.0%), selective interception splitting hard constraints from soft recommendations E5 (33.5%), combined CEM-v2 E6 (34.5%), and upstream fault-localization branching with scoped Best-of-N patch generation and contrastive verification E7 (63.0%). McNemar's paired test confirmed overwhelming statistical significance for E7 over E6 ($p = 1.57 \times 10^{-11}$). The groundwork was established for the Carry the Couch embodied robotics modules (environment setup, Body Design Module, and a 1,000-token budget ceiling).

## Evidence — Open Directly

- [Adapted beat sheet (12 beats)](beat_sheet.json).
- [Frictional log](Frictional.md).
- [Weekly hours](weekly_hours.md).
- [Explainer video](https://drive.google.com/file/d/1pkT49De-_GHOBI-F6t6xB9HxS_LeuFn1/view?usp=drive_link).
- [Progress video](https://drive.google.com/file/d/1JIj6hXEDv8WmXZKlges4AIuMUXBfKcXT/view?usp=drive_link).

## Attribution and Contribution

Original sources: SWE-bench defects (N=200 held-out tasks); frozen GLM 5.3 Flash model. Work by Kriti S.: weekly results structured into a 12-beat update, and narration script written, then voiced via Kokoro am_onyx (speaking as Kriti). Research and review by Kriti S.: specifying the 4-point improvement plan (applicability filtering, five-phase retrieval, hard constraints vs. soft recommendations), formalizing novelty dampening ($\alpha = 0.15$), diagnosing the 100% Pass@1 anomaly as test-patch leakage and rebuilding oracle boundaries, running the clean E1–E7 ablation matrix with McNemar's paired test, and specifying the Carry the Couch setup, Body Design, and Budget modules.

## Folder Contents

- README.md: result and evidence status
- report.md: comprehensive technical report, ablation matrix, and statistical protocol.
- beat_sheet.json: 12-beat weekly update production plan and cues.
- Frictional.md: process reflection and engineering friction log.
- weekly_hours.md: 20-hour weekly task breakdown and evidence index.
