The Cell Dies Rich: Why a Battery That Still Reads Full Can Reset Your Device

A device resets, the screen goes dark, and the coin cell inside it can still be most of the way full. So what ran out? Not the charge. A coin cell is a three volt source with a small resistor hidden inside it, and that resistor is the story. When the device asks for a burst of current, some of the voltage is spent pushing the current through it, and what is left is all the device sees. Give the device a reset line, a voltage below which it restarts, and the cell has a limit: the biggest burst it can pass is the open voltage minus the reset voltage, divided by the resistance. The resistor does not stay put. Energizer's own plot shows it climbing as the cell is used, so the line comes down while the charge is still there. I built a model of a CR2032-class cell from two manufacturers' published graphs and ran three asks down the same line: eight milliamps never meets it (nothing stranded), thirty milliamps meets it with about a sixth of the cell unspent, sixty milliamps with almost half. Then the rule, done on paper with an old cell, and two numbers for you to look up for your own device: its biggest current draw, and the voltage where its chip resets.

Chapters:
0:00 A battery that is not empty
0:13 What I built, and the one question
0:29 The hidden resistor
0:56 The reset line
1:19 The line moves
1:46 A small ask: 8 milliamps
2:06 A medium ask: 30 milliamps
2:23 A large ask: 60 milliamps
2:39 The rule, on paper
3:17 What changes the answer
3:48 What this is not
4:08 Your turn

What this video claims, and what it does not:

- It is a model, fitted to graphs I read off two data sheets, so every number on screen is "about", not exact. I tested no real cell.
- The reset line is my own choice (two volts), not a particular chip's. The shape is the claim: the bigger the burst, the more charge is left behind when the device resets. The exact percentages are this model's, at this reset line.
- Results in the model, for a CR2032-class cell: a burst of 8 milliamps or less strands nothing; 10 milliamps about 1%; 30 milliamps about 16.5% (the line meets it at about 174 of a plotted 208 milliamp-hours); 60 milliamps about 48%; 100 milliamps resets a fresh cell on the first burst. Raising the reset line to 2.4 volts makes the 30 milliamp ask strand about 42%; using the resistance curve from a very slow drain, about 40%; letting resistance vary about 15% from cell to cell, most cells at 30 milliamps land between about 11% and 23%.
- The cell's resistance curve is Energizer's, read from a plot of a pulse test of about 30 milliamps, to a few ohms. Energizer says a device whose cutoff is above two volts may leave significant capacity unused: this film puts a number on how much, in a model.
- Not modelled: cold (which makes the voltage drop worse), a capacitor across the cell, and any real device's reset behaviour.

Sources: Energizer, Primary Lithium Coin Handbook and Application Manual (May 2026 edition), the resistance plot and the guidance on devices with a high cutoff; Duracell, CR2032 Lithium/Manganese Dioxide Battery datasheet (CR2032PGOE, 225 mAh version), the 3.0 volt and 225 milliamp-hour figures. The simulation is our own (the film's folder in the Humanitarians AI fellows repository carries the code, the fact-check and the measurements). Both documents state their values are typical and for reference only.

Narration is a synthetic voice (Kokoro, run locally). Visuals are original code-drawn animations: the manufacturers' graphs are redrawn from my own readings, not reproduced, and there are no third-party images, recordings or music.

Humanitarians AI - @HumanitariansAI
Tanmay Kulkarni, in for Humanitarians AI

Tags: coin cell, CR2032, battery, internal resistance, brownout, device reset, voltage drop, electronics, simulation, explainer, STEM, Humanitarians AI
