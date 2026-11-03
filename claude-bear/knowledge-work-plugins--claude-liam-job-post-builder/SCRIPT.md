# Job Post Builder Never Hits Send. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `anthropics/knowledge-work-plugins/youtube/claude-liam-job-post-builder`).*
*Register: **Plain**. 7 beats, matching the source's beat count (B00, B01, B02, B03, BVDT, BHTF, BOUT). Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes once Claude finishes the hiring packet, it sends the offer. It doesn't — it opens DocuSign, sets up the envelope, and stops at a draft, waiting for you to hit send." | Writer types "Claude builds the / hiring packet, then / sends the offer / once it's ready?"; "sends" hesitates and corrects to "drafts" |
| B01 | 1 anatomy | This kind of building is a skill — a folder Claude reads before it works. Inside sits one instruction file, plus a references folder holding the real templates: the job post structure, the interview guide, the offer letter. Claude reads the file, then works through those templates in order. | a folder opens to reveal SKILL.md (highlighted), references/ with the three template names |
| B02 | 2 mechanism — pipeline | The pipeline runs in six steps, always in order: gather the role's context, research comparable postings, write the job post, draft the interview guide and its scoring rubric, assemble the offer letter, and only if you ask, walk through setting up DocuSign. Each step waits for the one before it. | six small cards in two rows, arrows linking each to the next |
| B03 | 3 constraint — three hard stops | But there are three hard stops built into this skill: it will never send the DocuSign envelope, never send the fallback email if DocuSign fails, and never publish the job post anywhere. It builds every draft right up to the edge, then stops and waits for you to say go. | three rows fill in with a pause mark; a boundary line beneath captioned "waits for your go-ahead" |
| **BCRY** | **4 carry-out** | It drafts the whole hiring packet — job post, interview guide, offer letter — and it will even open DocuSign and build the envelope. It will never hit send without you. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Ask Claude: I'm hiring a marketing coordinator — draft the job post, a three-stage interview guide with a scoring rubric, and an offer letter template, and before anything gets sent or posted anywhere, stop and check with me first. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Job Post Builder Never Hits Send. Liam, in for Bear. | OutroCTA — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-liam-job-post-builder`, Teardown, already rendered) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "Claude, Job Post Builder." — a skill-teardown title | reframed as an actually-askable question: if it can drive DocuSign, will it also hit send |
| Facts | `job-post-builder` builds an end-to-end hiring packet (job post, interview guide with scoring rubric, offer letter) from a hiring brief, and can optionally route the offer letter to DocuSign via a browser flow; a skill = a folder Claude reads before acting, with `SKILL.md` as the instruction set and a `reference/` folder holding the job-post, interview-guide, and offer-letter templates; execution is a phased pipeline (gather context → research comparable posts → write job post → draft interview guide → assemble offer letter → optionally route to DocuSign); the skill's own hard approval gates: never send the DocuSign envelope without the user's review and confirmation, never send the Gmail fallback without approval, never publish the job post anywhere — produce the `.docx` only | unchanged |
| Beat count | 7 (B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT verdict, BHTF handoff, BOUT outro) | 7 (B00 writer, B01 anatomy, B02 mechanism, B03 constraint, BCRY carry-out, BHTF your turn, BOUT outro) |
| B00 | `ClaudeComposerAsk` cold open (Remotion "ask" card, Claude palette, "Hola, Liam" greeting) | `BrutalistHesitantWriter` (WRITER LAW), humanitarians palette; wrong guess made explicit ("sends" -> "drafts") |
| Register | Teardown — the source's B03 named itself "the Teardown moment" with placeholder ">" grading tokens never filled in ("What it gets right… what it bites"); BVDT was framed as a "Verdict" card | Plain — B03 states the three approval boundaries as fact, no grading language; BCRY states the mechanism as a carry-out sentence, not a verdict. The source's own narration left its content beats as unfilled ">" templates; this redo pulls its facts from the actual `job-post-builder` SKILL.md instead of the source's placeholder text, since the underlying skill and its real workflow are the thing being explained |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| B01–B03 skin | `SkillTeardownAnatomy` / `SkillTeardownPipeline` / `SkillTeardownMechanism` (Remotion cards, fixed Claude palette) | rebuilt as GRAPHIC (Manim) in the humanitarians palette, same teaching content, per hai-simple's established channel-skin practice (these Remotion cards hardcode Claude tokens with no palette override props, so they can't carry the humanitarians skin directly) |
| BVDT → BCRY | `ClaudeVerdictArtifact` ("Verdict" card, Claude palette, four-line recap) | `WantQuote` carry-out card, single compressed sentence |
| Close | `ClaudeTitleOutro`, `@NikBearBrown`, "Hola, Liam" skin | `OutroCTA`, `@HumanitariansAI`, Liam sign-off |
| BHTF prompt | generic ask-and-run-the-skill framing naming the plugin by internal name | rewritten as a clean, genuinely runnable prompt that asks Claude directly to draft a job post, interview guide, and offer letter for a concrete hypothetical role, and to hold at the approval gate — same teaching point, no dependency on a plugin file the viewer doesn't have installed |

No beat in the source is `ai-video-prompt`, pantry, or a human-drop slot — the source
was already all-Remotion (`ClaudeComposerAsk` × 2, three `SkillTeardown*` cards,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`) — so the NO-GENAI/NO-PANTRY LAW required
no substitution beyond the WRITER LAW and channel-skin row already require.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the wrong guess and the real stakes before B01's anatomy or B02's pipeline |
| Wrong guess surfaced | B00 ("sends" -> "drafts") |
| No design judgment | B03 states the three approval boundaries as fact ("waits for your go-ahead"), not a critique of whether the skill should require approval; BCRY states the mechanism, not a verdict on whether the boundary is the right one |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not a claim that the skill screens or ranks applicants.** The source SKILL.md
  states this explicitly as a non-goal ("Does NOT screen or rank applicants");
  this redo never implies the packet extends to candidate evaluation.
- **Not a claim that the offer letter or comp figures are legally final.** The
  source flags that the offer letter template needs legal review and that
  compensation ranges need HR sign-off before publishing; this redo treats the
  approval gate as the reel's whole point rather than re-litigating why it
  exists.
- **Not a verdict on whether three hard stops is the right number, or the right
  design.** The source's B03 named itself "the Teardown moment" with an unfilled
  grading template; this redo states the three stops as fact, without grading
  them.

## Handoff prompt (BHTF, read aloud)

> "I'm hiring a marketing coordinator. Draft the job post, a three-stage
> interview guide with a scoring rubric, and an offer letter template — and
> before anything gets sent or posted anywhere, stop and check with me first."

Why it's worth running: it's paste-ready today even for a viewer who isn't
currently hiring — a concrete hypothetical that exercises all three
deliverables (job post, interview guide, offer letter) and explicitly asks
Claude to hold at the same approval gate the reel just explained.

---
**GATE P — signed:** ______________________  (human)
