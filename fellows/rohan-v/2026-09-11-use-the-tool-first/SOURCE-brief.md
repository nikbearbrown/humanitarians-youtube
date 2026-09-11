# SOURCE-brief — "Use the Tool First."

## What was asked for

Rohan, 2026-09-10:

> Now let's do this weeks videos. suggest 2 stem topics. I also want to make a
> video for this weeks update. This week i only worked on the midjourney
> videos. You can find all the information at
> `D:\Rohan\Claude\HAI\lyrical-literacy\youtube`
>
> This involved working on midjoruney myself, researching prompting techniques,
> taking screenshots of theinterface. planning the video.
>
> do one video for this and then one stem topic. keep it in audio. I want the
> best animations and visuals and everything should be of the best quality. aim
> for a total length of 2 mins for each video.
>
> Follow the same framework as last week. dont skip any steps.

## What it was built from

The pointer to `lyrical-literacy/youtube` was the whole brief for content —
everything on screen came from reading that directory and measuring what was
in it.

| Claim on screen | Where it came from |
|---|---|
| Six parts shipped, all 4K | `ffprobe` on `midjourney-part-{1..6}/*.mp4` |
| Per-part runtimes and 18:59 total | the same probe, summed |
| Part titles | `MIDJOURNEY-SERIES-PLAN.md` working-title table |
| The five overturned assumptions | `MIDJOURNEY-SERIES-PLAN.md` → "What the captures changed" |
| Two missing surfaces (Style Creator, video) | same document, stated explicitly |
| 29 captures | file count in `Midjourney Screenshots/` |
| 23 new components, named individually | `Mj*.tsx` in the shared Remotion kit |
| 863 lines of UI spec | `wc -l MIDJOURNEY-UI-SPEC.md` |
| Per-part beat checks and factchecks | `check_beats.py` / `FACTCHECK.md` present in all six folders |
| Signup docs still open; both tools next | Rohan's brief, first-hand |

## What the reading changed about the reel

The brief described the week as four activities: using Midjourney, researching
prompting, taking screenshots, planning. A literal reel would have given each
one a beat.

Reading the directory found a better story. `MIDJOURNEY-SERIES-PLAN.md` opens
with a section titled "What the captures changed", which lists five assumptions
the screenshots overturned and notes that two entire surfaces were missing from
the plan. That is a sharper and more honest account of the week than "I took
screenshots" — and it makes the four activities into one causal chain rather
than a list.

So the reel's spine became **the correction**, and the four brief items appear
as its inputs rather than as separate beats.

## What was deliberately excluded

- **Prompting-technique research gets no beat of its own.** It appears inside
  B02's corrections column. At 2:00 there is room for four body beats, and the
  correction earned the slot.
- **No Midjourney screenshots on screen.** The captures informed the work but
  the channel does not show screen captures; every interface is drawn in code.
- **No claim the series is perfect.** The plan records remaining capture gaps;
  they are outside the reel's scope but not contradicted by it.
- **No individuals named beyond the presenter.**
- **No "Midjourney is great / bad" framing.** The reel is about the planning
  error, not the product.
