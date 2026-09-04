# Claude, Salesforce API.

An empty response from Salesforce's REST API isn't a failure — `PATCH` and
`DELETE` return **204 No Content** on success, and that emptiness is the
success. A real failure looks different: it carries an actual body, a JSON
array with an `errorCode` inside it, and that shape never matches a
success response. Before touching any field, every call needs the org's
own instance URL — its My Domain — plus the versioned data path, and
`Describe` on the object to confirm a field is updateable and a picklist
value is valid. Query the open Opportunities closing this quarter, pull
the Id of the top match, `PATCH` its `StageName` to Closed Won, and the
response comes back 204 — exactly what success looks like. Chain several
updates in one Composite call instead, and the outer response returning
200 doesn't mean every subrequest succeeded — each one carries its own
`httpStatusCode`, and a single failed subrequest doesn't undo the others
either, unless `allOrNone` was set to true.

**Topic:** SALESFORCE API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-salesforce-api

---

## Chapters

0:00 An empty response from Salesforce means my update failed. Right?
0:12 Silent success, loud failure
0:32 Instance URL, Describe, then query
0:58 204, then the Composite caveat
1:29 Carry-out
1:47 Your turn
2:15 Outro

---

## YOUR TURN

"Find all open Opportunities closing this quarter, with Account name and
owner — then update the top one to Closed Won."

Why it's worth running: it forces three checks in one shot — does Claude
set the org's real instance URL before making any call, does it Describe
the Opportunity object to confirm `StageName` is updateable and `Closed
Won` is a valid picklist value before writing, and does it check the
actual status code afterward instead of treating an empty response as a
failure.

---

## Deliberately not claimed

Not a verdict on whether the salesforce-api skill is well designed —
that's Teardown territory; this reel states the mechanism and stops. Not
a claim that status codes are the only rule that matters — Describe,
SOQL's `FIELDS()`/`LIMIT 200` requirement, SOSL's `-G` flag, and the
external-ID upsert codes (201/200/300) are real, but the carry-out
compresses the one habit that governs reading every response, not the
full reference. Not a claim that every write needs a Composite call —
only that a hand-rolled request still owes the same "don't trust the
outer result alone" habit.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeAPI #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
