# PEDAGOGY — claude-liam-bigquery-api

## Skill reviewed
`anthropics/claude-tag-plugins/bigquery/skills/bigquery-api/SKILL.md`

## What learners will be able to do
- Understand the BigQuery job model (billing project, two execution modes, location pinning)
- Use bq_query.sh for both sync and async queries with cost controls
- Know the critical DONE ≠ success invariant (check status.errorResult)
- Use tabledata.list for free row previews
- Navigate the non-uniform pagination field names across endpoints

## What makes this teachable
The job model is concrete and well-motivated. The two invariants (DONE ≠ success, location always)
are clearly called out in the skill and worth amplifying as the primary rules.
The free preview operation is a genuinely useful tip.

## Gaps the teardown surfaces
- Pagination field name split (pageToken vs nextPageToken) is mentioned but easy to miss
- Nested/repeated f/v cell encoding unexplained with examples
- totalRows ≠ stop condition (counterintuitive, not highlighted)
- Auth placeholder fiction confusing outside runtime
- Write-heavy jobs deferred to references/api.md without inline preview

## VERDICT: PASS

Solid job model documentation, critical invariants explicit, bundled script is reference-quality.
Teardown adds value by amplifying DONE ≠ success and surfacing pagination split.
