# BEATS — structure, decisions, runtime (draft 2, 2026-10-16)

**Working title:** *The Birthday Paradox: Three Things You Could Change*
**Category:** `claude-for-video-production/birthday-paradox` (folder named at build time)
**Numbers come from:** `RESULTS.md`, `match-rates.json`, `cluster-rates.json`, `sqrt-rule.json` (seed 2701). Nothing in narration may state a figure that is not in those files or in `FACTCHECK.md`.
**Voice:** `am_onyx`, sign-off "Tanmay Kulkarni, in for Humanitarians AI". Years and numbers in words for Kokoro.
**Content rules:** no political content, no real individuals, no third-party text or images. Sources are our own simulations and US federal births-by-day counts.
**Supersedes:** draft 1 ("call it, then run it"), kept as `BEATS-DRAFT-v1-gateP-signed.md`. Draft 2 drops the written-prediction device after the form sweep found it is the stated thesis of `vox-prediction-lock` (see `PROOF-REVIEW.md` §1).

## The shape: THREE THINGS YOU COULD CHANGE

The film's chapters are the three parameters of the problem itself: **how many people**, **how uneven the days are**, **how many days there are**. Each gets one change and one reading of the odds. One moves them as expected, one barely moves them, one decides almost everything. The film then turns the finding into a rule the viewer can reuse:

> people needed for even odds ≈ **1.2 × √(days) + ½, rounded**

The rule is shown fitting every window the film already ran (365, 180, 90, 60, 30, 14, 7 days), applied once to a new case (birth month), and then handed to the viewer for a second new case (a number from one to fifty). The answer is revealed after a held pause.

| Change | What turns | Result | Expected? |
|---|---|---|---|
| 1. People | 10 → 57 people, even days | 12% → 99% | yes |
| 2. Evenness | real national calendar vs even days | 50.8% vs 50.7% | barely moves |
| 3. Days | 365 → 90 → 30 days | 50.8% → 95.4% → above 99.99% | decides almost everything |

## Beats

Planning rate 3.3 words per second. Visual language throughout: one 365-cell calendar grid, dots dropping into cells, a single counter. Every figure spoken is printed on screen in the same beat, with a source line (legibility contract). No locked-prediction device and no "my call" boxes.

### Cold open

**B01 · THE BET · ~16 s** (tone: dry, amused)
> Twenty three people in a room. Bet me two of them share a birthday. Most people take the other side. They lose that bet about half the time, and I want to show you exactly how I know.

*Visual:* empty calendar grid, 23 dots drop in, two land in one cell; the counter ends the beat at 50.7%.
*Source:* "Our simulation and exact calculation (see B04)."

**B02 · THE PLAN · ~26 s** (tone: direct)
> Hi, I'm Tanmay Kulkarni, in for Humanitarians AI. Three things could change that odds figure: how many people are in the group, how uneven the birthdays are, and how many days they have to land on. I'll change each one and watch the number. One of them barely matters, one matters the way you'd expect, and one decides almost everything. Hold a guess about which.

*Visual:* three labelled cards appear and stay on screen as the chapter index: PEOPLE, EVENNESS, DAYS. The counter sits beneath them.
*Source:* none needed.

### Change one: the people

**B03 · WHY TWENTY THREE · ~26 s** (tone: curious)
> The trick is to stop counting people and count pairs. Twenty three people make two hundred and fifty three pairs. Each pair is a small chance, and two hundred and fifty three small chances pile up faster than your gut expects.

*Visual:* lines connect the dots; the pair counter spins to 253. Do not animate this as a sum.
*Source:* "23 × 22 ÷ 2 = 253".

**B04 · PEOPLE · ~32 s** (tone: steady, building)
> First change: the people. I run four hundred thousand random groups of twenty three and count how often a pair shares a day. Fifty point seven percent. The exact calculation agrees. Now add people. With ten, about twelve percent. With thirty, seventy one percent. With fifty, ninety seven percent. By fifty seven people, past ninety nine percent. More people, more odds, just as you'd expect.

*Visual:* the counter fills to 50.7% beside "exact 50.73%"; then dots are added one at a time with 10, 30, 50, 57 flagged and printed with percentages (held ≥2 s).
*Source:* "Our simulation: 400,000 groups, seed 2701. Exact calculation also shown."

**B05 · MATCH ME · ~24 s** (tone: careful, short pull-back)
> One thing the claim does not say. It says some pair, not a pair with you. For somebody to share your birthday, you need two hundred and fifty three other people to reach even odds. With twenty two others in the room, your chance is under six percent. Same crowd, a different question.

*Visual:* "any pair" vs "someone with you" printed side by side: 23 people / 253 others; 50.7% / 5.9%, held ≥2 s.
*Source:* "Our calculation. Even days assumed."

### Change two: the evenness

**B06 · THE FALSE ASSUMPTION · ~28 s** (tone: investigative)
> Second change: how even the days are. So far every day was equally likely, and that's false. I used federal counts of babies born each day. They come from the National Center for Health Statistics and the Social Security Administration, and cover two thousand to two thousand fourteen. The busiest day runs about twelve percent above average. February twenty ninth runs at about a quarter of a normal day, because it only exists one year in four.

*Visual:* the grid recolours by real daily share with a scale; Feb 29 nearly dark with the label "exists one year in four". The credit line stays on screen for the whole beat.
*Source:* "Births data: US NCHS and SSA via FiveThirtyEight (CC BY 4.0)."

**B07 · THE REAL CALENDAR · ~20 s** (tone: quietly surprised, **peak 1**)
> So I ran it again on the real calendar. Fifty point eight percent, against fifty point seven for even days. Uneven days can only raise the odds, and they did, by a tenth of a point at most. That's tiny.

*Visual:* "even days 50.7%" and "real calendar 50.8%" side by side, held ≥2 s.
*Source:* "Our simulation and exact calculation on national births, 2000–2014."

**B08 · WHY SO SMALL · ~24 s** (tone: calm, pull-back)
> About ninety six percent of days sit within ten percent of average, so the real calendar is close enough to even that the model barely notices. The wrong assumption was forgiving. Keep that in mind, because the third change breaks the model somewhere else entirely.

*Visual:* a strip of the 365 day-shares, with the ±10% band shaded and "96% of days inside" printed.
*Source:* "Our count, SSA 2000–2014, Feb 29 excluded."

### Change three: the days

**B09 · THE WINDOW · ~24 s** (tone: leaning in, struck, **peak 2**)
> Third change: how many days there are to land on. Squeeze it. Not twenty three people from anywhere in the year, but twenty three people all born inside the same ninety days. Ninety five point four percent. Same group size, a quarter of the calendar, and the odds go from a coin flip to nearly certain.

*Visual:* the 365 grid dims to a 90-cell band; dots drop only inside it; the counter reaches 95.4% beside "full year 50.8%", held ≥2 s.
*Source:* "Our calculation, 90-day window, real weights."

**B10 · THE SWEEP · ~28 s** (tone: brisk, building)
> Let me slide the window. A full year: fifty point eight. Half a year: seventy seven. Ninety days: ninety five. Sixty days: ninety nine. Born in the same month: better than ninety nine point nine percent. And with a window of seven days, twenty three people can't avoid sharing, there aren't enough days.

*Visual:* the band shrinks across the grid; a five-row table (365, 180, 90, 60, 30 days with percentages) held ≥2 s.
*Source:* "Our calculation, real weights."

**B11 · HOW MANY IT TAKES · ~22 s** (tone: brisk)
> Flip it around and ask how many people you need for even odds. Across a whole year, twenty three. Ninety day window: twelve. Sixty days: ten. A thirty day window: seven. A fortnight: five. A week: four.

*Visual:* the shrinking band with the head-count column beside it, all six values printed.
*Source:* "Our calculation; people for even odds."

**B12 · WHAT ACTUALLY MOVED · ~30 s** (tone: clear, **the turn**)
> Here is what I almost missed. Does the uneven calendar still matter inside those windows? A tenth of a point at most, again. Seasons weren't the story. Of the three things, the head count moves the odds the way you'd expect. The evenness of the days barely moves them. And the number of days decides almost everything.

*Visual:* the three chapter cards return, each with its reading: PEOPLE "12% → 99%", EVENNESS "50.7% → 50.8%", DAYS "50.8% → 95.4%". Real vs even values for the 90-day window (95.44 vs 95.40) printed side by side.
*Source:* "Our calculation."

### The rule

**B13 · THE RULE · ~34 s** (tone: confident, discovering)
> Look at those head-counts again. Twenty three for three hundred and sixty five days. Twelve for ninety. Seven for thirty. They follow a rule. Take the square root of the days. Multiply by one point two. Add a half, and round. A year gives twenty three. Ninety days gives twelve. Thirty days gives seven. A week gives four. It is right for every window in this film, and never more than one person off anywhere from two slots to two thousand.

*Visual:* the rule printed as one line, then a table of days, √days, rule result, exact answer for 365, 180, 90, 60, 30, 14, 7, held ≥3 s with the match column highlighted. Under it, the honest tally: "exact for 1,161 of 1,999 slot counts; off by one for the other 838; never more". The rule line carries "round halves up".
*Source:* "Our calculation. Checked against the exact answer for every slot count from 2 to 2,000."

**B14 · THE SCHOOL YEAR · ~20 s** (tone: careful, short pull-back)
> A fair objection: classmates are all about the same age. But a school year with a cutoff date still contains every day of the calendar once, so it behaves like the full year, about fifty point eight percent. The squeeze only happens if the group is pinned to a narrow stretch of days.

*Visual:* the 365-day band labelled "one school-year cohort covers every day once".
*Source:* "Property of the calendar model."

**B15 · A NEW CASE · ~28 s** (tone: warm, applying)
> Now use it on something that isn't a birthday. Birth months: twelve slots. The square root of twelve is about three and a half. Times one point two, plus a half, rounds to five. So five people are enough for even odds that two share a birth month, if every month were equally likely. Four people give forty three percent. Five give sixty two.

*Visual:* twelve month-cells; the rule line worked step by step; 43% and 62% printed side by side.
*Source:* "Our calculation. Equal months assumed."

### Your turn

**B16 · YOUR TURN · ~22 s + 8 s hold** (tone: inviting, unhurried)
> Your turn. Everyone in a class picks a random number from one to fifty. How many people before two probably match? Use the rule. A tempting wrong answer is half the slots, twenty five. Pause, work it out, and I'll say.

*Visual:* "50 slots. How many people for even odds?" with the rule line printed under it. After the narration, an **8 s hold** with a silent countdown bar.
*Source:* none needed (a question).

**B17 · THE ANSWER · ~24 s** (tone: reassuring, landing)
> The root of fifty is about seven. Times one point two, plus a half, rounds to nine. Nine people give fifty three percent. Eight give forty five. Not twenty five. The slots set the scale, and their square root sets the crowd.

*Visual:* the working shown step by step; "9 people: 53%" beside "8 people: 45%"; the wrong answer "25 (half the slots)" struck through, held ≥2 s.
*Source:* "Our calculation. Random picks, equally likely."

### Close

**B18 · OUTRO · ~14 s** (tone: landing)
> Next time someone quotes odds that two things match, ask how many slots they could fall into. The square root of that number is about how many it takes. Tanmay Kulkarni, in for Humanitarians AI.

*Visual:* the rule line alone on screen; end card.
*Source:* none needed.

## Size and runtime (draft)

18 beats; narration word count and runtime are written by `make_read_sheet.py` into `READ-ALOUD.md` (add the 8 s hold in B16). Final runtime is measured by `build_beat_sheet.py` once it exists.

## Tone arc

dry → direct → curious → steady → careful → investigative → **quietly surprised (B07)** → calm → leaning in → **struck (B09)** → brisk → clear (B12, the turn) → confident (B13, the rule) → careful → warm → inviting → reassuring → landing. Two peaks, each followed by a pull-back. First-person curiosity only on genuine turns (B12 "what I almost missed").

## Structural differentiation (W15–W26 audit, plus the library)

- **No numbered framework and no rubric ending.** The chapters are the problem's own three parameters. The viewer task is one formula and one practice case.
- **Not `vox-prediction-lock`:** no written prediction, no "my call", no gap-between-guess-and-result teaching. The only guess is the one B02 invites silently.
- **Not W22's three witnesses + verdict.** The three changes are one machine run three ways. No verdict beat.
- **Not W21's "same move, one size up."** Each change turns a *different* thing, and B12 turns on the difference.
- **Not W20's instrument being read.** There are no gauges, scales or readings framed as an instrument; the counter is a plain on-screen number.
- **Not W25's coin experiment**, nor W17's. The sims are shown as checks.
- **No rooms or halls as staged space** (W23, W24, W26). "Room" appears only as ordinary speech in B01.
- **Nothing on base rates, test accuracy, Simpson, survivorship or Bayes.** A square-root-of-slots rule appears nowhere in the library or our Weeks (sweep on 20,811 files: 0 hits). Neighbour phrases like "change one thing at a time" appear in unrelated advice lines elsewhere; this film never uses that slogan.
- Signature phrasing to avoid: "confident, wrong answer", "two inputs look the same".

## Open items before building

1. Gate P was read on draft 1. Draft 2 changes most beats; see `READ-ALOUD.md` for which are unchanged and which need a re-read.
2. FACTCHECK rows for B08 (96%), B13 (the rule and its range), B15 and B17 are in `FACTCHECK.md`.
3. Kokoro phonemes for "Kulkarni", "fortnight" and "February twenty ninth" before audio.
4. No visuals designed yet beyond the sketches above. Graphics are generated; no third-party images.
