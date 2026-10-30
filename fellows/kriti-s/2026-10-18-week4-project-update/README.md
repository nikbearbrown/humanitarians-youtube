# Week 4: Pi Agent Autonomous Harvesting, In-Flight Backtracking, and Trajectory Benchmarking

**Group:** RL Environment· **Reporting week:** 2026-10-11 through 2026-10-18

## Executive Summary

The week delivered the mathematical formalization of counterfactual divergence ($\tau^+ / \tau^-$, pivot step $k^*$, dynamic lesson tuples $\mathcal{L}$), implemented Pi subsystem hooks (`pi_hook_manager.py`, `context_injector.py`, `contrastive_harvester.py`) with dynamic in-flight backtrack buffers, and replaced synthetic staging with true online autonomous harvesting. Empirical validation on 40 authentic OpenHands repository trajectories (20/20 train/eval split, zero data overlap) and 3-arm benchmarking across N=200 held-out software defects in `swe-rigrous-eval` demonstrated a 100% Trap Avoidance Rate (TAR), cutting task latency by 59.4% and completion tokens by 62.5% ($0.05/task cost). However, Pass@1 remained flat at 30.0% vs. 33.0% for Flat RAG ($p=0.48$), confirming that while execution efficiency and loop avoidance were solved, reasoning lift remained an open challenge.

## Evidence — Open Directly

- [Adapted beat sheet (12 beats)](beat_sheet.json).
- [Frictional log](Frictional.md).
- [Weekly hours](weekly_hours.md).
- [Explainer video](https://drive.google.com/file/d/1UWG-Oooucq-0SzXrK1-eoyOKRRNpSYaq/view?usp=drive_link).
- [Progress video](https://drive.google.com/file/d/1BySmRrefx7ZTTlI1L5-ANm53kYXNf29t/view?usp=drive_link).

## Attribution and Contribution

Original sources: `nebius/SWE-rebench-openhands-trajectories` (40 OpenHands agent trajectories); frozen GLM 5.3 Flash model. Work by Kriti S.: weekly results structured into a 12-beat update, and narration script written, then voiced via Kokoro am_onyx (Liam in for Kriti). Research and review by Kriti S.: diagnosing the empty `backtrackHistory` gap, building the Pi subsystem hooks (`pi_hook_manager.py`, `context_injector.py`, `contrastive_harvester.py`) with in-flight backtrack buffers, replacing synthetic forks with online autonomous harvesting, building the 20/20 train/eval task split with zero-leakage checks, and running the 3-arm `swe_rigorous_eval` benchmark across N=200 held-out defects.

## Folder Contents

- README.md: result and evidence status
- report.md: comprehensive technical report, architecture manifest, and execution guide.
- beat_sheet.json: 12-beat weekly update production plan and cues.
- Frictional.md: process reflection and engineering friction log.
- weekly_hours.md: 20-hour weekly task breakdown and evidence index.
