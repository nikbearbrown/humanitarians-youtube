# scenes.py — gemma4-unified
#
# Intentionally empty of Scene classes.
#
# This reel is PURE REMOTION: every beat's visual is a Remotion composition
# rendered through runtime/scripts/remotion_scenes.py. There are no Manim beats,
# so there is nothing for manim to render here.
#
# run.sh REFUSES any reel folder without a scenes.py (every real reel is
# supposed to carry its own graphics module rather than lean on the shared
# animated_graphics.py), so this file exists to satisfy that check and to
# document WHY it is empty.
#
# Beat → composition map (see beat_sheet.json for props):
#   B00  ClaudeComposerAsk        (UI — the ask)
#   B01  GemmaEncoderStack        focus="specialists"
#   B02  GemmaEncoderStack        focus="vision"
#   B03  GemmaEncoderStack        focus="audio"
#   B04  PredictCard              (commit before the reveal)
#   B05  GemmaScoreboard          focus="split"
#   B06  GemmaScoreboard          focus="confound"
#   B07  ClaudeVerdictArtifact    (UI — the verdict)
#   B08  GemmaConvergenceThread
#   B09  ClaudeComposerAsk        (UI — "Your turn.")
#   B10  ClaudeTitleOutro         (UI — title restate)
#
# If a math beat is ever added to this reel, add its Scene class here and set
# the beat's shot.source to "manim".
