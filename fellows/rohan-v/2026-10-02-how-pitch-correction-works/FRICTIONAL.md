# FRICTIONAL — How Pitch Correction Works

The frictional log for this piece of work: short, dated, honest entries about what was tried,
where it resisted, what was done about it and what was learned, appended as the work goes and
never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-05 — Pitch correction explainer (week of 28 Sep, STEM) — built late

> Written during the build, with Claude, from this session's record. Labelled late: this is
> the STEM video for the week of 28 Sep – 2 Oct, built and submitted on Monday 5 Oct because I
> forgot to submit on Friday. The decisions and corrections are mine.

**Working on.** How pitch correction (Auto-Tune style) finds the pitch of a sung note and pulls
it into tune: for Lyrical Literacy fellows who sing over Suno tracks and reach for a tuning
plug-in without knowing what its two big settings do.

**Tried, and expected.**
- Asked for this week's two videos plus every record brought up to the latest rules, after
  pulling the newest Brutalist code first (merged: three conflicts, all kept from both sides).
- Was offered four STEM topics with a recommendation (text-to-speech); I chose pitch
  correction instead. Expected a straightforward "detect, then snap" explainer.
- Expected the corrected melody to be measurably in tune, and the chromatic-versus-key
  example to land cleanly on the wrong note.

**Where it resisted, and what I did next.**
- The framework wants executable evidence, so `pitch_demo.py` was written to actually do it:
  YIN detection, snapping, a retune glide, TD-PSOLA pitch shifting, then the same detector run
  again on the corrected audio. Every "after" number is re-measured, not assumed.
- The wrong-note example misbehaved: with the last note 62 cents flat, the vibrato's peaks
  crossed the halfway point and the chromatic result flickered between F♯ and G. That is real,
  but it is not what the narration said. The note was moved to 75 cents flat, the run repeated,
  and three spoken numbers changed (37 → 40, 18 → 19, 62 → 75), so those beats were re-voiced.
- The portrait layouts first collided: two-line titles ran over the content and labels
  overlapped. They were rebuilt as phone-first layouts with one-line titles in the vertical
  sheet, checked again in probe stills.
- The first final was blocked by the type check (the brand terracotta curves read as text), and the
  first renders ran on a 20-second default clock, so the long beats froze before their listening
  clips. Both caught before any final was built; the curves were recoloured and the beats
  re-rendered with their measured lengths.
- "Retune speed" could not be verified on the Auto-Tune maker's site, so the video calls it
  "speed" and does not quote a product range. The 1997 release and the 1998 "Cher effect" are
  from Wikipedia's AutoTune article, cited in FACTCHECK.

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude proposed the topics, wrote the evidence script, the six scenes and the narration,
  and found the flickering-note problem in a probe frame.
- I rejected the recommended topic (text-to-speech) and chose pitch correction; I gave this
  week's hours (20) and confirmed the renewal was approved.
- Accepted: adding listening clips so viewers hear the before and after, rather than only
  seeing curves.
- My review of the preview: pending at the time of this entry (appended below once done).

**What I understand now, and what I still don't.**
- A corrector only knows the *nearest* allowed note. Setting the key is what stops it from
  confidently choosing the wrong one; speed is what decides whether it sounds like a person.
- Still don't know how commercial tools handle a note that sits exactly between two allowed
  notes, or how they avoid the onset jump the scoop produced here (C major snaps the start of
  the last note to F before it reaches G — visible at the left of B05 and B06).

Evidence: `pitch_demo.py`, `evidence/run.log`, `evidence/pitch_demo.json`, `mix_listen.py`,
`beat_sheet.json`, `vertical/beat_sheet.json`, QC sheets.

**My review, 2026-10-06.** Watched both cuts of this video (16:9 and 9:16) after they were built; no changes requested.
