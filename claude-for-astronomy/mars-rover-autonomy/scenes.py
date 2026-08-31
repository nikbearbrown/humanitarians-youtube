"""scenes.py — Manim scenes for mars-rover-autonomy.

*Nobody Is Coming to Approve It.* — ai-explainer, claude-hai, Ep. 06.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY — never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta — the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

THIS FILE IS ASPECT-AWARE — IT RENDERS BOTH CUTS
  The reel ships in 16:9 (3840x2160) and 9:16 (2160x3840). Manim keeps
  frame_height = 8.0 in both, so the VERTICAL band plan below is identical
  either way; only the horizontal extent changes — x +-6.15 landscape,
  x +-1.80 portrait. Every scene therefore reads PORTRAIT and either lays its
  elements side by side (landscape) or stacks them (portrait). There is no
  second hand-tuned scene file to drift out of sync with this one.

  Portrait is NOT just a crop: at 4.5 units wide against 14.22 it has less
  usable area, not more, because the height is the same. So portrait
  compositions carry FEWER elements, larger — that is a deliberate reduction,
  not an accident of scaling.

LAYOUT BAND PLAN (every scene obeys it — this is what keeps the gates green)
                        landscape      portrait
  title                   +3.02          +3.14
  hairline                +2.66          +2.84
  the figure       +2.40 .. -1.90   +2.62 .. -2.02
  the closing line        -2.50          -2.42   (terracotta rule 0.28 below)
  the citation            -3.20          -2.95   (left-anchored / centred)
  the wordmark bug        -3.12          -3.28   (right-anchored, LOGO LAW)

  GATE V's title-safe inset maps to x +-6.4, y +-3.6 (landscape) and
  x +-1.95, y +-3.4 (portrait). Everything here stays inside.

PLATES
  Every terrain plate is SYNTHETIC, produced by assets/gen_mars.py from a
  seeded procedural height field. Navcam and Hazcam are genuinely greyscale
  instruments, so a mono plate is the honest depiction. Scenes that could be
  mistaken for a NASA image caption them SYNTHETIC or SCHEMATIC.

GATE NOTES (learned the expensive way on Eps. 03-05)
  - `import numpy as np` explicitly: GATE A's stub does not re-export it.
  - Never build a Line from `mob.get_left()[0]`; under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set `_qc_intentional` or GATE B calls it text-on-curve.
  - Never run a stroke behind or through a label, even under an opaque chip.
  - ImageMobject is not a VMobject: group it with `Group`, never `VGroup`.
  - Do not rotate an ImageMobject; pre-bake rotations into the assets.
  - Manim's cache key does not hash the CONTENTS of an image a scene loads.
    Re-tuning a plate means deleting media/videos, not just manim/*.mp4.
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


def _rover(at, r=0.13):
    """The rover mark: the one thing on screen that has to commit."""
    return Dot(point=at, radius=r, color=ACCT)


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
        """Hold the finished composition until the narration is done."""
        target = BEAT_SECONDS.get(self.BEAT or "", 0.0)
        now = float(getattr(getattr(self, "renderer", None), "time", 0.0) or 0.0)
        self.wait(max(floor, target - now) if target else floor)


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 0.744, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "AI in Astronomy & Space Science  ·  Ep. 06",
               cite="brutalist.art  ·  ai-explainer  ·  Pragmatist register")

        name_at = P([-3.30, 1.30, 0], [0, 1.92, 0])
        name = _fit(_t("Om Mali", size=P(98, 66), weight="BOLD"),
                    P(5.6, 3.30), name_at)
        self.play(Write(name), run_time=1.1)
        hair = _underline(name, sw=P(7, 5), buff=P(0.22, 0.16), pad=0.12)
        self.play(Create(hair), run_time=0.6)

        role = _fit(_t("Humanitarians AI  ·  presenter", size=P(29, 22),
                       color=SOFT), P(5.6, 3.30))
        role.move_to([name_at[0], name_at[1] - P(1.40, 0.86), 0])
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)
        sub = _fit(_t("autonomy is what latency forces", size=P(26, 20),
                      color=SOFT), P(5.6, 3.30))
        sub.move_to([name_at[0], name_at[1] - P(2.10, 1.36), 0])
        self.play(FadeIn(sub), run_time=0.45)

        pw, ph = P(5.6, 3.52), P(3.60, 2.42)
        pc = P([3.20, 0.45, 0], [0, -0.90, 0])
        panel = _card(pw, ph, pc)
        self.play(Create(panel), run_time=0.7)

        # row 1 — the premise five episodes have shared, then struck
        r1 = _fit(_t("every episode so far", size=P(28, 22)), pw - 0.7)
        r1.move_to([pc[0], pc[1] + ph * 0.31, 0])
        r1b = _fit(_t("too much data", size=P(24, 19), color=SOFT), pw - 0.7)
        r1b.move_to([pc[0], pc[1] + ph * 0.13, 0])
        self.play(FadeIn(r1), FadeIn(r1b), run_time=0.5)
        s = _strike(r1b, pad=0.10)
        self.play(Create(s), run_time=0.45)

        div = Line([pc[0] - pw * 0.42, pc[1] - ph * 0.02, 0],
                   [pc[0] + pw * 0.42, pc[1] - ph * 0.02, 0],
                   color=RULE, stroke_width=2)
        self.play(Create(div), run_time=0.3)

        # row 2 — the premise of THIS one
        r2 = _fit(_t("this one", size=P(30, 24), color=ACCT, weight="BOLD"),
                  pw - 0.7)
        r2.move_to([pc[0], pc[1] - ph * 0.18, 0])
        r2b = _fit(_t("too much distance", size=P(26, 21), color=ACCT), pw - 0.7)
        r2b.move_to([pc[0], pc[1] - ph * 0.36, 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)

        closer(self, "Ep. 06  ·  the expert is too far away to ask.",
               size=P(28, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — EXECUTIVE SUMMARY
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.244, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath",
               cite="synthetic terrain, generated for this episode")

        pw = P(5.20, 3.30)
        pat = P([-3.30, 0.35, 0], [0, 1.45, 0])
        plate = _plate("navcam.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.8)
        cap = _cap("SYNTHETIC — not a NASA image", plate)
        self.play(FadeIn(cap), run_time=0.35)

        stage = P([3.05, 0.30, 0], [0, -0.95, 0])
        stage_w = P(5.6, 3.40)

        # set 1
        s1 = _fit(_t("one plan a day", size=P(46, 34), weight="BOLD"), stage_w,
                  [stage[0], stage[1] + P(0.55, 0.55), 0])
        s1b = _fit(_t("written on Earth, before the rover wakes",
                      size=P(24, 18), color=SOFT), stage_w,
                   [stage[0], stage[1] - P(0.25, 0.10), 0])
        self.play(FadeIn(s1, shift=UP * 0.12), run_time=0.7)
        self.play(FadeIn(s1b), run_time=0.5)
        self.wait(0.7)
        self.play(FadeOut(s1), FadeOut(s1b), run_time=0.45)

        # set 2 — the two decisions
        c1 = _quiet_chip("where to drive", size=P(24, 19), max_w=stage_w)
        c2 = _quiet_chip("what to look at", size=P(24, 19), max_w=stage_w)
        if PORTRAIT:
            c1.move_to([stage[0], stage[1] + 0.42, 0])
            c2.move_to([stage[0], stage[1] - 0.42, 0])
        else:
            c1.move_to([stage[0], stage[1] + 0.62, 0])
            c2.move_to([stage[0], stage[1] - 0.32, 0])
        self.play(FadeIn(c1, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(c2, shift=UP * 0.08), run_time=0.5)
        self.wait(0.6)
        self.play(FadeOut(c1), FadeOut(c2), run_time=0.45)

        # set 3 — the shape of the answer
        s3 = _fit(_t("scored", size=P(52, 38), color=ACCT, weight="BOLD"),
                  stage_w, [stage[0], stage[1] + P(0.55, 0.50), 0])
        s3b = _fit(_t("not asked", size=P(38, 28), color=SOFT), stage_w,
                   [stage[0], stage[1] - P(0.30, 0.25), 0])
        self.play(FadeIn(s3, shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(s3b), run_time=0.5)

        closer(self, "nobody is coming to approve it")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE GAP
# ═════════════════════════════════════════════════════════════════════════════
class B03_LightTime(Paced):
    BEAT, RT, HOLD = "B03", 1.151, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The number that forces everything else",
               cite="one-way light time, Mars–Earth  ·  ESA Mars Express")

        if PORTRAIT:
            a, b = np.array([-1.16, 1.98, 0]), np.array([1.16, 1.98, 0])
        else:
            a, b = np.array([-4.55, 1.32, 0]), np.array([4.55, 1.32, 0])

        earth = Circle(radius=P(0.40, 0.32), color=INK, stroke_width=3.2,
                       fill_color=CARD, fill_opacity=1.0).move_to(a)
        mars = Circle(radius=P(0.32, 0.26), color=ACCT, stroke_width=3.2,
                      fill_color=CARD, fill_opacity=1.0).move_to(b)
        el = _t("Earth", size=P(22, 18), color=SOFT)
        ml = _t("Mars", size=P(22, 18), color=SOFT)
        el.next_to(earth, DOWN, buff=P(0.20, 0.16))
        ml.next_to(mars, DOWN, buff=P(0.20, 0.16))
        self.play(Create(earth), Create(mars), FadeIn(el), FadeIn(ml),
                  run_time=0.9)

        d = (b - a) / np.linalg.norm(b - a)
        p0, p1 = a + d * P(0.62, 0.52), b - d * P(0.52, 0.44)
        chan = DashedLine(p0, p1, color=GHOST, stroke_width=2.4,
                          dash_length=0.12)
        self.play(Create(chan), run_time=0.7)

        pulse = Dot(point=p0, radius=0.11, color=ACC)
        self.play(FadeIn(pulse), run_time=0.2)
        self.play(pulse.animate.move_to(p1), run_time=1.1)

        lab1 = _fit(_t("3 to 22 minutes, one way", size=P(27, 20), color=ACCT,
                       weight="BOLD"), P(6.0, 3.30))
        lab1.move_to(P([0, 2.10, 0], [0, 1.10, 0]))
        self.play(FadeIn(lab1, shift=UP * 0.08), run_time=0.6)

        self.play(pulse.animate.move_to(p0), run_time=1.0)
        lab2 = _fit(_t("up to 44 for an answer", size=P(24, 18), color=SOFT),
                    P(6.0, 3.30))
        lab2.move_to(P([0, 0.62, 0], [0, 0.62, 0]))
        self.play(FadeIn(lab2), run_time=0.5)
        self.play(FadeOut(pulse), run_time=0.25)

        # no joystick
        chip = _quiet_chip("no real-time control", size=P(24, 19),
                           max_w=P(6.0, 3.40))
        chip.move_to(P([0, -0.35, 0], [0, -0.06, 0]))
        self.play(FadeIn(chip), run_time=0.5)
        st = _strike(chip[1], pad=0.10)
        self.play(Create(st), run_time=0.4)

        # the sol block
        bw = P(7.60, 3.40)
        bx = P(-3.80, -1.70)
        bar = _bar(1.0, bw, P(0.42, 0.34), [bx, P(-1.25, -0.92), 0], fill=GHOST)
        self.play(Create(bar[0]), FadeIn(bar[1]), run_time=0.6)
        blab = _fit(_t("one command block, uplinked before the rover wakes",
                       size=P(22, 16), color=SOFT), P(7.60, 3.44))
        blab.move_to([0, P(-1.76, -1.44), 0])
        self.play(FadeIn(blab), run_time=0.5)

        closer(self, "an unanswered question costs a day")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — WHAT IT SEES
# ═════════════════════════════════════════════════════════════════════════════
class B04_WhatItSees(Paced):
    BEAT, RT, HOLD = "B04", 1.55, 0.013

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Stereo in, one number per cell out",
               cite="synthetic terrain and cost grid, generated for this episode")

        pw = P(4.90, 2.70)
        left_at = P([-3.42, 0.62, 0], [0, 1.62, 0])
        right_at = P([3.42, 0.62, 0], [0, -0.95, 0])

        if not PORTRAIT:
            # the stereo partner, offset behind — two cameras, one scene
            back = _plate("navcam_far.png", pw,
                          [left_at[0] - 0.26, left_at[1] + 0.24, 0])
            self.play(FadeIn(back), run_time=0.6)
        cam = _plate("navcam.png", pw, left_at)
        self.play(FadeIn(cam), run_time=0.7)
        cap = _cap("SYNTHETIC — not a NASA image", cam)
        self.play(FadeIn(cap), run_time=0.35)

        if PORTRAIT:
            arr = _arrow([0, 0.28, 0], [0, 0.02, 0])
        else:
            arr = _arrow([-0.62, 0.62, 0], [0.62, 0.62, 0])
        self.play(GrowArrow(arr), run_time=0.5)

        grid = _plate("costmap.png", pw, right_at)
        self.play(FadeIn(grid), run_time=0.9)

        # one cell, called out
        gh = _plate_h("costmap.png", pw)
        cell = pw / 32.0
        cx = right_at[0] - pw * 0.5 + cell * 8.5
        cy = right_at[1] + gh * 0.5 - (gh / 21.5) * 12.5
        ring = Rectangle(width=cell * 2.6, height=cell * 2.6, color=ACC,
                         stroke_width=P(5, 4), fill_opacity=0)
        ring.move_to([cx, cy, 0])
        self.play(Create(ring), run_time=0.6)

        if not PORTRAIT:
            note = _fit(_t("each cell carries one number:  step height + slope",
                           size=22, color=SOFT), 6.4)
            note.next_to(grid, DOWN, buff=0.42)
            self.play(FadeIn(note), run_time=0.5)

        closer(self, "one number per cell is the whole world")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE CHOICE
# ═════════════════════════════════════════════════════════════════════════════
class B05_TheFan(Paced):
    BEAT, RT, HOLD = "B05", 1.55, 0.155

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "About 1,700 candidates, one commitment",
               cite="ENav path counts and horizon: IEEE Spectrum / Rankin et al. 2023")

        pw = P(6.10, 3.42)
        pat = P([-2.42, 0.32, 0], [0, 1.40, 0])

        a = _plate("pathfan_a.png", pw, pat)
        self.play(FadeIn(a), run_time=0.9)

        col_x = P(3.85, 0.0)
        chip_w = P(4.50, 3.44)
        ys = P([1.95, 1.05, 0.15, -0.75, -1.62],
               [-0.42, -1.06, -1.70, None, None])

        c1 = _chip("~1,700 paths, ≈6 m ahead", size=P(23, 18), max_w=chip_w)
        c1.move_to([col_x, ys[0], 0])
        self.play(FadeIn(c1, shift=UP * 0.08), run_time=0.55)

        c2 = _quiet_chip("scored on time + roughness", size=P(22, 17),
                         max_w=chip_w)
        c2.move_to([col_x, ys[1], 0])
        self.play(FadeIn(c2), run_time=0.5)

        b = _plate("pathfan_b.png", pw, pat)
        self.play(FadeIn(b), FadeOut(a), run_time=0.7)

        c3 = _quiet_chip("clearance check on the survivors", size=P(22, 17),
                         max_w=chip_w)
        c3.move_to([col_x, ys[2], 0])
        self.play(FadeIn(c3), run_time=0.5)

        c = _plate("pathfan.png", pw, pat)
        self.play(FadeIn(c), FadeOut(b), run_time=0.7)

        if not PORTRAIT:
            c4 = _chip("it drives the best survivor", size=23, max_w=chip_w)
            c4.move_to([col_x, ys[3], 0])
            self.play(FadeIn(c4, shift=UP * 0.08), run_time=0.55)
            c5 = _quiet_chip("and it looks while it drives", size=22,
                             max_w=chip_w)
            c5.move_to([col_x, ys[4], 0])
            self.play(FadeIn(c5), run_time=0.5)
        else:
            cap = _cap("SYNTHETIC — the plate draws a legible subset", c)
            self.play(FadeIn(cap), run_time=0.4)

        closer(self, "it commits while the wheels are turning")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — THE SECOND DECISION
# ═════════════════════════════════════════════════════════════════════════════
class B06_Aegis(Paced):
    BEAT, RT, HOLD = "B06", 1.55, 0.009

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The same move, on the science side",
               cite="AEGIS / Rockster: Francis et al. 2017  ·  synthetic terrain")

        pw = P(5.90, 3.40)
        pat = P([-2.55, 0.42, 0], [0, 1.48, 0])

        plain = _plate("rockfield.png", pw, pat)
        self.play(FadeIn(plain), run_time=0.8)
        cap = _cap("SYNTHETIC — not a NASA image", plain)
        self.play(FadeIn(cap), run_time=0.35)

        edges = _plate("rockfield_edges.png", pw, pat)
        self.play(FadeIn(edges), FadeOut(plain), run_time=0.9)

        col_x = P(3.70, 0.0)
        chip_w = P(4.40, 3.44)
        ys = P([1.92, 1.18, 0.44], [-0.34, -1.00, -1.66])
        chips = []
        for label, y in zip(("how big", "how bright", "how far away"), ys):
            ch = _quiet_chip(label, size=P(23, 19), max_w=chip_w)
            ch.move_to([col_x, y, 0])
            chips.append(ch)
            self.play(FadeIn(ch, shift=UP * 0.06), run_time=0.42)

        if not PORTRAIT:
            card = _card(4.40, 1.55, [col_x, -0.98, 0])
            self.play(Create(card), run_time=0.55)
            t1 = _fit(_t("SCENE PROFILE", size=21, color=ACCT, weight="BOLD"),
                      4.0, [col_x, -0.62, 0])
            t2 = _fit(_t("what counts as worth looking at,", size=19,
                         color=SOFT), 4.0, [col_x, -1.02, 0])
            t3 = _fit(_t("in this kind of terrain", size=19, color=SOFT),
                      4.0, [col_x, -1.34, 0])
            self.play(FadeIn(t1), run_time=0.4)
            self.play(FadeIn(t2), FadeIn(t3), run_time=0.45)

        ranked = _plate("rockfield_ranked.png", pw, pat)
        self.play(FadeIn(ranked), FadeOut(edges), run_time=0.9)

        closer(self, "the laser fires without asking")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — WORKED EXAMPLE
# ═════════════════════════════════════════════════════════════════════════════
class B07_Snowdrift(Paced):
    BEAT, RT, HOLD = "B07", 1.55, 0.508

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Snowdrift Peak, 2023",
               cite="distances and sol counts: NASA/JPL, 2023  ·  map is schematic")

        pw = P(5.30, 3.05)
        pat = P([-2.85, 0.42, 0], [0, 1.48, 0])
        m = _plate("route.png", pw, pat)
        self.play(FadeIn(m), run_time=0.9)
        cap = _cap("SCHEMATIC — the route is drawn, not surveyed", m)
        self.play(FadeIn(cap), run_time=0.35)

        col_x = P(3.55, 0.0)
        row_w = P(4.60, 3.44)
        ys = P([1.86, 0.86, -0.34, -1.28], [-0.28, -0.94, -1.62, None])

        sw1 = Line(LEFT, RIGHT, color=GHOST, stroke_width=7).set_width(0.62)
        l1 = _fit(_t("520 m  straight across", size=P(25, 20), color=SOFT),
                  row_w - 0.9)
        g1 = VGroup(sw1, l1).arrange(RIGHT, buff=0.24).move_to([col_x, ys[0], 0])
        self.play(FadeIn(g1), run_time=0.6)

        sw2 = Line(LEFT, RIGHT, color=ACC, stroke_width=9).set_width(0.62)
        l2 = _fit(_t("759 m  actually driven", size=P(26, 21), color=ACCT,
                     weight="BOLD"), row_w - 0.9)
        g2 = VGroup(sw2, l2).arrange(RIGHT, buff=0.24).move_to([col_x, ys[1], 0])
        self.play(FadeIn(g2, shift=UP * 0.08), run_time=0.6)

        n1 = _fit(_t("6 sols to cross it", size=P(29, 22), weight="BOLD"),
                  row_w, [col_x, ys[2], 0])
        self.play(FadeIn(n1, shift=UP * 0.08), run_time=0.55)

        if not PORTRAIT:
            n2 = _fit(_t("about 12 sols faster than", size=24, color=SOFT),
                      row_w, [col_x, ys[3] + 0.28, 0])
            n3 = _fit(_t("Curiosity would have managed", size=24, color=SOFT),
                      row_w, [col_x, ys[3] - 0.10, 0])
            self.play(FadeIn(n2), FadeIn(n3), run_time=0.55)

        closer(self, "it went further to get there sooner")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — THE DESIGN TELL
# ═════════════════════════════════════════════════════════════════════════════
class B08_TheProfile(Paced):
    BEAT, RT, HOLD = "B08", 1.483, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The design tell",
               cite="the scene profile is set by the science team  ·  Francis et al. 2017")

        cw, ch = P(6.30, 3.30), P(4.10, 3.10)
        cc = P([-1.85, 0.30, 0], [0, 0.92, 0])
        card = _card(cw, ch, cc)
        self.play(Create(card), run_time=0.8)

        head = _fit(_t("SCENE PROFILE", size=P(27, 22), color=ACCT,
                       weight="BOLD"), cw - 0.8,
                    [cc[0], cc[1] + ch * 0.40, 0])
        self.play(FadeIn(head), run_time=0.5)
        hr = Line([cc[0] - cw * 0.40, cc[1] + ch * 0.30, 0],
                  [cc[0] + cw * 0.40, cc[1] + ch * 0.30, 0],
                  color=RULE, stroke_width=2)
        self.play(Create(hr), run_time=0.3)

        rules = ("prefer  LARGE", "prefer  BRIGHT", "prefer  NEAR",
                 "prefer  THIS OUTLINE")
        for k, r in enumerate(rules):
            ln = _fit(_t(r, size=P(25, 20)), cw - 1.0,
                      [cc[0], cc[1] + ch * 0.13 - k * ch * 0.115, 0])
            self.play(FadeIn(ln, shift=RIGHT * 0.10), run_time=0.38)

        sig = _fit(_t("written on Earth, before launch", size=P(24, 19),
                      color=ACCT, weight="BOLD"), cw - 0.8,
                   [cc[0], cc[1] - ch * 0.36, 0])
        self.play(FadeIn(sig, shift=UP * 0.08), run_time=0.6)
        su = _underline(sig, buff=0.10)
        self.play(Create(su), run_time=0.35)

        # the gap the document has to cross
        if PORTRAIT:
            arr = _arrow([0, -0.80, 0], [0, -1.28, 0], color=ACC)
            rmark = _rover([0, -1.55, 0], r=0.15)
            rlab = _t("the rover", size=17, color=SOFT)
            rlab.next_to(rmark, DOWN, buff=0.16)
        else:
            arr = _arrow([1.45, 0.30, 0], [3.90, 0.30, 0], color=ACC)
            rmark = _rover([4.60, 0.30, 0], r=0.18)
            rlab = _t("the rover", size=20, color=SOFT)
            rlab.next_to(rmark, DOWN, buff=0.20)
        self.play(GrowArrow(arr), run_time=0.7)
        self.play(FadeIn(rmark), FadeIn(rlab), run_time=0.45)

        if not PORTRAIT:
            gap = _t("3–22 min", size=20, color=SOFT)
            gap.move_to([2.68, 0.76, 0])
            self.play(FadeIn(gap), run_time=0.4)

        closer(self, "the taste is a document, and it has an author")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — THE RESULT
# ═════════════════════════════════════════════════════════════════════════════
class B09_Result(Paced):
    BEAT, RT, HOLD = "B09", 1.55, 0.001

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What the autonomy actually buys",
               cite="autonomy share: IEEE Spectrum (sol 1,312)  ·  AEGIS figures: two evaluations, Curiosity/ChemCam")

        bw = P(4.30, 2.55)
        bh = P(0.36, 0.30)
        lx = P(-5.80, -1.62)
        rx = P(0.65, -1.62)

        def row(x0, y, frac, name, value, fill=ACC):
            lab = _fit(_t(name, size=P(23, 18), color=SOFT), bw)
            lab.move_to([x0 + lab.width / 2, y + P(0.36, 0.30), 0])
            bar = _bar(frac, bw, bh, [x0, y, 0], fill=fill)
            val = _t(value, size=P(24, 19), color=ACCT, weight="BOLD")
            val.move_to([x0 + bw + P(0.62, 0.42), y, 0])
            self.play(FadeIn(lab), run_time=0.30)
            self.play(Create(bar[0]), run_time=0.22)
            self.play(GrowFromEdge(bar[1], LEFT), FadeIn(val), run_time=0.62)
            return VGroup(lab, bar, val)

        if PORTRAIT:
            ys = [2.30, 1.35, 0.05, -0.90]
        else:
            ys = [1.25, 0.28, 1.25, 0.28]

        if not PORTRAIT:
            h1 = _fit(_t("share of distance driven autonomously", size=22,
                         color=INK), 5.4)
            h1.move_to([-3.55, 2.24, 0])
            self.play(FadeIn(h1), run_time=0.4)
        row(lx, ys[0], 0.062,
            P("Curiosity", "Curiosity — autonomous share"), "6.2%", fill=GHOST)
        row(lx, ys[1], 0.90,
            P("Perseverance", "Perseverance — autonomous share"), "~90%")

        rule = _fit(_t("699.9 m — longest drive with no human review",
                       size=P(23, 17), color=INK), P(5.4, 3.44))
        rule.move_to([P(-3.55, 0.0), P(-0.80, -1.75), 0])
        ru = _underline(rule, buff=0.12, sw=3)
        self.play(FadeIn(rule), run_time=0.5)
        self.play(Create(ru), run_time=0.35)

        if not PORTRAIT:
            div = Line([0.05, 2.00, 0], [0.05, -1.20, 0], color=RULE,
                       stroke_width=2)
            self.play(Create(div), run_time=0.35)

        if not PORTRAIT:
            h2 = _fit(_t("AEGIS picked the intended material", size=22,
                         color=INK), 5.4)
            h2.move_to([3.05, 2.24, 0])
            self.play(FadeIn(h2), run_time=0.4)
        row(rx, ys[2], 0.93,
            P("with onboard targeting", "AEGIS — onboard targeting"), ">93%")
        row(rx, ys[3], 0.20,
            P("pointed blind", "AEGIS — pointed blind"), "~20%", fill=GHOST)

        if not PORTRAIT:
            note = _fit(_t("Curiosity / ChemCam — two separate evaluations",
                           size=23, color=INK), 5.4)
            note.move_to([3.05, -0.80, 0])
            nu = _underline(note, buff=0.12, sw=3, color=GHOST)
            self.play(FadeIn(note), run_time=0.5)
            self.play(Create(nu), run_time=0.35)

        closer(self, "the numbers are real; so are the conditions",
               size=P(28, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — WHERE IT FAILS
# ═════════════════════════════════════════════════════════════════════════════
class B10_TwoLimits(Paced):
    BEAT, RT, HOLD = "B10", 1.462, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Two limits, and neither is a bug",
               cite="239 m and 255 sols are subtractions from the figures shown  ·  NASA/JPL")

        # ── limit one: caution, paid in metres ───────────────────────────────
        pw = P(3.40, 2.30)
        pat = P([-3.55, 0.92, 0], [0, 1.78, 0])
        m = _plate("route.png", pw, pat)
        self.play(FadeIn(m), run_time=0.7)

        big = _fit(_t("239 m", size=P(46, 36), color=ACCT, weight="BOLD"),
                   P(3.60, 3.20))
        big.move_to(P([-3.55, -0.72, 0], [0, 0.40, 0]))
        self.play(FadeIn(big, shift=UP * 0.10), run_time=0.6)
        bu = _underline(big, buff=0.12)
        self.play(Create(bu), run_time=0.35)

        if not PORTRAIT:
            sub = _fit(_t("of the crossing spent going around things",
                          size=22, color=SOFT), 4.60)
            sub.move_to([-3.55, -1.38, 0])
            self.play(FadeIn(sub), run_time=0.5)

        lab1 = _fit(_t("caution, paid in metres", size=P(25, 20), color=INK),
                    P(4.60, 3.44))
        lab1.move_to(P([-3.55, -1.86, 0], [0, -0.30, 0]))
        self.play(FadeIn(lab1), run_time=0.45)

        if not PORTRAIT:
            div = Line([0.05, 2.20, 0], [0.05, -2.05, 0], color=RULE,
                       stroke_width=2)
            self.play(Create(div), run_time=0.35)

        # ── limit two: you can only change its mind on a mission clock ───────
        ax_y = P(-0.10, -1.15)
        x0, x1 = P(1.05, -1.58), P(5.95, 1.58)
        axis = Line([x0, ax_y, 0], [x1, ax_y, 0], color=INK, stroke_width=2.6)
        self.play(Create(axis), run_time=0.6)

        # sol 442 and sol 697 placed proportionally on a 400..740 sol axis
        def at_sol(s):
            return x0 + (x1 - x0) * (s - 400.0) / 340.0

        t442, t697 = at_sol(442), at_sol(697)
        for tx, name in ((t442, "sol 442"), (t697, "sol 697")):
            tick = Line([tx, ax_y - 0.16, 0], [tx, ax_y + 0.16, 0], color=INK,
                        stroke_width=3)
            lb = _t(name, size=P(21, 16), color=SOFT)
            lb.move_to([tx, ax_y - 0.44, 0])
            self.play(Create(tick), FadeIn(lb), run_time=0.4)

        span = Line([t442, ax_y + P(0.42, 0.0), 0],
                    [t697, ax_y + P(0.42, 0.0), 0], color=ACC,
                    stroke_width=P(9, 8))
        self.play(Create(span), run_time=0.8)
        sl = _t("255 sols", size=P(30, 23), color=ACCT, weight="BOLD")
        sl.move_to([(t442 + t697) / 2, ax_y + P(0.86, 0.40), 0])
        self.play(FadeIn(sl, shift=UP * 0.08), run_time=0.55)

        if not PORTRAIT:
            lab2 = _fit(_t("one definition of interesting, then the next",
                           size=23, color=INK), 5.40)
            lab2.move_to([(x0 + x1) / 2, ax_y - 1.10, 0])
            self.play(FadeIn(lab2), run_time=0.5)

        closer(self, "you can only change its mind on a mission clock",
               size=P(29, 22))
        self.hold_to_beat()
