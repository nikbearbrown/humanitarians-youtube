# Self-Check Isn't Verification — Narration Script (redo, GATE P)

*Skill: `hai-simple`. Register: **Plain**. 10 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*
*Redo of `behind-the-model/claude-liam-self-check-vs-independent-verification`
— question, facts, and the five-claim worked example preserved; register
re-registered Teardown → Plain; cold open replaced with
`BrutalistHesitantWriter`; outro re-skinned Humanitarians AI.*

**Cold open:** `BrutalistHesitantWriter` (Remotion, machine-rendered — no puppet, no human step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes that when Claude checks its own answer and calls it verified, that's final. But self-check is only a first pass — so: is a self-check verification, or just a first pass?" | Writer types "Claude checked its own answer. / It says verified. / That's final. / Right?" — hesitates on "final", corrects to "a first pass" |
| B01 | 1 stakes — **ANCHOR PLANTED** | Ask Claude for a five-claim research summary, one citation per claim — then ask it to self-check each claim against the source it just cited. The first pass comes back clean: all five, verified. | THE ANCHOR — a five-row claim table, self-check column, all rows "verified" |
| B02 | 2 wrong guess | That looks like verification. The agent read the sources, wrote the claims, and checked its own work — three passes over the same material, all coming back clean. | Three passes looping over the same document, closing on a "VERIFIED" stamp |
| B03 | **2 break it** + 3 mechanism | Now swap claim three's citation for a paper that doesn't actually support it, and run the self-check again. It still comes back verified — because the check reasons from the same claim it's supposed to be testing, not from the paper itself. | The tampered claim's row; the self-check loop closes over it and still stamps "verified" |
| B04 | 3 mechanism, continued | Open the actual paper and the mismatch is immediate — the citation doesn't say what the claim says it says. That's independent verification: evidence from outside the agent's own reasoning, not another pass over the same one. | The self-check loop struck through; a separate "actual paper" icon, unconnected, flags the row "unsupported" |
| B05 | **5 direction A** | Catching this one wrong citation doesn't mean every claim got the same scrutiny — the check proves the citation matches the claim, not that the paper's underlying finding is solid. | A checked boundary around "citation matches claim"; a faded box outside reading "finding itself is solid" |
| B06 | **5 direction B** + **4 anchor payoff** | And a clean self-check elsewhere isn't proof those claims are safe either — the same five-row table, checked for real: claims one, two, four, and five hold up under an outside check too. Only the planted error needed independent eyes to catch. | THE ANCHOR RETURNS — the same five-row table, human-check column added; four rows agree, row three diverges |
| **BCRY** | **6 carry-out** | A self-check can only confirm what it already believes — verification means checking against a source the agent never wrote. | The sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. [reads the paste-ready prompt] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Self-Check Isn't Verification. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the worked case before B03/B04's mechanism claim |
| Wrong guess surfaced *and falsified by a case* | B02 states the shortcut (three clean passes look like verification); B03 falsifies it with the source's own case — a swapped citation still passes self-check |
| One anchor, planted early, paid off late | B01 → B06 (the five-claim table, first pass all clean → outside-checked with the planted error caught) |
| Both failure directions | B05 (a pass proves only what it checked) and B06 (a clean self-check elsewhere isn't proof either) |
| No design judgment | B03–B04 describe why self-check structurally can't catch its own error; no beat rules on whether the source's CLI workflow was well designed |

## Deliberately not claimed

- **Not "self-check is worthless."** B06 states the opposite — the unaltered
  claims held up under an outside check too; self-check isn't wrong, it's
  insufficient alone.
- **Not "one caught error proves the whole summary is scrutinized."** B05
  states a check proves exactly what it checks.
- **No accusation of anyone building bad tooling.** The self-check shortcut is
  an ordinary reasoning shortcut, treated as one.

## Handoff prompt (BHTF, read aloud)

> "Give me an output where you cite a source for every claim you make. Then
> self-check each claim against what you just wrote. After that, I'll open
> the actual sources myself and compare: what did your self-check catch,
> what did it miss, and why did the miss happen?"

(Adapted from the source reel's five-claim / self-check / human-check
comparison into a first-person prompt the viewer runs on their own output.)

---
**GATE P — signed:** ______________________  (human)
