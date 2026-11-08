"""scenes.py - Manim scenes for predictive-adaptive-optics.

*Aim Where It's Going.* - ai-explainer, claude-hai, Ep. 16.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL
  Terracotta marks THE SUBJECT OF EACH BEAT - the thing being examined. Ink
  marks the FIXED REFERENCE it is measured against.

    B03  the wavefront the mirror HOLDS   against the one that is really there
    B04  the full-phase lag error         against the part inside the band
    B06  prediction from the PAST         against the spatial and both bars
    B07  one layer                        against three
    B08  the servo-lag slice              against everything untouchable

  The load-bearing moment is B03, where two copies of the SAME cut sit 1.7 cm
  apart - nothing about the air differs, only when it was looked at. The
  mapping never flips, so B03 teaches it once and every later plate reads
  for free.

THIS FILE IS ASPECT-AWARE - IT RENDERS BOTH CUTS
  The reel ships in 16:9 (3840x2160) and 9:16 (2160x3840). Manim keeps
  frame_height = 8.0 in both, so the VERTICAL band plan is identical either
  way; only the horizontal extent changes - x +-6.15 landscape, x +-1.80
  portrait. Portrait is NOT a crop: it carries fewer elements, larger. The
  rule for choosing what goes: anything the narration SPEAKS stays, and the
  on-screen-only extras are what portrait loses.

LAYOUT BAND PLAN (every scene obeys it - this is what keeps the gates green)
                        landscape      portrait
  title                   +3.02          +3.14
  hairline                +2.66          +2.84
  the figure       +2.40 .. -1.90   +2.62 .. -2.02
  the closing line        -2.50          -2.42   (terracotta rule 0.28 below)
  the citation            -3.20          -2.95
  the wordmark bug        -3.12          -3.28   (right-anchored, LOGO LAW)

PLATES
  Every plate comes from assets/gen_ao.py, which runs the REAL calculation:
  von Karman phase screens synthesised by FFT, blown across an 8 m pupil
  under Taylor frozen flow, projected onto 60 Zernike modes, and handed to
  ridge predictors whose lambda is chosen on a held-out VALIDATION split and
  scored once on held-out TEST atmospheres.

  The headline servo-lag numbers are integrated EXACTLY off the spectrum
  rather than measured on the pixel grid, because a 1 ms lag at 10 m/s is
  half a pixel at 2 cm sampling - and half a pixel is where Nyquist
  truncation costs 8%. The screens then reproduce that integral to 2%, which
  is the independent check.

  EIGHT claims are ASSERTED and the generator writes nothing if any fails.

  TWO MEASURED RESULTS ARE DELIBERATELY NOT CLAIMED ON SCREEN. The in-band
  SHARE of total phase variance (~79%) swings with realisation, because a
  single screen's lowest modes scatter hard; only the 16% DRIFT share is
  stable enough to show. And the pure-Kolmogorov lag curve was dropped from
  lawlog.png - it sat exactly on top of the von Karman one and left the
  gap connector's top end ambiguous.

  A PLATE WAS REDRAWN TWICE. slide.png began as a full-bleed greyscale patch
  of turbulence with two boxes on it: its scale rules fell off the bottom
  edge, and a frame that is mostly mid-grey is the exact shape that failed
  GATE V on Ep. 15's B04. The second version added the residual at x10 and it
  overflowed its band through the rules. What ships is two line cuts, and the
  scale rules moved OUT of the plate into Manim - see B03.

PLATE GEOMETRY - ph = pw * (ih/iw). Do this arithmetic, do not assume it.
      slide   1560x470  0.3013
      lawlog  1560x780  0.5000     decomp  1560x780  0.5000
      noise   1560x780  0.5000     budget  1560x780  0.5000
  The landscape figure band is 4.30 units tall. The 0.50 plates run at
  pw 6.6 (3.30 tall) where nothing sits under them, and pw 6.2 (3.10) on
  B06 and B08, which need a label row beneath the plate.

GATE NOTES (learned the expensive way on Eps. 03-15)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - Never position a label from another Text's .width either - same reason.
    Ep. 15's _swatch_row did exactly that and GATE A caught x = 6.6 on a
    +-6.15 frame. Position from the CONTAINER.
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - A plate's IMAGE is invisible to GATE B, but its FRAME is a Rectangle and
    therefore a curve. So a label crossing a plate's OUTLINE is caught and a
    label inside it is not. EVERY landscape plate beat with a right-hand
    column puts its plate at x = -1.10, so the plate's right edge clears the
    column (2.52..5.96) by at least 0.32.
  - NEVER write `pat[0] +- pw * k` for a label OUTSIDE a plate. In landscape
    pw = 6.6 inside a 12.3-unit frame and it is fine; in portrait pw = 3.4
    and the same expression lands outside a 3.6-unit frame.
  - NEVER use a glyph outside the font's coverage. EB Garamond has no "check"
    character and Ep. 09 rendered it as stray digits on screen.
  - Leave >= 0.15 units between any two elements. A gap of 0.04 is eleven
    pixels at 4K and reads as contact.
  - Give every scene its footer EARLY. GATE V samples each beat at 50% and
    85%, and Ep. 11's B01 read 44% underfill because its footer landed last.
  - Same-colour-on-same-colour is invisible to EVERY gate. Ep. 14's B08 drew
    a terracotta span arrow on top of a terracotta bar and only the
    arrowheads showed. Read the frames.
  - Prefer SOFT over GHOST for any LARGE field of marks. Ep. 15's B09 passed
    GATE V in 16:9 and failed in 9:16 at 0.26, because portrait dropped the
    dark text that was carrying the contrast mean. A margin that depends on
    elements portrait drops is not a margin.
  - FadeOut takes a plate's frame with it; give the replacement one too.
  - Check BOTH aspects. Portrait failed GATE B 8/10 on Ep. 08's first pass.
  - Pacing: a scene landing above -0.15 s is floored; lower its RT. At the
    1.55 RT cap the remaining lever is HOLD. A scene whose portrait branch
    plays FEWER reveals needs RT_PORTRAIT - see the chassis note.
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
BG = ManimColor("#F2F0E9")
INK = ManimColor("#3D3929")
SOFT = ManimColor("#6E6A57")
GHOST = ManimColor("#B9B4A0")
ACC = ManimColor("#D97757")
ACCT = ManimColor("#A44A32")
CARD = ManimColor("#FFFFFF")
RULE = ManimColor("#D9D4C4")

# ── The aspect switch ────────────────────────────────────────────────────────
# Manim CE takes pixel dimensions from `-r W,H` but does NOT recompute
# frame_width, so a portrait render would otherwise keep the 16:9 default of
# 14.22 units and lay every scene out at a third of its intended size. Keep
# frame_height at 8.0 and derive frame_width from the real pixel aspect.
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
    """Struck-through rule, centred on the X-HEIGHT. `_qc_intentional` exempts
    it from GATE B's TEXT-ON-CURVE rule, which is what that hook exists for.

    WHY NOT `m.get_center()`. That is the centre of the GLYPH BOUNDING BOX,
    which rises with ascenders and falls with descenders -- so where the rule
    lands depends on which letters the words happen to contain. B01's
    "where the answer came from" has ascenders (h, t, f) and NO descenders at
    all, so its bbox centre sat near the TOP of the lowercase letters and the
    rule struck through their heads instead of their middles. B10's
    "a messier sky should break it" has a descender (y) and looked correct,
    which is exactly why the bug survived a frame-by-frame pre-flight: it is
    invisible on any string that happens to descend.

    The MEDIAN glyph top and bottom recover the x-height band itself. Most
    glyphs in a line of lower-case text are x-height, so the median top IS the
    x-height line and the median bottom IS the baseline, whatever the handful
    of ascenders do. Spaces carry no points and drop out on their own.
    """
    ln = Line(LEFT, RIGHT, color=color, stroke_width=sw)
    ln.set_width(max(float(m.width) + pad * 2, 0.4))
    glyphs = [g for g in m.family_members_with_points()]
    if glyphs:
        tops = sorted(g.get_top()[1] for g in glyphs)
        bots = sorted(g.get_bottom()[1] for g in glyphs)
        k = len(tops) // 2
        y = (tops[k] + bots[k]) / 2.0
    else:
        y = m.get_center()[1]
    ln.move_to([m.get_center()[0], y, 0])
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
    """A plate, framed like a figure in a paper.

    Returns a `Group`: ImageMobject is not a VMobject. Falls back to a blank
    plate if the asset is missing so a scene can never fail to render.
    """
    path = PLOTS / name
    parts = []
    hh = w * (780.0 / 1560.0)
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
        return w * 780.0 / 1560.0


def _swatch_row(text, col, at, w, size=18, val=None, sw_h=0.16):
    """A colour swatch with its label, centred on `at`, fitted to `w`.

    STUB-SAFE. The label is positioned from the CONTAINER, never from its own
    measured width: under GATE A's geometry stub a Text has no width, and
    Ep. 15's first version put this at x = 6.6 on a +-6.15 frame.
    """
    sw = Rectangle(width=0.34, height=sw_h, color=col, fill_color=col,
                   fill_opacity=1.0, stroke_width=0)
    sw.move_to([at[0] - w / 2.0 + 0.17, at[1], 0])
    lab = _t(text, size=size, color=INK)
    inner = w - 0.46
    if val is None:
        _fit(lab, inner)
        lab.move_to([at[0] + 0.11, at[1], 0])
        return VGroup(sw, lab)
    v = _t(val, size=size, color=ACCT, weight="BOLD")
    _fit(lab, inner * 0.62)
    _fit(v, inner * 0.34)
    lab.move_to([at[0] - w / 2.0 + 0.46 + inner * 0.31, at[1], 0])
    v.move_to([at[0] + w / 2.0 - inner * 0.17, at[1], 0])
    return VGroup(sw, lab, v)


# ── Pacing: the scene fits the narration, not the other way round ────────────
def _beat_seconds():
    try:
        import json
        d = json.loads((HERE / "beat_sheet.json").read_text(encoding="utf-8"))
        return {b["beat_id"]: float(b.get("actual_duration_s") or 0)
                for b in d.get("beats", [])}
    except Exception:
        return {}


BEAT_SECONDS = _beat_seconds()

TAIL_TRIM = 0.18


class Paced(Scene):
    """A Scene that paces itself to its beat's measured narration."""

    BEAT = None
    RT = 1.0             # run_time multiplier
    RT_PORTRAIT = None   # None means "use RT in both aspects"
    HOLD = 0.0           # rest after each reveal
    _raw = False

    # WHY RT_PORTRAIT EXISTS.
    # The pacing solve runs ONCE, in landscape, and writes the RT/HOLD line.
    # A scene whose portrait branch plays FEWER reveals then underfills its
    # beat: the body is shorter, hold_to_beat floors the difference, and the
    # clip sits on a frozen last frame for the remainder. Undershoot is safe
    # -- compile.py pads a short clip with a held frame, where a LONG clip
    # would be centre-cut and lose its closing line -- but a scene that
    # freezes for 5 s of a 14 s beat is dead air, not pacing.
    #
    # So scenes that drop on-screen-only extras in portrait carry a second,
    # larger RT for that aspect. It is a separate class attribute and NOT part
    # of the `BEAT, RT, HOLD = ...` line, so the pacing solver's regex still
    # finds and rewrites the canonical line without clobbering this one.

    @property
    def _rt(self):
        if PORTRAIT and self.RT_PORTRAIT:
            return float(self.RT_PORTRAIT)
        return float(self.RT)

    def play(self, *args, **kwargs):
        if self._raw:                      # re-entry from Scene.wait()
            return Scene.play(self, *args, **kwargs)
        kwargs["run_time"] = float(kwargs.get("run_time", 1.0)) * self._rt
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
        holding its last frame, which is invisible; a clip LONGER than its
        beat is centre-cut, which would clip the closing line off both ends.
        The target carries a TAIL_TRIM safety margin because renderer.time
        under-reports the true rendered length - each play's frame count
        rounds up and the error accumulates with the number of reveals.

        The lever is always RT. A per-scene trim override was built and tried
        on four scenes across two episodes and moved the measured duration by
        exactly zero every time, because `target - trim - now` was already
        below the floor in all four.
        """
        target = BEAT_SECONDS.get(self.BEAT or "", 0.0)
        now = float(getattr(getattr(self, "renderer", None), "time", 0.0) or 0.0)
        self.wait(max(floor, target - TAIL_TRIM - now) if target else floor)


# ─────────────────────────────────────────────────────────────────────────────
#  Plate placement and plate-internal coordinates
# ─────────────────────────────────────────────────────────────────────────────
PLATE_X = -1.10        # every landscape plate that has a right-hand column
RCOL_X = 4.24          # centre of that column
RCOL_W = 3.44          # and its width: it spans x 2.52 .. 5.96

# Plate-internal x positions, DERIVED from gen_ao.py's own geometry, not
# guessed. Axes() insets its box by 26 px on a 1560-wide plate, so a data x
# maps to plate fraction 26/1560 + (1508/1560) * (x - a) / (b - a), and the
# offset from the plate CENTRE is that fraction minus 0.5, in units of pw.
#
# lawlog.png: log10 x from log10(0.85) to log10(14.0).
LAW_TAU2_FX = -0.1881        # the 2 ms gap connector
LAW_TAU0_FX = +0.1074        # the 4.71 ms coherence-time rule
#
# noise.png: log10 x from log10(0.004) to log10(0.26).
NOISE_REAL_FX = +0.1015      # the dashed rule at 0.05 rad RMS per mode
#
# decomp.png: two bar groups at axis x 0.255 and 0.745.
DECOMP_GROUP_FX = (-0.2370, +0.2380)
#
# budget.png: two stacked bars at axis x 0.30 and 0.70.
BUDGET_BAR_FX = (-0.1930, +0.1930)
#
# All of these are safely INSIDE the plate (|f| < 0.5), which is what makes
# the `pw * k` form legal here. The form that is NOT legal is a label placed
# OUTSIDE a plate by a pw-scaled offset.

# ── Numbers the scenes put on screen ─────────────────────────────────────────
# Every one is printed by assets/gen_ao.py, kept here as named constants so a
# changed experiment cannot silently disagree with a label.
KECK_DELAY = "1.7 ms"          # PUBLISHED: Keck II PyWFS, measured
KECK_RATE = "1 kHz"            # PUBLISHED
WIND_TXT = "10 m/s"            # stated simulation parameter
SLIDE_TXT = "1.7 cm"           # COMPUTED: 10 m/s x 1.7 ms
R0_TXT = "15 cm"               # stated simulation parameter
TAU0_TXT = "4.71 ms"           # COMPUTED: 0.314 r0 / v
EXPONENT = "1.666667"          # COMPUTED: fitted, vs 5/3
BAND_PCT = "16%"               # COMPUTED: in-band share of the lag error
G_CLEAN = "331x"               # COMPUTED: 1 layer, no sensor noise
G_CLEAN3 = "183x"              # COMPUTED: 3 layers, no sensor noise
G_REAL = "11.2x"               # COMPUTED: 1 layer, 0.05 rad RMS per mode
G_REAL3 = "4.8x"               # COMPUTED: 3 layers, same noise
G_TIME = "5.1x"                # COMPUTED: temporal only
G_SPACE = "1.2x"               # COMPUTED: spatial only
LAG_SHARE = "22%"              # COMPUTED: implied lag share of the budget
KECK_TOTAL = "20%"             # PUBLISHED: Keck on-sky SH-WFS residuals
KECK_CONTRAST = "2.03x"        # PUBLISHED: vortex coronagraph, 3 lambda/D
TAPS_TXT = "24 frames"         # the predictor's history


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — THE PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 1.094, 0.000

    def construct(self):
        self.camera.background_color = BG
        hair = Line([-(X_MAX - 0.10), HAIR_Y, 0], [X_MAX - 0.10, HAIR_Y, 0],
                    color=RULE, stroke_width=2.4)
        top = _fit(_t("AI in Astronomy & Space Science  ·  Ep. 16",
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
        self.play(Create(_underline(name, color=ACC, sw=6, buff=0.18)),
                  run_time=0.45)
        role = _fit(_t("Humanitarians AI  ·  presenter", size=P(26, 20),
                       color=SOFT), P(5.2, 3.30))
        role.move_to([name_at[0], name_at[1] - P(0.86, 0.78), 0])
        self.play(FadeIn(role), run_time=0.5)

        card_at = P([3.10, 1.06, 0], [0, -0.44, 0])
        card = _card(P(5.5, 3.40), P(2.50, 2.30), card_at)
        self.play(Create(card), run_time=0.6)

        r1 = _fit(_t("fifteen episodes", size=P(28, 23), color=SOFT),
                  P(4.9, 3.00))
        r1.move_to([card_at[0], card_at[1] + P(0.80, 0.74), 0])
        r1b = _fit(_t("where the answer came from", size=P(23, 19), color=SOFT),
                   P(4.9, 3.00))
        r1b.move_to([card_at[0], card_at[1] + P(0.38, 0.34), 0])
        self.play(FadeIn(r1), run_time=0.45)
        self.play(FadeIn(r1b), run_time=0.4)
        self.play(Create(_strike(r1b, color=ACC, sw=4)), run_time=0.4)

        r2 = _fit(_t("this one", size=P(28, 23), color=ACCT, weight="BOLD"),
                  P(4.9, 3.00))
        r2.move_to([card_at[0], card_at[1] - P(0.30, 0.30), 0])
        r2b = _fit(_t("the answer is due early", size=P(23, 19), color=INK),
                   P(4.9, 3.00))
        r2b.move_to([card_at[0], card_at[1] - P(0.72, 0.70), 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)
        self.play(Create(SurroundingRectangle(VGroup(r2, r2b), color=ACC,
                                              buff=0.18, stroke_width=3,
                                              corner_radius=0.10)),
                  run_time=0.5)

        ser = _fit(_t("Ep. 16  ·  adaptive optics", size=P(23, 18), color=ACCT),
                   P(6.0, 3.34))
        ser.move_to([0, P(-2.34, -2.44), 0])
        self.play(FadeIn(ser), run_time=0.5)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — THE WHOLE IDEA, IN ONE BREATH
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.550, 0.312

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The Whole Idea")

        card = _card(P(10.6, 3.46), P(4.10, 4.30), [0, P(0.42, 0.34), 0])
        self.play(Create(card), run_time=0.7)

        rows = [
            ("MEASURE THE AIR, BEND THE MIRROR",
             "two milliseconds, round trip", INK, False),
            ("THE AIR DOES NOT WAIT",
             "the correction lands on air that moved", INK, False),
            ("SO AIM AHEAD, NOT AT",
             "predict the frame that has not arrived", ACCT, True),
        ]
        ys = [P(1.62, 1.72), P(0.42, 0.34), P(-0.80, -1.02)]
        for (head, sub, col, accent), y in zip(rows, ys):
            h = _fit(_t(head, size=P(31, 23), color=col,
                        weight="BOLD" if accent else None), P(9.6, 3.14))
            h.move_to([0, y + P(0.26, 0.24), 0])
            s = _fit(_t(sub, size=P(22, 17), color=SOFT), P(9.6, 3.14))
            s.move_to([0, y - P(0.24, 0.22), 0])
            self.play(FadeIn(h, shift=UP * 0.08), run_time=0.6)
            self.play(FadeIn(s), run_time=0.45)
            if accent:
                self.play(Create(_underline(h, color=ACC, sw=5, buff=0.10)),
                          run_time=0.45)

        closer(self, "before the light is recorded", cx=0.0)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE DELAY IS A DISTANCE
# ═════════════════════════════════════════════════════════════════════════════
class B03_TheDistance(Paced):
    BEAT, RT, HOLD = "B03", 1.550, 0.089
    RT_PORTRAIT = 1.798   # portrait plays 11 reveals, not 13

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Late Means Displaced",
               "Delay: Keck II PyWFS, measured on sky.  Cut: von Karman screen, r0 15 cm.")

        pw = P(6.6, 3.44)
        ph = _plate_h("slide.png", pw)
        px = P(PLATE_X, 0.0)
        ptop = P(2.30, 2.52)
        pat = [px, ptop - ph / 2.0, 0]
        plate = _plate("slide.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        # the two cuts, named OUTSIDE the plate
        if PORTRAIT:
            rows = [("the air now", INK), ("what the mirror holds", ACC)]
            ry = [0.92, 0.46]
            for (txt, col), y in zip(rows, ry):
                self.play(FadeIn(_swatch_row(txt, col, [0, y, 0], 3.40,
                                             size=19)), run_time=0.55)
        else:
            self.play(FadeIn(_swatch_row("the air now", INK,
                                         [RCOL_X, 1.86, 0], RCOL_W, size=21)),
                      run_time=0.55)
            self.play(FadeIn(_swatch_row("what the mirror holds", ACC,
                                         [RCOL_X, 1.30, 0], RCOL_W, size=21)),
                      run_time=0.55)
            # chip block sits LOW, not under the swatches. Up at y 0.62 it
            # left the whole bottom-right quadrant empty while the scale
            # rules ran along the left -- a FILL-THE-CANVAS defect that
            # every gate passes and only a rendered frame shows.
            chip = _chip(KECK_RATE + "  ·  " + KECK_DELAY, size=19,
                         max_w=RCOL_W)
            chip.move_to([RCOL_X, -0.52, 0])
            self.play(FadeIn(chip), run_time=0.5)
            note = _fit(_t("PUBLISHED  ·  Keck II", size=16, color=SOFT),
                        RCOL_W)
            note.move_to([RCOL_X, -0.98, 0])
            self.play(FadeIn(note), run_time=0.4)

        # the two scale rules, as Manim, so every gate can see them
        lx = P(-5.20, -1.58)
        r0_len = P(4.20, 2.30)
        sl_len = r0_len * (1.7 / 15.0)
        ry0, ry1 = P(-0.50, -0.26), P(-1.40, -1.20)
        lab_dy = P(0.0, -0.40)

        for y, length, col, txt, size in (
                (ry0, r0_len, INK, "r\u2080 = " + R0_TXT + "   one coherence cell",
                 P(22, 18)),
                (ry1, sl_len, ACC, SLIDE_TXT + "   the slide in one delay",
                 P(22, 18))):
            bar = Line([lx, y, 0], [lx + length, y, 0], color=col,
                       stroke_width=P(10, 9))
            cap = min(0.16, length * 0.34)
            c1 = Line([lx, y - cap, 0], [lx, y + cap, 0], color=col,
                      stroke_width=P(8, 7))
            c2 = Line([lx + length, y - cap, 0], [lx + length, y + cap, 0],
                      color=col, stroke_width=P(8, 7))
            lab = _fit(_t(txt, size=size, color=INK), P(4.4, 3.30))
            if PORTRAIT:
                lab.move_to([0, y + lab_dy, 0])
            else:
                lab.move_to([lx + length + 0.24 + lab.width / 2.0, y, 0])
            self.play(Create(VGroup(bar, c1, c2)), run_time=0.55)
            self.play(FadeIn(lab), run_time=0.45)

        closer(self, "same wavefront, wrong place")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — THE LAW, AND HOW LITTLE OF IT IS REACHABLE
# ═════════════════════════════════════════════════════════════════════════════
class B04_TheLaw(Paced):
    BEAT, RT, HOLD = "B04", 1.550, 0.410
    RT_PORTRAIT = 2.000   # portrait plays 8 reveals, not 11

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The Lag Is A Structure Function",
               "Integrated exactly from the von Karman spectrum; screens reproduce it to 2%.")

        pw = P(6.6, 3.44)
        ph = _plate_h("lawlog.png", pw)
        px = P(PLATE_X, 0.0)
        pat = [px, P(0.25, 1.00), 0]
        plate = _plate("lawlog.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        if PORTRAIT:
            rows = [("the whole wavefront", ACC, None),
                    ("what a mirror can shape", INK, BAND_PCT)]
            for (txt, col, val), y in zip(rows, (-0.92, -1.44)):
                self.play(FadeIn(_swatch_row(txt, col, [0, y, 0], 3.40,
                                             size=19, val=val)), run_time=0.6)
            lab = _fit(_t("coherence time " + TAU0_TXT + "  =  1 rad²",
                          size=19, color=SOFT), 3.44)
            lab.move_to([0, -1.92, 0])
            self.play(FadeIn(lab), run_time=0.5)
        else:
            self.play(FadeIn(_swatch_row("the whole wavefront", ACC,
                                         [RCOL_X, 1.92, 0], RCOL_W, size=21)),
                      run_time=0.6)
            self.play(FadeIn(_swatch_row("what a mirror can shape", INK,
                                         [RCOL_X, 1.36, 0], RCOL_W, size=21,
                                         val=BAND_PCT)), run_time=0.6)
            # The column runs down to -1.12 so it spans the plate instead of
            # crowding its top half and leaving the bottom-right empty.
            chip = _chip("exponent " + EXPONENT, size=19, max_w=RCOL_W)
            chip.move_to([RCOL_X, 0.50, 0])
            self.play(FadeIn(chip), run_time=0.5)
            n1 = _fit(_t("COMPUTED  ·  textbook 5/3", size=16, color=SOFT),
                      RCOL_W)
            n1.move_to([RCOL_X, 0.06, 0])
            self.play(FadeIn(n1), run_time=0.4)
            n2 = _fit(_t("coherence time " + TAU0_TXT, size=19, color=INK),
                      RCOL_W)
            n2.move_to([RCOL_X, -0.70, 0])
            n3 = _fit(_t("is where it costs 1 rad²", size=17, color=SOFT),
                      RCOL_W)
            n3.move_to([RCOL_X, -1.12, 0])
            self.play(FadeIn(n2), run_time=0.45)
            self.play(FadeIn(n3), run_time=0.4)

        closer(self, "most of it is out of reach")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — WHAT THE PREDICTOR ACTUALLY IS
# ═════════════════════════════════════════════════════════════════════════════
class B05_TheFilter(Paced):
    BEAT, RT, HOLD = "B05", 1.550, 0.067
    RT_PORTRAIT = None

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "One Linear Filter",
               "Ridge regression on 60 Zernike modes; lambda chosen on held-out atmospheres.")

        n = 24
        x0, x1 = P(-5.30, -1.60), P(1.20, 0.34)
        # ys sits LOW in BOTH aspects, for different reasons. In portrait a
        # higher row put the weight fan's caption through the title (GATE B
        # caught a 30% text-on-text overlap). In landscape the whole scene
        # sat in the top half and left everything below y = -0.5 empty --
        # a FILL-THE-CANVAS defect no gate tests. The fan now grows from the
        # lower third almost to the hairline.
        ys = P(-0.55, 0.10)
        tick_h = P(0.46, 0.38)
        bar_base, bar_h0, bar_h1 = P(0.54, 0.38), P(0.10, 0.08), P(1.85, 1.05)
        capx = P((x0 + x1) / 2.0, 0.0)     # captions centre on the FRAME in
        xs = np.linspace(x0, x1, n)        # portrait, not on the tick row
        ticks = VGroup(*[Line([x, ys - tick_h, 0], [x, ys + tick_h, 0],
                              color=SOFT, stroke_width=P(5, 4)) for x in xs])
        self.play(Create(ticks), run_time=1.0)

        lab = _fit(_t(TAPS_TXT + " of telemetry", size=P(23, 19), color=INK),
                   P(5.0, 3.30))
        lab.move_to([capx, ys - P(0.92, 0.86), 0])
        self.play(FadeIn(lab), run_time=0.5)

        # the weights: a fan that grows toward the newest frame
        w = np.linspace(0.10, 1.0, n) ** 1.6
        bars = VGroup(*[Rectangle(width=P(0.16, 0.058),
                                  height=bar_h0 + bar_h1 * float(v),
                                  color=ACC, fill_color=ACC, fill_opacity=1.0,
                                  stroke_width=0).move_to(
                            [x, ys + bar_base
                             + (bar_h0 + bar_h1 * float(v)) / 2.0, 0])
                        for x, v in zip(xs, w)])
        self.play(FadeIn(bars, shift=UP * 0.10), run_time=0.9)
        wl = _fit(_t("one weight each, fitted once", size=P(21, 17), color=SOFT),
                  P(5.0, 3.30))
        wl.move_to([capx, ys + P(2.77, 1.95), 0])
        self.play(FadeIn(wl), run_time=0.5)

        # the gap, and the frame that has not happened
        gx = P(3.95, 1.26)
        slot = Rectangle(width=P(0.44, 0.30), height=P(1.30, 0.80), color=ACC,
                         stroke_width=4, fill_color=ACC, fill_opacity=0.16)
        slot.move_to([gx, ys, 0])
        arr = Arrow(start=[x1 + 0.16, ys, 0], end=[gx - P(0.34, 0.22), ys, 0],
                    color=ACCT, stroke_width=5,
                    max_tip_length_to_length_ratio=0.16, buff=0.02)
        self.play(Create(arr), run_time=0.55)
        self.play(Create(slot), run_time=0.5)
        # In portrait this label CENTRES on the frame, it does not sit under
        # the slot: at x = gx it ran from -0.05 to 2.57 on a +-1.95 frame.
        # It also drops to ys - 1.30, because at -0.92 it collided with the
        # telemetry caption 0.18 above it.
        gl = _fit(_t("the frame that has not arrived", size=P(21, 17),
                     color=ACCT), P(3.6, 3.30))
        gl.move_to([0, ys - 1.50, 0] if PORTRAIT else [gx, ys + 1.30, 0])
        self.play(FadeIn(gl), run_time=0.5)
        dl = _fit(_t("2 ms", size=P(20, 17), color=SOFT), P(1.6, 1.0))
        dl.move_to([(x1 + gx) / 2.0, ys + P(0.52, 0.56), 0])
        self.play(FadeIn(dl), run_time=0.4)

        closer(self, "it learned the wind, not the physics")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — BACK IN TIME, OR ACROSS THE PUPIL
# ═════════════════════════════════════════════════════════════════════════════
class B06_BackOrAcross(Paced):
    BEAT, RT, HOLD = "B06", 1.550, 0.001
    RT_PORTRAIT = 1.759   # portrait plays 10 reveals, not 12

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Back, Or Across",
               "Gain over the zero-order hold at 2 ms, scored on held-out atmospheres.")

        pw = P(6.2, 3.44)
        ph = _plate_h("decomp.png", pw)
        px = P(PLATE_X, 0.0)
        pat = [px, P(0.45, 1.05), 0]
        plate = _plate("decomp.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        # group names UNDER the plate, at the measured group centres
        gy = pat[1] - ph / 2.0 - P(0.32, 0.30)
        for fx, txt in zip(DECOMP_GROUP_FX, ("one layer", "three layers")):
            g = _fit(_t(txt, size=P(21, 17), color=SOFT), P(2.4, 1.50))
            g.move_to([px + fx * pw, gy, 0])
            self.play(FadeIn(g), run_time=0.45)

        rows = (("ACROSS the pupil", SOFT, G_SPACE),
                ("BACK in time", ACC, G_TIME),
                ("both", INK, G_REAL))
        if PORTRAIT:
            for (txt, col, val), y in zip(rows, (-0.74, -1.20, -1.66)):
                self.play(FadeIn(_swatch_row(txt, col, [0, y, 0], 3.40,
                                             size=19, val=val)), run_time=0.6)
        else:
            for (txt, col, val), y in zip(rows, (1.74, 1.16, 0.58)):
                self.play(FadeIn(_swatch_row(txt, col, [RCOL_X, y, 0], RCOL_W,
                                             size=21, val=val)), run_time=0.6)
            n = _fit(_t("one frame, all 60 modes", size=16, color=SOFT), RCOL_W)
            n.move_to([RCOL_X, 0.12, 0])
            self.play(FadeIn(n), run_time=0.4)
            n2 = _fit(_t("vs 24 frames, one mode", size=16, color=SOFT), RCOL_W)
            n2.move_to([RCOL_X, -0.26, 0])
            self.play(FadeIn(n2), run_time=0.4)

        closer(self, "a still frame has no direction")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — WHAT ACTUALLY STOPS IT
# ═════════════════════════════════════════════════════════════════════════════
class B07_TheCeiling(Paced):
    BEAT, RT, HOLD = "B07", 1.550, 0.152
    RT_PORTRAIT = 1.878   # portrait plays 8 reveals, not 10

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The Sensor Is The Ceiling",
               "Measurement noise added to the predictor's inputs, not its targets.")

        pw = P(6.6, 3.44)
        ph = _plate_h("noise.png", pw)
        px = P(PLATE_X, 0.0)
        pat = [px, P(0.25, 1.00), 0]
        plate = _plate("noise.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        rows = (("one layer", ACC, G_REAL), ("three layers", INK, G_REAL3))
        if PORTRAIT:
            for (txt, col, val), y in zip(rows, (-0.92, -1.42)):
                self.play(FadeIn(_swatch_row(txt, col, [0, y, 0], 3.40,
                                             size=19, val=val)), run_time=0.6)
            lab = _fit(_t("at a realistic sensor", size=19, color=SOFT), 3.44)
            lab.move_to([0, -1.90, 0])
            self.play(FadeIn(lab), run_time=0.5)
        else:
            for (txt, col, val), y in zip(rows, (1.88, 1.30)):
                self.play(FadeIn(_swatch_row(txt, col, [RCOL_X, y, 0], RCOL_W,
                                             size=21, val=val)), run_time=0.6)
            chip = _chip("quiet sensor:  " + G_CLEAN, size=19, max_w=RCOL_W)
            chip.move_to([RCOL_X, 0.60, 0])
            self.play(FadeIn(chip), run_time=0.5)
            n = _fit(_t("COMPUTED  ·  the same filter", size=16, color=SOFT),
                     RCOL_W)
            n.move_to([RCOL_X, 0.16, 0])
            self.play(FadeIn(n), run_time=0.4)
            n2 = _fit(_t("noisier sensor to the right", size=17, color=INK),
                      RCOL_W)
            n2.move_to([RCOL_X, -0.46, 0])
            self.play(FadeIn(n2), run_time=0.45)

        closer(self, "the limit is the sensor, not the sky")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — THE ERROR BUDGET
# ═════════════════════════════════════════════════════════════════════════════
class B08_TheBudget(Paced):
    BEAT, RT, HOLD = "B08", 1.550, 0.024
    RT_PORTRAIT = 1.770   # portrait plays 10 reveals, not 12

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Crush A Fifth, Move A Fifth",
               "Keck II on-sky: 20% better Shack-Hartmann residuals vs a classic integrator.")

        pw = P(6.2, 3.44)
        ph = _plate_h("budget.png", pw)
        px = P(PLATE_X, 0.0)
        pat = [px, P(0.45, 1.05), 0]
        plate = _plate("budget.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        gy = pat[1] - ph / 2.0 - P(0.32, 0.30)
        for fx, txt in zip(BUDGET_BAR_FX, ("integrator", "predictor")):
            g = _fit(_t(txt, size=P(21, 17), color=SOFT), P(2.4, 1.50))
            g.move_to([px + fx * pw, gy, 0])
            self.play(FadeIn(g), run_time=0.45)

        rows = (("servo lag", ACC, LAG_SHARE),
                ("everything else", SOFT, None))
        if PORTRAIT:
            for (txt, col, val), y in zip(rows, (-0.74, -1.22)):
                self.play(FadeIn(_swatch_row(txt, col, [0, y, 0], 3.40,
                                             size=19, val=val)), run_time=0.6)
            lab = _fit(_t("total falls " + KECK_TOTAL, size=20, color=ACCT,
                          weight="BOLD"), 3.44)
            lab.move_to([0, -1.70, 0])
            self.play(FadeIn(lab), run_time=0.5)
        else:
            for (txt, col, val), y in zip(rows, (1.74, 1.16)):
                self.play(FadeIn(_swatch_row(txt, col, [RCOL_X, y, 0], RCOL_W,
                                             size=21, val=val)), run_time=0.6)
            n = _fit(_t("fitting error, noise, vibration", size=16, color=SOFT),
                     RCOL_W)
            n.move_to([RCOL_X, 0.74, 0])
            self.play(FadeIn(n), run_time=0.4)
            chip = _chip("total falls " + KECK_TOTAL, size=19, max_w=RCOL_W)
            chip.move_to([RCOL_X, 0.14, 0])
            self.play(FadeIn(chip), run_time=0.5)
            n2 = _fit(_t("PUBLISHED  ·  Keck II, on sky", size=16, color=SOFT),
                      RCOL_W)
            n2.move_to([RCOL_X, -0.30, 0])
            self.play(FadeIn(n2), run_time=0.4)

        closer(self, "a big win on a small slice")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — ON SKY, FOR REAL
# ═════════════════════════════════════════════════════════════════════════════
class B09_OnSky(Paced):
    BEAT, RT, HOLD = "B09", 1.550, 0.107
    RT_PORTRAIT = None

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What It Bought On Sky",
               "Both rows PUBLISHED: Keck II adaptive optics bench, NIRC2.")

        card_w, card_h = P(10.4, 3.46), P(1.56, 1.62)
        ys = (P(1.52, 1.78), P(-0.34, -0.26))
        rows = (
            ("2021  ·  vortex coronagraph",
             "contrast  " + KECK_CONTRAST + "  close in", ACC),
            ("2026  ·  Brackett gamma",
             "Strehl and contrast  comparable", INK),
        )
        for (head, body, col), y in zip(rows, ys):
            card = _card(card_w, card_h, [0, y, 0])
            self.play(Create(card), run_time=0.6)
            h = _fit(_t(head, size=P(23, 18), color=SOFT), card_w - 0.7)
            h.move_to([0, y + P(0.44, 0.46), 0])
            self.play(FadeIn(h), run_time=0.45)
            b = _fit(_t(body, size=P(31, 23), color=col, weight="BOLD"),
                     card_w - 0.7)
            b.move_to([0, y - P(0.22, 0.20), 0])
            self.play(FadeIn(b, shift=UP * 0.08), run_time=0.6)

        # The shared fact goes UNDER both cards, not between them. A joiner
        # line in the gap measured 0.10 units -- the cards sit 0.30 apart --
        # so it rendered as a stray tick with a label floating beside
        # nothing. Below both cards it also fills the band the cards leave
        # empty.
        # SOFT, not accented. The beat already spends its terracotta on the
        # 2021 result and on the closing line; a third accented line here
        # would break "one terracotta moment per beat".
        same = _fit(_t("the same predictor, four years apart",
                       size=P(24, 19), color=SOFT), P(7.6, 3.34))
        same.move_to([0, P(-1.56, -1.60), 0])
        self.play(FadeIn(same, shift=UP * 0.08), run_time=0.55)

        closer(self, "what you measure decides what it bought")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE TELL
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    BEAT, RT, HOLD = "B10", 1.550, 0.008
    RT_PORTRAIT = None

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The Tell",
               "Every figure COMPUTED here, seed 1616, scored on held-out atmospheres.")

        exp = _fit(_t("a messier sky should break it", size=P(31, 24),
                      color=SOFT), P(8.4, 3.30))
        exp.move_to([0, P(1.92, 2.24), 0])
        self.play(FadeIn(exp), run_time=0.6)
        self.play(Create(_strike(exp, color=ACC, sw=5)), run_time=0.5)

        pairs = (
            ("quiet sensor", G_CLEAN, G_CLEAN3, ACC),
            ("noisy sensor", G_REAL, G_REAL3, INK),
        )
        ys = (P(0.70, 0.88), P(-0.84, -0.92))
        for (lab, v1, v3, col), y in zip(pairs, ys):
            card = _card(P(10.4, 3.46), P(1.30, 1.42), [0, y, 0])
            self.play(Create(card), run_time=0.55)
            h = _fit(_t(lab, size=P(22, 18), color=SOFT), P(9.6, 3.00))
            h.move_to([0, y + P(0.38, 0.44), 0])
            self.play(FadeIn(h), run_time=0.4)
            if PORTRAIT:
                a = _fit(_t("1 layer  " + v1, size=20, color=col,
                            weight="BOLD"), 3.10)
                a.move_to([0, y - 0.02, 0])
                b = _fit(_t("3 layers  " + v3, size=20, color=col,
                            weight="BOLD"), 3.10)
                b.move_to([0, y - 0.42, 0])
            else:
                a = _fit(_t("one layer  " + v1, size=30, color=col,
                            weight="BOLD"), 4.6)
                a.move_to([-2.50, y - 0.22, 0])
                b = _fit(_t("three layers  " + v3, size=30, color=col,
                            weight="BOLD"), 4.6)
                b.move_to([2.50, y - 0.22, 0])
            self.play(FadeIn(a, shift=UP * 0.08), run_time=0.5)
            self.play(FadeIn(b, shift=UP * 0.08), run_time=0.5)

        closer(self, "noise, not complexity")
        self.hold_to_beat()
