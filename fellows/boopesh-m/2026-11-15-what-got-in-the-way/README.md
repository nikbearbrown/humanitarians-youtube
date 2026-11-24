# What Got in the Way — Boopesh M.

HAI progress video, week of 8–14 November 2026: what got in the way for the Humanitarians AI fellows, read from
the frictional logs they added to `nikbearbrown/humanitarians-youtube`, sorted into a few plain themes with short
examples and what fixed them, one comparison with last week, plus my own part — counted from git.

## This week's contribution
- **Question:** when the fellows write down what resisted them, what gets in the way most often, and what fixes it?
- **Prediction:** setting up the tools (installs, renders that crash) would be the biggest obstacle.
- **What I built:** `code/week_stats.py` (reads only the git history, computes both weeks with one function, sorts
  the obstacles in this week's frictional logs into themes by keyword, writes `code/results.json`), a 16:9 video
  (2:21) and a native 9:16 Short (0:49) whose numbers all come from it.
- **Observed result (`215e6a5f..dc2963ec`, Nov 8–14 America/New_York):** 32 frictional logs added by 13 fellows;
  31 describe obstacles. By a rough keyword sort (one log can count in several themes): layout & picture checks
  19 logs (8 fellows), facts & data 11, length & time 10, tools & setup 10, timing & pacing 8, the AI voice saying
  a word wrong 5; 2 logs fit none. In 17 of the 31 logs a problem was found by looking (watching the cut, viewing
  frames, re-reading the words). Versus last week, recounted by the same script: merged PRs 27 → 19 (19 merge
  commits, 0 squash merges), new work folders 75 → 53, fellows with new folders 19 → 17, frictional logs 95 → 32
  (last week's video said 26 / 74 / 18: PR #375 merged late on Sat Nov 7, after that count). My own two videos
  from last week (What the Fellows Taught 2:15 + Short 0:50; The Backtest Mirage 2:24 + Short 0:45; all 4K) were
  made and delivered for review; my GitHub pull request is still pending (fork attempt failed).
- **Prediction vs result:** wrong — tools & setup came in at 10 logs; checking the picture (19) came first.
- **Next experiment:** get my source folders onto GitHub, then run the B80 prompt on my own frictional logs.

## Human and AI work
- **My decisions, implementation and verification:** chose the weekly-progress format and the voice (`am_onyx`,
  approved 2026-10-24); reports the failed fork; reviews the result.
- **AI tools/voices used and what they generated:** Claude (Claude Code) adapted and ran `week_stats.py`, read all
  32 logs, picked and paraphrased five examples, drafted the script, beat sheets and Manim scenes, rendered and
  checked frames. Kokoro `am_onyx` speaks the narration (disclosed on screen and in the audio).
- **What I rejected or corrected:** see [FRICTIONAL.md](FRICTIONAL.md) (last week recounted 27 not 26; 19 PRs vs
  23 merges; keyword rules tightened after misfires; one example per fellow; no Drive claim).
- **What remains unverified or failed:** the failed fork is my own report, not checkable from git; Drive submission
  is not claimed; the theme sort and the "found by looking" count are heuristics; pronunciation checked by phonemes
  only.

## Files
| File | What it is |
|---|---|
| `code/week_stats.py` | the count (git only, no network) for this week and last week, plus the theme sort; writes `results.json`; `run.log` is the run (with each log's matched keywords) |
| `beat_sheet.json` / `make_sheet.py` | the 16:9 film as code (asserts every spoken number against `results.json`) |
| `scenes.py` | Manim scenes for the 16:9 film (read `results.json` directly) |
| `short/` | the native 9:16 Short: its own beat sheet, scenes and paperwork |
| `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`, `PROOF.md`, `FRICTIONAL.md`, `BUILD-LOG.md`, `description.txt` | paperwork |
| `assets/` | logos (GitHub, HAI) and one real frame from each of last week's videos |

## Reproduce
- **Brutalist version/commit and date checked:** `a99b5323`, checked 2026-11-15
- **Data:** `humanitarians-youtube` `origin/main` `dc2963ec` (2026-11-14 15:14 EST)
  ```bash
  python3 code/week_stats.py /path/to/humanitarians-youtube origin/main   # writes code/results.json
  python3 make_sheet.py && (cd short && python3 make_sheet.py)
  python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py <this folder>          # and short/
  python3 <brutalist>/runtime/scripts/remotion_scenes.py <this folder> --only B00     # also B10, B80; short: B00
  <brutalist>/art run <this folder>
  <brutalist>/art final <this folder> --height 2160          # short/: --height 3840
  ```

## Watch and review
- Landscape Drive link (add) — 3840×2160 — 2:21 — SHA-256: 371372ccbf4740c0319acbbb6923aeb8cd3e072fd40752273b98f69082bb2e7e (−14.2 LUFS; verified master 4b3e4d69…3312bc4d with audio loudness-normalised, video stream copied)
- Vertical Drive link (add) — 2160×3840 — 0:49 — SHA-256: 43c25a19cd76ed650d07d6c94ad94591b876b8f893fa46c3b1fc99ed5511f035 (−14.1 LUFS; verified master d0c0db11…be23f45c with audio loudness-normalised, video stream copied)
- PM review status: pending
- YouTube 4K processing check: pending upload
- Professors' publication decision: pending
