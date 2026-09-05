# No Verification Path, No Delegation — Narration Script (GATE P)

*Skill: `hai-simple`. Register: **Plain**. Redo of
`anthropics/youtube/behind-the-model/claude-liam-verification-matrix`
("Verification Matrix: Match the Check to the Output", Teardown register, 5-beat
CLI-audience spine) — question, facts, and argument kept; body recompressed to one
idea per beat; cold open replaced; close re-skinned.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (no puppet — hai-simple WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx` (unchanged from source).

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | Someone assumes that if Claude's output reads clean, they've verified it. They haven't — only edited it. So which check actually fits a citation, a claim, or a number? | writer types "If Claude's output reads clean, I've verified it — right?", hesitates on "verified", corrects to "edited" |
| B01 | 1 stakes | Claude can hand back a citation, a claim, and a quantified number in the same paragraph, in exactly the same confident voice. Fluent, assured prose is a training habit — it looks identical whether the content underneath is verified or invented. | a citation card, a claim card, a number card, all glowing with the same confident "voice" mark |
| B02 | 2 wrong guess | So the natural move is to proofread: read it over, check that it flows, catch typos and awkward phrasing. If it reads clean, it feels checked. | a passage, a red pen sweeping over it for style, a checkmark forming |
| B03 | **2 BREAK IT — ANCHOR PLANTED** | Here's the case that breaks it. A fabricated citation — real journal name, right year, a plausible title, not one typo. Reading it start to finish catches nothing. Opening the actual source is the only step that shows it doesn't exist. | THE ANCHOR — the citation card, checkmark forming, then cracking open to "SOURCE: NOT FOUND" |
| B04 | 3 mechanism | Editing asks: is this clear, coherent, well organized? Auditing asks: is this true, traceable, and supported by the source? Two different questions — and editing never once opens the source. | two question cards side by side, EDIT vs AUDIT; only the AUDIT arrow reaches a source document |
| B05 | 3 mechanism | The verification matrix assigns the right check before you read for clarity. A citation: open the source, confirm the title and author, confirm it says what's claimed. A number: recompute a sample, check the denominator. A claim: trace it to one specific sentence, not a vibe. | three-row matrix: CITATION → open the source; NUMBER → recompute + denominator; CLAIM → trace to one sentence |
| B06 | 3 mechanism | The depth of that check should match the consequence. Personal notes: light, just scan for obvious errors. An internal planning document: moderate, spot-check the figures. Anything published, submitted, or signed: strict, full audit before it leaves your hands. A client email is strict — the consequence is yours. | three gate tiers, LIGHT/MODERATE/STRICT, widening in weight; "client email" slots into STRICT |
| B07 | **3 ONE FLAG** | One flag: this only works if you can actually reach the primary source. Some claims sit behind paywalls or private data you can't open. Then the honest move is downgrading your confidence in that piece, not skipping the check and calling it verified anyway. | THE FLAG — a locked source card, a checklist step quietly downgrading from "VERIFIED" to "UNCONFIRMED" instead of being skipped |
| B08 | **3 mechanism + 5 both directions — ANCHOR PAYOFF** | Run the fabricated citation back through the matrix: open the source — not found. That's a record, not a guess. But passing every check doesn't prove the whole output is airtight — it catches the known risks for that type, not everything. And failing one check doesn't mean the whole thing is garbage either — it means that one piece needs a closer look. | THE ANCHOR RETURNS — the citation card, now run through the matrix to "SOURCE: NOT FOUND, logged"; two dimmed captions beneath |
| **BCRY** | **6 carry-out** | No verification path, no delegation. That's not outsourcing labor — it's outsourcing judgment. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. [reads prompt aloud] … Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | No Verification Path, No Delegation. Liam, in for Bear. | OutroCTA, Humanitarians AI skin |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01; mechanism waits until B04 |
| Wrong guess surfaced *and falsified by a case* | B02 states the read; B03 falsifies it with the fabricated-citation case — a clean read cannot catch a source that doesn't exist |
| One anchor, planted early, paid off late | B03 (the fabricated-citation card) → B08 (the same card, run through the matrix and logged) |
| Exactly one inference flag | **B07** — the matrix assumes the primary source is reachable; when it isn't, the honest move is downgrading confidence, not skipping the check |
| Both failure directions | B08 — what a completed matrix pass proves (the known risks for that output type were checked) vs. does not prove (the output is fully correct); what one failed check does not prove (that the whole output is wrong) |
| No design judgment | Beats describe why a check is or isn't sufficient evidence; none rules on whether any specific model or workflow was built well |

## Deliberately not claimed

- **Not "passing the matrix proves the output is correct."** B08's first direction bounds
  this: the matrix catches known risk patterns for that output type, not every possible
  error.
- **Not "one failed check proves the output is wrong."** B08's second direction bounds
  this: a failed check means a closer look at that piece, not an automatic verdict on the
  whole output.
- **No accusation that any specific model fabricates more than another** — the fabricated
  citation is a generic illustration of why fluent prose cannot substitute for opening the
  source.

## Handoff prompt (BHTF, read aloud then discussed)

> "I want to build a verification matrix for an agent that produces citations, claims,
> and quantified findings. For each output type, tell me the specific check I'd run, the
> evidence that check needs, and how I'd implement it as a concrete tool call before the
> output ships."

Why it's worth running: naming your own output types and writing one concrete check per
type — not a general "review it" — is the difference between having a verification path
and just intending to have one.

---
**GATE P — signed:** ______________________  (human)
