# Claude, Compose Outreach. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-compose-outreach`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first.*
*Voice: Liam, Kokoro `am_onyx`. Cold open: BrutalistHesitantWriter (Remotion).*

## The question

"What does Claude actually do when it 'composes outreach'?" — the general-audience
version of the source's teardown of Anthropic's `compose-outreach` skill (a
partner-built knowledge-work plugin, generating outreach messages from Common
Room signals).

## The wrong guess a newcomer makes

That the "personal touch" in an AI-drafted outreach message is Claude free-styling
— inferring a plausible-sounding detail about the contact from its own general
sense of them, so two runs might read as two different flavors of flattery.

## The mechanism

`compose-outreach` is a **skill** — a folder Claude reads before it acts,
containing `SKILL.md` and a `references` folder. The file's job is narrow:
generate personalized outreach messages using **Common Room signals** — a named
external data source — and it only runs on a named trigger: "draft outreach to
[person]," "write an email to [name]," "compose a message for [contact]," or any
outreach-drafting request. It doesn't infer a personal detail from a general
impression; it points at a specific signal the data actually has on file.

## Anchor example

Say a contact's title changed since your last outreach. Hold on to that. Later:
the line in the draft that mentions it isn't a flourish Claude invented — it's
the signal the file told it to go find and reference.

## Both directions

- When the draft names a real signal — a title change, a usage spike, a renewal
  date — that's the skill doing its job: a fact from the data, not a guess.
- When a draft reads generic, that doesn't mean the skill broke. It can mean no
  strong signal was on file for that contact — the file never tells Claude to
  invent one to fill the gap.

## Carry-out line

> The personal line in that email is a signal Claude was told to go find, not
> one it made up.

## Beat-by-beat

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone might ask Claude to compose outreach and assume it invents the personal touch. It doesn't — it fetches a specific signal from data and writes around that. So what does 'personalized' actually mean here?" | BrutalistHesitantWriter — "invents" corrected to "fetches" |
| S01 | 1 stakes | You ask Claude to draft outreach to a real contact — the message has to actually be about that person, not a template with a name dropped in. | SkillTeardownMechanism — "Not a template." |
| S02 | 2 wrong guess | The natural guess: Claude free-styles the personal touch — inferring a detail from its own general sense of the contact. | SkillTeardownMechanism — "Free-styled?" |
| S03 | 2 break it | Ask it twice for the same contact. A free-styling writer might return two different flavors of flattery. This doesn't — the file names one source to pull from, so both drafts point at the same signal. | SkillTeardownMechanism — verdict: SAME SOURCE, NOT A MOOD |
| S04 | 3 mechanism | That's because a skill is a folder Claude reads before it acts. Inside compose-outreach sits SKILL.md and a references folder — the instructions, in plain language. | SkillTeardownAnatomy — SKILL.md + references, 2 files |
| S05 | **4 anchor planted** | Say a contact's title changed since your last outreach. Hold on to that. | SkillTeardownMechanism — "Hold on to this." |
| S06 | 3 mechanism | It also names its own trigger — four phrases: "draft outreach to," "write an email to," "compose a message for," or any outreach-drafting request. | Opus5ChecklistCard — 4 trigger phrases |
| S07 | 3 mechanism | And it names exactly one job: generate personalized outreach messages using Common Room signals — a named external data source, not Claude's general sense of the contact. | SkillTeardownMechanism — "One named source." |
| S08 | 3 mechanism | Then it works the steps in order: read the file, look up the signal, return the draft. No branching, no improvising. | SkillTeardownPipeline — read / look up / return |
| S09 | **4 anchor payoff** | Back to that title change: the line in the draft that mentions it isn't a flourish — it's the signal the file told Claude to go find. | SkillTeardownMechanism — verdict: FETCHED, NOT INVENTED |
| S10 | 5 direction A | When the draft names a real signal — a title change, a usage spike — that's the skill doing its job: a fact from the data, not a guess. | SkillTeardownMechanism — verdict: REAL SIGNAL |
| S11 | 5 direction B | When a draft reads generic, that doesn't mean it broke. It can mean no strong signal was on file — the file never says invent one to fill the gap. | SkillTeardownMechanism — verdict: NOT A FAILURE |
| BCRY | 6 carry-out | The personal line in that email is a signal Claude was told to go find, not one it made up. | WantQuote |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: before you draft outreach to this contact, read the compose-outreach SKILL.md and tell me exactly what signal source you're pulling from and what triggered you. Then draft it, and check whether the personal line traces back to something real, or nothing at all. | ClaudeComposerAsk |
| BOUT1 | outro title | Claude, Compose Outreach. | OutroSeries |
| BOUT2 | outro cta | …Liam, in for Bear. | OutroCTA — Humanitarians AI skin |

## Six-move audit

| Move | Beat | Satisfied |
|---|---|---|
| 1 stakes first | S01 | yes — the drafting request, before any mechanism |
| 2 wrong guess | S02 → S03 | yes — stated, then falsified by "run it twice" |
| 3 mechanism | S04, S06, S07, S08 | yes — folder/file, trigger phrases, named job, linear steps |
| 4 anchor | S05 → S09 | yes — same illustrative signal (a title change), planted then paid off |
| 5 both directions | S10, S11 | yes — a named signal is real signal; generic isn't a failure |
| 6 carry-out | BCRY | yes |

No inference flag: every claim traces to the source SKILL.md description
("generate personalized outreach messages using Common Room signals," the four
trigger phrases, "same input, same output, every run," "limit: only what the
file says") or is an illustrative example clearly marked as hypothetical
("Say a contact's title changed…") rather than an asserted internal fact.
