# Reproduce First, Fix Last. — The Debug Skill (Structured Debugging Session)

A skill is a folder Claude reads before it acts, and `debug` is one of them:
its SKILL.md spells out a single job — run a structured debugging session —
reproduce, isolate, diagnose, then fix, always in that order. The session
only starts when Claude recognizes one of a few situations: an error message
or stack trace, "this works in staging but not in production," "something
broke after the deploy," or behavior that diverges from what's expected and
the cause isn't obvious. Run it twice on the same problem and you get the
same four steps in the same order — that's the guarantee. But the guarantee
only starts once your problem matches one of those triggers; describe
something outside that list, and the skill has nothing to say about it.

**Topic:** DEBUG · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-debug

---

## Chapters

0:00 The naive framing: "fix my code" vs. "debug it"
0:11 One file, one job
0:23 What starts the session
0:40 Repeatable, not universal
0:57 Carry-out
1:07 Your turn
1:22 Outro

---

## YOUR TURN

Paste this into Claude: I have a feature that works in staging but breaks in
production, and I don't know why. Read the debug skill and walk me through
what you will do — in order — before you start.

Watch whether it reproduces the problem first, or jumps straight to
guessing a fix. Run that today, on your own broken feature, not the
video's example.

---

## Deliberately not claimed

No claim that reproduce/isolate/diagnose/fix is the only valid way to debug
software — it's what this specific Skill's SKILL.md specifies. No claim
that Claude can debug anything: the session only fires on its stated
triggers, and outside that list this video makes no promise about what
happens. No design judgment on whether this is the "right" way to structure
a debugging session — Plain register describes the mechanism and stops.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #Debugging #LLM #HumanitariansAI #ProfessorBear

---
