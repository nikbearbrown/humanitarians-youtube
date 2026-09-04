# PPTX

Ask Claude to build a slide deck, and the natural guess is that it's one
script — write python-pptx and go. It isn't. The PPTX skill routes across
three paths depending on the task: markitdown to read or analyze a deck,
an edit workflow for reworking an existing template, and pptxgenjs to
create one from scratch. And the natural follow-up guess — since
pptxgenjs builds a deck, it can also edit one — breaks too: editing means
unpacking the slide XML directly, no library involved. Design is
mandatory, not optional: one dominant color at 60-70% of the visual
weight, one motif carried through every slide, a dark-light sandwich
structure, and never an accent line under a title — a known tell for
AI-generated slides. Watch one concrete ask — a five-slide investor pitch
deck for a carbon-capture startup — go in, get built against those rules,
and come back out right. And it doesn't ship until a subagent has
actually looked at the rendered slides.

**Topic:** PPTX · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-pptx

---

## Chapters

0:00 The naive framing: "do you need to learn python-pptx?"
0:10 Three paths, one skill
0:23 The ask, planted: a five-slide pitch deck
0:34 One tool, both jobs? — the wrong guess
0:43 It's slide XML, not a library — the case that breaks it
0:53 Designed for this deck, not any deck
1:06 One motif, dark-light sandwich
1:17 Never an accent line under a title
1:27 Two-stage QA, assume problems
1:42 The anchor returns: the same deck, now shipped right
1:56 What the QA pass catches
2:08 Known failures, not all failures — one flag
2:22 Carry-out
2:32 Your turn
3:04 Outro

---

## YOUR TURN

Create a 5-slide investor pitch deck for a climate tech startup that makes
carbon-capture hardware. Bold design — pick a palette that feels specific
to this topic, commit to one visual motif, use the dark-light sandwich
structure. Use the PPTX skill.

Then watch: does it read pptxgenjs.md before writing any code? And after
it generates, does it run visual QA — render the slides and inspect them
with a subagent — before calling it done? Check the slides themselves
too: is there an accent line under any title? If so, the design rules
were skipped.

---

## Deliberately not claimed

The source skill file logged in the source sheet's metadata
(`../anthropics/skills/skills/pptx/SKILL.md`) could no longer be located at
that path by the time of this build — the skills tree has been
reorganized since. Facts are carried over unchanged from the locked source
script (the three-path routing, the design rules, the two-stage QA
mandate, the accent-line tell) rather than re-verified against a live
skill file, per this series' redo contract.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #LLM #HumanitariansAI #ProfessorBear
