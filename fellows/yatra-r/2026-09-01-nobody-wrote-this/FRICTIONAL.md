# FRICTIONAL — Nobody Wrote This.

> Written 2026-11-03 from this folder's build records (README.md, BUILD-PROMPT.md,
> CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md, QC-LOG.md, SHOTLIST.md, SOURCES.md,
> YOUTUBE.md), not kept week by week during the build.

## 2026-09-01

**Tried / expected.** A 1–3 minute ai-explainer on LinkedIn being the most AI-saturated
platform in a ~1 million post scan: 41% of long-form posts fully AI-generated, only 4.3%
AI-assisted. Seven figures supplied verbatim by Yatra from two sources (Pangram Labs, "AI in
Your Feed," July 2026; Tech Times), with the instruction not to add numbers. 14 beats, 2:48,
Kokoro `af_bella`, `@Yatra`, 16:9 at 4K plus a full 9:16 vertical.

**Where it resisted, and what was done next.**
- *A number available by subtraction.* The human-written share (100 − 41 − 4.3) was never
  supplied. `LnkAllOrNothing` was built with no prop for a remainder figure; the band
  renders dashed and empty.
- *Ranges break the house parser.* The `num()` helper reads "4–13%" as 413. A new
  `LnkLadder` takes a separate `bar` number (range midpoint) while printing the verbatim
  string, instead of reusing `SeoCompare`.
- *Sensational framing.* "AI slop is taking over social media" was dropped; Substack (~10%)
  and Reddit (4–13%) in the same scan became the falsifier beat (B09). The B10 reputation
  argument is tagged INTERPRETATION on screen.
- *Four layout defects, all invisible to the mp4 probe.* A doubled "Source: Framing:" on
  B02; a dashed rule cutting through a label on B06; bands overlapping the citation on B07;
  the date axis striking through "August 2, 2026" on B10. Each fixed in scene source and
  re-rendered.
- *A failed re-render that exited 0.* `--only B02 B06 B07 B10` errored because the script
  takes one value, but the pipe to `tail` reported success. Caught only because B07 looked
  unchanged in the re-extracted frame; re-run as four separate calls.
- *GATE V false positive.* Pointed at the slate cut, it flagged the burned-in timecode as
  28 BLOCKERs. Re-run on the clean master: 0 BLOCKER, 2 MAJOR underfill on the outro,
  accepted as the stock card's design.
- *Wrong handle on the vertical.* The Short ended on `@nikbearbrown` because `shorts.py`
  defaults its `--handle`. Endcard regenerated with `@Yatra` and verified in the compiled
  mp4 at t=170.5s.
- *Environment.* System Python 3.14 has no wheels for the pinned deps, so the build ran in
  a 3.12 venv; Manim is not installed and no beat needed it.

**What Claude contributed, and what was accepted / changed.** Claude drafted the beat sheet,
narration and on-screen prompts, wrote nine new `Lnk*` scenes (reusing `JdgStakes` for B09),
ran audio, render and compile, did the frame-level QC and fixes, and wrote the paperwork.
Two shared-component changes were deliberately left alone: enlarging `ClaudeTitleOutro` and
adding a brand bug to `ClaudeVerdictArtifact`, both flagged for the channel owner. The
records do not say what Yatra changed or rejected.

**Now understood / still open.**
- Understood: a zero exit status on this pipeline proves nothing; check the frame.
- Open: the delivered reel `claude-liam-the-judgment-is-the-job` likely has the same
  `@nikbearbrown` endcard; flagged, not fixed. The upstream `shorts.py` fix was not applied.
- Open: Pangram Labs' methodology was not independently verified, and no URL was supplied
  for either source.
- Open: SOURCES.md flags that this reel argues somewhat against the existing
  `ClaudeLinkedin` reel's premise — worth checking before both are published.
