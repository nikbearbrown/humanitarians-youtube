# Frictional log — Ticker to Truth

_Reconstructed on 2026-11-03 from this folder's build record (git history, `beat_sheet.json` build stamps) and the working session with Claude. It was not written while the work happened. Append new entries below; never rewrite these._

- **Renders:** `ticker-to-truth.mp4` (16:9, 2:02) and `short/ticker-to-truth-short.mp4` (9:16, 2:07). Not committed; to be uploaded to the Google Drive folder https://drive.google.com/drive/folders/1uIFUKAMFJr0JWP6Fy_bIu_0sWwkZ2FGE.
- **Evidence in this folder:** `beat_sheet.json` (the only source), `README.md`.
- **Commit for this folder:** [99ffab2 added 2026-09-29](https://github.com/nikbearbrown/humanitarians-youtube/commit/99ffab2dd9f385ee6be88458586cbf614ee54ad7)
- **Code this video explains:** [Mycroft PR #13](https://github.com/nikbearbrown/mycroft/pull/13)

## 2026-09-28 — new Mycroft explainer, 16:9 + 9:16

**What was tried and expected.** An end-to-end overview of the SEC agent as the through-line for the three deep-dive Mycroft videos: ticker → CIK → official XBRL → normalized metrics → validation, in five deterministic steps.

**Where it resisted, and what was done next.**
- The render itself was clean: 8 beats, 0 failures, both formats.
- The scratch build script had been wiped by a session restart and had to be recreated before rendering.

**What Claude contributed, and what Asavari decided.**
- Claude recommended a different Mycroft topic, "Provenance: every number has a receipt." Asavari chose the full-pipeline overview instead.
- While planning, Asavari asked why the project doesn't use AI agents. Claude's answer: deterministic extraction is the point, because a model in the extraction path would make the numbers non-reproducible and impossible to audit. The video's closing beat makes the same point.
- Claude wrote the beat sheet and rendered it.

## What is understood, and what is still open

- This was rendered before the 2026-10-31 benchmark work found the tag-migration bug. The narration ("an ordered list of known XBRL tags … records exactly which tag matched") is still accurate, but doesn't mention that the agent now resolves tags per reporting period.
- No YouTube link yet; publishing waits on approval.

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
