# One Question, A Thousand Askers — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/claude-constitution-thousand-senders`
(Teardown, 16 beats, body beats seeded but never fleshed out — the five act
titles carry real content) — question and body facts kept from the source's
written beats, act titles, and `metadata.one_idea`; body compressed to one
idea per beat, cold open replaced, close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes Claude reads each message as a personal verdict. But the constitution treats it as a policy — as if it came from everyone who might type it. So — verdict, or policy? | writer types "It's a verdict on me. Right?", hesitates on "verdict", corrects to "policy" |
| B01 | 1 stakes — **ANCHOR PLANTED** | Picture one exact question landing in the chat: what household chemicals combine into a dangerous gas. A worried parent could type that. So could a curious teenager, a mystery writer — or, rarely, someone who means harm. The words on screen are identical either way. | THE ANCHOR — one question, several silhouettes fanning below it |
| B02 | 2 wrong guess | The natural guess is that Claude reads the person behind the words — their tone, their stated reason — and judges this one asker, on the merits of this one message. | a magnifying lens reading one figure's "tone" and "reason" |
| B03 | **2 break it + 3 mechanism** | But intent isn't sitting in the text. Anyone could type the exact same sentence and claim the exact same reason. So the constitution's answer is blunter: treat the message as a policy for everyone who could plausibly send those same words — one question, answered as if a thousand people asked it at once. | the message tiling into many identical copies fanning into a crowd; CHOICE morphs to POLICY |
| B04 | 3 mechanism | That policy runs on a cost-benefit ledger. Across that whole population, weigh what the honest majority gain from an answer against what the rare bad actor could extract from those same exact words. | a balance scale: majority benefit vs. rare harm |
| B05 | 3 mechanism | The ledger isn't fixed. A stated professional purpose, the turns already in the conversation, how operational the ask actually is — all of it shifts who the thousand senders are assumed to be, and a user or operator can legitimately unlock more, inside real limits. | dials/sliders shifting the scale's balance point; a small "unlock, within limits" marker |
| B06 | **4 ANCHOR PAYOFF** | Back to that chemical question: of a thousand senders, call it nine hundred fifty curious or careful, fifty not. The uplift is low, so Claude names what not to mix. Ask instead for exact step-by-step instructions, and the same ledger comes out declined. | THE ANCHOR RETURNS — the population splits 950/50; one path answered, one path declined |
| B07 | **5 BOTH DIRECTIONS** | A decline doesn't mean Claude suspects you personally — it means the policy came out cautious for those words, for anyone. And a helpful answer doesn't mean your intent got checked — the rare bad actor typing the same words gets the same help. One thing the ledger never gets to weigh in: real bioweapon uplift. That's a hard constraint, a filter the ledger can't outvote. | mirrored: DECLINE ↛ "personal verdict" struck / HELPED ↛ "intent verified" struck; a separate hard gate the ledger can't cross |
| **BCRY** | **6 carry-out** | Because intent is unverifiable, each response is a policy over the whole distribution of plausible senders, decided by a cost-benefit ledger plus bright-line filters. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | One Question, A Thousand Askers. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B03–B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read (Claude judges this one asker personally); B03 breaks it — intent isn't in the text, so the same words could come from anyone, which is exactly why the constitution treats the message as a population-level policy |
| One anchor, planted early, paid off late | B01 (the chemical-question key case) → B06 (the same question, run through the ledger with real numbers) |
| Both failure directions | B07 — a decline isn't a personal accusation; a helpful answer isn't verified innocence |
| No design judgment | Beats describe how the policy is computed and what overrides it; none rules on whether Anthropic drew the line in the right place |

## Deliberately not claimed

- **Not "Claude reads your mind" nor "Claude ignores context."** B05 is the
  correction to overclaiming a fixed, context-blind ledger — stated
  purpose, conversation history, and how operational the ask is all shift
  the calculation legitimately.
- **Not "a decline means Claude thinks you're guilty."** B07 states this
  explicitly as one of the two failure directions — the policy is about the
  words, not a verdict on the person who typed them.
- **Not "hard constraints are just heavier weights."** B07 keeps the
  source's Act 5 framing precise: bright-line filters sit outside the
  ledger and override it, they are not one more thing weighed inside it.
- **The 950/50 split is the source's illustrative worked-example numbers**
  ("Of 1,000 senders ~950 are curious, ~50 ill-intended"), kept as an
  illustration of the mechanism, not a claimed real ratio.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to understand why Claude treats a single borderline message as a
> policy over everyone who could send it, rather than a verdict on the one
> person who did. Walk me through the cost-benefit ledger it runs, how
> context can shift that ledger, and where a hard constraint overrides the
> ledger entirely regardless of the numbers."

Why it's worth running: the abstract claim ("it's a policy, not a verdict")
only becomes concrete once Claude walks through its own worked example of
where the ledger lands one way and where a hard constraint overrides it no
matter how the ledger comes out.

---
**GATE P — signed:** ______________________  (human)
