# BEATS — structure, decisions, runtime (draft 1, 2026-10-16)

**Working title:** *The Birthday Paradox: Three Tests of One Claim*
**Category:** `claude-for-video-production/birthday-paradox` (folder named at build time)
**Numbers come from:** `RESULTS.md`, `match-rates.json`, `cluster-rates.json` (seed 2701). Nothing in narration may state a figure that is not in those files.
**Voice:** `am_onyx`, sign-off "Tanmay Kulkarni, in for Humanitarians AI". Years and numbers in words for Kokoro.
**Content rules:** no political content, no real individuals, no third-party text or images. Sources are our own simulations and US federal births-by-day counts, credited in the description (see FACTCHECK, to be written).

## The shape: CALL IT, THEN RUN IT

The film has one claim and three tests. Before every test, the narrator **writes a number down** (it appears on screen as a locked prediction). Then the machine runs and the result lands beside the call. Three calls, three results. The film's form is the act of committing before looking.

| Test | Claim under test | Call | Result |
|---|---|---|---|
| 1. The model | 23 people: even odds of a shared birthday | "about half" | 50.7% |
| 2. The calendar | Real births are uneven, so the model must be wrong | "it goes up, by a little" | 50.8%: up by about a tenth of a point |
| 3. The window | Squeeze the group into fewer days | "it jumps" | 90 days: 95.4%. Same month: above 99.99% |

The reveal that carries the film comes in test 3: the thing that changed the answer is **how many days the group can occupy**, not how uneven the days are.

## Beats

Planning rate 3.3 words per second. Visual language throughout: one 365-cell calendar grid, dots dropping into cells, a single counter, the call locked in a box at left.

### Cold open

**B01 · THE BET · ~16 s** (tone: dry, amused)
> Twenty three people in a room. Bet me two of them share a birthday. Most people take the other side. They lose that bet about half the time, and I want to show you exactly how I know.

*Visual:* empty calendar grid, 23 dots drop in, two land in one cell.

**B02 · THE PLAN · ~20 s** (tone: direct)
> Hi, I'm Tanmay Kulkarni, in for Humanitarians AI. One claim, three tests. Before each one I'll write my number down, so I can't flatter myself afterwards. Here is the claim: with twenty three people, the odds of a shared birthday are about even.

### Test one: the model

**B03 · WHY TWENTY THREE · ~26 s** (tone: curious)
> The trick is to stop counting people and count pairs. Twenty three people make two hundred and fifty three pairs. Each pair is a small chance, and two hundred and fifty three small chances pile up faster than your gut expects.

*Visual:* lines connect the dots; the pair counter spins to 253.

**B04 · CALL ONE · ~22 s** (tone: steady)
> My call: about half. Now I run four hundred thousand groups of twenty three and count how often a pair shares a day. Fifty point seven percent. The exact calculation says the same. The claim holds, in a world where every day is equally likely.

*Visual:* locked box "about half", then the counter fills to 50.7%.

**B04b · THE CURVE · ~24 s** (tone: building)
> And it doesn't stop at even odds. Ten people: about twelve percent. Thirty: seventy one percent. Fifty: ninety seven. By fifty seven people the odds pass ninety nine percent. The middle of that curve is steep, which is why your gut, trained on small rooms, keeps missing it.

*Visual:* the counter climbs as dots are added one at a time; 10, 30, 50, 57 flagged.

**B05 · MATCH ME · ~24 s** (tone: careful, short pull-back)
> One thing the claim does not say. It says some pair, not a pair with you. For somebody to share your birthday, you need two hundred and fifty three other people to reach even odds. With twenty two others in the room, your chance is under six percent. Same crowd, a different question.

### Test two: the calendar

**B06 · THE FALSE ASSUMPTION · ~26 s** (tone: investigative)
> That world doesn't exist. Births aren't even. I used federal counts of babies born each day. They come from the National Center for Health Statistics and the Social Security Administration, and cover two thousand to two thousand fourteen. The busiest day runs about twelve percent above average. February twenty ninth runs at about a quarter of a normal day.

*Visual:* the grid recolours by real daily share; Feb 29 nearly dark.

**B07 · CALL TWO · ~14 s** (tone: committing)
> My call: uneven days can only make a match more likely, so the number goes up. By a little, I think. I'll say a few tenths of a point.

**B08 · RESULT TWO · ~22 s** (tone: quietly surprised, **peak 1**)
> Fifty point eight percent. Up from fifty point seven, so the direction was right. But that's a tenth of a point at most. I said a few tenths, and it was one. My call was too generous.

*Cut to check:* the actual call must be honest. If the written call says "a few tenths," the reveal says it was too high. Reword to match whatever number is locked in B07 before recording.

**B09 · WHY SO SMALL · ~22 s** (tone: calm, pull-back)
> Nearly every ordinary day sits within a few percent of average, so the real calendar is close enough to even that the model barely notices. The wrong assumption was forgiving. Keep that in mind, because the next test breaks the model, and it breaks it somewhere else entirely.

### Test three: the window

**B10 · CALL THREE · ~22 s** (tone: leaning in)
> Now squeeze the group. Not twenty three people from anywhere in the year, but twenty three people all born inside the same ninety days. My call: the number jumps. I'm going to say above ninety percent, and I'm unsure about the rest.

*Visual:* the 365 grid dims to a 90-cell band; dots drop only inside it.

**B11 · RESULT THREE · ~18 s** (tone: struck, **peak 2**)
> Ninety five point four percent. The same twenty three people, a quarter of the calendar, and the odds go from a coin flip to nearly certain.

**B12 · THE SWEEP · ~28 s** (tone: brisk, building)
> Let me slide the window. A full year: fifty point eight. Half a year: seventy seven. Ninety days: ninety five. Sixty days: ninety nine. Born in the same month: better than ninety nine point nine percent. And with a window of seven days, twenty three people can't avoid sharing, there aren't enough days.

*Visual:* the band shrinks across the grid; the counter climbs.

**B12b · HOW MANY IT TAKES · ~22 s** (tone: brisk)
> Flip it around and ask how many people you need for even odds. Across a whole year, twenty three. Ninety day window: twelve. Sixty days: ten. A thirty day window: seven. A fortnight: five. A week: four.

*Visual:* the shrinking band with the head-count ticking down beside it.

**B13 · WHAT ACTUALLY MOVED · ~26 s** (tone: clear, **the turn**)
> Here is what I almost missed. Did the real, uneven calendar matter inside these windows? A tenth of a point at most, again. Seasons weren't the story. What moved the number was one thing: how many days the group had room to land on. The second test changed the shape of the calendar and nothing happened. The third changed its size, and everything did.

**B14 · THE SCHOOL YEAR · ~20 s** (tone: careful, short pull-back)
> A fair objection: classmates are all about the same age. But a school year with a cutoff date still contains every day of the calendar once, so it behaves like the full year, about fifty point eight percent. The squeeze only happens if the group is pinned to a narrow stretch of days.

### Close

**B15 · THE WEIGHT-BEARING ASSUMPTION · ~24 s** (tone: reflective)
> So one wrong assumption cost almost nothing, and another one, how many days a group can fill, changes the answer completely. Every model rests on a few of these. The skill is finding which ones are holding the roof up, and you only find out by changing each in turn and watching.

**B16 · OUTRO · ~10 s** (tone: landing; the film's single open question, no rubric)
> When someone tells you the odds, ask what they assumed about the room, and which of those assumptions is carrying the weight. Tanmay Kulkarni, in for Humanitarians AI.

## Size and runtime (draft)

18 beats (16 + B04b + B12b), **about 797 narration words** (counted), about 4:00 at the 3.3 w/s planning rate. Length decision: stop here. B04b (the curve) and B12b (head-counts per window) are the only additions, both from already-computed figures, so no new numbers are needed. Padding beyond that would dilute the three-test form; this is shorter than Week 26 (about 6:04) on purpose. Final runtime is measured by `build_beat_sheet.py` once it exists.

## Tone arc

dry → direct → curious → steady → careful → investigative → committing → **quietly surprised (B08)** → calm → leaning in → **struck (B11)** → brisk → clear (B13, the turn) → careful → reflective → landing. Two peaks, each followed by a pull-back. First-person curiosity only on genuine turns (B08 "I was too generous", B13 "what I almost missed").

## Structural differentiation (W15–W26 audit)

- **No numbered framework and no rubric ending.** One open question closes the film, as in the "each film needs its own structure" rule.
- **Not W22's three witnesses + verdict.** The three tests are runs of one machine under changed conditions, not testimony, and there is no verdict beat.
- **Not W21's "same move, one size up."** The tests change *different things* (the model, the shape of the calendar, the size of the window), and B13 turns on exactly that difference.
- **Not W25's coin experiment** and not W17's experiment: the predictions locked before each result are the form, and the sims are shown as checks, not as the film's argument.
- **No rooms or halls** (W23, W24, W26): "the room" appears in B01 and B16 only as ordinary speech, never as a staged space.
- **Nothing on base rates, test accuracy, Simpson, survivorship or Bayes** (neighbouring fellows' videos). Pair counting and window size are not covered in the repo (angle audit, `ANGLE.md`).
- Signature phrasing to avoid: "confident, wrong answer", "two inputs look the same".

## Open items before building

1. **B07/B08 coherence:** the locked call in B07 and the reveal in B08 must be reworded together once the on-screen number is fixed. The honest rule: the reveal reports what the call actually was.
2. **B12:** "sixty days: ninety nine" and "seventy seven" are rounded from 99.24 and 77.05. Check every spoken figure against `cluster-rates.json` and `match-rates.json` in FACTCHECK.
3. **B06 data credit:** description line "Births data: US NCHS and SSA via FiveThirtyEight (CC BY 4.0)". The `births/` README states no separate terms, so FACTCHECK should record that the numbers are US government statistics and the repo-wide licence is CC BY 4.0.
4. **B14** is a claim about school-year cohorts. It rests on the model ("a school year spans every day once"), not on a sourced study. Keep it phrased as a property of the calendar, not as a finding about real schools.
5. **Not yet verified:** that no fellow's work uses the "predict before running" form. Run the repo blob sweep on "predict", "my call", "before I run" before PROOF.
6. **Style check pending:** narration should be read aloud against `narration-should-feel-human-not-robotic` before drafting `READ-ALOUD.md`.
7. **No visuals designed yet** beyond the grid sketch. Photo/image rights do not arise (all graphics are generated).
