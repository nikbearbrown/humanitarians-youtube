# PEDAGOGY — claude-liam-datadog-api

## Skill reviewed
`anthropics/claude-tag-plugins/datadog/skills/datadog-api/SKILL.md`

## What learners will be able to do
- State the v1/v2 resource split: v1 for metrics, monitors, dashboards, SLOs; v2 for logs, events, spans, incidents
- Know the two required headers: DD-API-KEY and DD-APPLICATION-KEY — both injected
- Know regional site configuration and that the wrong site returns 403 with valid credentials
- Understand the `curl -g` globoff requirement for bracketed params like `page[size]`
- Recognize three distinct pagination schemes: cursor (v2 search), page number (v1 monitors), offset (v2 collections)

## What makes this teachable
The v1/v2 split is explicit — not "use the newer one" but "use whichever version has your resource."
The regional site configuration with sanity check is a concrete first step before any operation.
The `curl -g` requirement is called out prominently — missed globoff kills requests silently.
The three pagination schemes are named and assigned to specific endpoints.

## Gaps the teardown surfaces
- Only one bundled script (dd_logs.sh) — all other operations are raw curl with no write helpers for monitors/dashboards
- Dashboard PUT replaces the whole document — the warning exists but is a single sentence, easy to miss
- Double `.attributes` on events (`data[].attributes.attributes.title`) is genuinely confusing and not highlighted
- Spans endpoint follows JSON:API envelope; logs endpoint does not — same v2, different shape, asymmetry causes 400s
- `date` command for downtime end time has different syntax GNU vs BSD/macOS — noted in a comment only

## VERDICT: PASS

Security note, v1/v2 routing by resource, regional site check, globoff requirement, and three pagination schemes are well-specified.
Single bundled script and the JSON:API envelope asymmetry between spans and logs are the key teachable gaps.
