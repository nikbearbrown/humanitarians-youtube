# QUESTION

**The question:** "Claude Plugins, Plugin Structure." — inside a Claude Code
plugin, a lot of paths point at the plugin's own files: a hook's command, an
MCP server's argument, a script reference. What do you write there so the
plugin still works after someone else installs it somewhere else entirely?
Answered using the `plugin-structure` skill's own portable-path rule
(`${CLAUDE_PLUGIN_ROOT}`) as the concrete case.

**Mode:** redo — source is
`anthropics/claude-plugins-official/youtube/claude-liam-plugin-structure/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`claude-plugins-official/plugins/plugin-dev/skills/plugin-structure/SKILL.md`.
7 beats — B00 cold open, B01 anatomy, B02 design/workflow, B05 teardown,
BVDT verdict, BHTF handoff, BOUT outro — B00 was already `ClaudeComposerAsk`
REMOTION, not AI-video/pantry, so NO-GENAI/NO-PANTRY LAW required no
substitution beyond the WRITER LAW swap). This reel keeps the question and
the source's body facts, re-registers the narration to Plain, replaces the
cold open with the Brutalist Hesitant Writer, folds the source's BVDT verdict
recap into a proper carry-out beat, restates the source's B05 "gets right /
bites" framing as a mechanism-and-both-directions fact instead of a design
judgment, and closes with the Humanitarians AI skin.

**Why it earns a reel:** A plugin's manifest, `plugin.json`, lives inside
`.claude-plugin/` and needs exactly one required field: `name`, in
kebab-case. Every component directory — `commands/`, `agents/`, `skills/`,
`hooks/`, `.mcp.json` — lives at the plugin's own ROOT, one level up, and
loads by auto-discovery: no registration step. The source names a third
rule with equal weight to the first two: every intra-plugin path reference —
a hook's command, an MCP server's argument, a script reference that crosses
a directory boundary — must be written through the `${CLAUDE_PLUGIN_ROOT}`
environment variable, never as a hardcoded absolute path and never as a path
relative to the working directory. The reason is concrete: plugins install
to different locations depending on install method, OS, and user
preference, and `CLAUDE_PLUGIN_ROOT` resolves to wherever THIS install
actually landed. A path written by hand, tested once on the author's own
machine, looks correct and works right up until the plugin is installed
somewhere else — at which point it points at nothing, silently. Command and
agent markdown files must mention the variable themselves for Claude to use
it there; hook JSON and MCP config pick it up as part of their own contract.

**Naive framing (B00, corrected on screen):** "My hook's path to its own
plugin's script — should it be a fixed address?" corrects "fixed" to
"portable" (the newcomer's default move, once a hook needs to find a file
inside its own plugin, is to just write down the path that works right now,
on the machine in front of them).

**Body facts carried from source (unchanged):**
- manifest `plugin.json` lives inside `.claude-plugin/`; one required field,
  `name`, kebab-case; everything else optional
- component directories (`commands/`, `agents/`, `skills/`, `hooks/`,
  `.mcp.json`) live at the plugin ROOT, not inside `.claude-plugin/`;
  auto-discovered by extension (commands/agents) or filename (skills'
  `SKILL.md`, hooks' `hooks.json`, `.mcp.json`)
- `${CLAUDE_PLUGIN_ROOT}` resolves to the plugin's actual install directory
  regardless of where on the system it landed — required for hook command
  paths, MCP server arguments, script references, any path crossing a
  directory boundary
- a hardcoded absolute path, or one relative to the working directory,
  works only on the machine that wrote it and breaks the moment the plugin
  installs somewhere else — silently, with nothing pointing at the cause
- command and agent markdown files must mention `${CLAUDE_PLUGIN_ROOT}`
  themselves for Claude to use it there — it is not injected automatically
  outside hook/MCP config
- source's Your Turn worked example: scaffold a plugin with a hook, a
  skill, and an MCP server, and check where the manifest sits, where the
  components sit, whether paths use `${CLAUDE_PLUGIN_ROOT}`, and whether the
  skill file is named exactly `SKILL.md`
