"""vox_scenes.py — What a Review Has to Do That a Reaction Never Does
(vox-review-not-reaction, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat whose source is own.
B11 is the only STILL (ai media slot) and has no scene here.
Durations read from beat_sheet.json actuals after audio lock; estimates as fallback.

Color law (teardown palette):
  CRIMSON = the reaction — vague, feeling-based, indefensible
  INK     = the defensible review — criteria, evidence, verdict (TEAL == INK in teardown)
  GOLD    = editor's-pen highlight wash, once, in B12

Gate B: every zero-width stroke is also zero-opacity.
Anchor-not-transcript: on-screen text never copies the narration sentence.
W7: WRITING kicker only — never the book title, never a chapter number.
"""
import sys, json, pathlib
# Reel is at books/writing-guide/youtube/vox-review-not-reaction/vox_scenes.py
# parents[3] = books/, so vox library is at parents[3]/vox/aspects/...
_REEL_DIR = pathlib.Path(__file__).resolve().parent
_BOOKS_DIR = _REEL_DIR.parents[2]   # books/
sys.path.insert(0, str(_BOOKS_DIR / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene
import numpy as np

# ---- duration table (estimates; overwritten from beat_sheet.json at runtime)
DUR = {
    "B01": 10.5, "B02": 11.0, "B03": 10.0, "B04": 11.0,
    "B05": 10.5, "B06": 10.5, "B07": 11.5, "B08": 11.5,
    "B09": 12.0, "B10": 14.0, "B11": 11.0, "B12": 12.0, "B13": 11.5,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 9.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---- shared triangle geometry -----------------------------------------------

TRI_TOP   = np.array([0.0,  1.9, 0])
TRI_LEFT  = np.array([-2.2, -1.1, 0])
TRI_RIGHT = np.array([ 2.2, -1.1, 0])
TRI_COLOR = INK


def _triangle_edges():
    """Three Line objects forming the triangle (no fill)."""
    e1 = Line(TRI_TOP,   TRI_LEFT,  stroke_width=3, color=TRI_COLOR)
    e2 = Line(TRI_LEFT,  TRI_RIGHT, stroke_width=3, color=TRI_COLOR)
    e3 = Line(TRI_RIGHT, TRI_TOP,   stroke_width=3, color=TRI_COLOR)
    return e1, e2, e3


def _corner_label(text, pos, accent=INK, offset=None):
    """SerifLabel placed near a triangle corner."""
    lbl = SerifLabel(text, accent=accent, size=26)
    if offset is None:
        if pos[1] > 0:           # top
            offset = np.array([0, 0.45, 0])
        elif pos[0] < 0:         # left
            offset = np.array([-0.55, -0.15, 0])
        else:                    # right
            offset = np.array([ 0.55, -0.15, 0])
    lbl.move_to(pos + offset)
    return lbl


def _dot(pos, color=INK, r=0.12):
    d = Dot(radius=r, color=color)
    d.set_fill(color, 1).set_stroke(width=0, opacity=0)
    d.move_to(pos)
    return d


# ---------------------------------------------------------------- B01 Title --

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        kicker = LabelChip("WRITING", accent=CRIMSON, size=22)
        kicker.to_corner(UL, buff=0.6)
        t1 = Text("Service was slow.", font=DISPLAY, color=CRIMSON,
                  font_size=52, weight="BOLD")
        t2 = Text("Food was okay.", font=DISPLAY, color=CRIMSON,
                  font_size=52, weight="BOLD")
        t3 = Text("Three stars.", font=DISPLAY, color=CRIMSON,
                  font_size=52, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.2).move_to(ORIGIN)
        # Underline grows under the last sentence — real shape motion
        u = Line(t3.get_corner(DL) + DOWN * 0.14, t3.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2.5)
        self.play(FadeIn(kicker), run_time=0.5)
        self.play(FadeIn(t1, shift=UP * 0.15), run_time=0.6)
        self.play(FadeIn(t2, shift=UP * 0.15), run_time=0.5)
        self.play(FadeIn(t3, shift=UP * 0.15), run_time=0.5)
        self.play(Create(u), run_time=0.5)
        self.wait(max(0.5, total - 2.6))


# ---------------------------------------------------------------- B02 Reaction card --

class B02_ReactionCard(Scene):
    def construct(self):
        total = DUR["B02"]
        kicker = LabelChip("REACTION", accent=CRIMSON, size=22)
        kicker.to_corner(UL, buff=0.6)
        s1 = Text("Service was slow.", font=SERIF, color=CRIMSON, font_size=38)
        s2 = Text("Food was okay.", font=SERIF, color=CRIMSON, font_size=38)
        s3 = Text("Three stars.", font=SERIF, color=CRIMSON, font_size=38)
        sentences = VGroup(s1, s2, s3).arrange(DOWN, buff=0.28).move_to(UP * 0.3)
        note = SerifLabel("usable by no one", CRIMSON, size=26)
        note.next_to(sentences, DOWN, buff=0.6)
        self.play(FadeIn(kicker), run_time=0.4)
        self.play(FadeIn(s1, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(s2, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(s3, shift=RIGHT * 0.2), run_time=0.5)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.5))


# ---------------------------------------------------------------- B03 Question card --

class B03_QuestionCard(Scene):
    def construct(self):
        total = DUR["B03"]
        kicker = LabelChip("WRITING", accent=CRIMSON, size=22)
        kicker.to_corner(UL, buff=0.6)
        q = Text("What does a review\nhave to do that a\nreaction never does?",
                 font=DISPLAY, color=INK, font_size=34, weight="BOLD",
                 line_spacing=1.1)
        q.move_to(ORIGIN)
        u = Line(q.get_corner(DL) + DOWN * 0.14, q.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(kicker), run_time=0.4)
        self.play(FadeIn(q, shift=UP * 0.15), Create(u), run_time=1.0)
        self.wait(max(0.5, total - 1.4))


# ---------------------------------------------------------------- B04 Reaction limit --

class B04_ReactionLimit(Scene):
    def construct(self):
        total = DUR["B04"]
        # Left column: REACTION
        r_chip = LabelChip("REACTION", accent=CRIMSON, size=22)
        r_feeling = Text("felt it", font=SERIF, color=CRIMSON,
                         font_size=34, slant=ITALIC)
        r_report = Text("reported it", font=SERIF, color=CRIMSON,
                        font_size=34, slant=ITALIC)
        r_col = VGroup(r_chip, r_feeling, r_report).arrange(DOWN, buff=0.35)
        r_col.move_to(LEFT * 3.4 + UP * 0.2)

        # Right column: READER
        reader_chip = LabelChip("READER", accent=INK, size=22)
        reader_q = Text("cannot verify", font=SERIF, color=INK,
                        font_size=34, slant=ITALIC)
        r2_col = VGroup(reader_chip, reader_q).arrange(DOWN, buff=0.35)
        r2_col.move_to(RIGHT * 3.4 + UP * 0.2)

        # Arrow crossed out
        arr = Arrow(r_col.get_right() + RIGHT * 0.2,
                    r2_col.get_left() + LEFT * 0.2,
                    color=INK, stroke_width=2, buff=0)
        cross = Line(arr.get_start() + UP * 0.28, arr.get_end() + DOWN * 0.28,
                     color=CRIMSON, stroke_width=4)
        cross._qc_intentional = True   # deliberate cross-through, Gate B exempt

        self.play(FadeIn(r_col, shift=RIGHT * 0.3), run_time=0.8)
        self.play(FadeIn(r2_col, shift=LEFT * 0.3), run_time=0.7)
        self.play(GrowArrow(arr), run_time=0.6)
        self.play(Create(cross), run_time=0.5)
        self.wait(max(0.5, total - 2.6))


# ---------------------------------------------------------------- B05 Triangle — C --

class B05_TriangleC(Scene):
    def construct(self):
        total = DUR["B05"]
        tri = VGroup(*_triangle_edges()).move_to(DOWN * 0.2)
        # Adjust corner positions to match tri's position
        offset = DOWN * 0.2
        c_dot = _dot(TRI_LEFT + offset, color=INK)
        c_lbl = _corner_label("criteria", TRI_LEFT + offset, INK,
                               np.array([-0.85, -0.05, 0]))
        self.play(Create(tri[0]), Create(tri[1]), Create(tri[2]), run_time=1.0)
        self.play(FadeIn(c_dot, scale=1.4), FadeIn(c_lbl, shift=LEFT * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B06 Triangle — CE --

class B06_TriangleCE(Scene):
    def construct(self):
        total = DUR["B06"]
        offset = DOWN * 0.2
        tri = VGroup(*_triangle_edges()).move_to(DOWN * 0.2)
        c_dot = _dot(TRI_LEFT + offset, color=INK)
        c_lbl = _corner_label("criteria", TRI_LEFT + offset, INK,
                               np.array([-0.85, -0.05, 0]))
        # start with criteria already present
        self.add(tri, c_dot, c_lbl)
        e_dot = _dot(TRI_RIGHT + offset, color=INK)
        e_lbl = _corner_label("evidence", TRI_RIGHT + offset, INK,
                               np.array([0.85, -0.05, 0]))
        self.play(FadeIn(e_dot, scale=1.4), FadeIn(e_lbl, shift=RIGHT * 0.15), run_time=0.7)
        self.wait(max(0.5, total - 0.7))


# ---------------------------------------------------------------- B07 Triangle — CEJ --

class B07_TriangleCEJ(Scene):
    def construct(self):
        total = DUR["B07"]
        offset = DOWN * 0.2
        tri = VGroup(*_triangle_edges()).move_to(DOWN * 0.2)
        c_dot = _dot(TRI_LEFT + offset, color=INK)
        c_lbl = _corner_label("criteria", TRI_LEFT + offset, INK,
                               np.array([-0.85, -0.05, 0]))
        e_dot = _dot(TRI_RIGHT + offset, color=INK)
        e_lbl = _corner_label("evidence", TRI_RIGHT + offset, INK,
                               np.array([0.85, -0.05, 0]))
        self.add(tri, c_dot, c_lbl, e_dot, e_lbl)
        j_dot = _dot(TRI_TOP + offset, color=INK)
        j_lbl = _corner_label("judgment", TRI_TOP + offset, INK,
                               np.array([0, 0.48, 0]))
        self.play(FadeIn(j_dot, scale=1.4), FadeIn(j_lbl, shift=UP * 0.15), run_time=0.8)
        # Connect the triangle visually — scale the dots to pulse
        self.play(c_dot.animate.scale(1.3), e_dot.animate.scale(1.3),
                  j_dot.animate.scale(1.3), run_time=0.5)
        self.play(c_dot.animate.scale(1.0 / 1.3), e_dot.animate.scale(1.0 / 1.3),
                  j_dot.animate.scale(1.0 / 1.3), run_time=0.4)
        self.wait(max(0.5, total - 1.7))


# ---------------------------------------------------------------- B08 Triangle failures --

class B08_TriangleFailures(Scene):
    def construct(self):
        total = DUR["B08"]

        def _mini_tri(missing, label_text, x_offset):
            """A small triangle with one corner missing (crimson chip below)."""
            scale = 0.55
            top   = np.array([0.0,  1.9, 0]) * scale + np.array([x_offset, 0.2, 0])
            left  = np.array([-2.2, -1.1, 0]) * scale + np.array([x_offset, 0.2, 0])
            right = np.array([ 2.2, -1.1, 0]) * scale + np.array([x_offset, 0.2, 0])
            corners = {"criteria": left, "evidence": right, "judgment": top}
            e1 = Line(top, left, stroke_width=2.5, color=INK)
            e2 = Line(left, right, stroke_width=2.5, color=INK)
            e3 = Line(right, top, stroke_width=2.5, color=INK)
            dots = VGroup()
            for name, pos in corners.items():
                c = CRIMSON if name == missing else INK
                d = _dot(pos, color=c, r=0.09)
                dots.add(d)
            chip = LabelChip(label_text, accent=CRIMSON, size=18)
            chip.move_to(np.array([x_offset, -1.4, 0]))
            return VGroup(e1, e2, e3, dots, chip)

        thesis   = _mini_tri("evidence",  "THESIS",          -4.2)
        descr    = _mini_tri("criteria",  "DESCRIPTION",      0.0)
        lit      = _mini_tri("judgment",  "LITERATURE PAPER", 4.2)

        self.play(LaggedStart(
            FadeIn(thesis, shift=UP * 0.2),
            FadeIn(descr,  shift=UP * 0.2),
            FadeIn(lit,    shift=UP * 0.2),
            lag_ratio=0.3, run_time=1.4))
        self.wait(max(0.5, total - 1.4))


# ---------------------------------------------------------------- B09 Reaction annotated --

class B09_ReactionAnnotated(Scene):
    def construct(self):
        total = DUR["B09"]

        # Reaction text box on left
        rx1 = Text("Service was slow.", font=SERIF, color=CRIMSON, font_size=26)
        rx2 = Text("Food was okay.", font=SERIF, color=CRIMSON, font_size=26)
        rx3 = Text("Three stars.", font=SERIF, color=CRIMSON, font_size=26)
        rbox_txt = VGroup(rx1, rx2, rx3).arrange(DOWN, buff=0.18)
        rbox = SurroundingRectangle(rbox_txt, buff=0.28, color=CRIMSON,
                                    stroke_width=2)
        rbox.set_fill(WHITE, 0.0)
        rgroup = VGroup(rbox, rbox_txt).move_to(LEFT * 3.9 + UP * 0.1)

        # Small triangle on right
        sc = 0.55
        t_off = RIGHT * 3.5 + UP * 0.1
        t_top   = np.array([0.0,  1.9 * sc, 0]) + t_off
        t_left  = np.array([-2.2 * sc, -1.1 * sc, 0]) + t_off
        t_right = np.array([ 2.2 * sc, -1.1 * sc, 0]) + t_off
        te1 = Line(t_top, t_left, stroke_width=2.5, color=INK)
        te2 = Line(t_left, t_right, stroke_width=2.5, color=INK)
        te3 = Line(t_right, t_top, stroke_width=2.5, color=INK)
        tri_group = VGroup(te1, te2, te3)
        c_lbl = Text("criteria", font=SERIF, color=INK, font_size=20, slant=ITALIC)
        c_lbl.move_to(t_left + np.array([-0.6, -0.05, 0]))
        e_lbl = Text("evidence", font=SERIF, color=INK, font_size=20, slant=ITALIC)
        e_lbl.move_to(t_right + np.array([0.62, -0.05, 0]))
        j_lbl = Text("judgment", font=SERIF, color=INK, font_size=20, slant=ITALIC)
        j_lbl.move_to(t_top + np.array([0, 0.42, 0]))

        # Annotation chips: ABSENT for each corner
        a_c = LabelChip("absent", accent=CRIMSON, size=16)
        a_c.move_to(t_left + np.array([-0.6, -0.55, 0]))
        a_e = LabelChip("absent", accent=CRIMSON, size=16)
        a_e.move_to(t_right + np.array([0.62, -0.55, 0]))
        a_j = LabelChip("unusable", accent=CRIMSON, size=16)
        a_j.move_to(t_top + np.array([0, 0.9, 0]))

        self.play(FadeIn(rgroup), run_time=0.8)
        self.play(Create(tri_group), FadeIn(c_lbl), FadeIn(e_lbl), FadeIn(j_lbl),
                  run_time=0.9)
        self.play(FadeIn(a_c, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(a_e, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(a_j, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, total - 2.9))


# ---------------------------------------------------------------- B10 Review annotated --

class B10_ReviewAnnotated(Scene):
    def construct(self):
        total = DUR["B10"]

        # Review text box on left (compressed)
        rv_lines = [
            "7:45 pm, Wednesday.",
            "Three tables un-bussed.",
            "Pasta held under a heat lamp.",
            "Standard: weeknight consistency.",
            "Verdict: structural failure.",
        ]
        rv_texts = VGroup(*[Text(ln, font=SERIF, color=INK, font_size=22)
                            for ln in rv_lines])
        rv_texts.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        rbox = SurroundingRectangle(rv_texts, buff=0.22, color=INK, stroke_width=2)
        rbox.set_fill(WHITE, 0.0)
        rgroup = VGroup(rbox, rv_texts).move_to(LEFT * 3.5 + UP * 0.1)

        # Small triangle on right
        sc = 0.55
        t_off = RIGHT * 3.5 + UP * 0.1
        t_top   = np.array([0.0,  1.9 * sc, 0]) + t_off
        t_left  = np.array([-2.2 * sc, -1.1 * sc, 0]) + t_off
        t_right = np.array([ 2.2 * sc, -1.1 * sc, 0]) + t_off
        te1 = Line(t_top, t_left, stroke_width=2.5, color=INK)
        te2 = Line(t_left, t_right, stroke_width=2.5, color=INK)
        te3 = Line(t_right, t_top, stroke_width=2.5, color=INK)
        tri_group = VGroup(te1, te2, te3)

        c_lbl = Text("criteria", font=SERIF, color=INK, font_size=20, slant=ITALIC)
        c_lbl.move_to(t_left + np.array([-0.6, -0.05, 0]))
        e_lbl = Text("evidence", font=SERIF, color=INK, font_size=20, slant=ITALIC)
        e_lbl.move_to(t_right + np.array([0.62, -0.05, 0]))
        j_lbl = Text("judgment", font=SERIF, color=INK, font_size=20, slant=ITALIC)
        j_lbl.move_to(t_top + np.array([0, 0.42, 0]))

        # Annotation chips: FILLED for each corner
        f_c = LabelChip("weeknight consistency", accent=INK, size=14)
        f_c.move_to(t_left + np.array([-0.65, -0.62, 0]))
        f_e = LabelChip("pasta / tables / time", accent=INK, size=14)
        f_e.move_to(t_right + np.array([0.65, -0.62, 0]))
        f_j = LabelChip("usable verdict", accent=INK, size=14)
        f_j.move_to(t_top + np.array([0, 0.9, 0]))

        self.play(FadeIn(rgroup), run_time=0.9)
        self.play(Create(tri_group), FadeIn(c_lbl), FadeIn(e_lbl), FadeIn(j_lbl),
                  run_time=0.9)
        self.play(FadeIn(f_c, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(f_e, shift=DOWN * 0.1), run_time=0.4)
        self.play(FadeIn(f_j, shift=UP * 0.1), run_time=0.4)
        # Dot on each corner lights up
        d_c = _dot(t_left, color=INK)
        d_e = _dot(t_right, color=INK)
        d_j = _dot(t_top, color=INK)
        self.play(FadeIn(d_c, scale=1.4), FadeIn(d_e, scale=1.4),
                  FadeIn(d_j, scale=1.4), run_time=0.6)
        self.wait(max(0.5, total - 3.6))


# ---------------------------------------------------------------- B12 Diagnostic quote --

class B12_DiagnosticQuote(Scene):
    def construct(self):
        _quote_scene(self,
                     "The criteria I am using are — and they apply because the work belongs to —",
                     "the diagnostic sentence",
                     None,
                     "criteria",
                     DUR["B12"],
                     qsize=36)


# ---------------------------------------------------------------- B13 Endcard --

class B13_Endcard(Scene):
    def construct(self):
        total = DUR["B13"]
        kicker = LabelChip("WRITING", accent=CRIMSON, size=22)
        kicker.to_corner(UL, buff=0.6)
        t1 = Text("criteria + evidence + judgment", font=DISPLAY, color=INK,
                  font_size=44, weight="BOLD")
        t1.move_to(UP * 0.3)
        u = Line(t1.get_corner(DL) + DOWN * 0.14, t1.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        sub = Text("the three moves a review must make", font=SERIF, color=INK,
                   font_size=28, slant=ITALIC)
        sub.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(kicker), run_time=0.4)
        self.play(FadeIn(t1, shift=UP * 0.15), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.7)
        self.wait(max(0.5, total - 2.1))
