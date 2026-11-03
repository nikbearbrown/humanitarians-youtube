# Stale, Not Broken. — The Debug-Plugins Skill (Claude Tag Plugin)

Before deciding anything, this diagnostic checks three things in order:
what actually arrived in the plugin mount, what flags Claude Code was
launched with, and what the startup log recorded — all collected before
any explanation is offered. Then it walks a short list of causes: the zip
isn't there, it's there but the launcher didn't pass a matching flag, it
failed to extract, the manifest is malformed (often just a stray capital
letter or space in the name), or the zip is fine but the skill file's own
header is broken. Two limits worth knowing: a session reads your
configuration once, when it starts — flip a setting mid-chat and the fix
is a new conversation, not a refresh — and some startup errors go to a
channel this diagnostic can't see, so a clean-looking log isn't proof
nothing went wrong.

**Topic:** DEBUG PLUGINS · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-debug-plugins

---

## Chapters

0:00 The naive framing: "is my config broken?"
0:10 Three steps, in order
0:24 Five failure causes
0:41 Two limits
1:01 Carry-out
1:12 Your turn
1:36 Outro

---

## YOUR TURN

Paste this into Claude Code: A plugin zip is sitting in
/mnt/account-plugins, but the skill inside it isn't showing up. Walk me
through what actually arrived, what you were launched with, and what the
startup log says, before telling me what's wrong. Then check three things:
does it collect all three before explaining anything? Does it say so if
the log file is missing? And if you flipped the setting a few minutes ago,
does it ask for a fresh conversation?

Run that today, on your own plugin, not the video's example.

---

## Deliberately not claimed

No claim about the internal security handling the source Skill documents
(treating log content as untrusted, preferring Read/Grep over cat) — this
video is about what a general user sees when a plugin doesn't show up, not
about the harness-internals audit a developer of the skill itself would
need. No claim that these five causes are exhaustive for every possible
Claude Code plugin failure; they're the failure ladder this particular
Skill version enumerates.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
