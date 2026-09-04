# The Script, Not The Understanding.

Ask whether Claude's `workshop` skill guarantees a participant actually
understands Claude Managed Agents, and the natural read is: if the skill's
own file coaches you correctly, you've learned it. The SKILL.md itself
answers this directly. It's a coach, not a builder — "You are the
participant's coach for this workshop... move them through WORKSHOP.md one
act at a time," across seven acts (zero through six), in one of two modes:
you drive while Claude hints, or Claude makes the change and walks you
through it after. Either way, the file fixes something else entirely: even
when a step breaks, Claude is explicitly barred from reading the solutions
folder or the project's git history for the fix — it checks the real
documentation and the error message instead, fixes forward, and explains
what changed, the same explanation it gives when a step just works. That
explanation always has a fixed five-part shape: what changed, why it works,
the platform concept it demonstrates, where to see it, one thing to try.
That shape is the artifact. Whether the participant actually walks away
understanding how a managed agent works is a different thing, and no text
file can promise that part.

**Topic:** WORKSHOP · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--claude-liam-workshop

---

## Chapters

0:00 The naive framing: "does Claude's skill do the workshop for me?"
0:10 Anatomy: a skill is a folder (7 acts, 2 modes, 1 file)
0:26 Mechanism: no peeking at the answer key — both directions (step works / step breaks)
0:50 The script, and the learning: the file fixes the explanation shape, not the grasp
1:09 Carry-out
1:16 Your turn
1:37 Outro

---

## YOUR TURN

Paste this into Claude: Write a short, five-part coaching file — what
changed, why it works, the concept it shows, where to see it, one thing to
try — for walking someone through fixing an off-by-one bug in a for loop.
Follow those exact steps to coach me through one I'll paste in. Then ask me
to explain the fix back in my own words, and tell me honestly whether that
proves I understood it, or just that I could repeat you.

Run that today, against a bug you actually have sitting open.

---

## Deliberately not claimed

Every claim in this reel restates the `workshop` Skill's own SKILL.md text
directly (mirrored, unchanged, at
`/Users/nik/Documents/Cowork/anthropics/cwc-workshops/research-desk/.claude/skills/workshop/SKILL.md`):
the coach framing ("You are the participant's coach for this workshop"),
the seven acts numbered zero through six, the two modes ("coach me" vs. "do
it and teach me", chosen once and remembered in the progress file), the
fixed five-part explanation shape, and the explicit bar on reading
`solutions/` or git history when a step fails. This redo drops the source
Teardown cut's generic "Read SKILL.md → Execute → Return output" pipeline
diagram — true of any skill, not specific to this one — and its
design-tell verdict framing ("what it gets right… what it bites"),
replacing both with the no-solutions-folder mechanism and the
both-directions pair (step works / step breaks), stated without judgment.
See BUILD-LOG.md for the full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
