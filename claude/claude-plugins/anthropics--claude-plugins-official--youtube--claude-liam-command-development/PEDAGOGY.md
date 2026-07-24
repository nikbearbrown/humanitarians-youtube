# PEDAGOGY — claude-liam-command-development

## Skill reviewed
`anthropics/claude-plugins-official/plugins/plugin-dev/skills/command-development/SKILL.md`

## What learners will be able to do
- Write slash commands as directives TO Claude, not messages TO the user
- Choose the right command location (project / personal / plugin) for the use case
- Use the five frontmatter fields (description, allowed-tools, model, argument-hint, disable-model-invocation) correctly
- Use $ARGUMENTS (full string) vs $1/$2 (positional) arguments and @ file references
- Use CLAUDE_PLUGIN_ROOT for portable plugin commands that work across installations

## What makes this teachable
The "commands are instructions FOR Claude" framing is the most-teaching-worthy distinction in the skill — most beginners write messages to the user instead.
The three-location taxonomy (project/personal/plugin) maps cleanly to scope.
The five frontmatter fields each have specific use-cases and defaults.
CLAUDE_PLUGIN_ROOT solves a concrete problem (hardcoded paths) with a named solution.

## Gaps the teardown surfaces
- Bash execution syntax (! backtick) is the most-used command feature but is deferred entirely to references/plugin-features-reference.md with no inline example
- The legacy format note (.claude/commands/ → .claude/skills/<name>/SKILL.md) is buried in a Note block, not prominently flagged
- $IF conditional syntax in argument validation examples — not a real template language; could be misread as actual syntax
- Bash(git:*) namespace scope rules are shown but not explained (why gitonly? what does the colon-star mean?)
- Plugin command auto-discovery from commands/ directory is stated but not compared to skills/ discovery

## VERDICT: PASS

"Commands are instructions FOR Claude" framing, three locations, five frontmatter fields, and CLAUDE_PLUGIN_ROOT are all solid.
Teardown adds value by surfacing the bash-deferral gap and the legacy-format burial.
