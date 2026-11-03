# Claude, Doc Extract. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-doc-extract`, Teardown). Register: **Plain**.
7 beats ≈ 1:25.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** BrutalistHesitantWriter (Remotion, no puppet host — hai-simple's WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "A document skill sounds like it should summarize what's inside. It doesn't — it turns the file into plain text. So what does doc-extract actually do?" | BrutalistHesitantWriter — types "A document skill just summarizes the PDF. Wait — what does it actually do?", trigger "summarizes" → "extracts text from" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is doc-extract. Its SKILL.md holds the whole instruction set, in plain language — no hidden logic. Claude reads the file, then acts on it. | SkillTeardownAnatomy — file tree, SKILL.md accented |
| B02 | pipeline | The instructions live in a Steps section. Claude reads each step in order, and runs it — one document in, one plain-text result out. No branching, unless a step says so. | SkillTeardownPipeline — Read SKILL.md → Execute → Return output |
| B03 | **mechanism (resolves the wrong guess)** | Here's the actual job: turn a document into plain text — PDF, DOCX, XLSX, PPTX, RTF, or plain text, markdown, HTML. Not a summary, not an analysis — just the words, pulled out. Ask for more than that, and that's a different skill. | SkillTeardownMechanism — heading "Just the words, extracted.", body = the format list |
| **BCRY** | **carry-out** | Turning a document into text, and understanding that text, are two different jobs — doc-extract only does the first one. | WantQuote — the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: I want to extract plain text from a document — PDF, DOCX, XLSX, PPTX, RTF, or plain text, markdown, or HTML. Read the doc-extract skill, and walk me through what you'll do before you do it. Watching the plan first is what shows the constraint, not just the result. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Doc Extract. Liam, in for Bear. | OutroCTA — HAI skin, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the naive framing (summarize) before any mechanism is shown |
| Wrong guess surfaced *and corrected* | B00 types "summarizes" → corrected to "extracts text from"; B03 resolves it in narration ("not a summary... just the words") |
| No inference — this reel makes no claim beyond the skill's own stated scope, so no flag is needed | n/a |
| Carry-out compresses the distinction, not the topic | BCRY: extraction vs. understanding, not "this is a document skill" |
| No design judgment | B03 states the constraint as fact (what the skill does / doesn't do), never "what it gets right / what it bites" — that framing is the source's Teardown language and is dropped here |
| Host handoff | B00 is Remotion (BrutalistHesitantWriter), not a puppet — hai-simple's WRITER LAW substitution for `simple`'s HOST LAW |

## What changed from the source (redo contract)

- **Facts kept, unchanged:** the skill is `doc-extract`; it turns a document file (PDF,
  DOCX, XLSX, PPTX, RTF, or plain text/markdown/HTML) into plain text; a skill is a
  folder Claude reads before acting, and `SKILL.md` is the full instruction set; the
  pipeline reads a Steps section and executes linearly; the skill's only job is
  extraction, not interpretation.
- **Dropped as internal/maintainer trivia, not viewer-facing argument:** the source's
  B00 clause about `fhir` invoking `scripts/extract.ts` directly and the contracts MCP
  server bundling its own copy for self-containment. That is a note to a future
  maintainer editing the skill's source, not a fact a general viewer needs to answer
  "what does this skill do" — cutting it is a Plain-register compression, not a fact
  removed from the argument.
- **Register:** Teardown → Plain. The source's B03 ("Here is the Teardown moment...
  What it gets right: repeatable results. What it bites: anything outside the spec.")
  and BVDT ("Verdict"/"Know the limit") explicitly judge the design's trade-offs; Plain
  states the same constraint as a fact (B03 here) and lands it as the carry-out (BCRY)
  instead of a verdict artifact.
- **B00:** ClaudeComposerAsk (puppet-free "Hola, Liam" composer ask) → BrutalistHesitantWriter,
  per hai-simple's WRITER LAW. The naive framing ("it summarizes") is the source's own
  implicit reading of "extract text from a document" — the resolution in B03 was already
  in the source narration ("What it gets right... what it bites" — the *bites* clause is
  literally "anything outside the spec," i.e. anything beyond extraction, which is the
  same corrected idea, restated as fact instead of verdict).
- **BVDT → BCRY:** `ClaudeVerdictArtifact` (a "Verdict" artifact card) → `WantQuote`
  (the bare carry-out sentence), matching `simple`'s law that the verdict-recap position
  becomes the carry-out line in Plain register. Same beat slot, same beat count.
- **Voice/persona:** unchanged — Liam, Kokoro `am_onyx`, "in for Bear." (source already
  used this voice; hai-simple's Liam-not-af_kore rule is satisfied without a change.)
- **Close:** BOUT's `ClaudeTitleOutro` (blank subline, `@NikBearBrown`) → `OutroCTA`
  (Humanitarians AI skin, `@HumanitariansAI`), per hai-simple's channel-skin law.
- **No AI-VIDEO, pantry, or human-drop beats existed in the source** — every source beat
  was already a registered Remotion component (`ClaudeComposerAsk`,
  `SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
  `ClaudeVerdictArtifact`), all still renderable (`./art scenes --check`). No
  NO-GENAI/NO-PANTRY substitution was needed beyond B00 (mandatory writer-open swap)
  and BOUT (mandatory HAI-skin swap).
- **Beat count:** 7 → 7 (B00, B01, B02, B03, BCRY, BHTF, BOUT). Unchanged.

## Handoff prompt (BHTF, read aloud in full)

> "I want to extract plain text from a document — PDF, DOCX, XLSX, PPTX, RTF, or plain
> text, markdown, or HTML. Read the doc-extract skill, and walk me through what you'll
> do before you do it."

Why it's worth running: watching Claude state its plan before it acts is what shows the
constraint (extraction only, nothing interpreted) — reading the *result* alone hides that
distinction.

---
**GATE P — signed:** ______________________  (human)
