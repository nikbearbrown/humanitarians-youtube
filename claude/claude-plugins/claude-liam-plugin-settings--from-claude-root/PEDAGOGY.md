# PEDAGOGY — plugin-settings

VERDICT: PASS

## What the learner walks away knowing

1. Plugin settings live in `.claude/plugin-name.local.md` — YAML frontmatter for structured config, markdown body for prompts/context.
2. Three consumers: bash hooks (sed parsing), commands (Read tool), agents (instructions reference).
3. Quick-exit pattern: check file exists → check enabled → exit 0. Never assume file present means active.
4. Three patterns: hook toggle, agent state management, configuration-driven behavior.
5. Restart required for changes — not hot-swapped. Gitignore `.claude/*.local.md` always.

## Where the skill is incomplete

- Restart requirement buried in Best Practices, not in the overview.
- `sed` frontmatter parser breaks silently on multiline YAML or quoted colons.
- Gitignore entry has no enforcement — manual step documented but no install hook creates it.
- Body-as-prompt pattern (ralph-wiggum loop) shown but not explained.
