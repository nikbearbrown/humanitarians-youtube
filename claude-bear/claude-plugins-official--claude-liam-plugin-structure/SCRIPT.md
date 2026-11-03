# Claude Plugins, Plugin Structure. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone wiring a plugin's hook figures a fixed address will do — it works on their machine. It's wrong: a plugin's path needs to survive being installed anywhere. So — should that address be fixed, or portable?" | BrutalistHesitantWriter — types "A hook's path to its own plugin's script — should it be a fixed address?", corrects "fixed" → "portable" |
| B01 | 1 stakes / 2 wrong guess | A plugin's manifest — plugin.json — lives inside .claude-plugin, and needs exactly one field: name, in kebab-case. Everything else — commands, agents, skills, hooks, even an MCP server file — lives at the plugin's own root, auto-discovered, no registration step. So it's tempting to wire a hook or an MCP server with the exact path on your machine. That path is only ever right on your machine. | a manifest card inside a .claude-plugin folder; four sibling folders at root; a hook command field typing out a machine-specific /Users/... path |
| B02 | 3 mechanism / **4 anchor planted** | There's a variable for exactly this: CLAUDE_PLUGIN_ROOT. It resolves, at runtime, to wherever this plugin is actually installed on this machine — Claude Code fills it in. Write a hook's command as CLAUDE_PLUGIN_ROOT slash scripts slash check dot sh, and it finds the script no matter where the plugin lives. The same rule covers MCP server arguments and any script reference that crosses a directory boundary. | THE ANCHOR — the same hook command field, the hardcoded path struck out, CLAUDE_PLUGIN_ROOT/scripts/check.sh typing in beside it |
| B03 | **4 anchor payoff / 5 both directions** | Install the same plugin on a teammate's machine, somewhere else entirely. The hook written with CLAUDE_PLUGIN_ROOT still finds its script and runs. The one with a hardcoded path points at a folder that doesn't exist there — and just doesn't fire, with nothing telling you why. Written through the variable, a path survives any install location. Typed by hand, it works only on the machine that wrote it. | THE ANCHOR RETURNS — same hook, on a second machine's install; the variable version lights green and runs, the hardcoded version dims to nothing, no error shown |
| **BCRY** | **6 carry-out** | Never hardcode a path inside a plugin. Write it through CLAUDE_PLUGIN_ROOT, so it still finds its way after the plugin's installed somewhere you'll never see. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Scaffold a plugin with a pre-tool-use hook that calls a helper script, and an MCP server with a startup argument pointing at a local file. Watch two things when Claude answers: does the hook's command path use CLAUDE_PLUGIN_ROOT, or a path typed straight from this machine? And does the MCP server's argument do the same? Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude Plugins, Plugin Structure. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the manifest/root split and the temptation to hardcode a path; CLAUDE_PLUGIN_ROOT itself waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (a fixed address will do); B03 falsifies it directly with a second install where the hardcoded version silently fails |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documentation of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (the same hook command, written two ways, tested on a second machine) |
| Both directions | B03 — written through CLAUDE_PLUGIN_ROOT, the path survives any install location (holds); typed by hand, it works only on the machine that wrote it (flips) |
| No design judgment | B03 states the portability rule and its silent failure mode as a fact about how the variable resolves, never a verdict on whether the skill's documentation should have led with it |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the placement
  rule, the `SKILL.md` naming requirement, the custom-path double-loading
  behavior, and the MCP-restart requirement as "what it gets right" /
  "where it bites" — Teardown language. Plain keeps the same underlying
  facts where they're used (a hand-written path breaks silently on
  reinstall; the manifest/component split is real; `SKILL.md` must be
  spelled exactly) but states them as mechanism boundaries, not a critique
  of the skill file.
- **Not that every source gap gets a beat.** The source names five gaps:
  the buried placement-mistake framing, custom-path double-scanning, the
  MCP-restart requirement, the exact-filename requirement for skills, and
  plugin-name collisions across installs. This reel foregrounds the
  portable-path rule as the anchor — compression for a 7-beat Plain cut,
  not a factual change. The manifest/component placement split and the
  `SKILL.md` requirement both appear in the body as supporting facts.
- **No claim that a hardcoded path never works.** B01 states plainly that
  it works, on the machine that wrote it, before showing where it breaks.

## Handoff prompt (BHTF, read aloud)

> "Scaffold a plugin with a pre-tool-use hook that calls a helper script,
> and an MCP server with a startup argument pointing at a local file."

Why it's worth running: watching whether Claude writes the hook's command
path and the MCP server's argument through `${CLAUDE_PLUGIN_ROOT}` rather
than a path specific to this machine surfaces whether the portability rule
from B01–B03 actually lands.

---
**GATE P — signed:** ______________________  (human)
