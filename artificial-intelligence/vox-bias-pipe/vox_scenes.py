import sys, json, pathlib, numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 9.0, "B04": 8.5, "B05": 9.0, "B07": 9.5,
    "B08": 8.5, "B09": 9.0, "B10": 9.0, "B11": 8.5,
    "B12": 18.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _BS["beats"]
    })
except Exception:
    pass

# ── B01 — Title ───────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Why Fixing the Model", font=DISPLAY, color=INK, font_size=46, weight=BOLD)
        t2 = Text("Didn't Fix the Bias", font=DISPLAY, color=CRIMSON, font_size=46, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# Shared pipe-graph layout for B07-B10
_PX = [-2.8, 0.0, 2.8]       # pipe x-centers: MODEL, PROXY, REVIEW
_PW  = 0.9                    # pipe width
_PBT = -1.7                   # pipe bottom y
_PTT = 1.7                    # pipe top y
_PH  = _PTT - _PBT            # pipe height = 3.4
_PLBLS = ["MODEL", "PROXY", "REVIEW"]
_PFRAC  = [0.35, 0.25, 0.40]  # illustrative fraction of total bias flow per pipe (sums to 1)


def _make_pipe(i):
    outline = Rectangle(width=_PW, height=_PH, color=SLATE, fill_opacity=0.08)
    outline.set_stroke(color=SLATE, width=2)
    outline.move_to(np.array([_PX[i], (_PBT + _PTT) / 2, 0]))
    return outline


def _make_fill(i, frac=1.0, color=CRIMSON):
    h = _PH * frac
    fill = Rectangle(width=_PW * 0.85, height=h, color=color, fill_opacity=0.80)
    fill.set_stroke(width=0, opacity=0)
    fill.move_to(np.array([_PX[i], _PBT + h / 2, 0]))
    return fill


def _make_pipe_label(i, txt):
    return LabelChip(txt, accent=SLATE, size=20).move_to(np.array([_PX[i], _PTT + 0.45, 0]))


def _pipe_scene_base():
    src = Text("PROTECTED ATTRIBUTE", font=DISPLAY, color=INK).scale(0.42).move_to(UP * 2.65)
    out = Text("OUTCOME", font=DISPLAY, color=INK).scale(0.42).move_to(DOWN * 2.25)
    pipes = [_make_pipe(i) for i in range(3)]
    lbls  = [_make_pipe_label(i, _PLBLS[i]) for i in range(3)]
    return src, out, pipes, lbls


class B02_ThreeTeams(Scene):
    def construct(self):
        header = LabelChip("SAME DEPLOYMENT", accent=SLATE).move_to(UP * 2.7)
        rows = [
            ("TEAM 1", "rewrote loss function",    "disparity -8%",   CRIMSON),
            ("TEAM 2", "resampled training data",  "disparity -11%",  CRIMSON),
            ("TEAM 3", "changed review process",   "disparity -90%",  TEAL),
        ]
        groups = []
        for j, (team, action, result, col) in enumerate(rows):
            y = 0.9 - j * 1.5
            team_chip  = LabelChip(team,   accent=col, size=20).move_to(np.array([-4.2, y, 0]))
            action_txt = Text(action, font=MONO, color=INK).scale(0.38).move_to(np.array([-0.8, y, 0]))
            result_txt = Text(result, font=MONO, color=col).scale(0.44).move_to(np.array([3.5, y, 0]))
            groups.append((team_chip, action_txt, result_txt))
        div1 = Line(np.array([-6.0, 0.15, 0]), np.array([6.0, 0.15, 0]), color=SLATE, stroke_width=1)
        div2 = Line(np.array([-6.0, -1.35, 0]), np.array([6.0, -1.35, 0]), color=SLATE, stroke_width=1)
        self.play(FadeIn(header))
        self.play(Create(div1), Create(div2))
        for team_chip, action_txt, result_txt in groups:
            self.play(FadeIn(team_chip), FadeIn(action_txt), FadeIn(result_txt), run_time=0.6)
        self.wait(max(0.3, DUR["B02"] - 5.5))


class B04_NaiveExpect(Scene):
    def construct(self):
        naive_lbl = LabelChip("NAIVE EXPECTATION", accent=SLATE).move_to(UP * 2.6)
        # Simple chain: PROTECTED ATTR -> MODEL -> OUTCOME
        a_box = Rectangle(width=2.8, height=0.8, color=SLATE, fill_opacity=0.12)
        a_box.set_stroke(color=SLATE, width=2)
        a_box.move_to(LEFT * 3.5 + UP * 0.2)
        a_lbl = Text("PROTECTED\nATTRIBUTE", font=MONO, color=INK).scale(0.34).move_to(LEFT * 3.5 + UP * 0.2)
        arr1 = Line(np.array([-2.1, 0.2, 0]), np.array([-0.9, 0.2, 0]),
                    color=CRIMSON, stroke_width=3)
        m_box = Rectangle(width=1.6, height=0.8, color=CRIMSON, fill_opacity=0.12)
        m_box.set_stroke(color=CRIMSON, width=2)
        m_box.move_to(ORIGIN + UP * 0.2)
        m_lbl = Text("MODEL", font=MONO, color=CRIMSON).scale(0.38).move_to(ORIGIN + UP * 0.2)
        arr2 = Line(np.array([0.8, 0.2, 0]), np.array([2.2, 0.2, 0]),
                    color=CRIMSON, stroke_width=3)
        o_box = Rectangle(width=2.2, height=0.8, color=SLATE, fill_opacity=0.12)
        o_box.set_stroke(color=SLATE, width=2)
        o_box.move_to(RIGHT * 3.2 + UP * 0.2)
        o_lbl = Text("BIASED\nOUTCOME", font=MONO, color=INK).scale(0.34).move_to(RIGHT * 3.2 + UP * 0.2)
        # Fix box overlay
        fix_box = Rectangle(width=2.0, height=1.1, color=TEAL, fill_opacity=0.2)
        fix_box.set_stroke(color=TEAL, width=2.5)
        fix_box.move_to(ORIGIN + UP * 0.2)
        fix_lbl = Text("FIX HERE", font=DISPLAY, color=TEAL).scale(0.45).move_to(ORIGIN + DOWN * 1.5)
        logic = Text("bias in model -> fix model -> fix bias", font=MONO, color=SLATE).scale(0.38).move_to(DOWN * 2.5)
        self.play(FadeIn(naive_lbl))
        self.play(GrowFromCenter(a_box), FadeIn(a_lbl))
        self.play(Create(arr1))
        self.play(GrowFromCenter(m_box), FadeIn(m_lbl))
        self.play(Create(arr2))
        self.play(GrowFromCenter(o_box), FadeIn(o_lbl))
        self.play(GrowFromCenter(fix_box), FadeIn(fix_lbl))
        self.play(FadeIn(logic))
        self.wait(max(0.3, DUR["B04"] - 8.0))


class B05_ThreePaths(Scene):
    def construct(self):
        src_lbl = Text("PROTECTED ATTRIBUTE", font=DISPLAY, color=INK).scale(0.42).move_to(UP * 2.7)
        out_lbl = Text("OUTCOME", font=DISPLAY, color=INK).scale(0.42).move_to(DOWN * 2.5)
        # Three converging arrows from top to bottom
        tops = [(-2.8, 2.2), (0.0, 2.2), (2.8, 2.2)]
        bots = [(-2.8, -2.0), (0.0, -2.0), (2.8, -2.0)]
        colors = [CRIMSON, CRIMSON, CRIMSON]
        path_lbls = ["MODEL PATH", "PROXY PATH", "REVIEW PATH"]
        arrows = []
        lbls = []
        for (tx, ty), (bx, by), col, plbl in zip(tops, bots, colors, path_lbls):
            arr = Line(np.array([tx, ty, 0]), np.array([bx, by, 0]),
                       color=col, stroke_width=5)
            arrows.append(arr)
            lbl = LabelChip(plbl, accent=col, size=18).move_to(np.array([tx, ty + 0.38, 0]))
            lbls.append(lbl)
        note = Text("three parallel paths, three separate leverage points", font=MONO, color=SLATE).scale(0.36).move_to(DOWN * 3.1)
        self.play(FadeIn(src_lbl), FadeIn(out_lbl))
        self.play(FadeIn(lbls[0]), FadeIn(lbls[1]), FadeIn(lbls[2]))
        for a in arrows:
            self.play(Create(a), run_time=0.7)
        self.play(FadeIn(note))
        self.wait(max(0.3, DUR["B05"] - 5.5))


class B07_PipeGraph(Scene):
    def construct(self):
        src, out, pipes, lbls = _pipe_scene_base()
        fills = [_make_fill(i) for i in range(3)]
        flow_lbl = SerifLabel("bias flowing", accent=CRIMSON, size=24).move_to(np.array([4.5, 0.0, 0]))
        self.play(FadeIn(src), FadeIn(out))
        self.play(FadeIn(lbls[0]), FadeIn(lbls[1]), FadeIn(lbls[2]))
        for p in pipes:
            self.play(Create(p), run_time=0.5)
        for f in fills:
            self.play(GrowFromEdge(f, DOWN), run_time=0.7)
        self.play(FadeIn(flow_lbl))
        self.wait(max(0.3, DUR["B07"] - 7.5))


class B08_QuoteModelPath(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Most algorithmic interventions block one path — the one running through "
            "the model's parameters — and leave the proxy paths and the deployment-context "
            "paths fully open.",
            "Computational Skepticism for AI, Chapter 6",
            None,
            "fully open",
            DUR["B08"],
        )


class B09_ModelBlock(Scene):
    def construct(self):
        src, out, pipes, lbls = _pipe_scene_base()
        fills = [_make_fill(i) for i in range(3)]
        self.add(src, out, *pipes, *lbls, *fills)
        # Block bar over MODEL pipe (index 0)
        block = Rectangle(width=_PW * 1.2, height=0.22, color=WHITE, fill_opacity=1.0)
        block.set_stroke(color=SLATE, width=2.5)
        block.move_to(np.array([_PX[0], 0.0, 0]))
        block_lbl = Text("BLOCKED", font=MONO, color=SLATE).scale(0.3).next_to(block, UP, buff=0.15)
        # Transform left fill to small residual
        small_fill = _make_fill(0, frac=0.08, color=CRIMSON)
        result_lbl = SerifLabel("flow reroutes", accent=CRIMSON, size=22).move_to(np.array([4.0, 0.0, 0]))
        self.play(GrowFromCenter(block), FadeIn(block_lbl))
        self.play(Transform(fills[0], small_fill))
        self.play(FadeIn(result_lbl))
        self.wait(max(0.3, DUR["B09"] - 5.0))


class B10_ReviewBlock(Scene):
    def construct(self):
        src, out, pipes, lbls = _pipe_scene_base()
        fills = [_make_fill(i) for i in range(3)]
        self.add(src, out, *pipes, *lbls, *fills)
        # Block bar over REVIEW pipe (index 2, right)
        block = Rectangle(width=_PW * 1.2, height=0.22, color=TEAL, fill_opacity=0.9)
        block.set_stroke(color=TEAL, width=2.5)
        block.move_to(np.array([_PX[2], 0.0, 0]))
        block_lbl = Text("HIGH LEVERAGE", font=MONO, color=TEAL).scale(0.3).next_to(block, UP, buff=0.15)
        # Transform right fill to tiny residual (most flow stops)
        tiny_fill = _make_fill(2, frac=0.06, color=CRIMSON)
        result_lbl = SerifLabel("disparity -90%", accent=TEAL, size=24).move_to(np.array([0.0, -3.2, 0]))
        self.play(GrowFromCenter(block), FadeIn(block_lbl))
        self.play(Transform(fills[2], tiny_fill))
        self.play(FadeIn(result_lbl))
        self.wait(max(0.3, DUR["B10"] - 5.0))


class B11_QuoteLeverage(Scene):
    def construct(self):
        _quote_scene(
            self,
            "You can intervene on what is in your house. But your intervention will be "
            "at the wrong leverage point, and the disparity will persist.",
            "Computational Skepticism for AI, Chapter 6",
            None,
            "leverage point",
            DUR["B11"],
        )


# ── B12 — ExampleLending (THE EXAMPLE) ────────────────────────────────────────

class B12_ExampleLending(Scene):
    def construct(self):
        total = DUR["B12"]

        title = Text("One Pipe Blocked — Two Still Open", font=DISPLAY, font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.2, height=3.6, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.0 + DOWN * 0.1)
        col_r = Rectangle(width=5.2, height=3.6, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.0 + DOWN * 0.1)

        lbl_l = Text("MODEL FIX", font=DISPLAY, font_size=18, color=TEAL).move_to(LEFT * 3.0 + UP * 1.5)
        lbl_r = Text("ZIP CODE PATH", font=DISPLAY, font_size=18, color=CRIMSON).move_to(RIGHT * 3.0 + UP * 1.5)

        gap_before = Text("gap: 22 pts", font="PT Mono", font_size=16, color=INK).move_to(LEFT * 3.0 + UP * 0.7)
        gap_after  = Text("gap in weights: 7 pts", font="PT Mono", font_size=16, color=TEAL).move_to(LEFT * 3.0 + DOWN * 0.1)
        result_l   = Text("MODEL PIPE: REDUCED", font=DISPLAY, font_size=15, color=TEAL).move_to(LEFT * 3.0 + DOWN * 0.9)

        zip_carry  = Text("carries: 18 pts", font="PT Mono", font_size=16, color=CRIMSON).move_to(RIGHT * 3.0 + UP * 0.4)
        zip_open   = Text("PATH: STILL OPEN", font=DISPLAY, font_size=15, color=CRIMSON).move_to(RIGHT * 3.0 + DOWN * 0.4)

        note = Text("Final approval gap: 20 pts. Model fix moved the flow.", font=DISPLAY, font_size=15, color=INK)
        note.move_to(DOWN * 2.5)
        note_rect = Rectangle(width=9.0, height=0.5, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.5)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.6)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(gap_before), run_time=0.3)
        self.play(Write(gap_after), Write(zip_carry), run_time=0.5)
        self.play(Write(result_l), Write(zip_open), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.3)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.5, total - 4.4))
