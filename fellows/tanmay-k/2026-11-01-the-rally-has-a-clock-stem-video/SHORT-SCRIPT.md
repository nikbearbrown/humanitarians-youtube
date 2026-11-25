# SHORT-SCRIPT — Short (9:16), draft 2

One continuous scene (the same rally, the same field), written for a viewer who never sees the long film. Hook on the first words; context by S02 (what Pong is, the essay's claim, why a model); its own ending (the answer to the opening bet); closes on the long film's exact searchable title and settles back to the first frame so it loops. Pauses between lines about 0.8 s, none of 1 s or more.

### S01 · THE BET
**Narration:** In my tiny Pong, a perfect defender loses on the sixth shot, and nobody makes a mistake. Here is why.

**Visual:** Hook on frame one: the field fills the safe area, the rally already moving; big counter at the top.

**Status:** MODEL (paddle speed 2.0; first undefendable shot is the sixth).

### S02 · THE CONTEXT
**Narration:** Pong is two paddles and one ball. An essay I read says it has no perfect defense, and I wanted to know when that is true. So I built the smallest Pong I could. I'm Tanmay Kulkarni, in for Humanitarians AI.

**Visual:** Same scene, the ball easing between the paddles; a settings chip in the safe area (858 by 525, paddle 60, plus five percent per shot); the two essay phrases as small captions.

**Status:** ESSAY (two phrases only); MODEL (settings on screen).

### S03 · THE COUNT
**Narration:** Watch the rally. Shot one. Shot two. Shot three. Shot four. Shot five. All defended. Shot six. The ball goes past.

**Visual:** Counter 1 to 6 in step with the words; the ball's path to the top edge each shot; on six the paddle stops 8.4 px short.

**Status:** SIM (break index 5 at paddle speed 2.0; gap 8.4 px).

### S04 · THE TIME
**Narration:** The defender can see where the ball is going. What it lacks is time, because the ball gets five percent faster on every shot.

**Visual:** A timer bar for one crossing shrinks with each shot; the ball's speed number steps up.

**Status:** MODEL (the +5% setting is ours).

### S05 · THE TWO BARS
**Narration:** Two bars explain it. The first is how far the paddle can travel while the ball crosses. The second is how far the worst shot makes it go, about half the field. If the first is longer, a perfect defense exists.

**Visual:** The two bars grow into view over the field (can travel 286 px at shot one; must travel 232.5 px), the line between them.

**Status:** MODEL (232.5 = (525 - 60) / 2).

### S06 · THE CLOCK
**Narration:** But the crossing keeps shrinking, so the first bar sinks. On the sixth shot it drops below the line, by about eight pixels. The arithmetic says shot six, and a search that tries every aim agrees. Nobody made a mistake. The rally ran out of time.

**Visual:** The first bar sinks shot by shot (286 to 224 px); on six it crosses the line; the gap lit; two ticks land on shot six.

**Status:** SIM (224 vs 232.5 at shot six; predicted 4.24 speed-ups, sixth; found sixth).

### S07 · THE LIMIT
**Narration:** It is only a model, with no spin and no real machine. But it shows that no perfect defense is true here only because the ball speeds up.

**Visual:** MODEL, NOT A MACHINE in the safe area; the no-speed-up row runs past the frame edge.

**Status:** SIM (no speed-up: paddle speeds 2.0 and 3.0 held for 200 shots).

### S08 · THE FILM
**Narration:** The full film is called The Rally Has a Clock: When Is No Perfect Defense True in Pong?

**Visual:** The title in the safe area; the scene settles back to the first frame (loop-friendly).

**Status:** Exact searchable title as in the long film's YouTube title.

---
## Shape
Bet (S01) -> context: what Pong is, the essay's claim, why a model, who built it (S02) -> the count that proves the bet (S03) -> why time is the issue (S04) -> the two bars (S05) -> the clock, checked two ways (S06) -> the limit and the payoff (S07) -> the film's title (S08). One arc: the opening bet is answered inside the Short.

## Not yet done
Gate P (your read), Short PROOF plan review, audio, one continuous 2160x3840 render, the 11-point gate on the compiled file.

## Phone contract (measured on the compiled file by the 11-point gate)
- Canvas 2160 x 3840. **Safe area: y 461 to 2880 (12% to 75% of the height), x 120 to 1800 (nothing in the right rail).** The field is drawn 1700 wide (about 1040 tall) in the upper safe band; counter, bars and captions below it, all inside the band.
- **Type at least 68 px at 2160 wide (34 px at 1080).** Bar labels 72 px, counter number 360 px, captions 88 px, headline 112 px, source line 68 px. The long film's 24-logical-px labels (13 px at phone width) are not reused.
- **A muted-readable headline per phase**, changing with the line: THE BET, PONG: TWO PADDLES, ONE BALL, SHOT SIX, THE DEFENDER SEES IT COMING, TWO BARS, THE CLOCK, A MODEL, NOT A MACHINE, THE RALLY HAS A CLOCK.
- **Every figure on screen when it is spoken:** "sixth shot" (counter 6), "five percent" (chip and speed number), "half the field" / 232.5 px (second bar), "about eight pixels" (8.4 px gap lit), "two ways" (two ticks on shot six).
- **Sources in the lowest safe band, at least 2 s each:** "Our simulation: field 858 x 525, paddle 60, +5% per shot" (S02 to S07), "From an essay in the Humanitarians AI repo" (with the phrase, S02).
- One continuous scene, never cut: the field, paddles, ball and counter persist; each phase changes the state, and the last frame equals the first state (loop-friendly).
- Pauses between lines 0.8 s, never 1 s or more; 0.3 s lead; ball always in motion; no tune needed.

## Change schedule (plan; times from the measured line lengths, voice, 0.3 s lead, 0.8 s pauses)
| t (s) | line | what visibly changes |
|---|---|---|
|  0.0 | S01 | frame 1: headline THE BET up; rally already moving; counter shows SHOT 1 |
|  2.3 | S01 | caption 'a perfect defender' marks the left paddle |
|  4.4 | S01 | caption 'loses on shot six' with a 6 in orange |
|  6.6 | S01 | headline -> PONG, TWO PADDLES, ONE BALL |
|  8.2 | S02 | chip: our tiny Pong (paddles up and down only) |
| 10.6 | S02 | essay credit line + the phrase 'no perfect defense' |
| 13.2 | S02 | question 'when is that true?' replaces the phrase |
| 15.6 | S02 | settings chip: 858 x 525, paddle 60, +5% per shot |
| 17.8 | S02 | name line: Tanmay Kulkarni, for Humanitarians AI |
| 20.6 | S03 | headline -> SHOT SIX; counter starts at 1 |
| 22.4 | S03 | counter steps 1 to 5 with the words, dots fill |
| 24.8 | S03 | 'all defended' tick row |
| 26.4 | S03 | counter 6, ball past, gap 8.4 px lit |
| 28.7 | S04 | headline -> THE DEFENDER SEES IT COMING; path drawn |
| 31.2 | S04 | caption 'what it lacks: time' with a timer bar |
| 33.6 | S04 | speed number steps +5% per shot; timer bar shrinks |
| 35.2 | S04 | chip +5% per shot lights; speed number reads 'ball 5% faster each shot' |
| 36.7 | S05 | headline -> TWO BARS; bars grow into view |
| 39.4 | S05 | first bar labelled CAN TRAVEL (286 px at shot one) |
| 42.2 | S05 | second bar labelled MUST TRAVEL (232.5 px), the line |
| 45.2 | S05 | caption 'first longer = perfect defense exists' |
| 47.3 | S05 | tick: first bar longer than the second at shot one |
| 49.4 | S06 | headline -> THE CLOCK; first bar sinks with the counter |
| 52.0 | S06 | bar crosses the line at shot six |
| 54.4 | S06 | gap 8.4 px lit |
| 57.0 | S06 | two ticks land on shot six: arithmetic, search |
| 60.0 | S06 | caption 'the rally ran out of time' |
| 61.9 | S06 | 'nobody made a mistake' caption; counter holds at 6 |
| 63.9 | S07 | headline -> A MODEL, NOT A MACHINE |
| 66.0 | S07 | chip: NO SPIN |
| 66.4 | S07 | 'no spin, no real machine' chips |
| 69.0 | S07 | no-speed-up row runs past the frame edge |
| 71.0 | S07 | payoff line: no perfect defense is true here only because the ball speeds up |
| 73.0 | S08 | headline -> THE RALLY HAS A CLOCK; title in the safe area |
| 75.6 | S08 | scene settles back to frame 1 (loop) |
| 77.0 | S08 | first frame returns (shot one, rally ready) |

Longest interval between visible changes: 3.0 s; the gate re-measures at 540 x 960, where a ball landing is invisible, so each row above is a text, bar or counter change.
