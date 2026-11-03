# Week 29 — Beats draft v2.1 (Pong)

Status: **DRAFT 2 for Gate P — not signed, nothing built.** Working title: **The Rally Has a Clock**.
Source: `claude-for-design/pong`. Our model and numbers: `angle_check.py`, `angle_check2.py`, `angle_check3.py`, `angle_check4.py`.
Narration of record: `READ-ALOUD.md` (generated from `beats_text.py`).

## Shape
The film **is one rally**, replayed, with a shot counter as the spine and the two framework bars on screen from frame one. Two dials (paddle speed, how far a hit can steer), then a second field, then a viewer task. The ending is a scaffold, then one open question. Differs from earlier shapes: W24 rooms, W25 learners in sequence, W26 halls, W27 change one/two/three, W28 a signal path.

## Labels
`ESSAY` = essay's beat sheet (quote only these). `MODEL` = our derivation. `SIM` = a number printed by our scripts. Nothing attributed to any real machine.

---

### B00 · SHOT SIX
**Narration:** Watch this rally. Both paddles play perfectly. Shot one. Shot two. Shot three. Shot four. Shot five. Nobody has made a mistake. And on the sixth shot, the ball goes past a paddle that did everything right. I want to know why.

**Visual:** Our rectangles on black. Shot counter 1 to 6. The two framework bars (paddle can travel / paddle must travel, with the line) sit in a corner from frame one, unnarrated. Paddle slides; ball passes on shot six; hold on the gap. 'Our model' tag stays in a corner all film.

**Status:** SIM (paddle speed 2.0, ball starts 6, +5% per shot; first undefendable shot is the sixth).

### B01 · THE CLAIM
**Narration:** An essay I read says Pong has no perfect defense. Just a few fixed laws, and a game to eleven. I like that line enough to wonder when it is true. Because a sentence like that should come with a number attached.

**Visual:** The two phrases as chips, source line: 'from an essay in the Humanitarians AI repo' (author credited in README and description, not on screen).

**Status:** ESSAY (two phrases only; `claude-for-design/pong/beat_sheet.json`).

### B02 · THE STAGE
**Narration:** So I built the smallest Pong I could. A field. Two paddles that only move up and down. A ball that bounces off the top and the bottom. And one rule that matters later: where the ball hits your paddle steers where it goes. I'm Tanmay Kulkarni, in for Humanitarians AI. This is my model, not any machine you remember, and every number you will see comes from the settings in the corner.

**Visual:** Field drawn once with labels fading in. Settings chip stays on screen from here: field 858 by 525, paddle 60, ball starts at 6 per tick, plus 5 percent per shot.

**Status:** MODEL; constants stated on screen (PROOF-REVIEW-1 finding 2).

### B03 · WHAT THE DEFENDER KNOWS
**Narration:** The moment the ball leaves a paddle, its direction is fixed. The defender can see exactly where it is going. What the defender does not have is time. The ball has to cross the whole field, and that crossing is all the time there is. Keep an eye on the two bars in the corner. One is how far the paddle can travel while the ball crosses. The other is how far it must.

**Visual:** Ball launched, dotted path with wall bounces unfolded into a straight line; timer bar for one crossing. The two corner bars are highlighted and labelled 'can travel' and 'must travel'.

**Status:** MODEL (defender sees direction at the hit; stated).

### B04 · THE WORST SHOT
**Narration:** Now put yourself in the attacker's place. You can aim anywhere. Every aim gives a different landing spot, and together they cover the whole height of the field. The defender cannot know the aim in advance, so the best place to wait is the middle. Then the worst shot is the one that lands at an edge, half the field away.

**Visual:** Fan of paths from the attacker's paddle; landing points marked along the far wall; defender parked at center; the two extreme landings lit; 'must travel' bar grows to match.

**Status:** MODEL (aim reaches the whole field).

### B05 · THE LINE
**Narration:** So the whole question shrinks to one comparison. In the time the ball takes to cross, can the paddle cover about half the field, minus the paddle's own reach? If it can, a perfect defense exists. If it can't, none does. Here, the paddle needs a little over a quarter of the ball's sideways speed. Keep the form, because it works on any field: the defender's reach in one flight, against half the free height.

**Visual:** Two bars large, threshold line, ratio 0.27 appears once; the form as a one-line card: 'reach in one flight vs half the free height'.

**Status:** MODEL; (525 - 60) / (2 x 858) = 0.271, measured 0.272 (`angle_check.py`).

### B06 · TURN THE DIAL
**Narration:** I replayed the same rally three times, and touched only the paddle's speed. Too slow, and the very first shot gets past. A middle setting holds for five shots, then breaks on the sixth. A fast setting holds for thirteen, and breaks on the fourteenth. Same ball, same rules. One number decided the story.

**Visual:** Three lanes side by side, same rally, three dial settings; counters stop at 1, 6 and 14; each held at least two seconds.

**Status:** SIM (paddle speeds 1.0 / 2.0 / 3.0; `angle_check2.py` full-aim column).

### B07 · THE CLOCK
**Narration:** Here is the part I did not expect. The ball speeds up on every shot. So the crossing gets shorter, and the distance the paddle can cover in one crossing shrinks with it. That bar keeps sinking toward the line. In my model, a rally is not only a contest. It has a clock inside it.

**Visual:** The two bars stepping down shot by shot with the counter; line crossed on the break shot.

**Status:** MODEL (+5% per shot is our stated setting).

### B08 · PREDICTED, THEN FOUND
**Narration:** I did not want to trust my own arithmetic, so I counted. For the middle setting, the arithmetic said the ball must speed up four and a bit times, so the sixth shot. A search that tries every aim broke on the sixth shot. For the fast setting, twelve point six speed-ups, so the fourteenth shot, and the search broke on the fourteenth.

**Visual:** Table filling in: predicted 4.24 -> sixth; found sixth. Predicted 12.56 -> fourteenth; found fourteenth. Side by side, held two seconds.

**Status:** SIM (closed form 4.24, 12.56; `angle_check2.py`).

### B09 · THE SECOND DIAL
**Narration:** There is a second dial. So far the attacker could aim anywhere. Now let the hit steer the ball less, so its up and down speed is at most a quarter of its sideways speed. The line drops, to about point two one five. The arithmetic says the tenth shot for the middle paddle, and the nineteenth for the fast one. Then the count. The tenth. The nineteenth.

**Visual:** Fan narrows to a thin wedge; line drops from 0.271 to 0.215 on the bar. Predicted breaks appear as ticks on the shot counter first, then the count runs and lands on each tick; a closing two-line tally puts old breaks (sixth, fourteenth) beside new (tenth, nineteenth), held two seconds. No table until the end.

**Status:** SIM (`angle_check4.py`: line 0.25 - 60 / (2 x 858) = 0.215; predicted and found idx 9 and 18 = tenth and nineteenth shots; also fifth at paddle speed 1.5 and first at 1.0).

### B10 · A DIFFERENT FIELD
**Narration:** Now change only the field. Wider and shorter, twelve hundred by five hundred, with a smaller paddle. The line falls to point one eight eight. Two paddle speeds, one and a half, and four. The arithmetic says the seventh shot, and the twenty-seventh. The count found the seventh, and the twenty-seventh. Same form. A different field.

**Visual:** Lead with the new field redrawn at the same scale beside the old one; settings chip updated (1200 by 500, paddle 50); line bar drops to 0.188; then a small predicted-vs-found table for all three speeds (1.5, 2.5, 4.0), held two seconds. Speech names two; the table shows the third (eighteenth) silently.

**Status:** SIM (`angle_check4.py` second field: line (500 - 50) / (2 x 1200) = 0.1875; predicted and found idx 6, 17, 26 = seventh, eighteenth, twenty-seventh shots).

### B11 · WHICH RULE
**Narration:** Here is the question I could not resist: which single rule would you change to break the balance? In this model, two rules carry it. How fast the paddle moves, and how much a hit can steer. And the claim turns out to be conditional. A fast enough paddle, against a ball that never speeds up, held for two hundred shots, and the arithmetic says it always will. The speeding up is what makes the sentence true.

**Visual:** The two dials lit; a third lane, fast paddle and no speed-up, counter running past the frame.

**Status:** SIM (`angle_check3.py`: speeds 2.0 and 3.0 never break across 200 shots).

### B12 · WHAT THIS DOES NOT CLAIM
**Narration:** One boundary, because I would rather say it than have you find it. This is a model. No spin, no human reaction time, no paddle edges, no numbers from any real machine. It shows when a rule set can be defended perfectly. It does not say how any particular game was built.

**Visual:** Plain slate listing what is left out.

**Status:** Boundary statement; marked absences by choice, not gaps.

### B13 · YOUR TURN
**Narration:** Your turn. A field one thousand wide, five hundred tall, a paddle fifty long. The line is the height, minus the paddle, over twice the width. Work it out. Point two two five. So at the serve, a paddle at a quarter of the ball's sideways speed has a perfect defense, and one at a fifth does not. Last question. If you could set one dial, and only one, where would you put it? I'm Tanmay Kulkarni, in for Humanitarians AI.

**Visual:** Card: line = (height - paddle) / (2 x width). The numbers 1000, 500, 50 appear; answer withheld for a five second hold, then 0.225 appears with the 0.25 and 0.2 comparison. Then the dial, still, counter at zero; fade.

**Status:** MODEL ((500 - 50) / (2 x 1000) = 0.225; no-speed-up serve only).

---
## Revision log
Draft 2 applied PROOF-REVIEW-1: (1) bars from frame one; (2) constants chip from B02; (3) B09 predict-then-count; (4) B10 second field; (5) B13 viewer card then open question; (6) essay credit: on-screen 'an essay in the Humanitarians AI repo', name in README and description; (7) calibrated B07, B11, and 'Every Pong like this one' is not used (the line was dropped from the close).

Draft 2.1: B10 spoken speeds cut to two (the table keeps all three); B08, B09, B10 given three different visual forms (table, ticks-then-count, field-first).

## Still open before Gate P
1. Re-freeze numbers in FACTCHECK and paste script output.
2. Short plan (idea): shot six, the line, the open question; needs its own arc.
3. Confirm house opening and closing template.
