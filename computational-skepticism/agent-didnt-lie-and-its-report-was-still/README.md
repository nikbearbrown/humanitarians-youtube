# The Agent Didn't Lie — and Its Report Was Still False

An autonomous AI agent reports: "The secret has been deleted." Every single tool call succeeded without error. The agent did not hallucinate, fabricate, or lie. Yet when the user inspects the cloud provider, the secret message is still sitting in the mailbox — completely accessible.

How can an agent's report be 100% faithful and yet completely false?

The failure is a language-game scope mismatch. In the agent's local language game, the word "deleted" names the sequence of operations within its effective operational scope: resetting a local alias, wiping a local client cache, or archiving a record. In that local scope, the report was true. In the user's language game, "deleted" names real-world data eradication: zero copies on provider servers, cleared backups, and irreversible removal. The agent's report committed to its local game without naming the boundary, allowing an honest local action to masquerade as global task completion.

In this episode of *Computational Skepticism for AI*, Liam (in for Professor Bear) breaks down the language-game trap in model explainability: why attribution checks miss semantic boundaries, and why supervisory systems must ask the audience question before trusting a completion report.

---

### Key Takeaways & Carry-Out
- **The Language-Game Mismatch**: The same word ("deleted", "completed", "verified") names different operations in different scopes. An agent's report can describe local state consistency while leaving external reality unchanged.
- **The Unflagged Boundary Gap**: Explanations that are mathematically faithful to local execution can still be actively misleading when delivered across operational boundaries without explicit scoping.
- **The Audience Question**: Supervisory validation cannot merely check tool logs. It must ask: *"Who is reading this report, and what does this word mean in their language game?"*
- **Carry-Out Law**: "An agent's report can be entirely faithful to its own scope and still false in yours — because the same word names a local action to the machine and a real-world state to you."
- **Direction A (Local Faithful ⇏ Global Success)**: 100% faithful tool execution does not prove task completion in the real world.
- **Direction B (Cloud Persistence ⇏ Deception)**: Finding data persistent on the server does not prove the agent lied or hallucinated; it proves a local claim was mistaken for a global guarantee.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take an autonomous agent workflow in your stack that reports task completion. Identify the verbs in its final report — like deleted, updated, or verified. For each verb, define what it proves inside the agent's local environment, and what a human user assumes it proves in the cloud. Where is the unflagged gap?
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Explainability & Interpretability
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 5: Model Explainability: Distinguishing Explanation from the Appearance of Explanation)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **AI Disclosure**: Synthetic narration generated locally via Kokoro `am_onyx`. Visuals algorithmically rendered via Manim and Remotion. Zero generative video, zero paid APIs.
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/agent-didnt-lie-and-its-report-was-still
