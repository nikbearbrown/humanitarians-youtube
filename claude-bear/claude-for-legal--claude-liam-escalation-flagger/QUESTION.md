# QUESTION

**The question:** "Claude, Escalation Flagger." — when Claude runs a Skill
named `escalation-flagger`, is the call to flag something for human
escalation Claude's own judgment about what looks risky, or is it a match
against criteria written down somewhere a person could read? Answered
using the general mechanism every Claude Skill shares (a folder, one
`SKILL.md`, criteria checked step by step) with `escalation-flagger` as the
named example.

**Mode:** redo — source is
`anthropics/claude-for-legal/youtube/claude-liam-escalation-flagger/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata
`register: "Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/commercial-legal/skills/escalation-flagger/SKILL.md`
— a path that exists only on the original build machine and is not
reachable from here). 7 beats — B00 cold open, B01 anatomy, B02 pipeline,
B03 design tell, BVDT verdict, BHTF handoff, BOUT outro.

**Source defect found on read (logged per the honesty rule):** four of the
source's seven beats carry a literal, unfilled `>` character sitting
exactly where `escalation-flagger`'s own specific content should have been
substituted in — B00 ("The skill is escalation-flagger. **>**. A SKILL.md
tells Claude exactly how."), B03 ("Claude's job: **>**. What it gets
right..."), BVDT ("The SKILL.md is the spec — **>**. Same input, same
output..."), and BHTF ("Paste this into Claude: 'I want to **>**. Read the
escalation-flagger skill...'"). This is the same batch-build
template-substitution defect class already found and logged on this
family's `auto-updater` and `amendment-history` siblings (both confirmed
against `anthropics/BUILD-SKILL-EXPLAINERS-LOG.md`'s 2026-07-25 batch,
shipped straight to "DONE ✓" with the placeholder never filled), not a
stylistic choice — the source never actually states what
`escalation-flagger` specifically checks for, what counts as an escalation
trigger, or who/what it escalates to. The real
`commercial-legal/skills/escalation-flagger/SKILL.md` is unreachable from
this machine, so those specifics cannot be recovered here.

**What this redo keeps and what it does not invent:** every fact the
source's readable text DOES establish is kept unchanged and generalized —
a Skill is a folder Claude reads before it works; its `SKILL.md` is the
full instruction set in plain language, not hidden logic ("the file is the
program"); the pipeline lives in a Steps section, read top to bottom,
linear, no branching unless a step says so; run the same input through it
twice and you get the same result both times; the guarantee holds only for
what the file actually describes. Per hai-simple's "when in doubt, describe
behavior generically" rule, this reel builds entirely on those
generic-but-true facts about how a Claude Skill works, using
`escalation-flagger` only as the *name* of the example skill — it never
states what specific criteria trigger a flag, or what the escalation
target is, since the source never actually said so and the real file is
unreachable. The one thing taken directly from the skill's own name (not
invented) is its category of behavior: it checks an input against written
criteria and flags matches for a human — that much is what "flagger" means
on its face, the same way `auto-updater`'s redo could say it "updates
something automatically" without stating what.

**Naive framing (B00, corrected on screen):** "Claude's escalation flagger
— is it flagging things it thinks are risky?" → corrects "thinks" to
"matches" (the newcomer's default read of a flag going off is that Claude
made a judgment call — sensed risk the way a person would; the correction
is that the flag fires on a match against criteria written in `SKILL.md`,
not on Claude's own read of the situation).

**Body facts carried from source (unchanged, generalized to any Skill):**
- a Claude Skill is a folder Claude reads before it works; this one is
  named `escalation-flagger`
- its `SKILL.md` is the whole instruction set, written in plain sentences,
  not code — "the file is the program"
- the pipeline lives in a Steps section; Claude reads each step (each
  criterion) in order and checks it, linear, no branching unless a step
  says so
- remove a criterion from that file and inputs that used to match it stop
  getting flagged — nothing hidden fills the gap
- run the same input through it twice and you get the same match and the
  same flag both times
- that guarantee holds only for input inside what the file describes;
  outside it, nothing gets flagged — not because Claude judged it safe, but
  because nothing in the file matched
