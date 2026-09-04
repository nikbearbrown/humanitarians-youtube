# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **PagerDuty splits in two: the REST API reads and manages everything with a
> Token header, while Events v2 triggers, acknowledges, and resolves alerts
> with a routing key in the body — no token there at all. Mix the two up,
> and you won't get an error message, you'll get an empty one.**

## The wrong guess it defeats

That one PagerDuty credential — the API token — works for everything,
including triggering an alert. It doesn't: triggering, acknowledging, and
resolving run through a completely separate API (Events v2), on a different
host, authenticated with a routing key sent in the request body, with no
Authorization header at all.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (two APIs, two hosts,
two unrelated auth schemes) and the one failure mode that wastes the most
debugging time (a 401 with no body, not a helpful error), without overstating
either.

## What it deliberately does not say

- Not a claim that the token is useless for triggering-adjacent work — it's
  exactly what the REST API needs to look up who's on call, or to trace an
  incident's log entries, before or after a trigger goes through Events v2.
- Not a verdict on whether the skill's documentation is good or bad — the
  gaps it surfaces (bracket-URL encoding, the `From:` header, reference-object
  `type` fields, plain-text Events v2 errors, mismatched rate limits) are
  facts to know, not a rating of the skill's writing.
- Not a claim that PagerDuty is unusual for splitting auth this way — plenty
  of alerting/paging systems separate "manage" credentials from "fire an
  event" credentials; this reel states what PagerDuty specifically does.

---
**GATE C — signed:** ______________________  (human)
