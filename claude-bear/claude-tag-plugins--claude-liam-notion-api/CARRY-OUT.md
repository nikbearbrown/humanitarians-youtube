# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Claude doesn't query a Notion database directly — it queries the data
> source underneath it, and needs that ID, not the database's. And when
> something can't be found, that almost always means it hasn't been shared
> with Claude yet, not that the ID is wrong.**

## The wrong guess it defeats

That the database's own ID is enough to query it, read its schema, or add a
row to it — as if a Notion database were one flat object with one ID. It
isn't: the database is a container, and the data source underneath it is
where the schema and the rows actually live, with its own separate ID.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (data source ID, not
database ID) and the one dead-end that wastes the most time (a 404 is a
sharing problem, not a bad ID), without overstating either.

## What it deliberately does not say

- Not a claim that the database ID is useless — it's exactly what you
  retrieve first, in order to read the `data_sources` list and find the ID
  that actually matters.
- Not a verdict on whether the skill's documentation is good or bad — the
  gaps it surfaces (missing recursion into sub-pages, expiring file URLs,
  an unguarded pagination loop, property-typed filters) are facts to know,
  not a rating of the skill's writing.
- Not a claim that sharing problems are a special Notion behavior — it's
  the ordinary consequence of any integration that only sees what it has
  explicitly been given access to.

---
**GATE C — signed:** ______________________  (human)
