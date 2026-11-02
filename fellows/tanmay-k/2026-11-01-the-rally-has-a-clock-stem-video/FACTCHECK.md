# FACTCHECK — Pong (long film), draft 2

Rule: every number is from our own scripts or our own stated settings. No outside statistic, person, date or machine
is cited. Claims about the essay are limited to what its beat sheet states. Shots are numbered from one (the scripts
count from zero: shot number = index + 1).

## Settings (shown on screen from B02)
Field 858 x 525, paddle 60, ball starts at 6 px/tick, +5% per shot. Paddle speeds 1.0 / 1.5 / 2.0 / 3.0 px/tick.
Aim: whole field (vertical speed up to the ball's sideways speed) or at most a quarter of it. Second field 1200 x 500,
paddle 50, paddle speeds 1.5 / 2.5 / 4.0.

| Beat | Claim (as spoken) | Verdict | Evidence |
|---|---|---|---|
| B00 | Perfect paddles; the sixth shot gets past at paddle speed 2.0 | SUPPORTED (model) | `angle_check2.py`: first undefendable index 5 = sixth shot |
| B01 | An essay says Pong has no perfect defense, a few fixed laws, a game to eleven | SUPPORTED (essay beat sheet) | `claude-for-design/pong/beat_sheet.json` beats B01-B03; essay HTML not in repo |
| B02 | Rules of our model; hit position steers the ball | OURS | stated design |
| B03 | Direction fixed at the hit; the crossing is all the time there is | MODEL | assumes the defender sees direction immediately |
| B04 | Aim reaches the whole height; best wait is the middle; worst shot half a field away | MODEL | worst landing minus midpoint = H/2 = 262.5 for full aim |
| B05 | Paddle covers about half the field less its own reach in one crossing; a little over a quarter of the ball's sideways speed | SUPPORTED (model) | (525 - 60) / (2 x 858) = 0.2710; search 0.272, 0.272, 0.273, 0.271 at four ball speeds (`angle_check.py`) |
| B06 | Too slow: first shot passes; middle holds five, breaks on sixth; fast holds thirteen, breaks on fourteenth | SUPPORTED (model) | `angle_check2.py` full-aim column: index 0, 5, 13 |
| B07 | Ball speeds up each shot; crossing shortens; reachable distance shrinks | SUPPORTED (model) | flight time = width / speed; +5% is our setting. Spoken as "in my model" |
| B08 | Arithmetic: four and a bit speed-ups (sixth shot), twelve point six (fourteenth); search matched | SUPPORTED | closed form 4.24 and 12.56 recomputed; search index 5 and 13 |
| B09 | Aim limited to a quarter: line about 0.215; predicted tenth and nineteenth; found the same | SUPPORTED (model) | `angle_check4.py`: 0.25 - 60/(2 x 858) = 0.2150; predicted idx 9, 18; found 9, 18 (also idx 4 at speed 1.5, idx 0 at 1.0) |
| B10 | Field 1200 x 500, paddle 50: line 0.188; spoken: seventh and twenty-seventh shots at 1.5 and 4.0; on-screen table also shows the eighteenth at 2.5; found the same | SUPPORTED (model) | `angle_check4.py`: (500 - 50)/(2 x 1200) = 0.1875; predicted idx 6, 17, 26; found 6, 17, 26 |
| B11 | Fast paddle, no speed-up: held for two hundred shots; arithmetic says it always will | SUPPORTED (model) | `angle_check3.py`: speeds 2.0 and 3.0, no break across 200 shots; with constant speed the margin is constant |
| B11 | Two rules carry the balance | QUALIFY | true of the two levers tested, not a proof no other rule matters; spoken as "in this model" |
| B12 | Left out: spin, reaction time, paddle edges, real-machine numbers | SUPPORTED | matches the model; absences stated by choice |
| B13 | Line = (height - paddle) / (2 x width); for 1000 x 500, paddle 50 = 0.225; at the serve a quarter-speed paddle has a perfect defense, a fifth does not | SUPPORTED (model) | arithmetic: 450 / 2000 = 0.225; 0.25 > 0.225 > 0.2. Serve only (ball not yet sped up). `angle_check5.py` (1000 x 500, paddle 50, no speed-up, full aim): quarter-speed paddle never breaks, a fifth breaks on the first shot |

## Removed or changed from earlier drafts
- "A game to eleven is a few dozen hits" - unsupported, removed.
- "Somebody chose where the clock sits so rallies last as long as people can stand" - designer intent, removed.
- "The essay leaves a question" - the 'which rule' prompt belongs to the folder's template, not the essay; now "the question I could not resist".
- "Defends perfectly, forever" -> "held for two hundred shots, and the arithmetic says it always will" (was "never broke in ..."; changed 2026-10-30 for a sound-alike join).
- "Every Pong has a clock" - dropped from the close.

## Open verifications
- B13's 1000 x 500 case: verified in `angle_check5.py` (done).
- Re-run all four scripts after the constants freeze and paste the output here.
- NEU-ISE post: about Atari-playing agents, unrelated.
- Essay credit: on screen "an essay in the Humanitarians AI repo"; author named in README and YouTube description.

## Sources and rights
Our own drawn rectangles and our own simulation only. No Atari footage or marks, no politics, no real people, no
third-party media. Two short essay phrases, attributed.
