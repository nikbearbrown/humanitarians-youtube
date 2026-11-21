"""scenes.py - Manim scenes for counting-craters.

*The Clock Needs a Rock.* - ai-explainer, claude-hai, Ep. 18.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL - and it never flips
  Terracotta is THE COUNT: the measurement, the thing a better detector
  changes. Ink is THE CLOCK: the chronology curve, and the dated rocks that
  hold it up.

    B03  terracotta craters on both patches     - the thing being counted
    B04  terracotta bars                        - three counts
    B06  terracotta bars                        - what the detector recovered
    B07  the ink curve                          - the clock
    B08  terracotta band THROUGH the ink curve  - the whole argument, in two
                                                  colours, in one figure
    B10  a terracotta bar (counted window) against an ink tick (the rock)

  ONE LOCAL CONVENTION, taught in-beat at B05 because it cannot be read off
  the contract: in spread.png a FILLED crater is one every analyst marked and
  an OPEN one is contested. The beat says so out loud and shows the legend.

THIS FILE IS ASPECT-AWARE - IT RENDERS BOTH CUTS
  The reel ships in 16:9 (3840x2160) and 9:16 (2160x3840). Manim keeps
  frame_height = 8.0 in both, so the VERTICAL band plan is identical either
  way; only the horizontal extent changes - x +-6.15 landscape, x +-1.80
  portrait. Portrait is NOT a crop: it restacks. Landscape puts a plate beside
  a right-hand column; portrait puts the column underneath.

  EVERY SCENE PLAYS THE SAME NUMBER OF REVEALS IN BOTH ASPECTS. No self.play()
  sits inside an `if PORTRAIT` branch - only COORDINATES differ. That is what
  makes RT_PORTRAIT unnecessary here: the pacing solve runs once, in
  landscape, and is correct for portrait too. If you add a portrait-only
  reveal, you have just bought yourself an RT_PORTRAIT line.

LAYOUT BAND PLAN (every scene obeys it - this is what keeps the gates green)
                        landscape      portrait
  title                   +3.02          +3.14
  hairline                +2.66          +2.84
  the figure       +2.40 .. -1.90   +2.62 .. -2.02
  the closing line        -2.50          -2.42   (terracotta rule 0.28 below)
  the citation            -3.20          -2.95
  the wordmark bug        -3.12          -3.28   (right-anchored, LOGO LAW)

PLATES - all six from assets/gen_craters.py, which asserts NINE claims and
writes nothing if any fails. Plates carry IMAGERY ONLY; every label on screen
is placed here, OUTSIDE the plate, because a plate arrives as an ImageMobject
and GATE B is nearly blind to its interior.

PLATE GEOMETRY - ph = pw * (ih/iw). Do this arithmetic, do not assume it.
      surface 1880x940   0.5000      pile    1880x620   0.3298
      spread  1000x1000  1.0000      curve   1760x1000  0.5682
      cost    1760x1000  0.5682      anchors 1880x530   0.2819
  The landscape figure band is 4.30 units tall. A 0.5682 plate therefore caps
  at pw 7.5; the beats that need a label row under the plate run narrower.

TWO PLATES WERE REDRAWN BECAUSE THEY TAUGHT THE OPPOSITE OF THEIR BEAT
  cost.png on an absolute time axis makes the two age windows 0.90 and
  0.56 Gyr - only 1.6x apart - so they read as "about the same" when the
  point is 90% against 16%. It now carries a second panel showing each window
  against its OWN age. pile.png read as a linear axis, making the automation
  gap look like 4x instead of 78x; it now has visible decade rails and B04
  says "x10 per rail" before anything else lands.

GATE NOTES (inherited; every one of these was paid for on Eps. 03-17)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - Never position a label from another Text's .width either - same reason.
    Position from the CONTAINER.
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - _strike() centres on the MEDIAN glyph top/bottom, i.e. the x-height band,
    NOT on get_center(). A bbox centre rises with ascenders, so the rule
    struck the TOPS of the letters on Ep. 16's B01 - and looked correct on a
    string that happened to have a descender. Text-geometry bugs are
    STRING-DEPENDENT; they survive a frame check on the wrong sentence.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - A plate's IMAGE is invisible to GATE B but its FRAME is a Rectangle and
    therefore a curve - so a label crossing a plate's OUTLINE is caught and a
    label inside it is not. Every landscape plate with a right-hand column
    clears that column (2.52..5.96) by at least 0.32.
  - NEVER write `pat[0] +- pw * k` for a label OUTSIDE a plate. Landscape
    pw 6.2 inside a 12.3-unit frame is fine; portrait pw 3.4 in a 3.6-unit
    frame is not.
  - NEVER use a glyph outside the font's coverage. EB Garamond has no "check"
    character and Ep. 09 rendered it as stray digits. Words, not symbols.
  - Leave >= 0.15 units between any two elements. 0.04 is eleven pixels at 4K
    and reads as contact.
  - Give every scene its footer EARLY. GATE V samples each beat at 50% and
    85%, and B01 on Ep. 17 read 30% fill for 4.6 s of an 8.4 s beat purely
    because its chrome was revealed in the LAST play.
  - Same-colour-on-same-colour is invisible to EVERY gate. Read the frames.
  - Prefer SOFT over GHOST for any LARGE field of marks. A contrast margin
    that depends on elements portrait DROPS is not a margin.
  - Stay inside the proven animation vocabulary: FadeIn, Create, Write,
    GrowFromEdge. All four are in GATE A's stub.
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

    The MEDIAN glyph top and bottom recover the x-height band itself. Most
    glyphs in a line of lower-case text are x-height, so the median top IS the
    x-height line and the median bottom IS the baseline, whatever the handful
    of ascenders do. A bbox centre would ride up with the ascenders - and
    would look right on any string that happens to contain a descender.
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
    hh = w * _ratio(name)
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


# Measured once from the generator's own canvas sizes. Hard-coded rather than
# read from disk so GATE A (which runs with no plates present) gets the same
# geometry the real render does.
_RATIO = {
    "surface.png": 940.0 / 1880.0,
    "pile.png": 620.0 / 1880.0,
    "spread.png": 1000.0 / 1000.0,
    "curve.png": 1000.0 / 1760.0,
    "cost.png": 1000.0 / 1760.0,
    "anchors.png": 530.0 / 1880.0,
}


def _ratio(name):
    return _RATIO.get(name, 0.5)


def _plate_h(name, w):
    """The height a plate of width w will occupy, without building it."""
    return w * _ratio(name)


def _marker_row(text, at, w, filled, size=18, col=ACC):
    """A crater marker and its label, centred on `at`, fitted to `w`.

    STUB-SAFE: the label is positioned from the CONTAINER, never from its own
    measured width - under GATE A's geometry stub a Text has no width.

    THE GAP IS LOAD-BEARING. The label is CENTRED, so reserving too little
    between marker and label welds the first letter to the marker on exactly
    the one row whose text fills its width. Reserve 0.10 and centre the label
    in what is left. (Ep. 17 shipped that defect past every gate.)
    """
    r = 0.15
    mk = Circle(radius=r, color=col, stroke_width=3.0,
                fill_color=col, fill_opacity=0.28 if filled else 0.0)
    mk.move_to([at[0] - w / 2.0 + r + 0.04, at[1], 0])
    lab = _t(text, size=size, color=INK)
    inner = w - 0.44
    _fit(lab, inner)
    lab.move_to([at[0] + 0.22, at[1], 0])
    return VGroup(mk, lab)


def _bar(x_left, y, w, h, col=ACC, opacity=1.0, stroke=0):
    return Rectangle(width=max(float(w), 0.004), height=h, color=col,
                     fill_color=col, fill_opacity=opacity,
                     stroke_width=stroke).move_to([x_left + w / 2.0, y, 0])


def _track(x_left, y, w, h):
    """The 100% reference behind a bar, so a proportion is readable as one."""
    return Rectangle(width=w, height=h, color=GHOST, fill_opacity=0.0,
                     stroke_width=1.6).move_to([x_left + w / 2.0, y, 0])


def _stat(value, caption, at, w, vsize=None, csize=None, vcol=ACCT, gap=None):
    """A big number with a small caption under it, centred on `at`."""
    gap = P(0.40, 0.34) if gap is None else gap
    v = _fit(_t(value, size=vsize or P(58, 46), color=vcol, weight="BOLD"),
             w * 0.95)
    v.move_to([at[0], at[1] + gap, 0])
    c = _fit(_t(caption, size=csize or P(20, 17), color=SOFT), w)
    c.move_to([at[0], at[1] - gap, 0])
    return VGroup(v, c)


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

    # WHY RT_PORTRAIT EXISTS (and why this reel needs none).
    # The pacing solve runs ONCE, in landscape, and writes the RT/HOLD line.
    # A scene whose portrait branch plays FEWER reveals then underfills its
    # beat: the body is shorter, hold_to_beat floors the difference, and the
    # clip sits on a frozen last frame for the remainder. Undershoot is safe
    # -- compile.py pads a short clip with a held frame, where a LONG clip
    # would be centre-cut and lose its closing line -- but a scene that
    # freezes for 5 s of a 14 s beat is dead air, not pacing.
    #
    # Every scene in THIS file plays the same reveals in both aspects, so the
    # landscape solve is correct for portrait. Keep it that way.

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
        """
        target = BEAT_SECONDS.get(self.BEAT or "", 0.0)
        now = float(getattr(getattr(self, "renderer", None), "time", 0.0) or 0.0)
        self.wait(max(floor, target - TAIL_TRIM - now) if target else floor)


# ─────────────────────────────────────────────────────────────────────────────
#  Plate placement and plate-internal coordinates
# ─────────────────────────────────────────────────────────────────────────────
PLATE_X = -1.30        # landscape plates that carry a right-hand column
RCOL_X = 4.24          # centre of that column
RCOL_W = 3.44          # and its width: it spans x 2.52 .. 5.96

# Plate-internal x offsets from the plate CENTRE, as a fraction of plate
# WIDTH, derived from gen_craters.py's own geometry rather than eyeballed.
# Manim y is up, PIL y is down, so every vertical offset below is negated
# relative to the generator's pixel coordinates. Get that backwards and the
# label points at the wrong row - which looks like a layout bug and is not.
#
# surface.png: two 760 px patches on an 1880 px canvas, left at x0=140 and
# right at x0=980, so their centres are 520 and 1360 against a centre of 940.
SURF_DX = 420.0 / 1880.0                      # +-0.2234

# pile.png: bars 112 px tall from y=70, pitch 182; canvas 620 tall, centre 310.
PILE_DY = [(310.0 - (70 + 56 + i * 182)) / 620.0 for i in range(3)]

# cost.png: the two relative bars sit at y = 790 and 910 on a 1000 px canvas.
COST_DY = [(500.0 - y) / 1000.0 for y in (790.0, 910.0)]

# anchors.png: ax(T) = 1720 - (T/4.2)*1560 on an 1880 px canvas, centre 940.
_ANC_L, _ANC_R = 160.0, 1720.0


def _anc_dx(T):
    return ((_ANC_R - (T / 4.2) * (_ANC_R - _ANC_L)) - 940.0) / 1880.0


ANC_OLD = _anc_dx(3.52)      # centre of the Apollo/Luna cluster
ANC_YOUNG = _anc_dx(0.32)    # centre of the young dated craters
ANC_GAP = _anc_dx(2.00)      # middle of the empty stretch
ANC_CE5 = _anc_dx(2.03)      # the Chang'e-5 anchor


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 1.550, 0.501

    def construct(self):
        self.camera.background_color = BG
        name = _fit(_t("OM MALI", size=P(54, 44), weight="BOLD"),
                    P(5.00, 3.20))
        name.move_to([P(-3.10, 0.0), P(1.40, 2.05), 0])
        rule = _underline(name, buff=0.18)
        role = _fit(_t("Humanitarians AI - presenter", size=P(22, 19),
                       color=SOFT), P(4.90, 3.20))
        role.move_to([P(-3.10, 0.0), P(0.60, 1.35), 0])
        self.play(Write(name), run_time=0.9)
        self.play(Create(rule), FadeIn(role), run_time=0.5)

        # THE CHROME GOES IN EARLY, NOT LAST. These two are the only content
        # in the lower band, and revealing them in the final play left the
        # bottom half of the frame empty for more than half of Ep. 17's B01 --
        # GATE V read 30% fill against a 55% floor from 25% through 80% of
        # the beat. B01 draws its own chrome because it has no title bar, and
        # the ORDER was the bug.
        ser = _t("Ep. 18", size=P(21, 19), color=SOFT)
        ser.move_to([0, CLOSE_Y, 0])
        bug = _t("@HumanitariansAI", size=P(19, 17), color=SOFT)
        bug.move_to([0, BUG_Y, 0]).align_to([X_MAX, 0, 0], RIGHT)
        self.play(FadeIn(ser), FadeIn(bug), run_time=0.45)

        cw, ch = P(5.30, 3.44), P(2.60, 2.30)
        cx, cy = P(2.95, 0.0), P(0.50, -0.70)
        card = _card(cw, ch, [cx, cy, 0])
        self.play(Create(card), run_time=0.5)

        # The card SPLITS. Landscape divides it left/right; portrait divides
        # it top/bottom, because two 1.7-unit columns would shrink the type
        # below the legibility floor. Same mobjects, same plays, different
        # coordinates -- see the aspect note at the top of this file.
        if PORTRAIT:
            split = Line([cx - cw / 2.0 + 0.10, cy, 0],
                         [cx + cw / 2.0 - 0.10, cy, 0],
                         color=RULE, stroke_width=2.2)
            a_at = [cx, cy + ch * 0.25, 0]
            b_at = [cx, cy - ch * 0.25, 0]
            half_w = cw - 0.56
        else:
            split = Line([cx, cy - ch / 2.0 + 0.10, 0],
                         [cx, cy + ch / 2.0 - 0.10, 0],
                         color=RULE, stroke_width=2.2)
            a_at = [cx - cw * 0.25, cy, 0]
            b_at = [cx + cw * 0.25, cy, 0]
            half_w = cw * 0.5 - 0.34
        self.play(Create(split), run_time=0.35)

        a1 = _fit(_t("COUNTING", size=P(27, 24), color=ACCT, weight="BOLD"),
                  half_w)
        a1.move_to([a_at[0], a_at[1] + P(0.28, 0.24), 0])
        a2 = _fit(_t("AI owns this", size=P(20, 18), color=SOFT), half_w)
        a2.move_to([a_at[0], a_at[1] - P(0.26, 0.22), 0])
        self.play(FadeIn(a1, shift=DOWN * 0.06), FadeIn(a2), run_time=0.55)

        b1 = _fit(_t("THE NUMBER", size=P(27, 24), weight="BOLD"), half_w)
        b1.move_to([b_at[0], b_at[1] + P(0.28, 0.24), 0])
        b2 = _fit(_t("it does not", size=P(20, 18), color=SOFT), half_w)
        b2.move_to([b_at[0], b_at[1] - P(0.26, 0.22), 0])
        self.play(FadeIn(b1, shift=DOWN * 0.06), FadeIn(b2), run_time=0.55)

        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — ONE BREATH  (EXECUTIVE-SUMMARY LAW: the BLUF, before any specific)
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.550, 0.719

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath.")

        cw, ch = P(10.40, 3.44), P(4.00, 4.20)
        cy = P(0.35, 0.30)
        card = _card(cw, ch, [0, cy, 0])
        self.play(Create(card), run_time=0.55)

        ys = (cy + ch * 0.30, cy, cy - ch * 0.30)
        heads = ("MORE CRATERS MEANS OLDER GROUND",
                 "YEARS NEED A CURVE",
                 "ONLY A ROCK MOVES THE CURVE")
        subs = ("density is the measurement",
                "and the curve needs dated rocks",
                None)
        for i, (h, sub, y) in enumerate(zip(heads, subs, ys)):
            col = ACCT if i == 2 else INK
            ht = _fit(_t(h, size=P(29, 22), color=col, weight="BOLD"),
                      cw - 0.70)
            ht.move_to([0, y + P(0.20, 0.17), 0])
            if sub:
                st = _fit(_t(sub, size=P(20, 17), color=SOFT), cw - 0.90)
                st.move_to([0, y - P(0.22, 0.19), 0])
                self.play(FadeIn(ht, shift=DOWN * 0.08), FadeIn(st),
                          run_time=0.6)
            else:
                self.play(FadeIn(ht, shift=DOWN * 0.08), run_time=0.6)
                self.play(Create(_underline(ht, buff=0.13)), run_time=0.35)

        closer(self, "a better counter only moves the measurement")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE RULE   plate: surface.png
# ═════════════════════════════════════════════════════════════════════════════
class B03_TheRule(Paced):
    BEAT, RT, HOLD = "B03", 1.550, 0.229

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Denser ground is older ground.",
               cite="Patches are synthetic; the 5.7x ratio is the Neukum "
                    "chronology function. See FACTCHECK F1.")

        pw = P(6.60, 2.80)
        ph = _plate_h("surface.png", pw)
        px, py = P(PLATE_X, 0.0), P(0.25, 1.90)
        plate = _plate("surface.png", pw, [px, py, 0])
        self.play(FadeIn(plate), run_time=0.7)

        # patch centres, derived from the generator's own canvas geometry
        lx = px - SURF_DX * pw
        rx = px + SURF_DX * pw
        under_y = py - ph / 2.0 - P(0.30, 0.32)
        young = _fit(_t("1.0 Ga", size=P(23, 19), color=SOFT), pw * 0.40)
        young.move_to([lx, under_y, 0])
        old = _fit(_t("3.5 Ga", size=P(23, 19), color=SOFT), pw * 0.40)
        old.move_to([rx, under_y, 0])
        self.play(FadeIn(young), FadeIn(old), run_time=0.5)

        # The counts, as a number beside a tally bar. The bars share a scale,
        # so 14 against 80 is a LENGTH the viewer reads, not two numerals to
        # compare. The second bar gets a longer run_time: the point of the
        # beat is that the old patch takes a while to fill.
        #
        # PORTRAIT PUTS THE NUMBER AND ITS BAR ON ONE LINE. Stacked
        # value-over-caption-over-bar is three rows per stat, and six rows
        # under a plate do not fit 4.64 units -- GATE B caught the "14"
        # sitting on the plate's own frame. Two rows per stat do fit.
        col_x = P(RCOL_X, 0.0)
        col_w = P(RCOL_W, 3.40)
        bar_max = P(2.90, 2.00)
        bar_l = P(RCOL_X - 1.45, -0.45)
        val_x = P(RCOL_X, -1.15)
        bh = P(0.26, 0.22)

        v1 = _fit(_t("14", size=P(58, 34), weight="BOLD"), P(3.20, 0.90))
        v1.move_to([val_x, P(1.45, 0.34), 0])
        c1 = _fit(_t(P("craters on the young patch", "on the young patch"),
                     size=P(20, 16), color=SOFT), col_w)
        c1.move_to([P(RCOL_X, 0.0), P(0.72, -0.14), 0])
        t1 = _track(bar_l, P(0.25, 0.34), bar_max, bh)
        b1 = _bar(bar_l, P(0.25, 0.34), bar_max * 14.0 / 80.0, bh)
        self.play(FadeIn(v1), FadeIn(c1), Create(t1), run_time=0.5)
        self.play(GrowFromEdge(b1, LEFT), run_time=0.35)

        v2 = _fit(_t("80", size=P(58, 34), color=ACCT, weight="BOLD"),
                  P(3.20, 0.90))
        v2.move_to([val_x, P(-0.45, -0.72), 0])
        c2 = _fit(_t(P("craters on the old one", "on the old one"),
                     size=P(20, 16), color=SOFT), col_w)
        c2.move_to([P(RCOL_X, 0.0), P(-1.18, -1.20), 0])
        t2 = _track(bar_l, P(-1.65, -0.72), bar_max, bh)
        b2 = _bar(bar_l, P(-1.65, -0.72), bar_max, bh)
        self.play(FadeIn(v2), FadeIn(c2), Create(t2), run_time=0.5)
        self.play(GrowFromEdge(b2, LEFT), run_time=0.95)

        closer(self, "every crater here is already on the ground")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — THE PILE   plate: pile.png
# ═════════════════════════════════════════════════════════════════════════════
class B04_ThePile(Paced):
    BEAT, RT, HOLD = "B04", 1.550, 0.333

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Count them all.",
               cite="Robbins & Hynek 2012 (D >= 1 km). Sub-km population: "
                    "Benedix et al. 2020.")

        pw = P(7.60, 3.40)
        ph = _plate_h("pile.png", pw)
        px, py = P(2.05, 0.0), P(0.55, 1.95)
        plate = _plate("pile.png", pw, [px, py, 0])
        self.play(FadeIn(plate), run_time=0.7)

        # THE AXIS NOTE LANDS SECOND, BEFORE ANY ROW. Without it the bars read
        # as linear and the automation gap looks like 4x instead of 78x.
        note = _fit(_t("log scale - every rail is another x10",
                       size=P(20, 17), color=SOFT), pw * 0.95)
        note.move_to([px, py - ph / 2.0 - P(0.30, 0.26), 0])
        self.play(FadeIn(note), run_time=0.45)

        col_x = P(-4.20, 0.0)
        col_w = P(3.50, 3.44)
        rows = (("7,048", "the training set", INK),
                ("384,343", "catalogued BY HAND", INK),
                ("~10 million+", "10 m to 1 km, on Mars", ACCT))
        # Landscape aligns each label to its own bar, using the generator's
        # row geometry. Portrait stacks them under the plate instead -- a
        # 3.4-wide plate leaves no column to align to.
        for i, (val, cap, col) in enumerate(rows):
            if PORTRAIT:
                ry = (0.42, -0.42, -1.26)[i]
            else:
                ry = py + PILE_DY[i] * ph
            v = _fit(_t(val, size=P(34, 27), color=col, weight="BOLD"),
                     col_w * 0.92)
            v.move_to([col_x, ry + P(0.22, 0.20), 0])
            c = _fit(_t(cap, size=P(19, 17), color=SOFT), col_w)
            c.move_to([col_x, ry - P(0.22, 0.20), 0])
            self.play(FadeIn(v, shift=LEFT * 0.08), FadeIn(c), run_time=0.55)

        closer(self, "hands stop here")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE DISAGREEMENT   plate: spread.png
# ═════════════════════════════════════════════════════════════════════════════
class B05_TheDisagreement(Paced):
    BEAT, RT, HOLD = "B05", 1.550, 0.383

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The same image. Different answers.",
               cite="Robbins et al. 2014, Icarus 234. The analysts in the "
                    "figure are synthetic; the +/-45% is theirs.")

        pw = P(3.90, 2.70)
        ph = _plate_h("spread.png", pw)
        px, py = P(-3.10, 0.0), P(0.25, 1.25)
        plate = _plate("spread.png", pw, [px, py, 0])
        self.play(FadeIn(plate), run_time=0.7)

        col_x = P(2.60, 0.0)
        col_w = P(6.20, 3.44)
        big = _fit(_t("+/-45%", size=P(76, 58), color=ACCT, weight="BOLD"),
                   col_w * 0.72)
        big.move_to([col_x, P(1.45, -0.42), 0])
        sub = _fit(_t("between EXPERT crater counters, on one image",
                      size=P(21, 18), color=SOFT), col_w)
        sub.move_to([col_x, P(0.72, -0.95), 0])
        self.play(FadeIn(big, shift=DOWN * 0.10), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.4)

        # The fill convention is taught HERE, in-beat: it cannot be read off
        # the reel's colour contract, which governs hue, not fill.
        r1 = _marker_row("every analyst marked it", [col_x, P(-0.10, -1.42), 0],
                         col_w * P(0.78, 1.00), True, size=P(21, 18))
        r2 = _marker_row("contested", [col_x, P(-0.72, -1.80), 0],
                         col_w * P(0.78, 1.00), False, size=P(21, 18))
        self.play(FadeIn(r1), run_time=0.45)
        self.play(FadeIn(r2), run_time=0.45)

        closer(self, "the disagreement is all in the small ones")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — THE MACHINE   no plate: this beat is numbers
# ═════════════════════════════════════════════════════════════════════════════
class B06_TheMachine(Paced):
    BEAT, RT, HOLD = "B06", 1.550, 0.416

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "So automate the counting.",
               cite="Silburt et al. 2019 (DeepMoon), Icarus 317. 92% is after "
                    "post-processing; 57% is the raw network.")

        bar_l = P(-2.40, -1.58)
        bar_w = P(8.30, 3.16)
        bar_h = P(0.52, 0.40)
        cap_x = P(-4.40, 0.52)
        cap_w = P(3.20, 2.05)

        # PORTRAIT PUTS THE VALUE AND ITS CAPTION ON ONE LINE ABOVE THE BAR.
        # Stacked, the 36 pt numeral and its caption leave under 0.1 units
        # between them and the next bar, and the third element of the beat
        # (the 42% line) ran off the right edge at x = 2.10 on a +-1.80
        # frame. Side by side, each bar needs one row instead of two.
        # Bar one: the headline.
        y1 = P(1.55, 1.70)
        c1 = _fit(_t("recall, AFTER post-processing", size=P(20, 16),
                     color=SOFT), cap_w)
        v1 = _fit(_t("92%", size=P(46, 34), weight="BOLD"), P(1.76, 0.80))
        if PORTRAIT:
            c1.move_to([cap_x, y1 + 0.60, 0])
            v1.move_to([-1.20, y1 + 0.60, 0])
        else:
            c1.move_to([cap_x, y1 - 0.30, 0])
            v1.move_to([cap_x, y1 + 0.24, 0])
        t1 = _track(bar_l, y1, bar_w, bar_h)
        b1 = _bar(bar_l, y1, bar_w * 0.92, bar_h)
        self.play(FadeIn(v1), FadeIn(c1), Create(t1), run_time=0.6)
        self.play(GrowFromEdge(b1, LEFT), run_time=0.7)

        # Bar two: the number the headline is usually quoted without. GHOSTED
        # BUT LEGIBLE -- it is evidence, not decoration, so it gets the same
        # type colour and only its FILL is dropped.
        y2 = P(0.30, 0.45)
        c2 = _fit(_t(P("the raw network, before post-processing",
                       "the raw network, before that"),
                     size=P(20, 16), color=SOFT), cap_w)
        v2 = _fit(_t("57%", size=P(46, 34), weight="BOLD"), P(1.76, 0.80))
        if PORTRAIT:
            c2.move_to([cap_x, y2 + 0.60, 0])
            v2.move_to([-1.20, y2 + 0.60, 0])
        else:
            c2.move_to([cap_x, y2 - 0.30, 0])
            v2.move_to([cap_x, y2 + 0.24, 0])
        t2 = _track(bar_l, y2, bar_w, bar_h)
        b2 = _bar(bar_l, y2, bar_w * 0.57, bar_h, opacity=0.38, stroke=2.0)
        self.play(FadeIn(v2), FadeIn(c2), Create(t2), run_time=0.6)
        self.play(GrowFromEdge(b2, LEFT), run_time=0.55)

        # THE 42% ROW SITS WELL CLEAR OF THE 57% CAPTION. At its first
        # landscape position the numeral's box touched that caption's by
        # 0.03 units -- three pixels short of contact at 4K -- and GATE B
        # passed it, because the two land in different plays and the audit
        # samples frames, not every pair of mobjects that ever coexist.
        # Found by reading a rendered frame. It also fills the lower band,
        # which was otherwise dead space under FILL-THE-CANVAS LAW.
        n = _fit(_t("42%", size=P(54, 42), color=ACCT, weight="BOLD"),
                 P(2.00, 1.40))
        n.move_to([P(-4.00, 0.0), P(-0.95, -0.30), 0])
        nc = _fit(_t(P("of what it returned had never been catalogued",
                       "of what it found had never\nbeen catalogued"),
                     size=P(23, 18), color=INK), P(7.00, 3.30))
        nc.move_to([P(1.10, 0.0), P(-0.95, -1.10), 0])
        self.play(FadeIn(n, shift=UP * 0.10), FadeIn(nc), run_time=0.65)

        closer(self, "this half is perception - and perception is AI's")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — THE CURVE   plate: curve.png
# ═════════════════════════════════════════════════════════════════════════════
class B07_TheCurve(Paced):
    BEAT, RT, HOLD = "B07", 1.550, 0.411

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Density is a lookup, not a date.",
               cite="Neukum chronology function: N(1) = 5.44e-14 (exp(6.93 T) "
                    "- 1) + 8.38e-4 T.")

        pw = P(6.20, 3.00)
        ph = _plate_h("curve.png", pw)
        px, py = P(PLATE_X, 0.0), P(0.35, 1.72)
        plate = _plate("curve.png", pw, [px, py, 0])
        self.play(FadeIn(plate), run_time=0.7)

        ax = _fit(_t("age of the surface, billions of years ->",
                     size=P(20, 16), color=SOFT), pw * 0.98)
        ax.move_to([px, py - ph / 2.0 - P(0.30, 0.26), 0])
        self.play(FadeIn(ax), run_time=0.45)

        col_x = P(RCOL_X, 0.0)
        col_w = P(RCOL_W, 3.44)

        ya = _fit(_t("y: craters per km2, log", size=P(19, 16), color=SOFT),
                  col_w)
        ya.move_to([col_x, P(1.85, 0.26), 0])
        self.play(FadeIn(ya), run_time=0.4)

        # PORTRAIT PUTS EACH HEAD BESIDE ITS SUB, NOT ABOVE IT. Eight stacked
        # rows under the plate leave well under 0.15 units between them, and
        # the axis caption landed on top of the y-axis caption outright.
        # Four rows of two fit; eight rows of one do not.
        hx, sx = P(RCOL_X, -1.00), P(RCOL_X, 0.75)
        hw, sw_ = P(RCOL_W, 1.45), P(RCOL_W, 1.60)

        r1h = _fit(_t("THE FLAT MIDDLE", size=P(24, 19), weight="BOLD"), hw)
        r1h.move_to([hx, P(1.25, -0.30), 0])
        r1s = _fit(_t("a slow, steady clock", size=P(19, 16), color=SOFT),
                   sw_)
        r1s.move_to([sx, P(0.88, -0.30), 0])
        self.play(FadeIn(r1h, shift=LEFT * 0.06), FadeIn(r1s), run_time=0.55)

        r2h = _fit(_t("THE STEEP END", size=P(24, 19), color=ACCT,
                      weight="BOLD"), hw)
        r2h.move_to([hx, P(0.28, -0.90), 0])
        r2s = _fit(_t("the early bombardment", size=P(19, 16), color=SOFT),
                   sw_)
        r2s.move_to([sx, P(-0.09, -0.90), 0])
        self.play(FadeIn(r2h, shift=LEFT * 0.06), FadeIn(r2s), run_time=0.55)

        big = _fit(_t("96%", size=P(60, 40), color=ACCT, weight="BOLD"),
                   P(2.06, 1.10))
        big.move_to([P(RCOL_X, -1.05), P(-0.80, -1.60), 0])
        cap = _fit(_t(P("of a 4.1 Ga surface's craters\nlanded in its first "
                        "600 Myr",
                        "of an old surface's craters\nlanded in its first\n"
                        "600 Myr"), size=P(19, 15), color=SOFT),
                   P(RCOL_W, 2.00))
        cap.move_to([P(RCOL_X, 0.55), P(-1.46, -1.60), 0])
        self.play(FadeIn(big, shift=UP * 0.08), FadeIn(cap), run_time=0.65)

        closer(self, "the clock runs fast early and crawls late")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — WHAT IT COSTS   plate: cost.png      THE LOAD-BEARING BEAT
# ═════════════════════════════════════════════════════════════════════════════
class B08_WhatItCosts(Paced):
    BEAT, RT, HOLD = "B08", 1.550, 0.323

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The same error, twice.",
               cite="+/-45%: Robbins et al. 2014. Curve: Neukum chronology "
                    "function. Windows asserted in gen_craters.py (C2, C3).")

        pw = P(6.20, 2.60)
        ph = _plate_h("cost.png", pw)
        px, py = P(PLATE_X, 0.0), P(0.35, 1.80)
        plate = _plate("cost.png", pw, [px, py, 0])
        self.play(FadeIn(plate), run_time=0.7)

        note = _fit(_t(P("the SAME +/-45% counting error, both times",
                         "the SAME +/-45% error, both times"),
                       size=P(20, 16), color=SOFT), pw * 0.98)
        note.move_to([px, py - ph / 2.0 - P(0.30, 0.26), 0])
        self.play(FadeIn(note), run_time=0.45)

        col_x = P(RCOL_X, 0.0)
        col_w = P(RCOL_W, 3.44)

        # ORDER MATCHES THE PLATE. cost.png draws the 1.0 Ga bar above the
        # 3.5 Ga bar (COST_DY), so the column reads in the same order and
        # each row states its own age -- the reader never has to infer which
        # bar a number belongs to.
        #
        # PORTRAIT PUTS "of the answer" BESIDE THE NUMERAL. Six stacked rows
        # under a 1.93-unit plate collided outright: GATE B found the axis
        # note sitting on "ground 1.0 Ga old" at 73% overlap.
        vx, sx = P(RCOL_X, -0.70), P(RCOL_X, 0.95)
        vw, sw_ = P(RCOL_W * 0.62, 1.20), P(RCOL_W, 1.50)

        a_cap = _fit(_t("ground 1.0 Ga old", size=P(21, 17), color=SOFT),
                     col_w)
        a_cap.move_to([col_x, P(1.55, 0.36), 0])
        a_val = _fit(_t("90%", size=P(64, 44), color=ACCT, weight="BOLD"), vw)
        a_val.move_to([vx, P(0.88, -0.22), 0])
        a_sub = _fit(_t("of the answer", size=P(20, 16), color=SOFT), sw_)
        a_sub.move_to([sx, P(0.38, -0.22), 0])
        self.play(FadeIn(a_cap), run_time=0.4)
        self.play(FadeIn(a_val, shift=DOWN * 0.10), FadeIn(a_sub),
                  run_time=0.65)

        b_cap = _fit(_t("ground 3.5 Ga old", size=P(21, 17), color=SOFT),
                     col_w)
        b_cap.move_to([col_x, P(-0.45, -0.82), 0])
        b_val = _fit(_t("16%", size=P(64, 44), weight="BOLD"), vw)
        b_val.move_to([vx, P(-1.12, -1.40), 0])
        b_sub = _fit(_t("of the answer", size=P(20, 16), color=SOFT), sw_)
        b_sub.move_to([sx, P(-1.62, -1.40), 0])
        self.play(FadeIn(b_cap), run_time=0.4)
        self.play(FadeIn(b_val, shift=DOWN * 0.10), FadeIn(b_sub),
                  run_time=0.65)

        closer(self, "consistency buys the most on young ground")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — THE GAP   plate: anchors.png
# ═════════════════════════════════════════════════════════════════════════════
class B09_TheGap(Paced):
    BEAT, RT, HOLD = "B09", 1.550, 0.148

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What the curve is nailed to.",
               cite="Anchor ages after Stoffler & Ryder 2001 (positions "
                    "illustrative). Chang'e-5: Li et al. 2021, Nature 600.")

        pw = P(9.60, 3.40)
        ph = _plate_h("anchors.png", pw)
        px, py = 0.0, P(0.25, 1.40)
        plate = _plate("anchors.png", pw, [px, py, 0])
        self.play(FadeIn(plate), run_time=0.7)

        top_y = py + ph / 2.0 + P(0.34, 0.30)
        ce5 = _fit(_t("Chang'e-5, 2.030 Ga", size=P(21, 17), color=INK),
                   P(3.20, 2.40))
        ce5.move_to([px + ANC_CE5 * pw, top_y, 0])

        under_y = py - ph / 2.0 - P(0.34, 0.30)
        if PORTRAIT:
            # 3.6 units of frame cannot hold three labels side by side, so
            # portrait stacks them. Same three plays either way.
            lab_pos = [(0.0, under_y), (0.0, under_y - 0.52),
                       (0.0, under_y - 1.04)]
            lab_w = 3.40
        else:
            lab_pos = [(px + ANC_OLD * pw, under_y),
                       (px + ANC_GAP * pw, under_y),
                       (px + ANC_YOUNG * pw, under_y)]
            lab_w = 3.10

        l_old = _fit(_t("Apollo + Luna", size=P(22, 19), color=SOFT), lab_w)
        l_old.move_to([lab_pos[0][0], lab_pos[0][1], 0])
        self.play(FadeIn(l_old), run_time=0.45)

        l_young = _fit(_t("a few dated craters", size=P(22, 19), color=SOFT),
                       lab_w)
        l_young.move_to([lab_pos[2][0], lab_pos[2][1], 0])
        self.play(FadeIn(l_young), run_time=0.45)

        l_gap = _fit(_t("1 - 3 Ga: NO ANCHOR", size=P(24, 20), color=ACCT,
                        weight="BOLD"), lab_w)
        l_gap.move_to([lab_pos[1][0], lab_pos[1][1], 0])
        self.play(FadeIn(l_gap, shift=UP * 0.08), run_time=0.55)

        self.play(FadeIn(ce5, shift=DOWN * 0.10), run_time=0.55)

        closer(self, "for two billion years, nothing held it")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE TELL   no plate: the counted window against the rock
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    BEAT, RT, HOLD = "B10", 1.550, 0.186

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Not wrong. Loose.",
               cite="Counted window: Qiao et al. 2021, GRL. Rock: Li et al. "
                    "2021. Curve shift: Yue et al. 2022, Nature Astronomy.")

        track_l = P(-4.60, -1.62)
        track_w = P(9.20, 3.24)
        bar_h = P(0.42, 0.34)

        c1 = _fit(_t("what counting said about one plain", size=P(21, 18),
                     color=SOFT), track_w)
        c1.move_to([track_l + track_w / 2.0, P(2.20, 2.30), 0])
        b1 = _bar(track_l, P(1.70, 1.84), track_w, bar_h)
        self.play(FadeIn(c1), run_time=0.4)
        self.play(GrowFromEdge(b1, LEFT), run_time=0.75)

        v1 = _fit(_t("1.3 - 2.7 Ga   =   a 1,400 Myr window", size=P(22, 18),
                     color=INK), track_w * 0.96)
        v1.move_to([track_l + track_w / 2.0, P(1.18, 1.40), 0])
        self.play(FadeIn(v1), run_time=0.45)

        # THE TICK IS DRAWN TO TRUE SCALE. 8 Myr against a 1,400 Myr bar is
        # 1/175 of its width -- 16 px at 4K landscape, 11 px at 4K portrait.
        # Both are plainly visible, so there is no reason to cheat it wider,
        # and cheating it would destroy the one comparison the beat exists to
        # make. Its x position is where 2.030 Ga actually falls inside the
        # counted window: (2.030 - 1.3) / 1.4 of the way along.
        c2 = _fit(_t("what the returned rock said", size=P(21, 18),
                     color=SOFT), track_w)
        c2.move_to([track_l + track_w / 2.0, P(0.62, 0.72), 0])
        tick_x = track_l + track_w * (2.030 - 1.3) / 1.4
        b2 = _bar(tick_x - track_w / 350.0, P(0.10, 0.24),
                  track_w / 175.0, bar_h, col=INK)
        g2 = _track(track_l, P(0.10, 0.24), track_w, bar_h)
        self.play(FadeIn(c2), Create(g2), run_time=0.5)
        self.play(GrowFromEdge(b2, LEFT), run_time=0.4)

        v2 = _fit(_t("2.030 +/- 0.004 Ga   =   8 Myr", size=P(22, 18),
                     color=INK), track_w * 0.96)
        v2.move_to([track_l + track_w / 2.0, P(-0.42, -0.26), 0])
        self.play(FadeIn(v2), run_time=0.45)

        # THESE TWO ARE STACKED, NOT SIDE BY SIDE. Landscape originally put
        # "175x tighter" at x = -2.30 and the counterweight at x = +2.10 on
        # one line; the counterweight is a 54-character sentence, so after
        # _fit it ran from -1.70 to 5.90 and the two overlapped by 1.5 units.
        # GATE B passed it -- 20/20, strict -- and a rendered frame did not.
        big = _fit(_t("175x tighter", size=P(50, 38), color=ACCT,
                      weight="BOLD"), P(5.60, 3.20))
        big.move_to([0.0, P(-1.05, -0.92), 0])
        self.play(FadeIn(big, shift=UP * 0.10), run_time=0.6)

        # The counterweight. Ghosted in WEIGHT, never in contrast: SOFT is
        # 4.7:1 on cream. It weakens the headline and it ships as a reveal.
        cw = _fit(_t("and the new anchor moved the curve by at most 0.24 Gyr",
                     size=P(20, 17), color=SOFT), P(9.00, 3.44))
        cw.move_to([0.0, P(-1.70, -1.56), 0])
        self.play(FadeIn(cw), run_time=0.5)

        closer(self, "counting was never wrong - it was loose")
        self.hold_to_beat()
