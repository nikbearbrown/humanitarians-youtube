# Ep. 02 — Exoplanet Hunting — Beat Breakdown

**Status: BUILT — 4K master rendered 2026-08-01.** Second episode of the "AI in Astronomy & Space
Science" series (see `weekly_stem_videos/ideas.md`, topic 02). Every claim below is sourced in
`FACTCHECK.md`.

Rebuilt 2026-08-01: a new presenter self-introduction/executive-summary beat was inserted as B02
(right after the B01 cold open), pushing every former B02-B19 beat up by one to B03-B20. This
mirrors the same insertion made for Ep.01 (`ai-vs-the-data-deluge`) for series consistency — same
"WELCOME" eyebrow convention, same headline pattern ("Hi, I'm Om Mali."). No other beat's content
changed.

Rebuilt again 2026-08-01 (second pass): swapped beats 1 and 2 so the presenter self-introduction
now opens the film, immediately followed by the cold-open hook — mirrors the same swap made for
Ep.01. Only the order changed; narration text, shot types, and rendered assets for both beats are
unchanged, just reassigned to the other slot. No other beat affected.

> **Why this isn't a Kepler-90i repeat:** Ep.01's README explicitly flagged that a follow-up
> episode should "go deeper (false-positive types, how the training set was built, other
> confirmed finds) rather than repeating the same anecdote." This episode does exactly that: it
> covers the three false-positive types Ep.01 never named, and centers on a different system
> (NASA's ExoMiner, 2021) with a different, more advanced mechanism — separate, explainable
> diagnostic-test branches instead of AstroNet's two-view (global/local) split.

| # | VO (beat) | Words | Shot type / source | Notes |
|---|-----------|-------|---------------------|-------|
| 1 | Hi, I'm Om Mali. This video is about how NASA built an AI system that explains exactly why it thinks a signal is a real planet, instead of just giving a yes or no answer. | 30 | Remotion | Presenter self-introduction / executive-summary card. WELCOME eyebrow, "Hi, I'm Om Mali." headline. Not a factual claim beat — see FACTCHECK.md. Moved to beat 1, 2026-08-01 second pass. |
| 2 | By 2021, thousands of Kepler's flagged 'maybe' signals were still sitting unconfirmed. | 12 | Manim | Dense grid of small light-curve tiles, all muted — a "backlog," nothing highlighted yet. Moved to beat 2, 2026-08-01 second pass. |
| 3 | Not because anyone missed them. It's because 'maybe' takes real proof to become 'yes.' | 14 | Remotion | COLD OPEN title/thesis card. |
| 4 | A dip in a star's brightness can come from three different impostors. It doesn't have to be a planet. | 19 | Manim | One light curve with a dip, three branch-lines fanning to three (as-yet unlabeled) icons. |
| 5 | The first impostor is an eclipsing binary. That's a pair of two stars orbiting each other, and when one passes in front of the other, it creates a dip that looks just like a planet crossing a single star. | 39 | Manim | Two-star icon eclipsing; curve shows the matching dip plus a faint secondary dip. |
| 6 | The second impostor is stellar variability. That's when a star dims on its own, with no planet or companion star involved, often because of starspots or flares. | 27 | Manim | Single star, irregular jittery brightness curve — no clean periodic dip. |
| 7 | The third impostor isn't a real signal at all. It's an instrumental artifact caused by the camera itself. | 18 | Manim | Sharp, jagged glitch-style dip in a visibly different (angular) line style. |
| 8 | Three impostors, one signal. Telling them apart took specialist time nobody had to spare. | 14 | Remotion | Act-closing summary card, closes THE PROBLEM. |
| 9 | In 2021, NASA's Ames Research Center built a different kind of classifier called ExoMiner. | 14 | Remotion | THE TURN name/org card — text only, no photo (see FACTCHECK for why). |
| 10 | It doesn't just scan the light curve. It runs the same diagnostic tests a human vetter would. | 17 | Manim | One curve splitting into parallel branch-lines, each ending in an empty checkbox. |
| 11 | Each test becomes its own branch of the network, checked separately before anything is decided. | 15 | Manim | Same branch diagram, now labeled: centroid / odd-even / secondary eclipse. |
| 12 | One branch checks the centroid. It asks whether the dip's light really comes from this star, or from a neighboring star sneaking in. | 23 | Manim | Target star + faint neighbor; centroid marker shifts toward neighbor during the dip (CRIMSON flag). |
| 13 | Another branch compares odd numbered and even numbered transits. A real planet repeats identically every time, but an eclipsing binary often doesn't. | 22 | Manim | Two stacked mini-panels: "odd transits" vs "even transits," matched (TEAL) vs mismatched (CRIMSON) depths. |
| 14 | A third branch hunts for a second, shallower dip. That's the signature of a hidden stellar companion. | 17 | Manim | Full-orbit folded curve; primary dip + small secondary dip, secondary ringed in CRIMSON. |
| 15 | Only after every branch reports back does the network merge them into one explainable verdict. | 15 | Manim | Synthesis: three branch chips feed one merge node, which outputs a single verdict chip. |
| 16 | At 99% precision, it recovered 93.6% of real planets. The previous best classifier caught just 76.3%. | 16 | Remotion | Stat overlay: precision/recall comparison vs. prior best classifier. |
| 17 | In a single pass through Kepler's unconfirmed backlog, it validated 301 new exoplanets at once. | 15 | Remotion | Stat overlay: 301-planet batch validation. |
| 18 | By 2026, the same diagnostic branch design was extended as ExoMiner Plus Plus, and it was screening TESS's ongoing candidate stream too. | 22 | Remotion | SCALING UP transition card. |
| 19 | It flagged 7,330 likely planets among more than 147,000 unconfirmed TESS signals. | 12 | Remotion | Stat counter. |
| 20 | This AI doesn't just say yes or no anymore. It shows exactly which test convinced it. | 16 | Remotion | Closing title/text card. |

## Shot-type summary (20 beats)
- **Manim:** 11 beats (1, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15)
- **Remotion:** 9 beats (2, 3, 8, 9, 16, 17, 18, 19, 20)
- **Generated image (Higgsfield, paid):** 0 beats — none drafted or planned; see `PROMPTS.md`.
- **Real archive imagery/video:** 0 beats — by design; see `FACTCHECK.md` "Resolved decisions."

## Approval status
- [x] Beat order/pacing approved (mirrors the same intro-beat insertion already approved and
      built for Ep.01)
- [x] Shot-type assignments approved
- [x] Runtime measured: 149.97s (~2:30) actual Kokoro `af_heart` audio, 4K (3840x2160) master
      rendered 2026-08-01 as `claude-for-astronomy_OmMali_01_08_2026.mp4`
- [x] `FACTCHECK.md` claims reviewed and signed off
- [x] Kokoro audio generation complete (Gate P — see `PEDAGOGY.md`)
