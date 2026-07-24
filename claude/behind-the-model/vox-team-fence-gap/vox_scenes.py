import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B03_FiveNodes(Scene):
    """Five TEAL-fenced nodes connected to unprotected CRIMSON shared center."""

    def construct(self):
        dur = DUR.get("B03", 20.0)

        # Shared center rectangle (no fence — unprotected)
        center_box = Rectangle(width=2.4, height=1.4)
        center_box.set_fill(CRIMSON, 0.18)
        center_box.set_stroke(CRIMSON, 2.5)
        center_box.move_to([0.0, 0.0, 0.0])

        center_lbl = Text("Shared\nFolder", font=SANS, font_size=16, color=CRIMSON)
        center_lbl.move_to([0.0, 0.0, 0.0])

        # Five node positions (pentagon-ish around center)
        node_positions = [
            [-4.5, 2.2, 0.0],
            [0.0, 3.2, 0.0],
            [4.5, 2.2, 0.0],
            [4.0, -2.2, 0.0],
            [-4.0, -2.2, 0.0],
        ]

        # Draw nodes first (TEAL fences)
        node_circles = []
        for pos in node_positions:
            node_c = Circle(radius=0.55)
            node_c.set_fill(TEAL, 0.2)
            node_c.set_stroke(TEAL, 2.5)
            node_c.move_to(pos)
            node_circles.append(node_c)
            self.play(FadeIn(node_c), run_time=0.2)

        # Fence boxes around each node
        for pos in node_positions:
            fence = Rectangle(width=1.4, height=1.4)
            fence.set_fill(TEAL, 0.0)
            fence.set_stroke(TEAL, 1.5)
            fence.move_to(pos)
            self.play(FadeIn(fence), run_time=0.15)

        # Draw connections from each node to center
        conn_endpoints = [
            ([-4.0, 1.9, 0.0], [-1.2, 0.5, 0.0]),
            ([0.0, 2.65, 0.0], [0.0, 0.7, 0.0]),
            ([4.0, 1.9, 0.0], [1.2, 0.5, 0.0]),
            ([3.6, -1.9, 0.0], [1.2, -0.5, 0.0]),
            ([-3.6, -1.9, 0.0], [-1.2, -0.5, 0.0]),
        ]
        for start, end in conn_endpoints:
            line = Line(start, end, stroke_width=1.8, color=SLATE)
            self.play(Create(line), run_time=0.15)

        # Draw shared center last (no fence)
        self.play(FadeIn(center_box), run_time=0.4)
        self.play(FadeIn(center_lbl), run_time=0.3)

        # Label "NO FENCE" below center
        no_fence = Text("no fence", font=SANS, font_size=14, color=CRIMSON)
        no_fence.move_to([0.0, -1.0, 0.0])
        self.play(FadeIn(no_fence), run_time=0.3)

        # Bottom separator
        sep = Line([-5.5, -3.0, 0.0], [5.5, -3.0, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(sep), run_time=0.3)

        self.wait(max(0.1, dur - 5.5))


class B05_DropboxSpread(Scene):
    """Four nodes — one adds MCP, account-level access spreads to all four."""

    def construct(self):
        dur = DUR.get("B05", 22.0)

        # Four node boxes in a row
        node_xs = [-4.5, -1.5, 1.5, 4.5]
        node_labels = ["A", "B", "C", "D"]

        nodes = []
        for i, (x, lbl) in enumerate(zip(node_xs, node_labels)):
            box = Rectangle(width=1.4, height=1.0)
            box.set_fill(TEAL, 0.18)
            box.set_stroke(TEAL, 2)
            box.move_to([x, 2.2, 0.0])
            txt = Text(lbl, font=DISPLAY, font_size=22, color=TEAL)
            txt.move_to([x, 2.2, 0.0])
            nodes.append(VGroup(box, txt))
            self.play(FadeIn(box), run_time=0.2)
            self.play(FadeIn(txt), run_time=0.15)

        # Member A adds MCP server
        mcp_box = Rectangle(width=2.0, height=0.7)
        mcp_box.set_fill(SLATE, 0.2)
        mcp_box.set_stroke(TEAL, 1.8)
        mcp_box.move_to([-4.5, 0.9, 0.0])
        mcp_lbl = Text("MCP server\n(Dropbox)", font=SANS, font_size=12, color=TEAL)
        mcp_lbl.move_to([-4.5, 0.9, 0.0])

        arrow_a = Line([-4.5, 1.7, 0.0], [-4.5, 1.25, 0.0], stroke_width=2, color=TEAL)
        self.play(Create(arrow_a), run_time=0.3)
        self.play(FadeIn(mcp_box), run_time=0.3)
        self.play(FadeIn(mcp_lbl), run_time=0.25)

        # "Account level" label
        acct_note = Text("added at account level", font=SANS, font_size=13, color=CRIMSON)
        acct_note.move_to([0.0, 0.3, 0.0])
        self.play(FadeIn(acct_note), run_time=0.3)

        # Separator
        sep1 = Line([-5.5, 0.0, 0.0], [5.5, 0.0, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(sep1), run_time=0.3)

        # Shared Dropbox box
        db_box = Rectangle(width=3.0, height=0.9)
        db_box.set_fill(CRIMSON, 0.18)
        db_box.set_stroke(CRIMSON, 2.5)
        db_box.move_to([0.0, -1.0, 0.0])
        db_lbl = Text("Shared Dropbox", font=SANS, font_size=16, color=CRIMSON)
        db_lbl.move_to([0.0, -1.0, 0.0])
        self.play(FadeIn(db_box), run_time=0.4)
        self.play(FadeIn(db_lbl), run_time=0.3)

        # All four nodes connect to Dropbox via CRIMSON lines
        for x in node_xs:
            line = Line([x, 1.7, 0.0], [x * 0.3, -0.55, 0.0], stroke_width=2, color=CRIMSON)
            self.play(Create(line), run_time=0.2)

        # Confidential file label
        conf_box = Rectangle(width=2.8, height=0.6)
        conf_box.set_fill(CRIMSON, 0.15)
        conf_box.set_stroke(CRIMSON, 2)
        conf_box.move_to([0.0, -1.9, 0.0])
        conf_lbl = Text("client contracts: CONFIDENTIAL", font=SANS, font_size=12, color=CRIMSON)
        conf_lbl.move_to([0.0, -1.9, 0.0])
        self.play(FadeIn(conf_box), run_time=0.3)
        self.play(FadeIn(conf_lbl), run_time=0.3)

        # Bottom separator line
        bot_sep = Line([-5.5, -2.7, 0.0], [5.5, -2.7, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(bot_sep), run_time=0.3)

        self.wait(max(0.1, dur - 6.5))


class B06_SharedFence(Scene):
    """Two columns: shared center without fence vs with fence and labeled rules."""

    def construct(self):
        dur = DUR.get("B06", 22.0)

        # Divider
        div = Line([0.0, 3.0, 0.0], [0.0, -3.0, 0.0], stroke_width=1.5, color=SLATE)
        self.play(Create(div), run_time=0.3)

        # Left header (CRIMSON)
        lhdr = Text("No Shared Rules", font=DISPLAY, font_size=20, color=CRIMSON)
        lhdr.move_to([-3.0, 2.7, 0.0])
        self.play(FadeIn(lhdr), run_time=0.3)

        # Right header (TEAL)
        rhdr = Text("Shared Rules", font=DISPLAY, font_size=20, color=TEAL)
        rhdr.move_to([3.0, 2.7, 0.0])
        self.play(FadeIn(rhdr), run_time=0.3)

        # Left: small fenced individuals + unprotected shared center
        individual_positions_l = [[-4.5, 1.6, 0.0], [-3.0, 1.6, 0.0], [-4.5, 0.3, 0.0], [-3.0, 0.3, 0.0]]
        for pos in individual_positions_l:
            c = Rectangle(width=0.9, height=0.7)
            c.set_fill(TEAL, 0.15)
            c.set_stroke(TEAL, 1.5)
            c.move_to(pos)
            self.play(FadeIn(c), run_time=0.18)

        l_center = Rectangle(width=2.0, height=0.8)
        l_center.set_fill(CRIMSON, 0.18)
        l_center.set_stroke(CRIMSON, 2)
        l_center.move_to([-3.5, -0.9, 0.0])
        l_center_lbl = Text("shared\n(no fence)", font=SANS, font_size=14, color=CRIMSON)
        l_center_lbl.move_to([-3.5, -0.9, 0.0])
        self.play(FadeIn(l_center), run_time=0.3)
        self.play(FadeIn(l_center_lbl), run_time=0.3)

        # Right: shared center with its own TEAL fence + 3 rule labels
        r_fence = Rectangle(width=4.5, height=2.8)
        r_fence.set_fill(TEAL, 0.06)
        r_fence.set_stroke(TEAL, 2.5)
        r_fence.move_to([3.0, 0.3, 0.0])
        self.play(FadeIn(r_fence), run_time=0.4)

        r_center = Rectangle(width=1.8, height=0.7)
        r_center.set_fill(TEAL, 0.2)
        r_center.set_stroke(TEAL, 2)
        r_center.move_to([3.0, 1.4, 0.0])
        r_center_lbl = Text("shared\n(fenced)", font=SANS, font_size=14, color=TEAL)
        r_center_lbl.move_to([3.0, 1.4, 0.0])
        self.play(FadeIn(r_center), run_time=0.3)
        self.play(FadeIn(r_center_lbl), run_time=0.3)

        # Three rule chips inside fence
        rules = ["data scope", "connector approval", "who is accountable"]
        rule_ys = [0.5, -0.1, -0.7]
        for rule, y in zip(rules, rule_ys):
            r_chip = Rectangle(width=4.0, height=0.48)
            r_chip.set_fill(TEAL, 0.12)
            r_chip.set_stroke(TEAL, 1.2)
            r_chip.move_to([3.0, y, 0.0])
            r_chip_lbl = Text(rule, font=SANS, font_size=13, color=TEAL)
            r_chip_lbl.move_to([3.0, y, 0.0])
            self.play(FadeIn(r_chip), FadeIn(r_chip_lbl), run_time=0.3)

        # Bottom separator
        bot_sep = Line([-5.5, -2.0, 0.0], [5.5, -2.0, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(bot_sep), run_time=0.3)

        self.wait(max(0.1, dur - 6.5))


class B07_TeamChecklist(Scene):
    """Three TEAL checklist chips for team capability evaluation."""

    def construct(self):
        dur = DUR.get("B07", 18.0)

        # Title
        title = Text("Before any team member adds a capability:", font=DISPLAY, font_size=20, color=TEAL)
        title.move_to([0.0, 2.8, 0.0])
        self.play(FadeIn(title), run_time=0.4)

        steps = [
            ("1", "What shared systems does it touch?"),
            ("2", "One account or all members?"),
            ("3", "Who owns the decision?"),
        ]

        chip_ys = [1.5, 0.3, -0.9]

        for i, (num, text) in enumerate(steps):
            y = chip_ys[i]

            num_circ = Circle(radius=0.36)
            num_circ.set_fill(TEAL, 0.35)
            num_circ.set_stroke(TEAL, 2)
            num_circ.move_to([-4.2, y, 0.0])

            num_lbl = Text(num, font=DISPLAY, font_size=22, color=TEAL)
            num_lbl.move_to([-4.2, y, 0.0])

            chip_box = Rectangle(width=7.5, height=0.72)
            chip_box.set_fill(TEAL, 0.1)
            chip_box.set_stroke(TEAL, 1.5)
            chip_box.move_to([0.5, y, 0.0])

            step_lbl = Text(text, font=SANS, font_size=18, color=TEAL)
            step_lbl.move_to([0.5, y, 0.0])

            self.play(FadeIn(num_circ), FadeIn(num_lbl), run_time=0.3)
            self.play(FadeIn(chip_box), FadeIn(step_lbl), run_time=0.35)

        # Separator
        sep = Line([-5.5, -1.9, 0.0], [5.5, -1.9, 0.0], stroke_width=1.2, color=SLATE)
        self.play(Create(sep), run_time=0.3)

        note = Text("Write it down before anyone connects anything.", font=SANS, font_size=15, color=SLATE)
        note.move_to([0.0, -2.5, 0.0])
        self.play(FadeIn(note), run_time=0.4)

        self.wait(max(0.1, dur - 5.0))
