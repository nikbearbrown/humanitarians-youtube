# Pedagogy Review

## Topic
Backwards Along the Tape: what backward() actually computes, built on Kehinde's ember repo

## Learning Objective
The viewer leaves able to say what backpropagation does in one sentence: multiply local
derivatives along a path, and add them where paths meet. They also leave with a concrete
way to check a gradient themselves.

## Audience
General audience with curiosity about how neural networks learn. No calculus fluency
assumed; the chain rule is explained in words before it is shown as notation.

## The ONE Idea
backward() is a single rule applied in reverse along a recorded tape. Each operation only
needs its own local derivative. Composition handles the rest.

## Math Gate (docs/MATH-TYPESETTING.md)
B03 uses TypesetMath with three structured SVG rows:
- The composition L = f(g(x))
- The chain rule with real fraction bars and partial symbols
- Gradient accumulation as a sum over paths, with a proper summation index
B04 is Manim MathTex, also structured typography, re-rendered at 3840x2160.
Algebra checked: the accumulation row is the multivariable chain rule where x feeds
several downstream values, which is exactly what ember's tape does when a tensor is used
more than once. Free index x, bound index k.

## Evidence Gate (docs/EXECUTABLE-EVIDENCE.md)
No figure is copied from the repo README. Every number was read in this session from
assets/parity_log.json (max gap 2.682e-07, mean 5.363e-08 over 300 steps),
assets/shakespeare_log.json (val loss 4.491 at init, 1.8336 final, 1,625 tokens/sec) and
assets/mnist_log.json (97.83% test accuracy). The uniform-guessing floor of 4.17 is
ln(65) for the 65-character vocabulary, computed here.

## Restraint Gate
- No claim that this engine competes with PyTorch on speed or coverage. The claim is
  agreement on gradients, which is what was measured.
- The "worse than guessing at initialisation" point is stated plainly rather than hidden.

## VERDICT: PASS
