# A Polished Output Is Not Evidence the Work Is Correct — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/claude-liam-vox-fluency-trap`
("Why a Polished Output Is Not Evidence the Work Is Correct", Teardown register,
vox-editorial 9-beat spine) — question, facts, and argument kept; body
recompressed to one idea per beat; cold open replaced; close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx` (unchanged from source).

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes a polished, confident answer from Claude must be correct. It isn't — confidence there just means the writing is fluent. So what actually tells you the work is right? | writer types "A polished, confident answer from Claude means it's correct — right?", hesitates on "correct", corrects to "fluent" |
| B01 | 1 stakes | Claude can hand back a citation, a claim, and a number in the same fluent paragraph, in exactly the same confident voice. Nothing in how it reads tells you which parts were checked and which were invented. | citation, claim, and number cards, all glowing with the same confident "voice" mark |
| B02 | 2 wrong guess | So the natural read: if the writing is this polished and organized, the sourcing underneath is probably solid too. Confidence feels like it has to be earned. | a polished passage, a checkmark forming underneath it |
| B03 | **2 BREAK IT — ANCHOR PLANTED** | Here's the case that breaks it. A summary came back with precise phrasing and three careful citations — polished enough that she opened all three. One paper didn't exist. One said the opposite of what the summary claimed. One was from an unrelated field entirely. | THE ANCHOR — three citation cards, each snapping from confident TEAL to broken CRIMSON in sequence |
| B04 | 3 mechanism | Language models are trained to produce fluent, coherent, well organized text. That training target is coherence, not accuracy — so the model gets very good at one thing: sounding right. | two bars, FLUENCY (trained, tall, TEAL) and ACCURACY (not the target, CRIMSON question mark) |
| B05 | 3 mechanism | High-confidence prose is structurally uncorrelated with correctness. The accurate paragraph and the invented one come from the exact same process — you cannot tell them apart just by reading. | two identical-looking paragraphs, one quietly labeled TRUE, one FABRICATED |
| B06 | **3 ONE FLAG** | This means the agent's own report isn't evidence either. "I checked the sources" can mean it matched citation text against memory, never opening a document. One flag: if the agent actually used a tool to open the file, that check is real — but you can't tell which case you're in from the fluent report alone. | THE FLAG — a clipboard reading "checked" beside a locked source document, a single terracotta flag marker |
| B07 | 3 mechanism | Carlos asks an agent to draft a policy brief citing five government reports in a folder. It reads two — three are password protected — and fills the rest from training data, producing plausible-looking citations to all five. Carlos spot-checks one claim: the cited page says the opposite. | five report icons, two filled TEAL ("read"), three CRIMSON ("locked"); one citation marked wrong |
| B08 | **3 mechanism + 5 both directions — ANCHOR PAYOFF** | Run the original summary back through: open each source — one confirmed nonexistent, one confirmed contradicting, one confirmed off-topic. That's a record now, not a guess. But checking three claims doesn't make the rest of the document airtight — it only covers what got opened. And one bad citation doesn't mean the whole report is worthless — it means that one claim needs redoing. | THE ANCHOR RETURNS — the three cards, now logged as confirmed broken; two dimmed captions beneath |
| **BCRY** | **6 carry-out** | A polished answer is not evidence it's correct. Fluency and accuracy come from different places. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. [reads prompt aloud] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Why a Polished Output Is Not Evidence the Work Is Correct. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read; B03 falsifies it with the three-citation case — a polished, organized summary can still carry a nonexistent source |
| One anchor, planted early, paid off late | B03 (the three-citation summary) → B08 (the same cards, run through the source checks and logged) |
| Exactly one inference flag | **B06** — the agent's own "I checked" report is not evidence unless a tool actually opened the file, and you can't tell which case you're in from the prose alone |
| Both failure directions | B08 — what completing three source checks proves (those three claims are confirmed) vs. does not prove (the rest of the document is airtight); what one bad citation does not prove (that the whole report is worthless) |
| No design judgment | Beats describe why fluent prose isn't a correctness signal; none rules on whether any specific model or workflow was built well |

## Deliberately not claimed

- **Not "checking three claims proves the document is correct."** B08's first
  direction bounds this: the check confirms only the claims that were opened,
  not the rest of the document.
- **Not "one bad citation means the whole report is wrong."** B08's second
  direction bounds this: a failed check means that one claim needs redoing,
  not a verdict on the whole piece.
- **No accusation that any specific model fabricates more than another** —
  the three-citation summary and Carlos's example are generic illustrations
  of why fluent prose cannot substitute for opening the source.

## Handoff prompt (BHTF, read aloud then discussed)

> "I'm reviewing an AI-generated summary that has citations and specific
> claims in it. Give me a short checklist for verifying it myself — what to
> open, what to recompute, and what to trace back to one exact sentence,
> before I trust any of it."

Why it's worth running: naming the exact three moves — open, recompute,
trace to one sentence — turns "I'll double-check it" from a vague intention
into something you can actually do in the next five minutes.

---
**GATE P — signed:** ______________________  (human)
