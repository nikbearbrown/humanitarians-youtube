# QUESTION

**The question:** "Claude, Redshift API." — when Claude runs SQL against
Amazon Redshift through the Data API, does a successful call mean the query
succeeded, or is something else happening underneath? Answered using the
redshift-api skill's own worked facts as the concrete case.

**Mode:** redo — source is
`anthropics/claude-tag-plugins/youtube/claude-liam-redshift-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, 7 beats — B00 cold
open, B01 anatomy/request setup/six operations, B02 design/workflow
patterns, B05 teardown tell, BVDT verdict, BHTF handoff, BOUT outro — all
already REMOTION, no puppet/AI-video/pantry beat to replace beyond the
WRITER LAW swap). This reel keeps the question and the source's body facts,
re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, and closes with the Humanitarians AI skin.

**Why it earns a reel:** the redshift-api skill covers Amazon Redshift
(provisioned clusters and Serverless) via the Redshift Data API. Every call
is a POST to `https://redshift-data.<region>.amazonaws.com/`, with
`X-Amz-Target: RedshiftData.<Action>` — there are no REST paths. The API is
fully asynchronous: `ExecuteStatement` submits and returns an `Id`, then
`DescribeStatement` is polled until a terminal state, then
`GetStatementResult` pages the rows on `NextToken`. The critical invariant:
`ExecuteStatement` returning 200 does not mean the SQL succeeded — a bad
query still gets accepted and only surfaces as `Status: FAILED` later, on
`DescribeStatement`. Request setup needs two things: a region (baked into
the endpoint hostname) and one connection target in `RS_TARGET` —
`WorkgroupName` for Serverless, `ClusterIdentifier` + `DbUser` for
provisioned with temporary credentials, or `SecretArn` for Secrets Manager.
Six core operations: run a query (the bundled `rs_query.sh` drives submit →
poll → page → decode), resume a statement by `Id`, cancel with
`CancelStatement` (best-effort), `BatchExecuteStatement` (all-commit-or-
rollback, sub-statement IDs with `:N` suffixes fetched separately),
`ListStatements` (finished-only by default, `ALL` to see everything), and
catalog browsing (`ListDatabases`/`ListSchemas`/`ListTables`/
`DescribeTable`, all paginated, all capped at 3 TPS versus 30 TPS for
`ExecuteStatement`). Result cells are typed one-key objects — reading them
needs `to_entries[0].value`, not a naive `.value`, which silently returns
nothing. One documented gap worth carrying: `ExecuteStatement` is not
idempotent unless a `ClientToken` is passed, so a retried write can submit
twice.

**Naive framing (B00, corrected on screen):** "A 200 from Redshift means my
query worked. Right?" → corrects "worked" to "began" (a 200 from
`ExecuteStatement` only means the request was accepted and the query began
running — whether it actually finished, and whether it finished cleanly,
is answered later by polling `DescribeStatement`).

**Body facts carried from source (unchanged):**
- every call is a POST to `redshift-data.<region>.amazonaws.com/`, header
  `X-Amz-Target: RedshiftData.<Action>` — no REST paths
- fully asynchronous: `ExecuteStatement` → `Id` → poll `DescribeStatement`
  to a terminal state → page `GetStatementResult` on `NextToken`
- critical invariant: a 200 from `ExecuteStatement` ≠ SQL success — the
  failure only shows up as `Status: FAILED` on `DescribeStatement`, never
  in the response to the submitting call
- request setup: region (endpoint hostname) + `RS_TARGET` in one of three
  shapes — `WorkgroupName`, `ClusterIdentifier` + `DbUser`, or `SecretArn`
- six operations: run (`rs_query.sh`), resume by `Id`, cancel
  (`CancelStatement`, best-effort), `BatchExecuteStatement` (sub-statement
  IDs fetched separately), `ListStatements`, catalog browsing (3 TPS cap)
- typed cell decoding: `to_entries[0].value`, not a naive `.value`
- documented gap: `ExecuteStatement` is not idempotent without
  `ClientToken` — a retried write can submit twice
- Your Turn: paste the source's own worked request (top 20 events from the
  past month, grouped by name, against a Redshift Serverless workgroup) and
  watch whether Claude sets region + `RS_TARGET` before calling, polls
  `DescribeStatement` to a terminal state before ever calling
  `GetStatementResult`, and decodes cells with `to_entries[0].value`
  instead of a naive `.value`.
