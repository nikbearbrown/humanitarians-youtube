# Claude, Redshift API.

A successful call to Amazon Redshift's Data API doesn't mean the SQL
succeeded — `ExecuteStatement` returning 200 only means the query was
**accepted**. It runs afterward, and if it fails, that failure never shows
up in the response to the call that submitted it — it appears only later,
as `Status: FAILED` on `DescribeStatement`. Before any call, two things
have to be set: a region (baked into the endpoint hostname) and a
connection target — a workgroup name for Serverless, a cluster plus a
database user for provisioned access, or a secret for Secrets Manager. Ask
for the top twenty events from the past month, grouped by name, and
`ExecuteStatement` hands back exactly one thing: an Id. Poll that Id with
`DescribeStatement` until it reaches `FINISHED`, then check `HasResultSet`
before calling `GetStatementResult` — a write statement can finish with
nothing to page. But `FINISHED` alone isn't proof the SQL was clean; that
same field can read `FAILED` instead. A statement still sitting at
`STARTED` isn't stuck either — that's what the poll loop is for. One habit
worth carrying past this one query: decode each result cell with
`to_entries[0].value`, not a naive `.value`, which silently returns
nothing.

**Topic:** REDSHIFT API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-redshift-api

---

## Chapters

0:00 A 200 from Redshift means my query worked. Right?
0:10 200 means accepted, not correct
0:29 Region + RS_TARGET, then submit
0:50 Finished isn't proof it succeeded
1:21 Carry-out
1:39 Your turn
2:03 Outro

---

## YOUR TURN

"Query my Redshift Serverless workgroup — find the top twenty events from
the past month, grouped by name."

Why it's worth running: it forces three checks in one shot — does Claude
set the region and the workgroup before making any call, does it poll
`DescribeStatement` to a terminal state before ever calling
`GetStatementResult`, and does it decode result cells with
`to_entries[0].value` instead of a naive `.value` that comes back empty.

---

## Deliberately not claimed

Not a verdict on whether the redshift-api skill is well designed — that's
Teardown territory; this reel states the mechanism and stops. Not a claim
that polling and cell decoding are the only rules that matter — the three
connection-target shapes, the six operations, the 3 TPS catalog cap, and
the `ClientToken` idempotency gap are real, but the carry-out compresses
the two habits that govern every single call, not the full reference. Not
a claim that every Redshift request needs the bundled script — only that a
hand-rolled request still owes the same two habits.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeAPI #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
