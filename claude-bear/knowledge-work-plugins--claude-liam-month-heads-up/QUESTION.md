# QUESTION

**The question:** "Claude, Month Heads Up." — when Claude runs a named
business skill like `month-heads-up`, did Claude write a custom program
to do it, or is something else going on?

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-month-heads-up/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, 7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro — all already REMOTION, no
puppet/AI-video/pantry beat to replace beyond the WRITER LAW swap).

**Source is clean, unlike some siblings in this batch:** the source's B00
carries the skill's full job description without truncation: "Runs on the
25th — shows the next 30-day cash-flow outlook and flags anything that
needs attention before month-end. Accepts optional 30 or 60 day horizon."
(Later beats — B03, BVDT, BHTF — repeat a truncated copy of the same
phrase, a template-length artifact in the source's batch build, not a
missing fact: the full line survives intact in B00, so nothing here is
invented.) B01's `files` list confirms the folder holds exactly one item:
`SKILL.md`, ~2k, no `reference/` folder for this skill (unlike some
siblings, e.g. `cash-flow-snapshot`, which does carry one) — this redo
keeps that distinction rather than copying the sibling's shape.

**Why it earns a reel:** the natural assumption about any named Claude
"skill" is that Claude programmed it — wrote custom logic to handle this
one task. It didn't. `month-heads-up`, like every Agent Skill, is one file
on disk: a `SKILL.md` (~2k) — plain language, not code. Claude reads that
file and executes what it says, one step at a time, in the order the Steps
section lists them, with no branching unless a step itself says so. The
skill's own job description gives this reel a genuine textured detail most
siblings lack: an optional parameter (a 30- or 60-day horizon) rather than
just a bare repeat-the-same-request case. Run the check on the 25th with
the default 30-day horizon and it comes back identical every time nothing
changes; switch the horizon to 60 days and the output changes too — same
fixed steps, different input, not different logic.

**Naive framing (B00, corrected on screen):** "Claude built the
month-heads-up skill. Right?" → corrects "built" to "reads" (Claude did
not write this skill's cash-flow logic on the fly; a human already wrote
the instructions, and Claude reads and follows them).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works, not code it writes
- `month-heads-up`'s folder holds exactly one file: `SKILL.md` (~2k,
  plain language) — no hidden script, no `reference/` folder
- the pipeline lives in the Steps section; Claude executes each step in
  order — linear, no branching unless a step says so
- the skill's job: runs on the 25th, shows the next 30-day cash-flow
  outlook, flags anything needing attention before month-end; accepts an
  optional 30- or 60-day horizon
- same input → same output, every run — the whole guarantee a skill makes
- switching the horizon parameter changes the output without changing the
  underlying steps — still determinism, just a different input
- Your Turn: ask Claude to read the skill's own `SKILL.md` before running
  it and explain the steps back, in order, in its own words

**Deliberately not claimed:** anything about the skill's actual formulas
or how it computes "cash-flow outlook" internally — the source states only
that Claude reads the Steps section and executes them in order; it never
specifies the arithmetic, and neither does this reel.
