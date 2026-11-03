# QUESTION

**The question:** "Claude, BigQuery API." — when Claude runs a query against
BigQuery, does it just send the SQL and hand back rows in one round trip, or
is something else happening underneath? Answered using the BigQuery API
skill's own worked facts as the concrete case.

**Mode:** redo — source is
`anthropics/claude-tag-plugins/youtube/claude-liam-bigquery-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, 7 beats — B00 cold
open, B01 job model/two modes, B02 eight operations, B05 teardown tell, BVDT
verdict, BHTF handoff, BOUT outro — all already REMOTION, no puppet/AI-video/
pantry beat to replace beyond the WRITER LAW swap). This reel keeps the
question and the source's body facts, re-registers the narration to Plain,
replaces the cold open with the Brutalist Hesitant Writer, folds the source's
BVDT verdict recap into a proper carry-out beat, and closes with the
Humanitarians AI skin.

**Why it earns a reel:** the BigQuery API skill covers
`bigquery.googleapis.com/bigquery/v2` plus a bundled `bq_query.sh` script.
Every query runs as a **job** in a **billing project** — the project charged
for bytes scanned is not necessarily where the data lives. Two execution
modes: synchronous (`jobs.query`, one call that blocks up to a timeout and
returns rows inline) for queries that finish quickly, asynchronous
(`jobs.insert` → poll `jobs.get` until `status.state` is `DONE` → page with
`getQueryResults`) for everything else. A job is pinned to the location it
ran in — omit location on a follow-up call and it 404s. The critical
invariant: a `DONE` job can still have failed — `status.errorResult` has to
be checked before trusting the rows. Eight core operations (run, submit
directly, cancel, list jobs, list datasets, list tables, get schema, preview
rows for free) cover the read/write surface. One documented gotcha worth
carrying: pagination field names are non-uniform — list endpoints return
`nextPageToken`, but a query's own result page returns `pageToken` — reading
the wrong field silently returns nothing and stops after page one.

**Naive framing (B00, corrected on screen):** "Claude must just make one API
call for my SQL and hand back my rows. Is that it?" → corrects "call" to
"job" (Claude isn't making one instant request — it's submitting a job that
gets tracked, checked, and sometimes paged, before the rows are trustworthy).

**Body facts carried from source (unchanged):**
- job model: billing project pays (not necessarily where the data lives);
  every job gets an ID and is pinned to a location
- two execution modes: synchronous (`jobs.query`, blocks to a timeout, rows
  inline) vs asynchronous (`jobs.insert` → poll `jobs.get` → page with
  `getQueryResults`)
- critical invariant: `DONE` ≠ success — check `status.errorResult` before
  trusting the rows
- location must be passed on every subsequent call or it 404s
- eight operations, one bundled script (`bq_query.sh`) that drives both
  modes, location threading, polling, pagination, and f/v cell decoding
- documented gap: pagination field names split — `nextPageToken` on list
  endpoints, `pageToken` on query results — reading the wrong one returns
  nothing silently
- Your Turn: paste the source's own worked request (top 5 names for Texas
  from the `usa_names` public dataset) and watch whether Claude carries
  location on every follow-up call, checks `errorResult` before trusting a
  `DONE` job, and uses the bundled script instead of a raw request that
  might miss a page
