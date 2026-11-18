# Frictional log — Same Number, Two Ways

_Reconstructed on 2026-11-03 from this folder's build record (git history, `beat_sheet.json` build stamps) and the working session with Claude. It was not written while the work happened. Append new entries below; never rewrite these._

- **Renders:** Google Drive https://drive.google.com/drive/folders/1uIFUKAMFJr0JWP6Fy_bIu_0sWwkZ2FGE. The 1080p first versions went up first; check that the 4K re-renders are uploaded too.
- **Evidence in this folder:** `beat_sheet.json` (current source), `slides.html` (first-version deck), `storyboard.md`, `README.md`.
- **Commits for this folder:** [97c2567 first version, 2026-08-29](https://github.com/nikbearbrown/humanitarians-youtube/commit/97c25675c3fee78ee392af8d1b605ebb180b8436) · [c0b47e5 official beat sheet, 2026-08-31](https://github.com/nikbearbrown/humanitarians-youtube/commit/c0b47e559ac93da62c0a04e22dae7cf00e0b89b5) · [34eb2cb executive-summary storyboard, 2026-08-31](https://github.com/nikbearbrown/humanitarians-youtube/commit/34eb2cb65bc0ac6449cae38f442ade1303847720) · [99ffab2 4K re-render, 2026-09-29](https://github.com/nikbearbrown/humanitarians-youtube/commit/99ffab2dd9f385ee6be88458586cbf614ee54ad7)
- **Code this video explains:** [17115ce SEC agent incl. period-end year keying, 2026-07-28](https://github.com/nikbearbrown/mycroft/commit/17115cebdab921b0b8a7727fb08da09befc401de) · [Mycroft PR #13](https://github.com/nikbearbrown/mycroft/pull/13)

## By 2026-08-29 — first version: a self-narrating HTML deck, then an MP4

**What was tried and expected.** A short explainer of the SEC agent built around one real bug: grouping annual data by the XBRL `fy` field put Microsoft's FY2025 revenue on the wrong year ($211.9B). Keying each year on its period-end date fixed it. The framing: rules catch the impossible; a cross-check catches the plausible.

**Where it resisted, and what was done next.**
- The first deliverable was an HTML deck that narrates itself in a browser, which is not a video file. Claude added a render path: headless Chrome frames + macOS `say` + ffmpeg, at 1920×1080 and 1080×1920.
- The narration sounded rushed and distorted. The cause was a pause/resume keep-alive in the speech code. It was replaced with sentence-by-sentence speech at 0.9 rate and 2.8–4.5 s pauses between slides.
- In dark mode some boxes showed light text on a light fill. Fixed with a theme colour token, then light cards with dark bold text.

**What Claude contributed, and what Asavari decided.**
- Claude: the deck, narration timing, render scripts and contrast fixes.
- Asavari: chose the fiscal-year bug as the central example; asked for slower audio with pauses between slides; asked for a real MP4 instead of an HTML file; asked for both 16:9 and 9:16.

## 2026-08-31 — rebuilt in the official Brutalist pipeline at 4K

**What was tried and expected.** Program review asked for three fixes on every video: the latest Brutalist format, 4K (3840×2160), and an executive summary on beat two. This reel was rebuilt first, to prove the pipeline before the other five.

**Where it resisted, and what was done next.** These were machine-level problems, found here once and fixed for every later video.
- `./setup` reported audio, captions and compile as blocked. The toolkit needs both `ffmpeg` and `ffprobe`, and the bundled ffmpeg had no `ffprobe`. Installed Homebrew ffmpeg (arm64) after a stale-Homebrew error (`brew update`), and removed an older x86 symlink that was shadowing it.
- The voice `af_kore` was rejected: the current toolkit allows only `af_bella` and `am_onyx`. Every beat sheet was switched to `af_bella`.
- On the first render every beat fell back to a blank slate. Remotion's bundler couldn't load its native module because the default `python3` (Anaconda) is x86_64, so it started `node` under Rosetta and looked for an x64 binary that wasn't installed. Running the render step with the arm64 `/usr/bin/python3` fixed it.
- The greeting and the opening shared beat id `B00`, so one 1.4 s clip was stretched 6.9× across the 9.6 s opening. The greeting got its own id, `B00G`.
- The visual QC gate flagged "underfill" on most beats: content filled 14–48% of the frame against a 55% target.

**What Claude contributed, and what Asavari decided.**
- Claude: diagnosed and fixed the four problems above, wrote the beat sheet, ran the renders.
- Asavari: after watching the first 4K cut, chose to fix the B00 slow-motion and keep the open Brutalist layout as it is (accepting the underfill flags) instead of redesigning denser scenes, then batch the rest.

## 2026-09-04 — 9:16 vertical version

- Built with `./art shorts`: every beat re-rendered in portrait through the toolkit's `…916` compositions (not a crop) and compiled at 2160×3840. This reel was checked first, then the other five were batched. By toolkit convention the short ends with a ~4.5 s silent card, so it runs 2:20 against the long version's 2:16.

## What is understood, and what is still open

- Understood: the ffprobe, voice and x86/arm64 problems were about this machine, not the script. The readiness check reported Remotion "ready" without ever trying a render.
- Open: underfill was accepted, not fixed. No YouTube link yet; publishing waits on approval.

## Your own notes

_Add what you remember: what surprised you, what you rejected, what you would do differently._
