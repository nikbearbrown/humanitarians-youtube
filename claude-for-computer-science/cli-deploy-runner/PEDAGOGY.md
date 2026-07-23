# Pedagogy Audit -- cli-deploy-runner

## Question on screen before answer
B01 frames the question: 94% in Python, 91% after toolchain -- where did the 3% go?
Answer arrives in B04 (layer 7 divergence spike) and B06 (CMSIS-NN FALLBACK explanation).

## Problem setup before CLI
B01_Problem distinguishes toolchain-induced accuracy loss from quantization error
before the terminal appears in B02. Stakes are concrete: silent accuracy drop.

## Concrete before abstract
The divergence bar chart (B04) shows the spike visually before the op-check mechanism (B06)
explains it. Viewers see the anomaly before the cause.

## One revision (B05 CHANGE)
The change adds per-op CMSIS-NN support check -- explains the mechanism behind the spike
and localizes the fix.

## Teardown voice
No "obviously", "clearly", "important to understand", "in this video."
B02 opens: "Ask for the experiment. In the terminal: claude --"
Concrete technical register throughout.

## Illustrative data disclosure
B08 NEXT STEPS narration explicitly notes output beats use illustrative divergence values
and instructs viewers to bring a real trained model + validation set.

## Duration check
Total estimated: 119s (under 5:00 cap).
B00=5, B01=14, B02=15, B03=15, B04=17, B05=12, B06=12, B07=11, B08=10, B09=8.

VERDICT: PASS
