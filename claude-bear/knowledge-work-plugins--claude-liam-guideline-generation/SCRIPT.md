# Claude, Guideline Generation. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-guideline-generation`, Teardown -> Plain).
Register: **Plain**. 7 beats.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter`, Remotion (no puppet host in hai-simple).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone assumes a brand voice guideline comes from Claude's own taste in writing. It doesn't — it comes from a spec that pulls patterns from your own samples. So how does that work?" | writer types "Does Claude use / taste / to write my brand / voice guideline?", hesitates on "taste", corrects to "your samples" |
| B01 | 1 stakes / 2 wrong guess, falsified | The natural guess is that a Claude brand voice guideline comes from good literary taste — an editor's ear for what your writing should sound like. But the skill doesn't work that way. It's a specification: a written instruction set that tells Claude exactly how to read your source material and pull out the same kind of patterns every time, run the same way no matter whose writing it is. Ask it to judge whether your voice is any good, and there's no step written for that. | a "Claude's taste" figure with a scattered thought-bubble, struck; a spec card (read SKILL.md / execute steps / return the guideline) lit instead |
| B02 | 3 mechanism / **4 anchor planted** | What the skill actually does: read the source material, extract the patterns the file defines, structure them into a guideline, and return the document. Watch the anchor: ten blog posts, handed over for a brand voice guideline. They get read, run through the same extraction steps, structured into sections, and returned as one guideline — tone, word choices, and examples pulled straight from those ten posts. | THE ANCHOR — four cards (READ / EXTRACT / STRUCTURE / RETURN), the "TEN BLOG POSTS" token traveling through all four, landing on "one guideline document" |
| B03 | **4 anchor payoff** / 5 both directions | That guideline holds because the extraction ran the same way every time — feed the same ten posts through twice, and the tone notes, the word choices, and the examples come back identical. But ask something outside that — say, whether the voice in those posts is actually a good one — and there's nothing tailored to reach for; the skill stops exactly where its extraction steps stop. | THE ANCHOR RETURNS, condensed; splits into "run twice — same guideline" and "any good? — no step" |
| **BCRY** | **6 carry-out** | A Claude brand voice guideline isn't its own taste in good writing — it's a fixed extraction run on your source material that returns the same patterns every time, and it stops the moment you ask it to judge rather than extract. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. Hand me a handful of your own writing samples, and run the guideline-generation skill: read them, extract the patterns, and return a brand voice guideline. Then ask me whether that voice is actually a good one, and see whether I invent an opinion, or tell you plainly that's outside what the file covers. Liam, in for Bear. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Claude, Guideline Generation. Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the wrong guess before B02 opens the mechanism |
| Wrong guess surfaced *and falsified by a case* | B01 states "good literary taste — an editor's ear"; falsified by "ask it to judge whether your voice is any good, and there's no step written for that" |
| Exactly one inference flag | none needed — every claim is stated directly from the source sheet's own intact fields (see QUESTION.md); the illustrative anchor (ten blog posts) is clearly a generic worked example, not a claim about the skill's literal internals, matching the disposition of every sibling reel in this batch |
| One anchor, planted early, paid off late | B02 -> B03 (ten blog posts: read → extract → structure → return "one guideline document," then paid off into "run twice, same guideline" / "asking whether the voice is good has no step") |
| Both failure directions | B03: "same input, same guideline, twice" (holds) / "asking it to judge the voice has nothing tailored to reach for" (flips) |
| No design judgment | B01/B02/B03 describe what the skill does and where it stops; no verdict on whether it was built well |

## Deliberately not claimed

- **Not that the skill is "wrong" or poorly designed.** Teardown's B03/BVDT
  in the source framed strengths/limits as a design-tell verdict ("what it
  gets right: repeatable results... what it bites: anything outside the
  spec"); Plain keeps only the mechanism and its two failure directions, no
  judgment on the design choice itself.
- **Not a claim about any specific company, brand, or the literal contents
  of `guideline-generation`'s SKILL.md steps.** The anchor (ten blog posts,
  read → extract → structure → return) is a generic, illustrative
  extraction scenario — no invented tool, dashboard, or output format
  beyond what the source confirms (a folder with `SKILL.md` + `references/`,
  read-then-execute-then-return, same input → same output, bounded by what
  the file specifies).
- **Not "Claude decides what a good brand voice sounds like."** The whole
  point of the wrong-guess/falsification pair (B01) is the opposite: it
  pulls patterns from the material you hand it, nothing it inferred
  independently from taste.

## Handoff prompt (BHTF, read aloud)

> "Hand me a handful of your own writing samples, and run the
> guideline-generation skill: read them, extract the patterns, and return
> a brand voice guideline. Then ask me whether that voice is actually a
> good one."

Why it's worth running: watching whether Claude invents an opinion about
an unsupported judgment question, or tells you plainly that it has nothing
tailored for it, is the fastest way to see that the guideline comes from a
written extraction procedure rather than private taste — rather than just
trusting that it does.

---
**GATE P — signed:** ______________________ (human)
