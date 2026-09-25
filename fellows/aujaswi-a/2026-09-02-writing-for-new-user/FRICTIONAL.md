# Frictional Log — Writing for a User Who Doesn't Know Your Product Yet

**Entry date:** 2026-09-24

**What I was working on:** Produced as part of the ten-topic automated batch, covering the discipline of writing product content as a first-time user rather than an informed insider.

**What I tried, and what I expected:** Standard pipeline run; expected a clean pass consistent with the rest of the batch.

**Where it resisted, and what I did next:** One naming issue outside the render pipeline itself: the auto-generated filename for this topic's working folder included an apostrophe (from "Doesn't"), which is unsafe in a Windows path context long-term. Manually renamed to strip the apostrophe before finalizing paths. No render or GATE V defect.

**What Claude contributed, what I accepted/changed/rejected:** Claude flagged the apostrophe-in-filename risk and renamed it directly; I accepted the rename as-is.

**What I understand now, and what I still don't:** Filename-safety issues from narration-derived slugs are easy to miss since they don't fail any render or QC gate — they only show up as friction later, e.g. during this reorganization pass. Worth checking the other 11 slugs for the same class of issue before final commit (checked as part of this reorg; none of the other 11 had it).
