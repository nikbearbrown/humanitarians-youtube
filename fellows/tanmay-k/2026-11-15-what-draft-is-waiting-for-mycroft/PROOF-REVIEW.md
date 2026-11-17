# Feedback: "What Draft Is Waiting For: Reading a Status as a Claim", Week 31 work video, long (16:9) and Short (9:16), final review on the compiled files (2026-11-17)

**Rubrics:** `PROOF.md` teaching rubric /12 plus production gate (long); the Shorts rubric /12 plus the measured compiled-file gate (Short). Narration of record: the Gate P signed text (`READ-ALOUD.md`, `READ-ALOUD-SHORT.md`). Figures: `FACTCHECK.md` (26 of 26 against `main` @ `894be6c`).
**What was reviewed, in order:** the script (long 12/12 at script level; Short 10/12 until its plan existed), the 21 rendered stills (Tanmay found two layout problems, fixed; long 12/12), the silent motion previews, the audio on the Kokoro `am_onyx` clock, and the compiled files `long.mp4` (3840 x 2160) and `short.mp4` (2160 x 3840). The scores below stand because the compiled files pass the measured gate.

## Verdicts
| | Rubric | Production gate (measured on the compiled file) | Verdict |
|---|---|---|---|
| Long (16:9) | **12/12** | **PASS** on every check below | clear on this review; publishing is Tanmay's call |
| Short (9:16) | **12/12** | **PASS** on every check below | clear on this review; publishing is Tanmay's call |

## Long: rubric
| Criterion | Score | Evidence |
|---|---|---|
| Explicit framework | 2 | The five-rung ladder is on screen from B02 to B10, with markers arriving as each recipe is named (B03 stress-test, B04 contradiction detector, B07 all five). |
| Reusable rubric | 2 | B10: three numbered questions (which rung, what evidence, what was not tested and what would void it) and a task. |
| Worked example | 2 | B03 the stress-test recipe's six dated closing lines against rung one's written test; B04 to B06 the contradiction detector's six gate records, their three fields and their version; B08 this week's 24-row self-test and its "did not test" card. |
| Falsifiability / edge case | 2 | B05 a status states what it covers and what voids it; B06 the records name 0.2.0 and the recipe is 0.2.1, status unchanged; B08 what was not tested. |
| Active task | 2 | B10: write the rung, the evidence and one thing not tested for your own project's last update. |
| Friction | 2 | B06 is where the ladder strains (the record can age while the status word stays put); B04 puts "a person" where the viewer expects "a script". |
| **Total** | **12** | |

## Short: rubric
| Criterion | Score | Evidence |
|---|---|---|
| Hook | 2 | Three plain questions at second zero (works how, tested on what, checked by whom), then the one word that has to answer them. |
| Standalone context | 2 | S01 defines recipe, agent and person; S03 defines status, evidence and sample data before S04 to S06 use them as evidence. |
| One arc, own ending | 2 | S00 question to S08 three questions and the title; one persistent ladder in every frame; the last frame returns to the first. |
| Phone legibility | 2 | Measured on the compiled file: ink x 60..901, y 256..1425 (limit 230..1440); right rail empty; smallest type 34 px logical. |
| Pace | 2 | Measured: longest stretch without a visible change 2.27 s against the 3.0 s limit; no silence of 1 s or more; 3.23 words a second overall. |
| Trailer function | 2 | S08 says and shows the exact title, "What Draft Is Waiting For: Reading a Status as a Claim". |
| **Total** | **12** | |

## Measured gate on the compiled files
```
  [PASS] no foreign handle in any on-screen text: no @handle in either plan (the only @ is the commit notation main @ 894be6c)

LONG 16:9  (long.mp4)
  [PASS] resolution: 3840x2160 (want 3840x2160)
  [PASS] frame rate: 30/1
  [PASS] duration matches plan: 222.43 s (plan 222.40 s)
  [PASS] audio 48 kHz AAC mono: 48000 Hz aac x1
  [PASS] loudness near -14 LUFS, true peak <= -1.5 dBTP: -14.8 LUFS, true peak -2.2 dBTP
  [PASS] frame 0 not black, no black frame anywhere: frame 0 luma 16.3, minimum over 6673 frames 16.3 (background 16.6)
  [PASS] no luma pop between frames (beat cuts excluded): 0 pops; beat-cut steps up to 18.2
  [PASS] no silence of 2.5 s or more in the long film: 0 found
  per beat: longest still stretch (gate 5.0 s)
  [PASS] B00 still stretch: 3.13 s at 2.9 s
  [PASS] B01 still stretch: 2.93 s at 5.0 s
  [PASS] B02 still stretch: 3.87 s at 0.1 s
  [PASS] B03 still stretch: 3.27 s at 8.9 s
  [PASS] B04 still stretch: 2.87 s at 4.7 s
  [PASS] B05 still stretch: 3.73 s at 13.9 s
  [PASS] B06 still stretch: 2.67 s at 19.1 s
  [PASS] B07 still stretch: 3.20 s at 12.9 s
  [PASS] B08 still stretch: 2.33 s at 18.1 s
  [PASS] B09 still stretch: 3.60 s at 5.3 s
  [PASS] B10 still stretch: 3.73 s at 0.4 s
  [PASS] B11 still stretch: 1.93 s at 0.6 s

SHORT 9:16  (short.mp4)
  [PASS] resolution: 2160x3840 (want 2160x3840)
  [PASS] frame rate: 30/1
  [PASS] duration matches plan: 125.80 s (plan 125.80 s)
  [PASS] audio 48 kHz AAC mono: 48000 Hz aac x1
  [PASS] loudness near -14 LUFS, true peak <= -1.5 dBTP: -14.5 LUFS, true peak -1.9 dBTP
  [PASS] frame 0 not black, no black frame anywhere: frame 0 luma 19.8, minimum over 3774 frames 19.8 (background 16.6)
  [PASS] no luma pop between frames (beat cuts excluded): 0 pops; beat-cut steps up to 0.0
  [PASS] no silence of 1.0 s or more in the Short: 0 found
  [PASS] M1 visible change at least every 3.0 s: longest still 2.27 s at 23.2 s
  [PASS] M2 no hard cut: largest one-frame change 1.85 grey levels
  [PASS] M3 loop: last frame equals first: mean abs difference 0.006
  [PASS] M5 ink in safe area, none in right rail: x 60..901, y 256..1425 logical; right-rail ink 0 px

ALL MEASURED GATES PASS
```
Beat-to-beat cuts in the long film are designed hard cuts (the largest luma step at one, 18.2, is a beat boundary); the check counts only steps that are not at a beat boundary.

## Uniqueness (Tanmay's rule)
Angle D passed an audit against all thirteen earlier work videos on claim, teachable move, shape, hook and vocabulary (`ANGLE.md`); the first recommendation failed it. A word-run check of both narrations against the earlier films found only the standing introduction and sign-off.

## What the measuring and reviewing caught before this pass (all fixed, re-measured)
1. **The first recommended angle was not unique** (it was Week 26's claim in a new instance, with Week 25's hook form); replaced by D after a five-axis audit.
2. **B03 promised "I will come back to why" and nothing paid it off** (script review); B09 now does. B06 got the strain beat; B10 got the task.
3. **The first Short draft was rushed and short on context** (303 words); rewritten to 406 words with every term defined before use, planned at 2.9 words a second.
4. **Layout (frames):** B00's quotes ran to the card edge and B04's boxes sat too close to the bottom (Tanmay); B05 said "invented", the record says "synthetic" (a gloss was added); the ladder covered the Short's captions in the first renders (fixed before review).
5. **Motion:** a label counted as a "change" that changed nothing left 4.8 s still in S03; the highlight outline leaked into the Short's right rail; the loop was almost, not quite, closed (0.393 to 0.006); B10 showed only its header for 4.7 s.
6. **Compile:** the long film's true peak was -1.2 dBTP with the standard limit (fails -1.5) and -15.1 LUFS with a much lower one (fails the level); a limit of -2.5 gave -14.8 LUFS and -2.2 dBTP. The handle check first flagged the commit notation "main @ 894be6c" and now looks for a real @handle.

## Not claimed
I measured the audio (loudness, silence, Whisper word check) but did not listen to the full masters; Tanmay's listening is the ear check. Whisper's possible differences (B06 "ladder" heard as "latter", B01 "opened" as "open", B02 "repository's" as "repositories") do not change the meaning in context and the picture shows each word. Four long beats read fast (B10 4.38, B04 4.07, B00 4.04, B06 4.01 words a second against 3.47 for the topic film); Tanmay's decision: compile as is. The recipe this film is about was not edited by the pull request (a rule of the week), so the repository's own check lists ten undocumented flags for the two new scripts; the film presents that as the next edit, already written out.
