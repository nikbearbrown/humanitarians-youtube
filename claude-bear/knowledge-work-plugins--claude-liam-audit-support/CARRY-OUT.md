# CARRY-OUT.md — knowledge-work-plugins--claude-liam-audit-support

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Audit-support tests the sample against the firm's own criteria and
> classifies what it finds — it never decides whether the company's
> controls pass.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (test-and-classify vs. render-the-
opinion) without naming the topic (SOX 404), and it survives being repeated
cold.

**The wrong guess it's built to defeat:** that a skill built to support a
SOX 404 audit also renders the audit opinion — whether the company's
internal controls pass overall. `audit-support` is deliberately narrower:
it picks the sample using the firm's sampling methodology, tests each item
against the control's stated criteria, and classifies any exception it
finds. Whether the company's controls pass as a whole is not this skill's
job and isn't in its file. That narrowness is stated as a design fact, not
judged as a strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill passes or fails the
audit" → "the skill only tests the sample and writes up what it finds."
