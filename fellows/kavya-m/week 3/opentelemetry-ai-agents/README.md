# OpenTelemetry for AI Agents — Kavya Mehta

STEM/AI topic film for the Humanitarians AI weekly submission (`docs/FELLOWS-SUBMISSION.md`).
It comes in two native exports: 16:9 at 3840×2160 and 9:16 at 2160×3840.

**Week:** 3 — topic (STEM/AI) video. Paired project-update video this week: `kavya-brutalist-week3-progress`.
## This week's contribution

- **Question:** when an agent ships a wrong answer, does a plain log tell you which step broke, or do you need a trace?
- **Prediction:** the same failed run will look like "finished, one warning" in a log, and the trace will point at the failing step.
- **What I built/tried:** `demo/otel_demo.py`. A scripted research agent is asked about churn in a Q3
  report; its search tool hits a misspelled index (`q3-reprots`) and returns nothing, and the answer still
  cites "p.4". A small stdlib tracer records the run in OpenTelemetry's span shape: trace id, span ids,
  parent links, timings, status, and `gen_ai.*` attributes. The script prints the run two ways, as a
  plain log and as a span tree.
- **Observed result:**
  - Plain log: "finished in 2,403 ms", the answer, and "citation not found". No failing step is recorded.
  - Trace: 5 spans, including `execute_tool search_docs  11 ms  <-- 0 hits` (index `q3-reprots`), then
    an answer span with `sources=0`, then `check_citations` with ERROR.
- **Next experiment:** instrument a real agent with the OpenTelemetry Python SDK and export over OTLP to
  a local collector. Check which GenAI attributes catch quiet failures (hit counts, token use) without
  logging sensitive prompt content.

## Human and AI work

- **My decisions, implementation and verification:** topic choice; review of script and claims *(Kavya to complete before submitting)*.
- **AI tools/voices used and what they generated:** Claude Code (Claude Opus 5.5) drafted the beat
  sheet, wrote `otel_demo.py`, and wrote these docs. Kokoro `am_onyx` (local TTS) generated all
  narration. This is a synthetic voice, not a recording of me or of Professor Brown, and the film says so
  in B00 and on the B08 card.
- **What I rejected or corrected:** the earlier draft's scenario figures were authored; they were
  replaced with running code. The film says plainly that the tracer imitates OpenTelemetry's shape and
  is not the SDK. Bear/Liam branding was removed.
- **What remains unverified or failed:**
  - No real model, search index or OpenTelemetry SDK was used. The SDK isn't installed, and no package
    was downloaded.
  - Timings and token counts come from a synthetic clock.
  - The GenAI semantic conventions are still marked "development".
  - YouTube 4K processing has not been checked.
  - The narration says the script is one "I wrote and checked" and the closing card says "reading my script", but the beat sheet and narration were drafted by Claude Code (see above). Correcting that wording means regenerating B00/B08 audio and re-exporting.

## Reproduce

- **Brutalist version/commit and date checked:** `b21f6253a336098f3f55847a9525ae6868ccbdb7` (2026-10-10),
  plus the uncommitted local scene changes listed in `kavya-semantic-layers-ai-context/README.md`
  (`Harness*` scenes, `durationSeconds`, opt-in portrait props). Checked 2026-10-28. GitHub `origin/main` has since moved to `a99b5323` (2026-10-23); these exports used the older local checkout.
- **Source commit used for this export:** not committed yet; fill in after committing this folder to your branch.
- **Beat sheet and custom scene files:** `beat_sheet.json` (16:9), `vertical/beat_sheet.json` (9:16),
  `demo/otel_demo.py`, and `runtime/remotion/src/scenes/{HarnessParts,HarnessTerminal,HarnessBoundaryCard}.tsx`.
- **Commands:** see `BUILD-PROMPT.md`. Dependencies are the toolkit's own (`./setup`). There are no external inputs.
- **Approvals and checks:** `FACTCHECK.md` (claims table; fact-check gate clean), `CHECKS-REPORT.md`,
  `SHOTLIST.md`, `PROMPTS.md`, `SOURCES.md`, `BUILD-LOG.md`, `TYPECHECK.md`, `_qc/REPORT.md`. No human
  sign-off is recorded yet.

## Watch and review

- Drive folder: https://drive.google.com/drive/folders/1YhX5prPlG97izfShV5QS5-tVPJLIN_Cf
- Landscape Drive link: *(add this file's Drive link)* — 3840×2160 — 2:17.7 — SHA-256 `116c23a93b32e5344edaf84691ce9f09a990cb5d3787bf9a0f3ec39c93cb5712`
  (local file: `renders/weekly-submission-3/landscape/OpenTelemetryAgents_KavyaMehta.mp4`; receipt status `ready`)
- Vertical Drive link: *(add this file's Drive link)* — 2160×3840 — 2:17.7 — SHA-256 `5b388c19fa0c0980b884d6e9d7feaa259258072cf3699297b78c3caf33868de9`
  (local file: `renders/weekly-submission-3/vertical/OpenTelemetryAgents_KavyaMehta.mp4`; receipt status `ready`)
- Automated checks: GATE T PASS and Gate V 0 BLOCKER / 0 MAJOR on each export. These are local
  automated passes, not human approval.
- Sources/large assets Drive link: none needed
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending

## Handoff (from `docs/FELLOWS-SUBMISSION.md`)

```text
weekly-submission/
  landscape/OpenTelemetryAgents_KavyaMehta.mp4
  vertical/OpenTelemetryAgents_KavyaMehta.mp4
```

The GitHub upload is source only: this README, both beat sheets, the `.md` files and `demo/`. Leave out
`mp3/`, `media/`, `clips/`, `_qc/` frames and every `.mp4`.
