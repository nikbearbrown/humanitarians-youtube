# PEDAGOGY — claude-liam-asana-api

## Skill reviewed
`anthropics/claude-tag-plugins/asana/skills/asana-api/SKILL.md`

## What learners will be able to do
- Understand the Asana resource hierarchy (workspace → project → section → task → story)
- Apply the three universal rules to any Asana API call (gid, data envelope, opt_fields)
- Use the bundled asana_tasks.sh script for paginated task listing
- Know rate limits, error codes, and when search is and isn't appropriate

## What makes this teachable
The three rules (gid, data envelope, opt_fields) create a mental model that applies uniformly.
The 10 operations are concrete and cover 95% of real workflows.
The bundled script is a best-practice example of pagination handling.

## Gaps the teardown surfaces
- Auth placeholder logic is confusing outside the runtime context
- Premium search cap (100 results, no pagination) is easy to miss
- opt_fields available values require references/api.md — not discoverable inline
- Two different pagination models (offset vs created_at.before) differ silently

## VERDICT: PASS

Content is well-structured, concrete, and immediately applicable.
Teardown adds value by surfacing the premium/pagination gotchas.
