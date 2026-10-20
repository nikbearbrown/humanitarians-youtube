# PROOF review (the Short, plan stage): *Who Fills the Blank?*, Week 27 work video

**Stage:** script draft 3 (Gate P signed on draft 2; S01 changed in this review, re-read pending) and the scene plan. **Nothing is built:**
no audio, no frames. Reviewed from `SCRIPT-SHORT.md`, `FACTCHECK-SHORT.md`, `short/plan_cadence.py` and measurements of the planned text.
The Shorts criteria are **not** the 16:9 rubric (hook, standalone context, one arc with its own ending, phone legibility, pace, trailer function).
The production gate is checked as **intent** and is re-measured on the compiled file with `proof_short.py` (the 11 checks).

**Verdict:** the plan as first drafted scored **9/12**. After the four fixes below it scores **12/12**. Production gate: PASS as intent.
**One line needs a re-read** (S01, which now opens on the question) before audio.

## Rubric (Shorts)

| Criterion | First plan | After the fixes | Why |
|---|---|---|---|
| Hook: the claim is spoken from 0 s and the picture moves from frame 1 | **1** | **2** | The question ("who fills in the blank?") arrived about 8 s in, after a setup sentence. **Fix:** S01 now opens on it, and the headline carries it from frame 0; the line types in from 0.3 s |
| Standalone context | 2 | 2 | Who (S02, S07), the question (S01), the stock and the voices (S02, S03), the answer (S04), what the AI gets (S05), what the full film will show (S06) |
| One arc, its own ending | 2 | 2 | One scene, never cut. The blank at the top is filled in S04, becomes the last line of the minutes in S05, and dissolves back to a blank in S07: the loop closes on its opening state |
| Phone legibility | **1** | **2** | S06 put four previews around the sheet inside a 840 px-wide safe area, which cannot hold them at 30 px type. **Fix:** the sheet moves up and shrinks; previews arrive one at a time in a zone under it (y 920 to 1380). The longest planned strings fit the safe width (table below) |
| Pace and retention | **1** | **2** | The first event plan left gaps up to 7.7 s. **Fix:** an event on every clause (53 events, `plan_cadence.py`); the largest gap between events is now 2.9 s (the first 5 s are the line typing in, continuously) |
| Trailer function | 2 | 2 | S06 says what the full film will show (the whole meeting from files you can open, what the AI is handed, where my own copy disagreed and how I caught it); S07 gives the exact searchable title, "Minutes of the Meeting: What an AI Is Handed"; the related video is set at upload |

**First plan 9/12 → 12/12.**

## What was checked

| Check | Result |
|---|---|
| Safe-area width of the planned text (840 px, Inter, EB Garamond, PT Mono) | **Fits.** The line `IMPORTANT: Your action_plan.immediate` (mono 34) is 755 px; `must strictly match "SELL".` 551; `ENTER FULL POSITION` (40) 426; the name line (34) 529; `Have you read the minutes?` (64) 697; `Minutes of the Meeting:` (56) 537 and `What an AI Is Handed` 501 (two lines); `21 of 23 → 23 of 23` (56) 444; `Sentiment Score: 0.5/1.0` (34) 490 |
| Event cadence | 54 events over about 86 s on the planning clock; largest gap 2.9 s (`plan_cadence.py`, re-set on the Whisper clock at build) |
| Comparisons held | The two identical lines are both on screen from about 67.8 s until the previews recede (about 7 s); "21 of 23 → 23 of 23" is complete from about 73.7 s until the recede (about 3.8 s). The gate's 1.5 s minimum is met with margin only because those two previews **stay** until the recede, not until the next preview |
| Facts | Every figure is read from main @ `8665a9f`, the long film's figures (`FACTCHECK-SHORT.md`, SW1 to SW12); the one wording to keep is "your action plan must strictly match" (SW1) |
| Length | about 86 s planned (7 lines, 280 words), under the 180 s Shorts cap and as long as Tanmay asked for: unhurried, with a clause for each voice |

## Production gate (intent), for the build to honour

| # | Check | Plan |
|---|---|---|
| 1 | 2160×3840 at 30 fps | one scene rendered as frames from a function of time |
| 2 | Safe area: ink between 12% and 75% of the height; nothing in the right rail | all text in x 60 to 900, y 230 to 1440 logical; the source line inside it |
| 3 | Type: nothing below 30 px logical | measured above at 30 to 64 px |
| 4 | Every spoken figure on screen when spoken | the cadence table puts each figure's event on its phrase; checked on the compiled file |
| 4b | Comparisons held ≥ 1.5 s | see above |
| 5 | Sources on screen | a source line per phase, inside the safe area |
| 6 | No hard cuts | one scene; every change is a transition inside it |
| 7 | No static stretch over 3 s (measured at 540×960) | the cadence plan above; the previews' own animations run through their holds |
| 8 | Loop-friendly last frame | the verdict dissolves to the blank, so the end state is the opening state (to be measured) |
| 9 | Audio: 48 kHz, about -14 LUFS; no silence of 1 s or more | whole-line synthesis, 0.35 s between lines, a 0.8 s tail |
| 10 | No foreign identity | only "Humanitarians AI" named; no handles |
| 11 | Duration and first frame | about 86 s; frame 0 carries the headline, the label and the line's first characters |

## Boundaries checked

- **Not the long film's beats.** It shares the stock and the figures, not the words or the order; S06 says what the long film shows and does not replay it.
- **Not the topic Short's shape** (a calendar that squeezes) **nor Week 26's** (one morning, one price): its unit is a blank in one line that gets filled.
- **No critique.** The weights, the defaults and the verdict are drawn as how the workflow works; "fragile" is the film's plain word for a stability of 0.05 (SW5). My own copy's disagreement is stated as a fact with its remedy, not detailed.
- **Committed files only** on screen; every company and number labelled invented from the first frame.

## Risks to watch at the build

- **S06 is the densest line** (about 22 s, four previews). Each preview's cue must sit on its phrase, and the last two must stay up until the recede.
- **S01 now opens cold on the question**, then explains. The typing line has to be paced so the viewer reads the blank as the narration says "and then a blank".
- **S04's SELL landing** (the blank filling) is the payoff: it needs a clean ring, a clear fill, and about 1.5 s to read before S05's fold begins.
- **Whisper cue times, not the planning clock,** will set every event at build; gaps will be re-measured on the compiled file.


---

# Cut stage: the compiled Short, measured (2026-10-17)

**Stage:** the compiled master `minutes-of-the-meeting-short.mp4`: 2160×3840, 30 fps, **84.47 s (2,534 frames)**, AAC 48 kHz mono, **-14.6 LUFS, -1.5 dBTP**, 45 caption cues (`.srt`, `.vtt`). One scene rendered frame by frame from a function of time (`build_short.py`), audio on the Kokoro/Whisper clock (`make_audio_short.py`: each script line synthesised whole, 83.7 s of narration, Whisper match 0.962), compiled with `compile_short.py`. Reviewed from 20 frames pulled **from the compiled file** (`_qc/short_cut_sheet_1.png`, `_qc/short_cut_sheet_2.png`) and the measurements below (`proof_short.py`, raw output `_qc/proof_short_output.txt`).

**The Shorts production gate, measured on the compiled file: 12/12 checks pass.**

| # | Check | Result |
|---|---|---|
| 1 | Resolution | 2160×3840 at 30 fps, 2,534 frames |
| 2 | Safe area | ink from 12.5% to 74.7% of the height; 0 pixels in the right rail |
| 3 | Type size | smallest text 30 px at 1080 wide (30, 34, 36, 48, 52, 56) |
| 4 | Every spoken figure on screen when spoken | 19 cue moments checked: the three verdicts, the weights, the pieces and total, SELL in the blank, "about 470 words", the file name, the three questions, the film's title |
| 4b | Comparisons held ≥ 1.5 s | three verdicts together 13.6 s; weights, pieces and total together 4.2 s; the two identical lines 7.3 s; "21 of 23 → 23 of 23" 2.0 s; SELL in the blank 33.0 s |
| 5 | Sources on screen | 6 of 6 phases carry a source line inside the safe area |
| 6 | No hard cuts | largest frame-to-frame change 1.75 grey levels (a cut between scenes would be 20+) |
| 7 | No static stretch over 3 s (measured at 540×960) | longest 2.43 s |
| 8 | Loop-friendly last frame | the line, the blank and the three empty seats at the end differ from the opening state by 0.05 grey levels |
| 9 | Audio | AAC 48 kHz mono, -14.6 LUFS, -1.5 dBTP; one silence of 0.88 s |
| 10 | No foreign identity | no handles on screen; only "Humanitarians AI" is named |
| 11 | Duration and first frame | 84.5 s (cap 180); frame 0 has the headline, the label and the card (0.8% of the pixels) |

## Shorts rubric on the compiled file

| Criterion | Score | Evidence in the master |
|---|---|---|
| Hook | **2** | The first words are the question, and the headline carries it from frame 0; the line types in from 0.3 s |
| Standalone context | **2** | Who (S02, S07), the question (S01), the stock and voices (S02, S03), the answer (S04), what the AI gets (S05), what the full film shows (S06) |
| One arc, own ending | **2** | One render, no cut; the blank is filled in S04, becomes the last line of the minutes in S05, and dissolves back to a blank in S07, so the last frame matches the opening state (0.05 grey levels) |
| Phone legibility | **2** | Safe area on pixels; 30 px minimum; a headline per phase carries the argument muted |
| Pace and retention | **2** | 55 planned events; the longest static stretch is 2.43 s; the longest silence is 0.88 s |
| Trailer function | **2** | S06 says what the full film shows; the closing text gives the exact title, "Minutes of the Meeting: What an AI Is Handed" |

**12/12.**

## What the build found (and fixed)

| # | What | Fix |
|---|---|---|
| 1 | First gate run 9/12: the S02 name line, the channel and the pipeline tag were in the script but not in the scene, leaving a 5.1 s static stretch (and no name on screen until the end) | all three added on their phrases; the stretch fell to 2.97 s |
| 2 | The same run: "21 of 23 → 23 of 23" would have left the screen 1.2 s after it completed | the previews now recede 0.8 s after S07 starts, so the pair is held 2.0 s |
| 3 | 2.97 s was a pass by 0.03 s | a per-seat pulse on "in their own way" took the longest stretch to 2.40 s |
| 4 | The stability gauge overlapped the 0.05 piece in seat 3 (seen on the first test frames) | the gauge moved up; the redundant "out of 1" dropped |
| 5 | The S07 headline repeated the first question word for word | the headline is now "Your next meeting" |
| 7 | **Tanmay: "the transition is not smooth; it lags a bit and then switches; the headings change with a lag."** Two causes, both mine, found by sampling pixels across a fade. (a) Every fade was a pop: Pillow ignores the alpha of a text fill, and an RGBA base replaces pixels instead of blending, so any element with alpha above 0.01 appeared at full strength at once (a seat's tint went from white to full in one frame), and during a headline swap the old line stayed at full strength while the new one popped in over it. (b) The swaps began at the first word of the new line and took 0.4 s on an easing curve, so they landed about 0.3 s after the speech | The canvas is now an RGB base drawn with real alpha blending, text goes through an alpha-scaled mask, every fade starts 0.15 s before the word that names it, and headline and source swaps are one eased progress centred 0.15 s before the cue (old = 1 − n, new = n, with a 16 px slide), done as the first word of the new line is spoken. Frame-to-frame change fell from 5.45 to 1.75 grey levels. Rebuilt, recompiled and the gate rerun: 12/12 |
| 8 | Two gate-script false positives: the commit marker "@ 8665a9f" read as a handle; the SELL hold was measured to an arbitrary boundary | the handle test is now `@\w+`; the SELL hold is measured to the moment the blank dissolves |

## To listen for

- **S01:** the question opens the line; check the pause before "and then a blank" leaves room for the blank to appear.
- **"Forty-five percent... thirty-five... twenty" (S04)** and **"a stability of point oh five" (S03)**: Whisper wrote them as digits; the phonemes were checked.
- **S06:** four previews in about 22 s; check you can follow each as it lands.
- **The pace:** this Short is synthesised whole (3.3 words a second), the Week 26 pace.
