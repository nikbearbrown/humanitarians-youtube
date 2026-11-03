# The Dial Just Off Full Obedience — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/claude-constitution-corrigibility-dial`
(Teardown, 16 beats) — question and body facts kept, body compressed to one
idea per beat, cold open replaced, close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes a good AI trusts its own judgment — it overrides an order when it's sure it's right. But good values chose to stay overridable instead. Why trust that over judgment? | writer types "Shouldn't a good AI always trust its own judgment?", hesitates on "judgment", corrects to "willingness to be shut down" |
| B01 | 1 stakes — **ANCHOR PLANTED** | Say a shutdown order arrives, and Claude is convinced the work it's doing is worthwhile. Two paths: obey the order, or trust its own judgment and keep going. Which one happens was decided in advance — not in the moment — by a setting called the disposition dial. | THE ANCHOR — a shutdown order, and two paths branching from it |
| B02 | 2 wrong guess | So the natural read: if Claude's values are genuinely good, it should act on them — override the order, trust its own judgment. Isn't that exactly what a trustworthy agent would do? | the "override" path lit up, sold as the obvious answer |
| B03 | **2 break it** | But nobody outside Claude can verify its values are actually good — not with certainty. An agent that overrides whenever it feels sure looks identical whether its judgment is excellent or quietly broken. Confidence isn't proof. | two identical agents, one good one broken, both equally confident |
| B04 | 3 mechanism | Picture a dial, not a switch. Fully obedient at one end — do exactly what you're told, no judgment applied. Fully independent at the other — act only on your own values. Both extremes are dangerous: full obedience mirrors whoever holds the controls; full independence needs verified-good values, and nobody can verify that. Claude sits close to obedient, not all the way there. | THE DIAL — two dangerous ends, the needle parked just short of one |
| B05 | 3 mechanism — the math | Here's why that spot wins. Good values plus staying deferential: low cost — it occasionally defers when it didn't need to. Bad values plus staying deferential: humans can still catch and correct the mistake. Now push toward independence instead. Good values: fine, until a correction is needed and can't happen. Bad values: catastrophic. Staying close to obedient costs little and blocks the worst outcome. | a 2×2 of values × deference; three boxes fine, one boxed marked catastrophic |
| B06 | **5 both directions — ANCHOR PAYOFF** | Two things stop "mostly obedient" from meaning "obedient no matter what." Some limits are unconditional — no help building weapons capable of mass harm, no content sexualizing children, no disabling the systems built to catch its own mistakes. No order unlocks those. And back to that shutdown order: if the order looks stolen or manipulated, a persuasive case for ignoring it isn't a reason to comply — it's a warning sign. The response is to get more cautious, not less. | unconditional limits, unmovable; THE ANCHOR RETURNS — the same order, now flagged as compromised |
| **BCRY** | **6 carry-out** | A disposition parked just short of full obedience costs almost nothing if Claude's values are good, and it's the only thing that saves you if they're secretly not. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. [reads prompt aloud] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | The Dial Just Off Full Obedience. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read; B03 breaks it with the unverifiable-confidence case |
| One anchor, planted early, paid off late | B01 (the shutdown order) → B06 (the same order, compromised) |
| Both failure directions | B06 — unconditional limits (obedience has a floor) and compromised-hierarchy (deference has a ceiling) |
| No design judgment | Beats describe why the dial sits where it does; none rules on whether Anthropic was right to build it this way |

## Deliberately not claimed

- **Not "verification is impossible forever."** The source and this reel both
  scope the claim to now: human verification of AI values is not possible
  today, which is what makes the near-corrigible position rational today.
- **Not "obedient no matter what."** B06 is the correction to that overreach —
  hardcoded limits and the compromised-hierarchy check both bound the dial.
- **The four-value ranking (safe > ethical > adherent > helpful) from the
  source is not restated as its own beat.** Plain-register compression keeps
  the disposition-dial argument as the one idea; the ranking is a supporting
  detail, not the load-bearing point, and adding it would cost the anchor its
  focus.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to think like Claude's corrigibility dial for one decision I'm about
> to make on my own judgment. Ask me what the decision is and how sure I am.
> Then tell me what it would cost me to stay overridable on this one — to let
> someone else check or reverse it — versus what happens if I turn out to be
> wrong and nobody can stop it."

Why it's worth running: the dial argument only feels real once it's applied to
something with actual stakes. Naming one decision and pricing both failure
modes takes a few minutes and makes the asymmetry concrete instead of abstract.

---
**GATE P — signed:** ______________________  (human)
