# How Does Claude Choose a Zoom Approach? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-choose-zoom-approach`, Teardown → Plain).*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it. 7 beats.*

**Cold open:** BrutalistHesitantWriter (free Remotion, no puppet, no spend).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer cold open | "Someone asks which Zoom API they should use. But Zoom isn't one API — it's several different approaches, each built for a different job. Liam is here to walk through how Claude actually chooses between them." | Writer types "Which Zoom API should I use?", hesitates on "API", corrects to "approach" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that integrating with Zoom means picking one API and building everything on top of it. But Zoom splits into several separate surfaces, and picking the wrong one costs you: ask the REST API to tell you the instant a meeting ends, and it won't — you'd have to poll it over and over, arriving late every time. A webhook fires the moment the meeting ends, no polling at all. | "ONE API FOR EVERYTHING" struck; a poll loop arriving late vs. a webhook firing instantly |
| B02 | 3 mechanism / 4 ANCHOR PLANTED | What the skill actually does is hold a fixed list of Zoom surfaces — REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone, Contact Center — and match your use case to whichever one fits its shape. Watch the anchor: "notify us the instant a meeting ends" is an event to be told about, not a value to look up — that shape points straight at Webhooks. | THE ANCHOR — the use case sentence, scanning down the fixed list, landing on Webhooks |
| B03 | 4 ANCHOR PAYOFF / 5 both directions | Match confirmed — Webhooks. But matching the shape doesn't finish the build: you still write the endpoint and handle what it sends you: the skill named the surface, not the code. And a use case that needs two things at once — say, a live meeting embedded in your product, plus that same instant notification — isn't a failure of the list. A hybrid of two surfaces, Meeting SDK and Webhooks together, is one of the answers on it. | THE ANCHOR RETURNS — Webhooks lit, then splits into "match ≠ finished build" and "hybrid is an answer, not an exception" |
| **BCRY** | **6 carry-out** | Picking a Zoom integration isn't picking one API — it's matching what the use case needs to one of several surfaces, and combining two of them when one isn't enough. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Describe a Zoom use case you actually have — say, "notify our support queue the moment a scheduled call no-shows." Read the choose-zoom-approach skill and walk me through which surface it picks, and why, before you touch any code. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | How Does Claude Choose a Zoom Approach? Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B01 states "one API for everything"; the poll-vs-webhook case breaks it — an event-notify use case fails on a pull-based API and succeeds on a push-based one |
| Exactly one inference flag | none needed — the source's own facts (the nine-plus named surfaces, the hybrid option) are stated directly, no inference beyond them |
| One anchor, planted early, paid off late | B02 → B03 ("notify the instant a meeting ends" → Webhooks) |
| Both failure directions | B03: a matched surface ≠ a finished build; an unclear/compound need ≠ no valid answer (hybrid is one) |
| No design judgment | B01/B03 describe why a use case fails or succeeds against a given surface; never a verdict on whether the skill itself was built well |

## Deliberately not claimed

- **Not "the skill writes the integration code."** B03 is explicit: the skill
  names the surface; everything downstream (the endpoint, the request
  handling) is still the builder's.
- **Not "hybrid is a fallback."** The source lists "a hybrid approach" as
  one of the skill's own named options, not an exception path — B03 keeps
  it that way.
- **No accusation that the skill is incomplete or badly scoped.** The
  Teardown source's "what it gets right / what it bites" verdict framing is
  removed; Plain states only what the mechanism does and its two limits.
- **No invented UI or model names.** Every named surface (REST API,
  Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP,
  Phone, Contact Center) is stated verbatim from the source sheet's own
  narration.

## Handoff prompt (BHTF, read aloud)

> "Describe a Zoom use case you actually have — say, 'notify our support
> queue the moment a scheduled call no-shows.' Read the choose-zoom-approach
> skill and walk me through which surface it picks, and why, before you
> touch any code."

Why it's worth running: naming the use case's shape out loud before the
tool call is what surfaces the real constraint logic — the same clause the
source sheet's own handoff insisted on.

---
**GATE P — signed:** ______________________  (human)
