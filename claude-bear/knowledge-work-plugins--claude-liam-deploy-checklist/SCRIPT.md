# Claude, Deploy Checklist. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-deploy-checklist`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first.*
*Voice: Liam, Kokoro `am_onyx`. Cold open: BrutalistHesitantWriter (Remotion).*

## The question

"What does Claude actually check before it says a release is ready to ship?" —
the general-audience version of the source's teardown of Anthropic's
`deploy-checklist` skill.

## The wrong guess a newcomer makes

That asking Claude if a release is "ready to deploy" triggers a human-style
judgment call — weighing risk and timing by feel, the way a release manager
might on a Friday afternoon — rather than a fixed, named checklist.

## The mechanism

`deploy-checklist` is a **skill** — a folder Claude reads before it acts,
containing one file: `SKILL.md`. That file names exactly three things to
check (CI status & approvals, database migrations or feature flags, and
rollback triggers documented ahead of time) and exactly what triggers it
(about to ship a release, or a change with a migration or feature flag).
Claude reads the file, then works fixed steps in order: read the checklist,
check each named item, return what's outstanding. No branching, no
improvising.

## Anchor example

A release that adds a database migration — a new column, live in
production. Planted early as "hold on to this," it returns late: the
checklist flags it, the same way it would on any other release day, because
that item is on the list.

## Both directions

- A flag is real signal: the item named in the file actually applies.
- A clean checklist is not a certificate: it only means nothing on *this*
  list tripped — a failure the file never names can still ship straight
  through, because it was never on the list to begin with.

## Carry-out line

> A skill is a checklist Claude reads before it acts. Know what's on this
> one, and you know exactly what "ready to deploy" checks — and exactly what
> it doesn't.

## Beat-by-beat

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone might ask Claude if a release is ready to ship and expect a judgment call. It doesn't guess — it runs one fixed checklist. So what's actually on that list?" | BrutalistHesitantWriter — "judgment" corrected to "checklist" |
| S01 | 1 stakes | You're about to ship a release and ask Claude if it's ready to go. Something has to decide what "ready" means. | SkillTeardownMechanism — "Before you ship." |
| S02 | 2 wrong guess | The natural guess: Claude weighs it the way a release manager would — a gut call on risk, made in the moment. | SkillTeardownMechanism — "A gut call?" |
| S03 | 2 break it | Run it before two different releases — a one-line typo fix, and a change with a database migration. A gut call might treat those the same on a Friday afternoon. Claude checks the same fixed list against both, every time. | SkillTeardownMechanism — verdict: SAME EVERY TIME |
| S04 | 3 mechanism | That's because a skill is a folder Claude reads before it acts. Inside sits one file — SKILL.md — the checklist, in plain language. | SkillTeardownAnatomy — SKILL.md, 1 file |
| S05 | **4 anchor planted** | Say the release adds a database migration — a new column, live in production. Hold on to that. | GitHubCodeDiff — the migration |
| S06 | 3 mechanism | For deploy-checklist, the file names exactly three things to check: CI status and approvals, database migrations or feature flags, and rollback triggers, documented ahead of time. | Opus5ChecklistCard — 3 items |
| S07 | 3 mechanism | It also names its own trigger — about to ship a release, or a change with a migration or feature flag. | SkillTeardownMechanism — "It names its own cue." |
| S08 | 3 mechanism | Then it works the steps in order: read the checklist, check each item, return what's outstanding. No branching, no improvising. | SkillTeardownPipeline — read / check / return |
| S09 | **4 anchor payoff** | Back to that migration: the checklist flags it — same as it would on any other release day. | GitHubCodeDiff — SAME diff, flagged |
| S10 | 5 direction A | A flag is real signal. The item named in the file actually applies. | SkillTeardownMechanism — verdict: REAL SIGNAL |
| S11 | 5 direction B | But a clean checklist isn't a certificate — it only means nothing on this list tripped. A failure the file never names can still ship straight through. | SkillTeardownMechanism — verdict: NOT A CERTIFICATE |
| BCRY | 6 carry-out | A skill is a checklist Claude reads before it acts. Know what's on this one, and you know exactly what "ready to deploy" checks — and exactly what it doesn't. | WantQuote |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: before you say this release is ready, read the deploy-checklist SKILL.md and tell me exactly what you're about to check — the items, and the trigger phrase. Then walk me through this release. | ClaudeComposerAsk |
| BOUT | outro | Claude, Deploy Checklist. … Liam, in for Bear. | OutroSeries + OutroCTA — Humanitarians AI skin |

## Six-move audit

| Move | Beat | Satisfied |
|---|---|---|
| 1 stakes first | S01 | yes — the ship decision, before any mechanism |
| 2 wrong guess | S02 → S03 | yes — stated, then falsified by "run it twice" |
| 3 mechanism | S04, S06, S07, S08 | yes — folder/file, checklist items, trigger, linear steps |
| 4 anchor | S05 → S09 | yes — same GitHubCodeDiff migration, same treatment, planted then paid off |
| 5 both directions | S10, S11 | yes — flag is signal; clean is not a certificate |
| 6 carry-out | BCRY | yes |

No inference flag: every claim here is what the source `SKILL.md` and its
teardown narration already stated as fact (checklist items, trigger
phrases, linear execution) — nothing in this reel is a leap requiring a
hedge.
