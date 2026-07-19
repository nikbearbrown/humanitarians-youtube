# PEDAGOGY — claude-liam-simd-free-speedup

## What the learner already knows
- int8 quantization reduces model size
- Microcontrollers have 32-bit registers
- Optimization usually requires code changes

## What this reel teaches
SIMD (Single Instruction Multiple Data) as a free 4× speedup already present in the hardware, left on the table by reference C kernels. The learner sees the scalar lane (4 clocks for 4 ops) vs the SIMD lane (1 clock for 4 ops packed in a register), and understands that enabling CMSIS-NN is a compile flag, not a rewrite.

## Act structure
- B00 COLD OPEN: hook — same chip, same clock, 4× faster if code asks
- B01 SCALAR LANE: 4 ops, 4 clocks — one-at-a-time sequential visualization
- B02 SIMD LANE: 4 int8 packed in one register, one instruction, 4 results — terracotta accent
- B03 SPEEDUP BAR: 4× comparison bar, "same chip, same clock, one compile flag"
- B04 YOUR TURN: ClaudeComposerAsk with CMSIS-NN build check prompt
- B05 OUTRO: ClaudeTitleOutro

## Pedagogy checklist
- Problem stated before solution (B01 scalar before B02 SIMD) ✓
- Root cause named: reference C code doesn't emit SIMD instructions ✓
- Mechanism animated: byte-lane packing in register, one instruction ✓
- Concrete numbers: 4 clocks vs 1 clock, 4× speedup ✓
- No technical term before the beat that created the need for it ✓
- Your Turn prompt is concrete and actionable ✓
- Length: ~67s estimated < 3:00 ✓

VERDICT: PASS
