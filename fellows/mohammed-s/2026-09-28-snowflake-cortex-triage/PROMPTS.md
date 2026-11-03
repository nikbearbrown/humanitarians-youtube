# PROMPTS — Cortex, In The Warehouse.

## Open slots

**None.** All 11 beats render from registered Remotion compositions. There is
no pantry request, no slate, and no human-supplied media in this reel.

## B00 — the cold-open ask (shown on screen, verbatim)

> I have 40,000 free-text support tickets in a Snowflake table. What is the
> smallest useful thing Snowflake Cortex can do with them — and what does it
> cost me in complexity?

## B04 — the generation ask (ASK→RESULT pair, receipt lands in B05)

> Write the SQL that triages these tickets: a category, a sentiment score, and
> a one-line summary — in one pass over the table.

## B09 — the handoff prompt (HANDOFF LAW: read aloud verbatim, then discussed)

> Here is the schema of one text-heavy table I own. Show me the single
> Cortex query that would produce the most decision-useful column — then
> tell me what it costs per million rows, and how to validate the labels.

**Why this prompt earns the slot.** It is not "learn more about Cortex". It
makes the viewer bring their own table, and it demands the two things the
vendor demo never hands over: the invoice and the error rate. Those are exactly
the two failure modes B07 just named, so the handoff extends the episode's
argument into the viewer's own work rather than restating it. The narration
reads it verbatim, then spends two lines on why the last two clauses are the
point, before inviting the pause.

## Build prompts used for the scene components

The five `Cortex*` components and the `ClaudeCodeBeat916` registration were
authored directly against the house dual-aspect law (one component, two
registrations, branch on `height > width`). No image or video generation model
was called at any point in this build. Total spend: $0.00.
