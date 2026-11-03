# What Does a Feature-Risk-Assessment Actually Tell You?

Asking Claude to run a feature-risk-assessment before a feature ships can
sound like asking for a safe/not-safe verdict. It isn't one. Take a feature
that looks harmless on a quick look — users upload a photo ID to prove
their age. The checklist asks a different question: where does that photo
go, how long is it kept, who can see it. Read the SKILL.md, work through it
step by step, and what comes back is four filled-in boxes — what's
collected, where it's stored, how long it's kept, who can access it — not
a judgment. All four boxes filled doesn't mean the feature is safe, and one
flag raised doesn't mean it gets killed. Either way, someone now has what
they need to decide.

**Topic:** FEATURE RISK ASSESSMENT · WORKING WITH CLAUDE
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-feature-risk-assessment

---

## Chapters

0:00 Claude, will you approve this new feature?
0:11 A quick look vs. a checklist
0:30 The anchor — four boxes, two blank
0:49 Filled in is not safe
1:09 Carry-out
1:15 Your turn
1:30 Outro

---

## YOUR TURN

"Walk through the feature I'm building or reviewing right now: what data it
touches, where that data is stored, how long it's kept, and who can access
it — before telling me whether it's fine."

That's the whole checklist: what, where, how long, who — documented, then
decided by a person.

---

## Deliberately not claimed

This reel is a partial reconstruction: most of the source reel's
skill-specific facts were never actually written (its narration carried
literal unfilled template placeholders, and the SKILL.md file it pointed at
doesn't exist on this machine — see QUESTION.md). The two facts the source
did state outright (a skill is one file, SKILL.md, read before Claude acts;
a linear read-execute-return pipeline) are kept. The checklist mechanism is
illustrated with a generic, uncontroversial anchor (a photo-ID upload and
four questions — what, where, how long, who) rather than inventing this
specific skill's real checklist fields or its legal domain's specifics.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AIagents #AgenticAI #LegalTech #HumanitariansAI #ProfessorBear #ClaudeBasics

---
