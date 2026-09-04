# SCRIPT — How to Measure What a Prompt Change Actually Did

*Reel: cwc-workshops--eval-driven-six-agent-variants*
*Skill: `hai-simple`. Register: **Plain** — explain, then stop.*
*Voice: Liam (Kokoro am_onyx), in for Bear.*
*Redo of: `anthropics/cwc-workshops/youtube/eval-driven-six-agent-variants` (Teardown → Plain; facts re-grounded directly against the workshop repo, the source's invented six-step waterfall dropped — see QUESTION.md).*

---

## B00 — HESITANT WRITER (Remotion)

*(Writer types the naive claim, hesitates on "looks", corrects to "scores",
then lands the real question.)*

**Liam:** "A newcomer tweaks their agent's prompt, looks at the new deck,
and calls it better. That's a glance, not a measurement. So what does
actually testing a prompt change look like, round after round?"

---

## S01 — Stakes

You've got a Claude agent that writes slide decks, and you keep editing
its system prompt hoping each version beats the last — for five different
topics, every time.

---

## S02 — Wrong Guess (planted)

The natural read: open the new deck, glance at it next to the old one,
and if it looks cleaner, ship it — glance in, glance out, decision made.

---

## S03 — ANCHOR PLANTED

*(THE ANCHOR — the diagram rule and its check. This exact check returns
at S08.)*

Hold onto one rule: every slide has to carry a real diagram, not just
text and boxes — and one grader does nothing but count whether that
actually happened.

---

## S04 — Break the Wrong Guess

But a glance won't catch a nine-point caption sitting under the
ten-point floor on slide four — a code grader parses the file's actual
font sizes and catches it in milliseconds, no eyeballing required.

---

## S05 — Mechanism (part 1)

The eval runs in two layers. Layer one is code — parsing the deck file
itself: slide count, images present, cluttered slides, tiny fonts, stray
emoji. No model call, pass or fail in milliseconds.

---

## S06 — Mechanism (part 2)

Layer two hands the rendered slide images to an LLM judge, scoring text,
imagery, layout, color, and whether the title actually matches the body
underneath it.

---

## S07 — Mechanism (part 3): the rounds

Round one just tightens typography and trims word count. Round two adds
that mandatory diagram. Round three adds a QA loop — the agent rasterizes
its own deck, inspects every slide for overlap and overflow, fixes what
it finds, and checks again before it's done.

---

## S08 — ANCHOR PAYOFF

*(THE DIAGRAM CHECK RETURNS — same grader, opposite result.)*

Then round four breaks the pattern entirely — it drops every one of
those rules and goes back to the plain prompt, just on a stronger model.
Check that same diagram grader, and it's empty again: that rule only
ever lived in the prompt.

---

## S09 — Both Directions (A)

When a code check fails — no diagram, a caption under the size floor —
that's a concrete defect, proven the moment the file's parsed, no
judgment call needed.

---

## S10 — Both Directions (B)

But every code check passing doesn't mean the deck is good — a slide can
hit every rule and still not explain the idea, which is exactly what the
LLM judge is there to catch.

---

## BCRY — Carry-Out (Remotion)

Score every version against the same fixed test and the same pinned
baseline — a rule that only lives in the prompt doesn't survive a model
swap.

---

## BHTF — Your Turn (Remotion)

Your turn. Here's the prompt — read it with me: "Take an agent I'm
iterating on. Freeze one fixed test set of real inputs, write one code
check that's just a plain fact — present or not — and one rubric a judge
model can score from the rendered result. Run every version, including
one where I swap the model instead of the prompt, against that same test
and the same pinned baseline. What actually moved, and what only looked
like it moved?" Liam, in for Bear.

---

## BOUT — Outro (Remotion)

Six Agent Variants: How to Measure What Prompt Changes Actually Do.
Liam, in for Bear.

---

## Six-move audit

| Move | Beat | Law |
|---|---|---|
| 1 stakes first | S01 | ✓ |
| 2 wrong guess, falsified by a case | S02 (planted) → S04 (broken by: a font-size floor violation invisible to a glance, caught by the code grader in milliseconds) | WRONG-GUESS LAW ✓ |
| 3 mechanism | S05–S07 | ✓ |
| 4 anchor planted + paid off | S03 → S08 (the mandatory-diagram grader: present under the polish/diagram/QA-loop rounds, empty again once the model-swap round drops the prompt rule) | ANCHOR LAW ✓ |
| 5 both directions | S09 + S10 | BOTH-DIRECTIONS LAW ✓ |
| 6 carry-out | BCRY | CARRY-OUT LAW ✓ |
| one flag | — none needed | see below |

## Deliberately not claimed

- **No inference flag.** Every claim restates the workshop repo's own
  files directly: the 7 code graders and 5 LLM-judge graders
  (`src/graders/all.ts`); the fixed 5-task test set (`tasks.json`); the
  pinned-baseline delta mechanism (`src/eval-runner.ts`, "Deltas always
  compare against the pinned baseline… not the immediately-previous run");
  the four rounds' actual rule changes (`solutions/01-polish` through
  `04-model-swap.agent.yaml`, including `04-model-swap`'s own description:
  "Tests the model lever vs the prompt lever"). Nothing here is this
  reel's inference about agent evals in general, so ONE-FLAG LAW correctly
  produces zero flags.
- **No fabricated numbers.** The source's B06 beat (`CwcVariantImprovement
  Waterfall`) narrated a cumulative 42%→81% climb across "ReAct reasoning
  loop, memory store, critic pass, tool planning, output formatting" — none
  of which exists in the workshop repo (a PowerPoint-writing agent, not a
  ReAct/tool-planning agent), and no `runs/` directory with actual scores
  exists to source any percentage from. This redo states the real
  mechanism and the real four round names and drops every invented number
  and label. See QUESTION.md for the full accounting.
- **The given title is kept, the count is not asserted in the body.** The
  source's title and this reel's SUBJECT.json both say "Six Agent
  Variants." The workshop repo supports five real configurations (a naive
  baseline plus four solution rounds), and the fourth is explicitly a
  lever-isolation test, not a sixth stacked prompt tweak. Rather than
  repeat a count the primary source doesn't support, no beat in the body
  states a specific total; the title is used only as the episode's given
  name at BOUT, exactly as handed down.
- **No invented UI or tool names.** `eval-audit-and-sweep`-style specifics
  are not reused here; every named check, round, and file
  (`slides-with-image`, `title-body-coherence`, `01-polish`,
  `04-model-swap`, `tasks.json`) is taken directly from the workshop repo.
