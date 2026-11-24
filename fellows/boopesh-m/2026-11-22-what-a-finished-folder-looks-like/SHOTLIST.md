# SHOTLIST — What a Finished Folder Looks Like (16:9, 3840×2160)

Audio-first: beat length = measured Kokoro `am_onyx` narration (speed 0.94). Total 140.0 s (2:20.0).
All Manim beats: cream ground `#FAF9F5`, mono kicker over an EB Garamond headline at top-left,
PANEL `#EEEADF` cards, teal `#1F4E5F` data, ACCENT `#A64B2A` only for the number that matters.
Structure appears first as dim ghost outlines and lights up on its narration cue.

| Beat | Len (s) | Renderer | What is on screen | Data |
|---|---|---|---|---|
| B00 INTRO | 14.06 | Remotion `ClaudeComposerAsk`, greeting “Hi, Boopesh”, folder chip @HumanitariansAI, model chip Claude | The ask typed into the composer, answered: 18 merged PRs · 54 folders · 19 fellows; most common beat_sheet.json 51/54; least common PROOF.md 4/54 | results.json |
| B10 THE WEEK | 14.64 | Manim `B10_TheWeek` | Kicker “GIT LOG · NOV 15–21 · MAIN”, headline “One week on main”; three stat cards 18 / **54** / 19 (54 in accent); two method lines (window, PR definition) | this_week |
| B20 NINE PIECES | 14.30 | Manim `B20_NinePieces` | 3×3 grid of the nine file names with a short plain caption each, lit one by one as narrated | — |
| B30 THE COUNT | 13.20 | Manim `B30_TheCount` | Horizontal bars, 9 rows sorted 51 → 4 on a 54-wide track; PROOF.md bar and “4” in accent | summary.piece_counts_sorted |
| B40 WHAT COMPLETE LOOKS LIKE | 14.76 | Manim `B40_EightOfNine` | Two folder cards by folder name (rohan-v/2026-11-20-how-auto-tune-works, likhith-r/2026-11-14-word2vec-king-man-woman-queen) with 8 ticks each; PROOF appears last as the empty accent box; footer “No folder had all 9 · 8 folders had 8 · all 8 lack only PROOF.md” | top_folder_pieces |
| B50 LAST WEEK, RECOUNTED | 16.20 | Manim `B50_LastWeek` | Table Nov 8–14 (recount) → Nov 15–21: PRs 20 → 18, folders 54 → 54, with a frictional log 34 → **45**; on-screen footnote: published 19 · 53 · 32, PR #402 merged Sat 9:42 pm after that count, undated folders skipped | last_week_recount, late_merge_check |
| B60 MY WEEK | 17.88 | Manim `B60_MyWeek` | Two video cards (titles, durations, “delivered for review” chip); GitHub logo + “Pull request: pending” (fork failed; not on main as of Nov 22); “Friction this week” (machine wiped, toolkit rebuilt from ./setup) | brief + boopesh_m_on_main |
| B70 TAKEAWAY | 14.38 | Manim `B70_Takeaway` — the one dark beat (#2B2A26) | “Before you open a pull request”: nine checkboxes tick; PROOF.md and description.txt flip to light chips (most often missing); closing line | — |
| B80 YOUR TURN | 13.18 | Remotion `ClaudeComposerAsk`, greeting “Your turn.” | The prompt to paste into Claude, read aloud in the narration | — |
| B90 OUTRO | 7.13 | Manim `B90_Outro` | Film title, SUBSCRIBE pill, HAI logo + @HumanitariansAI, credit “Boopesh M. · Humanitarians AI Fellow · Brutalist team”, “Narration: AI voice (Kokoro am_onyx)”, data source line | ref |

No footer text, no channel_title overlay (metadata.channel_title is empty). No person icons;
the GitHub mark is the toolkit’s own `icons/logos/github/github-01.png` (LOGO LAW); the HAI
mark is `logos/humanitarians/humanitarians-logo-1.svg`.
