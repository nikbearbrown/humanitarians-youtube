# What's a Cold-Start Interview? — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet whose narration
was never actually written — see QUESTION.md). Register: **Plain**. 7 beats ≈ 1:50.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone starting a brand-new legal matter asks what the brief should say to Claude. Wrong word — there's no brief to write here. The real question worth asking is: what's the interview?" | BrutalistHesitantWriter — types "New client — what's the brief?", corrects "brief" → "interview" |
| B01 | 1 stakes / 2 wrong guess, falsified | A brand-new matter, and Claude has no memory of your last one — every conversation starts from zero. So the instinct is to just brief it: paste in everything you think matters and hope that covers it. But a brief only covers what the writer remembers to mention — and the classic gaps, jurisdiction, conflicts, retainer scope, are exactly what people assume is obvious and never write down. | a "BRIEF" card with named-detail chips filled in; a dim, unlabeled "jurisdiction" chip sliding in underneath, unmarked, never joining the card |
| B02 | 3 mechanism / **4 anchor planted** | A cold-start interview flips it: instead of trusting what you remember to say, Claude asks the same fixed questions every time — client, matter type, jurisdiction, conflicts, scope. Watch the anchor: jurisdiction. It's the one detail everyone assumes goes without saying — which is exactly why a free-form brief leaves it out. | five fixed question chips lighting in turn (client / matter type / jurisdiction / conflicts / scope); THE ANCHOR — the jurisdiction chip returns, dim, off to the side, marked "not volunteered" |
| B03 | **4 anchor payoff / 5 both directions** | Ask it directly, and jurisdiction gets an answer even when nobody thought to volunteer it — the fixed question catches what the free brief missed. But answering once only covers this matter: it doesn't mean Claude now knows your practice, the next matter starts cold again. And a brief that feels thorough isn't the same as complete — only the same fixed questions, asked every time, guarantee the same facts every time. | THE ANCHOR RETURNS — the dim jurisdiction chip lights up, fills with an answer, slides into the row of five; then splits into two cards: "answered ≠ remembered" and "thorough ≠ complete" |
| **BCRY** | **6 carry-out** | A cold start isn't fixed by writing more — it's fixed by asking the same questions every time. That's what an interview does that a memory can't. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Before you start a new matter with Claude, don't just paste in a summary. Ask it to run you through a short intake: matter type, jurisdiction, conflicts, and scope — then answer each one directly. That's a cold start, done right. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | What's a Cold-Start Interview? Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the memory/brief gap; the fixed-questions mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive framing (write Claude a brief); B01 falsifies it directly — a brief only covers what its writer remembers, and the classic gaps get assumed rather than written down |
| Exactly one inference flag | none needed — the reel's one Claude-specific claim (a new conversation has no memory of a prior one) is a verifiable product property, not an inference about this particular skill's undocumented internals; see QUESTION.md for why the source carried no other facts to begin with |
| One anchor, planted early, paid off late | B02 → B03 (jurisdiction — the detail everyone assumes goes without saying) |
| Both directions | B03 — answering the interview once doesn't mean Claude now knows your practice going forward (next matter starts cold again); a brief that feels thorough doesn't mean it's complete (only the fixed questions guarantee the same facts every time) |
| No design judgment | B01–B03 state what a fixed interview does and why a brief alone can't, never a verdict on whether any specific skill or tool was well designed |

## Deliberately not claimed

- **Not a specific Claude product feature.** Because the source sheet's
  actual facts were never written (see QUESTION.md), this script describes
  the generic mechanics of a cold-start-interview practice (fixed questions
  vs. a remembered brief) rather than citing any particular tool's UI,
  question list, or output format.
- **Not that memory never carries forward.** The reel doesn't claim every
  Claude surface forgets everything always — only that a new conversation,
  absent context explicitly carried into it, starts without one. That's the
  ordinary, documented behavior the whole reel rests on.
- **No accusation that anyone was careless.** A skipped jurisdiction detail
  is presented as an ordinary gap in an informal brief, not a failure by any
  named person or team.

## Handoff prompt (BHTF, read aloud)

> "Before we start this matter, don't assume you know the details. Ask me a
> short fixed intake: matter type, jurisdiction, any conflicts, and scope.
> Ask them one at a time and wait for my answers before doing anything
> else."

Why it's worth running: it forces the same fixed list every time, instead
of trusting whatever you remembered to volunteer in a free-form brief —
which is the exact gap the reel is built around.

---
**GATE P — signed:** reconstructed per QUESTION.md; no human sign-off exists
for the original placeholder script.
