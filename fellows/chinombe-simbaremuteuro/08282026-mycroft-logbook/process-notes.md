# Process notes — Mycroft Logbook (both cuts)

**Google Drive:** https://drive.google.com/drive/folders/1H2fjjURBSxWyUZ5dBAkl9Ced5ANGVGSJ?usp=drive_link
**Status:** shipped-to-drive · not yet published to YouTube
**Channel:** claude-hai · **Resolution:** 3840x2160 (16:9) / 2160x3840 (9:16)
**Last updated:** 2026-08-28

Build log for `hai-mycroft-logbook` (16:9) and `hai-mycroft-logbook-916` (9:16 Shorts). Chronological; append-only going forward — add dated entries, don't rewrite history.

## 2026-08-28 — script → both cuts built at true 4K

**Starting point:** `SCRIPT-mycroft-logbook.md` (13-beat ai-explainer script, already written in a prior pass) was the only artifact in `youtube/hai-mycroft-logbook/`. This session built both final videos from it.

**GATE L:** searched `./art scenes` before authoring anything new. Every hit that came back was hard-coded to another reel (a cost table pinned to Opus/Sonnet/Haiku, a logo sting, a brand-drift case study) — confirmed genuine punts, not slates to fill from the existing library.

**9 new Remotion components authored** (in `runtime/remotion/src/scenes/`, registered in `Root.tsx`, each portrait/landscape-responsive off one motion-math source):
- `ClaudeStatement` / `ClaudeStatement916` — BLUF statement card (B01)
- `BlindSpotFlow` — request into an unmeasured "?" box (B02)
- `ReasonStack` — numbered reasons (B03)
- `RecordCardFill` — record card filling field-by-field + version stamps (B04)
- `WriteOrderSafety` — dual-write crash-safety sequence (B05)
- `SummaryPanels` — side-by-side summary panels (B06)
- `TwoWayCompare` — wrong-vs-correct comparison rows (B07)
- `GuardCards` — guard-rail rejection/acceptance cards (B08)
- `ResultsTable` / `ResultsTable916` — the real trial-data table + ratio comparator + caveat (B09, and Shorts B02)

**9:16 Shorts cut designed** per THE SHORTS LAW: single cycle, no revision pass — B00 (cold open) → B01 (the point) → B02 (results) → B03 (verdict, condensed) → B04 (outro, points back to the long cut).

**Audio:** Kokoro `af_bella`, one pass per cut — generated once at full length straight into true-4K rendering (no throwaway 1080p pass this time, unlike an earlier build in this pipeline). `actual_duration_s` in each beat sheet is ground truth for everything downstream.

**Rendering:** true 4K via `ART_SCALE` default (scale=2). Chrome launched from this session's own container (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`) with `--chrome-mode=chrome-for-testing` — omitting that flag fails with "Old Headless mode has been removed." 16:9 compiled at `--height 2160`; 9:16 at `--height 3840` (the long edge — `--height 2160` on a portrait composition silently produces the wrong 1216×2160).

**QC pass — 3 real defects caught and fixed** (VISUAL QC LAW: judged from rendered stills actually read, not from code review alone):

1. **FILL-THE-CANVAS violations** in `BlindSpotFlow`, `WriteOrderSafety`, `TwoWayCompare` — first-pass stills showed 35–50% of the safe area empty below the main content. Fixed by converting thin text/underline treatments into full-width bordered cards (matching the already-clean `RecordCardFill` / `GuardCards` pattern) and repositioning to spread ink across more of the safe area.

2. **`ResultsTable` text-overflow bug** (shared by 16:9 B09 and Shorts B02 — the highest-stakes shared component, since a bug here hits both cuts). Root cause: a classic CSS flexbox `min-width:auto` bug — `display:flex` cell wrappers let their text ignore an explicit `width` and overflow into the next column. Worst in portrait: "CALLS" data overlapped "COST/REQUEST", and the header row's "REQUESTS" and "CALLS" visually merged. Fixed in three iterations: (1) rewrapped the header cells only — still broken; (2) rewrapped the header without `nowrap` — still broken because the *outer* wrapper was still `display:flex`; (3) removed `display:flex` entirely from both header and row-cell wrappers in favor of plain block `<div>`s with explicit `width` + `overflow:hidden`, vertically centered via `top:50%` / `translateY(-50%)`. That fixed the data rows and the 16:9 header completely, but the portrait header's "REQUESTS" still read as cramped against "CALLS" — a data/header width mismatch, not a leftover flex bug: the requests *column* is sized for its single-digit data, not for an 8-character header.

3. **Portrait header fix:** rather than steal width from columns that already rendered clean, added a portrait-only abbreviated header set (`HEAD_PORTRAIT`) — "requests" → "reqs". Re-rendered still confirmed clean with margin to spare in the 9:16 header row.

**Propagation and final QC:** re-rendered `media/B02.mp4` (916 reel) and `media/B09.mp4` (169 reel) with the fixed component, recompiled both masters (`--force`), then sampled actual frames from the *compiled* output at each beat's real timestamp — not just the isolated component stills — to confirm the fix landed in the delivered file.

**Final specs:**

| Cut | Resolution | Duration | File size |
|---|---|---|---|
| 16:9 | 3840×2160 | 3:44 (223.6s) | 8.9 MB |
| 9:16 | 2160×3840 | 0:51 (51.4s) | 2.6 MB |

**Non-blocking lint carried from the compile logs (flagged, not treated as blocking):**
- 16:9: "illustrate" motion carries 6/13 beats (46%), over the ~40% pantry-cap guideline in `MOTION.md`. Worth a look if this reel gets a revision pass.
- 9:16: SKIN LINT on B00/B04 — `ClaudeComposerAsk916` / `ClaudeTitleOutro916` flagged against COLD OPEN LAW / OUTRO LAW, which check for the unsuffixed pattern name. Reads as a linter false positive (it doesn't account for the `916` responsive-variant naming convention already used elsewhere, e.g. `ResultsTable916`) rather than an actual skin violation — noting here rather than silently ignoring it.

**Delivered:** both masters sent to Simba and committed into `youtube/hai-mycroft-logbook/` on the connected device (`hai-mycroft-logbook.mp4`, `hai-mycroft-logbook-916.mp4`).

## Open item — publishing not yet possible from this repo

Checked `RENDER-4K-AND-UPLOAD.md` and `docs/PUBLISHING.md` at the toolkit root after delivery. `brutalist.art` deliberately stops at render + stage (`./art final` → `./art post` → `youtube/TOPOST/<slug>.mp4` + `staged.json`) and never uploads — `./art final`, `./art post`, and the `youtube-publisher` script aren't even present in this checkout ("Publishing is not included in this repository," per the doc). Actual upload requires a separate, private sibling repo (`brutalist.yt`, deliberately never nested inside `brutalist.art`) holding YouTube OAuth credentials, which doesn't exist yet on this machine.

Dropping the two finished mp4s straight into the reel's `youtube/` folder (as done above) is a reasonable interim landing spot but is not the sanctioned `TOPOST` staging path — that needs `./art final` / `./art post`, which needs this reel built inside a full `brutalist.art` checkout with those scripts present (this render used a trimmed toolkit copy that doesn't have them). Still open: scaffold `brutalist.yt` per the doc's own template and go through the real render → stage → dry-run → publish loop, or treat these two files as delivered-not-published and hand YouTube upload to a separate pass.
