# QUESTION

**The question:** "Claude just needs my PagerDuty API token, right?" — and
specifically: is one credential enough for everything Claude might do with
PagerDuty, or does part of it work a completely different way?

**Mode:** redo — source is
`anthropics/claude-tag-plugins/youtube/claude-liam-pagerduty-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel, 7 beats: `register:
"Teardown"`, `modifier: "skill-teardown"`, `brand: "claude-liam"`, cold open a
`ClaudeComposerAsk` typed ask, B01/B02 Remotion anatomy+design beats, B05 a
"gets it right / where it bites" teardown beat, `BVDT` a verdict artifact,
`BHTF` your-turn, `BOUT` `ClaudeTitleOutro`). This reel keeps the question and
the source's body facts, replaces the cold open with the Brutalist Hesitant
Writer, and closes with the Humanitarians AI skin.

**Why it earns a reel:** PagerDuty isn't one API with one credential — it's
two, on two different hosts, with two unrelated auth schemes. The REST API
(`api.pagerduty.com`) reads and manages everything — schedules, services,
escalation policies, incidents, users — with a `Token` header. Events v2
(`events.pagerduty.com`) triggers, acknowledges, and resolves alerts with a
`routing_key` field in the request body and no Authorization header at all.
Mix the two up and the failure mode isn't a clear error — it's a 401 with an
empty body, because curl shows nothing on failure unless you ask it to print
the status explicitly.

**Naive framing (B00, corrected on screen):** "Can Claude trigger a PagerDuty
alert with my API TOKEN?" → corrects "TOKEN" to "ROUTING KEY" (triggering runs
through Events v2, which authenticates with a routing key in the body, not
the Token header used everywhere else).

**Body facts carried from source (unchanged):**
- two separate APIs on two hosts: REST (`api.pagerduty.com`, `Authorization:
  Token token=<key>` — not Bearer, not Basic) for reading/managing; Events v2
  (`events.pagerduty.com`, `routing_key` in the JSON body, no Authorization
  header) for trigger/acknowledge/resolve
- the data model is a chain: an alert fires on a service, which routes
  through an escalation policy to schedules and users, opening an incident;
  log entries record who was notified, when, and through which channel —
  the authoritative record of who got paged and why
- sanity check first: `GET /v1/users/me` with the Token header; a 200 means
  the credential and host are right, a 401 comes back with an EMPTY body —
  curl shows nothing unless the HTTP status is printed explicitly (`-w` or
  `-o /dev/null -w`)
- every mutation (POST/PUT/PATCH/DELETE) needs a `From:` header with a real
  email address, or it returns a 400 that looks unrelated to the real cause
- raw curl calls to bracket-style filter params (`?user_ids[]=`) need `-g`/
  `--globoff`, or the filter gets silently mangled; the bundled
  `pd_oncall.sh` script already handles this
- reference objects in request bodies need both an `id` and a `type` field
  (e.g. `service_reference`), or the API returns a 400 naming the missing one
- Events v2 error responses are plain text, not JSON, so piping them through
  `jq` breaks immediately
- rate limits differ by API: REST gives 960 requests/minute with headers to
  watch; Events v2 has no per-request rate-limit header at all

**Deliberately reframed, not new:** the source's B05 "gets it right / where
it bites" list is a documentation-quality verdict — Teardown judgment on the
skill's own writing. Plain register keeps every fact in that list (folded
into NB03) but drops the verdict framing: this reel never rates the skill's
documentation, it only states what's true and what's easy to miss.
