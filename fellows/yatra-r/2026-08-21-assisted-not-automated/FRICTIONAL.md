# FRICTIONAL — Assisted, Not Automated.

> Written 2026-11-03 from this folder's build records (README.md, BUILD-LOG.md,
> CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md, SHOTLIST.md, beat_sheet.json,
> beat_sheet.short.json), not kept week by week during the build.

## 2026-08-21

**Tried / expected.** A 5–10 minute `deep-explainer` on AI in SEO and content — whether it
is replacement or reorganisation — built around seven figures Yatra supplied as verified,
with sources (Fractl, Typeface, Ahrefs via Stacc, Backlinko/QuickSEO). Instruction: cite
them as shown, alter none, add no other numbers. 16:9 master plus a full-length 9:16 for
TikTok. Built with Claude Code on the brutalist.art toolkit. The beat sheets' build stamps
are 2026-08-28 (master) and 2026-08-29 (short).

**Where it resisted, and what was done next.**
- *Two of three lanes blocked.* `deep-explainer` requires 20–25% VOX stills and 25–40%
  Manim. VOX was blocked: `smithsonian_index.py` and the local still library are not
  shipped, the `--s3` flag the fetch script recommends does not exist, and no `SI_API_KEY`
  was set. Manim was blocked: `manimpango` needs cairo via Homebrew, which needs a password
  the agent would not enter. Yatra was shown this before authoring and chose to build
  Remotion-only over a previz-plus-shopping-list build or getting a free Smithsonian key.
  The result is logged as the ai-explainer chassis at deep-explainer length, not a
  compliant deep-explainer, with the steps that would unblock each lane.
- *Shared compositions, one duration.* Several beats share a composition with a single
  `durationInFrames`. It was set to the shortest beat each backs, because longer frame
  counts get trimmed at compile and the citations land at 80–90% of each span.
- *Platform cap.* The 9:16 runs past the 3:00 Shorts/Reels cap by choice, so `shorts.py`
  was given an explicit empty drop plan to stop it auto-cutting beats.
- *Carried-over toolkit gaps.* No GATE T script, the Gate V review-cut false positive
  (verified against the clean master instead), missing skill reference files, no mascot.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat
sheet, narration and prompts, built stat scenes whose `source` field is required so no
figure can render without its citation, and wrote the fact-check and gate records. At QC,
22 of 24 beats were Gate V clean with zero edge-bleed; `underfill` on the B21 verdict
(0.50) and B23 outro (0.06) was accepted as in earlier reels. The fact-check records that
the seven figures were not independently re-verified — they are Yatra's, passed on with
their citations.

**Now understood / still open.**
- Open: the figures themselves were not checked against the primary sources in this build.
- Open: the episode is not a compliant `deep-explainer` until VOX and Manim are unblocked
  and the body is re-planned to the quota.
- The 9:16 beat sheet carries two SKIN LINT warnings (portrait cold open and outro
  components); the records do not say whether these were reviewed.
- The `@Yatra` / `claude-yatra` channel has no row in the skill's channels table.
