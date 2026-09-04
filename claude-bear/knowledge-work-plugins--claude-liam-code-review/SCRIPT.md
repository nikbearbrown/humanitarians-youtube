# Claude, Code Review. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-code-review`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first.*
*Voice: Liam, Kokoro `am_onyx`. Cold open: BrutalistHesitantWriter (Remotion).*

## The question

"What actually happens when you ask Claude to review your code?" — the general-audience
version of the source's teardown of Anthropic's `code-review` skill.

## The wrong guess a newcomer makes

That "review my code" triggers the same kind of broad, improvised judgment a human
reviewer brings — reading the whole diff and flagging whatever looks off, differently
each time depending on who's asking and how carefully they look.

## The mechanism

`code-review` is a **skill** — a folder Claude reads before it acts, containing one file:
`SKILL.md`. That file names exactly three things to check (security, performance,
correctness) and exactly what triggers it (a PR link, a diff, or "review this before I
merge"). Claude reads the file, then works fixed steps in order: read the diff, check
each named category, return findings. No branching, no improvising.

## Anchor example

A diff that adds a database call inside a loop — one extra query for every row (the
classic N+1 pattern). Planted early as "hold on to this," it returns late: the
performance check flags it, the same way it would on any other day, because that
category is on the list.

## Both directions

- A flag is real signal: the category named in the file actually tripped.
- A clean review is not a certificate: it only means nothing on *this* list tripped —
  a bug the file never mentions (a logic error, a bad UX call) can sail straight
  through, because it was never on the list to begin with.

## Carry-out line

> A skill is a checklist Claude reads before it acts. Know what's on the list, and you
> know exactly what a review catches — and exactly what it doesn't.

## Beat-by-beat

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone might ask Claude to review their code and assume it catches everything wrong. It doesn't — it catches exactly what one file tells it to. So what does 'review' actually check?" | BrutalistHesitantWriter — "everything" corrected to "some things" |
| S01 | 1 stakes | You paste a diff and ask Claude to review it before you merge. Something has to decide what counts as a problem. | SkillTeardownMechanism — "Before you merge." |
| S02 | 2 wrong guess | The natural guess: Claude reads it the way a senior engineer would — broad judgment, catching whatever looks off. | SkillTeardownMechanism — "Broad judgment?" |
| S03 | 2 break it | Run the same review twice on the same diff. A human reviewer's mood might drift. Claude's doesn't — the same categories get checked, every time. | SkillTeardownMechanism — verdict: SAME EVERY TIME |
| S04 | 3 mechanism | That's because a skill is a folder Claude reads before it acts. Inside sits one file — SKILL.md — the instructions, in plain language. | SkillTeardownAnatomy — SKILL.md, 1 file |
| S05 | **4 anchor planted** | Say the diff adds a database call inside a loop — one extra query for every row. Hold on to that. | GitHubCodeDiff — the N+1 loop |
| S06 | 3 mechanism | For code-review, the file names exactly three things to check: security, performance, correctness. | Opus5ChecklistCard — 3 items |
| S07 | 3 mechanism | It also names its own trigger — a PR link, a diff, or the words "review this before I merge." | SkillTeardownMechanism — "It names its own cue." |
| S08 | 3 mechanism | Then it works the steps in order: read the diff, check each category, return findings. No branching, no improvising. | SkillTeardownPipeline — read / check / return |
| S09 | **4 anchor payoff** | Back to that loop with the extra query: the performance check flags it — same as it would on any other day. | GitHubCodeDiff — SAME diff, flagged |
| S10 | 5 direction A | A flag is real signal. The category named in the file actually tripped. | SkillTeardownMechanism — verdict: REAL SIGNAL |
| S11 | 5 direction B | But a clean review isn't a certificate — it only means nothing on this list tripped. A bug the file never mentions can sail straight through. | SkillTeardownMechanism — verdict: NOT A CERTIFICATE |
| BCRY | 6 carry-out | A skill is a checklist Claude reads before it acts. Know what's on the list, and you know exactly what a review catches — and exactly what it doesn't. | WantQuote |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: before you review my code, tell me exactly what SKILL.md says you'll check — the categories, and the trigger phrase. Then paste a real diff, and watch it check only what it just told you. | ClaudeComposerAsk |
| BOUT | outro | Claude, Code Review. … Liam, in for Bear. | OutroSeries + OutroCTA — Humanitarians AI skin |

## Six-move audit

| Move | Beat | Satisfied |
|---|---|---|
| 1 stakes first | S01 | yes — the merge decision, before any mechanism |
| 2 wrong guess | S02 → S03 | yes — stated, then falsified by "run it twice" |
| 3 mechanism | S04, S06, S07, S08 | yes — folder/file, categories, trigger, linear steps |
| 4 anchor | S05 → S09 | yes — same GitHubCodeDiff diff, same treatment, planted then paid off |
| 5 both directions | S10, S11 | yes — flag is signal; clean is not a certificate |
| 6 carry-out | BCRY | yes |

No inference flag: every claim here is what the source `SKILL.md` and its teardown
narration already stated as fact (categories checked, trigger phrases, linear
execution) — nothing in this reel is a leap requiring a hedge.
