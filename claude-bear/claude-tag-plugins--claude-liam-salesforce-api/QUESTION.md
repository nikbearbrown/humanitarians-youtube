# QUESTION

**The question:** "Claude, Salesforce API." — when Claude PATCHes a
Salesforce record through the REST API and gets an empty response back,
did the write fail, or is that emptiness the whole point? Answered using
the salesforce-api skill's own worked facts as the concrete case.

**Mode:** redo — source is
`anthropics/claude-tag-plugins/youtube/claude-liam-salesforce-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, 7 beats — B00 cold
open (ClaudeComposerAsk, reading the skill's four governing rules aloud),
B01 anatomy/request setup/seven operations, B02 design/workflow patterns,
B05 teardown tell, BVDT verdict, BHTF handoff, BOUT outro — all already
REMOTION, no puppet/AI-video/pantry beat to replace beyond the WRITER LAW
swap). This reel keeps the question and the source's body facts,
re-registers the narration to Plain, replaces the cold open with the
Brutalist Hesitant Writer, folds the source's BVDT verdict recap into a
proper carry-out beat, and closes with the Humanitarians AI skin.

**Why it earns a reel:** the salesforce-api skill queries, reads, creates,
updates, and describes Salesforce records via the REST API. Every call
needs the org's own instance URL — its My Domain — plus a versioned data
path; there is no shared endpoint across orgs. Success and error responses
have different shapes: success comes back as a JSON object (or, for PATCH
and DELETE, as 204 No Content with an empty body); errors always come back
as a JSON array, so a jq projection written for the success shape crashes
on the error shape unless it is guarded with a type check first. SOQL has
no `SELECT *` — `FIELDS(ALL)` or `FIELDS(CUSTOM)` require a `LIMIT 200`.
Describe is the schema: field names, picklist values, relationship names
(custom fields end `__c`, custom relationships end `__r`), and the
createable/updateable flags — read before guessing a field name. Seven
operations: SOQL query (the bundled `sf_query.sh` pages `nextRecordsUrl`,
strips the per-record `attributes` envelope, flattens nested relationships
to dotted-key columns — `OFFSET` is hard-capped at 2000, so deep pagination
must follow `nextRecordsUrl`), SOSL full-text search (`GET /search` needs
`-G` with `--data-urlencode` or curl POSTs and the endpoint rejects it),
CRUD (GET/POST/PATCH/DELETE — PATCH and DELETE both return 204 No Content
on success, and DELETE moves the record to the recycle bin for 15 days),
upsert by external ID (PATCH on the external-ID path: 201 created, 200
updated, 300 the external ID matched multiple records and nothing was
written), Describe an sObject, Composite (chain up to 25 subrequests with
cross-references via `@{}` and `allOrNone` to roll back the whole batch on
any failure — the outer request returns 200 even when subrequests fail, so
each subrequest's own `httpStatusCode` must be checked individually), and
Limits (`GET /limits` — daily API cap has no `Retry-After`, you wait for
requests to age out of the 24-hour window).

**Naive framing (B00, corrected on screen):** "An empty response from
Salesforce means my update failed. Right?" → corrects "failed" to "worked"
(PATCH and DELETE return 204 No Content on success — an empty body is not
an error; a real failure carries an actual body, a JSON array with an
errorCode inside it).

**Body facts carried from source (unchanged):**
- PATCH/DELETE return 204 No Content on success — an empty body is the
  success state, not a failure signal
- errors always come back as a JSON array with an errorCode; success comes
  back as an object (or empty, for 204) — never the same shape as an error
- request setup: the org's own instance URL (My Domain) + versioned data
  path — no shared endpoint across orgs
- Describe before writing any field name: field names, picklist values,
  createable/updateable flags, custom `__c`/`__r` naming
- Composite: outer 200 does not mean every subrequest succeeded — check
  each subrequest's own `httpStatusCode`; only `allOrNone: true` rolls the
  whole batch back on one failure, otherwise partial writes stick
- upsert by external ID: 201 created, 200 updated, 300 matched multiple
  records and wrote nothing
- SOQL has no `SELECT *`; deep pagination follows `nextRecordsUrl`, not
  `OFFSET` (hard-capped at 2000)
- SOSL search needs `-G`/`--data-urlencode` or the endpoint rejects the
  request
- documented gap: composite subrequest URLs must repeat the same API
  version as the outer request, or the subrequest silently uses the wrong
  one
- Your Turn: paste the source's own worked request (find open
  Opportunities closing this quarter, with Account name and owner, then
  update the top one to Closed Won) and watch whether Claude sets the real
  instance URL, Describes the object before writing, and checks the actual
  status code instead of treating an empty response as a failure.
