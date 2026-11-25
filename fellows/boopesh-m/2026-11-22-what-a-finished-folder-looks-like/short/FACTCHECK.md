# FACTCHECK — Short: What a Finished Folder Looks Like (9:16, 2160×3840)

Same data as the landscape film: every number comes from `../code/results.json`
(`../code/week_stats.py`, run twice, identical output). Full claim table, matching rules and
limits: [`../FACTCHECK.md`](../FACTCHECK.md).

| Claim (beat) | Verdict | Source |
|---|---|---|
| 54 new work folders this past week (Nov 15–21, America/New_York) (B10) | ✅ | `this_week.new_work_folders` |
| Checked for nine pieces of paperwork, by file name (B10) | ✅ | `pieces` (9) and the matching rules in ../FACTCHECK.md |
| Beat sheet in 51; proof self-review in just 4; full sorted list on screen (B10) | ✅ | `summary.piece_counts_sorted` |
| No folder had all nine; 8 had eight (B20) | ✅ | `summary.folders_with_all_pieces = 0`, `folders_at_max_count = 8` |
| `rohan-v/2026-11-20-how-auto-tune-works` has README, fact-check, frictional log, shot list, prompts, beat sheet, code and description; its one gap, like the other seven, is PROOF (B20) | ✅ | `top_folder_pieces`, `missing_from_every_top_folder = ["PROOF"]` |
| The two most often missing are the proof and the description (B30) | ✅ | the two lowest counts: description 12, PROOF 4 |
| B00 composer output lines (most/least common) | ✅ | same fields |
| Narration is an AI voice (B00) | ✅ | Kokoro `am_onyx`, approved by Boopesh on 2026-10-24 |

No fellow is named in the narration; the example folder appears only by its folder name.
