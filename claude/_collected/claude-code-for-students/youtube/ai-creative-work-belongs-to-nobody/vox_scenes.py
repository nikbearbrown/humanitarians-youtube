"""vox_scenes.py — Why AI Creative Work Is Beautiful and Belongs to Nobody
(ai-creative-work-belongs-to-nobody, slate cut, 16:9).

One Scene per GRAPHIC/CARD beat whose source is 'own'.
B05 is the STILL (ai slot) — no scene here.

Color law (teardown palette): CRIMSON = AI defaults / absent authorship / the void.
INK = the intent layer / the written decision / retained authorship. Single accent. Never swap.

Exclusions: no deep copyright law history, no Midjourney case details, no Brutalist spec,
no conceptual art history at length.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[3] / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403

DUR = {
    "B01": 20.0, "B02": 10.0, "B03": 22.0, "B04": 18.0,
    "B06": 20.0, "B07": 20.0, "B08": 22.0, "B09": 22.0, "B10": 19.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ---------------------------------------------------------------- helpers

def _arrow(start, end, color=INK):
    return Arrow(start, end, color=color, stroke_width=2.5,
                 max_tip_length_to_length_ratio=0.18, buff=0.06)


def _row(text, color=INK, w=6.0, h=0.54):
    box = Rectangle(width=w, height=h).set_fill(color, 0.07).set_stroke(color, 1.4)
    txt = Text(text, font=SERIF, color=color, font_size=20, slant=ITALIC)
    if txt.width > w * 0.90:
        txt.scale_to_fit_width(w * 0.90)
    txt.move_to(box)
    return VGroup(box, txt)


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("80 hours. 624 prompt iterations.", font=SERIF, color=INK,
                  font_size=36, weight="BOLD")
        t2 = Text("First prize at the state fair.", font=SERIF, color=INK,
                  font_size=36)
        t3 = Text("The Copyright Office ruled: no one made it.", font=SERIF,
                  color=CRIMSON, font_size=32, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.28).move_to(UP * 0.15)
        eye.next_to(block, UP, buff=0.6)
        u = Line(t3.get_corner(DL) + DOWN * 0.12, t3.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 2.0))


class B02_TheQuestion(Scene):
    def construct(self):
        total = DUR["B02"]
        t1 = Text("80 hours should constitute authorship.", font=SERIF,
                  color=INK, font_size=38, weight="BOLD")
        t2 = Text("Why didn't it?", font=SERIF, color=CRIMSON,
                  font_size=46, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.44).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.6)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.3))


class B03_Defaults(Scene):
    def construct(self):
        total = DUR["B03"]
        # Two columns: PROMPT (left) and DEFAULTS (right) → OUTPUT
        lhead = Text("PROMPT", font=DISPLAY, color=INK, font_size=24,
                     weight="MEDIUM").move_to(LEFT * 3.8 + UP * 2.4)
        rhead = Text("DEFAULTS", font=DISPLAY, color=CRIMSON, font_size=24,
                     weight="MEDIUM").move_to(RIGHT * 3.8 + UP * 2.4)
        note = Text("(training distribution)", font=SERIF, color=CRIMSON,
                    font_size=18, slant=ITALIC).next_to(rhead, DOWN, buff=0.1)

        prompt_box = Rectangle(width=3.0, height=1.2)
        prompt_box.set_fill(INK, 0.09).set_stroke(INK, 1.8)
        prompt_txt = Text("what you said", font=SERIF, color=INK,
                          font_size=20, slant=ITALIC)
        prompt_txt.move_to(prompt_box)
        prompt = VGroup(prompt_box, prompt_txt).move_to(LEFT * 3.8 + UP * 0.3)

        default_items = ["palette", "register", "rhythm", "structure"]
        def_chips = VGroup(*[LabelChip(it, accent=CRIMSON, size=18)
                              for it in default_items])
        def_chips.arrange(DOWN, buff=0.22).move_to(RIGHT * 3.8 + UP * 0.3)

        # Both flow into output
        out_box = Rectangle(width=3.0, height=0.8)
        out_box.set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2.0)
        out_txt = Text("THE WORK", font=DISPLAY, color=CRIMSON, font_size=22,
                       weight="MEDIUM")
        out_txt.move_to(out_box)
        output = VGroup(out_box, out_txt).move_to(DOWN * 2.2)

        arr_l = _arrow(prompt.get_bottom(), output.get_top() + LEFT * 0.8, INK)
        arr_r = _arrow(def_chips.get_bottom(), output.get_top() + RIGHT * 0.8, CRIMSON)

        self.play(FadeIn(lhead), FadeIn(rhead), FadeIn(note), run_time=0.5)
        self.play(FadeIn(prompt), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(c) for c in def_chips], lag_ratio=0.12),
                  run_time=0.7)
        self.play(Create(arr_l), Create(arr_r), FadeIn(output), run_time=0.7)
        self.wait(max(0.5, total - 2.4))


class B04_MarcusCover(Scene):
    def construct(self):
        total = DUR["B04"]
        label = Text("illustrative", font=SERIF, color=INK, font_size=18,
                     slant=ITALIC).to_corner(DR, buff=0.4)

        qs = [
            ("Why is the palette blue?", "The model picked it.", CRIMSON),
            ("Why is the layout centered?", "The model decided.", CRIMSON),
            ("Who chose the font?", "Nobody. The model chose.", CRIMSON),
        ]
        rows = VGroup()
        for q, a, color in qs:
            q_txt = Text(q, font=SERIF, color=INK, font_size=22, slant=ITALIC)
            a_txt = Text(a, font=SERIF, color=color, font_size=22, weight="BOLD")
            row = VGroup(q_txt, a_txt).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            rows.add(row)
        rows.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to(UP * 0.1)

        verdict = Text("professional. belongs to nobody.", font=SERIF,
                       color=CRIMSON, font_size=26, slant=ITALIC).to_edge(DOWN, buff=0.55)

        self.play(FadeIn(label), run_time=0.3)
        for row in rows:
            self.play(FadeIn(row), run_time=0.5)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(max(0.5, total - 0.3 - 3 * 0.5 - 0.5))


class B06_DecisionsVsIterations(Scene):
    def construct(self):
        total = DUR["B06"]
        t1 = Text("Authorship requires decisions.", font=SERIF,
                  color=INK, font_size=44, weight="BOLD")
        t2 = Text("Not iterations on a model's proposals.", font=SERIF,
                  color=CRIMSON, font_size=36, weight="BOLD")
        sub = Text("the comma you kept against the rule", font=SERIF,
                   color=INK, font_size=24, slant=ITALIC)
        block = VGroup(t1, t2, sub).arrange(DOWN, buff=0.38).move_to(ORIGIN)
        u = Line(t2.get_corner(DL) + DOWN * 0.12, t2.get_corner(DR) + DOWN * 0.12,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, total - 1.9))


class B07_IntentLayer(Scene):
    def construct(self):
        total = DUR["B07"]
        t1 = Text("The intent layer", font=SERIF, color=INK,
                  font_size=46, weight="BOLD")
        t2 = Text("is what the work is for.", font=SERIF, color=INK,
                  font_size=40)
        t3 = Text("It cannot be delegated.", font=SERIF, color=CRIMSON,
                  font_size=44, weight="BOLD")
        block = VGroup(t1, t2, t3).arrange(DOWN, buff=0.30).move_to(ORIGIN)
        u = Line(t3.get_corner(DL) + DOWN * 0.13, t3.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(t1), FadeIn(t2), run_time=0.8)
        self.play(FadeIn(t3), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.5))


class B08_TwoBuilds(Scene):
    def construct(self):
        total = DUR["B08"]
        lhead = LabelChip("BUILD ONE", accent=CRIMSON, size=22).move_to(LEFT * 3.5 + UP * 2.4)
        rhead = LabelChip("BUILD TWO", accent=INK, size=22).move_to(RIGHT * 3.5 + UP * 2.4)

        l1 = _row("one prompt", CRIMSON, w=3.8)
        l2 = _row("Claude's defaults: tone, shape, commands", CRIMSON, w=3.8)
        l3 = _row("polished — not his", CRIMSON, w=3.8)
        left_col = VGroup(l1, l2, l3).arrange(DOWN, buff=0.28)
        left_col.move_to(LEFT * 3.5 + DOWN * 0.2)

        r1 = _row("three files written first", INK, w=3.8)
        r2 = _row("every decision traceable", INK, w=3.8)
        r3 = _row("same Claude — different authorship", INK, w=3.8)
        right_col = VGroup(r1, r2, r3).arrange(DOWN, buff=0.28)
        right_col.move_to(RIGHT * 3.5 + DOWN * 0.2)

        div = Line(UP * 3.0, DOWN * 2.6, color=HAIRLINE, stroke_width=1.3)

        self.play(FadeIn(div), FadeIn(lhead), FadeIn(rhead), run_time=0.5)
        for la, ra in zip(left_col, right_col):
            self.play(FadeIn(la), FadeIn(ra), run_time=0.45)
        self.wait(max(0.5, total - 0.5 - 3 * 0.45))


class B09_ThreeFiles(Scene):
    def construct(self):
        total = DUR["B09"]
        head = Text("Before Claude touches the file:", font=DISPLAY, color=INK,
                    font_size=24, weight="MEDIUM").to_edge(UP, buff=0.6)

        # Three nested rectangles
        outer = Rectangle(width=10.0, height=5.0).set_fill(INK, 0.04).set_stroke(INK, 1.4)
        middle = Rectangle(width=7.6, height=3.6).set_fill(INK, 0.06).set_stroke(INK, 1.6)
        inner = Rectangle(width=5.2, height=2.2).set_fill(CRIMSON, 0.10).set_stroke(CRIMSON, 2.0)
        outer.move_to(DOWN * 0.1)
        middle.move_to(DOWN * 0.1)
        inner.move_to(DOWN * 0.1)

        ol = Text("CLAUDE.md — what it is made of", font=DISPLAY, color=INK,
                  font_size=18, weight="MEDIUM").move_to(outer.get_top() + DOWN * 0.28)
        ml = Text("DESIGN.md — what it looks like", font=DISPLAY, color=INK,
                  font_size=18, weight="MEDIUM").move_to(middle.get_top() + DOWN * 0.26)
        il = Text("INTENT — what it is for", font=DISPLAY, color=CRIMSON,
                  font_size=20, weight="MEDIUM").move_to(inner)

        self.play(FadeIn(head), run_time=0.4)
        self.play(Create(outer), FadeIn(ol), run_time=0.7)
        self.play(Create(middle), FadeIn(ml), run_time=0.6)
        self.play(Create(inner), FadeIn(il), run_time=0.6)
        self.wait(max(0.5, total - 2.3))


class B10_End(Scene):
    def construct(self):
        total = DUR["B10"]
        eye = Text("CLAUDE CODE", font=DISPLAY, color=CRIMSON, font_size=22,
                   weight="MEDIUM")
        t1 = Text("AI handles technical execution.", font=SERIF, color=INK,
                  font_size=42, weight="BOLD")
        t2 = Text("You keep creative judgment.", font=SERIF, color=INK,
                  font_size=42, weight="BOLD")
        block = VGroup(t1, t2).arrange(DOWN, buff=0.28).move_to(UP * 0.15)
        eye.next_to(block, UP, buff=0.6)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.7)
        self.wait(max(0.5, total - 1.9))
