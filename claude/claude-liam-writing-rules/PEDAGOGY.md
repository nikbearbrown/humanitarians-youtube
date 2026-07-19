# PEDAGOGY — writing-rules

VERDICT: PASS

## What the learner walks away knowing

1. Rule file format: `.claude/hookify.{name}.local.md` — YAML frontmatter + markdown body; read dynamically on every tool use.
2. Five frontmatter fields: name (kebab-case, verb-first), enabled (bool), event (bash/file/stop/prompt/all), action (warn default / block), pattern or conditions.
3. Four event types: bash (command strings), file (Edit/Write/MultiEdit), stop (completion checks), prompt (user input).
4. Simple vs advanced: single pattern field OR conditions array (field + operator + pattern, ALL must match).
5. Message body: explain what detected, why problematic, suggest alternatives.
6. Pitfalls: too-broad patterns (log → catalog), too-specific (full path), YAML escaping (unquoted recommended).

## Where the skill is incomplete

- block action: described but never demonstrated — what does Claude/user actually see when blocked?
- stop/prompt condition fields: no documentation of available fields (stop_reason? user_prompt only?)
- Rule execution order: undefined — do multiple matching rules all fire? In what order?
- `all` event type: listed but no example, no performance/ordering note.
