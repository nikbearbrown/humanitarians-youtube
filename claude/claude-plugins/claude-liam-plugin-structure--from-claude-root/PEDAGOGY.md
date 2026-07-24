# PEDAGOGY — plugin-structure

VERDICT: PASS

## What the learner walks away knowing

1. Manifest goes in `.claude-plugin/plugin.json`; component dirs (commands/, agents/, skills/, hooks/) at plugin root — not inside .claude-plugin/.
2. Auto-discovery: .md files → commands/agents, subdirs with SKILL.md → skills, hooks.json → hooks. No registration step.
3. `${CLAUDE_PLUGIN_ROOT}` for all intra-plugin path references in hooks and MCP config — never hardcode.
4. Only required manifest field is `name` (kebab-case). Custom paths supplement defaults, not replace.
5. SKILL.md is the exact required filename — misname produces silent failure.

## Where the skill is incomplete

- Placement rule (manifest in .claude-plugin/, components at root) is mentioned once in Critical Rules but not reinforced throughout.
- Custom paths supplement defaults — can cause double-loading if both exist; not explained.
- Restart guidance inconsistent with hook-development skill.
- Command name collision between plugins: no resolution mechanism documented.
