# CARRY-OUT.md

**Carry-out line (BCRY narration):**
> A session report isn't Claude counting your tokens — it's a script that
> counts, and Claude that explains what the count means.

**Wrong guess it defeats:** that a session report full of exact numbers
means Claude read through the raw session logs and tallied tokens, cache
hits, and subagent calls itself (B00's hesitant-writer correction: "count"
→ "read"; broken at B02 with a falsifying case — delete
`analyze-sessions.mjs` from the skill folder and the report doesn't get a
little worse, it can't run at all, because there was no other way inside
this skill to get those numbers in the first place).

**Test:** if someone repeats only this sentence next week, it is still
true and still the distinction that matters — not a summary of the whole
topic.
