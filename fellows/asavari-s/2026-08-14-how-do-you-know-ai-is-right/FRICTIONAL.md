# Frictional log — How Do You Know an AI Is Right?

_Reconstructed on 2026-11-03 from this folder's build record (git history, `beat_sheet.json` build stamps) and the working session with Claude. It was not written while the work happened. Append new entries below; never rewrite these._

- **Renders:** Google Drive https://drive.google.com/drive/folders/1uIFUKAMFJr0JWP6Fy_bIu_0sWwkZ2FGE. The 1080p first versions went up first; check that the 4K re-renders are uploaded too.
- **Evidence in this folder:** `beat_sheet.json` (current source), `slides.html` (first-version deck), `storyboard.md`, `README.md`.
- **Commits for this folder:** [97c2567 first version, 2026-08-29](https://github.com/nikbearbrown/humanitarians-youtube/commit/97c25675c3fee78ee392af8d1b605ebb180b8436) · [c0b47e5 official beat sheet, 2026-08-31](https://github.com/nikbearbrown/humanitarians-youtube/commit/c0b47e559ac93da62c0a04e22dae7cf00e0b89b5) · [34eb2cb executive-summary storyboard, 2026-08-31](https://github.com/nikbearbrown/humanitarians-youtube/commit/34eb2cb65bc0ac6449cae38f442ade1303847720) · [99ffab2 4K re-render, 2026-09-29](https://github.com/nikbearbrown/humanitarians-youtube/commit/99ffab2dd9f385ee6be88458586cbf614ee54ad7)

## By 2026-08-29 — first version: a self-narrating HTML deck, then an MP4

- Second of the three AI/STEM videos Asavari chose: why a convincing demo isn't evidence, and what an honest evaluation needs (an answer key written first, an independent grader, a test that can't be gamed).
- Built with the same deck-and-render path as Same Number, Two Ways (headless Chrome + macOS `say` + ffmpeg), in 16:9 and 9:16, named per the program convention.
- Claude: deck and narration. Asavari: the topic.

## 2026-08-31 to 2026-09-02 — rebuilt in the official Brutalist pipeline at 4K

**Where it resisted, and what was done next.**
- This one finished two days after the others. One beat's clip (`B04`) was cut off mid-write when a Claude command hit its two-minute time limit during the render. The file existed but couldn't be read ("moov atom not found"), so the compile failed. The beat was deleted, re-rendered in the background without a time limit, and the video recompiled (1:46).
- Copying the finished videos to the Desktop folder picked this master up while it was still being written (1.3 MB, unreadable). It was re-copied from the finished source, and all files were re-checked for resolution and length.

**What Claude contributed.** Claude caused the cut-off render and fixed it. Otherwise the same as the other rebuilt videos: built after the machine problems were fixed on Same Number, Two Ways, with the same accepted underfill flags.

## 2026-09-04 — 9:16 vertical version

- Portrait re-render through the `…916` compositions at 2160×3840, plus the toolkit's silent end card (1:50).

## What is understood, and what is still open

- Understood: a file that exists isn't a file that's finished. Long renders belong in the background, and outputs get checked for readability, not just presence.
- The narration is general explanation, not sourced claims; no `FACTCHECK.md` was written. No YouTube link yet.

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
