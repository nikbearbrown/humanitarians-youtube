"""scenes.py — Manim scene set for `hussain-snowshift-migration-overview`.

DELIBERATELY EMPTY.

run.sh discovers Manim work by regex-scanning this file for
`class <BID>_<Name>(Scene)`, and refuses to run a reel with no scenes.py at all
(it would fall back to the toolkit's shared fixture scenes). This reel has no
Manim beats — every visual slot is a Remotion composition:

    B00 B04 B11   ClaudeComposerAsk      (cold open · ask micro-beat · handoff)
    B01           BrutalistHesitantWriter
    B02           SnowMonolith
    B03           SnowLintCatch
    B05           SnowDeployRail
    B06           SnowParity
    B07           SnowConstraintGap
    B08           SnowSmokeProof
    B09           CortexWhereItBites
    B10           ClaudeVerdictArtifact
    B12           CortexTitleOutro

The Snow* components live in runtime/remotion/src/scenes/SnowshiftIllus.tsx.
"""
