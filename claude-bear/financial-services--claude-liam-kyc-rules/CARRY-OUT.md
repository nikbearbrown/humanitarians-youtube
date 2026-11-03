# CARRY-OUT.md — financial-services--claude-liam-kyc-rules

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Kyc-rules scores a client file against the firm's own rules and flags what
> needs a person — it never decides whether to accept anyone.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (score vs. decide) without naming the
topic (KYC/AML), and it survives being repeated cold.

**The wrong guess it's built to defeat:** that a skill built to screen new
clients for compliance risk also makes the accept/reject call. `kyc-rules`
is deliberately narrower: it takes an already-parsed onboarding record,
applies the firm's KYC/AML rules grid to it, assigns a risk rating, cites
the rule behind every outcome, and flags what's missing or worth
escalating. Whether to onboard the client is not this skill's job and isn't
in its file. That narrowness is stated as a design fact, not judged as a
strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill approves or rejects the
client" → "the skill only scores the file and routes it to a person."
