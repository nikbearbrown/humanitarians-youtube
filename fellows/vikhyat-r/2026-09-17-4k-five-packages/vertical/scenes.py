"""scenes.py — PORTRAIT Manim scenes for hai-4k-five-packages-vertical.

Rendered by run.sh at -r 2160,3840. Manim does NOT derive a portrait frame from
a portrait pixel canvas — it keeps frame_width at 14.2222 and frame_height at
8.0 regardless, which scales the two axes by different amounts. The frame is
forced to 4.5 x 8.0 below; measured, not assumed. At that frame the portrait
canvas is a THIRD the width of the landscape one at the same height, while text
keeps its absolute size.

That is why this is a separate file rather than the landscape scenes re-rendered
at a different resolution. Every side-by-side arrangement in the landscape cut
(B01's number/source columns, B03 and B04's paired cards, B06's three-box chain,
B07's two folders) is re-laid-out as a vertical stack here. Nothing is cropped
and nothing is squeezed.

Safe area, as Gate B actually reports it for this frame:
  x in [-1.95, 1.95],  y in [-3.4, 3.4].

Class names match the parent beat sheet's shot.manim.scene_class so run.sh
resolves each beat to its portrait scene.
"""
from manim import *

# ── PORTRAIT FRAME — load-bearing, do not remove ─────────────────────────────
# Manim does NOT derive a narrow frame from a portrait pixel canvas. At
# -r 2160,3840 it leaves frame_width at its 14.2222 default and keeps
# frame_height at 8.0, which maps 14.2222 units onto 2160px horizontally and
# 8.0 units onto 3840px vertically — a non-uniform scale that distorts every
# shape and leaves the content in a small central band.
# Forcing 4.5 x 8.0 gives square pixels (480 px/unit both axes) and the
# 9:16 frame these scenes are actually composed for.
config.frame_width = 4.5
config.frame_height = 8.0

# ── Humanitarians palette (identical to the landscape cut) ───────────────────
BG      = ManimColor("#F3EBDD")
INK     = ManimColor("#2F2A26")
TEAL    = ManimColor("#1F4E5F")
CRIMSON = ManimColor("#E4572E")
SLATE   = ManimColor("#29335C")
SOFT    = ManimColor("#6E675E")
GHOST   = ManimColor("#B6AE9F")

SAFE_X = 1.95   # measured from Gate B's portrait report, not assumed


def _t(text, size=20, color=None, weight=None, lead=0.85):
    kw = {"font_size": size, "color": color or INK, "line_spacing": lead}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


def _cite(text, size=14, lead=0.8):
    return Text(text, font_size=size, color=SOFT, line_spacing=lead)


def _title(text, size=27):
    """Titles wrap by hand — Manim Text never wraps on its own."""
    return _t(text, size=size, weight="BOLD").to_edge(UP, buff=0.65)


def _card(w, h, stroke=INK, width=1.6):
    # outline only, same reasoning as the landscape cut: a white fill on cream
    # collapses Gate V's ink-vs-background separation
    return Rectangle(width=w, height=h, color=stroke,
                     stroke_width=width, fill_opacity=0.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B01 — four numbers, stacked. Landscape put source text beside the number;
#  at 4.5 units wide it sits underneath instead.
# ─────────────────────────────────────────────────────────────────────────────
class B01_FourNumbers(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("One question.\nFour answers.")
        self.play(Write(title), run_time=0.9)

        q = _t("What height does a\nfinal master use?", size=18, color=SLATE)
        q.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(q, shift=UP * 0.15), run_time=0.7)

        rows = [
            ("2160", "the final command", TEAL),
            ("1080", "a skill guide", CRIMSON),
            ("720",  "the built-in fallback", CRIMSON),
            ("1920", "the vertical helper", CRIMSON),
        ]
        y0 = 0.7
        for i, (num, src, col) in enumerate(rows):
            y = y0 - i * 1.02
            n = _t(num, size=34, color=col, weight="BOLD")
            n.move_to(LEFT * 1.0 + UP * y)
            s = _cite(src, size=14)
            s.move_to(RIGHT * 0.62 + UP * y)
            rule = Line(LEFT * 1.85 + UP * (y - 0.44),
                        RIGHT * 1.85 + UP * (y - 0.44),
                        stroke_width=0.8, color=GHOST)
            self.play(FadeIn(n, shift=RIGHT * 0.2), FadeIn(s), run_time=0.5)
            self.play(Create(rule), run_time=0.22)

        self.wait(1.6)
        note = _t("One of the four is\nthe stated target.", size=17, color=SLATE)
        note.move_to(DOWN * 3.0)
        self.play(FadeIn(note, shift=UP * 0.15), run_time=0.8)
        self.wait(2.2)


# ─────────────────────────────────────────────────────────────────────────────
#  B02 — the three positions as a VERTICAL spine (horizontal in landscape).
# ─────────────────────────────────────────────────────────────────────────────
class B02_ThreePositions(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Three places a\ncheck can sit")
        self.play(Write(title), run_time=0.9)

        spine = Line(UP * 1.55, DOWN * 2.1, stroke_width=2.2, color=INK)
        spine.shift(LEFT * 1.55)
        self.play(Create(spine), run_time=0.9)

        stations = [
            (1.55,  "PREVENT", "inside the toolkit", "one", TEAL),
            (-0.28, "CATCH",   "on your machine",    "one", SLATE),
            (-2.1,  "DETECT",  "in the Drive", "two or more", CRIMSON),
        ]
        for y, name, sub, cnt, col in stations:
            d = Dot(point=LEFT * 1.55 + UP * y, radius=0.1, color=col)
            lab = _t(name, size=20, color=col, weight="BOLD")
            lab.next_to(d, RIGHT, buff=0.28)
            sb = _cite(sub, size=13).next_to(lab, DOWN, buff=0.16)
            sb.align_to(lab, LEFT)
            ct = _cite(cnt, size=13).next_to(sb, DOWN, buff=0.1)
            ct.align_to(lab, LEFT)
            self.play(GrowFromCenter(d), FadeIn(lab, shift=RIGHT * 0.12),
                      run_time=0.55)
            self.play(FadeIn(sb), FadeIn(ct), run_time=0.4)

        self.wait(1.5)
        cap = _t("people involved by\nthe time it surfaces", size=16, color=SOFT)
        cap.move_to(DOWN * 3.1)
        self.play(FadeIn(cap), run_time=0.7)
        self.wait(2.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B03 — the two cards stack instead of sitting side by side.
# ─────────────────────────────────────────────────────────────────────────────
class B03_StarterKit(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("One — a starter kit")
        self.play(Write(title), run_time=0.9)

        a = _card(3.8, 2.25).move_to(UP * 1.35)
        a_h = _t("pasted before building", size=17, color=SLATE, weight="BOLD")
        a_h.move_to(a.get_top() + DOWN * 0.34)
        items = VGroup(*[_cite(s, size=14) for s in (
            "3840 × 2160  landscape",
            "2160 × 3840  vertical",
            "Project_Volunteer.mp4",
            "the channel it is for",
        )]).arrange(DOWN, aligned_edge=LEFT, buff=0.21)
        items.next_to(a_h, DOWN, buff=0.24)
        self.play(Create(a), run_time=0.55)
        self.play(FadeIn(a_h), run_time=0.35)
        for it in items:
            self.play(FadeIn(it, shift=RIGHT * 0.12), run_time=0.28)

        b = _card(3.8, 2.25).move_to(DOWN * 1.3)
        b_h = _t("run before uploading", size=17, color=SLATE, weight="BOLD")
        b_h.move_to(b.get_top() + DOWN * 0.34)
        checks = [("both formats", TEAL), ("both at size", TEAL),
                  ("filename", TEAL), ("opening line", CRIMSON)]
        rowg = VGroup()
        for label, col in checks:
            mark = _t("✓" if col is TEAL else "✗", size=16, color=col)
            rowg.add(VGroup(mark, _cite(label, size=14)).arrange(RIGHT, buff=0.18))
        rowg.arrange(DOWN, aligned_edge=LEFT, buff=0.21)
        rowg.next_to(b_h, DOWN, buff=0.24)
        self.play(Create(b), run_time=0.55)
        self.play(FadeIn(b_h), run_time=0.35)
        for r in rowg:
            self.play(FadeIn(r, shift=RIGHT * 0.12), run_time=0.28)

        self.wait(1.0)
        limit = _t("A nudge, not\na guarantee.", size=17, color=SLATE)
        limit.move_to(DOWN * 3.02)
        self.play(FadeIn(limit, shift=UP * 0.15), run_time=0.7)
        self.wait(2.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B04 — the paired "declined" cards stack.
# ─────────────────────────────────────────────────────────────────────────────
class B04_Standardise(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Two — decline at\nthe point of writing")
        self.play(Write(title), run_time=0.9)

        top_lab = _cite("the rule that already exists", size=14).move_to(UP * 1.95)
        self.play(FadeIn(top_lab), run_time=0.5)
        left = _card(3.8, 1.5, stroke=SLATE).move_to(UP * 1.05)
        l1 = _t("a placeholder remains", size=16).move_to(left.get_center() + UP * 0.3)
        l2 = _t("declined", size=21, color=TEAL, weight="BOLD")
        l2.move_to(left.get_center() + DOWN * 0.35)
        self.play(Create(left), run_time=0.5)
        self.play(FadeIn(l1), run_time=0.35)
        self.play(FadeIn(l2, scale=1.06), run_time=0.45)

        bot_lab = _cite("the same shape, for resolution", size=14).move_to(DOWN * 0.3)
        self.play(FadeIn(bot_lab), run_time=0.5)
        right = _card(3.8, 1.5, stroke=SLATE).move_to(DOWN * 1.2)
        r1 = _t("the size is not a target", size=16).move_to(right.get_center() + UP * 0.3)
        r2 = _t("declined", size=21, color=TEAL, weight="BOLD")
        r2.move_to(right.get_center() + DOWN * 0.35)
        self.play(Create(right), run_time=0.5)
        self.play(FadeIn(r1), run_time=0.35)
        self.play(FadeIn(r2, scale=1.06), run_time=0.45)

        mid = _t("a sibling of an existing\nhabit, not a new check",
                 size=16, color=SLATE)
        mid.move_to(DOWN * 2.6)
        self.play(FadeIn(mid, shift=UP * 0.15), run_time=0.7)
        cost = _cite("needs sign-off", size=14).move_to(DOWN * 3.25)
        self.play(FadeIn(cost), run_time=0.6)
        self.wait(6.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B05 — three columns, not four. 'format' is dropped; the size column is the
#  one the report exists to read, so it keeps the highlight.
# ─────────────────────────────────────────────────────────────────────────────
class B05_DriveReport(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Three — one row\nper file")
        self.play(Write(title), run_time=0.9)

        cols = [(-1.5, "fellow"), (0.05, "size"), (1.5, "verdict")]
        hdr = VGroup(*[_cite(n, size=13).move_to(RIGHT * x + UP * 1.5)
                       for x, n in cols])
        rule = Line(LEFT * 1.85 + UP * 1.22, RIGHT * 1.85 + UP * 1.22,
                    stroke_width=1.2, color=INK)
        self.play(FadeIn(hdr), Create(rule), run_time=0.7)

        data = [
            ("maya-r", "3840×2160", "pass", TEAL),
            ("maya-r", "1080×1920", "fail", CRIMSON),
            ("alex-t", "1920×1080", "fail", CRIMSON),
            ("sam-k",  "not sent",       "open", SOFT),
        ]
        for i, (who, size, verdict, col) in enumerate(data):
            y = 0.78 - i * 0.66
            cells = VGroup(
                _t(who, size=15).move_to(RIGHT * cols[0][0] + UP * y),
                _t(size, size=15).move_to(RIGHT * cols[1][0] + UP * y),
            )
            pill = RoundedRectangle(corner_radius=0.13, width=1.0, height=0.4,
                                    color=col, stroke_width=1.5, fill_opacity=0.0)
            pill.move_to(RIGHT * cols[2][0] + UP * y)
            v = _t(verdict, size=14, color=col, weight="BOLD").move_to(pill.get_center())
            sep = Line(LEFT * 1.85 + UP * (y - 0.33), RIGHT * 1.85 + UP * (y - 0.33),
                       stroke_width=0.7, color=GHOST)
            self.play(FadeIn(cells, shift=RIGHT * 0.15), run_time=0.38)
            self.play(Create(pill), FadeIn(v), Create(sep), run_time=0.4)

        self.wait(0.9)
        band = Rectangle(width=1.35, height=2.85, color=TEAL, stroke_width=1.8,
                         fill_color=TEAL, fill_opacity=0.07)
        band.move_to(RIGHT * cols[1][0] + DOWN * 0.22)
        self.play(Create(band), run_time=0.8)

        self.wait(0.7)
        dep = _t("grouping works because\nthe name is in the filename",
                 size=15, color=SLATE)
        dep.move_to(DOWN * 2.6)
        self.play(FadeIn(dep, shift=UP * 0.15), run_time=0.7)
        dep2 = _cite("no author field inside a video", size=13).move_to(DOWN * 3.22)
        self.play(FadeIn(dep2), run_time=0.6)
        self.wait(1.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B06 — the scale chain runs DOWN the frame instead of across it.
# ─────────────────────────────────────────────────────────────────────────────
class B06_RealVsStretched(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Four — the size is\nnot the picture")
        self.play(Write(title), run_time=0.9)

        # Size labels sit UNDER each box, centred — not beside it.
        # A label reads about 1.0 unit wide at size 13, so alongside even a
        # 2.0-wide box it lands at x=2.22 against a +/-1.95 safe edge. Box width
        # cannot fix that; the label has to move. Centred under the box, the
        # widest element in the column is the box itself at +/-1.0.
        # Vertical budget, measured rather than nudged. Gate B reports the
        # two-line title's box as y 2.47..3.35, so the first box must top out
        # below 2.47: at UP*2.0 it spans 2.31..1.69, clearing it by 0.16.
        # Chain below that: s_lab ~1.53..1.37, mid 0.99..0.12, m_lab ~-0.05,
        # big -0.59..-1.72, b_lab ~-1.88..-2.04, closing line -2.48..-2.92.
        small = _card(1.10, 0.62, stroke=SLATE).move_to(UP * 2.0)
        s_lab = _cite("1280 × 720", size=13).next_to(small, DOWN, buff=0.16)
        self.play(Create(small), FadeIn(s_lab), run_time=0.7)

        mid = _card(1.55, 0.87, stroke=SLATE).move_to(UP * 0.55)
        m_lab = _cite("2560 × 1440", size=13).next_to(mid, DOWN, buff=0.16)
        a1 = Arrow(s_lab.get_bottom(), mid.get_top(), buff=0.1,
                   stroke_width=2.0, color=INK,
                   max_tip_length_to_length_ratio=0.4)
        self.play(Create(a1), run_time=0.45)
        self.play(Create(mid), FadeIn(m_lab), run_time=0.7)

        big = _card(2.00, 1.13, stroke=CRIMSON, width=2.0).move_to(DOWN * 1.15)
        b_lab = _cite("3840 × 2160", size=13).next_to(big, DOWN, buff=0.16)
        b_tag = _t("stretched", size=15, color=CRIMSON).move_to(big.get_center())
        a2 = Arrow(m_lab.get_bottom(), big.get_top(), buff=0.1,
                   stroke_width=2.0, color=CRIMSON,
                   max_tip_length_to_length_ratio=0.4)
        self.play(Create(a2), run_time=0.45)
        self.play(Create(big), FadeIn(b_lab), run_time=0.7)
        self.play(FadeIn(b_tag), run_time=0.4)

        self.wait(1.4)
        line1 = _t("The file measures 4K.\nThe picture does not.", size=16, color=SLATE)
        line1.move_to(DOWN * 2.7)
        self.play(FadeIn(line1, shift=UP * 0.15), run_time=0.8)
        self.wait(0.8)
        self.wait(2.2)


# ────────────────────────────────────────────────────────────────────────────
#  B07 — the two folders stack.
# ─────────────────────────────────────────────────────────────────────────────
class B07_SortFolders(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Five — the folder\norganises itself")
        self.play(Write(title), run_time=0.9)

        hub = _card(2.6, 0.7, stroke=SLATE).move_to(UP * 1.7)
        hub_l = _t("the same checks", size=16, color=SLATE).move_to(hub.get_center())
        self.play(Create(hub), FadeIn(hub_l), run_time=0.7)

        passed = _card(3.5, 1.0, stroke=TEAL).move_to(UP * 0.25)
        p_l = _t("passed", size=19, color=TEAL, weight="BOLD")
        p_l.move_to(passed.get_center() + UP * 0.17)
        p_s = _cite("ready for review", size=13).move_to(passed.get_center() + DOWN * 0.26)

        needs = _card(3.5, 1.0, stroke=CRIMSON).move_to(DOWN * 1.2)
        n_l = _t("needs work", size=19, color=CRIMSON, weight="BOLD")
        n_l.move_to(needs.get_center() + UP * 0.17)
        n_s = _cite("reason attached", size=13).move_to(needs.get_center() + DOWN * 0.26)

        aL = Arrow(hub.get_bottom(), passed.get_top(), buff=0.12, stroke_width=2.0,
                   color=TEAL, max_tip_length_to_length_ratio=0.3)
        aR = Arrow(passed.get_bottom(), needs.get_top(), buff=0.12, stroke_width=2.0,
                   color=CRIMSON, max_tip_length_to_length_ratio=0.3)
        self.play(Create(aL), run_time=0.4)
        self.play(Create(passed), FadeIn(p_l), FadeIn(p_s), run_time=0.7)
        self.play(Create(aR), run_time=0.4)
        self.play(Create(needs), FadeIn(n_l), FadeIn(n_s), run_time=0.7)

        self.wait(0.7)
        note = _card(3.8, 0.62, stroke=GHOST).move_to(DOWN * 2.45)
        note_l = _cite("is 1080×1920, needs 2160×3840", size=13)
        note_l.move_to(note.get_center())
        self.play(Create(note), FadeIn(note_l), run_time=0.7)
        limit = _cite("sorting is convenience", size=13).move_to(DOWN * 3.2)
        self.play(FadeIn(limit), run_time=0.6)
        self.wait(1.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B08 — five narrow cards in a row collapse to three stacked outcomes.
# ─────────────────────────────────────────────────────────────────────────────
class B08_HonestAccounting(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Five packages,\ncounted honestly")
        self.play(Write(title), run_time=0.9)

        five = VGroup()
        for i in range(5):
            c = _card(0.66, 0.8, stroke=SLATE, width=1.3)
            lab = _t(str(i + 1), size=18, color=SLATE, weight="BOLD").move_to(c.get_center())
            five.add(VGroup(c, lab))
        five.arrange(RIGHT, buff=0.14).move_to(UP * 1.6)
        for g in five:
            self.play(FadeIn(g, shift=UP * 0.14), run_time=0.26)

        shared = _t("one, three and four read\nthe same finished folder",
                    size=16, color=SLATE)
        shared.move_to(DOWN * 2.75)
        self.play(FadeIn(shared), run_time=0.7)
        self.wait(1.1)

        out = VGroup(
            VGroup(_card(2.9, 0.78, stroke=TEAL), _t("one tool", size=18, color=TEAL, weight="BOLD")),
            VGroup(_card(2.9, 0.78, stroke=TEAL), _t("one rule", size=18, color=TEAL, weight="BOLD")),
            VGroup(_card(2.9, 0.78, stroke=GHOST), _t("one document", size=18, color=SOFT)),
        )
        for g in out:
            g[1].move_to(g[0].get_center())
        out.arrange(DOWN, buff=0.3).move_to(UP * 0.55)

        self.play(ReplacementTransform(five, out), run_time=1.4)
        self.wait(0.6)
        tail = _t("two pieces of work,\nand a document", size=17, color=INK)
        tail.move_to(DOWN * 1.55)
        self.play(FadeIn(tail, shift=UP * 0.15), run_time=0.7)
        self.wait(1.8)


# ─────────────────────────────────────────────────────────────────────────────
#  B10 — outro. Title wraps to four lines in the narrow frame.
# ─────────────────────────────────────────────────────────────────────────────
class B10_Outro(Scene):
    def construct(self):
        self.camera.background_color = BG

        anchors = VGroup(
            Dot(point=LEFT * 1.85 + UP * 3.3, radius=0.02, color=GHOST),
            Dot(point=RIGHT * 1.85 + UP * 3.3, radius=0.02, color=GHOST),
            Dot(point=LEFT * 1.85 + DOWN * 3.3, radius=0.02, color=GHOST),
            Dot(point=RIGHT * 1.85 + DOWN * 3.3, radius=0.02, color=GHOST),
        )
        self.add(anchors)

        eyebrow = _t("IRREDUCIBLY HUMAN", size=15, color=TEAL, weight="BOLD")
        eyebrow.move_to(UP * 2.1)
        self.play(FadeIn(eyebrow), run_time=0.6)

        # Four lines at 28, not three at 30. "Resolution Problem" on one line
        # measured ±2.13 against a ±1.95 safe edge; splitting it puts the
        # widest line ("Resolution") at roughly ±1.1.
        #
        # The last line is its OWN Text so the terracotta period can sit beside
        # it. next_to(block, RIGHT) on a multi-line Text aligns to the block's
        # bounding box — whose right edge is the widest line, "Resolution" —
        # which left the period orphaned in open space to the right of
        # "Problem". Pairing it with the final line only is the fix.
        head = _t("Five Ways\nto Catch a\nResolution", size=28, weight="BOLD", lead=0.95)
        last = _t("Problem", size=28, weight="BOLD")
        dot = _t(".", size=28, color=CRIMSON, weight="BOLD")
        dot.next_to(last, RIGHT, buff=0.03).align_to(last, DOWN)
        tail_line = VGroup(last, dot)
        body = VGroup(head, tail_line).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        body.move_to(UP * 0.35)
        self.play(FadeIn(body, shift=UP * 0.2), run_time=1.0)

        rule = Line(LEFT * 0.75, RIGHT * 0.75, stroke_width=2.4, color=CRIMSON)
        rule.move_to(DOWN * 1.15)
        self.play(Create(rule), run_time=0.6)

        handle = _t("@HumanitariansAI", size=22, color=INK).move_to(DOWN * 1.95)
        self.play(FadeIn(handle), run_time=0.7)

        tail = _cite("part two covers the\nthree workflows", size=14).move_to(DOWN * 2.9)
        self.play(FadeIn(tail), run_time=0.6)
        self.wait(2.2)
