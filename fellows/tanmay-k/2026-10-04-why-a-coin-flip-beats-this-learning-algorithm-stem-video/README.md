# Why a Coin Flip Beats This Learning Algorithm

*Why a Coin Flip Beats This Learning Algorithm.* Tanmay Kulkarni, in for Humanitarians AI · Week 25 topic video ·
built 2026-10-04

Text and code only. **The two masters live in the shared Google Drive**, not in this repository. See the links below.
The working folder (audio, clips, stills, QC frames) is outside this repo.

> **This repository copy:** the two `.mp4` masters aren't committed (video is gitignored repo-wide).
> The Short's files sit alongside the long's instead of in `short/`: `beat_sheet-short.json`,
> `FACTCHECK-SHORT.md`, `build_short_sheet.py` and the `…-short.*` captions and metadata.
> `experiment/` holds the code the film runs and links: `corridor.py`, `rps.py` and their results.

## The topic

**Chosen topic: `claude-for-education/reinforcement-learning-an-introduction`** in the
`humanitarians-youtube` repository. It's an unbuilt 10-beat auto-conversion of Humanitarians AI's
**["Reinforcement Learning: An Introduction — A Comprehensive Mapping"](https://humanitariansai.substack.com/p/reinforcement-learning-an-introduction)**
(February 2026; credited in the repo to Nik Bear Brown, Founder), a chapter-by-chapter review of
Sutton & Barto's textbook *Reinforcement Learning: An Introduction* (2nd ed., 2018).

- **The film builds on one line of that review:** that the book's short-corridor example (Example 13.1)
  shows ε-greedy action-value methods failing where policy gradient succeeds, by finding a stochastic
  policy of about 59% right. We reproduced the example, checked it against the book page by page,
  and extended it: why the best answer is random, and when it stops being.
- **Selection:** a randomized, unseeded draw over the library's singleton topics. Draw 1 of 6.
- **Uniqueness:** checked against `main` and all 54 fellow branches, read-only, on an isolated bare
  mirror; nothing in the shared repo was checked out, fetched into or modified. No fellow has built or
  extended the topic. The angle's narration was also checked against all of our Week 15–24 films.

The full draw, exclusions and uniqueness evidence are in `TOPIC-DECISION.md`, and the angle and its
boundaries are in `ANGLE.md`.

## The files

| | File | | |
|---|---|---|---|
| **Long** | `why-a-coin-flip-beats-this-learning-algorithm-final.mp4` | 3840×2160 · 24 fps · 5:03 (302.6 s) | −15.0 LUFS / −1.9 dBTP |
| **Short** | `why-a-coin-flip-beats-this-learning-algorithm-short-final.mp4` | 2160×3840 · 24 fps · 1:26 (85.9 s) | −15.0 LUFS / −1.9 dBTP |

Each film's master is on Drive (below); its captions (`.srt` and `.vtt`) and YouTube title, description, chapters
and tags (`*-youtube.md`) are in this folder. The experiments the film reports are in `experiment/`: plain Python,
standard library only, seeded, under a second each.

**Structure:**
- **Long, "THE CORRIDOR":** the book's puzzle is the set. Each chapter tries one answer to it (always
  right, always left, a button-scoring learner, a fair coin, the best biased coin, a learner that finds
  it, then sight), and every score lands on one line from B02 on. It ends with the blindfold test and
  both of its outcomes (the corridor, rock-paper-scissors), then a goalkeeper for the viewer.
- **Short, "ONE QUESTION":** its own script, not a cut of the long. One question carried through ("why
  does a coin win?"), with the blindfold test and a viewer task inside it.

## Links

Drive links added 2026-10-04. Add the YouTube URL once each film is live (replace each `<!-- YOUTUBE_LINK_… -->` placeholder).

| | Drive | YouTube |
|---|---|---|
| Long (16:9, 4K) | <!-- DRIVE_LINK_LONG --> [Drive](https://drive.google.com/file/d/1xb3JBvRdM4qaBNtZhrRZin0au_QbVT2J/view?usp=drive_link) | <!-- YOUTUBE_LINK_LONG --> *(to add)* |
| Short (9:16, 4K) | <!-- DRIVE_LINK_SHORT --> [Drive](https://drive.google.com/file/d/15Qz8jvks-h7o25QPYlvj5qVfPmmzuAQC/view?usp=drive_link) | <!-- YOUTUBE_LINK_SHORT --> *(to add)* |

**Placeholders in the descriptions:**
1. ~~`[CODE LINK]`~~ **Filled (2026-10-04):** the long's description links the published code,
   https://github.com/nikbearbrown/humanitarians-youtube/tree/tanmay-kulkarni/fellows/tanmay-k/2026-10-04-why-a-coin-flip-beats-this-learning-algorithm-stem-video/experiment. B17 says "the corridor script is linked below"; it is.
2. **`[FULL VIDEO LINK]`** in the Short's description. Swap in the long's YouTube URL once it's live, and
   set the long as the Short's related video in YouTube Studio.

## Uploading: three choices only you can make

1. **Altered or synthetic content.** The narration is a synthetic voice (Kokoro), introducing itself as
   Tanmay Kulkarni. Both descriptions say so. Whether to also tick YouTube's "altered or synthetic
   content" box is your call.
2. **Thumbnail.** Pick a custom one. B10's typeset *p*\* = 2 − √2 over the curve is the strongest frame.
3. **Captions.** Upload the `.srt` as English captions, not YouTube's auto-captions. It shows the
   written math ("2 − √2", "58.6%", "−44") where the voice says the words.

## The record

- **`FRICTIONAL.md`:** the dated process log: what was tried, where it resisted, what was done next, what
  Claude contributed and what I decided, each entry pointing at its record.
- **`FACTCHECK.md`:** A1–A25, every claim checked against the book (2nd ed., printed page numbers) or
  our runs, plus the algebra for 2 − √2. It also audits the source review's own three statistics (one
  qualified: the 19% / 27% controller figures).
- **`TOPIC-DECISION.md`**, **`ANGLE.md`:** the draw, the uniqueness checks, the angle and its boundaries.
- **`PEDAGOGY.md`:** the signed Gate P record: long form, Short, and the post-audio re-read of five
  beats after Whisper caught three sound-alike phrases (weight → "wait", too → "two", "right two" →
  "right to").
- **`READ-ALOUD.md`:** the sheet Gate P was read from.
- **`BEATS-DRAFT.md`:** the structural reasoning, the read-through logs and the 12/12 changes.
- **`PROOF-REVIEW.md`:** Reviews 1–7 and the final verdict, every defect each found and how it was fixed
  and re-checked on the frame. The final verdict:
  - both films **clear-for-public**
  - teaching rubric: long **12/12**, Short **12/12**
  - production gate PASS
  - claims on screen when spoken: **35/35** (long) and **22/22** (Short), sampled on the final files at
    each cue on the Whisper clock
  - 0 dark frames (per-frame luma scan, 9,316 frames), GATE V 0 BLOCKER / 0 MAJOR on both cuts

## Rebuilding

`beat_sheet.json` (here and in `short/`) is the source of truth, generated by `build_beat_sheet.py` /
`short/build_short_sheet.py`. Measured Kokoro audio is the clock and is never hand-repaired.

```
python3 build_beat_sheet.py                 # narration + props; cues on the Whisper clock (cue_align.py)
<toolkit>/generate_audio_kokoro.py <reel>   # only after Gate P
python3 whisper_align.py . short            # word timings + a word-by-word check of what the voice said
<toolkit>/remotion_scenes.py <reel> --only <beat> --force   # never while a sheet rebuild is running
python3 make_gate_f.py                      # SHOTLIST / PROMPTS / short FACTCHECK (GATE F)
<toolkit>/compile.py <reel> --height 2160   # 3840 for the Short
python3 pacing_pass.py <reel> --hold 0.3    # then normalise.py: two-pass loudnorm, −14 LUFS / −2 dBTP
python3 make_captions.py . 0.3              # and: python3 make_captions.py short 0.3
python3 assertion_frames.py <reel> <final.mp4> <out>   # PROOF: one frame per claim, on the final file
```

**Components.** `Corridor` and `CoinCurve` were written for this film in `brutalist.art`
(`runtime/remotion/src/scenes/`), local and uncommitted as in Week 24. Both are dual-aspect, use
absolute-second timing and have neutral defaults.
