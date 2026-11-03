# PROMPTS — Compiling Is Not Migrating.

## Open slots

**None.** All 13 beats render from registered Remotion compositions. There is
no pantry request, no slate and no human-supplied media.

## B00 — the cold-open ask (on screen, verbatim)

> I am moving a SQL Server financial planning database to Snowflake. The
> converted script is one 1,244-line file. Split it into something deployable,
> find what will not run on Snowflake, and tell me how I will prove the data and
> the procedures still behave the same.

## B04 — the deploy ask (ASK→RESULT pair; the receipt is B05)

> Deploy these 29 files to Snowflake in manifest order. Dry-run first. If a file
> fails, stop there and mark everything after it skipped. Never load the sample
> data in a production run.

## B11 — the handoff prompt (read aloud verbatim, then discussed)

> Here is one stored procedure from a database I am migrating. List every place
> it relies on the old engine to enforce something the new engine only
> declares: a unique key, a foreign key, a check, an identity value. For each
> one, show me what happens if the procedure runs twice.

**Why this prompt earns the slot.** It does not ask the viewer to learn about
Snowflake. It makes them bring their own procedure and hunt for exactly the
failure B07 named: behaviour the old engine enforced and the new one only
declares. The last clause, "runs twice", turns that into the cheapest possible
test, and the narration spends its discussion on why that clause matters.

## Build notes

The six `Snow*` components were authored directly against the house
dual-aspect law. No image or video generation model was called. Spend: $0.00.
