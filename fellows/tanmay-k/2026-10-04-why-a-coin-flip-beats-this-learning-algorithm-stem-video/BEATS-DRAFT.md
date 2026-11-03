# BEATS — structure, decisions, runtime

**Draft 2: THE CORRIDOR + THE BLINDFOLD TEST**, 2026-10-01 (draft 1 same day; changes below). `build_beat_sheet.py` generates `beat_sheet.json`, so edit the
script, not the JSON. Every factual line cites a `FACTCHECK.md` row (A1–A25).

**Current state:** 18 beats · 1,051 narration words · ~5:18 estimated at 3.3 words/s (planning rate,
`am_onyx`). No audio yet. **Gate P: PASS** (2026-10-01). Components `Corridor` / `CoinCurve` built in
brutalist.art (local, uncommitted, as W24), registered with 916 variants, and `./art scene-index` re-run.
All 18 beats reviewed as pre-audio stills in both aspects: 8 defects fixed (`PROOF-REVIEW.md` Review 1).

**Working title:** *Why a Coin Flip Beats This Learning Algorithm*. Per PLAYBOOK §1c it names the
subject: a coin vs. a learning algorithm. The outro card keeps the better phrase: "The best move was
a weighted coin."

---

## The shape: THE CORRIDOR

The structure is the subject. The book's own puzzle is the set, and each chapter is **one answer to
it**, tried in order of how sensible it sounds. Every chapter walks the same four squares on screen,
so the viewer sees each answer play out, not just its score.

| # | Answer | Beats | Score |
|---|---|---|---|
| 1 | always right | B03 | never finishes |
| 2 | always left | B04 | never finishes |
| 3 | a learner that scores buttons (Sarsa) | B05–B06 | ≈ −44 |
| 4 | a fair coin | B07–B08 | −12 |
| 5 | the best-weighted coin | B09–B10 | −11.66 |
| 6 | a learner that learns the weighting (REINFORCE) | B11–B13 | finds it |
| 7 | take off the blindfold | B14 | −3: the randomness **disappears** |
| — | rock, paper, scissors (the other outcome) | B15 | randomness **survives** |
| — | the blindfold test, then the goalkeeper | B16–B17 | viewer's case |

- **The turn** is answer 4. The dumbest answer beats the learning algorithm by 3.68×.
- **The payoff** is answers 5–6. The best answer isn't a button, and a different kind of learner finds it unaided.
- **The boundary** is answer 7. The coin was only ever the price of not seeing.
- **The framework** is B02's empty line: every rule is one chance of pressing right. It's on screen
  from 0:23, before any answer is tried (B03 at 0:52), and each answer drops its point onto it as
  its score is spoken (Corridor `scoreline` in B03/B04/B07, then `CoinCurve`). B09 draws the curve
  through the points the viewer has watched land.
- **The rubric** is the blindfold test (B16), built from the film's own two outcomes (B14
  disappears, B15 survives). It's one test with two results, not a numbered list.
- **The task** is the goalkeeper (B17): a new case, with strong and weak answers shown on screen.

## Tone arc

| Beat | Act | Intended state |
|---|---|---|
| B01 | THE PUZZLE | curious, playful (viewer is asked to answer) |
| B02 | THE PLAN | warm, clear (subject in plain words, §1c) |
| B03 | ALWAYS RIGHT | brisk |
| B04 | ALWAYS LEFT | dry, a small joke |
| B05 | THE BUTTON LEARNER | explanatory |
| B06 | MINUS FORTY-FOUR | deflated |
| B07 | THE COIN | **surprised**: the turn |
| B08 | WHY THE COIN WINS | pulling back, careful (cool-down after the peak, §1a) |
| B09 | WEIGHT THE COIN | curious, building |
| B10 | TWO MINUS ROOT TWO | quiet wonder |
| B11 | SOMETHING NEW | explanatory, satisfying |
| B12 | THE COIN LEARNER | building to payoff |
| B13 | WHY IT SITS HERE | reflective |
| B14 | TAKE OFF THE BLINDFOLD | still, honest |
| B15 | THE OTHER OUTCOME | curious, then firm |
| B16 | THE BLINDFOLD TEST | clear, confident |
| B17 | THE GOALKEEPER | direct, inviting |
| B18 | OUTRO | warm |

First-person lines mark real turns only, where I actually ran something: B05, B07, B12, B15.

## Structural differentiation (vs. this fellow's own films, W17–W24)

| Device in earlier films | Present here? |
|---|---|
| Numbered question framework (W17, W18, W21, W22, W23) | **no** |
| "Your turn" apply-the-rubric CTA (W17–W23) | **partly, knowingly.** B17 is a viewer task, which 12/12 requires. It is *not* a set of numbered questions applied to a case: it's the film's single test, applied to one new case, and the beat is named for the case (THE GOALKEEPER), not "your turn". If Tanmay feels it reads as the old ending anyway, the trade-back is to cut B17 and accept Active task = 1 |
| Rooms/house metaphor (W24), witnesses (W22), lineage (W23), instrument readings (W20) | **no** |
| Two side-by-side columns (W18) | **no** |
| **A "dial" device (W20: "one dial on the whole thing", "dial hard left")** | **removed in read-through.** The coin is *weighted*, never "dialled" |
| A puzzle posed to the viewer, answered by elimination on one reusable set | **new in this film** |

## Read-through log (PLAYBOOK §1e), draft 1

Read straight through with running timestamps.

1. **Reuse, W20.** "Turn the coin into a dial" / "tune the dial" echoed W20's central device. Now
   "weight the coin" / "learn the coin's weighting"; the chart component is renamed `CoinCurve`.
2. **Reuse, W17 B9 + W24 B12.** "But hold on." opened the cool-down beat in both. B08 now opens "Now,
   the coin isn't clever."
3. **Reuse.** "on purpose" appears in 7 earlier beats (W19–W24), so B15 says "deliberately".
4. **Accuracy, B08.** "The harder a rule leans one way, the longer it bounces" is false between 50% and
   58.6%: leaning slightly right *helps*. Now "Lean hard on either button and you pay for it,
   bouncing or stuck."
5. **Accuracy, B13.** "There, the reason is an opponent." The book files poker under the *same*
   imperfect-information reason (Sec. 13.1), so the line now says poker **adds** an opponent.
6. **Overclaim, B02.** "to explain why its thirteenth chapter exists" → "to show what its
   thirteenth chapter can do that the earlier chapters can't" (Sec. 13.1 lists other advantages too).
7. **Setup/payoff, B05 → B14.** B14's "a separate score for each square" had no setup. B05 now says
   "Just one score per button, since every square reads the same."
8. **Logic, B10.** "Leaves it as an exercise. *Which means*… irrational" was a non sequitur. Reordered
   so irrationality follows from the exact form.
9. **Calibration.** "about minus eleven point six six" (B10) loses "about"; "it was scoring" (B12)
   → "averaging", since the −13 is a 30-run block mean.
10. **B02 subject.** "a textbook on how machines learn by trial and error" → "about machines that learn
    from rewards". It no longer leans on a book quote that was checked from memory, not from the page.

## Read-through log, draft 2 (the 12/12 pass)

1. **Hole in the puzzle, B01.** A blindfolded person could *count steps* and open-loop right-left-right
   in 3 steps, with no coin. The book's learner has no memory (p. 197). B01 now says "you can't keep
   count of your steps", and A20's "every rule is a coin" depends on it.
2. **Overclaim, B15.** "Only an even three-way split broke even": we tried three strategies, not all.
   Now "The even three-way split broke even."
3. **Overclaim, B15.** "Take the learning opponent away, and every strategy breaks even" was measured
   against a *random* opponent, not any non-adapting one. Now "swap in an opponent that just plays at
   random, and always rock does as well as anything."
4. **Overclaim, B16.** "it works anywhere" → "you can carry it to other problems". The survive branch
   says "look for" an exploiter. It's a heuristic, not a theorem (FACTCHECK A20–A25 note).
5. **TTS, B17.** A spoken quotation with no quote marks → "Saying it's random because it's uncertain
   doesn't count."
6. **B02.** "learn from rewards" → "learn by trial and error", now checked on the page (A25, p. 1).
7. **Poker moved** from B13 to B15, where it belongs with the outcome it illustrates. B13 now ends on
   the question B14 answers ("Why did the best answer have to be random at all?").

## PROOF gate, draft 1 (superseded below)

**Production gate: PASS on paper.** It has to be re-run on rendered frames at the moment of assertion.

- **Sources on screen.** Every claim beat carries a `source` prop. Book claims cite Sutton & Barto (2018)
  with page numbers. Our numbers say "our runs / our calculation", and the seeded sample walks say they are samples.
- **Voiced quotes.** B11's "in this chapter we consider something new" is on the card with p. 321.
  B13's paraphrase card is labelled "(paraphrased)".
- **Side-by-side at comparison.** B07 shows −12.00 next to −44.21. B14 shows −3 next to −11.66. B06 shows both
  ε-greedy markers together. All are held for the beat.
- **Moment of assertion.** Every reveal is cued to its phrase (`*Cue` → absolute seconds, §2), and the cues
  get retimed on the Whisper clock after audio.

**Teaching rubric, estimated: 9/12.**

| Criterion | Score | Why |
|---|---|---|
| Explicit framework | 1 | The puzzle and "one rule for all squares" are on screen from B01. The weighting curve, the real framework, arrives at B08–B09, after two examples. Traded knowingly, as in W24: elimination order *is* the structure |
| Reusable rubric | 1 | "Ask what it can't see" is a portable question, not a scored rubric |
| Worked example | 2 | Every answer is walked live on the corridor |
| Falsifiability / edge | 2 | B14 removes the effect by changing one thing (sight) and measures it |
| Active task | 1 | The runnable code plus one change ("give it one more clue"). It becomes **2** only if the code is actually published and linked |
| Friction | 2 | B01 asks the viewer to answer, and B07 contradicts the likely answer |

## PROOF gate, draft 2 (2026-10-01)

**Production gate: PASS on paper.** Every new claim beat carries its source: B14 Sec. 17.3 p. 465 plus our
run, B15 `rps.py` plus Sec. 13.1, B16 both runs plus Sec. 17.3. Side-by-side: B14 shows −3 next to −11.66,
B15 shows all three strategies on one card, and B16 shows both outcomes with their numbers. All cues
resolve inside their beats (checked).

**Teaching rubric, estimated: 12/12.**

| Criterion | Score | Why |
|---|---|---|
| Explicit framework | 2 | B02's line ("every rule is a coin") is on screen from 0:23, its caption at ~0:35, before the first answer (0:52). Every answer then lands on it |
| Reusable rubric | 2 | The blindfold test (B16) is stated as one operation with two readable outcomes |
| Worked example | 2 | Every answer is walked live, and the test is worked on two cases (B14, B15) before the viewer gets one |
| Falsifiability / edge | 2 | B15 is the case where the test gives the *other* answer, measured, so the test sorts cases rather than being fitted to the corridor |
| Active task | 2 | B17 gives a new case, the exact operation, what a strong and a weak answer look like, and an optional code path |
| Friction | 2 | B01 puzzle; B07 contradicts the likely answer; B17 the viewer must decide |

Two caveats, stated plainly:
- **The 12 is my estimate on the script.** PROOF scores rendered frames plus narration, so it isn't
  real until the previz exists.
- **The framework lands at ~0:23–0:35, not PROOF's "~20 s".** It does land before any example, which
  is the rule's purpose. Pulling it earlier would mean cutting the presenter intro that §1c requires.

## Components

**Library-first check (`Root.tsx`, 724 registered ids):** nothing draws a gridworld or corridor.
`CrossSectionCurve` / `ContrastCurves` (W20's own) are the nearest charts. Reusing one would bring W20's
look back (see the dial note above), so the curve is a new, plain component.

- **`Corridor` (new).** Four squares, a token, a step counter.
  - `view`: `viewer` (the swapped square is marked for us), `blind` (every square drawn alike), `sees`
    (each square labelled).
  - `path` animates one square per `stepSeconds` from `walkAt`. `loopPath` handles the never-ending
    answers.
  - Dual-aspect from line one: a row in 16:9 and a column in 9:16 (PLAYBOOK §2: vertical flow when
    `height > width`).
  - Neutral defaults, absolute-second timing.
- **`CoinCurve` (new).** The exact value curve from `experiment/results.json`.
  - x = chance of pressing right, y = score.
  - Both ends are drawn as "never finishes", not as a number.
  - Markers appear on their cue, and the best weighting gets a single accent.
  - `showCurve: false` draws the axis and markers only (B02–B08). B09 draws the curve in on its cue.
  - Same dual-aspect rules as `Corridor`.
- **`Corridor.scoreline` (new prop).** A thin strip of the same axis under the corridor, carrying the
  markers placed so far, with the newest on its cue. This is how B03/B04/B07 put their points on the
  framework while the corridor is still the main picture.
- **Existing:** `ClaudeArtifactCardFullOFL` (B05, B11, B13, B15, B16, B17) and `ClaudeTitleOutroFullOFL`
  (B18), as W24 shipped them. Six cards is a lot. B16 (the test) is the strongest candidate for a custom
  blindfold-on/off visual if the cards feel samey in previz.
- **Skin warning to expect.** B01 opens on `Corridor`, not `ClaudeComposerAsk` ("COLD OPEN LAW").
  This is deliberate: the puzzle has to be the first thing seen. W24 shipped with the same class of warning.

**Third-party images: none.** The book is CC BY-NC-ND, so its figures are never reproduced
(FACTCHECK §C). Every chart is drawn from our data.

## The Short: its own script (draft, needs its own Gate P)

One arc, its own ending, in portrait `Corridor` and `CoinCurve`. State carries across cuts: the same
corridor, with the token where the last beat left it.

- **S1, the trap:** "Four squares. The second one swaps your buttons, you can't see which square
  you're on, and you can't count your steps. Always press right? You bounce between the first two
  squares. Forever."
- **S2, the learner:** "A classic learning algorithm settles on mostly right. Every step costs a point,
  and it scores about minus forty-four."
- **S3, the turn:** "Now flip a fair coin instead. No learning at all. Minus twelve."
- **S4, the number:** "And the best isn't fifty-fifty. It's a coin weighted to land right two minus root
  two of the time. Fifty-eight point six percent. A different kind of learner finds that on its own."
- **S5, the ending:** "But let the player see which square it's on, and the coin is useless. Right,
  left, right. Three steps. The randomness was the price of the blindfold."

Roughly 110 words, about 35–40 s. It ends on its own line, not on a pointer to the long video. The
endcard carries the title.

## Decisions (Tanmay, 2026-10-01)

1. **Title:** *Why a Coin Flip Beats This Learning Algorithm*. The outro card keeps "The best move was a
   weighted coin."
2. **Code:** publish `experiment/corridor.py` and `experiment/rps.py` with the video, so B17's "linked
   below" is true. They're pushed with the deliverables at delivery time, and the link goes in the
   YouTube description.
3. **Voice:** `am_onyx`.
4. **B17:** kept, so the film stays at an estimated 12/12.

## Next (front-loaded, per W24's time log)

Gate P read-sheet → Tanmay's read → `Corridor` + `CoinCurve` as stills in **both** aspects → audio →
Whisper-clock cues → render once.
