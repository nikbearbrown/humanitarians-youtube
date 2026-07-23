# Pedagogy Audit — cli-pareto-selector

## Question on screen before answer
B01 frames the question: the leaderboard winner runs at 400ms and misses the deadline.
What is the correct selection tool? The Pareto frontier is named at the end of B01,
demonstrated in B04.

## Problem setup before CLI
B01_Problem establishes the benchmark accuracy trap before the terminal appears in B02.
Stakes are concrete: accuracy alone fails the latency constraint.

## Concrete before abstract
The scatter plot (B04) shows real model positions before the abstract dominance definition
from the code (B03) is applied. Viewers see which models disappear before learning why.

## One revision (B05 CHANGE)
The change beat applies a 250ms constraint mask -- shows that the unconstrained frontier
still contains models that can't ship.

## Teardown voice
No "obviously", "clearly", "important to understand", "in this video."
B02 opens: "Ask for the experiment. In the terminal: claude --"
Concrete register throughout.

## Illustrative data disclosure
B08 NEXT STEPS narration explicitly flags illustrative data and instructs viewers
to swap in real accuracy, latency, and flash measurements.

## Duration check
Total estimated: 119s (under 5:00 cap).
B00=5, B01=14, B02=15, B03=15, B04=17, B05=12, B06=12, B07=11, B08=10, B09=8.

VERDICT: PASS
