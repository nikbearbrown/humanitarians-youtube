# FRICTIONAL — What a Finished Folder Looks Like

## 2026-11-23 — building the week of Nov 15–21

**Tried / expected.** Count the week’s merged PRs and new work folders, then check each new
folder for the nine pieces of fellows’ paperwork, and make a 16:9 film and a native 9:16 Short
with the Brutalist toolkit (pinned at `a99b5323`). Expected the same pipeline as earlier weeks.

**Where it resisted, and what was done next.**
- *The build machine was wiped.* None of my earlier reels (10 videos over 5 weeks) were on
  disk, so there were no local reference scenes to start from. The toolkit was rebuilt from its
  own `./setup`; readiness: audio, Manim, Remotion, compile and fonts ready, Manim LaTeX
  equation beats blocked (none used). Scenes were rewritten from the toolkit’s own gates and
  the house rules.
- *“Recount with the same code” did not match last week’s published numbers* (19 PRs, 53
  folders, 17 fellows, 32 logs vs a recount of 20 / 54 / 18 / 34). Rather than guess, the
  script re-ran last week with the snapshot taken just before the last PR of that week
  (#402, merged Sat Nov 14 at 9:42 pm New York time): that reproduces 19 / 53 / 17 / 32 exactly.
  The second, smaller cause is a definition choice made this week: undated folders (an hours
  folder last week, a renewal-requests folder this week) are not counted as work. Both causes
  are written on screen in B50.
- *File names are messy.* Two folders log friction in `FICTIONAL.md`; proof reviews appear as
  `PROOF-REVIEW.md`; beat sheets as `BEATSHEET-16x9 (1).json`. The matching rules are written
  down in FACTCHECK.md; the strict frictional rule does not count the misspelled file.
- *Text boxes lied to the layout audit.* Manim `Text(..., color=...)` and 4×-scaled long lines
  reported bounding boxes 2–3× taller than the drawn glyphs (Pango wrapped lines it never drew
  that way), which tripped GATE B’s text-on-text and safe-area checks on the outro. Fixed by
  setting colour after construction and building landscape text at 2×, not 4×.
- *Edge bleed you cannot see.* In the Short a PANEL-coloured card 0.08 units outside the 5 %
  title-safe band failed the frame check even though it reads as background; moved inside.
- Another build ran on the same 4 CPUs, so renders were run one at a time and the two
  `art final` exports were run one after the other.

**What Claude contributed, and what was accepted, changed or rejected.** Claude Code wrote
`week_stats.py`, `make_sheet.py`, both `scenes.py` files and this paperwork, and ran every
gate. Accepted: the first-parent PR definition and the snapshot-diff folder definition.
Changed: the first exploratory count took every new folder as work; the script counts dated folders only (the fellows README rule), with the all-folders count kept as a sensitivity check.
Rejected: blaming the whole recount gap on the late merge, because the evidence showed a
second cause.

**Understood / still open.** A file-name check proves a piece exists, not that it is good.
My own pull request is still pending (the fork attempt failed; `fellows/boopesh-m` is not on
main as of Nov 22).

---

## 2026-11-23 — Week of Nov 15–21: "What a Finished Folder Looks Like" (progress update)

**Record provenance:** Drafted on 2026-11-24 by Claude (Claude Code) from the build session's record, at
Boopesh's request, one day after the work. The build notes above were written during the build
(2026-11-23). Boopesh to review and add his own notes below; nothing here is his first-person reflection
unless he adds it.

- **What was being worked on:** this week's progress video, built from the fellows repository's git history
  for Nov 15–21. Code: [`code/week_stats.py`](code/week_stats.py) → [`code/results.json`](code/results.json).
- **What was tried, and what was expected:** count how many of the week's new work folders carry each of
  nine paperwork pieces. The expectation was that README and FRICTIONAL would be near-universal.
- **Where it resisted, and what was done next:**
  - The build machine had been wiped; the toolkit was reinstalled before rendering.
  - Last week's published counts did not match a recount (19 → 20 PRs) because PR #402 merged late on
    Sat Nov 14. The video shows both numbers and the reason on screen.
  - The strict layout audit failed on Manim text sizing; fixed by setting colour after creation and
    building long lines at 2×.
  - Boopesh's own pull request was still blocked this week (the fork attempt failed). GitHub push access
    arrived on 2026-11-24, so this folder is being submitted now, after the week it describes.
- **What Claude contributed, and what was accepted, changed or rejected:** Claude wrote the analysis
  script, scenes, script and paperwork, and rendered both films. Boopesh asked for this week's videos and
  approved the narrator voice. *Boopesh: add what you checked, changed or rejected.*
- **What is understood now, and what is still open:**
  - Understood: almost every new folder had a beat sheet (51 of 54); only 4 had a PROOF.md; none had all nine.
  - Open: the narration has not been listened to by a person; the Drive links are not yet in the README.
