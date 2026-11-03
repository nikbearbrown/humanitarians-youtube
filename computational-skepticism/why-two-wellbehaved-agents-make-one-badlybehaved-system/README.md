# Why Two Well-Behaved Agents Make One Badly-Behaved System

Agent A errs 2% of the time. Agent B errs 3% of the time. Naturally, intuition suggests their combined pipeline should succeed roughly 95% of the time. But in production, the chained system can fail on nearly a third of its runs.

Why does chaining two high-performing AI agents cause such a dramatic collapse?

When agents are evaluated in isolation, they are tested on clean, valid benchmark distributions. But when chained into an autonomous pipeline, Agent B does not receive ground truth—it receives Agent A's output as its unverified reality. Downstream agents condition on upstream outputs as if they were settled facts. When Agent A makes a minor slip, Agent B does not question the premise; it actively elaborates on the error, spawning dependent hallucinations that compound into systemic failure.

In this episode of *Computational Skepticism for AI*, Professor Bear and Liam unpack why per-agent unit testing cannot see the interaction term and why boundary invariants are essential to prevent cascading errors across multi-agent pipelines.

---

### Key Takeaways & Carry-Out
- **The Addition Fallacy**: Assuming multi-agent error rates simply add ($2\% + 3\% \approx 5\%$) treats agents as independent coin flips on clean data.
- **Conditioned Probability**: Downstream agents evaluate $P(\text{Action}_B \mid \text{Output}_A)$, not $P(\text{Action}_B \mid \text{Ground Truth})$.
- **Error Compounding**: One misplaced upstream token (e.g. an altered date) causes downstream planners to generate multiple conflicting bookings, cancellations, and false alerts.
- **The Interaction Term**: High benchmark scores on isolated tests guarantee almost nothing about pipeline safety when handoffs pass unchecked context.
- **Direction A (Isolation Blindspot)**: 99% accuracy on unit tests provides a false sense of security in unconstrained generative chains.
- **Direction B (Boundary Invariants Protect)**: Rigid boundary invariants, typed schemas, and ground-truth verification at handoff interfaces halt error cascades immediately.
- **Carry-Out Law**: Downstream agents treat upstream outputs as ground truth, so errors do not add—they compound.

---

### Your Turn — Prompt for Claude / AI Assistants
```
Take a multi-agent workflow in your stack where Agent B acts on Agent A's output. Inject a subtle, plausible error into Agent A's handoff document—a shifted date, a flipped polarity, or an omitted constraint. Run Agent B on that corrupted input. Does Agent B flag the anomaly, or does it elaborate on the false premise? Audit how your pipeline handles upstream errors before chaining your next agent.
```

---

### Metadata
- **Series**: Computational Skepticism for AI
- **Channel**: @HumanitariansAI (youtube.com/@HumanitariansAI)
- **Playlist**: Computational Skepticism — Validating Agentic AI
- **Source**: *Computational Skepticism for AI* by Nik Bear Brown (Chapter 8: Validating Agentic AI When Autonomous Systems Misbehave)
- **Voice**: Liam (synthesized via open-weights Kokoro `am_onyx`, in for Bear)
- **Visuals**: Manim + Remotion (Cream `#FAF9F5`, Warm Ink `#3D3929`, Terracotta `#D97757`)
- **Code (no media)**: https://github.com/nikbearbrown/humanitarians-youtube/tree/main/computational-skepticism/why-two-wellbehaved-agents-make-one-badlybehaved-system
- **AI Disclosure**: Voice synthesized via Kokoro TTS (am_onyx). Visual animations generated programmatically with Manim and Remotion.
