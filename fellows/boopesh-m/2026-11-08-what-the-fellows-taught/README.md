# What the Fellows Taught — Boopesh M.

HAI progress video, week of 1–7 November 2026: what the Humanitarians AI fellows *taught* in the new work
folders they added to `nikbearbrown/humanitarians-youtube`, counted from git, with one comparison to last week,
plus my own contribution.

## This week's contribution
- **Question:** when the fellows file a week of work, what do they actually teach — and how does this week compare
  with last week, counted the same way?
- **Prediction:** mostly progress updates, with a few explainers.
- **What I built:** `code/week_stats.py` (reads only the git history, computes both weeks with one function,
  writes `code/results.json`), a 16:9 video (2:15) and a native 9:16 Short (0:50) whose numbers all come from it.
- **Observed result (`bc722c05..a953b021`, Nov 1–7 America/New_York):** 74 new work folders from 18 fellows; by a
  rough sort 50 are STEM/explainer videos, 23 progress videos, 1 hours log; 28 dated this week, 45 older work filed
  this week. The 50 topic videos by subject (rough keyword sort): AI for product managers 12 (one fellow's series),
  testing & metrics 10 (from 6 fellows), how AI models work 9, making videos with AI 8, software & data tools 5,
  other topics 4, AI in marketing & business 2. Versus last week (same script): merged PRs 30 → 26 (25 merge
  commits + 1 squash merge), new work folders 84 → 74, fellows with new folders 22 → 18, frictional logs 72 → 95.
  My own two videos from last week (One Week of Fellows 2:24 + Short 0:47; The 99.9% Accuracy Trap 2:23 + Short
  0:53; all 4K) were made and delivered for review; my GitHub pull request is still pending (fork attempt failed).
- **Prediction vs result:** wrong — two thirds of the new folders are lessons, not status updates.
- **Next experiment:** get my source folders onto GitHub, then turn one idea from my own week into a short explainer.

## Human and AI work
- **My decisions, implementation and verification:** chose the weekly-progress format and the voice (`am_onyx`,
  approved 2026-10-24); reports the failed fork; reviews the result.
- **AI tools/voices used and what they generated:** Claude (Claude Code) adapted and ran `week_stats.py`, drafted
  the script, beat sheets and Manim scenes, rendered and checked frames. Kokoro `am_onyx` speaks the narration
  (disclosed on screen and in the audio).
- **What I rejected or corrected:** see [FRICTIONAL.md](FRICTIONAL.md) (DST-aware window; 26 PRs vs 28 merges;
  subject sort reading metadata; a misnamed folder; older work labelled as such; no Drive claim).
- **What remains unverified or failed:** the failed fork is my own report, not checkable from git; Drive submission
  of last week's videos is not claimed; kind and subject sorts are heuristics; pronunciation checked by phonemes only.

## Files
| File | What it is |
|---|---|
| `code/week_stats.py` | the count (git only, no network) for this week and last week; writes `results.json`; `run.log` is the run |
| `beat_sheet.json` / `make_sheet.py` | the 16:9 film as code (asserts every spoken number against `results.json`) |
| `scenes.py` | Manim scenes for the 16:9 film (read `results.json` directly) |
| `short/` | the native 9:16 Short: its own beat sheet, scenes and paperwork |
| `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `PROOF.md`, `FRICTIONAL.md`, `BUILD-LOG.md`, `description.txt` | paperwork |
| `assets/` | logos (GitHub, HAI) and one real frame from each of last week's videos |

## Reproduce
- **Brutalist version/commit and date checked:** `a99b5323`, checked 2026-11-08
- **Data:** `humanitarians-youtube` `origin/main` `a953b021` (2026-11-06 22:18 EST)
  ```bash
  python3 code/week_stats.py /path/to/humanitarians-youtube origin/main   # writes code/results.json
  python3 make_sheet.py && (cd short && python3 make_sheet.py)
  python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <this folder>          # and short/
  python3 <brutalist>/runtime/scripts/remotion_scenes.py <this folder> --only B00     # also B10, B80; short: B00
  <brutalist>/art run <this folder>
  <brutalist>/art final <this folder> --height 2160          # short/: --height 3840
  ```

## Watch and review
- Landscape Drive link (add) — 3840×2160 — 2:15 — SHA-256: a4330f9c97a218b6b72f7ca860c694338cbf9fdce8fc478fb924884f2c7ded22 (−14.1 LUFS; verified master 2cfbd322…2bd018c with audio loudness-normalised, video stream copied)
- Vertical Drive link (add) — 2160×3840 — 0:50 — SHA-256: 6690c00e32da881e5980da187fd3c7cfd7ac61bf53ec07f2cb42e157bc727b08 (−14.1 LUFS; verified master 5a073933…81a3565 with audio loudness-normalised, video stream copied)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
