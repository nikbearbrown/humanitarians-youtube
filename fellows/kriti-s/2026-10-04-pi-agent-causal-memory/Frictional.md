# Frictional Log — pi-causal-memory

## 2026-10-03 — Build Explainer Video on Pi Causal Memory in 16:9 and 9:16 format

Drafted by Optimus(AI) from videos folders and reviewed by me.

- **Work and expectation:** In the scenario, I review and verify the causal memory explainer and expect its primary distinction that causal memory acts as a bounded reactive safety gate in `beforeToolCall` rather than general intelligence to be clear to a newcomer in ~105 seconds.
- **What I try:** Formalize the five slot causal tuple (condition, action, outcome, mechanism, mitigation), show how rules plug into Pi's `beforeToolCall` hook in `agent-loop.ts`, and demonstrate the complete block and explain recovery cycle using an uncommitted git reset failure.
- **Where it resists, and what I do next::** 
  - *Audio Pacing:* The Remotion compiler required strict duration matching ($\pm 0.15$s), necessitating baked audio holds and lead silences across all 12 beats.
  - *Vertical Typography:* In the 9:16 portrait cut, Gate T §8.1 font floor exceptions were flagged on secondary rule labels and stock outro elements, noted for review prior to final master cut.
- **AI and other contributions:** Claude Code compiled the beat sheet, created custom Remotion compositions (`UpdRule`, `UpdMatch`, `UpdBlock`), verified claims against `SOURCES.md`, and executed the video pipeline. Audio voiced via Kokoro `am_onyx`. Human fellow defined the causal rule tuple, designed the recovery interaction flow, and verified technical alignment.
- **What I understand:** Causal memory rules in `beforeToolCall` are protective equipment and writing the underlying mechanism is the difficult analytical work that turns raw failure logs into actionable decision constraints.
- **Still unresolved:** Resolving vertical Gate T font floor exceptions before final master rendering; benchmarking pattern-matching overhead in `beforeToolCall`
- **Evidence:** [beat_sheet.json](beat_sheet.json)