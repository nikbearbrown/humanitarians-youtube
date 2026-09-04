# CARRY-OUT.md — financial-services--claude-liam-break-trace

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Break-trace finds exactly where two numbers stopped agreeing and says
> why — it never decides what happens next.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (trace vs. fix) without naming the
topic (reconciliation), and it survives being repeated cold.

**The wrong guess it's built to defeat:** that a skill named for finding a
discrepancy in the books also resolves it. `break-trace` is deliberately
narrower: it takes a break another skill has already flagged, follows the
audit trail on each side back to the originating entry, and states what's
different and why. Deciding what to do about the difference — reverse an
entry, escalate it, write it off — is not this skill's job and isn't in its
file. That narrowness is stated as a design fact, not judged as a
strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill fixes the break" → "the
skill only traces the break to its cause."
