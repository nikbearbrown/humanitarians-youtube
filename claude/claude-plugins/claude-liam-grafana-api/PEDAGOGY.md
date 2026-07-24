# PEDAGOGY — claude-liam-grafana-api

## Skill reviewed
`anthropics/claude-tag-plugins/grafana/skills/grafana-api/SKILL.md`

## What learners will be able to do
- State the three time formats: Unix milliseconds (ds/query + annotations), Unix seconds (state-history), RFC-3339 (silences)
- Distinguish the two alert rule surfaces: live state (Prometheus API, read-only) vs definitions (provisioning API, full CRUD)
- Understand that datasource query errors are embedded in results.<refId>.error — not reflected in HTTP status
- Know that dashboard updates require GET-then-full-replace, not partial PATCH
- Batch multiple queries[] into one /api/ds/query request instead of looping

## What makes this teachable
The time-unit inconsistency at the top of the skill is the right opening — it's the failure mode that produces silent empty results rather than errors, making it hard to diagnose. The two alert rule surfaces distinction prevents writing to the wrong endpoint. The data-frame response model is a non-obvious abstraction.

## Gaps the teardown surfaces
- grafana() helper is session-only — not a persisted script, referenced throughout operations
- GNU vs BSD date for silence creation: a one-line comment doesn't cover the macOS case well enough for reliable use
- Provisioning lock caveat (X-Disable-Provenance: true) appears at the end of the alert rules section, easy to miss
- The "grafana" literal in the Alertmanager alert rule URL path is not obviously a literal — looks like a placeholder
- /api/annotations pagination: no page param, time-window narrowing is documented but the constraint isn't surfaced upfront

## VERDICT: PASS

Time-unit inconsistency flagged at the top before operations is exactly right — it's the silent-empty-result failure mode. Two alert rule surfaces separated cleanly. Datasource error-in-200-response documented. Dashboard PUT-replaces-all documented. The grafana() session-only helper and GNU/BSD date discrepancy are the key teachable gaps.
