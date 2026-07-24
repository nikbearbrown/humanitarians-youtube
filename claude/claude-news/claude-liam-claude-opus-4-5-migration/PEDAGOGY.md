# PEDAGOGY — claude-liam-claude-opus-4-5-migration

## Skill reviewed
`anthropics/claude-code/plugins/claude-opus-4-5-migration/skills/claude-opus-4-5-migration/SKILL.md`

## What learners will be able to do
- Identify which model strings to replace across all four deployment platforms (Anthropic API, AWS Bedrock, Google Vertex AI, Azure AI Foundry)
- Know which models are excluded (Haiku) and which beta header to remove
- Apply the effort parameter addition as a migration step
- Use prompt adjustment triggers correctly — opt-in only, never applied by default
- Recognize the five known Opus 4.5 behavioral differences and when to act on each

## What makes this teachable
The platform matrix (4 platforms × 3 source models) is complete and paste-ready.
The Haiku exclusion is explicit and clearly stated.
The opt-in rule for prompt adjustments prevents silent breaking changes.
The five behavioral difference categories are named and distinguished clearly.

## Gaps the teardown surfaces
- Source model table has 3 platforms, target table has 4 — Azure AI Foundry has a target string but no source strings
- Prompt adjustment triggers are behavioral descriptions, not reproducible test cases ("reports tools called too frequently" is vague)
- "Integrate thoughtfully" has no examples of bad vs good integration placement
- Effort parameter deferred entirely to references/effort.md — no inline fallback if file is missing
- No rollback guidance — if migration breaks something, the skill offers only "let me know" with no structured recovery

## VERDICT: PASS

Platform matrix, Haiku exclusion, beta header removal, and opt-in prompt discipline are solid.
Teardown adds value by surfacing the Azure AI Foundry source-table gap and the vague behavioral triggers.
