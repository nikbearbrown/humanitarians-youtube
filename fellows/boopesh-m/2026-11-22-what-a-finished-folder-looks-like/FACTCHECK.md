# FACTCHECK — What a Finished Folder Looks Like (Boopesh M., week of Nov 15–21, 2026)

Every number in the narration and on screen comes from `code/results.json`, written by
`code/week_stats.py` (log: `code/run.log`). `make_sheet.py` spells the spoken numbers from
that file and asserts the story's claims against it before writing either beat sheet.

Source: `humanitarians-youtube`, `origin/main` = `2a32d04e` (Merge pull request #439,
2026-11-22 23:50:37 −05:00), cloned with `--filter=blob:none` (full history; the script reads
commit metadata and trees only, never file contents). Window: Sun Nov 15 00:00:00 to Sat
Nov 21 23:59:59 in `America/New_York` (Python `zoneinfo`, DST-aware; both weeks fall in EST, −05:00).

Determinism: the script was run twice; `results.json` and `run.log` were byte-identical
(SHA-256 `526c49ec…f291` and `00183c80…55cf`).

| # | Claim (where) | Verdict | Source / how checked | Fix / note |
|---|---|---|---|---|
| 1 | 18 pull requests merged into main, Nov 15–21 (B10 narration + card, B00 output) | ✅ | 18 first-parent “Merge pull request #N” merges with committer time in the window, 0 squash merges; list below and in `run.log` | `results.json → this_week.pr_numbers` |
| 2 | Plain count for the window: 102 commits, 24 merge commits (not spoken) | ✅ | `git rev-list --count` by committer date, reproduced in `run.log` | Matches the brief’s plain count |
| 3 | Excluded merges are not PRs | ✅ | 3 direct merges on the first-parent line (“ameya-p/Adding docs for week 9”, “Github restructuring for Renewal…”, “Weeks of 2026-10-26 to 2026-11-15…”) + 3 “Merge branch 'nikbearbrown:main' into main” commits off the first-parent line | Listed in `run.log` |
| 4 | 54 new dated work folders (B10, B30, B50) | ✅ | Folders `fellows/<fellow>/<folder>/` present at the end-of-week snapshot `5d7df2bb` and absent at the start snapshot `2946d360`: 55; 54 have a dated name | Undated `fellows/darshil-s/renewal-requests` is not counted as work (fellows README: “one dated folder per piece of work”) |
| 5 | “With direct uploads” — not every new folder came through a PR (B10) | ✅ | e.g. `fellows/chinombe-s/11142026Quantization` arrived in `5bac5461` “Add files via upload”, `fellows/hrishikesh-p/2026-11-20-RamanEffect` in `79df19b5`, both direct commits on main | — |
| 6 | 19 fellows (B10) | ✅ | distinct `fellows/<fellow>` among the 54 | — |
| 7 | “Almost always a video and its notes” (B10) | ✅ | 51 of 54 folders hold a beat sheet | Wording kept soft (“almost always”) |
| 8 | Piece counts: beat sheet 51, FRICTIONAL 45, README 43, FACTCHECK 39, SHOTLIST 35, PROMPTS 35, code 35, description 12, PROOF 4 (B30, Short B10) | ✅ | `results.json → summary.piece_counts_sorted`; rules below | — |
| 9 | No folder had all nine; 8 folders had eight; all 8 lack only PROOF (B40, Short B20) | ✅ | `summary.folders_with_all_pieces = 0`, `max_pieces = 8`, `folders_at_max_count = 8`, `missing_from_every_top_folder = ["PROOF"]` | — |
| 10 | Example folders `rohan-v/2026-11-20-how-auto-tune-works` and `likhith-r/2026-11-14-word2vec-king-man-woman-queen` each have README, FACTCHECK, FRICTIONAL, SHOTLIST, PROMPTS, beat sheet, code, description (B40) | ✅ | `results.json → top_folder_pieces` | Fellows appear only by folder name; no fellow is named in narration |
| 11 | Week before (Nov 8–14), recounted with the same code: 20 PRs, 54 work folders, 34 with a frictional log, 18 fellows (B50) | ✅ | `results.json → last_week_recount` | — |
| 12 | Published last week: 19 PRs · 53 folders · 17 fellows · 32 frictional logs; the recount differs (B50 on screen) | ✅ | Numbers as published (given in the brief). Re-running last week with the snapshot taken just before PR #402 (merged Sat 2026-11-14 21:42:28 −05:00) and counting every new folder reproduces 19 / 53 / 17 / 32 exactly (`late_merge_check`) | Two causes, both on screen: PR #402 merged after last week’s count (+1 PR, +2 folders, +1 fellow, +2 logs), and this code skips the undated `tanishaa-r/weekly-hours` folder (−1 folder) |
| 13 | This week 45 of 54 folders have a frictional log (B50) | ✅ | `this_week.frictional_logs` | — |
| 14 | Boopesh’s last two videos: “What Got in the Way” (2:21 + Short 0:49) and “Why Did the AI Say No?” on AI credit explainability (2:27 + Short 0:46), all 4K, delivered for review (B60) | ⚠️ not re-verified locally | Fellow’s own record, supplied in this week’s brief. The build machine was wiped, so those files are not on this machine | No Drive claim is made anywhere |
| 15 | Pull request still pending; the fork attempt failed (B60) | ✅ / ⚠️ | ✅ `fellows/boopesh-m` is not on `origin/main` @ `2a32d04e` and no remote branch contains it (`results.json → boopesh_m_on_main = false`; `git log --all -- fellows/boopesh-m` empty). ⚠️ “fork attempt failed” is the fellow’s report | — |
| 16 | Build machine wiped; toolkit rebuilt from its own setup script before rendering (B60) | ✅ | `./setup` readiness on this machine: audio, Manim, Remotion, slates/compile, fonts ready; Manim equation (LaTeX) beats blocked — none used | Logged in FRICTIONAL.md / BUILD-LOG.md |
| 17 | Narration is an AI voice (B00, outro) | ✅ | Kokoro `am_onyx`, approved by Boopesh on 2026-10-24 and re-approved for this week on 2026-11-23 (relayed by the coordinator) | approval record in `beat_sheet.json → metadata.approvals.voice` |

Merged PRs, Nov 15–21 (from `run.log`): #327 #398 #401 #404 #407 #408 #410 #412 #413 #414
#417 #418 #419 #420 #421 #429 #431 #432 — 18.

## How a piece is matched (case-insensitive file name, anywhere inside the folder)

| Piece | Rule | Note |
|---|---|---|
| README | `README.md` | |
| FACTCHECK | name starts with `factcheck` | |
| FRICTIONAL log | name contains `frictional` | Two `darshil-s` folders carry `FICTIONAL.md` (missing “R”); the strict rule does not count them |
| PROOF | name starts with `proof` | counts `PROOF-REVIEW.md` / `PROOF-REVIEW-RESULTS.md` too |
| SHOTLIST | name contains `shotlist` | |
| PROMPTS | `PROMPTS.md` | `BUILD-PROMPT.md` is a different file and does not count |
| beat sheet | `beat[_-]sheet*.json` | counts `beat_sheet_16x9.json`, `BEATSHEET-16x9.json`, `beat_sheet-short.json` |
| code | a `code/` folder or any `.py .ipynb .js .mjs .ts .tsx .jsx .r .sh .sql` file | Manim `scenes.py` counts as source |
| description | name contains `description` | `description.txt`, `DESCRIPTION.md` |

Sensitivity: counting every new folder (dated or not) gives 55 folders / 19 fellows / 45 logs this
week and 55 / 18 / 34 for the week before (`sensitivity_all_dirs`). Nothing spoken changes.

## Unverified / limits
- Row 14 and the “fork attempt failed” half of row 15 rest on the fellow’s own report.
- A file-name check shows a piece exists, not that it is good or complete.
- Folders that were renamed would count as new; none were removed this week (`removed: 0`).
