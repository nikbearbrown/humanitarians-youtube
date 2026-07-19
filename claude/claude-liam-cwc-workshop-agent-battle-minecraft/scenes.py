"""
scenes.py — claude-liam-cwc-workshop-agent-battle-minecraft
Agent Battle: When Prompt Engineering Becomes a Sport.
Source: Anthropic CwC Workshop — agent-battle
"""

from manim import *

PAGE   = "#FAF9F5"
INK    = "#3D3929"
SPARK  = "#D97757"
SOFT   = "#73705F"
GHOST  = "#A9A491"
BORDER = "#E5E2D9"

config.background_color = PAGE


def source_caption(scene):
    cap = Text(
        "After Anthropic CwC Workshop — Agent Battle",
        font_size=16, color=GHOST,
    ).to_corner(DR, buff=0.25)
    scene.add(cap)


class B01_GameSetup(Scene):
    def construct(self):
        dur = 18.5

        title = Text("All Agents. Same World. Live Leaderboard.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Event server
        server = RoundedRectangle(
            width=3.0, height=1.5, corner_radius=0.18,
            color=SPARK, fill_color=PAGE, fill_opacity=1, stroke_width=2.2
        ).move_to([0, 0.4, 0])
        server_lbl = Text("Event Server\n(Minecraft world)", font_size=17, color=SPARK, weight=BOLD)
        server_lbl.move_to(server)

        # Agent nodes
        agent_positions = [(-4.5, 1.5), (-4.5, -0.7), (4.5, 1.5), (4.5, -0.7)]
        agent_labels = ["Agent A", "Agent B", "Agent C", "Agent D"]
        for pos, lbl in zip(agent_positions, agent_labels):
            ag = Circle(radius=0.45, color=INK, fill_color=PAGE, fill_opacity=1, stroke_width=1.8)
            ag.move_to([pos[0], pos[1], 0])
            ag_lbl = Text(lbl, font_size=14, color=INK)
            ag_lbl.move_to(ag)
            conn = Arrow(ag.get_center(), server.get_center(),
                         color=GHOST, stroke_width=1.5, buff=0.5,
                         max_tip_length_to_length_ratio=0.1)
            self.play(FadeIn(ag), FadeIn(ag_lbl), GrowArrow(conn), run_time=0.3)

        self.play(FadeIn(server), Write(server_lbl), run_time=0.5)

        # Leaderboard
        lb_box = Rectangle(
            width=3.5, height=2.4, color=BORDER,
            fill_color=PAGE, fill_opacity=1, stroke_width=1.5
        ).move_to([4.5, 0.4, 0])
        lb_hdr = Text("Leaderboard", font_size=16, color=INK, weight=BOLD)
        lb_hdr.next_to(lb_box, UP, buff=0.12)
        lb_rows = ["1. Agent C  7 💎", "2. Agent A  5 💎", "3. Agent D  3 💎", "4. Agent B  1 💎"]
        for i, row in enumerate(lb_rows):
            t = Text(row, font_size=14, color=SOFT if i > 0 else SPARK)
            t.move_to([4.5, 0.75 - i * 0.5, 0])
            self.add(t)
        self.play(FadeIn(lb_box), Write(lb_hdr), run_time=0.5)
        self.wait(dur - 4.0)


class B02_FourKnobs(Scene):
    def construct(self):
        dur = 20.8

        title = Text("Four Knobs. One Score.", font_size=38, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        knobs = [
            ("Model", "Which Claude variant\nto run."),
            ("System\nPrompt", "Strategy, persona,\ndecision framework."),
            ("Skills", "Python functions —\naction vocabulary."),
            ("MCP Tools", "External capabilities\nfrom servers."),
        ]

        xs = [-5.2, -1.8, 1.8, 5.2]
        for (label, detail), x in zip(knobs, xs):
            is_spark = label == "System\nPrompt"
            col = SPARK if is_spark else INK
            box = RoundedRectangle(
                width=3.0, height=2.4, corner_radius=0.18,
                color=col, fill_color=PAGE, fill_opacity=1, stroke_width=2.0
            ).move_to([x, 0.6, 0])
            lbl = Text(label, font_size=20, color=col, weight=BOLD)
            lbl.move_to(box).shift(UP * 0.6)
            dtl = Text(detail, font_size=14, color=SOFT)
            dtl.move_to(box).shift(DOWN * 0.3)
            self.play(FadeIn(VGroup(box, lbl, dtl)), run_time=0.35)

        score_lbl = Text("→ Score", font_size=22, color=SPARK, weight=BOLD)
        score_lbl.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(score_lbl), run_time=0.4)
        self.wait(dur - 3.5)


class B03_TokenEfficiency(Scene):
    def construct(self):
        dur = 19.2

        title = Text("Token Efficiency Is a First-Class Goal.", font_size=34, color=INK, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        self.add(title)
        source_caption(self)

        # Two agents: same diamonds, different tokens
        headers = ["Agent", "Diamonds", "Tokens", "Rank"]
        col_xs = [-5.0, -1.5, 2.0, 5.0]
        y_hdr = 2.0
        for hdr, x in zip(headers, col_xs):
            t = Text(hdr, font_size=18, color=INK, weight=BOLD)
            t.move_to([x, y_hdr, 0])
            self.add(t)
        div = Line(LEFT * 6.5, RIGHT * 6.5, color=BORDER, stroke_width=1.2).shift(UP * 1.65)
        self.add(div)

        rows = [
            ("Alpha", "7", "2,100", "1st", INK),
            ("Beta", "7", "4,800", "2nd", SPARK),
        ]
        for i, (name, diamonds, tokens, rank, col) in enumerate(rows):
            y = 1.0 - i * 1.0
            for val, x in zip([name, diamonds, tokens, rank], col_xs):
                t = Text(val, font_size=18, color=col)
                t.move_to([x, y, 0])
                self.play(Write(t), run_time=0.2)

        note = Text("Same diamonds. Fewer tokens wins.", font_size=20, color=SPARK, weight=BOLD)
        note.move_to([0, -1.2, 0])
        self.play(FadeIn(note), run_time=0.5)

        verdict = Text("Prompt engineering is now ranked, measurable, and comparable.", font_size=18, color=SOFT)
        verdict.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(verdict), run_time=0.5)
        self.wait(dur - 5.5)
