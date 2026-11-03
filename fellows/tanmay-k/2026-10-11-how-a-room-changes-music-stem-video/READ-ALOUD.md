# READ-ALOUD: Gate P sheet

*How a Room Changes Music: One Cellist, Seven Concert Halls* (working title) · structure: THE VOICE CHANGES ROOMS · voice `am_onyx`

Generated from `beat_sheet.json` by `make_read_sheet.py`. If the narration changes, this sheet is
regenerated and the read starts again.

**How to run Gate P:** read each beat out loud at speaking pace, top to bottom, in one sitting.
Listen for rhythm, emphasis, and whether each turn lands. Tick the box or write a note. Also skim
the *on screen* line under each beat: card text is checked too (PLAYBOOK §1). Then reply
**"Gate P PASS"** (with any notes) or list the beats that tripped you.

**This film has two things a page can't show:**
- **DEMO beats (D01–D04)** are the same sentence played through a room. Read them aloud as
  marked: normal pace for D01, then *noticeably* slower for D02–D04. Their real sound (cathedral
  impulse response, or dry) is applied at the audio stage and checked by ear then.
- **Holds** after B18 and B19 are silence for you, the viewer, to clap and speak. When you reach
  them, *do the task*: clap, listen, say the sentence. That's the only honest way to judge it.

**No slates yet.** `RoomVoice`, `HallTempo` and `AskAnswer` aren't built, so this is a read-aloud
Gate P. Visuals are reviewed as rendered stills at the next stage, before any audio.

## Mechanical pass (`gate_p_lint.py`), already run

- 0 long sentences (three split: B04, B10, B12), 0 dropped units, 0 symbols or markup in narration.
- 3 ECHO flags and 3 'too' flags, all deliberate (below). 16 NAME flags → the ear checklist.
- 4 LONE-LETTER flags: "R P M" (deliberate letters) and a tokenizer split inside "Léveillé".

| Beat | Parallel | Why it stays |
|---|---|---|
| B09 | "Too much echo, slower. Too little echo, also slower." | the U-shape, said as a pair. The lint's 'too' flag is about numbers, and none are near |
| B13 | "If every player… If they answer differently…" | the test's two outcomes; the parallel *is* the rule |
| B18 | "If the clap hangs… If it dies right away…" | the clap test's two outcomes |
| D01–D04 | the same sentence four times | the film's device. Each one is a different room or pace |

## Say-it-right checklist

Kokoro's phonemes, checked 2026-10-10. ✗ = Kokoro gets it wrong on its own, so the audio stage feeds
the override phonemes instead (the narration text and captions keep the real spelling). **Read the
names the way the second column says**, and tell me if any should be said differently.

| Word | Should sound like | Kokoro alone | Override | Where |
|---|---|---|---|---|
| Byrne | BURN | `bˈaɪən ✗` | `bˈɜːn` | B04–B07, B15–B16 |
| Jean-Guihen | zhahn gee-EN | `dʒˈiːŋɡˈɪhən ✗` | `ʒˈɑːn ɡiˈɛn` | B08 |
| Queyras | keh-RAHSS | `kwˈaɪɹəz ✗` | `kɛɹˈɑːs` | B08 |
| Quantz | KVAHNTS | `kwˈɔnts ✗` | `kvˈɑːnts` | B07, B08 |
| Johann Joachim | YO-hahn YO-ah-kim | `jˈoʊhɑːn dʒˈoʊəkˌɪm (Joachim ✗)` | `jˈoʊɑːkɪm` | B07 |
| Léveillé Gauvin | lay-vay-YAY go-VAN | `lˌeɪveɪlˈeɪ ɡˈoʊvɪn (close)` | `Gauvin: ɡoʊvˈæn` | B16 |
| Leiden | LAY-den or LYE-den | `lˈeɪdən ✓` | `—` | B14 |
| CBGB | C-B-G-B | `sˌiːbˌiːdʒˌiːbˈiː ✓` | `—` | B06 |
| seventy-eight R P M | as written | `sˈɛvəntiˈeɪt ˈɑːɹ pˈiː ˈɛm ✓` | `—` | B15 |
| US top ten hits | U-S | `jˌuːˈɛs tˈɑːp tˈɛn hˈɪts ✓` | `—` | B16 |
| Stravinsky | struh-VIN-skee | `stɹævˈɪnski ✓` | `—` | B15 |
| great tits | plain, the bird's real name | `ɡɹˈeɪt tˈɪts ✓` | `—` | B14 |
| Kulkarni | kul-KAR-nee | `kˈʌlkɑːɹni ✓` | `—` | B04, B24 |

## Where to listen hardest

- **B01–B03**: the cold open. "Most of that got lost, right?" should sound amused, not scripted. Imagine the cathedral line actually blurring
- **B04**: **does a viewer know what the video is about after this beat alone?** (PLAYBOOK §1c) A book, Byrne, rooms shape music
- **B09**: **the turn.** "Then the part that made me stop." needs a real beat of surprise
- **B10**: the cool-down (PLAYBOOK §1a): careful, and "That's their reading, not his words" plain, not defensive
- **B13**: **the test.** Is it easy to remember on one hearing? Could you apply it to a song you know?
- **B17**: the second cool-down: "It still doesn't decide it" should land quietly
- **B18–B19**: **the task.** Read it as if you've never seen the script. Do you know exactly when to clap and when to speak? Actually clap, actually say the sentence, in the holds
- **B23**: the landing. "Same answer. Opposite questions." Unhurried, no lift

## The script

### [0:00] B01 · LISTEN  _(tone: quiet, inviting)_

Listen to one sentence, inside a simulated cathedral.

<sub>**On screen:** One sentence, one cathedral · Listen. · Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:02] D01 · DEMO  _(tone: (the sentence, normal pace, in the cathedral))_

> 🔊 **DEMO:** read **normal pace**. At audio: cathedral (York Minster IR), Kokoro speed 1.0.

**Every room you play in is asking you a question.**

> ☐ reads cleanly   ☐ note: ______________________

### [0:08] B02 · LOST  _(tone: curious, a little amused)_

Hear that? Every word is still ringing when the next one arrives. Same sentence, same cathedral. This time, slower, with room between the phrases.

<sub>**On screen:** Same sentence, same cathedral · Each word still ringing when the next arrives. · Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:15] D02 · DEMO  _(tone: (the sentence, with pauses, in the cathedral))_

> 🔊 **DEMO:** read **with a clear pause between the phrases**. At audio: cathedral (York Minster IR), phrases joined by 0.6 s silences.

**Every room you play in is asking you a question.**

> ☐ reads cleanly   ☐ note: ______________________

### [0:25] B03 · THE SPEAKER CHANGED  _(tone: pleased, then direct)_

Nobody touched the cathedral. The speaker changed. Hold on to that, because it's the whole video.

<sub>**On screen:** Nobody touched the cathedral · The room stayed the same. The speaker changed. · Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room. · our demonstration</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:30] B04 · THE PLAN  _(tone: warm, clear)_

Hi, this is Tanmay Kulkarni, in for Humanitarians AI. This video is about a book: How Music Works, by David Byrne, the singer from Talking Heads. Its big idea is that music is shaped by the room it's played in. I wanted to know how that shaping actually happens, so I went looking for people who measured it. Here's what I found. The room doesn't write the music. It asks a question. A player hears it, and answers. And different players answer the same room in different ways.

<sub>**On screen:** How a room shapes music · asks: too much echo, too little, too much noise · hears: the player, every night · answer: slower, shorter, higher, sparser · David Byrne, How Music Works (2012), ch. 1 “Creation in Reverse” · the research in this video</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [0:56] B05 · BYRNE'S CLAIM  _(tone: storytelling)_

In the book's first chapter, Byrne argues that music gets made, knowingly or not, to fit the places it'll be heard. On the radio he gave the clearest example I've found. Bach's church was smaller than the Gothic cathedrals before it, so Bach could write fast, busy lines. All of that, Byrne said, would just turn into mush in a Gothic cathedral. And the chant that came before barely changes key. So in a huge stone room, every note left hanging in the air is still in tune.

<sub>**On screen:** Byrne on churches and chant · “would just turn into mush in a Gothic cathedral” · Bach's church: smaller than the Gothic cathedrals before it → fast, busy lines · Gregorian chant: barely changes key → the hanging notes stay in tune · The book: music is made, knowingly or not, to fit where it will be heard · David Byrne, TED Radio Hour, NPR, 24 July 2020 · David Byrne, How Music Works (2012), ch. 1 “Creation in Reverse”</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:23] B06 · CBGB  _(tone: fond, specific)_

His own band is his best example. CBGB, in New York, was a small, long, narrow club. In the book he describes a room with very little echo, where every detail of a song came through. Later, Talking Heads played Carnegie Hall. And Byrne noticed that some of the songs he'd written didn't sound all that great in halls like that.

<sub>**On screen:** CBGB and Carnegie Hall · A small, dry club, then a grand hall · CBGB: “kind of long and sort of narrow”, “not that large of a place” · The book: very little echo, so every detail came through · Carnegie Hall and halls like it: the songs “didn't sound all that great” · David Byrne, TED Radio Hour, NPR, 24 July 2020 · David Byrne, How Music Works (2012), ch. 1 “Creation in Reverse”</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [1:42] B07 · THE OLD ADVICE  _(tone: thoughtful)_

That's composers adjusting over centuries. But if Byrne is right, it should show up in a single player on a single night. Musicians have said so for a long time. In seventeen fifty-two, the flautist Johann Joachim Quantz told players to slow down in echoing rooms, so the notes don't blur together. Which is exactly what I did with that sentence.

<sub>**On screen:** Quantz, 1752 · Slow down in echoing rooms · Played fast in a reverberant room, notes blur into each other · His advice: take a slower tempo · J. J. Quantz, Versuch einer Anweisung die Flöte traversiere zu spielen (1752), as cited in Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:00] B08 · SEVEN HALLS  _(tone: investigative, building)_

And then someone actually checked. Two researchers in Berlin recorded the cellist Jean-Guihen Queyras playing all six of Bach's cello suites in seven European concert halls. They measured how much each hall echoed, and how fast he played every movement. In the most echoing halls, he slowed down. Quantz would have nodded.

<sub>**On screen:** One cellist, seven halls · Shape only. The paper reports a fitted curve, not these points. · Most echoing halls → he played slower. · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:16] B09 · THE DRIEST HALL  _(tone: surprised)_

Then the part that made me stop. In the driest halls, the ones with almost no echo, he slowed down too. Too much echo, slower. Too little echo, also slower. And one measure of the hall's echo accounted for about seventy-four percent of how his tempo moved. That's one player in seven rooms. But it's a strong pattern.

<sub>**On screen:** He slowed down at both ends · 74% of his tempo variation · Shape only. The paper reports a fitted curve, not these points. · Driest halls → also slower. One cellist, seven halls. · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:33] B10 · WHY BOTH ENDS  _(tone: pulling back, careful)_

So why slow down in a dry room? He told them that in echoing halls he slows down to avoid a muddy sound, and lets the pauses run longer. For the dry halls, the explanation is the researchers' own. With no echo to carry a note, a player may hold notes longer, to make up for sound that isn't there. That's their reading, not his words. But look at what it means. The same answer, slower, to two opposite questions.

<sub>**On screen:** Why both ends · Same answer, two opposite questions · Echoing hall (his words): slow down to avoid mud, let the pauses run longer · Dry hall (the researchers' explanation): hold notes longer, to replace the missing decay · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3), interviews and discussion</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [2:58] B11 · TWELVE PLAYERS  _(tone: curious, then quietly delighted)_

So the same team tried it on more people. Twelve musicians, fourteen simulated concert halls. And here, the hall's echo explained under nine percent of their tempo, even after allowing for each player's own habits. The paper calls their strategies very individual. Almost all of them said they lengthen pauses in echoing rooms, but mostly in slow pieces. In fast pieces, they kept the notes short and clean instead.

<sub>**On screen:** Twelve musicians, fourteen simulated halls · The same question. Different answers. · The hall's reverberation explained 8.73% of tempo (one cellist, real halls: 74.36%) · Strategies: “very individual” · Slow pieces: longer pauses · fast pieces: short, clear notes · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3), lab study</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:19] B12 · NO SIMPLE RULE  _(tone: fair, measured)_

And to be fair to the simpler story, two earlier studies looked for it. One used the Cleveland Orchestra, the other a grand piano in a room with adjustable echo. Neither found the simple pattern: more echo, slower playing. That fits. The room doesn't set the tempo. It sets a problem, and each player solves it their own way.

<sub>**On screen:** Two earlier studies · Neither found “more echo, slower playing” · Cleveland Orchestra, halls of 1 to 2.1 s reverberation: not the expected pattern · MIDI grand piano, variable-acoustics room: no effect on mean tempo · The room sets a problem. Each player solves it their own way. · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3), §1 (refs 4–5)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:36] B13 · THE TEST  _(tone: clear, confident)_

So here's a way to listen for this anywhere. When a place seems to have shaped some music, listen for what the room takes away, who's hearing it, and what they changed to get it back. Then the test. If every player answers the same way, the room is close to deciding. If they answer differently, it's only asking.

<sub>**On screen:** Listen for it anywhere · asks: what the room takes away · hears: who's hearing it · answer: what they changed to get it back · Every player answers the same → the room is close to deciding. Different answers → it's only asking. · Our test, from Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3) (one cellist 74.36% · twelve players 8.73%)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [3:54] B14 · OUTDOORS  _(tone: light, curious)_

It isn't only people. In two thousand three, researchers in Leiden recorded great tits, a small songbird, in quiet and noisy parts of the city. Traffic noise is mostly low rumble. The birds in the noisy spots sang with a higher lowest note, lifting their songs above it. Here the room isn't echo. It's noise. And the answer isn't tempo. It's pitch.

<sub>**On screen:** A city is a room too · asks: low traffic rumble · hears: a great tit, in Leiden · answer: a higher lowest note · Slabbekoorn & Peet (2003), Nature 424:267</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [4:13] B15 · THE RECORD AS A ROOM  _(tone: storytelling, brisk)_

Byrne's book makes the same argument about machines. He starts with Edison's cylinders, when bands had to perform the same song again and again for each batch of recordings. A recording format is a room made of minutes. In nineteen twenty-five, Igor Stravinsky had a contract to record his music. So he wrote a piano suite, his Serenade in A, with every movement short enough to fit one side of a seventy-eight R P M record. About three minutes, at most.

<sub>**On screen:** A room made of minutes · asks: one 78 rpm side: three minutes at most · hears: Stravinsky, 1925, with a recording contract · answer: Serenade in A: every movement short enough for one side · Contracted to record on his first American tour · Byrne opens the technology chapters with Edison's cylinders · Boosey & Hawkes, Stravinsky: Serenade in A (1925) · David Byrne, How Music Works, “Technology Shapes Music”</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [4:38] B16 · THE SKIP BUTTON  _(tone: building, then struck)_

The newest room is a playlist you can skip. A researcher at Ohio State, Hubert Léveillé Gauvin, studied three hundred and three US top ten hits from nineteen eighty-six to two thousand fifteen. The wait before the voice comes in fell from more than twenty seconds in the mid eighties to about five. And talking to a reporter, he put it like this. It's just adapting yourself to your environment, whether you're aware of it or not. That's Byrne's argument, from someone who counted.

<sub>**On screen:** 303 US top-10 hits, 1986–2015 · asks: a skip button, seconds in · hears: songwriters and producers · answer: the voice arrives sooner: 20+ s → about 5 s · Mid-1980s: more than 20 seconds before the voice · 2015: about 5 · “It's just adapting yourself to your environment whether you're aware of it or not” (AFP, 2017) · Léveillé Gauvin (2018), Musicae Scientiae 22(3) · figures: Ohio State news, 2017</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [5:03] B17 · THE ROOM DOESN'T DECIDE  _(tone: cooling down, honest)_

One caution. In a second study, he compared hits with less popular songs by the same artists, and the pattern didn't hold. A short intro doesn't make a hit. So the room shapes the music. It still doesn't decide it.

<sub>**On screen:** The second study · Hits vs. less popular songs by the same artists · 2015: 60 popular vs 60 less popular songs · The data did not support the attention-economy predictions · Léveillé Gauvin (2018), Musicae Scientiae 22(3) · figures: Ohio State news, 2017</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [5:15] B18 · YOUR ROOM  _(tone: direct, inviting)_

Before I play mine, try yours. In a moment, clap once, wherever you are. If the clap hangs in the air after your hands stop, your room has echo. If it dies right away, it's dry. Go ahead.

> ⏸ **HOLD 2.5 s.** Silence for the viewer. Do the task now.

<sub>**On screen:** Try it in your room · First: clap once, and listen. · Clap hangs after your hands stop → echo · dies right away → dry · “Every room you play in is asking you a question.” · Strong answer: names what the room did (blurred your words, or swallowed them) · Weak answer: “it felt different” · Our listening heuristic, not a measurement</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [5:29] B19 · SAY IT  _(tone: direct, unhurried)_

Now say the sentence, every room you play in is asking you a question, at the pace your room seems to want.

> ⏸ **HOLD 4.0 s.** Silence for the viewer. Do the task now.

<sub>**On screen:** Try it in your room · Now: say the sentence at the pace your room wants. · Clap hangs after your hands stop → echo · dies right away → dry · “Every room you play in is asking you a question.” · Strong answer: names what the room did (blurred your words, or swallowed them) · Weak answer: “it felt different” · Our listening heuristic, not a measurement</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [5:40] B20 · YOUR ANSWER  _(tone: warm, firm)_

Did you speed up, or slow down? That's your answer. A real answer names what your room was doing, blurring your words or swallowing them. Just saying it felt different doesn't count.

<sub>**On screen:** Try it in your room · Did you speed up, or slow down? · Clap hangs after your hands stop → echo · dies right away → dry · “Every room you play in is asking you a question.” · Strong answer: names what the room did (blurred your words, or swallowed them) · Weak answer: “it felt different” · Our listening heuristic, not a measurement</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [5:50] B21 · TWO ROOMS  _(tone: quiet, deliberate)_

Here's mine, in two rooms like the ones the cellist slowed down in. First, the cathedral.

<sub>**On screen:** Two rooms like the ones he slowed down in · First: the cathedral. · Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room.</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [5:54] D03 · DEMO  _(tone: (the sentence, with pauses, in the cathedral))_

> 🔊 **DEMO:** read **with a clear pause between the phrases**. At audio: cathedral (York Minster IR), phrases joined by 0.6 s silences.

**Every room you play in is asking you a question.**

> ☐ reads cleanly   ☐ note: ______________________

### [6:04] B22 · NO ECHO  _(tone: quiet)_

And now, almost no echo at all.

<sub>**On screen:** Two rooms like the ones he slowed down in · Second: no echo. · Our narration with no impulse response applied</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [6:06] D04 · DEMO  _(tone: (the sentence, held longer, dry))_

> 🔊 **DEMO:** read **slower, holding the words longer**. At audio: dry, no echo, Kokoro speed 0.85.

**Every room you play in is asking you a question.**

> ☐ reads cleanly   ☐ note: ______________________

### [6:10] B23 · SAME ANSWER  _(tone: landing, unhurried)_

Both slower than I'd normally say it. One is waiting for the echo to clear. The other is filling in for an echo that never comes. Same answer. Opposite questions.

<sub>**On screen:** Same answer. Opposite questions. · Same answer. Opposite questions. · Simulated echo: our own impulse response (T30 4.7 s, measured). Not a measured room. · Schärer Kalkandjiev & Weinzierl (2015), Proc. Third Vienna Talk on Music Acoustics, pp. 215–219 · Psychomusicology 25(3)</sub>

> ☐ reads cleanly   ☐ note: ______________________

### [6:19] B24 · OUTRO  _(tone: warm)_

Every room is asking. Tanmay Kulkarni, in for Humanitarians AI, signing off.

<sub>**On screen:** Every room is asking. · Tanmay Kulkarni, in for Humanitarians AI</sub>

> ☐ reads cleanly   ☐ note: ______________________

_28 beats · 1187 words · estimated runtime 6:23 at 3.3 words/s, including 6.5 s of holds. Kokoro audio becomes the master clock once generated._

---

**The Short** isn't written yet. It gets its own script and its own Gate P after this one passes
(one arc: the sentence lost in the cathedral → the cellist slowing at both ends → two rooms).
