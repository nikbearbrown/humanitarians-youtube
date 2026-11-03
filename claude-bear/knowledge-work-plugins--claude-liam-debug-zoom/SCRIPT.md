# Claude, Debug Zoom. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:40.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks if Claude can just fix their broken Zoom integration. It can't — not directly. What debug-zoom actually does is diagnose it: isolate where it broke, and hand back what to check." | BrutalistHesitantWriter — types "My Zoom integration is broken — can Claude just fix it?", corrects "fix" → "diagnose" |
| B01 | 1 stakes / anatomy | A skill is a folder Claude reads before it acts. This one is debug-zoom — one file, SKILL.md, plain language, no hidden logic. Its job: isolate where a Zoom integration broke, then route to the right reference — auth, API, webhook, SDK, or MCP. The output isn't a fix. It's a ranked list of what to check, in order. | one-file folder card + five failure-category chips |
| B02 | 3 mechanism / **4 anchor planted** | Take the anchor: your Zoom webhook goes silent — no events arrive. debug-zoom reads its own SKILL.md, then works the pipeline: read the steps, execute them in order, return the result. For a webhook, that means checking the signing secret, the timestamp tolerance, and the endpoint URL — in that order, because each one rules out the next. Linear. No branching unless a step says so. | pipeline strip (read → execute → return) + THE ANCHOR: ranked hypothesis list typing in, one row at a time |
| B03 | **4 anchor payoff / 5 both directions** | Work through it, and debug-zoom hands back a ranked hypothesis list: check the secret first, most likely; then tolerance; then the URL — plus how to verify each one. Stay inside auth, API, webhook, SDK, or MCP, and that ranked path holds every time. Step outside it — a billing glitch, a UI bug — and the file has nothing to say. | THE ANCHOR RETURNS — same three rows, each gets a verification checkmark; then two outside-scope cards struck through |
| **BCRY** | **6 carry-out** | debug-zoom doesn't fix your Zoom integration. It isolates where it broke and hands you a ranked list of what to check, in order. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me. My Zoom webhook has stopped delivering events. Read the debug-zoom skill and walk me through what you'll check, in what order, before you check anything. Watch whether it hands you a fix immediately, or a ranked list to verify first — the list is the actual behavior. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Debug Zoom. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states the diagnose-not-fix split and the five-category scope before B02's pipeline mechanism |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read ("Claude will fix it"); B01 falsifies it directly — the output is a ranked list, not a fix |
| Exactly one inference flag | none needed — every claim about the skill's stated job, scope, and output is read directly off the source's own narration of the SKILL.md; the anchor's specific ranked order (secret → tolerance → URL) is flagged in QUESTION.md/CARRY-OUT.md as an illustrative worked example, not a quoted fact, and stays out of the narration as an assertion of file content |
| One anchor, planted early, paid off late | B02 → B03 (a silent Zoom webhook, ranked hypothesis list) |
| Both directions | B03 — inside the five named categories (auth, API, webhook, SDK, MCP) the ranked path holds every time (holds); outside them — a billing glitch, a UI bug — the file has nothing to say (flips) |
| No design judgment | B03 states scope and silence-outside-scope as a fact about how the skill works, never a verdict on whether the skill should cover more |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B03/BVDT framed "what it
  gets right: repeatable results" / "what it bites: anything outside the
  spec" as Teardown language. Plain keeps the same underlying facts (ranked
  output; scoped to five categories) but states them as mechanism boundaries.
- **Not a claim about the file's actual internal ranking logic.** The
  anchor's specific hypothesis order is an invented worked example built to
  visualize "ranked hypothesis list plus verification steps" — the source
  reel never specifies an order, and the `source_skill` SKILL.md is not
  locally readable (its path is on Bear's other machine). See QUESTION.md.
- **Not that debug-zoom covers every Zoom failure.** It's scoped to five
  named categories; B03's both-directions beat states the outside-scope
  case plainly rather than treating it as a gap to editorialize about.

## Handoff prompt (BHTF, read aloud)

> "My Zoom webhook has stopped delivering events. Read the debug-zoom skill
> and walk me through what you'll check, in what order, before you check
> anything."

Why it's worth running: watching whether Claude returns a ranked list to
verify — rather than attempting a fix outright — is the direct test of
B01–B03's central claim, that the skill's output is diagnostic, not
corrective.

---
**GATE P — signed:** ______________________  (human)
