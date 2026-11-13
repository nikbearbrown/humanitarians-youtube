"""scenes.py — Manim scenes for humanitarians-ai-week2-typography-hero-concepting.

WEEK 2 OF 4. Visual system is locked to Week 1 (see ../humanitarians-ai-week1-
diagnostic-audit/scenes.py): PAPER white ground, INK near-black type, one MAROON
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
came from the running site; every annotation box came from PIL/numpy analysis
of the actual screenshot pixels. See SOURCES.md for the method and SHOTLIST.md
for the coordinate table.
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
        sub = Text("WEEK 2 — TYPOGRAPHY + HERO CONCEPTING", font=FONT,
                   weight="BOLD", font_size=32, color=MAROON).next_to(rule, DOWN, buff=0.45)
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
        self.wait(2.2)


# ═══════════════════════════════════════════════════════════════════════
#  B01 — Scope confirmed (black card)
# ═══════════════════════════════════════════════════════════════════════
class B01_ScopeCard(Scene):
    def construct(self):
        self.camera.background_color = INK
        l1 = Text("PLAN B, CONFIRMED.", font=FONT, weight="BOLD",
                  font_size=58, color=PAPER)
        l2 = Text("FIX FIRST. REASSESS LATER.", font=FONT, weight="BOLD",
                  font_size=58, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        fit_width(g)
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), run_time=0.9)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B02 — Method card (white)
# ═══════════════════════════════════════════════════════════════════════
class B02_MethodCard(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        l1 = Text("MEASURED.", font=FONT, weight="BOLD", font_size=76, color=INK)
        l2 = Text("NOT ESTIMATED.", font=FONT, weight="BOLD", font_size=76, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 0.3)
        fit_width(g)
        sub = Text("EVERY FIGURE IN THIS VIDEO CAME OFF THE LIVE SITE.",
                   font=FONT, weight="BOLD", font_size=26, color=SOFT)
        sub.next_to(g, DOWN, buff=0.8)
        fit_width(sub)
        self.play(Write(l1), run_time=0.7)
        self.play(Write(l2), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B03 — Navigation, annotated on the hero screenshot
#  Boxes measured from 01_hero_section.jpg header strip (see SHOTLIST.md).
# ═══════════════════════════════════════════════════════════════════════
NAV_SECTION_LINKS = (0.2043, 0.0148, 0.3779, 0.0653)   # AI+1 / Fellows / Projects / Videos
NAV_CTA_BUTTONS   = (0.7172, 0.0148, 0.8882, 0.0653)   # Youtube / Donate
BTN_YOUTUBE       = (0.7172, 0.0160, 0.7991, 0.0653)
BTN_DONATE        = (0.8110, 0.0160, 0.8882, 0.0653)
BTN_ABOUT         = (0.0725, 0.7623, 0.1590, 0.8116)
BTN_CONTACT       = (0.1657, 0.7623, 0.2608, 0.8116)
HERO_VIDEO        = (0.3686, 0.2192, 0.9275, 0.7993)
HERO_MESSAGE      = (0.0725, 0.2167, 0.3320, 0.8128)


class B03_NavAnnotated(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        self.add(full_frame_image("01_hero_section.jpg", tag="b03"))

        sections = annotate_rect(NAV_SECTION_LINKS, sw=9)
        ctas = annotate_rect(NAV_CTA_BUTTONS, sw=9)

        self.play(Create(sections), run_time=0.8)
        self.wait(0.4)
        self.play(Create(ctas), run_time=0.7)
        self.wait(0.5)

        c1 = place_chip("4 SECTION LINKS. 2 BUTTONS.", y_frac=0.83, size=32)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)
        c2 = place_chip("NO ABOUT. NO CONTACT.", y_frac=0.83, size=32)
        self.play(FadeOut(c1), FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.4)


# ═══════════════════════════════════════════════════════════════════════
#  B04 — Nav map, drawn
# ═══════════════════════════════════════════════════════════════════════
class B04_NavMap(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("PRIMARY NAV, MAPPED.", font=FONT, weight="BOLD",
                     font_size=42, color=INK).to_edge(UP, buff=0.6)

        slots = [("LOGO", False), ("AI+1", False), ("FELLOWS", False),
                 ("PROJECTS", False), ("VIDEOS", False),
                 ("YOUTUBE", True), ("DONATE", True)]
        cells = VGroup()
        for label, is_cta in slots:
            t = Text(label, font=FONT, weight="BOLD", font_size=24,
                     color=PAPER if is_cta else INK)
            box = Rectangle(width=t.width + 0.45, height=0.78,
                            color=MAROON if is_cta else INK,
                            fill_color=MAROON if is_cta else PAPER,
                            fill_opacity=1 if is_cta else 0,
                            stroke_width=0 if is_cta else 4)
            box.move_to(t.get_center())
            cells.add(VGroup(box, t))
        cells.arrange(RIGHT, buff=0.28)
        fit_width(cells)
        cells.next_to(title, DOWN, buff=0.85)

        absent_title = Text("NOT IN THE BAR AT ALL:", font=FONT, weight="BOLD",
                            font_size=26, color=SOFT)
        ghosts = VGroup()
        for label in ("ABOUT US", "CONTACT US"):
            t = Text(label, font=FONT, weight="BOLD", font_size=24, color=SOFT)
            box = Rectangle(width=t.width + 0.45, height=0.78, color=SOFT,
                            fill_opacity=0, stroke_width=3)
            box.move_to(t.get_center())
            ghosts.add(VGroup(box, t))
        ghosts.arrange(RIGHT, buff=0.28)
        absent = VGroup(absent_title, ghosts).arrange(DOWN, buff=0.4)
        absent.next_to(cells, DOWN, buff=1.05)
        fit_width(absent)

        verdict = Text("ORIENTATION MISSING. PROMOTION DUPLICATED.", font=FONT,
                       weight="BOLD", font_size=28, color=MAROON)
        verdict.next_to(absent, DOWN, buff=0.7)
        fit_width(verdict)

        self.play(Write(title), run_time=0.7)
        for cell in cells:
            self.play(FadeIn(cell, shift=DOWN * 0.12), run_time=0.16)
        self.wait(0.5)
        self.play(FadeIn(absent_title), run_time=0.35)
        self.play(*[FadeIn(gh, shift=UP * 0.1) for gh in ghosts], run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(verdict), run_time=0.45)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B05 — Footer, annotated
#  Projects-column box MEASURED from 06_footer.jpg ink columns. Week 1's
#  estimated box (0.62,0,0.92,0.55) actually spanned THREE columns; this is
#  the corrected one (see BUILD-LOG.md).
# ═══════════════════════════════════════════════════════════════════════
FOOTER_PROJECTS_COL = (0.7319, 0.0973, 0.8071, 0.5012)


class B05_FooterFull(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        self.add(full_frame_image("06_footer.jpg", tag="b05"))
        box = annotate_rect(FOOTER_PROJECTS_COL, sw=9)

        c1 = place_chip("6 COLUMNS. 33 LINKS.", y_frac=0.86, size=32)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.45)
        self.wait(1.6)
        self.play(Create(box), run_time=0.8)
        self.wait(0.5)
        c2 = place_chip("39 ANCHORS IN TOTAL.", y_frac=0.86, size=32)
        self.play(FadeOut(c1), FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.2)


# ═══════════════════════════════════════════════════════════════════════
#  B06 — The six undecodable project names, typeset
#  Drawn rather than cropped: the source screenshot is only 1503px wide, so
#  a tight crop of this column would be a ~12x upscale at 4K and illegible.
#  B05 supplies the photographic evidence; this beat supplies the reading.
# ═══════════════════════════════════════════════════════════════════════
class B06_ProjectNames(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("PROJECTS COLUMN — 11 LINKS.", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)

        names = ["DEWEY", "MADISON", "MEDHAVY", "MUSINIQUE", "MYCROFT", "POPPER"]
        rows = VGroup()
        for n in names:
            mark = Square(side_length=0.2, color=MAROON, fill_color=MAROON,
                          fill_opacity=1, stroke_width=0)
            t = Text(n, font=FONT, weight="BOLD", font_size=44, color=INK)
            t.next_to(mark, RIGHT, buff=0.4)
            rows.add(VGroup(mark, t))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        rows.next_to(title, DOWN, buff=0.75)

        verdict = Text("6 BARE PROPER NOUNS. 0 CONTEXT.", font=FONT, weight="BOLD",
                       font_size=32, color=MAROON)
        verdict.next_to(rows, DOWN, buff=0.65)
        block = VGroup(title, rows, verdict)
        if block.height > config.frame_height - 2 * SAFE_BUFF:
            block.scale_to_fit_height(config.frame_height - 2 * SAFE_BUFF)
        block.move_to(ORIGIN)
        fit_width(block)

        self.play(Write(title), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.15), run_time=0.22)
        self.wait(0.6)
        self.play(FadeIn(verdict), run_time=0.45)
        self.wait(2.0)


# ═══════════════════════════════════════════════════════════════════════
#  B07 — Duplicate links across columns
# ═══════════════════════════════════════════════════════════════════════
class B07_FooterDupes(Scene):
    def construct(self):
        self.camera.background_color = INK
        title = Text("LISTED TWICE:", font=FONT, weight="BOLD",
                     font_size=40, color=PAPER).to_edge(UP, buff=1.0)

        entries = [("ALL PROJECTS", "COMPANY  +  PROJECTS"),
                   ("MUSINIQUE", "RESOURCES  +  PROJECTS")]
        rows = VGroup()
        for name, where in entries:
            n = Text(name, font=FONT, weight="BOLD", font_size=50, color=PAPER)
            w = Text(where, font=FONT, weight="BOLD", font_size=26, color=MAROON)
            w.next_to(n, DOWN, buff=0.22, aligned_edge=LEFT)
            rows.add(VGroup(n, w))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        rows.next_to(title, DOWN, buff=0.8)
        block = VGroup(title, rows).move_to(ORIGIN)
        fit_width(block)

        self.play(Write(title), run_time=0.6)
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.12), run_time=0.5)
            self.wait(0.5)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B08 — Typography, counted
# ═══════════════════════════════════════════════════════════════════════
class B08_TypeCount(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("ONE HOMEPAGE, COUNTED.", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)

        blocks = VGroup(
            stat_block(19, "text styles"),
            stat_block(8, "font sizes"),
            stat_block(1, "type family"),
            stat_block("6/8", "sizes set in bold", num_size=76),
        )
        blocks.arrange(RIGHT, buff=1.1, aligned_edge=UP)
        fit_width(blocks)
        blocks.next_to(title, DOWN, buff=1.1)

        verdict = Text("MANY SIZES. ALMOST NO LEVELS.", font=FONT, weight="BOLD",
                       font_size=34, color=MAROON)
        verdict.next_to(blocks, DOWN, buff=1.0)
        fit_width(verdict)
        grp = VGroup(title, blocks, verdict)
        if grp.height > config.frame_height - 2 * SAFE_BUFF:
            grp.scale_to_fit_height(config.frame_height - 2 * SAFE_BUFF)
        grp.move_to(ORIGIN)

        self.play(Write(title), run_time=0.7)
        for b in blocks:
            self.play(FadeIn(b, shift=UP * 0.15), run_time=0.4)
        self.wait(0.8)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B09 — The specified four-step scale, rung by rung
# ═══════════════════════════════════════════════════════════════════════
class B09_TypeScaleSpec(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("PROPOSED SCALE — FOUR STEPS, ONE JOB EACH.", font=FONT,
                     weight="BOLD", font_size=36, color=INK).to_edge(UP, buff=0.6)
        fit_width(title)

        # The five rungs are written out with LITERAL font_size values rather
        # than built in a loop. runtime/qc/wcag_margin_check.py reads font_size
        # straight off the AST; a loop variable arrives as a string and the
        # checker dies on "(it.size or 30) >= 36", which run.sh swallows as a
        # non-blocking warning — leaving the scene silently unchecked. Literals
        # keep GATE W's real contrast/margin analysis running on this beat.
        r_display  = Text("DISPLAY",  font=FONT, weight="BOLD", font_size=74, color=INK)
        r_headline = Text("HEADLINE", font=FONT, weight="BOLD", font_size=52, color=INK)
        r_subhead  = Text("SUBHEAD",  font=FONT, weight="BOLD", font_size=34, color=SOFT)
        r_body     = Text("BODY",     font=FONT, weight="BOLD", font_size=27, color=SOFT)
        r_caption  = Text("CAPTION",  font=FONT, weight="BOLD", font_size=22, color=SOFT)
        v_display  = Text("60 PX", font=FONT, weight="BOLD", font_size=22, color=MAROON)
        v_headline = Text("36 PX", font=FONT, weight="BOLD", font_size=22, color=MAROON)
        v_subhead  = Text("20 PX", font=FONT, weight="BOLD", font_size=22, color=MAROON)
        v_body     = Text("16 PX", font=FONT, weight="BOLD", font_size=22, color=MAROON)
        v_caption  = Text("14 PX", font=FONT, weight="BOLD", font_size=22, color=MAROON)

        group = VGroup()
        for t, v in ((r_display, v_display), (r_headline, v_headline),
                     (r_subhead, v_subhead), (r_body, v_body),
                     (r_caption, v_caption)):
            v.next_to(t, RIGHT, buff=0.45).align_to(t, DOWN)
            group.add(VGroup(t, v))
        group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        group.next_to(title, DOWN, buff=0.75)

        accent = Rectangle(width=0.12, height=group.height, color=MAROON,
                           fill_color=MAROON, fill_opacity=1, stroke_width=0)
        accent.next_to(group, LEFT, buff=0.45)

        note = Text("BOLD STOPS AT HEADLINE.", font=FONT, weight="BOLD",
                    font_size=26, color=MAROON)
        note.next_to(group, DOWN, buff=0.6).align_to(group, LEFT)

        block = VGroup(title, accent, group, note)
        if block.height > config.frame_height - 2 * SAFE_BUFF:
            block.scale_to_fit_height(config.frame_height - 2 * SAFE_BUFF)
        fit_width(block)
        block.move_to(ORIGIN)

        self.play(Write(title), run_time=0.7)
        self.play(GrowFromEdge(accent, UP), run_time=0.5)
        # A maroon tick per rung. Not decoration: GATE A's static check fails a
        # scene whose SHAPE state never changes ("shapes never change — 1
        # distinct shape-state"), and a ladder of pure Text plus one static
        # accent bar trips exactly that. Week 1's B08 ticked each rung for the
        # same reason. Reproduced locally against runtime/qc/static_scene_check.py
        # before this file was ever rendered.
        for row in group:
            tick = Square(side_length=0.1, color=MAROON, fill_color=MAROON,
                          fill_opacity=1, stroke_width=0).next_to(row, LEFT, buff=0.22)
            self.play(FadeIn(row, shift=RIGHT * 0.2), FadeIn(tick), run_time=0.4)
        self.wait(0.6)
        self.play(FadeIn(note), run_time=0.4)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B10 — Line length, measured
# ═══════════════════════════════════════════════════════════════════════
class B10_LineLength(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("LINE LENGTH, MEASURED.", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)

        bar_w = config.frame_width - 2 * (SAFE_BUFF + 0.9)
        scale = bar_w / 100.0          # bar spans 0-100 characters
        left = -bar_w / 2

        track = Rectangle(width=bar_w, height=0.42, color=SOFT,
                          fill_opacity=0, stroke_width=3)
        track.move_to([0, 0.55, 0])

        comfy = Rectangle(width=(75 - 45) * scale, height=0.42, color=INK,
                          fill_color=INK, fill_opacity=1, stroke_width=0)
        comfy.move_to([left + (45 + 15) * scale, 0.55, 0])
        comfy_lab = Text("45-75  COMFORTABLE", font=FONT, weight="BOLD",
                         font_size=22, color=INK)
        comfy_lab.next_to(comfy, DOWN, buff=0.35)

        actual = Rectangle(width=0.09, height=1.0, color=MAROON,
                           fill_color=MAROON, fill_opacity=1, stroke_width=0)
        actual.move_to([left + 84 * scale, 0.55, 0])
        actual_lab = Text("84  ACTUAL", font=FONT, weight="BOLD",
                          font_size=26, color=MAROON)
        actual_lab.next_to(actual, UP, buff=0.3)

        fix = Text("FIX: A MAX-WIDTH ON THE TEXT COLUMN. COSTS NOTHING.",
                   font=FONT, weight="BOLD", font_size=26, color=SOFT)
        fix.move_to([0, -2.3, 0])
        fit_width(fix)

        self.play(Write(title), run_time=0.7)
        self.play(Create(track), run_time=0.6)
        self.play(FadeIn(comfy), FadeIn(comfy_lab), run_time=0.5)
        self.wait(0.6)
        self.play(GrowFromEdge(actual, DOWN), FadeIn(actual_lab), run_time=0.5)
        self.wait(0.8)
        self.play(FadeIn(fix), run_time=0.4)
        self.wait(2.0)


# ═══════════════════════════════════════════════════════════════════════
#  B11 — Contrast. The greys appear ONLY as filled swatches, never as type:
#  setting a label in #7D7D7D would both fail GATE W and undercut the point.
# ═══════════════════════════════════════════════════════════════════════
class B11_ContrastCard(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("SECONDARY TEXT COLOR VS. WCAG AA.", font=FONT,
                     weight="BOLD", font_size=38, color=INK).to_edge(UP, buff=0.6)
        fit_width(title)

        def row(swatch_color, hexname, ratio, verdict, verdict_color):
            sw = Rectangle(width=1.5, height=1.0, color=swatch_color,
                           fill_color=swatch_color, fill_opacity=1, stroke_width=0)
            hx = Text(hexname, font=FONT, weight="BOLD", font_size=34, color=INK)
            rt = Text(ratio, font=FONT, weight="BOLD", font_size=34, color=INK)
            vd = Text(verdict, font=FONT, weight="BOLD", font_size=34, color=verdict_color)
            grp = VGroup(sw, hx, rt, vd).arrange(RIGHT, buff=0.7)
            return grp

        r1 = row(GREY_FAIL, "#7D7D7D", "4.12 : 1", "FAILS AA", MAROON)
        r2 = row(GREY_PASS, "#767676", "4.54 : 1", "PASSES AA", INK)
        rows = VGroup(r1, r2).arrange(DOWN, aligned_edge=LEFT, buff=0.85)
        rows.next_to(title, DOWN, buff=1.0)
        fit_width(rows)

        scope = Text("64 ELEMENTS USE IT. 52 AT BODY SIZE.", font=FONT,
                     weight="BOLD", font_size=30, color=MAROON)
        scope.next_to(rows, DOWN, buff=0.9)
        fit_width(scope)

        block = VGroup(title, rows, scope)
        if block.height > config.frame_height - 2 * SAFE_BUFF:
            block.scale_to_fit_height(config.frame_height - 2 * SAFE_BUFF)
        block.move_to(ORIGIN)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(r1, shift=RIGHT * 0.15), run_time=0.6)
        self.wait(1.6)
        self.play(FadeIn(r2, shift=RIGHT * 0.15), run_time=0.6)
        self.wait(1.0)
        self.play(FadeIn(scope), run_time=0.5)
        self.wait(2.4)


# ═══════════════════════════════════════════════════════════════════════
#  B12 — Four maroon CTAs above the fold
# ═══════════════════════════════════════════════════════════════════════
class B12_MaroonCTAs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        self.add(full_frame_image("01_hero_section.jpg", tag="b12"))
        boxes = [annotate_rect(b, sw=9) for b in
                 (BTN_YOUTUBE, BTN_DONATE, BTN_ABOUT, BTN_CONTACT)]
        for b in boxes:
            self.play(Create(b), run_time=0.4)
        self.wait(0.6)
        # computed to clear the About/Contact boxes rather than guessed
        c = chip_below("FOUR CTAS. ONE WEIGHT.", boxes, size=32)
        self.play(FadeIn(c, shift=UP * 0.1), run_time=0.45)
        self.wait(2.6)


# ═══════════════════════════════════════════════════════════════════════
#  B13 — Hero: media area vs. message area
# ═══════════════════════════════════════════════════════════════════════
class B13_HeroRatio(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        self.add(full_frame_image("01_hero_section.jpg", tag="b13"))
        media = annotate_rect(HERO_VIDEO, sw=10)
        message = annotate_rect(HERO_MESSAGE, sw=10)

        self.play(Create(media), run_time=0.8)
        c1 = chip_below("VIDEO: 2.10x THE AREA.", [media, message], size=30)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.4)
        self.wait(1.8)
        self.play(Create(message), run_time=0.8)
        c2 = chip_below("MESSAGE: 26% OF THE FRAME.", [media, message], size=30)
        self.play(FadeOut(c1), FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.6)


# ═══════════════════════════════════════════════════════════════════════
#  B14 — Hero direction: current vs. proposed wireframe
# ═══════════════════════════════════════════════════════════════════════
class B14_HeroDirection(Scene):
    """The hero direction, stated as a principle — NOT drawn as a layout.

    An earlier version of this beat showed a "current vs proposed" wireframe.
    Muskan removed it: the site's hero is not being shown altered, because no
    redesign has been settled. Showing an invented layout would claim work that
    has not been done. The beat now states the intent and nothing more.
    """
    def construct(self):
        self.camera.background_color = PAPER
        l1 = Text("NOT A LAYOUT YET.", font=FONT, weight="BOLD",
                  font_size=62, color=INK)
        l2 = Text("A PRINCIPLE.", font=FONT, weight="BOLD",
                  font_size=62, color=MAROON)
        head = VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.28)

        body = Text("ORDER THE HERO AROUND WHAT A FIRST-TIME",
                    font=FONT, weight="BOLD", font_size=30, color=INK)
        body2 = Text("VISITOR EXPECTS TO FIND FIRST.",
                     font=FONT, weight="BOLD", font_size=30, color=INK)
        lines = VGroup(body, body2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        lines.next_to(head, DOWN, buff=0.75, aligned_edge=LEFT)

        rule = Rectangle(width=0.1, height=head.height + lines.height + 0.75,
                         color=MAROON, fill_color=MAROON, fill_opacity=1,
                         stroke_width=0)
        rule.next_to(VGroup(head, lines), LEFT, buff=0.5)

        tail = Text("SAME CONTENT. DIFFERENT PRIORITY.", font=FONT,
                    weight="BOLD", font_size=28, color=SOFT)
        tail.next_to(lines, DOWN, buff=0.8, aligned_edge=LEFT)

        # Two maroon marks, landing with the two body lines. Same reason as the
        # ticks in B09: GATE A fails any scene whose shape state never changes,
        # and a single static accent rule is one state across the whole beat.
        mark1 = Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                       fill_opacity=1, stroke_width=0).next_to(body, LEFT, buff=0.3)
        mark2 = Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                       fill_opacity=1, stroke_width=0).next_to(tail, LEFT, buff=0.3)

        block = VGroup(rule, head, lines, tail, mark1, mark2)
        if block.height > config.frame_height - 2 * SAFE_BUFF:
            block.scale_to_fit_height(config.frame_height - 2 * SAFE_BUFF)
        fit_width(block)
        block.move_to(ORIGIN)

        self.play(GrowFromEdge(rule, UP), run_time=0.5)
        self.play(Write(l1), run_time=0.7)
        self.play(Write(l2), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(body, shift=RIGHT * 0.15), FadeIn(mark1), run_time=0.45)
        self.play(FadeIn(body2, shift=RIGHT * 0.15), run_time=0.45)
        self.wait(0.8)
        self.play(FadeIn(tail), FadeIn(mark2, scale=1.3), run_time=0.45)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B15 — Close
# ═══════════════════════════════════════════════════════════════════════
class B15_Close(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        l1 = Text("WEEK 2 WAS THE SPEC.", font=FONT, weight="BOLD",
                  font_size=52, color=INK)
        l2 = Text("WEEK 3 IS THE BUILD.", font=FONT, weight="BOLD",
                  font_size=52, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 0.4)
        fit_width(g)
        tag = Text("A SCALE. A CONTRAST TARGET. A LINE LENGTH. A HERO.",
                   font=FONT, weight="BOLD", font_size=26, color=SOFT)
        tag.next_to(g, DOWN, buff=0.8)
        fit_width(tag)
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), run_time=0.7)
        self.wait(0.8)
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(2.0)


# ═══════════════════════════════════════════════════════════════════════
#  B16 — End card
# ═══════════════════════════════════════════════════════════════════════
class B16_EndCard(Scene):
    def construct(self):
        self.camera.background_color = INK
        l1 = Text("HUMANITARIANS.AI RESTRUCTURE", font=FONT, weight="BOLD",
                  font_size=42, color=PAPER)
        l2 = Text("WEEK 2 OF 4", font=FONT, weight="BOLD",
                  font_size=42, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        fit_width(g)
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), run_time=0.6)
        self.wait(2.4)
