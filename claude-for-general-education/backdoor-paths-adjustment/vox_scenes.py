import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_BackdoorPaths(Scene):
    def construct(self):
        dur = DUR.get("B04", 20.0)
        title = Text("Backdoor Paths: Pricing DAG", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        dag_lbl = Text("DAG: Brand, Comp, Quality each -> T and -> Y;  T -> Y",
                       font="Prism", font_size=14, color=SLATE)
        dag_lbl.move_to([0, 2.8, 0])
        self.play(FadeIn(dag_lbl), run_time=0.3)
        sep = Line(start=[-5.5, 2.4, 0], end=[5.5, 2.4, 0], color=INK, stroke_width=2)
        self.play(Create(sep), run_time=0.3)
        path_hdr = Text("Backdoor Paths from T to Y:", font="Prism", font_size=17, color=INK, weight=BOLD)
        path_hdr.move_to([-2.0, 2.0, 0])
        self.play(FadeIn(path_hdr), run_time=0.25)
        paths = [
            ("1.", "T  <-  Brand  ->  Y", "Brand"),
            ("2.", "T  <-  Comp   ->  Y", "Comp"),
            ("3.", "T  <-  Quality ->  Y", "Quality"),
        ]
        y_top = 1.4
        for i, (num, path_str, blocker) in enumerate(paths):
            y = y_top - i * 0.75
            path_bg = Rectangle(width=9.0, height=0.6, fill_color=CREAM,
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
            path_bg.move_to([0, y, 0])
            self.play(GrowFromCenter(path_bg), run_time=0.25)
            num_bg = Rectangle(width=0.4, height=0.5, fill_color=CREAM,
                               fill_opacity=1, stroke_width=0, stroke_opacity=0)
            num_bg.move_to([-4.5, y, 0])
            self.add(num_bg)
            num_lbl = Text(num, font="Prism", font_size=16, color=CRIMSON, weight=BOLD)
            num_lbl.move_to([-4.5, y, 0])
            path_lbl = Text(path_str, font="Prism", font_size=16, color=INK)
            path_lbl.move_to([0.2, y, 0])
            self.play(FadeIn(num_lbl), FadeIn(path_lbl), run_time=0.3)
        adj_box = Rectangle(width=7.0, height=0.75, fill_color=GOLD,
                            fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        adj_box.move_to([0, -0.95, 0])
        self.play(GrowFromCenter(adj_box), run_time=0.4)
        adj_lbl = Text("Adjustment Set: { Brand, Comp, Quality }", font="Prism", font_size=18, color=CRIMSON, weight=BOLD)
        adj_lbl.move_to([0, -0.95, 0])
        self.play(FadeIn(adj_lbl), run_time=0.3)
        verify_hdr = Text("Each path blocked by one set member:", font="Prism", font_size=15, color=SLATE)
        verify_hdr.move_to([0, -1.65, 0])
        self.play(FadeIn(verify_hdr), run_time=0.25)
        for i, (_, path_str, blocker) in enumerate(paths):
            y = -2.1 - i * 0.5
            check_bg = Rectangle(width=6.0, height=0.4, fill_color=CREAM,
                                 fill_opacity=1, stroke_width=0, stroke_opacity=0)
            check_bg.move_to([0, y, 0])
            self.play(GrowFromCenter(check_bg), run_time=0.15)
            check_lbl = Text(f"{path_str}  ->  block on {blocker}  v", font="Prism", font_size=13, color=INK)
            check_lbl.move_to([0, y, 0])
            self.play(FadeIn(check_lbl), run_time=0.2)
        self.wait(max(0, dur - 6.0))


class B06_AdjustmentVerify(Scene):
    def construct(self):
        dur = DUR.get("B06", 14.0)
        title = Text("New Edge: Comp -> Brand", font="Prism", font_size=26, color=INK, weight=BOLD)
        title.move_to([0, 3.4, 0])
        self.play(FadeIn(title), run_time=0.4)
        new_edge_box = Rectangle(width=5.5, height=0.65, fill_color=CREAM,
                                 fill_opacity=1, stroke_color=CRIMSON, stroke_width=2)
        new_edge_box.move_to([0, 2.7, 0])
        self.play(GrowFromCenter(new_edge_box), run_time=0.35)
        new_edge_lbl = Text("Added: Comp -> Brand", font="Prism", font_size=17, color=CRIMSON, weight=BOLD)
        new_edge_lbl.move_to([0, 2.7, 0])
        self.play(FadeIn(new_edge_lbl), run_time=0.3)
        sep = Line(start=[-5.5, 2.3, 0], end=[5.5, 2.3, 0], color=SLATE, stroke_width=1.5)
        self.play(Create(sep), run_time=0.3)
        all_paths_hdr = Text("All backdoor paths (updated):", font="Prism", font_size=16, color=INK, weight=BOLD)
        all_paths_hdr.move_to([-1.5, 1.9, 0])
        self.play(FadeIn(all_paths_hdr), run_time=0.25)
        paths = [
            ("1.", "T <- Brand -> Y",          "Brand", False),
            ("2.", "T <- Comp -> Y",            "Comp",  False),
            ("3.", "T <- Quality -> Y",         "Quality",False),
            ("4.", "T <- Brand <- Comp -> Y",   "Brand + Comp", True),
        ]
        y_top = 1.4
        for i, (num, path_str, blocker, is_new) in enumerate(paths):
            y = y_top - i * 0.72
            bg_clr = GOLD if is_new else CREAM
            path_bg = Rectangle(width=9.5, height=0.6, fill_color=bg_clr,
                                fill_opacity=0.7 if is_new else 1.0,
                                stroke_width=0, stroke_opacity=0)
            path_bg.move_to([0, y, 0])
            self.play(GrowFromCenter(path_bg), run_time=0.25)
            num_bg = Rectangle(width=0.4, height=0.5, fill_color=bg_clr,
                               fill_opacity=1, stroke_width=0, stroke_opacity=0)
            num_bg.move_to([-4.7, y, 0])
            self.add(num_bg)
            num_lbl = Text(num, font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
            num_lbl.move_to([-4.7, y, 0])
            path_lbl = Text(path_str, font="Prism", font_size=15, color=INK)
            path_lbl.move_to([0.2, y, 0])
            self.play(FadeIn(num_lbl), FadeIn(path_lbl), run_time=0.25)
            if is_new:
                new_tag = Text("NEW", font="Prism", font_size=12, color=CRIMSON, weight=BOLD)
                new_tag.move_to([4.5, y, 0])
                self.play(FadeIn(new_tag), run_time=0.2)
        verdict_box = Rectangle(width=7.5, height=0.7, fill_color=GOLD,
                                fill_opacity=0.9, stroke_color=CRIMSON, stroke_width=2)
        verdict_box.move_to([0, -1.6, 0])
        self.play(GrowFromCenter(verdict_box), run_time=0.4)
        verdict_lbl = Text("Adj set unchanged — {Brand, Comp, Quality} still blocks all 4", font="Prism", font_size=15, color=CRIMSON, weight=BOLD)
        verdict_lbl.move_to([0, -1.6, 0])
        self.play(FadeIn(verdict_lbl), run_time=0.3)
        self.wait(max(0, dur - 5.5))
