# Week 2: Pinned Baseline, Persistent Logging, and Scoping Six Memory Designs (Pi Memory) — Beat Sheet

**Slug:** `claude-liam-pi-memory-week-two` · **Persona:** Kriti (voiced by Kokoro am_onyx) · **Voice:** Kokoro `am_onyx`

Generated from [`beat_sheet.json`](beat_sheet.json), which is the source of truth: edit the JSON, not this table. Start times add up each beat's rendered duration.

## 11 beats, 1:40 (100.2s)

| # | Act | Start | Dur | Pattern | Motion | Narration |
|---|---|---|---|---|---|---|
| B00 | cold open | 0:00 | 6.8s | ClaudeComposerAsk |  | Hello, this is Kriti, sharing the weekly update on evaluating memory architectures for Pi. |
| B01 | overview (BLUF) | 0:07 | 9.5s | BrutalistHesitantWriter |  | Week two built a solid baseline: Pi pinned, every run logged, and six memory designs scoped for testing. |
| B02 | body — pinned baseline | 0:16 | 9.8s | UpdPin |  | First, the baseline. I pinned Pi to one specific version from its GitHub repository, so every run uses exactly the same harness. |
| B03 | body — Optimus code | 0:26 | 9.2s | UpdFlow |  | Then I read through the model config and arm0_runner files that Optimus generated, to understand how a run is wired together. |
| B04 | body — runner change | 0:35 | 9.6s | UpdKeep |  | The runner used to write to temporary folders. I changed it to save to permanent directories, so every log is kept and every run can be audited. |
| B05 | body — check-in | 0:45 | 6.0s | UpdChecklist |  | I met with the team and the lead to review progress and agree on next steps. |
| B06 | body — episodic scoped | 0:51 | 13.2s | UpdConceptGrid |  | Then I scoped three episodic designs: contrastive memory that keeps failures next to successes, a milestone graph that recalls only the current phase, and closed-loop retrieval that drops memories that don't help. |
| B07 | body — causal scoped | 1:04 | 14.5s | UpdScorecard |  | And three causal designs: a dependency graph that traces an error to its root cause, intervention memory that suggests a better action instead of just blocking one, and a failure-repair graph that turns a failed run into a repair plan. |
| B09 | verdict | 1:19 | 4.1s | PiVerdict |  | Week two: pinned, logged, and scoped. |
| B10 | your turn handoff | 1:23 | 13.2s | ClaudeComposerAsk |  | Your turn: 'Review my agent experiment runner. What should every run log so the results can be audited and reproduced later?' A result you can't trace is a result you can't trust, so that's the question worth asking early. |
| B11 | outro | 1:36 | 4.2s | ClaudeTitleOutro |  | Pi Memory, Week Two. At Nik Bear Brown. |
