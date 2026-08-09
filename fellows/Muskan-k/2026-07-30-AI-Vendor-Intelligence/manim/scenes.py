"""scenes.py — reel-local Manim scenes for vendor-intel-how-it-works.

Empty for the first previz. B00/B06/B07/B08 render from registered Claude
Remotion comps; the body illustration beats (B01-B05) fall to labeled SLATES
until each is filled.

To fill a body beat with Manim, add one Scene subclass per beat, named with
the beat id as the prefix followed by an underscore and a name, e.g. a class
for B01 called B01_Overview. The runner discovers scenes by that class-name
pattern, so keep no such pattern in comments (the discovery is a text scan).

Alternatives to Manim for a body beat: register a reel-local Remotion comp
that wraps SourceFlow / ChipGrid / LayerStack with this reel's data, or drop a
still / mp4 into pantry/ named by beat id.
"""
