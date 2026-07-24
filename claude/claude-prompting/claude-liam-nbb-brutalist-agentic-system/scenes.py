"""scenes.py — Manim scenes for 'What is inside the Brutalist agentic system exactly?'
(nbb-brutalist-agentic-system)

One Scene subclass per GRAPHIC beat with shot.source == 'own'.
Beats: B01, B02, B04, B06, B07, B09, B09B, B11, B12, B14.
Palette: teardown — flat white GROUND, INK, CRIMSON (one accent), SLATE.
"""
import sys, pathlib, json
# locate brutalist-art/runtime/manim by walking up (layout-proof)
for _a in pathlib.Path(__file__).resolve().parents:
    _m = _a / "brutalist-art" / "runtime" / "manim"
    if (_m / "animated_graphics.py").is_file():
        sys.path.insert(0, str(_m)); break
from animated_graphics import *

# ── teardown palette
GROUND   = "#FFFFFF"
INK      = "#2A1A0E"
CRIMSON  = "#C8102E"
SLATE    = "#545454"
HAIRLINE = "#D4D4D4"
GOLD_FILL = "#F6D8DC"   # 14% wash of crimson — fill only, never text


def _dur(bid):
    bs = pathlib.Path(__file__).parent / "beat_sheet.json"
    if not bs.exists():
        return 0.0
    for b in json.loads(bs.read_text()).get("beats", []):
        if b["beat_id"] == bid:
            return float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0.0)
    return 0.0


# ══════════════════════════════════════════════════════════════
# B01 — CASCADE FLOW (18.16s)
# beat_sheet.json → orchestrator → doer → [ElevenLabs | Manim] → compile → mp4
# ══════════════════════════════════════════════════════════════
class B01_CascadeFlow(Scene):
    def construct(self):
        # ── boxes (small, fit in frame)
        def make_box(label, sub=None, accent=INK, w=2.0, h=0.65):
            lbl = Text(label, font=MONO, color=INK, font_size=18, weight=BOLD)
            box = Rectangle(width=w, height=h, fill_color=GROUND, fill_opacity=1,
                            stroke_color=accent, stroke_width=2.5)
            lbl.move_to(box.get_center())
            if sub:
                s = Text(sub, font=MONO, color=SLATE, font_size=13)
                s.next_to(box, DOWN, buff=0.12)
                return VGroup(box, lbl), s
            return VGroup(box, lbl), None

        bs_box, _ = make_box("beat_sheet.json", w=2.4, accent=CRIMSON)
        orch_box, _ = make_box("orchestrator")
        doer_box, _ = make_box("doer")
        el_box, el_sub   = make_box("ElevenLabs", "voice_id — exact", w=2.2)
        manim_box, mn_sub = make_box("Manim", "fps=24 — exact", w=2.2)
        compile_box, _ = make_box("compile")
        mp4_box, _ = make_box("mp4", accent=CRIMSON, w=1.4)

        # CONTRACT label above beat_sheet
        contract_lbl = Text("CONTRACT", font=DISPLAY, color=CRIMSON,
                            font_size=13, weight=BOLD)

        # taste-judged label below mp4
        taste_lbl = Text("taste-judged", font=SERIF, color=CRIMSON,
                         font_size=13, slant=ITALIC)

        # ── positions (horizontal cascade, two arms for the branch)
        bs_box.move_to(LEFT * 5.0)
        orch_box.move_to(LEFT * 2.6)
        doer_box.move_to(ORIGIN)
        el_box.move_to(RIGHT * 2.6 + UP * 1.2)
        manim_box.move_to(RIGHT * 2.6 + DOWN * 1.2)
        compile_box.move_to(RIGHT * 4.9)
        mp4_box.move_to(RIGHT * 6.3)

        contract_lbl.next_to(bs_box, UP, buff=0.12)
        taste_lbl.next_to(mp4_box, DOWN, buff=0.12)
        if el_sub: el_sub.next_to(el_box, DOWN, buff=0.12)
        if mn_sub: mn_sub.next_to(manim_box, DOWN, buff=0.12)

        # ── arrows
        def arr(start_mob, end_mob):
            s = start_mob.get_right() + RIGHT * 0.08
            e = end_mob.get_left() + LEFT * 0.08
            return Arrow(s, e, stroke_color=INK, stroke_width=2,
                         tip_length=0.18, buff=0)

        a1 = arr(bs_box, orch_box)
        a2 = arr(orch_box, doer_box)

        # branch arrows from doer to ElevenLabs and Manim
        branch_el = Arrow(doer_box.get_right() + RIGHT * 0.08,
                          el_box.get_left() + LEFT * 0.08,
                          stroke_color=INK, stroke_width=2, tip_length=0.18, buff=0)
        branch_mn = Arrow(doer_box.get_right() + RIGHT * 0.08,
                          manim_box.get_left() + LEFT * 0.08,
                          stroke_color=INK, stroke_width=2, tip_length=0.18, buff=0)

        merge_el = Arrow(el_box.get_right() + RIGHT * 0.08,
                         compile_box.get_left() + LEFT * 0.08,
                         stroke_color=INK, stroke_width=2, tip_length=0.18, buff=0)
        merge_mn = Arrow(manim_box.get_right() + RIGHT * 0.08,
                         compile_box.get_left() + LEFT * 0.08,
                         stroke_color=INK, stroke_width=2, tip_length=0.18, buff=0)

        a_compile = arr(compile_box, mp4_box)

        # ── reveal sequence
        self.play(FadeIn(bs_box, shift=RIGHT * 0.15), FadeIn(contract_lbl), run_time=0.6)
        self.play(GrowArrow(a1), run_time=0.4)
        self.play(FadeIn(orch_box, shift=RIGHT * 0.15), run_time=0.5)
        self.play(GrowArrow(a2), run_time=0.4)
        self.play(FadeIn(doer_box, shift=RIGHT * 0.15), run_time=0.5)
        self.wait(0.3)
        self.play(GrowArrow(branch_el), GrowArrow(branch_mn), run_time=0.5)
        self.play(FadeIn(el_box), FadeIn(manim_box), run_time=0.6)
        if el_sub: self.play(FadeIn(el_sub), FadeIn(mn_sub), run_time=0.4)
        self.play(GrowArrow(merge_el), GrowArrow(merge_mn), run_time=0.5)
        self.play(FadeIn(compile_box, shift=RIGHT * 0.15), run_time=0.5)
        self.play(GrowArrow(a_compile), run_time=0.4)
        self.play(FadeIn(mp4_box, shift=RIGHT * 0.15), FadeIn(taste_lbl), run_time=0.5)
        self.wait(max(0.5, _dur("B01") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B02 — TWO INPUTS COMPARE (18.65s)
# fps=24 (SPECIFIES) vs register:Teardown (INFLUENCES)
# ══════════════════════════════════════════════════════════════
class B02_TwoInputsCompare(Scene):
    def construct(self):
        # ── left card: SPECIFIES
        # Use explicit Rectangle (not surround_box) so Gate A can track it as a shape
        spec_header = Text("SPECIFIES", font=DISPLAY, color=INK,
                           font_size=20, weight=BOLD)
        spec_input  = Text("fps = 24", font=MONO, color=INK, font_size=28, weight=BOLD)
        eq_sign     = Text("=", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        spec_output = Text("output: 24 frames/sec\nguaranteed · reproducible",
                           font=SERIF, color=INK, font_size=18, line_spacing=0.9)
        spec_stack  = VGroup(spec_input, eq_sign, spec_output).arrange(DOWN, buff=0.22)
        spec_box    = Rectangle(width=3.4, height=2.6, fill_color=GROUND, fill_opacity=1,
                                stroke_color=INK, stroke_width=2.5)
        spec_box.move_to(LEFT * 3.3)
        spec_stack.move_to(spec_box.get_center())
        spec_header.next_to(spec_box, UP, buff=0.18)
        spec_group  = VGroup(spec_box, spec_stack, spec_header)

        # ── right card: INFLUENCES
        inf_header  = Text("INFLUENCES", font=DISPLAY, color=SLATE,
                           font_size=20, weight=BOLD)
        inf_input   = Text("register: Teardown", font=MONO, color=INK, font_size=22, weight=BOLD)
        tilde       = Text("~", font=DISPLAY, color=SLATE, font_size=40)
        opt1 = Text("output A", font=SERIF, color=HAIRLINE, font_size=17)
        opt2 = Text("output B", font=SERIF, color=HAIRLINE, font_size=17)
        opt3 = Text("output C", font=SERIF, color=HAIRLINE, font_size=17)
        opts = VGroup(opt1, opt2, opt3).arrange(DOWN, buff=0.12)
        inf_stack   = VGroup(inf_input, tilde, opts).arrange(DOWN, buff=0.22)
        inf_box     = Rectangle(width=3.4, height=2.6, fill_color=GROUND, fill_opacity=1,
                                stroke_color=SLATE, stroke_width=2.5)
        inf_box.move_to(RIGHT * 3.3)
        inf_stack.move_to(inf_box.get_center())
        inf_header.next_to(inf_box, UP, buff=0.18)
        inf_group   = VGroup(inf_box, inf_stack, inf_header)

        # highlighted opt1 + selection arrow
        opt1_hl   = opt1.copy().set_color(INK)
        sel_start = inf_box.get_center() + LEFT * 1.3 + DOWN * 0.6
        sel_end   = inf_box.get_center() + LEFT * 0.65 + DOWN * 0.6
        sel_arrow = Arrow(sel_start, sel_end,
                          stroke_color=CRIMSON, stroke_width=2, tip_length=0.16, buff=0)
        sel_lbl   = Text("model selects", font=SERIF, color=CRIMSON,
                         font_size=14, slant=ITALIC)
        sel_lbl.next_to(sel_arrow, UP, buff=0.08)

        # ── footer
        footer = Text("Two inputs.  Completely different structures.",
                      font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        footer.to_edge(DOWN, buff=0.55)

        # ── animate: left card first, then right, then footer
        self.play(FadeIn(spec_group, shift=RIGHT * 0.2), run_time=0.9)
        self.wait(1.5)
        self.play(FadeIn(inf_group, shift=LEFT * 0.2), run_time=0.9)
        self.wait(0.8)
        self.play(Transform(opt1, opt1_hl), run_time=0.4)
        self.play(GrowArrow(sel_arrow), FadeIn(sel_lbl), run_time=0.6)
        self.wait(0.8)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, _dur("B02") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B04 — UNDERDETERMINATION DIAGRAM (16.3s)
# Overdetermined (hex code → one answer) vs Underdetermined (persona → model selects)
# ══════════════════════════════════════════════════════════════
class B04_UnderdeterminationDiagram(Scene):
    def construct(self):
        # Divider stops at DOWN*2.4 so the footer below doesn't cross it
        divider = Line(UP * 3.2, DOWN * 2.4, stroke_color=HAIRLINE, stroke_width=1.5)

        # ── LEFT: overdetermined
        left_header = Text("OVERDETERMINED", font=DISPLAY, color=INK,
                           font_size=18, weight=BOLD)
        left_header.move_to(LEFT * 3.2 + UP * 2.8)

        input_box_l = Rectangle(width=2.0, height=0.65, fill_color=GOLD_FILL, fill_opacity=1,
                                 stroke_color=CRIMSON, stroke_width=2.5)
        input_lbl_l = Text("#C8102E", font=MONO, color=INK, font_size=18, weight=BOLD)
        input_lbl_l.move_to(input_box_l)
        input_l = VGroup(input_box_l, input_lbl_l).move_to(LEFT * 3.2 + UP * 1.5)

        arrow_l = Arrow(input_l.get_bottom() + DOWN * 0.05,
                        input_l.get_bottom() + DOWN * 1.2,
                        stroke_color=INK, stroke_width=2.5, tip_length=0.22, buff=0)

        output_box_l = Rectangle(width=2.4, height=0.65, fill_color=GROUND, fill_opacity=1,
                                  stroke_color=INK, stroke_width=2)
        output_lbl_l = Text("one right answer", font=SERIF, color=INK, font_size=18)
        output_lbl_l.move_to(output_box_l)
        output_l = VGroup(output_box_l, output_lbl_l)
        output_l.move_to(input_l.get_center() + DOWN * 1.8)

        sub_l = Text("hex code", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        sub_l.next_to(output_l, DOWN, buff=0.3)

        # ── RIGHT: underdetermined
        right_header = Text("UNDERDETERMINED", font=DISPLAY, color=SLATE,
                            font_size=18, weight=BOLD)
        right_header.move_to(RIGHT * 3.2 + UP * 2.8)

        # Wider box (3.0) and smaller font (14) so label fits without overflowing
        input_box_r = Rectangle(width=3.0, height=0.65, fill_color=GROUND, fill_opacity=1,
                                 stroke_color=SLATE, stroke_width=2.5)
        input_lbl_r = Text("register: Teardown", font=MONO, color=INK, font_size=14, weight=BOLD)
        input_lbl_r.move_to(input_box_r)
        input_r = VGroup(input_box_r, input_lbl_r).move_to(RIGHT * 3.2 + UP * 1.5)

        # five output boxes, fan out (tighter spread ±1.2 to avoid going off-frame)
        output_items_r = []
        offsets = [LEFT * 1.2, LEFT * 0.6, ORIGIN, RIGHT * 0.6, RIGHT * 1.2]
        for i, off in enumerate(offsets):
            ob = Rectangle(width=0.85, height=0.55, fill_color=GROUND, fill_opacity=1,
                           stroke_color=HAIRLINE, stroke_width=1.5)
            lb = Text(f"out {i+1}", font=MONO, color=HAIRLINE, font_size=13)
            lb.move_to(ob)
            g = VGroup(ob, lb).move_to(RIGHT * 3.2 + DOWN * 1.0 + off)
            output_items_r.append(g)

        # arrows fanning from input to each output
        fan_arrows = []
        for g in output_items_r:
            fa = Arrow(input_r.get_bottom() + DOWN * 0.05,
                       g.get_top() + UP * 0.05,
                       stroke_color=HAIRLINE, stroke_width=1.5, tip_length=0.15, buff=0)
            fan_arrows.append(fa)

        # highlight center output + crimson arrow; label goes below the center box
        center_out = output_items_r[2]
        sel_box = center_out[0].copy().set_stroke(CRIMSON, 3)
        sel_txt = center_out[1].copy().set_color(INK)
        sel_arrow_r = Arrow(input_r.get_bottom() + DOWN * 0.05,
                            center_out.get_top() + UP * 0.05,
                            stroke_color=CRIMSON, stroke_width=2.5, tip_length=0.2, buff=0)
        sel_lbl_r = Text("model selects", font=SERIF, color=CRIMSON, font_size=14, slant=ITALIC)
        sel_lbl_r.next_to(center_out, DOWN, buff=0.22)

        sub_r = Text("persona", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        sub_r.next_to(VGroup(*output_items_r), DOWN, buff=0.5)

        # Footer sits below where divider ends so it doesn't cross the divider stroke
        footer = Text("Not a temperature problem.  A structure problem.",
                      font=SERIF, color=INK, font_size=18, slant=ITALIC)
        footer.move_to(DOWN * 3.0)

        # ── animate
        self.play(Create(divider), run_time=0.3)
        self.play(FadeIn(left_header), FadeIn(right_header), run_time=0.5)
        self.play(FadeIn(input_l), FadeIn(input_r), run_time=0.6)
        self.play(GrowArrow(arrow_l), run_time=0.5)
        self.play(FadeIn(output_l), run_time=0.5)
        self.play(FadeIn(sub_l), run_time=0.3)
        self.wait(0.5)
        self.play(*[GrowArrow(fa) for fa in fan_arrows], run_time=0.7)
        self.play(*[FadeIn(g) for g in output_items_r], run_time=0.5)
        self.wait(0.5)
        self.play(Transform(center_out[0], sel_box),
                  Transform(center_out[1], sel_txt),
                  Transform(fan_arrows[2], sel_arrow_r),
                  FadeIn(sel_lbl_r), run_time=0.6)
        self.play(FadeIn(sub_r), run_time=0.3)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, _dur("B04") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B06 — TWO AXES MATRIX (18.63s)
# 2×2: SPECIFIES/INFLUENCES × INPUT/ARTIFACT
# ══════════════════════════════════════════════════════════════
class B06_TwoAxesMatrix(Scene):
    def construct(self):
        # ── axis lines
        h_line = Line(LEFT * 6, RIGHT * 6, stroke_color=INK, stroke_width=2.5)
        v_line = Line(UP * 3.5, DOWN * 3.5, stroke_color=INK, stroke_width=2.5)
        h_line.move_to(ORIGIN)
        v_line.move_to(ORIGIN)

        # ── axis labels
        lbl_specifies = Text("SPECIFIES", font=DISPLAY, color=INK,
                             font_size=18, weight=BOLD)
        lbl_influences = Text("INFLUENCES", font=DISPLAY, color=SLATE,
                              font_size=18, weight=BOLD)
        lbl_input    = Text("INPUT", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        lbl_artifact = Text("ARTIFACT", font=DISPLAY, color=INK, font_size=18, weight=BOLD)

        lbl_specifies.move_to(UP * 3.2 + LEFT * 4.5)
        lbl_influences.move_to(DOWN * 3.2 + LEFT * 4.5)
        lbl_input.move_to(LEFT * 2.8 + UP * 3.8)
        lbl_artifact.move_to(RIGHT * 2.8 + UP * 3.8)

        # ── quadrant content boxes
        def quad_content(lines, pos, col=INK):
            txt = VGroup(*[Text(l, font=MONO, color=col, font_size=15) for l in lines])
            txt.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
            txt.move_to(pos)
            return txt

        tl = quad_content(["voice_id", "fps = 24", "hex_code"],
                           LEFT * 2.8 + UP * 1.5, INK)
        bl = quad_content(["persona", "register", "prompt"],
                           LEFT * 2.8 + DOWN * 1.5, SLATE)
        tr = quad_content(["beat_sheet.json", "compile output"],
                           RIGHT * 2.8 + UP * 1.5, INK)

        # BR: mp4 with CRIMSON corner triangle
        br_txt = Text("mp4", font=MONO, color=INK, font_size=20, weight=BOLD)
        br_txt.move_to(RIGHT * 2.8 + DOWN * 1.2)
        br_sub = Text("taste-judged\nno schema possible", font=SERIF,
                      color=CRIMSON, font_size=14, line_spacing=0.9, slant=ITALIC)
        br_sub.next_to(br_txt, DOWN, buff=0.18)
        # corner triangle (crimson filled triangle in upper-right corner of BR quadrant)
        corner_tri = Triangle(fill_color=CRIMSON, fill_opacity=1, stroke_width=0).scale(0.3)
        corner_tri.move_to(RIGHT * 5.4 + DOWN * 0.3)

        # ── animate
        self.play(Create(h_line), Create(v_line), run_time=0.5)
        self.play(FadeIn(lbl_specifies), FadeIn(lbl_influences),
                  FadeIn(lbl_input), FadeIn(lbl_artifact), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(tl, shift=DOWN * 0.1), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(bl, shift=UP * 0.1), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(tr, shift=DOWN * 0.1), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(br_txt, shift=LEFT * 0.1),
                  FadeIn(br_sub, shift=LEFT * 0.1), run_time=0.6)
        self.play(FadeIn(corner_tri, scale=0.3), corner_tri.animate.scale(1/0.3), run_time=0.5)
        self.wait(max(0.5, _dur("B06") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B07 — INPUT STACK LAYERS (15.49s)
# 6 horizontal bars, most influencing (top) → most specifying (bottom)
# ══════════════════════════════════════════════════════════════
class B07_InputStackLayers(Scene):
    def construct(self):
        layers = [
            ("HUMAN",            "goal · taste · irreplaceable",    INK,      5.8),
            ("LLM",              "distribution over text · no goal", INK,      5.4),
            ("CONDITIONING TEXT","persona · reg · brand",            SLATE,    5.0),
            ("AGENT",            "orchestrator + doer",              SLATE,    4.6),
            ("PARAMETERS",       "fps · voice_id",                   SLATE,    4.2),
            ("SCRIPTS",          "generate · compile",               HAIRLINE, 3.8),
        ]

        top_y = 2.4
        spacing = 0.85
        BAR_H = 0.62
        BAR_X = 0.8

        bar_groups = []
        for i, (name, detail, col, bar_w) in enumerate(layers):
            y = top_y - i * spacing
            fill = col if col != HAIRLINE else GROUND
            stroke = col if col != HAIRLINE else SLATE
            bar = Rectangle(width=bar_w, height=BAR_H, fill_color=fill, fill_opacity=0.15,
                            stroke_color=stroke, stroke_width=2)
            bar.move_to(RIGHT * BAR_X + UP * y)

            name_txt = Text(name, font=DISPLAY, color=stroke if col != INK else INK,
                            font_size=16, weight=BOLD)
            name_txt.move_to(bar.get_left() + RIGHT * (name_txt.width / 2 + 0.2))

            detail_txt = Text(detail, font=MONO, color=SLATE, font_size=13)
            detail_txt.next_to(name_txt, RIGHT, buff=0.4)

            # Keep detail text inside the bar's right stroke (0.15 margin)
            bar_right_x = BAR_X + bar_w / 2.0
            overshoot = detail_txt.get_right()[0] - (bar_right_x - 0.15)
            if overshoot > 0:
                detail_txt.shift(LEFT * overshoot)

            bar_groups.append(VGroup(bar, name_txt, detail_txt))

        # Margin bracket
        top_bracket = Text("MOST INFLUENCING", font=DISPLAY, color=CRIMSON,
                           font_size=13, weight=BOLD)
        top_bracket.move_to(LEFT * 4.8 + UP * 2.4)
        bot_bracket = Text("MOST SPECIFYING", font=DISPLAY, color=INK,
                           font_size=13, weight=BOLD)
        bot_bracket.move_to(LEFT * 4.8 + DOWN * 2.0)
        bracket_line = Line(top_bracket.get_bottom() + DOWN * 0.1,
                            bot_bracket.get_top() + UP * 0.1,
                            stroke_color=HAIRLINE, stroke_width=1.5)

        # ── animate: bars reveal staggered
        self.play(FadeIn(top_bracket), FadeIn(bot_bracket), Create(bracket_line), run_time=0.5)
        for g in bar_groups:
            self.play(FadeIn(g, shift=RIGHT * 0.15), run_time=0.45)
        self.wait(max(0.5, _dur("B07") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B09 — CONDITIONING TEXT STACK (22.52s)
# Three boxes (persona × register × brand) compress to one CONDITIONING TEXT bar
# ══════════════════════════════════════════════════════════════
class B09_ConditioningTextStack(Scene):
    def construct(self):
        # ── three source boxes
        def make_sub_box(title, examples, sub_label):
            t = Text(title, font=DISPLAY, color=INK, font_size=17, weight=BOLD)
            ex = Text(examples, font=MONO, color=SLATE, font_size=13)
            sl = Text(sub_label, font=SERIF, color=CRIMSON, font_size=13, slant=ITALIC)
            content = VGroup(t, ex, sl).arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            box = surround_box(content, buff=0.28, fill_color=GROUND,
                               stroke_color=SLATE, stroke_width=2)
            return VGroup(box, content)

        box1 = make_sub_box("METHOD PERSONA", "script-writer · explainer · bio", "(WHAT to produce)")
        box2 = make_sub_box("VOICE REGISTER", "Teardown · sardonic · wonder",    "(HOW it sounds)")
        box3 = make_sub_box("BRAND",          "NikBearBrown · Hai · Medhavy",    "(WHOSE voice)")

        plus1 = Text("+", font=DISPLAY, color=INK, font_size=36, weight=BOLD)
        plus2 = Text("+", font=DISPLAY, color=INK, font_size=36, weight=BOLD)

        row = VGroup(box1, plus1, box2, plus2, box3).arrange(RIGHT, buff=0.3)
        row.move_to(UP * 0.9)

        # ── combined CONDITIONING TEXT bar
        cond_bar_box = Rectangle(width=8.5, height=0.7, fill_color=INK, fill_opacity=1,
                                  stroke_width=0)
        cond_bar_lbl = Text("CONDITIONING TEXT", font=DISPLAY, color=WHITE,
                            font_size=20, weight=BOLD)
        cond_bar_lbl.move_to(cond_bar_box)
        cond_bar = VGroup(cond_bar_box, cond_bar_lbl).move_to(DOWN * 0.6)

        # equals sign and LLM node
        eq_sign = Text("=", font=DISPLAY, color=SLATE, font_size=32)
        eq_sign.move_to(DOWN * 0.0)

        llm_node_box = Circle(radius=0.55, fill_color=GROUND, fill_opacity=1,
                              stroke_color=INK, stroke_width=2.5)
        llm_node_lbl = Text("LLM", font=DISPLAY, color=INK, font_size=18, weight=BOLD)
        llm_node_lbl.move_to(llm_node_box)
        llm_node = VGroup(llm_node_box, llm_node_lbl).move_to(DOWN * 2.2)

        steer_arrow = Arrow(cond_bar.get_bottom() + DOWN * 0.05,
                            llm_node.get_top() + UP * 0.05,
                            stroke_color=SLATE, stroke_width=2, tip_length=0.2, buff=0)
        steer_lbl = Text("steers the distribution", font=SERIF, color=SLATE,
                         font_size=15, slant=ITALIC)
        steer_lbl.next_to(steer_arrow, RIGHT, buff=0.2)

        # ── animate: boxes appear left to right, then compress
        self.play(FadeIn(box1, shift=DOWN * 0.1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(plus1), FadeIn(box2, shift=DOWN * 0.1), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(plus2), FadeIn(box3, shift=DOWN * 0.1), run_time=0.6)
        self.wait(0.8)
        # compress to bar
        self.play(
            FadeOut(row, shift=DOWN * 0.3),
            FadeIn(eq_sign, shift=DOWN * 0.1),
            FadeIn(cond_bar, shift=UP * 0.2),
            run_time=0.8
        )
        self.wait(0.5)
        self.play(GrowArrow(steer_arrow), FadeIn(steer_lbl), FadeIn(llm_node), run_time=0.7)
        self.wait(max(0.5, _dur("B09") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B09B — ONE WRITER MANY COSTUMES (13.37s)
# Center doer node + orbital costume rings; crossed-out "many writers" alternative
# ══════════════════════════════════════════════════════════════
class B09B_OneWriterManyCostumes(Scene):
    def construct(self):
        # ── doer circle — labels OUTSIDE the circle to avoid stroke-crossing
        doer_circle = Circle(radius=0.85, fill_color=GROUND, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
        doer_circle.move_to(LEFT * 2.8)
        doer_label  = Text("doer", font=DISPLAY, color=INK, font_size=22, weight=BOLD)
        doer_label.move_to(doer_circle.get_center())
        # Sub label placed BELOW the circle, not inside it
        doer_sub    = Text("LLM + goal + tools", font=SERIF, color=SLATE, font_size=13)
        doer_sub.next_to(doer_circle, DOWN, buff=0.2)

        # ── three costume labels stacked to the right with arrows into the doer
        costume_specs = [
            "persona: script-writer",
            "register: Teardown",
            "brand: NikBearBrown",
        ]
        costume_labels = []
        for label_text in costume_specs:
            lbl = Text(label_text, font=MONO, color=SLATE, font_size=14)
            costume_labels.append(lbl)
        costume_stack = VGroup(*costume_labels).arrange(DOWN, buff=0.38)
        costume_stack.move_to(RIGHT * 0.6)

        # Arrows from each label to the right edge of the doer circle
        costume_arrows = []
        for lbl in costume_labels:
            arr = Arrow(lbl.get_left() + LEFT * 0.05,
                        doer_circle.get_right() + RIGHT * 0.05,
                        stroke_color=SLATE, stroke_width=1.5, tip_length=0.15, buff=0)
            costume_arrows.append(arr)

        # ── wrong model: 3 circles (empty) with external labels
        wrong_circles = []
        wrong_lbls = []
        for i in range(3):
            wc = Circle(radius=0.42, fill_color=GROUND, fill_opacity=1,
                        stroke_color=HAIRLINE, stroke_width=1.5)
            wc.move_to(RIGHT * 4.9 + UP * (0.88 - i * 0.88))
            # label OUTSIDE the circle (to the right)
            wl = Text(f"{i+1}", font=MONO, color=HAIRLINE, font_size=14)
            wl.next_to(wc, RIGHT, buff=0.1)
            wrong_circles.append(wc)
            wrong_lbls.append(wl)
        wrong_group = VGroup(*wrong_circles)
        wrong_lbl_group = VGroup(*wrong_lbls)
        wrong_header = Text("wrong model", font=SERIF, color=SLATE,
                            font_size=14, slant=ITALIC)
        wrong_header.next_to(wrong_group, UP, buff=0.28)

        # X through wrong group
        wrong_x1 = Line(wrong_group.get_corner(UL) + UP * 0.15 + LEFT * 0.1,
                        wrong_group.get_corner(DR) + DOWN * 0.15 + RIGHT * 0.1,
                        stroke_color=CRIMSON, stroke_width=5)
        wrong_x1.set_z_index(10)
        wrong_x2 = Line(wrong_group.get_corner(UR) + UP * 0.15 + RIGHT * 0.1,
                        wrong_group.get_corner(DL) + DOWN * 0.15 + LEFT * 0.1,
                        stroke_color=CRIMSON, stroke_width=5)
        wrong_x2.set_z_index(10)

        # ── footer (safe area: within ±3.4 y)
        footer = Text("one writer  ·  many costumes  —  not many writers",
                      font=SERIF, color=INK, font_size=17, slant=ITALIC)
        footer.move_to(DOWN * 3.05)

        # ── animate
        self.play(FadeIn(doer_circle), FadeIn(doer_label), run_time=0.6)
        self.play(FadeIn(doer_sub), run_time=0.4)
        for lbl, arr in zip(costume_labels, costume_arrows):
            self.play(FadeIn(lbl, shift=LEFT * 0.1), GrowArrow(arr), run_time=0.4)
        self.wait(0.5)
        self.play(FadeIn(wrong_group), FadeIn(wrong_lbl_group),
                  FadeIn(wrong_header), run_time=0.6)
        self.play(Create(wrong_x1), Create(wrong_x2), run_time=0.5)
        self.wait(0.4)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.5, _dur("B09B") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B11 — UTILITY BELT (24.92s)
# 3 script boxes with parameter→output arrows; strikethrough "taste gate?" bubble
# ══════════════════════════════════════════════════════════════
class B11_UtilityBelt(Scene):
    def construct(self):
        # ── header
        header = Text("THE UTILITY BELT", font=DISPLAY, color=INK,
                      font_size=24, weight=BOLD)
        header.to_edge(UP, buff=0.7)

        # ── three script boxes: name + params stacked inside each box
        scripts = [
            ("generate_audio.py", "voice_id · stability"),
            ("remotion_scenes.py", "fps=24 · width=1920"),
            ("compile.py",         "clips/ · beat_sheet"),
        ]

        script_groups = []
        for name, params in scripts:
            lbl = Text(name, font=MONO, color=INK, font_size=15, weight=BOLD)
            sub = Text(params, font=MONO, color=SLATE, font_size=12)
            stack = VGroup(lbl, sub).arrange(DOWN, buff=0.12)
            box = Rectangle(width=3.6, height=1.1, fill_color=GROUND, fill_opacity=1,
                            stroke_color=INK, stroke_width=2)
            stack.move_to(box.get_center())
            script_groups.append(VGroup(box, stack))

        sg_row = VGroup(*script_groups).arrange(RIGHT, buff=0.7)
        sg_row.move_to(DOWN * 0.2)

        # ── simple arrows: one per box (left → box, box → right)
        # Arrow labels: short and positioned BELOW (not above) to stay below box stroke
        in_arrows = []
        out_arrows = []
        for sg in script_groups:
            ai = Arrow(sg.get_left() + LEFT * 0.8, sg.get_left() + LEFT * 0.05,
                       stroke_color=SLATE, stroke_width=2, tip_length=0.16, buff=0)
            ao = Arrow(sg.get_right() + RIGHT * 0.05, sg.get_right() + RIGHT * 0.8,
                       stroke_color=INK, stroke_width=2, tip_length=0.16, buff=0)
            in_arrows.append(ai)
            out_arrows.append(ao)

        # ── same in → same out label
        same_lbl = Text("same in  →  same out", font=SERIF, color=INK,
                        font_size=19, slant=ITALIC)
        same_lbl.next_to(sg_row, DOWN, buff=0.6)

        # ── taste gate? bubble with intentional strike-through marks
        bubble_box = Rectangle(width=2.4, height=0.7, fill_color=GOLD_FILL, fill_opacity=1,
                                stroke_color=CRIMSON, stroke_width=2)
        bubble_lbl = Text("taste gate?", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        bubble_lbl.move_to(bubble_box)
        bubble = VGroup(bubble_box, bubble_lbl)
        bubble.move_to(sg_row.get_center() + UP * 2.0)

        strike1 = Line(bubble.get_corner(UL), bubble.get_corner(DR),
                       stroke_color=CRIMSON, stroke_width=5)
        strike2 = Line(bubble.get_corner(UR), bubble.get_corner(DL),
                       stroke_color=CRIMSON, stroke_width=5)
        # Mark strikes intentional so Gate B skips TEXT_ON_CURVE for "taste gate?"
        strike1._qc_intentional = True
        strike2._qc_intentional = True

        absent_lbl = Text("absent — not needed", font=SERIF, color=SLATE,
                          font_size=14, slant=ITALIC)
        absent_lbl.next_to(bubble, RIGHT, buff=0.25)

        # ── animate
        self.play(FadeIn(header, shift=DOWN * 0.1), run_time=0.5)
        self.wait(0.3)
        for sg in script_groups:
            self.play(FadeIn(sg, shift=UP * 0.1), run_time=0.45)
        self.wait(0.4)
        for ai, ao in zip(in_arrows, out_arrows):
            self.play(GrowArrow(ai), GrowArrow(ao), run_time=0.4)
        self.play(FadeIn(same_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(0.6)
        self.play(FadeIn(bubble), run_time=0.5)
        self.play(Create(strike1), Create(strike2), run_time=0.5)
        self.play(FadeIn(absent_lbl), run_time=0.4)
        self.wait(max(0.5, _dur("B11") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B12 — ARTIFACT CLASSES (23.54s)
# Three columns: CONTRACT (crimson) / LOGS (slate) / DELIVERABLE (ink)
# ══════════════════════════════════════════════════════════════
class B12_ArtifactClasses(Scene):
    def construct(self):
        def make_column(title, title_color, items, judgment_label, x_pos):
            header = Text(title, font=DISPLAY, color=title_color,
                          font_size=20, weight=BOLD)
            col_items = VGroup(*[Text(item, font=MONO, color=INK, font_size=14)
                                  for item in items])
            col_items.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
            read_lbl = Text(judgment_label, font=SERIF, color=SLATE,
                            font_size=14, slant=ITALIC)
            col_stack = VGroup(col_items, read_lbl).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
            col_box = surround_box(col_stack, buff=0.32, fill_color=GROUND,
                                   stroke_color=title_color, stroke_width=2)
            header.next_to(col_box, UP, buff=0.18)
            return VGroup(col_box, col_stack, header).move_to(RIGHT * x_pos)

        col1 = make_column(
            "CONTRACT", CRIMSON,
            ["beat_sheet.json"],
            "read by agents · approved by you\njudgment: schema check → gate",
            -3.8
        )
        col2 = make_column(
            "LOGS", SLATE,
            ["align.json", "QC sheets", "request cards"],
            "consulted when broken\njudgment: none — diagnostic",
            0.0
        )
        col3 = make_column(
            "DELIVERABLE", INK,
            ["the mp4"],
            "read by you + audience\njudgment: TASTE",
            3.8
        )

        # Footer under col3 only
        footer = Text("The log will never tell you\nif it's worth watching.",
                      font=SERIF, color=CRIMSON, font_size=15, slant=ITALIC,
                      line_spacing=0.9)
        footer.next_to(col3, DOWN, buff=0.3)

        # ── animate: columns reveal left to right
        self.play(FadeIn(col1, shift=UP * 0.15), run_time=0.7)
        self.wait(0.6)
        self.play(FadeIn(col2, shift=UP * 0.15), run_time=0.7)
        self.wait(0.6)
        self.play(FadeIn(col3, shift=UP * 0.15), run_time=0.7)
        self.wait(0.6)
        self.play(FadeIn(footer, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, _dur("B12") - getattr(self, 'time', 0.0)))


# ══════════════════════════════════════════════════════════════
# B14 — TAXONOMY PAYOFF (23.82s)
# B01 cascade revisited with SPECIFIES/INFLUENCES annotation bands + gates
# ══════════════════════════════════════════════════════════════
class B14_TaxonomyPayoff(Scene):
    def construct(self):
        # ── rebuild the B01 cascade (smaller, to leave room for annotations)
        def mini_box(label, accent=INK, w=1.7, h=0.58):
            box = Rectangle(width=w, height=h, fill_color=GROUND, fill_opacity=1,
                            stroke_color=accent, stroke_width=2)
            lbl = Text(label, font=MONO, color=INK, font_size=14, weight=BOLD)
            lbl.move_to(box)
            return VGroup(box, lbl)

        bs   = mini_box("beat_sheet.json", CRIMSON, w=2.1)
        orch = mini_box("orchestrator")
        doer = mini_box("doer")
        el   = mini_box("ElevenLabs", w=1.9)
        mn   = mini_box("Manim",      w=1.6)
        comp = mini_box("compile")
        mp4  = mini_box("mp4", CRIMSON, w=1.3)

        bs.move_to(LEFT * 5.0 + DOWN * 0.2)
        orch.move_to(LEFT * 2.8 + DOWN * 0.2)
        doer.move_to(LEFT * 0.6 + DOWN * 0.2)
        el.move_to(RIGHT * 1.8 + UP * 0.8)
        mn.move_to(RIGHT * 1.8 + DOWN * 1.2)
        comp.move_to(RIGHT * 3.8 + DOWN * 0.2)
        mp4.move_to(RIGHT * 5.4 + DOWN * 0.2)

        def small_arr(a, b):
            return Arrow(a.get_right() + RIGHT * 0.05,
                         b.get_left() + LEFT * 0.05,
                         stroke_color=INK, stroke_width=1.5,
                         tip_length=0.15, buff=0)

        a1 = small_arr(bs, orch)
        a2 = small_arr(orch, doer)
        bel = Arrow(doer.get_right() + RIGHT * 0.05, el.get_left() + LEFT * 0.05,
                    stroke_color=INK, stroke_width=1.5, tip_length=0.15, buff=0)
        bmn = Arrow(doer.get_right() + RIGHT * 0.05, mn.get_left() + LEFT * 0.05,
                    stroke_color=INK, stroke_width=1.5, tip_length=0.15, buff=0)
        mel = Arrow(el.get_right() + RIGHT * 0.05, comp.get_left() + LEFT * 0.05,
                    stroke_color=INK, stroke_width=1.5, tip_length=0.15, buff=0)
        mmn = Arrow(mn.get_right() + RIGHT * 0.05, comp.get_left() + LEFT * 0.05,
                    stroke_color=INK, stroke_width=1.5, tip_length=0.15, buff=0)
        a3  = small_arr(comp, mp4)

        cascade = VGroup(bs, orch, doer, el, mn, comp, mp4,
                          a1, a2, bel, bmn, mel, mmn, a3)

        # ── annotation bands (reveal after cascade)
        # SPECIFIES band over el + mn only — keep right edge left of compile box (right=2.9)
        spec_band = Rectangle(width=2.2, height=0.45, fill_color="#E8F4F0",
                               fill_opacity=0.8, stroke_color=INK, stroke_width=1.5)
        spec_band.move_to(RIGHT * 1.8 + DOWN * 0.2)
        spec_band_lbl = Text("SPECIFIES — no gate", font=DISPLAY, color=INK,
                             font_size=13, weight=BOLD)
        spec_band_lbl.next_to(spec_band, UP, buff=0.12)

        # INFLUENCES band (crimson) over doer layer (persona/register)
        inf_band = Rectangle(width=1.9, height=0.45, fill_color=GOLD_FILL,
                              fill_opacity=0.8, stroke_color=CRIMSON, stroke_width=2)
        inf_band.move_to(LEFT * 0.6 + DOWN * 0.2)
        inf_band_lbl = Text("INFLUENCES — taste gate ▼", font=DISPLAY, color=CRIMSON,
                            font_size=13, weight=BOLD)
        inf_band_lbl.next_to(inf_band, UP, buff=0.12)

        # Gate icon + human silhouette
        gate_icon = Text("▼", font=DISPLAY, color=CRIMSON, font_size=22)
        gate_icon.next_to(doer, DOWN, buff=0.3)
        human_lbl = Text("human\njudgment", font=SERIF, color=CRIMSON,
                         font_size=13, slant=ITALIC, line_spacing=0.85)
        human_lbl.next_to(gate_icon, RIGHT, buff=0.2)

        # mp4 deliverable label
        mp4_lbl = Text("DELIVERABLE\ntaste-judged", font=DISPLAY, color=CRIMSON,
                       font_size=13, weight=BOLD, line_spacing=0.85)
        mp4_lbl.next_to(mp4, DOWN, buff=0.2)

        # ── header (buff=0.78 keeps it within ±3.4 safe area)
        header = Text("Back to the puzzle.", font=SERIF, color=INK,
                      font_size=20, slant=ITALIC)
        header.to_edge(UP, buff=0.78)

        # ── animate
        self.play(FadeIn(header), run_time=0.4)
        self.play(FadeIn(cascade), run_time=0.8)
        self.wait(0.8)
        # Annotation bands wipe in
        self.play(FadeIn(spec_band, shift=DOWN * 0.05),
                  FadeIn(spec_band_lbl), run_time=0.7)
        self.play(FadeIn(inf_band, shift=DOWN * 0.05),
                  FadeIn(inf_band_lbl), run_time=0.7)
        self.wait(0.5)
        self.play(FadeIn(gate_icon, scale=1.5), FadeIn(human_lbl), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(mp4_lbl), run_time=0.5)
        self.wait(max(0.5, _dur("B14") - getattr(self, 'time', 0.0)))
