# Beat 3 — Quality Gates

**Visual type:** Remotion
**Duration:** ~12 seconds

## What the viewer sees

A conveyor belt running left to right. Chunks (small rectangular cards) move along the belt toward the reader nodes on the right.

**Input gate (0-6s):**
A vertical gate barrier rises before the readers, labeled "INPUT GATE."

Chunks approach the gate in a steady stream. Most pass through — the gate lifts briefly for each good chunk and it continues right.

Three chunks are stopped in sequence:
1. A blank/grey chunk approaches → gate blocks it → stamp: "EMPTY" in red → chunk drops off the belt into a bin below labeled "Rejection Log"
2. A chunk with red-highlighted text → gate blocks it → stamp: "BOILERPLATE 0.87" → drops into the bin
3. A tiny sliver chunk → gate blocks it → stamp: "TOO SHORT" → drops into the bin

The rejection bin has a counter: "Rejected: 3" — it logs but doesn't process.

**Output gate (6-12s):**
The belt continues past the reader nodes and the triangulator (shown as compact icons, not fully drawn). A second gate barrier appears on the right side, labeled "CONFIDENCE GATE."

Signals come out of the triangulator and approach this gate. Most pass through. One signal shows a confidence badge of "0.31" — the gate stops it. Stamp: "LOW CONFIDENCE." It is diverted downward into a separate bin labeled "Audit Log." A small label appears: "Logged. Not scored."

The good signals continue past the gate into the Scorecard.

## Technical notes

- The conveyor belt should feel mechanical and systematic — this is quality control, not drama
- The two gates are the visual anchors — physical barriers that stop bad data
- Rejection stamps should be clear and readable — red text on the chunk
- The bins below should feel like organized storage, not trash — these are logged for analysis
- Keep the reader nodes and triangulator compact in this beat — they were the stars in Beats 1-2, here they're background
