# FACTCHECK — What the Fellows Taught (Boopesh M., week of 2026-11-01 → 11-07)

Every number is computed by `code/week_stats.py` from the git history of `nikbearbrown/humanitarians-youtube`
(`origin/main` = `a953b021`) and saved in `code/results.json` (run log: `code/run.log`). Checked 2026-11-08.

- **Window:** 2026-11-01 00:00 → 2026-11-07 23:59:59 America/New_York (DST ended Nov 1 at 02:00, so the
  window starts at UTC−4 and ends at UTC−5; handled with `zoneinfo`).
- **Range:** `bc722c05` (main as it stood when the week began: last first-parent commit before Nov 1, Oct 31
  22:12 EDT) `..` `a953b021` (last first-parent commit before Nov 8 = "Merge pull request #373", Nov 6 22:18 EST).
  Every first-parent commit in the range falls inside the window (asserted in the script).
- **Last week** (Oct 25–31, `c9fca929..bc722c05`) is recomputed by the **same function**; the script asserts it
  still reproduces last week's published 30 PRs / 84 folders / 22 fellows / 72 frictional logs.

| Beat | Claim | Evidence | Status |
|---|---|---|---|
| B00/B10/B20 | 74 new work folders from 18 fellows | 74 new `fellows/<fellow>/<folder>` paths between `bc722c05` and `a953b021`, 0 pure renames (`this_week.folders`) | ✅ |
| B10/B20/B70 | 50 of 74 teach a topic (STEM / explainer videos) | `folders.kinds` — last week's rule on folder name + first 80 words of README (beat-sheet title when there is no README). **Heuristic**, said as "my rough sort" | ✅ (approximate by design) |
| B20 | 23 progress videos, 1 hours log | `folders.kinds` | ✅ (heuristic) |
| B20 | 28 dated this week, 45 older work filed this week | folder-name date prefix inside/outside Nov 1–7; 1 more is undated (`rithwik-b/weekly-hours`) | ✅ |
| B30 | Subjects of the 50: AI for product managers 12, testing & metrics 10, how AI models work 9, making videos with AI 8, software & data tools 5, other topics 4, AI in marketing & business 2 | `folders.stem_subjects`; first-match keyword rules (`SUBJECTS` in the script) on folder name + title + the README's one-line description. **Heuristic**, said as "I sorted" / "rough sort" on screen | ✅ (approximate by design) |
| B30 | The 12 PM videos are one fellow's series; testing & metrics comes from 6 fellows | `folders.stem_subject_fellows` (AI for product managers: 1 = `vineet-s`; testing & metrics: 6) | ✅ |
| B40 | Titles: Mixture of Experts; Goodhart's Law — When the Proxy Stops Being the Target; Integration Hell; Likely False, Likely True; RAG Explained for Product Managers; Be the Sentence | README first heading, or beat-sheet title when no README (`examples`); all six are dated Nov 1–7 and sorted as STEM (asserted). Cards show the part before " — " | ✅ |
| B40 | "Be the Sentence" is about getting quoted by AI search | its README: "AI-Cited Authority: how SEO is turning into 'Search Everywhere Optimization' for ChatGPT, Claude and Google AI Overviews" | ✅ (paraphrase) |
| B00/B50 | Merged pull requests 30 → 26 | this week: 25 first-parent "Merge pull request #N" commits + 1 squash merge (`4fd35eb5`, "…(#366)") — `merged_prs`; last week 29 + 1 | ✅ |
| B50 | New work folders 84 → 74; fellows with new folders 22 → 18 | `comparison` (same function, same definitions) | ✅ |
| B00/B50 | Frictional logs 72 → 95 | files matching `friction*.md` added in the range (`frictional_logs_added`); this week in 16 fellow folders | ✅ |
| B60 | Last week Boopesh made "One Week of Fellows" 2:24 + Short 0:47 and "The 99.9% Accuracy Trap" (AI fraud detection) 2:23 + Short 0:53, all 4K | ffprobe of the delivered files in `weekly-submission/` (video stream 144.42 s / 47.42 s, 142.62 s / 52.67 s; 3840×2160 and 2160×3840) — `boopesh.last_week_deliveries` | ✅ |
| B60 | "delivered for review" | the four files exist in `weekly-submission/landscape|vertical`. **Not claimed:** Drive submission (unconfirmed) | ✅ (wording limited on purpose) |
| B60 | GitHub PR pending; fork attempt failed; folder not on main / not in these counts | `fellows/boopesh-m` absent from `a953b021` (`boopesh.folder_on_main = false`); the failed fork is Boopesh's own report | ✅ git part / ⚠️ fork from Boopesh |

Coordinator cross-check: a plain `--since 2026-11-01 --until 2026-11-07` count gives **80 commits and 28 two-parent
merges** (matches the brief's "about 80 commits and 28 merges"). The film counts **26 merged pull requests**: of
those 28 merges, 25 are "Merge pull request" commits on main; the other 3 are not pull requests (`db32596e`
"ameya-p/Adding docs for week 7", and two "merge main into my branch" commits inside PR branches, `37147d0c`,
`48af1fa1`); plus 1 squash-merged PR (#366) that has only one parent → 25 + 1 = 26. Counting everything that
landed on main (`bc722c05..a953b021`, including commits authored before Nov 1 inside PRs) gives 86 commits.

Monday Nov 2 was the busiest merge day (12, incl. four older PRs #320, #334, #335, #356 merged within a minute);
Wednesday Nov 4 and Saturday Nov 7 had none (`merged_prs.per_day`) — context only; not shown or spoken.

Privacy: on screen and in `results.json` people appear only as fellow folder names (e.g. `vineet-s`) or "First L.";
no surnames or emails. No fellow is named in the narration.
