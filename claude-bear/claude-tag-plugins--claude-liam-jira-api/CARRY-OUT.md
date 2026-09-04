# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this
sentence survivable.

## The line

> **Every Jira write Claude makes turns on two habits — a transition ID
> instead of a status you set, and a JSON tree instead of a string you
> type — get those right, and the three pagination schemes are the only
> thing left to watch for.**

## The wrong guess it defeats

That moving a ticket to Done is a direct status write, the way you'd set
any other field. It isn't: Jira has no status field to set. Claude has to
list the issue's available transitions, match the one it wants by name,
and post that transition's ID — and the ID isn't portable, because the
same-looking transition on a different ticket, in a different workflow,
often carries a different ID entirely. The same "write directly" instinct
also fails on comments: the body has to be a JSON tree (Atlassian Document
Format), not a plain string, or the request comes back a 400 that never
mentions ADF as the fix.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still
true?*

Yes — it compresses the one distinction that matters (Jira writes go
through a lookup-then-post shape, never a direct set) without overstating
what those two habits guarantee; the pagination caveat is flagged rather
than folded in, since getting the two write habits right doesn't by itself
guarantee a search loop terminates correctly.

## What it deliberately does not say

- Not a verdict on whether the jira-api skill is well designed — that's
  Teardown territory; this reel states the mechanism and stops.
- Not a claim that transitions and ADF are the *only* things that matter —
  accountId-not-email, the 404-vs-403 access-control quirk, and
  `maxResults` clamping are real, but the carry-out compresses the two
  habits that govern every write, not the full reference.
- Not a claim that the three pagination schemes are equally hard — JQL
  search's missing total is the one flagged in the reel because it's the
  one most likely to make a loop spin forever.

---
**GATE C — signed:** ______________________  (human)
