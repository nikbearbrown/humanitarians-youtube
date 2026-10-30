# Frictional Log


## 2026-10-18 — Week 4 Entry

**Record provenance:** Reflecting on the Week 4 online harvesting, in-flight backtracking, and trajectory benchmarking update

- **Work and expectation:** In the scenario, I review and verify the Week 4 engineering update, expecting the technical milestones—in-flight backtrack tracking, online autonomous harvesting of pivot step $k^*$, and empirical validation across 40 OpenHands trajectories and 200 held-out defects—to be clearly synthesized within ~60 seconds.
- **What I try:** Implement Pi subsystem hooks across `before_agent_turn`, `after_tool_call`, and `on_session_settled`; capture live tool errors dynamically via in-flight backtrack buffers; autonomously extract contrastive pairs from divergent pivot steps ($k^*$) without synthetic staging; prove complexity reduction from $O(b^d)$ to $O(d)$ through negative action pruning; and benchmark on 40 trajectories and 200 SWE-rebench defects across 3 arms under strict anti-leakage guards.
- **Where it resists:** 
  - *Unpopulated Backtrack History:* The agent runtime initially left `backtrackHistory` unpopulated during multi-turn runs; solved by engineering dynamic capture inside `after_tool_call` to log command failures and non-zero exit codes in real-time.
  - *Synthetic Staging vs. Real Trajectories:* Resisting artificial dual-session mockups; built true online autonomous harvesting that partitions unseeded multi-turn tool sessions into failed and successful forks.
  - *Efficiency vs. Reasoning Gap:* Transparently confronting the benchmark reality that 100% trap avoidance, 59.4% latency drop, and 62.5% token reduction yielded no statistically significant Pass@1 gain (30.0% vs 33.0%, $p=0.48$).
  - *Anti-Leakage Safeguards:* Enforcing strict isolation via `ReadOnlyMemoryProxy` to prevent evaluation contamination across repository splits.
- **What I do next:** Investigate multi-phase memory applicability filtering and novelty dampening to prevent template collapse, resolve the anomalous 100% Pass@1 leakage signal, and conduct clean E1–E7 ablation studies in Week 5.
- **AI and other contributions:** Claude Code compiled the beat sheet, configured Remotion scene flows (`ClaudeComposerAsk`, `ClaudeTitleOutro`), verified metrics against `report.md`, and executed the Brutalist build pipeline. Audio voiced via Kokoro `am_onyx` (Liam in for Kriti). Human fellow directed the in-flight backtrack buffer implementation, formalized the counterfactual divergence math, curated the 20/20 trajectory split, configured anti-leakage shields in `swe-rigrous-eval`, and approved the review cut.
- **What I understand:** Backtracking buffers, hook managers, and prompt injectors are operational equipment. Cutting latency and avoiding known failure loops does not inherently generate correct code. 
- **Evidence:** [beat_sheet.json](beat_sheet.json), [report.md](report.md), [weekly_hours.md](weekly_hours.md)