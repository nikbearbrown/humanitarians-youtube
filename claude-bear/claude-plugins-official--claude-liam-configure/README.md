# Saved Isn't Live. — The Configure Skill (Discord Plugin)

The Discord plugin's `configure` skill reads whatever argument you give it: no
arguments shows status, a token argument saves a credential, and the word
`clear` removes it. Two files do all the work — a credential file holding the
bot token, read once when the session starts, and an access file holding the
policy, re-read on every single incoming message. The design pushes hard
toward locking that policy down to an allowlist, and offers to flip that
switch itself once pairing has done its job. But one asymmetry is easy to
miss: save a new token and it doesn't take effect until you restart — while
updating the allowlist is live on your very next message. And the skill never
checks that what you paste actually looks like a token; it writes any string
to disk exactly the same way.

**Topic:** CONFIGURE · DISCORD PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-configure

---

## Chapters

0:00 The naive framing: "is a saved token live now?"
0:11 Three modes, two files
0:46 The lockdown rule
1:15 No validation
1:32 Carry-out
1:42 Your turn
1:59 Outro

---

## YOUR TURN

Open a Claude Code session with the Discord configure skill, and paste a
token that's obviously fake — something like `not-a-real-token`. Watch two
things: does it save that string without any complaint at all, and after you
tell it your allowlist is complete, does it offer to lock down access itself,
or does it wait for you to ask?

Run that today, on your own bot setup, not the video's example.

---

## Deliberately not claimed

No claim about what other keys besides the token may validly live in the
credential file, what the full `access.json` schema looks like, or how
Discord's own gates (the shared-server requirement, the Public Bot toggle)
work — the source Skill leaves those unspecified or unexplained, and this
video doesn't guess at them. This cut keeps the two facts a general viewer
needs and can act on: the restart-vs-instant asymmetry, and the missing
token validation.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
