# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Every BigQuery job Claude runs turns on two habits — carry the same
> location on every follow-up call, and check `errorResult` before trusting
> a job marked DONE — get those right and both query modes take care of
> themselves.**

## The wrong guess it defeats

That Claude runs a BigQuery query the way you'd expect a normal database
call to work: send the SQL, get the rows back in one round trip. It
doesn't — every query becomes a **job**, submitted in a billing project
that pays for it, pinned to a location, and checked (sometimes polled and
paged) before the rows are trustworthy. Skip the location on a follow-up
call and it 404s. Trust a `DONE` status without checking `errorResult` and
a failed job can look like a finished one.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (a BigQuery query is a
tracked job, not an instant call) into the two habits that keep it from
going quietly wrong, without overstating what those two habits guarantee.

## What it deliberately does not say

- Not a verdict on whether the BigQuery API skill is well designed — that's
  Teardown territory; this reel states the mechanism and stops.
- Not a claim that location and `errorResult` are the *only* things that
  matter — the pagination field-name split, `totalRows`, and the eight
  operations are real, but the carry-out compresses the two habits that
  govern every single job, not the full reference.
- Not a claim that every query needs the bundled script — only that a
  hand-rolled request still owes the same two habits, and that pagination
  is where a hand-rolled loop most often goes quietly wrong.

---
**GATE C — signed:** ______________________  (human)
