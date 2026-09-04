# Claude, Funding Digest. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `financial-services/claude-liam-funding-digest`, Teardown → Plain).*
*Register: **Plain** — explain, then stop. Carry-out written first (CARRY-OUT.md).*

**Cold open:** BrutalistHesitantWriter (Remotion, free/local). **Narrator:** Liam, Kokoro `am_onyx`.
**Channel skin:** Humanitarians AI — outro via `OutroSeries`/`OutroCTA`, handle `@HumanitariansAI`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | hesitant writer | "Someone assumed Claude already knows what belongs in a good funding digest. Not quite — it has to be told, in a file it reads before acting. Here's what that file actually spells out." | writer types "Claude already KNOWS what a good funding digest should say, right?", hesitates on KNOWS, corrects to "has to be told" — lands "Claude already has to be told what a good funding digest should say, right?" |
| B01 | anatomy | A skill is a folder Claude reads before it works. This one is funding-digest. The SKILL.md contains the full instruction set — plain language, no hidden logic. Claude reads it, then acts. The file is the program. | reused `SkillTeardownAnatomy` — LICENSE / SKILL.md / references folder tree |
| B02 | pipeline | The pipeline is in the Steps section. Claude reads each step in order and executes it. Linear — no branching unless the step says so. | reused `SkillTeardownPipeline` — read → execute → return |
| **B03** | **5 both directions** | Ask for exactly what the file names — a funding digest for the sectors or companies you're watching — and you get the same one-page slide, with the same fields, every time. Ask for something the file never mentions — a different format, a metric it doesn't list — and there's nothing else backing it up. The file is the entire spec. | `MedhavyTwoColumnCard` — "what the file names" vs. "what it doesn't say" |
| **BCRY** | **6 carry-out** | A skill doesn't make Claude judge what's newsworthy. It gives Claude one exact recipe — and outside that recipe, Claude has nothing written down to follow. | the sentence, alone, serif, large — `WantQuote` |
| BHTF | your turn handoff | Your turn. Here's the prompt — read it with me. Pick a report or slide you regularly ask for — a weekly recap, a status digest, anything you repeat. Before you ask Claude to write it, list every field and trigger phrase you actually expect it to cover. Then ask Claude to produce it, and check whether anything you expected is missing, or whether it added something you never asked for. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro series | Claude, Funding Digest. | `OutroSeries` — title restate |
| BCTA | outro cta | …Liam, in for Bear. | `OutroCTA` — handle @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| No judgment | B03 states the same underlying facts as the source's B03/BVDT (repeatable output for named triggers, nothing for anything outside the spec) as a both-directions split, not a "gets right / where it bites" verdict; the source's `SkillTeardownMechanism`-as-verdict framing and `ClaudeVerdictArtifact` "Verdict" card are both dropped rather than reused, because the verdict framing lives in the narration and the card title, not just in the props |
| Stakes → wrong guess → correction | carried entirely by B00 (WRITER LAW): the naive "Claude already knows" framing is spoken, corrected, and the corrected question is read, before any mechanism beat starts |
| Mechanism | B01–B02, reused verbatim from the source (`SkillTeardownAnatomy`, `SkillTeardownPipeline`) — already descriptive, not evaluative, in the original narration |
| Both directions | B03 — named-trigger requests get the fixed output; anything outside the file's stated scope has no spec to fall back on |
| Carry-out | BCRY compresses "recipe vs. judgment, named vs. unnamed," not the funding-digest skill as a topic |
| Hedge words | none outside a flag; `one_flag` in `beat_sheet.json` metadata is N/A — every claim here is carried directly from the source sheet's own quoted skill description, not an inference this build is making |

## Deliberately not claimed

- **Not "Claude decides what's newsworthy."** B00's correction and B03 both
  state the opposite: the output is fixed by named trigger phrases and named
  fields, not by Claude's own editorial judgment about market relevance.
- **Not "the skill covers every request."** B03 states both directions
  explicitly: requests matching the file's named triggers get the same output
  every run; requests outside that scope have nothing written down to guide
  them. The source's overall "PASS" framing (`PEDAGOGY.md`) is not restated —
  this reel describes the constraint, it doesn't grade the skill.
- **No invented technical specifics.** Every trigger phrase, file name, file
  size, and output field in B00–B03 is carried verbatim from the source
  sheet's own quoted skill description and its `SkillTeardownAnatomy`/
  `SkillTeardownPipeline` component props (see QUESTION.md).

## Handoff prompt (BHTF, read aloud)

> "Pick a report or slide you regularly ask for — a weekly recap, a status
> digest, anything you repeat. Before you ask Claude to write it, list every
> field and trigger phrase you actually expect it to cover. Then ask Claude to
> produce it, and check whether anything you expected is missing, or whether
> it added something you never asked for."

Why it's worth running: it turns the reel's central distinction — a fixed
recipe versus open-ended judgment — into something checkable on any recurring
request the viewer already makes, not just a funding digest.

---
**GATE P — signed:** ______________________  (human)
