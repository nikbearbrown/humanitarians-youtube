# PEDAGOGY — claude-liam-config-guide

## Skill reviewed
`anthropics/claude-tag-plugins/claude-tag-troubleshoot/skills/config-guide/SKILL.md`

## What learners will be able to do
- Name the four layered configuration objects (@Claude: agents, agent scopes, identity profiles, presets/connections/repos/instructions)
- Know which reference file to reach for each topic area
- Recognize that this is an index skill — not self-contained
- Know to suggest debug-plugins in a new Slack thread after explaining configuration
- Identify the Slack-only scope caveat

## What makes this teachable
The four-layer model is named and the resolution chain is referenced explicitly.
The index pattern (5 short reference files instead of one long SKILL.md) is itself teachable — good skill design.
The debug-plugins handoff is a concrete next step that closes the loop.

## Gaps the teardown surfaces
- Index pattern fails silently if any of the 5 reference files is missing — no fallback
- "Currently written for Slack surface" has no guidance on what differs for other surfaces
- Topic table describes files but not what answers they give — "agents-and-scopes.md" tells you nothing without opening it
- No mention of required admin permissions for the person configuring @Claude
- Debug-plugins handoff says "new Slack thread" without explaining why (container isolation — state changes per thread)

## VERDICT: PASS

Four-layer model, index pattern, Slack-scope caveat, and debug-plugins handoff are all correctly documented.
Teardown adds value by surfacing the silent-failure risk of the index pattern and the missing admin-permissions note.
