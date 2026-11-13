# Feedback: "The Sum Behind the Number" — long film (16:9), rendered beats, review 2

**Rubric:** `PROOF.md` teaching rubric (six criteria, 0–2 each, /12) plus the binary production gate.
**Reviewed:** the 17 rendered 3840×2160 stills (B01–B11, `_stills/`), the narration audio (`mp3/beat-*.wav`, `am_onyx`, 208.4 s with the two holds), Whisper's check of it, and measured checks from `proof_check_beats.py` and the build's collision check. **No video exists yet**, so hold times, motion and fades are scored from the plan, not measured.
**Prior review:** `PROOF-REVIEW.md` (script, 12/12). **Gate P:** passed 2026-10-25 (`GATE-P-SIGNOFF.md`).
**Verdict: clear-for-public at the stills-and-audio level.** Teaching **12/12**. Production gate **PASS on the stills**. The film passes its own standard: every claim carries a visible source or a visible artifact.
One line: this film attempts to teach that a stress-test percentage is a sum of named shocks, and delivers it by rebuilding the workflow's own number block by block, with every term traceable to a committed file.

## Rubric (on the rendered frames)

| Criterion | Score | Reason (frame) |
|---|---|---|
| Explicit framework | 2 | B01 shows the headline number with an empty stack outline labelled "made of: ?" from the first frame; B03-a states the rule on the scenario card ("for each holding, add up the shocks that belong to it") before any worked example. |
| Reusable rubric | 2 | B10 holds the three questions (which shocks, from which lists, has anyone run the adder beside the original) over the opening number, with "A good answer names the terms." |
| Worked example | 2 | B04-a/b/c land −15, −35, −40 one block at a time with the running total (−15, −50, −90); B05-a shows three bars and the arithmetic 36 + 27 + 15; B05-b returns the −78.0% with its parts; B06 repeats the rule on c12 (−45, −30, −30, −30 → 33.75%). |
| Falsifiability / edge case | 2 | B05-a: the third holding is off the AI list (−50, a different sum); B06: one holding takes a third block; B04-c: "another way to combine them is named in the README"; B08-a: weight totals 0.6 and 1.2 accepted and rescaled to 1.0. The weakest of the six. |
| Active task | 2 | B03-b holds a guess ("market −15% → the biggest holding falls how far?") beside an empty bar; B10 hands over the questions. |
| Friction | 2 | B01's opening question; B03-b's guess before B04 answers it. |
| **Total** | **12/12** | |

## Production gate (stills + audio; hold times need video)

| Check | Result |
|---|---|
| Evidence legible at the moment of assertion | **PASS.** `proof_check_beats.py`: **0 flags** on 17 stills (3840×2160, margins ≥ 60 px, an evidence caption on one baseline with the lowest ink at 2,003 px against a 2,060 limit). Contrast on cream: INK 10.98, INK_SOFT 4.73, SPARK_TEXT 4.70; on white cards 11.57 / 4.99. The accent colour (4.05 on white) is used only on large type; numerals on the coloured blocks (3.78–4.34) are large type. |
| Sources on screen, not just voiced | **PASS.** Every beat has an evidence caption naming a committed file or the README; every spoken figure (78, 15, 35, 40, 90, 50, 36, 27, 15, 45, 30, 33.75, 24, 12, 10, 2,200 of 10,000, the weights 0.6 and 1.2, five open items, PR 74) is asserted in that beat's text log by the build. |
| Side-by-side at the moment of comparison | **PASS by arrangement** (B05-a three bars, B06 four bars, B07-a two result columns each in one frame). **Held ≥ 2–3 s is not measurable on stills.** |
| Collisions (new check, after the Short's chip fix) | **PASS.** The build records text, chip, card, block and outline boxes: 0 hard collisions and 0 tight gaps. One tight gap (B08-b's two-line reasons, 6 px apart) was found and fixed. |
| Positive framing (standing instruction) | **PASS.** A scan of both builders and the stills' text shows nothing negative. "Critical" appears only as the workflow's label for losses above 30%. "Defective" appears only in a committed file's name inside an evidence caption. The −90 is shown as the README's own worked example. |

## Audio (measured)

| Measure | Result |
|---|---|
| Narration, whole film | 208.4 s (3:28) including the 3 s guess hold (B03) and the 2 s closing hold (B10) |
| Words per second by beat | 2.0 (B11) to 3.92 (B04); most 3.1–3.6. The brisk spots are B04 (3.92), B07 (3.66) and B08 (3.60) |
| Whisper vs the signed text | 0.805–1.000; every difference is numerals ("78%" for "seventy-eight percent") or hyphenation, none a missing word; "addition" heard as "edition" once (B08), an acoustic ambiguity, since Kokoro's phonemes are correct |
| Mycroft | the override `mˈaɪkɹɔft` is applied at synthesis |

## The problem

None that blocks. The film's one open point is **B07-a's columns**: the committed parity file records only "match: true", so both columns ("original code" and "my copy") show the same committed port output, with the caption "parity row c01: match true". It reads honestly; if you want it to show something else, it is a re-render of one still.

## Findings

1. **B07-a columns (above).** Optional change.
2. **Ticker symbols on screen** (NVDA, AMD, TSM, TSLA, META): each use carries "Invented portfolio · tickers from the workflow's own map"; the narration never says a ticker. The alternative is "chip stock A / B / C" on screen.
3. **B01–B04 are light in the lower third**, by design (content sits above the evidence caption).
4. **B04 is the brisk beat (3.92 words per second).** If it feels fast against the blocks landing in the video, the lever is Kokoro's speed for that beat only; I'd judge it on the video.
5. **Not yet measured (needs video):** holds ≥ 2–3 s for B05, B06 and B07, the fades and block-by-block timing against the words, the loudness of the master, and audio-to-picture sync.

## What works

- The running total is the argument: the number from the first second is rebuilt from its parts by B05 and returns at B10 with its parts faint behind the questions.
- Every number is read from a committed file and asserted on screen; my check of the adder is a result (24 of 24, 12 of 12), not a promise.
- The close hands the viewer a standard ("a good answer names the terms").

## Do next

1. Encode the beats as video and measure hold times, fades, loudness and sync (the production gate, on the video).
2. Re-run this review on the video.
3. Captions and the YouTube metadata.
