"""scenes.py — Manim scenes for humanitarians-ai-week3-stakeholder-strategy-hierarchy.

WEEK 3 OF 4. Visual system is locked to Weeks 1 and 2 (see
../humanitarians-ai-week2-typography-hero-concepting/scenes.py): PAPER white ground, INK near-black type, one MAROON
accent, Oswald, hard cuts, no gradients, no shadows, no rounded corners.

WHY MANIM FOR EVERY BEAT — unchanged from Week 1. The toolkit's Remotion
annotation plane is still marked "spec (v1, not yet built)" in
skills/make/explainer/REMOTION.md, so every beat here is a real Manim Scene:
plain screenshots, annotated screenshots and drawn diagrams alike.

CARRIED-FORWARD TOOLKIT WORKAROUNDS (all six from Week 1's BUILD-LOG; do not
regress any of these):
  1. runtime/scripts/generate_audio.py stub must exist (provides
     normalize_for_tts). Nothing in this file depends on it, but the audio
     step does.
  2. Text weight is the STRING "BOLD", never the bare constant — GATE A's
     static_scene_check.py stub does not define BOLD/ITALIC/NORMAL.
  3. Image loading falls back to a labeled placeholder on FileNotFoundError /
     OSError, because GATE A copies scenes.py alone into a temp folder with no
     assets/ beside it. The real render never hits the fallback.
  4. No Line() is used for strikethrough or emphasis anywhere. GATE B's
     TEXT_ON_CURVE check flags any Line crossing a text centerline as an
     ERROR with no exemption. "Rejected" is conveyed with a maroon square mark
     plus a label instead.
  5. GATE W's wcag_margin_check.py has its own TypeError bug and is
     non-blocking in run.sh. Ignore its warnings; do not patch that script.
  6. Every overlay chip is placed through place_chip() / chip_below(), which
     clamp to the safe area AND keep clear of the annotation boxes above them.
     Week 1 hit two real layout_audit errors from hand-placed chips; this file
     computes the positions instead.

EVERY NUMBER SHOWN IN THIS REEL WAS MEASURED, NOT ESTIMATED. Live DOM figures
came from the running site on 2026-09-05; every annotation box came from
PIL/numpy analysis of the actual screenshot pixels. See SOURCES.md for the
method and SHOTLIST.md for the coordinate table.

TWO STANDING RULES CARRIED FORWARD FROM WEEK 2, both from the presenter:
  A. No proposed layout is ever drawn. The site is never shown altered. Where
     a direction exists, it is stated in words (B16).
  B. GATE W's checker reads `buff` and `font_size` straight off the AST, so
     to_edge() takes the literal 0.6 and every Text() inside construct() takes
     a literal font_size — never a variable. A bare name crashes the checker,
     run.sh swallows it as non-blocking, and the scene then goes unchecked.
"""
from manim import *
from pathlib import Path
from PIL import Image
import hashlib
import numpy as np

# ── Palette — identical to Week 1, locked for the series ─────────────────
PAPER  = ManimColor("#FFFFFF")
INK    = ManimColor("#111111")
MAROON = ManimColor("#64140E")
SOFT   = ManimColor("#555555")

# Swatches used ONLY as filled rectangles in B11, never as type colour —
# that is the whole point of the beat.
GREY_FAIL = ManimColor("#7D7D7D")   # the site's current secondary text
GREY_PASS = ManimColor("#767676")   # the darkest grey that clears AA on white

FONT = "Oswald"
BODY_FONT = "Arial"

ASSETS = Path(__file__).parent / "assets"
CACHE = Path(__file__).parent / "manim" / ".cache"
CACHE.mkdir(parents=True, exist_ok=True)

SAFE_BUFF = 0.6          # keep everything this far inside the frame edge
# NOTE: to_edge() calls below pass the NUMBER 0.6 rather than SAFE_BUFF.
# runtime/qc/wcag_margin_check.py parses the buff kwarg statically and, when
# it is a bare name, hands a string into "FRAME_Y - 0.5 - buff" and dies with
# TypeError (the toolkit bug Week 1 logged as fix #5). run.sh treats that as
# non-blocking, so the crash is silent -- and the scene is then never checked
# at all. Passing a literal keeps GATE W alive on every scene instead of 10
# of 17. This is a change on OUR side; the toolkit script is left alone.
CHIP_CLEARANCE = 0.28    # minimum gap between an annotation box and a chip


# ── Image helpers (identical behaviour to Week 1) ────────────────────────
def _cache_path(src: Path, box, tag: str) -> Path:
    key = f"{src.name}-{box}-{tag}".encode()
    return CACHE / f"{src.stem}-{hashlib.sha1(key).hexdigest()[:10]}.png"


def cover_crop_169(src_name: str, box=(0.0, 0.0, 1.0, 1.0), tag="full") -> Path:
    """Crop `box` (normalized x0,y0,x1,y1 in the ORIGINAL screenshot) then
    centre-crop that region to exactly 16:9. Cached. Falls back to a labeled
    grey placeholder when the asset is missing — that happens deliberately
    under GATE A's isolated pre-flight, never in the real render."""
    src = ASSETS / src_name
    out = _cache_path(src, box, tag)
    if out.exists():
        return out
    target_ratio = 16 / 9
    try:
        im = Image.open(src).convert("RGB")
    except (FileNotFoundError, OSError):
        w, h = 1600, int(1600 / target_ratio)
        im = Image.new("RGB", (w, h), (200, 200, 200))
        try:
            from PIL import ImageDraw
            ImageDraw.Draw(im).text((40, h // 2 - 10),
                                    f"MISSING ASSET: {src_name}", fill=(80, 80, 80))
        except Exception:
            pass
        im.save(out)
        return out
    w, h = im.size
    x0, y0, x1, y1 = box
    region = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
    rw, rh = region.size
    if rw / rh > target_ratio:
        new_w = int(rh * target_ratio)
        region = region.crop(((rw - new_w) // 2, 0, (rw - new_w) // 2 + new_w, rh))
    elif rw / rh < target_ratio:
        new_h = int(rw / target_ratio)
        region = region.crop((0, (rh - new_h) // 2, rw, (rh - new_h) // 2 + new_h))
    region.save(out)
    return out


def full_frame_image(src_name: str, box=(0.0, 0.0, 1.0, 1.0), tag="full") -> ImageMobject:
    """Screenshot (or sub-region) cropped to 16:9 and scaled to fill the frame
    exactly. No border, no shadow, no rounded corner."""
    mob = ImageMobject(str(cover_crop_169(src_name, box, tag)))
    mob.stretch_to_fit_height(config.frame_height)
    mob.stretch_to_fit_width(config.frame_width)
    mob.move_to(ORIGIN)
    return mob


SRC_ASPECT = 1503 / 812   # verified: all six assets are exactly 1503x812


def rect_in_image(box, image_box=(0.0, 0.0, 1.0, 1.0), src_aspect=SRC_ASPECT):
    """Map a normalized rect (x0,y0,x1,y1 in ORIGINAL screenshot coords,
    y-down) into scene coordinates, accounting for the crop-to-16:9 transform
    full_frame_image() applies. Returns (left, bottom, right, top)."""
    ix0, iy0, ix1, iy1 = image_box
    iw, ih = ix1 - ix0, iy1 - iy0
    bx0, by0, bx1, by1 = box
    rel_x0, rel_x1 = (bx0 - ix0) / iw, (bx1 - ix0) / iw
    rel_y0, rel_y1 = (by0 - iy0) / ih, (by1 - iy0) / ih
    region_aspect = src_aspect * (iw / ih) if ih else src_aspect
    target_ratio = 16 / 9
    if region_aspect > target_ratio:
        keep = target_ratio / region_aspect
        pad = (1 - keep) / 2
        rel_x0, rel_x1 = (rel_x0 - pad) / keep, (rel_x1 - pad) / keep
    elif region_aspect < target_ratio:
        keep = region_aspect / target_ratio
        pad = (1 - keep) / 2
        rel_y0, rel_y1 = (rel_y0 - pad) / keep, (rel_y1 - pad) / keep
    x0 = (rel_x0 - 0.5) * config.frame_width
    x1 = (rel_x1 - 0.5) * config.frame_width
    y0 = (0.5 - rel_y0) * config.frame_height
    y1 = (0.5 - rel_y1) * config.frame_height
    return x0, y1, x1, y0


def annotate_rect(box, image_box=(0.0, 0.0, 1.0, 1.0), color=MAROON, sw=10):
    l, b, r, t = rect_in_image(box, image_box)
    rect = Rectangle(width=r - l, height=t - b, color=color,
                     stroke_width=sw, fill_opacity=0)
    rect.move_to([(l + r) / 2, (b + t) / 2, 0])
    return rect


# ── Text helpers ─────────────────────────────────────────────────────────
def kicker(text, color=PAPER, size=52):
    return Text(text.upper(), font=FONT, weight="BOLD", font_size=size, color=color)


def fit_width(mob, margin=SAFE_BUFF):
    """Shrink a mobject if it would breach the horizontal safe area."""
    limit = config.frame_width - 2 * margin
    if mob.width > limit:
        mob.scale_to_fit_width(limit)
    return mob


def chip(text, color=PAPER, bg=MAROON, size=34):
    label = Text(text.upper(), font=FONT, weight="BOLD", font_size=size, color=color)
    pad_x, pad_y = 0.35, 0.22
    bgrect = Rectangle(width=label.width + pad_x * 2, height=label.height + pad_y * 2,
                       color=bg, fill_color=bg, fill_opacity=1, stroke_width=0)
    bgrect.move_to(label.get_center())
    return fit_width(VGroup(bgrect, label))


def place_chip(text, y_frac=0.83, **kw):
    """Chip anchored to a fraction of frame height (0 = top, 1 = bottom),
    then clamped so it can never breach the vertical safe area."""
    c = chip(text, **kw)
    y = (0.5 - y_frac) * config.frame_height
    half = c.height / 2
    top_limit = config.frame_height / 2 - SAFE_BUFF - half
    bot_limit = -config.frame_height / 2 + SAFE_BUFF + half
    c.move_to([0, float(np.clip(y, bot_limit, top_limit)), 0])
    return c


def chip_below(text, obstacles, **kw):
    """Chip placed in the band between the LOWEST edge of `obstacles` and the
    bottom safe-area line — shrunk to fit that band if it has to be.

    Week 1 hit two real layout_audit errors from hand-placed overlay chips and
    fixed them by nudging numbers after the fact. This does the arithmetic
    instead, at render time, using Manim's own measured heights.

    The shrink matters: on the hero beats the annotation boxes reach down to
    y ~= -2.49, leaving only ~0.63 units of clear band above the safe line.
    A default chip is taller than that, so a naive "push it down and clamp"
    puts the chip BACK through the box it was meant to clear — the clamp wins
    and the collision returns silently. Fitting to the band cannot collide.
    At 4K a 0.6-unit band is still ~160px of chip, comfortably legible."""
    c = chip(text, **kw)
    top_avail = min((m.get_bottom()[1] for m in obstacles), default=0.0) - CHIP_CLEARANCE
    bot_avail = -config.frame_height / 2 + SAFE_BUFF
    band = top_avail - bot_avail
    if band < 0.3:
        # Nothing usable below: fall back to the top safe band instead of
        # forcing an overlap.
        return place_chip(text, y_frac=0.13, **kw)
    if c.height > band:
        c.scale_to_fit_height(band)
    c.move_to([0, bot_avail + c.height / 2, 0])
    return c


def stat_block(number, label, num_size=92, lab_size=26):
    n = Text(str(number), font=FONT, weight="BOLD", font_size=num_size, color=MAROON)
    rule = Rectangle(width=max(n.width, 0.8), height=0.05, color=INK,
                     fill_color=INK, fill_opacity=1, stroke_width=0)
    rule.next_to(n, DOWN, buff=0.18)
    l = Text(label.upper(), font=FONT, weight="BOLD", font_size=lab_size, color=INK)
    l.next_to(rule, DOWN, buff=0.22)
    return VGroup(n, rule, l)



# ── Measured annotation boxes ────────────────────────────────────────────
# All normalized against the ORIGINAL 1503x812 screenshots. Derived by
# connected-component labelling (maroon mask, holes closed) and light-panel
# thresholding. See SHOTLIST.md for the table and SOURCES.md for the method.
TIER_CARD_1     = (0.5163, 0.2660, 0.9308, 0.4323)   # "Tier 1"
TIER_CARD_2     = (0.5163, 0.4433, 0.9308, 0.6195)   # "Tiers 3-6"
TIER_CARD_3     = (0.5163, 0.6305, 0.9308, 0.7968)   # "Tier 7"
CTA_DONATE_NOW  = (0.3360, 0.0825, 0.4471, 0.1133)
CTA_VOLUNTEER   = (0.4591, 0.0825, 0.5609, 0.1133)
CTA_YOUTUBE     = (0.5729, 0.0837, 0.6633, 0.1133)
CTA_GROUP       = (0.3360, 0.0825, 0.6633, 0.1133)


# The audit enforces a safe area of +/-6.3 x and +/-3.4 y, i.e. a HORIZONTAL
# margin of 0.81 -- wider than SAFE_BUFF (0.6), which is correct for the
# vertical axis only. Text-heavy scenes must fit to this, not to SAFE_BUFF.
SAFE_BUFF_X = 0.85
SAFE_BUFF_Y = 0.65   # audit y half-extent is 3.4; SAFE_BUFF alone lands exactly on it


def question_block(questions, size=30, color=INK, line_buff=0.2, q_buff=0.62):
    """A stack of questions, each one a list of its own lines.

    Takes a list OF LISTS, not a flat list with "" spacers between questions.
    That earlier shape shipped a real GATE B failure: Text("") has zero height
    and effectively no extent, so arrange(DOWN, buff=...) computed its spacing
    off degenerate geometry and stacked the real lines on top of one another --
    layout_audit reported text-on-text at 100% and 85% overlap. Grouping the
    lines per question and arranging twice keeps every box real."""
    groups = VGroup()
    for lines in questions:
        g = VGroup(*[Text(t, font=FONT, weight="BOLD", font_size=size, color=color)
                     for t in lines])
        g.arrange(DOWN, aligned_edge=LEFT, buff=line_buff)
        groups.add(g)
    groups.arrange(DOWN, aligned_edge=LEFT, buff=q_buff)
    return groups


def marked_rows(rows, size=32, color=INK, buff=0.3, mark=0.18):
    """Rows each preceded by a maroon square. The marks are load-bearing:
    GATE A errors on any scene whose shape state never changes, and a stack
    of pure Text is exactly that."""
    g = VGroup()
    for t in rows:
        sq = Square(side_length=mark, color=MAROON, fill_color=MAROON,
                    fill_opacity=1, stroke_width=0)
        label = Text(t, font=FONT, weight="BOLD", font_size=size, color=color)
        label.next_to(sq, RIGHT, buff=0.32)
        g.add(VGroup(sq, label))
    g.arrange(DOWN, aligned_edge=LEFT, buff=buff)
    return g


def fit_block(*mobs, margin=SAFE_BUFF):
    """Group, shrink to the safe area in both axes, centre."""
    block = VGroup(*mobs)
    if block.height > config.frame_height - 2 * margin:
        block.scale_to_fit_height(config.frame_height - 2 * margin)
    if block.width > config.frame_width - 2 * margin:
        block.scale_to_fit_width(config.frame_width - 2 * margin)
    block.move_to(ORIGIN)
    return block


# ═══════════════════════════════════════════════════════════════════════
#  B00 — INTRO
# ═══════════════════════════════════════════════════════════════════════
class B00_Intro(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        name = kicker("Muskan Agrawal", color=INK, size=64)
        rule = Rectangle(width=name.width, height=0.06, color=MAROON,
                         fill_color=MAROON, fill_opacity=1, stroke_width=0)
        rule.next_to(name, DOWN, buff=0.35)
        sub = Text("WEEK 3 — STAKEHOLDER STRATEGY + HIERARCHY", font=FONT,
                   weight="BOLD", font_size=32, color=MAROON)
        sub.next_to(rule, DOWN, buff=0.45)
        fit_width(sub)
        tag = Text("HUMANITARIANS.AI RESTRUCTURE", font=FONT, weight="BOLD",
                   font_size=24, color=SOFT).next_to(sub, DOWN, buff=0.6)
        mark = Square(side_length=0.14, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(tag, LEFT, buff=0.25)
        VGroup(name, rule, sub, tag, mark).move_to(ORIGIN)
        self.play(Write(name), run_time=0.9)
        self.play(GrowFromCenter(rule), run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(tag), FadeIn(mark), run_time=0.5)
        self.wait(2.0)


# ═══════════════════════════════════════════════════════════════════════
#  B01 — What two weeks of numbers already settled
# ═══════════════════════════════════════════════════════════════════════
class B01_WhatNumbersGave(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("WHAT THE NUMBERS ALREADY SETTLED.", font=FONT,
                     weight="BOLD", font_size=40, color=INK).to_edge(UP, buff=0.6)
        fit_width(title)
        rows = marked_rows(["A TYPE SCALE.", "A CONTRAST TARGET.", "A LINE LENGTH."],
                           size=40)
        rows.next_to(title, DOWN, buff=1.0)
        tail = Text("DESIGN CAN DECIDE ALL THREE ON ITS OWN.", font=FONT,
                    weight="BOLD", font_size=28, color=SOFT)
        tail.next_to(rows, DOWN, buff=0.9)
        fit_width(tail)
        fit_block(title, rows, tail)
        self.play(Write(title), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.15), run_time=0.4)
        self.wait(0.6)
        self.play(FadeIn(tail), run_time=0.45)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B02 — The limit
# ═══════════════════════════════════════════════════════════════════════
class B02_LimitCard(Scene):
    def construct(self):
        self.camera.background_color = INK
        l1 = Text("A NUMBER CAN'T", font=FONT, weight="BOLD",
                  font_size=60, color=PAPER)
        l2 = Text("CHOOSE AN AUDIENCE.", font=FONT, weight="BOLD",
                  font_size=60, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        mark = Square(side_length=0.2, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(g, LEFT, buff=0.5)
        block = fit_block(mark, g)
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), FadeIn(mark, scale=1.3), run_time=0.8)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B03 — Eight audiences on one homepage
# ═══════════════════════════════════════════════════════════════════════
class B03_Audiences(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("ONE HOMEPAGE, EIGHT AUDIENCES.", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)
        fit_width(title)
        rows = marked_rows([
            "FELLOWS & INTERNATIONAL GRADUATES",
            "DONORS & SUPPORTERS",
            "MENTORS",
            "EDUCATORS & TEACHERS",
            "PARTNER ORGANISATIONS",
            "CHILDREN & FAMILIES",
            "VOLUNTEERS",
            "THE GENERAL PUBLIC",
        ], size=30, buff=0.26)
        rows.next_to(title, DOWN, buff=0.7)
        tail = Text("NO STATED ORDER OF PRIORITY.", font=FONT, weight="BOLD",
                    font_size=30, color=MAROON)
        tail.next_to(rows, DOWN, buff=0.65)
        fit_block(title, rows, tail)
        self.play(Write(title), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.12), run_time=0.2)
        self.wait(0.5)
        self.play(FadeIn(tail), run_time=0.45)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B04 — Internal shorthand, over the tier-framework screenshot
# ═══════════════════════════════════════════════════════════════════════
class B04_Terminology(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        self.add(full_frame_image("02_tier_framework.jpg", tag="b04"))
        boxes = [annotate_rect(b, sw=9) for b in (TIER_CARD_1, TIER_CARD_2, TIER_CARD_3)]
        for b in boxes:
            self.play(Create(b), run_time=0.45)
        self.wait(0.5)
        # Fitted to the band under the lowest card rather than pinned to a
        # y_frac: the third tier card reaches y = -2.37, which leaves only
        # 0.16 units of clearance for a pinned chip. chip_below measures it.
        c1 = chip_below("24 NAMED CONCEPTS.", boxes, size=32)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.4)
        self.wait(1.8)
        c2 = chip_below("ONE EVERY 50 WORDS.", boxes, size=32)
        self.play(FadeOut(c1), FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.2)


# ═══════════════════════════════════════════════════════════════════════
#  B05 — The exits
# ═══════════════════════════════════════════════════════════════════════
class B05_Exits(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("WAYS OFF THE HOMEPAGE.", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)
        blocks = VGroup(
            stat_block(13, "onward links"),
            stat_block(69, "clickable labels"),
            stat_block(54, "distinct labels"),
        ).arrange(RIGHT, buff=1.4, aligned_edge=UP)
        fit_width(blocks)
        blocks.next_to(title, DOWN, buff=1.1)
        tail = Text("THIRTEEN WAYS TO LEAVE. NO WAY TO BE LED.", font=FONT,
                    weight="BOLD", font_size=32, color=MAROON)
        tail.next_to(blocks, DOWN, buff=1.0)
        fit_width(tail)
        fit_block(title, blocks, tail)
        self.play(Write(title), run_time=0.7)
        for b in blocks:
            self.play(FadeIn(b, shift=UP * 0.15), run_time=0.4)
        self.wait(0.6)
        self.play(FadeIn(tail), run_time=0.5)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B06 — Three asks at once, over the mission-CTA screenshot
# ═══════════════════════════════════════════════════════════════════════
class B06_ThreeAsks(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        self.add(full_frame_image("05_mission_cta_spotify.jpg", tag="b06"))
        singles = [annotate_rect(b, sw=8) for b in
                   (CTA_DONATE_NOW, CTA_VOLUNTEER, CTA_YOUTUBE)]
        for b in singles:
            self.play(Create(b), run_time=0.35)
        self.wait(0.4)
        group_box = annotate_rect(CTA_GROUP, sw=10)
        self.play(Create(group_box), run_time=0.6)
        c = chip_below("THREE ASKS. NO PRIORITY.", [group_box], size=32)
        self.play(FadeIn(c, shift=UP * 0.1), run_time=0.4)
        self.wait(2.4)


# ═══════════════════════════════════════════════════════════════════════
#  B07 — Trust ledger
# ═══════════════════════════════════════════════════════════════════════
class B07_TrustLedger(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("WHAT A DONOR CAN VERIFY.", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)

        h1 = Text("ON THE PAGE", font=FONT, weight="BOLD", font_size=28, color=INK)
        left = marked_rows(["501(C)(3) STATUS", "EIN", "STATE REGISTRATION",
                            "PRIVACY POLICY", "TESTIMONIALS PAGE"],
                           size=26, buff=0.24, mark=0.15)
        left.next_to(h1, DOWN, buff=0.45, aligned_edge=LEFT)
        colL = VGroup(h1, left)

        h2 = Text("NOT ON THE PAGE", font=FONT, weight="BOLD", font_size=28, color=MAROON)
        right = marked_rows(["ANNUAL REPORT", "FORM 990", "A NAMED BOARD",
                             "A CHARITY RATING", "OUTCOME NUMBERS"],
                            size=26, buff=0.24, mark=0.15, color=MAROON)
        right.next_to(h2, DOWN, buff=0.45, aligned_edge=LEFT)
        colR = VGroup(h2, right)

        cols = VGroup(colL, colR).arrange(RIGHT, buff=1.6, aligned_edge=UP)
        cols.next_to(title, DOWN, buff=0.9)
        fit_block(title, cols)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(h1), run_time=0.3)
        for r in left:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.18)
        self.wait(0.4)
        self.play(FadeIn(h2), run_time=0.3)
        for r in right:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.18)
        self.wait(2.0)


# ═══════════════════════════════════════════════════════════════════════
#  B08 — The two donation claims. Both quoted from the live page.
# ═══════════════════════════════════════════════════════════════════════
class B08_DonationConflict(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("ONE PAGE. TWO PROMISES.", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)

        srcA = Text("MID-PAGE", font=FONT, weight="BOLD", font_size=22, color=SOFT)
        a1 = Text("“100% OF DONATIONS FUND THE PROGRAMS,", font=FONT,
                  weight="BOLD", font_size=28, color=INK)
        a2 = Text("MENTORSHIP AND PROJECT SUPPORT.”", font=FONT,
                  weight="BOLD", font_size=28, color=INK)
        blockA = VGroup(srcA, a1, a2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        barA = Rectangle(width=0.09, height=blockA.height, color=SOFT,
                         fill_color=SOFT, fill_opacity=1, stroke_width=0)
        barA.next_to(blockA, LEFT, buff=0.4)
        quoteA = VGroup(barA, blockA)

        srcB = Text("FOOTER, SAME PAGE", font=FONT, weight="BOLD", font_size=22, color=SOFT)
        b1 = Text("“100% OF ALL DONATIONS SUPPORT OUR DIRECT", font=FONT,
                  weight="BOLD", font_size=28, color=INK)
        b2 = Text("OPERATIONAL COSTS, INCLUDING LEGAL FEES", font=FONT,
                  weight="BOLD", font_size=28, color=INK)
        b3 = Text("AND STAFF SALARIES.”", font=FONT,
                  weight="BOLD", font_size=28, color=INK)
        blockB = VGroup(srcB, b1, b2, b3).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        barB = Rectangle(width=0.09, height=blockB.height, color=MAROON,
                         fill_color=MAROON, fill_opacity=1, stroke_width=0)
        barB.next_to(blockB, LEFT, buff=0.4)
        quoteB = VGroup(barB, blockB)

        quotes = VGroup(quoteA, quoteB).arrange(DOWN, aligned_edge=LEFT, buff=0.75)
        quotes.next_to(title, DOWN, buff=0.75)
        verdict = Text("BOTH CANNOT BE THE PROMISE.", font=FONT, weight="BOLD",
                       font_size=32, color=MAROON)
        verdict.next_to(quotes, DOWN, buff=0.7)
        fit_block(title, quotes, verdict)

        self.play(Write(title), run_time=0.7)
        self.play(GrowFromEdge(barA, UP), FadeIn(blockA, shift=RIGHT * 0.12), run_time=0.7)
        self.wait(1.8)
        self.play(GrowFromEdge(barB, UP), FadeIn(blockB, shift=RIGHT * 0.12), run_time=0.7)
        self.wait(1.6)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B09 — Every number on the page, and what it actually is
# ═══════════════════════════════════════════════════════════════════════
class B09_NoOutcomes(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("EVERY NUMBER ON THE HOMEPAGE.", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)
        rows = marked_rows([
            "TIER 1 / TIERS 3-6 / TIER 7  —  FRAMEWORK LABELS",
            "501(C)(3), EIN, STATE ID  —  LEGAL IDENTIFIERS",
            "18 CHAPTERS  —  A TABLE OF CONTENTS",
            "100%  —  A DONATION CLAIM",
            "2024-2026  —  A COPYRIGHT YEAR",
        ], size=26, buff=0.28, mark=0.15)
        rows.next_to(title, DOWN, buff=0.8)
        zero = Text("0 OUTCOMES.", font=FONT, weight="BOLD", font_size=52, color=MAROON)
        zero.next_to(rows, DOWN, buff=0.8)
        fit_block(title, rows, zero)
        self.play(Write(title), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.12), run_time=0.25)
        self.wait(0.8)
        self.play(FadeIn(zero, scale=1.1), run_time=0.5)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B10 — Not design decisions
# ═══════════════════════════════════════════════════════════════════════
class B10_NotDesignDecisions(Scene):
    def construct(self):
        self.camera.background_color = INK
        l1 = Text("NONE OF THAT IS", font=FONT, weight="BOLD",
                  font_size=56, color=PAPER)
        l2 = Text("A DESIGN DECISION.", font=FONT, weight="BOLD",
                  font_size=56, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        tail = Text("SURFACE IT. DON'T DECIDE IT ALONE.", font=FONT,
                    weight="BOLD", font_size=28, color=SOFT)
        tail.next_to(g, DOWN, buff=0.85, aligned_edge=LEFT)
        mark = Square(side_length=0.18, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(tail, LEFT, buff=0.3)
        fit_block(g, tail, mark)
        self.play(Write(l1), run_time=0.7)
        self.play(Write(l2), run_time=0.7)
        self.wait(0.5)
        self.play(FadeIn(tail), FadeIn(mark, scale=1.3), run_time=0.45)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B11 — The eight themes
# ═══════════════════════════════════════════════════════════════════════
class B11_EightThemes(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("THE DISCUSSION GUIDE — EIGHT THEMES.", font=FONT,
                     weight="BOLD", font_size=38, color=INK).to_edge(UP, buff=0.6)
        fit_width(title)
        colA = marked_rows(["AUDIENCE PRIORITY", "FIRST IMPRESSION",
                            "PRIMARY ACTION", "TERMINOLOGY"], size=30, buff=0.32)
        colB = marked_rows(["NAVIGATION", "TONE", "TRUST SIGNALS",
                            "SUCCESS METRICS"], size=30, buff=0.32)
        cols = VGroup(colA, colB).arrange(RIGHT, buff=1.8, aligned_edge=UP)
        cols.next_to(title, DOWN, buff=1.0)
        fit_block(title, cols)
        self.play(Write(title), run_time=0.7)
        for a, b in zip(colA, colB):
            self.play(FadeIn(a, shift=RIGHT * 0.12), FadeIn(b, shift=RIGHT * 0.12),
                      run_time=0.3)
        self.wait(2.2)


# ═══════════════════════════════════════════════════════════════════════
#  B12 — Questions: audience and message
# ═══════════════════════════════════════════════════════════════════════
class B12_QuestionsAudience(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        kick = Text("AUDIENCE & MESSAGE", font=FONT, weight="BOLD",
                    font_size=26, color=MAROON).to_edge(UP, buff=0.6)
        qs = question_block([
            ["IF A VISITOR READS ONE SENTENCE AND LEAVES,", "WHAT SHOULD IT HAVE TOLD THEM?"],
            ["WHICH SINGLE AUDIENCE MATTERS MOST", "THIS QUARTER?"],
            ["WHAT DO PEOPLE MOST OFTEN MISUNDERSTAND", "ABOUT WHAT THIS ORGANISATION DOES?"],
        ], size=30)
        qs.next_to(kick, DOWN, buff=0.75, aligned_edge=LEFT)
        bar = Rectangle(width=0.09, height=qs.height, color=MAROON,
                        fill_color=MAROON, fill_opacity=1, stroke_width=0)
        bar.next_to(qs, LEFT, buff=0.45)
        # One maroon mark per question. GATE A errors on a scene whose SHAPE
        # state never changes, and a page of questions plus one static bar is
        # exactly one shape-state.
        marks = VGroup(*[
            Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                   fill_opacity=1, stroke_width=0).next_to(q, LEFT, buff=0.28)
            for q in qs
        ])
        block = VGroup(kick, bar, qs, marks)
        if block.height > config.frame_height - 2 * SAFE_BUFF_Y:
            block.scale_to_fit_height(config.frame_height - 2 * SAFE_BUFF_Y)
        if block.width > config.frame_width - 2 * SAFE_BUFF_X:
            block.scale_to_fit_width(config.frame_width - 2 * SAFE_BUFF_X)
        block.move_to(ORIGIN)
        self.play(FadeIn(kick), run_time=0.4)
        self.play(GrowFromEdge(bar, UP), run_time=0.5)
        for group, mark in zip(qs, marks):
            self.play(FadeIn(group[0], shift=RIGHT * 0.1), FadeIn(mark, scale=1.3),
                      run_time=0.3)
            for line in group[1:]:
                self.play(FadeIn(line, shift=RIGHT * 0.1), run_time=0.25)
            self.wait(0.25)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B13 — Questions: action, terminology, navigation
# ═══════════════════════════════════════════════════════════════════════
class B13_QuestionsAction(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        kick = Text("ACTION & LANGUAGE", font=FONT, weight="BOLD",
                    font_size=26, color=MAROON).to_edge(UP, buff=0.6)
        qs = question_block([
            ["IF A VISITOR DOES EXACTLY ONE THING,", "WHAT SHOULD IT BE?"],
            ["WHICH NAMED CONCEPTS WOULD YOU KEEP IF A", "STRANGER READ THE PAGE UNHELPED?"],
            ["WHICH NAV LINKS EXIST BECAUSE", "SOMEONE STILL NEEDS THEM?"],
        ], size=30)
        qs.next_to(kick, DOWN, buff=0.75, aligned_edge=LEFT)
        bar = Rectangle(width=0.09, height=qs.height, color=MAROON,
                        fill_color=MAROON, fill_opacity=1, stroke_width=0)
        bar.next_to(qs, LEFT, buff=0.45)
        # One maroon mark per question. GATE A errors on a scene whose SHAPE
        # state never changes, and a page of questions plus one static bar is
        # exactly one shape-state.
        marks = VGroup(*[
            Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                   fill_opacity=1, stroke_width=0).next_to(q, LEFT, buff=0.28)
            for q in qs
        ])
        block = VGroup(kick, bar, qs, marks)
        if block.height > config.frame_height - 2 * SAFE_BUFF_Y:
            block.scale_to_fit_height(config.frame_height - 2 * SAFE_BUFF_Y)
        if block.width > config.frame_width - 2 * SAFE_BUFF_X:
            block.scale_to_fit_width(config.frame_width - 2 * SAFE_BUFF_X)
        block.move_to(ORIGIN)
        self.play(FadeIn(kick), run_time=0.4)
        self.play(GrowFromEdge(bar, UP), run_time=0.5)
        for group, mark in zip(qs, marks):
            self.play(FadeIn(group[0], shift=RIGHT * 0.1), FadeIn(mark, scale=1.3),
                      run_time=0.3)
            for line in group[1:]:
                self.play(FadeIn(line, shift=RIGHT * 0.1), run_time=0.25)
            self.wait(0.25)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B14 — Questions: trust, metrics, tone
# ═══════════════════════════════════════════════════════════════════════
class B14_QuestionsTrust(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        kick = Text("TRUST & PROOF", font=FONT, weight="BOLD",
                    font_size=26, color=MAROON).to_edge(UP, buff=0.6)
        qs = question_block([
            ["WHAT WOULD A DONOR NEED TO SEE", "TO GIVE WITH CONFIDENCE?"],
            ["WHAT IS THE ONE NUMBER THAT WOULD SHOW", "THIS YEAR WAS WORTH FUNDING?"],
            ["WHERE SHOULD THIS SOUND LIKE RESEARCH,", "AND WHERE LIKE A PROGRAMME TO JOIN?"],
        ], size=30)
        qs.next_to(kick, DOWN, buff=0.75, aligned_edge=LEFT)
        bar = Rectangle(width=0.09, height=qs.height, color=MAROON,
                        fill_color=MAROON, fill_opacity=1, stroke_width=0)
        bar.next_to(qs, LEFT, buff=0.45)
        # One maroon mark per question. GATE A errors on a scene whose SHAPE
        # state never changes, and a page of questions plus one static bar is
        # exactly one shape-state.
        marks = VGroup(*[
            Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                   fill_opacity=1, stroke_width=0).next_to(q, LEFT, buff=0.28)
            for q in qs
        ])
        block = VGroup(kick, bar, qs, marks)
        if block.height > config.frame_height - 2 * SAFE_BUFF_Y:
            block.scale_to_fit_height(config.frame_height - 2 * SAFE_BUFF_Y)
        if block.width > config.frame_width - 2 * SAFE_BUFF_X:
            block.scale_to_fit_width(config.frame_width - 2 * SAFE_BUFF_X)
        block.move_to(ORIGIN)
        self.play(FadeIn(kick), run_time=0.4)
        self.play(GrowFromEdge(bar, UP), run_time=0.5)
        for group, mark in zip(qs, marks):
            self.play(FadeIn(group[0], shift=RIGHT * 0.1), FadeIn(mark, scale=1.3),
                      run_time=0.3)
            for line in group[1:]:
                self.play(FadeIn(line, shift=RIGHT * 0.1), run_time=0.25)
            self.wait(0.25)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B15 — The structural hierarchy order
#  An abstract content order, NOT a layout of their page. See rule A.
# ═══════════════════════════════════════════════════════════════════════
class B15_HierarchyOrder(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("STRUCTURAL HIERARCHY — THE ORDER.", font=FONT,
                     weight="BOLD", font_size=38, color=INK).to_edge(UP, buff=0.6)
        fit_width(title)

        steps = [("01", "WHAT THEY CAME LOOKING FOR"),
                 ("02", "WHY IT IS CREDIBLE"),
                 ("03", "THE ONE THING TO DO NEXT"),
                 ("04", "EVERYTHING ELSE THE ORG OFFERS")]
        rows = VGroup()
        for num, label in steps:
            n = Text(num, font=FONT, weight="BOLD", font_size=34, color=MAROON)
            t = Text(label, font=FONT, weight="BOLD", font_size=34, color=INK)
            t.next_to(n, RIGHT, buff=0.5)
            rows.add(VGroup(n, t))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.42)
        rows.next_to(title, DOWN, buff=0.9)
        bar = Rectangle(width=0.1, height=rows.height, color=MAROON,
                        fill_color=MAROON, fill_opacity=1, stroke_width=0)
        bar.next_to(rows, LEFT, buff=0.45)
        fit_block(title, bar, rows)

        self.play(Write(title), run_time=0.7)
        self.play(GrowFromEdge(bar, UP), run_time=0.5)
        for r in rows:
            tick = Square(side_length=0.12, color=MAROON, fill_color=MAROON,
                          fill_opacity=1, stroke_width=0).next_to(r, LEFT, buff=0.22)
            self.play(FadeIn(r, shift=RIGHT * 0.15), FadeIn(tick), run_time=0.4)
        self.wait(2.0)


# ═══════════════════════════════════════════════════════════════════════
#  B16 — The hero stays a direction (rule A, carried from Week 2)
# ═══════════════════════════════════════════════════════════════════════
class B16_HeroHeld(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        l1 = Text("THE HERO STAYS", font=FONT, weight="BOLD",
                  font_size=58, color=INK)
        l2 = Text("A DIRECTION.", font=FONT, weight="BOLD",
                  font_size=58, color=MAROON)
        head = VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        b1 = Text("NOT REDRAWN UNTIL THE PEOPLE WHO OWN", font=FONT,
                  weight="BOLD", font_size=28, color=INK)
        b2 = Text("THE MESSAGE SAY WHICH MESSAGE LEADS.", font=FONT,
                  weight="BOLD", font_size=28, color=INK)
        body = VGroup(b1, b2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        body.next_to(head, DOWN, buff=0.8, aligned_edge=LEFT)
        bar = Rectangle(width=0.1, height=head.height + body.height + 0.8,
                        color=MAROON, fill_color=MAROON, fill_opacity=1, stroke_width=0)
        bar.next_to(VGroup(head, body), LEFT, buff=0.5)
        fit_block(bar, head, body)
        self.play(GrowFromEdge(bar, UP), run_time=0.5)
        self.play(Write(l1), run_time=0.7)
        self.play(Write(l2), run_time=0.6)
        self.wait(0.5)
        m1 = Square(side_length=0.15, color=MAROON, fill_color=MAROON,
                    fill_opacity=1, stroke_width=0).next_to(b1, LEFT, buff=0.28)
        m2 = Square(side_length=0.15, color=MAROON, fill_color=MAROON,
                    fill_opacity=1, stroke_width=0).next_to(b2, LEFT, buff=0.28)
        self.play(FadeIn(b1, shift=RIGHT * 0.12), FadeIn(m1), run_time=0.4)
        self.play(FadeIn(b2, shift=RIGHT * 0.12), FadeIn(m2, scale=1.3), run_time=0.4)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B17 — Close: the four-week arc
# ═══════════════════════════════════════════════════════════════════════
class B17_Close(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        rows = VGroup()
        for num, label, col in (("WEEK 1", "THE AUDIT", SOFT),
                                ("WEEK 2", "THE SPECIFICATION", SOFT),
                                ("WEEK 3", "THE QUESTIONS", MAROON),
                                ("WEEK 4", "NAV CLEANUP + HANDOFF", INK)):
            n = Text(num, font=FONT, weight="BOLD", font_size=34, color=col)
            t = Text(label, font=FONT, weight="BOLD", font_size=34, color=col)
            t.next_to(n, RIGHT, buff=0.6)
            rows.add(VGroup(n, t))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        bar = Rectangle(width=0.1, height=rows.height, color=MAROON,
                        fill_color=MAROON, fill_opacity=1, stroke_width=0)
        bar.next_to(rows, LEFT, buff=0.5)
        fit_block(bar, rows)
        self.play(GrowFromEdge(bar, UP), run_time=0.5)
        for r in rows:
            tick = Square(side_length=0.12, color=MAROON, fill_color=MAROON,
                          fill_opacity=1, stroke_width=0).next_to(r, LEFT, buff=0.22)
            self.play(FadeIn(r, shift=RIGHT * 0.15), FadeIn(tick), run_time=0.45)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B18 — End card
# ═══════════════════════════════════════════════════════════════════════
class B18_EndCard(Scene):
    def construct(self):
        self.camera.background_color = INK
        l1 = Text("HUMANITARIANS.AI RESTRUCTURE", font=FONT, weight="BOLD",
                  font_size=42, color=PAPER)
        l2 = Text("WEEK 3 OF 4", font=FONT, weight="BOLD",
                  font_size=42, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, buff=0.35)
        mark = Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(g, DOWN, buff=0.5)
        fit_block(g, mark)
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), FadeIn(mark, scale=1.3), run_time=0.7)
        self.wait(2.2)
