# Frictional Log — the-rally-has-a-clock (Week 29 topic video)

**Record provenance:** drafted 2026-10-30 with Claude from this folder's own records (`TOPIC-DECISION.md`, `ANGLE.md`, `FACTCHECK.md`,
`AUDIO-CHECK.md`, the proof reviews, the gate logs), after the work was done rather than while it happened. **Awaiting Tanmay's review.**
Every entry points at the record it comes from.

## 2026-10-30 — A topic nobody had taken, and a duplicate that looked unique
- **Work and expectation:** draw the week's topic at random from the `claude-for-<topic>` collections, check nothing else covers it, with git commands that only read.
- **Where it resisted:** the first draw, `claude-for-computer-science/cli-int8-mash`, passed my pool filter but exists as three variant folders (`claude-liam-cli-`, `nbb-cli-`, `cli-`) beside a related fellow video on the same subject. The filter stripped only one variant prefix at a time, so the stacked prefixes hid the duplicates.
- **What was done:** the filter was fixed to strip prefixes repeatedly, the draw was rejected before any angle work, and six real singleton topics remained; the redraw landed on `claude-for-design/pong`. A plain `git fetch` refreshed the local remote refs (the one non-read-only command, flagged); the rest was `ls-tree`/`show`/`grep` and one pass over 60,568 text files on all 104 refs.
- **Record:** `TOPIC-DECISION.md`.

## 2026-10-30 — A claim that needed a number
- **Work and expectation:** the essay's "no perfect defense" is a sentence; the film needed to say when it is true.
- **Where it resisted:** it is true only under conditions (paddle speed against ball flight time; a ball that speeds up). Nothing in the folder gave the threshold, so it was derived and then tested: a closed form, a brute-force search over every aim, a narrower aim, a different field, and a ball that never speeds up. Every prediction matched the search; none was fitted.
- **What it changed:** the script's "half the field, less its own height" was wrong (the exact figure is height minus paddle, over two); shot numbering was off by one (the simulation counts from zero); two unsupported lines about real rally length and designer intent were removed. All caught at the read-aloud and fact-check, before audio.
- **Record:** `FACTCHECK.md`, `PROOF-REVIEW-1.md`, `PROOF-REVIEW.md`.

## 2026-10-30 — Three words the voice would not say
- **Work and expectation:** the signed narration, spoken by the voice, matches the text.
- **Where it resisted:** two Whisper models both heard "lest" for "less", "broken" for "broke in" and "like" for "liked": sound-alike joins that a text check cannot see.
- **What was done:** three one-word edits, approved by Tanmay, only those beats regenerated, Gate P re-signed for those lines. Two now match exactly; one differs by a weak "and".
- **Record:** `AUDIO-CHECK.md`, `GATE-P-SIGNOFF.md`.

## 2026-10-30 — Cues on a clock that spells numbers its own way
- **Work and expectation:** every picture change lands on its word.
- **Where it resisted:** Whisper writes "sixth" as "6th" and "point two two five" as "225", so the stored sentence times collapsed for exactly the count-off lines.
- **What was done:** a cue script normalises numerals and ordinals before aligning; the hold-then-answer in the closing beat is anchored to the end of the 5 s hold; spot-checked against the larger model and the audio's energy envelope.
- **Record:** `cues.py`, `AUDIO-CHECK.md`.

## 2026-10-30 — What the measurements found before anyone watched
- **Where it resisted:** a digit swap showed 4 and 5 overlapping; one beat sat still for 10.5 s while the narration worked through "can it, can't it"; the narration said "that bar keeps sinking" over a chart with no bar; the Short's gate failed three times (the ending still for 5.8 s, a 5.0 s and a 3.2 s stretch) and once on peak level (-1.4 against -1.5 dBTP). One failure was in the test, not the picture.
- **What was done:** each was fixed and re-measured; the long film's audio was recompiled for the same peak margin.
- **Record:** `PROOF-REVIEW-FRAMES.md`, `PROOF-REVIEW-SHORT-VIDEO.md`.
