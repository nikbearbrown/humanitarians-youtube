# FRICTIONAL — Testing AI Video Editors, and a Setup Guide for New Fellows

The frictional log for this piece of work: short, dated, honest entries about what
was tried, where it resisted, what was done about it and what was learned —
appended as the work goes, never rewritten. What an entry contains, and why:
<https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-09-25 — Agentic editing research + setup guide (week 6, progress)

> Written during the build, with Claude, from this session's record and the
> 2026-09-16 HyperFrames session. The decisions and corrections are mine.

**Working on.** Two things for Lyrical Literacy: whether an AI agent can take on
video editing, to speed up how we make tutorials, and a step-by-step setup guide
for new fellows (Discord, Suno, Midjourney, Canva, and access to the accounts).

**Tried, and expected.**
- Looked at four ways to let an agent edit: Remotion, HyperFrames, OpenReel and
  a DaVinci Resolve MCP connector.
- Tested HyperFrames on 2026-09-16: gave it the finished Suno Part 1 footage and
  audio, asked for white captions that light up word by word, a new intro, and
  motion graphics where needed.

**Where it resisted, and what I did next.**
- The glass look I asked for vanished on our cream backgrounds; the footage was
  moved onto a dark stage.
- The captions copied the phonetic spelling of my name from the voice script
  until they were corrected.
- The render needed about 61 GB of scratch and filled my C: drive. I stopped it:
  nothing goes on C:. Everything was moved into the repo folder on D:.
- The result was a 4:05 cut at 1920 × 1080 — short of our 4K standard.
- The setup guide isn't written yet. The video says it's in progress and claims
  nothing more.
- A first draft of the video said "the other three tools haven't been tested",
  which wrongly included Remotion — Brutalist runs on it. Fixed to OpenReel and
  DaVinci Resolve before the final render.
- The first 9:16 cuts failed the framework's type check: on a phone, body text has
  to be about 4% of the screen height, and most portrait labels were half that.
  Every portrait layout was rebuilt with less text, larger, and short strings
  written for the vertical cut only.
- I had to ask whether the verticals were rendering: they had been reported as
  running before they had actually started.

**What Claude contributed — accepted, changed, rejected.**
- Claude ran the HyperFrames install and the test edit (2026-09-16), then this
  week built the progress video: four new scenes, reuse of three library scenes,
  and every claim traced in FACTCHECK.md.
- Rejected: installing onto C:. Changed: the test's captions (real spelling).
- Kept out on purpose: frames showing other Suno users' names, and the end card
  carrying my surname.

**Understand now / still don't.**
- Now: an agent editor is good at packaging footage that already exists —
  captions, titles, an intro — but it did not add teaching visuals and did not
  reach 4K.
- Still don't know: how OpenReel and DaVinci Resolve compare on the same footage;
  neither has been tested yet.

**Evidence:** [`FACTCHECK.md`](./FACTCHECK.md) · [`SOURCES.md`](./SOURCES.md) · [`pantry/`](./pantry/) ·
[`qc-sheet-16x9.png`](./qc-sheet-16x9.png)
