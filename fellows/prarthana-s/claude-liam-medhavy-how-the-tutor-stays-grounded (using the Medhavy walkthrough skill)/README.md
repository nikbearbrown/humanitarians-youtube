# How the Tutor Stays Grounded in Your Textbook — Prarthana Shetty

**Status:** production complete (2026-09-29).
- Landscape and vertical 4K finals are exported, QC'd and uploaded to Google Drive.
- The source and docs in this folder are being prepared for manual upload to GitHub.
- Nothing has been published to YouTube.

## This week's contribution

**Question:** When I ask Medhavy's tutor a question, what connects its answer back to the textbook?

**Prediction (from the code, before filming):**
- When a student asks a real question, the system searches the textbook for related passages.
- The page that's open doesn't decide that search. It only shapes the suggested-question chips.
- The passages are given to the model as context. The model also receives tutor instructions and recent conversation context.
- The same passages appear as source cards that the student can open.
- This makes answers more connected to the book and easier to verify, but not automatically correct.
- The cards are not a sentence-by-sentence citation.

**What I built/tried:**
- A source-code investigation (`AI-TUTOR-SOURCE.md`).
- A reel-local redaction wrapper (`capture/capture_masked.py`). It passed an offline self-test before any live run.
- Masked live captures of the hub and the cancer textbook, all through the admin view:
  - `run-signin` (signed out)
  - `run-pilot`
  - `run-book` (landscape)
  - `run-portrait-test`
  - `run-portrait` (portrait source)
- Reel-local Remotion scenes: `GroundingFlow`, `GroundingFlow916`, `PanelFocus916`.
- A 16-beat, 167.93 s film. It is built mostly on real Medhavy footage, and the landscape and vertical versions are composed separately.

**Observed result.** The live site behaved as the code predicted:
- Source cards arrived just before the answer text.
- "Dive deeper into all sources (10)" was present.
- Opening the 5.4.2 Gene Amplification card led to that section, on a different page from the one open.
- Some retrieved cards were less relevant (Chapter 12 and Chapter 25).
- The follow-up built on the earlier answer, while its new cards drifted off topic.
- "Thanks!" showed no cards (pilot only).
- There was no "Most Relevant" badge and no automatic page switch.
- The chips follow the page title.

See FACTCHECK.md for the full record.

**Next experiment:** none scheduled. PM review and the professors' publication decision are pending.

## Decisions made

**2026-09-23 (planning):**

| Topic | Decision |
|---|---|
| Account | Admin route only; no student dashboard is shown or described |
| Redaction | My name in the hub header is masked before recording |
| Outro | `ClaudeTitleOutro`, as the skill requires ("At Nik Bear Brown") |
| `GroundingFlow` | Lives locally in this folder; brutalist.art is not modified |
| Vertical | A separate portrait composition from a dedicated portrait-source capture (1280×720 CSS, DPR 3) |
| Tutor memory | Not cleared. Inspect first; any clear is my decision (none was made) |
| Narration | Kept within the 430–460-word budget; B10 in plain language |

**2026-09-24 to 2026-09-29 (production):**

| Topic | Decision |
|---|---|
| Masking wrapper | Built to the reviewed design, self-tested offline with a dummy term, then used for every capture |
| Landscape and portrait footage | Locked after redaction and behaviour review |
| B11 | Separate wording for landscape and vertical, each matching what its own footage shows |
| Vertical B01 | The small "What I Checked" card was removed and the main line enlarged (vertical only) |
| Vertical B10 | Portrait text enlarged to the toolkit's type floor; the side note was dropped (the vertical only) |
| Vertical B15 | Exported via direct `compile.py` with a documented exception for the locked outro's handle text height |
| Memory | Never cleared |

## Human and AI work

**My decisions, implementation and verification:**
- The topic, central question and wording rules.
- Approving AI-TUTOR-SOURCE.md.
- Confirming the admin account and signing in myself.
- Setting the mask term privately and running the signed-in captures from my own shell.
- All the production decisions above.
- Reviewing footage, narration and the final exports.
- Uploading the finals to Google Drive.

**AI tools and voices used, and what they generated:**
- **Claude Code (Opus):**
  - read the code
  - drafted AI-TUTOR-SOURCE.md, the planning files and the narration
  - built the masking wrapper and the reel-local scenes
  - ran the renders and QC
- **Kokoro `am_onyx` ("Liam"):** generated and voiced the narration used in both finals. It is an AI voice, not mine, and B00 discloses this.
- **The live Medhavy tutor:** produced the on-screen answers. They are shown unedited.

**What I rejected or corrected:**
- The reference reel's "uses this chapter as context" and "SQLite memory keyed by session".
- "The page plays no role anywhere".
- Describing memory as "per user".
- Using "Top sources used" as evidence.
- A student-dashboard branch.
- A 517-word script, which was too dense.
- "Three cards show at first" (only about 1.5 fit on screen).

**What remains unverified or open:**
- Production configuration: model, hybrid-search flag, system-prompt file. It isn't visible from the repo.
- The deploy commit behind the live site can't be verified.
- **The vertical automated type gate does not pass.** It fails on B15, the locked `ClaudeTitleOutro916` handle (49 px against a 72 px floor). This is documented in QC-REPORT.md.

## Reproduce

| Item | Value |
|---|---|
| Brutalist version and commit | `6a8380a` (2026-09-20), checked 2026-09-23 |
| Source commits | `medhavi-cancer@b8b6c21`, `medhavi-hub@efcc3f5` |
| Beat sheets | `beat_sheet.json` (landscape), `vertical/beat_sheet.json` (vertical), `vertical-windows.json` (portrait framing) |
| Reel-local scenes | `remotion/src/GroundingFlow.tsx` (`GroundingFlow`, `GroundingFlow916`), `remotion/src/PanelFocus916.tsx`, `remotion/src/theme.ts`, `remotion/src/Root.tsx`, `remotion/src/index.ts` |
| Reel-local capture wrapper | `capture/capture_masked.py`, plus `capture/plan-*.json` |
| Commands | `BUILD-PROMPT.md` (WSL Ubuntu, plain `python3`) |
| QC | `QC-REPORT.md` |
| Approvals | No formal voice or professor sign-off is recorded in `metadata.approvals`; the voice record remains `pending` |

## Watch and review

| Deliverable | Status |
|---|---|
| Landscape 4K (3840×2160, 167.93 s): `claude-liam-medhavy-how-the-tutor-stays-grounded.mp4` | Complete — QC passed; uploaded to Google Drive |
| Vertical 4K (2160×3840, 167.93 s): `claude-liam-medhavy-how-the-tutor-stays-grounded-vertical.mp4` | Complete — QC completed with documented locked-B15 toolkit exception; uploaded to Google Drive |
| Google Drive upload | Complete |
| PM review | Pending |
| YouTube 4K processing check | Pending only if/when published |
| Professors' publication decision | Pending |
