"""scenes.py — Manim scenes for claude-code-explained (cli-explainer).
5 Manim beats (B01, B02, B05, B08, B09); the other 7 render via Remotion.
Claude-skin palette: cream ground, warm ink, one terracotta accent (the loop's
return arrow — the one move the reel is about), plus the functional
teal/crimson pass/fail pair used in the banking reels.
Class names are `B0X_Name(Scene)` — required for run.sh's scene-detection regex.
No LaTeX (Text/Pango only). Every number on screen is a sourced figure from
FACTCHECK.md; nothing is invented.

Every scene carries the "Supriya" corner handle (PM requirement 4 / LOGO LAW) —
see `handle()`.

DUR values are the measured actual_duration_s from mp3/timings.json (audio locked
2026-10-01); narration cue times were rescaled by actual/estimated per beat.
If audio is ever regenerated, reconcile again — never hand-trim an mp4.
"""
from manim import *
import numpy as np

CREAM = "#FAF9F5"; INK = "#3D3929"; TERRACOTTA = "#D97757"
TEAL = "#1F6F5C"; CRIMSON = "#BF3339"; SEC = "#6B6357"; RULE = "#D9D4C7"
MONO = "PT Mono"


def checkmark(color=TEAL, size=0.32):
    """A real vector checkmark — Gate A's distinctness stub ignores Text, so a
    glyph-as-check reads as 'no shape ever changes'."""
    mark = VMobject(color=color, stroke_width=7)
    mark.set_points_as_corners([
        np.array([-0.5, 0.05, 0]) * size,
        np.array([-0.1, -0.45, 0]) * size,
        np.array([0.55, 0.5, 0]) * size,
    ])
    return mark


def handle(scene):
    """Visible author handle, lower-right inside the safe area, on from frame 0."""
    h = Text("Supriya", color=SEC, font_size=26, weight="BOLD").set_opacity(0.8)
    h.to_corner(DR, buff=0.9)  # right edge ≈ 6.21, inside Gate B's ±6.3 safe x
    scene.add(h)
    return h


def portrait_frame(height, color=INK):
    """A 9:16 frame outline — the canvas the reel's two bugs were about."""
    return Rectangle(width=height * 9 / 16, height=height, color=color, stroke_width=4,
                     fill_color=WHITE, fill_opacity=1)


def text_bars(width, n, gap, bar_h=0.16, first_w=0.8):
    """Stand-in 'content' lines for a frame: a title bar then shorter body bars."""
    bars = VGroup()
    for i in range(n):
        w = width * (first_w if i == 0 else (0.95 if i % 3 else 0.7))
        bars.add(RoundedRectangle(corner_radius=bar_h / 2, width=w, height=bar_h if i else bar_h * 1.6,
                                  stroke_width=0, fill_color=INK if i == 0 else SEC, fill_opacity=1))
    bars.arrange(DOWN, buff=gap, aligned_edge=LEFT)
    return bars


def pad(scene, elapsed, target):
    scene.wait(max(0.4, target - elapsed - 0.2))


class B01_CannotWatch(Scene):
    """PROBLEM — every file check passes; the frame is still a fifth full; 139.5 kbps."""
    DUR = 16.30

    def construct(self):
        self.camera.background_color = CREAM
        handle(self)
        elapsed = 0.0

        head = Text("A file check is not a look.", color=INK, weight="BOLD",
                    font_size=52).to_edge(UP, buff=0.7)
        self.play(Write(head), run_time=1.2); elapsed += 1.2

        # Right: the portrait frame with content only in its top fifth.
        frame = portrait_frame(5.4).move_to([3.0, -0.55, 0])  # clear of the corner handle
        block = text_bars(frame.width * 0.8, 4, 0.12)
        block.scale_to_fit_height(frame.height * 0.17)
        block.move_to(frame.get_top() + DOWN * (frame.height * 0.03 + block.height / 2))
        self.play(Create(frame), run_time=0.8); elapsed += 0.8
        self.play(FadeIn(block, shift=DOWN * 0.1), run_time=0.6); elapsed += 0.6

        # Left: the probe readout — every line passes.
        probe_lines = ["2160 × 3840", "h264 · yuv420p", "duration ✓ audio ✓"]
        rows = VGroup()
        for s in probe_lines:
            t = Text(s, font=MONO, color=INK, font_size=32)
            rows.add(VGroup(checkmark(size=0.42), t).arrange(RIGHT, buff=0.35))
        rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to([-3.1, 1.0, 0])
        probe_tag = Text("ffprobe", font=MONO, color=SEC, font_size=26).next_to(rows, UP, buff=0.35,
                                                                               aligned_edge=LEFT)
        # Word-cue times (rescaled to measured audio): "An earlier vertical cut…" ≈ 7.4s.
        cue = 6.04
        if cue > elapsed:
            self.wait(cue - elapsed); elapsed = cue
        self.play(FadeIn(probe_tag), run_time=0.4); elapsed += 0.4
        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1], shift=RIGHT * 0.15), run_time=0.6)
            self.wait(0.5); elapsed += 1.1

        # The fill measurement on the frame.
        brace = Brace(block, direction=LEFT, color=CRIMSON)
        fifth = Text("≈ 1/5", color=CRIMSON, font_size=34, weight="BOLD").next_to(brace, LEFT, buff=0.15)
        cue = 10.35  # "…the text filled a fifth of the frame"
        if cue > elapsed:
            self.wait(cue - elapsed); elapsed = cue
        self.play(GrowFromCenter(brace), FadeIn(fifth), run_time=0.8); elapsed += 0.8
        cue = 12.59  # "Bitrate: …"
        if cue > elapsed:
            self.wait(cue - elapsed); elapsed = cue

        # The bitrate, counted up and landing in crimson.
        label = Text("bitrate", font=MONO, color=SEC, font_size=30)
        # Lay out at the FINAL value so the unit clears the widest number, then reset;
        # DecimalNumber keeps its left edge fixed as the value changes.
        num = DecimalNumber(139.5, num_decimal_places=1, color=CRIMSON, font_size=96)
        unit = Text("kbps", color=CRIMSON, font_size=40, weight="BOLD")
        rate = VGroup(num, unit).arrange(RIGHT, buff=0.25, aligned_edge=DOWN)
        VGroup(label, rate).arrange(DOWN, buff=0.2, aligned_edge=LEFT).next_to(rows, DOWN, buff=0.9,
                                                                             aligned_edge=LEFT)
        num.set_value(0)
        self.play(FadeIn(label), FadeIn(rate), run_time=0.5); elapsed += 0.5
        self.play(ChangingDecimal(num, lambda a: 139.5 * a), run_time=1.6); elapsed += 1.6
        note = Text("true 4K pixels, almost no picture", color=INK, font_size=30,
                    slant="ITALIC").next_to(rate, DOWN, buff=0.35, aligned_edge=LEFT)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.7); elapsed += 0.7
        pad(self, elapsed, self.DUR)


class B02_TheLoop(Scene):
    """MECHANISM — plan → gate → execute → verify, each with the real file that carries it;
    the terracotta return arrow is the point."""
    DUR = 18.75

    def node(self, title, sub, owner):
        box = RoundedRectangle(corner_radius=0.2, width=5.6, height=2.0, color=INK, stroke_width=4,
                               fill_color=WHITE, fill_opacity=1)
        t = Text(title, color=INK, weight="BOLD", font_size=50)
        s = Text(sub, font=MONO, color=SEC, font_size=22)
        o = Text(owner, color=TEAL, font_size=24, weight="BOLD")
        inner = VGroup(t, s, o).arrange(DOWN, buff=0.16)
        inner.move_to(box.get_center())
        return VGroup(box, inner)

    def construct(self):
        self.camera.background_color = CREAM
        handle(self)
        elapsed = 0.0

        specs = [("PLAN", "PLAN.md", "approved by a person", [-3.5, 1.65, 0]),
                 ("GATE", "PEDAGOGY.md · VERDICT: PASS", "signed by a person", [3.5, 1.65, 0]),
                 ("EXECUTE", "run.sh → renders", "Claude", [3.5, -1.75, 0]),
                 ("VERIFY", "_qc/ frames", "someone looks", [-3.5, -1.75, 0])]
        nodes = [self.node(a, b, c).move_to(p) for a, b, c, p in specs]
        # Spoken-word cue times (rescaled to measured audio) for each node's name.
        cues = [1.44, 3.61, 9.56, 12.98]
        arrows = [
            Arrow(nodes[0].get_right(), nodes[1].get_left(), color=INK, stroke_width=6, buff=0.15),
            Arrow(nodes[1].get_bottom(), nodes[2].get_top(), color=INK, stroke_width=6, buff=0.15),
            Arrow(nodes[2].get_left(), nodes[3].get_right(), color=INK, stroke_width=6, buff=0.15),
        ]
        for i, (n, cue) in enumerate(zip(nodes, cues)):
            if cue > elapsed:
                self.wait(cue - elapsed); elapsed = cue
            if i:
                self.play(GrowArrow(arrows[i - 1]), run_time=0.4); elapsed += 0.4
            self.play(FadeIn(n, shift=UP * 0.2), run_time=0.6); elapsed += 0.6

        never = Text("the agent never signs its own gate", color=SEC, font_size=26,
                     slant="ITALIC").next_to(nodes[1], UP, buff=0.25)
        self.play(FadeIn(never), run_time=0.5); elapsed += 0.5

        back_cue = 15.87
        if back_cue > elapsed:
            self.wait(back_cue - elapsed); elapsed = back_cue
        ret = Arrow(nodes[3].get_top(), nodes[0].get_bottom(), color=TERRACOTTA, stroke_width=10,
                    buff=0.15)
        ret_lbl = Text("fails → back to plan", color=TERRACOTTA, font_size=32,
                       weight="BOLD").next_to(ret, RIGHT, buff=0.3)
        self.play(GrowArrow(ret), FadeIn(ret_lbl, shift=RIGHT * 0.1), run_time=0.9); elapsed += 0.9
        pad(self, elapsed, self.DUR)


class B05_FillBefore_After(Scene):
    """OUTPUT, cycle 1 — the composer rebuild: 55% → 86% of frame height, 276 → 341 kbps."""
    DUR = 13.80

    def side(self, x, fill_frac, color, pct, kbps, label, outer):
        frame = portrait_frame(5.4).move_to([x, 0.1, 0])
        # Same bar thickness on both sides — only the SPACING changes, because the
        # rebuild moved anchors, not type size (B04's whole point).
        bars = text_bars(frame.width * 0.78, 9, 0.2)
        gap = (frame.height * fill_frac - sum(b.height for b in bars)) / (len(bars) - 1)
        bars.arrange(DOWN, buff=gap, aligned_edge=LEFT)
        top_inset = frame.height * 0.05
        bars.move_to(frame.get_top() + DOWN * (top_inset + bars.height / 2))
        tag = Text(label, color=SEC, font_size=30, weight="BOLD").next_to(frame, UP, buff=0.2)
        brace = Brace(bars, direction=outer, color=color)
        p = Text(pct, color=color, font_size=54, weight="BOLD")
        k = DecimalNumber(kbps, num_decimal_places=0, color=color, font_size=40)
        ku = Text("kbps", color=color, font_size=26)
        kk = VGroup(k, ku).arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
        stack = VGroup(p, kk).arrange(DOWN, buff=0.2)
        stack.next_to(brace, outer, buff=0.25)
        return frame, bars, tag, brace, stack, k

    def construct(self):
        self.camera.background_color = CREAM
        handle(self)
        elapsed = 0.0

        f0, b0, t0, br0, s0, _ = self.side(-2.3, 0.55, CRIMSON, "55%", 276, "before", LEFT)
        f1, b1, t1, br1, s1, k1 = self.side(2.3, 0.86, TEAL, "86%", 276, "after", RIGHT)

        self.play(Create(f0), FadeIn(t0), run_time=0.7); elapsed += 0.7
        self.play(FadeIn(b0, shift=DOWN * 0.1), run_time=0.6); elapsed += 0.6
        self.play(GrowFromCenter(br0), FadeIn(s0), run_time=0.7); elapsed += 0.7

        self.wait(0.6); elapsed += 0.6
        self.play(Create(f1), FadeIn(t1), run_time=0.7); elapsed += 0.7
        # The same content, spread down the frame — the rebuild moved anchors, not type size.
        self.play(TransformFromCopy(b0, b1), run_time=1.6); elapsed += 1.6
        self.play(GrowFromCenter(br1), FadeIn(s1[0]), FadeIn(s1[1]), run_time=0.7); elapsed += 0.7

        cue = 7.83  # "Bitrate rose…"
        if cue > elapsed:
            self.wait(cue - elapsed); elapsed = cue
        self.play(ChangingDecimal(k1, lambda a: 276 + (341 - 276) * a), run_time=1.6); elapsed += 1.6
        note = Text("same encoder settings", color=INK, font_size=30, slant="ITALIC").to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.6); elapsed += 0.6
        pad(self, elapsed, self.DUR)


class B08_WholeFrame(Scene):
    """OUTPUT, cycle 2 — center quarter → full frame once the coordinate frame is portrait.
    Illustration of the mechanism (REBUILD LAW); numbers are the sourced ones."""
    DUR = 12.71

    def construct(self):
        self.camera.background_color = CREAM
        handle(self)
        elapsed = 0.0

        frame = portrait_frame(6.8).move_to([-2.4, 0, 0])
        full = text_bars(frame.width * 0.84, 11, 0.24)
        full.stretch_to_fit_height(frame.height * 0.86).move_to(frame.get_center())
        small = full.copy().scale(0.5).move_to(frame.get_center())  # ≈ 25% of the area

        grid = VGroup(*[Line(frame.get_left() + UP * y, frame.get_right() + UP * y, color=RULE,
                             stroke_width=2) for y in np.linspace(-3.0, 3.0, 7)])

        self.play(Create(frame), run_time=0.7); elapsed += 0.7
        self.play(FadeIn(small), FadeIn(grid), run_time=0.7); elapsed += 0.7

        tag_x = 0.3  # left edge of the tag column; frame right edge is at -0.49
        audit = VGroup(checkmark(CRIMSON, 0.4),
                       Text("layout audit: PASS", font=MONO, color=CRIMSON, font_size=30))
        audit.arrange(RIGHT, buff=0.3).move_to([tag_x, 1.9, 0], aligned_edge=LEFT)
        quarter = Text("≈ the center quarter", color=CRIMSON, font_size=32,
                       weight="BOLD").next_to(audit, DOWN, buff=0.35, aligned_edge=LEFT)
        self.play(Create(audit[0]), FadeIn(audit[1]), run_time=0.6); elapsed += 0.6
        self.play(FadeIn(quarter, shift=UP * 0.1), run_time=0.5); elapsed += 0.5

        cfg_old = Text("frame_width = 14.222", font=MONO, color=SEC, font_size=32)
        cfg_new = Text("frame_width = 4.5", font=MONO, color=TEAL, font_size=32)
        cfg_old.next_to(quarter, DOWN, buff=0.8, aligned_edge=LEFT)
        cfg_new.move_to(cfg_old, aligned_edge=LEFT)
        self.play(FadeIn(cfg_old), run_time=0.4); elapsed += 0.4

        cue = 3.83  # "After, they span the full frame…"
        if cue > elapsed:
            self.wait(cue - elapsed); elapsed = cue
        grid_target = VGroup(*[Line(frame.get_left() + UP * y, frame.get_right() + UP * y, color=RULE,
                                    stroke_width=2) for y in np.linspace(-3.3, 3.3, 12)])
        self.play(Transform(cfg_old, cfg_new), Transform(grid, grid_target),
                  Transform(small, full), run_time=1.8); elapsed += 1.8

        gate_v = VGroup(checkmark(TEAL, 0.4),
                        Text("Gate V: PASS", font=MONO, color=TEAL, font_size=30))
        gate_v.arrange(RIGHT, buff=0.3).move_to(audit, aligned_edge=LEFT)
        full_lbl = Text("the full frame", color=TEAL, font_size=32, weight="BOLD").move_to(quarter,
                                                                                       aligned_edge=LEFT)
        self.play(Transform(audit, gate_v), Transform(quarter, full_lbl), run_time=0.9); elapsed += 0.9

        cue = 8.36  # "The audit was right about its own coordinates…"
        if cue > elapsed:
            self.wait(cue - elapsed); elapsed = cue
        moral = Text("right about its own coordinates,\nwrong about the video", color=INK,
                     font_size=30, slant="ITALIC", line_spacing=0.9).next_to(cfg_old, DOWN, buff=0.8,
                                                                        aligned_edge=LEFT)
        self.play(FadeIn(moral, shift=UP * 0.1), run_time=0.8); elapsed += 0.8
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
        cores, whats, whos = VGroup(), [], []
        for name, what, who in rows_spec:
            ck = checkmark(TEAL, 0.5)
            n = Text(name, color=INK, weight="BOLD", font_size=56)
            cores.add(VGroup(ck, n).arrange(RIGHT, buff=0.45))
            whats.append(Text(what, color=SEC, font_size=38))
            whos.append(Text(who, color=TEAL, font_size=34, weight="BOLD"))
        cores.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        cores.move_to([-5.8, 0.75, 0], aligned_edge=LEFT)
        desc_x = max(c.get_right()[0] for c in cores) + 0.6
        rows = VGroup()
        for c, w, o in zip(cores, whats, whos):
            y = c[1].get_center()[1]
            w.move_to([desc_x, y, 0], aligned_edge=LEFT)
            o.move_to([5.6, y, 0], aligned_edge=RIGHT)
            rows.add(VGroup(c[0], c[1], w, o))

        for r in rows:
            self.play(Create(r[0]), FadeIn(r[1]), FadeIn(r[2]), FadeIn(r[3]), run_time=0.6)
            self.wait(1.3); elapsed += 1.9

        rule = Line(LEFT * 5.6, RIGHT * 5.6, color=RULE, stroke_width=3).next_to(rows, DOWN, buff=0.5)
        closer = Text("Both bugs looked fine on paper.", color=INK, font_size=46,
                      slant="ITALIC").next_to(rule, DOWN, buff=0.4)
        self.play(GrowFromEdge(rule, LEFT), run_time=0.35); elapsed += 0.35
        self.play(Write(closer), run_time=1.3); elapsed += 1.3
        pad(self, elapsed, self.DUR)
