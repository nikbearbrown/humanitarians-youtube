# PEDAGOGY — claude-liam-pagerduty-api

**Skill:** pagerduty-api  
**Register:** Teardown  
**Verdict:** PASS

## What the skill gets right

1. Two-API architecture explained clearly: REST at api.pagerduty.com for reading and managing, Events v2 at events.pagerduty.com for triggering/ack/resolving.
2. Auth difference documented explicitly: REST uses `Authorization: Token token=<t>` (not Bearer); Events v2 uses routing_key in body — no Authorization header.
3. 401 empty body gotcha called out: must use `-w "%{http_code}"` or `-o /dev/null -w` to see HTTP status; curl default shows nothing on 401.
4. Bundled pd_oncall.sh script handles the bracket-param URL encoding problem automatically.
5. Rate limits documented with specific numbers (960 req/min REST, ~120 events/min Events v2) and the right headers to watch.

## Where it bites

1. curl bracket parameters need `-g`/`--globoff` for `?user_ids[]=` style filters — easy to forget on raw curl calls outside the bundled script.
2. `From:` header required on all mutations — silent failure (usually 400) if omitted.
3. Reference objects need a `type` field alongside the `id` — e.g. `{"id": "...", "type": "service_reference"}` — API returns 400 validation error otherwise.
4. Events v2 routing_key error responses are plain text, not JSON — a naive `jq` pipe on error output breaks.
5. Rate limit headers are on the REST API only; Events v2 has no per-request rate limit header.

## Teaching strategy

Cold open with the dual-API surprise: "Two separate hosts, two different auth schemes — REST uses Token, Events v2 uses routing_key in the body." Anatomy beat shows the data model (alert→service→escalation policy→schedule→user→incident) and the two-API split. Design beat walks sanity check → trace routing → log entries for paged-why → From: header on mutations. Teardown names the five right calls and five bites. Handoff asks viewer to trigger a test incident and trace it through the full chain.
