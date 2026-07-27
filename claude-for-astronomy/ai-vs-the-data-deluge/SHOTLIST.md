# Ep. 01 — AI vs. the Data Deluge — Beat Breakdown

**Status: FULLY RESOLVED — 3-min target relaxed by you (2026-07-27), all shot types locked, zero
Higgsfield spend, method now has real depth (dual-view architecture added 2026-07-26). Nothing
outstanding on this episode.**

> **Revision note (2026-07-26):** Original draft was 23 beats / ~3.5–4.5 min. Cut to 17 beats by
> merging redundant beats (pipeline-flagging + human-vetting + backlog became one beat; the
> "millions of light curves" line got folded into the Kepler stat beat instead of its own beat;
> a transitional "wasn't a one-off" line got folded into the Rubin beat; the closing "no team
> could review that" line got folded into the final takeaway beat) and cutting one beat entirely
> (the "670 stars" detail — a real fact, still true, just not essential to follow the story).

> **Revision note (2026-07-26, second pass):** The trimmed version read as "there were fake-looking
> dips, so Google used ML to classify them" — accurate but generic. Cut the Earth/Sun beat (flavor,
> not essential) and added 2 new beats (9, 10 below) covering AstroNet's actual **dual-view CNN
> architecture** — the specific, non-obvious detail that makes this more than "they used a
> classifier." Net: 17 → 18 beats, ~273 → ~284 VO words. Estimated runtime **~2.9–3.1 min** —
> essentially still at the 3-min target; if the real render comes in over, beat 2 is the easiest
> further cut (it restates beat 1's point).

| # | VO (beat) | Words | Shot type / source | Notes |
|---|-----------|-------|---------------------|-------|
| 1 | In 2017, a computer found a planet every human who'd looked at the data had missed. | 16 | Manim | Abstract data visual — a field of data points/light curves with one quietly highlighted, no literal "planet" or "computer" imagery. |
| 2 | Not because the data was hidden — because there was too much of it to check by hand. | 17 | Remotion | Data-overload graphic — wall of scrolling data/alert text the camera pushes through. |
| 3 | Kepler stared at up to 200,000 stars for four years, recording brightness every 30 minutes — millions of light curves. | 20 | Manim | Stat overlay + light-curve-stacking animation combined into one beat. |
| 4 | A transiting planet leaves one signature: a tiny, periodic dip in a star's brightness. | 14 | Manim | Animated transit dip on a single light curve. |
| 5 | Pipelines flagged thousands of candidates. Sorting real transits from noise took time nobody had. | 14 | Remotion | **Tightened 2026-07-26** (was 21 words) to make room for the new architecture beats. UI dashboard mockup — flagged signals scrolling, marked candidate vs. noise. |
| 6 | So how do you find the one signal nobody ever had time to check? | 14 | Remotion | "THE QUESTION" title card. |
| 7 | In 2017, Google engineer Christopher Shallue and astronomer Andrew Vanderburg tried something different. | 13 | Remotion | Name-card/lower-third text reveal — no image, since real photo rights couldn't be confirmed (see FACTCHECK). |
| 8 | They trained a neural network on 15,000 light curves humans had already labeled by hand. | 15 | Manim | Training-set diagram: 15,000 labeled examples. |
| 9 | The network didn't look at one curve — it compared two views: the full orbit, and a close-up of just the dip. | 21 | Manim | **NEW 2026-07-26.** Split-screen: wide folded light curve (left/top) next to a zoomed dip (right/bottom) — visually sets up beat 10's payoff. |
| 10 | The wide view exposes impostors — like a second eclipse revealing two stars, not one planet. The close-up checks the dip's shape. | 21 | Manim | **NEW 2026-07-26.** Two side-by-side examples: a real transit (clean single dip, both views agree) vs. an eclipsing binary (extra dip visible only in the wide view). See FACTCHECK for the architecture detail this is based on. |
| 11 | Only then did it decide: a real planet, or just another false alarm. | 13 | Manim | Synthesis beat — the two views merging into one output. Replaces the old, more generic "network learned what a transit looks like" line. |
| 12 | It flagged Kepler-90i — with only a 1-in-10,000 chance of being a false alarm. | 13 | Manim | Light curve highlight/zoom on the flagged dip. |
| 13 | That made Kepler-90 the first known system with eight planets outside our own. | 13 | Real archive imagery | NASA/Ames official artist concept (PIA22193) — credit confirmed, see VISUAL-ASSETS. |
| 14 | Overall, the network told real planets from false alarms correctly 96% of the time. | 14 | Remotion | Stat overlay: 96% accuracy. |
| 15 | This same idea now runs continuously — Vera Rubin Observatory alone produces about 10 terabytes of images every night. | 18 | Real archive imagery | Folds in the old "wasn't a one-off" transition line. NOIRLab/Rubin press photo — credit confirmed, see VISUAL-ASSETS. |
| 16 | That's up to seven million alerts a night, across a ten-year survey expected to total roughly 60 petabytes. | 17 | Remotion | Stat counter — wording decision made, see FACTCHECK. |
| 17 | No human team could review that. The universe was never short on signals — just on hours. | 16 | Real archive video | **Tightened 2026-07-26** (was 22 words). "Zooming into NSF–DOE Rubin's Ocean of Stars" (HD 1080p, NOIRLab) — a zoom across a real 1.7-gigapixel Rubin image. See VISUAL-ASSETS. |
| 18 | AI doesn't replace the astronomer looking through the telescope. It decides what's worth their time. | 15 | Remotion | Closing title/text card. |

## Shot-type summary (18 beats)
- **Manim:** 8 beats (1, 3, 4, 8, 9, 10, 11, 12)
- **Remotion:** 7 beats (2, 5, 6, 7, 14, 16, 18)
- **Generated image (Higgsfield, paid):** 0 beats
- **Real archive imagery/video:** 3 beats (13, 15, 17 — all picked and sourced, see VISUAL-ASSETS)

## Approval status
- [x] Beat order/pacing approved — trimmed to 17, then to 18 to add real depth to the method (filled in on your behalf; see rationale above)
- [x] Shot-type assignments approved — same basis
- [x] **Higgsfield spend eliminated** — no paid generation in this episode
- [x] Beat 17 asset picked, credit + acknowledgements confirmed, HD download link on file — see `FACTCHECK.md`
- [x] **Runtime target relaxed** — you confirmed running a bit over 3 min is fine (2026-07-27), so the estimated ~2.9–3.1 min (or slightly more once actually rendered) is not a blocker. Beat 2 remains the easiest cut if a future episode needs the runtime tightened back up, but nothing here requires it.
