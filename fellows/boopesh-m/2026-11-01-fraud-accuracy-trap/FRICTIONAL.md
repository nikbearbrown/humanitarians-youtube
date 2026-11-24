# FRICTIONAL — The 99.9% Accuracy Trap

_Drafted by Claude (Claude Code) from the build session; Boopesh to read, correct and add his own entries._

## 2026-11-01
- **Tried:** download the real Kaggle / ULB credit-card dataset. **Found:** Kaggle, OpenML and Zenodo are blocked
  from the build container. **Did:** generated a seed-locked synthetic dataset with exactly the real dataset's size
  and fraud rate (284,807 rows, 492 frauds) and said "synthetic" on screen and in the narration every time a model
  number appears.
- **Tried:** verify the dataset facts. **Found:** kaggle.com unreachable. **Did:** read the dataset description
  verbatim from a public GitHub copy; the paper's title, authors and venue from the IEEE Xplore search result.
  The Kaggle→paper citation link is flagged ⚠️ in FACTCHECK.md.
- **Resisted (honesty about tuning):** the first synthetic run (`class_sep = 1.0`) was so hard that every model was
  weak (boosted model caught 54 of 148). I raised `class_sep` to 2.0 so the demo shows a model that clearly works.
  That is a design choice, not a finding; both runs are kept in `code/` and the parameter is in FACTCHECK.md.
- **Resisted:** "1 in 600" from the brief → the real ratio is 1 in 579, so the film says "about 1 in 580".
- **Resisted:** the lazy model's precision is 0/0. sklearn reports 0; the film shows "n/a".
- **Resisted:** the cost rule (a miss costs 50× a false alarm) is invented for illustration. The film labels it
  "(assumption)" and the narration says "Say a miss costs…".
- **Resisted:** first cut ran 2:40, at the length limit. Trimmed B20, B30, B50 and B60 narration to 2:22.
- **Resisted:** first layouts had a label running past the safe area (B30 verdict, B50 right column), overlapping
  the "1.9×" callout and a crowded threshold dial; fixed by looking at preview frames.
- **Resisted:** the hesitant writer first never made its correction (the trigger included the full stop);
  caught by looking at the last frame, fixed and re-rendered.
- **Resisted:** toolkit gates caught a label touching the red ring (GATE B), rotated row labels and short card
  titles below the minimum type size (GATE T). Removed or enlarged; see BUILD-LOG.md.
- **AI contribution:** Claude wrote the experiment, script, sheets and scenes. Kokoro `am_onyx` speaks the narration.
- **Still open:** try the real dataset when Kaggle is reachable; pronunciation needs a human listen.

---

## 2026-11-24 — Submission note for the week of Oct 25–31 (written later than the week it describes)

**Record provenance:** added on 2026-11-24 by Claude (Claude Code) at Boopesh's request, when this folder was
first committed. The entries above were drafted during the build, in the week of the work.

- **Why this commit is late:** the films and this source were delivered in the week of Oct 25–31. They could not
  be committed then: Boopesh's fork of the repository failed, and push access only arrived on 2026-11-24.
  This folder is restored unchanged from the source archive delivered that week.
- **Who did what:** Boopesh gave the prompts and instructions for the week (the topic direction, and
  the voice approval on 2026-10-24) and reviewed the delivered videos and code. Claude did the research,
  code, scenes, narration script and rendering.
- **Still open:** the Drive link for each film goes in this folder's README; Boopesh to add any notes of
  his own on what he checked, changed or rejected.
