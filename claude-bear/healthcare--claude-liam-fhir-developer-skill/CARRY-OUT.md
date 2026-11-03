# CARRY-OUT.md — healthcare--claude-liam-fhir-developer-skill

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Fhir-developer-skill doesn't just pass or fail a request — it returns the
> exact status code that names what's wrong, and that code is the spec.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (specific code vs. binary pass/fail)
without needing the topic (FHIR APIs) explained further, and it survives
being repeated cold.

**The wrong guess it's built to defeat:** that a validator's job ends at
"valid" or "invalid" — one gate, two outcomes. `fhir-developer-skill` is
narrower and more specific than that: every rejection carries the exact
HTTP status code for the exact reason (422 for an invalid enum value, 412
for an ETag mismatch), so the code itself is part of the specification, not
just a pass/fail flag. That specificity is stated as a design fact, not
judged as a strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "it just says pass or fail" → "it
says exactly what failed, in a code that means the same thing every time."
