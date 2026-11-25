# FRICTIONAL — The Judgment Is the Job.

> Written 2026-11-03 from this folder's build records (README.md, BUILD-PROMPT.md,
> CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md, QC-LOG.md, SHOTLIST.md, beat_sheet.json,
> beat_sheet.short.json), not kept week by week during the build.

## 2026-08-21

**Tried / expected.** A 1–3 minute ai-explainer on what AI did to advertising — it took
over the execution of copy and visual concepts, not the judgment — covering four areas
Yatra asked for. Her instruction: no statistics or numbers she couldn't verify; use
rankings or described comparisons unless she supplied a source. None was supplied, so the
reel shows no figure. Built with Claude Code on the brutalist.art toolkit, first as a Liam
/ `am_onyx` reel, then revised twice.

**Where it resisted, and what was done next.**
- *Little resistance on the first build.* 10/10 beats rendered first time. The QC log
  credits lessons from *The Bottleneck Moved*: the three number-printing deck patterns were
  excluded, the safe-area wrapper was in place, branch labels were kept short, the outro
  got `subline: ""`, and motions were labelled accurately. Both risks carried into QC
  (card labels wrapping on `JdgOptions`, row crowding on `JdgStakes`) resolved clean.
- *One numeral.* The numeral sweep found "my last 5 pieces" in the B08 handoff prompt. Kept:
  it sizes the viewer's own exercise, not a claim about the world. During authoring, a speed
  multiple, a proportion of affected roles and "twelve concepts" were cut from narration.
- *Bella ran over.* Switching the voice to `af_bella` (the only permitted female voice)
  took the reel to 180.02s — 0.02s over the 3:00 Shorts cap, which would make `shorts.py`
  cut beats from the portrait version. Fixed by trimming the eight wordiest beats ~20% and
  regenerating audio, to 160.27s.
- *9:16 needed new scenes.* The five illustration scenes had no portrait versions, so they
  were written as relayouts (stacked bands, a 3×4 grid) inside the Shorts UI keep-out, with
  the corner bug moved lower-left.
- *Handle change broke the framing.* Moving from `@NikBearBrown` to `@Yatra` made "in for
  Bear" false, so it was removed; B01 now opens "Hi, I'm Yatra" and B00 no longer
  introduces her. `@HumanitariansAI` was offered; `@Yatra` was chosen.
- *A reference video could not be used.* One was supplied for style; Claude cannot watch
  video, so the intro was built from Yatra's written spec. Recorded so no one assumes it
  was matched.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat sheet,
narration and prompts, wrote the scenes and their portrait versions, ran audio, render and
compile, did the frame-level QC, and carried out both revisions. Accepted rather than
fixed: `underfill` on B07 (0.46) and B09 (0.06) as shipped fidelity components, mono labels
on the two reused patterns, two terracotta elements on B05, the "Fable 5" model chip in the
composer chrome. Zero edge-bleed on the delivered master; Gate V's blanket BLOCKERs were the
known review-cut false positive.

**Now understood / still open.**
- Open: the slug and filenames still read `claude-liam-…`; renaming was left for a decision.
- Open: the `claude-yatra` channel has no row in the skill's channels table.
- Open: *The Bottleneck Moved*'s beat sheet and mp3s were switched to Yatra/Bella but its
  mp4 was not rebuilt, so its master and sheet disagree — flagged here, not fixed.
- The records disagree on runtime: README says 2:40.2, Revision 2 says 160.70s, the beat
  sheet sums to 160.25s, and SHOTLIST still shows the original 2:29 Onyx timings.
- GATE T still cannot run; the 9:16 sheet carries two SKIN LINT warnings not discussed in
  the log.
