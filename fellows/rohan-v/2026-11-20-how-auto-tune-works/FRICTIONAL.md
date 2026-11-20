# FRICTIONAL — How Auto-Tune Works

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-11-19 — A synthetic singer, a pitch corrector, and the numbers that had to be fixed first

> Written during the build (19 Nov, for the week of 16–20 Nov).

**Working on.** One of this week's two STEM explainers: how Auto-Tune works. I chose the topics for both videos
(this one and Bluetooth audio), chose HyperFrames + three.js again, and gave 20 hours for the week. The evidence is
a small pitch corrector built from textbook parts: a synthetic singer singing a short tune in C major slightly
off-key, a pitch detector, a corrector with two retune speeds, and three ways of moving a held note up four
semitones. B05 plays the singer's three takes so viewers can hear the difference.

**Tried, and expected.**
- No written prediction is on file. What the fact sheet led us to expect: that zero retune speed would snap the
  voice to the notes while a slower speed would let the vibrato survive, and that shifting pitch the old way
  (without formant correction) would move the vowel. Those held: at zero the voice sat within 5 cents of a note
  90.6% of the time, against 29.8% at 60 ms with the vibrato kept (about ±14 cents); plain resampling moved the
  vowel +25.8% for a ×1.260 shift.
- Expected: that PSOLA, re-spacing single cycles, would keep the vowel. It did: +0.6%.

**Where it resisted, and what I did next.**
- Two of the first measurements were wrong in ways the numbers alone didn't announce. A "how fast does it reach
  the note" metric was thrown off by the singer's scoops and detune, so it was replaced by the share of sung time
  within 5 cents of a note. The first vowel measure, picking peaks from the average spectrum, gave +14% and −8%,
  because the first two resonances of "ah" merge; a stretch fit on the smoothed spectral envelope replaced it
  (BUILD-LOG §1).
- The detector misses 11 frames, all within 11 ms of a note's start. They stay in the numbers; only the drawing
  leaves them out, after they showed up as spikes in the snapshots (BUILD-LOG §1, §5).
- PSOLA's output had a click at its edge (0.26), fixed with 10 ms fades.
- Research showed that Auto-Tune's patent moves pitch by resampling and repeating whole cycles, which my first
  comparison didn't include. Adding it showed the patent's way keeps the length but moves the vowel about as much
  as plain resampling (+27.8%), so B04 now shows three methods, and the film speaks of the patent, not of today's
  product.
- The fact check held two lines: "under seven cents off" hid one note still 19 cents flat (now "averaged"), and the
  close described my method as if it were Auto-Tune's (now it names the job). Both were re-voiced (BUILD-LOG §2).
- Snapshot review found tracks washed to white where they crossed, a blank 3D stage in B04 (a panel id clashing
  with the page's data script), labels outside the stage and colliding lane labels; each was fixed before the
  renders (BUILD-LOG §5).

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched the release, the patent, "Believe" and tuning (the graded fact sheet), wrote the synthetic
  singer, the detector, the corrector and the shift comparison, the three.js scenes, the HUD and the docs, and ran
  an independent fact-check pass. I chose the topic, chose HyperFrames + three.js again, set the week's hours, kept
  my week-11 phone rule, and kept the fellows-repo rule that no surnames appear, so the inventor and the producers
  are not named. Review of the 4K finals was pending at the time of writing.

**What I understand now, and what I still don't.**
- Now: pitch is how often a wave repeats, and finding it means sliding the wave along itself until it lines up;
  "off key" is usually tens of cents, not a wrong note; retune speed is the whole difference between a natural
  correction and the robotic one; and moving a pitch without moving the vowel needs the cycles re-spaced, not the
  recording sped up.
- Still don't: how Antares' current versions detect and correct pitch beyond what the patent describes; whether my
  synthetic singer sounds enough like a singer for the takes to convince; and whether the three takes are clearly
  different on a phone speaker. Both of the last two are open in FEEDBACK.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md).
