# FACTCHECK: Renumbering a Textbook (report video, week of 09-07-2026)

Format: claim | verdict | source | fix. Written 09-07-2026 after rebuilding the video.
Verdicts: VERIFIED = matches code or output I saw. CONFIRM = comes from my own account; check before relying on it. OVERSTATED = true in spirit, stronger than the evidence.

## Narration

| Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|
| B00, B09 | One script renumbered "every figure in a whole cancer-biology textbook" / "a whole textbook" | OVERSTATED | The script skipped Chapter 25's `11_Summary.mdx` (no numbered frontmatter title); it is a tracked open item | Optional: say "nearly every caption", or name the exception |
| B01 | Labels drifted into styles like 4-4-2b, 5-4-2, 7-7-4-2a | CONFIRM | 4-4-2b, 6-3-3a and 14-2-2 appear in my earlier session. 5-4-2 and 7-7-4-2a appear only in the beat sheet | Check against the dry-run output, or swap in examples I saw directly |
| B01 | References to those figures point at the wrong place | CONFIRM | General statement, not tested | Reword as "can point" if challenged |
| B02 | Walks MDX files in order; reads section from each file's frontmatter title; renumbers Figure, Video and Table captions as chapter.section.index; dry run first; writes only on `apply` | VERIFIED | `renumber_all.py` (`TITLE_RE`, per-type counters, `dry_run` guard) as shown in my earlier session | None |
| B03 | Dry run is the default; files written only when the second argument is `apply` | VERIFIED | `dry_run = (len(sys.argv) <= 2 or sys.argv[2] != "apply")` | None |
| B03 | Each type keeps its own counter | VERIFIED | `counters = {"Figure": 0, "Video": 0, "Table": 0}` | None |
| B03, B04 | Figure 4-4-2b becomes 4.5.1 | CONFIRM | Shown in the on-screen diff; Chapter 4 DNA repair section is 4.5 | Check against the dry-run output |
| B04 | Figure 1.1 in the organelles section becomes 1.2.1 | VERIFIED | Dry run: `2_Cellular_Organelles...mdx: Figure 1.1 -> Figure 1.2.1` | None |
| B05 | Run on a fresh branch, loop over every chapter with `apply`, review as one diff | VERIFIED | Branch `renumber-all`, loop command, pull request into `development` | None |
| B06 | Captions line up into one scheme: chapter, section, index | VERIFIED | Dry-run and diff output | None |
| B07 | Reading the output caught a collision where a Video and a Figure shared one counter | CONFIRM | My own account; my earlier session also shows Figure 1.4.1 and Video 1.4.1 coexisting, which is a separate open question for Evin | Confirm what the collision was before relying on this line |

## On screen

| Beat | Item | Verdict | Fix |
|---|---|---|---|
| B03, B06, B07 | Code shown is an excerpt of `renumber_all.py`, trimmed with `...` | VERIFIED against my earlier session. The original file was not on my machine to re-check | None |
| B00, B02, B05, B08 | Composer shows model label "Fable 5 High" | Dates the video | Leave, or change to "Claude" |
| B00, B02, B05, B08 | Folder chip shows @HumanitariansAI | VERIFIED in frame check | None |

## Not claimed anywhere
No caption counts appear in the narration or on screen. Totals still need to be taken from the merged pull request before they are quoted.
