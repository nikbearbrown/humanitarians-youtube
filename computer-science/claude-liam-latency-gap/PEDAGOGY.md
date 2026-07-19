# PEDAGOGY — claude-liam-latency-gap

## What the learner already knows
- Embedded AI models run inference on microcontrollers
- There is a gap between spec-sheet estimates and real hardware performance
- Profiling exists as a concept

## What this reel teaches
Three named, fixable causes for the latency gap — reference vs SIMD kernels, activation memory spill, and float vs int8 — presented as a waterfall of sequential fixes, each with a named mechanism and a measured drop. The learner leaves knowing where to look and in what order.

## Act structure
- B00 COLD OPEN: hook — the gap (367 ms predicted, 1,200 ms measured)
- B01 INITIAL GAP: visualize the 1,200 ms bar vs 100 ms target — stakes
- B02 FIX 1 SIMD: SIMD kernels drop bar to 400 ms — mechanism named
- B03 FIX 2 MEMORY: memory spill fix drops bar to 200 ms — mechanism named
- B04 FIX 3 INT8: int8 drops bar to 45 ms under target — outcome celebrated
- B05 YOUR TURN: ClaudeComposerAsk with profiler prompt
- B06 OUTRO: ClaudeTitleOutro

## Pedagogy checklist
- Problem stated before fixes (B01 precedes B02-B04) ✓
- Each fix has a named mechanism and a measured result ✓
- Waterfall structure: sequential, cumulative, concrete ✓
- No technical term before the beat that created the need for it ✓
- Manim scenes show data, not decorative text ✓
- Anchor-not-transcript: Manim labels are data chips ✓
- No utility framing ✓
- Your Turn prompt is concrete and actionable ✓
- Length: ~89s estimated < 3:00 ✓

VERDICT: PASS
