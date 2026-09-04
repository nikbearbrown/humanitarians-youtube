# CARRY-OUT.md — healthcare--claude-liam-clinical-note-extract-skill

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Clinical-note-extract-skill only writes down what the note actually says,
> citing the exact text — and marks everything else null instead of
> guessing.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (cite vs. guess) without needing the
topic (clinical notes) explained further, and it survives being repeated
cold.

**The wrong guess it's built to defeat:** that an extraction tool built
against clinical notes fills a missing field the way a clinician would —
inferring a likely value from context and domain knowledge.
`clinical-note-extract-skill` is deliberately narrower: it reports a value
only when it can cite the exact span of text supporting it, and returns an
explicit null for anything it can't find. It never infers past what's on
the page. That narrowness is stated as a design fact, not judged as a
strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill fills in what's probably
true" → "the skill only reports what it can point to, and says so when it
can't."
