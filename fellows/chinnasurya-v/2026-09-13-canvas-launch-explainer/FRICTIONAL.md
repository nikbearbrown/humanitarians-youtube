# Frictional — How a Canvas Launch Works

> Entries for 2026-09-13 are compiled from the contemporaneous `BUILD-LOG.md`
> written during that build. The 2026-10-28 entry was written on the day.

## 2026-09-13 — what I expected and where it resisted

Expected the reel to come out around 4:20 because the script runs 660 spoken
words and I assumed about 2.55 words a second. It measured 3:15.4. Kokoro read
roughly 19 percent faster than I had planned for. I did not pad holds to close
the gap. The duration is an output of the narration, not a target I get to hit,
and inventing silence to reach a number would have been dishonest about the
pacing.

The real fight was with the frame. The first render passed GATE V and still
looked wrong: content bunched into the top 55 percent with a dead band above the
footer, and type reading small at 4K. The gate measures a content bounding box,
and my footer line stretched that box to the frame edge, so the check passed on a
frame that was visibly underfilled. **A bounding-box test is not a fill test.**
That is the thing I actually learned here, and it took a visual inspection to
find because no gate was going to tell me.

The fix was not a tweak. I rewrote the scene layout off hand-set pixel offsets
onto fractions of the available band between header and footer, and scaled type
up across the board: display 230 to 280, h1 150 to 200, h2 104 to 140, body 80 to
108, data 66 to 88, caption 52 to 62. All 11 beats re-rendered and re-inspected.

## 2026-09-13 — what Claude contributed and what I changed

Claude drove the toolkit and the scene renderer under my direction. The script,
the framing decision, and the call on what to cut were mine. Two judgment calls I
made and want on the record:

- The narration says "Surya" in B00. That was taken from conversation context
  rather than from the script, and it was flagged to me at build time. I left it.
- An earlier draft carried two security findings from my own review of the code.
  I cut them and went to a pure-mechanism framing, because the reel is about how
  the protocol works and not about a specific system's weaknesses. The draft is
  kept at `script-findings-v1.md` rather than deleted.

GATE P was proceeded through with `--no-gate` and `PEDAGOGY.md` still carries
`VERDICT: PENDING`. I did not self-sign it. The narration is my own approved
text, but the pedagogy gate asks for a human signature and I am not going to
pretend one exists.

## 2026-09-13 — two lints I reported rather than silenced

`SKIN LINT: NO RENDERABLE BEATS` fires because no beat carries a Remotion
pattern, since every visual is pre-rendered out of tree. The same run reports
11/11 filled. It is a false positive for this architecture and I left it visible.

`'step-reveal' carries 6/11 beats (54%), over the ~40% cap` is real, but the
motion labels come from my own shot list. Relabelling them to pass the linter
would have misdescribed the motion. Left as written.

## 2026-09-13 — still open

- No 9:16 cut. At 3:15 it is over the 180 second Shorts cap, so a vertical
  version needs beats dropped, and that is my call to make rather than the
  build's.
- No captions or word clock. `faster-whisper` is not installed on this machine.

## 2026-10-28 — filing this as fellowship evidence

Moved the film-as-code source into my fellows folder for the renewal. The render
stays on Drive per the repo rule; what is here is the beat sheet, the script, the
fact-check, the sources, the pedagogy note, the build log, the scene renderer and
the QC contact sheets. Writing this entry made me notice how much of the useful
record was sitting only on my laptop for six weeks.


## 2026-10-28 — the portrait pass, six weeks late

This reel shipped in September as 16:9 only. The 9:16 cut was attempted then and
abandoned: the render crashed with `ValueError: x1 must be greater than or equal
to x0` and I recorded it as "beats compute right-hand positions from landscape
width", which was true but not the whole story.

What I expected: a font-sizing problem. What it actually was, three separate
faults stacked on each other.

**First, I ran the renderer without `--aspect 9:16`.** It defaults to 16:9. My
first note this session said the renderer "never reads `aspect_ratio` from the
beat sheet" — wrong, and wrong in a way that would have sent the next person
looking in the wrong file. It takes the aspect as a flag and I had not passed it.

**Second, hardcoded landscape coordinates.** Five beats placed boxes at literal
pixel columns — `lx1, rx0 = 1560, 2280`, `cx = 1980`, `c3 = 2980`. In a
2160-wide frame the right edge of a box landed left of its left edge, which is
what the crash was. These are now stacked single-column layouts in portrait,
branched on `L.portrait`, not rescaled two-column ones: a 426px column cannot
hold a 470px numeral, and the lesson from the two reels built last week is that
single-column reads better on a phone anyway.

**Third, and this is the one worth keeping.** `fit()` promised in its own
docstring that "overflow is a gate-V blocker, so never risk it", and then
measured only glyph *advances*. A heavy display face inks past its last glyph's
advance, so a string that measured as fitting still crossed the title-safe edge
by about 76px. It now measures the rendered bbox as well and takes the worse of
the two. Separately, fifteen `d.text` calls used a fixed font size with no width
bound at all; they go through a `btext()` helper now that fits before drawing.

One more, in `Four Documents` only: the title card sized its font on the word
`FOUR` and then drew `DOCUMENTS` with it. At 16:9 there was slack to absorb the
difference. At 9:16 there was not.

What I got wrong in reporting, before the code: I told Surya ten of twelve files
were done as though that were finishing, twice. It was not. The two missing cuts
were the two that needed real layout work rather than a re-run.

Both masters are now 1216x2160, GATE V clean at 0 blockers and 0 majors, and the
contact sheets were read against the script rather than just gate-checked —
because a gate passing is not the same as a beat reading correctly, which this
folder has already learned once.
