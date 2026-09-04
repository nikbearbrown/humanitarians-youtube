# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Every Redshift query Claude runs turns on two habits — poll
> `DescribeStatement` to a terminal state before ever calling
> `GetStatementResult`, and decode each cell with `to_entries[0].value`
> instead of a naive `.value` — get those right and a 200 from
> `ExecuteStatement` stops meaning anything it doesn't.**

## The wrong guess it defeats

That a successful `ExecuteStatement` call means the query succeeded — the
way a normal database call would tell you right away whether it worked. It
doesn't. `ExecuteStatement` returning 200 only means Redshift accepted the
submission; the SQL runs afterward, and if it fails, that failure never
appears in the response to the call that submitted it. It shows up only
later, as `Status: FAILED` on `DescribeStatement` — and only if you poll
for it.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (a Redshift call is a
submission, not an answer) into the two habits that keep it from going
quietly wrong, without overstating what those two habits guarantee.

## What it deliberately does not say

- Not a verdict on whether the redshift-api skill is well designed — that's
  Teardown territory; this reel states the mechanism and stops.
- Not a claim that polling and cell decoding are the *only* things that
  matter — the three connection-target shapes, the six operations, the 3
  TPS catalog cap, and the `ClientToken` idempotency gap are real, but the
  carry-out compresses the two habits that govern every single call, not
  the full reference.
- Not a claim that every request needs the bundled script — only that a
  hand-rolled request still owes the same two habits, and that cell
  decoding is where a hand-rolled reader most often goes quietly wrong.

---
**GATE C — signed:** ______________________  (human)
