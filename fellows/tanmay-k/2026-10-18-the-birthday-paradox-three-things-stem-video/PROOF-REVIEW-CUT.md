# PROOF review (compiled cut): "The Birthday Paradox: Three Things You Could Change" — Tanmay Kulkarni, Week 27 topic film

**Stage:** first compiled master, `the-birthday-paradox-three-things.mp4`. Reviewed from frames extracted from the compiled file at 15 / 50 / 85% of every beat (54 frames, `_qc/`, contact sheets `_qc/cut_sheet_1..3.png`), 84 per-reveal timing checks against the cut, and measurements on the master (`proof_cut.py`, output in `_qc/proof_cut_output.txt`). PROOF cannot listen or watch playback, so audio quality, the feel of the motion and caption sync in a player are listed as not assessable.

**Master:** 3840×2160, 30 fps, H.264; AAC 48 kHz mono; **289.1 s (4.82 min)**, 104 caption cues (`.srt`, `.vtt`). *This is the second master: the first (383.7 s) was narrated sentence by sentence and Tanmay heard it as slow motion; see the addendum at the end. The frame-by-frame findings below were made on the first master; the addendum has the current measurements.*

**Verdict:** **unlisted-until-fixed**, i.e. not yet cleared for public. Nothing in the frames blocks it; it needs Tanmay's watch-through and listen (three words to hear, below). Teaching **12/12** holds on frames. Production gate **PASS**, with 2 MINOR flags.

One line: this film shows every figure when it is spoken, sourced, and held long enough to read; what remains is what only an ear and a playback can judge.

## Rubric on the compiled frames

| Criterion | On the cut |
|---|---|
| Explicit framework | **2.** The three cards appear in B02 before any change is made and stay as the chapter index (B03–B11), returning with readings in B12 |
| Reusable rubric | **2.** B13 builds the rule on screen in the order it is spoken: the table of days and exact answers first, then the rule, then the square-root column, then the rule's results, the check marks, and the honest tally |
| Worked example | **2.** B15 and B17 add the square-root line, the working line, then the two exact percentages one at a time |
| Falsifiability / edge | **2.** B05 (some pair vs you), B13 tally, B14 school year, all revealed at the moment they are spoken |
| Active task | **2.** B16 reveals the question, the rule, the wrong answer, then a countdown from 8 s that ticks down once a second to the end of the hold; B17 gives the working |
| Friction | **2.** The three cards set the puzzle in B02; B12 resolves it card by card as each verdict is spoken |

**Total: 12/12.**

## Production gate, measured on the master

| Check | Result |
|---|---|
| **Reveals on cue** | **PASS.** 84 reveals checked: 0.5 s after each cue the frame is nearer the new state, 0.4 s before it is nearer the old one. (An unchanged frame differs from its PNG by about 2.2 grey levels from the YUV conversion; that is codec colour, not timing.) |
| **Every spoken figure on screen when spoken** | **PASS after two fixes found in this review** (below) |
| **Comparisons held ≥ 2 s with every item on screen** | **PASS.** B05 9.8 s, B07 4.5 s, B09 5.9 s, B12 4.7 s, B13 table complete 3.0 s then the tally to the end, B15 3.5 s, B17 2.8 s |
| **B16's 8 s hold** | **PASS.** Measured silence in the master: 8.69 s (8 s hold plus the 0.45 s tail and the beat join), with the bar and "n s" counter ticking down once per second |
| **Gaps inside narration** | **PASS.** No silence ≥ 0.5 s inside any beat except the 0.56–0.75 s beat joins and the B16 hold |
| **Black frames** | none |
| **Loudness** | integrated **−14.9 LUFS**, true peak **−1.9 dBTP**, LRA 2.9. Target was −14 / −2.0, so it is 0.9 LU under and 0.1 dB over the ceiling. Both are inside what YouTube accepts (it normalises, and its ceiling is −1 dBTP), but see flag 1 |

## Findings from the frames (both fixed, cut re-encoded for B08 and B13 and recompiled once)

| # | Finding | Fix |
|---|---|---|
| 1 | **B13: figures spoken before they were on screen.** "Twenty three for three hundred and sixty five days. Twelve for ninety. Seven for thirty" were spoken over about 10 s of an empty slide; the table appeared only at "A year gives twenty three". | The table frame with the *days* and *exact answer* columns now appears at "Twenty three for"; the rule, the square-root column, the rule's results, the checks and the tally follow on their own cues |
| 2 | **B08: "96%" headline appeared 3 s after it was spoken.** | The headline now appears with the chart; only the explanatory line waits |

The final frame of every beat is pixel-identical to the still Tanmay approved; the staged versions only change when things appear.

## Flags

**MINOR**
1. **Loudness.** −14.9 LUFS and −1.9 dBTP: re-run with a −2.5 dBTP ceiling if you want it strictly under −2.0, which would land near −15.4 LUFS. [EDIT]
2. **Two slow starts.** B02 shows only its heading for the first ~7 s while Tanmay introduces himself, and B12 shows only the bottom block for ~9 s before the three cards appear. Both are narration-led and pass, but B12's three empty card frames could be on screen from the start to show the structure early. [EDIT, optional]

## By ear: three words PROOF cannot judge

Whisper (small.en) confirms every word of the signed narration apart from digit formatting, with three real differences to listen for:
- **B09:** "Squeeze it. Not twenty three people…" was heard as "Squeeze at not…". A short "it" at a sentence end.
- **B13:** "Add a half, and round." was heard as "add a half in round". "and" may be reduced.
- **B16:** "A tempting wrong answer…" was heard as "Attempting wrong answer…". The "a" may run into "tempting".
If any of the three sounds wrong in the master, the fix is a phoneme or pause override at audio, not a text change (the narration is Gate P signed). Also listen for "Kulkarni" and "Tanmay" in B02 and B18, the doubled `ɹɹ` in "Security", and "point eight" in B07 (`PHONEMES-CHECK.md`).

## Not assessable here

- Rhythm and emphasis of the delivery, and whether B16's 8 s feels right when you do the task.
- How the 0.25 s crossfades feel on playback.
- Caption sync in a player (captions are timed from the sentence boundaries of the audio, not hand-checked).
- Legibility on a phone at arm's length. The type was raised to ≥ 24 px at 1080p scale after the stills review; check it on a device.

## Do X next

1. **[EDIT]** Tanmay: watch the master once through and listen, with the three words above and the names in mind. Reply with what to change.
2. **[EDIT]** Optional: loudness ceiling (flag 1) and the empty-card start in B12 (flag 2).
3. **[EDIT]** Any audio fix is a phoneme or pause override and a re-run of `make_audio.py`, then re-encode only the affected beats and recompile once (`build_motion.py --encode Bnn`, `compile_master.py`).
4. **[RESHOOT/NEW SOURCE]** None.
5. Before pushing to the shared repo: write the folder README per the established set (text and code only; masters on the shared Drive; Links table with the two Drive placeholders), and do not copy the toolkit or any fellow's files.

## What works

- **Figures arrive with their words.** After the fixes, nothing is spoken before it is on screen, and each comparison is held.
- **The hold is a real hold.** The 8 s in B16 is measured silence with a visible countdown.
- **The rule builds in the order it is spoken.** The table the viewer already heard sits on screen first, so "it follows a rule" has something to follow.
- **Clean sourcing throughout.** Federal counts plus our own simulations, no third-party media, no political content, no real individuals.


---

# Addendum: pace correction, second master (2026-10-17)

**Why:** while reviewing the Week 27 work video, Tanmay heard its audio as "slow motion". Cause: the audio script synthesised each *sentence* alone, which Kokoro reads about 30% slower than a whole paragraph (2.5 words a second against 3.5, the pace of Week 26). The topic video was built with the same script, so it had the same problem. Each beat is now synthesised whole; the sentence times for the captions come from the Whisper word clock. The voice (`am_onyx`) and its speed (`1.0`) were not the cause. The first master, its audio and its captions are kept in `_superseded-persentence/`.

**What changed and what did not:** the 18 stills, the narration and every cue phrase are unchanged. The narration is 289 s instead of 384 s. The cues were re-timed on the new Whisper clock, the 18 beats re-encoded, and the master recompiled.

**Master:** 3840×2160, 30 fps, H.264; AAC 48 kHz mono; **289.1 s (4.82 min)**; **-14.7 LUFS, -1.8 dBTP, LRA 2.9**; 104 caption cues.

| Check | Result on the second master |
|---|---|
| Reveals on cue | **PASS.** 84 reveals checked, 0 mistimed |
| Black or frozen-start frames | **PASS.** none |
| Gaps inside narration | **PASS.** every silence of 0.5 s or more is an end-of-beat hold or the B16 hold, judged against each beat's last heard word |
| B16 countdown hold | **PASS.** 8.70 s of silent hold measured |
| Comparisons held ≥ 2 s with every item on screen | **PASS with 2 MINOR flags.** B05 8.2 s, B07 3.9 s, B09 5.9 s, B12 3.3 s, B15 2.4 s. **B13 stage 5: 1.9 s; B17 stage 4: 1.4 s.** In both, the next stage only adds an annotation and nothing is removed, so the comparison stays on screen to the end of the beat (B13 6.2 s, B17 5.7 s); the faster narration shortened the gap before that next addition |
| Whisper word match vs the signed text | worst B07 0.91, B13 0.93, B10 0.93, B14 0.93; every difference is Whisper's spelling (".8%" as "8", "fortnight" as "Fortnite", "cutoff" as "cut off", "a tempting" as "attempting") |

**Verdict unchanged:** teaching **12/12**; production gate **PASS** with the 2 MINOR flags above (they replace the two of the first master). Not yet public until Tanmay has watched and listened to this master.

**To listen for:** "fortnight" (B11), "a tempting" (B16), and the overall pace, which is now the Week 26 pace.
