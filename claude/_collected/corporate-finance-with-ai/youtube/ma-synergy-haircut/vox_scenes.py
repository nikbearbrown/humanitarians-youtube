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


class B04_SynergyHaircut(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"; AMBER="#E8A020"

        # Values: standalone=$850M, adj synergies=$122M, overpay=$128M, total=$1100M
        standalone = 850
        adj_syn = 122   # cost $68M + revenue $54M
        overpay = 128
        total = 1100

        scale = 10.0 / total   # units per $M; 10 units = $1100M
        x_start = -5.0
        bar_h = 1.0
        bar_y = 0.0

        # x coordinates
        x_standalone_end = x_start + standalone * scale     # 2.727
        x_syn_end = x_standalone_end + adj_syn * scale      # 3.836
        x_overpay_end = x_syn_end + overpay * scale         # 5.0

        title = Text(
            "M&A Synergy Haircut: What You Should Pay vs. What They Ask",
            font="Georgia", font_size=19, color=ManimColor(INK), weight=BOLD
        ).move_to([0, 3.2, 0])

        # Main bars
        standalone_bar = Rectangle(
            width=standalone * scale, height=bar_h,
            fill_color=ManimColor(PASS_CLR), fill_opacity=0.85,
            stroke_width=0, stroke_opacity=0
        ).move_to([x_start + standalone * scale / 2, bar_y, 0])

        syn_bar = Rectangle(
            width=adj_syn * scale, height=bar_h,
            fill_color=ManimColor(AMBER), fill_opacity=0.9,
            stroke_width=0, stroke_opacity=0
        ).move_to([x_standalone_end + adj_syn * scale / 2, bar_y, 0])

        overpay_bar = Rectangle(
            width=overpay * scale, height=bar_h,
            fill_color=ManimColor(CRIMSON), fill_opacity=0.9,
            stroke_width=0, stroke_opacity=0
        ).move_to([x_syn_end + overpay * scale / 2, bar_y, 0])

        # Labels in bars
        sa_lbl = Text("STANDALONE $850M", font="Georgia", font_size=14, color=ManimColor(CREAM))
        sa_lbl.move_to([x_start + standalone * scale / 2, bar_y, 0])

        syn_lbl_bg = Rectangle(width=1.8, height=0.28, fill_color=ManimColor(AMBER),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([x_standalone_end + adj_syn * scale / 2, bar_y, 0])
        syn_lbl = Text("ADJ. SYN. $122M", font="Georgia", font_size=11, color=ManimColor(INK))
        syn_lbl.move_to([x_standalone_end + adj_syn * scale / 2, bar_y, 0])

        op_lbl_bg = Rectangle(width=1.4, height=0.28, fill_color=ManimColor(CRIMSON),
                              fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                              ).move_to([x_syn_end + overpay * scale / 2, bar_y, 0])
        op_lbl = Text("OVERPAY $128M", font="Georgia", font_size=11, color=ManimColor(CREAM))
        op_lbl.move_to([x_syn_end + overpay * scale / 2, bar_y, 0])

        # Max price vertical line at x_syn_end — label to LEFT of the line
        max_line = Line([x_syn_end, bar_y - bar_h / 2 - 0.08, 0],
                        [x_syn_end, bar_y + bar_h / 2 + 0.6, 0],
                        stroke_width=2, color=ManimColor(INK))
        max_lbl_bg = Rectangle(width=1.5, height=0.3, fill_color=ManimColor(CREAM),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([x_syn_end - 0.9, bar_y + bar_h / 2 + 0.8, 0])
        max_lbl = Text("MAX = $972M", font="Georgia", font_size=14, color=ManimColor(INK))
        max_lbl.move_to([x_syn_end - 0.9, bar_y + bar_h / 2 + 0.8, 0])

        # Deal price end line at x=5.0 — label above at a different height
        deal_line = Line([x_overpay_end, bar_y - bar_h / 2 - 0.08, 0],
                         [x_overpay_end, bar_y + bar_h / 2 + 0.25, 0],
                         stroke_width=2, color=ManimColor(CRIMSON))
        deal_lbl_bg = Rectangle(width=1.2, height=0.28, fill_color=ManimColor(CREAM),
                                fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                                ).move_to([x_overpay_end - 0.7, bar_y + bar_h / 2 + 0.45, 0])
        deal_lbl = Text("DEAL $1,100M", font="Georgia", font_size=12, color=ManimColor(CRIMSON))
        deal_lbl.move_to([x_overpay_end - 0.7, bar_y + bar_h / 2 + 0.45, 0])

        # Raw synergies comparison bar (thinner, below)
        raw_y = bar_y - 1.5
        raw_bar_h = 0.4
        raw_cost_w = 80 * scale
        raw_rev_w = 120 * scale
        raw_total_w = (80 + 120) * scale

        raw_cost_bar = Rectangle(
            width=raw_cost_w, height=raw_bar_h,
            fill_color=ManimColor(PASS_CLR), fill_opacity=0.5,
            stroke_width=0, stroke_opacity=0
        ).move_to([x_standalone_end + raw_cost_w / 2, raw_y, 0])

        raw_rev_bar = Rectangle(
            width=raw_rev_w, height=raw_bar_h,
            fill_color=ManimColor(AMBER), fill_opacity=0.5,
            stroke_width=0, stroke_opacity=0
        ).move_to([x_standalone_end + raw_cost_w + raw_rev_w / 2, raw_y, 0])

        raw_end_x = x_standalone_end + raw_total_w   # 4.545

        # Haircut arrow from raw_end to adj_end
        haircut_arrow = Arrow(
            [raw_end_x, raw_y, 0],
            [x_syn_end, raw_y, 0],
            stroke_width=2, color=ManimColor(CRIMSON),
            buff=0.0, max_tip_length_to_length_ratio=0.2
        )
        haircut_bg = Rectangle(width=1.2, height=0.26, fill_color=ManimColor(CREAM),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([(raw_end_x + x_syn_end) / 2, raw_y + 0.28, 0])
        haircut_lbl = Text("HAIRCUT -$78M", font="Georgia", font_size=11, color=ManimColor(CRIMSON))
        haircut_lbl.move_to([(raw_end_x + x_syn_end) / 2, raw_y + 0.28, 0])

        # Realization rates label
        rates_bg = Rectangle(width=5.0, height=0.28, fill_color=ManimColor(CREAM),
                             fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                             ).move_to([0, -2.3, 0])
        rates_lbl = Text(
            "Cost realization: 85%  |  Revenue realization: 45%",
            font="Georgia", font_size=13, color=ManimColor(SLATE)
        ).move_to([0, -2.3, 0])

        # Verdict
        verdict_bg = Rectangle(width=6.5, height=0.32, fill_color=ManimColor(CREAM),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([0, -2.85, 0])
        verdict = Text(
            "X VALUE-DESTROYING: Deal $1,100M > Max price $972M",
            font="Georgia", font_size=14, color=ManimColor(CRIMSON)
        ).move_to([0, -2.85, 0])

        # Animation
        self.play(Write(title))                                              # 1
        self.play(FadeIn(standalone_bar), FadeIn(sa_lbl))                   # 2
        self.play(FadeIn(syn_bar), FadeIn(syn_lbl_bg), FadeIn(syn_lbl))    # 3
        self.play(FadeIn(overpay_bar), FadeIn(op_lbl_bg), FadeIn(op_lbl),
                  FadeIn(max_line), FadeIn(max_lbl_bg), FadeIn(max_lbl),
                  FadeIn(deal_line), FadeIn(deal_lbl_bg), FadeIn(deal_lbl)) # 4
        self.play(FadeIn(raw_cost_bar), FadeIn(raw_rev_bar),
                  FadeIn(haircut_arrow), FadeIn(haircut_bg), FadeIn(haircut_lbl))  # 5
        self.play(FadeIn(rates_bg), FadeIn(rates_lbl),
                  FadeIn(verdict_bg), FadeIn(verdict))                       # 6
