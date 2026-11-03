# Draft, Not Send. — The Handle Complaint Skill

A skill is a folder Claude reads before it works — this one, a single
SKILL.md file, about two kilobytes, plain language, no hidden logic. Its
job, word for word: pulls context on the complaint, drafts a response, and
suggests an operational fix, with an optional email or ticket ID as input.
Once triggered, Claude reads the Steps section and runs each one in order.
That's a draft-and-suggest tool, not a resolve-it tool: run the same
complaint through twice and you get the same kind of response and the same
kind of fix, every time — but Claude never sends the reply or makes the
fix itself, and anything the SKILL.md doesn't spec is outside what it does.

**Topic:** HANDLE COMPLAINT · KNOWLEDGE WORK PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-handle-complaint

---

## Chapters

0:00 The naive framing: "will Claude send the reply?"
0:11 A folder, not a program
0:27 How it gets picked up
0:43 Drafts and suggests, not sends
1:00 Carry-out
1:10 Your turn
1:26 Outro

---

## YOUR TURN

Paste this into Claude: I want to handle an incoming customer complaint —
read the handle-complaint skill and walk me through what you will do before
you do it. That clause matters: having Claude explain itself first, before
it acts, is how you actually see the draft and the fix it's proposing, not
just the result.

Run that today, on a complaint you're actually looking at, not the video's
example.

---

## Deliberately not claimed

No claim about how Claude's underlying dispatch mechanism matches a
request against a description (pattern-match vs. model judgment) — the
source Skill's SKILL.md doesn't document that internal mechanism, and this
video doesn't guess. No claim about what "operational fix" can cover beyond
what the job description states (a suggestion returned alongside the
drafted response) — the skill is never described as implementing that fix.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #CustomerService #LLM #HumanitariansAI #ProfessorBear

---
