# Frictional log — Every Reading Said Fine

## 2026-10-12 — The beat that was never going to render

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1YZ3bLjWZ74sSdhdx4vC9X8MTLOykNk_6?usp=drive_link (`Medhavy_Kehinde/STEM Topic/every-reading-said-fine/`)
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** github.com/Kenny0bi/real-time-vitals-pipeline
- **Paired report:** [Fact-Checking Chapter 9](../2026-10-13-chapter-9-review/)

**What I was working on.**

The STEM explainer for week 7, paired with the Chapter 9 audit. One idea: a threshold
that is correct on every individual reading still misses a patient who is deteriorating,
because deterioration is in the trend and a threshold only sees the instant.

**What I tried, and what I expected.**

New doctrine landed upstream in late September: `docs/EXECUTABLE-EVIDENCE.md` says run
the code, do not copy numbers out of a README. So I ran the repo's own simulator and
scorer at seed 42 rather than quoting my own documentation. Twelve patients, 1,800
readings for the one I follow.

The numbers that came back are better than the ones I would have written from memory.
62.1 percent of readings on a deteriorating patient still scored two or below. 1.3
percent crossed the immediate-review threshold. Oxygen saturation fell eighteen points
across that span. I also ran the test suite: 101 passed, 1 skipped.

Running it changed the video. I had been going to say the threshold "misses"
deterioration. It does not miss it. It fires correctly, 24 times, on a patient who has
been sliding for most of an hour. That is a different and more interesting claim, and I
only got to it because I ran the thing.

**Where it resisted, and what I did next.**

One beat cost most of the build. B02 is the beat where I say "this is the front end I
built for it", and it would not render. Both compiles were refused with the same
message: the clean master would carry one slate, B02. There was no error anywhere in
the log, which is what made it slow. The scenes pass printed B00 ok, B01 ok, then B03
ok. B02 was not failing. It was being skipped.

The cause was in my own beat sheet. The beat had been authored as a screenshot beat and
carried a `rendered` stub pointing at `media/B02.mp4`, a file nothing was ever going to
write, and no renderable pattern at all. The renderer skips any beat with no pattern,
silently, and the compiler then finds no media and calls it a slate. Two correct
behaviours that between them produce no error message.

My first instinct was to replace the beat with an abstract two-column card, which would
have rendered immediately. I did not do that, because the narration says "this is the
front end I built for it" and pointing those words at a diagram would have made them
untrue. Instead I went and got the real thing: the project ships a capture of the
telemetry wall in `docs/screenshots/`, and it matches the narration line for line.
Twelve patients, 1 Hz refresh, the five-spoke MEWS rose, amber tiles in the second row,
nine stable and three deteriorating.

That left a second problem. The component that puts a real capture on screen,
`BrowserCapture`, only had a landscape layout, and the 9:16 deliverable has to be a
native render rather than a crop. So I added a portrait layout to it: a re-laid-out
window on the 1080x1920 canvas with type set larger relative to the frame, and
registered the portrait composition beside the landscape one. It is the same component
and the same props, which is how the other dual-aspect components in this toolkit work.

Two smaller things. The capture overflowed the window and clipped the page header, so I
cropped it to the region the narration actually refers to, which also removed a band of
dead black space. And the portrait render died once on Remotion's 30 second
initial-render timeout while the same component rendered fine in 34 seconds when given
room, so I raised that timeout in the pipeline.

**What Claude contributed, and what I did with it.**
- Mine: the project, the idea, the decision to run the code rather than quote it, and
  the call to go find the real screenshot instead of accepting a substitute.
- Claude's: the diagnosis of the silent skip, the portrait layout for `BrowserCapture`,
  the camera move and ring coordinates, and the beat sheet draft.
- Accepted: the three camera moves, which land on the full wall, then the legend that
  explains the five-spoke rose, then one amber patient at MEWS 4 beside a near-bare
  patient at MEWS 1.
- Rejected/changed: the proposed substitute card for B02. The narration promises my
  actual interface, so the beat had to show it.
- Evidence: `FACTCHECK.md` lists all 12 on-screen claims and how each was measured.
  Every figure is reproducible at seed 42.

**What I understand now, and what I still do not.**
- Understood: the silent-skip failure mode. A beat with no renderable pattern produces
  no error, only a refusal two steps later naming a slate. I will check that a beat has
  a pattern before I check anything else.
- Understood: running the code is not a formality. It changed what the video argues.
- Not understood: why 62.1 percent is as high as it is. Most of it is the long early
  stretch where the patient is genuinely still in range, but I have not separated that
  from the later readings where the score lags behind a patient who is visibly going.
- Open: the 62.1 percent figure is one patient at one seed. I would want a sweep across
  seeds and deterioration types before I put a number like that in front of anyone
  clinical.
