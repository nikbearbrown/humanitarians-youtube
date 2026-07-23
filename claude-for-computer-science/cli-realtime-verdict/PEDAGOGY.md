# Pedagogy Audit — cli-realtime-verdict

## Question on screen before answer
B01 frames the key question: if mean latency passes the test, why does the system fail?
Answer: WCET tail exceeds the deadline, demonstrated in B04.

## Problem setup before CLI
B01_Problem establishes the mean-vs-WCET distinction before the terminal appears in B02.
The GC pause scenario grounds the stakes concretely.

## Concrete before abstract
The histogram (B04) shows the actual tail before the formal classification (soft/firm/hard)
from the code. GC jitter added in B06 extends that concrete demonstration.

## One revision (B05 CHANGE)
The change adds GC/DMA jitter -- extends the tail past the original WCET to show
that the mean remains unchanged while the worst case doubles.

## Teardown voice
No "obviously", "clearly", "important to understand", "in this video."
B02 opens: "Ask for the experiment. In the terminal: claude --"
No hedging, no padding.

## Illustrative data disclosure
B08 NEXT STEPS narration explicitly notes output beats use illustrative distributions
and instructs viewers to swap in their real measured latency array.

## Duration check
Total estimated: 119s (under 5:00 cap).
B00=5, B01=14, B02=15, B03=15, B04=17, B05=12, B06=12, B07=11, B08=10, B09=8.

VERDICT: PASS
