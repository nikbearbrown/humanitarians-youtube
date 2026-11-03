# Claude, Metrics Review. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-metrics-review`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first.*
*Voice: Liam, Kokoro `am_onyx`. Cold open: BrutalistHesitantWriter (Remotion).*

## The question

"What actually happens when you ask Claude to review your metrics?" — the
general-audience version of the source's teardown of Anthropic's
`metrics-review` skill.

## The wrong guess a newcomer makes

That "review my metrics" triggers freeform judgment — Claude eyeballing a
week of numbers and calling out whatever looks interesting, differently
each time depending on what catches its eye.

## The mechanism

`metrics-review` is a **skill** — a folder Claude reads before it acts,
containing one file: `SKILL.md` (17k of plain-language instructions). That
file names what a review covers (trend analysis, comparison against
targets, a scorecard with recommended actions) and exactly what triggers
it (a weekly, monthly, or quarterly review, or a request to investigate a
spike or drop). Claude reads the file, then works fixed steps in order:
read the numbers, run the analysis, return the scorecard. No branching, no
improvising.

## Anchor example

A week where a metric — say, weekly active users — drops twenty percent
with no obvious cause. Planted early as "hold on to this," it returns
late: the spike-or-drop case named in the file catches it, the same way
it would on any other week, because that case is on the list.

## Both directions

- A flagged drop is real signal: the case named in the file actually
  happened.
- A clean scorecard is not a clean bill of health: it only means nothing
  on *this* list tripped — a metric the file never tracks can slip
  straight through, because it was never on the list to begin with.

## Carry-out line

> A metrics review is a checklist Claude runs against your numbers. Know
> what's on the list, and you know exactly what the review will catch —
> and exactly what it won't.

## Beat-by-beat

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone might ask Claude to review their metrics and assume it catches everything that's off. It doesn't — it catches exactly what one file tells it to. So what does 'review' actually check?" | BrutalistHesitantWriter — "everything" corrected to "some things" |
| S01 | 1 stakes | You hand Claude a week of numbers and ask for a review before the meeting. Something has to decide what counts as worth flagging. | SkillTeardownMechanism — "Before the meeting." |
| S02 | 2 wrong guess | The natural guess: Claude just eyeballs the numbers and tells you whatever looks interesting — different each time, depending on what catches its eye. | SkillTeardownMechanism — "Whatever looks interesting?" |
| S03 | 2 break it | Run the same week of numbers through twice. Freeform judgment could drift. Claude's doesn't — the same steps run, in the same order, every time. | SkillTeardownMechanism — verdict: SAME EVERY TIME |
| S04 | 3 mechanism | That's because metrics-review is a skill — a folder Claude reads before it acts. Inside sits one file, SKILL.md, seventeen kilobytes of plain-language instructions. | SkillTeardownAnatomy — SKILL.md, 1 file |
| S05 | **4 anchor planted** | Say weekly active users drop twenty percent, out of nowhere. Hold on to that drop. | SkillTeardownMechanism (quote card) — the drop, stated |
| S06 | 3 mechanism | For metrics-review, the file names what a review covers: trend analysis, comparison against targets, and a scorecard with recommended actions. | Opus5ChecklistCard — 3 items |
| S07 | 3 mechanism | It also names its own moment to run — a weekly, monthly, or quarterly review, or the words "investigate this spike or drop." | SkillTeardownMechanism — "It names its own cue." |
| S08 | 3 mechanism | Then it works the steps in order: read the numbers, run the analysis, return the scorecard. No branching, no improvising. | SkillTeardownPipeline — read / analyze / return |
| S09 | **4 anchor payoff** | Back to that twenty-percent drop: the spike-or-drop case catches it, same as it would on any other week. | SkillTeardownMechanism (quote card) — SAME wording, flagged |
| S10 | 5 direction A | A flagged drop is real signal. The case named in the file actually happened. | SkillTeardownMechanism — verdict: REAL SIGNAL |
| S11 | 5 direction B | But a clean scorecard isn't a clean bill of health — it only means nothing on this list tripped. A metric the file never tracks can slip straight through. | SkillTeardownMechanism — verdict: NOT A CLEAN BILL |
| BCRY | 6 carry-out | A metrics review is a checklist Claude runs against your numbers. Know what's on the list, and you know exactly what the review will catch — and exactly what it won't. | WantQuote |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: before you review my metrics, tell me exactly what SKILL.md says you'll check — the analysis, the targets, and the trigger. Then paste a real week of numbers, and watch it check only what it just told you. | ClaudeComposerAsk |
| BOUT | outro | Claude, Metrics Review. … Liam, in for Bear. | OutroSeries + OutroCTA — Humanitarians AI skin |

## Six-move audit

| Move | Beat | Satisfied |
|---|---|---|
| 1 stakes first | S01 | yes — the pre-meeting decision, before any mechanism |
| 2 wrong guess | S02 → S03 | yes — stated, then falsified by "run it twice" |
| 3 mechanism | S04, S06, S07, S08 | yes — folder/file, coverage, trigger, linear steps |
| 4 anchor | S05 → S09 | yes — same quote card, same wording, planted then paid off |
| 5 both directions | S10, S11 | yes — flag is signal; clean is not a clean bill of health |
| 6 carry-out | BCRY | yes |

No inference flag: every claim here is what the source `SKILL.md` and its
teardown narration already stated as fact (coverage, trigger phrases,
linear execution) — nothing in this reel is a leap requiring a hedge.

## Deliberately not claimed

- No invented UI or dashboard — the source never describes one, so this
  reel doesn't either.
- No specific numeric thresholds beyond the illustrative twenty-percent
  anchor, which is stated as an example ("say... drop twenty percent"),
  not a fact about the skill's internals.
