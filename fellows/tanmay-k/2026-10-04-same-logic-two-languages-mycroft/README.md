# Same Logic, Two Languages

*Same Logic, Two Languages.* Tanmay Kulkarni, in for Humanitarians AI · Week 25 work video · built 2026-10-04

Text and code only. **The two masters live in the shared Google Drive**, not in this repository. See the links below.
The working folder (audio, clips, stills, QC frames) is outside this repo. The Mycroft recipe contribution the films are
about is in the Mycroft repository: [the recipe on `main`](https://github.com/nikbearbrown/mycroft/blob/main/recipes/contradiction-detection-agent.md)
and [the contribution's files](https://github.com/nikbearbrown/mycroft/pull/60/files) (merged as PR #60).

## The work

This week's work is a contribution to **Mycroft** (`nikbearbrown/mycroft`), which describes itself as "both a book
and a working agentic repository" for finance. I took one recipe,
[`contradiction-detection-agent`](https://github.com/nikbearbrown/mycroft/blob/main/recipes/contradiction-detection-agent.md),
and made it run on sample data: the six step scripts it names, a Python port of its detector checked against the
original workflow's JavaScript, a frozen sample corpus of invented companies, gate tests that can fail, a recorded
self-test and the human gate decisions that take it to `RUNNABLE-SAMPLE`. The full account, with every file, check
and decision, is in the Mycroft repository: [the recipe page](https://github.com/nikbearbrown/mycroft/blob/main/recipes/contradiction-detection-agent.md) (its status basis, steps, gates and *Notes from
porting*) and [the recorded self-test](https://github.com/nikbearbrown/mycroft/blob/main/logs/contradiction-detection-agent/self-test-results.md).

The film is about one question from that work: **I rewrote it in Python. How do I know it still says the same
thing?** Its answer: two versions agreeing only counts where they had a chance to disagree, so find where they could
differ, and put a test exactly there.

## The files

| | File | | |
|---|---|---|---|
| **Long** | `same-logic-two-languages-final.mp4` | 3840×2160 · 24 fps · 4:31 (270.9 s) | −14.1 LUFS / −2.2 dBTP |
| **Short** | `same-logic-two-languages-short-final.mp4` | 2160×3840 · 24 fps · 2:20 (140.1 s) | −14.2 LUFS / −2.4 dBTP |

Each film's master is on Drive (below); its captions (`.srt` and `.vtt`) and YouTube title, description, chapters and
tags (`*-youtube.md`) are in this folder.

**Structure:**
- **Long, "THREE MATCHES":** two columns throughout, the original JavaScript and my Python. It opens on one number
  with two answers (0.625 → "0.63" in JavaScript, "0.62" in Python), then walks three matches: my reading against
  the original (answers written before any code), my Python against the original JavaScript (16/16, and why that
  told me almost nothing until two companies stood exactly on the line), and my report against my own log. It ends on
  where I stopped (sample data only, live mode declined) and one question for the viewer.
- **Short, "ONE TABLE":** its own script, not a cut of the long, and complete on its own: what Mycroft and the
  detector are, the answers first, 16/16, my own changes going unnoticed, two companies placed on the line, the
  limits, and the question.

## Links

Drive links added 2026-10-04. Add the YouTube URL once each film is live (replace each `<!-- YOUTUBE_LINK_… -->` placeholder).

| | Drive | YouTube |
|---|---|---|
| Long (16:9, 4K) | <!-- DRIVE_LINK_LONG --> [Drive](https://drive.google.com/file/d/10VVcDmb82JM3uILcM0c_SnX2sONAYkl5/view?usp=drive_link) | <!-- YOUTUBE_LINK_LONG --> *(to add)* |
| Short (9:16, 4K) | <!-- DRIVE_LINK_SHORT --> [Drive](https://drive.google.com/file/d/1rUCpSdo6kpppGXKIWAijkPH5pJlAYbY7/view?usp=drive_link) | <!-- YOUTUBE_LINK_SHORT --> *(to add)* |
| Recipe (Mycroft) | [`recipes/contradiction-detection-agent.md`](https://github.com/nikbearbrown/mycroft/blob/main/recipes/contradiction-detection-agent.md) | — |

**Placeholder in the descriptions:** `[FULL VIDEO LINK]` in the Short's description. Swap in the long's YouTube URL
once it's live, and set the long as the Short's related video in YouTube Studio. Both descriptions link the recipe on
Mycroft's `main` branch.

## Uploading: three choices only you can make

1. **Altered or synthetic content.** The narration is a synthetic voice (Kokoro), introducing itself as Tanmay
   Kulkarni. Both descriptions say so. Whether to also tick YouTube's "altered or synthetic content" box is your call.
2. **Thumbnail.** Pick a custom one. B01's two columns, "0.63" ≠ "0.62", is the strongest frame.
3. **Captions.** Upload the `.srt` as English captions, not YouTube's auto-captions. They show "0.625", "0.61" and
   "Mycroft" where the voice says the words (the narration respells Mycroft as "My-croft" so the voice says it right).

## The record

- **`ANGLE.md`:** the approved angle, its structure, and its uniqueness audit against every earlier work video
  (W15–W24).
- **`SCRIPT.md`**, **`SCRIPT-SHORT.md`:** the narration, with on-screen notes and fact-check references per beat.
- **`FACTCHECK.md`:** every claim (live runs in Node and Python, or a committed Mycroft file); the Short claims nothing
  the long doesn't.
- **`PEDAGOGY.md`:** the verdict log: Gate P for both scripts (verbatim), audio locks, the B11 line removed at your
  request, and every review.
- **`READ-ALOUD.md`**, **`READ-ALOUD-SHORT.md`:** the sheets Gate P was read from, with Kokoro's own phonemes.
- **`PROOF-REVIEW.md`:** every review and what it found: pre-production (5 fixes), the stills in both formats (8),
  the Short's stills and cuts (7), both masters, and the **final verdict**:
  - both films **clear to publish**
  - teaching rubric: long **12/12**, Short **12/12**
  - GATE V 0 BLOCKER / 0 MAJOR on both; 0 dark frames (9,853 frames scanned)
  - claims on screen when spoken: 41 frames (long), 44 incl. every cut (Short), sampled on the final files
  - captions rebuilt on the word clock after the final review caught them drifting from the voice
- **Visuals:** every beat is a code-drawn Remotion scene; no AI imagery, no
  third-party images, open-licence fonts only.

## Rebuilding

`beat_sheet.json` / `beat_sheet-short.json` are the source of truth: narration from `SCRIPT.md` / `SCRIPT-SHORT.md`
(`script_to_sheet.py`), scene props and cues from `build_beat_sheet.py` / `build_short_sheet.py`. Measured Kokoro audio
is the clock; cues resolve on the word clock (`mp3/words.json`, from the toolkit's `align.py`). Captions were built
on the same clock by `make_captions_words.py` (display forms from `make_captions.py`). In the working folder the
Short's files sit in `short/` under their plain names; the scripts expect that layout. The audio, render, pacing and
loudness steps use the `brutalist.art` toolkit.

**Scene.** `TwoLanguages` was written for this film in `brutalist.art` (`runtime/remotion/src/scenes/`,
registered as `TwoLanguagesOFL` / `TwoLanguagesOFL916`), local and uncommitted as in Weeks 24 and 25. It's
dual-aspect, uses absolute-second timing, and every string is a prop.
