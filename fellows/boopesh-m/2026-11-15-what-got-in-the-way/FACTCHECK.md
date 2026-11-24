# FACTCHECK — What Got in the Way (Boopesh M., week of 2026-11-08 → 11-14)

Every number is computed by `code/week_stats.py` from the git history of `nikbearbrown/humanitarians-youtube`
(`origin/main` = `dc2963ec`) and saved in `code/results.json` (run log: `code/run.log`). Checked 2026-11-15.

- **Window:** 2026-11-08 00:00 → 2026-11-14 23:59:59 America/New_York (EST, UTC−5 all week; `zoneinfo`).
  Last week (Nov 1–7) starts at EDT, UTC−4, because DST ended Nov 1 at 02:00 — same DST-aware function.
- **Range:** `215e6a5f` (last first-parent commit before Nov 8 = "Merge pull request #375", Sat Nov 7 21:07 EST)
  `..` `dc2963ec` (last first-parent commit before Nov 15 = "Merge pull request #400", Sat Nov 14 15:14 EST).
  Every first-parent commit in the range falls inside the window (asserted in the script).
- **Frictional logs:** files matching `friction*.md` *added* in that range under `fellows/` (last week's rule,
  unchanged). No existing frictional log was modified in the range (checked: no `M` entries match).

| Beat | Claim | Evidence | Status |
|---|---|---|---|
| B00/B20 | 32 frictional logs added, by 13 fellows | `friction.logs_added`, `friction.fellows` (= `this_week.folders.frictional_logs_fellows`) | ✅ |
| B00/B20 | 31 describe obstacles | the 32nd, `hrishikesh-p/2026-11-13 - RamanEffect/FRICTIONAL.md`, holds a JEPA video description (no tried/resisted/fixed text); the `OBSTACLE` keyword rule finds nothing in it (`friction.logs_without_obstacles`) | ✅ |
| B20 | Six themes, logs per theme (out of 31): layout & picture checks 19, facts & data 11, length & time 10, tools & setup 10, timing & pacing 8, voice & pronunciation 5 | `friction.theme_logs`: one log counts once per theme when any keyword rule in `THEMES` matches the log's obstacle text (the log minus contribution / understood-now / expected / link sections). **Heuristic**, said as "my rough sort"; one log can land in several themes; 2 logs (both `heet-k`, about planning and holding work) fit none. Matched keywords per log are printed in `run.log` | ✅ (approximate by design) |
| B20 | Layout & picture checks: 19 logs from 8 fellows; "things running off the edge, overlapping, or too small to read" | `friction.theme_fellows`; the matched keywords in `run.log` (safe area/edge, overlap, edge-bleed, size floor, text-size, underfill, below 4K) | ✅ |
| B10 | "the most common obstacle was checking the result" (not installing the tools) | layout & picture checks 19 logs vs tools & setup 10 (rough sort). The wording echoes one log (`tanishaa-r/2026-10-30-learning-brutalist`: "the hard part … isn't installing the tools, it's checking the result") | ✅ (rough sort) |
| B30 | A chart passed the frame checks, but showed the opposite of the narration (layout & picture checks) | `jainil-s/2026-11-06-ai-significant-on-tuesday/FRICTIONAL.md`: "passed GATE V and GATE T, and asserted the opposite of the narration"; "found by looking at frames"; "Fixed by tinting the two outer regions instead" | ✅ paraphrase |
| B30 | A working title didn't survive the data, so the title changed (facts & data) | `gomathy-s/2026-11-10-most-insider-trades-arent-buys/FRICTIONAL.md`: "The title didn't survive the data … The title became 'Most Insider Trades Aren't Buys'" | ✅ paraphrase |
| B30 | A script ran 4:22 (262 s) for a 4:00 slot; trimmed five times without cutting a number (length & time) | `agrima-p/2026-11-11-foundation-search-research/FRICTIONAL.md`: "the first narration pass measured 262 s. It took five rounds of trimming … (no figure, source, hedge or label removed) to reach 239.9 s" | ✅ paraphrase |
| B30 | A checking script took over 40 minutes; now it streams frames, 87 s (tools & setup) | `tanmay-k/2026-11-08-where-the-eighty-lives-stem-video/FRICTIONAL.md`: "ran for over 40 minutes"; "the check now streams frames and runs in 87 seconds" | ✅ paraphrase |
| B30 | Words on screen appeared late, until each reveal was timed to the voice (timing & pacing) | `tanishaa-r/2026-10-30-what-is-rag/FRICTIONAL.md`: "items appeared late"; "word times were measured from Bella's audio … reveals now start 0.2 s before each word" | ✅ paraphrase |
| B30 | (all five) | each example's key phrases are asserted against the log text by the script (`EXAMPLES[].must`), and each example's theme is asserted to be one the rough sort gave that log; five different fellows; shown by folder name only, never named aloud | ✅ |
| B40 | In 17 of the 31 logs a problem was found by watching the cut, viewing the frames, or re-reading the words | `friction.found_by_looking_logs` = 17 (from 7 fellows): keyword rule `LOOKED` (e.g. "after watching", "previews showed", "snapshot review", "sampling frames", "looking at frames", "re-read the"), matches printed per log in `run.log`. **Heuristic count**; it does not say who looked (some logs were drafted by Claude in the first person) | ✅ (approximate by design) |
| B40 | "A passing check tells you the frame fits. Only looking tells you it's right." | a takeaway, paraphrasing `jainil-s`: "a clean GATE V means the frame is correctly sized, not that it is readable" | ✅ (opinion, sourced) |
| B50 | Merged pull requests 27 → 19 | this week: 19 first-parent "Merge pull request #N" commits + 0 squash merges (`merged_prs`) | ✅ |
| B50 | New work folders 75 → 53; fellows with new folders 19 → 17; frictional logs 95 → 32 | `comparison` (same `week()` function, same definitions) | ✅ |
| B50 | "recounted today": last week's video said 26 / 74 / 18 | the same function on main as it was then (`a953b021`) still gives 26 / 74 / 18 / 95 (asserted). Today it gives 27 / 75 / 19 / 95 because PR #375 (`215e6a5f`, Sat Nov 7 21:07 EST, inside last week's window) merged after that count; it added one work folder (`akshay-c/2026-11-04_how_circuit_breakers_prevent_cascading_failures`) from a fellow with no other new folder that week (`last_week_published_vs_recounted`). Shown on screen | ✅ |
| B60 | Last week Boopesh made "What the Fellows Taught" 2:15 + Short 0:50 and "The Backtest Mirage" (AI in finance) 2:24 + Short 0:45, all 4K | ffprobe of the delivered files in `weekly-submission/` (video 135.42 s / 49.79 s, 144.25 s / 45.29 s; 3840×2160 and 2160×3840) — `boopesh.last_week_deliveries` | ✅ |
| B60 | "delivered for review" | the four files exist in `weekly-submission/landscape|vertical`. **Not claimed:** any Drive submission | ✅ (wording limited on purpose) |
| B60 | His obstacle is access: fork attempt failed; PR pending; folder not on main / not in these counts | `fellows/boopesh-m` absent from `dc2963ec` (`boopesh.folder_on_main = false`); the failed fork is Boopesh's own report | ✅ git part / ⚠️ fork from Boopesh |

**Coordinator cross-check:** a plain `--since 2026-11-08 --until 2026-11-14` count gives **91 commits and 23
two-parent merges** (matches the brief's "about 91 commits and 23 merge commits"). The film counts **19 merged pull
requests**: of the 23 merges, 20 are "Merge pull request" commits, but one of them (#389, `863e9ccb`, "from
nikbearbrown/main") merged main *into a fellow's branch* and is not on main's first-parent line; the other 3 are
direct merges, not pull requests (`e1f6bc90` "ameya-p/Adding docs for week 8", `52aa0a09`, `0162f031` video-upload
merges). There were no squash-merged PRs this week. 20 − 1 + 0 = 19. Counting everything that landed on main
(`215e6a5f..dc2963ec`, including commits authored before Nov 8 inside PRs) gives 93 commits; 14 commits went
directly to main. Friday Nov 13 was the busiest merge day (7) — context only.

Context, not spoken: 6 of the 32 logs are from one fellow (`tanishaa-r`), 4 each from `agrima-p` and `rohan-v`, so
theme counts lean on a few prolific writers; the "from N fellows" column shows that (timing & pacing: 8 logs, 3
fellows). Several logs are dated for older work but were added this week (e.g. `heet-k/2026-10-29-…`).

Privacy: on screen and in `results.json` people appear only as fellow folder names (e.g. `rohan-v`); no surnames or
emails. No fellow is named in the narration. Examples are short paraphrases, not long quotes.
