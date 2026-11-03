# Feedback: "Minutes of the Meeting" (working title): stills stage, Week 27 work video

**Stage:** the 12 stills (3840×2160, one per beat, 16:9, at their final state) and the beat sheet on the **planning
clock** (no audio yet). Reviewed from `beat_sheet.json`, `_stills/B01…B12-16x9.png`, `SCRIPT.md` (Gate P signed, draft 2)
and `FACTCHECK.md`. Tanmay looked at the stills and had no changes.

**Verdict:** **12/12 on the rubric. Production gate: PASS as intent**, with the checks below run on the files, not assumed.
Two join findings were fixed in this pass (one slate label, one slate caption); neither changes narration, so Gate P stands.

## Checks run (machine half)

| Check | Result |
|---|---|
| Slate figures against the narration (`build_slates.py` `checks()`) | **OK.** 82% and STRONG SELL (B04); 3 of 6 nudges and stability 0.05 (B06); weights 45/35/20, pieces 0.37, 1.75, 0.05, total 2.17, SELL (B07); about 470 words and the last line verbatim (B08); defaults 15% and 0.5 (B03); both hand-offs `approved_for_live_action: false`, `DRAFT`, `todos_open: 5` (B10); `Math.min(1, NaN)` is NaN and Python's `min(1, nan)` is 1, run in Node and Python (B09) |
| Every figure comes from the merged repository | Read with `git show 8665a9f:<path>`; nothing on a slate is typed. The nine Sim 1 signals are parsed from the workflow's own code |
| Beat sheet guards (`build_beat_sheet.py`) | **OK.** 12 beats; every slate stage has exactly one cue and every cue phrase is in its narration, in narration order; every ref is a W-row in FACTCHECK; no digit years, no placeholders |
| On-screen checks (`check_onscreen.py`, final stage of every slate) | **OK.** Every text ≥ 24 px on the 1080 grid (48 px on the 4K master); contrast ≥ 4.5:1 against its real backdrop (≥ 3:1 at 48 px and up); nothing past the safe edges |

The contrast check found real failures on the tinted and pill backgrounds (4.1 to 4.2:1) on its first run. Fixed at the
palette level: soft ink `#73705F` → `#6A6757`, accent text `#B5532F` → `#A74C2B`. Now 4.7:1 on those backgrounds.

## Findings from looking at the pictures, fixed before review

| Beat | What the render showed | Fix |
|---|---|---|
| all | Kicker line touching the heading; text sitting on rule lines or clipped by card edges (mixed fonts anchored at their tops) | one baseline system for every text; kicker and heading re-spaced |
| B01 | highlight box not matching its line; the closing line cramped | the line wrapped at a larger size inside its box |
| B02 | "growth vs sentiment" and "how close to a change" overran their boxes | three-line captions; box text re-set |
| B05 | ticks and "exactly on the limit" off the value baselines | row grid rebuilt on one baseline |
| B06 | "STABILITY" overprinting the large number | label moved up; rows re-gridded |
| B07 | the PIECE column ran off the right edge; the scale's labels collided with the table; the SELL band sat on the "2" tick | columns re-fitted; scale moved left; numeric tick labels dropped except the two ends |
| B09 | the fixed Python line printed over the broken one | both lines now stacked in the Python box, so the fix is read against the slip |

## Findings from this review

| Beat | Finding | Action |
|---|---|---|
| B03 | The narration says "an aggressive investor"; the card said only `risk appetite high`. A viewer hears "aggressive" and sees "high", and B05 then says AGGRESSIVE | **[FIXED]** the card reads `high · aggressive` (the workflow's own profile name for "high": `profile.name`, c11 `sim2_risk_appetite`) |
| B08 | The "someone typed" card showed `"sentiment_score": 0.5` as if it were a recorded request. It is an illustration of what the template prints, not one of the corpus requests | **[FIXED]** the card is labelled "someone types, for example"; the source line names the Build AI Prompt template |
| B09 | The stage order followed the slate, not the narration ("21 of 23" before "I fixed it") | **[FIXED]** stages re-ordered: requests and "21 of 23" → the two languages and the slip → the fix → "23 of 23"; cues follow the narration |
| B10 | The recipe card came before the open list, but the narration says "five items still open" first | **[FIXED]** open list is stage 2, recipe card stage 3 |
| B02 | The PR line appeared before the question the narration asks first | **[FIXED]** question is stage 4, "PR #70 · merged" stage 5 |

## Rubric (stills stage)

| Criterion | Score | Why |
|---|---|---|
| Explicit framework | 2 | B02 states the question on screen ("Who had a vote, and how much?") and B03 draws the chair and voices before any voice speaks; B07 shows the weights, the scale and the pieces on one frame |
| Reusable rubric | 2 | B11 puts the three questions on screen, one per beat of narration, then the good and the weak answer |
| Worked example | 2 | One stock, c11, on screen from B03 to B07 with every figure traceable to a file |
| Falsifiability / edge | 2 | B09 shows the slip and its fix side by side; B10 shows what is still open and what was never called |
| Active task | 2 | B11 gives a good answer ("names the voices and their weights") and a weak one ("the AI will figure it out") |
| Friction | 2 | B07 sets STRONG SELL against ENTER FULL POSITION, and the 45% weight against its 0.37 piece, on one slide, with the scale that reconciles them |

**12/12.**

## Production gate (intent), for the audio and motion stages

| Check | Result |
|---|---|
| Sources on screen | Every claim beat's slate names a committed file or files in its source line (B01 to B10, FACTCHECK W1 to W20); B11 and B12 make no claim and carry none |
| Evidence at the moment of assertion | Cues are set per beat (the beat sheet); each stage is tied to the phrase that triggers it. **To be re-set on the measured Whisper word times once audio exists**, then checked on rendered frames |
| Side-by-side | B03 (two requests), B05 (three seats), B08 (typed and defaulted), B09 (two languages) |
| Invented numbers labelled | The chip "Invented · sample data" is on every slate that shows a number (B01 to B10; B02 says "Every company and number invented"; B09 says "Sample requests · invented"); B02 and B12 also say it in words, with "Not investment advice" |
| Types and contrast | Machine-checked above |

## Boundaries checked

- **W25 (porting, parity, tests on the line):** B09 shows one difference between two languages and its fix; no rounding panel, no threshold, no deliberate break of my own copy.
- **W26 (a bad value quietly becoming a plausible one):** B03 and B08 show defaults as how the meeting starts and the briefing's identical line; the thesis on screen is who voted and how much.
- **No critique:** the defaults, the weights and the scale are drawn as how the workflow works, with no judgment; the NaN request cards are labelled as sample requests.
- **Committed files only:** no guard, no fixture builder, nothing from the session on any slate. `d07` and `d08` are committed fixtures.

## Risks to watch at the next stages

- **B07 is the densest slide:** at motion, each of its six stages must land on its phrase (voices, weights, scale, pieces, total, SELL) or the viewer falls behind. Check on rendered frames.
- **B09's slipped line** ("a different verdict on those two") is shown without the verdict values themselves, because the corpus holds no result for those two requests (step 3 rejects them). The film says only what RUN_LOG and the self-test row say.
- **Short fragments** ("Invented.", "Four out of four.", "Who had a vote?"): Whisper must confirm Kokoro voices them as written.
- **Only 16:9 stills exist.** The Short (9:16) is built later from its own script.
