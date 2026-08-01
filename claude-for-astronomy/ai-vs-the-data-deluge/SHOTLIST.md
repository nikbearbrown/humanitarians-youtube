# Ep. 01 — AI vs. the Data Deluge — Beat Breakdown

**Status: FULLY RESOLVED — 3-min target relaxed by you (2026-07-27), all shot types locked, zero
Higgsfield spend, method now has real depth (dual-view architecture added 2026-07-26). A
presenter self-introduction beat was added 2026-08-01 (new beat 2). Nothing outstanding on this
episode.**

> **Revision note (2026-07-26):** Original draft was 23 beats / ~3.5–4.5 min. Cut to 17 beats by
> merging redundant beats (pipeline-flagging + human-vetting + backlog became one beat; the
> "millions of light curves" line got folded into the Kepler stat beat instead of its own beat;
> a transitional "wasn't a one-off" line got folded into the Rubin beat; the closing "no team
> could review that" line got folded into the final takeaway beat) and cutting one beat entirely
> (the "670 stars" detail — a real fact, still true, just not essential to follow the story).

> **Revision note (2026-07-26, second pass):** The trimmed version read as "there were fake-looking
> dips, so Google used ML to classify them" — accurate but generic. Cut the Earth/Sun beat (flavor,
> not essential) and added 2 new beats (9, 10 in that numbering) covering AstroNet's actual
> **dual-view CNN architecture** — the specific, non-obvious detail that makes this more than "they
> used a classifier." Net: 17 → 18 beats, ~273 → ~284 VO words. Estimated runtime **~2.9–3.1 min**.

> **Revision note (2026-08-01, third pass):** Inserted a new presenter self-introduction /
> executive-summary beat as beat 2, right after the B01 cold open — every beat from the previous
> pass's beat 2 onward shifted up by one (old 2→3, old 3→4, … old 18→19). Net: 18 → 19 beats. All
> narration audio regenerated fresh (Kokoro `af_heart`) for all 19 beats.

> **Revision note (2026-08-01, fourth pass):** Swapped beats 1 and 2 so the presenter
> self-introduction now opens the film, immediately followed by the cold-open hook. Only the
> order changed — narration text, shot types, and rendered assets for both beats are unchanged
> from the third pass, just reassigned to the other slot. No other beat affected.

| # | VO (beat) | Words | Shot type / source | Notes |
|---|-----------|-------|---------------------|-------|
| 1 | Hi, I'm Om Mali. This video is about how AI helps astronomers find real signals hidden inside far more data than any human team could ever check by hand. | 27 | Remotion | Presenter self-introduction / executive-summary card (SlateCard pattern, eyebrow "WELCOME"). Not a factual claim — see FACTCHECK.md. Moved to beat 1, 2026-08-01 fourth pass. |
| 2 | In 2017, a computer found a planet every human who'd looked at the data had missed. | 16 | Manim | Abstract data visual — a field of data points/light curves with one quietly highlighted, no literal "planet" or "computer" imagery. Moved to beat 2, 2026-08-01 fourth pass. |
| 3 | Not because the data was hidden — because there was too much of it to check by hand. | 17 | Remotion | Data-overload graphic — wall of scrolling data/alert text the camera pushes through. |
| 4 | Kepler stared at up to 200,000 stars for four years, recording brightness every 30 minutes — millions of light curves. | 20 | Manim | Stat overlay + light-curve-stacking animation combined into one beat. |
| 5 | A transiting planet leaves one signature: a tiny, periodic dip in a star's brightness. | 14 | Manim | Animated transit dip on a single light curve. |
| 6 | Pipelines flagged thousands of candidates. Sorting real transits from noise took time nobody had. | 14 | Remotion | UI dashboard mockup — flagged signals scrolling, marked candidate vs. noise. |
| 7 | So how do you find the one signal nobody ever had time to check? | 14 | Remotion | "THE QUESTION" title card. |
| 8 | In 2017, Google engineer Christopher Shallue and astronomer Andrew Vanderburg tried something different. | 13 | Remotion | Name-card/lower-third text reveal — no image, since real photo rights couldn't be confirmed (see FACTCHECK). |
| 9 | They trained a neural network on 15,000 light curves humans had already labeled by hand. | 15 | Manim | Training-set diagram: 15,000 labeled examples. |
| 10 | The network didn't look at one curve — it compared two views: the full orbit, and a close-up of just the dip. | 21 | Manim | Split-screen: wide folded light curve (left/top) next to a zoomed dip (right/bottom) — visually sets up beat 11's payoff. |
| 11 | The wide view exposes impostors — like a second eclipse revealing two stars, not one planet. The close-up checks the dip's shape. | 21 | Manim | Two side-by-side examples: a real transit (clean single dip, both views agree) vs. an eclipsing binary (extra dip visible only in the wide view). See FACTCHECK for the architecture detail this is based on. |
| 12 | Only then did it decide: a real planet, or just another false alarm. | 13 | Manim | Synthesis beat — the two views merging into one output. |
| 13 | It flagged Kepler-90i — with only a 1-in-10,000 chance of being a false alarm. | 13 | Manim | Light curve highlight/zoom on the flagged dip. |
| 14 | That made Kepler-90 the first known system with eight planets outside our own. | 13 | Real archive imagery | NASA/Ames official artist concept (PIA22193) — credit confirmed, see VISUAL-ASSETS. |
| 15 | Overall, the network told real planets from false alarms correctly 96% of the time. | 14 | Remotion | Stat overlay: 96% accuracy. |
| 16 | This same idea now runs continuously — Vera Rubin Observatory alone produces about 10 terabytes of images every night. | 18 | Real archive imagery | Folds in the old "wasn't a one-off" transition line. NOIRLab/Rubin press photo — credit confirmed, see VISUAL-ASSETS. |
| 17 | That's up to seven million alerts a night, across a ten-year survey expected to total roughly 60 petabytes. | 17 | Remotion | Stat counter — wording decision made, see FACTCHECK. |
| 18 | No human team could review that. The universe was never short on signals — just on hours. | 16 | Real archive video | "Zooming into NSF–DOE Rubin's Ocean of Stars" (HD 1080p, NOIRLab) — a zoom across a real 1.7-gigapixel Rubin image. See VISUAL-ASSETS. |
| 19 | AI doesn't replace the astronomer looking through the telescope. It decides what's worth their time. | 15 | Remotion | Closing title/text card. |

## Shot-type summary (19 beats)
- **Manim:** 8 beats (1, 4, 5, 9, 10, 11, 12, 13)
- **Remotion:** 8 beats (2, 3, 6, 7, 8, 15, 17, 19)
- **Generated image (Higgsfield, paid):** 0 beats
- **Real archive imagery/video:** 3 beats (14, 16, 18 — all picked and sourced, see VISUAL-ASSETS)

## Approval status
- [x] Beat order/pacing approved — trimmed to 17, then to 18 to add real depth to the method, then
  to 19 to add a presenter self-introduction beat (filled in on your behalf; see rationale above)
- [x] Shot-type assignments approved — same basis
- [x] **Higgsfield spend eliminated** — no paid generation in this episode
- [x] Beat 18 asset picked, credit + acknowledgements confirmed, HD download link on file — see `FACTCHECK.md`
- [x] **Runtime target relaxed** — you confirmed running a bit over 3 min is fine (2026-07-27), so
  the estimated runtime (or slightly more once actually rendered) is not a blocker.
