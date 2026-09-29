# PROMPTS.md — Backwards Along the Tape

No open slots. Every beat is a deterministic render: Remotion components from the beat
sheet, three structured math rows produced locally by `runtime/scripts/typeset_math.py`,
and one Manim scene re-rendered from the source repo. No generation prompts, no pantry
requests, no paid API calls. Fellow tier throughout.

The two prompts that appear ON SCREEN, as content:

## B00 — the cold-open ask
> I wrote a tensor autograd engine from scratch on raw NumPy and trained a 624K-parameter
> GPT with it, no PyTorch anywhere in the loop. Help me explain what backward() actually
> computes, and how I proved my version agrees with PyTorch rather than just claiming it
> does.

## B08 — the viewer handoff prompt
> Take the smallest network you can write and work out one gradient by hand. Then nudge
> that weight and measure how the loss changes. If the analytic number and the numerical
> number agree, you understand backpropagation.

Read aloud verbatim in the narration, per HANDOFF LAW.

## B04 — the Manim beat
Not a prompt. `ChainRuleOnTape` from `assets/manim_chain_rule.py` in
github.com/Kenny0bi/ember, re-rendered at 3840x2160 with manim 0.18.1. The dark ember
palette is the author's own and is deliberately not retinted to the Claude cream ground.

Build note: this scene uses MathTex, so it needs `dvisvgm` on PATH. On this machine that
lives in TinyTeX at `~/Library/TinyTeX/bin/universal-darwin` and is not on the default
PATH. Without it manim fails at the .dvi to SVG step.

## Data provenance
Figures were read from the repo's committed run logs in the build session, not taken from
its README. See FACTCHECK.md for the file-by-file trace.
