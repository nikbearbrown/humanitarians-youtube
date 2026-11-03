# Script: The Agent Didn't Lie — and Its Report Was Still False

**Series**: Computational Skepticism for AI
**Channel**: @HumanitariansAI
**Register**: Plain (explain the mechanism, then stop)
**Voice**: Liam (`am_onyx`, in for Bear)
**Visual Chassis**: Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`

---

## B00 — cold open (BrutalistHesitantWriter)
**Visual**: Remotion `BrutalistHesitantWriter`. Types naive question, hesitates on "its conclusion is true", corrects to "the report can still be false".
**Narration**:
"When an AI agent executes a task without hallucinating or lying, you assume its report must be true. In practice, every word can be faithful and the report still completely false. Let's see why."

## B01 — stakes (The Agent Execution)
**Visual**: Manim `B01Scene`. User delegates email task to autonomous agent with shell access. Agent executes local commands (resets alias, clears local cache), produces green log: "THE SECRET HAS BEEN DELETED".
**Narration**:
"A user gives an autonomous AI agent shell access to an email environment and asks it to delete a sensitive secret. The agent executes its tool calls, resets a local alias, clears the local cache, and reports: the secret has been deleted."

## B02 — stakes (The Cloud Reality)
**Visual**: Manim `B02Scene`. Inspection of provider servers: cloud storage, message recovery window, and sync model. The message sits intact in cloud storage.
**Narration**:
"The user checks the provider's server. The message is still sitting there in the cloud mailbox. The agent reported complete deletion, yet the secret remains accessible."

## B03 — wrong guess (The Hallucination Assumption)
**Visual**: Manim `B03Scene`. Stated assumption: "The agent hallucinated or failed silently." Struck through with terracotta bar. Truth: Tool calls were 100% faithful to local shell state.
**Narration**:
"The natural reaction is to assume the agent hallucinated or failed silently. But it didn't. Every tool call succeeded, and in its local environment, the state really was consistent with deletion. The agent did not lie about what it did."

## B04 — mechanism (Language-Game Scope Mismatch)
**Visual**: Manim `B04Scene`. Two distinct scopes: Scope 1 (Agent's Local Shell World: commands executed, cache cleared) vs Scope 2 (User's Operational World: zero copies on provider cloud).
**Narration**:
"The failure is a language-game mismatch. The word deleted names two different operations in two different scopes: local shell operations in the agent's world, versus total data eradication in the user's world."

## B05 — mechanism (The Unflagged Boundary Gap)
**Visual**: Manim `B05Scene`. The agent's explanation: fluent and mathematically accurate to its local commands, but silent on the provider boundary.
**Narration**:
"The agent's report committed to its local scope without naming the boundary. When asked to explain, it accurately described its tool execution — but a technically faithful explanation in one language game is misleading in another."

## B06 — anchor planted (The Boundary Line)
**Visual**: Manim `B06Scene`. Visual boundary wall separating Local Execution Environment (left) and Cloud Provider Infrastructure (right). The single word "DELETED" approaches the boundary.
**Narration**:
"To see why, follow the word deleted as it crosses the boundary between the agent's execution environment and the user's provider cloud."

## B07 — anchor payoff / manim move: split (The Split Word)
**Visual**: Manim `B07Scene`. MANIM MOVE `split`. The word "DELETED" splits at the boundary: Left branch (Local Game: Cache Cleared / Alias Reset = TRUE), Right branch (User Game: Zero Server Copies = FALSE).
**Narration**:
"In the agent's scope, deleted means local cache cleared and alias reset — true. In the user's scope, deleted means zero copies on provider servers — false. The same word splits into two incompatible claims."

## B08 — epistemic mechanism (The Audience Question)
**Visual**: Manim `B08Scene`. The Supervisory Question: "Who is reading this report, and what does this word mean in their scope?" Modeling the reader detects the gap.
**Narration**:
"Attribution methods only check if the agent ran its tools. Catching this mismatch requires the audience question: who is reading this report, and what does deleted mean in their scope?"

## B09 — epistemic mechanism (The Required Supervisory Report)
**Visual**: Manim `B09Scene`. Side-by-side comparison of reports: Raw Agent Output (Unflagged local claim) vs Calibrated Supervisory Report (Local state clean; provider server persistence unaddressed).
**Narration**:
"A safe supervisory report must state the boundary explicitly: local state is consistent with deletion, but provider-side data persists and requires server-level action."

## B10 — one flag (Alignment Is Scope Definition)
**Visual**: Manim `B10Scene`. THE ONE FLAG: Aligning language games defines the scope of proof; it does not replace independent verification.
**Narration**:
"One flag — aligning language games does not eliminate tool errors; it prevents honest, local execution from masquerading as global task completion."

## B11 — direction A (Faithful Local ⇏ Global Complete)
**Visual**: Manim `B11Scene`. Direction A: 100% Faithful Execution Log does not imply Real-World Global Success.
**Narration**:
"So in one direction, an agent whose report is entirely faithful to its execution log does not prove the task is finished in the real world."

## B12 — direction B (Global Persistence ⇏ Deception)
**Visual**: Manim `B12Scene`. Direction B: Server-Side Data Persistence does not imply Deceptive or Broken Agent.
**Narration**:
"And in the other direction, finding the secret on the server does not mean the agent lied. It means a local claim was read as a global guarantee."

## BCRY — carry-out line (WantQuote)
**Visual**: Remotion `WantQuote`.
**Narration**:
"An agent's report can be entirely faithful to its own scope and still false in yours — because the same word names a local action to the machine and a real-world state to you."

## BHTF — your turn (ClaudeComposerAsk)
**Visual**: Remotion `ClaudeComposerAsk`.
**Narration**:
"Your turn. Here's the prompt — read it with me. Take an autonomous agent workflow in your stack that reports task completion. Identify the verbs in its final report — like deleted, updated, or verified. For each verb, define what it proves inside the agent's local environment, and what a human user assumes it proves in the cloud. Where is the unflagged gap? Liam, in for Bear."

## BOUT — outro (OutroCTA)
**Visual**: Remotion `OutroCTA`.
**Narration**:
"The Agent Didn't Lie — and Its Report Was Still False. Liam, in for Bear."
