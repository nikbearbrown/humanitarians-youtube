# Claude, Dpa Review. — The DPA-Review Skill

When Claude reviews a vendor's Data Processing Agreement, it isn't
approving the agreement — it's reading a Skill. A Skill is a folder with
one instruction file, SKILL.md, written in plain language: no hidden
logic, no freeform judgment. Claude reads it, then executes each step in
order — read the file, execute the steps, return the result — linear, no
branching unless a step says otherwise. One rule inside this particular
Skill is specific: check whether the agreement names every sub-processor,
and states what happens to the data when the contract ends — deleted, or
returned. Those two clauses go missing most often. What the Skill can't do
is judge whether the described security measures are actually strong
enough for the data involved. Claude isn't judging whether the agreement
is good enough. It's checking the SKILL.md's list of required clauses, one
step at a time, and only doing what that file says.

**Topic:** DPA-REVIEW · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-for-legal--claude-liam-dpa-review

---

## Chapters

0:00 The naive framing: "does Claude approve it, or check clauses?"
0:10 A Skill is a folder
0:24 Read, execute, return
0:35 What the checklist covers
0:55 Carry-out
1:05 Your turn
1:19 Outro

---

## YOUR TURN

Paste this into Claude: I'm about to sign a vendor's data processing
agreement. Read the dpa-review skill, and before you check anything, walk
me through exactly what you'll do — which clauses you'll check for, what
counts as missing, and what you won't be able to tell me.

Run that today, on your own agreement, not the video's example.

---

## Deliberately not claimed

No claim about what any specific DPA will say in a real case — the
mechanism (a named folder, one instruction file, a linear pipeline, one
specific clause-checklist rule) holds regardless of the agreement
involved. No claim that Claude replaces a privacy lawyer's review; the
video states the opposite throughout — Claude checks the file's list, and
the file's list is the limit.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudeForLegal #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
