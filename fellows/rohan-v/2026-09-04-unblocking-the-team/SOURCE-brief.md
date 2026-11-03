# SOURCE-brief — "Unblocking the Team."

## What was asked for

Rohan's brief, 2026-08-29, for the first of two videos in the week-02 submission:

> The first video will be a progress update that I am sharing. At the start of
> the week, I gave a quick workshop on how to use brutalist to members on the
> marketing team because they were having trouble with this especially the part
> where they had to upload the code to github. They are all non technical and
> creative people so this was a blocker for them and since I had figured it out
> I helped them. I also created a brutalist video on how to setup brutalist
> using an AI first approach [...] I also submitted this video as part of last
> weeks submission.
>
> This week I worked on creating the suno tutorial videos that will be used in
> training the new members of our team [...] I am also in the process of
> creating written documentation for the whole signup process covering discord,
> suno, midjourney and adobe creative cloud. This will be an essential resource
> for incoming fellows.
>
> This took up the major part of my week. I am going to soon start working on
> the Midjourney series soon and will be done with those by next week. [...]
> Aim for a total length of 2 mins

Plus the standing weekly constraints: 16:9 and 9:16, both 4K.

## What it was built from

| Claim on screen | Where it came from |
|---|---|
| Suno series is 3 parts, all finished | `D:\Rohan\Claude\HAI\lyrical-literacy\youtube\suno-part-{1,2,3}\` — all three `.mp4` present |
| Per-part runtimes (3:57 / 3:09 / 3:29) | `ffprobe` on each master, run 2026-08-29 |
| Total 10:35 | sum of the three probed durations = 634.70s |
| All three at 4K | `ffprobe` stream dimensions = 3840×2160 on all three |
| Part titles and core skills | `D:\Rohan\Claude\HAI\lyrical-literacy\SERIES-PLAN.md`, series structure table |
| "Rebuilt in code, not screen-recorded" | `SERIES-PLAN.md` format standards: "No screenshots — all UI is programmatic Remotion" |
| The GitHub blocker, the workshop | Rohan's brief above (first-hand account) |
| The agent-first walkthrough video exists | `youtube/week-01/2026-08-28-agent-first-brutalist/`, submitted in the week-01 packet |
| Four signup accounts | Rohan's brief above |
| Signup guide status = IN PROGRESS | No document on disk as of 2026-08-29; labelled in-progress rather than shipped |
| Midjourney series, end of next week | Rohan's brief above — a stated commitment, framed as such |

## What was deliberately excluded

- **No individuals named.** The brief describes helping specific colleagues; the
  reel says "our marketing team" and names no one but the presenter.
- **No Pro-access or perk framing.** Carried over from the standing Suno series
  rule — this is internal reporting, not a pitch.
- **No claim the signup guide is finished.** It is not. B03 and B04 both stamp it
  `IN PROGRESS`.
- **No forward-dated work presented as done.** The Midjourney series sits on the
  dashed side of the B04 timeline, behind the NOW pin.
