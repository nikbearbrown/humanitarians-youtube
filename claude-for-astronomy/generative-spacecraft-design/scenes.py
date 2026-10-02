"""scenes.py - Manim scenes for generative-spacecraft-design.

*Nothing Left To Remove.* - ai-explainer, claude-hai, Ep. 11.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL
  Terracotta marks WHAT THE OPTIMISER DID: the load it was given, the
  material it kept, the load path it built, and the penalty when that path is
  cut. Ink marks WHAT A PERSON WOULD HAVE DONE: the solid plate, the uniform
  material, the dumb baseline that turns out to be the tolerant one.

  The load-bearing moment is B08, where the ink plate barely moves and the
  terracotta bracket leaves the scale. The accent that has meant "the
  optimiser's work" for eight beats is now the thing that failed, and the
  mapping never flips, so B04 teaches it once and every later plate reads
  for free.

THIS FILE IS ASPECT-AWARE - IT RENDERS BOTH CUTS
  The reel ships in 16:9 (3840x2160) and 9:16 (2160x3840). Manim keeps
  frame_height = 8.0 in both, so the VERTICAL band plan is identical either
  way; only the horizontal extent changes - x +-6.15 landscape, x +-1.80
  portrait. Portrait is NOT a crop: it has LESS usable area, so it carries
  fewer elements, larger. The rule for choosing what goes: anything the
  narration SPEAKS stays on screen.

  The two-panel comparisons therefore ship in BOTH arrangements - shapes.png
  and damage.png side by side for landscape, shapes_v.png and damage_v.png
  stacked for portrait. A 4:1 image squeezed into portrait's 3.44 units is
  0.84 units tall and the truss is unreadable.

LAYOUT BAND PLAN (every scene obeys it - this is what keeps the gates green)
                        landscape      portrait
  title                   +3.02          +3.14
  hairline                +2.66          +2.84
  the figure       +2.40 .. -1.90   +2.62 .. -2.02
  the closing line        -2.50          -2.42   (terracotta rule 0.28 below)
  the citation            -3.20          -2.95
  the wordmark bug        -3.12          -3.28   (right-anchored, LOGO LAW)

PLATES
  Every plate comes from assets/gen_struct.py, which runs a real plane-stress
  finite-element model and a SIMP topology optimiser (assets/topo.py), then
  the published fail-safe damage test: an 8x8 void swept over the domain,
  worst case taken (Jansen et al. 2014).

  THREE claims are ASSERTED and the generator writes nothing if any fails.
  It already refused once, for a threshold I had picked before measuring:
  claim 3 asserted the 60%-mass bracket's damage sensitivity would fall
  below 1.5x. It reads 1.63x. The claim was rewritten to the measured effect
  - the penalty collapses by a factor of 19 - rather than the tolerance
  loosened.

  There is NO random number in this pipeline. SIMP from a uniform start is
  deterministic given the problem, so there is no seed to log; SOURCES.md
  records the mesh and the parameters instead.

  PUBLISHED vs COMPUTED-HERE is kept visibly apart. B03 is a published
  ledger (ESA's own caption, 1.4 -> 0.94 kg) and says so on screen; B04-B08
  and B10 are computed here and say so.

PLATE GEOMETRY - ph = pw * (ih/iw). Do this arithmetic, do not assume it.
  domain   1560x720  0.462     evolve   1464x744  0.508
  shapes   1554x380  0.245     paths    1560x780  0.500
  damage   1554x380  0.245     price    1560x780  0.500
  shapes_v  980x1010 1.031     damage_v  980x1010 1.031
  The landscape figure band is 4.30 units tall, so a 0.50-ratio plate at
  pw = 8.0 is 4.00 tall and leaves nothing for labels - paths and price run
  at pw 6.6 and domain at 7.2. The 0.245 pair can go wide. The stacked
  variants are ~1.03, so in portrait at pw 3.40 they are 3.50 tall and need
  the whole figure band, which is why those beats carry nothing else there.

GATE NOTES (learned the expensive way on Eps. 03-10)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - NEVER use a glyph outside the font's coverage. EB Garamond has no "check"
    character and Ep. 09 rendered it as stray digits on screen. Draw marks
    from Lines.
  - A label under a grid of Squares lands ON a stroke - GATE B calls that a
    label on a curve. Put it above (Ep. 09 B07).
  - Anything placed with next_to() has a y that DEPENDS on its neighbour's
    rendered height. Measure it, do not estimate it (Ep. 08 B03, twice).
  - Keep a chip clear of an axis-label row by more than 0.04 units. Ep. 10's
    B04 passed GATE B with eleven pixels of gap at 4K and read as if the
    label were sitting on the chip.
  - Check BOTH aspects. Portrait failed GATE B 8/10 on Ep. 08's first pass.
  - Pace the scene to the narration (see Paced). hold_to_beat subtracts
    TAIL_TRIM because renderer.time UNDER-reports the rendered length, and a
    scene that OVERSHOOTS gets centre-cut, losing its closing line.
  - Render ONE Manim process at a time per reel folder (Ep. 07).
"""
from manim import *
import numpy as np
import glob
import os
from pathlib import Path

# ── EB Garamond, registered from the toolkit's bundled fonts ─────────────────
SERIF = None
try:
    import manimpango
    _homes = [os.environ.get("ART_HOME") or "",
              r"E:/NEU/Jobs/Humanitarians_AI/brutalist.art"]
    for _h in _homes:
        if not _h:
            continue
        for _f in glob.glob(os.path.join(_h, "runtime", "fonts", "EB_Garamond",
                                         "static", "*.ttf")):
            manimpango.register_font(_f)
    if "EB Garamond" in manimpango.list_fonts():
        SERIF = "EB Garamond"
except Exception:
    SERIF = None

HERE = Path(__file__).resolve().parent
PLOTS = HERE / "assets" / "plots"

# ── Palette ──────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
SOFT  = ManimColor("#6E6A57")
GHOST = ManimColor("#B9B4A0")
ACC   = ManimColor("#D97757")
ACCT  = ManimColor("#A44A32")
CARD  = ManimColor("#FFFFFF")
RULE  = ManimColor("#D9D4C4")

# ── The aspect switch ────────────────────────────────────────────────────────
# Manim CE takes pixel dimensions from `-r W,H` but does NOT recompute
# frame_width, so a portrait render would otherwise keep the 16:9 default of
# 14.22 units and lay every scene out at a third of its intended size. Keep
# frame_height at 8.0 and derive frame_width from the real pixel aspect. This
# is the same fix runtime/manim/animated_graphics.py applies; it is repeated
# here because these scenes deliberately do not import that module.
try:
    _pw, _ph = config.pixel_width, config.pixel_height
    if _pw and _ph and abs(config.frame_width
                           - config.frame_height * _pw / _ph) > 0.01:
        config.frame_width = config.frame_height * (_pw / _ph)
except Exception:
    pass

PORTRAIT = float(config.frame_width) < float(config.frame_height)


def P(landscape, portrait):
    """Pick a value per aspect. Reads as a table at the call site."""
    return portrait if PORTRAIT else landscape


def _kclip(rng, n, lim=1.55):
    """Samples from a TRUNCATED normal.

    A raw rng.normal() fan is unbounded, so one draw in a couple of dozen
    lands two or three sigma out and leaves the figure band entirely. B09's
    first version put a line at y = 3.6 - above the hairline and through the
    title - and GATE A caught it. Clipping is the correct fix: the fan is a
    picture of an uncertainty region, and the region genuinely is finite.
    """
    return np.clip(rng.normal(0, 1.0, n), -lim, lim)


X_MAX = P(6.15, 1.80)
Y_MAX = 3.30
TITLE_Y, HAIR_Y = P(3.02, 3.14), P(2.66, 2.84)
FIG_TOP, FIG_BOT = P(2.40, 2.62), P(-1.90, -2.02)
CLOSE_Y = P(-2.50, -2.42)
CITE_Y, BUG_Y = P(-3.20, -2.95), P(-3.12, -3.28)
TITLE_W = P(11.4, 3.42)
CLOSE_W = P(8.8, 3.44)
CITE_W = P(8.4, 3.44)
FIG_MID = (FIG_TOP + FIG_BOT) / 2


# ── Type helpers ─────────────────────────────────────────────────────────────
def _t(txt, size=26, color=None, weight=None):
    kw = {"font_size": size, "color": color if color is not None else INK}
    if SERIF:
        kw["font"] = SERIF
    if weight:
        kw["weight"] = weight
    return Text(txt, **kw)


def _fit(m, max_w, at=None):
    if m.width > max_w:
        m.scale(max_w / m.width)
    if at is not None:
        m.move_to(at)
    return m


def _chip(txt, size=20, fill=ACC, fg=CARD, max_w=None):
    label = _t(txt, size=size, color=fg)
    if max_w and label.width > max_w - 0.46:
        label.scale((max_w - 0.46) / label.width)
    box = RoundedRectangle(width=label.width + 0.46, height=label.height + 0.30,
                           corner_radius=0.12, color=fill, fill_color=fill,
                           fill_opacity=1.0, stroke_width=0)
    label.move_to(box.get_center())
    return VGroup(box, label)


def _quiet_chip(txt, size=20, max_w=None):
    label = _t(txt, size=size, color=INK)
    if max_w and label.width > max_w - 0.46:
        label.scale((max_w - 0.46) / label.width)
    box = RoundedRectangle(width=label.width + 0.46, height=label.height + 0.28,
                           corner_radius=0.12, color=GHOST, fill_color=CARD,
                           fill_opacity=1.0, stroke_width=1.6)
    label.move_to(box.get_center())
    return VGroup(box, label)


def _card(w, h, at, radius=0.16, stroke=GHOST, sw=1.8):
    return RoundedRectangle(width=w, height=h, corner_radius=radius,
                            color=stroke, stroke_width=sw,
                            fill_color=CARD, fill_opacity=1.0).move_to(at)


def _underline(m, color=ACC, sw=4, buff=0.14, pad=0.10):
    ln = Line(LEFT, RIGHT, color=color, stroke_width=sw)
    ln.set_width(max(float(m.width) + pad * 2, 0.4))
    ln.next_to(m, DOWN, buff=buff)
    return ln


def _strike(m, color=ACC, sw=4, pad=0.16):
    """Struck-through rule. `_qc_intentional` exempts it from GATE B's
    TEXT-ON-CURVE rule, which is what that hook exists for."""
    ln = Line(LEFT, RIGHT, color=color, stroke_width=sw)
    ln.set_width(max(float(m.width) + pad * 2, 0.4))
    ln.move_to(m.get_center())
    ln._qc_intentional = True
    return ln


def chrome(scene, title, cite=None):
    head = _fit(_t(title, size=P(36, 30), weight="BOLD"), TITLE_W, [0, TITLE_Y, 0])
    hair = Line([-(X_MAX - 0.10), HAIR_Y, 0], [X_MAX - 0.10, HAIR_Y, 0],
                color=RULE, stroke_width=2.4)
    bug = _t("@HumanitariansAI", size=P(19, 17), color=SOFT)
    bug.move_to([0, BUG_Y, 0]).align_to([X_MAX, 0, 0], RIGHT)
    scene.play(FadeIn(head, shift=DOWN * 0.12), Create(hair), FadeIn(bug),
               run_time=0.8)
    group = VGroup(head, hair, bug)
    if cite:
        c = _fit(_t(cite, size=P(17, 14), color=SOFT), CITE_W)
        if PORTRAIT:
            c.move_to([0, CITE_Y, 0])
        else:
            c.move_to([0, CITE_Y, 0]).align_to([-X_MAX, 0, 0], LEFT)
        scene.play(FadeIn(c), run_time=0.4)
        group.add(c)
    return group


def closer(scene, text, cx=None, size=None):
    cx = P(-0.6, 0.0) if cx is None else cx
    line = _fit(_t(text, size=size or P(31, 26), color=ACCT, weight="BOLD"),
                CLOSE_W, [cx, CLOSE_Y, 0])
    under = _underline(line, buff=0.16)
    scene.play(FadeIn(line, shift=UP * 0.10), run_time=0.75)
    scene.play(Create(under), run_time=0.4)
    return VGroup(line, under)


# ── Plate helpers ────────────────────────────────────────────────────────────
def _plate(name, w, at, frame=True, opacity=1.0):
    """A synthetic terrain plate, framed like a figure in a paper.

    Returns a `Group`: ImageMobject is not a VMobject. Falls back to a blank
    plate if the asset is missing so a scene can never fail to render.
    """
    path = PLOTS / name
    parts = []
    hh = w * (860.0 / 1280.0)
    try:
        img = ImageMobject(str(path))
        img.width = w
        img.move_to(at)
        if opacity < 1.0:
            img.set_opacity(opacity)
        hh = float(img.height)
        parts.append(img)
    except Exception:
        parts.append(Rectangle(width=w, height=hh, color=CARD, fill_color=CARD,
                               fill_opacity=1, stroke_width=0).move_to(at))
    if frame:
        parts.append(Rectangle(width=w, height=hh, color=GHOST, stroke_width=1.6,
                               fill_opacity=0).move_to(at))
    return Group(*parts)


def _plate_h(name, w):
    """The height a plate of width w will occupy, without building it."""
    try:
        from PIL import Image as _I
        iw, ih = _I.open(PLOTS / name).size
        return w * ih / iw
    except Exception:
        return w * 860.0 / 1280.0


def _cap(txt, target, size=None, buff=0.16):
    """A caption under a plate. Every plate that could be mistaken for a NASA
    image gets one — that is a SOURCES.md promise, not a nicety."""
    c = _t(txt, size=size or P(16, 14), color=SOFT)
    c.next_to(target, DOWN, buff=buff)
    return c


def _bar(value, full_w, h, at, fill=ACC, track=True):
    """A horizontal proportion bar, left-anchored at `at`."""
    g = VGroup()
    if track:
        t = Rectangle(width=full_w, height=h, color=GHOST, stroke_width=1.4,
                      fill_color=CARD, fill_opacity=1.0)
        t.move_to([at[0] + full_w / 2, at[1], 0])
        g.add(t)
    w = max(full_w * float(value), 0.02)
    b = Rectangle(width=w, height=h, color=fill, fill_color=fill,
                  fill_opacity=1.0, stroke_width=0)
    b.move_to([at[0] + w / 2, at[1], 0])
    g.add(b)
    return g


def _arrow(a, b, color=None, sw=4.2, tip=0.20):
    return Arrow(start=a, end=b, color=color or GHOST, stroke_width=sw,
                 max_tip_length_to_length_ratio=tip, buff=0.06)


# ── Pacing: the scene fits the narration, not the other way round ────────────
# compile.py fills a beat by SLOWING the clip to length. These scenes originally
# ran 8-12 s against 22-34 s beats, so the compiler stretched them up to 3.3x —
# visible slow-motion, and it flagged three beats for replacement. The fix is not
# to shorten the narration (the human signed it) but to pace the picture to it:
# every reveal takes longer (RT) and rests afterwards (HOLD), and the tail pads
# to the measured duration. The compiler's fit factor then lands at ~1.0.
#
# RT/HOLD are per scene because the beats are not the same length. They are set
# to UNDERSHOOT slightly; hold_to_beat() absorbs the remainder, which is also why
# the same numbers work in portrait, where some scenes carry fewer elements.
def _beat_seconds():
    try:
        import json
        d = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
        return {b["beat_id"]: float(b.get("actual_duration_s") or 0)
                for b in d.get("beats", [])}
    except Exception:
        return {}


BEAT_SECONDS = _beat_seconds()

# Safety margin subtracted from every beat target — see Paced.hold_to_beat.
TAIL_TRIM = 0.18


class Paced(Scene):
    """A Scene that paces itself to its beat's measured narration."""

    BEAT = None
    RT = 1.0        # run_time multiplier
    HOLD = 0.0      # rest after each reveal
    _raw = False

    def play(self, *args, **kwargs):
        if self._raw:                      # re-entry from Scene.wait()
            return Scene.play(self, *args, **kwargs)
        kwargs["run_time"] = float(kwargs.get("run_time", 1.0)) * self.RT
        Scene.play(self, *args, **kwargs)
        if self.HOLD:
            self.wait(self.HOLD)

    def wait(self, duration=1.0, **kwargs):
        prev = self._raw
        self._raw = True
        try:
            Scene.wait(self, duration, **kwargs)
        finally:
            self._raw = prev

    def hold_to_beat(self, floor=0.35):
        """Hold the finished composition until the narration is done.

        Every scene must land UNDER its beat. compile.py pads a short clip by
        holding its last frame, which is invisible; a clip LONGER than its beat
        is centre-cut, which would clip the closing line off both ends.

        renderer.time UNDER-reports the true rendered length, because each
        play's frame count rounds up and the error accumulates with the number
        of reveals. B10 has 20 of them and overshot by +0.12 s. That cannot be
        fixed by lowering RT or HOLD -- a smaller body raises `target - now` by
        exactly the same amount and the total does not move -- so the target
        itself carries a safety trim.

        A scene that does NOT respond to the trim is already sitting on
        `floor`, and then the only lever left is RT. Ep. 11's B01 and B07 are
        both that case: a per-scene trim was tried first and changed nothing,
        because `target - trim - now` was already below 0.35 s. B01 runs 13
        reveals at the reel's smallest RT, where each play's round-up is the
        largest share of its run_time, so its body had simply grown past its
        beat. Lowering RT is what fixed it.
        """
        target = BEAT_SECONDS.get(self.BEAT or "", 0.0)
        now = float(getattr(getattr(self, "renderer", None), "time", 0.0) or 0.0)
        self.wait(max(floor, target - TAIL_TRIM - now) if target else floor)




# ─────────────────────────────────────────────────────────────────────────────
#  Plate geometry note. A plate placed by WIDTH gets its height for free:
#      ph = pw * (ih / iw)
#  The eight plates from gen_struct.py, in pixels and as ratios:
#      domain   1560x720  (0.462)   evolve    1464x744  (0.508)
#      shapes   1554x380  (0.245)   paths     1560x780  (0.500)
#      damage   1554x380  (0.245)   price     1560x780  (0.500)
#      shapes_v  980x1010 (1.031)   damage_v   980x1010 (1.031)
#  The landscape figure band is 4.30 units tall, so a 0.50-ratio plate at
#  pw = 8.0 is 4.00 tall and leaves almost nothing for labels. Do this
#  arithmetic; Ep. 08's B04 defect was this multiplication left undone, and
#  the plate covered its own title.
# ─────────────────────────────────────────────────────────────────────────────


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    # RT lowered from the solved 0.837: 13 reveals at this multiplier
    # rounded up to a body 0.25 s past the beat, and the tail was already on
    # the floor, so the trim could not absorb it. See Paced.hold_to_beat.
    BEAT, RT, HOLD = "B01", 0.803, 0.000

    def construct(self):
        self.camera.background_color = BG
        hair = Line([-(X_MAX - 0.10), HAIR_Y, 0], [X_MAX - 0.10, HAIR_Y, 0],
                    color=RULE, stroke_width=2.4)
        top = _fit(_t("AI in Astronomy & Space Science  ·  Ep. 11",
                      size=P(22, 17), color=SOFT), TITLE_W, [0, TITLE_Y, 0])
        cite = _fit(_t("brutalist.art  ·  ai-explainer  ·  Pragmatist register",
                       size=P(17, 14), color=SOFT), CITE_W)
        cite.move_to([0, CITE_Y, 0])
        if not PORTRAIT:
            cite.align_to([-X_MAX, 0, 0], LEFT)
        bug = _t("@HumanitariansAI", size=P(19, 17), color=SOFT)
        bug.move_to([0, BUG_Y, 0]).align_to([X_MAX, 0, 0], RIGHT)
        self.play(FadeIn(top, shift=DOWN * 0.10), Create(hair), run_time=0.7)
        self.play(FadeIn(cite), FadeIn(bug), run_time=0.45)

        name_at = P([-3.05, 1.30, 0], [0, 2.00, 0])
        name = _fit(_t("Om Mali", size=P(72, 54)), P(5.4, 3.30), name_at)
        self.play(Write(name), run_time=0.9)
        rule = _underline(name, color=ACC, sw=6, buff=0.18)
        self.play(Create(rule), run_time=0.45)
        role = _fit(_t("Humanitarians AI  ·  presenter", size=P(26, 20),
                       color=SOFT), P(5.2, 3.30))
        role.move_to([name_at[0], name_at[1] - P(0.86, 0.78), 0])
        self.play(FadeIn(role), run_time=0.5)

        # the pivot, as two rows: one struck, one boxed
        card_at = P([3.10, 1.06, 0], [0, -0.44, 0])
        card = _card(P(5.5, 3.40), P(2.50, 2.30), card_at)
        self.play(Create(card), run_time=0.6)

        r1 = _fit(_t("ten episodes", size=P(28, 23), color=SOFT),
                  P(4.9, 3.00))
        r1.move_to([card_at[0], card_at[1] + P(0.80, 0.74), 0])
        r1b = _fit(_t("AI reads the sky", size=P(23, 19), color=SOFT),
                   P(4.9, 3.00))
        r1b.move_to([card_at[0], card_at[1] + P(0.38, 0.34), 0])
        self.play(FadeIn(r1), run_time=0.45)
        self.play(FadeIn(r1b), run_time=0.4)
        st = _strike(r1b, color=ACC, sw=4)
        self.play(Create(st), run_time=0.4)

        r2 = _fit(_t("this one", size=P(28, 23), color=ACCT, weight="BOLD"),
                  P(4.9, 3.00))
        r2.move_to([card_at[0], card_at[1] - P(0.30, 0.30), 0])
        r2b = _fit(_t("AI makes the part", size=P(23, 19), color=INK),
                   P(4.9, 3.00))
        r2b.move_to([card_at[0], card_at[1] - P(0.72, 0.70), 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)
        box = SurroundingRectangle(VGroup(r2, r2b), color=ACC, buff=0.18,
                                   stroke_width=3, corner_radius=0.10)
        self.play(Create(box), run_time=0.5)

        ser = _fit(_t("Ep. 11  ·  the optimiser deletes the margin",
                      size=P(23, 18), color=ACCT), P(6.0, 3.34))
        ser.move_to([0, P(-2.34, -2.44), 0])
        self.play(FadeIn(ser), run_time=0.5)

        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — THE WHOLE IDEA IN ONE BREATH  (EXECUTIVE-SUMMARY LAW)
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.550, 0.063

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath",
               cite="the mechanism, before any number")

        card = _card(P(9.4, 3.46), P(4.10, 4.30), [0, P(0.26, 0.30), 0])
        self.play(Create(card), run_time=0.7)

        rows = [
            ("YOU GIVE IT THREE THINGS", "a volume, the loads, a mass budget",
             INK, False),
            ("IT GIVES BACK A SHAPE", "lighter and stiffer than a person draws",
             INK, False),
            ("IT GETS THERE BY DELETING", None, ACCT, True),
        ]
        y0 = P(1.56, 1.66)
        dy = P(1.18, 1.44)
        last = None
        for i, (head, sub, colr, accent) in enumerate(rows):
            y = y0 - dy * i
            # P()'s portrait figure must be <= the card width (3.46) and
            # inside the safe area (+-1.80). 4.60 was neither.
            h = _fit(_t(head, size=P(36, 25), color=colr,
                        weight="BOLD" if accent else None), P(8.6, 3.06),
                     [0, y, 0])
            self.play(FadeIn(h, shift=UP * 0.10), run_time=0.7)
            if accent:
                self.play(Create(_underline(h, color=ACC, sw=5, buff=0.14)),
                          run_time=0.45)
                last = h
            if sub:
                s = _fit(_t(sub, size=P(23, 17), color=SOFT), P(8.4, 3.00))
                s.move_to([0, y - P(0.42, 0.38), 0])
                self.play(FadeIn(s), run_time=0.45)

        closer(self, "everything not carrying your load", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE REAL PART  (PUBLISHED)
# ═════════════════════════════════════════════════════════════════════════════
class B03_RealPart(Paced):
    BEAT, RT, HOLD = "B03", 1.550, 0.042

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "It already flies",
               cite="ESA, Sentinel-1 upper S-band antenna support — published, "
                    "not measured here")

        # An ISOTYPE bracket, drawn from primitives. REBUILD LAW: never a
        # photograph and never a traced outline of the real part.
        gx, gy = P(-3.55, 0.0), P(1.08, 1.74)
        s = P(1.0, 0.72)
        body = VGroup(
            Line([gx - 1.5 * s, gy + 0.9 * s, 0], [gx + 1.5 * s, gy + 0.9 * s, 0],
                 color=INK, stroke_width=P(9, 7)),
            Line([gx - 1.5 * s, gy + 0.9 * s, 0], [gx - 1.5 * s, gy - 0.9 * s, 0],
                 color=INK, stroke_width=P(9, 7)),
            Line([gx - 1.5 * s, gy - 0.9 * s, 0], [gx + 1.5 * s, gy + 0.9 * s, 0],
                 color=INK, stroke_width=P(7, 5)),
            Line([gx - 0.2 * s, gy + 0.9 * s, 0], [gx - 1.5 * s, gy - 0.1 * s, 0],
                 color=INK, stroke_width=P(7, 5)),
        )
        lug = Square(side_length=0.34 * s, color=INK, fill_color=INK,
                     fill_opacity=1.0, stroke_width=0)
        lug.move_to([gx + 1.5 * s, gy + 0.9 * s, 0])
        self.play(LaggedStart(*[Create(m) for m in body], lag_ratio=0.22),
                  run_time=1.0)
        self.play(FadeIn(lug), run_time=0.35)

        chip = _quiet_chip("published ledger", size=P(19, 15), max_w=P(3.6, 3.0))
        chip.move_to([gx, gy - P(1.40, 1.14), 0])
        self.play(FadeIn(chip), run_time=0.45)

        # the mass bar: runs DOWN from 1.4 and stops at 0.94
        bx = P(0.70, -1.70)
        by = P(1.30, -0.44)
        full = P(4.60, 3.40)
        before = _fit(_t("1.4 kg", size=P(30, 24), color=SOFT),
                      P(2.0, 1.6), [bx + full * 0.5, by + P(0.62, 0.46), 0])
        self.play(FadeIn(before), run_time=0.45)
        track = _bar(1.0, full, P(0.42, 0.34), [bx, by, 0], fill=GHOST)
        self.play(FadeIn(track), run_time=0.45)
        kept = _bar(0.671, full, P(0.42, 0.34), [bx, by, 0], fill=INK,
                    track=False)
        self.play(GrowFromEdge(kept, LEFT), run_time=0.8)
        after = _fit(_t("0.94 kg", size=P(30, 24), color=INK, weight="BOLD"),
                     P(2.2, 1.7),
                     [bx + full * 0.671 * 0.5, by - P(0.62, 0.56), 0])
        self.play(FadeIn(after), run_time=0.45)

        # the delta, in the accent
        dx0 = bx + full * 0.671
        delta = Rectangle(width=full * 0.329, height=P(0.42, 0.34), color=ACC,
                          fill_color=ACC, fill_opacity=1.0, stroke_width=0)
        delta.move_to([dx0 + full * 0.329 * 0.5, by, 0])
        self.play(FadeIn(delta), run_time=0.5)
        lab = _fit(_t("a third lighter", size=P(26, 20), color=ACCT,
                      weight="BOLD"), P(3.0, 2.6))
        # Landscape labels the delta in place. Portrait has no room beside
        # the bar -- at x=1.79 it was touching the 1.80 safe edge and read as
        # "1.4 kg a third lighter" -- so it goes under the bar, centred.
        lab.move_to([dx0 + full * 0.329 * 0.5 if not PORTRAIT else 0.0,
                     by + 0.62 if not PORTRAIT else -1.62, 0])
        self.play(FadeIn(lab, shift=UP * 0.08), run_time=0.5)

        # LANDSCAPE ONLY — the vendor/process tag. Never spoken.
        if not PORTRAIT:
            tag = _fit(_t("selective laser melting  ·  RUAG Space Switzerland, "
                          "with Altair and EOS", size=19, color=SOFT), 9.0)
            tag.move_to([0, -1.74, 0])
            self.play(FadeIn(tag), run_time=0.4)

        closer(self, "this is not a demo", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — THE BRIEF
# ═════════════════════════════════════════════════════════════════════════════
class B04_TheBrief(Paced):
    BEAT, RT, HOLD = "B04", 1.539, 0.000
    # The ONLY scene whose portrait branch is LONGER than its landscape one:
    # landscape adds a single FadeIn for its note, portrait calls closer(),
    # which is two plays and 1.15 s of nominal run_time. The pacing solve
    # runs once, in landscape, so portrait inherited an RT fitted to the
    # shorter body and overshot its beat by +0.92 s. Seven other scenes also
    # differ across aspects, but all of them are SHORTER in portrait, and a
    # short body is absorbed by hold_to_beat's tail -- only the long one
    # needed its own multiplier. Kept on a separate line so pace11.py's
    # regex still rewrites the landscape value.
    if PORTRAIT:
        RT = 1.347

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Everything it was told",
               cite="computed in this reel: 120x60 elements, one load case")

        # domain.png is 1560x720 -> 0.462. pw 7.2 -> ph 3.33, which fits the
        # 4.30 band with a chip row beneath.
        pw = P(7.20, 3.40)
        pat = [0, P(0.74, 0.96), 0]
        plate = _plate("domain.png", pw, pat, frame=False)
        ph = _plate_h("domain.png", pw)
        self.play(FadeIn(plate), run_time=0.8)

        # ring each given in the order the voice names it
        def ring(cx, cy, rw, rh, label, lx, ly):
            r = RoundedRectangle(width=rw, height=rh, corner_radius=0.08,
                                 color=ACC, stroke_width=3, fill_opacity=0)
            r.move_to([pat[0] + cx, pat[1] + cy, 0])
            lb = _fit(_t(label, size=P(21, 16), color=INK), P(2.9, 1.5))
            lb.move_to([pat[0] + lx, pat[1] + ly, 0])
            return r, lb

        items = [
            ring(-pw * 0.383, 0.0, pw * 0.055, ph * 0.90, "bolted root",
                 -pw * 0.28, -ph * 0.60),
            ring(pw * 0.385, 0.0, pw * 0.065, ph * 0.17, "one lug",
                 pw * 0.28, ph * 0.32),
        ]
        for r, lb in items:
            self.play(Create(r), run_time=0.5)
            self.play(FadeIn(lb), run_time=0.4)

        arr = _fit(_t("one load", size=P(21, 16), color=ACCT, weight="BOLD"),
                   P(2.6, 1.5))
        arr.move_to([pat[0] + pw * 0.30, pat[1] - ph * 0.44, 0])
        self.play(FadeIn(arr, shift=LEFT * 0.08), run_time=0.5)

        chip = _chip("use 40% of the metal", size=P(23, 18), fill=ACC,
                     max_w=P(5.2, 3.30))
        chip.move_to([0, P(-1.70, -1.62), 0])
        self.play(FadeIn(chip, shift=UP * 0.08), run_time=0.55)

        # LANDSCAPE ONLY — portrait's plate owns the band.
        if not PORTRAIT:
            note = _fit(_t("no stress limit, no damage case, no second load — "
                           "nothing else is given", size=19, color=SOFT), 9.6)
            note.move_to([0, -2.24, 0])
            self.play(FadeIn(note), run_time=0.4)
        else:
            closer(self, "that is the whole brief", cx=0.0)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — WATCH IT DESIGN
# ═════════════════════════════════════════════════════════════════════════════
class B05_WatchItDesign(Paced):
    BEAT, RT, HOLD = "B05", 1.247, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Nobody drew this",
               cite="computed in this reel: SIMP iterates 1, 3, 8 and 90")

        # evolve.png is 1464x744 -> 0.508. pw 6.30 -> ph 3.20.
        pw = P(6.30, 3.40)
        pat = [P(-1.40, 0.0), P(0.60, 0.80), 0]
        plate = _plate("evolve.png", pw, pat, frame=False)
        ph = _plate_h("evolve.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        # the four iterate labels, landing in order with the panels
        if PORTRAIT:
            # one line instead of four chips: a sub-panel here is 1.6 x 0.8
            # units and a chip was 28% of its width.
            lb = _fit(_t("iterations 1, 3, 8 and 90", size=18, color=SOFT),
                      3.30)
            lb.move_to([pat[0], pat[1] - ph * 0.5 - 0.30, 0])
            self.play(FadeIn(lb), run_time=0.5)
        else:
            for i, m in enumerate(["1", "3", "8", "90"]):
                cx = pat[0] + (-0.25 + 0.5 * (i % 2)) * pw
                cy = pat[1] + (0.25 - 0.5 * (i // 2)) * ph
                lb = _chip(m, size=20, fill=ACC if i == 3 else INK,
                           max_w=1.2)
                lb.move_to([cx - pw * 0.20, cy + ph * 0.18, 0])
                self.play(FadeIn(lb), run_time=0.45)

        # LANDSCAPE ONLY — a side column explaining what is moving
        if not PORTRAIT:
            col_at = [3.75, 1.10, 0]
            for i, (big, small) in enumerate(
                    [("uniform", "every element half-full"),
                     ("flowing", "material moves to the load"),
                     ("starved", "the rest drops to nothing"),
                     ("a truss", "iteration 90")]):
                y = col_at[1] - 0.78 * i
                a = _fit(_t(big, size=25,
                            color=ACCT if i == 3 else INK,
                            weight="BOLD" if i == 3 else None), 4.2,
                         [col_at[0], y, 0])
                b = _fit(_t(small, size=18, color=SOFT), 4.4,
                         [col_at[0], y - 0.32, 0])
                self.play(FadeIn(a), FadeIn(b), run_time=0.5)

        closer(self, "it is the answer to the question I typed",
               cx=P(-0.6, 0.0), size=P(28, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — SAME MASS, BETTER SHAPE                       (the pitch, and it is true)
# ═════════════════════════════════════════════════════════════════════════════
class B06_SameMass(Paced):
    BEAT, RT, HOLD = "B06", 1.550, 0.189

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Same mass, better shape",
               cite="computed in this reel: compliance under the design load, "
                    "equal mass")

        name = "shapes_v.png" if PORTRAIT else "shapes.png"
        pw = P(10.40, 3.30)
        pat = [0, P(1.06, 0.50), 0]
        plate = _plate(name, pw, pat, frame=False)
        ph = _plate_h(name, pw)
        self.play(FadeIn(plate), run_time=0.9)

        # which is which — the labels sit ABOVE each panel in landscape and
        # beside the stack in portrait, never under a stroke.
        if PORTRAIT:
            # OUTSIDE the stack. Inside, the lower label landed on the truss.
            pairs = [("a plate, thinned to fit", pat[1] + ph * 0.50 + 0.24),
                     ("the optimiser's answer", pat[1] - ph * 0.50 - 0.26)]
            for txt, y in pairs:
                lb = _fit(_t(txt, size=17, color=SOFT), 3.30, [0, y, 0])
                self.play(FadeIn(lb), run_time=0.4)
        else:
            # BELOW the panels. Above, at y 2.59, the label box spanned
            # 2.45..2.74 and crossed the hairline at +2.66.
            for i, txt in enumerate(["a plate, thinned to fit",
                                     "the optimiser's answer"]):
                lb = _fit(_t(txt, size=21, color=SOFT), 4.6,
                          [(-0.25 + 0.5 * i) * pw,
                           pat[1] - ph * 0.5 - 0.34, 0])
                self.play(FadeIn(lb), run_time=0.4)

        # both mass chips read 40%
        chips = []
        n_chips = 1 if PORTRAIT else 2
        for i in range(n_chips):
            c = _quiet_chip("40% of the mass", size=P(20, 16),
                            max_w=P(3.6, 3.20))
            cx = 0.0 if PORTRAIT else (-0.25 + 0.5 * i) * pw
            c.move_to([cx, P(-1.10, -1.96), 0])
            chips.append(c)
        self.play(LaggedStart(*[FadeIn(c) for c in chips], lag_ratio=0.3),
                  run_time=0.55)

        # the stiffness pair, growing to value
        if not PORTRAIT:
            bw, bx = 3.00, -0.25 * pw
            # stiffness, not compliance: 81.31/100.03 = 0.813 for the plate
            # against 1.000 for the bracket. Longer is stiffer.
            for i, (v, colr) in enumerate([(0.813, SOFT), (1.00, ACC)]):
                at = [(-0.25 + 0.5 * i) * pw - bw / 2, -1.70, 0]
                self.play(FadeIn(_bar(1.0, bw, 0.30, at, fill=GHOST)),
                          run_time=0.3)
                self.play(GrowFromEdge(
                    _bar(v, bw, 0.30, at, fill=colr, track=False), LEFT),
                    run_time=0.6)

        big = _fit(_t("23% stiffer", size=P(42, 32), color=ACCT, weight="BOLD"),
                   P(5.0, 3.36))
        big.move_to([0, P(-2.45, -2.44), 0])
        self.play(FadeIn(big, shift=UP * 0.08), run_time=0.6)
        # The "the pitch is true" sub-line used to sit at -3.00, which left
        # 0.02 units between it and the citation. It is spoken, so the screen
        # does not need it.
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — ONE PATH
# ═════════════════════════════════════════════════════════════════════════════
class B07_OnePath(Paced):
    BEAT, RT, HOLD = "B07", 1.286, 0.000   # likewise on the floor

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Every member is working",
               cite="computed in this reel: elastic strain-energy density")

        # paths.png is 1560x780 -> 0.500. pw 6.60 -> ph 3.30.
        pw = P(6.60, 3.40)
        pat = [P(-1.30, 0.0), P(0.70, 0.86), 0]
        plate = _plate("paths.png", pw, pat, frame=False)
        ph = _plate_h("paths.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        tally = _fit(_t("no idle material", size=P(26, 21), color=ACCT,
                        weight="BOLD"), P(4.4, 3.30))
        tally.move_to([pat[0], pat[1] - ph * 0.5 - P(0.27, 0.40), 0])
        self.play(FadeIn(tally, shift=UP * 0.08), run_time=0.55)

        if not PORTRAIT:
            col_at = [3.90, 1.44, 0]
            for i, txt in enumerate(["the load arrives",
                                     "it splits once",
                                     "both halves reach the root",
                                     "and that is all there is"]):
                a = _fit(_t(txt, size=23,
                            color=ACCT if i == 3 else INK,
                            weight="BOLD" if i == 3 else None), 4.3,
                         [col_at[0], col_at[1] - 0.68 * i, 0])
                self.play(FadeIn(a, shift=LEFT * 0.06), run_time=0.5)

            # the ghost arrow that hunts for a second route and fails
            gq = _fit(_t("a second route?", size=21, color=SOFT), 4.0,
                      [col_at[0], col_at[1] - 0.68 * 4 - 0.18, 0])
            self.play(FadeIn(gq), run_time=0.45)
            gx = _strike(gq, color=GHOST, sw=3)
            self.play(Create(gx), run_time=0.4)

        spare = _fit(_t("spare mass", size=P(30, 24), color=SOFT),
                     P(4.4, 3.30))
        # Landscape puts it in the side column, where the ghost question
        # already lives; centred at -2.14 its strike-through ran into both
        # "no idle material" above and the closing line below.
        spare.move_to([3.90, -2.16, 0] if not PORTRAIT else [0, -1.84, 0])
        self.play(FadeIn(spare), run_time=0.5)
        st = _strike(spare, color=ACC, sw=5)
        self.play(Create(st), run_time=0.45)

        closer(self, "that was the instruction" if not PORTRAIT
               else "is what I told it to delete", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — ONE VOID                                      (the load-bearing beat)
# ═════════════════════════════════════════════════════════════════════════════
class B08_OneVoid(Paced):
    BEAT, RT, HOLD = "B08", 1.550, 0.301

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "One void, in the worst place",
               cite="computed in this reel: an 8x8 void swept over 398 "
                    "locations, worst case shown (method: Jansen et al. 2014)")

        name = "damage_v.png" if PORTRAIT else "damage.png"
        pw = P(10.40, 3.30)
        # portrait drops a little to open a gap between the hairline (+2.84)
        # and the figure, because that is where the chip now lives.
        pat = [0, P(1.10, 0.50), 0]
        plate = _plate(name, pw, pat, frame=False)
        ph = _plate_h(name, pw)
        self.play(FadeIn(plate), run_time=0.9)

        chip = _quiet_chip("0.89% of the area", size=P(20, 16),
                           max_w=P(3.8, 3.00))
        # Landscape: under the plate, centred, above the value rows.
        # Portrait: ABOVE the plate. Below, it landed on both value labels.
        chip.move_to([0, P(-0.56, 2.52), 0])
        self.play(FadeIn(chip), run_time=0.5)

        # the two penalties, as counters that land on the spoken figure
        rows = [("the plate", "1.2x", INK, P(-2.60, -0.86)),
                ("the optimised bracket", "31.2x", ACCT, P(2.60, 0.86))]
        for i, (nm, val, colr, cx) in enumerate(rows):
            y = P(-2.06, -1.98)
            lb = _fit(_t(nm, size=P(21, 15), color=SOFT), P(4.2, 1.56))
            lb.move_to([cx, y + P(0.46, 0.42), 0])
            v = _fit(_t(val, size=P(46, 32), color=colr, weight="BOLD"),
                     P(3.2, 1.56))
            v.move_to([cx, y - P(0.18, 0.16), 0])
            self.play(FadeIn(lb), run_time=0.4)
            self.play(FadeIn(v, shift=UP * 0.10), run_time=0.6)

        # LANDSCAPE ONLY — the 90th percentile, so the worst case is in context
        if not PORTRAIT:
            p90 = _fit(_t("and at the 90th percentile of all 398 locations: "
                          "3.4x against the plate's 1.08x", size=19,
                          color=SOFT), 10.0)
            p90.move_to([0, -2.78, 0])
            self.play(FadeIn(p90), run_time=0.45)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — A KNOWN PROBLEM  (PUBLISHED)
# ═════════════════════════════════════════════════════════════════════════════
class B09_KnownProblem(Paced):
    BEAT, RT, HOLD = "B09", 1.550, 0.121

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "A known problem",
               cite="fail-safe topology optimisation literature — published, "
                    "not measured here")

        card_at = P([-3.20, 1.00, 0], [0, 1.40, 0])
        card = _card(P(5.6, 3.40), P(2.60, 2.30), card_at)
        self.play(Create(card), run_time=0.65)

        head = _fit(_t("minimise mass, one load case", size=P(23, 18),
                       color=SOFT), P(5.1, 3.10))
        head.move_to([card_at[0], card_at[1] + P(0.82, 0.76), 0])
        self.play(FadeIn(head), run_time=0.45)
        q = _fit(_t("no alternative", size=P(32, 24), color=ACCT,
                    weight="BOLD"), P(5.1, 3.10))
        q.move_to([card_at[0], card_at[1] + P(0.16, 0.14), 0])
        q2 = _fit(_t("load-paths", size=P(32, 24), color=ACCT, weight="BOLD"),
                  P(5.1, 3.10))
        q2.move_to([card_at[0], card_at[1] - P(0.40, 0.38), 0])
        self.play(Write(q), run_time=0.6)
        self.play(Write(q2), run_time=0.5)
        self.play(Create(_underline(q2, color=ACC, sw=4, buff=0.12)),
                  run_time=0.4)

        req_at = P([3.30, 1.34, 0], [0, -0.96, 0])
        req = _fit(_t("and in aerospace", size=P(23, 18), color=SOFT),
                   P(5.0, 3.34), [req_at[0], req_at[1] + P(0.52, 0.46), 0])
        req2 = _fit(_t("those paths are required", size=P(28, 22), color=INK,
                       weight="BOLD"), P(5.2, 3.40),
                    [req_at[0], req_at[1] - P(0.06, 0.04), 0])
        self.play(FadeIn(req), run_time=0.45)
        self.play(FadeIn(req2, shift=UP * 0.08), run_time=0.55)

        # LANDSCAPE ONLY — the ST5 receipt. Never spoken.
        if not PORTRAIT:
            st5 = _card(5.4, 1.46, [3.30, -0.70, 0])
            self.play(Create(st5), run_time=0.5)
            a = _fit(_t("AI-designed hardware already flies", size=21,
                        color=INK), 5.0, [3.30, -0.42, 0])
            b = _fit(_t("NASA ST5 — three evolved antennas, 2006", size=18,
                        color=SOFT), 5.0, [3.30, -0.94, 0])
            self.play(FadeIn(a), run_time=0.45)
            self.play(FadeIn(b), run_time=0.4)

        closer(self, "nobody asked the optimiser for them", cx=P(0.0, 0.0),
               size=P(29, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE PRICE
# ═════════════════════════════════════════════════════════════════════════════
class B10_ThePrice(Paced):
    BEAT, RT, HOLD = "B10", 1.550, 0.239

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The design tell",
               cite="computed in this reel: worst-case damaged and undamaged "
                    "compliance against the mass budget")

        # price.png is 1560x780 -> 0.500. pw 6.00 -> ph 3.00.
        pw = P(6.00, 3.30)
        pat = [P(-1.65, 0.0), P(0.86, 1.00), 0]
        plate = _plate("price.png", pw, pat, frame=False)
        ph = _plate_h("price.png", pw)
        self.play(FadeIn(plate), run_time=0.85)

        xlab = _fit(_t("mass budget  →", size=P(20, 16), color=SOFT),
                    P(4.4, 3.20))
        xlab.move_to([pat[0], pat[1] - ph * 0.5 - P(0.30, 0.34), 0])
        self.play(FadeIn(xlab), run_time=0.4)

        if not PORTRAIT:
            for txt, colr, dx, y in [("worst void", ACCT, 0.40, 1.15),
                                     ("undamaged", INK, -0.25, -1.28)]:
                lb = _fit(_t(txt, size=20, color=colr), 2.6,
                          [pat[0] + pw * dx, pat[1] + y, 0])
                self.play(FadeIn(lb), run_time=0.35)

        col_at = P([3.55, 1.40, 0], [0, -1.10, 0])
        a = _fit(_t("1.6x", size=P(44, 34), color=ACCT, weight="BOLD"),
                 P(3.2, 2.00), [col_at[0], col_at[1], 0])
        self.play(FadeIn(a, shift=UP * 0.10), run_time=0.6)
        b = _fit(_t("not 31x, at 60% mass", size=P(22, 18), color=SOFT),
                 P(4.4, 3.34))
        b.move_to([col_at[0], col_at[1] - P(0.62, 0.56), 0])
        self.play(FadeIn(b), run_time=0.45)

        if not PORTRAIT:
            roll = _fit(_t("and the saving falls", size=21, color=SOFT), 4.4,
                        [col_at[0], col_at[1] - 1.32, 0])
            self.play(FadeIn(roll), run_time=0.4)
            r2 = _fit(_t("60%  →  40%", size=34, color=INK, weight="BOLD"), 4.4,
                      [col_at[0], col_at[1] - 1.90, 0])
            self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.55)

        closer(self, "a third of the saving, given back", cx=P(0.0, 0.0),
               size=P(29, 23))
        self.hold_to_beat()
