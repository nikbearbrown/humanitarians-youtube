# CARRY-OUT.md — knowledge-work-plugins--claude-liam-legal-risk-assessment

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Legal-risk-assessment sorts legal issues by severity and likelihood and
> flags which ones need escalation — it never scores the matter with a
> single verdict of its own.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (sort-by-a-grid vs. render-a-verdict)
without naming the topic (any specific contract or matter), and it survives
being repeated cold.

**The wrong guess it's built to defeat:** that a skill built to "assess"
legal risk hands back a legal opinion — a single risk score or verdict on
whether something is safe to sign or too dangerous to proceed with.
`legal-risk-assessment` is deliberately narrower: given a legal issue, it
classifies it against a severity-by-likelihood grid and applies escalation
criteria — does this need senior counsel, or outside legal review. Whether
the underlying legal question resolves in the client's favor is not this
skill's job and isn't in its file. That narrowness is stated as a design
fact, not judged as a strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill scores my legal risk" →
"the skill only sorts the issue by severity and likelihood and flags it for
a person when escalation criteria are met."
