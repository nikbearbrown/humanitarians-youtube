# Frictional Log — four-mornings (Week 26 work video)

**Record provenance:** drafted 2026-10-11 with Claude from this folder's own records (`ANGLE.md`, `FACTCHECK.md`,
`SCRIPT.md`, `short/SCRIPT-SHORT.md`, `PEDAGOGY.md`, the `PROOF-REVIEW*.md` files), after the work was done rather
than while it happened. **Awaiting Tanmay's review.** Every entry points at the record it comes from.

## 2026-10-10 — A second recipe film that couldn't look like the first

- **Work and expectation:** a video about the merged PR #64 whose structure is new. Last week's work video was
  also a Mycroft recipe contribution.
- **Where it resisted:**
  - PR #64 repeats several of last week's mechanics: a `toFixed` tie, the `||` fallback, a parity check.
  - Last week's film had already used three of the obvious frames: "fixture data as a theme", "where I
    stopped" and "provenance read line by line".
- **What was done:**
  - A narration search across every earlier work video (W15–W25, 375 beats) for the ideas #64 actually has.
    Four had zero hits: one workflow calling another; a link held by name only; the same fact written twice;
    zero treated as missing.
  - The structure was taken from the subject: one morning in the life of the dashboard's reader, repeated,
    with a different hand-off slipping each time.
  - Porting, parity and rounding were ruled out as themes. Their only trace is B07's one-cent catch.
- **Decided by:** Claude proposed angles A and B. Tanmay chose A, with the dashboard shown as a labelled illustration.
- **Record:** `ANGLE.md` §§0–2.

## 2026-10-10 — 11/12 to 12/12, and a join only a straight read could find

- **Where it resisted:**
  - The first script's B09 asked a real question but gave no scaffold (active task 1).
  - Reading straight through, B03 ("I kept that behaviour") and B07 ("I broke my own calculation") assumed the
    viewer knew I had rebuilt the math step, but B02 only said "added checks to both".
- **What was done:**
  - B09 gained a strong and a weak answer.
  - B02 gained one clause, "and rebuilt the math step so it runs on test data", and FACTCHECK W3 was extended.
  - B04 was given its source on screen (the original's two lines of Calculate Metrics).
- **Decided by:** Tanmay asked for B09's line with his Gate P PASS, and re-read B02 at Gate P.
- **Record:** `PROOF-REVIEW.md` (reviews 1 and 2), `PEDAGOGY.md`.

## 2026-10-10 — A new component, and a digit that rounded the wrong way

- **Work and expectation:** a dashboard scene for both aspects (`MorningDashboard`), with stills of every beat.
- **Where it resisted:**
  - The NVDA row showed 25,228.12. The merged file holds 25,228.125, and the workflow's JavaScript `toFixed`
    shows that as .13. My display formatting was Python's.
  - 16:9 text was too small, with the bottom third empty.
  - The outro under-filled the frame (Gate V 43% against 55%).
- **What was done:**
  - `money()` now rounds like JavaScript, so the illustration can't disagree with the system it illustrates.
  - The landscape type scale went up about 30%.
  - The outro card title became "Four mornings, one dashboard." (the spoken line didn't change).
- **Decided by:** caught at self-QC, before review. Tanmay approved the 20 stills.
- **Record:** `PROOF-REVIEW.md`, stills stage.

## 2026-10-10 — The right content at the wrong moment

- **Where it resisted:** the stills showed the right things, but frames taken at the spoken moments didn't:
  - B05's two portfolio copies appeared about six seconds after "Edit the shares in the first…".
  - B07's "pass" was already struck through when "It passed. All green." was said.
  - In B03–B06, each hand-off box was lit from the first frame, before the check had been named.
- **What was done:** the component gained optional reveal times (null by default, so nothing else changed): each
  side-by-side item, the strike-through, and each hand-off. The build turns narration phrases into seconds, and
  fails if a phrase isn't in the narration. Each fix was checked on frames rendered just before and just after
  its spoken word.
- **Decided by:** Tanmay asked for the PROOF review on the rendered beats. The fixes were found there.
- **Record:** `PROOF-REVIEW-2.md` (E1–E3).

## 2026-10-10 — Two clocks disagreed in B07

- **Where it resisted:** with the audio measured, the pause-anchored cue clock ran 0.7 s late on "It passed"
  and 1.2 s late on "Now the test". B07's long sentences give it no pauses to anchor to.
- **What was done:** cues now come from Whisper's start time for each cue's first word (`align_words.py`). The
  pause clock stays as the fallback. All 13 long-film cues and 13 Short cues aligned.
- **Record:** `PROOF-REVIEW-2.md`, audio stage.

## 2026-10-10 — The Short, rushed and then rewritten

- **Work and expectation:** a Short that a first-time viewer can follow without the long film. Tanmay had asked
  for this on the topic Short too.
- **Where it resisted:**
  - Draft 1 passed Gate P, but its stills showed what was wrong. There was no frame for 50 seconds (Mycroft first
    appeared in S04). The idea came after the example. "Previous close" was never explained. The record was never
    shown. The ending showed four STOPS boxes the Short never explains.
  - Tanmay's note: "make sure that shorts gives the right context and is not something that is done in a hurry."
- **What was done:**
  - An honest audit, written at the top of `short/SCRIPT-SHORT.md`, then draft 2. It opens with who and what,
    gives the idea and one question before the example, says the rule in plain words, and reads the record out
    line by line as the answer.
  - Re-reading the merged record found half the story missing. GOOGL also used the previous close (its quote had
    no current price), so it's two of five prices, not one. FACTCHECK W20–W22 were added from the merged files.
  - The 9:16 layout was spread across the Shorts zone (Gate V had found 41–51% fill against 55%). A row can now
    light up at its spoken moment.
  - Looking at the frames found two text overlaps (S03, S05) that neither pixel gate catches. Both were fixed.
- **Decided by:** Tanmay's note started it. He passed draft 2 at Short Gate P.
- **Record:** `short/SCRIPT-SHORT.md` (the audit table), `FACTCHECK.md` W20–W22, `PROOF-REVIEW-2.md` (masters).

## 2026-10-10 — Gate F, and a word the voice swallowed

- **Where it resisted:**
  - The first 16:9 compile was refused at Gate F, because the SHOTLIST.md record was missing.
  - In the Short's S01, Kokoro blended "Five stocks, and one total" into "five stocks in one total" (Whisper
    heard "in").
  - The Short now tagged GOOGL, but the long film's B03 didn't, so the two cuts disagreed.
- **What was done:**
  - `make_gate_f.py` writes SHOTLIST, PROMPTS and the Short's FACTCHECK map from the beat sheets.
  - S01 became "Five stocks. One total". Only S01's audio was regenerated (`make_audio.py --only`), then re-timed
    and re-rendered.
  - B03 tags GOOGL as well as META, a picture-only change. Each change re-rendered one beat, kept the other beats'
    render stamps, and was followed by a recompile and a re-check of the master.
- **Decided by:** Tanmay approved both changes.
- **Record:** `PROOF-REVIEW-2.md` (masters).

## 2026-10-11 — Both masters, and one repeated heading

- **Where it resisted:** on the 16:9 master, B08's panel title "Still on trust" sat right above a list labelled
  "STILL ON TRUST".
- **What was done:** the panel was retitled "Both recipes still say DRAFT". B08 was re-rendered alone, and the
  master was recompiled, re-paced, re-normalised and re-checked.
- **Verdict:** long 12/12 and Short 11/12, production gate PASS on both. Every reveal was checked on frames from
  the final files (22 and 19).
- **Decided by:** Tanmay asked for the review and approved the fix. The Short's missing point (no test of the fix
  inside the Short) is recorded as a choice.
- **Record:** `PROOF-REVIEW-3.md`.

## Still open

- Nothing blocks public. Before uploading, the Drive and YouTube links in `README.md` need adding, and the Short's
  `[FULL VIDEO LINK]` needs swapping in.
- Neither pixel gate catches overlapping text, so every frame still has to be looked at. This is recorded in
  `PROOF-REVIEW-3.md` as a tooling limit.
