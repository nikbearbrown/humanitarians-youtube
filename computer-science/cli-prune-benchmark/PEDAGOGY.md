# Pedagogy Audit — cli-prune-benchmark

## Question on screen before answer
B01 ends with the implicit question: when does pruning actually reduce latency?
The answer arrives in B04 with the bar chart punchline.

## Problem setup before CLI
B01_Problem establishes the pruning lie (sparse on paper, dense in silicon)
before the terminal appears in B02. Stakes are clear: SRAM and latency don't
move for unstructured pruning on embedded kernels.

## Concrete before abstract
Dense GEMM kernel behavior explained through the 3-metric bar chart (B04)
before the hypothetical sparse path (B06). No jargon without definition.

## One revision (B05 CHANGE)
The change beat adds the hypothetical sparse kernel column -- shows the counterfactual
and draws the boundary between what ships today and what would require kernel support.

## Teardown voice
No "obviously", "clearly", "important to understand", "in this video."
B02 opens: "Ask for the experiment. In the terminal: claude --"
Technical register maintained throughout.

## Illustrative data disclosure
B08 NEXT STEPS narration explicitly notes output beats use illustrative data
and instructs viewers to swap in real on-target latency captures.

## Duration check
Total estimated: 119s (under 5:00 cap). Each beat within expected range.
B00=5, B01=14, B02=15, B03=15, B04=17, B05=12, B06=12, B07=11, B08=10, B09=8.

VERDICT: PASS
