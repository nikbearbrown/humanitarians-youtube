# FRICTIONAL — How Netflix Streams

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-11-10 — Encoding and streaming a show in miniature, and the first three.js stages

> Written during the build (9–10 Nov, for the week of 9–13 Nov).

**Working on.** One of this week's two STEM explainers: how Netflix keeps a show playing when the internet slows,
from the quality ladder and the VMAF score to the player choosing chunk by chunk and servers inside your provider.
I chose the topic, chose HyperFrames for both of this week's videos, then asked for three.js and "beautiful motion
designs".

**Tried, and expected.**
- No expected result was stated up front. The build's working assumption (Claude's) was that the clean test card
  would need far fewer bits than the grainy clip for the same score, and that a player watching its buffer would
  avoid the stalls that always picking the best quality runs into.
- three.js for the 3D stage of each beat, with the HUD kept in HTML on the word clock.

**Where it resisted, and what I did next.**
- libvmaf rejected a log path containing "D:", because the colon breaks ffmpeg's filter syntax; it now writes a
  relative log path from the work folder (BUILD-LOG §1).
- The run bore out both assumptions, but the speed-guessing player didn't stall either, so the buffer player's
  edge is only a higher average bitrate and fewer switches. The first script called that "looked better"; it now
  says "streamed at a higher quality" (BUILD-LOG §1, §2).
- The fact check caught three things: B04 marked slow downloads red as if they were stalls, on lanes the
  narration says never stalled; B06 gave 2022 server figures in the present tense; B07 said a steady connection
  matters "more than" a fast one, stronger than Netflix's own advice. All three were fixed and B04, B06 and B07
  re-voiced (BUILD-LOG §2, §5).
- The narrator read "AV1" as "av one" and "A V one" as "uh vee one"; respelled "A-V-1" (BUILD-LOG §3).
- three.js's module file imports `./three.core.js`, so the core file had to be added and the imports rewritten
  (BUILD-LOG §4).
- The snapshots showed VMAF columns too fat and close, 3D labels placed from the previous camera position, labels
  colliding on the phone and on the globe, and a globe too dim; the gate pre-check found the ground glow counted as
  ink past the title-safe edge and type under the 4K size floor. All fixed before rendering (BUILD-LOG §5). My
  week-11 phone rule applied again: no overlaps; remove text from the bottom and use the room to space the panels.

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched what Netflix has published, wrote the evidence program, the script, the compositions, the
  three.js scenes and the docs, and recommended three.js for the 3D stage with the HUD in HTML. I accepted that
  split and approved the two downloads (three.js 0.187.0 and the Netflix N logo). I set the topic, the renderer,
  the plain-language beginner register and the phone layout rule. Nothing has been rejected yet; my review of the
  renders and of the open questions in FEEDBACK is still to come.

**What I understand now, and what I still don't.**
- Now: one fixed ladder wastes bits on easy pictures and starves hard ones; a player that watches how much video
  it has saved up can ride out a dip that would stall a player always asking for the best; and a server a few
  milliseconds away makes each chunk's trip far shorter on a fresh connection.
- Still don't: what Netflix's players run today, how long its chunks are now, or its current ladders, none of which
  it publishes; and how far VMAF scores on synthetic test clips carry over to real shows.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md).

**Added after the 4K finals (same night, 2026-11-10).** Two things showed up only on the finished frames. On the
landscape QC sheet, B03's curve labels ("CLEAN CARD", "GRAINY ZOOM") ran past the 3D stage into the HUD numbers;
they now sit inside the stage, and B03 and the landscape final were redone. On the phone, B01 and B04's columns
were full (18 px gaps); following my phone rule, B01's two clip cards were dropped on the phone (the 3D panes
switch clips on the word) and B04's numbers were set smaller. Every phone column now has at least 59 px between
panels; all six phone clips were re-rendered and the vertical final rebuilt. B05's phone frame at Gate V's 50%
sample is under-filled because the trip times reveal later on their words; that is declared in the beat sheet
with its reason. QC sheets: [`qc-sheet-16x9.png`](./qc-sheet-16x9.png), [`qc-sheet-9x16.png`](./qc-sheet-9x16.png).
