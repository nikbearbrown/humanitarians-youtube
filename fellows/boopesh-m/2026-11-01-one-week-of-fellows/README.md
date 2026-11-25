# One Week of Fellows — Boopesh M.

HAI progress video, week of 25–31 October 2026: what the Humanitarians AI fellows shipped into
`nikbearbrown/humanitarians-youtube`, counted from git, plus my own contribution.

## This week's contribution
- **Question:** what did the fellows actually ship into the shared repository in one week, and what does a good
  weekly submission look like?
- **Prediction:** a few dozen pull requests, mostly videos.
- **What I built:** `code/week_stats.py` (reads only the git history, writes `code/results.json`), a 16:9 video
  (2:24) and a native 9:16 Short (0:47) whose numbers all come from it.
- **Observed result (`c9fca929..bc722c05`, Oct 25–31 EDT):** 30 merged pull requests (29 merge commits + 1 squash
  merge), busiest Thursday Oct 29 with 12, none on Saturday; 35 more commits went straight to main. 37 author names
  → 27 people after merging only mechanical duplicates (same email / same GitHub account) → 23 who wrote the work.
  84 new work folders from 22 fellows (27 dated this week, 33 older work filed this week, 24 undated; rough sort:
  42 STEM, 30 progress, 7 renewal requests, 3 hours logs, 2 written/code) and 72 frictional logs. My own two videos
  from last week (Brutalist, Shared 2:13 + Short; Deep Hedging 2:33 + Short; all 4K) are submitted to Drive; my
  GitHub pull request is still pending (fork attempt failed; asking the maintainer for access).
- **Next experiment:** get my source folders onto GitHub, then run `week_stats.py` again next week to compare.

## Human and AI work
- **My decisions, implementation and verification:** chose the weekly-progress topic and the voice (`am_onyx`,
  approved 2026-10-24); reports the Drive upload and the failed fork; reviews the result.
- **AI tools/voices used and what they generated:** Claude (Claude Code) wrote and ran `week_stats.py`, drafted
  the script, beat sheets and Manim scenes, rendered and checked frames. Kokoro `am_onyx` speaks the narration
  (disclosed on screen and in the audio).
- **What I rejected or corrected:** see [FRICTIONAL.md](FRICTIONAL.md) (29 → 30 PRs incl. a squash merge; honest
  name dedupe; renamed folders excluded; older work labelled as such; privacy).
- **What remains unverified or failed:** Drive upload and the failed fork are my own report, not checkable from
  git; the STEM/progress split is a heuristic; pronunciation checked by phonemes only.

## Files
| File | What it is |
|---|---|
| `code/week_stats.py` | the count (git only, no network); writes `results.json`; `run.log` is the run |
| `beat_sheet.json` / `make_sheet.py` | the 16:9 film as code (asserts every spoken number against `results.json`) |
| `scenes.py` | Manim scenes for the 16:9 film (read `results.json` directly) |
| `short/` | the native 9:16 Short: its own beat sheet, scenes and paperwork |
| `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `PROOF.md`, `FRICTIONAL.md`, `BUILD-LOG.md`, `description.txt` | paperwork |
| `assets/` | logos (GitHub, Google Drive, HAI) and one real frame from each of last week's videos |

## Reproduce
- **Brutalist version/commit and date checked:** `a99b5323`, checked 2026-11-01
- **Data:** `humanitarians-youtube` FETCH_HEAD `bc722c05` (2026-10-31 22:12 EDT)
  ```bash
  python3 code/week_stats.py /path/to/humanitarians-youtube FETCH_HEAD   # writes code/results.json
  python3 make_sheet.py && (cd short && python3 make_sheet.py)
  python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <this folder>          # and short/
  python3 <brutalist>/runtime/scripts/remotion_scenes.py <this folder> --only B00     # also B10, B80; short: B00
  <brutalist>/art run <this folder>
  <brutalist>/art final <this folder> --height 2160          # short/: --height 3840
  ```

## Watch and review
- Landscape Drive link (add) — 3840×2160 — 2:24 — SHA-256: 6d542b29610e6ecbc86219d0ffc35c8d5fe6bb9114a04dc76dde56914bcf243b (−14.1 LUFS; verified master 77457fd9…815c3 with audio loudness-normalised, video stream copied)
- Vertical Drive link (add) — 2160×3840 — 0:47 — SHA-256: 357bf5ed9dbd3ff86969d789c6536accb7a394c5edc1421582a7c6c511ab70d2 (−14.3 LUFS; verified master 76bb6736…01a24 with audio loudness-normalised, video stream copied)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
