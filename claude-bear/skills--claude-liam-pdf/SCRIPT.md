# PDF — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-pdf`, Teardown). Register: **Plain**.
7 beats ≈ 1:40.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** BrutalistHesitantWriter (Remotion, no puppet host — hai-simple's WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Hand Claude a PDF task and it feels like one all-purpose library should handle it. It doesn't — it routes: a different tool for manipulating, extracting, and creating. So how does the pdf skill decide?" | BrutalistHesitantWriter — types "There's one PDF library / for every job. / Wait — how does / the pdf skill actually decide?", trigger "one" → "no one" |
| B01 | anatomy | The skill routes to three Python libraries — pypdf (manipulation), pdfplumber (extraction), reportlab (creation) — plus CLI tools (pdftotext, qpdf, pdftk) and two specialist files (FORMS.md, REFERENCE.md). | PdfAnatomy — 3 library cards + CLI tools + specialist files |
| B02 | self-demo | Quick reference: task → library → code, for merge/split/extract-text/extract-tables/create/CLI-merge/OCR. Plus the reportlab gotcha: never Unicode subscripts, use XML `<sub>`/`<super>` tags. | PdfOperations — 8-row quick reference + gotcha callout |
| B03 | **mechanism (resolves the wrong guess)** | The whole architecture is one routing rule: manipulation, extraction, and creation each get their own library, never one library for every job. Forms and advanced pypdfium2/pdf-lib work live in their own files. Accessibility, tagging, and signatures aren't in this skill at all. | SkillTeardownMechanism — heading "Route by task. Never guess." |
| **BCRY** | **carry-out** | There's no do-everything PDF library. The skill's job is routing each task — move, read, or build — to the tool built for it. | WantQuote — the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: I have a scanned invoice, saved as invoice.pdf. Extract all the text, pull out any tables, and save the tables to an Excel file. Watch what Claude does with the scan — a real extraction needs OCR first, not a direct text read, and the tables need to land as an actual spreadsheet, not a wall of numbers. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | PDF. Liam, in for Bear. | OutroCTA — HAI skin, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the naive framing (one library, every job) before any mechanism is shown |
| Wrong guess surfaced *and corrected* | B00 types "one" → corrected to "no one"; B03 resolves it in narration ("never one library for every job") |
| No inference — the reel makes no claim beyond the skill's own documented library/tool map, so no flag is needed | n/a |
| Carry-out compresses the distinction, not the topic | BCRY: routing by task across three domains, not "this video is about a PDF skill" |
| No design judgment | B03 states the delegation and the gap (forms/advanced files, no accessibility/signatures) as fact, never "what it gets right / what it bites" — that framing is the source's Teardown language (`PdfTell`'s two-column card, `ClaudeVerdictArtifact`) and is dropped here |
| Host handoff | B00 is Remotion (BrutalistHesitantWriter), not a puppet — hai-simple's WRITER LAW substitution for `simple`'s HOST LAW |

## What changed from the source (redo contract)

- **Facts kept, unchanged:** three Python libraries own distinct domains — `pypdf`
  (manipulation: merge/split/rotate/watermark/encrypt/decrypt/metadata), `pdfplumber`
  (extraction: text with layout, tables → pandas), `reportlab` (creation: Canvas or
  Platypus); CLI tools `pdftotext`/`qpdf`/`pdftk`; OCR is a two-step pipeline
  (`pdf2image` → `pytesseract`, never one step); the reportlab gotcha (never Unicode
  subscripts — solid black boxes in the built-in fonts; use XML `<sub>`/`<super>` tags
  in Paragraph objects instead); `FORMS.md` and `REFERENCE.md` are separate specialist
  files for form filling and advanced pypdfium2/pdf-lib use, read before attempting
  either; the skill does not cover PDF accessibility, tagging, or digital signatures.
- **Register: Teardown → Plain.** The source's B05 (`PdfTell` — "What it gets right" /
  "Where it bites" two-column judgment card) and BVDT ("Verdict" artifact,
  `ClaudeVerdictArtifact`) explicitly rank the design's trade-offs. Plain states the
  identical delegation and gap as fact (this reel's B03: "never one library for every
  job... read those before attempting either... accessibility, tagging, and digital
  signatures [are not] in this skill at all") and lands it as the carry-out (BCRY)
  instead of a verdict artifact or a gets-right/bites card — same facts, judgment
  removed.
- **B00:** `ClaudeComposerAsk` (puppet-free "Hola, Liam" composer ask, source's table +
  merge example) → `BrutalistHesitantWriter`, per hai-simple's WRITER LAW. The naive
  framing ("one all-purpose library should handle it") is the same misconception the
  source's own handoff beat (BHTF) already tests for — "if Claude uses pypdf's
  extract_text on a scanned PDF... it missed the OCR path" only matters if you assumed
  one tool does everything — restated here as the wrong guess instead of an opening ask.
- **B05 (`PdfTell`) + BVDT (`ClaudeVerdictArtifact`) → B03 (`SkillTeardownMechanism`) +
  BCRY (`WantQuote`):** the source's two judgment-carrying beats (gets-right/bites card,
  verdict artifact) collapse into one factual mechanism beat (the routing rule + what's
  delegated + what's absent) and the bare carry-out sentence — matching `simple`'s law
  that the verdict-recap position becomes the carry-out line in Plain register. Same
  beat count (7 → 7), renumbered sequentially (B00, B01, B02, B03, BCRY, BHTF, BOUT
  vs. source's B00, B01, B02, B05, BVDT, BHTF, BOUT).
- **BHTF:** kept the source's scanned-invoice OCR+tables prompt near-verbatim — it's
  already a real, paste-ready Claude prompt a general viewer can run today, and it
  drills the exact wrong guess (one tool does everything) B00 opened with. Dropped only
  the explicit "Use the PDF skill" instruction, since a general first-time viewer is
  being handed a task, not told to invoke a specific skill by name.
- **Voice/persona:** unchanged — Liam, Kokoro `am_onyx`, "in for Bear." (source already
  used this voice; hai-simple's Liam-not-af_kore rule is satisfied without a change.)
- **Close:** BOUT's `ClaudeTitleOutro` (`@NikBearBrown`) → `OutroCTA` (Humanitarians AI
  skin, `@HumanitariansAI`), per hai-simple's channel-skin law.
- **No AI-VIDEO, pantry, or human-drop beats existed in the source** — every source
  beat was already a registered Remotion component (`ClaudeComposerAsk`, `PdfAnatomy`,
  `PdfOperations`, `PdfTell`, `ClaudeVerdictArtifact`), confirmed still renderable
  (`./art scenes --check`). B01/B02 reuse `PdfAnatomy`/`PdfOperations` as-is — their
  content is purely factual (library/task/tool tables, the reportlab gotcha), no
  judgment baked into either component, so no NO-GENAI/NO-PANTRY substitution was
  needed beyond B00 (mandatory writer-open swap), B03 (mandatory judgment-card swap,
  since `PdfTell`'s "gets right/bites" columns are baked into the component pixels and
  can't be neutralized by narration alone), and BOUT (mandatory HAI-skin swap).
- **Beat count:** 7 → 7 (B00, B01, B02, B03, BCRY, BHTF, BOUT). Unchanged.

## Handoff prompt (BHTF, read aloud in full)

> "I have a scanned invoice, saved as invoice.pdf. Extract all the text, pull out any
> tables, and save the tables to an Excel file."

Why it's worth running: a scanned PDF has no text layer at all, so a correct run has
to detect that and reach for OCR (`pdf2image` → `pytesseract`) instead of a direct
text read — and the tables need to come back as an actual spreadsheet, not a wall of
numbers. Watching where that split happens is what shows the routing decision this
skill is built around.

---
**GATE P — signed:** ______________________  (human)
