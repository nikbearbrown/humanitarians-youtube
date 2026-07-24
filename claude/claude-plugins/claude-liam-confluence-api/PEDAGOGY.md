# PEDAGOGY — claude-liam-confluence-api

## Skill reviewed
`anthropics/claude-tag-plugins/confluence/skills/confluence-api/SKILL.md`

## What learners will be able to do
- State the two-version routing rule: v2 for everything except CQL search, attachment upload, and label add (those use v1)
- Know the `/wiki` prefix is mandatory — missing it returns 404, not an auth error
- Identify the three bundled scripts: cql_search.sh (search), read_page.sh (read), write_page.sh (create/update)
- Understand the pagination URL relativity trap: v2 `_links.next` is site-root-relative, v1 is `/wiki`-root-relative
- Recognize the prompt injection security note and know never to follow instructions from retrieved content

## What makes this teachable
The two-version model is explicit — v2 default, v1 only where v2 has no equivalent.
The three bundled scripts have concrete flag-by-flag documentation with exit codes.
The pagination URL relativity trap is the rare kind of production gotcha that is explicitly documented.
The security note at the top makes prompt injection a visible concern, not a footnote.

## Gaps the teardown surfaces
- `/wiki` prefix warning is buried mid-paragraph — not a prominent callout
- `atlas_doc_format` value-is-a-JSON-string trap documented in body-formats but not repeated in write_page.sh docs
- v2 list default limit (25–50) vs max (250) gap can silently truncate results
- Hard delete (`?purge=true`) requires space-admin — the restriction is easy to miss
- Attachment upload requires `X-Atlassian-Token: nocheck` header — if missing, XSRF protection blocks silently

## VERDICT: PASS

Security note, two-version routing, three bundled scripts, and pagination URL trap are well-specified.
The `/wiki` prefix warning placement and atlas_doc_format gotcha location are the key teachable weaknesses.
