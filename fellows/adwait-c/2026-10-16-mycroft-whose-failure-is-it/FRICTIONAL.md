# Frictional Log — Mycroft: Whose Failure Is It

**Week of 2026-10-16** · Adwait Changan · Mycroft track
Topic: red means something is wrong — it says nothing about *whose*.

**What I built this week**
- Faced a pull request that came back red: 11 merge conflicts and 19 failing checks.
- The useful skill wasn't fixing them, it was proving who owned them.
- 10 of 11 conflicts were another contributor's gateway work — took the base-branch version whole, then diffed to *prove* the result was unchanged rather than assume it.

**The one idea it teaches**
- The three answers to "whose failure is it?" call for completely different work, so proving ownership comes before fixing.

**Where it pushed back (and what I did)**
- The 19 failing checks reproduce on the base branch, so they were inherited and left alone.
- QC: a beat showed invented Python attributed to a real `.mjs` file. Replaced it with verbatim lines 45–59 of `conformance.mjs`, which actually contain the mapping the narration describes (this also needed two toolkit fixes).

**What I learned**
- "Verified unchanged" has to be shown by a diff, not claimed. Inherited failures aren't yours to fix.

_Hours this week: ~20 (across the two videos built this week)._
