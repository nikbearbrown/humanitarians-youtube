# FACTCHECK — One Week of Fellows (Boopesh M., week of 2026-10-25 → 10-31)

Every number is computed by `code/week_stats.py` from the git history of `nikbearbrown/humanitarians-youtube`
and saved in `code/results.json` (run log: `code/run.log`). Checked 2026-11-01.

- **Window:** 2026-10-25 00:00 → 2026-10-31 23:59:59 US Eastern (EDT, UTC−4; DST ends Nov 1).
- **Range:** `c9fca929` (main as it stood when the week began: last first-parent commit before Oct 25,
  "Merge pull request #294", Oct 24 15:01 EDT) `..` `bc722c05` (FETCH_HEAD = current main, Oct 31 22:12 EDT).
  Every first-parent commit in the range falls inside the window (asserted in the script).

| Beat | Claim | Evidence | Status |
|---|---|---|---|
| B00/B20 | 30 pull requests merged in 7 days | 29 first-parent "Merge pull request #N" commits + 1 squash merge (`00dadbe6`, "…(#312)", committer GitHub) — `merged_prs` | ✅ |
| B20 | Per day (EDT): Sun 4, Mon 4, Tue 1, Wed 5, Thu 12, Fri 4, Sat 0 | `merged_prs.per_day`; Oct 25 2026 is a Sunday | ✅ |
| B20 | Busiest day Thursday Oct 29, 12 merges | `merged_prs.busiest_day`; merges `2dc775a8` … `a79f41a3` | ✅ |
| B20 | 35 more commits went straight to main without a pull request | first-parent non-merge commits without "(#N)": `direct_commits_to_main` | ✅ |
| B30 | 37 distinct author names | over all 132 commits that landed (`base..head`, incl. commits authored earlier inside PRs) | ✅ |
| B30 | 27 people after obvious dedupe | linked only by same commit email, same GitHub noreply account, author name = that handle, or same letters; 10 links listed in `contributors.dedupe_links` | ✅ (method stated) |
| B30 | 23 wrote the work; the rest only merged | 23 deduped people authored ≥1 non-merge commit; 4 appear only on merge commits (incl. the repo owner and the PM) | ✅ |
| B30 | Two more pairs look alike, left separate | `possible_same_person_not_merged` (two spellings of one first name; a laptop-name author on a fellow's branch). If merged: 25 people, still 23 authors | ✅ |
| B10/B40 | 84 new work folders from 22 fellows | 93 new `fellows/<fellow>/<folder>` paths minus 9 that are renames of existing work (mohammed-s folders given dated names; files R100 + a new FRICTIONAL.md) | ✅ |
| B40 | 42 STEM explainer, 30 progress, 7 renewal requests, 3 hours logs, 2 written/code | rule on folder name + first 80 words of README (`classification_note`). **Heuristic** — said as "my rough sort" | ✅ (approximate by design) |
| B40 | 27 dated this week, 33 older work filed this week | folder-name date prefix inside/outside Oct 25–31; the other 24 are undated (12 physics-engine weeks + 2 more from one fellow, 7 renewal, 3 hours) | ✅ |
| B50 | Titles: What Is RLHF?, Encrypted Twice, Right Answer, Wrong Chain, Ads in the Picture (+ two on screen) | README first heading, or beat-sheet title when no README — `representative_titles` | ✅ |
| B50 | Most common topic word "physics" (12), from one fellow's 12-week physics-engine series; then agent(s), memory | `topic_words_top`: physics 12, engine 12, agent 5, memory 5 (+ "agents" 2) — all 12 physics folders are `jash-s/physics-engine-week-NN` | ✅ |
| B60 | Boopesh: Brutalist, Shared 2:13 + Short; Deep Hedging 2:33 + Short; all 4K | ffprobe of the delivered files: 3840×2160 133.5 s / 2160×3840 39.9 s; 3840×2160 153.2 s / 2160×3840 51.3 s (`boopesh.last_week_deliveries`) | ✅ |
| B60 | Submitted to Drive; GitHub PR pending; fork attempt failed; asking maintainer for access | `fellows/boopesh-m` absent from `bc722c05` (`boopesh.folder_on_main = false`); Drive upload and the failed fork are Boopesh's own report (not checkable from git) | ✅ git part / ⚠️ Drive + fork from Boopesh |
| B70 | 72 frictional logs landed this week | files matching `friction*.md` added in `base..head` (`frictional_logs_added`), in 17 fellow folders | ✅ |

Coordinator cross-check: a plain `--since 2026-10-24 --until 2026-10-31` count gives 31 "Merge pull request" commits
and 37 names (it includes Oct 24, two merges). The film uses the exact Oct 25–31 window: 29 merge commits + 1 squash.

Privacy: on screen and in `results.json` people appear only as fellow folder names (e.g. `jash-s`) or "First L.";
no surnames or emails. No fellow is named in the narration.
