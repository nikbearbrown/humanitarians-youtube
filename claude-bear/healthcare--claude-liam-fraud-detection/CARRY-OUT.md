# CARRY-OUT.md — healthcare--claude-liam-fraud-detection

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Fraud-detection ranks and cites suspect claims for a person to
> investigate — it never decides that fraud happened.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (rank/cite vs. decide) without naming
the topic (Medicare/Medicaid), and it survives being repeated cold.

**The wrong guess it's built to defeat:** that a skill built to screen
claims for fraud also renders the fraud determination itself. `fraud-
detection` is deliberately narrower: it screens a Medicare/Medicaid claims
corpus, ranks candidate claims, and produces fully-cited referrals — each
naming a provider's NPI, the suspected scheme, the dollar exposure, and a
confidence score — for an SIU / program-integrity team to open and
investigate. Whether fraud actually occurred is not this skill's call and
isn't in its file. That narrowness is stated as a design fact, not judged
as a strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill catches / convicts the
fraud" → "the skill only ranks and cites candidates, and hands the call to
a person."
