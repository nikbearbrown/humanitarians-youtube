# CARRY-OUT.md — knowledge-work-plugins--claude-liam-compliance-check

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Compliance-check surfaces the regulations, approvals, and risks that apply
> to a proposed action — it never decides whether the action gets approved.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (surface-what-applies vs. render-the-
approval) without naming the topic (any specific regulation), and it
survives being repeated cold.

**The wrong guess it's built to defeat:** that a skill built to run a
compliance check also grants the compliance sign-off — that Claude clears
the feature to ship. `compliance-check` is deliberately narrower: given a
proposed action, product feature, or business initiative, it surfaces which
regulations touch it, which approvals are required, and where the risk
areas sit. Whether the feature is approved to launch is not this skill's job
and isn't in its file. That narrowness is stated as a design fact, not
judged as a strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill clears the feature for
launch" → "the skill only surfaces what applies and writes it up."
