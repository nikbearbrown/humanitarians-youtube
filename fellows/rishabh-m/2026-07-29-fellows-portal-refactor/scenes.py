# scenes.py — claude-hai-fellows-portal-refactor
#
# No Manim scenes: every GRAPHIC beat renders via Remotion
# (runtime/scripts/remotion_scenes.py), and B04/B07/B10/B11 are real
# screen-capture mp4s already sitting in media/. This file exists only to
# satisfy run.sh's scenes.py guard (it refuses to run against the shared
# animated_graphics.py fixture for any reel that isn't the electoral-college
# test fixture) — it intentionally defines zero Scene classes.
from manim import *  # noqa: F401,F403
