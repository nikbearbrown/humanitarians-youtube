# Right Format, No Function. — What a Slash Command File Actually Is

A Claude slash command file is five frontmatter fields — name, description,
argument-hint, allowed-tools, and model — sitting above a body. Whatever you
type after the command's name lands verbatim in one slot called ARGUMENTS.
The body itself follows a parse-perform-report shape, but in the reference
example that shape is only described, not carried out: running it produces
the template, not real action. Matching the format exactly doesn't prove the
command does anything; skipping an optional field (like argument-hint)
doesn't mean it's broken, either. A single-file legacy layout
(`commands/<name>.md`) loads exactly the same way — only the file location
differs.

**Topic:** SLASH COMMANDS · CLAUDE PLUGINS
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-example-command

---

## Chapters

0:00 The naive framing: "already works, right?"
0:10 The shortcut you want
0:18 The wrong guess most newcomers make
0:27 Break it: running the reference file
0:40 Five fields
0:50 The anchor planted: $ARGUMENTS
1:03 argument-hint
1:12 allowed-tools
1:24 model override
1:34 The body pattern
1:46 The anchor returns
1:57 One flag, and the legacy layout
2:12 Direction A: format isn't proof
2:21 Direction B: optional isn't broken
2:30 Carry-out
2:41 Your turn
2:59 Outro

---

## YOUR TURN

Paste this into Claude: build me a real slash command called /word-count.
It should take a file path as its required argument, count the words in
that file, and report the total back to me. Show me the exact SKILL.md
file you'd write for it, and then explain, in plain terms, what ARGUMENTS
actually contains the moment I run it.

Run that today, on your own command idea, not the video's example.

---

## Deliberately not claimed

No claim about which model — haiku, sonnet, or opus — to pick for a given
command, or what the cost and capability tradeoffs are; the source
skill lists the option without guidance, and this video doesn't guess at
one. No claim about Bash's blast radius inside allowed-tools, or about how
to narrow a tool list to least privilege — that's a design judgment on the
reference file's choices, not a fact a newcomer needs to run their first
command. No claim about description-length limits or phrasing for slash
help display. These were the source Teardown's design gaps; this cut keeps
only the facts a general viewer can act on.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
