# SCRIPT — The 402-Line Prompt: How Decomposition Makes Agents 5x Faster

*Reel: cwc-workshops--agent-decomposition-skills-vs-tools*
*Skill: `hai-simple`. Register: **Plain** — explain, then stop.*
*Voice: Liam (Kokoro am_onyx), in for Bear.*
*Redo of: `anthropics/cwc-workshops/youtube/agent-decomposition-skills-vs-tools` (Teardown → Plain; same question, same measured case, judgment removed).*

---

## B00 — HESITANT WRITER (Remotion)

*(Writer types the naive fix, hesitates on "more", corrects to "fewer", then lands
the real question.)*

**Liam:** "A newcomer might think a slow agent needs more tools, more context, more
instructions. It's the opposite: why does cutting a 402-line prompt make agents five
times faster?"

---

## S01 — Stakes

You built an agent that works. But it's slow, and every call costs more than it
should.

---

## S02 — Wrong Guess (planted)

The natural fix is to add more: more tools, more context, more instructions packed
into the system prompt so it never misses a case.

---

## S03 — ANCHOR PLANTED

*(THE ANCHOR. This exact case returns at S09.)*

Hold on to one case: a 402-line prompt, 12 tools, one task — a daily low-stock
sweep. It took 102 tool calls and 488 seconds.

---

## S04 — Break the Wrong Guess

But every one of those 402 lines gets read on every call, and all 12 tools get
considered even when only one applies. More isn't the problem — carrying all of it,
always, is.

---

## S05 — Mechanism (part 1)

Three levers trade cost for control. Tools: stateless calls — ask, get an answer,
decide next. Skills: instructions loaded only when needed. Subagents: a separate
context window for a task that needs full autonomy.

---

## S06 — Mechanism (part 2)

So the 402-line prompt splits. The core shrinks to 15 lines — just the role, the
decision logic, the output format. Five skill modules — reorder policy, forecasting,
notifications, vendor lookup, audit logging — load only when a task needs them.

---

## S07 — Mechanism (part 3)

Here's what a skill call looks like. The core issues one instruction: run the
forecasting skill. On the other side of that line, the skill loads its own
two-hundred-line sub-prompt, runs its own reasoning, and returns one result. The core
never touches those lines — complexity hides behind the interface.

---

## S08 — ONE FLAG

*(The reel's only hedge — labelled as one.)*

One flag: these numbers — five times faster, a hundred seconds — are one team's
measurement on one workflow. How much you gain depends on how cleanly your own task
splits into bounded pieces.

---

## S09 — ANCHOR PAYOFF

*(THE ANCHOR RETURNS — same case as S03.)*

Back to the sweep: same 402-line case, now decomposed. The same task that took 102
tool calls and 488 seconds now runs as 3 scripts in about 100 seconds. Same
correctness. About five times faster.

---

## S10 — Both Directions (A)

This works when the pieces are genuinely separable — a lookup, a policy check, a
template — each bounded enough to hand to a tool or a skill on its own.

---

## S11 — Both Directions (B)

It flips when the task is one continuous judgment call. Splitting that just adds a
boundary to cross, and the back-and-forth can cost more than the single big prompt
ever did.

---

## BCRY — Carry-Out (Remotion)

Faster agents don't know less — they load only the knowledge each task actually
needs, exactly when it needs it.

---

## BHTF — Your Turn (Remotion)

Your turn. Here's the prompt — read it with me: "Here's my agent's system prompt —
find the lines that are decision logic versus the lines that are domain knowledge,
split the knowledge into skills the agent loads on demand, and estimate the token and
latency difference." Run it on your own agent, and find your split. Liam, in for
Bear.

---

## BOUT — Outro (Remotion)

The 402-Line Prompt: How Decomposition Makes Agents 5x Faster. Liam, in for Bear.

---

## Six-move audit

| Move | Beat | Law |
|---|---|---|
| 1 stakes first | S01 | ✓ |
| 2 wrong guess, falsified by a case | S02 (planted) → S04 (broken by: reads every line, considers every tool, every call) | WRONG-GUESS LAW ✓ |
| 3 mechanism | S05–S07 | ✓ |
| 4 anchor planted + paid off | S03 → S09 (402-line/12-tool low-stock sweep) | ANCHOR LAW ✓ |
| 5 both directions | S10 + S11 | BOTH-DIRECTIONS LAW ✓ |
| 6 carry-out | BCRY | CARRY-OUT LAW ✓ |
| one flag | S08 | ONE-FLAG LAW ✓ |

## Deliberately not claimed

- **Not "always 5x."** S08 flags that the 5x/488s→100s numbers are one measured
  workflow, not a guaranteed multiplier — the source's own Teardown cut states these
  as measured, and Plain keeps the number but strips the implied universality.
- **No design verdict.** The source's B08 "verdict" beat recapped and implicitly
  endorsed the three-lever split as correct engineering; BCRY here states the fact
  (what loading-on-demand buys you) and stops, per Plain's no-judgment rule.
- **No invented UI or tool names.** "run_skill" mechanics are described generically
  (an instruction crossing a boundary) rather than asserting a specific API surface
  Claude exposes today.
