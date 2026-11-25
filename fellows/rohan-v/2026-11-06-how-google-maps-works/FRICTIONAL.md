# FRICTIONAL — How Google Maps Works

The frictional log for this piece of work: short, dated, honest entries about what was tried, where it
resisted, what was done about it and what was learned, appended as the work goes and never rewritten. What an
entry contains, and why: <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-11-09 — Simulating a maps app, and the first video built in HyperFrames

> Written during the build (Monday 9 Nov, for the week of 2–6 Nov).

**Working on.** The second of this week's two STEM explainers: how Google Maps finds you, routes you, sees
traffic and predicts crowds, each part simulated because Google's data and routing algorithm aren't public. I
asked for its motion beats to be built in HyperFrames instead of Remotion.

**Tried, and expected.**
- No expected result was stated up front. The build's working assumption (Claude's) was that enough phones
  would reveal a crash that history can't see; the first run didn't show it.
- A first HyperFrames version in the channel's cream style.

**Where it resisted, and what I did next.**
- The crash never turned red, because the simulated phones routed around it using live speeds no real driver has.
  They now plan with usual speeds, and 500 phones turn it red (BUILD-LOG §2).
- The narrator read "A star" as "uh star"; respelled "A-star" and re-voiced (BUILD-LOG §3).
- I asked for a more premium, non-cream look and for the Google Maps elements to look exactly like the app: the
  night-city version, with the cream one kept (BUILD-LOG §5).
- Rendering fought the machine: about 21 GB of temporary frames headed for C: (moved to D:), failures while C:
  was full and Pro Tools held about 10 GB of memory, a render cancelled from a hidden-window launcher while a
  direct run worked, and HyperFrames windows opening on my screen, which I flagged (BUILD-LOG §6).

**What Claude contributed, and what I accepted, changed or rejected.**
- Claude researched what Google has published, wrote the simulation, the compositions and the docs. I set the
  brief and the hours, chose HyperFrames, rejected the cream look, asked for app-accurate Google Maps elements,
  and freed space on C: for the renders.

**What I understand now, and what I still don't.**
- Now: the fourth satellite is there for the phone's clock; a search that aims at the destination checks far
  fewer corners for the same route; and traffic, busyness and crowding only exist where enough people's phones
  or answers are pooled.
- Still don't: which routing algorithm Google actually runs, which it doesn't publish; and what "accurate" means
  in its 97% arrival-time figure, which it doesn't define.

Evidence: [`evidence/run.log`](./evidence/run.log), [BUILD-LOG](./BUILD-LOG.md).
