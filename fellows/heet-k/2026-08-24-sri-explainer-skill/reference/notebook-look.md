<!-- Bundled reference for sri-explainer. Origin: user-supplied Google NotebookLM
     "Video Overview" samples (Physics video 1-4.mp4, watermarked "NotebookLM" —
     confirmed by direct frame extraction, 2026-08-16). NotebookLM's Video Overview
     is a proprietary Google feature with no public API — this file is NOT a call
     into that engine. It is a from-scratch Manim recipe that reproduces the FEEL
     (dark background, glowing accent curves, bold sans titles, red box callouts)
     using only tools already in this toolkit. Validated by a real render:
     scratchpad/notebook_look_test.py -> NotebookLookTest, checked frame-by-frame. -->

# notebook-look.md — the dark "Notebook" visual register

An alternate visual language for `sri-explainer`'s **body beats** (the
GRAPHIC/Manim beats between the Claude bookends) — a from-scratch Manim
reproduction of Google NotebookLM's Video Overview style: near-black
background, one glowing accent color, bold sans titles, red rectangle
callouts around key numbers. This is a second **look**, not a second
register — the Sridhar writing-voice rules (`prof-sridhar-style.md`) still
govern narration content unchanged. Only the paint changes.

Reference source was 4 user-supplied videos, each carrying a "NotebookLM"
watermark (confirmed by pulling raw frames, not assumed from the filenames).
That is a closed Google product with no API — nothing here calls it or
depends on it existing. Everything below is built from Manim primitives
already available in this toolkit.

## When to use this look vs. the default cream Sridhar look

- **Default (unchanged):** the cream/parchment palette in
  `prof-sridhar-style.md` / the existing reel `scenes.py` files
  (`BG=#F2F0E9`, `INK=#3D3929`, `ACC=#D97757`, `SOFT=#6E6A57`,
  `GHOST=#A8A491`). Use this unless the notebook look is asked for.
- **Notebook look:** use when the human asks for this look by name, points
  at the NotebookLM-style reference videos, or asks for a "dark," "glowing,"
  or "chalkboard-style" chapter video.
- The Claude bookend chrome (`ClaudeComposerAsk`, `ClaudeVerdictArtifact`,
  `ClaudeComposerAsk` handoff, `ClaudeTitleOutro` — all Remotion components)
  is **unchanged by either look**. Swapping their palette is out of scope —
  they carry the toolkit's own brand identity, not the chapter's. Only the
  Manim GRAPHIC beats in between change paint.

## Palette

```python
BG_DARK   = ManimColor("#14151A")  # near-black charcoal background
INK_LIGHT = ManimColor("#F5F5F0")  # titles, primary on-dark text
GLOW      = ManimColor("#4DE8E0")  # the one glowing accent — curves, highlights
CALLOUT   = ManimColor("#D9524F")  # red — boxed numbers/results only
MUTE      = ManimColor("#6B6E76")  # axes, secondary/background lines
```

One glow color per scene, same one-accent discipline as the cream look's
one-terracotta rule — cyan is the validated default; swap it per-chapter if
a chapter already has its own accent (never rainbow multiple glows).

## Recipes (validated by real render)

**Dark background** — same `BaseScene` pattern as the cream look, just a
different constant:

```python
class BaseSceneNotebook(Scene):
    def setup(self):
        self.camera.background_color = BG_DARK
```

**Bold sans titles** — the cream look leaves `font=` unset (falls back to
the system serif); the notebook look sets it explicitly, or the titles
render serif and break the look:

```python
title = Text("...", font="Arial", font_size=34, color=INK_LIGHT, weight=BOLD)
```

**Glow curve** — layer widening, fading copies of the same stroke behind a
crisp top copy. This is the one technique that makes the look read as
"NotebookLM-ish" rather than "flat Manim plot" — don't skip it:

```python
def glow_curve(mobject, color=GLOW, layers=4, base_width=4):
    group = VGroup()
    for i in range(layers, 0, -1):
        c = mobject.copy().set_stroke(color=color, width=base_width + i * 5, opacity=0.06)
        group.add(c)
    group.add(mobject.copy().set_stroke(color=color, width=base_width, opacity=1))
    return group
```

Apply to any `ax.plot(...)` result before `Create`/`FadeIn`. Axes themselves
stay `MUTE`, not glowing — glow is reserved for the one data curve per beat
(the moving-spotlight discipline from `EQUATIONS.md`, applied to a curve
instead of a symbol).

**Red callout box** — a plain rectangle, not a hand-jittered one. (A
literal chalk-sketch wobble was tried conceptually and rejected: done badly
it reads as a rendering glitch, not a style choice — clean-edged reads as
intentional. This is a deliberate divergence from the literal reference,
not an oversight.)

```python
box = Rectangle(width=2.6, height=1.0, color=CALLOUT, stroke_width=3)
value = Text("1.85 eV", font="Arial", font_size=32, color=CALLOUT, weight=BOLD)
value.move_to(box.get_center())
callout = VGroup(box, value)
```

**Margin caution (found during validation):** the test render placed a
callout box using `.next_to(ax, RIGHT, buff=0.6)`, which ran the box off
the right edge of frame at default axis widths — `next_to` a wide `Axes`
object doesn't know about the frame boundary. Always position callouts by
an explicit `.to_edge(...)` or a checked coordinate, then verify with a
frame-sample QC pass (`../../../../runtime` convention — same VISUAL QC LAW
as everywhere else in this toolkit), never trust `next_to` alone near a
frame edge.

## Production techniques (the craft level, not just the palette)

Recoloring alone reads as a palette swap, not the reference's actual craft —
camera movement, real 3D hero objects, and chart dressing are what the
NotebookLM-style videos are actually doing. Validated by real renders in
both `claude-sri-*` reels (2026-08-23):

**Gradient background (every scene, not just hero beats).** A perfectly
flat single-color background reads as cheap next to the reference's subtly
textured one. Add a large gradient `Rectangle` behind everything in
`BaseScene.setup()`:

```python
class BaseScene(Scene):
    def setup(self):
        self.camera.background_color = BG
        bg = Rectangle(width=16, height=10, stroke_width=0, fill_opacity=1)
        bg.set_color_by_gradient(BG2, BG)
        bg.set_z_index(-100)
        self.add(bg)
```

`BG2` a touch lighter than `BG` (e.g. `#1F222C` over `#101114`) is enough —
it should read as "not flat," not as an obvious effect.

**3D hero objects with camera orbit — for the chapter's own hook beat.**
Where the chapter's opening image is a physical object (a heated block, a
crystal, a lattice), build it as real 3D geometry in a `ThreeDScene`
subclass, not a flat 2D shape standing in for one. This is the single
biggest craft-level lift and the one most worth spending the beat on:

```python
class BaseScene3D(ThreeDScene):
    """3D hero-object scenes (camera orbit). Solid background ONLY — see
    the gotcha below."""
    def setup(self):
        self.camera.background_color = BG
```

```python
self.set_camera_orientation(phi=65 * DEGREES, theta=-50 * DEGREES, zoom=1.0)
hero = Cube(side_length=2.0, fill_color=..., fill_opacity=1, stroke_color=INK)
hero.set_shade_in_3d(True)
self.play(FadeIn(hero, scale=0.7))
self.begin_ambient_camera_rotation(rate=0.2)
...  # the rest of the beat's animation
self.stop_ambient_camera_rotation()
```

`Cube`, `Sphere`, and `Dot3D` all take real lighting/shading in Manim CE
(`set_shade_in_3d(True)`) — this is genuine 3D geometry with a moving
camera, not a photoreal render, but it is unmistakably a step up from a flat
`Square`/`Dot` standing in for a physical object. Use `Dot3D` for anything
that reads as "atoms/particles in an arrangement" (a crystal lattice is
literally a grid of `Dot3D` — this reads far better than 2D hexagons ever
did) and `Cube`/`Sphere` for a single physical hero object.

**GOTCHA (found during validation): never combine a fixed-in-frame
full-bleed background rectangle with `begin_ambient_camera_rotation`.**
`add_fixed_in_frame_mobjects` on a background that spans the whole frame
occludes the 3D object entirely once the camera starts orbiting — the cube
vanished mid-rotation in the first test render. `BaseScene3D` uses a solid
`camera.background_color` only, never a background mobject. Small
fixed-in-frame overlays that don't cover the hero object (a title, a corner
callout box) ARE safe and were confirmed not to occlude anything.

**GOTCHA (found while converting the Ch1/Ch2 hero beats): a Transform
target must never also be separately `add_fixed_in_frame_mobjects`-ed.**
Adding the target of a `Transform(temp_label, stage)` as its own
fixed-in-frame mobject puts BOTH the transforming original and the
independent target on screen at once — the same double-exposed-text failure
mode as the NO-COLLISION LAW (SKILL.md rule 7), just reached by a new path
specific to `ThreeDScene`'s fixed-in-frame API. Only the mobject actually
being animated (`temp_label`) goes through `add_fixed_in_frame_mobjects`,
once, before the loop that transforms it repeatedly.

**Gridlines on every chart.** A bare `Axes` reads flatter than the
reference's chart panels. Add faint background gridlines at the tick
positions:

```python
def grid_lines(ax, x_ticks, y_ticks, color=None, opacity=0.2):
    color = color if color is not None else GHOST
    lines = VGroup()
    for x in x_ticks:
        lines.add(Line(ax.c2p(x, ax.y_range[0]), ax.c2p(x, ax.y_range[1]),
                        color=color, stroke_width=1, stroke_opacity=opacity))
    for y in y_ticks:
        lines.add(Line(ax.c2p(ax.x_range[0], y), ax.c2p(ax.x_range[1], y),
                        color=color, stroke_width=1, stroke_opacity=opacity))
    return lines
```

Play it with `FadeIn` alongside `Create(ax)` — it should read as structure,
not as a second data series.

**Direct end-labeling over a legend box, when there are ≤3 series.** The
reference videos use legend boxes, but a chart where each line/curve is
labeled at its own endpoint (already the convention in these two reels'
multi-line charts) needs zero lookup and is the stronger technique when the
series count is small. Reach for an actual legend box only past ~4 series,
where end-labels would collide.

## MovingCameraScene is the base class, but 2D beats stay locked-off

A first pass at this look (2026-08-16) only changed the palette — same
locked-off static camera, same one scene = one composition structure as the
cream look. That reads as a reskin, not the reference's actual craft, and
was called out as such. A second pass (2026-08-23) overcorrected the other
way: `self.camera.frame.animate.scale(...).move_to(...)` zoom/pan choreography
was added to every single 2D beat. That was **also** called out and reverted
(2026-09-02) — it read as gimmicky rather than purposeful, and on review
several of the zooms added no clarity (zooming into a data point that was
already legible, panning between two columns that were already both on
screen). `BaseScene` still extends `MovingCameraScene`, not `Scene`, but only
for API convenience (so a scene CAN add a camera move if one is actually
earned) — it is not an instruction to add one by default:

```python
class BaseScene(MovingCameraScene):
    def setup(self):
        super().setup()
        self.camera.background_color = BG
        bg = Rectangle(width=16, height=10, stroke_width=0, fill_opacity=1)
        bg.set_color_by_gradient(BG2, BG)
        bg.set_z_index(-100)
        self.add(bg)
```

**Current rule: 2D beats keep a static, locked-off camera.** Do not add
`self.camera.frame.animate` calls to a `BaseScene` beat unless the human asks
for one, or a beat is otherwise genuinely illegible at its establishing
zoom (e.g. a value spans many orders of magnitude and needs a true zoom to
be seen at all — in that specific case, prefer fixing the layout/scale of
the mobjects themselves first). Camera motion as a matter of course is
reserved for `BaseScene3D`'s ambient orbit (below), which exists to sell
real depth on 3D geometry, not to add movement for its own sake.

## How much of a chapter's video should be full 3D

Five of the sixteen GRAPHIC beats across the two rebuilt reels are full
`BaseScene3D` scenes with camera orbit (not just the chapter's cold-open
hook): a heated 3D block, a crystal lattice both forming and diffracting a
beam, a photon-electron scattering event, an electron traveling through a
biprism. The other eleven are 2D `BaseScene` with a camera move (above).
That is roughly the right ratio — reach for `BaseScene3D` whenever the
beat's own content is a physical object or event in space (a lattice, a
collision, a block, a particle's path), not for a beat that's fundamentally
a chart, a worked calculation, or a text comparison. Converting a
chart-shaped beat to 3D just to have more 3D does not read as better craft;
it reads as decoration. Camera movement (above) is what every beat gets;
3D geometry is for beats whose content is actually spatial.

## GOTCHA: a scene can silently drop a caption if it's built but never played

Found while auditing `B08_TonomuraBuildup` (Ch2) during this pass: a
`fringe_note` Text mobject was constructed, positioned with `next_to(...)`,
and then the scene moved on to `self.wait(...)` — the `self.play(FadeIn(...))`
or `Write(...)` call was simply missing, so the caption was built,
positioned, and never once rendered. This is easy to miss because the scene
still renders and plays without error; nothing crashes, the beat is just
quietly one caption short. When auditing or revising an existing scene,
grep the scene body for every mobject assigned a variable and confirm each
one appears inside a `self.play(...)` or `self.add(...)` call somewhere
below its definition — a constructed-but-never-played mobject is a silent
content loss, not a rendering error.

## GOTCHA: Unicode superscript/subscript characters render as blank boxes

Found while auditing the Ch2 reel (2026-09-02): labels built with raw
Unicode superscript/subscript characters inside `Text(..., font="Arial")` —
e.g. `Text("2.8×10⁻¹⁵ m")`, `Text("log₁₀(...)")`, `Text("C₆₀ buckyball")` —
rendered with the superscript/subscript glyphs replaced by empty tofu boxes
on this toolkit's Windows render setup. Regular digits/letters in the same
string render fine; only the superscript/subscript code points
(`⁰¹²³⁴⁵⁶⁷⁸⁹⁻` / `₀₁₂₃₄₅₆₇₈₉`) are missing from the font's glyph coverage.
**Fix: never put superscript/subscript Unicode characters in a `Text()`
mobject. Use `MathTex` instead**, which typesets real LaTeX super/subscripts
and has no glyph-coverage issue:

```python
# WRONG — renders "2.8×10" + [box] + "15 m"
Text("classical electron radius: 2.8×10⁻¹⁵ m", font="Arial", ...)

# RIGHT
MathTex(r"\text{classical electron radius: } 2.8\times10^{-15}\ \text{m}", ...)
```

This applies to exponents (`10⁻¹⁵`), log bases (`log₁₀`), and chemical/atomic
subscripts (`C₆₀`) alike — any of these belongs in `MathTex` with `^{}`/`_{}`,
never as a literal Unicode super/subscript character in `Text`.

## GOTCHA: near-white text on a white card is invisible, not just low-contrast

Found in the same audit: `B07_ThreeImpossibleFacts` (Ch1) drew panel
headings with `color=INK` (`#F5F5F0`, near-white — correct for text on the
dark background) on top of a `RoundedRectangle` card with
`fill_color="#FFFFFF"` (pure white). White-on-near-white is essentially
invisible on screen, not merely hard to read. Any mobject placed on a light
card/box needs a dark color (`BG`, not `INK`); `INK` is only for text on the
dark gradient background. Whenever a scene introduces a light-colored card
or box, check every text color placed on it against that card's fill, not
against the scene's usual dark background.

## What this look deliberately does NOT reproduce

- **Photoreal PBR rendering** (the reference's rendered metal spheres with
  real reflections, chalk-dust concrete texture) — that needs a 3D
  asset/render pipeline this toolkit doesn't have (no image/3D-texture
  generation model in the brutalist free-only tier). `BaseScene3D` DOES
  build real 3D geometry with camera movement and basic shading (see
  "Production techniques" above) — that part is genuinely reproduced, not
  faked. What's skipped is surface realism (reflections, material texture,
  ambient occlusion) on top of that geometry.
- **Hand-drawn chalk texture/dust particles** — same reason; a plain dark
  background reads cleaner than a fake grain overlay.
- **The literal NotebookLM engine** — nothing here calls Google's product.
  If a pixel-identical NotebookLM render is ever actually wanted, that is a
  manual step (upload the chapter to notebooklm.google.com, generate the
  Video Overview there) — outside this toolkit and outside what this skill
  can trigger or fetch.
