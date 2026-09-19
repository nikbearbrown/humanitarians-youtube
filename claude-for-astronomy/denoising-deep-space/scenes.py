"""scenes.py - Manim scenes for denoising-deep-space.

*The Sharpest Guess.* - ai-explainer, claude-hai, Ep. 09.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL
  Terracotta marks WHAT THE PRIOR SUPPLIED: the difference between two skies
  the telescope cannot distinguish, the disagreement between posterior
  samples, the variance-ratio curve, the invented half of a reconstruction.
  Ink marks WHAT THE PHOTONS MEASURED: the observation, the data-consistent
  part, the agreed core. The mapping never flips, so B05 teaches it once and
  every later plate reads for free.

  The load-bearing consequence is B08, where the disagreement map is the ONLY
  terracotta thing on screen and it is also the only honest output.

THIS FILE IS ASPECT-AWARE - IT RENDERS BOTH CUTS
  The reel ships in 16:9 (3840x2160) and 9:16 (2160x3840). Manim keeps
  frame_height = 8.0 in both, so the VERTICAL band plan is identical either
  way; only the horizontal extent changes - x +-6.15 landscape, x +-1.80
  portrait. Portrait is NOT a crop: at 4.5 units wide against 14.22 with the
  same height it has LESS usable area, so portrait compositions carry fewer
  elements, larger. That is a deliberate reduction, and the rule for choosing
  what goes is: anything the narration SPEAKS stays on screen.

LAYOUT BAND PLAN (every scene obeys it - this is what keeps the gates green)
                        landscape      portrait
  title                   +3.02          +3.14
  hairline                +2.66          +2.84
  the figure       +2.40 .. -1.90   +2.62 .. -2.02
  the closing line        -2.50          -2.42   (terracotta rule 0.28 below)
  the citation            -3.20          -2.95
  the wordmark bug        -3.12          -3.28   (right-anchored, LOGO LAW)

PLATES
  Every plate comes from assets/gen_deconv.py, which RUNS the calculations
  this episode describes: a real circular-aperture OTF with its hard zero,
  Poisson photons and Gaussian read noise, a Fourier stripe fit on known-dark
  columns (what NSClean does), a bisection that forces three different priors
  to identical chi-squared, and an EXACT posterior - a linear-Gaussian problem
  with a circulant PSF is diagonal in Fourier space, so the samples are exact
  rather than approximate.

  TWO CLAIMS ARE ASSERTED and the generator writes nothing if either fails:
  that detector striping is recoverable while lost information is not, and
  that two skies differing by half their structure produce IDENTICAL images.
  The sky is synthetic and every beat that shows it says so.

  PUBLISHED vs COMPUTED-HERE is kept visibly apart. B09 shows this reel's
  computed variance-ratio curve AND the two published figures beside it, with
  a tag separating them.

GATE NOTES (learned the expensive way on Eps. 03-08)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - An opaque chip over a texture is NOT enough for GATE B - clear a keep-out
    hole in the texture (Ep. 07 B10).
  - A _strike on a horizontal arrow is invisible; use a crossing X (Ep. 07).
  - Use _kclip() for any random fan: a raw rng.normal() is unbounded and one
    draw in a couple of dozen leaves the figure band entirely (Ep. 08 B09 put
    a line through the title).
  - SIZE A PLATE TO ITS BAND. Ep. 08's B04 plate was 4.19 units tall in a
    4.30-unit band and covered the title; no gate caught it. ph = pw * (ih/iw),
    so check it.
  - Anything placed with next_to() has a y that DEPENDS on its neighbour's
    rendered height. Measure it, do not estimate it (Ep. 08 B03).
  - Check BOTH aspects. Portrait failed GATE B 8/10 on Ep. 08's first pass
    where landscape failed 1/10.
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
        """
        target = BEAT_SECONDS.get(self.BEAT or "", 0.0)
        now = float(getattr(getattr(self, "renderer", None), "time", 0.0) or 0.0)
        self.wait(max(floor, target - TAIL_TRIM - now) if target else floor)






# ─────────────────────────────────────────────────────────────────────────────
#  Plate geometry note. Every plate here is a ROW of square panels, so
#      ph = pw * (ih / iw)
#  and iw/ih are known from gen_deconv.py: a 4-panel row is 1888x460 (4.10:1),
#  a 3-panel row is 1420x460 (3.09:1), the 5-panel posterior row is 2364x460
#  (5.14:1), and varratio is 1640x820 (2.00:1). The figure band is 4.30 units
#  tall (landscape) so a 4-panel row at pw = 11.0 is only 2.68 tall and fits
#  with room for labels. Ep. 08's B04 defect was exactly this arithmetic left
#  undone.
# ─────────────────────────────────────────────────────────────────────────────


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 0.816, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "AI in Astronomy & Space Science  ·  Ep. 09",
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

        r1 = _fit(_t("eight episodes", size=P(28, 22)), pw - 0.7)
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
        r2b = _fit(_t("AI draws it", size=P(26, 21), color=ACCT), pw - 0.7)
        r2b.move_to([pc[0], pc[1] - ph * 0.36, 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)

        closer(self, "Ep. 09  ·  the detail is not a measurement", size=P(27, 21))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — EXECUTIVE SUMMARY (BLUF)
# ═════════════════════════════════════════════════════════════════════════════
# EXECUTIVE-SUMMARY LAW: beat 2 is the one-breath gist and is explicitly "a
# text/kinetic-type beat or a single framing card - never a data dump, never
# the first exhibit". No plate here. The first exhibit is B03.
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.55, 0.337

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath",
               cite="some of the damage is arithmetic; the rest is an assumption")

        stage_w, stage_h = P(9.6, 3.44), 3.10
        sc = [0, P(0.55, 0.62), 0]
        self.play(Create(_card(stage_w, stage_h, sc)), run_time=0.7)

        rows = [("BLURRED AND NOISY", "every image", INK),
                ("SOME OF IT IS ARITHMETIC", "subtract and move on", INK),
                ("THE REST IS AN ASSUMPTION", "about what galaxies look like", ACCT)]
        for i, (big, small, col) in enumerate(rows):
            y = sc[1] + stage_h * (0.30 - 0.30 * i)
            a = _fit(_t(big, size=P(35, 24), color=col, weight="BOLD"),
                     stage_w - P(1.0, 0.5), [sc[0], y, 0])
            b = _fit(_t(small, size=P(24, 18), color=SOFT),
                     stage_w - P(1.0, 0.5), [sc[0], y - P(0.42, 0.34), 0])
            self.play(FadeIn(a, shift=UP * 0.10), run_time=0.55)
            self.play(FadeIn(b), run_time=0.35)
            if i == 2:
                self.play(Create(_underline(a, buff=0.10)), run_time=0.35)

        closer(self, "the gap gets filled either way", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — TWO KINDS OF DENOISING
# ═════════════════════════════════════════════════════════════════════════════
class B03_TwoKinds(Paced):
    BEAT, RT, HOLD = "B03", 1.55, 0.413

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Two different things called denoising",
               cite="1/f detector striping is fitted in blank sky and subtracted — NSClean, Rauscher 2024")

        # twokinds.png is a 4-panel row, 1888x460. pw 10.6 -> ph 2.58.
        pw = P(10.6, 3.44)
        pat = [0, P(1.02, 1.42), 0]
        plate = _plate("twokinds.png", pw, pat, frame=False)
        ph = _plate_h("twokinds.png", pw)
        self.play(FadeIn(plate), run_time=0.75)

        quarter = pw / 4.0
        names = ["striped", "cleaned", "blurred", "the truth"]
        labs = VGroup()
        for i, nm in enumerate(names):
            col = SOFT if i < 2 else ACCT
            lb = _fit(_t(nm, size=P(21, 14), color=col), quarter - P(0.26, 0.10))
            lb.move_to([pat[0] - pw / 2 + quarter * (i + 0.5),
                        pat[1] - ph / 2 - P(0.28, 0.20), 0])
            labs.add(lb)
        self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.18),
                  run_time=0.8)

        cap = _fit(_t("a synthetic field — the optics are real, the stars are not",
                      size=P(16, 13), color=SOFT), P(9.4, 3.30))
        cap.move_to([0, pat[1] - ph / 2 - P(0.82, 0.58), 0])
        self.play(FadeIn(cap), run_time=0.35)

        q = _quiet_chip("a pattern: measured, subtracted, 3.6% left",
                        size=P(20, 15), max_w=P(5.0, 3.34))
        q.move_to([P(-2.85, 0.0), P(-1.62, -1.30), 0])
        self.play(FadeIn(q, shift=UP * 0.08), run_time=0.55)

        a = _chip("a loss: nothing subtracts this", size=P(20, 15),
                  max_w=P(5.0, 3.34))
        a.move_to([P(2.85, 0.0), P(-1.62, -1.76), 0])
        self.play(FadeIn(a, shift=UP * 0.08), run_time=0.55)

        closer(self, "one is a pattern, one is a loss", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — THE CHAIN
# ═════════════════════════════════════════════════════════════════════════════
class B04_TheChain(Paced):
    BEAT, RT, HOLD = "B04", 1.55, 0.336

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What the telescope actually does",
               cite="circular-aperture OTF: H(k) = 0 above the cutoff, exactly — not approximately")

        pw = P(10.2, 3.44)
        pat = [0, P(1.18, 1.48), 0]
        plate = _plate("forward.png", pw, pat, frame=False)
        ph = _plate_h("forward.png", pw)
        self.play(FadeIn(plate), run_time=0.75)

        quarter = pw / 4.0
        names = ["the real sky", "blurred", "photons", "plus read noise"]
        labs = VGroup()
        for i, nm in enumerate(names):
            lb = _fit(_t(nm, size=P(20, 14), color=SOFT), quarter - P(0.24, 0.10))
            lb.move_to([pat[0] - pw / 2 + quarter * (i + 0.5),
                        pat[1] - ph / 2 - P(0.28, 0.20), 0])
            labs.add(lb)
        self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.16),
                  run_time=0.85)

        lossy = _chip("LOSSY", size=P(21, 16), max_w=P(2.0, 1.5))
        lossy.move_to([pat[0] - pw / 2 + quarter * 1.5,
                       pat[1] - ph / 2 - P(0.655, 0.62), 0])
        self.play(FadeIn(lossy, shift=UP * 0.08), run_time=0.5)

        n_at = P([0, -1.28, 0], [0, -1.30, 0])
        big = _fit(_t("98%", size=P(66, 46), color=ACCT, weight="BOLD"), P(2.2, 1.6))
        big.move_to(n_at)
        sub = _fit(_t("of the frequencies in the grid carry nothing at all",
                      size=P(22, 16), color=SOFT), P(7.6, 3.34))
        sub.move_to([n_at[0], n_at[1] - P(0.58, 0.48), 0])
        self.play(FadeIn(big, shift=UP * 0.10), run_time=0.55)
        self.play(FadeIn(sub), run_time=0.4)

        closer(self, "multiplied by zero, and gone", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE NULL SPACE  (the centrepiece; computed and asserted)
# ═════════════════════════════════════════════════════════════════════════════
class B05_SameData(Paced):
    BEAT, RT, HOLD = "B05", 1.55, 0.279

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Two skies, one image",
               cite="computed in this reel: the difference lies entirely above the cutoff, so H·δ = 0 exactly")

        pw = P(10.6, 3.44)
        pat = [0, P(1.05, 1.45), 0]
        plate = _plate("nullspace.png", pw, pat, frame=False)
        ph = _plate_h("nullspace.png", pw)
        self.play(FadeIn(plate), run_time=0.8)

        quarter = pw / 4.0
        names = (["sky one", "sky two", "how they differ", "what both look like"]
                 if not PORTRAIT else
                 ["sky one", "sky two", "differ", "observed"])
        labs = VGroup()
        for i, nm in enumerate(names):
            col = ACCT if i == 2 else SOFT
            lb = _fit(_t(nm, size=P(20, 13), color=col), quarter - P(0.24, 0.08))
            lb.move_to([pat[0] - pw / 2 + quarter * (i + 0.5),
                        pat[1] - ph / 2 - P(0.28, 0.20), 0])
            labs.add(lb)
        self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.18),
                  run_time=0.85)

        left_at = P([-3.10, -1.30, 0], [0, -0.30, 0])
        a = _fit(_t("52%", size=P(54, 38), color=ACCT, weight="BOLD"), P(1.9, 1.4))
        a.move_to(left_at)
        al = _fit(_t("apart, as skies", size=P(21, 16), color=SOFT), P(3.4, 3.30))
        al.move_to([left_at[0] + P(1.75, 0.0), left_at[1] + P(0.0, -0.50), 0])
        self.play(FadeIn(a, shift=UP * 0.10), run_time=0.5)
        self.play(FadeIn(al), run_time=0.35)

        right_at = P([2.70, -1.30, 0], [0, -1.35, 0])
        b = _fit(_t("0.0000", size=P(54, 38), weight="BOLD"), P(2.8, 2.0))
        b.move_to(right_at)
        bl = _fit(_t("noise sigma between their images", size=P(21, 16), color=SOFT),
                  P(4.6, 3.34))
        bl.move_to([right_at[0] + P(0.0, 0.0), right_at[1] - P(0.52, 0.44), 0])
        self.play(FadeIn(b, shift=UP * 0.10), run_time=0.5)
        self.play(FadeIn(bl), run_time=0.35)
        self.play(Create(_underline(b, buff=0.08)), run_time=0.3)

        closer(self, "the data cannot tell them apart", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — THREE ANSWERS
# ═════════════════════════════════════════════════════════════════════════════
class B06_ThreeAnswers(Paced):
    BEAT, RT, HOLD = "B06", 1.55, 0.275

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Three assumptions, three sharp galaxies",
               cite="each prior's strength is solved so χ²/N = 1 — equally consistent with the same data")

        # threeanswers.png is a 3-panel row, 1420x460 (3.09:1)
        pw = P(8.4, 3.42)
        pat = [0, P(1.15, 1.42), 0]
        plate = _plate("threeanswers.png", pw, pat, frame=False)
        ph = _plate_h("threeanswers.png", pw)
        self.play(FadeIn(plate), run_time=0.8)

        third = pw / 3.0
        names = ["smooth prior", "matched prior", "rough prior"]
        chis = ["χ²/N = 1.008", "χ²/N = 1.007", "χ²/N = 1.008"]
        labs, cl = VGroup(), VGroup()
        for i, nm in enumerate(names):
            lb = _fit(_t(nm, size=P(21, 15), color=SOFT), third - P(0.24, 0.10))
            lb.move_to([pat[0] - pw / 2 + third * (i + 0.5),
                        pat[1] - ph / 2 - P(0.28, 0.22), 0])
            labs.add(lb)
            cv = _fit(_t(chis[i], size=P(19, 14), color=INK), third - P(0.24, 0.10))
            cv.move_to([pat[0] - pw / 2 + third * (i + 0.5),
                        pat[1] - ph / 2 - P(0.58, 0.46), 0])
            cl.add(cv)
        self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.2),
                  run_time=0.7)
        self.play(LaggedStart(*[FadeIn(c) for c in cl], lag_ratio=0.2),
                  run_time=0.7)

        # No rule here. It sat 0.10 units above this line and GATE B read the
        # line as a label on a curve; the sentence says "equally" on its own.
        eq = _fit(_t("all three match the data equally well",
                     size=P(22, 16), color=SOFT), P(7.4, 3.34))
        eq.move_to([pat[0], pat[1] - ph / 2 - P(0.92, 0.76), 0])
        self.play(FadeIn(eq), run_time=0.4)

        chip = _chip("yet they differ from each other by 36%", size=P(23, 17),
                     max_w=P(6.0, 3.34))
        chip.move_to([0, P(-1.74, -1.70), 0])
        self.play(FadeIn(chip, shift=UP * 0.08), run_time=0.55)

        closer(self, "sharpness is a choice", size=P(31, 24))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — WHERE THE DETAIL COMES FROM
# ═════════════════════════════════════════════════════════════════════════════
class B07_WhereItComesFrom(Paced):
    BEAT, RT, HOLD = "B07", 1.55, 0.057

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Where the detail comes from",
               cite="diffusion prior trained on 17,852 TNG100 cutouts; DPS at inference (arXiv:2411.19158)")

        bw, bh = P(4.30, 3.20), P(2.30, 1.46)
        left = P([-3.45, 1.10, 0], [0, 1.80, 0])
        right = P([3.45, 1.10, 0], [0, -0.60, 0])

        # the training set, as a grid of tiles — ink, because it is real data
        card = _card(bw, bh, left)
        self.play(Create(card), run_time=0.6)
        # The label is a HEADING, above the grid. Beneath it, it landed on the
        # bottom row of tiles — and a Square has a stroke, so GATE B correctly
        # called it a label on a curve.
        lt = _fit(_t("the training set", size=P(21, 16), color=SOFT), bw - 0.4)
        lt.move_to([left[0], left[1] + bh * 0.36, 0])
        self.play(FadeIn(lt), run_time=0.35)

        rng = np.random.default_rng(23)
        tiles = VGroup()
        cols, rows = P(11, 8), P(6, 5)
        for i in range(cols):
            for j in range(rows):
                tx = left[0] - bw * 0.40 + (i + 0.5) * (bw * 0.80 / cols)
                ty = left[1] + bh * 0.16 - (j + 0.5) * (bh * 0.58 / rows)
                tiles.add(Square(side_length=P(0.17, 0.14), color=GHOST,
                                 fill_color=INK,
                                 fill_opacity=float(rng.uniform(0.25, 0.85)),
                                 stroke_width=0.8).move_to([tx, ty, 0]))
        self.play(LaggedStart(*[FadeIn(t) for t in tiles], lag_ratio=0.004),
                  run_time=0.9)

        # the prior — terracotta, because everything it supplies is an assumption
        pb = RoundedRectangle(width=bw, height=bh, corner_radius=0.14,
                              color=ACC, fill_color=ACC, fill_opacity=1.0,
                              stroke_width=0).move_to(right)
        self.play(Create(pb), run_time=0.6)
        pt = _fit(_t("THE PRIOR", size=P(24, 19), color=CARD, weight="BOLD"),
                  bw - 0.5, [right[0], right[1] + bh * 0.20, 0])
        pq = _fit(_t("what a galaxy looks like", size=P(22, 17), color=CARD),
                  bw - 0.5, [right[0], right[1] - bh * 0.16, 0])
        self.play(FadeIn(pt), FadeIn(pq), run_time=0.5)

        if PORTRAIT:
            arr = _arrow([0, left[1] - bh / 2 - 0.10, 0],
                         [0, right[1] + bh / 2 + 0.10, 0], color=INK)
        else:
            arr = _arrow([left[0] + bw / 2 + 0.10, left[1], 0],
                         [right[0] - bw / 2 - 0.10, right[1], 0], color=INK)
        self.play(GrowArrow(arr), run_time=0.5)

        n_at = P([-3.45, -1.35, 0], [0, -1.55, 0])
        n = _fit(_t("17,852", size=P(52, 36), color=ACCT, weight="BOLD"), P(2.6, 1.9))
        n.move_to(n_at)
        nl = _fit(_t("simulated galaxies", size=P(21, 16), color=SOFT), P(4.2, 3.30))
        nl.move_to([n_at[0], n_at[1] - P(0.52, 0.44), 0])
        self.play(FadeIn(n, shift=UP * 0.10), run_time=0.5)
        self.play(FadeIn(nl), run_time=0.35)

        # LANDSCAPE ONLY: the cost pair. Portrait has no room for a third
        # column of figures and the narration never speaks these two.
        if not PORTRAIT:
            # "133 GPU-hours" collapsed 133 hours x 32 V100s by a factor of
            # 32. The paper's figure is 133 hours ON 32 GPUs.
            cost = _fit(_t("133 hours on 32 GPUs to train  ·  100 seconds to sample",
                           size=20, color=SOFT), 6.6)
            cost.move_to([3.20, -1.42, 0])
            self.play(FadeIn(cost), run_time=0.4)

        closer(self, "the most likely galaxy it was ever shown", size=P(28, 21))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — MANY ANSWERS
# ═════════════════════════════════════════════════════════════════════════════
class B08_ManyAnswers(Paced):
    BEAT, RT, HOLD = "B08", 1.55, 0.297

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Return the range, not the picture",
               cite="256 EXACT posterior samples — linear-Gaussian with a circulant PSF is diagonal in Fourier space")

        # posterior.png is a 5-panel row, 2364x460 (5.14:1)
        pw = P(11.4, 3.44)
        pat = [0, P(1.35, 1.72), 0]
        plate = _plate("posterior.png", pw, pat, frame=False)
        ph = _plate_h("posterior.png", pw)
        self.play(FadeIn(plate), run_time=0.8)

        # PORTRAIT DROPS THE PANEL LABELS. Five of them across 3.44 units are
        # 0.69 units each and unreadable; the two sentence rows below name
        # what the panels are, and the narration speaks them.
        if not PORTRAIT:
            fifth = pw / 5.0
            names = ["a sample", "another", "another", "their mean",
                     "where they disagree"]
            labs = VGroup()
            for i, nm in enumerate(names):
                col = ACCT if i == 4 else SOFT
                lb = _fit(_t(nm, size=19, color=col), fifth - 0.20)
                lb.move_to([pat[0] - pw / 2 + fifth * (i + 0.5),
                            pat[1] - ph / 2 - 0.26, 0])
                labs.add(lb)
            self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.14),
                      run_time=0.9)

        rows = [("where they agree, the photons decided", SOFT),
                ("where they disagree, the prior did", ACCT)]
        base = P([0, -0.62, 0], [0, -0.45, 0])
        for i, (txt, col) in enumerate(rows):
            y = base[1] - i * P(0.62, 0.56)
            bold = "BOLD" if i == 1 else None
            a = _fit(_t(txt, size=P(27, 19), color=col, weight=bold),
                     P(10.6, 3.36), [base[0], y, 0])
            self.play(FadeIn(a, shift=UP * 0.06), run_time=0.45)

        chip = _chip("above the cutoff the spread IS the prior — 1.0000",
                     size=P(21, 15), max_w=P(6.8, 3.34))
        chip.move_to([0, P(-1.78, -1.80), 0])
        self.play(FadeIn(chip, shift=UP * 0.08), run_time=0.55)

        closer(self, "the spread is the answer", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — THE DETECTOR
# ═════════════════════════════════════════════════════════════════════════════
class B09_WhenItInvents(Paced):
    BEAT, RT, HOLD = "B09", 1.55, 0.176

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "A ratio that says how much was invented",
               cite="curve computed here; the two figures beside it are published (arXiv:2411.19158)")

        # varratio.png is 1640x820, so ph = pw / 2 — by far the tallest plate
        # in the reel. At pw = 7.2 it is 3.60 units tall in a 4.30-unit band,
        # which pushed its top to +2.72 (past FIG_TOP) and put its axis label
        # into the title. Sized to the band, and BOTH axis labels go below it.
        pw = P(5.80, 3.40)
        pat = [P(-3.10, 0.0), P(0.85, 1.42), 0]
        plate = _plate("varratio.png", pw, pat, frame=True)
        ph = _plate_h("varratio.png", pw)
        self.play(FadeIn(plate), run_time=0.8)

        ax = _fit(_t("the data gets stronger  →", size=P(20, 15), color=SOFT),
                  P(5.0, 3.30))
        ax.move_to([pat[0], pat[1] - ph / 2 - P(0.28, 0.24), 0])
        self.play(FadeIn(ax), run_time=0.35)
        yl = _fit(_t("posterior spread ÷ prior spread", size=P(19, 14), color=SOFT),
                  P(5.0, 3.30))
        yl.move_to([pat[0], pat[1] - ph / 2 - P(0.56, 0.52), 0])
        self.play(FadeIn(yl), run_time=0.35)

        # The ring carries itself. Its label crossed the portrait safe edge at
        # x = -2.11 and collided with the axis label in both aspects.
        ring_at = [pat[0] - pw * 0.34, pat[1] + ph * 0.26, 0]
        self.play(Create(Circle(radius=P(0.50, 0.30), color=ACC,
                                stroke_width=P(5, 4)).move_to(ring_at)),
                  run_time=0.45)

        col_at = P([3.90, 1.45, 0], [0, -0.50, 0])
        col_w = P(4.00, 3.36)
        pub = [("0.0114", "at signal-to-noise 699"),
               ("0.0685", "at signal-to-noise 7")]
        for i, (big, small) in enumerate(pub):
            y = col_at[1] - i * P(1.16, 0.72)
            a = _fit(_t(big, size=P(44, 32), weight="BOLD"), col_w,
                     [col_at[0], y, 0])
            b = _fit(_t(small, size=P(20, 15), color=SOFT), col_w,
                     [col_at[0], y - P(0.50, 0.40), 0])
            self.play(FadeIn(a, shift=UP * 0.08), run_time=0.45)
            self.play(FadeIn(b), run_time=0.3)

        tag = _quiet_chip("published, not measured here", size=P(19, 14),
                          max_w=P(4.40, 3.30))
        tag.move_to([col_at[0], col_at[1] - P(2.10, 1.52), 0])
        self.play(FadeIn(tag), run_time=0.5)

        closer(self, "the ratio is the alarm", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE DESIGN TELL
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    BEAT, RT, HOLD = "B10", 1.278, 0.0

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The design tell",
               cite="HST reconstructions checked against JWST of the same sources — a QUALITATIVE comparison only")

        cw, ch = P(6.00, 3.30), P(2.80, 2.25)
        cc = P([-3.00, 0.90, 0], [0, 1.32, 0])
        self.play(Create(_card(cw, ch, cc)), run_time=0.65)
        head = _fit(_t("WHAT A DENOISER ACTUALLY DOES", size=P(23, 18),
                       color=ACCT, weight="BOLD"), cw - 0.7,
                    [cc[0], cc[1] + ch * 0.33, 0])
        self.play(FadeIn(head), run_time=0.45)
        self.play(Create(Line([cc[0] - cw * 0.40, cc[1] + ch * 0.19, 0],
                              [cc[0] + cw * 0.40, cc[1] + ch * 0.19, 0],
                              color=RULE, stroke_width=2)), run_time=0.3)

        r1 = _fit(_t("removes the noise", size=P(27, 21)), cw - 1.0,
                  [cc[0], cc[1] - ch * 0.02, 0])
        self.play(FadeIn(r1), run_time=0.45)
        self.play(Create(_strike(r1, pad=0.12)), run_time=0.45)

        r2 = _fit(_t("adds an assumption", size=P(27, 21), color=ACCT,
                     weight="BOLD"), cw - 1.0, [cc[0], cc[1] - ch * 0.30, 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.45)
        box = Rectangle(width=min(float(r2.width) + 0.44, cw - 0.6),
                        height=float(r2.height) + 0.34, color=ACC,
                        stroke_width=P(4, 3), fill_opacity=0).move_to(r2)
        self.play(Create(box), run_time=0.45)

        # The external check. PORTRAIT DROPS THE TWO CARDS: their labels
        # collided with QUALITATIVELY, and the word is the part the narration
        # actually speaks.
        qual_x = P(3.62, 0.0)
        if not PORTRAIT:
            gw = 1.95
            ga = [2.55, 1.25, 0]
            gb = [4.70, 1.25, 0]
            for at, nm, soft in ((ga, "Hubble", True), (gb, "Webb", False)):
                self.play(Create(_card(gw, gw, at, radius=0.10)), run_time=0.4)
                # Schematic, not data: a soft blob for the blurred view and a
                # tighter one with structure for the sharper view. An empty
                # white card read as an unfilled placeholder.
                if soft:
                    g = Ellipse(width=gw * 0.52, height=gw * 0.34, color=GHOST,
                                fill_color=GHOST, fill_opacity=0.55,
                                stroke_width=0).move_to(at)
                    self.play(FadeIn(g), run_time=0.3)
                else:
                    g = VGroup(Ellipse(width=gw * 0.44, height=gw * 0.26,
                                       color=SOFT, fill_color=SOFT,
                                       fill_opacity=0.5,
                                       stroke_width=0).move_to(at))
                    for dx, dy in ((-0.30, 0.16), (0.26, -0.13), (0.10, 0.22)):
                        g.add(Dot(point=[at[0] + dx * gw, at[1] + dy * gw,
                                         0], radius=0.045, color=INK))
                    self.play(FadeIn(g), run_time=0.3)
                lb = _fit(_t(nm, size=20, color=SOFT), gw)
                lb.move_to([at[0], at[1] - gw / 2 - 0.24, 0])
                self.play(FadeIn(lb), run_time=0.3)

            # A DRAWN tick. The "✓" character is absent from EB Garamond and
            # rendered as stray digits on screen.
            mid = [(ga[0] + gb[0]) / 2, (ga[1] + gb[1]) / 2 + 0.92, 0]
            r = 0.20
            tick = VGroup(
                Line([mid[0] - r, mid[1], 0],
                     [mid[0] - r * 0.25, mid[1] - r * 0.7, 0],
                     color=ACCT, stroke_width=7),
                Line([mid[0] - r * 0.25, mid[1] - r * 0.7, 0],
                     [mid[0] + r, mid[1] + r * 0.8, 0],
                     color=ACCT, stroke_width=7))
            self.play(Create(tick), run_time=0.4)

        qual = _fit(_t("QUALITATIVELY", size=P(22, 20), weight="BOLD"),
                    P(3.4, 3.30))
        qual.move_to([qual_x, P(-0.62, -1.10), 0])
        self.play(FadeIn(qual), run_time=0.45)

        # LANDSCAPE ONLY — portrait has no room, and the closer carries it
        note = _fit(_t("no published rate for how often it is wrong",
                       size=P(19, 17), color=SOFT), P(5.6, 3.34))
        note.move_to([qual_x, P(-1.22, -1.66), 0])
        self.play(FadeIn(note), run_time=0.4)

        closer(self, "report the range, not the picture", size=P(29, 22))
        self.hold_to_beat()
