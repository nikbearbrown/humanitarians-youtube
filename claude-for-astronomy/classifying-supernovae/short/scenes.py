"""scenes.py - Manim scenes for classifying-supernovae.

*What We Chased Before.* - ai-explainer, claude-hai, Ep. 10.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL
  Terracotta marks WHAT DOUBT FINDS: the rare class in every plot, the
  uncertainty-sampling picks, the exploration quota, the one recall curve that
  actually moves. Ink marks THE CONFIDENT MAJORITY: the well-sampled classes,
  the accuracy number that rises while nothing improves, and the count of
  confirmed Ia that exploration costs you.

  The load-bearing consequence is B06, where the ink curves lie flat on the
  axis at zero for twelve seasons while the accuracy panel beside them climbs.
  That contrast is the episode.

THIS FILE IS ASPECT-AWARE - IT RENDERS BOTH CUTS
  The reel ships in 16:9 (3840x2160) and 9:16 (2160x3840). Manim keeps
  frame_height = 8.0 in both, so the VERTICAL band plan is identical either
  way; only the horizontal extent changes - x +-6.15 landscape, x +-1.80
  portrait. Portrait is NOT a crop: it has LESS usable area, so it carries
  fewer elements, larger. The rule for choosing what goes: anything the
  narration SPEAKS stays on screen.

LAYOUT BAND PLAN (every scene obeys it - this is what keeps the gates green)
                        landscape      portrait
  title                   +3.02          +3.14
  hairline                +2.66          +2.84
  the figure       +2.40 .. -1.90   +2.62 .. -2.02
  the closing line        -2.50          -2.42   (terracotta rule 0.28 below)
  the citation            -3.20          -2.95
  the wordmark bug        -3.12          -3.28   (right-anchored, LOGO LAW)

PLATES
  Every plate comes from assets/gen_triage.py, which RUNS a real closed-loop
  experiment: 60 repeats x 12 seasons x 20 spectra, three follow-up
  strategies, and a hand-written Gaussian naive Bayes chosen precisely BECAUSE
  a class with no labelled examples cannot be predicted at all - so the
  feedback mechanism this episode is about is visible in the model rather than
  buried inside an ensemble.

  The central claim is ASSERTED and the generator writes nothing if it fails.
  Results are MEDIANS: the outcome is bimodal (a greedy run either stumbles on
  a rare object early or never sees one), and a 12-repeat mean read 0.088
  where the median is 0.000 and 48 runs in 60 end with no recall at all.

  PUBLISHED vs COMPUTED-HERE is kept visibly apart. B04 is a published ledger
  and says so on screen; B06-B08 and B10 are computed here and say so.

PLATE GEOMETRY - ph = pw * (ih/iw). Do this arithmetic, do not assume it.
  selection   1500x760   0.507     deadline  1560x780  0.500
  loop        1720x740   0.430     composition 1720x620 0.360
  boundary    1720x700   0.407     budget    1560x780  0.500
  The landscape figure band is 4.30 units tall, so a plate at pw = 8.0 with
  ratio 0.50 is 4.00 tall and leaves almost nothing for labels. Ep. 09's B09
  put a 3.60-unit plate at y = 0.92 and its top hit +2.72, past FIG_TOP.

GATE NOTES (learned the expensive way on Eps. 03-09)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - NEVER use a glyph outside the font's coverage. EB Garamond has no "check"
    character and Ep. 09 rendered it as stray digits on screen. Draw marks
    from Lines.
  - Use _kclip() for any random fan: a raw rng.normal() is unbounded.
  - A label under a grid of Squares lands ON a stroke - GATE B calls that a
    label on a curve. Put it above (Ep. 09 B07).
  - Anything placed with next_to() has a y that DEPENDS on its neighbour's
    rendered height. Measure it, do not estimate it (Ep. 08 B03, twice).
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
        """
        target = BEAT_SECONDS.get(self.BEAT or "", 0.0)
        now = float(getattr(getattr(self, "renderer", None), "time", 0.0) or 0.0)
        self.wait(max(floor, target - TAIL_TRIM - now) if target else floor)






# ─────────────────────────────────────────────────────────────────────────────
#  Plate geometry note. A plate placed by WIDTH gets its height for free:
#      ph = pw * (ih / iw)
#  The six plates from gen_triage.py are, in pixels and as ratios:
#      selection 1500x760 (0.507)   deadline    1560x780 (0.500)
#      loop      1720x740 (0.430)   composition 1720x620 (0.360)
#      boundary  1720x700 (0.407)   budget      1560x780 (0.500)
#  The landscape figure band is 4.30 units tall, so `deadline` at pw = 8.0 is
#  4.00 tall and leaves almost nothing for labels -- B03 sets pw = 6.40 for
#  exactly that reason. Do this arithmetic; Ep. 08's B04 defect was this
#  multiplication left undone, and the plate covered its own title.
# ─────────────────────────────────────────────────────────────────────────────




# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 0.721, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "AI in Astronomy & Space Science  ·  Ep. 10",
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

        r1 = _fit(_t("nine episodes", size=P(28, 22)), pw - 0.7)
        r1.move_to([pc[0], pc[1] + ph * 0.31, 0])
        r1b = _fit(_t("AI looks at the sky", size=P(24, 19), color=SOFT), pw - 0.7)
        r1b.move_to([pc[0], pc[1] + ph * 0.13, 0])
        self.play(FadeIn(r1), FadeIn(r1b), run_time=0.5)
        self.play(Create(_strike(r1b, pad=0.10)), run_time=0.45)

        self.play(Create(Line([pc[0] - pw * 0.42, pc[1] - ph * 0.02, 0],
                              [pc[0] + pw * 0.42, pc[1] - ph * 0.02, 0],
                              color=RULE, stroke_width=2)), run_time=0.3)

        r2 = _fit(_t("this one", size=P(30, 24), color=ACCT, weight="BOLD"), pw - 0.7)
        r2.move_to([pc[0], pc[1] - ph * 0.18, 0])
        r2b = _fit(_t("AI chooses what we look at", size=P(23, 18), color=ACCT),
                   pw - 0.8)
        r2b.move_to([pc[0], pc[1] - ph * 0.36, 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)

        closer(self, "Ep. 10  ·  the sample is the decision", size=P(28, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — EXECUTIVE SUMMARY (BLUF)
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.550, 0.042

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath",
               cite="the training set is the record of what we chose last time")

        stage_w, stage_h = P(9.6, 3.44), 3.10
        sc = [0, P(0.55, 0.62), 0]
        self.play(Create(_card(stage_w, stage_h, sc)), run_time=0.7)

        rows = [("IT FADES IN DAYS", "decide tonight", INK),
                ("THERE ARE TOO MANY", "something must choose", INK),
                ("IT LEARNED FROM OUR LAST CHOICE", "", ACCT)]
        for i, (big, small, col) in enumerate(rows):
            y = sc[1] + stage_h * (0.30 - 0.30 * i)
            a = _fit(_t(big, size=P(35, 23), color=col, weight="BOLD"),
                     stage_w - P(1.0, 0.5), [sc[0], y, 0])
            self.play(FadeIn(a, shift=UP * 0.10), run_time=0.55)
            if small:
                b = _fit(_t(small, size=P(24, 18), color=SOFT),
                         stage_w - P(1.0, 0.5), [sc[0], y - P(0.42, 0.34), 0])
                self.play(FadeIn(b), run_time=0.35)
            else:
                self.play(Create(_underline(a, buff=0.10)), run_time=0.4)

        closer(self, "the loop was already closed", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE DEADLINE
# ═════════════════════════════════════════════════════════════════════════════
class B03_TheDeadline(Paced):
    BEAT, RT, HOLD = "B03", 1.550, 0.124

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "It fades while you decide",
               cite="computed Bazin light curves; Rubin alert volume and follow-up fraction are published")

        # deadline.png is 1560x780 -> ratio 0.500. pw 6.0 -> ph 3.00.
        pw = P(6.40, 3.30)
        pat = [P(-2.85, 0.0), P(0.75, 1.02), 0]
        plate = _plate("deadline.png", pw, pat, frame=True)
        ph = _plate_h("deadline.png", pw)
        self.play(FadeIn(plate), run_time=0.8)

        ax = _fit(_t("days from discovery  →", size=P(20, 15), color=SOFT),
                  P(5.2, 3.30))
        ax.move_to([pat[0], pat[1] - ph / 2 - P(0.28, 0.24), 0])
        self.play(FadeIn(ax), run_time=0.35)
        # LANDSCAPE ONLY. The narration says "a spectrum is only useful
        # early", so this caption is on-screen-only, and portrait cannot fit
        # plate + two captions + two counters with sublines + a closer.
        if not PORTRAIT:
            win = _fit(_t("the window where a spectrum still says something",
                          size=19, color=ACCT), 5.6)
            win.move_to([pat[0], pat[1] - ph / 2 - 0.58, 0])
            self.play(FadeIn(win), run_time=0.4)

        col_at = P([3.60, 1.42, 0], [0, -0.55, 0])
        col_w = P(4.20, 3.34)
        stats = [("10,000,000", "changes a night, once Rubin is running", INK),
                 ("1 in 10", "ever gets a spectrum", ACCT)]
        for i, (big, small, colr) in enumerate(stats):
            y = col_at[1] - i * P(1.30, 0.86)
            a = _fit(_t(big, size=P(44, 32), color=colr, weight="BOLD"), col_w,
                     [col_at[0], y, 0])
            b = _fit(_t(small, size=P(20, 15), color=SOFT), col_w,
                     [col_at[0], y - P(0.52, 0.42), 0])
            self.play(FadeIn(a, shift=UP * 0.10), run_time=0.5)
            self.play(FadeIn(b), run_time=0.32)
            if i == 1:
                self.play(Create(_underline(a, buff=0.06)), run_time=0.3)

        closer(self, "the decision cannot wait", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — WHICH ONES
# ═════════════════════════════════════════════════════════════════════════════
class B04_WhichOnes(Paced):
    BEAT, RT, HOLD = "B04", 1.550, 0.478

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "And which ones got chosen",
               cite="published confirmation fractions by peak magnitude — a ledger, not measured here")

        # selection.png is 1500x760 -> ratio 0.507. pw 7.4 -> ph 3.75 (too tall);
        # pw 6.4 -> ph 3.24, which fits the 4.30 band with labels beneath.
        pw = P(6.40, 3.40)
        pat = [0, P(0.74, 0.92), 0]
        plate = _plate("selection.png", pw, pat, frame=False)
        ph = _plate_h("selection.png", pw)
        self.play(FadeIn(plate), run_time=0.8)

        quarter = pw / 4.0
        names = ["< 17", "17–18.5", "18.5–20", "20–22"]
        labs = VGroup()
        for i, nm in enumerate(names):
            col = ACCT if i >= 2 else SOFT
            lb = _fit(_t(nm, size=P(21, 15), color=col), quarter - P(0.22, 0.10))
            lb.move_to([pat[0] - pw / 2 + quarter * (i + 0.5),
                        pat[1] - ph / 2 - P(0.28, 0.22), 0])
            labs.add(lb)
        self.play(LaggedStart(*[FadeIn(l) for l in labs], lag_ratio=0.18),
                  run_time=0.8)

        # No axis label: the bar labels already name the magnitudes, and it
        # sat between the tag and the note and collided with both.
        tag = _quiet_chip("published, not measured here", size=P(19, 14),
                          max_w=P(4.20, 3.30))
        tag.move_to([P(-3.50, 0.0), P(-1.52, -1.28), 0])
        self.play(FadeIn(tag), run_time=0.5)

        note = _fit(_t("nobody wrote that rule down", size=P(24, 18), color=ACCT,
                       weight="BOLD"), P(4.60, 3.34))
        note.move_to([P(2.95, 0.0), P(-1.52, -1.80), 0])
        self.play(FadeIn(note, shift=UP * 0.08), run_time=0.5)

        closer(self, "the bright ones, every time", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE LOOP
# ═════════════════════════════════════════════════════════════════════════════
class B05_TheLoop(Paced):
    BEAT, RT, HOLD = "B05", 1.214, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The loop was already closed",
               cite="Ishida+2019: the spectroscopic sample over-represents bright objects and SNe Ia")

        steps = [("WE CHOOSE", "what to point at"),
                 ("IT GETS A LABEL", "a spectrum, a type"),
                 ("THE MODEL LEARNS", "from those labels"),
                 ("IT RECOMMENDS", "more of the same")]
        bw, bh = P(2.72, 3.10), P(1.05, 0.72)
        if PORTRAIT:
            pos = [[0, 1.94 - i * 0.92, 0] for i in range(4)]
        else:
            pos = [[-4.35 + i * 2.90, 1.28, 0] for i in range(4)]

        for i, ((big, small), at) in enumerate(zip(steps, pos)):
            last = i == 3
            bx = RoundedRectangle(width=bw, height=bh, corner_radius=0.12,
                                  color=ACC if last else GHOST,
                                  fill_color=ACC if last else CARD,
                                  fill_opacity=1.0,
                                  stroke_width=0 if last else 1.8).move_to(at)
            tb = _fit(_t(big, size=P(19, 17), color=CARD if last else INK,
                         weight="BOLD"), bw - 0.28,
                      [at[0], at[1] + bh * 0.18, 0])
            ts = _fit(_t(small, size=P(16, 14), color=CARD if last else SOFT),
                      bw - 0.28, [at[0], at[1] - bh * 0.21, 0])
            self.play(Create(bx), run_time=0.40)
            self.play(FadeIn(tb), FadeIn(ts), run_time=0.34)
            if i:
                if PORTRAIT:
                    self.play(GrowArrow(_arrow(
                        [0, pos[i - 1][1] - bh / 2 - 0.04, 0],
                        [0, at[1] + bh / 2 + 0.04, 0], color=INK, sw=3.4)),
                        run_time=0.26)
                else:
                    self.play(GrowArrow(_arrow(
                        [pos[i - 1][0] + bw / 2 + 0.04, at[1], 0],
                        [at[0] - bw / 2 - 0.04, at[1], 0], color=INK, sw=3.4)),
                        run_time=0.26)

        # The return leg, routed BELOW (or beside) every label rather than
        # through it. A closed ellipse drawn across the boxes put a stroke
        # under all eight text objects and GATE B called every one of them a
        # label on a curve.
        if PORTRAIT:
            rx = 1.46
            legs = [[rx, pos[3][1], 0], [rx, pos[0][1], 0], [0.62, pos[0][1], 0]]
            start = [pos[3][0] + bw / 2 + 0.04, pos[3][1], 0]
        else:
            ry = 0.18
            legs = [[pos[3][0], ry, 0], [pos[0][0], ry, 0],
                    [pos[0][0], pos[0][1] - bh / 2 - 0.06, 0]]
            start = [pos[3][0], pos[3][1] - bh / 2 - 0.04, 0]
        path = VMobject().set_points_as_corners([start] + legs[:-1])
        path.set_stroke(ACC, width=P(6, 5))
        self.play(Create(path), run_time=0.7)
        self.play(GrowArrow(_arrow(legs[-2], legs[-1], color=ACC, sw=P(6, 5))),
                  run_time=0.4)

        chip = _chip("the training set is the output of the last decision",
                     size=P(21, 15), max_w=P(7.4, 3.34))
        chip.move_to([0, P(-1.52, -1.62), 0])
        self.play(FadeIn(chip, shift=UP * 0.08), run_time=0.55)

        closer(self, "best at what we already looked at", size=P(29, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — TWELVE SEASONS  (the experiment; computed here)
# ═════════════════════════════════════════════════════════════════════════════
class B06_TwelveSeasons(Paced):
    BEAT, RT, HOLD = "B06", 1.550, 0.491

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Twelve seasons, spent on confidence",
               cite="computed in this reel: 60 repeats × 12 seasons × 20 spectra; medians, because the outcome is bimodal")

        # ratio 0.430. At pw = 9.0 this is 3.87 units tall in a 4.30 band and
        # left 0.43 for two panel labels, an axis label and a counter. In
        # landscape the counter moves BESIDE the plate instead.
        pw = P(7.00, 3.44)
        ph = _plate_h("loop.png", pw)
        pat = [P(-2.45, 0.0), P(0.85, 1.58), 0]
        plate = _plate("loop.png", pw, pat, frame=False)
        self.play(FadeIn(plate), run_time=0.8)

        for i, nm in enumerate(["overall accuracy", "rare-class recall"]):
            col = INK if i == 0 else ACCT
            lb = _fit(_t(nm, size=P(20, 14), color=col), pw / 2 - P(0.30, 0.12))
            lb.move_to([pat[0] - pw / 4 + (pw / 2) * i,
                        pat[1] - ph / 2 - P(0.28, 0.22), 0])
            self.play(FadeIn(lb), run_time=0.4)

        n_at = P([3.55, 1.10, 0], [0, -0.55, 0])
        big = _fit(_t("48 of 60", size=P(50, 38), color=ACCT, weight="BOLD"),
                   P(3.6, 2.4))
        big.move_to(n_at)
        sub = _fit(_t("runs end without recognising the rare class even once",
                      size=P(21, 16), color=SOFT), P(4.60, 3.36))
        sub.move_to([n_at[0], n_at[1] - P(0.62, 0.52), 0])
        self.play(FadeIn(big, shift=UP * 0.10), run_time=0.55)
        self.play(FadeIn(sub), run_time=0.4)

        closer(self, "accuracy never warned anyone", size=P(30, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — WHAT GOT LABELLED
# ═════════════════════════════════════════════════════════════════════════════
class B07_WhatGotLabelled(Paced):
    BEAT, RT, HOLD = "B07", 1.550, 0.105

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "What ended up in the training set",
               cite="computed in this reel: class composition of the labelled set, season by season")

        # composition.png is 1720x620 -> ratio 0.360. pw 10.0 -> ph 3.60.
        pw = P(8.60, 3.44)
        ph = _plate_h("composition.png", pw)
        pat = [0, P(2.35 - ph / 2, 1.46), 0]
        plate = _plate("composition.png", pw, pat, frame=False)
        self.play(FadeIn(plate), run_time=0.8)

        for i, nm in enumerate(["spent on confidence", "spent on doubt"]):
            col = INK if i == 0 else ACCT
            lb = _fit(_t(nm, size=P(22, 15), color=col), pw / 2 - P(0.40, 0.14))
            lb.move_to([pat[0] - pw / 4 + (pw / 2) * i,
                        pat[1] - ph / 2 - P(0.28, 0.22), 0])
            self.play(FadeIn(lb), run_time=0.4)

        base = P([0, -1.60, 0], [0, -1.32, 0])
        pair = [("0.19%", INK), ("16.8%", ACCT)]
        for i, (v, colr) in enumerate(pair):
            # SIDE BY SIDE in both aspects. Stacked, the portrait caption
            # ended up below its own closing line.
            x = base[0] + P(-2.55, -0.88) + P(5.10, 1.76) * i
            a = _fit(_t(v, size=P(50, 32), color=colr, weight="BOLD"),
                     P(3.0, 1.66), [x, base[1], 0])
            self.play(FadeIn(a, shift=UP * 0.10), run_time=0.5)
        lab = _fit(_t("of the labelled set is the rare class, after 240 spectra",
                      size=P(21, 14), color=SOFT), P(9.0, 3.36))
        lab.move_to([base[0], base[1] - P(0.56, 0.52), 0])
        self.play(FadeIn(lab), run_time=0.4)

        closer(self, "it kept confirming what it knew", size=P(29, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — SPEND IT ON DOUBT
# ═════════════════════════════════════════════════════════════════════════════
class B08_SpendItOnDoubt(Paced):
    BEAT, RT, HOLD = "B08", 1.550, 0.261

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Spend it where the model is least sure",
               cite="Fink's deployed rule takes the alerts closest to a 50/50 call; picks computed here")

        # boundary.png is 1720x700 -> ratio 0.407. pw 9.4 -> ph 3.83.
        pw = P(7.60, 3.44)
        ph = _plate_h("boundary.png", pw)
        pat = [0, P(2.35 - ph / 2, 1.44), 0]
        plate = _plate("boundary.png", pw, pat, frame=False)
        self.play(FadeIn(plate), run_time=0.8)

        for i, nm in enumerate(["season one", "season eight"]):
            lb = _fit(_t(nm, size=P(22, 15), color=SOFT), pw / 2 - P(0.40, 0.14))
            lb.move_to([pat[0] - pw / 4 + (pw / 2) * i,
                        pat[1] - ph / 2 - P(0.28, 0.22), 0])
            self.play(FadeIn(lb), run_time=0.4)

        # Short enough to sit in one clear band. The full sentence was 6.3
        # units wide and landed on both the panel labels above it and the
        # chips below.
        key = _fit(_t("ink = already labelled  ·  terracotta = the next spectra",
                      size=P(18, 13), color=SOFT), P(7.2, 3.38))
        key.move_to([pat[0], pat[1] - ph / 2 - P(0.64, 0.46), 0])
        self.play(FadeIn(key), run_time=0.4)

        # ONE ROW of chips rather than figure-over-subline: stacked, the
        # sublines landed exactly on the panel labels above them.
        base = P([0, -1.92, 0], [0, -1.30, 0])
        for i, txt in enumerate(("3.6× the base rate",
                                 "8.4× eight seasons later")):
            x = base[0] + P(-2.70 + 5.40 * i, 0.0)
            y = base[1] - P(0.0, 0.62 * i)
            c = _chip(txt, size=P(22, 16), max_w=P(5.0, 3.30))
            c.move_to([x, y, 0])
            self.play(FadeIn(c, shift=UP * 0.08), run_time=0.5)

        closer(self, "doubt goes where the labels are not", size=P(28, 21))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — THE RECEIPT
# ═════════════════════════════════════════════════════════════════════════════
class B09_TheReceipt(Paced):
    BEAT, RT, HOLD = "B09", 1.522, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Deployed, not simulated",
               cite="Fink real-time active learning on ZTF, follow-up at the ANU 2.3 m (arXiv:2502.19555)")

        cw, ch = P(6.20, 3.34), P(2.60, 2.10)
        cc = P([-2.95, 1.00, 0], [0, 1.40, 0])
        self.play(Create(_card(cw, ch, cc)), run_time=0.65)
        head = _fit(_t("DEPLOYED, NOT SIMULATED", size=P(23, 18), color=ACCT,
                       weight="BOLD"), cw - 0.7, [cc[0], cc[1] + ch * 0.33, 0])
        self.play(FadeIn(head), run_time=0.45)
        self.play(Create(Line([cc[0] - cw * 0.40, cc[1] + ch * 0.19, 0],
                              [cc[0] + cw * 0.40, cc[1] + ch * 0.19, 0],
                              color=RULE, stroke_width=2)), run_time=0.3)
        r1 = _fit(_t("92 spectra, not 127", size=P(27, 21)), cw - 1.0,
                  [cc[0], cc[1] - ch * 0.04, 0])
        self.play(FadeIn(r1), run_time=0.45)
        r1b = _fit(_t("for the same performance", size=P(20, 16), color=SOFT),
                   cw - 1.0, [cc[0], cc[1] - ch * 0.26, 0])
        self.play(FadeIn(r1b), run_time=0.35)

        chip = _chip("25% fewer", size=P(24, 18), max_w=P(3.0, 2.4))
        chip.move_to([cc[0], cc[1] - ch / 2 - P(0.34, 0.30), 0])
        self.play(FadeIn(chip, shift=UP * 0.08), run_time=0.5)

        col_at = P([3.20, 1.40, 0], [0, -0.60, 0])
        col_w = P(4.60, 3.36)
        found = _fit(_t("and it turned up", size=P(22, 17), color=SOFT), col_w,
                     [col_at[0], col_at[1], 0])
        self.play(FadeIn(found), run_time=0.4)
        for i, nm in enumerate(("microlensing events", "flaring stars")):
            a = _fit(_t(nm, size=P(27, 21), color=ACCT, weight="BOLD"), col_w,
                     [col_at[0], col_at[1] - P(0.60, 0.46) * (i + 1), 0])
            self.play(FadeIn(a, shift=UP * 0.08), run_time=0.45)
        gone = _fit(_t("never in anyone's training set", size=P(21, 16)), col_w)
        gone.move_to([col_at[0], col_at[1] - P(2.00, 1.38), 0])
        self.play(FadeIn(gone), run_time=0.4)
        self.play(Create(_strike(gone, pad=0.12)), run_time=0.45)

        closer(self, "it found things nobody asked for", size=P(29, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE DESIGN TELL
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    BEAT, RT, HOLD = "B10", 1.479, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The design tell",
               cite="computed in this reel: exploration fraction against the chance of ever finding the rare class")

        cw, ch = P(5.60, 3.30), P(2.50, 2.05)
        cc = P([-3.20, 1.05, 0], [0, 1.44, 0])
        self.play(Create(_card(cw, ch, cc)), run_time=0.65)
        head = _fit(_t("WHAT THE ACCURACY NUMBER HIDES", size=P(21, 17),
                       color=ACCT, weight="BOLD"), cw - 0.6,
                    [cc[0], cc[1] + ch * 0.33, 0])
        self.play(FadeIn(head), run_time=0.45)
        self.play(Create(Line([cc[0] - cw * 0.40, cc[1] + ch * 0.19, 0],
                              [cc[0] + cw * 0.40, cc[1] + ch * 0.19, 0],
                              color=RULE, stroke_width=2)), run_time=0.3)

        r1 = _fit(_t("it is getting better", size=P(26, 20)), cw - 0.9,
                  [cc[0], cc[1] - ch * 0.02, 0])
        self.play(FadeIn(r1), run_time=0.45)
        self.play(Create(_strike(r1, pad=0.12)), run_time=0.45)
        r2 = _fit(_t("it is getting narrower", size=P(26, 20), color=ACCT,
                     weight="BOLD"), cw - 0.9, [cc[0], cc[1] - ch * 0.30, 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.45)
        box = Rectangle(width=min(float(r2.width) + 0.44, cw - 0.6),
                        height=float(r2.height) + 0.34, color=ACC,
                        stroke_width=P(4, 3), fill_opacity=0).move_to(r2)
        self.play(Create(box), run_time=0.45)

        # budget.png is 1560x780 -> ratio 0.500
        pw = P(4.90, 3.30)
        ph = _plate_h("budget.png", pw)
        pat = P([3.10, 1.08, 0], [0, -0.72, 0])
        plate = _plate("budget.png", pw, pat, frame=True)
        self.play(FadeIn(plate), run_time=0.7)
        # LANDSCAPE ONLY: in portrait it brushed the counter beneath it, and
        # the closing line already says what the axis is.
        if not PORTRAIT:
            ax = _fit(_t("share of the budget spent on doubt  →",
                         size=19, color=SOFT), 5.0)
            ax.move_to([pat[0], pat[1] - ph / 2 - 0.28, 0])
            self.play(FadeIn(ax), run_time=0.35)

        n_at = P([0, -1.68, 0], [0, -1.88, 0])
        big = _fit(_t("35%  →  92%", size=P(40, 30), color=ACCT,
                      weight="BOLD"), P(5.4, 3.36))
        big.move_to(n_at)
        self.play(FadeIn(big, shift=UP * 0.08), run_time=0.5)

        # LANDSCAPE ONLY — portrait has no room, and the closer carries it.
        if not PORTRAIT:
            sub = _fit(_t("chance of ever finding the rare class, for 18% of "
                          "the confirmations", size=20, color=SOFT), 9.4)
            sub.move_to([0, -2.14, 0])
            self.play(FadeIn(sub), run_time=0.4)

        closer(self, "one night in ten", size=P(30, 23))
        self.hold_to_beat()
