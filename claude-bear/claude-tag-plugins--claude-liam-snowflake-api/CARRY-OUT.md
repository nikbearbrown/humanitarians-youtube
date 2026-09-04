# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Every Snowflake query Claude runs turns on one habit — treat the submit
> call as a receipt, not an answer: poll the handle to a terminal state,
> then fetch the result one partition at a time — get that right and a
> response from the SQL API stops meaning anything it doesn't.**

## The wrong guess it defeats

That submitting SQL to Snowflake hands back the rows directly, the way a
normal database call would. It doesn't. The submit call is asynchronous —
what comes back first is a statement handle, not the answer. The real
result, and whether the query even succeeded, is only visible later, by
polling that handle and then fetching the result in partitions.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (a Snowflake submit
call is a receipt, not an answer) into the habit that keeps a caller from
mistaking "accepted" for "finished," without overstating what that habit
guarantees.

## What it deliberately does not say

- Not a verdict on whether the snowflake-api skill is well designed —
  that's Teardown territory; this reel states the mechanism and stops.
- Not a claim that polling and partitioned fetching are the *only* things
  that matter — cancelling a running statement and browsing warehouses,
  databases, schemas, and tables are real parts of the skill; the carry-out
  compresses the one habit that governs every single query, not a full
  reference.
- Not a claim about specific field names, header names, or exact
  terminal-state strings — the source's description confirms the shape
  (submit → handle → poll → fetch in partitions) but not that level of
  implementation detail, so the reel never invents it.

---
**GATE C — signed:** ______________________  (human)
