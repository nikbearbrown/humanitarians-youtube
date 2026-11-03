# READ-ALOUD: Gate P sheet, the Short

*He Slowed Down in the Driest Hall Too* (working title) · 9:16 · voice `am_onyx`

Generated from `short/beat_sheet.json`. Its own script, written fresh for a viewer who never sees the
long film (not long-form beats cut down). Same method as the long sheet: read it aloud, top to bottom,
in one sitting, then reply **"Short Gate P PASS"** or list the beats that tripped you.

**DEMO lines (SD1–SD3)** are the long film's measured demo audio, copied (not re-recorded): read them
as marked. Pronunciation overrides are the same as the long film's (say-it-right table in `READ-ALOUD.md`).

## Changed since your Short Gate P PASS (Option A: framework early + the clap task)

Only these lines are new or changed. Every other line is word-for-word what you signed; the beats
after S02 were renumbered (old S03–S08 are now S04–S06 and S09–S11).

| Beat | Status | Line |
|---|---|---|
| S03 | **new** | The way I'd put it: the room asks a question, and the player answers. |
| S07 | **new** | Try it yourself first. In a moment, clap once. If the clap hangs in the air, your room has echo. If it dies right away, it's dry. Go ahead. *(2 s silence)* |
| S08 | **new** | Now say the sentence, every room you play in is asking you a question, at the pace your room seems to want. *(3 s silence)* |
| S09 | **changed** | Did you speed up, or slow down? A good answer names what your room was doing. Here's mine. First, the cathedral, with room between the phrases. *(was: Here's my sentence in both kinds of room. First, the cathedral, with room between the phrases.)* |

## Does it carry its own context? (the thing to judge)

| A first-time viewer needs | Where | How the Short gives it |
|---|---|---|
| Who is speaking | S01, S11 | Tanmay Kulkarni, for Humanitarians AI, at both ends (W24/W25 convention) |
| What the cathedral is | S01 | said aloud: “a simulated cathedral”; labelled on screen as not a measured room |
| Who says rooms shape music | S02 | David Byrne, named as the singer from Talking Heads, and his book *How Music Works* |
| The framework, before any example | S03 | the room asks a question, and the player answers (three stations on screen) |
| Who measured it, when, how | S04 | two researchers in Berlin, 2015; one cellist, Bach's six suites, seven halls; echo and tempo measured |
| Why slowing down is expected | S04 | musicians' advice since at least 1752 (Quantz, on screen) |
| The turn | S05 | slower in the driest halls too; 74%, said as one player in seven rooms |
| Why, kept honest | S06 | his words (pauses) vs the researchers' explanation (held notes), attributed separately |
| Your turn, scaffolded | S07–S08 | clap, listen, say the sentence; strong/weak answers on screen; silences of 2 s and 3 s |
| The payoff answers you | S09–SD3 | “Did you speed up, or slow down?… Here's mine”, then the sentence in both rooms |
| Where to go next | S11 | the full video: twelve more musicians, birds in Leiden, the skip button |

## Mechanical pass (`gate_p_lint.py`), already run

- 0 long sentences, 0 symbols or markup.
- Deliberate parallels: S05 "Too much echo… Too little echo…", S06 "In echoing halls… In dry halls…", S07 "If the clap hangs… If it dies…".
- PROOF static check: 0 fails. Portrait pixel gate 14/14; toolkit Gate V on stills 0 BLOCKER / 0 MAJOR.

## Where to listen hardest

- **S03**: **new.** One plain sentence. Does it sound like the idea, not a slogan?
- **S07–S08**: **new.** Read it as a first-time viewer. Do you know exactly when to clap and when to speak? Actually do it, in the silences
- **S09**: **changed.** "Did you speed up, or slow down?" should sound like a real question, then turn to "Here's mine"

## The script

### [0:00] S01 · LISTEN  _(tone: quiet, inviting)_

This is Tanmay Kulkarni, for Humanitarians AI. Listen to one sentence, inside a simulated cathedral.

<sub>**On screen:** One sentence, one cathedral · Listen. · Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:04] SD1 · DEMO  _(tone: (the sentence, normal pace, in the cathedral))_

> 🔊 **DEMO** (the sentence, normal pace, in the cathedral), audio from `../mp3/beat-D01.mp3`

**Every room you play in is asking you a question.**

> ☐ reads cleanly   ☐ note: ______________________

### [0:10] S02 · BYRNE  _(tone: curious, storytelling)_

Hear how every word is still ringing when the next one arrives? David Byrne, the singer from Talking Heads, wrote a book about this, called How Music Works. His big idea is that a room doesn't just hold music. It shapes it.

<sub>**On screen:** A room shapes the music in it · David Byrne, How Music Works: music is made to fit the place it will be heard. · Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room. · David Byrne, How Music Works (2012), ch. 1 “Creation in Reverse”</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:23] S03 · THE FRAME  _(tone: clear, plain)_

The way I'd put it: the room asks a question, and the player answers.

<sub>**On screen:** How a room shapes music · asks: echo, silence, noise · hears: whoever is playing · answers: what they change · David Byrne, How Music Works (2012), ch. 1 “Creation in Reverse” · the research in this video</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:27] S04 · SEVEN HALLS  _(tone: investigative, building)_

In two thousand fifteen, two researchers in Berlin measured how much one player changes from room to room. The cellist Jean-Guihen Queyras played all six of Bach's cello suites in seven European concert halls. They measured how much each hall echoed, and how fast he played. In the most echoing halls, he slowed down. Musicians have advised that since at least seventeen fifty-two: give the echo time to clear.

<sub>**On screen:** One cellist, seven halls · Most echoing halls → he played slower, as Quantz advised in 1752. · Shape only. The paper reports a fitted curve, not these points. · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3) · Quantz (1752), as cited there</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:48] S05 · THE DRIEST HALL  _(tone: surprised)_

But in the driest halls, the ones with almost no echo, he slowed down too. Too much echo, slower. Too little echo, also slower. One measure of the hall's echo accounted for about seventy-four percent of how his tempo moved.

<sub>**On screen:** He slowed down at both ends · Driest halls → also slower. One cellist, seven halls. · 74% of his tempo variation · Shape only. The paper reports a fitted curve, not these points. · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:00] S06 · WHY BOTH ENDS  _(tone: careful, then landing)_

Why both? In echoing halls, he told them, he lets the pauses run longer. In dry halls, the researchers think a player holds notes longer, to fill in for an echo that isn't there. Same answer. Opposite questions.

<sub>**On screen:** Same answer, opposite questions · asks: too much echo, or too little · hears: the cellist · answers: slower, for opposite reasons · Echoing hall (his words): let the pauses run longer · Dry hall (the researchers' explanation): hold notes longer · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3), interviews and discussion</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:11] S07 · YOUR ROOM  _(tone: direct, inviting)_

Try it yourself first. In a moment, clap once. If the clap hangs in the air, your room has echo. If it dies right away, it's dry. Go ahead.

<sub>**On screen:** First: clap once, and listen. · asks: clap once: does it hang, or die? · hears: you · answers: the pace you choose · Strong answer: names what the room did (blurred your words, or swallowed them) · Weak answer: “it felt different” · Our listening heuristic, not a measurement</sub>

> ⏸ **HOLD 2.0 s.** Silence for the viewer. Do the task now.

> ☐ reads cleanly   ☐ note: ______________________

### [1:22] S08 · SAY IT  _(tone: direct, unhurried)_

Now say the sentence, every room you play in is asking you a question, at the pace your room seems to want.

<sub>**On screen:** Now: say the sentence at your room's pace. · asks: clap once: does it hang, or die? · hears: you · answers: the pace you choose · Strong answer: names what the room did (blurred your words, or swallowed them) · Weak answer: “it felt different” · Our listening heuristic, not a measurement</sub>

> ⏸ **HOLD 3.0 s.** Silence for the viewer. Do the task now.

> ☐ reads cleanly   ☐ note: ______________________

### [1:32] S09 · BOTH ROOMS  _(tone: quiet, deliberate)_

Did you speed up, or slow down? A good answer names what your room was doing. Here's mine. First, the cathedral, with room between the phrases.

<sub>**On screen:** Two rooms like the ones he slowed down in · First: the cathedral. · Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:40] SD2 · DEMO  _(tone: (the sentence, with pauses, in the cathedral))_

> 🔊 **DEMO** (the sentence, with pauses, in the cathedral), audio from `../mp3/beat-D03.mp3`

**Every room you play in is asking you a question.**

> ☐ reads cleanly   ☐ note: ______________________

### [1:49] S10 · NO ECHO  _(tone: quiet)_

And now, almost no echo at all, holding the words longer.

<sub>**On screen:** Two rooms like the ones he slowed down in · Second: no echo. · Our narration with no impulse response applied</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:53] SD3 · DEMO  _(tone: (the sentence, held longer, dry))_

> 🔊 **DEMO** (the sentence, held longer, dry), audio from `../mp3/beat-D04.mp3`

**Every room you play in is asking you a question.**

> ☐ reads cleanly   ☐ note: ______________________

### [1:57] S11 · EVERY ROOM IS ASKING  _(tone: warm, landing)_

So a room doesn't write the music. It asks a question, and the player answers. The full video tries that on twelve more musicians, a city full of birds, and the skip button. Tanmay Kulkarni, for Humanitarians AI.

<sub>**On screen:** Every room is asking. · Full video: twelve more musicians, birds in Leiden, the skip button · @HumanitariansAI · Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room. · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3)</sub>

> ☐ reads cleanly   ☐ note: ______________________

_14 beats · 374 words · about 2:08 (planning clock for narration, measured for the demos). Kokoro audio for S-beats is generated after this Gate P._
