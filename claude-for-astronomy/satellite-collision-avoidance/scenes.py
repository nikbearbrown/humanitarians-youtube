"""scenes.py - Manim scenes for satellite-collision-avoidance.

*Safer By Not Looking.* - ai-explainer, claude-hai, Ep. 15. THE SERIES FINALE.

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

    B04  the hard-body disk        against the probability field
    B05  the Pc curve              against the action threshold
    B06  the degraded-tracking bar against the well-tracked bar
    B07  the alerts that climb     against the ones that fade
    B08  the trained model         against the naive baseline
    B10  Pc as it dilutes          against the scale-free bound

  The load-bearing moment is B06, where two bars for the SAME conjunction sit
  on either side of the action threshold - nothing about the two objects
  differs, only how well one of them was tracked. The mapping never flips, so
  B04 teaches it once and every later plate reads for free.

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
  Every plate comes from assets/gen_conj.py, which runs the REAL calculation:
  the short-encounter collision-probability integral (Foster's method), in
  its numerically stable form, over a simulated population of 120,000
  conjunctions whose covariance shrinks as closest approach arrives.

  Using the real integral is the point. The episode's subject is a PROPERTY
  of that integral - that it is not monotonic in your own uncertainty - and
  a property can only be shown by the thing that has it.

  FOUR claims are ASSERTED and the generator writes nothing if any fails.

  TWO MEASURED RESULTS ARE DELIBERATELY NOT CLAIMED ON SCREEN as fixes:
  adding sigma/d as a feature moves the notified error by -2.7% (nothing),
  and reweighting the tail 300x improves the notified error 2.4x while
  costing 15x on the aggregate and STILL losing to persistence. Both are in
  the paperwork. B10 says the first one out loud, because "the fix I tried
  did not work" is the honest shape of that beat.

  A PLATE WAS REDRAWN AFTER BEING MEASURED. shrink.png was first drawn to
  show alerts BREAKING LATE - quiet until the last message, then jumping.
  The population contains ZERO such events, and that is not an artefact: as
  the covariance shrinks below the miss distance, Pc falls, so better
  tracking almost always makes an alert DECAY. The plate now shows what is
  actually there.

PLATE GEOMETRY - ph = pw * (ih/iw). Do this arithmetic, do not assume it.
      geometry  1560x620  0.397
      dilution  1560x780  0.500     flip      1560x780  0.500
      shrink    1560x780  0.500     bars      1560x780  0.500
      maxpc     1560x780  0.500
  The landscape figure band is 4.30 units tall, so a 0.50-ratio plate at
  pw = 8.0 is 4.00 tall and leaves nothing for labels; the 0.50 plates run at
  pw 6.6 (3.30 tall). geometry runs at 7.4 (2.94) and is CENTRED, because it
  is the one plate beat with no right-hand column.

GATE NOTES (learned the expensive way on Eps. 03-14)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - A plate's IMAGE is invisible to GATE B, but its FRAME is a Rectangle and
    therefore a curve. So a label crossing a plate's OUTLINE is caught and a
    label inside it is not. Ep. 14's B08/B10 were flagged for exactly this.
    EVERY landscape plate beat with a right-hand column puts its plate at
    x = -1.10, so the plate's right edge is 2.20 and the column (2.52..5.96)
    clears it by 0.32.
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
    RT_PORTRAIT = None   # see below; None means "use RT in both aspects"
    HOLD = 0.0      # rest after each reveal
    _raw = False

    # WHY RT_PORTRAIT EXISTS.
    # The pacing solve runs ONCE, in landscape, and writes the RT/HOLD line.
    # A scene whose portrait branch plays FEWER reveals then underfills its
    # beat: the body is shorter, hold_to_beat floors the difference, and the
    # clip sits on a frozen last frame for the remainder. Undershoot is safe
    # -- compile.py pads a short clip with a held frame, where a LONG clip
    # would be centre-cut and lose its closing line -- but B08 portrait would
    # have frozen for ~5 s of a 14 s beat, which is dead air, not pacing.
    #
    # So the five scenes that drop on-screen-only extras in portrait carry a
    # second, larger RT for that aspect. It is a separate class attribute and
    # NOT part of the `BEAT, RT, HOLD = ...` line, so pace14.py's regex still
    # finds and rewrites the canonical line without clobbering this one.
    #
    # A larger RT in portrait is also right on its own terms: portrait shows
    # fewer things, so each one can afford to take longer to arrive.

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
        holding its last frame, which is invisible; a clip LONGER than its beat
        is centre-cut, which would clip the closing line off both ends.

        renderer.time UNDER-reports the true rendered length, because each
        play's frame count rounds up and the error accumulates with the number
        of reveals. B10 has 20 of them and overshot by +0.12 s. That cannot be
        fixed by lowering RT or HOLD -- a smaller body raises `target - now` by
        exactly the same amount and the total does not move -- so the target
        itself carries a safety trim.

        IN PRACTICE THE LEVER IS ALWAYS RT, because a scene that lands thin
        has already hit `floor`. A per-scene trim override was built and
        tried on four scenes across two episodes -- Ep. 11's B01 and B07,
        Ep. 12's B07 and B09 -- and moved the measured duration by exactly
        zero every time, because `target - trim - now` was already below
        0.35 s in all four. Once the wait is floored the total is just
        `body + floor`, and only a smaller body changes it.

        So the rule is short: a scene landing above -0.15 s is floored; lower
        its RT until it sits with its siblings near -0.20. Do not reach for a
        trim knob -- it was tried, twice, and it is not the one.
        """
        target = BEAT_SECONDS.get(self.BEAT or "", 0.0)
        now = float(getattr(getattr(self, "renderer", None), "time", 0.0) or 0.0)
        self.wait(max(floor, target - TAIL_TRIM - now) if target else floor)


# ─────────────────────────────────────────────────────────────────────────────
#  Plate geometry. A plate placed by WIDTH gets its height for free:
#      ph = pw * (ih / iw)
#      geometry 1560x620 (0.397)
#      dilution 1560x780 (0.500)   flip  1560x780 (0.500)
#      shrink   1560x780 (0.500)   bars  1560x780 (0.500)
#      maxpc    1560x780 (0.500)
#
#  WHERE A LABEL MAY SIT. gen_conj.py draws IMAGERY ONLY -- no text, no tick
#  labels, no legend. Everything named on screen is a Manim mobject placed
#  OUTSIDE the plate rectangle.
#
#  A plate's IMAGE is invisible to GATE B; its FRAME is a Rectangle, and so a
#  curve. A label crossing the OUTLINE is caught, one inside it is not. Every
#  landscape plate beat that uses the right-hand column therefore puts its
#  plate at x = -1.10 (right edge 2.20, column 2.52..5.96, 0.32 clear).
#  B04 is the exception: it has no right-hand column, so it centres.
# ─────────────────────────────────────────────────────────────────────────────
PLATE_X = -1.10        # every landscape plate that has a right-hand column
RCOL_X = 4.24          # centre of that column
RCOL_W = 3.44          # and its width: it spans x 2.52 .. 5.96


# ── Plate-internal coordinates, computed once, not guessed ───────────────────
# Axes() insets its box by 18 px on a 1560-wide plate, so a data x maps to
# fraction 18/1560 + (1524/1560) * (x - a) / (b - a).
#
# flip.png: xlim (0, 2), bars at x = 0.62 and 1.38.
FLIP_FX = (-0.18563, +0.18563)      # offsets from plate CENTRE, in units of pw
#
# bars.png is two independent panels, pad 18 and gap 40 on 1560, so each panel
# is 742 wide. Panel centres, and the bar centres inside them:
BARS_PANEL_FX = (-0.25064, +0.25064)
#
# These are all safely INSIDE the plate (|f| < 0.5), which is what makes the
# `pw * k` form legal here. The form that is NOT legal is a label placed
# OUTSIDE a plate by a pw-scaled offset -- landscape pw = 6.6 in a 12.3-unit
# frame fits, portrait pw = 3.4 in a 3.6-unit frame does not.
#
# geometry.png is three panels, pad 16 and gap 18 on 1560, each 502 wide:
GEOM_PANEL_FX = (-0.33333, 0.0, +0.33333)

# Numbers the scenes put on screen. Every one is printed by
# assets/gen_conj.py, kept here as named constants so a changed experiment
# cannot silently disagree with a label.
N_EVENTS_PUB = "15,321"       # ESA challenge, published
N_CDMS_PUB = "199,082"        # published
N_DANGER_PUB = "30"           # published: events ever above 1e-4
N_TEAMS = "97"                # published
N_BEAT = "12"                 # published: teams that beat the naive forecast
P_GOOD = "1.6 in a thousand"  # computed: Pc at the peak, d = 300 m
P_BAD = "8 in a million"      # computed: Pc at sigma = 5000 m
INFLATE = "7x"                # computed: sigma inflation that crosses 1e-4
THRESH = "1 in 10,000"        # the action threshold drawn on every plate
N_TEST = "40,000"             # computed: test events
N_NOTIFIED = "124"            # computed: test events ever above the floor
FACTOR_ALL = "4x"             # computed: ridge over persistence, all events
FACTOR_HI = "3x"              # computed: persistence over ridge, notified
GEOM_MOVE = "three percent"   # computed: what the sigma/d feature bought


def _plate_at(name, pw, at, frame=True):
    """A plate plus the height it took, so callers can place labels around it."""
    g = _plate(name, pw, at, frame=frame)
    return g, _plate_h(name, pw)


def _axis_note(scene, text, y, col=SOFT, size=(22, 18), x=None, rt=0.45):
    n = _fit(_t(text, size=P(*size), color=col),
             P(RCOL_W, 3.34), [RCOL_X if x is None else x, y, 0])
    scene.play(FadeIn(n), run_time=rt)
    return n


def _swatch_row(text, col, at, w, size=18, val=None):
    """A legend row: colour chip then name. Portrait's substitute for a column.

    The label is placed from the CONTAINER, never from its own width. An
    earlier version positioned it at `left + swatch + lab.width/2`, which is
    correct in a real render but meaningless under GATE A's geometry stub,
    where a Text has no width -- the gate computed x = 6.6 on a +-6.15 frame
    and flagged it. Since the label is already fitted to `w - 0.42`, centring
    it in the space right of the swatch is exact in both.
    """
    sw = Rectangle(width=0.22, height=0.22, color=col, fill_color=col,
                   fill_opacity=1.0, stroke_width=0)
    sw.move_to([at[0] - w / 2.0 + 0.11, at[1], 0])
    if val is None:
        lab = _fit(_t(text, size=size, color=INK), w - 0.42)
        lab.move_to([at[0] + 0.11, at[1], 0])
        return VGroup(sw, lab)
    # With a value, name and number share ONE line. Stacking them cost 0.02
    # units of clearance in portrait and read as a single run-on block.
    lab = _fit(_t(text, size=size, color=INK), w * 0.56)
    v = _fit(_t(val, size=size + 2, weight="BOLD",
                color=ACCT if col is ACC else INK), w * 0.34)
    lab.move_to([at[0] - w * 0.14, at[1], 0])
    v.move_to([at[0] + w * 0.31, at[1], 0])
    return VGroup(sw, lab, v)


def _field(n, cols, sp, at, radius, color=INK):
    """A rectangular field of marks, row-major from the top left."""
    g = VGroup()
    rows = (n + cols - 1) // cols
    for k in range(n):
        r, c = divmod(k, cols)
        g.add(Dot(radius=radius, color=color).move_to(
            [at[0] + (c - (cols - 1) / 2.0) * sp,
             at[1] - (r - (rows - 1) / 2.0) * sp, 0]))
    return g


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 1.035, 0.000

    def construct(self):
        self.camera.background_color = BG
        hair = Line([-(X_MAX - 0.10), HAIR_Y, 0], [X_MAX - 0.10, HAIR_Y, 0],
                    color=RULE, stroke_width=2.4)
        top = _fit(_t("AI in Astronomy & Space Science  ·  Ep. 15",
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

        r1 = _fit(_t("fourteen episodes", size=P(28, 23), color=SOFT),
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
        r2b = _fit(_t("it moves when you do", size=P(23, 19), color=INK),
                   P(4.9, 3.00))
        r2b.move_to([card_at[0], card_at[1] - P(0.72, 0.70), 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)
        self.play(Create(SurroundingRectangle(VGroup(r2, r2b), color=ACC,
                                              buff=0.18, stroke_width=3,
                                              corner_radius=0.10)),
                  run_time=0.5)

        ser = _fit(_t("Ep. 15  ·  the last one", size=P(23, 18), color=ACCT),
                   P(6.0, 3.34))
        ser.move_to([0, P(-2.34, -2.44), 0])
        self.play(FadeIn(ser), run_time=0.5)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — THE WHOLE IDEA, IN ONE BREATH
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.550, 0.171

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath")

        cy = FIG_MID
        card = _card(P(9.40, 3.50), P(4.20, 4.50), [0, cy, 0])
        self.play(Create(card), run_time=0.8)

        tw = P(8.60, 3.10)

        def row(head, sub, hy, sy, hcol, hsize, bold=None):
            h = _fit(_t(head, size=P(*hsize), color=hcol, weight=bold), tw,
                     [0, cy + hy, 0])
            self.play(FadeIn(h, shift=UP * 0.08), run_time=0.6)
            if sub:
                s = _fit(_t(sub, size=P(24, 18), color=SOFT), tw,
                         [0, cy + sy, 0])
                self.play(FadeIn(s), run_time=0.5)
            return h

        row("NOT THE CHANCE THEY HIT", "that is what everyone hears",
            1.45, 0.98, INK, (30, 21), "BOLD")
        row("GIVEN YOUR OWN UNCERTAINTY", "that is what is computed",
            0.15, -0.32, INK, (30, 21), "BOLD")
        h3 = row("SO IT IS PARTLY ABOUT YOU", None,
                 -1.30, 0.0, ACCT, (32, 22), "BOLD")
        self.play(Create(_underline(h3, color=ACC, sw=5, buff=0.16)),
                  run_time=0.5)

        closer(self, "know less, look safer", cx=0.0)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE BENCHMARK
# ═════════════════════════════════════════════════════════════════════════════
class B03_TheBenchmark(Paced):
    """An isotype at honest scale: one mark is ten close approaches.

    15,321 events against 30 is a ratio of 511 to 1, which cannot be drawn as
    two blocks side by side -- at any mark size that makes the small block
    visible, the large one does not fit. So the thirty are drawn INSIDE the
    field, as three terracotta marks among 1,532. The ratio is then the
    picture rather than a caption on it, and the caption only has to say what
    one mark is worth.
    """
    BEAT, RT, HOLD = "B03", 1.550, 0.052
    RT_PORTRAIT = 2.225

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Fifteen thousand close approaches",
               cite="ESA Collision Avoidance Challenge  ·  Uriot et al. 2020  "
                    "·  one mark = 10 close approaches")

        if not PORTRAIT:
            chip = _chip("PUBLISHED  ·  ESA, 2015-2019", size=20, max_w=5.4)
            chip.move_to([-4.05, 2.18, 0])
            self.play(FadeIn(chip, shift=DOWN * 0.08), run_time=0.6)

        cols, sp = P(56, 38), P(0.082, 0.068)
        at = [P(-1.05, 0.0), P(0.0, 0.40), 0]
        field = _field(1532, cols, sp, at, P(0.022, 0.019), INK)
        lab = _fit(_t("%s close approaches" % N_EVENTS_PUB, size=P(26, 21),
                      color=INK, weight="BOLD"), P(4.40, 3.30))
        lab.move_to([at[0], at[1] + P(1.52, 1.75), 0])
        self.play(FadeIn(lab), run_time=0.5)
        self.play(FadeIn(field, lag_ratio=0.0006), run_time=1.6)

        # the thirty, in place, at the same mark size
        # Three marks, scattered through the field rather than clustered, so
        # the eye has to find them. That is the point of the beat.
        # 2.8x, not 1.7x. At 1.7 the three marks were measured in a rendered
        # frame and could not be found by eye in a field of 1,532 -- and the
        # whole beat asks the viewer to find them. At 2.8 the mark nearly
        # fills its own cell: unmistakably one mark, unmistakably visible.
        hot = VGroup(*[field[k].copy().set_color(ACC).scale(2.8)
                       for k in (281, 744, 1190)])
        self.play(LaggedStart(*[GrowFromCenter(h) for h in hot],
                              lag_ratio=0.22), run_time=0.9)
        hl = _fit(_t("%s were ever dangerous" % N_DANGER_PUB, size=P(26, 21),
                     color=ACCT, weight="BOLD"), P(4.40, 3.30))
        hl.move_to([at[0], at[1] - P(1.52, 1.70), 0])
        self.play(FadeIn(hl, shift=UP * 0.08), run_time=0.55)

        if not PORTRAIT:
            _axis_note(self, "%s warning" % N_CDMS_PUB, 0.52, col=INK)
            _axis_note(self, "messages", 0.12, col=INK)
            _axis_note(self, "about thirteen", -0.62)
            _axis_note(self, "per approach", -1.00)

        closer(self, "thirty mattered", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — WHAT THE NUMBER IS
# ═════════════════════════════════════════════════════════════════════════════
class B04_TheNumber(Paced):
    """The one plate beat with no right-hand column, so its plate CENTRES.

    The plate draws 1, 2 and 3 sigma COVARIANCE ELLIPSES, not a shaded
    density field. Two earlier versions shaded the Gaussian and neither could
    satisfy both the physics and GATE V's low-contrast check -- see the long
    note in gen_conj.geometry_plate. Rings are also how conjunction geometry
    is actually drawn, and they say the same thing: the ellipse grows while
    the hard-body disk does not.
    """
    BEAT, RT, HOLD = "B04", 1.550, 0.359

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The same encounter, three tracking solutions",
               cite="computed in this reel  ·  miss distance 300 m, hard-body "
                    "radius 20 m  ·  rings are 1, 2 and 3 sigma")

        # 6.40, not 7.40. The plate is a large, deliberately pale field, and
        # GATE V averages the colour of every inked pixel in the FRAME -- so
        # a wider plate is a lower score. Narrowing it and bolding the labels
        # buys the contrast that darkening the plate would have bought by
        # misstating the physics.
        pw = P(7.40, 3.46)
        pat = [0.0, P(0.86, 1.52), 0]
        plate, ph = _plate_at("geometry.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        names = [("tracked well", SOFT, 0), ("in between", SOFT, 1),
                 ("tracked badly", ACCT, 2)]
        for text, col, i in names:
            lab = _fit(_t(text, size=P(30, 23), color=col,
                          weight="BOLD"), P(2.20, 1.05))
            if PORTRAIT:
                lab.move_to([0, pat[1] - ph / 2.0 - 0.40 - i * 0.44, 0])
            else:
                lab.move_to([pat[0] + GEOM_PANEL_FX[i] * pw,
                             pat[1] - ph / 2.0 - 0.38, 0])
            self.play(FadeIn(lab, shift=UP * 0.06), run_time=0.5)

        note = _fit(_t("the same disk, twenty metres across, in all three",
                       size=P(29, 21), color=ACCT, weight="BOLD"),
                    P(7.60, 3.34))
        note.move_to([0, pat[1] - ph / 2.0 - P(1.02, 1.76), 0])
        self.play(FadeIn(note), run_time=0.55)

        closer(self, "less on the disk", cx=0.0)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE CURVE HAS A SUMMIT
# ═════════════════════════════════════════════════════════════════════════════
class B05_Dilution(Paced):
    BEAT, RT, HOLD = "B05", 1.550, 0.065
    RT_PORTRAIT = 2.137

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The probability, against your own uncertainty",
               cite="computed in this reel  ·  the short-encounter integral, "
                    "miss distance 300 m")

        pw = P(6.60, 3.40)
        pat = [P(PLATE_X, 0.0), P(0.60, 1.50), 0]
        plate, ph = _plate_at("dilution.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        ends = [("you know exactly", -0.34), ("you know almost nothing", 0.34)]
        if not PORTRAIT:
            for text, f in ends:
                lab = _fit(_t(text, size=22, color=SOFT), 2.70)
                lab.move_to([pat[0] + f * pw, pat[1] - ph / 2.0 - 0.36, 0])
                self.play(FadeIn(lab), run_time=0.45)
            _axis_note(self, "horizontal  ·  how big your", 1.96)
            _axis_note(self, "position error is", 1.58)
            chip = _chip("act above %s" % THRESH, size=24, max_w=3.30)
            chip.move_to([RCOL_X, 0.62, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
            _axis_note(self, "the dashed rule", 0.10)
            _axis_note(self, "the summit: as bad as this", -0.66, col=INK)
            _axis_note(self, "encounter is ever allowed to look", -1.04, col=INK)
        else:
            _axis_note(self, "left  ·  you know exactly where they are",
                       0.12, x=0.0)
            _axis_note(self, "right  ·  you know almost nothing", -0.38, x=0.0)
            chip = _chip("act above %s" % THRESH, size=22, max_w=3.30)
            chip.move_to([0.0, -1.10, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
            _axis_note(self, "the dot is the summit", -1.70, col=INK, x=0.0)

        closer(self, "the curve has a summit", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — THE FLIP
# ═════════════════════════════════════════════════════════════════════════════
class B06_TheFlip(Paced):
    """The load-bearing beat. Two bars, one conjunction, opposite decisions."""
    BEAT, RT, HOLD = "B06", 1.497, 0.000
    RT_PORTRAIT = 2.253

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "One conjunction. Two answers.",
               cite="computed in this reel  ·  the same two objects, the same "
                    "miss distance, the same day")

        pw = P(6.60, 3.40)
        pat = [P(PLATE_X, 0.0), P(0.66, 1.52), 0]
        plate, ph = _plate_at("flip.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        bars = [("tracked well", P_GOOD, INK, 0), ("uncertainty %s larger"
                % INFLATE, P_BAD, ACC, 1)]
        if PORTRAIT:
            for i, (name, val, col, _j) in enumerate(bars):
                row = _swatch_row(name, col, [0.0, 0.20 - i * 0.56, 0], 3.40,
                                  size=17, val=val)
                self.play(FadeIn(row, shift=RIGHT * 0.06), run_time=0.55)
            chip = _chip("the threshold sits between them", size=20,
                         max_w=3.40)
            chip.move_to([0.0, -1.20, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
        else:
            for name, val, col, i in bars:
                x = pat[0] + FLIP_FX[i] * pw
                nm = _fit(_t(name, size=22,
                             color=ACCT if col is ACC else SOFT), 2.30,
                          [x, pat[1] - ph / 2.0 - 0.36, 0])
                vl = _fit(_t(val, size=27,
                             color=ACCT if col is ACC else INK,
                             weight="BOLD"), 2.30,
                          [x, pat[1] - ph / 2.0 - 0.80, 0])
                self.play(FadeIn(nm), run_time=0.42)
                self.play(FadeIn(vl, shift=UP * 0.06), run_time=0.48)
            chip = _chip("act above %s" % THRESH, size=24, max_w=3.30)
            chip.move_to([RCOL_X, 0.86, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
            _axis_note(self, "nothing about the two", 0.16, col=INK)
            _axis_note(self, "objects is different", -0.22, col=INK)
            _axis_note(self, "only how well one of", -0.90)
            _axis_note(self, "them was tracked", -1.28)

        closer(self, "the alert goes away", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — WHAT THE FORECAST IS ACTUALLY FOR
# ═════════════════════════════════════════════════════════════════════════════
class B07_TheTask(Paced):
    BEAT, RT, HOLD = "B07", 1.550, 0.064
    RT_PORTRAIT = 2.141

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Risk, as closest approach arrives",
               cite="computed in this reel  ·  120,000 conjunctions, seven "
                    "messages each")

        pw = P(6.60, 3.40)
        pat = [P(PLATE_X, 0.0), P(0.60, 1.50), 0]
        plate, ph = _plate_at("shrink.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        if PORTRAIT:
            self.play(FadeIn(_swatch_row("alerts that fade away", GHOST,
                                         [0.0, 0.18, 0], 3.40)), run_time=0.5)
            self.play(FadeIn(_swatch_row("the ones that climb", ACC,
                                         [0.0, -0.34, 0], 3.40)), run_time=0.5)
            _axis_note(self, "the rule  ·  forecast from here", -1.02, x=0.0)
            _axis_note(self, "two days to closest approach", -1.64,
                       col=INK, x=0.0)
        else:
            _axis_note(self, "vertical  ·  the reported risk", 1.96)
            _axis_note(self, "horizontal  ·  days to closest", 1.58)
            self.play(FadeIn(_swatch_row("alerts that fade", GHOST,
                                         [RCOL_X, 0.86, 0], RCOL_W, 21)),
                      run_time=0.5)
            self.play(FadeIn(_swatch_row("the ones that climb", ACC,
                                         [RCOL_X, 0.40, 0], RCOL_W, 21)),
                      run_time=0.5)
            _axis_note(self, "the vertical rule is where", -0.34, col=INK)
            _axis_note(self, "the forecast is made", -0.72, col=INK)
            _axis_note(self, "nothing quiet here turns", -1.34)
            _axis_note(self, "dangerous later", -1.72)

        closer(self, "they announce themselves early", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — THE REVERSAL
# ═════════════════════════════════════════════════════════════════════════════
class B08_TheReversal(Paced):
    """Two panels that CANNOT share an axis, which is the beat.

    The two errors differ by two orders of magnitude. Forcing them onto one
    axis would flatten the right-hand panel to nothing -- and the right-hand
    panel is the only one an operator cares about. The panels are therefore
    scaled independently, and the scene says so out loud.
    """
    BEAT, RT, HOLD = "B08", 1.550, 0.084
    RT_PORTRAIT = 1.964

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Same model. Opposite verdict.",
               cite="computed in this reel  ·  mean squared error on the final "
                    "risk  ·  panels scaled independently")

        pw = P(6.60, 3.40)
        pat = [P(PLATE_X, 0.0), P(0.66, 1.52), 0]
        plate, ph = _plate_at("bars.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        panels = [("scored on all %s" % N_TEST, 0),
                  ("scored on the %s notified" % N_NOTIFIED, 1)]
        if PORTRAIT:
            for i, (text, _j) in enumerate(panels):
                lab = _fit(_t(text, size=19, color=INK), 3.30,
                           [0.0, 0.24 - i * 0.46, 0])
                self.play(FadeIn(lab), run_time=0.5)
            self.play(FadeIn(_swatch_row("the trained model", ACC,
                                         [0.0, -0.72, 0], 3.40)), run_time=0.5)
            self.play(FadeIn(_swatch_row("assume nothing changes", INK,
                                         [0.0, -1.18, 0], 3.40)), run_time=0.5)
            chip = _chip("%s better left, %s worse right"
                         % (FACTOR_ALL, FACTOR_HI), size=19, max_w=3.40)
            chip.move_to([0.0, -1.74, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
        else:
            for text, i in panels:
                lab = _fit(_t(text, size=22, color=INK), 2.80,
                           [pat[0] + BARS_PANEL_FX[i] * pw,
                            pat[1] - ph / 2.0 - 0.38, 0])
                self.play(FadeIn(lab, shift=UP * 0.06), run_time=0.5)
            self.play(FadeIn(_swatch_row("the trained model", ACC,
                                         [RCOL_X, 1.42, 0], RCOL_W, 21)),
                      run_time=0.5)
            self.play(FadeIn(_swatch_row("assume nothing changes", INK,
                                         [RCOL_X, 0.96, 0], RCOL_W, 21)),
                      run_time=0.5)
            chip = _chip("%s better" % FACTOR_ALL, size=26, max_w=2.60)
            chip.move_to([RCOL_X, 0.10, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.55)
            bad = _fit(_t("%s worse" % FACTOR_HI, size=30, color=ACCT,
                          weight="BOLD"), 2.60, [RCOL_X, -0.68, 0])
            self.play(FadeIn(bad, shift=UP * 0.08), run_time=0.55)
            self.play(Create(_underline(bad, color=ACC, sw=4, buff=0.14)),
                      run_time=0.45)
            _axis_note(self, "on the only ones anybody saw", -1.42)

        closer(self, "same model, opposite verdict", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — NINETY-SEVEN TEAMS
# ═════════════════════════════════════════════════════════════════════════════
class B09_NinetySeven(Paced):
    BEAT, RT, HOLD = "B09", 1.419, 0.000
    RT_PORTRAIT = 2.089

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Ninety-seven teams tried this for real",
               cite="ESA Collision Avoidance Challenge  ·  Uriot et al. 2020  "
                    "·  one mark = one team")

        if not PORTRAIT:
            chip = _chip("PUBLISHED  ·  ESA, 2020", size=20, max_w=5.0)
            chip.move_to([-4.30, 2.18, 0])
            self.play(FadeIn(chip, shift=DOWN * 0.08), run_time=0.6)

        cols, sp = P(14, 10), P(0.34, 0.26)
        at = [P(-1.60, 0.0), P(0.0, 0.45), 0]
        # SOFT, not GHOST, for the unlit teams. Ghost-grey sits barely above
        # GATE V's ink threshold, and 85 pale dots are the dominant ink in
        # this frame once PORTRAIT drops the chip and the pull-quote -- the
        # 9:16 cut failed low-contrast at 0.26 against a 0.30 floor while
        # landscape passed, purely because landscape still had that extra
        # dark text. Soft is a fill, so the palette rule is untouched, and
        # the twelve terracotta marks still separate by hue, not by being
        # the only thing on screen that is visible.
        cold = _field(97, cols, sp, at, P(0.105, 0.085), SOFT)
        self.play(FadeIn(cold, lag_ratio=0.006), run_time=1.1)
        lab = _fit(_t("%s teams" % N_TEAMS, size=P(26, 21), color=INK,
                      weight="BOLD"), P(4.00, 3.30))
        lab.move_to([at[0], at[1] + P(1.62, 1.72), 0])
        self.play(FadeIn(lab), run_time=0.5)

        hot = VGroup(*[cold[k].copy().set_color(ACC) for k in range(12)])
        self.play(LaggedStart(*[GrowFromCenter(h) for h in hot],
                              lag_ratio=0.07), run_time=0.9)
        hl = _fit(_t("%s beat the naive forecast" % N_BEAT, size=P(26, 21),
                     color=ACCT, weight="BOLD"), P(4.40, 3.34))
        hl.move_to([at[0], at[1] - P(1.62, 1.70), 0])
        self.play(FadeIn(hl, shift=UP * 0.08), run_time=0.55)

        if not PORTRAIT:
            q = _fit(_t("“surprisingly effective”", size=30,
                        color=ACCT, weight="BOLD"), RCOL_W,
                     [RCOL_X, 0.56, 0])
            self.play(FadeIn(q, shift=UP * 0.08), run_time=0.6)
            _axis_note(self, "the organisers' own words", -0.04)
            _axis_note(self, "for a forecast that says", -0.78, col=INK)
            _axis_note(self, "nothing will change", -1.16, col=INK)

        closer(self, "twelve of ninety-seven", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE TELL
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    """The beat that says the fix I tried did not work.

    Giving the model sigma/d -- where the conjunction sits on the dilution
    curve -- moved the notified error by 2.7%. That is nothing, and saying so
    is the honest shape of this beat: the problem was never the features.
    """
    BEAT, RT, HOLD = "B10", 1.550, 0.074
    RT_PORTRAIT = 1.987

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Ask a question that does not depend on you",
               cite="computed in this reel  ·  the probability, and the worst "
                    "this geometry allows")

        pw = P(6.60, 3.40)
        pat = [P(PLATE_X, 0.0), P(0.60, 1.50), 0]
        plate, ph = _plate_at("maxpc.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        if PORTRAIT:
            self.play(FadeIn(_swatch_row("the probability you compute", ACC,
                                         [0.0, 0.18, 0], 3.40)), run_time=0.5)
            self.play(FadeIn(_swatch_row("the worst this geometry allows", INK,
                                         [0.0, -0.32, 0], 3.40)), run_time=0.5)
            chip = _chip("same uncertainty, two answers", size=20, max_w=3.40)
            chip.move_to([0.0, -1.04, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
            _axis_note(self, "one says no action, one says act", -1.68,
                       col=INK, x=0.0)
        else:
            self.play(FadeIn(_swatch_row("the probability you compute", ACC,
                                         [RCOL_X, 1.86, 0], RCOL_W, 21)),
                      run_time=0.5)
            self.play(FadeIn(_swatch_row("the worst this geometry allows", INK,
                                         [RCOL_X, 1.40, 0], RCOL_W, 21)),
                      run_time=0.5)
            chip = _chip("same uncertainty, two answers", size=21,
                         max_w=3.34)
            chip.move_to([RCOL_X, 0.62, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
            _axis_note(self, "one reads no action,", -0.10)
            _axis_note(self, "the other reads act", -0.48)
            _axis_note(self, "I gave it the geometry too -", -1.16, col=INK)
            _axis_note(self, "it moved the error %s" % GEOM_MOVE, -1.54,
                       col=INK)

        closer(self, "it stops depending on you", cx=P(-0.6, 0.0))
        self.hold_to_beat()
