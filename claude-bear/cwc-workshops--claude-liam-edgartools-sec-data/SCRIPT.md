# SCRIPT — Claude's SEC Filings Skill: Reliable, Not All-Knowing

*Reel: cwc-workshops--claude-liam-edgartools-sec-data*
*Skill: `hai-simple`. Register: **Plain** — explain, then stop.*
*Voice: Liam (Kokoro am_onyx), in for Bear.*
*Redo of: `anthropics/cwc-workshops/youtube/claude-liam-edgartools-sec-data` (Teardown → Plain; same skill, same facts, judgment removed).*

---

## B00 — HESITANT WRITER (Remotion)

*(Writer types the naive claim, hesitates on "understands finance", corrects to
"follows the file", then lands the real question.)*

**Liam:** "A newcomer might think adding a skill means Claude now understands
finance in general. It doesn't — it follows the file. So what does a skill file
actually let Claude do?"

---

## S01 — Stakes

Ask Claude to pull data from a company's SEC filings, and it reaches for a skill
built for exactly that — a folder called edgartools-sec-data.

---

## S02 — Wrong Guess (planted)

The natural read: give Claude a skill for SEC data, and it must now generally
understand finance and filings — ask it anything, and it'll know.

---

## S03 — ANCHOR PLANTED

*(THE ANCHOR. This exact list returns at S08.)*

Hold on to what the file actually says: company lookups, filings, XBRL financial
statements, and sections like Item 1A risk factors. That's the whole list.

---

## S04 — Break the Wrong Guess

Ask for something off that list — say, whether the filing looks risky to you — and
there's no step for it. The file never wrote that down.

---

## S05 — Mechanism (part 1)

A skill is just a folder Claude reads before it acts. Here, one file does the job:
SKILL.md — plain language, the whole instruction set, no hidden logic.

---

## S06 — Mechanism (part 2)

Claude reads the file, then works through its steps in order — read, then execute,
then hand back the result. Linear, unless a step says otherwise.

---

## S07 — Mechanism (part 3)

That's what makes it repeatable: the same request runs the same steps, and produces
the same kind of output, every single time.

---

## S08 — ANCHOR PAYOFF

*(THE ANCHOR RETURNS — same list as S03.)*

Back to that list: ask for a company lookup or an XBRL statement, and you get the
same reliable pull, every time. Ask outside it, and nothing happens — that step was
never written.

---

## S09 — Both Directions (A)

So the skill is dependable exactly when your question matches the file — a lookup,
a filing, a financial statement.

---

## S10 — Both Directions (B)

It flips the moment your question needs judgment the file doesn't have — asking
whether a company looks like a good bet was never written into these steps.

---

## BCRY — Carry-Out (Remotion)

A skill file makes Claude's actions repeatable, not all-knowing — it only does what
the file actually wrote down.

---

## BHTF — Your Turn (Remotion)

Your turn. Here's the prompt — read it with me: "Read the edgartools-sec-data
skill, and list, in your own words, exactly which four things it lets you pull from
SEC filings — then tell me one thing about a company you might want to know that
isn't on that list." Liam, in for Bear.

---

## BOUT — Outro (Remotion)

Claude's SEC Filings Skill: Reliable, Not All-Knowing. Liam, in for Bear.

---

## Six-move audit

| Move | Beat | Law |
|---|---|---|
| 1 stakes first | S01 | ✓ |
| 2 wrong guess, falsified by a case | S02 (planted) → S04 (broken by: asking for a risk opinion, which has no step) | WRONG-GUESS LAW ✓ |
| 3 mechanism | S05–S07 | ✓ |
| 4 anchor planted + paid off | S03 → S08 (the four-item spec list: lookup, filings, XBRL, Item 1A) | ANCHOR LAW ✓ |
| 5 both directions | S09 + S10 | BOTH-DIRECTIONS LAW ✓ |
| 6 carry-out | BCRY | CARRY-OUT LAW ✓ |
| one flag | — none needed | see below |

## Deliberately not claimed

- **No inference flag.** Every claim here — the skill is a folder, SKILL.md is the
  instruction set, the steps run in order, the scope is company lookup / filings /
  XBRL statements / Item 1A-style sections — restates the source SKILL.md's own
  description of itself (confirmed by the source's PEDAGOGY.md and AUDIT.md, which
  quote the file directly). Nothing here is this reel's inference about how Skills
  work in general, so ONE-FLAG LAW correctly produces zero flags rather than a
  hedge.
- **No design verdict.** The source's BVDT "verdict" beat recapped and implicitly
  praised the spec-bounded design ("Repeatable. Spec-bounded."); BCRY here states the
  fact (bounded, reliable within that bound) and stops, per Plain's no-judgment
  rule.
- **No invented UI or tool names.** The `edgartools` Python package and SEC EDGAR
  are named because the source names them; no new tool, model, or interface is
  invented.
- **Beat count expanded from the source's 7 (B00–B03, BVDT, BHTF, BOUT) to 15.**
  The source's Teardown cut compressed its whole body into 3 beats (~113 words,
  itself flagged by the source's own AUDIT.md as "below the 5-beat/180-word
  threshold"). Plain register's mandatory structure — a planted-and-broken wrong
  guess, a planted-and-paid-off anchor, an explicit both-directions pair — needs its
  own beat per move. Every fact is the source's; only the segmentation changed, one
  idea per beat.
