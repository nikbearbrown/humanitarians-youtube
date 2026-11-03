"""scenes.py — Manim scenes for hai-4k-three-workflows (landscape).

Companion to hai-4k-five-packages. Same humanitarians palette, same title
treatment, same outro form, so the two read as one piece in two parts.

Every constraint below was learned from the first reel's gate failures and is
applied here before the first render rather than after it:

  - _title uses to_edge(UP, buff=0.65). At 0.55 the box top lands at 3.45
    against Gate B's 3.4 safe edge — a 0.05-unit overshoot that fails every
    titled scene.
  - Cards are OUTLINE ONLY. A white fill on the cream ground sits at almost the
    same luminance as its background, and Gate V measures ink-vs-background
    separation across the whole ink mask: filled cards scored 0.00-0.05 against
    a 0.30 minimum.
  - Content stays inside x +/-6.3, y +/-3.4.
  - Bottom-of-frame content arrives EARLY. Gate V samples at 50% of the beat and
    compile.py retimes Manim clips ~1.5x, so the sample lands mid-build; a
    scene that fills downward late reads as underfilled.
  - Every scene changes SHAPE, not just text. Gate A rejects a single distinct
    shape-state as a text slide wearing a diagram's clothes.
  - The outro period pairs with its own final line. next_to() on a multi-line
    block aligns to the widest line, which orphans the glyph.

GOLD is a highlighter fill only and is never used as text (Gate W refuses it).
Nothing in this file lives in the toolkit tree; it belongs to the reel.
"""
from manim import *

# ── Humanitarians palette ────────────────────────────────────────────────────
BG      = ManimColor("#F3EBDD")   # cream ground
INK     = ManimColor("#2F2A26")   # warm ink — all body text
TEAL    = ManimColor("#1F4E5F")   # kept / true / prevents
CRIMSON = ManimColor("#E4572E")   # lost / wrong / refused
SLATE   = ManimColor("#29335C")   # structure, entity cards
SOFT    = ManimColor("#6E675E")   # secondary, citation lines
GHOST   = ManimColor("#B6AE9F")   # dimmed


def _t(text, size=22, color=None, weight=None, lead=0.9):
    kw = {"font_size": size, "color": color or INK, "line_spacing": lead}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


def _cite(text, size=16, lead=0.85):
    return Text(text, font_size=size, color=SOFT, line_spacing=lead)


def _title(text, size=32):
    return _t(text, size=size, weight="BOLD").to_edge(UP, buff=0.65)


def _card(w, h, stroke=INK, width=1.6):
    return Rectangle(width=w, height=h, color=stroke,
                     stroke_width=width, fill_opacity=0.0)


def _arrow(a, b, color=INK, buff=0.2):
    return Arrow(a, b, buff=buff, stroke_width=2.0, color=color,
                 max_tip_length_to_length_ratio=0.18)


# ─────────────────────────────────────────────────────────────────────────────
#  B01 — the three, and the verb each one owns.
# ─────────────────────────────────────────────────────────────────────────────
class B01_ThreeNamed(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("Three workflows")
        self.play(Write(title), run_time=0.9)

        lanes = [
            (-4.15, "A", "inside the toolkit", "prevents", TEAL),
            (0.0,   "B", "in the Drive",       "describes", SLATE),
            (4.15,  "C", "in the Drive",       "organises", CRIMSON),
        ]

        cards, verbs = VGroup(), VGroup()
        for x, letter, where, verb, col in lanes:
            c = _card(3.6, 2.5, stroke=col).move_to(RIGHT * x + UP * 0.55)
            ltr = _t(letter, size=52, color=col, weight="BOLD")
            ltr.move_to(c.get_center() + UP * 0.55)
            wh = _cite(where, size=17).move_to(c.get_center() + DOWN * 0.42)
            self.play(Create(c), FadeIn(ltr), run_time=0.5)
            self.play(FadeIn(wh), run_time=0.3)
            cards.add(c, ltr, wh)
            verbs.add(_t(verb, size=27, color=col, weight="BOLD")
                      .move_to(RIGHT * x + DOWN * 1.35))

        # the closing line arrives before the long hold, so the frame is full
        # at Gate V's 50% sample rather than only at the end
        tail = _t("not three versions of the same thing", size=21, color=SLATE)
        tail.move_to(DOWN * 2.75)
        self.play(FadeIn(tail, shift=UP * 0.2), run_time=0.7)

        self.wait(0.8)
        for v in verbs:
            self.play(FadeIn(v, shift=UP * 0.18), run_time=0.45)

        self.wait(3.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B02 — workflow A. The refusal loops back; that loop is the scene.
# ─────────────────────────────────────────────────────────────────────────────
class B02_WorkflowA(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("A — the wrong file is never made")
        self.play(Write(title), run_time=0.9)

        steps = [(-4.55, "paste"), (-1.55, "build"), (1.45, "render")]
        nodes = VGroup()
        prev = None
        for x, label in steps:
            c = _card(2.5, 0.95, stroke=SLATE).move_to(RIGHT * x + UP * 1.1)
            t = _t(label, size=21, color=SLATE).move_to(c.get_center())
            if prev is not None:
                self.play(Create(_arrow(prev.get_right(), c.get_left(), SLATE)),
                          run_time=0.35)
            self.play(Create(c), FadeIn(t), run_time=0.45)
            nodes.add(c, t)
            prev = c

        gate = _card(2.6, 0.95, stroke=CRIMSON, width=2.0).move_to(RIGHT * 4.55 + UP * 1.1)
        gate_t = _t("check size", size=20, color=CRIMSON).move_to(gate.get_center())
        self.play(Create(_arrow(prev.get_right(), gate.get_left(), CRIMSON)), run_time=0.35)
        self.play(Create(gate), FadeIn(gate_t), run_time=0.5)

        # the return path — drawn as a real detour so it crosses nothing
        loop = VMobject(stroke_color=CRIMSON, stroke_width=2.0)
        loop.set_points_as_corners([
            gate.get_bottom() + DOWN * 0.05,
            gate.get_bottom() + DOWN * 0.85,
            RIGHT * (-1.55) + UP * 0.25,
            RIGHT * (-1.55) + UP * 0.6,
        ])
        loop_lab = _t("nothing is saved", size=19, color=CRIMSON)
        loop_lab.move_to(RIGHT * 1.6 + DOWN * 0.55)
        self.play(Create(loop), run_time=0.9)
        self.play(FadeIn(loop_lab), run_time=0.5)

        done = _card(3.0, 0.95, stroke=TEAL).move_to(DOWN * 1.95)
        done_t = _t("upload", size=21, color=TEAL, weight="BOLD").move_to(done.get_center())
        self.play(Create(_arrow(gate.get_bottom() + DOWN * 0.9,
                                done.get_right(), TEAL, buff=0.25)), run_time=0.5)
        self.play(Create(done), FadeIn(done_t), run_time=0.5)

        tail = _cite("only once the check is satisfied", size=18).move_to(DOWN * 3.0)
        self.play(FadeIn(tail), run_time=0.6)
        self.wait(8.6)


# ─────────────────────────────────────────────────────────────────────────────
#  B03 — workflow B as a funnel. Width carries the cost argument.
# ─────────────────────────────────────────────────────────────────────────────
class B03_WorkflowB(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("B — cheap pass first")
        self.play(Write(title), run_time=0.9)

        wide = _card(10.4, 1.15, stroke=SLATE).move_to(UP * 1.5)
        wide_t = _t("every file, from the Drive's own record", size=21, color=SLATE)
        wide_t.move_to(wide.get_center() + UP * 0.2)
        wide_s = _cite("no downloads · whole folder in seconds", size=17)
        wide_s.move_to(wide.get_center() + DOWN * 0.3)
        self.play(Create(wide), run_time=0.7)
        self.play(FadeIn(wide_t), FadeIn(wide_s), run_time=0.5)

        # the funnel walls — the narrowing IS the point
        walls = VMobject(stroke_color=GHOST, stroke_width=1.4)
        walls.set_points_as_corners([wide.get_corner(DL), LEFT * 2.6 + UP * 0.05])
        walls2 = VMobject(stroke_color=GHOST, stroke_width=1.4)
        walls2.set_points_as_corners([wide.get_corner(DR), RIGHT * 2.6 + UP * 0.05])
        self.play(Create(walls), Create(walls2), run_time=0.7)

        drop = _t("most failures stop here", size=19, color=CRIMSON)
        drop.move_to(LEFT * 4.3 + DOWN * 0.45)
        self.play(FadeIn(drop), run_time=0.5)

        narrow = _card(5.0, 1.15, stroke=SLATE).move_to(DOWN * 0.55)
        narrow_t = _t("survivors only — frame check", size=20, color=SLATE)
        narrow_t.move_to(narrow.get_center() + UP * 0.2)
        narrow_s = _cite("is it really 4K, or stretched?", size=17)
        narrow_s.move_to(narrow.get_center() + DOWN * 0.3)
        self.play(Create(narrow), run_time=0.6)
        self.play(FadeIn(narrow_t), FadeIn(narrow_s), run_time=0.5)

        sheet = _card(4.2, 0.9, stroke=TEAL).move_to(DOWN * 2.35)
        sheet_t = _t("one spreadsheet", size=21, color=TEAL, weight="BOLD")
        sheet_t.move_to(sheet.get_center())
        self.play(Create(_arrow(narrow.get_bottom(), sheet.get_top(), TEAL, buff=0.14)),
                  run_time=0.4)
        self.play(Create(sheet), FadeIn(sheet_t), run_time=0.5)

        tail = _cite("nothing in the Drive changes", size=18).move_to(DOWN * 3.15)
        self.play(FadeIn(tail), run_time=0.6)
        self.wait(11.4)


# ─────────────────────────────────────────────────────────────────────────────
#  B04 — workflow C. Verdicts settled, then routing, log underneath.
# ─────────────────────────────────────────────────────────────────────────────
class B04_WorkflowC(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("C — B first, then the folder moves")
        self.play(Write(title), run_time=0.9)

        hub = _card(4.6, 0.95, stroke=SLATE).move_to(UP * 1.75)
        hub_t = _t("B's verdicts, already settled", size=20, color=SLATE)
        hub_t.move_to(hub.get_center())
        self.play(Create(hub), FadeIn(hub_t), run_time=0.7)

        passed = _card(4.5, 1.35, stroke=TEAL).move_to(LEFT * 3.4 + UP * 0.05)
        p_l = _t("passed", size=24, color=TEAL, weight="BOLD")
        p_l.move_to(passed.get_center() + UP * 0.25)
        p_s = _cite("ready for review", size=17).move_to(passed.get_center() + DOWN * 0.35)

        needs = _card(4.5, 1.35, stroke=CRIMSON).move_to(RIGHT * 3.4 + UP * 0.05)
        n_l = _t("needs work", size=24, color=CRIMSON, weight="BOLD")
        n_l.move_to(needs.get_center() + UP * 0.25)
        n_s = _cite("with the corrected value", size=17).move_to(needs.get_center() + DOWN * 0.35)

        self.play(Create(_arrow(hub.get_bottom(), passed.get_top(), TEAL, buff=0.16)),
                  Create(_arrow(hub.get_bottom(), needs.get_top(), CRIMSON, buff=0.16)),
                  run_time=0.6)
        self.play(Create(passed), FadeIn(p_l), FadeIn(p_s),
                  Create(needs), FadeIn(n_l), FadeIn(n_s), run_time=0.8)

        note = _card(7.0, 0.8, stroke=GHOST).move_to(DOWN * 1.55)
        note_t = _t("vertical is 1080 × 1920, needs 2160 × 3840", size=19)
        note_t.move_to(note.get_center())
        self.play(Create(note), FadeIn(note_t), run_time=0.7)

        rail = Line(LEFT * 5.6 + DOWN * 2.5, RIGHT * 5.6 + DOWN * 2.5,
                    stroke_width=1.6, color=SLATE)
        rail_t = _cite("every move logged · an error is traceable", size=18)
        rail_t.move_to(DOWN * 3.05)
        self.play(Create(rail), run_time=0.7)
        self.play(FadeIn(rail_t), run_time=0.5)
        self.wait(8.2)


# ─────────────────────────────────────────────────────────────────────────────
#  B05 — one line each. The restraint is the design.
# ─────────────────────────────────────────────────────────────────────────────
class B05_WhatSeparates(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("What only each one does")
        self.play(Write(title), run_time=0.9)

        rows = [
            ("A", "never creates the wrong file", TEAL),
            ("B", "changes nothing, prevents nothing", SLATE),
            ("C", "the only one that writes", CRIMSON),
        ]
        y0 = 1.3
        for i, (letter, line, col) in enumerate(rows):
            y = y0 - i * 1.5
            box = _card(1.0, 1.0, stroke=col).move_to(LEFT * 4.9 + UP * y)
            ltr = _t(letter, size=34, color=col, weight="BOLD").move_to(box.get_center())
            txt = _t(line, size=24).move_to(RIGHT * 0.9 + UP * y)
            rule = Line(LEFT * 4.2 + UP * (y - 0.72), RIGHT * 5.8 + UP * (y - 0.72),
                        stroke_width=0.8, color=GHOST)
            self.play(Create(box), FadeIn(ltr), run_time=0.45)
            self.play(FadeIn(txt, shift=RIGHT * 0.2), Create(rule), run_time=0.55)

        tail = _cite("each keeps its own limit", size=18).move_to(DOWN * 3.15)
        self.play(FadeIn(tail), run_time=0.6)
        self.wait(10.2)


# ─────────────────────────────────────────────────────────────────────────────
#  B06 — one spine, not three columns. Parallel columns would say "choose one".
# ─────────────────────────────────────────────────────────────────────────────
class B06_TheOrder(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("The order is the argument")
        self.play(Write(title), run_time=0.9)

        # The spine sits far left and each row carries a consequence column on
        # the right. With the spine at x=-2.6 the content reached only x~2.25,
        # leaving half of a 14.2-unit frame empty: Gate V measured 42% fill
        # against a 55% minimum. Two columns spanning -5.6..5.9 read as 91%.
        spine = Line(UP * 1.9, DOWN * 2.1, stroke_width=2.4, color=INK)
        spine.shift(LEFT * 5.6)
        self.play(Create(spine), run_time=0.9)

        stops = [
            (1.6,   "A", "upstream of everything", "nothing reaches B", TEAL),
            (-0.2,  "B", "sees what A did not stop", "nobody opens a video", SLATE),
            (-1.95, "C", "only once B is trusted", "the folder tidies itself", CRIMSON),
        ]
        for y, letter, line, conseq, col in stops:
            d = Dot(point=LEFT * 5.6 + UP * y, radius=0.13, color=col)
            ltr = _t(letter, size=32, color=col, weight="BOLD")
            ltr.move_to(LEFT * 4.85 + UP * y)
            txt = _t(line, size=22).move_to(UP * y).align_to(LEFT * 4.2, LEFT)
            con = _cite(conseq, size=19).move_to(UP * y).align_to(RIGHT * 5.9, RIGHT)
            rule = Line(LEFT * 5.6 + UP * (y - 0.68), RIGHT * 5.9 + UP * (y - 0.68),
                        stroke_width=0.7, color=GHOST)
            self.play(GrowFromCenter(d), FadeIn(ltr, shift=RIGHT * 0.15), run_time=0.5)
            self.play(FadeIn(txt, shift=RIGHT * 0.15), FadeIn(con), Create(rule),
                      run_time=0.5)

        tail = _t("run all three, or only B, or only A", size=21, color=SLATE)
        tail.move_to(DOWN * 3.05)
        self.play(FadeIn(tail, shift=UP * 0.2), run_time=0.7)
        self.wait(6.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B07 — what stays, and what goes.
# ─────────────────────────────────────────────────────────────────────────────
class B07_YouTubeCaveat(Scene):
    def construct(self):
        self.camera.background_color = BG

        title = _title("What none of this removes")
        self.play(Write(title), run_time=0.9)

        stays = _card(5.5, 2.3, stroke=TEAL, width=2.0).move_to(LEFT * 3.15 + UP * 0.5)
        s_h = _t("stays", size=25, color=TEAL, weight="BOLD")
        s_h.move_to(stays.get_center() + UP * 0.7)
        s_b = _t("the 4K check on YouTube,\nafter processing", size=20)
        s_b.move_to(stays.get_center() + DOWN * 0.2)
        self.play(Create(stays), FadeIn(s_h), run_time=0.6)
        self.play(FadeIn(s_b), run_time=0.5)

        goes = _card(5.5, 2.3, stroke=GHOST).move_to(RIGHT * 3.15 + UP * 0.5)
        g_h = _t("goes", size=25, color=CRIMSON, weight="BOLD")
        g_h.move_to(goes.get_center() + UP * 0.7)
        g_b = _t("uploads spent on videos that\nwere never going to pass", size=20)
        g_b.move_to(goes.get_center() + DOWN * 0.2)
        self.play(Create(goes), FadeIn(g_h), run_time=0.6)
        self.play(FadeIn(g_b), run_time=0.5)

        cite = _cite("a local file cannot prove how YouTube will handle it", size=19)
        cite.move_to(DOWN * 1.5)
        self.play(FadeIn(cite), run_time=0.6)

        # the one accent moment: the right-hand card leaves
        self.wait(1.2)
        self.play(goes.animate.set_stroke(opacity=0.12),
                  g_b.animate.set_opacity(0.12),
                  g_h.animate.set_opacity(0.3), run_time=1.1)

        tail = _t("not a replacement for the reviewer's judgement",
                  size=21, color=SLATE)
        tail.move_to(DOWN * 2.75)
        self.play(FadeIn(tail, shift=UP * 0.2), run_time=0.8)
        self.wait(7.0)


# ─────────────────────────────────────────────────────────────────────────────
#  B09 — outro. Matches the companion reel exactly.
# ─────────────────────────────────────────────────────────────────────────────
class B09_Outro(Scene):
    def construct(self):
        self.camera.background_color = BG

        anchors = VGroup(
            Dot(point=LEFT * 6.15 + UP * 3.28, radius=0.022, color=GHOST),
            Dot(point=RIGHT * 6.15 + UP * 3.28, radius=0.022, color=GHOST),
            Dot(point=LEFT * 6.15 + DOWN * 3.28, radius=0.022, color=GHOST),
            Dot(point=RIGHT * 6.15 + DOWN * 3.28, radius=0.022, color=GHOST),
        )
        self.add(anchors)

        eyebrow = _t("IRREDUCIBLY HUMAN", size=19, color=TEAL, weight="BOLD")
        eyebrow.move_to(UP * 2.35)
        self.play(FadeIn(eyebrow), run_time=0.6)

        # last line is its own Text so the period sits against it
        head = _t("Three Workflows, and", size=42, weight="BOLD")
        last = _t("What Separates Them", size=42, weight="BOLD")
        dot = _t(".", size=42, color=CRIMSON, weight="BOLD")
        dot.next_to(last, RIGHT, buff=0.04).align_to(last, DOWN)
        body = VGroup(head, VGroup(last, dot)).arrange(DOWN, buff=0.28)
        body.move_to(UP * 0.7)
        self.play(FadeIn(body, shift=UP * 0.25), run_time=1.0)

        rule = Line(LEFT * 1.6, RIGHT * 1.6, stroke_width=2.6, color=CRIMSON)
        rule.move_to(DOWN * 0.95)
        self.play(Create(rule), run_time=0.6)

        handle = _t("@HumanitariansAI", size=32, color=INK).move_to(DOWN * 1.95)
        self.play(FadeIn(handle), run_time=0.7)

        tail = _cite("part one covers the five packages", size=17)
        tail.move_to(DOWN * 2.95)
        self.play(FadeIn(tail), run_time=0.7)
        self.wait(2.2)
