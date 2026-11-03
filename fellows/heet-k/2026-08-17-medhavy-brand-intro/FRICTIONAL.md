# Frictional log — Medhavy brand intro

## 2026-08-30 — logo reel and ident, first pass

> Written 2026-09-28, after the week it describes. Reconstructed from the beat
> sheet, the scene code and [script.md](script.md); it is not a contemporaneous entry.

- **Drive:** https://drive.google.com/drive/folders/1fZCmWm_aQgs1epDGp085T5Ucs0VcK7XK
- **Beat sheet:** [beat_sheet.json](beat_sheet.json) — 80 beats
- **Scene code:** [medhavy_logo_reel.py](medhavy_logo_reel.py), [medhavy_logo_ident.py](medhavy_logo_ident.py)

**What I was working on.** Giving the Medhavy channel a brand sting — an animated
logo reel that establishes the mark, wordmark, tagline and URL, plus a shorter ident.

**What I tried, and what I expected.** I expected picking the logo to be the quick
part and the animation to be the hard part. It was the other way round. There were
58 candidate marks and no brand guidance to choose between them, so I built a
contact sheet and chose `medhavy-08` by eye. I also expected a single "best"
animation to emerge; instead the montage section exists precisely because it
didn't — the reel shows several build patterns rather than committing to one.

**Where it resisted, and what I did next.**

- **No brand colour existed.** Nothing specified ink or accent. Rather than stall,
  I picked `#15151c` ink and `#2A6FB0` accent and wrote them into
  [script.md](script.md) as a labelled default — "no brand color was specified;
  these are a tasteful default" — so a later decision would overwrite a stated
  guess rather than an invisible one.
- **The wordmark wouldn't match the CSS spec.** Manim has no letter-spacing
  primitive. Solved with a `tracked_text(..., track=0.28)` helper that positions
  each glyph individually to hit the 0.28em spec.
- **Narration drifted against the silent sections.** The reel is mostly silent
  construction with three spoken lines that must land on specific frames. Fixed by
  marking the construction, montage and hold beats `"silent": true` so the three
  spoken lines stay pinned to their own sections instead of being spread across
  the whole timeline.
- **ElevenLabs mispronunciation risk on "Medhavy."** I did not solve this; I wrote
  the remedy down in [script.md](script.md) — set `tts_normalized_text` to a
  phonetic spelling on `B02_NAME` and re-render that beat alone.
- **I chose not to build the 9:16 cut.** It was a real deliverable and I deferred
  it, recording it in [script.md](script.md) as available on request. That deferral
  stayed open for six weeks and was closed in Week 16.

**What Claude contributed, and what I accepted, changed or rejected.**

- Accepted: PNG tile-assembly as the render path, and a different build pattern per
  logo. It makes the montage read as a showcase rather than a repetition.
- Accepted: the `"silent": true` beat flag as the sync mechanism.
- Changed: the hero mark. The choice among 58 was mine, made from the contact
  sheet, not delegated.
- Left open: the palette. Recorded as a default rather than presented as a decision
  I was entitled to make.

**What I understand now, and what I still do not.**

I understand that when a spec is missing, writing down the guess *as a guess* is
more useful than either stalling or quietly deciding — the palette note is the
reason a later reviewer could have overruled me cheaply.

I do not know whether the accent blue reads correctly against the channel's
thumbnails at small sizes, because I never tested it there. I also do not know
whether `medhavy-08` was the right hero; I chose it on a contact sheet, not against
any stated criterion.

*Answered 2026-10-17 — see the entry below.*

---

## 2026-10-17 — the feedback that came back on these intros

> Written 2026-10-17, well after the week it describes. Appended; the entry
> above stands as written.

The professor did give specific feedback on this first intro set, and I worked
on it the following week. It was about **length, the use of colour, the
background**, and similar presentation choices — the surface of the thing
rather than the concept.

**This is where my palette guess got answered.** The entry above records that no
brand colour had been specified, so I picked `#15151c` ink and `#2A6FB0` accent
and wrote them down as a labelled default rather than a decision. Colour use
coming back as feedback is exactly the correction that note was there to make
cheap. Writing the guess down as a guess worked — it gave the review something
explicit to push against instead of something assumed.

**Length too.** The reel ran ~118s across 80 beats, which I had treated as a
showcase length. For a brand sting that is long, and the feedback said so.

**What I still cannot say precisely** is which specific changes I made in
response — the revisions happened in the following week and I did not log them
against this feedback at the time. The result is in
[Week 14](../2026-09-04-medhavy-brand-outro/), where the intros were confirmed
final.
