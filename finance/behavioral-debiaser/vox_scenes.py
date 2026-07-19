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


class B04_DebiasComparison(Scene):
    def construct(self):
        INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
        PASS_CLR="#2A7A2A"; AMBER="#E8A020"

        # Values
        groups = [
            ("COST SYN.", 80, 68, "Plan. fallacy", -15),
            ("REVENUE SYN.", 120, 54, "Overconfidence", -55),
            ("INTEG. COST", 40, 52, "Underestimate", +30),
        ]

        # Scale: $130M max -> y_plot range = 4.0 units
        y_max_val = 130.0
        y_base = -1.5
        y_top = 2.5
        y_scale = (y_top - y_base) / y_max_val

        def bh(v):
            return abs(v) * y_scale

        def bar_top(v):
            return y_base + v * y_scale

        # Group x positions
        group_xs = [-3.0, 0.0, 3.0]
        bar_w = 0.7
        inside_dx = -0.4
        adj_dx = 0.4

        title = Text(
            "Reference Class Forecasting: Replacing Hope with Base Rates",
            font="Georgia", font_size=18, color=ManimColor(INK), weight=BOLD
        ).move_to([0, 3.2, 0])

        # Axes
        y_axis = Line([-4.5, y_base, 0], [-4.5, y_top, 0],
                      stroke_width=2, color=ManimColor(SLATE))
        x_axis = Line([-4.5, y_base, 0], [4.5, y_base, 0],
                      stroke_width=2, color=ManimColor(SLATE))

        # y ticks at $0, $40, $80, $120
        y_ticks = VGroup()
        for v in [0, 40, 80, 120]:
            ty = y_base + v * y_scale
            tick = Line([-4.5, ty, 0], [-4.65, ty, 0], stroke_width=1, color=ManimColor(SLATE))
            bg = Rectangle(width=0.5, height=0.22, fill_color=ManimColor(CREAM),
                           fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                           ).move_to([-5.05, ty, 0])
            lbl = Text(f"${v}M", font="Georgia", font_size=11, color=ManimColor(SLATE)
                       ).move_to([-5.05, ty, 0])
            y_ticks.add(VGroup(tick, bg, lbl))

        axes = VGroup(y_axis, x_axis, y_ticks)

        cost_bars = VGroup()
        rev_bars = VGroup()
        integ_bars = VGroup()
        all_bar_groups = [cost_bars, rev_bars, integ_bars]

        bias_labels = VGroup()
        arrows = VGroup()

        for gi, (name, inside_v, adj_v, bias_name, pct) in enumerate(groups):
            gx = group_xs[gi]
            bar_group = all_bar_groups[gi]

            # Inside bar (amber)
            ix = gx + inside_dx
            ih = bh(inside_v)
            inside_bar = Rectangle(
                width=bar_w, height=ih,
                fill_color=ManimColor(AMBER), fill_opacity=0.85,
                stroke_width=0, stroke_opacity=0
            ).move_to([ix, y_base + ih / 2, 0])
            inside_top = y_base + ih

            # Adjusted bar (teal/pass)
            ax_ = gx + adj_dx
            ah = bh(adj_v)
            adj_bar = Rectangle(
                width=bar_w, height=ah,
                fill_color=ManimColor(PASS_CLR), fill_opacity=0.85,
                stroke_width=0, stroke_opacity=0
            ).move_to([ax_, y_base + ah / 2, 0])
            adj_top = y_base + ah

            bar_group.add(inside_bar, adj_bar)

            # Group label below
            glbl_bg = Rectangle(width=1.4, height=0.22, fill_color=ManimColor(CREAM),
                                fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                                ).move_to([gx, y_base - 0.25, 0])
            glbl = Text(name, font="Georgia", font_size=11, color=ManimColor(SLATE)
                        ).move_to([gx, y_base - 0.25, 0])
            bar_group.add(glbl_bg, glbl)

            # Bias label above inside bar
            bias_bg = Rectangle(width=1.4, height=0.24, fill_color=ManimColor(CREAM),
                                fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                                ).move_to([ix, inside_top + 0.25, 0])
            bias_lbl = Text(bias_name, font="Georgia", font_size=10, color=ManimColor(INK)
                            ).move_to([ix, inside_top + 0.25, 0])
            bias_labels.add(VGroup(bias_bg, bias_lbl))

            # Inside value label
            iv_bg = Rectangle(width=0.6, height=0.22, fill_color=ManimColor(AMBER),
                              fill_opacity=0.9, stroke_width=0, stroke_opacity=0
                              ).move_to([ix, y_base + ih / 2, 0])
            iv_lbl = Text(f"${inside_v}M", font="Georgia", font_size=11, color=ManimColor(INK)
                          ).move_to([ix, y_base + ih / 2, 0])
            bar_group.add(iv_bg, iv_lbl)

            # Adj value label
            av_bg = Rectangle(width=0.6, height=0.22, fill_color=ManimColor(PASS_CLR),
                              fill_opacity=0.9, stroke_width=0, stroke_opacity=0
                              ).move_to([ax_, y_base + ah / 2, 0])
            av_lbl = Text(f"${adj_v}M", font="Georgia", font_size=11, color=ManimColor(CREAM)
                          ).move_to([ax_, y_base + ah / 2, 0])
            bar_group.add(av_bg, av_lbl)

            # Arrow from inside top to adj top
            if inside_top != adj_top:
                arr = Arrow(
                    [ix, inside_top, 0], [ax_, adj_top, 0],
                    stroke_width=1.5, color=ManimColor(CRIMSON),
                    buff=0.05, max_tip_length_to_length_ratio=0.2
                )
                arrows.add(arr)

        # Legend
        swatch_amber = Rectangle(width=0.28, height=0.22, fill_color=ManimColor(AMBER),
                                 fill_opacity=0.85, stroke_width=0, stroke_opacity=0
                                 ).move_to([-3.5, -2.7, 0])
        lbl_inside = Text("Inside view", font="Georgia", font_size=12, color=ManimColor(INK))
        lbl_inside.next_to(swatch_amber, RIGHT, buff=0.1)

        swatch_teal = Rectangle(width=0.28, height=0.22, fill_color=ManimColor(PASS_CLR),
                                fill_opacity=0.85, stroke_width=0, stroke_opacity=0
                                ).move_to([0.5, -2.7, 0])
        lbl_adj = Text("Reference-class adjusted", font="Georgia", font_size=12, color=ManimColor(INK))
        lbl_adj.next_to(swatch_teal, RIGHT, buff=0.1)

        legend = VGroup(swatch_amber, lbl_inside, swatch_teal, lbl_adj)

        # Verdict
        verdict_bg = Rectangle(width=6.8, height=0.3, fill_color=ManimColor(CREAM),
                               fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                               ).move_to([0, -3.12, 0])
        verdict = Text(
            "ADJ. MAX PRICE = $850 + $68 + $54 - $52 = $920M vs. DEAL PRICE $1.1B",
            font="Georgia", font_size=12, color=ManimColor(INK)
        ).move_to([0, -3.12, 0])

        verdict2_bg = Rectangle(width=4.0, height=0.26, fill_color=ManimColor(CREAM),
                                fill_opacity=1.0, stroke_width=0, stroke_opacity=0
                                ).move_to([0, -3.40, 0])
        verdict2 = Text(
            "X VALUE-DESTROYING at reference-class rates",
            font="Georgia", font_size=12, color=ManimColor(CRIMSON)
        ).move_to([0, -3.40, 0])

        # Animation
        self.play(Write(title))                                       # 1
        self.play(Create(axes))                                       # 2
        self.play(FadeIn(cost_bars))                                  # 3
        self.play(FadeIn(rev_bars))                                   # 4
        self.play(FadeIn(integ_bars))                                 # 5
        self.play(FadeIn(bias_labels), FadeIn(arrows))                # 6
        self.play(FadeIn(legend), FadeIn(verdict_bg), FadeIn(verdict),
                  FadeIn(verdict2_bg), FadeIn(verdict2))              # 7
