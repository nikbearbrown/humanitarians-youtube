# READ-ALOUD — The Cell Dies Rich (long film, 16:9), draft 2, signed

Narration of record, **signed at Gate P on 2026-11-23** (B10 re-signed the same day after one clause was reworded). Numbers in words. Every figure comes from `experiment/stranded_energy.py` (our own simulation, results in `MEASUREMENTS.md`) or the manufacturer values listed in `FACTCHECK.md`. The estimated seconds in the beat headings are from the draft; the measured timing is in `beat_sheet.json`. The reset line is our own chosen number and the film says so.

TTS note: say the name as "Cool-car-knee" (respelled in the audio script, kept as Kulkarni on screen); every other flagged word checked with Kokoro's phonemizer and reads cleanly (milliamps, milliamp-hours, ohms, Energizer, reset, stranded).

Companion: the Short (`READ-ALOUD-SHORT.md`) is written to stand alone and to hand the viewer to this film. It covers the one idea (the line that moves) and two of the three asks; this film adds the third ask, the sums, what changes the answer, and the limits.

**B00 · THE CRASH** (~17 s) — curious

A battery can be most of the way full and still be finished for the thing it powers. The gadget resets, the screen goes dark, and the cell can still have plenty inside. So what, exactly, ran out? In that case, it was not the charge.

**B01 · THE SETUP** (~19 s) — hands-on

I'm Tanmay Kulkarni, in for Humanitarians AI. I did not open a real battery. I built a model of a C R twenty thirty-two coin cell from two manufacturers' published graphs. Then I asked it one question again and again: how much is still left at the moment a device resets?

**B02 · THE HIDDEN RESISTOR** (~34 s) — plain

First, why a battery's voltage drops at all. A coin cell is a three volt source with a small resistor hidden inside it. Energizer, a maker of these cells, says a fresh one starts near ten ohms. When a device asks for current, some of the voltage is spent pushing that current through the resistor, and what is left is what the device sees. Ask for thirty milliamps, and a fresh cell loses about three tenths of a volt. Voltage at the terminals equals the open voltage, minus the current times the resistance.

**B03 · THE LINE** (~29 s) — diagnostic

Now give the device a reset line. Below some voltage, it restarts. I chose two volts for mine. That turns into a limit. The largest burst the cell can pass is the open voltage, minus two volts, divided by the resistance. A fresh cell, at ten ohms, can pass about a hundred milliamps. Anything larger, and the device resets on the first try. So there is a line, and your burst either sits under it or it does not.

**B04 · THE LINE MOVES** (~35 s) — surprised

Here is what made me sit up. The resistor does not stay ten ohms. Energizer's own plot, from a pulse test of about thirty milliamps, shows it climbing as the cell is used. As I read it: about fourteen ohms, then nineteen, then twenty-eight, then forty-five, and about sixty-five at the very end. So the line comes down. At the start, about a hundred milliamps. A hundred and fifty milliamp-hours in, about forty-three. Near the end, about eight and a half. The cell is the same cell the whole time. What it can safely give is not.

**B05 · A SMALL ASK** (~28 s) — measured

Now I make three asks. First, a small one: eight milliamps. I ran it all the way down. It never crosses the line. Even at the very end of the plotted run, the line is only just above eight. So in my model the device uses the whole cell, and nothing is stranded. At ten milliamps, the cell is nearly spent when it resets, with about one percent left. A small ask spends almost everything.

**B06 · A MEDIUM ASK** (~19 s) — surprised

Second, a medium ask: thirty milliamps. Now the falling line meets it. It happens at about one hundred seventy-four milliamp-hours used, out of a plotted two hundred eight. The device resets with about sixteen and a half percent of the cell unspent. Roughly one part in six, locked inside a cell that tests fine.

**B07 · A LARGE ASK** (~19 s) — deflated

Third, a large ask: sixty milliamps. This one meets the line at about one hundred eight milliamp-hours. The device resets with almost half the cell unspent, forty-eight percent. And at a hundred milliamps, a fresh cell resets on the first burst, with all of it left. Same cell, three asks, and three different endings.

**B08 · THE RULE** (~47 s) — careful

Here is the rule, and you can do it on paper. The largest burst a cell can pass is the open voltage, minus the reset voltage, divided by the resistance. Let's try one together, with an old cell: its resistance is forty ohms, and its open voltage is two point seven volts. Two point seven, minus two, is point seven. Point seven, divided by forty, is about seventeen and a half milliamps. Any burst over that, and the device resets, however much charge is left. Check it: a device asking for twenty-five milliamps resets on that old cell, and one asking for ten does not. Now do yours, by looking up two numbers in your device's data sheet: its biggest current draw, and the voltage where its chip resets.

**B09 · WHAT CHANGES THE ANSWER** (~38 s) — careful

I pushed on the model to see what moves it. Raise the reset line from two volts to two point four, and the thirty milliamp ask strands forty-two percent, not sixteen and a half. Energizer's handbook makes the same point: a device whose cutoff is above two volts may leave significant capacity unused. Use a resistance curve from a very slow drain, and the same ask strands about forty percent. And one cell is not every cell. If I let resistance vary by about fifteen percent from cell to cell, most cells at thirty milliamps land between about eleven and twenty-three percent.

**B10 · WHAT THIS IS NOT** (~27 s) — careful

Let me be plain about what this is. It is a model, fitted to graphs I read off two data sheets, so every number is about, not exact. I tested no real cell. I did not model cold, which makes the voltage drop worse. I did not model a capacitor. And the reset line is my own choice, not a chip's. What holds is the shape: the bigger the ask, the more is left behind.

**B11 · YOUR TURN** (~17 s) — handed over

So the next time something resets with a battery that still reads fine, do not ask how much charge is left. Ask how big its biggest burst is, and where the line sits. A cell can die rich. How rich depends on what you ask of it.

---
Word counts, runtime and checks are in the build notes; first-pass read at about two point seven words a second is roughly five and a half minutes.
