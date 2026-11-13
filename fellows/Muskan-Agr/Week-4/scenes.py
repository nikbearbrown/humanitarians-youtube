"""scenes.py — Manim scenes for humanitarians-ai-week4-navigation-cleanup-handoff.

WEEK 4 OF 4. Visual system is locked to Weeks 1-3 (see
../humanitarians-ai-week3-stakeholder-strategy-hierarchy/scenes.py): PAPER white ground, INK near-black type, one MAROON
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
  C. Never build a text stack with "" spacer lines. Text("") has zero height,
     arrange() computes its spacing off degenerate geometry, and the real lines
     land on top of each other. That shipped a genuine GATE B failure in Week 3
     (text-on-text at 100% overlap). Group the lines and arrange twice.
  D. Card-like scenes need at least one SHAPE that appears over time, or GATE A
     errors with "shapes never change". Every marked_rows() mark is load-bearing.
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



# ── Measured constants ───────────────────────────────────────────────────
# Projects-column box, measured from 06_footer.jpg by ink-column profiling in
# Week 2 (and correcting Week 1's estimate, which spanned three columns).
FOOTER_PROJECTS_COL = (0.7319, 0.0973, 0.8071, 0.5012)

# Live-site counts, re-measured 2026-09-06. Identical to the Week 2 and Week 3
# measurements: the cleanup is agreed but not yet deployed.
NOW_PROJECTS, AFTER_PROJECTS = 11, 6
NOW_FOOTER_LINKS, AFTER_FOOTER_LINKS = 33, 28
NOW_BARE_NOUNS, AFTER_BARE_NOUNS = 6, 1

REMOVING = ["DEWEY", "MADISON", "MEDHAVY", "MYCROFT", "POPPER"]


def counter_row(label, before, after, lab_size=24, num_size=64):
    """before -> after, with the arrow drawn as a maroon block rather than an
    arrow glyph. No Line() anywhere in this file (GATE B TEXT_ON_CURVE)."""
    b = Text(str(before), font=FONT, weight="BOLD", font_size=num_size, color=SOFT)
    step = Rectangle(width=0.5, height=0.09, color=MAROON, fill_color=MAROON,
                     fill_opacity=1, stroke_width=0)
    a = Text(str(after), font=FONT, weight="BOLD", font_size=num_size, color=MAROON)
    nums = VGroup(b, step, a).arrange(RIGHT, buff=0.35)
    lab = Text(label.upper(), font=FONT, weight="BOLD", font_size=lab_size, color=INK)
    lab.next_to(nums, DOWN, buff=0.25)
    return VGroup(nums, lab)


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
        sub = Text("WEEK 4 — NAVIGATION CLEANUP + HANDOFF", font=FONT,
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
#  B01 — What is still pending
# ═══════════════════════════════════════════════════════════════════════
class B01_MeetingPending(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("STILL PENDING FROM WEEK 3:", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)
        rows = marked_rows(["THE STAKEHOLDER MEETING",
                            "AUDIENCE PRIORITY",
                            "FIRST-IMPRESSION MESSAGING",
                            "SUCCESS METRICS"], size=34, buff=0.34)
        rows.next_to(title, DOWN, buff=0.9)
        tail = Text("WAITING FOR IT WOULD HAVE COST A WEEK.", font=FONT,
                    weight="BOLD", font_size=30, color=MAROON)
        tail.next_to(rows, DOWN, buff=0.85)
        fit_block(title, rows, tail)
        self.play(Write(title), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.12), run_time=0.3)
        self.wait(0.6)
        self.play(FadeIn(tail), run_time=0.45)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B02 — Move the part that isn't blocked
# ═══════════════════════════════════════════════════════════════════════
class B02_MoveWhatIsntBlocked(Scene):
    def construct(self):
        self.camera.background_color = INK
        l1 = Text("MOVE THE PART", font=FONT, weight="BOLD",
                  font_size=62, color=PAPER)
        l2 = Text("THAT ISN'T BLOCKED.", font=FONT, weight="BOLD",
                  font_size=62, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        mark = Square(side_length=0.2, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(g, LEFT, buff=0.5)
        fit_block(mark, g)
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), FadeIn(mark, scale=1.3), run_time=0.8)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B03 — The audit becomes a working document
# ═══════════════════════════════════════════════════════════════════════
class B03_AuditBecomesWorkingDoc(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("ONE QUESTION, ASKED OF EVERY LINK:", font=FONT,
                     weight="BOLD", font_size=38, color=INK).to_edge(UP, buff=0.6)
        fit_width(title)
        q1 = Text("IS THERE A DEFINED PROJECT", font=FONT, weight="BOLD",
                  font_size=54, color=INK)
        q2 = Text("BEHIND THIS?", font=FONT, weight="BOLD",
                  font_size=54, color=MAROON)
        q = VGroup(q1, q2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        q.next_to(title, DOWN, buff=1.0)
        bar = Rectangle(width=0.1, height=q.height, color=MAROON,
                        fill_color=MAROON, fill_opacity=1, stroke_width=0)
        bar.next_to(q, LEFT, buff=0.5)
        tail = Text("THE WEEK 2 AUDIT, USED AS A WORKING DOCUMENT.", font=FONT,
                    weight="BOLD", font_size=26, color=SOFT)
        tail.next_to(q, DOWN, buff=0.9)
        tmark = Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                       fill_opacity=1, stroke_width=0).next_to(tail, LEFT, buff=0.3)
        fit_block(title, bar, q, tail, tmark)
        self.play(Write(title), run_time=0.7)
        self.play(GrowFromEdge(bar, UP), run_time=0.5)
        self.play(Write(q1), run_time=0.7)
        self.play(Write(q2), run_time=0.6)
        self.wait(0.6)
        # Mark lands with the tail: GATE A errors on a scene whose shape state
        # never changes, and one static accent bar is a single shape-state.
        self.play(FadeIn(tail), FadeIn(tmark, scale=1.3), run_time=0.45)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B04 — The footer as it stands today
# ═══════════════════════════════════════════════════════════════════════
class B04_FooterToday(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        self.add(full_frame_image("06_footer.jpg", tag="b04"))
        box = annotate_rect(FOOTER_PROJECTS_COL, sw=9)
        c1 = place_chip("PROJECTS COLUMN: 11 LINKS.", y_frac=0.86, size=32)
        self.play(Create(box), run_time=0.8)
        self.play(FadeIn(c1, shift=UP * 0.1), run_time=0.4)
        self.wait(2.2)
        c2 = place_chip("5 WITH NOTHING BEHIND THEM.", y_frac=0.86, size=32)
        self.play(FadeOut(c1), FadeIn(c2, shift=UP * 0.1), run_time=0.4)
        self.wait(2.4)


# ═══════════════════════════════════════════════════════════════════════
#  B05 — The five names, marked for removal
#  "Removed" is shown with a maroon block and a REMOVING label — never a
#  strikethrough Line(), which GATE B's TEXT_ON_CURVE check errors on.
# ═══════════════════════════════════════════════════════════════════════
class B05_FiveNames(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("SCOPED FOR REMOVAL:", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)
        rows = VGroup()
        for n in REMOVING:
            block = Rectangle(width=0.28, height=0.28, color=MAROON,
                              fill_color=MAROON, fill_opacity=1, stroke_width=0)
            t = Text(n, font=FONT, weight="BOLD", font_size=46, color=SOFT)
            t.next_to(block, RIGHT, buff=0.4)
            rows.add(VGroup(block, t))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        rows.next_to(title, DOWN, buff=0.7)
        tail = Text("FLAGGED IN WEEK 1. COUNTED IN WEEK 3. SCOPED IN WEEK 4.",
                    font=FONT, weight="BOLD", font_size=26, color=MAROON)
        tail.next_to(rows, DOWN, buff=0.7)
        fit_block(title, rows, tail)
        self.play(Write(title), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.12), run_time=0.28)
        self.wait(0.6)
        self.play(FadeIn(tail), run_time=0.5)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B06 — The arithmetic
# ═══════════════════════════════════════════════════════════════════════
class B06_Arithmetic(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("THE ARITHMETIC.", font=FONT, weight="BOLD",
                     font_size=40, color=INK).to_edge(UP, buff=0.6)
        rows = VGroup(
            counter_row("projects column links", NOW_PROJECTS, AFTER_PROJECTS),
            counter_row("footer column links", NOW_FOOTER_LINKS, AFTER_FOOTER_LINKS),
            counter_row("bare proper nouns", NOW_BARE_NOUNS, AFTER_BARE_NOUNS),
        ).arrange(RIGHT, buff=1.3, aligned_edge=UP)
        fit_width(rows)
        rows.next_to(title, DOWN, buff=1.1)
        tail = Text("NO REDESIGN REQUIRED.", font=FONT, weight="BOLD",
                    font_size=34, color=MAROON)
        tail.next_to(rows, DOWN, buff=1.0)
        fit_block(title, rows, tail)
        self.play(Write(title), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.15), run_time=0.45)
        self.wait(0.8)
        self.play(FadeIn(tail), run_time=0.5)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B07 — The cheapest improvement
# ═══════════════════════════════════════════════════════════════════════
class B07_CheapestImprovement(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        l1 = Text("NO NEW LAYOUT.", font=FONT, weight="BOLD",
                  font_size=52, color=INK)
        l2 = Text("NO NEW TYPE. NO NEW COLOUR.", font=FONT, weight="BOLD",
                  font_size=52, color=INK)
        l3 = Text("FIVE FEWER DEAD ENDS.", font=FONT, weight="BOLD",
                  font_size=52, color=MAROON)
        g = VGroup(l1, l2, l3).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        mark = Square(side_length=0.2, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(l3, LEFT, buff=0.4)
        fit_block(g, mark)
        self.play(Write(l1), run_time=0.6)
        self.play(Write(l2), run_time=0.7)
        self.wait(0.4)
        self.play(Write(l3), FadeIn(mark, scale=1.3), run_time=0.7)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B08 — Status, stated precisely
#  Verified against the live site on 2026-09-06: the links are still there.
#  This beat exists so the reel cannot be caught overclaiming.
# ═══════════════════════════════════════════════════════════════════════
class B08_StatusNotDeployed(Scene):
    def construct(self):
        self.camera.background_color = INK
        title = Text("STATUS, PRECISELY:", font=FONT, weight="BOLD",
                     font_size=36, color=SOFT).to_edge(UP, buff=1.0)
        rows = VGroup()
        for label, col in (("DECIDED.", PAPER), ("SPECIFIED.", PAPER),
                           ("NOT YET DEPLOYED.", MAROON)):
            sq = Square(side_length=0.22, color=MAROON, fill_color=MAROON,
                        fill_opacity=1, stroke_width=0)
            t = Text(label, font=FONT, weight="BOLD", font_size=54, color=col)
            t.next_to(sq, RIGHT, buff=0.4)
            rows.add(VGroup(sq, t))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        rows.next_to(title, DOWN, buff=0.8)
        tail = Text("THE OLD LINKS ARE STILL LIVE TODAY.", font=FONT,
                    weight="BOLD", font_size=26, color=SOFT)
        tail.next_to(rows, DOWN, buff=0.8)
        fit_block(title, rows, tail)
        self.play(FadeIn(title), run_time=0.5)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.12), run_time=0.4)
        self.wait(0.6)
        self.play(FadeIn(tail), run_time=0.45)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B09 — The turn to process
# ═══════════════════════════════════════════════════════════════════════
class B09_TurnToProcess(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        l1 = Text("PROCESS", font=FONT, weight="BOLD", font_size=84, color=INK)
        l2 = Text("BEFORE PIXELS.", font=FONT, weight="BOLD", font_size=84, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        sub = Text("AGREE THE HANDOFF BEFORE ANY VISUALS START.", font=FONT,
                   weight="BOLD", font_size=26, color=SOFT)
        sub.next_to(g, DOWN, buff=0.85, aligned_edge=LEFT)
        mark = Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(sub, LEFT, buff=0.3)
        fit_block(g, sub, mark)
        self.play(Write(l1), run_time=0.7)
        self.play(Write(l2), run_time=0.7)
        self.wait(0.4)
        self.play(FadeIn(sub), FadeIn(mark, scale=1.3), run_time=0.45)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B10 — Where handoff friction actually comes from
# ═══════════════════════════════════════════════════════════════════════
class B10_HandoffFriction(Scene):
    def construct(self):
        self.camera.background_color = INK
        l1 = Text("THE ARGUMENT IS RARELY", font=FONT, weight="BOLD",
                  font_size=44, color=SOFT)
        l2 = Text("ABOUT THE DESIGN.", font=FONT, weight="BOLD",
                  font_size=56, color=PAPER)
        l3 = Text("IT'S ABOUT WHAT A FINISHED", font=FONT, weight="BOLD",
                  font_size=44, color=SOFT)
        l4 = Text("HANDOFF LOOKS LIKE.", font=FONT, weight="BOLD",
                  font_size=56, color=MAROON)
        g = VGroup(l1, l2, l3, l4).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        mark = Square(side_length=0.18, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(l4, LEFT, buff=0.35)
        fit_block(g, mark)
        self.play(FadeIn(l1), run_time=0.35)
        self.play(Write(l2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(l3), run_time=0.35)
        self.play(Write(l4), FadeIn(mark, scale=1.3), run_time=0.6)
        self.wait(1.4)


# ═══════════════════════════════════════════════════════════════════════
#  B11 — The question put to the developer
# ═══════════════════════════════════════════════════════════════════════
class B11_TheQuestion(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("ASKED THE DEVELOPER FIRST:", font=FONT, weight="BOLD",
                     font_size=38, color=INK).to_edge(UP, buff=0.6)

        hA = Text("A — FIGMA DEV MODE", font=FONT, weight="BOLD",
                  font_size=30, color=INK)
        rowsA = marked_rows(["INSPECT COMPONENTS", "SPACING VALUES",
                             "STYLE VALUES IN-FILE"], size=25, buff=0.24, mark=0.14)
        rowsA.next_to(hA, DOWN, buff=0.45, aligned_edge=LEFT)
        colA = VGroup(hA, rowsA)

        hB = Text("B — DOCUMENTED HANDOFF", font=FONT, weight="BOLD",
                  font_size=30, color=MAROON)
        rowsB = marked_rows(["WRITTEN SPECS", "COMPONENT STATES",
                             "REQUIREMENTS UP FRONT"], size=25, buff=0.24,
                            mark=0.14, color=MAROON)
        rowsB.next_to(hB, DOWN, buff=0.45, aligned_edge=LEFT)
        colB = VGroup(hB, rowsB)

        cols = VGroup(colA, colB).arrange(RIGHT, buff=1.7, aligned_edge=UP)
        cols.next_to(title, DOWN, buff=0.95)
        tail = Text("HER ANSWER SETS THE FORMAT.", font=FONT, weight="BOLD",
                    font_size=30, color=MAROON)
        tail.next_to(cols, DOWN, buff=0.95)
        fit_block(title, cols, tail)

        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(hA), run_time=0.3)
        for r in rowsA:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.2)
        self.wait(0.3)
        self.play(FadeIn(hB), run_time=0.3)
        for r in rowsB:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.2)
        self.wait(0.5)
        self.play(FadeIn(tail), run_time=0.45)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B12 — Framework, parts one and two
# ═══════════════════════════════════════════════════════════════════════
class B12_FrameworkOneTwo(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("THE COLLABORATION FRAMEWORK.", font=FONT, weight="BOLD",
                     font_size=38, color=INK).to_edge(UP, buff=0.6)
        n1 = Text("01", font=FONT, weight="BOLD", font_size=44, color=MAROON)
        t1 = Text("A SHARED COMPONENT LIBRARY", font=FONT, weight="BOLD",
                  font_size=40, color=INK)
        s1 = Text("MIRRORING THE SITE'S CODED COMPONENTS", font=FONT,
                  weight="BOLD", font_size=24, color=SOFT)
        t1.next_to(n1, RIGHT, buff=0.5)
        s1.next_to(t1, DOWN, buff=0.22, aligned_edge=LEFT)
        one = VGroup(n1, t1, s1)

        n2 = Text("02", font=FONT, weight="BOLD", font_size=44, color=MAROON)
        t2 = Text("DEV MODE ACCESS", font=FONT, weight="BOLD",
                  font_size=40, color=INK)
        s2 = Text("WITH CLEAN, STRUCTURED LAYER NAMING", font=FONT,
                  weight="BOLD", font_size=24, color=SOFT)
        t2.next_to(n2, RIGHT, buff=0.5)
        s2.next_to(t2, DOWN, buff=0.22, aligned_edge=LEFT)
        two = VGroup(n2, t2, s2)

        rows = VGroup(one, two).arrange(DOWN, aligned_edge=LEFT, buff=0.95)
        rows.next_to(title, DOWN, buff=1.0)
        # A maroon rule per part. Without a real SHAPE this scene records none
        # and GATE A warns "text-only"; the rule also anchors each block.
        rules = VGroup(*[
            Rectangle(width=0.1, height=grp.height, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(grp, LEFT, buff=0.45)
            for grp in (one, two)
        ])
        fit_block(title, rows, rules)
        self.play(Write(title), run_time=0.7)
        for grp, rule in zip((one, two), rules):
            self.play(GrowFromEdge(rule, UP), FadeIn(grp[0], scale=1.2), run_time=0.35)
            self.play(FadeIn(grp[1], shift=RIGHT * 0.12), run_time=0.4)
            self.play(FadeIn(grp[2]), run_time=0.3)
            self.wait(0.4)
        self.wait(1.4)


# ═══════════════════════════════════════════════════════════════════════
#  B13 — Why the shared library compounds
# ═══════════════════════════════════════════════════════════════════════
class B13_LibraryCompounds(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        l1 = Text("IF THE FILE MIRRORS", font=FONT, weight="BOLD",
                  font_size=50, color=INK)
        l2 = Text("WHAT IS ACTUALLY CODED,", font=FONT, weight="BOLD",
                  font_size=50, color=INK)
        l3 = Text("THE GAP STOPS WIDENING.", font=FONT, weight="BOLD",
                  font_size=50, color=MAROON)
        g = VGroup(l1, l2, l3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        bar = Rectangle(width=0.1, height=g.height, color=MAROON,
                        fill_color=MAROON, fill_opacity=1, stroke_width=0)
        bar.next_to(g, LEFT, buff=0.5)
        mark = Square(side_length=0.2, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(l3, LEFT, buff=0.35)
        fit_block(bar, g, mark)
        self.play(GrowFromEdge(bar, UP), run_time=0.5)
        self.play(Write(l1), run_time=0.6)
        self.play(Write(l2), run_time=0.6)
        self.wait(0.4)
        self.play(Write(l3), FadeIn(mark, scale=1.3), run_time=0.7)
        self.wait(1.8)


# ═══════════════════════════════════════════════════════════════════════
#  B14 — Framework, parts three and four
# ═══════════════════════════════════════════════════════════════════════
class B14_FrameworkThreeFour(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("THE COLLABORATION FRAMEWORK.", font=FONT, weight="BOLD",
                     font_size=38, color=INK).to_edge(UP, buff=0.6)
        n3 = Text("03", font=FONT, weight="BOLD", font_size=44, color=MAROON)
        t3 = Text("A SPEC FOR INTERACTION STATES", font=FONT, weight="BOLD",
                  font_size=40, color=INK)
        s3 = Text("HOVER, FOCUS, ACTIVE, MOBILE COLLAPSED", font=FONT,
                  weight="BOLD", font_size=24, color=SOFT)
        t3.next_to(n3, RIGHT, buff=0.5)
        s3.next_to(t3, DOWN, buff=0.22, aligned_edge=LEFT)
        three = VGroup(n3, t3, s3)

        n4 = Text("04", font=FONT, weight="BOLD", font_size=44, color=MAROON)
        t4 = Text("AGREED BREAKPOINTS", font=FONT, weight="BOLD",
                  font_size=40, color=INK)
        s4 = Text("MOBILE, TABLET, DESKTOP — DECIDED ONCE", font=FONT,
                  weight="BOLD", font_size=24, color=SOFT)
        t4.next_to(n4, RIGHT, buff=0.5)
        s4.next_to(t4, DOWN, buff=0.22, aligned_edge=LEFT)
        four = VGroup(n4, t4, s4)

        rows = VGroup(three, four).arrange(DOWN, aligned_edge=LEFT, buff=0.95)
        rows.next_to(title, DOWN, buff=1.0)
        rules = VGroup(*[
            Rectangle(width=0.1, height=grp.height, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(grp, LEFT, buff=0.45)
            for grp in (three, four)
        ])
        fit_block(title, rows, rules)
        self.play(Write(title), run_time=0.7)
        for grp, rule in zip((three, four), rules):
            self.play(GrowFromEdge(rule, UP), FadeIn(grp[0], scale=1.2), run_time=0.35)
            self.play(FadeIn(grp[1], shift=RIGHT * 0.12), run_time=0.4)
            self.play(FadeIn(grp[2]), run_time=0.3)
            self.wait(0.4)
        self.wait(1.2)


# ═══════════════════════════════════════════════════════════════════════
#  B15 — The interaction-state gap
# ═══════════════════════════════════════════════════════════════════════
class B15_InteractionStates(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("A FILE SHOWS ONE STATE.", font=FONT, weight="BOLD",
                     font_size=40, color=SOFT).to_edge(UP, buff=0.6)
        sub = Text("A BROWSER HAS TO SHOW FOUR.", font=FONT, weight="BOLD",
                   font_size=44, color=INK)
        sub.next_to(title, DOWN, buff=0.4)
        chips = VGroup(*[chip(t, size=30) for t in
                         ("HOVER", "FOCUS", "ACTIVE", "COLLAPSED")])
        chips.arrange(RIGHT, buff=0.5)
        fit_width(chips)
        chips.next_to(sub, DOWN, buff=1.0)
        tail = Text("WHAT ISN'T SPECIFIED GETS INVENTED AT BUILD TIME.",
                    font=FONT, weight="BOLD", font_size=26, color=MAROON)
        tail.next_to(chips, DOWN, buff=0.95)
        fit_block(title, sub, chips, tail)
        self.play(FadeIn(title), run_time=0.4)
        self.play(Write(sub), run_time=0.7)
        for c in chips:
            self.play(FadeIn(c, shift=UP * 0.12), run_time=0.28)
        self.wait(0.6)
        self.play(FadeIn(tail), run_time=0.45)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B16 — Staged rollout
# ═══════════════════════════════════════════════════════════════════════
class B16_Rollout(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        title = Text("A STAGED ROLLOUT, WRITTEN DOWN.", font=FONT,
                     weight="BOLD", font_size=38, color=INK).to_edge(UP, buff=0.6)
        rows = marked_rows(["TECHNICAL FEASIBILITY MAPPED",
                            "PHASE-BY-PHASE ROADMAP",
                            "AN ORDER, NOT A WISH LIST"], size=36, buff=0.4)
        rows.next_to(title, DOWN, buff=1.0)
        fit_block(title, rows)
        self.play(Write(title), run_time=0.7)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.14), run_time=0.42)
        self.wait(2.0)


# ═══════════════════════════════════════════════════════════════════════
#  B17 — The four-week arc, complete
# ═══════════════════════════════════════════════════════════════════════
class B17_FourWeekArc(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        rows = VGroup()
        for num, label in (("WEEK 1", "THE AUDIT"),
                           ("WEEK 2", "THE SPECIFICATION"),
                           ("WEEK 3", "THE QUESTIONS"),
                           ("WEEK 4", "THE WORKING AGREEMENT")):
            n = Text(num, font=FONT, weight="BOLD", font_size=34, color=MAROON)
            t = Text(label, font=FONT, weight="BOLD", font_size=34, color=INK)
            t.next_to(n, RIGHT, buff=0.6)
            rows.add(VGroup(n, t))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        bar = Rectangle(width=0.1, height=rows.height, color=MAROON,
                        fill_color=MAROON, fill_opacity=1, stroke_width=0)
        bar.next_to(rows, LEFT, buff=0.5)
        tail = Text("THE SITE DOESN'T LOOK DIFFERENT YET.", font=FONT,
                    weight="BOLD", font_size=28, color=SOFT)
        tail.next_to(rows, DOWN, buff=0.9, aligned_edge=LEFT)
        fit_block(bar, rows, tail)
        self.play(GrowFromEdge(bar, UP), run_time=0.5)
        for r in rows:
            tick = Square(side_length=0.12, color=MAROON, fill_color=MAROON,
                          fill_opacity=1, stroke_width=0).next_to(r, LEFT, buff=0.22)
            self.play(FadeIn(r, shift=RIGHT * 0.15), FadeIn(tick), run_time=0.42)
        self.wait(0.6)
        self.play(FadeIn(tail), run_time=0.45)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B18 — What remains open
# ═══════════════════════════════════════════════════════════════════════
class B18_StillOpen(Scene):
    def construct(self):
        self.camera.background_color = INK
        l1 = Text("STILL OPEN:", font=FONT, weight="BOLD",
                  font_size=42, color=SOFT)
        l2 = Text("THE STAKEHOLDER MEETING,", font=FONT, weight="BOLD",
                  font_size=52, color=PAPER)
        l3 = Text("AND THE ANSWERS IT OWES.", font=FONT, weight="BOLD",
                  font_size=52, color=MAROON)
        g = VGroup(l1, l2, l3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        mark = Square(side_length=0.2, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(l3, LEFT, buff=0.4)
        fit_block(g, mark)
        self.play(FadeIn(l1), run_time=0.4)
        self.play(Write(l2), run_time=0.7)
        self.play(Write(l3), FadeIn(mark, scale=1.3), run_time=0.7)
        self.wait(1.6)


# ═══════════════════════════════════════════════════════════════════════
#  B19 — End card
# ═══════════════════════════════════════════════════════════════════════
class B19_EndCard(Scene):
    def construct(self):
        self.camera.background_color = INK
        l1 = Text("HUMANITARIANS.AI RESTRUCTURE", font=FONT, weight="BOLD",
                  font_size=42, color=PAPER)
        l2 = Text("WEEK 4 OF 4", font=FONT, weight="BOLD",
                  font_size=42, color=MAROON)
        g = VGroup(l1, l2).arrange(DOWN, buff=0.35)
        mark = Square(side_length=0.16, color=MAROON, fill_color=MAROON,
                      fill_opacity=1, stroke_width=0).next_to(g, DOWN, buff=0.5)
        fit_block(g, mark)
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), FadeIn(mark, scale=1.3), run_time=0.7)
        self.wait(2.2)
