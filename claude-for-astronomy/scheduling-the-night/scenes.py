"""scenes.py - Manim scenes for scheduling-the-night.

*Finish What You Start.* - ai-explainer, claude-hai, Ep. 17.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL
  Terracotta is THE PLANNER - the thing being examined. Ink is GREEDY, the
  fixed reference it is measured against.

    B06  the planner's block tour       against greedy's wander
    B08  the planner's started fields   against greedy's, holes and all
    B10  the planner's airmass          against greedy's

  B06 teaches the mapping once, with both dials side by side and labelled
  OUTSIDE the plate, and it never flips afterwards.

  TWO LOCAL EXCEPTIONS, both taught in-beat because they cannot be read off
  the contract:
    B03  terracotta marks three HIGHLIGHTED FIELDS. No scheduler exists yet
         at B03 - the beat is the board, before anyone has moved.
    B09  the terracotta CURVE is greedy-under-payment, and marker FILL is the
         price: filled = exposure rate held, hollow = rate given up. The beat
         says this out loud, because a hollow marker means nothing otherwise.

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
  Every plate comes from assets/gen_sched.py, which runs the REAL experiment:
  a simulated 8-hour night at -30 deg, 450 paired request sets on a Fibonacci
  sphere, Kasten-Young airmass, a trapezoidal alt-az slew model, and two
  schedulers - a myopic greedy rule maximising instantaneous volumetric
  survey speed, and a block planner that solves an Integer Linear Program
  (scipy/HiGHS) and then orders each block with a 2-opt tour.

  SIX claims are ASSERTED and the generator writes nothing if any fails.

  THE DECISIVE NUMBER IS A FRACTION, NOT A RATE. Sequence completion - of the
  fields a scheduler STARTED, how many did it finish - is the measurement
  ZTF's own paper leans on, and it is the only one that separates the two
  schedulers here. Exposures per hour are 90.5 against 90.0 and say nothing.

  THE EPISODE SHIPS ITS OWN COUNTER-EXPERIMENT. B09 is a finish-bonus sweep
  that PAYS greedy to care about completing pairs. It climbs to 0.975. That
  weakens the clean version of the story, so it is a beat rather than a
  footnote - see FACTCHECK F12.

  A PLATE WAS REDRAWN. completion.png began as four bars (completion and
  rate, two schedulers). With no tick labels - plates carry imagery only -
  four floating slabs are unreadable. What ships is one square per STARTED
  field, hollow where the pair was stranded, which needs no axis at all.
  tour.png also changed: its dots were coloured by BAND, and because each
  block happens to be single-band that read as a scheduler encoding and
  fought every other plate. Dots are now coloured by scheduler.

PLATE GEOMETRY - ph = pw * (ih/iw). Do this arithmetic, do not assume it.
      window  1560x780  0.5000     tour    1560x780  0.5000
      completion 1560x780 0.5000   bonus   1560x780  0.5000
      airmass 1560x780  0.5000
  The landscape figure band is 4.30 units tall, so a 0.50 plate runs at
  pw 6.6 (3.30 tall) where nothing sits under it, and pw 6.2 (3.10) on the
  beats that need a label row beneath the plate.

GATE NOTES (learned the expensive way on Eps. 03-16)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - Never position a label from another Text's .width either - same reason.
    Position from the CONTAINER.
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - _strike() centres on the MEDIAN glyph top/bottom, i.e. the x-height band,
    NOT on get_center(). A bbox centre rises with ascenders, so on Ep. 16's
    B01 the rule struck the tops of the letters - and the same code looked
    correct on a string that happened to contain a descender. A text-geometry
    bug is STRING-DEPENDENT; it survives a frame check on the wrong sentence.
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
    character and Ep. 09 rendered it as stray digits on screen. This reel uses
    the word ALLOWED and a struck row instead of tick/cross marks.
  - Leave >= 0.15 units between any two elements. A gap of 0.04 is eleven
    pixels at 4K and reads as contact.
  - Give every scene its footer EARLY. GATE V samples each beat at 50% and
    85%.
  - Same-colour-on-same-colour is invisible to EVERY gate. Read the frames.
  - Prefer SOFT over GHOST for any LARGE field of marks. A contrast margin
    that depends on elements portrait DROPS is not a margin.
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
    # THE GAP IS LOAD-BEARING. The label is CENTRED, so with the old
    # inner = w - 0.46 about x = at + 0.11 a label that filled its width had
    # its left edge at exactly at - w/2 + 0.34 -- which is the swatch's RIGHT
    # edge. Short labels centred with slack and looked fine; the one long
    # label in the reel (B03's third row) rendered with its first letter
    # welded to the chip. No gate sees it: the swatch and the label are
    # separate mobjects that merely touch. Reserve 0.10 between them and
    # centre the label in what is left.
    inner = w - 0.44
    if val is None:
        _fit(lab, inner)
        lab.move_to([at[0] + 0.22, at[1], 0])
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

# Plate-internal x offsets from the plate CENTRE, as a fraction of plate
# width, DERIVED from gen_sched.py's own geometry rather than eyeballed.
#
# completion.png: two 20-column grids, pitch 30 px, first dot centres at
# x = 120 and x = 840 on a 1560-wide plate, so the blocks centre on 405 and
# 1125.
COMP_BLOCK_FX = (-0.2404, +0.2212)
# tour.png: the two alt-az dials centre at 0.26 and 0.74 of the width.
TOUR_DIAL_FX = (-0.2400, +0.2400)

# Those fractions are used ONLY to derive the per-aspect label positions
# below, which are then written out as literals. A label OUTSIDE a plate is
# never positioned as `plate_x +- pw * k`: in portrait pw is 3.44 and a
# fraction that is harmless in landscape walks straight off a 3.6-unit frame.
DIAL_X = P(1.344, 0.826)        # tour.png, +-0.24 of pw 5.6 / 3.44
COMP_L_X = P(-1.394, -0.827)    # completion.png, left grid
COMP_R_X = P(+1.283, +0.761)    # completion.png, right grid

# ── Numbers the scenes put on screen ─────────────────────────────────────────
# Every one is printed and ASSERTED by assets/gen_sched.py, kept here as named
# constants so a changed experiment cannot silently disagree with a label.
N_ORDER = "10^2567"            # COMPUTED: log10(1000!) = 2567.6
N_ATOMS = "10^80"              # standard scale anchor, see FACTCHECK F2
RUBIN_TICK = "EVERY 30 SECONDS"  # PUBLISHED: SMTN-020, verbatim
N_BLOCKS = "16 BLOCKS"         # this simulation's night: 8 h / 30 min
G_STARTED = "401 STARTED"      # MEASURED
G_STRAND = "78 STRANDED"       # MEASURED
P_STARTED = "360 STARTED"      # MEASURED
P_STRAND = "0 STRANDED"        # MEASURED
G_RATE = "90.5 /h"             # MEASURED
P_RATE = "90.0 /h"             # MEASURED
G_X = "1.7"                    # MEASURED, one decimal: see FACTCHECK F10
P_X = "1.3"                    # MEASURED, one decimal
BONUS_TOP = "0.975"            # MEASURED: greedy, finish-bonus 20x
ZTF_FILT_G = "2.0"             # PUBLISHED: ZTF greedy, filter changes/night
ZTF_FILT_I = "3.6"             # PUBLISHED: ZTF ILP, filter changes/night

CITE_ZTF = "Bellm et al. 2019, PASP 131 068003 (ZTF surveys & scheduler)"
CITE_RUBIN = "Jones et al., SMTN-020 (Rubin Feature Based Scheduler)"
CITE_SIM = "simulated night: 450 paired requests, 8 h, -30 deg - assets/gen_sched.py"


def _rows_at(n):
    """Y positions for n label rows: a right-hand column in landscape, a
    stack beneath the plate in portrait. Positions are literals per aspect,
    never derived from a plate's measured height."""
    if PORTRAIT:
        base = (0.05, -0.42, -0.89, -1.36)
    else:
        base = (1.16, 0.38, -0.40, -1.18)
    return base[:n]


def _row_x():
    return P(RCOL_X, 0.0)


def _row_w():
    return P(RCOL_W, 3.40)


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — THE PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 1.550, 0.235

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
        # bottom half of the frame empty for 4.6 s of an 8.4 s beat -- GATE V
        # read 30% fill against a 55% floor from 25% through 80% of the beat.
        # Every other beat lays its chrome down first, via chrome(); B01 draws
        # its own because it has no title bar, and the order was the bug.
        # Same play count and the same run_times, so the pacing solve stands.
        ser = _t("Ep. 17", size=P(21, 19), color=SOFT)
        ser.move_to([0, CLOSE_Y, 0])
        bug = _t("@HumanitariansAI", size=P(19, 17), color=SOFT)
        bug.move_to([0, BUG_Y, 0]).align_to([X_MAX, 0, 0], RIGHT)
        self.play(FadeIn(ser), FadeIn(bug), run_time=0.45)

        cw, ch = P(5.30, 3.44), P(2.60, 2.10)
        cx, cy = P(2.95, 0.0), P(0.50, -0.60)
        card = _card(cw, ch, [cx, cy, 0])
        self.play(Create(card), run_time=0.5)

        r1 = _fit(_t("big enough to look like AI's job", size=P(23, 19)),
                  cw - 0.64)
        r1.move_to([cx, cy + ch * 0.23, 0])
        s1 = _strike(r1)
        r2 = _fit(_t("a constraint, not a guess", size=P(23, 19), color=ACCT,
                     weight="BOLD"), cw - 0.78)
        r2.move_to([cx, cy - ch * 0.21, 0])
        box = RoundedRectangle(width=cw - 0.44, height=P(0.66, 0.58),
                               corner_radius=0.10, color=ACC, stroke_width=2.4,
                               fill_opacity=0).move_to([cx, cy - ch * 0.21, 0])
        self.play(FadeIn(r1), run_time=0.5)
        self.play(Create(s1), run_time=0.4)
        self.play(FadeIn(r2), Create(box), run_time=0.6)

        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — ONE BREATH
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.550, 0.568

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath.")

        cw, ch = P(10.40, 3.44), P(4.00, 4.20)
        cy = P(0.35, 0.30)
        card = _card(cw, ch, [0, cy, 0])
        self.play(Create(card), run_time=0.55)

        ys = (cy + ch * 0.30, cy, cy - ch * 0.30)
        heads = ("A NIGHT IS AN ORDER",
                 "THE ORDERS CANNOT BE SEARCHED",
                 "SO CHANGE WHAT A MOVE IS")
        subs = ("a few thousand exposures, one sequence",
                "not a big space - no space at all",
                None)
        for i, (h, sub, y) in enumerate(zip(heads, subs, ys)):
            col = ACCT if i == 2 else INK
            ht = _fit(_t(h, size=P(29, 23), color=col, weight="BOLD"),
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

        closer(self, "where to point, decided before any photon arrives")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE BOARD
# ═════════════════════════════════════════════════════════════════════════════
class B03_TheBoard(Paced):
    BEAT, RT, HOLD = "B03", 1.550, 0.253
    RT_PORTRAIT = None

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "A night is a moving window.", CITE_SIM)

        pw = P(6.20, 3.44)
        px, py = P(PLATE_X, 0.0), P(0.25, 1.28)
        plate = _plate("window.png", pw, [px, py, 0])
        self.play(FadeIn(plate), run_time=0.8)

        rx, rw = _row_x(), _row_w()
        ys = _rows_at(3)
        rows = [
            ("each curve is one field", SOFT),
            ("three of them, highlighted", ACC),
            ("below 20 deg: cannot point", GHOST),
        ]
        for (txt, col), y in zip(rows, ys):
            self.play(FadeIn(_swatch_row(txt, col, [rx, y, 0], rw,
                                         size=P(19, 18))), run_time=0.5)

        closer(self, "this is the board, not the game")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — THE NUMBER
# ═════════════════════════════════════════════════════════════════════════════
class B04_TheNumber(Paced):
    BEAT, RT, HOLD = "B04", 1.550, 0.514

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "How many orders is that?")

        top = _fit(_t("1000 EXPOSURES", size=P(32, 26), color=INK,
                      weight="BOLD"), P(6.0, 3.30))
        top.move_to([0, P(1.80, 2.00), 0])
        self.play(FadeIn(top, shift=DOWN * 0.10), run_time=0.6)

        big = _fit(_t(N_ORDER, size=P(96, 70), color=ACCT, weight="BOLD"),
                   P(6.4, 3.30))
        big.move_to([0, P(0.60, 0.95), 0])
        lab = _fit(_t("ORDERINGS", size=P(26, 22), color=SOFT), P(5.0, 3.20))
        lab.move_to([0, P(-0.28, 0.14), 0])
        self.play(FadeIn(big, scale=1.05), run_time=0.8)
        self.play(FadeIn(lab), run_time=0.35)

        hair = Line([-P(4.6, 1.62), P(-0.80, -0.44), 0],
                    [P(4.6, 1.62), P(-0.80, -0.44), 0],
                    color=RULE, stroke_width=2.4)
        atoms = _fit(_t("the whole observable universe holds " + N_ATOMS
                        + " atoms",
                        size=P(26, 20), color=SOFT), P(8.4, 3.36))
        atoms.move_to([0, P(-1.24, -0.88), 0])
        self.play(Create(hair), run_time=0.35)
        self.play(FadeIn(atoms), run_time=0.55)

        closer(self, "NOT A BIG SEARCH. NOT A SEARCH.")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — RUBIN'S MOVE
# ═════════════════════════════════════════════════════════════════════════════
class B05_RubinsMove(Paced):
    BEAT, RT, HOLD = "B05", 1.550, 0.339

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Rubin shrinks the move to NOW.", CITE_RUBIN)

        side = P(1.52, 0.88)
        gap = P(0.56, 0.16)
        xs = [-(side + gap), 0.0, (side + gap)]
        ytop = P(1.42, 1.88)
        # A label that _fit() has to scale sits at a different size from
        # its neighbours and reads as a mistake. Portrait gets the short
        # word so all three stay at one size.
        names = ("SLEW", "DEPTH", P("COVERAGE OWED", "COVERAGE"))

        maps = []
        for x, nm in zip(xs, names):
            sq = RoundedRectangle(width=side, height=side, corner_radius=0.10,
                                  color=GHOST, stroke_width=1.8,
                                  fill_color=GHOST, fill_opacity=0.30)
            sq.move_to([x, ytop, 0])
            lb = _fit(_t(nm, size=P(18, 14), color=SOFT), side + gap * 0.6)
            lb.move_to([x, ytop - side / 2.0 - P(0.30, 0.26), 0])
            maps.append(VGroup(sq, lb))
        self.play(*[FadeIn(m) for m in maps], run_time=0.75)

        plus = VGroup(*[_t("+", size=P(28, 20), color=SOFT).move_to(
            [(xs[i] + xs[i + 1]) / 2.0, ytop, 0]) for i in range(2)])
        wts = _fit(_t("x weights", size=P(19, 15), color=ACCT),
                   P(3.0, 1.70))
        wts.move_to([P(3.95, 0.0), P(1.42, 0.80), 0])
        self.play(FadeIn(plus), FadeIn(wts), run_time=0.5)

        ybot = P(-0.78, -0.30)
        comb = RoundedRectangle(width=side, height=side, corner_radius=0.10,
                                color=ACC, stroke_width=2.2,
                                fill_color=ACC, fill_opacity=0.22)
        comb.move_to([0, ybot, 0])
        clab = _fit(_t("COMBINED REWARD", size=P(18, 14), color=SOFT),
                    P(3.0, 2.00))
        clab.move_to([0, ybot - side / 2.0 - P(0.30, 0.26), 0])
        self.play(FadeIn(comb), FadeIn(clab), run_time=0.6)

        ring = Circle(radius=P(0.20, 0.13), color=ACC, stroke_width=5,
                      fill_opacity=0)
        ring.move_to([P(0.34, 0.20), ybot + P(0.26, 0.15), 0])
        self.play(Create(ring), run_time=0.45)

        tick = _chip(RUBIN_TICK, size=P(19, 15), max_w=P(3.3, 2.10))
        tick.move_to([P(3.95, 0.0), P(-0.78, -1.44), 0])
        self.play(FadeIn(tick), run_time=0.45)

        closer(self, "highest reward wins. no lookahead.")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — ZTF'S MOVE   (teaches the colour contract)
# ═════════════════════════════════════════════════════════════════════════════
class B06_ZtfsMove(Paced):
    BEAT, RT, HOLD = "B06", 1.550, 0.670

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "ZTF shrinks it to WHICH BLOCK.", CITE_ZTF)

        n = 16
        bw = P(0.56, 0.19)
        bh = P(0.34, 0.24)
        gap = P(0.09, 0.034)
        y0 = P(2.06, 2.26)
        x0 = -((n - 1) * (bw + gap)) / 2.0
        blocks = VGroup(*[
            Rectangle(width=bw, height=bh, color=GHOST, stroke_width=1.5,
                      fill_color=CARD, fill_opacity=1.0).move_to(
                [x0 + i * (bw + gap), y0, 0]) for i in range(n)])
        self.play(FadeIn(blocks), run_time=0.6)

        lit = Rectangle(width=bw, height=bh, color=ACC, stroke_width=2.4,
                        fill_color=ACC, fill_opacity=0.85).move_to(
            [x0 + 8 * (bw + gap), y0, 0])
        nb = _fit(_t(N_BLOCKS + ", one filter each", size=P(19, 15),
                     color=SOFT), P(6.0, 3.20))
        nb.move_to([0, y0 - bh / 2.0 - P(0.30, 0.26), 0])
        self.play(FadeIn(lit), FadeIn(nb), run_time=0.55)

        # pw 5.6, not 6.6: at 6.6 the plate's top edge sits at y 1.71 and
        # swallows the "16 blocks" sub-label at 1.59 completely. Nothing
        # catches that - a plate is opaque and GATE B is blind to its inside.
        pw = P(5.60, 3.44)
        py = P(-0.16, 0.52)
        plate = _plate("tour.png", pw, [0, py, 0])
        self.play(FadeIn(plate), run_time=0.8)

        ylab = P(-1.84, -1.52)
        gl = _fit(_t("GREEDY", size=P(23, 19), color=INK, weight="BOLD"),
                  P(2.6, 1.40))
        gl.move_to([-DIAL_X, ylab, 0])
        pl = _fit(_t("PLANNER", size=P(23, 19), color=ACCT, weight="BOLD"),
                  P(2.6, 1.40))
        pl.move_to([DIAL_X, ylab, 0])
        self.play(FadeIn(gl), FadeIn(pl), run_time=0.55)

        closer(self, "choosing the SET is the hard half")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — THE EQUALS SIGN
# ═════════════════════════════════════════════════════════════════════════════
class B07_TheEqualsSign(Paced):
    BEAT, RT, HOLD = "B07", 1.550, 0.146

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "One constraint does the work.", CITE_ZTF)

        gy = P(1.78, 2.20)
        gchip = _quiet_chip("one GREEN exposure", size=P(20, 16),
                            max_w=P(3.8, 3.30))
        gchip.move_to([P(-1.90, 0.0), gy, 0])
        rchip = _quiet_chip("one RED exposure", size=P(20, 16),
                            max_w=P(3.8, 3.30))
        rchip.move_to([P(1.90, 0.0), P(gy, gy - 0.54), 0])
        self.play(FadeIn(gchip), FadeIn(rchip), run_time=0.6)
        pairlab = _fit(_t("= ONE REQUEST", size=P(21, 17), color=SOFT),
                       P(3.4, 3.20))
        pairlab.move_to([P(4.40, 0.0), P(gy, gy - 1.02), 0])
        self.play(FadeIn(pairlab), run_time=0.4)

        cw, ch = P(9.00, 3.40), P(2.10, 1.86)
        cy = P(-0.10, -0.20)
        card = _card(cw, ch, [0, cy, 0])
        self.play(Create(card), run_time=0.45)

        rows = (("TAKE BOTH", "allowed", INK, False),
                ("TAKE NEITHER", "allowed", INK, False),
                ("TAKE ONE", "forbidden", ACCT, True))
        ys = (cy + ch * 0.31, cy, cy - ch * 0.31)
        for (head, tail, col, struck), y in zip(rows, ys):
            line = _fit(_t(head + "   -   " + tail, size=P(24, 19), color=col,
                           weight="BOLD" if struck else None), cw - 0.70)
            line.move_to([0, y, 0])
            self.play(FadeIn(line), run_time=0.45)
            if struck:
                self.play(Create(_strike(line)), run_time=0.4)

        eq = _fit(_t("sum_t Y[r,t,f]  =  n_req[r,f] . Z[r]", size=P(22, 17),
                     color=ACCT), P(7.0, 3.30))
        eq.move_to([0, P(-1.62, -1.40), 0])
        self.play(FadeIn(eq), run_time=0.5)

        closer(self, "that is an equals sign, not a preference")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — WHAT IT BOUGHT
# ═════════════════════════════════════════════════════════════════════════════
class B08_WhatItBought(Paced):
    BEAT, RT, HOLD = "B08", 1.550, 0.651

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "One square per field it STARTED.", CITE_SIM)

        ytop = P(2.10, 2.22)
        gl = _fit(_t("GREEDY", size=P(23, 18), color=INK, weight="BOLD"),
                  P(2.4, 1.30))
        gl.move_to([COMP_L_X, ytop, 0])
        g2 = _fit(_t(G_STARTED, size=P(19, 15), color=SOFT), P(2.4, 1.30))
        g2.move_to([COMP_L_X, ytop - P(0.34, 0.29), 0])
        pl = _fit(_t("PLANNER", size=P(23, 18), color=ACCT, weight="BOLD"),
                  P(2.4, 1.30))
        pl.move_to([COMP_R_X, ytop, 0])
        p2 = _fit(_t(P_STARTED, size=P(19, 15), color=SOFT), P(2.4, 1.30))
        p2.move_to([COMP_R_X, ytop - P(0.34, 0.29), 0])
        self.play(FadeIn(gl), FadeIn(g2), FadeIn(pl), FadeIn(p2),
                  run_time=0.6)

        pw = P(5.80, 3.44)
        py = P(-0.14, 0.36)
        plate = _plate("completion.png", pw, [0, py, 0])
        self.play(FadeIn(plate), run_time=0.8)

        ybot = P(-1.86, -1.52)
        gs = _fit(_t(G_STRAND, size=P(22, 18), color=ACCT, weight="BOLD"),
                  P(2.6, 1.40))
        gs.move_to([COMP_L_X, ybot, 0])
        ps = _fit(_t(P_STRAND, size=P(22, 18), color=INK, weight="BOLD"),
                  P(2.6, 1.40))
        ps.move_to([COMP_R_X, ybot, 0])
        self.play(FadeIn(gs), FadeIn(ps), run_time=0.55)

        closer(self, "half a pair is zero detections")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — PAY IT TO CARE   (the attack on this episode's own claim)
# ═════════════════════════════════════════════════════════════════════════════
class B09_PayItToCare(Paced):
    BEAT, RT, HOLD = "B09", 1.550, 0.278

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "So pay greedy to finish them.", CITE_SIM)

        pw = P(6.20, 3.44)
        px, py = P(PLATE_X, 0.0), P(0.45, 1.34)
        plate = _plate("bonus.png", pw, [px, py, 0])
        self.play(FadeIn(plate), run_time=0.8)

        xlab = _fit(_t("paid more to finish", size=P(19, 16), color=SOFT),
                    P(5.6, 3.30))
        xlab.move_to([px, P(-1.52, -0.12), 0])
        self.play(FadeIn(xlab), run_time=0.4)

        rx, rw = _row_x(), _row_w()
        ys = _rows_at(3) if PORTRAIT else _rows_at(3)
        if PORTRAIT:
            ys = (-0.62, -1.06, -1.50)
        rows = [
            ("dashed: the planner, 1.00", GHOST),
            ("filled: rate held", INK),
            ("hollow: rate given up", ACC),
        ]
        for (txt, col), y in zip(rows, ys):
            self.play(FadeIn(_swatch_row(txt, col, [rx, y, 0], rw,
                                         size=P(19, 17))), run_time=0.5)

        top = _chip("tops out at " + BONUS_TOP, size=P(19, 16),
                    max_w=P(3.3, 2.60))
        top.move_to([P(RCOL_X, 0.0), P(-1.60, -1.92), 0])
        self.play(FadeIn(top), run_time=0.45)

        closer(self, "it bought that by becoming LESS greedy")
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE TELL
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    BEAT, RT, HOLD = "B10", 1.550, 0.365

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Speed was never the difference.", CITE_ZTF)

        cy = P(2.02, 2.34)
        c1 = _quiet_chip("greedy  " + G_RATE, size=P(20, 16),
                         max_w=P(3.4, 1.66))
        c1.move_to([P(-1.80, -0.86), cy, 0])
        c2 = _quiet_chip("planner  " + P_RATE, size=P(20, 16),
                         max_w=P(3.4, 1.66))
        c2.move_to([P(1.80, 0.86), cy, 0])
        self.play(FadeIn(c1), FadeIn(c2), run_time=0.6)

        pw = P(6.20, 3.44)
        # The plate FRAME is a curve, so a chip straddling its top edge is a
        # GATE B error (caught landscape, t=2.6s). The plate drops rather than
        # the chips rising, because at 0.15 clearance above the chips the
        # hairline at 2.66 is the next thing they would hit.
        px, py = P(PLATE_X, 0.0), P(0.10, 1.06)
        plate = _plate("airmass.png", pw, [px, py, 0])
        self.play(FadeIn(plate), run_time=0.75)

        rx, rw = _row_x(), _row_w()
        ys = (1.16, 0.38) if not PORTRAIT else (-0.70, -1.14)
        self.play(FadeIn(_swatch_row("greedy, median " + G_X, SOFT,
                                     [rx, ys[0], 0], rw, size=P(19, 17))),
                  run_time=0.5)
        self.play(FadeIn(_swatch_row("planner, median " + P_X, ACC,
                                     [rx, ys[1], 0], rw, size=P(19, 17))),
                  run_time=0.5)

        hy = P(-0.80, -1.70)
        hcard = _card(P(RCOL_W, 3.40), P(1.26, 0.86), [rx, hy, 0])
        h1 = _fit(_t("ZTF's ILP made MORE", size=P(19, 16), color=INK),
                  P(RCOL_W - 0.34, 3.10))
        h1.move_to([rx, hy + P(0.28, 0.19), 0])
        h2 = _fit(_t("filter changes: " + ZTF_FILT_I + " vs " + ZTF_FILT_G,
                     size=P(19, 16), color=ACCT), P(RCOL_W - 0.34, 3.10))
        h2.move_to([rx, hy - P(0.28, 0.19), 0])
        self.play(Create(hcard), run_time=0.4)
        self.play(FadeIn(h1), FadeIn(h2), run_time=0.55)

        closer(self, "it was told to avoid them. it made more.")
        self.hold_to_beat()
