# Pedagogy Review

## Topic
Nothing Errored: how you find out a working AI model has quietly stopped working
(built on my own loom repo)

## Learning Objective
The viewer leaves knowing that a failing model keeps answering every request, so
uptime tells you nothing about correctness, and that the practical check is to
watch whether the inputs still look like the inputs you trained on. They can
apply that to any automated thing they rely on.

## Audience
General audience. No machine learning background assumed. "Drift" is explained as
the routine changing, and the statistics are described in words before they appear
as notation.

## The ONE Idea
A broken model does not look broken. It answers on time, every time, and the
answers are worse. The output side gives you no signal, so the signal has to come
from the input side.

## Math Gate (docs/MATH-TYPESETTING.md)
B03 uses TypesetMath with two structured SVG rows, not formula strings:
- Population stability index as a sum over buckets, with a real fraction inside
  the logarithm and proper subscripts
- The two-proportion z-test with a real fraction bar and a radical

Algebra check: PSI sums over buckets i with free index i bound by the summation;
each term is (actual minus expected) times the log of their ratio, which is the
standard symmetrised form. The z-test denominator uses the pooled proportion, so
the hat on p is deliberate and distinct from the two group proportions.

## Evidence Gate (docs/EXECUTABLE-EVIDENCE.md)
No figure is taken from the repo README. Every number was recomputed in this
session from `assets/lifecycle.json`, the committed record of the simulated year.
Where the README and the run data disagreed (the README narrates a drop from 0.70,
the data records 0.638 to 0.555) the run data was used and the README was treated
as stale. B04 is my own Manim scene re-rendered at 3840x2160 rather than upscaled.

## Restraint Gate
- The demo is a simulation on synthetic caregiver logs, not a clinical system and
  not a claim about real patients. The video says "a care programme" and does not
  present it as deployed.
- No claim that this platform is production-grade or competes with managed MLOps
  tools. The measured claim is that it detected a drift, earned two promotions on
  live traffic and reverted a poisoned model automatically.
- The false alarm at 112 samples is reported as a bug in my own monitor, not
  smoothed over.

## VERDICT: PASS
