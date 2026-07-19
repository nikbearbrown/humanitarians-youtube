# PEDAGOGY — skill-development

VERDICT: PASS

## What the learner walks away knowing

1. Three-level progressive disclosure: metadata (~100 words, always) → SKILL.md body (<5k, on trigger) → bundled resources (as needed).
2. Description format: third-person + specific trigger phrases. "This skill should be used when the user asks to [phrase1], [phrase2]..." — not vague.
3. Body format: imperative/infinitive form, 1,500-2,000 words, detailed content in references/, always reference resources.
4. Three resource types: scripts/ (deterministic code), references/ (docs loaded when needed), assets/ (output files not loaded to context).
5. 6-step creation: understand → plan → create → edit → validate → iterate.

## Where the skill is incomplete

- Trigger mechanism never explained: does Claude match description text or use LM judgment? Affects how to write descriptions.
- Understand step has no systematic discovery technique — just "ask questions."
- skill-reviewer agent mentioned but invocation and checklist underdocumented.
- Reference loading trigger ("as needed by Claude") implied autonomous mechanism not documented.
