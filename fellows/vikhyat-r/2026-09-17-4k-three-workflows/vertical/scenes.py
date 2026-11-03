"""scenes.py — PORTRAIT Manim scenes for hai-4k-three-workflows-vertical.

A real portrait rewrite, not the landscape scenes at another resolution. This
reel leans harder on horizontal arrangements than its companion, so more had to
be rethought:

  B02  landscape ran paste -> build -> render -> check left to right with a
       return loop underneath. Here the flow runs DOWNWARD and the refusal
       loops back up the left-hand side.
  B03  the funnel narrowed left-to-right. Here it tapers top-to-bottom, which
       is the more natural reading of a funnel anyway.
  B04  two folders side by side become two folders stacked.
  B06  a left-hand spine with a right-hand consequence column becomes one
       column with the consequence beneath each row.
  B07  "stays" and "goes" sat side by side; here they stack, and the lower one
       still fades to make the point.

Frame: Manim does NOT derive a portrait frame from a portrait pixel canvas — at
-r 2160,3840 it keeps frame_width at 14.2222 and frame_height at 8.0, scaling
the axes by different amounts. Forced to 4.5 x 8.0 below, giving square pixels
at 480 px/unit.

Safe area, as Gate B reports it for this frame: x in [-1.95, 1.95],
y in [-3.4, 3.4]. Measured, not derived.

Class names match the parent beat sheet's shot.manim.scene_class.
"""
from manim import *

# ── PORTRAIT FRAME — load-bearing, do not remove ─────────────────────────────
config.frame_width = 4.5
config.frame_height = 8.0

# ── Humanitarians palette (identical to every other cut) ─────────────────────
BG      = ManimColor("#F3EBDD")
INK     = ManimColor("#2F2A26")
TEAL    = ManimColor("#1F4E5F")
CRIMSON = ManimColor("#E4572E")
SLATE   = ManimColor("#29335C")
SOFT    = ManimColor("#6E675E")
GHOST   = ManimColor("#B6AE9F")


def _t(text, size=19, color=None, weight=None, lead=0.85):
    kw = {"font_size": size, "color": color or INK, "line_spacing": lead}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


def _cite(text, size=13, lead=0.8):
    return Text(text, font_size=size, color=SOFT, line_spacing=lead)


def _title(text, size=26):
    return _t(text, size=size, weight="BOLD").to_edge(UP, buff=0.65)


def _card(w, h, stroke=INK, width=1.5):
    return Rectangle(width=w, height=h, color=stroke,
                     stroke_width=width, fill_opacity=0.0)


def _arrow(a, b, color=INK, buff=0.1):
    return Arrow(a, b, buff=buff, stroke_width=1.8, color=color,
                 max_tip_length_to_length_ratio=0.35)


# ─────────────────────────────────────────────────────────────────────────────
#  B01 — three stacked lanes.
# ─────────────────────────────────────────────────────────────────────────────
class B01_ThreeNamed(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Three workflows")
        self.play(Write(title), run_time=0.9)

        lanes = [
            (1.65,  "A", "inside the toolkit", "prevents", TEAL),
            (-0.15, "B", "in the Drive",       "describes", SLATE),
            (-1.95, "C", "in the Drive",       "organises", CRIMSON),
        ]
        verbs = VGroup()
        for y, letter, where, verb, col in lanes:
            c = _card(3.8, 1.35, stroke=col).move_to(UP * y)
            ltr = _t(letter, size=34, color=col, weight="BOLD")
            ltr.move_to(c.get_center() + LEFT * 1.35)
            wh = _cite(where, size=13).move_to(c.get_center() + RIGHT * 0.4 + UP * 0.25)
            self.play(Create(c), FadeIn(ltr), run_time=0.5)
            self.play(FadeIn(wh), run_time=0.3)
            v = _t(verb, size=21, color=col, weight="BOLD")
            v.move_to(c.get_center() + RIGHT * 0.4 + DOWN * 0.3)
            verbs.add(v)

        tail = _t("not three versions of\nthe same thing", size=17, color=SLATE)
        tail.move_to(DOWN * 3.05)
        self.play(FadeIn(tail, shift=UP * 0.15), run_time=0.7)

        self.wait(0.5)
        for v in verbs:
            self.play(FadeIn(v, shift=UP * 0.12), run_time=0.4)
        self.wait(2.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B02 — the flow runs downward; the refusal loops back up the left.
# ─────────────────────────────────────────────────────────────────────────────
class B02_WorkflowA(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("A — the wrong file\nis never made")
        self.play(Write(title), run_time=0.9)

        ys = [1.35, 0.35, -0.65]
        labels = ["paste", "build", "render"]
        nodes = []
        prev = None
        for y, label in zip(ys, labels):
            c = _card(2.3, 0.62, stroke=SLATE).move_to(RIGHT * 0.35 + UP * y)
            t = _t(label, size=17, color=SLATE).move_to(c.get_center())
            if prev is not None:
                self.play(Create(_arrow(prev.get_bottom(), c.get_top(), SLATE)),
                          run_time=0.3)
            self.play(Create(c), FadeIn(t), run_time=0.4)
            nodes.append(c)
            prev = c

        gate = _card(2.6, 0.7, stroke=CRIMSON, width=1.9).move_to(RIGHT * 0.35 + DOWN * 1.75)
        gate_t = _t("check size", size=17, color=CRIMSON).move_to(gate.get_center())
        self.play(Create(_arrow(prev.get_bottom(), gate.get_top(), CRIMSON)), run_time=0.3)
        self.play(Create(gate), FadeIn(gate_t), run_time=0.45)

        # the refusal returns up the left-hand side, clear of every node
        loop = VMobject(stroke_color=CRIMSON, stroke_width=1.8)
        loop.set_points_as_corners([
            gate.get_left() + LEFT * 0.05,
            LEFT * 1.72 + DOWN * 1.75,
            LEFT * 1.72 + UP * 0.35,
            RIGHT * (0.35) + UP * 0.35 + LEFT * 1.15,
        ])
        self.play(Create(loop), run_time=0.9)
        loop_lab = _cite("nothing\nis saved", size=13).move_to(LEFT * 1.35 + DOWN * 0.75)
        self.play(FadeIn(loop_lab), run_time=0.45)

        done = _card(2.6, 0.7, stroke=TEAL).move_to(RIGHT * 0.35 + DOWN * 2.75)
        done_t = _t("upload", size=18, color=TEAL, weight="BOLD").move_to(done.get_center())
        self.play(Create(_arrow(gate.get_bottom(), done.get_top(), TEAL)), run_time=0.35)
        self.play(Create(done), FadeIn(done_t), run_time=0.45)

        self.wait(7.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B03 — the funnel tapers downward, which reads better than sideways anyway.
# ─────────────────────────────────────────────────────────────────────────────
class B03_WorkflowB(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("B — cheap pass first")
        self.play(Write(title), run_time=0.9)

        wide = _card(3.85, 1.0, stroke=SLATE).move_to(UP * 1.7)
        wide_t = _t("every file, from\nthe Drive's record", size=16, color=SLATE)
        wide_t.move_to(wide.get_center())
        self.play(Create(wide), run_time=0.6)
        self.play(FadeIn(wide_t), run_time=0.45)
        wide_s = _cite("no downloads · seconds", size=13).next_to(wide, DOWN, buff=0.14)
        self.play(FadeIn(wide_s), run_time=0.35)

        wl = VMobject(stroke_color=GHOST, stroke_width=1.3)
        wl.set_points_as_corners([wide.get_corner(DL), LEFT * 1.1 + UP * 0.35])
        wr = VMobject(stroke_color=GHOST, stroke_width=1.3)
        wr.set_points_as_corners([wide.get_corner(DR), RIGHT * 1.1 + UP * 0.35])
        self.play(Create(wl), Create(wr), run_time=0.65)

        narrow = _card(2.2, 0.95, stroke=SLATE).move_to(DOWN * 0.15)
        narrow_t = _t("survivors only:\nframe check", size=15, color=SLATE)
        narrow_t.move_to(narrow.get_center())
        self.play(Create(narrow), FadeIn(narrow_t), run_time=0.6)

        # Below the narrow card, not beside it. At x=-1.28 y=-0.55 this label
        # measured x -1.84..-0.72 / y -0.8..-0.3, which intersects the card
        # (x +/-1.1, y -0.625..0.325) at its bottom-left corner — Gate B flags
        # that as a label sitting on a line. There is no room to its left
        # either: the funnel wall passes through (-1.5, 0.76).
        drop = _t("most stop here", size=15, color=CRIMSON)
        drop.move_to(LEFT * 1.15 + DOWN * 1.0)
        self.play(FadeIn(drop), run_time=0.45)

        sheet = _card(3.0, 0.72, stroke=TEAL).move_to(DOWN * 1.85)
        sheet_t = _t("one spreadsheet", size=17, color=TEAL, weight="BOLD")
        sheet_t.move_to(sheet.get_center())
        self.play(Create(_arrow(narrow.get_bottom(), sheet.get_top(), TEAL)), run_time=0.35)
        self.play(Create(sheet), FadeIn(sheet_t), run_time=0.45)

        tail = _cite("nothing in the Drive changes", size=13).move_to(DOWN * 2.6)
        self.play(FadeIn(tail), run_time=0.5)
        self.wait(10.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B04 — the two folders stack.
# ─────────────────────────────────────────────────────────────────────────────
class B04_WorkflowC(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("C — B first, then\nthe folder moves")
        self.play(Write(title), run_time=0.9)

        hub = _card(3.6, 0.7, stroke=SLATE).move_to(UP * 1.6)
        hub_t = _t("B's verdicts, settled", size=16, color=SLATE).move_to(hub.get_center())
        self.play(Create(hub), FadeIn(hub_t), run_time=0.6)

        passed = _card(3.5, 0.95, stroke=TEAL).move_to(UP * 0.3)
        p_l = _t("passed", size=19, color=TEAL, weight="BOLD")
        p_l.move_to(passed.get_center() + UP * 0.17)
        p_s = _cite("ready for review", size=13).move_to(passed.get_center() + DOWN * 0.25)

        needs = _card(3.5, 0.95, stroke=CRIMSON).move_to(DOWN * 1.05)
        n_l = _t("needs work", size=19, color=CRIMSON, weight="BOLD")
        n_l.move_to(needs.get_center() + UP * 0.17)
        n_s = _cite("with the corrected value", size=13).move_to(needs.get_center() + DOWN * 0.25)

        self.play(Create(_arrow(hub.get_bottom(), passed.get_top(), TEAL)), run_time=0.35)
        self.play(Create(passed), FadeIn(p_l), FadeIn(p_s), run_time=0.6)
        self.play(Create(_arrow(passed.get_bottom(), needs.get_top(), CRIMSON)), run_time=0.35)
        self.play(Create(needs), FadeIn(n_l), FadeIn(n_s), run_time=0.6)

        rail = Line(LEFT * 1.85 + DOWN * 2.2, RIGHT * 1.85 + DOWN * 2.2,
                    stroke_width=1.5, color=SLATE)
        rail_t = _cite("every move logged ·\nan error is traceable", size=13)
        rail_t.move_to(DOWN * 2.8)
        self.play(Create(rail), run_time=0.55)
        self.play(FadeIn(rail_t), run_time=0.45)
        self.wait(7.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B05 — one line each, stacked. Same restraint as landscape.
# ─────────────────────────────────────────────────────────────────────────────
class B05_WhatSeparates(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("What only each\none does")
        self.play(Write(title), run_time=0.9)

        rows = [
            ("A", "never creates\nthe wrong file", TEAL),
            ("B", "changes nothing,\nprevents nothing", SLATE),
            ("C", "the only one\nthat writes", CRIMSON),
        ]
        y0 = 1.3
        for i, (letter, line, col) in enumerate(rows):
            y = y0 - i * 1.55
            box = _card(0.8, 0.8, stroke=col).move_to(LEFT * 1.4 + UP * y)
            ltr = _t(letter, size=26, color=col, weight="BOLD").move_to(box.get_center())
            txt = _t(line, size=17).move_to(RIGHT * 0.55 + UP * y)
            rule = Line(LEFT * 1.85 + UP * (y - 0.68), RIGHT * 1.85 + UP * (y - 0.68),
                        stroke_width=0.7, color=GHOST)
            self.play(Create(box), FadeIn(ltr), run_time=0.42)
            self.play(FadeIn(txt, shift=RIGHT * 0.15), Create(rule), run_time=0.5)

        tail = _cite("each keeps its own limit", size=13).move_to(DOWN * 3.15)
        self.play(FadeIn(tail), run_time=0.5)
        self.wait(9.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B06 — one column; the consequence sits beneath each row, not beside it.
# ─────────────────────────────────────────────────────────────────────────────
class B06_TheOrder(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("The order is\nthe argument")
        self.play(Write(title), run_time=0.9)

        spine = Line(UP * 1.5, DOWN * 2.1, stroke_width=2.2, color=INK)
        spine.shift(LEFT * 1.6)
        self.play(Create(spine), run_time=0.8)

        stops = [
            (1.5,   "A", "upstream of everything", "nothing reaches B", TEAL),
            (-0.3,  "B", "sees what A missed",     "nobody opens a video", SLATE),
            (-2.1,  "C", "only once B is trusted", "the folder tidies itself", CRIMSON),
        ]
        for y, letter, line, conseq, col in stops:
            d = Dot(point=LEFT * 1.6 + UP * y, radius=0.1, color=col)
            ltr = _t(letter, size=24, color=col, weight="BOLD")
            ltr.next_to(d, RIGHT, buff=0.24)
            txt = _t(line, size=16).next_to(ltr, RIGHT, buff=0.26)
            con = _cite(conseq, size=13)
            con.next_to(ltr, DOWN, buff=0.16).align_to(ltr, LEFT)
            self.play(GrowFromCenter(d), FadeIn(ltr, shift=RIGHT * 0.1), run_time=0.45)
            self.play(FadeIn(txt), FadeIn(con), run_time=0.45)

        tail = _t("run all three, or\nonly B, or only A", size=16, color=SLATE)
        tail.move_to(DOWN * 3.05)
        self.play(FadeIn(tail, shift=UP * 0.15), run_time=0.6)
        self.wait(5.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B07 — stays above, goes below. The lower card still fades away.
# ─────────────────────────────────────────────────────────────────────────────
class B07_YouTubeCaveat(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("What none of\nthis removes")
        self.play(Write(title), run_time=0.9)

        stays = _card(3.85, 1.75, stroke=TEAL, width=1.9).move_to(UP * 1.35)
        s_h = _t("stays", size=21, color=TEAL, weight="BOLD")
        s_h.move_to(stays.get_center() + UP * 0.55)
        s_b = _t("the 4K check on\nYouTube, after\nprocessing", size=16)
        s_b.move_to(stays.get_center() + DOWN * 0.22)
        self.play(Create(stays), FadeIn(s_h), run_time=0.6)
        self.play(FadeIn(s_b), run_time=0.5)

        goes = _card(3.85, 1.75, stroke=GHOST).move_to(DOWN * 0.85)
        g_h = _t("goes", size=21, color=CRIMSON, weight="BOLD")
        g_h.move_to(goes.get_center() + UP * 0.55)
        g_b = _t("uploads spent on\nvideos that were\nnever going to pass", size=16)
        g_b.move_to(goes.get_center() + DOWN * 0.22)
        self.play(Create(goes), FadeIn(g_h), run_time=0.6)
        self.play(FadeIn(g_b), run_time=0.5)

        self.wait(1.1)
        self.play(goes.animate.set_stroke(opacity=0.12),
                  g_b.animate.set_opacity(0.12),
                  g_h.animate.set_opacity(0.3), run_time=1.1)

        tail = _t("not a replacement for\nthe reviewer's judgement", size=16, color=SLATE)
        tail.move_to(DOWN * 2.85)
        self.play(FadeIn(tail, shift=UP * 0.15), run_time=0.7)
        self.wait(6.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B09 — outro. Matches every other cut; period paired with its own last line.
# ─────────────────────────────────────────────────────────────────────────────
class B09_Outro(Scene):
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

        head = _t("Three Workflows,\nand What", size=27, weight="BOLD", lead=0.95)
        last = _t("Separates Them", size=27, weight="BOLD")
        dot = _t(".", size=27, color=CRIMSON, weight="BOLD")
        dot.next_to(last, RIGHT, buff=0.03).align_to(last, DOWN)
        body = VGroup(head, VGroup(last, dot)).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        body.move_to(UP * 0.35)
        self.play(FadeIn(body, shift=UP * 0.2), run_time=1.0)

        rule = Line(LEFT * 0.75, RIGHT * 0.75, stroke_width=2.4, color=CRIMSON)
        rule.move_to(DOWN * 1.15)
        self.play(Create(rule), run_time=0.6)

        handle = _t("@HumanitariansAI", size=22, color=INK).move_to(DOWN * 1.95)
        self.play(FadeIn(handle), run_time=0.7)

        tail = _cite("part one covers the\nfive packages", size=14).move_to(DOWN * 2.9)
        self.play(FadeIn(tail), run_time=0.6)
        self.wait(1.8)
