# PEDAGOGY — claude-liam-hook-development

## Skill
hook-development (claude-plugins-official / plugin-dev)

## Learning objective
Understand the two Claude hook types (Prompt-Based and Command), the two config formats (plugin hooks.json vs settings), and the critical restriction that prompt hooks only work on 4 of the 9 lifecycle events.

## Prior knowledge assumed
Knows what Claude plugins are; has seen hooks mentioned in passing.

## Key concepts
1. Two hook types: Prompt-Based (LLM-driven, recommended) vs Command (bash, deterministic)
2. Two config formats: Plugin hooks.json wrapper vs Settings direct format
3. 9 hook events — but prompt hooks restricted to 4: PreToolUse, Stop, SubagentStop, UserPromptSubmit
4. Hooks load at session start — no hot-swap
5. All matching hooks run in parallel — no ordering, no shared state

## VERDICT: PASS

Hooks are useful, the skill covers the mechanics correctly. The key gap to surface:
prompt hooks are recommended without stating the 4-event restriction upfront.
