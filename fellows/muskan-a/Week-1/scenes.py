"""scenes.py — Manim scenes for humanitarians-ai-week1-diagnostic-audit.

WHY MANIM FOR EVERYTHING (including the "plain screenshot" beats):
This toolkit's own docs (skills/make/explainer/REMOTION.md) mark the
Remotion word-keyed annotation plane — the thing that would normally draw
the red boxes/arrows/underlines over a screenshot — as "spec v1, not yet
built." Rather than reference a feature that doesn't exist in this checkout,
every beat in this reel (plain full-bleed screenshots, annotated screenshots,
and text cards) is a real, renders-today Manim scene. This is the documented
fallback: run.sh itself says "write scenes.py, one Scene per beat" when a
reel has GRAPHIC beats.

Palette — sampled directly from the supplied screenshots (see BUILD-LOG.md
for the exact pixel coordinates used), NOT the toolkit's default "claude"
cream preset. This matches the brief: black type, white ground, one maroon
accent, no gradients, no shadows, no rounded corners.

  PAPER  #FFFFFF   the site's white ground
  INK    #111111   near-black type (the site never uses pure #000 body text)
  MAROON #64140E   sampled from the Donate/YouTube button pixels in
                   01_hero_section.jpg (average of 3 sample points)
  SOFT   #555555   secondary/caption-weight text only — never the only
                   signal (WCAG contrast gate)

Font: Oswald (bold, condensed, all-caps friendly) — already fetched by this
toolkit's own `./setup --install` step, so it's on the machine that renders
this. Falls back to Arial/Helvetica/Liberation Sans if Oswald isn't found;
Pango will substitute silently, so double check overlay type in the first
`./art run` previz.

Beat-id-prefixed class names (B00_Intro, B01_HeroFullBleed, ...) are what
run.sh's regex looks for to route each scene to its slot.
"""
from manim import *
from pathlib import Path
from PIL import Image
import hashlib
import numpy as np

# ── Palette ──────────────────────────────────────────────────────────────
PAPER  = ManimColor("#FFFFFF")
INK    = ManimColor("#111111")
MAROON = ManimColor("#64140E")
SOFT   = ManimColor("#555555")

FONT = "Oswald"          # all-caps overlay / kicker type
BODY_FONT = "Arial"      # only used for the tiny "Learn more" style captions

ASSETS = Path(__file__).parent / "assets"
CACHE = Path(__file__).parent / "manim" / ".cache"
CACHE.mkdir(parents=True, exist_ok=True)


# ── Image helpers ────────────────────────────────────────────────────────
def _cache_path(src: Path, box, tag: str) -> Path:
    key = f"{src.name}-{box}-{tag}".encode()
    h = hashlib.sha1(key).hexdigest()[:10]
    return CACHE / f"{src.stem}-{h}.png"


def cover_crop_169(src_name: str, box=(0.0, 0.0, 1.0, 1.0), tag="full") -> Path:
    """Crop `box` (normalized x0,y0,x1,y1 in the ORIGINAL screenshot) out of
    the source image, then center-crop that region to exactly a 16:9 ratio
    (trims width, since every source shot here is slightly wider than
    16:9 — full height is always preserved, so no UI content near the top
    or bottom is lost). Returns a cached path; safe to call every render,
    only regenerates when the source file changes (mtime is not checked —
    delete manim/.cache/ if you swap a screenshot for a new export).

    Falls back to a labeled gray placeholder if the source file is missing
    — this happens deliberately during run.sh's GATE A pre-flight, which
    copies scenes.py alone into an isolated temp folder (no assets/ beside
    it) to keep the check fast and render-free. The REAL render always
    runs from the actual reel directory, where assets/ is present, so this
    fallback never fires there. If you ever see a placeholder in an actual
    rendered clip (not the pre-flight check), the asset filename is wrong —
    check assets/ against SHOTLIST.md."""
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
            d = ImageDraw.Draw(im)
            d.text((40, h // 2 - 10), f"MISSING ASSET: {src_name}", fill=(80, 80, 80))
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
        left = (rw - new_w) // 2
        region = region.crop((left, 0, left + new_w, rh))
    elif rw / rh < target_ratio:
        new_h = int(rw / target_ratio)
        top = (rh - new_h) // 2
        region = region.crop((0, top, rw, top + new_h))
    region.save(out)
    return out


def full_frame_image(src_name: str, box=(0.0, 0.0, 1.0, 1.0), tag="full") -> ImageMobject:
    """A screenshot (or a sub-region of one), cropped to 16:9 and scaled to
    fill the render frame exactly — the 'full-bleed hard crop' the brief
    asks for. No border, no drop shadow, no rounded corner."""
    path = cover_crop_169(src_name, box, tag)
    mob = ImageMobject(str(path))
    mob.stretch_to_fit_height(config.frame_height)
    mob.stretch_to_fit_width(config.frame_width)
    mob.move_to(ORIGIN)
    return mob


SRC_ASPECT = 1503 / 812  # all six screenshots share this exact resolution


def rect_in_image(box, image_box=(0.0, 0.0, 1.0, 1.0), src_aspect=SRC_ASPECT):
    """Map a normalized rectangle `box` (x0,y0,x1,y1 in ORIGINAL screenshot
    coords, y-down) onto scene coordinates, accounting for the crop-to-16:9
    transform `full_frame_image` applied when displaying `image_box`. Used
    to place the red annotation rectangle/ellipse/arrow precisely over the
    real button/element it's calling out, instead of eyeballing it.

    `src_aspect` is the ORIGINAL image's real pixel aspect ratio (width/
    height) — needed because a normalized region tuple like (0,0,1,1) is
    always ~square in fraction-space regardless of the image's actual
    pixel shape; using the box's own fractional aspect here (an earlier,
    wrong version of this function did that) silently computes the wrong
    crop and can push annotations off-frame."""
    ix0, iy0, ix1, iy1 = image_box
    iw, ih = ix1 - ix0, iy1 - iy0
    bx0, by0, bx1, by1 = box
    rel_x0, rel_x1 = (bx0 - ix0) / iw, (bx1 - ix0) / iw
    rel_y0, rel_y1 = (by0 - iy0) / ih, (by1 - iy0) / ih
    # real pixel aspect ratio of the displayed region (image_box), scaled
    # from the source image's aspect by how much width/height it spans
    region_aspect = src_aspect * (iw / ih) if ih else src_aspect
    target_ratio = 16 / 9
    if region_aspect > target_ratio:
        keep = target_ratio / region_aspect
        pad = (1 - keep) / 2
        rel_x0 = (rel_x0 - pad) / keep
        rel_x1 = (rel_x1 - pad) / keep
    elif region_aspect < target_ratio:
        keep = region_aspect / target_ratio
        pad = (1 - keep) / 2
        rel_y0 = (rel_y0 - pad) / keep
        rel_y1 = (rel_y1 - pad) / keep
    x0 = (rel_x0 - 0.5) * config.frame_width
    x1 = (rel_x1 - 0.5) * config.frame_width
    y0 = (0.5 - rel_y0) * config.frame_height
    y1 = (0.5 - rel_y1) * config.frame_height
    return x0, y1, x1, y0  # left, bottom, right, top


def annotate_rect(box, image_box=(0.0, 0.0, 1.0, 1.0), color=MAROON, sw=10):
    l, b, r, t = rect_in_image(box, image_box)
    rect = Rectangle(width=r - l, height=t - b, color=color, stroke_width=sw, fill_opacity=0)
    rect.move_to([(l + r) / 2, (b + t) / 2, 0])
    return rect


def annotate_ellipse(box, image_box=(0.0, 0.0, 1.0, 1.0), color=MAROON, sw=12):
    l, b, r, t = rect_in_image(box, image_box)
    ell = Ellipse(width=(r - l) * 1.12, height=(t - b) * 0.9, color=color, stroke_width=sw, fill_opacity=0)
    ell.move_to([(l + r) / 2, (b + t) / 2, 0])
    return ell


# ── Text helpers ─────────────────────────────────────────────────────────
def kicker(text, color=PAPER, size=52):
    return Text(text.upper(), font=FONT, weight="BOLD", font_size=size, color=color)


def chip(text, color=PAPER, bg=MAROON, size=34):
    label = Text(text.upper(), font=FONT, weight="BOLD", font_size=size, color=color)
    pad_x, pad_y = 0.35, 0.22
    bgrect = Rectangle(width=label.width + pad_x * 2, height=label.height + pad_y * 2,
                        color=bg, fill_color=bg, fill_opacity=1, stroke_width=0)
    bgrect.move_to(label.get_center())
    return VGroup(bgrect, label)


def bottom_bar_chip(text, y_frac=0.83, **kw):
    """Overlay chip anchored to the lower band of the frame — where the
    brief's overlay type sits (never on top of a face/button it needs you
    to read)."""
    c = chip(text, **kw)
    c.move_to([0, (0.5 - y_frac) * config.frame_height, 0])
    return c


def top_bar_chip(text, y_frac=0.13, **kw):
    c = chip(text, **kw)
    c.move_to([0, (0.5 - y_frac) * config.frame_height, 0])
    return c


SAFE_BUFF = 0.6  # keep text this far inside the frame edge (Manim units)


# ═══════════════════════════════════════════════════════════════════════
#  B00 — INTRO (Muskan Agrawal, on camera-voice, cold open)
# ═══════════════════════════════════════════════════════════════════════
class B00_Intro(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        name = kicker("Muskan Agrawal", color=INK, size=64)
        rule = Rectangle(width=name.width, height=0.06, color=MAROON,
                          fill_color=MAROON, fill_opacity=1, stroke_width=0)
        rule.next_to(name, DOWN, buff=0.35)
        sub = Text("WEEK 1 — DIAGNOSTIC AUDIT", font=FONT, weight="BOLD",
                    font_size=34, color=MAROON).next_to(rule, DOWN, buff=0.45)
        tag = Text("HUMANITARIANS.AI RESTRUCTURE", font=FONT, weight="BOLD",
                    font_size=24, color=SOFT).next_to(sub, DOWN, buff=0.6)
        mark = Square(side_length=0.14, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(tag, LEFT, buff=0.25)
        self.play(Write(name), run_time=0.9)
        self.play(GrowFromCenter(rule), run_time=0.4)
        self.play(FadeIn(sub, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(tag), FadeIn(mark), run_time=0.5)
        self.wait(2.2)


# ═══════════════════════════════════════════════════════════════════════
#  B01 — Full-bleed hero, "WEEK 1." kicker
# ═══════════════════════════════════════════════════════════════════════
class B01_HeroFullBleed(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        img = full_frame_image("01_hero_section.jpg", tag="b01")
        self.add(img)
        label = top_bar_chip("WEEK 1.", y_frac=0.13)
        self.play(FadeIn(label, shift=DOWN * 0.1), run_time=0.5)
        self.wait(3.0)


# ═══════════════════════════════════════════════════════════════════════
#  B02 — Black card: GOAL
# ═══════════════════════════════════════════════════════════════════════
class B02_GoalCard(Scene):
    def construct(self):
        self.camera.background_color = INK
        line1 = Text("GOAL:", font=FONT, weight="BOLD", font_size=58, color=PAPER)
        line2 = Text("DIAGNOSE BEFORE YOU DESIGN.", font=FONT, weight="BOLD",
                      font_size=58, color=MAROON)
        group = VGroup(line1, line2).arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(ORIGIN)
        if group.width > config.frame_width - 2 * SAFE_BUFF:
            group.scale_to_fit_width(config.frame_width - 2 * SAFE_BUFF)
        self.play(Write(line1), run_time=0.6)
        self.play(Write(line2), run_time=0.9)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B03 — Hero, annotated: heuristic audit vs. original ask
#  Red box: About Us / Contact Us buttons.  Red arrow: the Donate button
#  (the only donate CTA visible in this frame — see BUILD-LOG.md).
# ═══════════════════════════════════════════════════════════════════════
class B03_HeroAnnotated(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        img = full_frame_image("01_hero_section.jpg", tag="b03")
        self.add(img)

        # measured from the source screenshot (see BUILD-LOG.md)
        about_contact_box = (0.0725, 0.762, 0.261, 0.812)
        donate_box = (0.811, 0.016, 0.888, 0.065)

        box = annotate_rect(about_contact_box, color=MAROON, sw=10)
        l, b, r, t = rect_in_image(donate_box)
        arrow_tip = np.array([(l + r) / 2, t + 0.15, 0])
        arrow_tail = arrow_tip + DOWN * 1.6 + LEFT * 0.3
        arrow = Arrow(arrow_tail, arrow_tip, color=MAROON, stroke_width=10,
                      buff=0, tip_length=0.35, max_tip_length_to_length_ratio=0.5)

        self.play(Create(box), run_time=0.8)
        self.wait(0.3)
        self.play(GrowArrow(arrow), run_time=0.7)
        self.wait(0.5)

        c1 = bottom_bar_chip("HEURISTIC AUDIT.", y_frac=0.83)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.4)
        self.wait(1.4)
        c2 = bottom_bar_chip("COMPETITIVE BENCHMARK.", y_frac=0.83)
        self.play(FadeOut(c1), FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        self.wait(1.4)
        c3 = bottom_bar_chip("ASSUMPTION: REBUILD. STATUS: UNVERIFIED.", y_frac=0.83, size=28)
        self.play(FadeOut(c2), FadeIn(c3, shift=UP * 0.1), run_time=0.4)
        self.wait(2.0)


# ═══════════════════════════════════════════════════════════════════════
#  B04 — Tier framework screenshot, full-bleed
# ═══════════════════════════════════════════════════════════════════════
class B04_TierFramework(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        img = full_frame_image("02_tier_framework.jpg", tag="b04")
        self.add(img)
        self.wait(4.2)


# ═══════════════════════════════════════════════════════════════════════
#  B05 — Program cards screenshot + hierarchy verdict chips
# ═══════════════════════════════════════════════════════════════════════
class B05_ProgramCards(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        img = full_frame_image("03_program_cards.jpg", tag="b05")
        self.add(img)
        c1 = top_bar_chip("SIX CONCEPTS BEFORE ONE ASK.", y_frac=0.13, size=30)
        self.play(FadeIn(c1), run_time=0.5)
        self.wait(1.6)
        c2 = top_bar_chip("HIERARCHY, NOT CONTENT.", y_frac=0.13, size=30)
        self.play(FadeOut(c1), FadeIn(c2), run_time=0.4)
        self.wait(2.2)


# ═══════════════════════════════════════════════════════════════════════
#  B06 — Footer, zoomed on the Projects column
# ═══════════════════════════════════════════════════════════════════════
class B06_FooterZoom(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # approximate Projects-column region of the footer capture —
        # widen/shift this box in BUILD-LOG.md's noted follow-up if the
        # first previz shows it off by a column.
        box = (0.62, 0.0, 0.92, 0.55)
        img = full_frame_image("06_footer.jpg", box=box, tag="b06")
        self.add(img)
        self.wait(1.0)
        c1 = bottom_bar_chip("8 UNLABELED LINKS. 0 CONTEXT.", y_frac=0.83, size=30)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.5)
        self.wait(3.6)


# ═══════════════════════════════════════════════════════════════════════
#  B07 — Typography audit: three crops, one weight problem
# ═══════════════════════════════════════════════════════════════════════
class B07_TypographyCompare(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # three representative crops: hero headline, a card header, body copy
        hero_crop = cover_crop_169("01_hero_section.jpg", box=(0.06, 0.19, 0.40, 0.45), tag="b07h")
        card_crop = cover_crop_169("03_program_cards.jpg", box=(0.05, 0.28, 0.30, 0.42), tag="b07c")
        body_crop = cover_crop_169("01_hero_section.jpg", box=(0.06, 0.30, 0.36, 0.58), tag="b07b")

        panels = Group(*[ImageMobject(str(p)) for p in (hero_crop, card_crop, body_crop)])
        for p in panels:
            p.scale_to_fit_width((config.frame_width - 2 * SAFE_BUFF - 1.0) / 3)
        panels.arrange(RIGHT, buff=0.5).move_to(ORIGIN).shift(UP * 0.2)

        labels = VGroup(*[
            Text(t, font=FONT, weight="BOLD", font_size=24, color=SOFT)
            for t in ("PAGE TITLE", "CARD LABEL", "BODY COPY")
        ])
        for lbl, p in zip(labels, panels):
            lbl.next_to(p, DOWN, buff=0.25)

        self.play(FadeIn(panels), run_time=0.8)
        self.play(*[Write(l) for l in labels], run_time=0.8)
        self.wait(2.4)

        verdict_text = Text("ONE WEIGHT. EVERY LEVEL.", font=FONT, weight="BOLD",
                             font_size=40, color=MAROON)
        mark_left = Text("[", font=FONT, weight="BOLD", font_size=44, color=MAROON)
        mark_right = Text("]", font=FONT, weight="BOLD", font_size=44, color=MAROON)
        mark_left.next_to(verdict_text, LEFT, buff=0.3)
        mark_right.next_to(verdict_text, RIGHT, buff=0.3)
        verdict = VGroup(mark_left, verdict_text, mark_right).move_to(DOWN * 2.6)
        flag = Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(mark_right, RIGHT, buff=0.3)
        self.play(FadeIn(verdict_text), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(mark_left, shift=RIGHT * 0.1), FadeIn(mark_right, shift=LEFT * 0.1),
                   FadeIn(flag, scale=1.4), run_time=0.4)
        self.wait(2.0)


# ═══════════════════════════════════════════════════════════════════════
#  B08 — Proposed 4-step type scale, built rung by rung (nopunt: a ladder
#  → animate as a ladder → Manim, never a text card)
# ═══════════════════════════════════════════════════════════════════════
class B08_TypeScaleLadder(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("PROPOSED: A CLEAR 4-STEP TYPE SCALE.", font=FONT, weight="BOLD",
                      font_size=40, color=INK).to_edge(UP, buff=SAFE_BUFF)
        self.play(Write(title), run_time=0.8)

        rungs = [("DISPLAY", 64), ("HEADLINE", 46), ("SUBHEAD", 32), ("BODY", 22)]
        group = VGroup()
        for label, size in rungs:
            t = Text(label, font=FONT, weight="BOLD", font_size=size * 1.6, color=INK)
            group.add(t)
        group.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        group.next_to(title, DOWN, buff=0.9).align_to(title, LEFT).shift(RIGHT * 0.3)

        accent = Rectangle(width=0.12, height=group.height, color=MAROON,
                            fill_color=MAROON, fill_opacity=1, stroke_width=0)
        accent.next_to(group, LEFT, buff=0.4)

        self.play(GrowFromEdge(accent, UP), run_time=0.5)
        for t in group:
            tick = Square(side_length=0.1, color=MAROON, fill_color=MAROON,
                          fill_opacity=1, stroke_width=0).next_to(t, LEFT, buff=0.2)
            self.play(FadeIn(t, shift=RIGHT * 0.2), FadeIn(tick), run_time=0.45)
        self.wait(2.6)


# ═══════════════════════════════════════════════════════════════════════
#  B09 — Hero rework: red circle on the video embed, media-first vs.
#  message-first
# ═══════════════════════════════════════════════════════════════════════
class B09_HeroReworkAnnotated(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        img = full_frame_image("01_hero_section.jpg", tag="b09")
        self.add(img)

        video_box = (0.300, 0.219, 0.927, 0.799)  # measured, see BUILD-LOG.md
        ring = annotate_ellipse(video_box, color=MAROON, sw=12)
        self.play(Create(ring), run_time=1.0)
        self.wait(0.5)

        c1 = bottom_bar_chip("CURRENT: MEDIA FIRST.", y_frac=0.83, size=30)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.5)
        self.wait(1.8)
        c2 = bottom_bar_chip("DIRECTION: MESSAGE FIRST.", y_frac=0.83, size=30)
        self.play(FadeOut(c1), FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.4)


# ═══════════════════════════════════════════════════════════════════════
#  B10 — The pivot, part 1: Plan A (crossed out)
# ═══════════════════════════════════════════════════════════════════════
class B10_PivotPlanA(Scene):
    def construct(self):
        self.camera.background_color = INK
        text = Text("PLAN A: REBUILD EVERYTHING.", font=FONT, weight="BOLD",
                     font_size=48, color=PAPER).move_to(UP * 0.6)
        self.play(Write(text), run_time=0.9)
        self.wait(0.6)
        reject_mark = Square(side_length=0.22, color=MAROON, fill_color=MAROON,
                              fill_opacity=1, stroke_width=0)
        reject_mark.next_to(text, LEFT, buff=0.4)
        reject_label = Text("REJECTED", font=FONT, weight="BOLD",
                             font_size=22, color=MAROON).next_to(text, DOWN, buff=0.5)
        self.play(FadeIn(reject_mark, scale=1.3), FadeIn(reject_label), run_time=0.5)
        self.wait(2.2)


# ═══════════════════════════════════════════════════════════════════════
#  B11 — The pivot, part 2: Plan B (the resolution)
# ═══════════════════════════════════════════════════════════════════════
class B11_PivotPlanB(Scene):
    def construct(self):
        self.camera.background_color = INK
        text = Text("PLAN B: FIX WHAT'S BROKEN.", font=FONT, weight="BOLD",
                     font_size=48, color=PAPER).move_to(UP * 0.3)
        text2 = Text("REASSESS LATER.", font=FONT, weight="BOLD",
                      font_size=48, color=MAROON).next_to(text, DOWN, buff=0.35)
        self.play(Write(text), run_time=0.8)
        self.play(Write(text2), run_time=0.7)
        self.wait(2.6)


# ═══════════════════════════════════════════════════════════════════════
#  B12 — Close: Week 2 handoff
# ═══════════════════════════════════════════════════════════════════════
class B12_Close(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        line1 = Text("WEEK 1 WAS THE AUDIT.", font=FONT, weight="BOLD",
                      font_size=52, color=INK)
        line2 = Text("WEEK 2 IS THE FIX.", font=FONT, weight="BOLD",
                      font_size=52, color=MAROON)
        group = VGroup(line1, line2).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(UP * 0.4)
        self.play(Write(line1), run_time=0.8)
        self.play(Write(line2), run_time=0.7)
        self.wait(1.0)
        tag = Text("NEXT: WEEK 2, NAVIGATION AND HERO.", font=FONT, weight="BOLD",
                    font_size=28, color=SOFT).next_to(group, DOWN, buff=0.8)
        self.play(FadeIn(tag), run_time=0.5)
        self.wait(2.2)


# ═══════════════════════════════════════════════════════════════════════
#  B13 — End card
# ═══════════════════════════════════════════════════════════════════════
class B13_EndCard(Scene):
    def construct(self):
        self.camera.background_color = INK
        line1 = Text("HUMANITARIANS.AI RESTRUCTURE", font=FONT, weight="BOLD",
                      font_size=42, color=PAPER)
        line2 = Text("WEEK 1 OF 4", font=FONT, weight="BOLD",
                      font_size=42, color=MAROON)
        group = VGroup(line1, line2).arrange(DOWN, buff=0.35).move_to(ORIGIN)
        self.play(Write(line1), run_time=0.8)
        self.play(Write(line2), run_time=0.6)
        self.wait(2.6)
