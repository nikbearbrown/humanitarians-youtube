# Week 32 FACTCHECK (draft v2, 2026-11-23)

Sources read once and then deleted (downloaded with Tanmay's permission on 2026-11-23, to a temporary folder; the PDFs and page images were deleted after reading):
- **[E]** Energizer, *Primary Lithium Coin Handbook and Application Manual* (May 2026 edition, `Lithium-Coin-app-manual-0526.pdf`, 8 pages, 1.1 MB), pages 2 and 4 to 5 used.
- **[D]** Duracell, *CR2032 Lithium/Manganese Dioxide Battery* datasheet CR2032PGOE M0421, 225 mAh version (3 pages, 0.6 MB), page 1 used.
Both state their data is typical, for reference only, and subject to change.

| # | claim | status | source |
|---|---|---|---|
| 1 | Nominal 3 V Li/MnO2 coin cell; open-circuit voltage 3.0 V at +20 C | VERIFIED | [E] p1 (3 V nominal), [D] p1 |
| 2 | Nominal capacity 225 mAh (15 kOhm continuous, 2.0 V cut-off); nominal energy 657 mWh | VERIFIED | [D] p1 |
| 3 | Maximum continuous current 3 mA; maximum pulse current 10 mA at 1 s | VERIFIED | [D] p1. Note: the library film's "about 3 mA" is the continuous rating |
| 4 | AC impedance at 1 kHz is 20 ohm | VERIFIED | [D] p1 (a different measurement from the DC pulse resistance below) |
| 5 | Starting internal resistance of a 2032 is near 10 ohm (AA alkaline near 0.25 ohm) | VERIFIED | [E] p4 |
| 6 | Dual-pulse method: IR = change in voltage / change in current; worked example (3.279 V - 2.429 V) / (0.097 A - 0.000003 A) = 9 ohm | VERIFIED | [E] p4 |
| 7 | IR typically rises during discharge because of reaction by-products | VERIFIED | [E] p4 |
| 8 | IR curve, 2032 under a 75 ohm pulse (about 30 mA, 0.1 s on / 4.9 s off): about 10 ohm at start, about 13 to 15 up to roughly 100 mAh, about 19 near 150 mAh, about 28 near 185 mAh, about 45 near 200 mAh, about 65 near 208 mAh (cell exhausted at about 210 mAh) | READ FROM GRAPH, approximate (+/- a few ohm) | [E] p4 plot. Say "about" on screen; our model is fitted to this curve, not claimed as theirs |
| 9 | Resistance rise depends on drain: at 3 uA the same cell reaches about 25 ohm by 50 mAh and about 100 ohm by about 90 mAh | READ FROM GRAPH, approximate | [E] p4 inset. We use the 30 mA-pulse curve and say that drain changes the curve |
| 10 | Devices with a cut-off above 2.0 V "may leave significant capacity unused" | VERIFIED (quote, under 15 words) | [E] p2. This is the manufacturer's own statement of the thesis |
| 11 | Flat discharge curve until near end of life, then a quick voltage drop | VERIFIED | [E] p5 |
| 12 | Inrush currents can be several times the normal load and cause higher than expected drop | VERIFIED | [E] p5 |
| 13 | Colder temperatures reduce voltage and runtime; cold can cause an "excessive voltage drop" (garage-door sensor example) | VERIFIED | [E] p3. B10 says "cold ... makes the voltage drop worse"; the earlier wording "cold raises resistance" was dropped because [E] does not state it |
| 14 | Microcontroller reset threshold values | UNVERIFIED | pick one named public datasheet and cite it, or use our own "reset line" as a chosen parameter, labelled illustrative |
| 15 | Library film uses 1000 ohm, 8 mA, 2 V reset | VERIFIED | `cli-brownout/PEDAGOGY.md` and `README.md` on origin/main |

## Consequences for the angle
- At the datasheet's 10 ohm fresh figure, a fresh cell cannot brown out at 8 mA (drop 0.08 V). Brownout at a 2 V line needs R >= (3.0 - 2.0) / I: 125 ohm at 8 mA (beyond the graph's exhausted end), 33 ohm at 30 mA (reached near 190 mAh), 10 ohm at 100 mA (a fresh cell fails at once). So the burst size decides the stranded share, which is the film's measurable claim. The numbers go through our simulation before any is stated.
- Open-circuit voltage also falls near the end; the model must carry it, or the stranded share is overstated.
- Rule: a value stays "about" on screen if read from a graph; unverified values are dropped or labelled illustrative.
