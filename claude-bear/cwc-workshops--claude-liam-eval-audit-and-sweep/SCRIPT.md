# SCRIPT — Claude's Eval Skill: Audits First, Sweeps Second

*Reel: cwc-workshops--claude-liam-eval-audit-and-sweep*
*Skill: `hai-simple`. Register: **Plain** — explain, then stop.*
*Voice: Liam (Kokoro am_onyx), in for Bear.*
*Redo of: `anthropics/cwc-workshops/youtube/claude-liam-eval-audit-and-sweep` (Teardown → Plain; same skill, facts re-grounded directly against the source SKILL.md, judgment removed).*

---

## B00 — HESITANT WRITER (Remotion)

*(Writer types the naive claim, hesitates on "sweeps", corrects to "audits",
then lands the real question.)*

**Liam:** "A newcomer might expect Claude's eval skill to jump straight into
sweeping models for the best one. It doesn't — it audits the eval first. So
what does audit-and-sweep actually do?"

---

## S01 — Stakes

You want to know which Claude model gives you the best results for the least
cost, and you reach for a skill built for exactly that: eval-audit-and-sweep.

---

## S02 — Wrong Guess (planted)

The natural read: hand it your eval, ask which model wins, and it runs
straight into the sweep — model versus model, cost versus quality, done.

---

## S03 — ANCHOR PLANTED

*(THE ANCHOR. This exact order returns at S08.)*

Hold onto the order the skill actually enforces: audit first, sweep second.
Ambiguous request or not, that order doesn't move.

---

## S04 — Break the Wrong Guess

Ask it to skip straight to the sweep, and it won't — a sweep run over a
broken eval produces misleading numbers, so audit goes first.

---

## S05 — Mechanism (part 1)

There's no runnable script inside. Claude reads your actual eval code, reads
the audit and sweep reference files, and writes the glue code your specific
setup needs.

---

## S06 — Mechanism (part 2)

First it locates your eval — the golden set, the scoring function, the one
command that runs a full pass.

---

## S07 — Mechanism (part 3)

The audit is a health check: task design, harness design, metric hygiene,
and whether the grader itself is biased.

---

## S08 — ANCHOR PAYOFF

*(THE ORDER RETURNS — same sequence as S03.)*

Only once the audit clears does the sweep run — the full grid, every
accessible model against every parameter setting, never trimmed down early.

---

## S09 — Both Directions (A)

With two or more models cleared for access, the grid genuinely answers which
model wins — cost against quality, side by side.

---

## S10 — Both Directions (B)

It flips the moment only one model survives that access check — now the grid
can only rank that model's own settings, not the field.

---

## BCRY — Carry-Out (Remotion)

Eval-audit-and-sweep audits the eval before it ranks models — and it only
answers "which model" when more than one model actually made the grid.

---

## BHTF — Your Turn (Remotion)

Your turn. Here's the prompt — read it with me: "Read the
eval-audit-and-sweep skill, and tell me: if I ask you to find my cheapest
model that still passes, what do you check before you ever run the sweep,
and why?" Liam, in for Bear.

---

## BOUT — Outro (Remotion)

Claude's Eval Skill: Audits First, Sweeps Second. Liam, in for Bear.

---

## Six-move audit

| Move | Beat | Law |
|---|---|---|
| 1 stakes first | S01 | ✓ |
| 2 wrong guess, falsified by a case | S02 (planted) → S04 (broken by: skipping to the sweep, which the skill refuses because a sweep over a broken eval gives misleading numbers) | WRONG-GUESS LAW ✓ |
| 3 mechanism | S05–S07 | ✓ |
| 4 anchor planted + paid off | S03 → S08 (the audit-then-sweep order, enforced) | ANCHOR LAW ✓ |
| 5 both directions | S09 + S10 | BOTH-DIRECTIONS LAW ✓ |
| 6 carry-out | BCRY | CARRY-OUT LAW ✓ |
| one flag | — none needed | see below |

## Deliberately not claimed

- **No inference flag.** Every claim here restates the source SKILL.md's own
  text directly: the two independent phases; audit-before-sweep when the
  request is ambiguous or both, "because a sweep over a broken eval produces
  misleading numbers" (SKILL.md step 2, near-verbatim); no runnable scripts,
  Claude reads the user's eval code and reference files and writes glue
  (SKILL.md's own framing, paragraph 2); locating the golden set/scoring
  function/entrypoint (step 1); the audit checklist naming task design,
  harness design, metrics hygiene, and grader/judge bias (step 3); the sweep
  as a full, non-trimmed cross-product grid (step 4, "do not invite the user
  to trim it"); and the <2-models boundary condition, where the skill itself
  says the result "will only rank parameter settings within one model, not
  answer 'which model'" (step 4, near-verbatim). Nothing here is this reel's
  inference about evals in general, so ONE-FLAG LAW correctly produces zero
  flags.
- **No design verdict.** The source's BVDT "verdict" beat recapped and
  implicitly praised the design ("makes Claude execute one task reliably…
  know the limit"). It had also invented a claim not in the skill file — that
  "the sweep grid is a ranked artifact; the production system under real load
  is a different world" — which reads as the source's own added lens
  (confirmed against its REBUILD-LOG.md, which names this a deliberately
  authored "Popper/Plato" philosophical framing, not a source-file quote).
  This redo drops that invented claim entirely rather than carrying it
  forward as fact, and BCRY here states only what the file itself says —
  the audit-before-sweep order and the model-count boundary — then stops.
- **No invented UI or tool names.** `eval-audit-and-sweep`, `audit.md`,
  `sweep.md`, and `tau2-bench.md` are named because the source SKILL.md names
  them; nothing new is invented.
- **Beat count expanded from the source's 7 (B00–B03, BVDT, BHTF, BOUT) to
  14.** Plain register's mandatory structure — a planted-and-broken wrong
  guess, a planted-and-paid-off anchor, an explicit both-directions pair —
  needs its own beat per move, and the facts themselves were re-derived from
  the primary SKILL.md source rather than compressed from the Teardown cut's
  3-beat body.
