# CARRY-OUT.md

**Carry-out line (BCRY narration):**
> There's one endpoint, not many — and neither a 200 nor a 400 tells you the
> truth by itself: a 200 can still mean it failed, and a 400 can just mean
> you're rate-limited.

**Wrong guess it defeats:** that Linear works like a typical REST API — a
family of endpoints keyed by object name (`/issues`, `/projects`), where the
HTTP status line is the whole story (B00's hesitant-writer correction: "REST"
→ "GraphQL" — the naive framing asks how to call the Linear *REST* API; the
corrected question asks how to call the *GraphQL* API, which is what the rest
of the reel shows: one endpoint for every read and write, and a status code
that doesn't settle whether the call actually succeeded).

**Test:** if someone repeats only this sentence next week, it is still true
and still the distinction that matters — not a summary of the whole topic.
