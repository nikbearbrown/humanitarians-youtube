# FRICTIONAL — The Bottleneck Moved.

> Written 2026-11-03 from this folder's build records (README.md, BUILD-PROMPT.md,
> CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md, QC-LOG.md, SHOTLIST.md, beat_sheet.json),
> not kept week by week during the build.

## 2026-08-20

**Tried / expected.** A 1–3 minute ai-explainer arguing that AI made producing marketing
content nearly free but left the cost of attention and trust where it was. Ten beats, all
Remotion, free path only. No external source was used, so the reel was built as an
argument from a stated model: every magnitude on screen is an ordinal ranking, labelled as
ordinal in the frame. Built with Claude Code on the brutalist.art toolkit.

**Where it resisted, and what was done next.**
- *Shipped components printed numbers.* Three of the five reused deck patterns broke the
  no-measured-figure rule or crashed. `ScaleComparison` crashed the render (`log10(0)` on
  an axis starting at 0) and is a log-scale component anyway. `AttritionChain` multiplied
  survivals into "1 / 100" and "1% remain". `Threshold` printed a 0–100 axis and clipped its
  own label. All three were replaced with purpose-built ordinal scenes.
- *Picture contradicted caption.* B01's terracotta line climbed while labelled
  "unchanged"; relabelled "did not fall". A doubled arrow (`→ →`) on the same beat was also
  removed.
- *Labels past title-safe.* B01 and B06 put label boxes at x≈3792 of 3840. Rather than edit
  patterns shared with other reels, the whole composition was mapped onto the safe box in a
  reel-local `Stage` wrapper.
- *Wrong outro subline.* B09 showed Musinique's "bot vs bot, season one" because the sheet
  passed a `slug` prop the component ignores; now passes `subline: ""`.
- *Smaller fixes.* B05's prop shape was wrong (caught by checking payloads against the
  TypeScript types before the first render); B03 lacked a spark line (caught by SKIN LINT);
  five beats all labelled `motion: illustrate` tripped the 40% cap and were relabelled.
- *Gate V failed every frame.* 20 identical `edge-bleed` BLOCKERs, traced to Gate V
  checking the review cut and flagging its own top-right burn-in, which `BURN_IN_EXCLUDE`
  does not mask. Measured on the clean master instead: zero edge-bleed.
- *Toolkit gaps.* `type_check.py` (GATE T) is not shipped, so type was checked by eye; the
  outro mascot components are absent; Manim could not be installed (no Homebrew/sudo for
  cairo). None of these changed the reel, which has no Manim beats.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat
sheet, narration and on-screen prompts, wrote the fact-check and the PROOF GATE report,
wrote and replaced the scenes, and did the frame-level QC. Accepted rather than fixed, with
reasons logged: `underfill` on the B07 verdict card (0.46) and B09 title outro (0.07),
since both are shipped fidelity components; mono labels on the two reused patterns; two
terracotta elements on B06; a "Fable 5" model chip in the composer chrome on B00/B03/B08.
A planned palette retint was dropped once the patterns turned out to use the claude values
already.

**Now understood / still open.**
- The records disagree with each other. BUILD-PROMPT, PROMPTS and SHOTLIST describe a
  Liam / `am_onyx` / `@NikBearBrown` build at 2:20.5; README and `beat_sheet.json` give
  Yatra / `af_bella` at 2:46.1, with the beat sheet still on the `@NikBearBrown` handle and
  "in for Bear" framing while README says `@Yatra`. Nothing in this folder records when the
  switch happened or whether the master was rebuilt after it.
- Open: the Gate V false positive and missing GATE T script are toolkit issues, flagged
  upstream in the QC log, not fixed here.
