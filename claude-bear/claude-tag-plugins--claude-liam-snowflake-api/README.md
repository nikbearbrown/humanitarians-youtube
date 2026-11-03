# Claude, Snowflake Api.

Submitting SQL to Snowflake through the `snowflake-api` skill doesn't hand
back your rows directly — the first thing back is a **statement handle**,
not an answer. Submit a query with a typo and the API still accepts it just
as cleanly; the failure only shows up later, when you poll that handle,
never in the response to the call that submitted it. Before any query,
Claude needs a warehouse to run it on, chosen from what's browsable —
warehouses, databases, schemas, and tables. Ask what tables are in a
schema, and the API hands back exactly one thing: a handle. Poll that
handle until it reaches a terminal state, then fetch the result — but it
can arrive in more than one partition, so one fetch isn't always the whole
answer. Reaching a terminal state isn't proof of success either; that same
status can read failed instead. A handle still shown as running isn't
stuck — that's what polling is for, and what you'd cancel if you needed to
stop it early.

**Topic:** SNOWFLAKE API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-snowflake-api

---

## Chapters

0:00 I submit SQL to Snowflake and get my answer back. Right?
0:10 Submit returns a handle, not rows
0:31 Warehouse, then submit
0:56 Terminal isn't proof it succeeded
1:32 Carry-out
1:49 Your turn
2:14 Outro

---

## YOUR TURN

"List the tables in a schema I have access to in Snowflake."

Why it's worth running: it forces three checks in one shot — does Claude
treat the first response as a handle to check rather than a finished
answer, does it poll that handle to a terminal state before trusting it,
and does it fetch more than one partition if the table list is long.

---

## Deliberately not claimed

Not a verdict on whether the snowflake-api skill is well designed — that's
Teardown territory; this reel states the mechanism and stops. Not specific
field names, header names, or terminal-state strings — the source's
description confirms the shape (submit → handle → poll → fetch in
partitions → cancel → browse) but not that level of implementation detail,
so this reel states exactly that shape and adds nothing invented beyond
it. Not a claim that polling and partitioned fetching are the only rules
that matter — cancelling and browsing warehouses/databases/schemas/tables
are real parts of the skill, but the carry-out compresses the one habit
that governs every single query, not a full reference.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeAPI #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
