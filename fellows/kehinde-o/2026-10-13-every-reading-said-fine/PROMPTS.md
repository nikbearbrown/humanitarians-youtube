# PROMPTS.md — Every Reading Said Fine

No open slots. Every beat is a deterministic render: Remotion components from the
beat sheet, plus two structured math rows produced locally by
`runtime/scripts/typeset_math.py`. No generation prompts, no pantry requests, no
paid API calls. Fellow tier throughout.

The two prompts that appear ON SCREEN, as content:

## B00 — the cold-open ask
> I ran my vitals pipeline over 1,800 readings from one deteriorating patient.
> Their oxygen saturation fell 18 points. 62 percent of the individual readings
> still scored as normal. Help me explain why a single reading cannot see this,
> and what does.

## B08 — the viewer handoff prompt
> Take a number you check regularly. Instead of asking whether today's value is
> acceptable, line up the last five and ask which way they point. That question
> catches what no single check will.

Read aloud verbatim in the narration, per HANDOFF LAW.

## A beat that was considered and dropped
The project's own telemetry interface was going to be shown as a still. It was
dropped: the committed screenshot is 1440 pixels wide and would have needed a 2.7x
upscale to fill a 4K frame, and re-capturing the live demo at 3840 reflows the
layout into a single row with two thirds of the frame empty. The build requires 4K
at source, so the beat was rebuilt as a native component instead.

## Data provenance
Figures were computed by running the repo's own simulator and scorer in the build
session. See FACTCHECK.md for the reproduction recipe.
