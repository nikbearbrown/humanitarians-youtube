"""scenes.py - Manim scenes for asteroid-impact-warning.

*The Number Went Up.* - ai-explainer, claude-hai, Ep. 08.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL
  Terracotta marks WHAT THE MACHINE DECIDES: the detections the network calls
  real, the two real postage-stamp classes out of eight, the fitted tracklet,
  the uncertainty cloud, the probability curve. Ink marks WHAT THE SKY
  ACTUALLY DOES: the Earth, the capture disc, the catalogued fraction. The
  mapping never flips. B04 teaches it once and every later plate reads free.

  The single most important consequence: at B06 the terracotta STOPS at a
  boundary. The learned half of the pipeline ends there, and the number that
  frightens people comes out of the ink half. That is the episode.

THIS FILE IS ASPECT-AWARE - IT RENDERS BOTH CUTS
  The reel ships in 16:9 (3840x2160) and 9:16 (2160x3840). Manim keeps
  frame_height = 8.0 in both, so the VERTICAL band plan is identical either
  way; only the horizontal extent changes - x +-6.15 landscape, x +-1.80
  portrait. Every scene reads PORTRAIT and either lays its elements side by
  side or stacks them. Portrait is NOT a crop: at 4.5 units wide against 14.22
  with the same height it has LESS usable area, so portrait compositions carry
  fewer elements, larger. That is a deliberate reduction.

LAYOUT BAND PLAN (every scene obeys it - this is what keeps the gates green)
                        landscape      portrait
  title                   +3.02          +3.14
  hairline                +2.66          +2.84
  the figure       +2.40 .. -1.90   +2.62 .. -2.02
  the closing line        -2.50          -2.42   (terracotta rule 0.28 below)
  the citation            -3.20          -2.95
  the wordmark bug        -3.12          -3.28   (right-anchored, LOGO LAW)

PLATES
  Every plate comes from assets/gen_neo.py, which RUNS the calculations this
  episode describes: real image differencing on a synthetic field, the eight
  artefact classes each synthesised from its OWN physical model, a
  least-squares tracklet fit, and a target-plane quadrature for the impact
  probability that ASSERTS its own analytic peak and refuses to write a plate
  if it disagrees. The sky frames are a TOY - right mechanism, invented field -
  and every beat that shows one says so.

  PUBLISHED vs COMPUTED-HERE is kept visibly apart. B07 and B09 quote the real
  2024 YR4 record and cite it. B08 shows this reel's own computation of why
  that record had the shape it did, and captions itself as such.

GATE NOTES (learned the expensive way on Eps. 03-07)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - An opaque chip over a texture is NOT enough for GATE B - clear a keep-out
    hole in the texture (Ep. 07 B10).
  - A _strike on a horizontal arrow is invisible; use a crossing X (Ep. 07).
  - Check BOTH aspects. Ep. 06's worst defect was a P() call with its
    landscape/portrait values transposed: harmless at 14.22 units wide, and an
    edge-bleed blocker at 4.5.
  - Pace the scene to the narration (see Paced). compile.py fills a beat by
    SLOWING the clip, and a 3x stretch is visible slow-motion that GATE V,
    which samples still frames, can never see.
  - Render ONE Manim process at a time per reel folder. Two concurrent renders
    corrupt each other's ffmpeg concat and silently drop frames (Ep. 07).
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
    BEAT, RT, HOLD = "B01", 0.867, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "AI in Astronomy & Space Science  ·  Ep. 08",
               cite="brutalist.art  ·  ai-explainer  ·  Pragmatist register")

        name_at = P([-3.30, 1.30, 0], [0, 1.92, 0])
        name = _fit(_t("Om Mali", size=P(98, 66), weight="BOLD"),
                    P(5.6, 3.30), name_at)
        self.play(Write(name), run_time=1.1)
        self.play(Create(_underline(name, sw=P(7, 5), buff=P(0.22, 0.16), pad=0.12)),
                  run_time=0.6)

        role = _fit(_t("Humanitarians AI  ·  presenter", size=P(29, 22), color=SOFT),
                    P(5.6, 3.30))
        role.move_to([name_at[0], name_at[1] - P(1.40, 0.86), 0])
        self.play(FadeIn(role, shift=UP * 0.1), run_time=0.5)

        pw, ph = P(5.6, 3.52), P(3.60, 2.30)
        pc = P([3.20, 0.45, 0], [0, -0.80, 0])
        self.play(Create(_card(pw, ph, pc)), run_time=0.7)

        r1 = _fit(_t("seven episodes", size=P(28, 22)), pw - 0.7)
        r1.move_to([pc[0], pc[1] + ph * 0.31, 0])
        r1b = _fit(_t("AI reads the sky", size=P(24, 19), color=SOFT), pw - 0.7)
        r1b.move_to([pc[0], pc[1] + ph * 0.13, 0])
        self.play(FadeIn(r1), FadeIn(r1b), run_time=0.5)
        self.play(Create(_strike(r1b, pad=0.10)), run_time=0.45)

        self.play(Create(Line([pc[0] - pw * 0.42, pc[1] - ph * 0.02, 0],
                              [pc[0] + pw * 0.42, pc[1] - ph * 0.02, 0],
                              color=RULE, stroke_width=2)), run_time=0.3)

        r2 = _fit(_t("this one", size=P(30, 24), color=ACCT, weight="BOLD"), pw - 0.7)
        r2.move_to([pc[0], pc[1] - ph * 0.18, 0])
        r2b = _fit(_t("the reading ends, the arithmetic begins",
                      size=P(23, 18), color=ACCT), pw - 0.8)
        r2b.move_to([pc[0], pc[1] - ph * 0.36, 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)

        closer(self, "Ep. 08  ·  the number is not the news.", size=P(28, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — EXECUTIVE SUMMARY (BLUF)
# ═════════════════════════════════════════════════════════════════════════════
# EXECUTIVE-SUMMARY LAW: beat 2 is the one-breath gist for a smart outsider.
# It is explicitly "a text/kinetic-type beat or a single framing card - never a
# data dump, never the first exhibit", so this scene shows NO plate. The first
# exhibit is B03.
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.55, 0.234

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath",
               cite="the pipeline has a learned half and a computed half")

        stage_w, stage_h = P(9.6, 3.44), 3.10
        sc = [0, P(0.55, 0.62), 0]
        self.play(Create(_card(stage_w, stage_h, sc)), run_time=0.7)

        rows = [("THE SKY IS SCANNED", "every night", INK),
                ("A NETWORK REMOVES", "the junk", INK),
                ("ARITHMETIC DECIDES", "whether to worry", ACCT)]
        prev = None
        for i, (big, small, col) in enumerate(rows):
            y = sc[1] + stage_h * (0.30 - 0.30 * i)
            a = _fit(_t(big, size=P(38, 27), color=col, weight="BOLD"),
                     stage_w - P(1.0, 0.6), [sc[0], y, 0])
            b = _fit(_t(small, size=P(25, 19), color=SOFT),
                     stage_w - P(1.0, 0.6), [sc[0], y - P(0.42, 0.34), 0])
            self.play(FadeIn(a, shift=UP * 0.10), run_time=0.55)
            self.play(FadeIn(b), run_time=0.35)
            if i == 2:
                self.play(Create(_underline(a, buff=0.10)), run_time=0.35)
            prev = (a, b)

        closer(self, "finding it is learned.  fearing it is not.", size=P(30, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE HAYSTACK
# ═════════════════════════════════════════════════════════════════════════════
class B03_TheHaystack(Paced):
    BEAT, RT, HOLD = "B03", 1.55, 0.465

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Subtract last night from tonight",
               cite="ATLAS: 0.5 m f/2, four 30 s frames per field, ~26,000 sq deg a night (Tonry+ 2018)")

        pw = P(7.6, 3.44)
        pat = [0, P(1.11, 1.55), 0]
        plate = _plate("detect.png", pw, pat, frame=False)
        ph = _plate_h("detect.png", pw)
        self.play(FadeIn(plate), run_time=0.7)
        self.play(Create(Rectangle(width=pw, height=ph, color=GHOST,
                                   stroke_width=1.8, fill_opacity=0).move_to(pat)),
                  run_time=0.4)

        # the three panels, named left to right
        names = ["last night", "tonight", "the difference"]
        third = pw / 3.0
        labs = VGroup()
        for i, nm in enumerate(names):
            col = ACCT if i == 2 else SOFT
            lb = _fit(_t(nm, size=P(21, 15), color=col),
                      third - P(0.30, 0.14))
            lb.move_to([pat[0] - pw / 2 + third * (i + 0.5),
                        pat[1] - ph / 2 - P(0.30, 0.22), 0])
            labs.add(lb)
        self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.22),
                  run_time=0.8)

        cap = _fit(_cap("a synthetic field — the mechanism is real, the stars are not",
                        labs, size=P(16, 13), buff=P(0.20, 0.16)), P(9.4, 3.32))
        self.play(FadeIn(cap), run_time=0.35)

        chip = _chip("about 100,000 alerts a night", size=P(24, 18),
                     max_w=P(5.4, 3.30))
        chip.move_to([0, P(-1.42, -1.30), 0])
        self.play(FadeIn(chip, shift=UP * 0.08), run_time=0.55)

        note = _fit(_t("cosmic rays · satellites · every star the subtraction got wrong",
                       size=P(21, 15), color=SOFT), P(9.4, 3.42))
        note.move_to([0, P(-1.98, -1.78), 0])
        self.play(FadeIn(note), run_time=0.45)

        closer(self, "most of what moves is not a rock", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — EIGHT KINDS OF DOT
# ═════════════════════════════════════════════════════════════════════════════
class B04_EightKinds(Paced):
    BEAT, RT, HOLD = "B04", 1.55, 0.066

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Eight kinds of dot",
               cite="8 postage-stamp classes, ResNet-18 + MLP (Chyba Rabeendran & Denneau 2021)")

        # ph = pw * 680/1200. Keep ph <= 3.35 so the plate fits the figure
        # band (+2.40 .. -1.90) with its labels, and centre it flush under the
        # top of the band. At pw = 7.4 the plate was 4.19 tall and ran over
        # the title.
        pw = P(5.90, 3.44)
        pat = [P(-1.55, 0.0), P(0.68, 1.10), 0]
        plate = _plate("stamps.png", pw, pat, frame=False)
        ph = _plate_h("stamps.png", pw)
        self.play(FadeIn(plate), run_time=0.75)

        leg = _fit(_t("asteroid · point source · cosmic ray · dipole",
                      size=P(20, 15), color=SOFT), P(6.0, 3.42))
        leg.move_to([pat[0], pat[1] - ph / 2 - P(0.30, 0.24), 0])
        leg2 = _fit(_t("spike · streak · bleed · noise",
                       size=P(20, 15), color=SOFT), P(6.0, 3.42))
        leg2.move_to([pat[0], pat[1] - ph / 2 - P(0.60, 0.50), 0])
        self.play(FadeIn(leg), run_time=0.45)
        self.play(FadeIn(leg2), run_time=0.4)

        # ring the two classes the narration actually names
        cell = pw / 4.0
        rr = cell * 0.40
        for idx in (2, 3):
            cxx = pat[0] - pw / 2 + cell * (idx + 0.5)
            cyy = pat[1] + ph * 0.24
            self.play(Create(Circle(radius=rr, color=ACC,
                                    stroke_width=P(5, 4)).move_to([cxx, cyy, 0])),
                      run_time=0.45)

        col_at = P([4.30, 0.35, 0], [0, -0.85, 0])
        col_w = P(3.30, 3.30)
        facts = [("one pixel", "a cosmic ray has no point-spread function"),
                 ("two lobes", "a subtraction the registration got wrong")]
        for i, (big, small) in enumerate(facts):
            y = col_at[1] - i * P(1.15, 0.53)
            a = _fit(_t(big, size=P(30, 24), color=ACCT, weight="BOLD"), col_w,
                     [col_at[0], y, 0])
            self.play(FadeIn(a, shift=UP * 0.08), run_time=0.45)
            # PORTRAIT DROPS THE SUBLINES. With them the second subline landed
            # exactly on the closing line and the chip landed on the wordmark
            # bug - two GATE B errors. The two spoken words survive; the gloss
            # is what portrait can afford to lose.
            if not PORTRAIT:
                b = _fit(_t(small, size=19, color=SOFT), col_w,
                         [col_at[0], y - 0.38, 0])
                self.play(FadeIn(b), run_time=0.3)

        two = _chip("only two of the eight are real", size=P(23, 18),
                    max_w=P(3.30, 3.20))
        two.move_to([col_at[0], col_at[1] - P(2.16, 1.00), 0])
        self.play(FadeIn(two, shift=UP * 0.08), run_time=0.55)

        closer(self, "it learns what the camera lies about", size=P(29, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE TRACKLET
# ═════════════════════════════════════════════════════════════════════════════
class B05_Tracklet(Paced):
    BEAT, RT, HOLD = "B05", 1.55, 0.036

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Four detections, one hour",
               cite="second-stage MLP scores the tracklet, not the pictures (arXiv:2101.08912)")

        pw = P(6.6, 3.40)
        pat = [P(-2.30, 0.0), P(0.90, 1.55), 0]
        plate = _plate("tracklet.png", pw, pat, frame=True)
        ph = _plate_h("tracklet.png", pw)
        self.play(FadeIn(plate), run_time=0.75)

        leg = VGroup()
        l1 = _t("a real rock: one straight line, one steady rate",
                size=P(19, 15), color=ACCT)
        l2 = _t("artefacts: no line fits them", size=P(19, 15), color=SOFT)
        for i, l in enumerate((l1, l2)):
            _fit(l, P(6.4, 3.40))
            l.move_to([pat[0], pat[1] - ph / 2 - P(0.30, 0.24) - i * P(0.34, 0.28), 0])
            leg.add(l)
        self.play(LaggedStart(*[FadeIn(l) for l in leg], lag_ratio=0.25),
                  run_time=0.7)

        col_at = P([3.70, 1.62, 0], [0, -0.80, 0])
        col_w = P(4.10, 3.30)
        stats = [("99.6%", "on real asteroids", ACCT),
                 ("0.4%", "false negatives", INK),
                 ("90%", "less for humans to screen", ACCT)]
        # PORTRAIT DROPS THE MIDDLE STAT. Three stacked counters put the last
        # subline on the citation and the last figure on the closing line.
        # 99.6% and 90% are the two the narration speaks; 0.4% is the one the
        # screen can afford to lose.
        if PORTRAIT:
            stats = [stats[0], stats[2]]
        for i, (big, small, col) in enumerate(stats):
            y = col_at[1] - i * P(1.22, 0.80)
            a = _fit(_t(big, size=P(50, 34), color=col, weight="BOLD"), col_w,
                     [col_at[0], y, 0])
            b = _fit(_t(small, size=P(20, 15), color=SOFT), col_w,
                     [col_at[0], y - P(0.58, 0.46), 0])
            self.play(FadeIn(a, shift=UP * 0.10), run_time=0.45)
            self.play(FadeIn(b), run_time=0.28)
            if i == len(stats) - 1:
                self.play(Create(_underline(a, buff=0.04)), run_time=0.3)

        closer(self, "the point was speed, not cleverness", size=P(29, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — WHERE THE LEARNING STOPS
# ═════════════════════════════════════════════════════════════════════════════
# The colour contract's load-bearing beat: the terracotta STOPS at the boundary.
class B06_WhereLearningStops(Paced):
    BEAT, RT, HOLD = "B06", 1.55, 0.009

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Where the learning stops",
               cite="Scout and Sentry at JPL · Aegis at ESA · NEODyS at Pisa")

        bw, bh = P(4.20, 3.24), P(1.30, 1.05)
        left = P([-3.35, 1.62, 0], [0, 1.96, 0])
        right = P([3.35, 1.62, 0], [0, 0.30, 0])

        # the LEARNED box — terracotta fill, because the machine owns it
        lb = RoundedRectangle(width=bw, height=bh, corner_radius=0.14,
                              color=ACC, fill_color=ACC, fill_opacity=1.0,
                              stroke_width=0).move_to(left)
        lt = _fit(_t("LEARNED", size=P(22, 18), color=CARD, weight="BOLD"),
                  bw - 0.5, [left[0], left[1] + bh * 0.22, 0])
        lq = _fit(_t("is this dot real?", size=P(26, 21), color=CARD),
                  bw - 0.5, [left[0], left[1] - bh * 0.20, 0])
        self.play(Create(lb), run_time=0.6)
        self.play(FadeIn(lt), FadeIn(lq), run_time=0.5)

        # the COMPUTED box — ink outline on cream, because the sky owns it
        rb = RoundedRectangle(width=bw, height=bh, corner_radius=0.14,
                              color=INK, fill_color=CARD, fill_opacity=1.0,
                              stroke_width=P(4, 3)).move_to(right)
        rt = _fit(_t("COMPUTED", size=P(22, 18), color=INK, weight="BOLD"),
                  bw - 0.5, [right[0], right[1] + bh * 0.22, 0])
        rq = _fit(_t("where does it go?", size=P(26, 21), color=INK),
                  bw - 0.5, [right[0], right[1] - bh * 0.20, 0])
        self.play(Create(rb), run_time=0.6)
        self.play(FadeIn(rt), FadeIn(rq), run_time=0.5)

        if PORTRAIT:
            arr = _arrow([0, left[1] - bh / 2 - 0.10, 0],
                         [0, right[1] + bh / 2 + 0.10, 0], color=INK)
        else:
            arr = _arrow([left[0] + bw / 2 + 0.10, left[1], 0],
                         [right[0] - bw / 2 - 0.10, right[1], 0], color=INK)
        self.play(GrowArrow(arr), run_time=0.5)
        stop = _fit(_t("the terracotta stops here", size=P(18, 14), color=SOFT),
                    P(2.40, 1.55))
        stop.move_to(P([0, 0.88, 0], [0.95, (left[1] + right[1]) / 2, 0]))
        self.play(FadeIn(stop), run_time=0.4)

        # one fitted track, then the cloud of orbits the data still permits
        ox, oy = P(-3.60, -1.40), P(-0.55, -1.30)
        span = P(7.2, 3.10)
        base = Line([ox, oy, 0], [ox + span, oy + P(0.55, 0.42), 0],
                    color=INK, stroke_width=P(5, 4))
        self.play(Create(base), run_time=0.5)
        rng = np.random.default_rng(31)
        fan = VGroup()
        for k in _kclip(rng, 22):
            fan.add(Line([ox, oy, 0],
                         [ox + span,
                          oy + P(0.55, 0.42) + k * P(0.46, 0.34), 0],
                         color=ACC, stroke_width=P(2.2, 1.8)))
        self.play(LaggedStart(*[Create(l) for l in fan], lag_ratio=0.035),
                  run_time=0.9)
        fl = _fit(_t("every orbit the data still allows", size=P(20, 15), color=SOFT),
                  P(5.4, 3.34))
        fl.move_to([ox + span * P(0.52, 0.50), oy - P(0.82, 0.72), 0])
        self.play(FadeIn(fl), run_time=0.4)

        closer(self, "it never computes a risk", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — THE NUMBER WENT UP   (PUBLISHED record, rebuilt per REBUILD LAW)
# ═════════════════════════════════════════════════════════════════════════════
class B07_TheNumberWentUp(Paced):
    BEAT, RT, HOLD = "B07", 1.542, 0.0

    # the published Sentry record for 2024 YR4 (PMC12963224, Table 1):
    # days after discovery (27 Dec 2024) -> Earth impact probability, per cent
    TRACK = [(2, 0.6, "29 Dec"), (12, 1.8, "8 Jan"), (26, 1.1, "22 Jan"),
             (53, 3.1, "18 Feb"), (55, 0.9, "20 Feb"), (58, 0.05, "23 Feb")]

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Five days from record high to zero",
               cite="2024 YR4 · found by ATLAS Río Hurtado 27 Dec 2024 · 60 ± 7 m (JWST) · Sentry record")

        x0, x1 = P(-5.30, -1.55), P(1.60, 1.55)
        y0, y1 = P(-1.55, -1.35), P(2.20, 2.35)
        pmax = 3.4

        def X(day):
            return x0 + (day / 60.0) * (x1 - x0)

        def Y(p):
            return y0 + (p / pmax) * (y1 - y0)

        axes = VGroup(Line([x0, y0, 0], [x1, y0, 0], color=INK, stroke_width=3),
                      Line([x0, y0, 0], [x0, y1, 0], color=INK, stroke_width=3))
        self.play(Create(axes), run_time=0.55)
        grid = VGroup()
        for p in (1.0, 2.0, 3.0):
            grid.add(Line([x0, Y(p), 0], [x1, Y(p), 0], color=RULE, stroke_width=1.6))
        self.play(Create(grid), run_time=0.4)
        # LANDSCAPE ONLY. Rotated 90 degrees this label is 1.4 units TALL and
        # 0.2 wide, so in portrait it must sit hard against x = -1.95 and
        # crosses it. Ep. 07's B07 hit the identical defect.
        if not PORTRAIT:
            yl = _fit(_t("chance of impact", size=19, color=SOFT), 3.0)
            yl.rotate(PI / 2).move_to([x0 - 0.42, (y0 + y1) / 2, 0])
            self.play(FadeIn(yl), run_time=0.3)

        pts = [[X(d), Y(p), 0] for d, p, _ in self.TRACK]
        # the climb
        self.play(Create(VMobject().set_points_as_corners(pts[:4])
                         .set_stroke(ACC, width=P(6, 5))), run_time=0.9)
        dots = VGroup(*[Dot(point=q, radius=P(0.10, 0.08), color=ACC)
                        for q in pts[:4]])
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.2),
                  run_time=0.6)

        peak = _fit(_t("3.1%", size=P(46, 34), color=ACCT, weight="BOLD"), P(2.2, 1.4))
        peak.move_to([pts[3][0] + P(0.95, 0.00), pts[3][1] + P(0.10, 0.52), 0])
        self.play(FadeIn(peak, shift=UP * 0.10), run_time=0.5)
        self.play(Create(_underline(peak, buff=0.10)), run_time=0.3)

        # x1 is the plot's right edge; the chip must clear it entirely or it
        # lands on the very curve it annotates (GATE B: label on a curve).
        chip = _chip("Torino 3 — only Apophis ever matched it", size=P(21, 16),
                     max_w=P(3.90, 2.30))
        chip.move_to([P(3.95, -0.80), P(0.55, -1.80), 0])
        self.play(FadeIn(chip), run_time=0.5)

        # the collapse
        self.play(Create(VMobject().set_points_as_corners(pts[3:])
                         .set_stroke(INK, width=P(6, 5))), run_time=0.7)
        zero = _fit(_t("below 0.1%", size=P(26, 20), color=INK, weight="BOLD"),
                    P(2.6, 1.7))
        zero.move_to([pts[-1][0] - P(0.10, 0.15), Y(0.0) - P(0.42, 0.30), 0])
        self.play(FadeIn(zero), run_time=0.45)

        closer(self, "nobody made a mistake", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — WHY IT HAD TO   (COMPUTED HERE — the episode's central claim)
# ═════════════════════════════════════════════════════════════════════════════
class B08_WhyItHadTo(Paced):
    BEAT, RT, HOLD = "B08", 1.55, 0.325

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Why it had to go up first",
               cite="target-plane quadrature, computed in this reel · peak at σ = d/√2, asserted by the script")

        if PORTRAIT:
            bw, bat = 3.42, [0, 1.72, 0]
            cw, cat = 3.42, [0, -0.42, 0]
        else:
            bw, bat = 6.30, [-2.95, 0.62, 0]
            cw, cat = 5.10, [3.25, 0.55, 0]

        bplane = _plate("bplane.png", bw, bat, frame=False)
        bh = _plate_h("bplane.png", bw)
        self.play(FadeIn(bplane), run_time=0.7)

        tags = ["in the core", "on the tail", "past the Earth"]
        third = bw / 3.0
        labs = VGroup()
        for i, nm in enumerate(tags):
            lb = _fit(_t(nm, size=P(20, 15), color=SOFT), third - P(0.24, 0.10))
            lb.move_to([bat[0] - bw / 2 + third * (i + 0.5),
                        bat[1] - bh / 2 - P(0.28, 0.20), 0])
            labs.add(lb)
        self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.2),
                  run_time=0.7)

        key = _fit(_t("terracotta = the uncertainty · ink = the Earth, to scale",
                      size=P(17, 13), color=SOFT), P(6.2, 3.40))
        key.move_to([bat[0], bat[1] - bh / 2 - P(0.62, 0.46), 0])
        self.play(FadeIn(key), run_time=0.35)

        curve = _plate("impactprob.png", cw, cat, frame=True)
        ch = _plate_h("impactprob.png", cw)
        self.play(FadeIn(curve), run_time=0.7)

        ax = _fit(_t("the region shrinks  →", size=P(19, 15), color=SOFT),
                  P(4.6, 3.30))
        ax.move_to([cat[0], cat[1] - ch / 2 - P(0.28, 0.22), 0])
        self.play(FadeIn(ax), run_time=0.35)
        # LANDSCAPE ONLY: stacked, the curve's top edge is exactly where the
        # b-plane's scale key sits, and the two overlapped by 77%. The curve
        # carries its own ink peak marker, so portrait loses only the word.
        if not PORTRAIT:
            pk = _fit(_t("the peak", size=20, color=INK, weight="BOLD"), 2.0)
            pk.move_to([cat[0] + cw * 0.14, cat[1] + ch / 2 + 0.26, 0])
            self.play(FadeIn(pk, shift=DOWN * 0.08), run_time=0.4)

        chip = _chip("computed in this reel, not redrawn", size=P(21, 17),
                     max_w=P(5.0, 3.34))
        chip.move_to([cat[0], cat[1] - ch / 2 - P(0.74, 0.60), 0])
        self.play(FadeIn(chip, shift=UP * 0.08), run_time=0.5)

        closer(self, "a rising number was never bad news", size=P(29, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — IT HAPPENED AGAIN
# ═════════════════════════════════════════════════════════════════════════════
class B09_Again(Paced):
    BEAT, RT, HOLD = "B09", 1.118, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Then the Moon",
               cite="lunar impact ruled out 5 Mar 2026, from JWST observations of 18 & 26 Feb 2026 (NASA)")

        moon_at = P([-3.15, 0.75, 0], [0, 1.62, 0])
        rmoon = P(0.95, 0.72)
        moon = Circle(radius=rmoon, color=INK, fill_color=INK,
                      fill_opacity=1.0, stroke_width=0).move_to(moon_at)
        self.play(GrowFromCenter(moon), run_time=0.6)
        ml = _fit(_t("the Moon", size=P(22, 18), color=SOFT), P(2.6, 2.2))
        ml.move_to([moon_at[0], moon_at[1] - rmoon - P(0.34, 0.28), 0])
        self.play(FadeIn(ml), run_time=0.35)

        # the same object, the same date, the same shrinking cloud
        rng = np.random.default_rng(77)
        fan = VGroup()
        y_hi = moon_at[1] + rmoon * 0.35
        for k in _kclip(rng, 26):
            fan.add(Line([moon_at[0] - P(2.15, 1.45), y_hi + k * P(0.66, 0.50), 0],
                         [moon_at[0] + P(2.15, 1.45), y_hi + k * P(0.22, 0.18), 0],
                         color=ACC, stroke_width=P(2.2, 1.8)))
        self.play(LaggedStart(*[Create(l) for l in fan], lag_ratio=0.03),
                  run_time=0.9)

        col_at = P([3.20, 1.50, 0], [0, -0.92, 0])
        col_w = P(4.40, 3.40)
        big = _fit(_t("4.3%", size=P(64, 44), color=ACCT, weight="BOLD"), col_w,
                   [col_at[0], col_at[1], 0])
        sub = _fit(_t("lunar impact, and it held for months",
                      size=P(20, 16), color=SOFT), col_w,
                   [col_at[0], col_at[1] - P(0.56, 0.44), 0])
        self.play(FadeIn(big, shift=UP * 0.10), run_time=0.55)
        self.play(FadeIn(sub), run_time=0.35)

        # PORTRAIT DROPS THE CHIP. Stacked, chip + "ruled out" pushed the last
        # line onto the closing line at 100% overlap. The chip is the one
        # element in this beat the narration never speaks.
        if not PORTRAIT:
            chip = _quiet_chip("same object · same date · same shape of story",
                               size=20, max_w=4.40)
            chip.move_to([col_at[0], col_at[1] - 1.22, 0])
            self.play(FadeIn(chip), run_time=0.5)

        self.play(Create(_strike(big, pad=0.14)), run_time=0.5)
        out = _fit(_t("ruled out — 5 March 2026, from Webb",
                      size=P(22, 17), color=INK, weight="BOLD"), col_w)
        out.move_to([col_at[0], col_at[1] - P(1.84, 1.05), 0])
        self.play(FadeIn(out, shift=UP * 0.08), run_time=0.5)

        closer(self, "the shape repeats because the geometry does", size=P(28, 21))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE DESIGN TELL
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    BEAT, RT, HOLD = "B10", 1.274, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The design tell",
               cite="~40% of the ≥140 m population catalogued against a 90% mandate; NEO Surveyor closes it")

        cw, ch = P(6.10, 3.30), P(2.85, 2.30)
        cc = P([-2.95, 0.85, 0], [0, 1.30, 0])
        self.play(Create(_card(cw, ch, cc)), run_time=0.65)
        head = _fit(_t("WHAT IS ACTUALLY AUTOMATED", size=P(24, 19), color=ACCT,
                       weight="BOLD"), cw - 0.7, [cc[0], cc[1] + ch * 0.33, 0])
        self.play(FadeIn(head), run_time=0.45)
        self.play(Create(Line([cc[0] - cw * 0.40, cc[1] + ch * 0.19, 0],
                              [cc[0] + cw * 0.40, cc[1] + ch * 0.19, 0],
                              color=RULE, stroke_width=2)), run_time=0.3)

        r1 = _fit(_t("is this dot real?", size=P(28, 22), color=ACCT,
                     weight="BOLD"), cw - 1.0, [cc[0], cc[1] - ch * 0.02, 0])
        self.play(FadeIn(r1, shift=UP * 0.08), run_time=0.45)
        box = Rectangle(width=min(float(r1.width) + 0.44, cw - 0.6),
                        height=float(r1.height) + 0.34, color=ACC,
                        stroke_width=P(4, 3), fill_opacity=0).move_to(r1)
        self.play(Create(box), run_time=0.45)

        r2 = _fit(_t("should you move?", size=P(28, 22)), cw - 1.0,
                  [cc[0], cc[1] - ch * 0.30, 0])
        self.play(FadeIn(r2), run_time=0.45)
        self.play(Create(_strike(r2, pad=0.12)), run_time=0.45)

        # PORTRAIT DROPS THE COMPLETENESS PLATE. Card + plate + counter
        # stacked put three separate pairs of labels on top of each other
        # (three GATE B errors). The plate is on-screen-only evidence that the
        # narration never speaks, so dropping it keeps every SPOKEN item
        # visible - which is the right way to choose what portrait loses.
        if not PORTRAIT:
            pw = 4.60
            pat = [3.35, 0.95, 0]
            plate = _plate("completeness.png", pw, pat, frame=True)
            ph = _plate_h("completeness.png", pw)
            self.play(FadeIn(plate), run_time=0.65)

            third = pw / 3.0
            cls = VGroup()
            for i, nm in enumerate(["1 km", "140 m", "30 m"]):
                lb = _fit(_t(nm, size=20, color=SOFT), third - 0.20)
                lb.move_to([pat[0] - pw / 2 + third * (i + 0.5),
                            pat[1] - ph / 2 - 0.26, 0])
                cls.add(lb)
            self.play(LaggedStart(*[FadeIn(l) for l in cls], lag_ratio=0.18),
                      run_time=0.6)
            cap = _fit(_t("catalogued, by size class — the rule is the 90% target",
                          size=17, color=SOFT), 4.80)
            cap.move_to([pat[0], pat[1] - ph / 2 - 0.58, 0])
            self.play(FadeIn(cap), run_time=0.35)

        n_at = P([-2.95, -1.55, 0], [0, -0.55, 0])
        n = _fit(_t("11", size=P(54, 40), color=ACCT, weight="BOLD"), P(1.6, 1.2))
        n.move_to(n_at)
        nl = _fit(_t("caught before impact, ever", size=P(20, 16), color=SOFT),
                  P(4.6, 3.30))
        nl.move_to([n_at[0] + P(1.85, 0.0), n_at[1] + P(0.0, -0.52), 0])
        self.play(FadeIn(n, shift=UP * 0.10), run_time=0.5)
        self.play(FadeIn(nl), run_time=0.35)

        closer(self, "the search is the unfinished part", size=P(29, 22))
        self.hold_to_beat()
