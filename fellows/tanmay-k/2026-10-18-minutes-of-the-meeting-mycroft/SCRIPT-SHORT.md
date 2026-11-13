# SHORT SCRIPT: *Who Fills the Blank?* (the Week 27 work video, as a trailer, 9:16)

**Working title:** *Who Fills the Blank?* (the long film is *Minutes of the Meeting: What an AI Is Handed*)
**Status:** draft 3, 2026-10-17, **Gate P signed** (draft 2 after Tanmay asked for a longer Short; draft 3 moved the question to the first words of S01). Draft 2 follows Tanmay's note: the Short may run well over a minute and should not rush; its job is to give the viewer the context of what the full film will do.
**Role:** a trailer for the long film that stands on its own **and sets expectations for the master video**. A viewer who never sees the long film gets the question, one stock, three voices that disagree, the weighing, what the AI is actually handed, a plain account of what the full film will show (S06), and a closed loop. About 85 s, unhurried.
**Written fresh for the Short.** None of the long film's beats are reused or cut down; it shares the stock and the figures, not the words.
**Voice:** `am_onyx`, each line synthesised whole. The question is in the first words (spoken from 0 s); the name rides in line 2; the channel is named again at the end. Numbers in words.
**Content rules:** no political content, no real individuals, no third-party media. Every company and number is invented. Sources: files merged into `nikbearbrown/mycroft` main @ `8665a9f` (see `FACTCHECK-SHORT.md`).

## The shape: ONE BLANK THAT GETS FILLED

One scene, never cut. At the top sits the last line an AI is handed, with a **blank** where the verdict goes. Below it, a meeting
forms around one invented stock: three seats fill with three verdicts that disagree, a chair weighs them, and the answer is
written into the blank at the top. The meeting then folds into the minutes the AI actually receives, with that same line at its
foot. Under that sheet the **previews of the full film** arrive one at a time (S06), each a piece of the long film's content, all
anchored to the same sheet. Then they recede, the question comes back, and the verdict dissolves to a blank again: the loop closes where it opened.

| Time (planned) | The one scene | State that carries |
|---|---|---|
| S01 | The line types in with a blank where the verdict goes; the blank is ringed; three empty seats are drawn | the line, the blank |
| S02 | The stock's tag arrives ("Ironbridge Power, invented") and the name line fades in; the seats get their labels | the seats, the line |
| S03 | The seats fill one by one: STRONG SELL, ENTER FULL POSITION, stability 0.05 | the three verdicts |
| S04 | Weights appear on the seats (45, 35, 20), then their pieces, then the total on a bar; the blank at the top fills with SELL | the verdicts with weights and a total; the filled line |
| S05 | The seats fold into a sheet of five stacked sections ("about 470 words"); the line slides to the sheet's foot, where it is last | the filled line, now the last line of the minutes |
| S06 | The sheet moves up and shrinks; four previews arrive one at a time in a zone under it: a file tag (every figure from a file you can open), the sheet outlined (what the AI is handed), two identical lines (what the minutes don't say), and two boxes "original / my copy" with "21 of 23 → 23 of 23" (where my copy disagreed, and how I caught it) | the sheet, with the line at its foot |
| S07 | The previews and the sheet recede; the three questions arrive; the closing title overlays; SELL dissolves to a blank | the opening state, restored |

## Layout and phone rules (the Shorts gate, applied from the start)

Canvas 1080×1920 logical (rendered at 2160×3840). All text and cards inside the **safe area**:
- **vertical:** between 12% and 75% of the height (y 230 to 1440 logical). **horizontal:** x 60 to 900; nothing in the right rail (x > 920).
- **type:** nothing below 30 px logical; key figures much larger. **Contrast** at least 4.5:1 on the backdrop each text sits on.
- **a headline line** (y 270) carries the argument in a few words so the Short reads with the sound off; it changes with each line below.
- **motion:** one continuous scene, no hard cuts; something on screen changes at least every 3 s; nothing is held static more than 3 s (measured at 540×960).
- **end:** no separate end card. The closing text overlays the restored opening scene (a loop-friendly last frame), inside the safe area, for about 2.5 s.
- **labels:** "Invented stock · sample data" on screen from the first frame; a source line per phase inside the safe area.

## Lines

### S01 · THE BLANK · ~10 s (tone: curious, then dry)
> Who fills in the blank? An AI is about to give advice on a stock, and the very last thing it's told is: your action plan must strictly match, and then a blank.

*On screen:* from the first frame: the headline "Who fills in the blank?" (the question is the first thing spoken and the first thing read) and, typing in from 0.3 s, paced to the narration, the line `IMPORTANT: Your action_plan.immediate must strictly match "▯▯▯▯".` in two lines of mono type; the blank is ringed in the accent on "a blank". Three empty seat outlines are then drawn under it, one every 0.9 s. Label "Invented stock · sample data".
*Source:* "The closing line of the briefing the workflow builds: Build AI Prompt node, Mycroft main @ 8665a9f."

### S02 · THREE VOICES · ~11 s (tone: warm, plain)
> I'm Tanmay Kulkarni, for Humanitarians AI. In an open-source finance pipeline I contributed to, three simulators, I call them voices, each read the same invented stock in their own way.

*On screen:* headline "Three voices, one stock". As he says the name, a name line fades in inside the safe area ("Tanmay Kulkarni · Humanitarians AI"). A stock tag lands above the seats: "Ironbridge Power · invented". The seats get their labels, one on each "voice": Sim 1 growth against sentiment, Sim 2 three investors, Sim 3 how close to a change.
*Source:* "Mycroft, What-If Simulation Agent recipe; PR #70, merged."

### S03 · THEY DISAGREE · ~16 s (tone: even, then a beat of surprise)
> The first voice weighs the stock's growth against its sentiment, and says strong sell. The second asks how an aggressive investor would see it, and says enter a full position. The third checks how close the verdict is to changing, and says it's fragile: a stability of point oh five.

*On screen:* headline "They don't agree". The seats fill on their phrases: STRONG SELL (82%); ENTER FULL POSITION (four limits met, exactly); stability 0.05 with a small gauge near zero.
*Source:* "c11, simulation-results.json: sim1, sim2, sim3."

### S04 · THE WEIGHING · ~14 s (tone: brisk, then landing)
> They were asked different questions, so a chair weighs them. Forty-five percent for the first, thirty-five for the second, twenty for the third. Together, two point one seven out of five. That's a sell, and the blank fills in.

*On screen:* headline "The chair weighs them". The weights land on the seats (45%, 35%, 20%), then the pieces (0.37, 1.75, 0.05), then the total on a one-to-five bar (2.17, in the SELL band). On "the blank fills in", SELL is written into the ringed blank at the top: the loop's payoff.
*Source:* "c11, aggregate: weights, pieces, score; bands from the Aggregate node."

### S05 · THE MINUTES · ~13 s (tone: quieter, a little ominous without drama)
> But the AI never heard that meeting. All it gets is the minutes: about four hundred and seventy words, a profile, three simulations, a verdict, and, at the very bottom, the line you just saw.

*On screen:* headline "What the AI gets". The three seats fold into a sheet of five stacked sections (profile, three simulations, verdict); the label "about 470 words" arrives; the filled line slides to the sheet's foot and stays last.
*Source:* "c11, ai_prompt: five sections, 471 words."

### S06 · WHAT THE FULL FILM SHOWS · ~22 s (tone: friendly, concrete, no hype)
> In the full film, I follow that one stock through the whole meeting, and every figure comes from a file you can open. I show what the AI is handed, and what the minutes don't say. And I show the one place where my own copy of these steps disagreed with the original, and how I caught it.

*On screen:* headline "In the full film". The sheet moves up and shrinks to the top of the scene; four previews arrive **one at a time** in a preview zone under it (y 920 to 1380, full safe width), each replacing the last: a file tag opens to a path ("simulation-results.json"); the sheet is outlined ("what the AI is handed"); two identical lines appear one after the other ("0.5 typed" and "0.5 filled in", both printed "Sentiment Score: 0.5/1.0"); two boxes "original" and "my copy" with "21 of 23" turning to "23 of 23".
*Source:* "The long film: the meeting, the minutes, and my own minute-taker."

### S07 · THE QUESTION · ~14 s (tone: warm, unhurried)
> So before an AI summarises your next meeting, have you read the minutes? Who had a vote, and how much of one? The full film is Minutes of the Meeting: What an AI Is Handed.

*On screen:* headline "Have you read the minutes?" The previews and the sheet recede; the questions arrive one per phrase ("Have you read the minutes?", "Who had a vote?", "How much of one?"); on "The full film is", the closing title overlays inside the safe area ("Minutes of the Meeting: What an AI Is Handed · Humanitarians AI") and SELL dissolves back to a blank, restoring the opening state.
*Source:* none needed (the title is the pointer).

## Why this is one arc, not a cut-down

- **One scene, one state.** Everything the viewer saw is still there at the next step: the line at the top, then the seats under it, then the sheet that folds from them with the line at its foot.
- **It has its own payoff and ending.** The opening question ("who fills in the blank?") is answered inside the Short (S04: the chair does, by weighing), and the ending turns it into the viewer's question.
- **It is not the long film's beats.** It shares the stock and the figures, not the words or the order. S06 is a plain account of what the long film shows, so a viewer knows what to expect; it does not replay any of it.
- **It takes its time.** About 85 s: each voice gets its own clause, the weighing is said once at a natural pace, and the previews are given a phrase each.

## Cadence plan (events on the narration clock, planned at 3.4 words a second; re-set on the Whisper word clock at build)

Something on screen changes at least every 3 s. Planned: **55 events over 86 s; the largest gap between events is 2.9 s** (the first 5 s are the line typing in, continuously).

| Planned t | Line | Event |
|---|---|---|
|   0.0 s | S01 | headline; the line starts typing, paced to the narration (continuous to the highlight) |
|   6.9 s | S01 | the line is highlighted |
|   8.7 s | S01 | the blank is ringed |
|   9.6 s | S01 | seat 1 drawn |
|  10.2 s | S02 | headline changes; the name line fades in |
|  10.5 s | S01 | seat 2 drawn |
|  11.1 s | S02 | the channel joins the name line |
|  11.4 s | S01 | seat 3 drawn |
|  12.6 s | S02 | a small tag: open-source finance pipeline |
|  14.6 s | S02 | stock tag lands |
|  15.2 s | S02 | seat labels (Sim 1, Sim 2, Sim 3) |
|  16.4 s | S02 | stock tag and seats glow together |
|  18.1 s | S02 | the seats pulse in turn |
|  19.7 s | S03 | headline changes |
|  19.7 s | S03 | seat 1 highlighted; 'growth' and 'sentiment' marks join it |
|  21.7 s | S03 | 'sentiment' mark |
|  22.9 s | S03 | seat 1 fills: STRONG SELL |
|  23.8 s | S03 | seat 2 highlighted |
|  25.0 s | S03 | an investor mark joins seat 2 |
|  27.0 s | S03 | seat 2 fills: ENTER FULL POSITION |
|  28.5 s | S03 | seat 3 highlighted; small nudge arrows run |
|  30.8 s | S03 | the arrows reach a change |
|  32.6 s | S03 | seat 3 fills: stability 0.05, gauge |
|  34.7 s | S04 | headline changes; the chair appears |
|  37.7 s | S04 | weight 45% lands on seat 1 |
|  39.4 s | S04 | weight 35% lands on seat 2 |
|  40.9 s | S04 | weight 20% lands on seat 3 |
|  41.2 s | S04 | pieces 0.37, 1.75, 0.05 |
|  42.1 s | S04 | total 2.17 on the bar |
|  44.4 s | S04 | the bar's SELL band lights |
|  45.6 s | S04 | SELL is written into the blank |
|  47.5 s | S05 | headline changes; the seats begin to fold |
|  49.2 s | S05 | the sheet is outlined |
|  51.0 s | S05 | 'about 470 words' label |
|  52.7 s | S05 | section 1 (profile) lights |
|  53.3 s | S05 | sections 2 to 4 (three simulations) light |
|  53.9 s | S05 | section 5 (verdict) lights |
|  56.0 s | S05 | the filled line slides to the sheet's foot |
|  57.8 s | S06 | headline changes |
|  59.0 s | S06 | a trail runs through the sheet (the whole meeting) |
|  61.9 s | S06 | the sheet moves up and shrinks; preview 1: a file tag arrives |
|  63.7 s | S06 | the tag opens to a path |
|  65.1 s | S06 | preview 2 replaces it: the sheet is outlined |
|  66.9 s | S06 | preview 3 replaces it: a typed line |
|  67.8 s | S06 | preview 3: the identical filled-in line |
|  69.3 s | S06 | preview 4 replaces it: the box 'original' |
|  70.4 s | S06 | preview 4: the box 'my copy' |
|  72.2 s | S06 | '21 of 23' |
|  73.7 s | S06 | '23 of 23' |
|  75.2 s | S07 | headline changes; the previews and the sheet recede |
|  77.5 s | S07 | question 1 |
|  79.0 s | S07 | question 2 |
|  80.5 s | S07 | question 3 |
|  81.7 s | S07 | closing title overlays; SELL dissolves to the blank |
|  84.0 s | S07 | the subtitle line of the title draws in; the channel name settles |
