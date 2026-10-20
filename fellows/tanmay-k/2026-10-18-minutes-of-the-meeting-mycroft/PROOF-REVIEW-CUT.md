# PROOF review (compiled cut): "Minutes of the Meeting", Week 27 work video

**Stage:** the compiled master, `minutes-of-the-meeting.mp4`. Reviewed from frames extracted **from the compiled file** at
15 / 50 / 85% of every beat (36 frames in `_qc/`, contact sheets `_qc/cut_sheet_1..3.png`), 51 per-reveal timing checks against
the cut, a spoken-figure check on the Whisper word clock, and measurements on the master.

**Master:** 3840×2160, 30 fps, H.264; AAC 48 kHz mono, **-14.8 LUFS, true peak -1.9 dBTP, LRA 3.1**; **234.3 s (3.91 min)**;
77 caption cues (`.srt`, `.vtt`).

**Pace correction (after Tanmay's first listen: "it feels like slow motion").** The first master (308 s) was right on every
check and still wrong to the ear. Cause: the audio script synthesised each *sentence* alone, which Kokoro reads about 30% slower
(2.5 words a second against 3.5 for a whole paragraph, the pace Week 26's audio has). The voice (`am_onyx`) and `speed=1.0` were
never the problem; the sampling rates and headers were checked and are correct. Each beat is now synthesised whole, the sentence
times for the captions come from the Whisper word clock, and the film is 74 s shorter. The per-sentence audio and master are kept
in `_superseded-persentence/`. A second finding at the same step: Kokoro merges "What-If" into "wudif" (Whisper heard "word of");
it is now voiced as "what if", with the text and captions keeping the real spelling.

**Verdict:** **cleared for Tanmay's watch-through and listen. Not yet cleared for public.** Nothing in the frames blocks it; what
remains is what only an ear and a playback can judge (the listen list below). Teaching **12/12** holds on the frames. Production
gate **PASS**. Five defects were found by this review and fixed (below); each fix needed a recompile, so the master was compiled
six times, not once.

## Rubric on the compiled frames

| Criterion | On the cut |
|---|---|
| Explicit framework | **2.** B02 puts "Who had a vote, and how much?" on screen as it is asked; B03 draws the chair and the voices before any voice speaks |
| Reusable rubric | **2.** B11 reveals the three questions one by one as they are spoken, then the good and the weak answer |
| Worked example | **2.** One stock, c11, from B03 to B07; each figure appears as it is spoken |
| Falsifiability / edge | **2.** B09 builds the two minute-takers, the two requests, the language difference, the fix, and "23 of 23", in the order the narration tells it; B10 shows the hand-offs never made and the items still open |
| Active task | **2.** B11 holds the question and both answers for 8.6 s |
| Friction | **2.** B07 holds STRONG SELL against ENTER FULL POSITION, then the weights, the scale, the pieces, the total and SELL, each at its phrase |

**Total: 12/12.**

## Production gate, measured on the master

| Check | Result |
|---|---|
| **Reveals on cue** (`proof_cut.py`) | **PASS.** 51 reveals checked: 0.5 s after each cue the frame is nearer the new state; 0.4 s before it, nearer the old. 0 mistimed (an unchanged frame differs from its PNG by about 2.5 grey levels from the YUV conversion; that is codec colour, not timing) |
| **Every spoken figure on screen when spoken** (`check_figures.py`) | **PASS after one fix.** 25 figures checked against the Whisper word clock; every one is on screen at or before it is spoken, rechecked on the final audio. The first run found one late: B08's "about 470 words" was spoken at 2.98 s and shown at 9.16 s |
| **Comparisons held ≥ 2 s with every item on screen** | **PASS after one fix.** B05 4.0 s, B07 4.2 s, B08 2.6 s, B09 5.6 s, B10 2.9 s, B11 7.1 s. B08 first held only 1.85 s; it now has a 1 s hold |
| **No gaps inside narration** | **PASS.** Every silence of 0.5 s or more is a beat's end hold or join (0.7 to 3.0 s). The one the script labels "inside narration" (B08, 17.2 s) starts after the last word ends (16.96 s): Kokoro's own trailing silence plus the hold |
| **No black or frozen-start frames** | **PASS.** `blackdetect`: none |
| **Resolution** | **PASS.** 3840×2160 at 30 fps; audio 48 kHz |
| **Loudness** | **PASS.** -14.8 LUFS integrated (target -14, two-pass, linear), true peak -1.9 dBTP |
| **Types and contrast** (`check_onscreen.py`, every slate's final state) | **PASS.** ≥ 24 px on the 1080 grid; ≥ 4.5:1 against the real backdrop |
| **Sources on screen** | **PASS.** Every claim beat's frames carry the committed file(s) in their source line |
| **Invented numbers labelled** | **PASS.** "Invented · sample data" on every beat with a number (B02 and B09 carry their own wording; B02 and B12 also say it in words with "Not investment advice") |
| **Audio check** | Whisper (small.en) word match against the signed text, worst first: B07 0.81, B04 0.87, B03 0.92, B05 0.94, B06 0.94, B09 0.96, the rest ≥ 0.97. **Every difference is Whisper's spelling, not Kokoro's speech:** "sell" written "cell", "forty-five" as two words, "82 %" as a symbol, "price-to-earnings" as "priced earnings". The listen list below is what a transcript cannot settle |
| **Short sentences** | Whisper heard "Invented.", "Who had a vote?", "Nobody has made a mistake.", "Four out of four.", "I fixed it." and "Adjourned" as written |
| **Override** | "Mycroft" is voiced MY-croft (`mˈaɪkɹɔft`), asserted at synthesis; it is spoken once, in B02 |

## Defects this review found, and what was done

| Beat | What the cut showed | Fix |
|---|---|---|
| all | **Slow-motion pace** (found by Tanmay's ear; every machine check had passed): per-sentence synthesis reads about 30% slower than a whole paragraph | whole-beat synthesis (above); audio, cues, motion and master rebuilt; the 12 slates are unchanged |
| B08 | "About 470 words" was spoken at 2.98 s but its figure appeared at 9.16 s (a spoken-figure-before-visual defect); the closing caption held only 1.85 s | the slate now has six stages: the word count has its own stage, at its phrase; a 1 s hold was added to the beat |
| B02, B06, B09 | The first 7 s, 5 s and 10 s of these beats showed only a heading | B02 now carries the recipe's path from the start; B06's rows appear at "how close is it to changing its mind"; B09 builds the two minute-takers' cards at "to check the original", so the story is on screen as it is told |
| B02 | **The fix above overprinted the README quote with the recipe's path** (caught on the 50% and 85% frames) | the quote, the strip and the questions moved down; re-rendered, re-checked |
| B09 | A stage-order mismatch: "21 of 23" appeared before the language difference was shown | stages follow the narration: cards, then requests and "21 of 23", then the two languages, then the fix, then "23 of 23" |

## Boundaries (carried from the stills review)

- **W25:** B09 shows one difference between two languages and its fix; no rounding panel, no threshold, no deliberate break of my own copy.
- **W26:** the defaults are shown as how the meeting starts and as the briefing's identical line; the on-screen thesis stays "who had a vote, and how much".
- **No critique:** defaults, weights, scale and the NaN request cards are drawn as how the workflow works.
- **Committed files only** on screen; nothing from the session.

## For Tanmay's watch and listen (what a transcript cannot settle)

1. **"The chair's scale" (B07).** Whisper wrote "chair scale"; the phonemes carry the possessive (`tʃˈɛɹz`), but check by ear that the "s" is audible.
2. **"A, B, C" (B09).** The phonemes read "ay, bee, see"; check it does not sound like "uh".
3. **Short sentences** ("Invented." in B03, "Four out of four." in B05, "I fixed it." in B09, "Adjourned." in B12): they are synthesised alone and joined with 0.22 s gaps; check they do not sound clipped.
4. **The new pace (3.5 words a second in narration) and B07 (32 s, 109 words).** B07 is the densest beat; check that each element lands on its phrase and you can keep up. If it feels quick anywhere, the lever is the beat's holds, not the voice speed.
5. **The two empty-looking openings that remain:** B05's first seconds show the three seats while "Second voice" is spoken, and B12 opens on one word. Both are intended.

## Not done yet

- No 9:16 Short, no folder README, no push or final folders for the work video.
- This review has not been listened to by a human; the audio checks above are machine checks.
