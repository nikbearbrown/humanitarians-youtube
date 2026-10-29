# Agents Touching Data They Shouldn't — Kavya Mehta

STEM/AI topic film for the Humanitarians AI weekly submission (`docs/FELLOWS-SUBMISSION.md`).
It comes in two native exports: 16:9 at 3840×2160 and 9:16 at 2160×3840.

**Week:** 4 — topic (STEM/AI) video. Paired project-update video this week: `kavya-cabstream-week1-progress`.
## This week's contribution

- **Question:** when an agent exposes another customer's data, is that the agent's judgment, or the
  credential it was given?
- **Prediction:** with the agent's query held fixed, a credential scoped to the ticket's customer will
  stop the overreach that a wide credential allows.
- **What I built/tried:** `demo/overreach_demo.py`. Ticket 4471 from customer 812 asks which card is on
  file. A scripted support agent searches by surname (`LIKE '%Rivera%'`), which matches two customers.
  The same query runs through a tool wrapper twice: first with a grant on the whole `customers` table,
  then with a grant on a per-ticket view. The tool, not the agent, enforces the grant and writes the
  audit log.
- **Observed result:**
  - Wide: two rows (812 and 903), an answer with both card stand-ins (4417 and 9021), and an audit
    flagging 903 as outside the ticket.
  - Scoped: the full-table query is DENIED; the retry on `ticket_customer` returns one row, one card
    (4417), and an audit showing 812 only.
- **Next experiment:** reproduce this with real database roles and row-level security (for example
  PostgreSQL RLS keyed to the ticket's customer), and a real model choosing its own queries.

## Human and AI work

- **My decisions, implementation and verification:** topic choice; review of script and claims *(Kavya to complete before submitting)*.
- **AI tools/voices used and what they generated:** Claude Code (Claude Opus 5.5) drafted the beat
  sheet, wrote `overreach_demo.py`, and wrote these docs. Kokoro `am_onyx` (local TTS) generated all
  narration. This is a synthetic voice, not a recording of me or of Professor Brown, and the film says so
  in B00 and on the B08 card.
- **What I rejected or corrected:** the earlier draft's run was authored, and it is now real code. The
  film says the boundary is enforced in a tool wrapper, not claimed as database row security. Bear/Liam
  branding was removed.
- **What remains unverified or failed:**
  - The agent is scripted, and the "credential" is a table allowlist plus a view, not a production
    role, token or RLS policy.
  - All data is fake.
  - YouTube 4K processing has not been checked.
  - The narration says the script is one "I wrote and checked" and the closing card says "reading my script", but the beat sheet and narration were drafted by Claude Code (see above). Correcting that wording means regenerating B00/B08 audio and re-exporting.

## Reproduce

- **Brutalist version/commit and date checked:** `b21f6253a336098f3f55847a9525ae6868ccbdb7` (2026-10-10),
  plus the uncommitted local scene changes listed in `kavya-semantic-layers-ai-context/README.md`.
  Checked 2026-10-28. GitHub `origin/main` has since moved to `a99b5323` (2026-10-23); these exports used the older local checkout.
- **Source commit used for this export:** not committed yet; fill in after committing this folder to your branch.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16),
  `demo/overreach_demo.py`, and `runtime/remotion/src/scenes/{HarnessParts,HarnessTerminal,HarnessBoundaryCard}.tsx`.
- **Commands:** see `BUILD-PROMPT.md`. Dependencies are the toolkit's own (`./setup`). There are no external inputs.
- **Approvals and checks:** `FACTCHECK.md` (claims table; fact-check gate clean), `CHECKS-REPORT.md`,
  `SHOTLIST.md`, `PROMPTS.md`, `SOURCES.md`, `BUILD-LOG.md`, `TYPECHECK.md`, `_qc/REPORT.md`. No human
  sign-off is recorded yet.

## Watch and review

- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- Landscape Drive link: *(add this file's Drive link)* — 3840×2160 — 2:17.6 — SHA-256 `57deac66b6eb5db78d2c80674a408a83a4460f818e5c03cf12683f23769cd889`
  (local file: `renders/weekly-submission-4/landscape/AgentDataOverreach_KavyaMehta.mp4`; receipt status `ready`)
- Vertical Drive link: *(add this file's Drive link)* — 2160×3840 — 2:17.6 — SHA-256 `e2f0d440d477e3a8793998e7979d7c5d6fcadba71c334fb9509620a04480d107`
  (local file: `renders/weekly-submission-4/vertical/AgentDataOverreach_KavyaMehta.mp4`; receipt status `ready`)
- Automated checks: GATE T PASS and Gate V 0 BLOCKER / 0 MAJOR on each export. These are local
  automated passes, not human approval.
- Sources/large assets Drive link: none needed
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Handoff (from `docs/FELLOWS-SUBMISSION.md`)

```text
weekly-submission/
  landscape/AgentDataOverreach_KavyaMehta.mp4
  vertical/AgentDataOverreach_KavyaMehta.mp4
```

The GitHub upload is source only: this README, both beat sheets, the `.md` files and `demo/`. Leave out
`mp3/`, `media/`, `clips/`, `_qc/` frames and every `.mp4`.
