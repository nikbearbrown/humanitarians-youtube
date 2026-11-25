# Causal Memory and Prevention Layers (Pi Memory) — Beat Sheet

**Slug:** `claude-liam-pi-causal-memory` · **Persona:** Liam (in for Kriti) · **Voice:** Kokoro `am_onyx`

Generated from [`beat_sheet.json`](beat_sheet.json), which is the source of truth: edit the JSON, not this table. Start times add up each beat's rendered duration.

## 12 beats, 1:43 (103.2s)

| # | Act | Start | Dur | Pattern | Motion | Narration |
|---|---|---|---|---|---|---|
| B00 | cold open | 0:00 | 6.3s | ClaudeComposerAsk |  | Hello, this is Liam, in for Kriti, explaining how causal memory works in Pi. |
| B01 | overview (BLUF) | 0:06 | 9.5s | BrutalistHesitantWriter |  | Causal memory is a safety layer: it remembers why past actions failed, and stops Pi from repeating them before they run. |
| B02 | body — what it keeps | 0:16 | 8.5s | UpdConceptGrid |  | From each failure, Pi keeps a causal rule: the condition, the action, the outcome, the mechanism behind it, and a way to avoid it. |
| B03 | body — rule shape | 0:24 | 7.6s | UpdRule |  | Every rule has the same shape: if condition C and action A, then outcome O, because of mechanism M. |
| B04 | body — example | 0:32 | 11.8s | UpdScorecard |  | Here's an example. If there are uncommitted changes and the action is git reset hard, those changes are lost, because reset throws away uncommitted work. The fix: stash or commit first. |
| B05 | body — where it lives | 0:44 | 8.9s | UpdFlow |  | In Pi, these rules live in the beforeToolCall hook in agent-loop.ts, which every proposed tool call passes through before it runs. |
| B06 | body — the check | 0:53 | 9.6s | UpdMatch |  | Each proposed action is checked against the known failure conditions. Here, the agent wants to reset hard with uncommitted changes. That's a match. |
| B07 | body — block + explain | 1:02 | 7.0s | UpdBlock |  | So the middleware blocks the call and sends the model a causal explanation: what would happen, and why. |
| B08 | body — reconsider | 1:09 | 6.3s | UpdFlow |  | The model reconsiders, and picks a safer strategy, like stashing the changes first. |
| B09 | verdict | 1:16 | 8.6s | PiVerdict |  | The verdict: causal memory is a reactive safety layer. Strong against failures it has seen, and blind to the ones it hasn't. |
| B10 | your turn handoff | 1:24 | 14.7s | ClaudeComposerAsk |  | Your turn: 'Here's a mistake my coding agent made. Write it as a causal rule: if condition and action, then outcome, because mechanism, plus a mitigation.' Writing the mechanism is the hard part, and that's exactly what makes the rule useful. |
| B11 | outro | 1:39 | 4.3s | ClaudeTitleOutro |  | Causal Memory in Pi. At Nik Bear Brown. |
