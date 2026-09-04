# The Hard Case — Narration Script (redo of `preserve-cognitive-demand-differentiation`)

*Skill: `hai-simple`. Register: **Plain**. Voice: Liam, Kokoro `am_onyx`. 8 beats.*
*Redo of `anthropics/k12-teacher-skills/youtube/preserve-cognitive-demand-differentiation/beat_sheet.json`
(8 filled beats, `nikbearbrown` brand) — same question, same facts, same beat count.*

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer / wrong guess | "Someone assumes the fix for a struggling student is an easier task. It isn't — that removes the thinking you wanted built. So what actually changes: the task, or just the way in?" | `BrutalistHesitantWriter` — types "make their task easier?", corrects "easier" → "different" |
| B01 | anchor planted, mechanism | "Take one problem: seventeen divided by five. Three tiers, one hard case. Below tier: draw seventeen dots, group them by five, circle the two left over. At tier: three, remainder two — a basket analogy, two apples left over. Above tier: same equation, then a proof — why must the remainder always be smaller than the divisor? Three different doors into the same room. Notice what didn't happen: nobody got a simpler problem. The hard case — the remainder — lives in every tier." | Three tier cards (Below/At/Above) converging on one "remainder = 2" card |
| B02 | mechanism, wrong guess falsified | "That's the general rule. Differentiation changes the scaffold, the representation, the entry point — never the intellectual demand. Here's the case that breaks the easier-task instinct: give a struggling reader a simpler book, and you've solved today's problem while creating next month's gap — they never practice the hard case at all. Give them the same text with more support instead, and you've given them a real chance to close that gap. Same book. Different scaffold." | Simpler book (struck, gap grows) vs. same book + scaffold (gap closes) |
| B03 | **both directions** | "Here's the test for whether you're differentiating or just tracking. Ask one question: does every tier arrive at the same place? Three doors into one room — that's differentiation, and it holds. One entry into three separate ceilings, where the below-tier task caps out lower than the rest — that's tracking, even if it started from a good scaffold. Widening the path keeps everyone in the room. Forking it means some students never reach it at all." | Two columns: 3 arrows → 1 room (differentiation); 1 entry → 3 capped ceilings (tracking) |
| B04 | **anchor payoff** | "Cognitive load theory explains why this matters. Extraneous load is waste — confusing formats, clutter, extra steps — and the scaffold should absorb all of it. Germane load is the actual struggle with the concept, and that is the curriculum itself. Go back to seventeen divided by five: the remainder is germane load. Strip it out to make the task easier, and you haven't simplified anything — you've deleted the lesson." | Two piles, EXTRANEOUS (absorbed by scaffold) and GERMANE (kept by learner); the remainder token drops into GERMANE |
| **BCRY** | carry-out | "Differentiation changes the door in — never the hard case waiting behind it." | `WantQuote`, the sentence alone |
| BHTF | your turn | "Your turn. Here's the prompt — read it with me. Take a lesson you already teach. Tell Claude the main concept and the hard case — the exact moment where students get stuck. Ask it to design three tiers: concrete, representational, and abstract, all keeping that same hard case. Then compare the three side by side: does each one actually arrive at the same intellectual demand? Liam, in for Bear." | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | "The Hard Case. Liam, in for Bear." | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the trap before B01 shows the mechanism |
| Wrong guess, stated and falsified by a case | B00 states it ("an easier task"); B02 falsifies it with a concrete case (simpler book solves today, creates next month's gap) |
| One anchor, planted early, paid off late | B01 → B04 (17 ÷ 5's remainder) |
| Both failure directions | B03: three-doors-one-room holds as differentiation; one-entry-three-ceilings is tracking even from a good scaffold |
| No design judgment | B01–B04 describe the mechanism and its failure mode; no verdict on any specific curriculum or teacher's choice |

## Deliberately not claimed

- **Not that all differentiation is fine as long as it varies representation.** B03's ceiling
  check is the flip side: representation-only variation can still be tracking if the
  ceilings differ. That's the one flag this reel needs — the source already states it as
  a test, not a guarantee.
- **No specific curriculum, grade band, or teacher named.** The 17 ÷ 5 example is the
  source's own worked case; nothing is invented beyond it.

## Handoff prompt (BHTF, read aloud)

> "Here is my lesson's main concept and the hard case where students get stuck. Design
> three tiers — concrete, representational, and abstract — that all keep that same hard
> case. Show me all three side by side so I can compare whether the intellectual demand
> is the same."
