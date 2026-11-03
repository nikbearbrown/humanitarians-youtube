# PROMPT — "Why Your Track Sounds Thin On A Phone"

The brief, and how each constraint was resolved.

## Constraints given

Rohan, 2026-09-15 — the week's standing brief:

> Great lets plan out 2 more videos for this week. use stem topics for both

then the production bar:

> I want beautiful animations and nice motion graphics. Take as much time as you
> need. I want everything to be visually appealing. I want to keep the viewer
> hooked. So use as many visuals as you can so that the concepts are very easy
> for the viewer to understand.

then, on tooling:

> Also are you using remotion for the motion graphics? I want these to look more
> premium and clean. Do research and search for remotion assets/libraries if any
> so that you can use them.

then, on length:

> also, dont cut video lenght. i like 2 mins. I just want it to be simple and
> easy for everyone to understand. give examples, nice motion graphics, fluid
> animations. It should look like a professionlly made video

and finally, authorising the build:

> proceed with the full build. 16x9 and 9x16. I am off to bed. I want everything
> perfect and done by morning. Make sure to QC. Also for 9x16 make sure its
> native and not just the 16x9 version squeezed down

| # | Constraint | How it was resolved |
|---|---|---|
| 1 | STEM topic, audio | Mono fold-down — chosen because it is measurable locally *and* predictable in closed form, so one of its two experiments could be predicted before being measured |
| 2 | **No assumed knowledge** | Two of five body beats (42s of 125s) spent before the mechanism: two sides and one speaker, then a door. Full vocabulary table in [PEDAGOGY.md](./PEDAGOGY.md) |
| 3 | **But the viewer must learn something** | The measured evidence stays (B03) and the honest caveat stays (B04). What was cut is the detail *inside* them, not the beats |
| 4 | ~2:00, do not cut length | **2:05.** Length was held and complexity was cut instead — four detail blocks removed, no beat dropped |
| 5 | Premium motion, researched libraries | Seven libraries wired in, not name-dropped: `remotion-bits` (`AnimatedText`, `AnimatedCounter`, `StaggeredMotion`), `@remotion/noise`, `@remotion/paths`, `@remotion/shapes`, `@remotion/motion-blur`, `@remotion/layout-utils`, `@remotion/google-fonts`. Spring constants taken from the convention across 81 professional templates |
| 6 | 16:9 and 9:16, both 4K | 3840×2160 landscape; 2160×3840 **re-rendered natively** through four purpose-written `916` siblings via THE ONDA CHECK |
| 7 | QC before calling it done | Gate V on the clean master, both orientations, plus contact sheets read frame by frame. Findings and fixes in [BUILD-LOG.md](./BUILD-LOG.md) |
| 8 | Same framework, no steps skipped | measurement → library-first search → beat sheet → audio → word clock → 4K landscape → Gate V → native portrait → Gate V → 12 docs + both QC sheets → GitHub → `./art drive` |

## Constraints inherited from earlier feedback

| Source | Rule | Applied |
|---|---|---|
| Week-01 review | identical start/end screens across reels | `ClaudeComposerAsk` opener, HAI end card |
| Week-01 review | mention Humanitarians AI in intro and outro | B00 opens with it, B06 closes with it |
| Week-02 review | name phonetic in narration only | `Row-Haan` in `narration_text`; on-screen spelling stays *Rohan V.* |
| Week-02 review | 9:16 native, never a letterbox | four `916` siblings, each re-laid out rather than scaled |
| Week-03 review | portrait cuts must not carry mojibake | both short beat sheets byte-checked; `shorts.py` UTF-8 read fixed at source |
| Week-03 build | HAI components, not the Claude-locked ones | `HaiApplyCard`, `HaiTitleOutro` |
| Standing | no personal references in narration | none |
| Standing | free by default | Fellow Tier cost **$0.00** — Kokoro, faster-whisper, Remotion, numpy, ffmpeg |
| Standing | only docs go to GitHub; mp4s go to Drive | enforced by `.gitignore` in this folder |

## What the factcheck changed

Running FACTCHECK as a gate rather than a write-up did two things here:

- **It forced the hedge on claim 13.** "Most stereo width comes from delaying one
  side" is true of the common widener designs and not of all of them, so the
  narration says *most*.
- **It made the nulls' depth a feature rather than a footnote.** The measurement
  showed about −10 dB, not −∞, for two legitimate reasons. Writing that up is
  what produced B04's title and its entire framing. A cleaner result would have
  made a worse reel, because "silence" is not the symptom anyone hears.

## What Gate V changed

The visual gate blocked the first clean master with **0 blockers and 1 major**:
B02 `underfill`, 50% against a 55% floor.

It was right. The canvas-fill law measures the **bounding box** of all ink
against the safe area, and with the wave panel keyed to `agree` (0.808) the
entire right half of that frame was empty at its own midpoint. Moving the panel
to `opposite` (0.311) fixed the gate **and** improved the teaching: the viewer
now watches the two lanes go out of phase exactly as the narration says they do,
and sees the sum lane collapse on `nomove`, instead of meeting an
already-collapsed sum at the end. Full before/after in
[BUILD-LOG.md](./BUILD-LOG.md).

The contact-sheet read caught something no gate could: in an earlier pass both
figures' arrows pointed the same way during the "pushing against each other"
state, directly contradicting the narration. That is the argument for reading
frames rather than trusting a pass.

## What was not done

- **Not published.** brutalist.art renders; it has no upload path, and none was
  improvised. The masters went to Drive; publishing is a human workflow.
- **No paid API.** No ElevenLabs, no image model, no video model.
- **No hand-patched timings.** Every reveal is bound to a measured word. Where a
  reveal looked early or late, the anchor phrase in `cues.json` was changed and
  `sync_cues.py` re-run — never a magic number typed into a component.
