# PROMPTS.md — Nothing Errored

No open slots. Every beat is a deterministic render: Remotion components from the
beat sheet, two structured math rows from `runtime/scripts/typeset_math.py`, and
one Manim scene re-rendered from the source repo. No generation prompts, no
pantry requests, no paid API calls. Fellow tier throughout.

The two prompts that appear ON SCREEN, as content:

## B00 — the cold-open ask
> I ran a model through a simulated year of production. At week 7 its accuracy
> fell eight points and not one request failed. Help me explain how the platform
> noticed, and why watching the inputs catches what watching the outputs cannot.

## B08 — the viewer handoff prompt
> Take an automated thing you rely on that has not errored lately. Do not check
> whether it is running. Check whether what goes into it still looks like what
> went into it when you built it.

Read aloud verbatim in the narration, per HANDOFF LAW.

## B04 — the Manim beat
Not a prompt. `DriftPSI` from `assets/manim_psi.py` in github.com/Kenny0bi/loom,
re-rendered at 3840x2160 with manim 0.18.1. The dark palette is the author's own
and is deliberately not retinted to the Claude cream ground.

Build note: the scene uses MathTex, so it needs `dvisvgm` on PATH. On this machine
that lives in TinyTeX at `~/Library/TinyTeX/bin/universal-darwin`, which is not on
the default PATH. Without it manim fails at the .dvi to SVG step.

## Data provenance
Figures were recomputed from the repo's committed `assets/lifecycle.json` during
the build, not taken from its README. Where the two disagreed, the run data was
used. See FACTCHECK.md.
