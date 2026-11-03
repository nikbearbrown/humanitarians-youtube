# CARRY-OUT — GATE C

Written before any other narration. Every beat exists to make this sentence survivable.

## The line

> **Never hardcode a path inside a plugin. Write it through
> `${CLAUDE_PLUGIN_ROOT}`, so it still finds its way after the plugin is
> installed somewhere you'll never see.**

## The wrong guess it defeats

That a plugin's hook command, MCP server argument, or script reference can
just be the path that works right now, on the machine writing it. It can't —
plugins install to different locations depending on install method, OS, and
user preference, and a path typed by hand is only ever correct for the one
install it was tested against. The source names this rule with the same
weight as the manifest-location and component-location rules, and it fails
exactly the same way they do: silently. A hardcoded path doesn't error, it
just points at nothing on any other machine.

## The secondhand test

*If someone repeats only this sentence in a meeting next week, is it still true?*

Yes — it compresses the one distinction that matters (a path written by hand
survives one install; a path routed through the variable survives all of
them) without needing the full mechanism restated.

## What it deliberately does not say

- **Not a verdict on the design.** The source's B05 framed the placement
  rule, the `SKILL.md` naming requirement, the custom-path double-loading
  behavior, and the MCP-restart requirement as "what it gets right" /
  "where it bites" — Teardown language, including judgments about what the
  skill's documentation buries versus states plainly. Plain keeps the
  underlying facts (a hand-written path breaks silently on reinstall; the
  variable doesn't) but states them as a mechanism boundary, not a critique
  of the skill file.
- **Not that every source gap gets a beat.** The source names five gaps:
  the buried "most common mistake" framing on placement, custom-path
  double-scanning, the MCP-restart requirement, the exact-filename
  requirement for skills, and plugin-name collisions across installs. This
  reel foregrounds the portable-path rule as the anchor — compression for a
  7-beat Plain cut, not a factual change. The manifest/component placement
  split and the `SKILL.md` exact-filename rule are both stated in the body
  as supporting facts, not dropped.
- **Not a claim that hardcoded paths never work.** They work — on exactly
  one machine, the one that wrote them. The reel states that plainly before
  showing where it breaks.

---
**GATE C — signed:** ______________________  (human)
