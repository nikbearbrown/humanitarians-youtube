# PEDAGOGY — claude-liam-agent-development

Skill: agent-development (Claude Code)
Register: Teardown (skill-teardown modifier)

## What the skill does
Claude Code plugin agent creation: YAML frontmatter (name, description, model, color, optional tools) + markdown body as system prompt. Description field is the critical trigger — must have "Use this agent when" + 2-4 example blocks (Context/user/assistant/commentary).

## Key concepts
- Agents = autonomous multi-step; Commands = user-initiated
- description = most critical field; no examples = no reliable triggering
- model: inherit by default; color: 6 semantic options; tools: least privilege
- System prompt: 2nd person, 5-section structure (Responsibilities/Process/Standards/Output/EdgeCases)
- Two creation paths: AI-assisted JSON prompt or 9-step manual

## VERDICT: PASS
