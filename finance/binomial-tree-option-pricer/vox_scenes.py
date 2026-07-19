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


class B04_BinomialTree(Scene):
    def construct(self):
        u = 1.0733
        d = 1.0 / u
        K = 100.0

        def S_val(step, j):
            return 100.0 * (u ** (step - j)) * (d ** j)

        terminal_payoff = [max(S_val(4, j) - K, 0.0) for j in range(5)]

        def node_pos(step, j):
            x = -4.5 + step * 2.0
            n_above = (step / 2.0) - j
            y = n_above * 0.65
            return [x, y, 0]

        def make_node_label(price_str, pos, txt_color=INK):
            t = Text(price_str, color=txt_color, font_size=15)
            t.move_to(pos)
            bg = Rectangle(
                width=0.58, height=0.32,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=1.0, stroke_color=INK
            )
            bg.move_to(pos)
            return VGroup(bg, t)

        def make_payoff_label(payoff_str, pos):
            t = Text(payoff_str, color=CRIMSON, font_size=14)
            t.move_to(pos)
            bg = Rectangle(
                width=t.width + 0.14, height=t.height + 0.08,
                fill_color=CREAM, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            )
            bg.move_to(pos)
            return VGroup(bg, t)

        def short_line(p1, p2, margin=0.32):
            """Draw a line between p1 and p2, shrunk by margin at each end."""
            import math
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            dist = math.sqrt(dx**2 + dy**2)
            if dist < 2 * margin:
                return None
            ux = dx / dist
            uy = dy / dist
            sp = [p1[0] + ux * margin, p1[1] + uy * margin, 0]
            ep = [p2[0] - ux * margin, p2[1] - uy * margin, 0]
            return Line(sp, ep, color=SLATE, stroke_width=1.5)

        # ---- Title ----
        title = Text("BINOMIAL TREE — N=4 STEPS", color=INK, font_size=32, weight=BOLD)
        title.move_to([0, 3.2, 0])

        # Step labels at y=2.55 (below title)
        step_labels = VGroup()
        for step in range(5):
            x = -4.5 + step * 2.0
            lbl_str = "T=0.5" if step == 4 else f"t={step}"
            sl = Text(lbl_str, color=SLATE, font_size=18)
            sl.move_to([x, 2.55, 0])
            step_labels.add(sl)

        # ---- Step 0 ----
        s0_pos = node_pos(0, 0)
        s0_node_lbl = make_node_label(f"${S_val(0,0):.0f}", s0_pos)

        # ---- Steps 1-3: nodes + edges ----
        def build_step(step):
            nodes = VGroup()
            edges = VGroup()
            for j in range(step + 1):
                pos = node_pos(step, j)
                nl = make_node_label(f"${S_val(step,j):.0f}", pos)
                nodes.add(nl)
                if step > 0:
                    if j < step:
                        ppos = node_pos(step - 1, j)
                        ln = short_line(ppos, pos)
                        if ln:
                            edges.add(ln)
                    if j > 0:
                        ppos = node_pos(step - 1, j - 1)
                        ln = short_line(ppos, pos)
                        if ln:
                            edges.add(ln)
            return nodes, edges

        s1_nodes, s1_edges = build_step(1)
        s2_nodes, s2_edges = build_step(2)
        s3_nodes, s3_edges = build_step(3)

        # ---- Step 4: terminal nodes + edges + payoffs ----
        s4_nodes = VGroup()
        s4_edges = VGroup()
        terminal_payoff_labels = VGroup()

        for j in range(5):
            pos = node_pos(4, j)
            nl = make_node_label(f"${S_val(4,j):.0f}", pos)
            s4_nodes.add(nl)
            if j < 4:
                ppos = node_pos(3, j)
                ln = short_line(ppos, pos)
                if ln:
                    s4_edges.add(ln)
            if j > 0:
                ppos = node_pos(3, j - 1)
                ln = short_line(ppos, pos)
                if ln:
                    s4_edges.add(ln)
            pval = terminal_payoff[j]
            poff_pos = [pos[0] + 1.0, pos[1], 0]
            terminal_payoff_labels.add(make_payoff_label(f"C=${pval:.0f}", poff_pos))

        verdict_text = make_payoff_label("Converges to B-S: $10.45 at N=100", [0.0, -3.1, 0])

        # ---- Sequence (7 play() calls) ----
        self.play(Write(title), Write(step_labels))
        self.play(FadeIn(s0_node_lbl))
        self.play(FadeIn(s1_edges), FadeIn(s1_nodes))
        self.play(FadeIn(s2_edges), FadeIn(s2_nodes))
        self.play(FadeIn(s3_edges), FadeIn(s3_nodes))
        self.play(FadeIn(s4_edges), FadeIn(s4_nodes))
        self.play(Write(terminal_payoff_labels), Write(verdict_text))
