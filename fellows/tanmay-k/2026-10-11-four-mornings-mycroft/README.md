# Four Mornings: What a Dashboard Takes on Trust

*Four Mornings: What a Dashboard Takes on Trust.* Tanmay Kulkarni, in for Humanitarians AI · Week 26 work video ·
built 2026-10-11

Text and code only. **The two masters live in the shared Google Drive**, not in this repository. See the links below.
The working folder (audio, clips, stills, QC frames) is outside this repo. The Mycroft contribution the films are about
is in the Mycroft repository: [the recipe on `main`](https://github.com/nikbearbrown/mycroft/blob/main/recipes/portfolio-price-fetcher.md)
and [the contribution's files](https://github.com/nikbearbrown/mycroft/pull/64/files) (merged as PR #64).

> **This repository copy:** the two `.mp4` masters aren't committed (video is gitignored repo-wide). The Short's files
> sit alongside the long's instead of in `short/`: `beat_sheet-short.json`, `SCRIPT-SHORT.md`, `READ-ALOUD-SHORT.md`,
> `build_short_sheet.py`, `make_read_sheet_short.py` and the `…-short.*` captions and metadata. Where the records below
> say `short/…`, read the flat name. The Gate F records (SHOTLIST, PROMPTS) and the toolkit helpers (pacing, loudness,
> portrait check, assertion frames) stay in the working folder, as in earlier work folders.

## The contribution

**[nikbearbrown/mycroft#64](https://github.com/nikbearbrown/mycroft/pull/64), merged (commit `5097a8f`).**
It closes four `[TODO: DEV]` steps in Mycroft's Portfolio Visualization Agent, in sample mode:
- provenance checks for `portfolio-price-fetcher` and `portfolio-dashboard`
- data-shape validation, which writes the record of which price each stock used
- the calculation step, rebuilt to run on test data, with a self-test that has to see its broken version
  actually run

Every fact in the films is read from files merged into `main` @ `5097a8f` (`FACTCHECK.md`, W1–W22).

## The angle

Last week's work video was also a Mycroft recipe contribution, built as three pairs that must agree. This film
takes none of that structure, and porting, parity and rounding aren't its subject. Its unit is **one morning in
the life of the person reading the dashboard**. Each act opens on the same illustrated dashboard, and one
hand-off behind it slips:
- a price of zero
- a stock the portfolio doesn't hold
- a list written twice
- a call by name

Then comes the morning it was my own check, and the same dashboard again. The audit against Weeks 15–25 and the
framing rules are in `ANGLE.md`.

## The files

| | File | | |
|---|---|---|---|
| **Long** | `four-mornings-final.mp4` | 3840×2160 · 24 fps · 3:06 (186.4 s) | −14.8 LUFS / −1.6 dBTP |
| **Short** | `four-mornings-short-final.mp4` | 2160×3840 · 24 fps · 1:53 (112.6 s) | −14.7 LUFS / −1.9 dBTP |

Each film carries its captions (`.srt` and `.vtt`) and its YouTube title, description, chapters and tags
(`*-youtube.md`) beside it.

**Structure:**
- **Long, "FOUR MORNINGS":** 10 beats. A four-box hand-off strip fills in as the film goes, each box lighting on
  the line that names its check. B07 is the turn: my own test, shown with its fix. B09 gives the viewer a task.
- **Short, *The Price That Wasn't There*:** its own script (draft 2, rewritten for context after review), one
  morning (the zero price), one arc. Who and what come first, then the idea and its question, the slip in plain
  words, two of five prices, the record as the answer, and your turn.

## Links

Add the temporary Drive links and, once live, the YouTube URLs.

| | Drive | YouTube |
|---|---|---|
| Long (16:9, 4K) | <!-- DRIVE_LINK_LONG --> *(to add)* | <!-- YOUTUBE_LINK_LONG --> *(to add)* |
| Short (9:16, 4K) | <!-- DRIVE_LINK_SHORT --> *(to add)* | <!-- YOUTUBE_LINK_SHORT --> *(to add)* |

**Placeholder in the descriptions:** `[FULL VIDEO LINK]` in the Short's description. Swap in the long's YouTube
URL once it's live, and set the long as the Short's related video in YouTube Studio.

## Uploading: three choices only you can make

1. **Altered or synthetic content.** The narration is a synthetic voice (Kokoro), introducing itself as Tanmay
   Kulkarni, and every price is invented. Both descriptions say so. Whether to also tick YouTube's "altered or
   synthetic content" box is your call.
2. **Thumbnail.** Pick a custom one. B07's struck "pass" beside "caught" is the strongest frame. B03, with two
   prices tagged "previous close", is the clearest for the Short's story.
3. **Captions.** Upload the `.srt` as English captions, not YouTube's auto-captions. They show "$65,098",
   "21%" and "590" where the voice says the words, and no name is split across two cues.

## The record

- **`FRICTIONAL.md`:** the dated process log: what was tried, where it resisted, what was done next, and who
  decided. Drafted from the records; awaiting your review.
- **`FACTCHECK.md`:** W1–W22, every claim with its evidence at `5097a8f`, plus what's left out and why.
- **`ANGLE.md`:** the approved angle, the uniqueness audit, the framing rules.
- **`SCRIPT.md`**, **`SCRIPT-SHORT.md`:** the signed scripts. The Short's file opens with the audit of
  draft 1 and what draft 2 changed.
- **`PEDAGOGY.md`:** the Gate P record (long form, the B09 line, the B02 re-read).
- **`READ-ALOUD.md`**, **`READ-ALOUD-SHORT.md`:** the sheets Gate P was read from.
- **`PROOF-REVIEW.md` → `PROOF-REVIEW-3.md`:** beat sheet → rendered beats, audio and masters → both masters
  in review. The final verdict:
  - long: production gate PASS, **12/12**
  - Short: production gate PASS, **11/12** (no in-Short test of the fix: a choice, recorded)
  - every reveal on its spoken line, checked on frames pulled from the final files: 22 (long) and 19 (Short)
  - Gate V: 0 BLOCKER / 0 MAJOR on both cuts; Shorts zones 19/19
- **Gate F records** (`SHOTLIST.md`, `PROMPTS.md`, the Short's FACTCHECK map): kept in the working folder.

## Rebuilding

`beat_sheet.json` (here and in `short/`) is the source of truth, generated by `build_beat_sheet.py` /
`short/build_short_sheet.py`. Both read the merged files from a local clone of Mycroft at `5097a8f` (read-only
`git show`). Measured Kokoro audio is the clock and is never hand-repaired. Run from the working folder
(`Week 26/work-video/`); the scripts resolve the toolkit relative to it.

```
python3 build_beat_sheet.py                     # narration + props; cues on the measured clock
/opt/homebrew/bin/python3.12 make_audio.py      # only after Gate P; Mycroft override asserted; --dir short; --only <IDs>
/opt/homebrew/bin/python3.12 align_words.py     # Whisper word times → cue clock + caption timing; --dir short
python3 build_beat_sheet.py                     # again, so cues land on the measured clock
node render_stills.mjs                          # (from brutalist.art/runtime/remotion) stills; STILLS_PLAN=<plan.json>
<toolkit>/remotion_scenes.py <reel> --only <beat> --force   # never while a sheet rebuild is running
/opt/homebrew/bin/python3.12 portrait_check.py <9:16 frames>  # Shorts zones, on pixels
python3 make_gate_f.py                          # SHOTLIST / PROMPTS / short FACTCHECK (Gate F)
/opt/homebrew/bin/python3.12 <toolkit>/compile.py <reel> --height 2160   # 3840 for the Short
python3 pacing_pass.py <reel> --hold 0.3        # reads each beat's hold_after_s; then normalise.py
python3 make_captions.py . 0.3 ; python3 make_captions.py short 0.3
python3 assertion_frames.py <reel> <final.mp4> <out>   # PROOF: one frame per reveal, on the final file
```

**Component.** `MorningDashboard` was written for this film in `brutalist.art` (`runtime/remotion/src/scenes/`),
local and uncommitted as in Weeks 24–25, and registered as `MorningDashboardOFL` and `MorningDashboardOFL916`.
It's dual-aspect, uses absolute-second timing, and keeps display text in props. Optional reveal times on rows,
compare items and hand-offs are null by default, so they change nothing unless they're set.
