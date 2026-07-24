# PEDAGOGY — claude-liam-claude-automation-recommender

## Skill reviewed
`anthropics/claude-plugins-official/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`

## What learners will be able to do
- Identify what each of the five automation types is for (Hooks, Subagents, Skills, Plugins, MCP Servers)
- Read codebase signals and match them to the right automation type and specific recommendation
- Apply the 1-2 per category discipline — not overwhelming users with a list of everything possible
- Use invocation control correctly: user-only / Claude-only / both and when to use each
- Know the skill is read-only: it analyzes and recommends, never creates files

## What makes this teachable
The five-type taxonomy is clean and covers the full Claude Code extensibility surface.
The signal-to-recommendation mapping tables make the skill concrete and learnable.
The 1-2 per category cap prevents the skill from becoming an undifferentiated dump.
The invocation control distinction (disable-model-invocation vs user-invocable:false) is subtle but important.

## Gaps the teardown surfaces
- "Go beyond the reference files" has no enforcement — model may stop at the reference tables
- Phase 1 bash commands assume standard file locations; no guidance for monorepos or non-standard layouts
- Subagent recommendations don't mention how to create agents — references/subagent-templates.md is not inline
- Plugin recommendations don't include installation commands — each requires a separate lookup
- Decision framework covers "when to recommend" but not "when NOT to recommend" each type

## VERDICT: PASS

Five-type taxonomy, signal tables, 1-2 discipline, and invocation control are all complete.
Teardown adds value by surfacing the reference-file-escape gap and the creation-vs-recommendation asymmetry.
