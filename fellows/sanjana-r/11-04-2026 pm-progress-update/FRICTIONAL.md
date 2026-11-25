# FRICTIONAL.md — running diary (what I did, and what didn't work)

*Not graded. Required weekly. Keep the friction in.*

---

## 2026-11-13 — Week of Nov 4 progress reel

**What I did**
- Produced the weekly-progress ai-explainer ("Week of Nov 4") in 16:9 and 9:16 4K, stats only,
  no names. Reused the `WeekBoard` component from last week (tiles / bars / flags) — no new
  component needed, so this build was fast.
- Headlined the real win: the **4K auto-check (AppScript) is live** — built and tested with the
  dev team. That closes the exact gap the Oct-25 report flagged ("push 4K checks upstream").
- Logged the week: 28 videos reviewed, 24 cleared, 4 sent back (not 4K), ~9 creators, 2 new
  reviewers onboarded and trained.

**The week's actual friction (the org work)**
- Four videos still shipped **not in 4K** this week — caught at review, then chased by mail,
  and the fix didn't land until 11/11 (several days of back-and-forth). The new auto-check
  should prevent this class going forward, but it wasn't live early enough to catch these.
- The **watermark check is still manual** — only the 4K gate is automated so far. One video
  also had a **non-standard project name** on screen; judged low-risk and cleared for upload,
  but it's another thing a human had to eyeball.
- **Onboarding is unmeasured** — two reviewers were trained, but there's no rubric yet for when
  a new reviewer is "calibrated" enough to clear videos solo.

**What didn't work / next week**
- Automating one gate (4K) made the week lighter; the watermark gate is the obvious next
  target. Next week: extend the auto-check to the watermark and ramp the two new reviewers onto
  live videos with a light calibration check.

**On producing this report**
- Reused WeekBoard; pre-flagged the stat/flag beats `sparse_by_design` up front (learned from
  last week's GATE V underfill on data displays).
- The AppScript screenshots (code editor + log sheet) arrived mid-build, and the ask became
  "put the images on screen." Two frictions there: (1) I can't use the raw files — the inline
  paste isn't on disk and the Apps Script URL is login-gated — and the log sheet is full of
  fellow names, which violates the no-names rule; so I **rebuilt** both as native beats (B02B
  code, B02C log), faithful but name-free. (2) First tried the log as a `ClaudeCodeBeat`, but
  GATE §8.12 rejected it ("prose-in-code-card — not real code") and the min-size filter
  discarded the short log tokens; switched the log to a `WeekBoard` flags list, which reads as a
  results log and passes. Also missed one `sparse_by_design` flag (B02 two-callout beat) on the
  first final — GATE V caught it, added it, re-cut.
