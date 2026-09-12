# SOURCES — "Use the Tool First."

## Primary source

Rohan's own account of the week, given 2026-09-10:

> This week i only worked on the midjourney videos. [...] This involved working
> on midjourney myself, researching prompting techniques, taking screenshots of
> the interface. planning the video.

Reproduced in [SOURCE-brief.md](./SOURCE-brief.md). This is a progress report,
so the presenter is the primary source for what he did — but everything with a
number attached was verified independently.

## Verified by execution

Run 2026-09-10 against the actual files.

| What | How | Result |
|---|---|---|
| Six part masters exist | directory listing of `lyrical-literacy/youtube/midjourney-part-{1..6}/` | all six `.mp4` present |
| Resolution of each | `ffprobe -select_streams v:0 -show_entries stream=width,height` | 3840×2160 × 6 |
| Duration of each | `ffprobe -show_entries format=duration` | 200.30 / 196.20 / 182.42 / 203.94 / 179.23 / 176.88 s |
| Series total | arithmetic on the six | 1138.96s = 18:58.96 → **18:59** |
| Capture count | `ls "Midjourney Screenshots" \| wc -l` | **29** |
| UI spec length | `wc -l MIDJOURNEY-UI-SPEC.md` | **863** |
| New component count | `ls scenes/ \| grep -c '^Mj'` | **23** |
| Registered Mj compositions | `grep -oE 'id="Mj[A-Za-z0-9]*"' Root.tsx \| sort -u \| wc -l` | 42 |
| Per-part checks exist | `check_beats.py` and `FACTCHECK.md` presence per folder | present in all six |
| Beat narration durations | `generate_audio_kokoro.py` output | 18.97 / 22.72 / 24.43 / 23.55 / 21.93 / 10.50 s |
| Reel total | sum of the above | 122.10s = 2:02 |
| New components render | `./art scenes --check` | 3 landscape + 3 portrait, all `RENDERABLE` |

## Repository sources

| Source | Used for |
|---|---|
| `lyrical-literacy/youtube/MIDJOURNEY-SERIES-PLAN.md` | the five overturned assumptions (its "What the captures changed" table), part working titles |
| `lyrical-literacy/youtube/MIDJOURNEY-UI-SPEC.md` | spec line count; the record of what the captures established |
| `lyrical-literacy/youtube/midjourney-part-{1..6}/` | the masters themselves, and the per-part check scripts |
| `RohanClaudeHAIbrutalist.art/runtime/remotion/src/scenes/Mj*.tsx` | the component names shown as chips in B03 |
| `RohanClaudeHAIbrutalist.art/runtime/scripts/shorts.py` | THE ONDA CHECK — portrait rewiring |

## Two upstream inconsistencies, and how they were handled

**The plan document contradicts itself on capture count.** Its header says
"23 captures, all read directly"; a later line says "29 captures". The
directory holds 29 files. The reel uses 29.

**The plan document says 18:58; the reel says 18:59.** Both describe
1138.96s — truncated versus rounded. The reel rounds, per the convention fixed
in week-02.

Both are recorded in [FACTCHECK.md](./FACTCHECK.md). The pattern is now
familiar enough to state as a rule: **planning documents drift, so measure
instead of quoting.** The same thing happened with the Suno runtimes in
week-02.

## Not used

- No external web sources. Every number came from a command run locally.
- No screen recordings, of Midjourney or anything else.
- No AI-generated video or audio beyond Kokoro narration.
- No individuals named beyond the presenter.
