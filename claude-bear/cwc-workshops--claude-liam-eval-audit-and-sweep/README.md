# Claude, Eval Audit And Sweep.

Ask Claude's eval-audit-and-sweep skill which model is cheapest and best for
your task, and the natural read is that it jumps straight into a model-vs-model
sweep. It doesn't. Ask it to skip straight to the sweep and it refuses — a
sweep run over a broken eval produces misleading numbers, so the skill audits
the eval first: locating the golden set, the scoring function, and the
one-pass command, then checking task design, harness design, metric hygiene,
and grader bias. Only once that audit clears does the sweep run — the full
grid, every accessible model against every parameter setting, never trimmed
down early. And the grid's answer is bounded by what actually made it in: with
two or more models cleared for access it genuinely ranks models against each
other, but with only one model cleared, it can only rank that model's own
settings, not the field.

**Topic:** CLAUDE BASICS · EVAL AUDIT & SWEEP
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--claude-liam-eval-audit-and-sweep

---

## Chapters

0:00 The naive framing: "it just sweeps for my best model?"
0:10 Stakes: cheapest model that still passes
0:18 The wrong guess: straight to the sweep
0:26 The anchor: audit first, sweep second
0:34 Broken, with a case: a sweep over a broken eval misleads
0:42 Mechanism: no script inside, just files to read
0:51 Locating the eval: golden set, scorer, one-pass command
0:58 The audit checklist: task, harness, metrics, grader bias
1:04 The anchor returns: audit clears, sweep unlocks
1:13 Both directions (A): two-plus models, a real answer
1:20 Both directions (B): one model, settings only
1:28 Carry-out
1:37 Your turn
1:49 Outro

---

## YOUR TURN

Read the eval-audit-and-sweep skill, and tell me: if I ask you to find my
cheapest model that still passes, what do you check before you ever run the
sweep, and why?

Run that today, against your own eval.

---

## Deliberately not claimed

Every claim in this reel restates the source SKILL.md's own text directly:
the two independent phases; audit-before-sweep on any ambiguous-or-both
request, because a sweep over a broken eval produces misleading numbers; no
runnable scripts — Claude reads the user's eval code and reference files and
writes the glue; locating the golden set, scoring function, and entrypoint;
the audit checklist naming task design, harness design, metric hygiene, and
grader bias; the sweep as a full, non-trimmed grid; and the boundary where
fewer than two models means the result only ranks settings within one model,
not "which model." This redo drops a claim the source Teardown cut had added
on top of the skill file — "the sweep grid vs. production under real load" —
because that framing is not in the skill's own text. See BUILD-LOG.md for the
full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AgentSkills #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
