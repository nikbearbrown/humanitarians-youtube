# Feedback: "How a Room Changes Music: One Cellist, Seven Concert Halls" — Tanmay Kulkarni, Week 26 topic film

**Stage:** beat sheet, draft 2 (2026-10-10). No audio, no renders. Reviewed from `beat_sheet.json`,
`READ-THROUGH.txt` and `FACTCHECK.md`. PROOF can't see frames that don't exist yet, so the
production gate is checked at **prop level** and re-checked on rendered frames later.

**Verdict:** **cleared for Gate P.** Not yet shippable (unlisted-until-fixed applies to any cut
until rendered frames pass). Teaching **12/12**. Production gate **PASS at prop level**.

One line: this film tries to show *how* a room shapes music, and it gets there by making the
viewer hear one sentence fail and survive. The risk is no longer the argument. It's whether
the two things only sound can prove (the cathedral demo and the clap task) actually work on
the ear.

## Rubric

| Criterion | What it means | This cut |
|---|---|---|
| Explicit framework | Shown as a structure before the examples | **2.** The cold open demonstrates it (0:00–0:20: same room, the speaker changed); B04 puts *the room asks → a player hears → the answer* on screen at 0:20, before Byrne or any study |
| Reusable rubric | A viewer could apply the same axes to a new case | **2.** B13 gives three listening axes and one falsifiable rule (same answers → the room is close to deciding; different → it's only asking). B14–B16 then run the same graphic on birds, Stravinsky and the skip button |
| Worked example | One case walked through live | **2.** The cellist: Quantz's prediction, seven halls, the wet side, then the dry side that breaks the simple story, then his words vs the researchers' reading |
| Falsifiability / edge | Stress-tested against a counterexample | **2.** The U-turn in the driest halls; 8.73% in the lab vs 74.36% for one cellist; two older null studies; the intro study's own null second study, which the B13 rule predicts |
| Active task | The viewer does something structured | **2.** B18–B20: clap and listen (2.5 s hold), say the sentence at your room's pace (4 s hold), then name what the room did. Strong and weak answers are on screen. **Conditional on Gate P** (see The problem) |
| Friction | The viewer must resolve a tension | **2.** Why would anyone slow down in a *dry* room? Held open for one beat (B09), resolved in B10 without putting words in the cellist's mouth |

**Total: 12/12.**

## Production gate (prop level)

Static half run by `proof_check.py` (exit 0). It was mutation-tested on a scratch copy: a missing
quote, a missing figure, a late reveal and a missing source were all caught.

| Check | Result |
|---|---|
| **Sources on screen, not just voiced** | **PASS.** All 17 beats that cite an external FACTCHECK row carry a non-empty on-screen source. Our own material is labelled as ours: "our demonstration" (D01–D04), "Our test" (B13), "Our listening heuristic, not a measurement" (B18–B20) |
| **Evidence legible at the moment of assertion** | **PASS (intent).** Every quote the narration attributes is printed in the same beat (B05 Byrne, B06 Byrne, B11 the paper, B16 Léveillé Gauvin). Every figure spoken is printed in the same beat (1752, 74%, 8.73%, twelve, fourteen, 2003, 1925, 78, three minutes, 303, 1986, 2015, 20 s, 5 s). No reveal is timed past its beat. **Owed:** rendered frames at each cue timestamp, after Whisper alignment |
| **Side-by-side at the moment of comparison** | **PASS.** B10: his words next to the researchers' reading. B11: 8.73% next to 74.36% for the whole beat. B05: Bach's lines next to chant. B23: both slowed passes held together |

**Watch items (eyes-only, at render):**
- B13's rule line is 100 characters and B16's quote is 95. Check both wrap cleanly in 9:16.
- `HallTempo` must render its "Shape only. The paper reports a fitted curve, not these points."
  note at full legibility. A schematic U without that line would show more than the evidence
  establishes (FACTCHECK A9).

## The problem

**Two beats can only pass by ear, and nothing upstream can check them.**

1. **The cold-open demo (D01/D02).** The film's first claim is "Most of that got lost, right?"
   If the normal-pace sentence in the York Minster IR is still intelligible, or the slowed one
   isn't clearly better, the opening asserts something the viewer can't hear: invisible evidence,
   in audio form. **Fix order:** render D01/D02 first, before any other audio or component. Listen,
   and adjust speed or wet level until the difference is obvious to someone who isn't you
   (BEATS.md Part 5). If it can't be made obvious, rewrite B02 to say what *is* audible. [EDIT]
2. **The task (B18–B19).** It earns its 2 only if a first-time listener knows exactly what to do
   and when. Gate P has to judge "In a moment, clap once…" and "Go ahead." aloud, and the 2.5 s and
   4 s holds have to be measured in the compiled cut, not trusted from the sheet. [EDIT]

## Do X next

1. **[EDIT] Pronunciation overrides at audio.** Kokoro's own phonemes are wrong for four names:
   - **Byrne** comes out "BYE-un" (`bˈaɪən`)
   - **Queyras** comes out "KWY-rus" (`kwˈaɪɹəz`)
   - **Jean-Guihen** comes out "JEEN-gih-hen" (`dʒˈiːŋɡˈɪhən`)
   - **Quantz** comes out "kwonts" (`kwˈɔnts`)

   Kokoro accepts phoneme input (`is_phonemes=True`), and the corrected phonemes (`bˈɜːn`, `kɛɹˈɑːs`,
   `ʒˈɑːn ɡiˈɛn`, `kvˈɑːnts`) are all in its vocabulary. Apply them in the local audio wrapper; don't
   respell the narration, or the captions inherit the respelling.
2. **[RESHOOT/NEW SOURCE] Book check** for FACTCHECK A1, A5, A18 (CBGB's "very little echo" is the
   one most at risk). Blocking before audio.
3. **[NEW SOURCE]** Read the 20 s → 5 s intro figures in the paper itself (A20), or keep the Ohio
   State citation visible as it is now.
4. **[EDIT]** Download the York Minster IR, confirm the CC BY 4.0 line on that file, log its hash
   (A23), then render D01/D02 first (The problem, 1).
5. **[EDIT]** Extend the local `pacing_pass.py` to read `hold_after_s` per beat, then measure the
   silence after B18 and B19 in the compiled master.

## What works

- **The form *is* the argument.** The viewer hears the room take the sentence away before
  anyone explains why, so the framework arrives as something already experienced.
- **The turn is real.** "In the driest halls… he slowed down too" is a finding most viewers won't
  predict, and it comes from the paper, not from staging.
- **Attribution discipline in B10.** "That's their reading, not his words" keeps the film to its
  own standard at the exact place it would be easiest to blur.
- **The caveat is earned.** B13's rule predicts B17's null result, so "it still doesn't decide it"
  lands as the test working.
- **The ending answers the viewer.** B20 asks "did you speed up, or slow down?" and the payoff's
  "both slower" is a reply, not a recap.
