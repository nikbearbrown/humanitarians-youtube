# SCRIPT — Causal Memory in Pi. (claude-liam-pi-causal-memory)

**Channel:** `@NikBearBrown`  
**Voice:** Kokoro `am_onyx` (Liam, in for Kriti)  
**Total Timeline:** 104.9s (12 beats)  
**Format:** 16:9 Landscape (`pi-agent-causal-memory.mp4`) & 9:16 Portrait (`vertical/`)

---

### B00 — ASK / Cold Open (`ClaudeComposerAsk` · 6.33s)
- **Show:** Claude desktop composer displays `Hello, Kriti` above prompt in cream and warm ink; topic `PI MEMORY · CAUSAL MEMORY`, segment `Causal Memory in Pi.`; running indicator pulses with *"reading the causal memory notes…"*; three summary takeaways cascade into view:
  1. *Stores rules learned from failures: condition, action, outcome, mechanism*
  2. *Checks every proposed tool call in the beforeToolCall hook*
  3. *Blocks matches and explains why, so the model picks another way*
- **Narration:** "Hello, this is Liam, in for Kriti, explaining how causal memory works in Pi."

---

### B01 — BLUF / Executive Summary (`BrutalistHesitantWriter` · 9.5s)
- **Show:** Hesitant writer types *"Causal memory makes Pi smarter."* in EB Garamond; *"makes Pi smarter"* highlights in terracotta, strikes through, deletes, and retypes as *"is a safety layer"*; line 2 types on.
- **Narration:** "Causal memory is a safety layer: it remembers why past actions failed, and stops Pi from repeating them before they run."

---

### B02 — WHAT IT KEEPS / Five Slot Tuple (`UpdConceptGrid` · 8.51s)
- **Show:** Five rule component slots land onto the canvas sequentially: Condition, Action, Outcome, Mechanism, and Mitigation; descriptive prompt labels appear under each slot.
- **Narration:** "From each failure, Pi keeps a causal rule: the condition, the action, the outcome, the mechanism behind it, and a way to avoid it."

---

### B03 — RULE SHAPE / Causal Schema (`UpdRule` · 7.61s)
- **Show:** Formal causal schema structure builds step by step: IF condition C · AND action A · → outcome O · BECAUSE mechanism M.
- **Narration:** "Every rule has the same shape: if condition C and action A, then outcome O, because of mechanism M."

---

### B04 — WORKED EXAMPLE / Uncommitted Git Reset (`UpdScorecard` · 11.82s)
- **Show:** Structured worked example displays:
  - *IF:* Uncommitted local changes exist
  - *AND:* `git reset --hard` is executed
  - *→:* Working changes are permanently lost
  - *BECAUSE:* Hard reset discards uncommitted working tree state
  - *MITIGATION:* Stash or commit changes first
- **Narration:** "Here's an example. If there are uncommitted changes and the action is git reset hard, those changes are lost, because reset throws away uncommitted work. The fix: stash or commit first."

---

### B05 — INTEGRATION SEAM / BeforeToolCall Hook (`UpdFlow` · 8.91s)
- **Show:** Architecture flow diagram displays proposed tool action passing directly into `beforeToolCall` hook in `packages/agent/src/agent-loop.ts` before reaching execution.
- **Narration:** "In Pi, these rules live in the beforeToolCall hook in agent-loop.ts, which every proposed tool call passes through before it runs."

---

### B06 — INTERCEPTION / Pattern Matching (`UpdMatch` · 9.58s)
- **Show:** Proposed action card evaluates against known failure rules; rule 2 flags a positive match on uncommitted working tree and `git reset --hard`.
- **Narration:** "Each proposed action is checked against the known failure conditions. Here, the agent wants to reset hard with uncommitted changes. That's a match."

---

### B07 — INTERVENTION / Block and Explain (`UpdBlock` · 6.99s)
- **Show:** Middleware stamps proposed tool call as `BLOCKED` in terracotta; constructs and returns structured causal explanation card to model context.
- **Narration:** "So the middleware blocks the call and sends the model a causal explanation: what would happen, and why."

---

### B08 — RECONSIDERATION / Adaptive Recovery (`UpdFlow` · 6.29s)
- **Show:** Model receives explanation of consequence, suppresses forbidden call, and emits alternative mitigation proposal (`git stash`).
- **Narration:** "The model reconsiders, and picks a safer strategy, like stashing the changes first."

---

### B09 — VERDICT / Teardown Judgment (`PiVerdict` · 8.56s)
- **Show:** Full verdict card titled *"Causal Memory in Pi."* with heading *"Causal memory, in three lines"*:
  1. *Rules from failures: condition, action, outcome, mechanism, mitigation.*
  2. *Checked in beforeToolCall, before every tool runs.*
  3. *Reactive: it prevents known failures, not new ones.*
- **Narration:** "The verdict: causal memory is a reactive safety layer. Strong against failures it has seen, and blind to the ones it hasn't."

---

### B10 — YOUR TURN / Viewer Handoff (`ClaudeComposerAsk` · 14.64s)
- **Show:** Claude desktop composer opens with greeting *"Your turn."* and viewer prompt: *"Here's a mistake my coding agent made: [describe it]. Write it as a causal rule: IF condition AND action, then outcome, BECAUSE mechanism, plus a mitigation."* Running indicator reads *"paste this into Claude…"*.
- **Narration:** "Your turn: 'Here's a mistake my coding agent made. Write it as a causal rule: if condition and action, then outcome, because mechanism, plus a mitigation.' Writing the mechanism is the hard part, and that's exactly what makes the rule useful."

---

### B11 — OUTRO (`ClaudeTitleOutro` · 4.29s)
- **Show:** Title restate card *"Causal Memory in Pi."* in EB Garamond with `@NikBearBrown` channel chip.
- **Narration:** "Causal Memory in Pi. At Nik Bear Brown."
