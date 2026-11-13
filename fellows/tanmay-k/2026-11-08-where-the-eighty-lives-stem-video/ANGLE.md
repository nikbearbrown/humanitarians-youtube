# Week 30 — Topic Video Angle (chosen)

Topic: `claude-for-computer-science/claude-liam-lstm-ops`. Formats: **16:9 long (3840x2160)** and **9:16 Short
(2160x3840)**, built side by side.

## What the source gives us
A clear, memorable observation: a model with fewer parameters can run far slower on a small device. The base film
shows it with a counter that climbs once per time step, and lands on the idea that parameters measure storage while
operations measure time. That is our starting point, and we keep it: the observation, the opening tension, and the
"choose by the number that matters for your deadline" ending.

## Our angle: "Where the Eighty Lives"
The base answers *what* happens (smaller, yet far slower). We take the next step and ask **what number predicts the
time**. A model's cost has two parts: how much arithmetic it does, and how much of that arithmetic can happen at the
same moment. The recurrent model's arithmetic is small and every step waits for the one before it. The convolutional
model's arithmetic is spread across positions that can all run together.

So the film follows one dial, **how much the chip can do at once** (its overlap), and one object, a single time step:
- Same weights and same arithmetic on both sides (our own matched sizes, stated on screen).
- Dial at zero: a chip that does one thing at a time. Both models take the same time (measured 1.0x).
- Turn it up: the chip can reuse each loaded weight across many positions. The parallel model speeds up; the
  recurrent one cannot, because step t+1 needs step t. Measured 1.0x -> 1.4x -> 5.7x. The work stays level, the gap opens.
- Sequence length is the second, quieter axis: the recurrent cost grows steadily with it and the ratio holds.
- The payoff returns to the opening observation and gives it a second number to sit beside the first:
  parameters say what it stores, operations say what it computes, **overlap says how long it waits**. The
  "eighty" is the base film's observed result; here is the part of the story that lives in the chip.

Framing rule: this is the base film's idea taken one level further, never a correction of it. On screen and in
narration we say "here is what sits underneath that number", not "the usual count misses it".

## Why it is unique
- Library: no other folder states "equal operations, unequal time" or dependency depth as the cause (code search
  of all branches, 2026-11-07). Nearest neighbours are quantization films, a different mechanism.
- Our Weeks 15-29: nothing on embedded latency or recurrent models.
- Shape: one dial and one repeating object, not a checklist. Different from Week 29's single rally replayed and from
  earlier list-shaped films.

## Evidence we will own (measured, not borrowed)
- First-principles counts for our stated sizes (an LSTM does about one multiply-accumulate per parameter per step).
- Our own timing (`MEASUREMENTS.md`, compiled C, same weights, same MACs, only the dependency differs): ratio 1.0x
  with no overlap available, 1.4x with weight reuse across rows, 5.7x with a vendor blocked matmul. The rough 28x from
  the first Python pass was interpreter overhead and is retired. Consequence: the dial is how much the chip can
  overlap, and the penalty belongs to model x hardware.
- Every number on screen is labelled as our model on our machine, not a claim about any specific chip or product.

## Two formats, one idea
- **Long (16:9):** the full dial. Opening observation, the matched-arithmetic setup, the overlap dial turning, the
  breakdown of where the time goes, the return to the opening object, a boundary, one viewer exercise.
- **Short (9:16):** its own arc, not the long cut shortened. Opens on the observation, shows one decisive turn of the overlap dial,
  ends on the three-numbers line as a finished thought. Own narration, own ending, state carries across cuts.
- Shared: one measured data file feeds both; same numbers, same palette, same terms. Vertical layouts are designed
  for 2160x3840, not cropped from 16:9.

## Boundaries (so we do not over-claim)
- Simplified model: dense LSTM and a conv-style stack at matched arithmetic; no specific MCU, no vendor numbers
  unless sourced.
- The source book is not in the repo, so we cite only what the folder's beat sheet states.
- Our laptop CPU is not an embedded chip. The film says what is general (dependency limits overlap) and what is
  ours (the measured ratio).

## Still to do before building (front-loaded)
1. DONE 2026-11-07: clean compiled measurement (`MEASUREMENTS.md`). Open: decide whether the film's dial is chip
   overlap (what the data supports) with sequence length as a secondary axis.
2. Optional: a second machine or a real embedded target; without one, no microcontroller number is claimed.
3. Content sweep of all refs for dependency-depth / parallelism / latency ideas in fellows' narration (read-only).
4. Read-aloud, FACTCHECK, FRICTIONAL, PEDAGOGY drafted for both formats before any render.
