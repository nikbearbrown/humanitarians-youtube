# PEDAGOGY — claude-liam-build-mcp-app

## Skill reviewed
`anthropics/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-app/SKILL.md`

## What learners will be able to do
- Route correctly: elicitation vs widget vs plain text
- Implement two-part registration (tool + resource)
- Inline the ext-apps bundle (mandatory for CSP)
- Use App class methods correctly (ontoolresult, sendMessage, updateModelContext)
- Write widgets that degrade gracefully without the apps surface

## What makes this teachable
The routing decision tree (text/elicitation/widget) prevents over-building.
The two-part registration has a clear mental model: tool returns data, resource serves HTML.
The silent failure modes (wrong MIME, no bundle inlining) are specific and learnable.

## Gaps the teardown surfaces
- Desktop cache flush (full quit required) buried in testing section
- CSP blank rectangle documented in reference file, not inline
- frameDomains restriction mentioned in footnote-sized table cell
- Wrong MIME type = silent blank rectangle, no explicit error documented
- sendMessage vs updateModelContext distinction after method list, not at decision point

## VERDICT: PASS

Routing table + two-part registration + bundle-inlining pattern are all complete.
Teardown adds value by surfacing the two silent failure modes prominently.
