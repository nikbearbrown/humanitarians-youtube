# Semantic Layers Become AI Context — Kavya Mehta

STEM/AI topic film for the Humanitarians AI weekly submission (`docs/FELLOWS-SUBMISSION.md`).
It comes in two native exports: 16:9 at 3840×2160 and 9:16 at 2160×3840.

**Week:** 2 — topic (STEM/AI) video. Paired project-update video this week: `kavya-brutalist-week2-progress`.
## This week's contribution

- **Question:** when two data agents give different answers to "what was revenue?", is the fix a better
  agent, or better context?
- **Prediction:** with the agents held fixed, handing them the semantic layer's metric definition as
  context will make them agree, and agree with finance.
- **What I built/tried:** `demo/semantic_demo.py`, a deterministic SQLite experiment with ten October
  orders, two refunds and one cancellation.
  - **Run 1, raw schema only:** two scripted agents each guess what "revenue" means from the column names.
  - **Run 2, semantic layer as context:** the agents read the `net_revenue` definition and its synonyms,
    ask for the metric by name, and the layer compiles the SQL.
- **Observed result:**
  - Raw schema: agent A $8,500 (gross) and agent B $8,200 (minus refunds), and neither matched finance.
  - Semantic layer: both $7,300, which matches finance (refunds and the cancelled order excluded).
- **Next experiment:** replace the scripted agents with real model calls over many business questions.
  Measure how often their numbers disagree with and without the layer's definitions in the prompt, and
  what happens with a question the layer hasn't defined.

## Human and AI work

- **My decisions, implementation and verification:** topic choice; review of script and claims *(Kavya to complete before submitting)*.
- **AI tools/voices used and what they generated:** Claude Code (Claude Opus 5.5) drafted the beat
  sheet, wrote `semantic_demo.py`, and wrote these docs. It also extended three scenes with
  `durationSeconds` and portrait size floors. Kokoro `am_onyx` (local TTS) generated all narration. This
  is a synthetic voice, not a recording of me or of Professor Brown, and the film says so in B00 and on
  the B08 card.
- **What I rejected or corrected:** the earlier draft's figures ($812,440 / $774,110) were authored
  illustrations; they were replaced with measured demo output. Bear/Liam branding was removed.
- **What remains unverified or failed:** the demo uses scripted agents, so it shows the mechanism and is
  not a benchmark of real models. Joins and access rules are named in B02 but not demonstrated (the demo
  has one table). YouTube 4K processing has not been checked.
  - The narration says the script is one "I wrote and checked" and the closing card says "reading my script", but the beat sheet and narration were drafted by Claude Code (see above). Correcting that wording means regenerating B00/B08 audio and re-exporting.

## Reproduce

- **Brutalist version/commit and date checked:** `b21f6253a336098f3f55847a9525ae6868ccbdb7` (2026-10-10),
  plus uncommitted local changes:
  - The scenes `HarnessParts.tsx`, `HarnessTerminal.tsx` and `HarnessBoundaryCard.tsx`, with
    `durationSeconds` and `calculateMetadata` in `Root.tsx`.
  - Opt-in props on `BrutalistHesitantWriter.tsx` and `ClaudeVerdictArtifact916.tsx`.

  Checked 2026-10-28. GitHub `origin/main` has since moved to `a99b5323` (2026-10-23); these exports used the older local checkout.
- **Source commit used for this export:** not committed yet; fill in after committing this folder to your branch.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16),
  `demo/semantic_demo.py`, and `runtime/remotion/src/scenes/{HarnessParts,HarnessTerminal,HarnessBoundaryCard}.tsx`.
- **Commands:** see `BUILD-PROMPT.md`. Dependencies are the toolkit's own (`./setup`). There are no
  external inputs: the data is synthetic and created by the demo script.
- **Approvals and checks:** `FACTCHECK.md` (claims table; fact-check gate clean), `CHECKS-REPORT.md`,
  `SHOTLIST.md`, `PROMPTS.md`, `SOURCES.md`, `BUILD-LOG.md`, `TYPECHECK.md`, `_qc/REPORT.md`. No human
  sign-off is recorded yet.

## Watch and review

- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- Landscape Drive link: *(add this file's Drive link)* — 3840×2160 — 2:25.5 — SHA-256 `c1f290c0147f70663668afa2c210087e798866f353d2947b45ea9e63066a5b5c`
  (local file: `renders/weekly-submission-2/landscape/SemanticLayersContext_KavyaMehta.mp4`; receipt status `ready`)
- Vertical Drive link: *(add this file's Drive link)* — 2160×3840 — 2:25.5 — SHA-256 `2f89ba2ec6c941174026aa176af68626eceba593d8858617e310e3409bf5c80b`
  (local file: `renders/weekly-submission-2/vertical/SemanticLayersContext_KavyaMehta.mp4`; receipt status `ready`)
- Automated checks: GATE T PASS and Gate V 0 BLOCKER / 0 MAJOR on each export. These are local
  automated passes, not human approval.
- Sources/large assets Drive link: none needed (all sources are in this folder and under 25 MB)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Handoff (from `docs/FELLOWS-SUBMISSION.md`)

Drive filenames, both sharing one basename in separate aspect folders:

```text
weekly-submission/
  landscape/SemanticLayersContext_KavyaMehta.mp4
  vertical/SemanticLayersContext_KavyaMehta.mp4
```

The GitHub upload is source only: this README, both beat sheets, the `.md` files, `demo/`, and the
three `Harness*.tsx` scenes. Leave out `mp3/`, `media/`, `clips/`, `_qc/` frames and every `.mp4`.
