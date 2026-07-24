# PEDAGOGY — claude-liam-example-command

## Skill reviewed
`anthropics/claude-plugins-official/plugins/example-plugin/skills/example-command/SKILL.md`

## What learners will be able to do
- Name the five frontmatter fields: name, description, argument-hint, allowed-tools, model
- Understand that $ARGUMENTS is the injection point where user-provided text reaches the skill body
- Know that argument-hint provides UX affordance for slash command arguments shown to the user
- Recognize that allowed-tools pre-approves tools for a skill, reducing permission prompts
- Understand that skills/<name>/SKILL.md and commands/<name>.md are equivalent — same loading, different layout

## What makes this teachable
The skill is self-referential — it demonstrates the format by being an example of the format.
Five frontmatter fields are all present with their names and purposes, giving a complete schema reference.
The legacy equivalence note matters for teams migrating from commands/ to skills/ layout.

## Gaps the teardown surfaces
- No functional behavior: the skill body is documentation only; invoking it produces just the three-step template
- model override values (haiku, sonnet, opus) listed but no guidance on when to choose which
- $ARGUMENTS parsing left entirely implicit — no example of split, validation, or defaults
- Bash in allowed-tools has wide blast radius; no note on scoping or minimal-permission principle
- No guidance on writing a good description for /help display (length, phrasing, what gets shown)

## VERDICT: PASS

Five frontmatter fields documented, $ARGUMENTS injection point shown, legacy equivalence noted, allowed-tools pre-approval practical implication stated.
The skill is a format reference, not a functional demo — that's by design, but the gaps are real for anyone building their first skill from this template.
