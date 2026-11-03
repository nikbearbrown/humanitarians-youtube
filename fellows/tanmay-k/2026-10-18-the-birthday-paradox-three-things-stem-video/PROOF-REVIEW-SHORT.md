# PROOF review (Shorts criteria, plan stage): "Take Away Days", the 9:16 trailer for *The Birthday Paradox: Three Things You Could Change*

**Stage:** the Short's script (Gate P signed 2026-10-17: 7 lines, 142 words, about 62 s) and its design in `short/SHORT-SCRIPT.md`. No audio, no frames yet, so this review scores the plan and sets the checks every later stage must pass. It is reviewed against **Shorts criteria**, which differ from the 16:9 rubric (below).

**Verdict:** **unlisted-until-fixed** (nothing exists to publish). Shorts score **12/12 at plan level** after the second pass below (it was 10/12 on the first). Production gate: **checks defined; none measurable until frames exist.** The design fixes are applied. The narration of S03 to S07 is untouched and stays signed; **S01 and S02 were reworded and need a Gate P re-read** (see Update).

One line: this Short is built to stand on its own as one scene, and the two things that held it at 10/12 (a spoken hook that started after a name introduction, and a pointer a Short cannot link) are now closed in the script and the frame.

## Why the Shorts criteria differ from the 16:9 rubric

| Question | 16:9 film (PROOF rubric) | Short (this review) |
|---|---|---|
| Who is the viewer | Chose to watch and can sit through a task | Swiping past: decides in about 3 s, often with sound off |
| What teaches | Explicit framework, reusable rubric, worked example, falsifiability, active task, friction | One idea, closed: a claim, a surprise, a rule, a payoff. A framework or viewer task is optional |
| Time | Held figures ≥ 2 s; a task may hold 8 s of silence | No dead air; something changes at least every 3 s; the format cannot afford a held silence |
| Screen | 16:9, legible on a laptop | 9:16 at phone width, **inside the UI safe area**: text between 12% and 75% of the height, clear of the right button rail |
| Structure | Chapters and a rubric ending are fine | **One scene, no stitched beats, state carries across every cut, its own ending** (Tanmay's rule since Weeks 23 and 24) |
| Context | May lean on earlier chapters | Must carry its own: who is speaking, the claim, why, the rule |
| Role | The film | A trailer: earns the click to the film, without needing it |
| Ending | Single open question or payoff | Closes where it opened, so it also plays as a loop |

## The Shorts rubric (score each 0–2, total /12)

| Criterion | What it means for a Short |
|---|---|
| **Hook** | In the first ~3 s something moves on screen *and* the spoken claim has started |
| **Standalone context** | A viewer who has not seen the long film gets who, what, why and the rule, with every term defined on screen |
| **One arc, own ending** | One continuous scene (no hard cut), state carried across every line, an ending that closes the arc |
| **Phone legibility** | Safe-area zones, type size, muted comprehension: the argument reads with the sound off |
| **Pace and retention** | Under the 180 s cap with no dead air; a visible change at least every 3 s; nothing static longer than 3 s |
| **Trailer function** | Names the full film and what it adds; one pointer, not buried; the Short never depends on it |

### Production gate for a Short (binary; any fail blocks public)

1. **9:16 at 4K:** 2160×3840, probed with `ffprobe` (never trust the tool's default).
2. **Safe area, on pixels:** no text ink above 12% or below 75% of the height; none in the right 12% of the width below the top third.
3. **Type size:** nothing below 30 px logical (1080 wide) on a data label, 40 px on a key figure's caption. Measured from the draw log, not by eye.
4. **Every spoken figure on screen when spoken**, and every comparison held ≥ 1.5 s (shorter than the long film's 2 s because the format is faster).
5. **Sources on screen** inside the safe area.
6. **No hard cuts:** no consecutive-frame jump above the eased-motion ceiling; the scene is one render.
7. **No static stretch longer than 3 s** (frame difference).
8. **Loop-friendly last frame:** the closing frame matches the opening state (mean difference measured).
9. **Audio:** 48 kHz mono AAC (the sample-rate parity rule), −14 LUFS ±1, true peak ≤ −1.5 dBTP, **no silence ≥ 1 s**.
10. **No foreign identity:** no other channel's handle, no toolkit default copy.
11. **Duration:** well under 180 s (target ≤ 70 s including the closing text).

## Plan-level scores

| Criterion | Score | Why |
|---|---|---|
| Hook | **2** | Was 1: the claim started after a 3.5 s name introduction. Now the first spoken words are the bet ("Twenty three people in a room. Bet me two of them share a birthday.") over a calendar already filling, and the name rides in the answer (S02). To be confirmed by the Gate P re-read |
| Standalone context | **2** | Who (S01, S07), the claim (S01–S02), the surprise (S03), why (S04), the rule (S05–S06), the ending (S07). Two undefined terms found and fixed on screen: "even odds" now carries "= a 50% chance"; "days" now reads "possible birthdays" |
| One arc, own ending | **2** | One scene by design: the calendar narrows around the same 23 dots, then widens and the loop closes at "a year, twenty three". Written fresh; none of the long film's beats are reused |
| Phone legibility | **2 (design level)** | The layout rules are now written into the script: safe area, type sizes, a headline line that carries the argument muted. To be proven on frames |
| Pace and retention | **2 (design level)** | About 62 s plus 2.5 s of closing text, no silent holds. The rule was one 9 s static block; it is now revealed in three steps as spoken, and the end card is now an overlay on the restored scene, not a separate card |
| Trailer function | **2** | Was 1: a Short cannot carry a link. S07 names the film and what it adds ("three things you could change, and the one that decides it"), and the closing text now gives its exact searchable title, so the pointer works without a link. Setting the related video at upload is still on the upload checklist (finding 7), not part of the film |

**Total: 12/12 at plan level** (was 10/12). The two design-level 2s (legibility, pace) and the two re-scored 2s (hook, trailer) are claims about the plan until the frames and the re-read confirm them.

## Findings

**MAJOR (fixed in the design)**
1. **A static rule block.** S05's rule was a single typeset line held about 9 s while the narration reads it: a swipe-away risk and a break of the "changes every 3 s" criterion. Fixed: it is revealed in three steps as spoken (√d, then 1.2 ×, then + ½).
2. **Safe area and type size were unspecified.** The Week 26 long-film rules (≥ 24 px at 1080p) are not enough for a phone-held 1080-wide frame. Fixed: zone and size rules added to `SHORT-SCRIPT.md`.

**MINOR (fixed in the design)**
3. "Even odds" and "days" were undefined for a first-time viewer. Labels added.
4. A separate end card would have cost a loop. The closing text now overlays the restored opening scene.
5. The argument needed a muted path. A one-line headline now changes with each line of the script ("Two of these 23 share a day", "Same 23 people. Fewer days.", "What decides it?", "The rule", "Try it").

**Update: the two items that held it at 10/12 (applied 2026-10-17)**
6. **Hook (1 to 2).** Option B was refined so the "name at both ends" convention stays: S01 is now only the bet ("Twenty three people in a room. Bet me two of them share a birthday.") and S02 carries the name ("I'm Tanmay Kulkarni, for Humanitarians AI, and you'd lose that bet about half the time."). The word count is unchanged (142). S01 and S02 need a Gate P re-read; S03 to S07 stay signed (`GATE-P-SIGNOFF-SHORT.md`, `SIGNED-NARRATION.json`).
7. **Pointer (1 to 2).** The closing text now reads "The full video. Search: The Birthday Paradox: Three Things You Could Change · Humanitarians AI", an exact searchable title, so the pointer works where a link cannot. Upload checklist (not scored): set the long film as the Short's related video in YouTube Studio and put its URL in the Short's description once it is public.

**What would take it back down:** the S01/S02 re-read finding the new wording awkward (Hook to 1); the frames failing the safe-area, type-size or 3-second-change checks (Legibility or Pace to 1); a hard cut or a static stretch over 3 s in the cut (One arc or Pace to 1).

## Do X next

1. **[GATE P]** Tanmay: re-read S01 and S02 (new wording) and reply "Short Gate P PASS" or give notes.
2. **[EDIT]** Build audio from the signed script, then the continuous animation (one render, 2160×3840), with the layout rules above; compile once.
3. **[EDIT]** Run the Shorts production gate (items 1 to 11) on frames and measurements from the compiled file; re-score this rubric on the master.
4. **[UPLOAD]** After the long film is public: related video and description URL (finding 7).
5. **[RESHOOT/NEW SOURCE]** None. Every figure is the long film's.

## What works

- **One scene.** The whole argument is one object that changes: a calendar around the same 23 dots.
- **It stands alone.** Nothing in it needs the long film, and it still points to it.
- **Its ending is real.** It closes where it opened, so "that's why it's twenty three" lands and the last frame loops into the first.

---

# Cut stage: the compiled Short, measured (2026-10-17)

**Stage:** the compiled master `the-birthday-paradox-three-things-short.mp4`: 2160×3840, 30 fps, 46.97 s (1,409 frames) *(second master; see the addendum at the end)*, AAC 48 kHz mono. One scene rendered frame by frame from a function of time (`build_short.py`), audio on the Kokoro/Whisper clock (`make_audio_short.py`), compiled once (`compile_short.py`). Reviewed from frames pulled from the compiled file (`_qc/short_sheet_1.png`, `_qc/short_sheet_2.png`, 20 frames) and the measurements below (`proof_short.py`, raw output `_qc/proof_short_output.txt`).

**Verdict:** **unlisted-until-fixed** (not yet cleared for public; it needs Tanmay's watch-through and listen, and the upload steps). **Shorts rubric 12/12.** **Shorts production gate 12/12 checks pass.**

## Production gate, measured on the master

| # | Check | Result |
|---|---|---|
| 1 | 9:16 at 4K | **PASS.** 2160×3840, 30 fps, 1,633 frames |
| 2 | Safe area, on pixels (every 0.25 s) | **PASS.** Ink from 13.5% to 74.9% of the height (limits 12% to 75%); 0 pixels in the right rail. The bottom edge is 0.1% inside the limit (the closing text), see flag 1 |
| 3 | Type size | **PASS.** Smallest label drawn: 30 px at 1080 wide (sizes used: 30, 32, 34, 40, 46, 52, and the counter) |
| 4 | Every spoken figure on screen when spoken | **PASS.** 14 cue moments checked (50.7%; possible birthdays 90 and 30; 95.4%; 99.99%; 23, kept; +0.1 point at most; 365 → 30; the rule's key; 365 days → 23 people; 30 days → 7 people; 50.7% again; the film's title; the channel) |
| 4b | Comparisons held ≥ 1.5 s | **PASS.** 95.4% beside 90 days 3.1 s; 99.99% beside 30 days 2.2 s; 365 days → 23 people 3.7 s; 30 days → 7 people 1.6 s |
| 5 | Sources on screen inside the safe area | **PASS.** 6 of 6 phases carry one (the closing phase has none to show) |
| 6 | No hard cuts | **PASS.** Largest frame-to-frame change 2.33 grey levels (a cut between scenes is 20+) across 1,633 frames |
| 7 | No static stretch over 3 s | **PASS.** Longest stretch with fewer than 10 pixels changing: 2.57 s |
| 8 | Loop-friendly last frame | **PASS.** Calendar and dots at the end vs the opening state: 0.16 grey levels apart |
| 9 | Audio | **PASS.** AAC, 48 kHz, mono; −14.6 LUFS; −1.5 dBTP; the only silence ≥ 0.5 s is the 0.84 s tail |
| 10 | No foreign identity | **PASS.** No handles anywhere; only "Humanitarians AI" named |
| 11 | Duration and first frame | **PASS.** 47.0 s (cap 180 s); frame 0 already holds the headline and the calendar |

Stream lengths: video 54.433 s, audio 54.433 s (an earlier compile trimmed four frames; fixed by padding the audio to the video length).

## Shorts rubric on the cut

| Criterion | Score | Evidence in the master |
|---|---|---|
| Hook | **2** | The first words are the bet; frame 0 has the headline and the calendar; dots start landing at 0.3 s |
| Standalone context | **2** | Who (S02, S07), the claim (S01–S02), the surprise (S03), why (S04 rows), the rule (S05–S06), the ending (S07); "possible birthdays" and "a 50% chance" are defined on screen |
| One arc, own ending | **2** | One render; no consecutive-frame jump above 2.33 grey levels; the loop closes (0.16 grey levels from the opening state) |
| Phone legibility | **2** | Safe area on pixels; 30 px minimum; a headline per phase carries the argument muted |
| Pace and retention | **2** | 54.4 s; something moves at least every 2.57 s; no silence ≥ 1 s |
| Trailer function | **2** | The closing text gives the long film's exact title, searchable; the related-video step is on the upload checklist |

**Total: 12/12.**

## What was found and fixed on the way (recorded, not hidden)

| # | Finding | Fix |
|---|---|---|
| 1 | **"Add a half." came out of Kokoro as "that'll have"** when synthesised as a 3-word sentence on its own (both Whisper small.en and medium.en heard it that way). | Short sentences (< 5 words) are merged into their neighbour before synthesis; Whisper then hears "at a half" (a weaker, different miss: see By ear) |
| 2 | **The compile trimmed 4 frames and the audio ran 0.2 s past the video.** `-shortest` cut the video copy at an earlier packet. | Audio padded to the exact video length; both now 54.433 s |
| 3 | **The counter showed intermediate numbers when it came back.** It re-appeared while the calendar was still widening (57%, then 50.8%), not the 50.7% being spoken. | The widening now finishes as "twenty three" is said; the counter returns after the rule has faded |
| 4 | **"30 days → 7 people" was fully visible for 1.1 s** (the rule faded at "That's why"). | The rule block now fades 0.45 s later: 1.6 s visible |
| 5 | **A static stretch of 3.07 s** while the narration said "and it's ninety five percent". | The number now swells on its cue; the longest stretch is 2.57 s |
| 6 | **Overlapping closing lines and cross-fading headlines** showed in the frames. | Lines now sit on baselines; headlines fade out then in, not together |
| 7 | **The gate measured too coarsely at first** (a 108×192 frame cannot see a dot land). | The static-stretch test now reads 540×960 frames |

## Flags

**MINOR**
1. **The bottom margin is thin.** The closing text reaches 74.9% of the height against the 75% limit. It passes, but moving the closing block up by about 20 px would give margin against any platform's overlay changes. [EDIT, optional]
2. **The opening is sparse.** From 0 to 9.8 s the lower half of the frame is empty (the counter has not appeared). It is the safe-area layout, not a defect, but the grid could sit lower at the start and move up as the counter arrives. [EDIT, optional]
3. **Loudness is −14.6 LUFS at −1.5 dBTP**, at the lower edge of the −14 ± 1 target, with the Short's true-peak ceiling raised from −2.0 to −1.5 to reach it. Inside what YouTube accepts.

## By ear: PROOF cannot judge

- **"Add a half."** Whisper (small.en) hears "at a half" after the merge. It is the same phrase Tanmay accepted in the long film's B13 ("Add a half, and round."). If it sounds like "at" in the master, the fix is a phoneme override at audio, not a text change (the narration is Gate P signed).
- **"Squeeze it to one month"**: "it" may read as "at".
- **Pace.** 142 words in about 53 s is 2.7 words a second, faster than the long film's 2.3, because each line is spoken in one pass. Listen for "rushed".
- **The names** ("Tanmay Kulkarni") as in the long film; and whether the captions (`.srt`, spelled-out numbers as signed) line up in a player.

## Upload checklist (not scored)

1. Upload the Short with its `.srt` as English captions.
2. Once the long film is public: set it as the Short's related video in YouTube Studio and put its URL in the Short's description.
3. Decide on YouTube's "altered or synthetic content" box (the narration is a synthetic voice, said in the description).
4. Choose a thumbnail frame: 18.0 s (95.4% on the narrowed calendar) is the strongest single frame; 38 s (the rule) the most distinctive.

## Do X next

1. **[EDIT]** Tanmay: watch and listen once through (the by-ear items above) and reply with changes.
2. **[EDIT]** Optional: flags 1 and 2.
3. **[EDIT]** Folder work: add the Short's files to a `short/` folder inside the `2026-10-18-…` staging folder, then assemble the flat `final/` folder (repo convention: `-short` suffix, no `.mp4`).


---

# Addendum: pace correction, second master (2026-10-17)

**Why:** the Short's audio was synthesised sentence by sentence, as the long film's was; Kokoro reads that about 30% slower than a whole paragraph (Tanmay heard the work video built the same way as "slow motion"). Each script line is now synthesised whole, with 0.35 s between lines; the sentence times come from the Whisper word clock; the three-word sentence ("Add a half.") that had to be merged before is now voiced inside its line (phonemes `ˈæd ɐ hˈæf`; Whisper writes "at a half", a d/t confusion, not the earlier "that'll have"). Narration is 46.15 s for 142 words (Whisper match 0.972). The first master is kept in `short/_superseded-persentence/`.

**Master:** 2160×3840, 30 fps, 46.97 s (1,409 frames); AAC 48 kHz mono, **-14.4 LUFS, -1.5 dBTP**; 28 caption cues. Video and audio streams are 46.967 s each.

**The Shorts production gate, rerun on the second master (`proof_short.py`): 12/12 checks pass.**

| | Result |
|---|---|
| Resolution, frame rate | 2160×3840 at 30 fps, 1,409 frames |
| Safe area | ink from 13.5% to 74.9% of the height; 0 pixels in the right rail |
| Type size | smallest text 30 px at 1080 wide |
| Every spoken figure on screen when spoken | 14 cue moments checked |
| Comparisons held ≥ 1.5 s | 95.4% beside 90 days 1.8 s; 99.99% beside 30 days 2.1 s; 365 days → 23 people 3.7 s; 30 days → 7 people 1.6 s |
| Sources on screen | 6 of 6 phases |
| No hard cuts | largest frame-to-frame change 2.59 grey levels |
| No static stretch over 3 s | longest 2.17 s |
| Loop-friendly last frame | 0.16 grey levels from the opening state |
| Audio | -14.4 LUFS, -1.5 dBTP; one silence of 0.89 s |
| No foreign identity | none |
| Duration and first frame | 47.0 s (cap 180 s); frame 0 has content |

The scores in the tables above hold, with these updated measurements: pace 47.0 s, something moves at least every 2.2 s, no silence of 1 s or more. **To listen for:** "Add a half." (S05).


---

# Addendum: fade correction, third master (2026-10-17)

**Why:** Tanmay, reviewing the work video's Short: "the transition is not smooth; it lags a bit and then it switches". The cause was in the scene canvas, which the topic Short shares: Pillow ignores the alpha of a text fill, and an RGBA base replaces pixels instead of blending, so every fade was a pop (an element appeared at full strength as soon as its alpha passed 0.01, and during a headline change the old and new lines overlapped at full strength). The canvas is now an RGB base drawn with real alpha blending, with text drawn through an alpha-scaled mask. The first master of this Short is kept in `short/_superseded-persentence/`; the pre-fix scene code is `short/build_short-v1-superseded.py`.

**What did not change:** the narration, the audio, the cues, the layout and the figures. Every fade is now a real fade.

**Master:** 2160×3840, 30 fps, 46.97 s (1,409 frames); AAC 48 kHz mono, **-14.4 LUFS, -1.5 dBTP**; 28 caption cues. **The Shorts production gate, rerun on the compiled file: 12/12 checks pass.** Largest frame-to-frame change **1.62** grey levels (was 2.59); longest static stretch 2.23 s; loop-friendly last frame 0.17 grey levels; safe area 13.5% to 74.9%; smallest text 30 px.
