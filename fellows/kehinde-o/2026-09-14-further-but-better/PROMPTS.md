# PROMPTS.md — Further, But Better

No open generation slots. Every beat is either a deterministic Remotion render
or the author's own Manim animation, so there are no prompts to fill and no paid
API calls.

The two prompts that appear ON SCREEN, as content:

## B00 — the cold-open ask
> I implemented three post-training quantization methods on GPT-2 from their
> papers and measured 34 configurations on one fixed protocol. The winning method
> ends up with weights FURTHER from the originals than naive rounding, yet its
> outputs are closer. Help me explain why moving further can hurt less.

## B07 — the viewer handoff prompt
> Take a benchmark comparing two methods, mine or one from a paper. List every
> setting that differs between the two arms: data, preprocessing, tuning budget,
> scale granularity, hardware, evaluation protocol. Then tell me which of those
> differences could produce the reported result on its own. Do not tell me which
> method is better. Tell me what else changed.

Read aloud verbatim in the narration, per HANDOFF LAW.
