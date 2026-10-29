# Data Agents Win With a Better Harness, Not a Bigger Model — Kavya Mehta

STEM/AI topic film for the Humanitarians AI weekly submission (`docs/FELLOWS-SUBMISSION.md`).
It comes in two native exports: 16:9 at 3840×2160 and 9:16 at 2160×3840.

**Week:** 1 — topic (STEM/AI) video. Paired project-update video this week: `kavya-brutalist-week1-progress`.
## This week's contribution

- **Question:** when a data agent ships a confident wrong answer, is the model the problem, or the harness around it?
- **Prediction:** with the model's output held fixed, a harness that verifies its answer will catch an error that a thin harness ships.
- **What I built/tried:** `demo/harness_demo.py`, a deterministic SQLite experiment. A scripted stand-in
  for the model writes the same SQL for two harnesses. The thin harness gets the full schema, runs the
  query and returns the result. The real harness scopes the context to the tables it needs, uses a
  read-only connection, runs an invariant check (regional revenue must sum to total revenue) and keeps
  state across retries.
- **Observed result:** the thin harness returned East 720 / West 800 with 0 checks; the truth is
  400 / 500. The real harness failed its check on try 1 (1,520 ≠ 900, fan-out join on `order_items`),
  passed on try 2, and returned 400 / 500.
- **Next experiment:** replace the scripted stand-in with a real model call over many questions, and
  measure wrong-answer rate with and without the verify step.

## Human and AI work

- **My decisions, implementation and verification:** topic choice; review of script and claims *(Kavya to complete before submitting)*.
- **AI tools/voices used and what they generated:** Claude Code (Claude Opus 5.5) drafted the beat
  sheet, wrote `harness_demo.py`, wrote `HarnessBoundaryCard.tsx`, and wrote these docs. Kokoro
  `am_onyx` (local TTS) generated all narration. This is a synthetic voice, not a recording of me or of
  Professor Brown, and the film says so in B00 and on the B08 card.
- **What I rejected or corrected:** the earlier draft said the model "catches its own mistake". The
  check is the harness's, and the retry is scripted, so that line was removed. Bear/Liam branding was
  also removed.
- **What remains unverified or failed:** the demo uses a scripted model, so it shows the mechanism and
  is not a benchmark of real models. YouTube 4K processing has not been checked.
  - The narration says the script is one "I wrote and checked" and the closing card says "reading my script", but the beat sheet and narration were drafted by Claude Code (see above). Correcting that wording means regenerating B00/B08 audio and re-exporting.

## Reproduce

- **Brutalist version/commit and date checked:** `b21f6253a336098f3f55847a9525ae6868ccbdb7` (2026-10-10),
  plus uncommitted local changes. Those include the new scenes `HarnessParts.tsx`, `HarnessTerminal.tsx` and
  `HarnessBoundaryCard.tsx`; opt-in props added to `BrutalistHesitantWriter.tsx` (title and label sizes) and to
  `ClaudeVerdictArtifact916.tsx` (`lectureLayout`); and their `Root.tsx` registrations. Checked 2026-10-28. GitHub `origin/main` has since moved to `a99b5323` (2026-10-23); these exports used the older local checkout.
- **Source commit used for this export:** not committed yet; fill in after committing this folder to your branch.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16),
  `demo/harness_demo.py`, and `runtime/remotion/src/scenes/{HarnessParts,HarnessTerminal,HarnessBoundaryCard}.tsx`.
- **Commands:** see `BUILD-PROMPT.md`. Dependencies are the toolkit's own (`./setup`). There are no
  external inputs: the data is synthetic and created by the demo script.
- **Approvals and checks:** `FACTCHECK.md` (claims table), `CHECKS-REPORT.md`, `SHOTLIST.md`,
  `PROMPTS.md`, `SOURCES.md`, `_qc/REPORT.md`, `TYPECHECK.md`. No human sign-off is recorded yet.

## Watch and review

- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- Landscape Drive link: *(add this file's Drive link)* — 3840×2160 — 2:23.9 — SHA-256 `6215c0f544584b79b3b2dddd50dad47bc642719813133a4b331827b40a544780`
  (local file: `renders/weekly-submission/landscape/DataAgentsHarness_KavyaMehta.mp4`; receipt `kavya-data-agents-harness.verified.json`, status `ready`)
- Vertical Drive link: *(add this file's Drive link)* — 2160×3840 — 2:23.9 — SHA-256 `13eec2c69e1c5ba6462f214133fc6a99262f2cd28b5a561dca22723dd85d62a7`
  (local file: `renders/weekly-submission/vertical/DataAgentsHarness_KavyaMehta.mp4`; receipt `kavya-data-agents-harness-vertical.verified.json`, status `ready`)
- Automated checks on both exports: GATE T PASS; Gate V 0 BLOCKER / 0 MAJOR (`_qc/REPORT.md`, `vertical/_qc/REPORT.md`).
  These are local automated passes, not human approval.
- Sources/large assets Drive link: none needed (all sources are in this folder and under 25 MB)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Handoff (from `docs/FELLOWS-SUBMISSION.md`)

Drive filenames, both sharing one basename in separate aspect folders:

```text
weekly-submission/
  landscape/DataAgentsHarness_KavyaMehta.mp4
  vertical/DataAgentsHarness_KavyaMehta.mp4
```

The GitHub upload is source only: this README, both beat sheets, the `.md` files, `demo/`, and the
three `Harness*.tsx` scenes. Leave out `mp3/`, `media/`, `clips/`, `_qc/` frames and every `.mp4`.
