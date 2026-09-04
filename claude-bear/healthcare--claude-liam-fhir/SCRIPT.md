# Claude, Fhir. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-fhir`, Teardown). Register: **Plain**.
7 beats ≈ 1:35.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** BrutalistHesitantWriter (Remotion, no puppet host — hai-simple's WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Connect Claude to a hospital's records, and it sounds like it should diagnose the patient. It doesn't — it pulls structured clinical data out. So what does the fhir skill actually do?" | BrutalistHesitantWriter — types "Connect Claude to the EHR and it diagnoses the patient. Wait — what does fhir actually do?", trigger "diagnoses" → "pulls records for" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is fhir. Its SKILL.md holds the whole instruction set, in plain language — no hidden logic. Claude reads the file, then acts on it. | SkillTeardownAnatomy — file tree, SKILL.md accented |
| B02 | pipeline | The instructions live in a Steps section. Claude reads each step in order, and runs it — connect to the FHIR server, pull the record, return structured findings. No branching, unless a step says so. | FlowDiagram — Your Request → Read SKILL.md → FHIR R4 Server → Clinical Data |
| B03 | **mechanism (resolves the wrong guess)** | Here's the actual job: connect to a FHIR R4 endpoint — Epic, Oracle Health slash Cerner, MEDITECH, athenahealth, or any SMART-on-FHIR system — pull a patient's clinical data and notes, and extract structured findings. Not a diagnosis, not clinical judgment — just the data, structured. Ask for more than that, and that's a different skill. | SkillTeardownMechanism — heading "Just the data, structured.", body = the endpoint list |
| **BCRY** | **carry-out** | Pulling a patient's record out of the system, and making sense of what it means, are two different jobs — fhir only does the first one. | WantQuote — the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: I want to connect to a hospital's FHIR R4 server — Epic, Oracle Health/Cerner, MEDITECH, athenahealth, or any SMART-on-FHIR endpoint. Read the fhir skill, and walk me through what you'll do before you do it. Watching the plan first is what shows the constraint, not just the result. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Fhir. Liam, in for Bear. | OutroCTA — HAI skin, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the naive framing (diagnose) before any mechanism is shown |
| Wrong guess surfaced *and corrected* | B00 types "diagnoses" → corrected to "pulls records for"; B03 resolves it in narration ("not a diagnosis... just the data, structured") |
| No inference — this reel makes no claim beyond the skill's own stated scope, so no flag is needed | n/a |
| Carry-out compresses the distinction, not the topic | BCRY: retrieval vs. interpretation, not "this is a healthcare skill" |
| No design judgment | B03 states the constraint as fact (what the skill does / doesn't do), never "what it gets right / what it bites" — that framing is the source's Teardown language and is dropped here |
| Host handoff | B00 is Remotion (BrutalistHesitantWriter), not a puppet — hai-simple's WRITER LAW substitution for `simple`'s HOST LAW |

## What changed from the source (redo contract)

- **Facts kept, unchanged:** the skill is `fhir`; it connects to a hospital's FHIR R4
  server (Epic, Oracle Health/Cerner, MEDITECH, athenahealth, or any SMART-on-FHIR
  endpoint), pulls a patient's clinical data and notes, and extracts structured
  findings; a skill is a folder Claude reads before acting, and `SKILL.md` is the full
  instruction set; the pipeline reads a Steps section and executes linearly.
- **Register:** Teardown → Plain. The source's B03 ("Here is the Teardown moment...
  What it gets right: repeatable results. What it bites: anything outside the spec.")
  and BVDT ("Verdict" artifact, "the limit is the spec, and that is the point") judge
  the design's trade-offs; Plain states the identical constraint as a fact (B03 here)
  and lands it as the carry-out (BCRY) instead of a verdict artifact — same fact,
  judgment removed.
- **B00:** ClaudeComposerAsk (puppet-free "Hola, Liam" composer ask) → BrutalistHesitantWriter,
  per hai-simple's WRITER LAW. The naive framing ("it diagnoses the patient") is the
  same idea the source's own "bites" clause already implies (anything outside the
  spec — i.e., anything beyond structured retrieval, such as clinical interpretation),
  restated here as the newcomer's wrong guess instead of a verdict.
- **BVDT → BCRY:** `ClaudeVerdictArtifact` (a "Verdict" artifact card) → `WantQuote`
  (the bare carry-out sentence), matching `simple`'s law that the verdict-recap position
  becomes the carry-out line in Plain register. Same beat slot, same beat count.
- **Voice/persona:** unchanged — Liam, Kokoro `am_onyx`, "in for Bear." (source already
  used this voice; hai-simple's Liam-not-af_kore rule is satisfied without a change.)
- **Close:** BOUT's `ClaudeTitleOutro` (blank subline, `@NikBearBrown`) → `OutroCTA`
  (Humanitarians AI skin, `@HumanitariansAI`), per hai-simple's channel-skin law.
- **No AI-VIDEO, pantry, or human-drop beats existed in the source** — every source
  beat was already a registered Remotion component (`ClaudeComposerAsk`,
  `SkillTeardownAnatomy`, `FlowDiagram`, `SkillTeardownMechanism`,
  `ClaudeVerdictArtifact`), all still renderable (`./art scenes --check`). No
  NO-GENAI/NO-PANTRY substitution was needed beyond B00 (mandatory writer-open swap)
  and BOUT (mandatory HAI-skin swap).
- **Beat count:** 7 → 7 (B00, B01, B02, B03, BCRY, BHTF, BOUT). Unchanged.

## Handoff prompt (BHTF, read aloud in full)

> "I want to connect to a hospital's FHIR R4 server — Epic, Oracle Health/Cerner,
> MEDITECH, athenahealth, or any SMART-on-FHIR endpoint. Read the fhir skill, and walk
> me through what you'll do before you do it."

Why it's worth running: watching Claude state its plan before it acts is what shows the
constraint (structured retrieval only, nothing diagnosed) — reading the *result* alone
hides that distinction.

---
**GATE P — signed:** ______________________  (human)
