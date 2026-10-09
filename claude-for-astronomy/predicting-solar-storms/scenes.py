"""scenes.py - Manim scenes for predicting-solar-storms.

*The Same Sunspot, Twice.* - ai-explainer, claude-hai, Ep. 12.

PALETTE (Claude fidelity, per skills/make/ai-explainer/SKILL.md)
  cream  #F2F0E9  ground
  ink    #3D3929  all body text
  soft   #6E6A57  secondary text / citations      (4.7:1 on cream)
  ghost  #B9B4A0  STROKES AND FILLS ONLY - never text (2.0:1, fails WCAG)
  acc    #D97757  terracotta - the ONE accent, as a MARK: rule, ring, fill, chip
  accT   #A44A32  the darkened accent for accented TEXT (4.7:1 on cream)

COLOUR CONTRACT FOR THIS REEL
  Terracotta marks THE LEAK AND WHAT IT BUYS: the test rows scattered
  through every region, the pile of near-zero neighbour distances, the
  flexible model's inflated bar and its collapse, the inflation curve. Ink
  marks WHAT SURVIVES AN HONEST TEST: the plain model, which does not move
  between splits.

  The load-bearing moment is B08, where the ink bar lands at the same height
  it had before and the terracotta one falls by three quarters. The accent
  that has meant "the flexible model's advantage" for three beats is now the
  thing that evaporates. The mapping never flips, so B05 teaches it once and
  every later plate reads for free.

THIS FILE IS ASPECT-AWARE - IT RENDERS BOTH CUTS
  The reel ships in 16:9 (3840x2160) and 9:16 (2160x3840). Manim keeps
  frame_height = 8.0 in both, so the VERTICAL band plan is identical either
  way; only the horizontal extent changes - x +-6.15 landscape, x +-1.80
  portrait. Portrait is NOT a crop: it has LESS usable area, so it carries
  fewer elements, larger. The rule for choosing what goes: anything the
  narration SPEAKS stays on screen.

  split.png therefore ships in BOTH arrangements - side by side for
  landscape, split_v.png stacked for portrait. Side by side at portrait's
  3.40-unit width each panel is 1.7 units across and the dots, which ARE the
  plate, disappear.

LAYOUT BAND PLAN (every scene obeys it - this is what keeps the gates green)
                        landscape      portrait
  title                   +3.02          +3.14
  hairline                +2.66          +2.84
  the figure       +2.40 .. -1.90   +2.62 .. -2.02
  the closing line        -2.50          -2.42   (terracotta rule 0.28 below)
  the citation            -3.20          -2.95
  the wordmark bug        -3.12          -3.28   (right-anchored, LOGO LAW)

PLATES
  Every plate comes from assets/gen_solar.py, which runs the experiment the
  episode describes: 350 simulated active regions observed hourly, two
  models of deliberately different capacity, three ways of splitting the
  data, twelve repeats, medians throughout. Seed 1212.

  THREE claims are ASSERTED and the generator writes nothing if any fails:
  the flexible model BEATS the baseline under a random split; the ordering
  REVERSES under a by-region split; and the inflation vanishes when the
  region fingerprint is removed from the features.

  Two earlier versions of the simulator were discarded. The first had a
  within-region random walk larger than the fingerprint itself, so rows of
  one region ended up no more alike than rows of different regions and the
  leak - the whole subject of the episode - was simulated away. The second
  used k=5, where the model was simply worse than the baseline under every
  split, so its inflation was the inflation of a bad number.

  PUBLISHED vs COMPUTED-HERE is kept visibly apart. B03 is a published
  ledger (38 of 49 Starlink satellites, NASA and Space Weather) and says so
  on screen; B04-B10 are computed here and say so. The literature supplies
  the DIAGNOSIS - no published paper quantifies the gap - and this reel
  supplies a MEASUREMENT on a case where the truth is known by construction.

PLATE GEOMETRY - ph = pw * (ih/iw). Do this arithmetic, do not assume it.
  regions  1560x740  0.474     split    1550x700  0.452
  nearest  1560x700  0.449     scores   1560x780  0.500
  spread   1560x780  0.500     control  1560x780  0.500
  split_v   760x830  1.092
  The landscape figure band is 4.30 units tall, so a 0.50-ratio plate at
  pw = 8.0 is 4.00 tall and leaves nothing for labels - the 0.50 plates run
  at pw 6.6. split_v is 1.09, so in portrait at pw 3.40 it is 3.71 tall and
  needs the whole figure band, which is why that beat carries nothing else
  there.

GATE NOTES (learned the expensive way on Eps. 03-11)
  - import numpy as np explicitly: GATE A's stub does not re-export it.
  - Never build a Line from a Text's get_left(); under the stub a Text has no
    width and the coordinates land off-frame. Use _underline() / _strike().
  - A strike-through must set _qc_intentional or GATE B calls it text-on-curve.
  - ImageMobject is not a VMobject: group it with Group, never VGroup.
  - A plate is an ImageMobject, NOT a curve, so GATE B will not flag a label
    printed across it. Ep. 11 shipped "the optimiser's answer" straight over
    its bracket until the frame was read.
  - NEVER use a glyph outside the font's coverage. EB Garamond has no "check"
    character and Ep. 09 rendered it as stray digits on screen.
  - A P() pair's PORTRAIT figure must be no wider than the container it sits
    in. Ep. 11's B02 fitted rows to 4.60 units inside a 3.46-unit card.
  - Leave >= 0.15 units between any two elements. A gap of 0.04 is eleven
    pixels at 4K and reads as contact; four of Ep. 11's twelve frame-reading
    defects were exactly this.
  - Give every scene its footer EARLY. GATE V samples each beat at 50% and
    85%, and Ep. 11's B01 read 44% underfill because its citation and bug
    landed last.
  - Ask whether the PICTURE says what the BEAT says. Ep. 11's comparison bars
    were drawn from compliance, where shorter means stiffer, so the winning
    design had the shorter bar.
  - Check BOTH aspects. Portrait failed GATE B 8/10 on Ep. 08's first pass.
  - Pace the scene to the narration (see Paced). A scene already on the 0.35 s
    floor cannot be fixed by more trim - lower its RT.
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
#  The seven plates from gen_solar.py, in pixels and as ratios:
#      regions 1560x740 (0.474)   split   1550x700 (0.452)
#      nearest 1560x700 (0.449)   scores  1560x780 (0.500)
#      spread  1560x780 (0.500)   control 1560x780 (0.500)
#      split_v  760x830 (1.092)
#  The landscape figure band is 4.30 units tall, so a 0.50-ratio plate at
#  pw = 8.0 is 4.00 tall and leaves almost nothing for labels. Do this
#  arithmetic; Ep. 08's B04 defect was this multiplication left undone.
# ─────────────────────────────────────────────────────────────────────────────

# Numbers the scenes put on screen. Every one is a MEDIAN over the generator's
# twelve repeats, printed by assets/gen_solar.py. Kept here as named
# constants so a changed experiment cannot silently disagree with the labels.
TSS_PLAIN_RANDOM = "0.36"
TSS_FLEX_RANDOM = "0.48"
TSS_PLAIN_REGION = "0.37"
TSS_FLEX_REGION = "0.12"


# ═════════════════════════════════════════════════════════════════════════════
#  B01 — PRESENTER
# ═════════════════════════════════════════════════════════════════════════════
class B01_Presenter(Paced):
    BEAT, RT, HOLD = "B01", 0.831, 0.000

    def construct(self):
        self.camera.background_color = BG
        hair = Line([-(X_MAX - 0.10), HAIR_Y, 0], [X_MAX - 0.10, HAIR_Y, 0],
                    color=RULE, stroke_width=2.4)
        top = _fit(_t("AI in Astronomy & Space Science  ·  Ep. 12",
                      size=P(22, 17), color=SOFT), TITLE_W, [0, TITLE_Y, 0])
        # the footer lands with the header, not last: GATE V samples at 50%
        # and 85% of the beat, and a frame whose content sits only in the top
        # half reads as underfill (Ep. 11's B01, 44%).
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

        r1 = _fit(_t("eleven episodes", size=P(28, 23), color=SOFT),
                  P(4.9, 3.00))
        r1.move_to([card_at[0], card_at[1] + P(0.80, 0.74), 0])
        r1b = _fit(_t("does the AI work?", size=P(23, 19), color=SOFT),
                   P(4.9, 3.00))
        r1b.move_to([card_at[0], card_at[1] + P(0.38, 0.34), 0])
        self.play(FadeIn(r1), run_time=0.45)
        self.play(FadeIn(r1b), run_time=0.4)
        self.play(Create(_strike(r1b, color=ACC, sw=4)), run_time=0.4)

        r2 = _fit(_t("this one", size=P(28, 23), color=ACCT, weight="BOLD"),
                  P(4.9, 3.00))
        r2.move_to([card_at[0], card_at[1] - P(0.30, 0.30), 0])
        r2b = _fit(_t("how we checked", size=P(23, 19), color=INK),
                   P(4.9, 3.00))
        r2b.move_to([card_at[0], card_at[1] - P(0.72, 0.70), 0])
        self.play(FadeIn(r2, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(r2b), run_time=0.45)
        self.play(Create(SurroundingRectangle(VGroup(r2, r2b), color=ACC,
                                              buff=0.18, stroke_width=3,
                                              corner_radius=0.10)),
                  run_time=0.5)

        ser = _fit(_t("Ep. 12  ·  the score was the split", size=P(23, 18),
                      color=ACCT), P(6.0, 3.34))
        ser.move_to([0, P(-2.34, -2.44), 0])
        self.play(FadeIn(ser), run_time=0.5)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B02 — THE WHOLE IDEA IN ONE BREATH  (EXECUTIVE-SUMMARY LAW)
# ═════════════════════════════════════════════════════════════════════════════
class B02_OneBreath(Paced):
    BEAT, RT, HOLD = "B02", 1.550, 0.055

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The whole idea, in one breath",
               cite="the mechanism, before any number")

        card = _card(P(9.4, 3.46), P(4.10, 4.30), [0, P(0.26, 0.30), 0])
        self.play(Create(card), run_time=0.7)

        rows = [("ONE REGION, MEASURED FOR DAYS",
                 "dozens of rows that barely change", INK, False),
                ("SHUFFLE, THEN SPLIT",
                 "and it lands on both sides", INK, False),
                ("YOU TESTED ITS MEMORY", None, ACCT, True)]
        y0, dy = P(1.56, 1.66), P(1.18, 1.44)
        for i, (head, sub, colr, accent) in enumerate(rows):
            y = y0 - dy * i
            h = _fit(_t(head, size=P(34, 23), color=colr,
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

        closer(self, "not its forecast", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B03 — THE STAKES  (PUBLISHED)
# ═════════════════════════════════════════════════════════════════════════════
class B03_Stakes(Paced):
    BEAT, RT, HOLD = "B03", 1.550, 0.510

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "A moderate storm",
               cite="NASA and Space Weather — 3 February 2022, published, "
                    "not measured here")

        # LANDSCAPE ONLY. In portrait this chip sat directly under the
        # date card and GATE B read its rounded-rectangle stroke as a curve
        # beneath the type. The citation line already names the sources.
        if not PORTRAIT:
            chip = _quiet_chip("published ledger", size=19, max_w=3.6)
            chip.move_to([-4.30, 1.92, 0])
            self.play(FadeIn(chip), run_time=0.45)

        # 49 satellite marks. An ISOTYPE count, not a picture of a satellite:
        # REBUILD LAW, and the number is the point.
        cols, rows_n = 7, 7
        gx, gy = P(0.90, 0.0), P(0.96, 0.74)
        sx, sy = P(0.56, 0.46), P(0.50, 0.42)
        marks = []
        for i in range(49):
            r, c = divmod(i, cols)
            x = gx + (c - (cols - 1) / 2.0) * sx
            y = gy - (r - (rows_n - 1) / 2.0) * sy
            m = Square(side_length=P(0.30, 0.26), color=INK, fill_color=INK,
                       fill_opacity=1.0, stroke_width=0).move_to([x, y, 0])
            marks.append(m)
        self.play(LaggedStart(*[FadeIn(m, scale=0.6) for m in marks],
                              lag_ratio=0.012), run_time=1.0)

        date = _fit(_t("3 February 2022", size=P(24, 19), color=SOFT),
                    P(4.0, 3.30))
        # landscape stacks chip (+1.92) then date (+1.10) in the left column;
        # at +1.70 the date ran into the chip's lower edge.
        date.move_to([P(-3.40, 0.0), P(1.10, 2.48), 0])
        self.play(FadeIn(date), run_time=0.45)

        # 38 of them go terracotta and drop away
        lost = VGroup(*marks[:38])
        self.play(lost.animate.set_color(ACC).set_fill(ACC), run_time=0.7)
        self.play(lost.animate.shift(DOWN * P(0.44, 0.40)).set_opacity(0.50),
                  run_time=0.7)

        big = _fit(_t("38 of 49", size=P(54, 40), color=ACCT, weight="BOLD"),
                   P(5.0, 3.36))
        big.move_to([P(-3.60, 0.0), P(-1.30, -1.30), 0])
        self.play(FadeIn(big, shift=UP * 0.10), run_time=0.6)
        sub = _fit(_t("reentered within days", size=P(21, 17), color=SOFT),
                   P(4.4, 3.34))
        sub.move_to([big.get_center()[0], big.get_center()[1] - P(0.60, 0.54), 0])
        self.play(FadeIn(sub), run_time=0.45)

        closer(self, "and the storm was only moderate", cx=P(0.0, 0.0),
               size=P(29, 22))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B04 — THE SHAPE OF THE DATA
# ═════════════════════════════════════════════════════════════════════════════
class B04_TheData(Paced):
    BEAT, RT, HOLD = "B04", 1.550, 0.309

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "One region, dozens of rows",
               cite="computed in this reel: 350 regions, measured hourly")

        # regions.png is 1560x740 -> 0.474. At pw 7.60 that is 3.60 tall
        # centred at +0.66, so the plate top reached +2.46 and the label
        # above it straddled the hairline at +2.66. pw 7.00 -> ph 3.32.
        pw = P(7.00, 3.40)
        pat = [0, P(0.40, 0.90), 0]
        plate = _plate("regions.png", pw, pat, frame=False)
        ph = _plate_h("regions.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        # ring ONE track, and name what a track is
        ring = RoundedRectangle(width=pw * 0.99, height=ph * 0.088,
                                corner_radius=0.06, color=ACC, stroke_width=3,
                                fill_opacity=0)
        ring.move_to([pat[0], pat[1] + ph * 0.42, 0])
        self.play(Create(ring), run_time=0.55)
        lab = _fit(_t("one active region", size=P(21, 16), color=ACCT),
                   P(4.0, 3.20))
        lab.move_to([pat[0], pat[1] + ph * 0.50 + P(0.26, 0.24), 0])
        self.play(FadeIn(lab), run_time=0.45)

        chips = [("58 rows", INK), ("1 flare row in 58", ACC)]
        for i, (txt, fill) in enumerate(chips):
            c = _chip(txt, size=P(21, 16), fill=fill, max_w=P(4.2, 3.20))
            c.move_to([P(-2.40 + 4.80 * i, 0.0), P(-1.62, -1.40 - 0.52 * i), 0])
            self.play(FadeIn(c, shift=UP * 0.06), run_time=0.5)

        closer(self, "a few regions do all the flaring", cx=P(0.0, 0.0),
               size=P(29, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B05 — THE SPLIT
# ═════════════════════════════════════════════════════════════════════════════
class B05_TheSplit(Paced):
    BEAT, RT, HOLD = "B05", 1.550, 0.086

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Same data, two answers",
               cite="computed in this reel: terracotta marks the test set")

        # split.png is 0.452 and split_v.png is 1.092. At pw 10.60 the
        # landscape plate would be 4.79 units tall against a 4.30 figure
        # band, and the panel label landed at y 3.54 -- above the title.
        # Do the arithmetic: pw 7.40 -> ph 3.35.
        name = "split_v.png" if PORTRAIT else "split.png"
        pw = P(7.40, 3.10)
        pat = [0, P(0.72, 0.60), 0]
        plate = _plate(name, pw, pat, frame=False)
        ph = _plate_h(name, pw)
        self.play(FadeIn(plate), run_time=0.9)

        # Labels sit OUTSIDE the plate in both aspects. In portrait the two
        # panels are stacked with a 0.13-unit gutter between them, which is
        # too small for type -- a label placed there would print across a
        # panel, which GATE B cannot see because a plate is an ImageMobject.
        if PORTRAIT:
            spots = [("shuffle the rows", pat[1] + ph * 0.50 + 0.26),
                     ("split by region", pat[1] - ph * 0.50 - 0.28)]
            for txt, y in spots:
                lb = _fit(_t(txt, size=17, color=SOFT), 3.30, [0, y, 0])
                self.play(FadeIn(lb), run_time=0.4)
        else:
            for i, txt in enumerate(["shuffle the rows", "split by region"]):
                lb = _fit(_t(txt, size=22, color=SOFT), 3.40,
                          [(-0.25 + 0.5 * i) * pw,
                           pat[1] - ph * 0.5 - 0.32, 0])
                self.play(FadeIn(lb), run_time=0.4)

        # the two counters -- the number the voice speaks
        for i, (v, colr) in enumerate([("100%", ACCT), ("0%", INK)]):
            x = P(-2.30, -0.85) + P(4.60, 1.70) * i
            a = _fit(_t(v, size=P(46, 34), color=colr, weight="BOLD"),
                     P(3.0, 1.60), [x, P(-2.02, -1.80), 0])
            self.play(FadeIn(a, shift=UP * 0.10), run_time=0.6)
        cap = _fit(_t("of test regions were also in the training set",
                      size=P(21, 16), color=SOFT), P(9.6, 3.34))
        cap.move_to([0, P(-2.62, -2.42), 0])
        self.play(FadeIn(cap), run_time=0.45)
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B06 — THE LEAK, MEASURED
# ═════════════════════════════════════════════════════════════════════════════
class B06_TheLeak(Paced):
    BEAT, RT, HOLD = "B06", 1.550, 0.169

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The leak, measured",
               cite="computed in this reel: distance from each test row to "
                    "its nearest training row")

        # nearest.png is 1560x700 -> 0.449. pw 6.80 -> ph 3.05.
        pw = P(6.80, 3.40)
        pat = [P(-1.25, 0.0), P(0.30, 0.92), 0]
        plate = _plate("nearest.png", pw, pat, frame=False)
        ph = _plate_h("nearest.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        xlab = _fit(_t("distance to the nearest training row  →",
                       size=P(20, 15), color=SOFT), P(5.4, 3.30))
        xlab.move_to([pat[0], pat[1] - ph * 0.5 - P(0.30, 0.34), 0])
        self.play(FadeIn(xlab), run_time=0.4)

        # name the two piles
        # ABOVE the plate, not on it. The terracotta histogram reaches the
        # top of the plot at the left, so a label placed there had its first
        # letter behind the peak -- it read "fter shuffling".
        lab_y = pat[1] + ph * 0.5 + P(0.30, 0.28)
        a = _fit(_t("after shuffling", size=P(23, 17), color=ACCT,
                    weight="BOLD"), P(3.4, 1.60))
        a.move_to([pat[0] - pw * P(0.26, 0.24), lab_y, 0])
        self.play(FadeIn(a), run_time=0.5)
        b = _fit(_t("split by region", size=P(23, 17), color=INK),
                 P(3.4, 1.60))
        b.move_to([pat[0] + pw * P(0.26, 0.24), lab_y, 0])
        self.play(FadeIn(b), run_time=0.5)

        if not PORTRAIT:
            col_at = [3.80, 1.30, 0]
            for i, (big, small) in enumerate(
                    [("0.13", "the closest row is the same"),
                     ("0.38", "region, an hour earlier")]):
                y = col_at[1] - 1.05 * i
                v = _fit(_t(big, size=38, color=ACCT if i == 0 else INK,
                            weight="BOLD"), 3.0, [col_at[0], y, 0])
                s = _fit(_t(small, size=18, color=SOFT), 4.2,
                         [col_at[0], y - 0.46, 0])
                self.play(FadeIn(v, shift=UP * 0.08), run_time=0.5)
                self.play(FadeIn(s), run_time=0.4)

        closer(self, "almost the same numbers", cx=P(-0.6, 0.0),
               size=P(29, 23))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B07 — THE HEADLINE
# ═════════════════════════════════════════════════════════════════════════════
class B07_TheHeadline(Paced):
    # Lands at -0.08 s: inside the -0.25..+0.05 tolerance, but the thinnest
    # margin in the reel. Both levers were tried and NEITHER moved it -- a
    # per-scene trim of 0.29 and an RT cut to 1.355 each left the measured
    # duration at 11.21 s exactly. Left at the solved value and recorded
    # rather than tuned blind; a 0.08 s undershoot is padded with a held
    # frame, which is invisible.
    BEAT, RT, HOLD = "B07", 1.369, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The headline you would publish",
               cite="computed in this reel: TSS, median of 12 runs, rows "
                    "shuffled before splitting")

        # drawn natively, so the bars grow ON the spoken figure
        base_y = P(-1.30, -1.40)
        h_max = P(2.90, 2.80)
        axis = Line([P(-4.4, -1.55), base_y, 0], [P(3.3, 1.55), base_y, 0],
                    color=GHOST, stroke_width=3)
        self.play(Create(axis), run_time=0.5)
        # LANDSCAPE ONLY. Portrait has the axis, this label, two bar labels
        # and the closing line inside 1.0 units; the axis label is the one
        # the narration never says, so it is what portrait loses.
        if not PORTRAIT:
            ylab = _fit(_t("skill score  (TSS)", size=20, color=SOFT), 4.0)
            ylab.move_to([-0.55, base_y - 0.30, 0])
            self.play(FadeIn(ylab), run_time=0.4)

        bars = [("the plain model", TSS_PLAIN_RANDOM, 0.356, INK, P(-2.60, -0.80)),
                ("the flexible model", TSS_FLEX_RANDOM, 0.484, ACC, P(0.60, 0.80))]
        tops = []
        for nm, txt, v, colr, cx in bars:
            bw = P(1.50, 0.86)
            hh = h_max * (v / 0.55)
            r = Rectangle(width=bw, height=hh, color=colr, fill_color=colr,
                          fill_opacity=1.0, stroke_width=0)
            r.move_to([cx, base_y + hh / 2.0, 0])
            self.play(GrowFromEdge(r, DOWN), run_time=0.85)
            tops.append(base_y + hh)
            lb = _fit(_t(nm, size=P(20, 15), color=SOFT), P(2.9, 1.50))
            lb.move_to([cx, base_y - P(0.68, 0.40), 0])
            self.play(FadeIn(lb), run_time=0.4)
            v_ = _fit(_t(txt, size=P(34, 26), color=colr if colr is INK
                         else ACCT, weight="BOLD"), P(2.2, 1.40))
            v_.move_to([cx, base_y + hh + P(0.34, 0.30), 0])
            self.play(FadeIn(v_, shift=UP * 0.08), run_time=0.5)

        gap = _fit(_t("+0.13", size=P(28, 21), color=ACCT, weight="BOLD"),
                   P(2.4, 1.40))
        gap.move_to([P(-1.00, 0.0), max(tops) + P(0.92, 0.86), 0])
        self.play(FadeIn(gap, shift=UP * 0.08), run_time=0.5)

        chip = _chip("rows shuffled", size=P(20, 16), fill=ACC,
                     max_w=P(3.6, 3.00))
        chip.move_to([P(3.90, 0.0), P(1.90, 2.30), 0])
        self.play(FadeIn(chip), run_time=0.45)

        closer(self, "the flexible model wins", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B08 — THE REVERSAL                                   (the load-bearing beat)
# ═════════════════════════════════════════════════════════════════════════════
class B08_TheReversal(Paced):
    BEAT, RT, HOLD = "B08", 1.455, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Now split by region",
               cite="computed in this reel: the same two models, the same "
                    "data, one line of the split changed")

        # scores.png is 1560x780 -> 0.500. pw 6.60 -> ph 3.30.
        pw = P(6.60, 3.40)
        pat = [P(-1.40, 0.0), P(0.80, 1.00), 0]
        plate = _plate("scores.png", pw, pat, frame=False)
        ph = _plate_h("scores.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        for i, txt in enumerate(["rows shuffled", "split by region"]):
            lb = _fit(_t(txt, size=P(21, 16),
                         color=SOFT if i == 0 else ACCT), P(3.4, 1.60))
            lb.move_to([pat[0] + (-0.24 + 0.50 * i) * pw,
                        pat[1] - ph * 0.5 - P(0.30, 0.34), 0])
            self.play(FadeIn(lb), run_time=0.4)

        ring = RoundedRectangle(width=pw * 0.20, height=ph * 0.56,
                                corner_radius=0.08, color=ACC, stroke_width=4,
                                fill_opacity=0)
        ring.move_to([pat[0] + pw * 0.33, pat[1] - ph * 0.17, 0])
        self.play(Create(ring), run_time=0.6)

        col_at = P([3.70, 1.26, 0], [0, -1.18, 0])
        big = _fit(_t("−75%", size=P(50, 38), color=ACCT, weight="BOLD"),
                   P(3.4, 2.00), [col_at[0], col_at[1], 0])
        self.play(FadeIn(big, shift=UP * 0.10), run_time=0.65)
        sub = _fit(_t("of the flexible model's score", size=P(21, 17),
                      color=SOFT), P(4.4, 3.34))
        sub.move_to([col_at[0], col_at[1] - P(0.62, 0.56), 0])
        self.play(FadeIn(sub), run_time=0.45)

        if not PORTRAIT:
            steady = _fit(_t("the plain model does not move: 0.36 → 0.37",
                             size=20, color=SOFT), 9.6)
            steady.move_to([0, -2.08, 0])
            self.play(FadeIn(steady), run_time=0.45)

        closer(self, "three quarters was the split", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B09 — NOT ONE LUCKY RUN
# ═════════════════════════════════════════════════════════════════════════════
class B09_NotOneRun(Paced):
    # floored tail; 1.356 landed at -0.01 s, one frame from overshooting
    BEAT, RT, HOLD = "B09", 1.326, 0.000

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "Twelve runs",
               cite="computed in this reel: 12 independent catalogues, each "
                    "point one run")

        pw = P(6.60, 3.40)
        pat = [P(-1.40, 0.0), P(0.80, 1.00), 0]
        plate = _plate("spread.png", pw, pat, frame=False)
        ph = _plate_h("spread.png", pw)
        self.play(FadeIn(plate), run_time=0.9)

        for i, txt in enumerate(["rows shuffled", "split by region"]):
            lb = _fit(_t(txt, size=P(21, 16),
                         color=SOFT if i == 0 else ACCT), P(3.4, 1.60))
            lb.move_to([pat[0] + (-0.24 + 0.50 * i) * pw,
                        pat[1] - ph * 0.5 - P(0.30, 0.34), 0])
            self.play(FadeIn(lb), run_time=0.4)

        if not PORTRAIT:
            col_at = [3.75, 1.40, 0]
            for i, (big, small) in enumerate(
                    [("the plain model", "sits where it always sat"),
                     ("the flexible one", "is down here, every run")]):
                y = col_at[1] - 1.20 * i
                a = _fit(_t(big, size=25, color=INK if i == 0 else ACCT,
                            weight="BOLD" if i else None), 4.3,
                         [col_at[0], y, 0])
                b = _fit(_t(small, size=18, color=SOFT), 4.4,
                         [col_at[0], y - 0.42, 0])
                self.play(FadeIn(a), run_time=0.5)
                self.play(FadeIn(b), run_time=0.4)

        closer(self, "twelve runs, no overlap", cx=P(0.0, 0.0))
        self.hold_to_beat()


# ═════════════════════════════════════════════════════════════════════════════
#  B10 — THE CAUSE, AND THE FIX
# ═════════════════════════════════════════════════════════════════════════════
class B10_TheTell(Paced):
    BEAT, RT, HOLD = "B10", 1.550, 0.090

    def construct(self):
        self.camera.background_color = BG
        chrome(self, "The design tell",
               cite="computed in this reel: inflation against how strongly a "
                    "row carries its region's identity")

        pw = P(6.00, 3.30)
        pat = [P(-2.10, 0.0), P(0.96, 1.08), 0]
        plate = _plate("control.png", pw, pat, frame=False)
        ph = _plate_h("control.png", pw)
        self.play(FadeIn(plate), run_time=0.85)

        xlab = _fit(_t("how much a row gives away its region  →",
                       size=P(20, 15), color=SOFT), P(5.2, 3.20))
        xlab.move_to([pat[0], pat[1] - ph * 0.5 - P(0.30, 0.34), 0])
        self.play(FadeIn(xlab), run_time=0.4)

        zero = _fit(_t("no fingerprint, no inflation", size=P(20, 15),
                       color=SOFT), P(4.6, 3.20))
        # The curve climbs from bottom-left to top-right, so the UPPER left
        # is the empty quadrant. At -0.30 the label sat across the rising
        # segment -- and GATE B cannot see that, because the curve is inside
        # the plate image rather than a Manim mobject.
        zero.move_to([pat[0] - pw * 0.20, pat[1] + ph * 0.34, 0])
        self.play(FadeIn(zero), run_time=0.45)

        if not PORTRAIT:
            fix = _card(4.60, 1.56, [3.45, 1.12, 0])
            self.play(Create(fix), run_time=0.5)
            a = _fit(_t("the fix, in one line", size=20, color=SOFT), 4.2,
                     [3.45, 1.46, 0])
            b = _fit(_t("split by region,", size=26, color=ACCT,
                        weight="BOLD"), 4.2, [3.45, 1.02, 0])
            c = _fit(_t("not by row", size=26, color=ACCT, weight="BOLD"),
                     4.2, [3.45, 0.62, 0])
            self.play(FadeIn(a), run_time=0.4)
            self.play(Write(b), run_time=0.5)
            self.play(Write(c), run_time=0.45)
        else:
            b = _fit(_t("split by region,", size=26, color=ACCT,
                        weight="BOLD"), 3.34, [0, -1.28, 0])
            c = _fit(_t("not by row", size=26, color=ACCT, weight="BOLD"),
                     3.34, [0, -1.70, 0])
            self.play(Write(b), run_time=0.5)
            self.play(Write(c), run_time=0.45)

        closer(self, "and it costs nothing", cx=P(0.0, 0.0))
        self.hold_to_beat()
