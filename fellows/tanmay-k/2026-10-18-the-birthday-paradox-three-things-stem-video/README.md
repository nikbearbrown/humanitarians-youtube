# The Birthday Paradox: Three Things You Could Change

*The Birthday Paradox: Three Things You Could Change* and its Short, *Take Away Days*. Tanmay Kulkarni, in for Humanitarians AI ·
Week 27 topic video · built 2026-10-16 and 2026-10-17

Text and code only. **The two masters live in the shared Google Drive**, not in this repository. See the links below.
The working folder (audio, motion states, frames, stills, QC frames and the two source CSVs) is outside this repo.

> **This repository copy:** the two `.mp4` masters aren't committed (video is gitignored repo-wide), and neither are the audio,
> the rendered frames, stills and motion states, or the two births CSVs (see *Rebuilding* for where they come from). The Short's
> files sit alongside the long's instead of in `short/`: `SHORT-SCRIPT.md`, `beat_sheet-short.json`, `FACTCHECK-SHORT.md`,
> `SHOTLIST-SHORT.md`, `READ-ALOUD-SHORT.md`, `PROOF-REVIEW-SHORT.md`, `GATE-P-SIGNOFF-SHORT.md`, `SIGNED-NARRATION-SHORT.json`,
> `proof_short_output.txt`, the Short's scripts (`build_short.py`, `make_audio_short.py`, `compile_short.py`, `proof_short.py`,
> `build_short_sheet.py`, `make_read_sheet_short.py`) and the `…-short.*` captions and metadata. Where the records below say
> `short/…`, read the flat name. There is no `PROMPTS.md` because nothing here is generated imagery; every
> slate is drawn in code. Where a record mentions `_stills/`, `_qc/`, `_motion/` or `mp3/`, those folders are in the working
> folder only.

## The topic

**Chosen topic: `claude-for-video-production/birthday-paradox`** in the `humanitarians-youtube` repository (a new topic
name; the folder did not exist before this one).

- **Selection:** a seeded draw in three stages, all of it recorded. The category pool was the 22 `claude-for-<topic>`
  collections. Seed 20261016 drew `claude-for-cancer`, which Tanmay asked to redraw; seed 27 drew
  `claude-for-video-production`. Ten counterintuitive-statistics subjects were then checked inside it (four already taken);
  seed 2701 drew the birthday paradox from the six free ones.
- **Uniqueness:** checked against all 65 local branch and remote-tracking refs, read-only (`git for-each-ref`, `ls-tree`,
  `cat-file`): one pass over 56,521 text files for the name and for the ideas (pair counting, collisions, a
  square-root-of-slots rule), with a control search to show the scan works. **0 hits.** Nothing in the shared repo was checked
  out, fetched into or modified. The refs are as last fetched locally. The one device overlap found during review
  (`vox-prediction-lock`, a written prediction before each result) led to a restructure; the film no longer uses it.
- **Our own weeks:** Weeks 15 to 26 narration and beat sheets were searched for the same ideas: no use.

The draw, exclusions and uniqueness evidence are in `DRAW.md`, `CANDIDATES.md` and `TOPIC-DECISION.md`; the angle and its
boundaries are in `ANGLE.md`.

## The film

| | File | | |
|---|---|---|---|
| **Long** | `the-birthday-paradox-three-things.mp4` | 3840×2160 · 30 fps · 4:49 (289.1 s) | −14.7 LUFS / −1.8 dBTP |
| **Short** | `the-birthday-paradox-three-things-short.mp4` | 2160×3840 · 30 fps · 0:47 (47.0 s) | −14.4 LUFS / −1.5 dBTP |

Each film carries its captions (`.srt` and `.vtt`) and its YouTube title, description and tags (`*-youtube.md`; chapters for the long)
beside it.

**Structure: THREE THINGS YOU COULD CHANGE.** The chapters are the problem's own three parameters: how many people, how
uneven the days are, how many days there are. Each is changed once and the odds read off. One moves them as expected (12% to
99%), one barely moves them (50.7% to 50.8%), one decides almost everything (50.8% to 95.4%). The film then turns that into a
rule the viewer can use, people for even odds ≈ round(1.2 × √days + ½), applies it to a case it never ran (birth months),
and hands the viewer a second (a number from 1 to 50) with an 8 s hold before the answer.

**Short, "ONE GRID THAT SQUEEZES":** its own script, written fresh for a viewer who never sees the long film, and one scene that never
cuts. A calendar of possible birthdays holds 23 dots. The narration takes days away, the calendar narrows around the same dots and the
odds climb (50.7%, then 95.4%, then above 99.99%), the rule is typeset step by step, and the calendar widens again so the loop closes
on the opening state (a year, twenty three people). It carries its own context (who, the claim, why, the rule), reads with the sound off
(a headline per phase), stays inside the Shorts safe area, and ends by giving the long film's exact searchable title.

**Sources:** US federal births-by-day counts (NCHS 1994 to 2003; SSA 2000 to 2014) as redistributed in the
`fivethirtyeight/data` repository (`births/`), plus our own simulations and exact calculations. No third-party images, no
named individuals, no political content.

## Links

Add the temporary Drive links and, once live, the YouTube URLs.

| | Drive | YouTube |
|---|---|---|
| Long (16:9, 4K) | <!-- DRIVE_LINK_LONG --> *(to add)* | <!-- YOUTUBE_LINK_LONG --> *(to add)* |
| Short (9:16, 4K) | <!-- DRIVE_LINK_SHORT --> *(to add)* | <!-- YOUTUBE_LINK_SHORT --> *(to add)* |

**Placeholder in the Short's description:** `[FULL VIDEO LINK]`. Swap in the long's YouTube URL once it's live, and set the long as the
Short's related video in YouTube Studio (the Short's closing text also gives the exact title to search for).
## Before public: one open condition

**The births data licence.** The `births/` folder of `fivethirtyeight/data` states no terms of its own. The repository's
top-level `LICENSE` is CC BY 4.0, and the underlying numbers are US government statistics. The description carries the
credit line ("Births data: US NCHS and SSA via FiveThirtyEight (CC BY 4.0)") and the film shows it on screen at B06 and in the
end card. If you want certainty beyond that, confirm with FiveThirtyEight's data policy; nothing else in the film depends on it
(the uniform-days results, the rule and the window results are our own calculations).

## Uploading: three choices only you can make

1. **Altered or synthetic content.** The narration is a synthetic voice (Kokoro), introducing itself as Tanmay Kulkarni. The
   description says so. Whether to also tick YouTube's "altered or synthetic content" box is your call.
2. **Thumbnail.** Pick a custom one. B09's band of 90 days with "95.4%" is the strongest single frame; B13's rule with its
   check marks is the most distinctive.
3. **Captions.** Upload each `.srt` as English captions, not YouTube's auto-captions. The cues are the narration exactly as
   signed at Gate P, so numbers are spelled out ("fifty point seven percent"), not shown as digits; the figures themselves
   are on screen throughout.
4. **The Short's thumbnail and link.** The strongest single frame is at 18.0 s (95.4% on the narrowed calendar); the most distinctive
   is at about 38 s (the rule). Once the long film is public, set it as the Short's related video and put its URL in the Short's
   description.

## The record

- **`FRICTIONAL.md`:** the dated process log: what was tried, where it resisted, what was done next, and who decided. Drafted
  from the records; awaiting your review.
- **`FACTCHECK.md`:** every spoken figure traced to the result files, with sources, licences and the claims that need care
  (`FACTCHECK-v1.md` is draft 1's table).
- **`RESULTS.md`:** the match-rate results, clustered-window results and the licence note.
- **`TOPIC-DECISION.md`**, **`DRAW.md`**, **`CANDIDATES.md`**, **`ANGLE.md`:** the draw, the uniqueness checks, the angle audit and
  its boundaries.
- **`PEDAGOGY.md`**, **`GATE-P-SIGNOFF.md`:** the signed Gate P record (draft 1, then draft 2).
- **`READ-ALOUD.md`:** the sheet Gate P was read from for draft 2 (`READ-ALOUD-v1-signed.md` is draft 1's).
- **`PHONEMES-CHECK.md`:** Kokoro's phonemes for the names and numbers; no overrides needed.
- **`BEATS-DRAFT.md`:** the structure, tone arc, differentiation audit and open items (`BEATS-DRAFT-v1-gateP-signed.md` is
  draft 1).
- **`SHOTLIST.md`**, **`beat_sheet.json`:** what is on screen at each beat, the measured audio clock and every reveal cue.
- **`PROOF-REVIEW.md` → `PROOF-REVIEW-STILLS.md` → `PROOF-REVIEW-CUT.md`:** beat sheet → stills → compiled master. The final
  verdict: teaching **12/12**, production gate **PASS**; 84 reveals on cue; every spoken figure on screen when spoken; the
  8 s hold measured at 8.69 s; no black frames; no gaps inside narration.
- **The Short:** `SHORT-SCRIPT.md` (the script and its layout rules), `READ-ALOUD-SHORT.md`, `GATE-P-SIGNOFF-SHORT.md` and
  `SIGNED-NARRATION-SHORT.json` (Gate P, read twice), `FACTCHECK-SHORT.md`, `SHOTLIST-SHORT.md`, `beat_sheet-short.json`, and
  **`PROOF-REVIEW-SHORT.md`**: the Shorts-specific criteria (hook, standalone context, one arc, phone legibility, pace, trailer
  function, plus an 11-point production gate), scored at plan stage (10/12, then 12/12) and on the compiled master. The final
  verdict: rubric **12/12**, production gate **12/12 checks pass** (2160×3840; ink between 13.5% and 74.9% of the height; type ≥ 30 px;
  no cut above 2.33 grey levels; longest static stretch 2.57 s; loop-friendly last frame; −14.6 LUFS).
- **`STILLS-QC.md`:** how the stills were built, checked and fixed, and what was not covered.
- **`proof_cut_output.txt`:** the raw output of the cut's mechanical checks.

## Rebuilding

`BEATS-DRAFT.md` holds the signed narration and the on-screen description; `build_beat_sheet.py` turns it, the measured audio
and the reveal cues into `beat_sheet.json`. Measured Kokoro audio is the clock and is never hand-repaired. Run from the working
folder (`Week 27/topic-video/`).

The two births CSVs are **not** committed. Download them into `data/` from the `fivethirtyeight/data` repository
(`births/US_births_1994-2003_CDC_NCHS.csv`, `births/US_births_2000-2014_SSA.csv`).

```
python3 -I compute_match_rates.py                    # uniform and real-calendar match rates (seed 2701) -> match-rates.json
python3 -I cluster_rates.py                          # window-of-days results -> cluster-rates.json
python3 -I sqrt_rule.py                              # the rule vs the exact answer, 2 to 2,000 slots -> sqrt-rule.json
python3 make_read_sheet.py                           # READ-ALOUD.md from BEATS-DRAFT.md (+ a mechanical lint)
/opt/homebrew/bin/python3.12 make_audio.py           # only after Gate P: Kokoro am_onyx, Whisper check
/opt/homebrew/bin/python3.12 build_slates.py         # the 18 4K stills (and, staged, the reveal states)
/opt/homebrew/bin/python3.12 check_onscreen.py       # spoken figures on screen, type size, contrast, margins
/opt/homebrew/bin/python3.12 build_motion.py --plan --render --encode   # cues, reveal states, one 4K video per beat
/opt/homebrew/bin/python3.12 compile_master.py       # master mp4, captions, loudness (once)
/opt/homebrew/bin/python3.12 proof_cut.py            # frames at 15/50/85%, reveal timing, holds, silence, black frames
python3 build_beat_sheet.py                          # beat_sheet.json and SHOTLIST.md
```

The Short (run from the working folder; its files are in `short/`):

```
python3 make_read_sheet_short.py                     # short/READ-ALOUD-SHORT.md from short/SHORT-SCRIPT.md (+ lint)
/opt/homebrew/bin/python3.12 short/make_audio_short.py   # only after Gate P: one Kokoro pass per line, Whisper word times
/opt/homebrew/bin/python3.12 short/build_short.py --cues --render --encode   # event times, every frame at 2160x3840, silent video
/opt/homebrew/bin/python3.12 short/compile_short.py  # master, loudness, captions (once)
/opt/homebrew/bin/python3.12 short/proof_short.py    # the Shorts production gate, measured on the compiled file
python3 short/build_short_sheet.py                   # beat_sheet-short.json and SHOTLIST-SHORT.md
```

**Components.** Nothing from `brutalist.art` is used except its bundled open-licence fonts (EB Garamond, Inter), read in
place by `build_slates.py`. The equations use a small structural layout in that script (real radical, fraction bar, sized
parentheses) because the toolkit's `typeset_math.py` needs matplotlib, which was not installed; the algebra is checked
separately by `sqrt_rule.py`. All the slates, animation and compile steps are in this folder.
