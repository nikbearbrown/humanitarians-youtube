# QUESTION

**The question:** "Claude, Cash Flow Snapshot." — when Claude runs a named
business skill like `cash-flow-snapshot`, did Claude write a custom program
to do it, or is something else going on?

**Mode:** redo — source is
`anthropics/knowledge-work-plugins/youtube/claude-liam-cash-flow-snapshot/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, `audience:
"Claude"`, 7 beats — B00 cold open, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro — all already REMOTION, no
puppet/AI-video/pantry beat to replace beyond the WRITER LAW swap).

**Source defect, disclosed:** the source's batch-build pipeline substitutes
a per-skill "job" phrase into a template slot (visible as `>` in this
sheet — e.g. B03: *"Claude's job: >."*). For most sibling skills in this
same batch (e.g. `financial-statements`) that slot filled correctly; for
`cash-flow-snapshot` it never did — every occurrence in the delivered
source is a bare `>`. No local copy of the skill's own `SKILL.md` exists on
this machine to recover the missing line (its path in the source metadata,
`/Users/bear/Documents/CoWork/.../small-business/skills/cash-flow-snapshot/SKILL.md`,
resolves on a different machine, not this one). **This redo does not
invent that missing line.** It never claims what fields or formulas a
"cash flow snapshot" specifically produces — only the mechanism the
source's own *other* beats already state as confirmed fact: a skill is a
folder Claude reads (not code Claude writes), the pipeline runs the Steps
section top to bottom, and the same input produces the same output every
time. Because nothing in this reel is inference beyond what the source
itself asserts elsewhere, **no ONE-FLAG beat is needed** — see CARRY-OUT.md
"what it deliberately does not say."

**Why it earns a reel:** the natural assumption about any named Claude
"skill" is that Claude programmed it — wrote custom logic to handle this
one task. It didn't. `cash-flow-snapshot`, like every Agent Skill, is two
files on disk: a `SKILL.md` (the source's own build measured it at ~6k) —
plain language, not code — plus a `reference/` folder. Claude reads that
file and executes what it says, one step at a time, in the order the Steps
section lists them, with no branching unless a step itself says so. Run
the same request twice and the same steps run twice, producing the same
output both times. That determinism is the whole guarantee a skill makes;
it is also the whole limit — only what the file says.

**Naive framing (B00, corrected on screen):** "Claude built the
cash-flow-snapshot skill. Right?" → corrects "built" to "reads" (Claude
did not write this skill's logic on the fly; a human already wrote the
instructions, and Claude reads and follows them).

**Body facts carried from source (unchanged):**
- a skill is a folder Claude reads before it works, not code it writes
- `cash-flow-snapshot`'s folder holds exactly two things: `SKILL.md`
  (~6k, plain language) and a `reference/` folder — no hidden script
- the pipeline lives in the Steps section; Claude executes each step in
  order — linear, no branching unless a step says so
- same input → same output, every run — the whole guarantee a skill makes
- the limit is only what the file says — nothing outside the spec
- Your Turn: ask Claude to read the skill's own `SKILL.md` before running
  it and explain the steps back, in order, in its own words

**Deliberately not claimed:** the specific fields, formulas, or output
shape of an actual cash flow snapshot — that line did not survive into the
source, and no other copy of the skill exists on this machine to verify
it. See CARRY-OUT.md.
