"""scenes.py - Manim scenes for seti-signal-detection.

*The Signal We Imagined.* - ai-explainer, claude-hai, Ep. 13.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL
  Terracotta marks WHAT THE ASSUMPTION DECIDES: the injected signal's track,
  the recall that appears the moment the search is widened, and the cadence
  test, which does not depend on the guess at all. Ink marks WHAT IS THERE
  REGARDLESS: the interference standing vertical at zero drift, and the
  morphology search's own score.

  The load-bearing moment is B07, where the ink bar for the drift-corrected
  signal lies flat on the axis at zero and the terracotta bar beside it
  stands at full height -- the same signal, the same data, one number
  changed. The mapping never flips, so B04 teaches it once and every later
  plate reads for free.

THIS FILE IS ASPECT-AWARE - IT RENDERS BOTH CUTS
  The reel ships in 16:9 (3840x2160) and 9:16 (2160x3840). Manim keeps
  frame_height = 8.0 in both, so the VERTICAL band plan is identical either
  way; only the horizontal extent changes - x +-6.15 landscape, x +-1.80
  portrait. Portrait is NOT a crop: it carries fewer elements, larger. The
  rule for choosing what goes: anything the narration SPEAKS stays.

  three.png is 0.271 -- at portrait's 3.44 units each of its three panels
  would be 1.1 units across and the lean of the marked track, which is the
  entire content, stops being readable. Portrait loads three_v.png instead.

LAYOUT BAND PLAN (every scene obeys it - this is what keeps the gates green)
                        landscape      portrait
  title                   +3.02          +3.14
  hairline                +2.66          +2.84
  the figure       +2.40 .. -1.90   +2.62 .. -2.02
  the closing line        -2.50          -2.42   (terracotta rule 0.28 below)
  the citation            -3.20          -2.95
  the wordmark bug        -3.12          -3.28   (right-anchored, LOGO LAW)

PLATES
  Every plate comes from assets/gen_seti.py, which runs the REAL detection
  statistic: the de-Doppler sum that a radio technosignature pipeline
  computes, swept over trial drift rates. Using the real algorithm is the
  point -- it puts the episode's subject, the assumption, in plain sight as
  a single number, the range of drift rates the search is told to try.

  THREE claims are ASSERTED and the generator writes nothing if any fails.

  A FOURTH CLAIM WAS MEASURED AND CUT. An earlier version argued that zero
  drift is too crowded with interference to search. The measurement does not
  support it: 6 look-alikes for a drifting candidate against 5 for a
  stationary one. Raising the interference count until the claim came true
  would be tuning the experiment to the conclusion, so the claim went and
  the measurement stayed in the paperwork. BLC1's look-alike argument
  appears in the reel as a PUBLISHED result only.

  Two simulators were discarded before this one. The first took a single
  maximum over the whole field, which can never work: the interference is
  brighter than the signal, so the maximum was always an interference line.
  The second ran at 16 rows and 0.15-0.60 Hz/s, where a signal drifts only
  2-10 channels across the integration and de-Doppler cannot separate it
  from a stationary line at all.

PLATE GEOMETRY - ph = pw * (ih/iw). Do this arithmetic, do not assume it.
  waterfall 1500x700  0.467     three    1552x420  0.271
  recall    1560x780  0.500     edge     1560x780  0.500
  compare   1560x780  0.500     cadence  1150x478  0.416
  three_v    760x940  1.237
  The landscape figure band is 4.30 units tall, so a 0.50-ratio plate at
  pw = 8.0 is 4.00 tall and leaves nothing for labels; the 0.50 plates run
  at pw 6.6. three_v is 1.24, so in portrait at pw 3.00 it is 3.71 tall and
  needs the whole band, which is why that beat carries nothing else there.

GATE NOTES (learned the expensive way on Eps. 03-12)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - A plate is an ImageMobject, NOT a curve, so GATE B will not flag a label
    printed across it, or a card overlapping it. Ep. 12 shipped both until
    the frames were read.
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
  - A zero-height bar must still be drawn as a visible zero, or the beat
    reads as a missing bar rather than a measured nothing. B07 depends on it.
  - Check BOTH aspects. Portrait failed GATE B 8/10 on Ep. 08's first pass.
  - Pacing: a scene landing above -0.15 s is floored; lower its RT. A
    per-scene trim override was built and tried on four scenes across two
    episodes and moved the duration by exactly zero every time.
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
#  The seven plates from gen_seti.py, in pixels and as ratios:
#      waterfall 1500x700 (0.467)   three   1552x420 (0.271)
#      recall    1560x780 (0.500)   edge    1560x780 (0.500)
#      compare   1560x780 (0.500)   cadence 1150x478 (0.416)
#      three_v    760x940 (1.237)
#  The landscape figure band is 4.30 units tall, so a 0.50-ratio plate at
#  pw = 8.0 is 4.00 tall and leaves almost nothing for labels. Do this
#  arithmetic; Ep. 12's B05 put a 4.79-unit plate in a 4.30-unit band and a
#  label landed above the title.
# ─────────────────────────────────────────────────────────────────────────────

# Numbers the scenes put on screen. Every one is printed by
# assets/gen_seti.py, kept here as named constants so a changed experiment
# cannot silently disagree with the labels.
R_ASSUMED = "80 of 80"
R_CORRECTED_EXCL = "0 of 80"
R_CORRECTED_INCL = "80 of 80"
CAD_CORRECTED = "0.76"
EDGE_HZ = "0.06 Hz/s"


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 0.906, 0.000

    def construct(self):
        self.camera.background_color = BG
        hair = Line([-(X_MAX - 0.10), HAIR_Y, 0], [X_MAX - 0.10, HAIR_Y, 0],
                    color=RULE, stroke_width=2.4)
        top = _fit(_t("AI in Astronomy & Space Science  ·  Ep. 13",
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

        r1 = _fit(_t("twelve episodes", size=P(28, 23), color=SOFT),
                  P(4.9, 3.00))
        r1.move_to([card_at[0], card_at[1] + P(0.80, 0.74), 0])
        r1b = _fit(_t("things that exist", size=P(23, 19), color=SOFT),
                   P(4.9, 3.00))
        r1b.move_to([card_at[0], card_at[1] + P(0.38, 0.34), 0])
        self.play(FadeIn(r1), run_time=0.45)
        self.play(FadeIn(r1b), run_time=0.4)
        self.play(Create(_strike(r1b, color=ACC, sw=4)), run_time=0.4)

        r2 = _fit(_t("this one", size=P(28, 23), color=ACCT, weight="BOLD"),
                  P(4.9, 3.00))
        r2.move_to([card_at[0], card_at[1] - P(0.30, 0.30), 0])
        r2b = _fit(_t("nobody has found it", size=P(23, 19), color=INK),
                   P(4.9, 3.00))
        r2b.move_to([card_at[0], card_at[1] - P(0.72, 0.70), 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)
        self.play(Create(SurroundingRectangle(VGroup(r2, r2b), color=ACC,
                                              buff=0.18, stroke_width=3,
                                              corner_radius=0.10)),
                  run_time=0.5)

        ser = _fit(_t("Ep. 13  ·  the positive class is imaginary",
                      size=P(23, 18), color=ACCT), P(6.0, 3.34))
        ser.move_to([0, P(-2.34, -2.44), 0])
        self.play(FadeIn(ser), run_time=0.5)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — THE WHOLE IDEA IN ONE BREATH  (EXECUTIVE-SUMMARY LAW)
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.132, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath",
               cite="the problem, before any method")

        card = _card(P(9.4, 3.46), P(4.10, 4.30), [0, P(0.26, 0.30), 0])
        self.play(Create(card), run_time=0.7)

        rows = [("WE HAVE NEVER DETECTED ONE", "not once", INK, False),
                ("SO YOU ASSUME A FORM",
                 "there is nothing else to do", INK, False),
                ("AND THEN YOU FIND IT", None, ACCT, True)]
        y0, dy = P(1.56, 1.66), P(1.18, 1.44)
        for head, sub, colr, accent in rows:
            y = y0 - dy * rows.index((head, sub, colr, accent))
            h = _fit(_t(head, size=P(34, 22), color=colr,
                        weight="BOLD" if accent else None), P(8.6, 3.06),
                     [0, y, 0])
            self.play(FadeIn(h, shift=UP * 0.10), run_time=0.7)
            if accent:
                self.play(Create(_underline(h, color=ACC, sw=5, buff=0.14)),
                          run_time=0.45)
            if sub:
                s = _fit(_t(sub, size=P(23, 17), color=SOFT), P(8.4, 3.00))
                s.move_to([0, y - P(0.42, 0.38), 0])
                self.play(FadeIn(s), run_time=0.45)

        closer(self, "the one you assumed", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — BLC1  (PUBLISHED)
# ═════════════════════════════════════════════════════════════════════════════
class B03_BLC1(Paced):
    BEAT, RT, HOLD = "B03", 1.550, 0.045

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The one that got a name",
               cite="Sheikh et al., Nature Astronomy 2021 — published, not "
                    "measured here")

        if not PORTRAIT:
            chip = _quiet_chip("published ledger", size=19, max_w=3.6)
            chip.move_to([-4.40, 1.92, 0])
            self.play(FadeIn(chip), run_time=0.45)

        # a frequency axis with one tone on it
        ax_y = P(0.60, 1.00)
        half = P(4.60, 1.56)
        axis = Line([-half, ax_y, 0], [half, ax_y, 0], color=GHOST,
                    stroke_width=3)
        self.play(Create(axis), run_time=0.5)
        xlab = _fit(_t("frequency  →", size=P(20, 15), color=SOFT),
                    P(4.0, 3.20))
        xlab.move_to([0, ax_y - P(0.46, 0.42), 0])
        self.play(FadeIn(xlab), run_time=0.4)

        tone = Line([P(-0.60, -0.14), ax_y, 0],
                    [P(-0.60, -0.14), ax_y + P(1.30, 1.00), 0],
                    color=ACC, stroke_width=P(9, 7))
        self.play(Create(tone), run_time=0.6)
        nm = _fit(_t("982 MHz", size=P(24, 18), color=ACCT, weight="BOLD"),
                  P(2.8, 1.70))
        nm.move_to([P(-0.60, -0.14), ax_y + P(1.56, 1.22), 0])
        self.play(FadeIn(nm, shift=UP * 0.08), run_time=0.5)

        if not PORTRAIT:
            # BELOW the axis. Above it the look-alike tones run through
            # the card.
            card = _card(4.4, 1.20, [3.70, -0.40, 0])
            self.play(Create(card), run_time=0.45)
            a = _fit(_t("Parkes, 29 April 2019", size=20, color=SOFT), 4.0,
                     [3.70, -0.14, 0])
            b = _fit(_t("pointed at Proxima Centauri", size=22, color=INK),
                     4.0, [3.70, -0.58, 0])
            self.play(FadeIn(a), run_time=0.4)
            self.play(FadeIn(b), run_time=0.45)

        # dozens of look-alikes appear along the axis
        rng = np.random.default_rng(13)
        others = VGroup()
        for _ in range(26):
            x = float(rng.uniform(-half * 0.94, half * 0.94))
            h = float(rng.uniform(0.30, 0.95)) * P(1.20, 0.92)
            others.add(Line([x, ax_y, 0], [x, ax_y + h, 0], color=INK,
                            stroke_width=P(5, 4)))
        self.play(LaggedStart(*[Create(m) for m in others], lag_ratio=0.03),
                  run_time=1.1)

        self.play(tone.animate.set_color(INK), run_time=0.6)
        big = _fit(_t("one of them", size=P(40, 30), color=ACCT,
                      weight="BOLD"), P(5.0, 3.30))
        big.move_to([0, P(-1.70, -1.40), 0])
        self.play(FadeIn(big, shift=UP * 0.10), run_time=0.6)

        closer(self, "dozens of look-alikes, all terrestrial",
               cx=P(0.0, 0.0), size=P(28, 21))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — WHAT THE DATA IS
# ═════════════════════════════════════════════════════════════════════════════
class B04_TheData(Paced):
    BEAT, RT, HOLD = "B04", 1.550, 0.505

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Time down, frequency across",
               cite="computed in this reel: one dynamic spectrum, 32 rows x "
                    "512 channels")

        # waterfall.png is 1500x700 -> 0.467. pw 7.00 -> ph 3.27.
        pw = P(7.00, 3.40)
        pat = [0, P(0.20, 0.60), 0]
        plate = _plate("waterfall.png", pw, pat, frame=False)
        ph = _plate_h("waterfall.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        # LANDSCAPE ONLY: at portrait's pw = 3.40 a label hung off the
        # plate's left edge lands at x -2.00, outside the 1.80 safe edge.
        if not PORTRAIT:
            tlab = _fit(_t("time  ↓", size=19, color=SOFT), 2.4)
            tlab.move_to([pat[0] - pw * 0.5 - 0.42, pat[1], 0])
            self.play(FadeIn(tlab), run_time=0.3)
        flab = _fit(_t("frequency  →", size=P(19, 15), color=SOFT),
                    P(3.4, 2.00))
        flab.move_to([pat[0], pat[1] - ph * 0.5 - P(0.30, 0.32), 0])
        self.play(FadeIn(flab), run_time=0.4)

        # These offsets are a fraction of the PLATE width, which is 7.00 in
        # landscape and 3.40 in portrait -- so portrait centres them instead.
        side = pat[0] - pw * 0.30 if not PORTRAIT else 0.0
        us = _fit(_t("these are us", size=P(22, 17), color=INK,
                     weight="BOLD"), P(3.4, 3.00))
        # headline above, sub beneath it -- the first version had them the
        # other way round, so the explanation sat above the thing it explained
        us.move_to([side, pat[1] + ph * 0.5 + P(0.64, 0.58), 0])
        self.play(FadeIn(us), run_time=0.5)
        sub = _fit(_t("transmitters on the ground, standing still",
                      size=P(19, 14), color=SOFT), P(5.4, 3.20))
        sub.move_to([side, pat[1] + ph * 0.5 + P(0.30, 0.28), 0])
        self.play(FadeIn(sub), run_time=0.4)

        # Landscape pairs this with "these are us" ABOVE the plate -- they
        # are the contrast the beat is about, and below the plate it ran
        # into the closing line. Portrait keeps it beneath, centred, where
        # there is nothing else.
        lean = _fit(_t("a signal from the sky leans", size=P(22, 17),
                       color=ACCT, weight="BOLD"), P(4.6, 3.20))
        lean.move_to([P(2.10, 0.0),
                      pat[1] + ph * 0.5 + 0.28 if not PORTRAIT
                      else pat[1] - ph * 0.5 - 0.74, 0])
        self.play(FadeIn(lean, shift=UP * 0.08), run_time=0.55)

        chip = _quiet_chip("and you cannot see it", size=P(20, 15),
                           max_w=P(4.0, 3.10))
        chip.move_to([P(-2.60, 0.0), P(-1.92, -1.36), 0])
        self.play(FadeIn(chip), run_time=0.5)

        closer(self, "which is why you integrate", cx=P(0.6, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE ASSUMPTION, AS A NUMBER
# ═════════════════════════════════════════════════════════════════════════════
class B05_TheAssumption(Paced):
    BEAT, RT, HOLD = "B05", 1.351, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The range you try is the assumption",
               cite="computed in this reel: the de-Doppler sweep a real "
                    "pipeline computes")

        bw, bh = P(6.00, 3.20), P(3.40, 2.70)
        bx, by = P(-1.55, 0.0), P(0.52, 0.72)
        box = Rectangle(width=bw, height=bh, color=GHOST, stroke_width=2.4,
                        fill_color=CARD, fill_opacity=1.0)
        box.move_to([bx, by, 0])
        self.play(Create(box), run_time=0.6)

        # a fan of trial tracks
        fan = VGroup()
        for k in range(7):
            dx = (-0.30 + 0.10 * k) * bw
            fan.add(Line([bx - bw * 0.30, by + bh * 0.46, 0],
                         [bx - bw * 0.30 + dx, by - bh * 0.46, 0],
                         color=GHOST, stroke_width=3))
        self.play(LaggedStart(*[Create(m) for m in fan], lag_ratio=0.12),
                  run_time=1.1)

        best = Line([bx - bw * 0.30, by + bh * 0.46, 0],
                    [bx - bw * 0.30 + 0.20 * bw, by - bh * 0.46, 0],
                    color=ACC, stroke_width=P(7, 6))
        self.play(Create(best), run_time=0.55)

        br = _fit(_t("the range you try", size=P(21, 16), color=ACCT),
                  P(4.0, 3.00))
        br.move_to([bx, by - bh * 0.5 - P(0.32, 0.34), 0])
        self.play(FadeIn(br), run_time=0.45)

        # a vertical track outside the searched range
        out = Line([bx + bw * 0.40, by + bh * 0.46, 0],
                   [bx + bw * 0.40, by - bh * 0.46, 0],
                   color=INK, stroke_width=P(7, 6))
        self.play(Create(out), run_time=0.5)
        ol = _fit(_t("outside it", size=P(20, 15), color=SOFT), P(2.6, 1.60))
        ol.move_to([bx + bw * 0.40, by + bh * 0.5 + P(0.28, 0.26), 0])
        self.play(FadeIn(ol), run_time=0.4)

        if not PORTRAIT:
            col_at = [3.80, 1.20, 0]
            for i, (big, small) in enumerate(
                    [("not missed", "that would mean looked for"),
                     ("never looked for", "the search did not try")]):
                y = col_at[1] - 1.10 * i
                a = _fit(_t(big, size=26, color=ACCT if i else INK,
                            weight="BOLD" if i else None), 4.2,
                         [col_at[0], y, 0])
                b = _fit(_t(small, size=18, color=SOFT), 4.4,
                         [col_at[0], y - 0.42, 0])
                self.play(FadeIn(a), run_time=0.5)
                self.play(FadeIn(b), run_time=0.4)

        closer(self, "never looked for" if PORTRAIT else "the assumption is a number",
               cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — THREE TRANSMITTERS
# ═════════════════════════════════════════════════════════════════════════════
class B06_Three(Paced):
    # RT is already at the 1.55 cap and the tail is floored, so neither of
    # the usual levers applies; HOLD is what is left. 0.034 landed at
    # -0.30 s, outside the -0.25 tolerance.
    BEAT, RT, HOLD = "B06", 1.550, 0.043

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Three things a transmitter can do",
               cite="computed in this reel: the same field, three hypotheses")

        name = "three_v.png" if PORTRAIT else "three.png"
        pw = P(10.60, 2.60)
        pat = [0, P(0.74, 0.70), 0]
        plate = _plate(name, pw, pat, frame=False)
        ph = _plate_h(name, pw)
        self.play(FadeIn(plate), run_time=0.9)

        labs = [("it leans", "what we assume", ACCT),
                ("it corrects its drift", "what we do", INK),
                ("it blinks", "also allowed", INK)]
        for i, (big, small, colr) in enumerate(labs):
            if PORTRAIT:
                # BELOW the stack, as a three-line key. Inside, each line
                # printed straight across a panel.
                y = pat[1] - ph * 0.5 - 0.34 - 0.33 * i
                a = _fit(_t("%s — %s" % (big, small), size=14, color=colr),
                         3.30, [0.0, y, 0])
                self.play(FadeIn(a), run_time=0.45)
            else:
                x = (-0.333 + 0.333 * i) * pw
                a = _fit(_t(big, size=23, color=colr,
                            weight="BOLD" if i == 0 else None), 3.3,
                         [x, pat[1] - ph * 0.5 - 0.30, 0])
                b = _fit(_t(small, size=18, color=SOFT), 3.3,
                         [x, pat[1] - ph * 0.5 - 0.66, 0])
                self.play(FadeIn(a), run_time=0.45)
                self.play(FadeIn(b), run_time=0.35)

        closer(self, "all three are allowed", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — THE BLIND SPOT                                 (the load-bearing beat)
# ═════════════════════════════════════════════════════════════════════════════
class B07_BlindSpot(Paced):
    BEAT, RT, HOLD = "B07", 1.528, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Run the search",
               cite="computed in this reel: 80 trials per hypothesis, "
                    "threshold fixed on noise")

        pw = P(6.60, 3.40)
        pat = [P(-1.40, 0.0), P(0.80, 0.98), 0]
        plate = _plate("recall.png", pw, pat, frame=False)
        ph = _plate_h("recall.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        for i, txt in enumerate(["leans", "corrects", "blinks"]):
            lb = _fit(_t(txt, size=P(20, 15), color=SOFT), P(2.6, 1.10))
            lb.move_to([pat[0] + (-0.31 + 0.31 * i) * pw,
                        pat[1] - ph * 0.5 - P(0.30, 0.32), 0])
            self.play(FadeIn(lb), run_time=0.35)

        ring = RoundedRectangle(width=pw * 0.10, height=ph * 0.16,
                                corner_radius=0.06, color=ACC, stroke_width=4,
                                fill_opacity=0)
        ring.move_to([pat[0] - pw * 0.055, pat[1] - ph * 0.42, 0])
        self.play(Create(ring), run_time=0.6)

        col_at = P([3.70, 1.30, 0], [0, -1.20, 0])
        a = _fit(_t(R_CORRECTED_EXCL, size=P(46, 32), color=INK,
                    weight="BOLD"), P(3.4, 1.90), [col_at[0], col_at[1], 0])
        self.play(FadeIn(a, shift=UP * 0.10), run_time=0.6)
        c = _fit(_t(R_CORRECTED_INCL, size=P(46, 32), color=ACCT,
                    weight="BOLD"), P(3.4, 1.90))
        c.move_to([col_at[0], col_at[1] - P(1.26, 0.58), 0])
        self.play(FadeIn(c, shift=UP * 0.10), run_time=0.6)
        # LANDSCAPE ONLY: portrait fits the two counters and the closing
        # line in the lower band and nothing else.
        if not PORTRAIT:
            b = _fit(_t("searching as we do", size=20, color=SOFT), 4.4)
            b.move_to([col_at[0], col_at[1] - 0.56, 0])
            self.play(FadeIn(b), run_time=0.4)
            d = _fit(_t("one number wider", size=20, color=SOFT), 4.4)
            d.move_to([col_at[0], col_at[1] - 1.82, 0])
            self.play(FadeIn(d), run_time=0.4)

        closer(self, "the same signal, both times", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — THE EDGE
# ═════════════════════════════════════════════════════════════════════════════
class B08_TheEdge(Paced):
    BEAT, RT, HOLD = "B08", 1.473, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Where the blind spot begins",
               cite="computed in this reel: recall against the search's "
                    "lower drift limit")

        pw = P(6.40, 3.30)
        pat = [P(-1.55, 0.0), P(0.86, 1.00), 0]
        plate = _plate("edge.png", pw, pat, frame=False)
        ph = _plate_h("edge.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        xlab = _fit(_t("lowest drift rate the search tries  →",
                       size=P(19, 15), color=SOFT), P(5.4, 3.30))
        xlab.move_to([pat[0], pat[1] - ph * 0.5 - P(0.30, 0.34), 0])
        self.play(FadeIn(xlab), run_time=0.4)
        if not PORTRAIT:
            ylab = _fit(_t("recall", size=19, color=SOFT), 2.0)
            ylab.move_to([pat[0] - pw * 0.5 - 0.36, pat[1] + ph * 0.30, 0])
            self.play(FadeIn(ylab), run_time=0.35)

        chip = _chip(EDGE_HZ, size=P(21, 16), fill=ACC, max_w=P(3.0, 2.40))
        chip.move_to([pat[0] - pw * 0.18, pat[1] - ph * 0.30, 0])
        self.play(FadeIn(chip, shift=UP * 0.06), run_time=0.5)

        if not PORTRAIT:
            note = _fit(_t("above this, every one is found; below it, none",
                           size=20, color=SOFT), 9.4)
            note.move_to([0, -2.02, 0])
            self.play(FadeIn(note), run_time=0.45)

        closer(self, "a cliff, not a slope", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — THE OTHER TEST
# ═════════════════════════════════════════════════════════════════════════════
class B09_OtherTest(Paced):
    BEAT, RT, HOLD = "B09", 1.550, 0.346

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Point at it. Look away.",
               cite="computed in this reel: the integrated spectrum at the "
                    "candidate's own drift rate")

        # cadence.png is 1150x478 -> 0.416. pw 7.20 -> ph 2.99.
        pw = P(7.20, 3.40)
        pat = [0, P(0.50, 0.60), 0]
        plate = _plate("cadence.png", pw, pat, frame=False)
        ph = _plate_h("cadence.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        for i, (txt, colr) in enumerate([("pointed at the star", ACCT),
                                         ("pointed away", INK)]):
            lb = _fit(_t(txt, size=P(22, 16), color=colr,
                         weight="BOLD" if i == 0 else None), P(4.4, 1.60))
            lb.move_to([pat[0] + (-0.26 + 0.52 * i) * pw,
                        pat[1] + ph * 0.5 + P(0.28, 0.26), 0])
            self.play(FadeIn(lb), run_time=0.45)

        got = _fit(_t("a peak, three times", size=P(22, 16), color=ACCT),
                   P(4.4, 1.70))
        got.move_to([pat[0] - pw * 0.26, pat[1] - ph * 0.5 - P(0.30, 0.32), 0])
        flat = _fit(_t("flat, three times", size=P(22, 16), color=SOFT),
                    P(4.4, 1.70))
        flat.move_to([pat[0] + pw * 0.26, pat[1] - ph * 0.5 - P(0.30, 0.32), 0])
        self.play(FadeIn(got), run_time=0.45)
        self.play(FadeIn(flat), run_time=0.45)

        closer(self, "it comes and goes with the telescope",
               cx=P(0.0, 0.0), size=P(28, 21))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE TELL
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    BEAT, RT, HOLD = "B10", 1.550, 0.095

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The design tell",
               cite="computed in this reel: morphology search against the "
                    "cadence test, same signals")

        pw = P(6.40, 3.30)
        pat = [P(-1.55, 0.0), P(0.86, 1.00), 0]
        plate = _plate("compare.png", pw, pat, frame=False)
        ph = _plate_h("compare.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        for i, txt in enumerate(["leans", "corrects", "blinks"]):
            lb = _fit(_t(txt, size=P(20, 15), color=SOFT), P(2.6, 1.10))
            lb.move_to([pat[0] + (-0.31 + 0.31 * i) * pw,
                        pat[1] - ph * 0.5 - P(0.30, 0.32), 0])
            self.play(FadeIn(lb), run_time=0.35)

        col_at = P([3.70, 1.16, 0], [0, -1.24, 0])
        big = _fit(_t(CAD_CORRECTED, size=P(50, 36), color=ACCT,
                      weight="BOLD"), P(3.4, 2.00),
                   [col_at[0], col_at[1], 0])
        self.play(FadeIn(big, shift=UP * 0.10), run_time=0.65)
        sub = _fit(_t("found, where the search found nothing",
                      size=P(20, 15), color=SOFT), P(4.6, 3.34))
        sub.move_to([col_at[0], col_at[1] - P(0.58, 0.50), 0])
        self.play(FadeIn(sub), run_time=0.45)

        if not PORTRAIT:
            key = _fit(_t("ink: the morphology search      "
                          "terracotta: the cadence test", size=19,
                          color=SOFT), 9.6)
            key.move_to([0, -2.06, 0])
            self.play(FadeIn(key), run_time=0.45)

        closer(self, "ask where it came from", cx=P(0.0, 0.0))
        self.hold_to_beat()
