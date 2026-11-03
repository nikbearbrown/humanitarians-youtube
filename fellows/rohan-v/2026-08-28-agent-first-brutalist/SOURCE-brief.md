# SOURCE-brief — "Your Weekly Video, Handled."

What was asked for, and what the source material was.

## The request

Build a video explaining how to use Brutalist and how Humanitarians AI fellows
should submit their weekly output — everything from setting up the repository to
final submission. Targeted at people who are **not necessarily experienced with
code**, and understandable by any audience.

Specifically required:

1. Outline every step a fellow performs to deliver videos each week.
2. Make explicit **which steps are manual and which the agent automates**.
3. Show **how the fellow interacts with Claude** (the desktop app).
4. Show **how videos are saved locally** and **how code is submitted to GitHub**.
5. Give the **exact links** — toolkit repo, submission repo, Drive folder.
6. State that four 4K files are due per week — two topics, each in 16:9 and 9:16.
7. Open with "Hi, I'm Rohan"; sign off "Rohan V.".
8. Fluid animation; recreate the Claude desktop app, the GitHub website, and the
   other windows a fellow meets along the way.
9. Voice: Kokoro `af_bella`.
10. Keep the on-screen greeting simple — the presenter's name only; Humanitarians
    AI may be named. No other individual named in narration or on-screen copy.

## Source material supplied

Three screenshots of internal email, read for factual content only:

| Source | Supplies |
|---|---|
| "Weekly videos: what to make, what to upload, due Fridays" (2026-08-20) | The two-video / two-format / four-file requirement, the Friday deadline, and the flexibility floor |
| "Re: Updated Drive folder for video submissions" (2026-08-24) | The Drive folder link and the `fellows/` code path |
| "Compliance review — please make sure your reporting is current" (2026-08-27) | Context on why reporting matters; **not** cited as fact in the reel |

Plus a screenshot of the existing submission folder layout, used to match this
folder's document set to the convention already in the fellows repository.

Full verification of every derived claim is in [`FACTCHECK.md`](FACTCHECK.md);
provenance for each source is in [`SOURCES.md`](SOURCES.md).

## Decisions taken during the build

| Question | Decision | Why |
|---|---|---|
| Which skill? | `ai-explainer`, Pragmatist register | Single-purpose instructional reel at 3–5 minutes; the HAI register requires stating where the method fails, which this topic needs (B05, B09) |
| Should the agent push straight to `main`? | No — pull request, both routes | New fellows lack write access; B08 shows fork+PR and branch+PR converging on the same review |
| Should the agent upload to Drive? | No | Confirmed as a human step. The reel states it plainly rather than implying automation that does not exist |
| Read the URLs aloud? | No — shown on screen only | Spoken URLs are unusable to a listener, and the repo path contains a name the narration must omit |
| 9:16 version? | Deferred | The reel is 4:14, over the 3:00 Shorts cap, and none of the ten components has a portrait layout yet. Raised as a separate decision rather than silently cropping — `shorts.py` explicitly refuses to centre-cut Remotion beats because it chops text mid-word |
| Ship the component source with the reel? | No | Only the beat sheet and the build documents travel to the repository; the components live in the toolkit's shared scene library, where the next fellow's reel can reuse them |

## Status

Built, compiled, and QC'd. **Not published** — the toolkit has no publishing
machinery by design, and putting this in front of an audience is a human
decision. Awaiting review.
