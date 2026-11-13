"""scenes.py — Manim scene set for `ai-data-quality`.

DELIBERATELY EMPTY.

run.sh discovers Manim work by regex-scanning this file for
`class <BID>_<Name>(Scene)`. It also REFUSES to run a reel that has no
scenes.py at all, because it would then fall back to the toolkit's shared
animated_graphics.py — which carries only the electoral-college fixture
scenes, and would slot another film's graphics into these beats.

This reel has no Manim beats. Every one of its twelve visual slots is a
Remotion composition (see beat_sheet.json → shot.remotion.pattern):

    B00 B04 B10   ClaudeComposerAsk      (cold open · ask micro-beat · handoff)
    B01           DqScoreVsField
    B02           DqRuleScale
    B03           DqRuleCard
    B05           DqProposal
    B06           DqRatifyGate
    B07           DqPipelineGate
    B08           DqWhereItBites
    B09           ClaudeVerdictArtifact
    B11           ClaudeTitleOutro

So this file exists to satisfy the guard and to declare, in writing, that the
absence of Manim here is a choice and not an oversight. Defining zero Scene
classes makes run.sh's PENDING list empty — it prints "nothing to render —
recompiling only", skips GATE F/A/W/B, and goes straight to the Remotion
fill-in pass and the compile.

If a future revision adds a math or simulation beat, add it here as
`B0X_SomethingDescriptive(Scene)` and run.sh will pick it up with no other
change.
"""
