"""scenes.py — portrait (9:16) Manim scenes for claude-code-explained/short.
Full-length short (no beats cut): all 5 Manim beats re-laid-out for portrait —
B01, B02, B05, B08, B09. Not copies of the landscape scenes: the portrait frame
is narrow in x (frame_width=4.5, Gate B safe ±1.95) and unchanged in y
(frame_height=8.0, safe ±3.4), so every layout is restacked vertically with
next_to() chains rather than shrunk.

Same palette, helpers, timings and sourced numbers as ../scenes.py. DUR = the
measured actual_duration_s; cue times match the 16:9 scenes.
"""
from manim import *
import numpy as np

# `manim -r 2160,3840` does NOT reset the coordinate frame to portrait — without
# these two lines every scene below renders in the 16:9 default space
# (frame_width=14.222) and shrinks into the center of the canvas. This is the
# exact bug beat B07 of this reel is about.
config.frame_width = 4.5
config.frame_height = 8.0

CREAM = "#FAF9F5"; INK = "#3D3929"; TERRACOTTA = "#D97757"
TEAL = "#1F6F5C"; CRIMSON = "#BF3339"; SEC = "#6B6357"; RULE = "#D9D4C7"
MONO = "PT Mono"
SAFE_X = 1.95


def checkmark(color=TEAL, size=0.22):
    mark = VMobject(color=color, stroke_width=6)
    mark.set_points_as_corners([
        np.array([-0.5, 0.05, 0]) * size,
        np.array([-0.1, -0.45, 0]) * size,
        np.array([0.55, 0.5, 0]) * size,
    ])
    return mark


def handle(scene):
    """Visible author handle, lower-right inside the portrait safe area."""
    h = Text("Supriya", color=SEC, font_size=20, weight="BOLD").set_opacity(0.8)
    h.move_to([SAFE_X - 0.05, -3.25, 0], aligned_edge=RIGHT)
    scene.add(h)
    return h


def portrait_frame(height, color=INK):
    return Rectangle(width=height * 9 / 16, height=height, color=color, stroke_width=3,
                     fill_color=WHITE, fill_opacity=1)


def text_bars(width, n, gap, bar_h=0.1, first_w=0.8):
    bars = VGroup()
    for i in range(n):
        w = width * (first_w if i == 0 else (0.95 if i % 3 else 0.7))
        bars.add(RoundedRectangle(corner_radius=bar_h / 2, width=w, height=bar_h if i else bar_h * 1.6,
                                  stroke_width=0, fill_color=INK if i == 0 else SEC, fill_opacity=1))
    bars.arrange(DOWN, buff=gap, aligned_edge=LEFT)
    return bars


def wait_until(scene, elapsed, cue):
    if cue > elapsed:
        scene.wait(cue - elapsed)
        return cue
    return elapsed


def pad(scene, elapsed, target):
    scene.wait(max(0.4, target - elapsed - 0.2))


class B01_CannotWatch(Scene):
    """PROBLEM — every file check passes; the frame is a fifth full; 139.5 kbps."""
    DUR = 16.30

    def construct(self):
        self.camera.background_color = CREAM
        handle(self)
        elapsed = 0.0

        head = Text("A file check\nis not a look.", color=INK, weight="BOLD", font_size=40,
                    line_spacing=0.85).move_to([0, 2.75, 0])
        self.play(Write(head), run_time=1.2); elapsed += 1.2

        # The portrait frame (right) and the bitrate column (left) share one row.
        frame = portrait_frame(2.4)
        block = text_bars(frame.width * 0.8, 4, 0.07)
        block.scale_to_fit_height(frame.height * 0.17)
        block.move_to(frame.get_top() + DOWN * (frame.height * 0.03 + block.height / 2))
        fr = VGroup(frame, block)

        probe_lines = ["2160 × 3840", "h264 · yuv420p", "duration ✓ audio ✓"]
        rows = VGroup()
        for s in probe_lines:
            t = Text(s, font=MONO, color=INK, font_size=20)
            rows.add(VGroup(checkmark(size=0.3), t).arrange(RIGHT, buff=0.22))
        rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        probe_tag = Text("ffprobe", font=MONO, color=SEC, font_size=18)
        probe = VGroup(probe_tag, rows).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        probe.next_to(head, DOWN, buff=0.45).set_x(-SAFE_X + probe.width / 2)

        fr.next_to(probe, DOWN, buff=0.5).set_x(SAFE_X - frame.width / 2 - 0.02)
        self.play(Create(frame), run_time=0.8); elapsed += 0.8
        self.play(FadeIn(block, shift=DOWN * 0.05), run_time=0.6); elapsed += 0.6

        elapsed = wait_until(self, elapsed, 6.04)
        self.play(FadeIn(probe_tag), run_time=0.4); elapsed += 0.4
        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1], shift=RIGHT * 0.1), run_time=0.6)
            self.wait(0.5); elapsed += 1.1

        elapsed = wait_until(self, elapsed, 10.35)
        brace = Brace(block, direction=LEFT, color=CRIMSON, buff=0.06)
        # Label above the frame, not beside the brace: the bitrate column owns that space.
        fifth = Text("≈ 1/5", color=CRIMSON, font_size=26, weight="BOLD").next_to(frame, UP, buff=0.08,
                                                                              aligned_edge=LEFT)
        self.play(GrowFromCenter(brace), FadeIn(fifth), run_time=0.8); elapsed += 0.8

        elapsed = wait_until(self, elapsed, 12.59)
        label = Text("bitrate", font=MONO, color=SEC, font_size=20)
        num = DecimalNumber(139.5, num_decimal_places=1, color=CRIMSON, font_size=52)
        unit = Text("kbps", color=CRIMSON, font_size=26, weight="BOLD")
        rate = VGroup(num, unit).arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
        col = VGroup(label, rate).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        # Inset from the safe line; top-aligned with the frame so the caption stays above y=-3.4.
        col.move_to([-SAFE_X + 0.08 + col.width / 2, 0, 0]).align_to(frame, UP)
        num.set_value(0)
        self.play(FadeIn(label), FadeIn(rate), run_time=0.5); elapsed += 0.5
        self.play(ChangingDecimal(num, lambda a: 139.5 * a), run_time=1.6); elapsed += 1.6
        note = Text("true 4K pixels,\nalmost no picture", color=INK, font_size=22, slant="ITALIC",
                    line_spacing=0.85).next_to(col, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.7); elapsed += 0.7
        pad(self, elapsed, self.DUR)


class B02_TheLoop(Scene):
    """MECHANISM — plan → gate → execute → verify stacked; terracotta return arc."""
    DUR = 18.75

    def node(self, title, sub, owner):
        box = RoundedRectangle(corner_radius=0.14, width=3.4, height=1.1, color=INK, stroke_width=3,
                               fill_color=WHITE, fill_opacity=1)
        t = Text(title, color=INK, weight="BOLD", font_size=34)
        s = Text(sub, font=MONO, color=SEC, font_size=14)
        o = Text(owner, color=TEAL, font_size=17, weight="BOLD")
        VGroup(t, s, o).arrange(DOWN, buff=0.09).move_to(box.get_center())
        return VGroup(box, t, s, o)

    def construct(self):
        self.camera.background_color = CREAM
        handle(self)
        elapsed = 0.0

        specs = [("PLAN", "PLAN.md", "approved by a person"),
                 ("GATE", "PEDAGOGY.md · VERDICT: PASS", "a person signs, never the agent"),
                 ("EXECUTE", "run.sh → renders", "Claude"),
                 ("VERIFY", "_qc/ frames", "someone looks")]
        nodes = VGroup(*[self.node(*sp) for sp in specs]).arrange(DOWN, buff=0.36)
        nodes.move_to([-SAFE_X + 1.7, 0.55, 0])  # bottom label ends ≈ -2.7, clear of the handle
        arrows = [Arrow(nodes[i].get_bottom(), nodes[i + 1].get_top(), color=INK, stroke_width=5,
                        buff=0.05, max_tip_length_to_length_ratio=0.45) for i in range(3)]

        for i, (n, cue) in enumerate(zip(nodes, [1.44, 3.61, 9.56, 12.98])):
            elapsed = wait_until(self, elapsed, cue)
            if i:
                self.play(GrowArrow(arrows[i - 1]), run_time=0.4); elapsed += 0.4
            self.play(FadeIn(n, shift=UP * 0.12), run_time=0.6); elapsed += 0.6

        elapsed = wait_until(self, elapsed, 15.87)
        ret = CurvedArrow(nodes[3].get_right() + RIGHT * 0.05, nodes[0].get_right() + RIGHT * 0.05,
                          # Positive angle bulges RIGHT, outside the boxes; PI/5 peaks ≈ x 1.85 (< 1.95 safe).
                          angle=PI / 5, color=TERRACOTTA, stroke_width=7)
        ret_lbl = Text("fails → back to plan", color=TERRACOTTA, font_size=24,
                       weight="BOLD").next_to(nodes, DOWN, buff=0.28)
        self.play(Create(ret), FadeIn(ret_lbl, shift=UP * 0.05), run_time=0.9); elapsed += 0.9
        pad(self, elapsed, self.DUR)


class B05_FillBefore_After(Scene):
    """OUTPUT, cycle 1 — 55% → 86% of frame height, 276 → 341 kbps. Same bar thickness
    both sides: only the spacing changes (position, not size)."""
    DUR = 13.80

    def side(self, x, fill_frac, color, pct, kbps, label):
        frame = portrait_frame(3.3).move_to([x, 0.45, 0])
        bars = text_bars(frame.width * 0.78, 9, 0.1)
        gap = (frame.height * fill_frac - sum(b.height for b in bars)) / (len(bars) - 1)
        bars.arrange(DOWN, buff=gap, aligned_edge=LEFT)
        bars.move_to(frame.get_top() + DOWN * (frame.height * 0.05 + bars.height / 2))
        tag = Text(label, color=SEC, font_size=24, weight="BOLD").next_to(frame, UP, buff=0.15)
        p = Text(pct, color=color, font_size=46, weight="BOLD")
        k = DecimalNumber(kbps, num_decimal_places=0, color=color, font_size=30)
        ku = Text("kbps", color=color, font_size=20)
        kk = VGroup(k, ku).arrange(RIGHT, buff=0.08, aligned_edge=DOWN)
        stack = VGroup(p, kk).arrange(DOWN, buff=0.12).next_to(frame, DOWN, buff=0.25)
        return frame, bars, tag, stack, k

    def construct(self):
        self.camera.background_color = CREAM
        handle(self)
        elapsed = 0.0

        head = Text("The rebuild, rendered", color=INK, weight="BOLD", font_size=26).move_to([0, 3.05, 0])
        f0, b0, t0, s0, _ = self.side(-0.98, 0.55, CRIMSON, "55%", 276, "before")
        f1, b1, t1, s1, k1 = self.side(0.98, 0.86, TEAL, "86%", 276, "after")

        self.play(FadeIn(head), Create(f0), FadeIn(t0), run_time=0.7); elapsed += 0.7
        self.play(FadeIn(b0, shift=DOWN * 0.05), run_time=0.6); elapsed += 0.6
        self.play(FadeIn(s0), run_time=0.7); elapsed += 0.7
        self.wait(0.6); elapsed += 0.6
        self.play(Create(f1), FadeIn(t1), run_time=0.7); elapsed += 0.7
        self.play(TransformFromCopy(b0, b1), run_time=1.6); elapsed += 1.6
        self.play(FadeIn(s1[0]), FadeIn(s1[1]), run_time=0.7); elapsed += 0.7

        elapsed = wait_until(self, elapsed, 7.83)
        self.play(ChangingDecimal(k1, lambda a: 276 + (341 - 276) * a), run_time=1.6); elapsed += 1.6
        note = Text("same encoder settings", color=INK, font_size=24, slant="ITALIC").next_to(
            VGroup(s0, s1), DOWN, buff=0.3)
        self.play(FadeIn(note, shift=UP * 0.05), run_time=0.6); elapsed += 0.6
        pad(self, elapsed, self.DUR)


class B08_WholeFrame(Scene):
    """OUTPUT, cycle 2 — center quarter → full frame once the coordinate frame is portrait.
    Illustration of the mechanism (REBUILD LAW); numbers are the sourced ones."""
    DUR = 12.71

    def construct(self):
        self.camera.background_color = CREAM
        handle(self)
        elapsed = 0.0

        frame = portrait_frame(3.5).move_to([0, 1.55, 0])  # moral ends ≈ -2.8
        full = text_bars(frame.width * 0.84, 11, 0.12)
        full.stretch_to_fit_height(frame.height * 0.86).move_to(frame.get_center())
        small = full.copy().scale(0.5).move_to(frame.get_center())
        grid = VGroup(*[Line(frame.get_left() + UP * y, frame.get_right() + UP * y, color=RULE,
                             stroke_width=2) for y in np.linspace(-1.5, 1.5, 7)])
        self.play(Create(frame), run_time=0.7); elapsed += 0.7
        self.play(FadeIn(small), FadeIn(grid), run_time=0.7); elapsed += 0.7

        audit = VGroup(checkmark(CRIMSON, 0.28),
                       Text("layout audit: PASS", font=MONO, color=CRIMSON, font_size=19))
        audit.arrange(RIGHT, buff=0.18).next_to(frame, DOWN, buff=0.35)
        quarter = Text("≈ the center quarter", color=CRIMSON, font_size=24,
                       weight="BOLD").next_to(audit, DOWN, buff=0.18)
        self.play(Create(audit[0]), FadeIn(audit[1]), run_time=0.6); elapsed += 0.6
        self.play(FadeIn(quarter, shift=UP * 0.05), run_time=0.5); elapsed += 0.5

        cfg_old = Text("frame_width = 14.222", font=MONO, color=SEC, font_size=20).next_to(
            quarter, DOWN, buff=0.35)
        cfg_new = Text("frame_width = 4.5", font=MONO, color=TEAL, font_size=20).move_to(cfg_old)
        self.play(FadeIn(cfg_old), run_time=0.4); elapsed += 0.4

        elapsed = wait_until(self, elapsed, 3.83)
        grid_target = VGroup(*[Line(frame.get_left() + UP * y, frame.get_right() + UP * y, color=RULE,
                                    stroke_width=2) for y in np.linspace(-1.7, 1.7, 12)])
        self.play(Transform(cfg_old, cfg_new), Transform(grid, grid_target),
                  Transform(small, full), run_time=1.8); elapsed += 1.8

        gate_v = VGroup(checkmark(TEAL, 0.28),
                        Text("Gate V: PASS", font=MONO, color=TEAL, font_size=19))
        gate_v.arrange(RIGHT, buff=0.18).move_to(audit)
        full_lbl = Text("the full frame", color=TEAL, font_size=24, weight="BOLD").move_to(quarter)
        self.play(Transform(audit, gate_v), Transform(quarter, full_lbl), run_time=0.9); elapsed += 0.9

        elapsed = wait_until(self, elapsed, 8.36)
        moral = Text("right about its own coordinates,\nwrong about the video", color=INK,
                     font_size=21, slant="ITALIC", line_spacing=0.85).next_to(cfg_old, DOWN, buff=0.3)
        self.play(FadeIn(moral, shift=UP * 0.05), run_time=0.8); elapsed += 0.8
        pad(self, elapsed, self.DUR)


class B09_FourMoves(Scene):
    """SUMMARY — four moves and who owns each; the closing line is the lesson."""
    DUR = 10.77

    def construct(self):
        self.camera.background_color = CREAM
        handle(self)
        elapsed = 0.0

        rows_spec = [("Plan", "approved first", "you"),
                     ("Gate", "signed by a person", "you"),
                     ("Execute", "where Claude is fastest", "Claude"),
                     ("Verify", "by looking", "you")]
        cores, whos = VGroup(), []
        for name, what, who in rows_spec:
            ck = checkmark(TEAL, 0.36)
            n = Text(name, color=INK, weight="BOLD", font_size=44)
            VGroup(ck, n).arrange(RIGHT, buff=0.25)
            w = Text(what, color=SEC, font_size=24).next_to(n, DOWN, buff=0.1, aligned_edge=LEFT)
            cores.add(VGroup(ck, n, w))
            whos.append(Text(who, color=TEAL, font_size=26, weight="BOLD"))
        # Arrange the name/description cores first, THEN place owners — an owner left at
        # the origin inside a row would skew the arrangement.
        cores.arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        cores.move_to([0, 1.1, 0]).set_x(-SAFE_X + cores.width / 2)
        rows = VGroup()
        for c, o in zip(cores, whos):
            o.move_to([SAFE_X - 0.06, c[1].get_center()[1], 0], aligned_edge=RIGHT)
            rows.add(VGroup(c[0], c[1], c[2], o))

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), FadeIn(r[2]), FadeIn(r[3]), run_time=0.6)
            self.wait(1.3); elapsed += 1.9

        rule = Line(LEFT * SAFE_X, RIGHT * SAFE_X, color=RULE, stroke_width=3).next_to(rows, DOWN, buff=0.4)
        closer = Text("Both bugs looked\nfine on paper.", color=INK, font_size=36, slant="ITALIC",
                      line_spacing=0.85).next_to(rule, DOWN, buff=0.3)
        self.play(GrowFromEdge(rule, LEFT), run_time=0.35); elapsed += 0.35
        self.play(Write(closer), run_time=1.3); elapsed += 1.3
        pad(self, elapsed, self.DUR)
