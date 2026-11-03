# "Verified" Isn't Evidence — Narration Script (redo, GATE P)

*Skill: `hai-simple`. Register: **Plain**. 10 beats ≈ 2:00.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*
*Redo of `behind-the-model/claude-liam-independent-verification-protocol` — question,
facts, and beat count preserved; register re-registered Teardown → Plain;
cold open replaced with `BrutalistHesitantWriter`; outro re-skinned Humanitarians AI.*

**Cold open:** `BrutalistHesitantWriter` (Remotion, machine-rendered — no puppet, no human step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes an agent's 'verified' means the claim is true. But verified only means something you can check — an artifact you name before the task starts. So: does verified mean true, or checkable?" | Writer types "The agent says / it's verified. / Verified means true. / Right?" — hesitates on "true", corrects to "checkable" |
| B01 | 1 stakes — **ANCHOR PLANTED** | Before an agent starts a task, ask it to generate a verification protocol: the output type, the independent evidence that would confirm it worked, the specific check for the likeliest failure, and the artifact that has to exist afterward. On a citation-summary task: evidence is a source map — which file backs which claim. | THE ANCHOR — a four-field card (OUTPUT TYPE / INDEPENDENT EVIDENCE / KEY CHECK / REQUIRED ARTIFACT), filled for a research task |
| B02 | 2 wrong guess | The natural shortcut: the agent already read every source once, so ask it to reread its own summary and confirm the citations hold. If it says "verified," that should be enough. | The agent's own output looping back into itself, a self-check circle, ending in a "VERIFIED" stamp |
| B03 | **2 break it** + 3 mechanism | But that check runs on the same reasoning that wrote the summary — a citation matched against the agent's own training data instead of the actual paper can get re-confirmed as "verified" by the exact same process. Independent evidence has to come from outside the agent's own say-so: open the cited document yourself. | The self-check loop struck through; an independent artifact icon standing apart, unconnected to the loop |
| B04 | 3 mechanism, continued | That's why the protocol gets designed before the agent starts, not after it finishes: name the output type and the required artifact first, and "verified" always cashes out to something you can go check, not just a word the agent used. | A timeline: the four-field card appears before a "TASK STARTS" gate, not after "TASK DONE" |
| B05 | **5 direction A** | A checked artifact only proves what its specific check covers — the source map proves every claim traces to a real document, not that the summary's interpretation of those documents is fair or complete. | The source-map artifact, a checkmark on "traces to a document," a faded box outside the checked boundary reading "interpretation is fair" |
| B06 | **5 direction B** + **4 anchor payoff** | And an artifact that looks different isn't a verdict on the agent generally — reapply the exact same four-field card to a code change, and the fills swap entirely: evidence becomes running the tests and reading the diff, the artifact becomes that test output plus the diff. Same structure, an independent check, every time. | THE ANCHOR RETURNS — the same four-box card, now filled for a code task |
| **BCRY** | **6 carry-out** | An agent's "verified" is a claim, not evidence — the artifact you name before the task starts is what makes it checkable. | The sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. [reads the paste-ready prompt] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | "Verified" Isn't Evidence. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the protocol structure before B03's mechanism claim |
| Wrong guess surfaced *and falsified by a case* | B02 states the self-check shortcut; B03 falsifies it with the source's own case — a citation matched to training data instead of the real document, re-confirmed by the same process |
| One anchor, planted early, paid off late | B01 → B06 (the four-field card, research fill → code fill) |
| Both failure directions | B05 (a pass doesn't prove more than its check) and B06 (a different fill isn't a verdict on the agent) |
| No design judgment | B03–B04 describe why independence and up-front design matter mechanically; no beat rules on whether the source's CLI workflow was well designed |

## Deliberately not claimed

- **Not "agents can't be trusted."** The claim is narrower: self-report isn't
  *independent* evidence, not that agents are generally unreliable.
- **Not "one artifact proves the whole task."** B05 states the opposite —
  a check proves exactly what it checks.
- **No accusation of anyone building bad tooling.** The self-check shortcut is
  an ordinary reasoning shortcut, treated as one.

## Handoff prompt (BHTF, read aloud)

> "I want to build an independent verification protocol for an agent output
> in my workflow. Walk me through the protocol structure: what makes
> verification genuinely independent rather than just re-checking the same
> way? What classes of error does each check catch — and what does the
> minimum viable protocol look like for a high-stakes output?"

(Near-verbatim from the source reel's Your Turn beat — the prompt itself
needed no register change.)

---
**GATE P — signed:** ______________________  (human)
