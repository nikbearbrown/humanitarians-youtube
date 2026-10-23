"""scenes.py - Manim scenes for stellar-spectra-labels.

*What The Model Would Say.* - ai-explainer, claude-hai, Ep. 14.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL
  Terracotta marks WHAT THE LABELS BROUGHT WITH THEM: the physics model in
  the chain, the error against the truth, the inherited temperature trend,
  and the large precise biased training set. Ink marks WHAT THE MODEL ITSELF
  DOES WELL: its agreement with its own labels, its repeat-measurement
  scatter, and the anchored run that escapes the inheritance.

  The load-bearing moment is B07, where the SAME scatter from B06 keeps its
  points and swaps only its x-axis - the labels for the truth - and the
  cloud visibly leaves the one-to-one line. Nothing about the model changed.
  The mapping never flips, so B05 teaches it once and every later plate
  reads for free.

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
  Every plate comes from assets/gen_stars.py, which runs the REAL algorithm:
  a quadratic polynomial in the labels fitted at every wavelength pixel and
  inverted at test time by Gauss-Newton, which is the published form of a
  data-driven spectral model. It contains no physics. Its only contact with
  the world is the labels it was handed - and those labels are themselves a
  physics pipeline's output, carrying a temperature-dependent metallicity
  bias of 0.18 dex per 1000 K.

  Using the real method matters because the episode's subject is WHAT THE
  MODEL IS ACTUALLY FITTING. With the real fit on screen that is visible
  rather than asserted.

  THREE claims are ASSERTED and the generator writes nothing if any fails.

  A fourth figure was built and cut: a per-pixel plot of the fitted
  coefficients. It is the prettiest thing the generator makes and it says
  nothing the beat sheet needs, so it went.

PLATE GEOMETRY - ph = pw * (ih/iw). Do this arithmetic, do not assume it.
      spectra   1560x700  0.449
      agree     1560x780  0.500     truth     1560x780  0.500
      bars      1560x780  0.500     structure 1560x780  0.500
      anchor    1560x780  0.500
  The landscape figure band is 4.30 units tall, so a 0.50-ratio plate at
  pw = 8.0 is 4.00 tall and leaves nothing for labels; the 0.50 plates run
  at pw 6.6 (3.30 tall). spectra at pw 7.4 is 3.32 tall.

GATE NOTES (learned the expensive way on Eps. 03-13)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - A plate is an ImageMobject, NOT a curve, so GATE B will not flag a label
    printed across it, or a card overlapping it. Eps. 11, 12 and 13 all
    shipped or nearly shipped exactly that. Read the frames.
  - NEVER write `pat[0] +- pw * k` for a label offset. In landscape pw = 7
    inside a 12.3-unit frame and it is fine; in portrait pw = 3.4 and the
    same expression lands outside a 3.6-unit frame. Six of Ep. 13's seven
    GATE B failures were this one line shape.
  - NEVER use a glyph outside the font's coverage. EB Garamond has no "check"
    character and Ep. 09 rendered it as stray digits on screen.
  - A P() pair's PORTRAIT figure must be no wider than the container it sits
    in. Ep. 11's B02 fitted rows to 4.60 units inside a 3.46-unit card.
  - Leave >= 0.15 units between any two elements. A gap of 0.04 is eleven
    pixels at 4K and reads as contact.
  - Give every scene its footer EARLY. GATE V samples each beat at 50% and
    85%, and Ep. 11's B01 read 44% underfill because its footer landed last.
  - Ask whether the PICTURE says what the BEAT says. Ep. 11's bars were drawn
    from compliance, so the winning design had the SHORTER bar.
  - Check BOTH aspects. Portrait failed GATE B 8/10 on Ep. 08's first pass.
  - Pacing: a scene landing above -0.15 s is floored; lower its RT. A
    per-scene trim override was built and tried on four scenes across two
    episodes and moved the duration by exactly zero every time. At the 1.55
    RT cap the remaining lever is HOLD (Ep. 13's B06).
  - The pacing solve runs ONCE, in landscape. A scene whose portrait branch
    does MORE plays will overshoot its beat; measure both aspects.
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
#  Plate geometry note. A plate placed by WIDTH gets its height for free:
#      ph = pw * (ih / iw)
#  The six plates from gen_stars.py, in pixels and as ratios:
#      spectra   1560x700 (0.449)
#      agree     1560x780 (0.500)   truth     1560x780 (0.500)
#      bars      1560x780 (0.500)   structure 1560x780 (0.500)
#      anchor    1560x780 (0.500)
#  The landscape figure band is 4.30 units tall, so a 0.50-ratio plate at
#  pw = 8.0 is 4.00 tall and leaves almost nothing for labels. The 0.50 plates
#  run at pw 6.6 (3.30 tall); spectra runs at 7.4 (3.32). Do this arithmetic;
#  Ep. 12's B05 put a 4.79-unit plate in a 4.30-unit band and a label landed
#  above the title.
#
#  WHERE A LABEL MAY SIT. gen_stars.py draws IMAGERY ONLY -- no text, no tick
#  labels, no legend. Everything named on screen is a Manim mobject placed
#  OUTSIDE the plate rectangle, because a plate is an ImageMobject and GATE B
#  cannot see a label printed across one. The only things drawn ON a plate are
#  deliberate MARKS -- B04's wavelength guide -- never text.
# ─────────────────────────────────────────────────────────────────────────────

# ── Plate-internal coordinates, computed once, not guessed ───────────────────
# Axes() insets its box by 18 px on a 1560-wide plate, so a data x maps to
# fraction 18/1560 + (1524/1560) * x / 3. Both bar plates use xlim (0, 3) and
# bars at x = 0.55 / 1.50 / 2.45, which is:
BAR_FX = (-0.30936, 0.0, +0.30936)   # offset from plate CENTRE, in units of pw
# These are safely INSIDE the plate (|0.309| < 0.5), which is what makes the
# `pw * k` form legal here. The form that is NOT legal is a label placed
# OUTSIDE a plate by a pw-scaled offset -- in landscape pw = 6.6 inside a
# 12.3-unit frame and it fits; in portrait pw = 3.4 and the same expression
# leaves a 3.6-unit frame. Six of Ep. 13's seven GATE B failures were that.

# spectra.png stacks three spectra; these are the row centres as a fraction of
# plate HEIGHT, from pad 22 and row height (700 - 44) / 3.
SPEC_FY = (0.1876, 0.5000, 0.8124)
# The strongest METAL-SENSITIVE line in the frozen bank is pixel 47 of 160.
# Between [Fe/H] = -0.90 and +0.35 at fixed Teff and log g its depth grows by
# 0.345 in normalised flux -- 0.365 against 0.020 -- so a guide dropped here
# genuinely cuts a line that deepens down the stack. Measured, not eyeballed.
SPEC_LINE_FX = 0.3014

# Numbers the scenes put on screen. Every one is printed by
# assets/gen_stars.py, kept here as named constants so a changed experiment
# cannot silently disagree with the labels.
PRECISION = "0.008"
VS_LABELS = "0.033"
VS_TRUTH = "0.128"
UNDERSTATED = "15x"
CORR = "0.995"
SLOPE = "+0.18 dex per 1000 K"
CONTROL = "0.013"
ANCHORED = "0.032"
N_REF = "542"
N_LABELLED = "56,000"


def _plate_at(name, pw, at, frame=True):
    """A plate plus the height it took, so callers can place labels around it."""
    g = _plate(name, pw, at, frame=frame)
    return g, _plate_h(name, pw)


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 0.906, 0.000

    def construct(self):
        self.camera.background_color = BG
        hair = Line([-(X_MAX - 0.10), HAIR_Y, 0], [X_MAX - 0.10, HAIR_Y, 0],
                    color=RULE, stroke_width=2.4)
        top = _fit(_t("AI in Astronomy & Space Science  ·  Ep. 14",
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

        r1 = _fit(_t("thirteen episodes", size=P(28, 23), color=SOFT),
                  P(4.9, 3.00))
        r1.move_to([card_at[0], card_at[1] + P(0.80, 0.74), 0])
        r1b = _fit(_t("is the answer right", size=P(23, 19), color=SOFT),
                   P(4.9, 3.00))
        r1b.move_to([card_at[0], card_at[1] + P(0.38, 0.34), 0])
        self.play(FadeIn(r1), run_time=0.45)
        self.play(FadeIn(r1b), run_time=0.4)
        self.play(Create(_strike(r1b, color=ACC, sw=4)), run_time=0.4)

        r2 = _fit(_t("this one", size=P(28, 23), color=ACCT, weight="BOLD"),
                  P(4.9, 3.00))
        r2.move_to([card_at[0], card_at[1] - P(0.30, 0.30), 0])
        r2b = _fit(_t("where the answers came from", size=P(23, 19), color=INK),
                   P(4.9, 3.00))
        r2b.move_to([card_at[0], card_at[1] - P(0.72, 0.70), 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)
        self.play(Create(SurroundingRectangle(VGroup(r2, r2b), color=ACC,
                                              buff=0.18, stroke_width=3,
                                              corner_radius=0.10)),
                  run_time=0.5)

        ser = _fit(_t("Ep. 14  ·  the labels are a model's output",
                      size=P(23, 18), color=ACCT), P(6.0, 3.34))
        ser.move_to([0, P(-2.34, -2.44), 0])
        self.play(FadeIn(ser), run_time=0.5)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — THE WHOLE IDEA, IN ONE BREATH
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.550, 0.288

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

        row("NOBODY MEASURES A STAR DIRECTLY",
            "the labels come from a physics model",
            1.45, 0.98, INK, (30, 21), "BOLD")
        row("THE AI LEARNS THE LABELS", "and nothing else",
            0.15, -0.32, INK, (30, 21), "BOLD")
        h3 = row("SO IT PREDICTS THE MODEL", None,
                 -1.30, 0.0, ACCT, (32, 22), "BOLD")
        self.play(Create(_underline(h3, color=ACC, sw=5, buff=0.16)),
                  run_time=0.5)

        closer(self, "not the star", cx=0.0)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE METHOD, AS PUBLISHED
# ═════════════════════════════════════════════════════════════════════════════
class B03_TheMethod(Paced):
    """An isotype at HONEST scale: one mark is 100 stars, in BOTH blocks.

    542 reference stars is 5 marks; 56,000 is 560. Drawing the big block as
    'a lot of dots' and the small one as 'a few' would make the ratio a
    decoration. At 100 stars a mark the picture IS the ratio, and the caption
    says what a mark is worth so nobody has to take it on trust.
    """
    BEAT, RT, HOLD = "B03", 1.550, 0.061
    RT_PORTRAIT = 1.695

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Trained on 542 stars. Applied to 56,000.",
               cite="Ness, Hogg, Rix, Ho & Zasowski 2015, ApJ 808, 16  ·  "
                    "one mark = 100 stars")

        # The PUBLISHED chip is landscape-only. Portrait's 4.64-unit band has
        # to carry a label, five marks, a label, a 24x24 grid, a card and the
        # closer; the chip is the one item the narration does not speak, and
        # the citation line already names the paper. So it is what goes.
        if not PORTRAIT:
            chip = _chip("PUBLISHED  ·  The Cannon, ApJ 2015", size=20,
                         max_w=6.0)
            chip.move_to([-3.40, 2.22, 0])
            self.play(FadeIn(chip, shift=DOWN * 0.08), run_time=0.6)

        # ── the 542: five marks ──────────────────────────────────────────────
        few_at = P([-4.05, 1.22, 0], [0.0, 2.12, 0])
        few = VGroup(*[Dot(radius=P(0.085, 0.075), color=ACC)
                       .move_to([few_at[0] + (i - 2) * 0.30, few_at[1], 0])
                       for i in range(5)])
        few_lab = _fit(_t("%s reference stars" % N_REF, size=P(25, 20),
                          color=ACCT, weight="BOLD"), P(3.30, 3.30))
        few_lab.move_to([few_at[0], few_at[1] + P(0.52, 0.38), 0])
        self.play(FadeIn(few_lab), run_time=0.5)
        self.play(LaggedStart(*[GrowFromCenter(d) for d in few],
                              lag_ratio=0.18), run_time=0.9)

        # ── the 56,000: 560 marks ────────────────────────────────────────────
        cols, rows_n, sp = 24, 24, P(0.10, 0.085)
        grid_at = P([2.05, 0.52, 0], [0.0, 0.34, 0])
        marks = VGroup()
        for n in range(560):
            r, c = divmod(n, cols)
            marks.add(Dot(radius=0.030, color=INK).move_to(
                [grid_at[0] + (c - (cols - 1) / 2.0) * sp,
                 grid_at[1] - (r - (rows_n - 1) / 2.0) * sp, 0]))
        many_lab = _fit(_t("%s stars labelled" % N_LABELLED, size=P(25, 20),
                           color=INK, weight="BOLD"), P(3.60, 3.30))
        many_lab.move_to([grid_at[0], grid_at[1] + P(1.45, 1.34), 0])
        self.play(FadeIn(many_lab), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(m, scale=0.6) for m in marks],
                              lag_ratio=0.0012), run_time=1.5)

        # ── what it does NOT contain ─────────────────────────────────────────
        note_at = P([-4.05, -0.95, 0], [0.0, -1.48, 0])
        note = _card(P(3.90, 3.50), P(1.05, 0.92), note_at)
        n1 = _fit(_t("no stellar models", size=P(24, 20), color=INK),
                  P(3.50, 3.10))
        n1.move_to([note_at[0], note_at[1] + 0.21, 0])
        n2 = _fit(_t("no line list", size=P(24, 20), color=INK), P(3.50, 3.10))
        n2.move_to([note_at[0], note_at[1] - 0.21, 0])
        self.play(Create(note), run_time=0.5)
        self.play(FadeIn(n1), FadeIn(n2), run_time=0.6)

        closer(self, "only the labels", cx=P(1.9, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — WHAT IT READS
# ═════════════════════════════════════════════════════════════════════════════
class B04_TheData(Paced):
    BEAT, RT, HOLD = "B04", 1.550, 0.228

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Same star, three metallicities",
               cite="computed in this reel  ·  Teff 5200 K, log g 2.8, S/N 100")

        pw = P(7.40, 3.40)
        pat = [P(1.05, 0.0), P(0.52, 1.46), 0]
        plate, ph = _plate_at("spectra.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        # Row labels sit OUTSIDE the plate: to its left in landscape, stacked
        # underneath in portrait. SPEC_FY are the measured row centres.
        rows = [("fewest metals", SOFT, 0), ("in between", INK, 1),
                ("most metals", ACCT, 2)]
        for text, col, i in rows:
            lab = _fit(_t(text, size=P(26, 21), color=col,
                          weight="BOLD" if i == 2 else None), P(2.95, 3.30))
            if PORTRAIT:
                lab.move_to([0, pat[1] - ph / 2.0 - 0.40 - i * 0.46, 0])
            else:
                lab.move_to([0, pat[1] + (0.5 - SPEC_FY[i]) * ph, 0])
                lab.align_to([pat[0] - pw / 2.0 - 0.24, 0, 0], RIGHT)
            self.play(FadeIn(lab, shift=RIGHT * 0.08), run_time=0.5)

        # The wavelength guide. Drawn ON the plate deliberately: it is a mark,
        # not text, and SPEC_LINE_FX is the measured pixel of the line whose
        # depth grows most with metallicity.
        gx = pat[0] + (SPEC_LINE_FX - 0.5) * pw
        guide = DashedLine([gx, pat[1] + ph / 2.0 - 0.06, 0],
                           [gx, pat[1] - ph / 2.0 + 0.06, 0],
                           color=ACC, stroke_width=4, dash_length=0.10)
        guide._qc_intentional = True
        self.play(Create(guide), run_time=0.7)
        gl = _fit(_t("one absorption line, deepening", size=P(22, 18),
                     color=ACCT), P(5.20, 3.34))
        gl.move_to([pat[0], pat[1] - ph / 2.0 - P(0.36, 1.86), 0])
        self.play(FadeIn(gl), run_time=0.5)

        closer(self, "it never learns why", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE CHAIN
# ═════════════════════════════════════════════════════════════════════════════
class B05_TheChain(Paced):
    """Where the colour contract is taught. Terracotta is the physics model -
    the link that is neither nature nor the AI, and whose errors every later
    plate in this reel inherits."""
    BEAT, RT, HOLD = "B05", 1.550, 0.085

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Four links. One of them is nature.")

        links = [("the star", INK, False), ("the spectrum", INK, False),
                 ("a physics model", ACCT, True), ("the AI", INK, False)]
        bw, bh = P(2.58, 2.60), P(1.10, 0.80)
        cxp = -0.30          # portrait chain centre, shifted to free the right
        boxes, labels = [], []
        for i, (text, col, hot) in enumerate(links):
            at = ([cxp, 2.16 - i * 1.15, 0] if PORTRAIT
                  else [-4.30 + i * 2.8667, 0.95, 0])
            boxes.append(RoundedRectangle(
                width=bw, height=bh, corner_radius=0.14,
                color=ACC if hot else GHOST, stroke_width=3.0 if hot else 1.8,
                fill_color=CARD, fill_opacity=1.0).move_to(at))
            labels.append(_fit(_t(text, size=P(25, 22), color=col,
                                  weight="BOLD" if hot else None),
                               bw - 0.30, at))

        for i, (box, lab) in enumerate(zip(boxes, labels)):
            if i:
                a, b = boxes[i - 1], box
                if PORTRAIT:
                    arr = _arrow([a.get_center()[0], a.get_bottom()[1], 0],
                                 [b.get_center()[0], b.get_top()[1], 0])
                else:
                    arr = _arrow([a.get_right()[0], a.get_center()[1], 0],
                                 [b.get_left()[0], b.get_center()[1], 0])
                self.play(Create(arr), run_time=0.35)
            self.play(Create(box), FadeIn(lab), run_time=0.55)

        # The bracket closes under (landscape) or beside (portrait) links 2-4.
        if PORTRAIT:
            bx = boxes[1].get_right()[0] + 0.20
            br = Line([bx, boxes[1].get_top()[1], 0],
                      [bx, boxes[3].get_bottom()[1], 0],
                      color=ACC, stroke_width=4)
            bl = _fit(_t("not nature", size=20, color=ACCT, weight="BOLD"),
                      1.40)
            bl.rotate(PI / 2).move_to(
                [bx + 0.26, (boxes[1].get_top()[1]
                             + boxes[3].get_bottom()[1]) / 2.0, 0])
        else:
            by = boxes[1].get_bottom()[1] - 0.44
            br = Line([boxes[1].get_left()[0], by, 0],
                      [boxes[3].get_right()[0], by, 0],
                      color=ACC, stroke_width=4)
            bl = _fit(_t("not nature", size=27, color=ACCT, weight="BOLD"),
                      3.20)
            bl.move_to([(boxes[1].get_left()[0]
                         + boxes[3].get_right()[0]) / 2.0, by - 0.38, 0])
        self.play(Create(br), run_time=0.6)
        self.play(FadeIn(bl), run_time=0.5)

        closer(self, "only the first one is nature", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ─────────────────────────────────────────────────────────────────────────────
#  Shared furniture for the four plate beats (B06-B10)
#
#  Landscape puts the plate left of centre and reads its axes, numbers and
#  notes in a right-hand column. Portrait has no right-hand column at 3.6
#  units, so the same information stacks underneath as legend rows. That is
#  the portrait reduction rule applied literally: every item below is spoken
#  by the narration, so nothing here may be dropped -- only re-laid-out.
# ─────────────────────────────────────────────────────────────────────────────
RCOL_X = 4.24          # centre of the landscape right-hand column
RCOL_W = 3.44          # and its width: it spans x 2.52 .. 5.96
# EVERY landscape plate beat therefore places its plate at x = -1.10, putting
# the plate's right edge at 2.20 and leaving 0.32 clear of this column. A plate
# centred at x = 0 reaches 3.30 and collides -- GATE B flagged exactly that on
# B08 and B10, because a plate's FRAME is a curve even though its image is not.


def _axis_note(scene, text, y, col=SOFT, size=(22, 18), x=None):
    n = _fit(_t(text, size=P(*size), color=col),
             P(RCOL_W, 3.34), [RCOL_X if x is None else x, y, 0])
    scene.play(FadeIn(n), run_time=0.45)
    return n


def _swatch_row(text, value, col, at, w):
    """A legend row for portrait: colour chip, name, value."""
    sw = Rectangle(width=0.22, height=0.22, color=col, fill_color=col,
                   fill_opacity=1.0, stroke_width=0)
    lab = _fit(_t(text, size=18, color=INK), w - 1.30)
    val = _fit(_t(value, size=20, color=col if col is not ACC else ACCT,
                  weight="BOLD"), 0.90)
    sw.move_to([at[0] - w / 2.0 + 0.11, at[1], 0])
    lab.move_to([at[0] - w / 2.0 + 0.11 + 0.18 + lab.width / 2.0, at[1], 0])
    val.move_to([at[0] + w / 2.0 - val.width / 2.0, at[1], 0])
    return VGroup(sw, lab, val)


# Both bar plates share Axes ylim (0, 0.155) with an 18 px inset on a 780 px
# image, so a value maps to a fraction of plate HEIGHT measured from the top:
#     frac = (762 - 744 * v / 0.155) / 780
def _bar_fy(v):
    return (762.0 - 744.0 * v / 0.155) / 780.0


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — IT AGREES WITH ITS TEACHER
# ═════════════════════════════════════════════════════════════════════════════
class B06_Agrees(Paced):
    BEAT, RT, HOLD = "B06", 1.550, 0.135
    RT_PORTRAIT = 1.830

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Against the labels it was trained on",
               cite="computed in this reel  ·  500 training stars, 400 test "
                    "stars, S/N 100")

        pw = P(6.60, 3.40)
        pat = [P(-1.10, 0.0), P(0.60, 1.50), 0]
        plate, ph = _plate_at("agree.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        # Trace the one-to-one line. Axes() insets the box by 18 px, so the
        # diagonal runs corner to corner of that inset box -- a MARK over the
        # plate, which is allowed; text over a plate is not.
        fx0, fx1 = 18.0 / 1560.0, 1542.0 / 1560.0
        fy0, fy1 = 18.0 / 780.0, 762.0 / 780.0
        diag = Line([pat[0] + (fx0 - 0.5) * pw, pat[1] + (0.5 - fy1) * ph, 0],
                    [pat[0] + (fx1 - 0.5) * pw, pat[1] + (0.5 - fy0) * ph, 0],
                    color=INK, stroke_width=3.2)
        diag._qc_intentional = True
        self.play(Create(diag), run_time=0.8)

        if PORTRAIT:
            _axis_note(self, "vertical  ·  what the model says", 0.15, x=0.0)
            _axis_note(self, "horizontal  ·  what the labels say", -0.35, x=0.0)
            chip = _chip("%s dex" % VS_LABELS, size=24, max_w=2.20)
            chip.move_to([0.0, -1.08, 0])
            self.play(FadeIn(chip, scale=0.9), run_time=0.55)
            _axis_note(self, "agreement with its own labels", -1.68,
                       col=INK, x=0.0)
        else:
            _axis_note(self, "vertical  ·  what the model says", 1.92)
            _axis_note(self, "horizontal  ·  what the labels say", 1.36)
            chip = _chip("%s dex" % VS_LABELS, size=30, max_w=2.60)
            chip.move_to([RCOL_X, 0.44, 0])
            self.play(FadeIn(chip, scale=0.9), run_time=0.55)
            _axis_note(self, "agreement with its", -0.22, col=INK)
            _axis_note(self, "own labels", -0.62, col=INK)
            _axis_note(self, "the diagonal is one-to-one", -1.36)

        closer(self, "this is the plot a paper shows", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — AND AGAINST THE TRUTH
# ═════════════════════════════════════════════════════════════════════════════
class B07_TheTruth(Paced):
    """The load-bearing beat.

    B06 and B07 are both scatter plots, and two consecutive beats sharing one
    visual scheme read as two slides. So this beat does not PRESENT a second
    scatter: it opens on B06's closing composition and changes exactly one
    thing -- the horizontal axis -- while the points cross-dissolve in place
    and visibly leave the diagonal. Nothing about the model changed, which is
    the entire argument.

    The dissolve is FadeOut+FadeIn of two ImageMobjects at identical width and
    position, NOT a Transform: ImageMobject is not a VMobject and cannot be
    interpolated. On screen the points appear to spread, which is what the
    narration says happens.
    """
    BEAT, RT, HOLD = "B07", 1.550, 0.010

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Now against the truth",
               cite="computed in this reel  ·  the same 400 test stars, the "
                    "same fitted model")

        pw = P(6.60, 3.40)
        pat = [P(-1.10, 0.0), P(0.60, 1.50), 0]
        before, ph = _plate_at("agree.png", pw, pat)
        after, _ = _plate_at("truth.png", pw, pat)
        self.play(FadeIn(before), run_time=0.55)

        fx0, fx1 = 18.0 / 1560.0, 1542.0 / 1560.0
        fy0, fy1 = 18.0 / 780.0, 762.0 / 780.0
        diag = Line([pat[0] + (fx0 - 0.5) * pw, pat[1] + (0.5 - fy1) * ph, 0],
                    [pat[0] + (fx1 - 0.5) * pw, pat[1] + (0.5 - fy0) * ph, 0],
                    color=INK, stroke_width=3.2)
        diag._qc_intentional = True
        self.add(diag)

        nx = 0.0 if PORTRAIT else RCOL_X
        ny = -0.35 if PORTRAIT else 1.36
        old = _fit(_t("horizontal  ·  what the labels say", size=P(22, 18),
                      color=SOFT), P(RCOL_W, 3.34), [nx, ny, 0])
        new = _fit(_t("horizontal  ·  what the TRUTH says", size=P(22, 18),
                      color=ACCT, weight="BOLD"), P(RCOL_W, 3.34), [nx, ny, 0])
        vert = _fit(_t("vertical  ·  what the model says", size=P(22, 18),
                       color=SOFT), P(RCOL_W, 3.34),
                    [nx, 0.15 if PORTRAIT else 1.92, 0])
        self.play(FadeIn(vert), FadeIn(old), run_time=0.5)

        # one thing changes
        self.play(Transform(old, new), run_time=0.7)
        self.play(FadeOut(before), FadeIn(after), run_time=1.1)
        self.play(after.animate.set_opacity(1.0), run_time=0.3)

        c_old = _chip("%s dex" % VS_LABELS, size=P(30, 24), max_w=P(2.60, 2.20))
        c_old.move_to([nx, -1.08 if PORTRAIT else 0.44, 0])
        c_new = _chip("%s dex" % VS_TRUTH, size=P(30, 24), max_w=P(2.60, 2.20))
        c_new.move_to([nx, -1.08 if PORTRAIT else 0.44, 0])
        self.play(FadeIn(c_old, scale=0.9), run_time=0.45)
        self.play(Transform(c_old, c_new), run_time=0.65)
        _axis_note(self, "nothing about the model changed",
                   -1.68 if PORTRAIT else -0.52, col=INK, x=nx)

        closer(self, "four times worse than it looked", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — PRECISION IS NOT ACCURACY
# ═════════════════════════════════════════════════════════════════════════════
class B08_Precision(Paced):
    BEAT, RT, HOLD = "B08", 1.550, 0.006
    RT_PORTRAIT = 2.417

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Three numbers you could quote",
               cite="computed in this reel  ·  [Fe/H], 400 test stars, dex")

        pw = P(6.60, 3.40)
        pat = [P(-1.10, 0.0), P(0.65, 1.55), 0]
        plate, ph = _plate_at("bars.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        bars = [("measure the same star twice", PRECISION, INK, 0.0083),
                ("agrees with its own labels", VS_LABELS, INK, 0.0329),
                ("the real error", VS_TRUTH, ACC, 0.1280)]

        if PORTRAIT:
            for i, (name, val, col, _v) in enumerate(bars):
                row = _swatch_row(name, "%s dex" % val, col,
                                  [0.0, 0.30 - i * 0.60, 0], 3.40)
                self.play(FadeIn(row, shift=RIGHT * 0.06), run_time=0.55)
            chip = _chip("the error bars understate it %s" % UNDERSTATED,
                         size=21, max_w=3.40)
            chip.move_to([0.0, -1.72, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
        else:
            for i, (name, val, col, _v) in enumerate(bars):
                x = pat[0] + BAR_FX[i] * pw
                nm = _fit(_t(name, size=22,
                             color=ACCT if col is ACC else SOFT), 1.80,
                          [x, pat[1] - ph / 2.0 - 0.36, 0])
                vl = _fit(_t("%s dex" % val, size=28,
                             color=ACCT if col is ACC else INK,
                             weight="BOLD"), 1.80,
                          [x, pat[1] - ph / 2.0 - 0.78, 0])
                self.play(FadeIn(nm), run_time=0.4)
                self.play(FadeIn(vl, shift=UP * 0.06), run_time=0.45)

            # The 15x span, drawn INSIDE the plate as marks and labelled
            # outside it. _bar_fy() converts a value to a height fraction.
            y_lo = pat[1] + (0.5 - _bar_fy(0.0083)) * ph
            y_hi = pat[1] + (0.5 - _bar_fy(0.1280)) * ph
            # Bar three spans x 0.38..1.50; the span sits clear of it at
            # 1.85, still 0.35 inside the plate's right edge at 2.20.
            x_span = pat[0] + BAR_FX[2] * pw + 0.92
            guide = DashedLine([pat[0] + BAR_FX[0] * pw, y_lo, 0],
                               [x_span, y_lo, 0],
                               color=GHOST, stroke_width=3, dash_length=0.10)
            guide._qc_intentional = True
            span = DoubleArrow([x_span, y_lo, 0], [x_span, y_hi, 0],
                               color=ACC, stroke_width=4, buff=0.0,
                               max_tip_length_to_length_ratio=0.10)
            span._qc_intentional = True
            self.play(Create(guide), run_time=0.6)
            self.play(Create(span), run_time=0.7)
            tag = _fit(_t(UNDERSTATED, size=40, color=ACCT, weight="BOLD"),
                       1.40, [RCOL_X, (y_lo + y_hi) / 2.0, 0])
            self.play(FadeIn(tag, shift=LEFT * 0.10), run_time=0.55)
            _axis_note(self, "the gap between what you",
                       (y_lo + y_hi) / 2.0 - 0.72)
            _axis_note(self, "would quote and what is true",
                       (y_lo + y_hi) / 2.0 - 1.12)

        closer(self, "the error bars describe neither", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — THE ERROR HAS A SHAPE
# ═════════════════════════════════════════════════════════════════════════════
class B09_Structure(Paced):
    BEAT, RT, HOLD = "B09", 1.539, 0.000
    RT_PORTRAIT = 2.072

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The error against temperature",
               cite="computed in this reel  ·  400 test stars, [Fe/H] error "
                    "against Teff")

        pw = P(6.60, 3.40)
        pat = [P(-1.10, 0.0), P(0.60, 1.50), 0]
        plate, ph = _plate_at("structure.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        # ylim is (-0.34, +0.34), so zero error is the plate's vertical centre,
        # and the plate's own dashed rule is already drawn there. Landscape
        # names it in the margin beside the plate. PORTRAIT CANNOT: the plate
        # is 3.40 wide in a 3.60-unit frame, so a label beside it would sit at
        # x = 2.14 and leave the frame entirely. Portrait names the rule in a
        # note underneath instead -- same information, a legal position.
        if not PORTRAIT:
            zero = _fit(_t("zero", size=21, color=SOFT), 1.40)
            zero.move_to([0, pat[1], 0]).align_to(
                [pat[0] - pw / 2.0 - 0.24, 0, 0], RIGHT)
            self.play(FadeIn(zero), run_time=0.45)

        if PORTRAIT:
            _axis_note(self, "the dashed rule is zero error", 0.12, x=0.0)
            _axis_note(self, "horizontal  ·  temperature", -0.38, x=0.0)
            chip = _chip("correlation %s" % CORR, size=22, max_w=3.20)
            chip.move_to([0.0, -1.10, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
            _axis_note(self, SLOPE, -1.70, col=INK, x=0.0)
        else:
            _axis_note(self, "vertical  ·  error against", 1.96)
            _axis_note(self, "the truth", 1.58)
            _axis_note(self, "horizontal  ·  temperature", 1.02)
            chip = _chip("correlation %s" % CORR, size=27, max_w=3.30)
            chip.move_to([RCOL_X, 0.10, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
            _axis_note(self, SLOPE, -0.56, col=INK)
            _axis_note(self, "a trend survives every check", -1.14)
            _axis_note(self, "that compares averages", -1.52)

        closer(self, "a line, not a cloud", cx=P(-0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE TELL
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    """The only beat where the terracotta bar is the one you do NOT want.

    The colour contract holds: terracotta is still what the labels brought
    with them. Here that is the 500-star training set -- precise, inherited
    and worst against the truth -- and the two ink/soft bars beside it are the
    runs that escaped the inheritance. Ep. 11 shipped a bar chart whose
    winning design had the SHORTER bar and it read as a failure; here the
    shorter bar IS the win, so the names carry it, not the length alone.
    """
    BEAT, RT, HOLD = "B10", 1.550, 0.000
    RT_PORTRAIT = 2.057

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Error against the truth, three ways",
               cite="computed in this reel  ·  [Fe/H], 400 test stars, dex")

        pw = P(6.60, 3.40)
        pat = [P(-1.10, 0.0), P(0.65, 1.55), 0]
        plate, ph = _plate_at("anchor.png", pw, pat)
        self.play(FadeIn(plate), run_time=0.9)

        bars = [("500 precise, inherited labels", VS_TRUTH, ACC),
                ("120 independent, noisier ones", ANCHORED, INK),
                ("an unbiased teacher  ·  control", CONTROL, SOFT)]

        if PORTRAIT:
            for i, (name, val, col) in enumerate(bars):
                row = _swatch_row(name, "%s dex" % val, col,
                                  [0.0, 0.30 - i * 0.60, 0], 3.40)
                self.play(FadeIn(row, shift=RIGHT * 0.06), run_time=0.55)
            chip = _chip("four times fewer. four times more accurate.",
                         size=19, max_w=3.40)
            chip.move_to([0.0, -1.72, 0])
            self.play(FadeIn(chip, scale=0.92), run_time=0.6)
        else:
            for i, (name, val, col) in enumerate(bars):
                x = pat[0] + BAR_FX[i] * pw
                nm = _fit(_t(name, size=21,
                             color=ACCT if col is ACC else SOFT), 1.80,
                          [x, pat[1] - ph / 2.0 - 0.36, 0])
                vl = _fit(_t("%s dex" % val, size=28,
                             color=ACCT if col is ACC else INK,
                             weight="BOLD"), 1.80,
                          [x, pat[1] - ph / 2.0 - 0.78, 0])
                self.play(FadeIn(nm), run_time=0.4)
                self.play(FadeIn(vl, shift=UP * 0.06), run_time=0.45)
            tag = _fit(_t("four times fewer.", size=25, color=INK),
                       RCOL_W, [RCOL_X, 0.62, 0])
            tag2 = _fit(_t("four times more accurate.", size=25, color=ACCT,
                           weight="BOLD"), RCOL_W, [RCOL_X, 0.16, 0])
            self.play(FadeIn(tag), run_time=0.5)
            self.play(FadeIn(tag2, shift=UP * 0.06), run_time=0.55)
            self.play(Create(_underline(tag2, color=ACC, sw=4, buff=0.14)),
                      run_time=0.45)

        closer(self, "fewer, noisier, and right", cx=P(-0.6, 0.0))
        self.hold_to_beat()
