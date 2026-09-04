# CARRY-OUT.md (GATE C)

**Carry-out sentence (written before the body, per CARRY-OUT LAW):**

> A saved token isn't a live token — the credential file is only read once,
> at restart. The access policy has no such wait; it's checked on your
> very next message.

**The wrong guess it defeats:** that saving a new token through the
`configure` skill makes the bot start using it immediately — the same way
updating the access allowlist takes effect right away. It doesn't: the
skill writes two different kinds of state to two different files, and only
one of them is re-read live.

**Test:** if someone repeats only this sentence in a meeting next week, is
it still true? Yes — it compresses the distinction that matters (two files,
two different read timings), not the topic ("Discord bot configuration" in
general).

**Signed:** GATE C — SIGNED (this build).
