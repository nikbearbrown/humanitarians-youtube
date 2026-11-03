# The Prompt Is The Deliverable. — The Playground Skill (Claude Plugins)

The skill organizes around six templates across four zones — design,
data, learning, and review — and every playground has to meet five core
requirements: one self-contained HTML file, a live preview that updates
with no Apply button, a copy button, three to five ready-made presets, and
a prompt written in natural language instead of a dump of values. The whole
thing runs on one invariant: a single state object — every control writes
to it, every part of the preview reads from it, and one function refreshes
both the preview and the prompt together. Here's the catch: nothing in the
skill actually stops the value-dump output from happening. Whether the
prompt reads as a natural instruction or as a colon-separated list of
settings is left entirely to whoever writes the code — which is exactly why
opening the finished file in a browser is a required last step, not an
afterthought.

**Topic:** PLAYGROUND · CLAUDE PLUGINS
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-playground

---

## Chapters

0:00 The naive framing: "does it hand back values?"
0:09 Six templates, four zones
0:48 One state object
1:24 Nothing enforces it
1:46 Carry-out
1:56 Your turn
2:23 Outro

---

## YOUR TURN

Paste this into Claude: build an interactive playground for designing a
card component — border radius, shadow, padding, and color — with a live
preview and a copyable prompt. Then check what comes out: does the prompt
read like an instruction, or like a printout of numbers? Does every control
update the preview instantly, with no button to click? Are there at least
three presets already in place when it loads? And does opening the file in
a browser actually work?

Run that today, on your own component idea, not the video's example.

---

## Deliberately not claimed

No claim about how Claude decides which template to use when a request
could fit more than one — the source Skill names no disambiguation rule for
that case, and this video doesn't invent one. No claim that a value-dump
prompt is common in practice or rare in practice — only that nothing in the
skill's own design prevents it, which is a fact about the design, not a
measurement of outcomes.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
