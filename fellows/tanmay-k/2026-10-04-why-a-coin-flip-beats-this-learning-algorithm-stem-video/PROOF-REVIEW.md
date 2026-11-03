# PROOF-REVIEW — Week 25 topic video

## Review 1: pre-audio stills, both aspects (2026-10-01)

**What was reviewed.** 36 stills: every beat in 16:9 and 9:16, rendered with the beat's **real props**
from `beat_sheet.json` (PLAYBOOK §4). `Corridor` / `CoinCurve` beats were sampled at the moment of
assertion: the last timed element + 1.6 s, on the planning clock. Cards were sampled at 85% of the
beat, once their stagger has settled. Renders are at half scale for review. They are QC stills
(`render_stills.mjs`), not beat renders: beat renders go through `remotion_scenes.py` after audio, per
the toolkit's CLAUDE.md. Contact sheets: `_stills/contact-16x9.png`, `_stills/contact-9x16.png`.

**Timing caveat.** Cues are on the 3.3 words/s planning clock. They get re-resolved on the Whisper clock
after audio, and moment-of-assertion sampling is redone then.

### Defects found and fixed (all [EDIT], all re-rendered and re-checked on the frame)

| # | Beat / aspect | Defect | Fix |
|---|---|---|---|
| 1 | B07 both | Scoreline: "never finishes" end labels collided with −82 / −44 ("never fi−82shes"), making the framework strip illegible at its moment | Never-finishing answers merge into the end labels under the axis ("never right: never finishes"); finite scores label above |
| 2 | Corridor 9:16 | Scoreline and square labels ≈ 7 pt at phone width (W24's defect class) | Label scale ×1.5 portrait / ×1.25 landscape; portrait squares larger |
| 3 | B10 | "2 − √2" as plain text, no radical bar, with equation and prose on one caption line (MATH-TYPESETTING.md) | `CoinCurve.equation`: italic *p*\*, a radical with a drawn bar, ≈ for the approximation. Algebra logged in FACTCHECK A7 |
| 4 | B10 | Best-point label sat on its own ring | Label raised; page-colour halo on all chart labels |
| 5 | B08 | Heading "Lean harder, score worse" restated the claim the read-through removed: false between 50% and 58.6% | "Commit hard, and you pay for it" |
| 6 | B14 | Token (accent) vanished into the goal square (also accent) at the payoff moment | Goal goes ink when reached; the accent stays on the token |
| 7 | B10/B12 9:16 | Best-point label collided with the "never finishes ↓" end labels | End labels moved to their own row above the plot area |
| 8 | B10 | The *p*\* asterisk rendered as a dot | Superscript enlarged; checked on a 3× crop |

### Production gate on the stills: PASS (pre-audio)

- **Evidence legible at assertion:** every number in the narration is on the frame when sampled, and
  labels are readable at half scale in both aspects.
- **Sources on screen:** all 18 frames carry a source or an "our runs / our calculation" line. B11's
  voiced quote shows its page (p. 321).
- **Side-by-side:** B07 −12.00 next to −44.21; B14 −3 next to −11.66; B06/B08/B09 all markers on one
  chart; B15 all strategies on one card; B16 both outcomes together.
- **No third-party images; open-licence fonts only** (OFL compositions).

### Known, accepted

- **Cards in 9:16** (B05, B11, B13, B15–B17) run into the bottom Shorts zone. They're used only in the
  16:9 long film. The Short is built from `Corridor` / `CoinCurve` only, so this doesn't reach a
  portrait frame. Re-check if that changes.
- **Six `ClaudeArtifactCardFull` beats** number their lines (1, 2, 3). That's the component's own style
  and the same as W24. It isn't the "numbered framework" device: the numbers are line markers, not
  axes.
- **Skin warning to expect:** B01 opens on `Corridor`, not `ClaudeComposerAsk`. Deliberate (BEATS-DRAFT).

### Still to check at the next stage

- Equation frames at 15/50/85% of B10 in the final aspect (MATH-TYPESETTING.md), on rendered beats.
- Walk timing: the token's steps against the spoken "Square one, right… Square two…" in B03, on the
  Whisper clock.
- Per-frame luma scan of the master (W24 fade-to-black lesson).

---

## Review 2: every beat, both cuts, full resolution, pre-audio (2026-10-01)

**Asked for by Tanmay:** one picture per beat to go through himself, plus the same PROOF pass as
before audio. 24 stills in `_review/`: **B01–B18 at 1920×1080** (long form, 16:9) and **S01–S06 at
1080×1920** (Short, 9:16). Each was rendered with the beat's real props at its moment of assertion on the
planning clock (`make_stills_plan.py` → `render_stills.mjs`).

**What changed since Review 1.**
- The Short now has its own sheet (`short/build_short_sheet.py`) and presenter credit at both ends,
  as in the W24 Short: S01 opens with Tanmay's name, and S06 signs off with it and points to the full
  video.
- S02's step counter was removed (finding R2-1 below).

### Finding

| # | Beat | Defect | Fix | Tag |
|---|---|---|---|---|
| R2-1 | S02 | The seeded 22-step sample walk showed "steps 22 · score −22" beside the caption "About −44". The frame contradicted its own claim | Counter hidden for this sample; the scoreline carries the −44. Re-rendered and checked | [EDIT] |

### Per-beat gate, long form (16:9)

| Beat | Claim at this moment | On screen, legible | Source on screen | Side-by-side | Verdict |
|---|---|---|---|---|---|
| B01 | the puzzle's rules; same reading, no counting | corridor, swapped tag, caption | S&B Ex. 13.1 p. 323 · p. 197 | — | PASS |
| B02 | every rule is a coin (framework) | empty line, both ends, caption | S&B Ex. 13.1 | — | PASS |
| B03 | always right never finishes | looping token, climbing counter, end label in accent | rules of Ex. 13.1 | — | PASS |
| B04 | always left never finishes | token bumping the wall, both end labels | rules of Ex. 13.1 | — | PASS |
| B05 | 30/30 runs mostly right | card, three lines | our runs + settings | 30 vs 0 on one card | PASS |
| B06 | ≈ −44 / ≈ −82 | both markers on the chart | S&B p. 323 + our exact values | both together | PASS |
| B07 | fair coin −12, 3.68× | −12.00 next to −44.21; scoreline | our exact value; walk labelled a sample | yes, both numbers | PASS |
| B08 | commit hard, you pay | heading now true; three markers | our exact values | three together | PASS |
| B09 | best weighting is not 50% | full curve through the placed points | our exact values | — | PASS |
| B10 | p* = 2 − √2 ≈ 0.586; book "about 0.59" | **typeset** equation; book's wording in caption | S&B p. 323 + Ex. 13.1 p. 324 | ours next to the book's | PASS |
| B11 | voiced quote, p. 321 | quote as the card heading | p. 321 + the gradient-bandit exception | — | PASS |
| B12 | REINFORCE from −82 to an average of 58.6% | start marker; average on the best point; 53–65% range | our runs + settings | start and end together | PASS |
| B13 | no natural way / policy methods can | card, paraphrase labelled | Sec. 13.1 p. 323 (paraphrased) | — | PASS |
| B14 | 30/30 right-left-right → −3; book: fixed rule exists | walk to the goal (token visible), caption | our runs + Sec. 17.3 p. 465 | −3 next to −11.66 | PASS |
| B15 | RPS: −0.999 / −0.29 / ≈ 0; random opponent ≈ 0 | card, four lines | rps.py + Sec. 13.1 (poker) | all strategies together | PASS |
| B16 | the blindfold test | card: rule + both outcomes with numbers | both scripts + Sec. 17.3 | both outcomes together | PASS |
| B17 | the task: strong vs weak answer | card | (a task, not a claim) · code path shown | strong next to weak | PASS |
| B18 | outro | title, handle, name | — | — | PASS |

### Per-beat gate, the Short (9:16)

| Beat | Claim at this moment | On screen | Source on screen | Shorts zones | Verdict |
|---|---|---|---|---|---|
| S01 | rules; always right never finishes; **name spoken** | corridor, loop, scoreline end label | S&B Ex. 13.1 | heading ≈14% from the top; source above the bottom 25% | PASS |
| S02 | the learner ≈ −44 | −44 on the scoreline, caption with 30/30 | S&B + our runs; walk labelled a sample | ok | PASS (after R2-1) |
| S03 | fair coin −12 | −12 beside −44 on the same strip; counter matches (−12) | our exact value | ok | PASS |
| S04 | best p* = 2 − √2 ≈ 0.586; learner finds it | curve with the carried scores; typeset equation | S&B + our runs | ok | PASS |
| S05 | see the state → −3 | walk to the goal, caption −3 vs −11.66 | our runs + Sec. 17.3 | ok | PASS |
| S06 | sign-off + pointer; **name on the card and spoken** | full title, handle, name | — | subline at ≈74% height, inside the safe area but close: **re-check on the final cut** | PASS (watch) |

### Production gate: PASS on all 24 stills (pre-audio)

Every spoken number is on the frame. Every claim beat shows its source. Every comparison shows both
sides together. No third-party images; open-licence fonts only.

### Teaching rubric

- **Long form: 12/12 (estimate on stills).** Unchanged from BEATS-DRAFT. The framework is on screen at
  B02, before the first answer; the rubric is B16; falsifiability is B14 + B15; the task is B17.
- **Short: 9/12.** It's scored separately, as W24 did:

  | Criterion | Score | Why |
  |---|---|---|
  | Explicit framework | 2 | The scoreline from S01 is the line every answer lands on |
  | Reusable rubric | 1 | "The randomness was the price of the blindfold" is portable, but the two-outcome test is only named in S06 |
  | Worked example | 2 | Each answer walks the corridor |
  | Falsifiability | 2 | S05 removes the effect by giving sight |
  | Active task | 0 | No task. A ~50 s Short points to the full video's task instead (S06) |
  | Friction | 2 | The coin beats the learner (S03) |

  It's a trailer by design, and complete as a story. Adding the goalkeeper task would push it past one
  arc, so I'd keep 9/12 here and let the long form carry the 12.

### Carry-forward checks for after audio

1. S02 → S03: the S02 walk ends at the goal and S03's walk restarts at square 1. It reads as a new
   attempt, but check the cut once timing is on the Whisper clock.
2. S01's loop: the token should be at square 1 when S01 ends, so S02 starts where S01 left off. Set
   from measured audio.
3. S06 subline at ≈74% height: verify against the YouTube Shorts overlay on the final.
4. Everything in Review 1's "still to check" list.

---

## Review 3: the Short rewritten to carry the full film's context (2026-10-01)

**Tanmay's bar:** the Short must give real context of the full-length video, not 3–4 beats stitched
together.

**Verdict on draft 1: it failed that bar.** Three reasons:
- S01–S05 mapped one-to-one onto B03 → B05/B06 → B07 → B10 → B14: the long form's beats in their own
  order, shortened. That's the pattern rejected in W24.
- The film's actual teach, the blindfold test with two outcomes, never appeared. S06 then named "the
  test that tells the two kinds of randomness apart" to viewers who had never heard of it.
- The joins were cuts, not reasons ("Now flip a fair coin instead").

**Draft 2: one question, carried through.** "Why does a coin beat a learning algorithm here?" Each beat
answers the line before it:

| Beat | Job | Hand-off |
|---|---|---|
| S01 | name + the result as the hook (3.68×) | "Here's why, and what it says about randomness." |
| S02 | the puzzle, credited to the book | "So whatever you press, you press everywhere." |
| S03 | why the learner fails: it hunts for a best button | "There is no best button here." |
| S04 | the coin, then the best coin (2 − √2), and that this is chapter 13's subject | the number |
| S05 | **the full film's thesis:** give it more information; the coin vanishes (sight) or survives (an opponent), both on screen | "Lean on rock, and you get punished." |
| S06 | the portable question + pointer + name | "ask what the player can't see, or who's watching" |

240 words, ~73 s estimated. Lint: 0 flags beyond the name checklist.

### Findings this pass (all [EDIT], re-rendered and checked on the frame)

| # | Where | Defect | Fix |
|---|---|---|---|
| R3-1 | S04 | "A fair coin takes about twelve": twelve of what (unit drop by ear) | "gets there in about twelve steps" |
| R3-2 | S02/S05/S06 | Three sentence-openers "So" in 50 s | S06 → "Next time the best move is random…" |
| R3-3 | S05 | The still showed only the first outcome: the sampler ignored the outcome rows' cues, so it missed "the coin survives", the beat's point | `make_stills_plan.py` now includes outcome cues |
| R3-4 | both builders | A carried marker (cue `None`) was resolved to 0.6 s, so carried scores popped in after every cut, and two sharing 0.6 s were both accented as "newest" (S02) | `None` stays `None` = on screen from frame 0. Long-form narration fingerprint unchanged (`0670e387…`) |

### Gate on the new Short stills: PASS

Every spoken number is on its frame. S05 shows both outcomes together, with numbers and sources (our
runs + Sec. 17.3). Every frame carries its source. The accent marks only the new element. Everything
sits inside the Shorts safe area (S06's subline still to verify on the final).

### Rubric, Short draft 2: 11/12 (was 9)

| Criterion | Score | Why |
|---|---|---|
| Explicit framework | 2 | The scoreline from S01 carries every score |
| Reusable rubric | 2 | The test is stated (S05) and handed over as a question (S06) |
| Worked example | 2 | The corridor walked; both outcomes shown |
| Falsifiability | 2 | S05: the same test, two different results |
| Active task | 1 | S06's question is portable, but the scaffolded task lives in the full video |
| Friction | 2 | The coin beats the learner (S01, S03) |

### Gate P

The Short's narration is a full rewrite, so **the whole Short (S01–S06) needs Tanmay's read**, not only
S01/S06. The long form's signature is unaffected.

---

## Review 4: chart labels off the line (Tanmay, 2026-10-01)

**Tanmay's note (B09, B12):** "try not [to] place the text on the line, we can place it next to the dots."
Near both ends the curve is steep, so the "mostly left", "mostly right" and "start: −82" labels sat on
it.

**Fix (`CoinCurve.tsx`, one rule for every chart):**
- A marker within 20% of either end puts its label **beside** its dot, on the side away from the
  curve (right of a left-end dot, left of a right-end dot), vertically centred.
- In the flat middle a label sits above its dot, or below it next to the best point. That's how the
  orange best/average labels already worked.

**Checked on the frame:** B06, B08, B09, B10, B12 (16:9) and S04 (9:16), all re-rendered. No label touches
the curve or a dot in any of them. B02 has no markers. Narration is unchanged, so neither Gate P is
affected by this.

---

## Review 5: the Short to 12/12 (Tanmay, 2026-10-01)

**The missing point was Active task (1).** S06's question was portable, but it handed the viewer nothing
structured to do.

**Change:** S06 becomes **THE TASK**: the portable question, the goalkeeper case, the test as one
question, and what a strong and a weak answer look like, each on screen at its cue. This is the long
form's B17, compressed and already approved there. A new **S07 THE CLOSE** carries the pointer to the
full video and Tanmay's name. 7 beats · 276 words · ~84 s estimated. Lint: 0 flags beyond the name
checklist.

**Component:** `Corridor.showCorridor = false` gives a heading + outcome-panel text frame that stays
inside the Shorts safe area. (`ClaudeArtifactCardFull` spills into the bottom 25% in 9:16, so it's not
used.) Additive; no other beat changes.

**Checked on the frame:** S06 shows all four rows, legible, with the case question accented, and the
source line ends above the bottom 25%. S07 shows the title, handle and name.

### Rubric, Short: 12/12 (estimate on stills)

| Criterion | Score | Why |
|---|---|---|
| Explicit framework | 2 | The scoreline from S01 carries every score |
| Reusable rubric | 2 | The test, stated (S05) and handed over (S06) |
| Worked example | 2 | The corridor walked; both outcomes shown |
| Falsifiability | 2 | S05: the same test, two different results |
| Active task | 2 | S06: a new case, the exact question, strong vs. weak answers on screen |
| Friction | 2 | The coin beats the learner (S01, S03); S06 the viewer must decide |

As with the long form, the 12 is confirmed only when PROOF scores the rendered cut.

---

## Review 6: generated audio (2026-10-01)

**Generated:** Kokoro `am_onyx`, 25 beats, $0. Long form **297.1 s (4:57)**; Short **83.9 s**. Durations are
the master clock (`mp3/timings.json`, `short/mp3/timings.json`).

**Checks run (front-loaded, per W24's time log), before any render:**

| Check | Result |
|---|---|
| Words/s per beat (desync test) | 3.0–4.2 w/s. B01 (4.23) is fast but Whisper matched it **100%**: real pace, no dropped words. B18/S07 (2.2–2.5) are sign-offs |
| `silencedetect -40 dB, 0.55 s` | 5 pauses, 0.55–0.63 s, all at sentence or idea boundaries (B07's follows "Minus twelve.", the deliberate beat). No mid-phrase holes |
| Whisper `base.en`, word-aligned against `narration_text` | 25/25 beats ≥ 90.9% matched; every miss inspected (below) |
| Whisper tail on B15 | "We'll see you in a second" at 25.92 s: zero-length words on the trailing silence. Hallucination, not audio |

**Defects Whisper found, the class a page lint can't see:**

| # | Beat | Heard as | Fix |
|---|---|---|---|
| A-1 | B09, B11, S04 (+ B02) | "weight" → **"wait"**, "weighting" → **"waiting"**, "weighted to" → **"waited to"** | "bias" / "setting" / "biased coin, set to" |
| A-2 | B06 | "the book's number too" → **"number two"** | "The book reports the same number." |
| A-3 | S04 | "land right two minus root two" → **"right to minus root 2"** | percentage first: "…about fifty-eight point six percent of the time: two minus root two, exactly." |

All five beats were regenerated and re-transcribed, and each is now heard as written. `gate_p_lint.py`
HOMOPHONES gains weight / weighting / weighted / too. My earlier lint caught "weigh" but not "weight",
and that miss is logged here. On-screen headings follow the spoken words ("Every setting of the coin",
"The best setting"). The outro card keeps "weighted coin", which is printed, not spoken.

Everything else Whisper "missed" is its own formatting: digits for spoken numbers, "Kolkarni" for
kˈʌlkɑːɹni (Kokoro's pronunciation is correct), "write" for "right".

**Gate P re-opened for B02, B06, B09, B11, S04 only** (narration changed). Every other line is word-for-word
as signed.

**Next:** cue timing on the Whisper clock → render each beat once → compile → full PROOF on the first
compile (luma scan, loudness to −14 LUFS target before assembly per the W24 lesson, Shorts overlay).

---

## Review 7: first compile, both cuts (2026-10-01)

**Pipeline.** Whisper-clock cues (`cue_align`) → `remotion_scenes.py` per beat, 4K → `compile.py`
(16:9 `--height 2160`, Short `--height 3840`) → `pacing_pass.py --hold 0.3` → two-pass loudnorm → `-final.mp4`.

**Found on the way, before the first good compile:**
- **GATE F:** `SHOTLIST.md` / `PROMPTS.md` / `short/FACTCHECK.md` missing. Now generated by `make_gate_f.py`.
- **Short compiled as a 16:9 crop:** the sheet said `aspect`; `compile.py` reads `aspect_ratio`.
  GATE V caught it (11 BLOCKER edge-bleed). The Short now writes the same metadata as `shorts.py`, with
  `short_validation` *computed* (registered 916 patterns + `require_short_duration`). The validator
  caught a bug in its own first version (it doubled the suffix).
- **GATE V MAJOR underfill on S06 (52% < 55%):** the text-only task frame. Fixed by larger type
  (×1.22), which also reads better on a phone; not by moving things to game the metric.

**Checks on the final files:**

| Check | 16:9 final | Short final |
|---|---|---|
| Resolution | 3840×2160 | 2160×3840 |
| Duration (paced) | 302.6 s (17 holds × 0.3 s) | 85.8 s (6 holds) |
| GATE V (compile.py) | 36 frames · 0 BLOCKER · 0 MAJOR | 14 frames · 0 BLOCKER · 0 MAJOR |
| Per-frame luma (YAVG < 80) | 7,258 frames · min 221.1 · **0** below | 2,058 frames · min 222.9 · **0** below |
| Loudness | −24.6 → **−15.0 LUFS**, TP −1.9 dBTP | −24.4 → **−15.0 LUFS**, TP −1.9 dBTP |
| Claims at assertion | 35 frames on the final timeline | 22 frames |
| B10 equation at 15/50/85% | legible: radical bar, *p*\*, ≈ | — |

**Loudness note.** −15.0 is 1.0 LU under −14, the edge of tolerance, the same as W24 (−14.9). A
limiter-then-linear pass was tried and gained only 0.1 LU, so the limit is Kokoro's flat narration,
not its peaks. Kept. YouTube turns loud audio down, never quiet audio up.

**Defects found on the final file (all cue timing, all [EDIT]):**

| # | Beat | Defect | Fix |
|---|---|---|---|
| F1 | B03, B04, B06 | Caption stated the beat's conclusion before the narration (B03 "Never reaches the goal." at 0.6 s, before the walk) | Each caption cued to its spoken line |
| F2 | B10, B12 | The curve carried from B09 re-drew itself at every cut | Carried curve = drawn from frame 0 (`curveAt` −10) |
| F3 | B09 | Markers carried from B08 popped in again, two at once in the accent | Carried (`None`); the curve is the only new element |
| F4 | B12 | "…the average landed on the best setting" ~1 s before the average dot | Caption on the dot's cue |
| F5 | S01 | Learner marker on "a coin flip", coin on "beats a", ratio caption before both | Sentence order: coin → learner → 3.68× |

Re-rendered the 9 beats whose props changed, re-compiled once, re-paced, re-normalised, and re-ran
the luma scan and the assertion frames. **All five confirmed fixed on the final file.** Narration is
unchanged (fingerprints as signed).

**Production gate on the finals: PASS.** Still to do before upload: captions (SRT/VTT), YouTube
metadata, and Tanmay watching both cuts end to end. A clean scorecard isn't evidence the film lands
(PLAYBOOK §1c).

---

## Final verdict (2026-10-04)

Tanmay watched both cuts end to end: "its perfect now".

- **Long form: clear-for-public.** Teaching 12/12 · production gate PASS · 35/35 claims on screen when
  spoken (final file, Whisper clock) · 0 dark frames · GATE V clean · −15.0 LUFS / −1.9 dBTP.
- **Short: clear-for-public.** Teaching 12/12 · production gate PASS · 22/22 claims on screen when spoken ·
  0 dark frames · GATE V clean · inside the Shorts safe area · −15.0 LUFS / −1.9 dBTP.
- **Captions:** 110 + 29 cues, word timing on the Whisper clock, written math forms, self-checked
  against the narration word for word. Four cues are under 1.2 s, each a short phrase that ends on a
  real pause; all are readable at 17 cps.
- **Metadata:** both `*-youtube.md` written. Topic source and book URLs verified live (2026-10-04).
- **Before the long goes public:** fill `[CODE LINK]` (B17 promises it). Before the Short: `[FULL VIDEO LINK]`.
