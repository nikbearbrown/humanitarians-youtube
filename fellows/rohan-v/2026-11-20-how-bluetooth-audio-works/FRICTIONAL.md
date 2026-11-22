# FRICTIONAL — How Bluetooth Audio Works

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-11-19 — Real encoders, a simulated radio, and numbers that had to match what the beat says

> Written during the build (19 Nov, for the week of 16–20 Nov).

**Working on.** One of this week's two STEM explainers: how Bluetooth audio works. I chose the topics for both
videos (this one and Auto-Tune), chose HyperFrames + three.js again, and gave 20 hours for the week. The evidence
has two halves: a synthetic pop track encoded with ffmpeg's real SBC, aptX, aptX HD and AAC encoders, with the data
rates measured from the bytes, and a simulated A2DP link (hopping, a busy Wi-Fi network, body blocking, re-sends and
the headphone buffer). B04 plays the track through that link with a small and a big buffer.

**Tried, and expected.**
- No written prediction is on file. What the fact sheet led us to expect: SBC at about a quarter of CD's data rate,
  adaptive hopping cutting the losses from Wi-Fi, and a bigger buffer trading gaps for delay. Those held: SBC at
  330.7 kbit/s (1/4.3 of CD); 17.4% of tries lost to Wi-Fi without adaptive hopping, 0.9% with it; 30 glitches in
  two minutes at 50 ms, 3 at 200 ms, none at 300 ms.
- Open going in: whether a few seconds of the small-buffer clip would make a gap audible. In the chosen window it
  is one short stutter; whether that is enough is the first question in FEEDBACK.

**Where it resisted, and what I did next.**
- The first codec table had a quality column (waveform SNR) and a frequency-cutoff column. SNR ranks codecs built
  around hearing unfairly, aligning aptX's output for it failed, and the cutoff didn't separate the codecs, so both
  columns were dropped. With no listening test, the film makes no quality ranking (BUILD-LOG §1).
- The listening window could have been picked to sound dramatic. It was picked as typical instead: the 6 s whose
  glitch rate is closest to the 50 ms buffer's average (BUILD-LOG §1).
- The fact check found B02's first numbers (22% failing, under 8% with adaptive hopping) included body blocking,
  which B02 never mentions; most of the remaining 8% was body blocking, not Wi-Fi. B02 now gives the Wi-Fi-only
  figures, 17% and about 1%, and B04 names both causes. It also held "Apple's devices use AAC" (now "prefer") and
  "the newest version, LE Audio" (now "next generation"). All were re-voiced the same day (BUILD-LOG §2).
- At about 2:26 the video is longer than the usual ~2:08, mostly because B04 carries two clips. Left as it is for
  review (FEEDBACK).
- No Bluetooth SIG, Qualcomm or Sony mark was in the toolkit, and downloading needs my OK, so Sony and the SIG are
  named on screen without a mark for now (FEEDBACK).
- Snapshot review found 3D labels showing outside the stage, B04's tank labels colliding on the phone and bar
  labels running long; each was fixed before the renders (BUILD-LOG §5).

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched the radio, the codecs, latency, delay reporting and LE Audio (the graded fact sheet), wrote the
  encoder runs and the link simulation, the listening clips, the three.js scenes, the HUD and the docs, and ran an
  independent fact-check pass. I chose the topic, chose HyperFrames + three.js again, set the week's hours, and kept
  my week-11 phone rule. Review of the 4K finals was pending at the time of writing.

**What I understand now, and what I still don't.**
- Now: Bluetooth can't comfortably carry CD-quality data, so the music is always squeezed first; the radio hops to
  dodge Wi-Fi, and adaptive hopping simply stops using the busy channels; the buffer that rides out lost packets is
  the same thing that makes earbuds lag; and videos can hide that lag by holding the picture back, games can't.
- Still don't: how real earbuds size their buffers, which no source here gives; how much a game mode actually
  reduces the delay; and how my simulated losses compare with a real phone in a real pocket.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md).
