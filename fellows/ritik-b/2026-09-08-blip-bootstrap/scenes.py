"""scenes.py — intentionally empty.

This reel has no Manim beats. Every visual is a Remotion composition (see
remotion/scenes/ and patches/brutalist-toolkit.patch), so there are no Scene
classes for the Manim pipeline to discover. The file exists because the
toolkit's reel contract expects it; deleting it makes `art` report a missing
scene module rather than "no Manim beats", which is the wrong signal.
"""
