# FRICTIONAL — The Mask Slips.

> Written 2026-11-03 from this folder's build records (README.md, BUILD-PROMPT.md,
> CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md, QC-LOG.md, SHOTLIST.md, beat_sheet.json),
> not kept week by week during the build.

## 2026-10-21

**Tried / expected.** A concept explainer on AI influencer accounts that go viral and earn
money within days, then lose engagement once audiences identify them as AI. Six supplied
figures, all from one source (Garbage Day, October 2026), with the instruction not to add
numbers or details, to paraphrase rather than quote, and to cite on screen. "Bella, in for
Yatra" intro, `@Yatra` bug, true 4K in 16:9 and 9:16. Result: 13 beats, 2:48.8, eight new
`Msk*` scenes.

**Where it resisted, and what was done next.**
- *Hedged and non-numeric figures.* `$13,700` was supplied as "reported", the engagement
  loss as roughly 50%, and the second case only as "the same drop". Values were typed as
  verbatim strings so none could be sharpened or converted; `MskMoney` requires a
  `reported` stamp beside the figure.
- *Unnamed accounts.* Neither account (nor the platform) was named, so `MaskSlips.tsx` has
  no name, handle or platform prop; cases are labelled with Yatra's own descriptions. No
  screenshots and no AI-generated "influencer" imagery were used.
- *A curve that could imply data.* B05's rise-and-fall arc has no numeric prop, no axis
  ticks, and a required on-screen note: "Shape only — this curve carries no figures."
- *Defects found by reading frames.* B05's "created → viral" label sat where the curve
  drew through it (MAJOR) — moved below the baseline. On B03 the accent rule landed right
  under the source line, so it read as emphasising the citation rather than the caveat
  (MAJOR) — source line lifted clear.
- *Render failures.* After the machine slept mid-render, every render failed to connect to
  the browser: orphaned `chrome-headless-shell` processes and stale puppeteer profile dirs.
  Killed and cleared. Renders then hit Remotion's 30s per-frame timeout, already flagged as
  a risk on Interest Media; an `ART_TIMEOUT` knob (default 120000) was added to
  `runtime/scripts/remotion_scenes.py`. QC-LOG.md records these as costing hours.
- *Toolkit gates.* GATE V false BLOCKERs and missing GATE T handled by substitution, as on
  earlier reels, and logged.

**What Claude contributed, and what was accepted / changed.** Yatra supplied the figures,
their source and the narrative arc ("they turn", authenticity as the lesson). The build
side wrote the beat sheet and scenes, ran audio/render/compile, did the frame QC and made
the `remotion_scenes.py` timeout change. The two framing claims are presented on screen as
argument, not finding. The records don't attribute individual decisions beyond this.

**Now understood / still open.**
- Understood: don't render and encode 4K at the same time; a machine sleep mid-render
  leaves Chrome processes that must be killed before rendering again.
- Open: the Garbage Day report itself was not re-checked in this build.
- Open: README.md says "2:48.3" and "narrated by Yatra"; SHOTLIST.md says 2:48.8 and
  "Bella, in for Yatra". Not reconciled.
