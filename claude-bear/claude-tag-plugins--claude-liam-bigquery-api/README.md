# Claude, BigQuery API.

Claude doesn't run a BigQuery query by sending your SQL and getting rows
back in one round trip — it submits a **job**, in a billing project that
pays for the bytes scanned (not necessarily where the data lives), pinned
to the location it ran in. Sometimes the job finishes fast enough that the
rows come straight back — synchronous mode. A slower query can't finish
inside that window, so it's submitted instead and checked until it's ready
— asynchronous mode. Ask for the top ten names in California from a public
names dataset, and every later check on that job has to carry the same
location back, or it 404s. Get the location right and the check comes back
clean — but reaching `DONE` isn't proof the job succeeded; the result can
carry an error, so that gets checked before the rows are trusted. One
exception worth knowing: the field name for "more pages" isn't the same
everywhere — list endpoints use `nextPageToken`, but a query's own results
use `pageToken` — read the wrong one and it comes back empty, silently,
after page one.

**Topic:** BIGQUERY API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-bigquery-api

---

## Chapters

0:00 Claude must just make one API call. Is that it?
0:12 One call, or a tracked job
0:29 Billing project pays. Location pins it.
0:47 DONE isn't proof it succeeded
1:14 Carry-out
1:26 Your turn
1:49 Outro

---

## YOUR TURN

"Run a query against the BigQuery public dataset
bigquery-public-data.usa_names.usa_1910_current and return the top five
names for Texas."

Why it's worth running: it forces three checks in one shot — does Claude
carry the same location on every follow-up call, does it check for an
error before trusting a job marked done, and does it reach for the bundled
script's pagination instead of a single request that quietly misses rows
past the first page.

---

## Deliberately not claimed

Not a verdict on whether the BigQuery API skill is well designed — that's
Teardown territory; this reel states the mechanism and stops. Not a claim
that location and the error check are the only rules that matter — the
eight operations, `totalRows`, and the write-heavy job types are real, but
the carry-out compresses the two habits that govern every single job, not
the full reference. Not a claim that every BigQuery request needs the
bundled script — only that a hand-rolled request still owes the same two
habits.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeAPI #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
