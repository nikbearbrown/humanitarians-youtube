"""scenes.py — portrait (9:16, ±2.25 x, ±4.0 y) Manim scenes
for 'What is inside the Brutalist agentic system exactly?' SHORT.

One class per GRAPHIC beat in the short beat sheet.
Beats: B01, B02, B04, B06, B07, B09B.
"""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "runtime" / "manim"))
from animated_graphics import *

GROUND   = "#FFFFFF"
INK      = "#2A1A0E"
CRIMSON  = "#C8102E"
SLATE    = "#545454"
HAIRLINE = "#D4D4D4"
GOLD_FILL = "#F6D8DC"


def _dur(bid):
    bs = pathlib.Path(__file__).parent / "beat_sheet.json"
    if not bs.exists():
        return 0.0
    for b in json.loads(bs.read_text()).get("beats", []):
        if b["beat_id"] == bid:
            return float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0.0)
    return 0.0


# ══════════════════════════════════════════════════════════════
# B01 — CASCADE FLOW portrait (≈9s)
# Vertical top-to-bottom flow; portrait frame ±2.25x / ±4.0y
# ══════════════════════════════════════════════════════════════
class B01_CascadeFlow(Scene):
    def construct(self):
        def make_box(label, accent=INK, w=3.8, h=0.6):
            box = Rectangle(width=w, height=h, fill_color=GROUND, fill_opacity=1,
                            stroke_color=accent, stroke_width=2.5)
            lbl = Text(label, font=MONO, color=INK, font_size=18, weight=BOLD)
            lbl.move_to(box.get_center())
            return VGroup(box, lbl)

        bs_box   = make_box("beat_sheet.json", CRIMSON, w=3.6)
        orch_box = make_box("orchestrator")
        doer_box = make_box("doer")
        el_box   = make_box("ElevenLabs", w=1.7)
        mn_box   = make_box("Manim", w=1.5)
        comp_box = make_box("compile")
        mp4_box  = make_box("mp4", CRIMSON, w=1.6)

        # positions: vertical cascade (y from top to bottom)
        bs_box.move_to(UP * 3.2)
        orch_box.move_to(UP * 2.2)
        doer_box.move_to(UP * 1.2)
        el_box.move_to(UP * 0.0 + LEFT * 1.0)
        mn_box.move_to(UP * 0.0 + RIGHT * 1.0)
        comp_box.move_to(DOWN * 1.2)
        mp4_box.move_to(DOWN * 2.2)

        contract = Text("CONTRACT", font=DISPLAY, color=CRIMSON, font_size=13, weight=BOLD)
        contract.next_to(bs_box, UP, buff=0.12)

        def arr_v(top_mob, bot_mob):
            return Arrow(top_mob.get_bottom() + DOWN * 0.05,
                         bot_mob.get_top() + UP * 0.05,
                         stroke_color=INK, stroke_width=2, tip_length=0.18, buff=0)

        a1 = arr_v(bs_box, orch_box)
        a2 = arr_v(orch_box, doer_box)
        bel = Arrow(doer_box.get_bottom() + DOWN * 0.05,
                    el_box.get_top() + UP * 0.05,
                    stroke_color=INK, stroke_width=2, tip_length=0.16, buff=0)
        bmn = Arrow(doer_box.get_bottom() + DOWN * 0.05,
                    mn_box.get_top() + UP * 0.05,
                    stroke_color=INK, stroke_width=2, tip_length=0.16, buff=0)
        mel = Arrow(el_box.get_bottom() + DOWN * 0.05,
                    comp_box.get_top() + UP * 0.05,
                    stroke_color=INK, stroke_width=2, tip_length=0.16, buff=0)
        mmn = Arrow(mn_box.get_bottom() + DOWN * 0.05,
                    comp_box.get_top() + UP * 0.05,
                    stroke_color=INK, stroke_width=2, tip_length=0.16, buff=0)
        a3  = arr_v(comp_box, mp4_box)

        self.play(FadeIn(bs_box), FadeIn(contract), run_time=0.5)
        self.play(GrowArrow(a1), run_time=0.3)
        self.play(FadeIn(orch_box, shift=DOWN * 0.1), run_time=0.4)
        self.play(GrowArrow(a2), run_time=0.3)
        self.play(FadeIn(doer_box, shift=DOWN * 0.1), run_time=0.4)
        self.play(GrowArrow(bel), GrowArrow(bmn), run_time=0.4)
        self.play(FadeIn(el_box), FadeIn(mn_box), run_time=0.5)
        self.play(GrowArrow(mel), GrowArrow(mmn), run_time=0.4)
        self.play(FadeIn(comp_box, shift=DOWN * 0.1), run_time=0.4)
        self.play(GrowArrow(a3), FadeIn(mp4_box, shift=DOWN * 0.1), run_time=0.4)
        self.wait(max(0.5, _dur("B01") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B02 — TWO INPUTS COMPARE portrait (≈9s)
# Two cards stacked vertically
# ══════════════════════════════════════════════════════════════
class B02_TwoInputsCompare(Scene):
    def construct(self):
        # SPECIFIES card (top)
        spec_header = Text("SPECIFIES", font=DISPLAY, color=INK, font_size=20, weight=BOLD)
        spec_input  = Text("fps = 24", font=MONO, color=INK, font_size=26, weight=BOLD)
        eq          = Text("=", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        spec_out    = Text("24 frames/sec · guaranteed", font=SERIF, color=INK, font_size=16)
        spec_stack  = VGroup(spec_input, eq, spec_out).arrange(DOWN, buff=0.18)
        spec_box    = Rectangle(width=4.0, height=2.2, fill_color=GROUND, fill_opacity=1,
                                stroke_color=INK, stroke_width=2.5)
        spec_stack.move_to(spec_box.get_center())
        spec_header.next_to(spec_box, UP, buff=0.12)
        spec_group  = VGroup(spec_box, spec_stack, spec_header).move_to(UP * 1.8)

        # INFLUENCES card (bottom)
        inf_header = Text("INFLUENCES", font=DISPLAY, color=SLATE, font_size=20, weight=BOLD)
        inf_input  = Text("register: Teardown", font=MONO, color=INK, font_size=17, weight=BOLD)
        tilde      = Text("~  model selects", font=DISPLAY, color=SLATE, font_size=20)
        inf_out    = Text("one biased output", font=SERIF, color=CRIMSON, font_size=16, slant=ITALIC)
        inf_stack  = VGroup(inf_input, tilde, inf_out).arrange(DOWN, buff=0.18)
        inf_box    = Rectangle(width=4.0, height=2.2, fill_color=GROUND, fill_opacity=1,
                               stroke_color=SLATE, stroke_width=2.5)
        inf_stack.move_to(inf_box.get_center())
        inf_header.next_to(inf_box, UP, buff=0.12)
        inf_group  = VGroup(inf_box, inf_stack, inf_header).move_to(DOWN * 1.5)

        self.play(FadeIn(spec_group, shift=DOWN * 0.15), run_time=0.8)
        self.wait(0.8)
        self.play(FadeIn(inf_group, shift=UP * 0.15), run_time=0.8)
        self.wait(max(0.5, _dur("B02") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B04 — UNDERDETERMINATION portrait (≈8s)
# Two stacked panels: OVERDETERMINED (top) / UNDERDETERMINED (bottom)
# ══════════════════════════════════════════════════════════════
class B04_UnderdeterminationDiagram(Scene):
    def construct(self):
        divider = Line(LEFT * 2.2, RIGHT * 2.2, stroke_color=HAIRLINE, stroke_width=1.5)
        divider.move_to(ORIGIN)

        # ── TOP: overdetermined
        od_header = Text("OVERDETERMINED", font=DISPLAY, color=INK, font_size=17, weight=BOLD)
        od_header.move_to(UP * 3.0)

        od_in_box = Rectangle(width=2.0, height=0.6, fill_color=GOLD_FILL, fill_opacity=1,
                              stroke_color=CRIMSON, stroke_width=2.5)
        od_in_lbl = Text("#C8102E", font=MONO, color=INK, font_size=17, weight=BOLD)
        od_in_lbl.move_to(od_in_box)
        od_in = VGroup(od_in_box, od_in_lbl).move_to(UP * 2.1)

        od_arrow = Arrow(od_in.get_bottom() + DOWN * 0.05,
                         od_in.get_bottom() + DOWN * 0.9,
                         stroke_color=INK, stroke_width=2.5, tip_length=0.2, buff=0)

        od_out_box = Rectangle(width=2.6, height=0.6, fill_color=GROUND, fill_opacity=1,
                               stroke_color=INK, stroke_width=2)
        od_out_lbl = Text("one right answer", font=SERIF, color=INK, font_size=16)
        od_out_lbl.move_to(od_out_box)
        od_out = VGroup(od_out_box, od_out_lbl)
        od_out.move_to(od_in.get_center() + DOWN * 1.4)

        # ── BOTTOM: underdetermined
        ud_header = Text("UNDERDETERMINED", font=DISPLAY, color=SLATE, font_size=17, weight=BOLD)
        ud_header.move_to(DOWN * 0.4)

        ud_in_box = Rectangle(width=3.0, height=0.6, fill_color=GROUND, fill_opacity=1,
                              stroke_color=SLATE, stroke_width=2.5)
        ud_in_lbl = Text("register: Teardown", font=MONO, color=INK, font_size=14, weight=BOLD)
        ud_in_lbl.move_to(ud_in_box)
        ud_in = VGroup(ud_in_box, ud_in_lbl).move_to(DOWN * 1.3)

        ud_out_lbl = Text("model selects\nfrom distribution", font=SERIF,
                          color=CRIMSON, font_size=16, slant=ITALIC, line_spacing=0.85)
        ud_out_lbl.move_to(DOWN * 2.6)

        footer = Text("Not a temperature problem.", font=SERIF,
                      color=INK, font_size=15, slant=ITALIC)
        footer.move_to(DOWN * 3.6)

        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(od_header), FadeIn(od_in), run_time=0.5)
        self.play(GrowArrow(od_arrow), FadeIn(od_out), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(ud_header), FadeIn(ud_in), run_time=0.5)
        self.play(FadeIn(ud_out_lbl), run_time=0.5)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.4)
        self.wait(max(0.5, _dur("B04") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B06 — TWO AXES MATRIX portrait (≈10s)
# 2×2 matrix — narrower cells to fit ±2.25x
# ══════════════════════════════════════════════════════════════
class B06_TwoAxesMatrix(Scene):
    def construct(self):
        h_line = Line(LEFT * 2.2, RIGHT * 2.2, stroke_color=INK, stroke_width=2.5)
        v_line = Line(UP * 3.5, DOWN * 3.5, stroke_color=INK, stroke_width=2.5)
        h_line.move_to(ORIGIN)
        v_line.move_to(ORIGIN)

        lbl_spec   = Text("SPECIFIES", font=DISPLAY, color=INK, font_size=16, weight=BOLD)
        lbl_infl   = Text("INFLUENCES", font=DISPLAY, color=SLATE, font_size=16, weight=BOLD)
        lbl_input  = Text("INPUT", font=DISPLAY, color=INK, font_size=16, weight=BOLD)
        lbl_artif  = Text("ARTIFACT", font=DISPLAY, color=INK, font_size=16, weight=BOLD)

        lbl_spec.move_to(LEFT * 1.1 + UP * 3.0)
        lbl_infl.move_to(LEFT * 1.1 + DOWN * 3.0)
        lbl_input.move_to(LEFT * 1.1 + UP * 3.8)
        lbl_artif.move_to(RIGHT * 1.1 + UP * 3.8)

        # Each quadrant: Rectangle bg + text stack so Gate A sees distinct shapes
        def quad_card(lines, pos, col=INK, accent=HAIRLINE):
            bg = Rectangle(width=1.9, height=1.5, fill_color=GROUND, fill_opacity=0.5,
                           stroke_color=accent, stroke_width=1.2)
            txt = VGroup(*[Text(l, font=MONO, color=col, font_size=13) for l in lines])
            txt.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            bg.move_to(pos)
            txt.move_to(pos)
            return VGroup(bg, txt)

        tl = quad_card(["voice_id", "fps=24"], LEFT * 1.1 + UP * 1.5, INK)
        bl = quad_card(["persona", "register"], LEFT * 1.1 + DOWN * 1.5, SLATE)
        tr = quad_card(["beat_sheet"], RIGHT * 1.1 + UP * 1.5, INK)
        br = quad_card(["mp4", "taste-judged"], RIGHT * 1.1 + DOWN * 1.5, CRIMSON, CRIMSON)

        self.play(Create(h_line), Create(v_line), run_time=0.4)
        self.play(FadeIn(lbl_spec), FadeIn(lbl_infl),
                  FadeIn(lbl_input), FadeIn(lbl_artif), run_time=0.5)
        self.play(FadeIn(tl, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(bl, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(tr, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(br, shift=LEFT * 0.1), run_time=0.5)
        self.wait(max(0.5, _dur("B06") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B07 — INPUT STACK LAYERS portrait (≈7s)
# 6 horizontal bars, full portrait width
# ══════════════════════════════════════════════════════════════
class B07_InputStackLayers(Scene):
    def construct(self):
        layers = [
            ("HUMAN",            INK,      4.0),
            ("LLM",              INK,      3.7),
            ("CONDITIONING TEXT",SLATE,    3.3),
            ("AGENT",            SLATE,    2.9),
            ("PARAMETERS",       SLATE,    2.5),
            ("SCRIPTS",          HAIRLINE, 2.1),
        ]
        top_y   = 2.9
        spacing = 0.95
        BAR_H   = 0.65

        bar_groups = []
        for i, (name, col, bar_w) in enumerate(layers):
            y = top_y - i * spacing
            fill   = col if col != HAIRLINE else GROUND
            stroke = col if col != HAIRLINE else SLATE
            bar = Rectangle(width=bar_w, height=BAR_H, fill_color=fill, fill_opacity=0.15,
                            stroke_color=stroke, stroke_width=2)
            bar.move_to(UP * y)
            name_txt = Text(name, font=DISPLAY, color=stroke if col != INK else INK,
                            font_size=14, weight=BOLD)
            name_txt.move_to(bar.get_center())
            bar_groups.append(VGroup(bar, name_txt))

        top_lbl = Text("MOST INFLUENCING ↑", font=DISPLAY, color=CRIMSON, font_size=12, weight=BOLD)
        top_lbl.move_to(UP * 3.6)
        bot_lbl = Text("MOST SPECIFYING ↓", font=DISPLAY, color=INK, font_size=12, weight=BOLD)
        bot_lbl.move_to(DOWN * 2.8)

        self.play(FadeIn(top_lbl), FadeIn(bot_lbl), run_time=0.4)
        for g in bar_groups:
            self.play(FadeIn(g, shift=RIGHT * 0.1), run_time=0.35)
        self.wait(max(0.5, _dur("B07") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B09B — ONE WRITER MANY COSTUMES portrait (≈8s)
# Doer circle at center top, costume list below, wrong model at bottom
# ══════════════════════════════════════════════════════════════
class B09B_OneWriterManyCostumes(Scene):
    def construct(self):
        doer_circle = Circle(radius=0.85, fill_color=GROUND, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
        doer_circle.move_to(UP * 2.5)
        doer_lbl = Text("doer", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        doer_lbl.move_to(doer_circle.get_center())
        doer_sub = Text("LLM + goal + tools", font=SERIF, color=SLATE, font_size=13)
        doer_sub.next_to(doer_circle, DOWN, buff=0.2)

        costumes = [
            "persona: script-writer",
            "register: Teardown",
            "brand: NikBearBrown",
        ]
        c_labels = [Text(c, font=MONO, color=SLATE, font_size=14) for c in costumes]
        c_stack = VGroup(*c_labels).arrange(DOWN, buff=0.3)
        c_stack.move_to(UP * 0.6)

        arrows = []
        for lbl in c_labels:
            arrows.append(Arrow(lbl.get_top() + UP * 0.05,
                                doer_circle.get_bottom() + DOWN * 0.05,
                                stroke_color=SLATE, stroke_width=1.5, tip_length=0.14, buff=0))

        # Wrong model (3 circles row, crossed out)
        wrong_circles = []
        for i in range(3):
            wc = Circle(radius=0.38, fill_color=GROUND, fill_opacity=1,
                        stroke_color=HAIRLINE, stroke_width=1.5)
            wc.move_to(DOWN * 2.2 + LEFT * 1.1 + RIGHT * i * 1.1)
            wrong_circles.append(wc)
        w_grp = VGroup(*wrong_circles)
        w_hdr = Text("wrong model", font=SERIF, color=SLATE, font_size=13, slant=ITALIC)
        w_hdr.next_to(w_grp, UP, buff=0.2)
        w_x1 = Line(w_grp.get_corner(UL), w_grp.get_corner(DR), stroke_color=CRIMSON, stroke_width=4)
        w_x2 = Line(w_grp.get_corner(UR), w_grp.get_corner(DL), stroke_color=CRIMSON, stroke_width=4)
        w_x1._qc_intentional = True
        w_x2._qc_intentional = True

        footer = Text("one writer  ·  many costumes", font=SERIF,
                      color=INK, font_size=15, slant=ITALIC)
        footer.move_to(DOWN * 3.4)

        self.play(FadeIn(doer_circle), FadeIn(doer_lbl), run_time=0.5)
        self.play(FadeIn(doer_sub), run_time=0.3)
        for lbl, arr in zip(c_labels, arrows):
            self.play(FadeIn(lbl), GrowArrow(arr), run_time=0.35)
        self.wait(0.3)
        self.play(FadeIn(w_grp), FadeIn(w_hdr), run_time=0.5)
        self.play(Create(w_x1), Create(w_x2), run_time=0.4)
        self.play(FadeIn(footer), run_time=0.4)
        self.wait(max(0.5, _dur("B09B") - getattr(self, 'time', 0.0)))
