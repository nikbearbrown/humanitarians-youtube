# PEDAGOGY — cli-int8-mash

## What the learner already knows
- Basic Python and numpy
- That model weights are stored as float32 in training
- Vague notion that quantization saves memory

## What this reel teaches
The workflow loop, not the math: how to write a precise quantization prompt (formula +
both tensors + what to measure), how to read the generated affine-int8 code and find the
scale line, how to verify the collapse metric (unique floats vs distinct levels), and how
to issue the per-channel fix command. The mash is the excuse to run the loop.

## Loop structure (CLI style)
1. PROBLEM: why int8 quantization matters — and where it silently breaks
2. ASK: write a script that implements the formula and tests two cases
3. CODE: find the scale/zero-point lines; verify the formula
4. OUTPUT: run it; check the collapse metric (249 levels vs 2 levels)
5. CHANGE: give each channel its own scale
6. OUTPUT: verify recovery (2 levels -> 255 levels)
7. SUMMARY: name the root cause
8. NEXT STEPS: give the viewer a concrete action

## Act structure (10-beat required spine)
- B00 INTRO brand open — no thesis ✓
- B01 PROBLEM sets up the stakes (4x smaller, harmless for weights, lethal for activations) ✓
- B02 ASK cold open terminal prompt — the experiment framed ✓
- B03 CODE names the mechanism (scale sets step size, one denominator) ✓
- B04 OUTPUT Manim: 249 levels vs 2 levels — the divergence revealed ✓
- B05 CHANGE iterate beat — per-channel fix command ✓
- B06 OUTPUT Manim: 255 levels recovered — the fix confirmed ✓
- B07 SUMMARY root cause named: one scale for all vs per-channel ✓
- B08 NEXT STEPS concrete viewer actions: dump activations, verify toolchain ✓
- B09 OUTRO brand close ✓

## Pedagogy checklist
- Problem stated before CLI (B01 precedes B02) ✓
- Mechanism animated, not stated as text ✓
- THE PRACTICE present: "per-channel scale from own min/max" is a concrete, checkable move ✓
- Root cause named explicitly: "one scale set by the widest tensor" ✓
- No utility framing ("important to understand", "in this video") ✓
- No technical term before the beat that created the need for it ✓
- Simulation-first: B04 and B06 are animations, not stills ✓
- Length: ~118s < 5:00 ✓
- Anchor-not-transcript: on-screen text (Manim labels) are chips, not spoken sentences ✓
- No equations on screen ✓
- Next steps are concrete and actionable (not "learn more") ✓

VERDICT: PASS
