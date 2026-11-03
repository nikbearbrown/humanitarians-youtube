"""
scenes.py -- Manim scenes for "The Tier That Grades the Papers" (hai-kk_brutalist).

This reel is entirely Remotion-driven -- there are no Manim beats. Every beat
resolves via one of five Remotion patterns declared in beat_sheet.hai.json
under shot.remotion.pattern:

    ClaudeComposerAsk     -- B00 (cold open), B08 (handoff)
    TierPyramidBeat       -- B01, B02, B03, B05, B06 (the tier-framework exhibit)
    PredictCard           -- B04 (mid-reel commitment beat)
    ClaudeVerdictArtifact -- B07 (verdict)
    ClaudeTitleOutro      -- B09 (outro)

All five are rendered by runtime/scripts/remotion_scenes.py, not by this file.

This stub file exists purely so that run.sh's Manim-scenes guard -- which
refuses to render the shared animated_graphics.py electoral-college fixture
into an unrelated film's beats -- finds a scenes.py to resolve against and
sees zero pending Manim scenes to build. Nothing else in the pipeline reads
this file's contents; it is a satisfied precondition, not active code.
"""
