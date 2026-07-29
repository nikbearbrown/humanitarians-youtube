"""scenes.py — intentionally carries ZERO Manim Scene classes.

This reel (claude-hai · "Personalized, Project-Driven Reading Roadmaps for CaNCURE
Trainees") is REMOTION-ONLY. Every beat renders from a registered Remotion composition:

  B00 / B08  ClaudeComposerAsk        (shipping claude scene)
  B07        ClaudeVerdictArtifact    (shipping claude scene)
  B09        ClaudeTitleOutro         (shipping claude scene)
  B01–B06    ReadingRoadmaps.tsx      (reel-local, registered in runtime/remotion/src/Root.tsx;
                                        portable copy in this reel's remotion-src/)

runtime/scripts/run.sh REFUSES to render a reel that has no scenes.py (so it never slots
the shared electoral-college fixture scenes into another film). This placeholder satisfies
that guard: it defines no `class Bxx_...(Scene)`, so run.sh renders no Manim, then proceeds
to the Remotion fill-in pass (remotion_scenes.py) and compile.py. Do not add Manim scenes here.
"""
