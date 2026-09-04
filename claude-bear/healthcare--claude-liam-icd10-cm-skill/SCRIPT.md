# Claude, Icd10 Cm Skill. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-liam-icd10-cm-skill`, Teardown). Register: **Plain**.
7 beats ≈ 1:35.*

*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** BrutalistHesitantWriter (Remotion, no puppet host — hai-simple's WRITER LAW).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Hand Claude a clinical note and it sounds like it should diagnose the patient. It doesn't — it only turns what's already documented into billing codes. So what does icd10-cm-skill actually do?" | BrutalistHesitantWriter — types "Give Claude a clinical note / and it diagnoses the patient. / Wait — what does / icd10-cm-skill actually do?", trigger "diagnoses" → "codes" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is icd10-cm-skill. Its SKILL.md holds the full instruction set, in plain language — no hidden logic. Claude reads the file, then acts on it. | SkillTeardownAnatomy — file tree, SKILL.md accented |
| B02 | pipeline | The instructions live in a Steps section. Claude reads each step in order, and runs it — a clinical note in, a set of billable codes out. No branching, unless a step says so. | SkillTeardownPipeline — Read SKILL.md → Execute → Return output |
| B03 | **mechanism (resolves the wrong guess)** | Here's the actual job: turn a clinical note into billable ICD-10-CM codes, the way a professional coder builds the claim — code only what's already documented. Not a diagnosis, not clinical judgment. Ask Claude to decide what's wrong with the patient, and that's outside the skill. | SkillTeardownMechanism — heading "Just what's documented, coded.", body = the note-to-code shape |
| **BCRY** | **carry-out** | Coding a diagnosis and making the diagnosis are two different jobs — icd10-cm-skill only does the first one. | WantQuote — the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Paste this into Claude: here's a note — chest pain, shortness of breath, history of hypertension, leg swelling on exam. List every diagnosis that's explicitly written down. Then, separately, tell me what you'd be tempted to infer — like heart failure — that you won't code, because it isn't documented. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Claude, Icd10 Cm Skill. Liam, in for Bear. | OutroCTA — HAI skin, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the naive framing (diagnose) before any mechanism is shown |
| Wrong guess surfaced *and corrected* | B00 types "diagnoses" → corrected to "codes"; B03 resolves it in narration ("not a diagnosis, not clinical judgment") |
| No inference — this reel makes no claim beyond the skill's own stated scope, so no flag is needed | n/a |
| Carry-out compresses the distinction, not the topic | BCRY: coding vs. diagnosing, not "this video is about a medical skill" |
| No design judgment | B03 states the constraint as fact (what the skill does / doesn't do), never "what it gets right / what it bites" — that framing is the source's Teardown language and is dropped here |
| Host handoff | B00 is Remotion (BrutalistHesitantWriter), not a puppet — hai-simple's WRITER LAW substitution for `simple`'s HOST LAW |

## What changed from the source (redo contract)

- **Facts kept, unchanged:** the skill is `icd10-cm-skill`; it extracts billable
  ICD-10-CM diagnosis codes from a clinical note "the way a professional coder builds
  the claim"; used when a user says "code this encounter," "assign ICD-10 codes,"
  "what diagnosis codes apply," "code this chart," or turns clinical documentation into
  claim-ready diagnosis codes; a skill is a folder Claude reads before acting, and
  `SKILL.md` is the full instruction set (2 files total: `README.md`, `SKILL.md`); the
  pipeline reads a Steps section and executes linearly, no branching unless a step says
  so; same input produces the same output every run; the limit is only what the
  `SKILL.md` specifies.
- **Register:** Teardown → Plain. The source's B03 ("Here is the Teardown moment...
  What it gets right: repeatable results. What it bites: anything outside the spec.")
  and BVDT ("Verdict"/"Know the limit: only what the file says") explicitly judge the
  design's trade-offs; Plain states the same constraint as fact (B03 here: "Not a
  diagnosis, not clinical judgment... ask Claude to decide what's wrong with the
  patient, and that's outside the skill") and lands it as the carry-out (BCRY) instead
  of a verdict artifact.
- **B00:** `ClaudeComposerAsk` (puppet-free "Hola, Liam" composer ask) →
  `BrutalistHesitantWriter`, per hai-simple's WRITER LAW. The naive framing ("it
  diagnoses the patient") makes explicit what the source's own "bites" clause already
  implied ("anything outside the spec" — deciding the diagnosis is outside the spec),
  restated here as the newcomer's wrong guess instead of a verdict.
- **BVDT → BCRY:** `ClaudeVerdictArtifact` (a "Verdict" artifact card) → `WantQuote`
  (the bare carry-out sentence), matching `simple`'s law that the verdict-recap position
  becomes the carry-out line in Plain register. Same beat slot, same beat count.
- **BHTF:** the source's prompt asked the viewer to "read the icd10-cm-skill skill,"
  which needs a specific Anthropic healthcare-plugin install a general viewer won't
  have. Substituted an equivalent paste-ready exercise that needs no install and drills
  the exact same boundary — documented vs. inferred — using a hypothetical, non-patient
  note.
- **Voice/persona:** unchanged — Liam, Kokoro `am_onyx`, "in for Bear." (source already
  used this voice; hai-simple's Liam-not-af_kore rule is satisfied without a change.)
- **Close:** BOUT's `ClaudeTitleOutro` (blank subline, `@NikBearBrown`) → `OutroCTA`
  (Humanitarians AI skin, `@HumanitariansAI`), per hai-simple's channel-skin law.
- **No AI-VIDEO, pantry, or human-drop beats existed in the source** — every source beat
  was already a registered Remotion component (`ClaudeComposerAsk`,
  `SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
  `ClaudeVerdictArtifact`), all confirmed still renderable (`./art scenes --check`). No
  NO-GENAI/NO-PANTRY substitution was needed beyond B00 (mandatory writer-open swap)
  and BOUT (mandatory HAI-skin swap).
- **Beat count:** 7 → 7 (B00, B01, B02, B03, BCRY, BHTF, BOUT). Unchanged.

## Handoff prompt (BHTF, read aloud in full)

> "Here's a note: chest pain, shortness of breath, history of hypertension, leg
> swelling on exam. List every diagnosis that's explicitly written down. Then,
> separately, tell me what you'd be tempted to infer — like heart failure — that you
> won't code, because it isn't documented."

Why it's worth running: watching Claude separate "written down" from "inferred" is
what shows the constraint this skill enforces — reading only a finished code list
hides that distinction.

---
**GATE P — signed:** ______________________  (human)
