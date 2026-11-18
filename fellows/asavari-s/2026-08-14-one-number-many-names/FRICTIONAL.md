# Frictional log — One Number, Many Names

_Reconstructed on 2026-11-03 from this folder's build record (git history, `beat_sheet.json` build stamps) and the working session with Claude. It was not written while the work happened. Append new entries below; never rewrite these._

- **Renders:** Google Drive https://drive.google.com/drive/folders/1uIFUKAMFJr0JWP6Fy_bIu_0sWwkZ2FGE. The 1080p first versions went up first; check that the 4K re-renders are uploaded too.
- **Evidence in this folder:** `beat_sheet.json` (current source), `slides.html` (first-version deck), `storyboard.md`, `README.md`.
- **Commits for this folder:** [97c2567 first version, 2026-08-29](https://github.com/nikbearbrown/humanitarians-youtube/commit/97c25675c3fee78ee392af8d1b605ebb180b8436) · [c0b47e5 official beat sheet, 2026-08-31](https://github.com/nikbearbrown/humanitarians-youtube/commit/c0b47e559ac93da62c0a04e22dae7cf00e0b89b5) · [34eb2cb executive-summary storyboard, 2026-08-31](https://github.com/nikbearbrown/humanitarians-youtube/commit/34eb2cb65bc0ac6449cae38f442ade1303847720) · [99ffab2 4K re-render, 2026-09-29](https://github.com/nikbearbrown/humanitarians-youtube/commit/99ffab2dd9f385ee6be88458586cbf614ee54ad7)
- **Code this video explains:** [17115ce concept map, 2026-07-28](https://github.com/nikbearbrown/mycroft/commit/17115cebdab921b0b8a7727fb08da09befc401de) · [c0d2b33 custom-extension mapping, 2026-07-30](https://github.com/nikbearbrown/mycroft/commit/c0d2b33db78f599a4a2a1677ddeeb5d3c2e4c8df) · [be2ee7e period-aware tag resolution, 2026-10-31](https://github.com/nikbearbrown/mycroft/commit/be2ee7e515d51a4bc800241543f395a6d2e3ce55) · [Mycroft PR #13](https://github.com/nikbearbrown/mycroft/pull/13)

## By 2026-08-29 — first version: a self-narrating HTML deck, then an MP4

- Explainer of concept normalization: companies tag the same figure with different XBRL concepts, so the agent tries an ordered list of acceptable tags and records which one matched. Written to pair with the Substack article of the same name.
- Built with the same deck-and-render path as Same Number, Two Ways (headless Chrome + macOS `say` + ffmpeg), in 16:9 and 9:16, named per the program convention.
- Claude: deck and narration. Asavari: chose the topic as part of the three-video Mycroft set and matched it to the article.

## 2026-08-31 — rebuilt in the official Brutalist pipeline at 4K

- Rebuilt as `beat_sheet.json` with the executive-summary beat two, voice `af_bella`, 3840×2160 (1:49).
- Built after the machine problems were fixed on Same Number, Two Ways (see that folder's log). Nothing new resisted here. It carries the same underfill flags, under the same decision to accept them.

## 2026-09-04 — 9:16 vertical version

- Portrait re-render through the `…916` compositions at 2160×3840, plus the toolkit's silent end card (1:54).

## What is understood, and what is still open

- The narration describes the agent's own design; no separate `FACTCHECK.md` was written.
- No YouTube link yet; publishing waits on approval.

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
