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


class B04_GhostTrackDAG(Scene):
    def construct(self):
        # Title
        title = Text("GHOSTTRACK SPOTIFY DAG",
                     color=INK, weight=BOLD, font_size=36).move_to([0, 3.2, 0])

        # Node positions
        organic_pos   = [-4.5,  0.0, 0]
        viral_pos     = [ 4.5,  0.0, 0]
        promo_pos     = [ 0.0,  2.5, 0]
        play_pos      = [ 2.5, -1.8, 0]

        # Nodes
        organic_node = Circle(radius=0.45, color=INK,
                              fill_color=CREAM, fill_opacity=1).move_to(organic_pos)
        viral_node   = Circle(radius=0.45, color=INK,
                              fill_color=CREAM, fill_opacity=1).move_to(viral_pos)
        promo_node   = Circle(radius=0.45, color=CRIMSON,
                              fill_color="#FFE5E5", fill_opacity=1).move_to(promo_pos)
        play_node    = Circle(radius=0.35, color=SLATE,
                              fill_color=CREAM, fill_opacity=1).move_to(play_pos)

        # Labels — centered on nodes
        organic_label = Text("organic\nfeatures", color=INK, font_size=18, weight=BOLD).move_to(organic_pos)
        viral_label   = Text("viral_flag", color=INK, font_size=18, weight=BOLD).move_to(viral_pos)
        promo_label   = Text("latent\npromotion", color=CRIMSON, font_size=16, weight=BOLD).move_to(promo_pos)
        play_label    = Text("play\ncount", color=SLATE, font_size=16).move_to(play_pos)

        # UNOBSERVED label — placed right of promo node, clear of arrows
        # Arrows from promo pass left-down and right-down; x=2.0 y=2.5 is clear
        unobserved_txt = Text("UNOBSERVED", color=CRIMSON, font_size=20, weight=BOLD)
        unobserved_txt.move_to([2.2, 2.5, 0])
        unobserved_bg = Rectangle(
            width=unobserved_txt.width + 0.18, height=unobserved_txt.height + 0.1,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(unobserved_txt.get_center())
        unobserved_label = VGroup(unobserved_bg, unobserved_txt)

        # Arrows
        organic_to_viral_arrow = Arrow(
            start=[-4.05, 0.0, 0], end=[4.05, 0.0, 0],
            color=PASS_CLR, tip_length=0.2, buff=0.0
        )
        causal_label_txt = Text("causal path", color=PASS_CLR, font_size=20)
        causal_label_txt.move_to([0.0, 0.3, 0])
        causal_label_bg = Rectangle(
            width=causal_label_txt.width + 0.15, height=causal_label_txt.height + 0.08,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(causal_label_txt.get_center())
        causal_label = VGroup(causal_label_bg, causal_label_txt)

        promo_to_organic_arrow = Arrow(
            start=[promo_pos[0] - 0.35, promo_pos[1] - 0.2, 0],
            end=[organic_pos[0] + 0.3, organic_pos[1] + 0.3, 0],
            color=CRIMSON, tip_length=0.2, buff=0.0
        )
        promo_to_play_arrow = Arrow(
            start=[promo_pos[0] + 0.2, promo_pos[1] - 0.35, 0],
            end=[play_pos[0] - 0.15, play_pos[1] + 0.3, 0],
            color=CRIMSON, tip_length=0.2, buff=0.0
        )
        play_to_viral_arrow = Arrow(
            start=[play_pos[0] + 0.3, play_pos[1] + 0.1, 0],
            end=[viral_pos[0] - 0.3, viral_pos[1] - 0.2, 0],
            color=CRIMSON, tip_length=0.2, buff=0.0
        )

        # Back-door label with CREAM bg
        backdoor_txt = Text("back-door: UNBLOCKED", color=CRIMSON, font_size=26, weight=BOLD)
        backdoor_txt.move_to([0.0, -2.7, 0])
        backdoor_bg = Rectangle(
            width=backdoor_txt.width + 0.2, height=backdoor_txt.height + 0.1,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(backdoor_txt.get_center())
        backdoor_label = VGroup(backdoor_bg, backdoor_txt)

        # Verdict with CREAM bg to avoid text-on-line Gate B errors
        verdict_txt_obj = Text("Effect NOT identified — promotion unmeasured",
                               color=CRIMSON, font_size=26, weight=BOLD)
        verdict_txt_obj.move_to([0, -3.1, 0])
        verdict_bg = Rectangle(
            width=verdict_txt_obj.width + 0.2, height=verdict_txt_obj.height + 0.1,
            fill_color=CREAM, fill_opacity=1, stroke_width=0, stroke_opacity=0
        ).move_to(verdict_txt_obj.get_center())
        verdict_text = VGroup(verdict_bg, verdict_txt_obj)

        # 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(organic_node), FadeIn(viral_node),
                  Write(organic_label), Write(viral_label))
        self.play(FadeIn(organic_to_viral_arrow), Write(causal_label))
        self.play(FadeIn(promo_node), Write(promo_label), Write(unobserved_label))
        self.play(FadeIn(promo_to_organic_arrow), FadeIn(promo_to_play_arrow),
                  FadeIn(play_node), Write(play_label))
        self.play(FadeIn(play_to_viral_arrow), Write(backdoor_label))
        self.play(Write(verdict_text))
        self.wait(1)
