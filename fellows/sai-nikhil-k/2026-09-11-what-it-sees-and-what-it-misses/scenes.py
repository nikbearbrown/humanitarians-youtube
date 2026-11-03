"""
Manim scenes for claude-sai-what-it-sees-and-what-it-misses.

INTENTIONALLY EMPTY — this is an all-Remotion ai-explainer reel. Every graphic
beat is a registered Remotion composition rendered by remotion_scenes.py, and
the two evidence beats are stills composed by make_plates.py. There are no
Manim beats to declare.

This file exists only to satisfy the guard in run.sh, which refuses any reel
folder without a scenes.py. Do NOT add a scene class here, and do not describe
one in prose either: the GATE F scanner matches raw text, not parsed code, so a
class declaration written inside a comment or a docstring is enough to make the
build think a Manim beat is pending and start asking for a shotlist.
"""
