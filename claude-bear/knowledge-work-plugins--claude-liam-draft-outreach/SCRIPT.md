# Claude, Draft Outreach. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-draft-outreach`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first.*
*Voice: Liam, Kokoro `am_onyx`. Cold open: BrutalistHesitantWriter (Remotion).*

## The question

"What does Claude actually check before it writes a cold email to a real
prospect?" — the general-audience version of the source's teardown of
Anthropic's `draft-outreach` skill (research a prospect, then draft
personalized outreach).

## The wrong guess a newcomer makes

That Claude already "knows" the prospect company — pulling personal color
from whatever it remembers from training — rather than checking anything
today. If that were true, two prospects with the same public profile would
get interchangeable flattery, and anything that happened recently would be
invisible to it.

## The mechanism

`draft-outreach` is a **skill** — a folder Claude reads before it acts. This
one is a single file: `SKILL.md`, about 9k, nothing else. Its named job has
**two steps in order**: research a prospect, then draft personalized
outreach. Web research runs **by default** — Claude looks the company up
before writing anything. That default can be supercharged with enrichment
and CRM data layered on top, but the base habit is the same either way: go
check, don't guess. It only runs on three named triggers: "draft outreach to
[person/company]," "write cold email to [prospect]," "reach out to [name]."

## Anchor example

Say the prospect closed a funding round last week. Hold on to that. Later:
the line in the draft that mentions it isn't something Claude recalled from
training — training has a cutoff, and last week is past it. It's what the
research step found when it actually looked.

## Both directions

- When a draft names something specific and current — a raise, a launch, a
  new hire — that's the research step doing its job: a fact just checked,
  not a fact assumed.
- When a draft reads generic, that doesn't mean the skill broke. It can mean
  the research turned up little, or enrichment and CRM aren't hooked up —
  the file never tells Claude to invent detail to fill the gap.

## Carry-out line

> The detail in that cold email isn't something Claude remembered. It's
> something it just checked.

## Beat-by-beat

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone might ask Claude to draft outreach and assume it already knows the company from training. It doesn't rely on memory — it checks, researching the prospect first. So what does it actually look up?" | BrutalistHesitantWriter — "knows" corrected to "checks" |
| S01 | 1 stakes | You ask Claude to draft outreach to a real prospect — the message has to be about them specifically, not a company name slotted into a template. | SkillTeardownMechanism — "Not a template." |
| S02 | 2 wrong guess | The natural guess: Claude already knows the company — pulling color from what it remembers, not from anything checked today. | SkillTeardownMechanism — "Already knows them?" |
| S03 | 2 break it | Ask about a prospect that just made news — a funding round, a new product. Recall alone can't reach that; it's past any fixed memory. The file has Claude actually go look. | SkillTeardownMechanism — verdict: CHECKED, NOT RECALLED |
| S04 | 3 mechanism | That's because a skill is a folder Claude reads before it acts. draft-outreach is one file — SKILL.md — the whole instruction set, in plain language. | SkillTeardownAnatomy — SKILL.md, 1 file |
| S05 | **4 anchor planted** | Say the prospect closed a funding round last week. Hold on to that. | SkillTeardownMechanism — "Hold on to this." |
| S06 | 3 mechanism | It names its own triggers too — three phrases: "draft outreach to," "write cold email to," or "reach out to" a name. | Opus5ChecklistCard — 3 trigger phrases |
| S07 | 3 mechanism | And its job has two steps, in order: research the prospect, then draft personalized outreach. Web research runs by default — Claude looks the company up. | SkillTeardownMechanism — "Research first, then draft." |
| S08 | 3 mechanism | That default can be supercharged — enrichment services and your CRM layered on top — but the base step is the same: go check, don't guess. | SkillTeardownMechanism — "Supercharged, not required." |
| S09 | 3 mechanism | Then it runs the steps in order: read the file, research the prospect, return the draft. No branching, no improvising. | SkillTeardownPipeline — read / research / return |
| S10 | **4 anchor payoff** | Back to that funding round: the line in the draft that mentions it isn't recalled from training — it's what the research step found this week. | SkillTeardownMechanism — verdict: CHECKED, NOT REMEMBERED |
| S11 | 5 direction A | When a draft names something specific and current — a raise, a launch, a new hire — that's the research step doing its job. | SkillTeardownMechanism — verdict: REAL CHECK |
| S12 | 5 direction B | When a draft reads generic, that doesn't mean it broke. It can mean the research turned up little, or enrichment and CRM aren't hooked up — the file never says invent detail to fill the gap. | SkillTeardownMechanism — verdict: NOT A FAILURE |
| BCRY | 6 carry-out | The detail in that cold email isn't something Claude remembered. It's something it just checked. | WantQuote |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: before you draft outreach to this prospect, read the draft-outreach SKILL.md and tell me exactly what you'll research and how you'll trigger it. Then draft it, and show me which line traces back to something you actually checked — and which don't. | ClaudeComposerAsk |
| BOUT1 | outro title | Claude, Draft Outreach. | OutroSeries |
| BOUT2 | outro cta | …Liam, in for Bear. | OutroCTA — Humanitarians AI skin |

## Six-move audit

| Move | Beat | Satisfied |
|---|---|---|
| 1 stakes first | S01 | yes — the drafting request, before any mechanism |
| 2 wrong guess | S02 → S03 | yes — stated, then falsified by "ask about recent news" |
| 3 mechanism | S04, S06, S07, S08, S09 | yes — folder/file, trigger phrases, two-step job, optional layers, linear pipeline |
| 4 anchor | S05 → S10 | yes — same illustrative signal (a funding round), planted then paid off |
| 5 both directions | S11, S12 | yes — a real checked fact is real; generic isn't a failure |
| 6 carry-out | BCRY | yes |

No inference flag: every claim traces to the source SKILL.md description
("Research a prospect then draft personalized outreach. Uses web research
by default, supercharged with enrichment and CRM," the three trigger
phrases, "same input, same output, every run," "limit: only what the file
says") or is an illustrative example clearly marked as hypothetical ("Say
the prospect closed a funding round last week…") rather than an asserted
internal fact. The one generic-true fact this reel leans on beyond the
source — that Claude's training has a knowledge cutoff, so very recent
events aren't in its memory — is a stable, current fact about how Claude
works, not an invented one.
