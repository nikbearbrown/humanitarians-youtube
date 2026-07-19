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


class B04_BrandArchetypeDAG(Scene):
    def construct(self):
        # Title
        title = Text("BRAND ARCHETYPE CAUSAL AUDIT",
                     color=INK, weight=BOLD, font_size=36).move_to([0, 3.2, 0])

        # Node positions — advertising_spend moved to y=2.3 (safe from title)
        brand_pos    = [-4.5,  0.0, 0]
        revenue_pos  = [ 4.5,  0.0, 0]
        adspend_pos  = [ 0.0,  2.3, 0]
        pricing_pos  = [ 1.0, -2.2, 0]
        awareness_pos = [3.5,  1.8, 0]

        # Nodes
        brand_node    = Circle(radius=0.45, color=INK,
                               fill_color=CREAM, fill_opacity=1,
                               stroke_width=1.5).move_to(brand_pos)
        revenue_node  = Circle(radius=0.45, color=INK,
                               fill_color=CREAM, fill_opacity=1,
                               stroke_width=1.5).move_to(revenue_pos)
        adspend_node  = Circle(radius=0.45, color=INK,
                               fill_color=GOLD, fill_opacity=1,
                               stroke_width=1.5).move_to(adspend_pos)
        pricing_node  = Circle(radius=0.45, color=INK,
                               fill_color="#CCE5FF", fill_opacity=1,
                               stroke_width=1.5).move_to(pricing_pos)
        awareness_node = Circle(radius=0.45, color=INK,
                                fill_color="#FFD6D6", fill_opacity=1,
                                stroke_width=1.5).move_to(awareness_pos)

        # Labels — use short names for space; awareness gets CREAM bg (crosses arrows)
        brand_label    = Text("brand\narchetype", color=INK, font_size=16, weight=BOLD).move_to(brand_pos)
        revenue_label  = Text("revenue\ngrowth", color=INK, font_size=16, weight=BOLD).move_to(revenue_pos)
        adspend_label  = Text("ad_spend", color=INK, font_size=18, weight=BOLD).move_to(adspend_pos)
        pricing_label  = Text("pricing\nstrategy", color=INK, font_size=14).move_to(pricing_pos)
        # awareness label placed to the left of the node (arrows approach from left-down, right)
        awareness_lbl_txt = Text("awareness", color=INK, font_size=14)
        awareness_lbl_txt.move_to([2.2, 1.9, 0])
        awareness_lbl_bg = Rectangle(
            width=awareness_lbl_txt.width + 0.12, height=awareness_lbl_txt.height + 0.08,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(awareness_lbl_txt.get_center())
        awareness_label = VGroup(awareness_lbl_bg, awareness_lbl_txt)

        # Direct arrow: brand -> revenue
        direct_arrow = Arrow(
            start=[-4.05, 0.0, 0], end=[4.05, 0.0, 0],
            color=INK, tip_length=0.15, buff=0.0
        )

        # Ad spend arrows: adspend -> brand, adspend -> revenue
        adspend_to_brand = Arrow(
            start=[adspend_pos[0] - 0.35, adspend_pos[1] - 0.2, 0],
            end=[brand_pos[0] + 0.3, brand_pos[1] + 0.25, 0],
            color="#E06400", tip_length=0.15, buff=0.0
        )
        adspend_to_revenue = Arrow(
            start=[adspend_pos[0] + 0.35, adspend_pos[1] - 0.2, 0],
            end=[revenue_pos[0] - 0.25, revenue_pos[1] + 0.25, 0],
            color="#E06400", tip_length=0.15, buff=0.0
        )
        adspend_arrows = VGroup(adspend_to_brand, adspend_to_revenue)

        # Pricing arrows (mediator): brand -> pricing, pricing -> revenue
        brand_to_pricing = Arrow(
            start=[brand_pos[0] + 0.3, brand_pos[1] - 0.2, 0],
            end=[pricing_pos[0] - 0.35, pricing_pos[1] + 0.1, 0],
            color="#0055AA", tip_length=0.15, buff=0.0
        )
        pricing_to_revenue = Arrow(
            start=[pricing_pos[0] + 0.35, pricing_pos[1] + 0.1, 0],
            end=[revenue_pos[0] - 0.3, revenue_pos[1] - 0.25, 0],
            color="#0055AA", tip_length=0.15, buff=0.0
        )
        pricing_arrows = VGroup(brand_to_pricing, pricing_to_revenue)

        # Awareness arrows (collider): brand -> awareness, revenue -> awareness
        brand_to_awareness = Arrow(
            start=[brand_pos[0] + 0.35, brand_pos[1] + 0.25, 0],
            end=[awareness_pos[0] - 0.4, awareness_pos[1] - 0.1, 0],
            color=CRIMSON, tip_length=0.15, buff=0.0
        )
        revenue_to_awareness = Arrow(
            start=[revenue_pos[0] - 0.15, revenue_pos[1] + 0.4, 0],
            end=[awareness_pos[0] + 0.2, awareness_pos[1] + 0.1, 0],
            color=CRIMSON, tip_length=0.15, buff=0.0
        )
        awareness_arrows = VGroup(brand_to_awareness, revenue_to_awareness)

        # "do not adjust" warning for mediator (pricing) — placed left of bottom
        mediator_warn_txt = Text("do not adjust", color=CRIMSON, font_size=20)
        mediator_warn_txt.move_to([-2.5, -3.0, 0])
        mediator_warn_bg = Rectangle(
            width=mediator_warn_txt.width + 0.15, height=mediator_warn_txt.height + 0.08,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(mediator_warn_txt.get_center())
        mediator_warning = VGroup(mediator_warn_bg, mediator_warn_txt)

        # "do not adjust" warning for collider (awareness) — y=2.4 (below title)
        collider_warn_txt = Text("do not adjust", color=CRIMSON, font_size=20)
        collider_warn_txt.move_to([3.5, 2.4, 0])
        collider_warn_bg = Rectangle(
            width=collider_warn_txt.width + 0.15, height=collider_warn_txt.height + 0.08,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(collider_warn_txt.get_center())
        collider_warning = VGroup(collider_warn_bg, collider_warn_txt)

        # Legend (bottom-right area)
        def legend_item(fill_col, label_str, x, y):
            rect = Rectangle(width=0.3, height=0.25, fill_color=fill_col,
                              fill_opacity=1, stroke_width=0, stroke_opacity=0).move_to([x, y, 0])
            lbl  = Text(label_str, color=INK, font_size=18).move_to([x + 0.85, y, 0])
            return VGroup(rect, lbl)

        legend = VGroup(
            legend_item(GOLD,      "confounder", 3.8, -2.1),
            legend_item("#CCE5FF", "mediator",   3.8, -2.5),
            legend_item("#FFD6D6", "collider",   3.8, -2.9),
        )

        # Verdict — within safe area (y >= -3.4), place at y=-3.2
        verdict_text = Text("Adjust for ad_spend only",
                            color=PASS_CLR, font_size=26, weight=BOLD).move_to([2.5, -3.0, 0])

        # 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(brand_node), FadeIn(revenue_node),
                  FadeIn(direct_arrow), Write(brand_label), Write(revenue_label))
        self.play(FadeIn(adspend_node), Write(adspend_label), FadeIn(adspend_arrows))
        self.play(FadeIn(pricing_node), Write(pricing_label), FadeIn(pricing_arrows))
        self.play(Write(mediator_warning))
        self.play(FadeIn(awareness_node), Write(awareness_label), FadeIn(awareness_arrows))
        self.play(Write(collider_warning), FadeIn(legend), Write(verdict_text))
        self.wait(1)
