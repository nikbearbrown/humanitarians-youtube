# SHORT SCRIPT: The Birthday Paradox, as a trailer (9:16)

**Working title:** *Take Away Days* (the long film is *The Birthday Paradox: Three Things You Could Change*)
**Role:** a trailer for the long film that stands on its own. A viewer who never sees the long film gets the claim, one surprise, the rule, and a closed loop.
**Written fresh for the Short.** None of the long film's beats are reused or cut down.
**Voice:** `am_onyx`. The bet comes first (spoken from 0 s); the name rides in the answer (S02); the channel is named again at the end. Numbers and years in words.
**Content rules:** no political content, no real individuals, no third-party media. Sources: our own simulations and calculations (see `FACTCHECK-SHORT.md`).

## The shape: ONE GRID THAT SQUEEZES

One scene, never cut. A single calendar of days holds 23 dots (the group). The narration takes days away, and the calendar visibly
narrows around the same dots while the odds counter climbs. Then it widens again, and the loop closes where it opened: a year,
twenty three people.

| Time | The one scene | State that carries |
|---|---|---|
| S01–S02 | A full year of days; 23 dots land; two share a day (ringed); the counter reads 50.7% | the 23 dots, the ring |
| S03 | The same dots slide inward as the calendar narrows: 365 to 90 days (counter 95.4%), then to 30 (above 99.99%) | the dots keep their relative places |
| S04 | The squeeze holds. Three small rows beside it: PEOPLE (kept), EVENNESS (a tenth of a point), DAYS (the one) | the narrowed calendar |
| S05 | The rule is typeset over the scene | |
| S06 | The calendar widens to a year (23 dots, "even odds: 23"), then narrows to a month (7 dots, "even odds: 7") | dots leave or return as the number changes |
| S07 | Back to a full year, 23 dots, 50.7%, then the end card | the opening state, restored |

## Layout and phone rules (added after the Shorts PROOF review, 2026-10-17)

Canvas 1080×1920 logical (rendered at 2160×3840). All text and cards inside the **safe area**:
- **vertical:** between 12% and 75% of the height (y 230 to 1440 logical). The top bar and the Shorts title, captions and buttons own the rest.
- **horizontal:** x 60 to 900 (the right-hand button rail sits over x > 920 in the lower half).
- **type:** nothing below 30 px logical on a data label, 40 px on a key figure's caption; the headline line 56 px; the counter 260 px.
- **a headline line** (y 270) carries the argument in a few words so the Short reads with the sound off; it changes with each line below.
- **motion:** one continuous scene, no hard cuts; something on screen changes at least every 3 s; nothing is held static more than 3 s.
- **end:** no separate end card. The closing text overlays the restored opening scene (a loop-friendly last frame), inside the safe area, for about 2.5 s.

## Lines

### S01 · THE BET · ~6 s (tone: dry, direct)
> Twenty three people in a room. Bet me two of them share a birthday.

*On screen:* from the first frame: the headline "Two of these 23 share a day" and an empty calendar of 365 days (months down, days across), label "possible birthdays: 365". Dots start landing at 0.3 s, one every 0.25 s; the last two land in one cell, which is ringed.
*Source:* "Illustration: one random group of 23, seed 2701. Not data."

### S02 · HALF THE TIME · ~7 s (tone: amused)
> I'm Tanmay Kulkarni, for Humanitarians AI, and you'd lose that bet about half the time.

*On screen:* headline "You'd lose about half the time". As he says the name, a small name line fades in inside the safe area ("Tanmay Kulkarni · Humanitarians AI"). The counter fades in at 260 px: 50.7%, label "of random groups of 23 have a shared birthday".
*Source:* "Our calculation: exact, 400,000 simulated groups agree."

### S03 · TAKE AWAY DAYS · ~16 s (tone: leaning in, then struck)
> Now keep the group at twenty three, and take away days. Squeeze the calendar to ninety days, and it's ninety five percent. Squeeze it to one month, and it's almost certain.

*On screen:* headline "Same 23 people. Fewer days." The calendar narrows around the same dots (a band of lit days shrinks from the full year to 90 days, then to 30; label "possible birthdays: 365 → 90 → 30" follows). The counter climbs with it: 95.4%, then "above 99.99%". Dots slide inward and pile onto shared days.
*Source:* "Our calculation: 23 people, days equally likely."

### S04 · WHAT DECIDES IT · ~14 s (tone: clear, building)
> So what decides it? Not the people, we kept them. Not uneven birthdays, they move it a tenth of a point. It's how many days there are.

*On screen:* headline "What decides it?" Three rows slide in below the narrowed calendar, one on each phrase: PEOPLE "23, kept"; EVENNESS "+0.1 point at most"; DAYS "365 → 30", ringed in the accent as the one that moved it.
*Source:* "Our calculation. Real US births, NCHS and SSA via FiveThirtyEight (CC BY 4.0)."

### S05 · THE RULE · ~9 s (tone: confident)
> Here's the rule. Take the square root of the days. Multiply by one point two. Add a half.

*On screen:* headline "The rule". The rows clear and the rule is typeset in three steps, each as it is spoken: √d, then 1.2 ×, then + ½ (final form: n ≈ round(1.2 × √d + ½), with d = possible birthdays, n = people for even odds, "even odds = a 50% chance").
*Source:* "Our calculation. Checked against the exact answer for every day count from 2 to 2,000."

### S06 · TRY IT · ~8 s (tone: brisk)
> For even odds, a year needs twenty three people. One month needs seven.

*On screen:* headline "Try it". The calendar widens to a year: 23 dots, "365 days → 23 people for even odds". Then it narrows to a month: dots leave one by one until 7 remain, "30 days → 7 people for even odds".
*Source:* "Our calculation. 365 days → 23 people; 30 days → 7."

### S07 · THAT'S WHY TWENTY THREE · ~10 s (tone: warm, landing)
> That's why it's twenty three. The full video shows three things you could change, and the one that decides it. It's on Humanitarians AI.

*On screen:* the opening scene again, restored: a full year, 23 dots, the ringed pair, 50.7%. The rule fades. Closing text over the scene (inside the safe area, about 2.5 s): "The full video. Search:" then "The Birthday Paradox: Three Things You Could Change" then "Humanitarians AI". The exact title is searchable, so the pointer works even where a link cannot.
*Source:* none needed.
