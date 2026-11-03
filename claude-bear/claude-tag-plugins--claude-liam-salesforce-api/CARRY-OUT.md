# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this
sentence survivable.

## The line

> **An empty response from Salesforce isn't a failure — 204 with no body
> is what success looks like. Trust the status code, not the silence, and
> when a call carries several writes at once, check each one's own code,
> not just the one wrapping it.**

## The wrong guess it defeats

That getting nothing back from Salesforce means the write didn't happen —
the way most APIs return the updated record, or at least a confirmation
body, on success. Salesforce doesn't. PATCH and DELETE return 204 No
Content on success; the emptiness is the success. A real failure looks
different: it carries an actual body, a JSON array with an errorCode
inside it, and that shape never matches a success response.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it
still true?*

Yes — it compresses the one distinction that matters (silence is success,
not failure) into the habit that keeps it from going quietly wrong: check
the code, and check every code when a call bundles more than one write.

## What it deliberately does not say

- Not a verdict on whether the salesforce-api skill is well designed —
  that's Teardown territory; this reel states the mechanism and stops.
- Not a claim that status codes are the only thing that matters — Describe,
  SOQL's `FIELDS()`/`LIMIT 200` rule, SOSL's `-G` requirement, and the
  external-ID upsert codes are real parts of the skill; the carry-out
  compresses the one habit that governs reading every response, not the
  full reference.
- Not a claim that every write needs a Composite call — only that the same
  "don't trust the outer result alone" habit applies the moment a call
  bundles more than one write.

---
**GATE C — signed:** ______________________  (human)
