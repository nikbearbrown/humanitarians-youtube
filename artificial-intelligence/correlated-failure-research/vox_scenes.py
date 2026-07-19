import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_CorrelatedFailure(Scene):
    def construct(self):
        title = Text("CORRELATED FAILURE IN AI AUDITING", color=INK, font_size=32, weight=BOLD).move_to([0, 3.2, 0])

        # Divider at x=0 — only in upper portion (stops above the audit table)
        divider = Line((0.0, -1.6, 0), (0.0, 2.8, 0), color=SLATE, stroke_width=1, stroke_opacity=0.4)

        # Panel labels
        left_label_bg = Rectangle(width=2.8, height=0.4, fill_color=CREAM, fill_opacity=1,
                                 stroke_width=0, stroke_opacity=0).move_to([-2.5, 2.2, 0])
        left_label = Text("CORRELATED FAILURE", color=CRIMSON, font_size=24, weight=BOLD).move_to([-2.5, 2.2, 0])
        left_label_grp = VGroup(left_label_bg, left_label)

        right_label_bg = Rectangle(width=2.9, height=0.4, fill_color=CREAM, fill_opacity=1,
                                  stroke_width=0, stroke_opacity=0).move_to([3.0, 2.2, 0])
        right_label = Text("INDEPENDENT FAILURE", color=PASS_CLR, font_size=24, weight=BOLD).move_to([3.0, 2.2, 0])
        right_label_grp = VGroup(right_label_bg, right_label)

        # LEFT PANEL: Two overlapping circles representing LLMs
        llm1_circle = Circle(radius=1.2, color=SLATE, stroke_width=2,
                            fill_color="#E8E8E8", fill_opacity=0.6)
        llm1_circle.move_to([-3.2, 0.5, 0])

        llm2_circle = Circle(radius=1.2, color=SLATE, stroke_width=2,
                            fill_color="#E8E8E8", fill_opacity=0.6)
        llm2_circle.move_to([-1.8, 0.5, 0])

        # Labels for circles — placed above the circle tops (radius=1.2, center y=0.5 -> top y=1.7)
        llm1_bg = Rectangle(width=0.8, height=0.35, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([-4.5, 1.9, 0])
        llm1_lbl = Text("LLM-1", color=SLATE, font_size=22).move_to([-4.5, 1.9, 0])

        llm2_bg = Rectangle(width=0.8, height=0.35, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([-0.6, 1.9, 0])
        llm2_lbl = Text("LLM-2", color=SLATE, font_size=22).move_to([-0.6, 1.9, 0])

        # Overlap label (SHARED BIAS)
        overlap_bg = Rectangle(width=1.4, height=0.7, fill_color=CREAM, fill_opacity=0.85,
                              stroke_width=0, stroke_opacity=0).move_to([-2.5, 0.5, 0])
        overlap_lbl = Text("SHARED\nBIAS", color=CRIMSON, font_size=20, weight=BOLD).move_to([-2.5, 0.5, 0])
        overlap_label = VGroup(overlap_bg, overlap_lbl, llm1_bg, llm1_lbl, llm2_bg, llm2_lbl)

        consensus_bg = Rectangle(width=2.4, height=0.6, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to([-2.5, -1.5, 0])
        consensus_lbl = Text("CONSENSUS\nnot verification", color=CRIMSON, font_size=22).move_to([-2.5, -1.5, 0])
        consensus_label = VGroup(consensus_bg, consensus_lbl)

        # RIGHT PANEL: LLM claim rect -> arrow -> code check rect
        claim_rect = Rectangle(width=1.8, height=0.7, fill_color=SLATE, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([1.5, 0.5, 0])
        claim_lbl = Text("LLM claim", color=INK, font_size=20).move_to([1.5, 0.5, 0])
        claim_grp = VGroup(claim_rect, claim_lbl)

        audit_arrow = Arrow((2.4, 0.5, 0), (3.1, 0.5, 0), color=INK, stroke_width=2)

        check_rect = Rectangle(width=1.8, height=0.7, fill_color=PASS_CLR, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([4.1, 0.5, 0])
        check_lbl = Text("eval()", color=INK, font_size=20).move_to([4.1, 0.5, 0])
        check_grp = VGroup(check_rect, check_lbl)

        verification_bg = Rectangle(width=2.7, height=0.6, fill_color=CREAM, fill_opacity=1,
                                   stroke_width=0, stroke_opacity=0).move_to([3.0, -1.5, 0])
        verification_lbl = Text("VERIFICATION\nnot consensus", color=PASS_CLR, font_size=22).move_to([3.0, -1.5, 0])
        verification_label = VGroup(verification_bg, verification_lbl)

        # Audit pairing mini-table at bottom (y=-2.0 to -3.0)
        TABLE_ROWS = [
            ("Factual claim", "LLM-on-LLM", "Retrieval lookup"),
            ("Math result",   "LLM-on-LLM", "eval() / sympy"),
            ("Schema match",  "LLM-on-LLM", "JSON validator"),
        ]
        TABLE_COL_XS = [-4.5, 0.2, 4.3]
        TABLE_COL_W  = [2.8,   2.5,  2.8]
        TABLE_ROW_YS = [-2.1, -2.5, -2.9]
        TABLE_H = 0.32

        audit_table_rows = VGroup()
        for ri, (ct, wt, rt) in enumerate(TABLE_ROWS):
            ty = TABLE_ROW_YS[ri]
            for ci, (cell_txt, cx, cw) in enumerate(zip([ct, wt, rt], TABLE_COL_XS, TABLE_COL_W)):
                c_col = CRIMSON if ci == 1 else (PASS_CLR if ci == 2 else INK)
                bg = Rectangle(width=cw, height=TABLE_H, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([cx, ty, 0])
                txt = Text(cell_txt, color=c_col, font_size=18).move_to([cx, ty, 0])
                audit_table_rows.add(bg, txt)

        verdict_bg = Rectangle(width=5.0, height=0.38, fill_color=CREAM, fill_opacity=1,
                              stroke_width=0, stroke_opacity=0).move_to([0, -3.1, 0])
        verdict_text = Text(
            "Checkers must fail differently — not just more",
            color=INK, font_size=22
        ).move_to([0, -3.1, 0])

        # 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(left_label_grp), FadeIn(right_label_grp), FadeIn(divider))
        self.play(FadeIn(llm1_circle), FadeIn(llm2_circle), Write(overlap_label))
        self.play(Write(consensus_label))
        self.play(FadeIn(claim_grp), FadeIn(check_grp), FadeIn(audit_arrow))
        self.play(Write(verification_label))
        self.play(FadeIn(audit_table_rows), FadeIn(verdict_bg), Write(verdict_text))
