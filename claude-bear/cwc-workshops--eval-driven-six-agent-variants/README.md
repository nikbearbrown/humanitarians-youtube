# Six Agent Variants: How to Measure What Prompt Changes Actually Do

You keep editing a slide-writing Claude agent's prompt, and the natural read
is to open the new deck next to the old one — if it looks cleaner, ship it.
A glance won't catch a nine-point caption sitting under a ten-point floor,
though; a code grader parses the file itself and catches that in
milliseconds. The eval runs in two layers: code checks that parse the deck
file directly (slide count, images present, clutter, font size, emoji — no
model call), then an LLM judge that scores the rendered slides on text,
imagery, layout, color, and title-body coherence. Four rounds build on a
naive baseline — typography, a mandatory diagram, then a QA loop where the
agent rasterizes and inspects its own deck — all against the same five fixed
tasks and the same pinned baseline. Then one round breaks the pattern
entirely: it drops every prompt rule and swaps the model instead. Check the
diagram grader again, and it's empty — that rule only ever lived in the
prompt.

**Topic:** CLAUDE BASICS · AGENT EVALS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--eval-driven-six-agent-variants

---

## Chapters

0:00 The naive framing: "my new prompt looks better. Done."
0:10 Stakes: a prompt, edited again, across five tasks
0:19 The wrong guess: glance in, glance out, ship it
0:27 The anchor: the mandatory-diagram grader
0:36 Broken, with a case: a font-size floor a glance can't catch
0:48 Mechanism: layer one, the code checks
1:00 Mechanism: layer two, the LLM judge
1:10 Mechanism: three rounds, each adding one rule
1:25 The anchor returns: the diagram check, empty again
1:38 Both directions (A): a code fail, proven at parse time
1:47 Both directions (B): all checks pass, judge still needed
1:57 Carry-out
2:06 Your turn
2:27 Outro

---

## YOUR TURN

Take an agent you're iterating on. Freeze one fixed test set of real inputs,
write one code check that's just a plain fact — present or not — and one
rubric a judge model can score from the rendered result. Run every version,
including one where you swap the model instead of the prompt, against that
same test and the same pinned baseline. What actually moved, and what only
looked like it moved?

---

## Deliberately not claimed

This is a redo of a Teardown-register cut of the same workshop. That source
narrated a six-step cumulative score climb (42% to 81%, via a "ReAct
reasoning loop, memory store, critic pass, tool planning, output
formatting") — none of which appears in the workshop's own repository, which
builds a PowerPoint-writing agent, not a ReAct/tool-planning agent, and
contains no recorded run scores at all. This reel drops that invented
waterfall and rebuilds the mechanism from the workshop's own files: 7 code
graders and 5 LLM-judge graders (`src/graders/all.ts`), a fixed 5-task test
set (`tasks.json`), a pinned-baseline delta mechanism, and four real rounds
(`01-polish`, `02-diagram`, `03-qa-loop`, `04-model-swap` — the last
explicitly described in its own file as testing "the model lever vs the
prompt lever"). No beat in the body asserts a specific total variant count,
since the workshop repo supports five configurations (a baseline plus four
rounds), not six; the given title is kept as the episode's name. Full
accounting in BUILD-LOG.md and QUESTION.md.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no
account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and
Remotion (motion graphics). No human-performed audio or video in this
production.*

#AI #ClaudeAI #ClaudeSkills #AgentEvals #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
