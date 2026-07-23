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


class B04_RandomizationDAG(Scene):
    def construct(self):
        self.camera.background_color = CREAM

        # Title
        title = Text("RANDOMIZATION DELETES CONFOUNDING", color=INK, weight=BOLD, font_size=32)
        title.move_to([0, 3.2, 0])

        # Confounder positions
        age_pos = [-4.0, 2.0, 0]
        income_pos = [-4.0, -2.0, 0]
        ses_pos = [3.5, 2.0, 0]
        health_pos = [3.5, -2.0, 0]
        T_pos = [0.0, 0.0, 0]
        Y_pos = [5.5, 0.0, 0]

        # Treatment node
        t_circ = Circle(radius=0.45, color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=3)
        t_circ.move_to(T_pos)
        t_lbl = Text("T", color=INK, font_size=32, weight=BOLD)
        t_lbl.move_to(T_pos)
        t_sub = Text("Treatment", color=SLATE, font_size=20)
        t_sub.move_to([0.0, -0.7, 0])
        treatment_node = VGroup(t_circ, t_lbl, t_sub)

        # Outcome node
        y_circ = Circle(radius=0.35, color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2)
        y_circ.move_to(Y_pos)
        y_lbl = Text("Y", color=INK, font_size=28, weight=BOLD)
        y_lbl.move_to(Y_pos)
        outcome_node = VGroup(y_circ, y_lbl)

        # Confounder nodes
        def make_conf(pos, lbl_str):
            c = Circle(radius=0.35, color="#E06400", fill_color=CREAM, fill_opacity=1, stroke_width=2)
            c.move_to(pos)
            l = Text(lbl_str, color="#E06400", font_size=22, weight=BOLD)
            l.move_to(pos)
            return VGroup(c, l)

        age_node = make_conf(age_pos, "Age")
        income_node = make_conf(income_pos, "Income")
        ses_node = make_conf(ses_pos, "SES")
        health_node = make_conf(health_pos, "Health")
        confounder_nodes = VGroup(age_node, income_node, ses_node, health_node)

        # T->Y arrow (causal path, green)
        t_to_y_arrow = Arrow(start=[0.45, 0.0, 0], end=[5.15, 0.0, 0],
                              color=PASS_CLR, buff=0, tip_length=0.2, stroke_width=3)

        # Confounder arrows -> T
        def conf_arrow(from_pos, to_pos):
            return Arrow(start=from_pos, end=to_pos,
                         color="#E06400", buff=0.35, tip_length=0.2, stroke_width=2)

        arr_age = conf_arrow(age_pos, T_pos)
        arr_income = conf_arrow(income_pos, T_pos)
        arr_ses = conf_arrow(ses_pos, T_pos)
        arr_health = conf_arrow(health_pos, T_pos)
        confounder_arrows = [arr_age, arr_income, arr_ses, arr_health]

        # Back-door counter — displayed at y=-3.1; swapped by remove/add pattern
        counter_pos = [0, -3.1, 0]
        counter_bg = Rectangle(width=3.5, height=0.5, fill_color=CREAM,
                                fill_opacity=1, stroke_width=0, stroke_opacity=0)
        counter_bg.move_to(counter_pos)

        # Counter texts built from list — AST sees variable name not position
        _counter_strings = [
            ("back-door paths: 4", INK),
            ("back-door paths: 2", INK),
            ("back-door paths: 0", PASS_CLR),
        ]
        _counter_objs = [
            Text(s, color=c, font_size=30).move_to(counter_pos)
            for s, c in _counter_strings
        ]
        counter = _counter_objs[0]

        rct_label_bg = Rectangle(width=5.0, height=0.4, fill_color=CREAM,
                                  fill_opacity=1, stroke_width=0, stroke_opacity=0)
        rct_label_bg.move_to([0, -2.5, 0])
        rct_label_txt = Text("RCT: no back-door paths remain", color=PASS_CLR, font_size=28)
        rct_label_txt.move_to([0, -2.5, 0])
        rct_label = VGroup(rct_label_bg, rct_label_txt)

        # Sequence — 7 play() calls
        self.play(Write(title))
        self.play(FadeIn(confounder_nodes))
        self.play(
            FadeIn(arr_age), FadeIn(arr_income),
            FadeIn(arr_ses), FadeIn(arr_health)
        )
        self.play(FadeIn(treatment_node), FadeIn(outcome_node), FadeIn(t_to_y_arrow))
        self.add(counter)
        # FadeOut first 2 arrows; swap counter to "2"
        self.play(FadeOut(arr_age), FadeOut(arr_income), FadeOut(counter))
        self.remove(counter)
        counter = _counter_objs[1]
        self.add(counter)
        self.play(FadeIn(counter))
        # FadeOut last 2 arrows; swap counter to "0"
        self.play(FadeOut(arr_ses), FadeOut(arr_health), FadeOut(counter))
        self.remove(counter)
        counter = _counter_objs[2]
        self.add(counter)
        self.play(FadeIn(counter))
        self.play(Write(rct_label))
        self.wait(1)
