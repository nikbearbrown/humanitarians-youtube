# Week 32 topic video — ANGLE (final, 2026-11-23)

**Topic:** `claude-for-computer-science/cli-brownout` (library film: "A Battery Can Be Full and Still Crash Your Device").
**Formats:** one 16:9 long film (3840x2160) and one 9:16 Short (2160x3840), each with its own script (not a cut).
**Working title:** "The Cell Dies Rich" (slug `the-cell-dies-rich`).

## Thesis (measured in our simulation, `MEASUREMENTS.md`; title kept by Tanmay 2026-11-23)
A coin cell is finished for a device not when its charge runs out but when its internal resistance R crosses
**(V_open - V_reset) / I_burst**, so **how rich the cell dies depends on the burst you ask for**. In our model
(2.0 V reset line, a cell fitted to published graphs): a burst of 8 mA or less strands nothing; 10 mA about 1%;
30 mA about one sixth; 50 mA about a third; 60 mA nearly half; 100 mA all of it. The title is true for large bursts and
the film says exactly that, with the numbers, and names where it stops being true. Teachable move: compute the usable
limit from resistance and burst current, not from the percentage left.

## What the library film states, and what ours adds
States: V = V_oc - I*R; one fixed illustrative resistance (1000 ohm), an 8 mA burst, a 2 V reset line; a 100 uF
capacitor flattens the sag; energy and instantaneous delivery are different questions. Leaves open: find the threshold,
measure the burst, size the cap. Ours starts from the same puzzle and adds one thing it does not show: resistance is
not fixed, it grows as the cell is used, so the **burst current that is safe shrinks over the cell's life**, and the
share of energy still unspent at the first brownout can be computed for any burst. No capacitor sizing (that is the
library film's hand-off; we leave it alone).

## Our own evidence (built and run)
`experiment/stranded_energy.py` (python3.12 + numpy, seed 32): terminal voltage = Voc(q) - I*R(q), curves read from the
Energizer and Duracell graphs, first burst under the reset line is the brownout; reports the share unspent. Checked two
ways (grid vs burst-by-burst, agree to 0.009 mAh), plus sensitivity to reset line, resistance scale, open-circuit curve
and drain-dependent resistance, and a unit-spread band. Results and limits: `MEASUREMENTS.md`. The reset line is our
chosen parameter.

## Inputs (sourced; see FACTCHECK.md v2)
Nominal 3 V, 225 mAh, 657 mWh, 10 mA max pulse, 3 mA max continuous (Duracell datasheet); starting resistance near
10 ohm and a resistance curve that climbs from about 10 ohm to about 65 ohm over the cell's life under a roughly
30 mA pulse (Energizer handbook, read from a graph: "about"). Energizer itself notes that a device cut-off above 2.0 V
can leave significant capacity unused: the thesis, stated by the maker. Reset line is our chosen illustrative
parameter unless a named datasheet is cited.

## Boundaries (stated on screen, deliberate)
- An illustrative model, not a bench measurement. We measured no real cell.
- One cell type, room temperature. Cold raises resistance; not modelled beyond a sentence.
- Pulse behaviour is modelled as a simple resistor; real cells also sag over a long pulse (polarisation). Said, not modelled.
- Resistance values come from public datasheet-order figures, cited in FACTCHECK; the film says "order of" not exact.
- The library film's 1000 ohm is a round teaching number; ours uses datasheet-order values and says why the number differs.
  No fault-finding; it is a different question (fixed R versus R that grows).

## Structure (derived from the subject, not a template)
**Long, "THE LINE MOVES":** one fixed picture from the first frame: a tank (charge left) beside a line that is the
largest burst the cell can still pass. Each burst size draws a horizontal "ask" on the chart; as the cell is used the
allowed-burst curve falls; the moment the curve drops under an ask, the device browns out, and the tank still shows
what is left. Three asks (about 10, 30 and 60 mA) fail at three different fill levels (about 1%, 16% and 48% left); an 8 mA ask never fails, and the film says so. The cell is never shown wasting much for small bursts. Then the viewer's exercise.
**Short, one scene:** the tank and the line, one ask, the curve falls, the crash, the tank still full-ish, last line is
the question the long film answers.

## Tone arc
puzzled (the gauge says plenty) -> hands-on (watch the line move) -> surprised (the same cell has three different
deaths) -> careful (what the model leaves out) -> handed over (your device, your burst). First person, humane, years
in words, no politics, no third-party media.

## Uniqueness (swept 2026-11-23)
Fellow folder names, fellow file contents (local refs), our Weeks 15-31 narration/scripts/angles: no battery,
resistance or sag material. Content check of the 30 moved fellow branches: all 4,140 recent text files fetched (0 failed), 0 hits for
brownout, internal resistance, coin cell, CR2032, Thevenin. Run on the final narration, the only overlap with earlier films is the read-aloud header text and the standard sign-on (4.5% of words).
