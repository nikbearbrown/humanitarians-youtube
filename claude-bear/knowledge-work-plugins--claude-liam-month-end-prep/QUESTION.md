# QUESTION

**The question:** "Claude, Month End Prep." — when Claude runs the
month-end-prep skill, is it drawing on something it learned about closing
the books, or reading a file it opens fresh every time?

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-month-end-prep/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, `source_skill` pointing at the month-end-prep small-business
skill. 7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03 teardown
tell, BVDT verdict, BHTF handoff, BOUT outro — all already REMOTION, no
puppet/AI-video/pantry beat to replace beyond the WRITER LAW swap). This
reel keeps the question and the source's body facts, re-registers the
narration to Plain, replaces the cold open with the Brutalist Hesitant
Writer, folds the source's BVDT verdict recap into a proper carry-out beat,
and closes with the Humanitarians AI skin.

**Known gap in the source, logged honestly:** the source sheet's own
per-skill description field never got filled in for month-end-prep — B03's
narration reads `"Claude's job: >."` and BHTF's reads `"I want to >."`,
literal unfilled template placeholders (sibling reels in the same batch,
e.g. `close-management` and `journal-entry-prep`, got their descriptions
filled; `month-end-prep` and `month-heads-up`'s missing text is specific to
this one). The source SKILL.md itself
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/month-end-prep/SKILL.md`)
lives on a machine this build cannot reach. Rather than invent the specific
month-end checklist steps the file might contain, this redo carries forward
only the facts the source sheet actually states about the *mechanism* —
what a Skill is, how it executes, and what it guarantees — and does not
fabricate the business-specific content of month-end-prep's steps.

**Why it earns a reel anyway:** the mechanism claim is the actually
interesting one for a general audience meeting Claude Skills for the first
time — that a Skill is a folder Claude reads before it acts (a `SKILL.md`
file plus a reference folder), that it executes the Steps section linearly,
and that running it is deterministic (same file, same steps, every run) but
bounded (nothing beyond what the file says). That claim is fully supported
by the source's B01/B02/BVDT beats independent of the missing per-skill
description.

**Naive framing (B00, corrected on screen):** "How does Claude learn a
skill like month-end-prep?" → corrects "learn" to "read" (there is no
training step; Claude opens the same SKILL.md file fresh, every time it
runs the skill).

**Body facts carried from source (unchanged):**
- a Skill is a folder Claude reads before it works; month-end-prep's folder
  holds a `SKILL.md` (the full instruction set, plain language) plus a
  `reference` folder — "the file is the program"
- the pipeline lives in the Steps section: Claude reads each step in order
  and executes it, linearly, no branching unless a step itself says so
- the verdict/limit, restated without judgment: same input, same output,
  every run; the boundary is exactly what the file says, nothing outside it
- Your Turn: paste a prompt asking Claude to read the month-end-prep skill
  and narrate each step it's about to take, tracing every action back to a
  specific line in the file — the same "explain before acting" move as the
  source's own handoff, adapted to test the mechanism claim directly.
