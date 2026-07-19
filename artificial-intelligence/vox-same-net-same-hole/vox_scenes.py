"""vox_scenes.py — Why Two AIs Checking Each Other Is One Blind Spot Twice
(vox-same-net-same-hole, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. B02 is the only
STILL (ai media slot) and has no scene here. Durations read from this reel's
beat_sheet.json (actuals after audio lock; estimates as fallback).

Render everything (from books/):
  bash vox/scripts/vox_run.sh computational-skepticism-for-ai/youtube/vox-same-net-same-hole

Color law: teal #1F6F5C = the valid/independent check (the good thing that
stops the flaw); crimson #BF3339 = the flaw / correlated blind spot (the bad
grain). Gold = editor's pen, once (B05 quote highlight).

Card exclusions honored: no Godel formalism, no seven-tier taxonomy, no
chain-of-thought-monitoring literature, one spoken aside for aircraft/trials
(B08 only).

Gate B conventions: every zero-width stroke is also zero-opacity.
"""
import sys
import json
import pathlib

# Resolve the shared graphics library wherever this reel lives.
# parents[3] from this file goes up to books/; then into vox/aspects/.../manim.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403  (re-exports manim + vox components)
from vox_graphics import _quote_scene

DUR = {
    "B01": 9.0, "B03": 8.5, "B04": 8.5, "B05": 7.5,
    "B06": 9.5, "B07": 8.5, "B08": 8.5, "B09": 8.5,
    "B10": 8.5, "B11": 14.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update(
        {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
         for b in _BS["beats"]}
    )
except Exception:
    pass

# ----------------------------------------------------------------- constants

HOLE_HALF = 0.275    # half of the sieve's gap (hole) width
BAR_H = 0.37         # sieve bar height


# ----------------------------------------------------------------- helpers

def _sieve(cx, cy, bar_w=2.0, color=TEAL):
    """Two-bar sieve: left bar | hole | right bar, hole centered on cx."""
    sl = Rectangle(width=bar_w, height=BAR_H)
    sl.set_fill(color, 0.28).set_stroke(color, 2.5)
    sl.move_to([cx - HOLE_HALF - bar_w / 2, cy, 0])
    sr = Rectangle(width=bar_w, height=BAR_H)
    sr.set_fill(color, 0.28).set_stroke(color, 2.5)
    sr.move_to([cx + HOLE_HALF + bar_w / 2, cy, 0])
    return VGroup(sl, sr)


def _solid_bar(cx, cy, bar_w=2.0, color=TEAL):
    """A solid bar — no hole — represents a genuinely independent check."""
    b = Rectangle(width=bar_w * 2 + HOLE_HALF * 2, height=BAR_H)
    b.set_fill(color, 0.55).set_stroke(color, 2.5)
    b.move_to([cx, cy, 0])
    return b


def _grain(cx, cy):
    """The bad grain (crimson dot)."""
    d = Dot(radius=0.17)
    d.set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
    d.move_to([cx, cy, 0])
    return d


# ----------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM",
                   font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("Same Net,", font=DISPLAY, color=INK, font_size=58, weight=BOLD)
        t2 = Text("Same Hole.", font=DISPLAY, color=INK, font_size=58, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.1)
        u = Line(t2.get_corner(DL) + DOWN * 0.14, t2.get_corner(DR) + DOWN * 0.14,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.65)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_OneSieve(Scene):
    """Single sieve — one bad grain falls through the hole."""
    def construct(self):
        total = DUR["B03"]
        lbl = LabelChip("AI generator", accent=TEAL, size=24)
        lbl.move_to([0, 2.9, 0])
        sieve = _sieve(0, 0.2)
        grain = _grain(0, 2.2)
        flaw_lbl = SerifLabel("flaw slips through", CRIMSON, size=22)
        flaw_lbl.move_to([0, -1.5, 0])

        self.play(FadeIn(lbl), Create(sieve), run_time=0.9)
        self.play(grain.animate.move_to([0, 0.58, 0]), run_time=0.45)
        self.play(grain.animate.move_to([0, -1.1, 0]), run_time=0.65)
        self.play(FadeIn(flaw_lbl, shift=UP * 0.1), run_time=0.55)
        self.wait(max(0.5, total - 2.65))


class B04_TwoSieves(Scene):
    """Checker sieve slides in below the generator — the safety claim setup."""
    def construct(self):
        total = DUR["B04"]
        # Generator sieve (already in place)
        s1 = _sieve(0, 1.2)
        lbl1 = LabelChip("generator", accent=TEAL, size=22)
        lbl1.next_to(s1, UP, buff=0.2)

        # Checker sieve — built at final position then shifted offscreen
        s2 = _sieve(0, -1.1)
        lbl2 = LabelChip("checker", accent=TEAL, size=22)
        lbl2.next_to(s2, DOWN, buff=0.2)
        checker_grp = VGroup(s2, lbl2)
        checker_grp.shift(DOWN * 7.0)   # start below screen

        grain = _grain(0, 2.8)

        self.play(FadeIn(lbl1), Create(s1), run_time=0.9)
        self.play(grain.animate.move_to([0, 1.8, 0]), run_time=0.4)
        self.play(checker_grp.animate.shift(UP * 7.0), run_time=1.0)
        self.play(grain.animate.move_to([0, 1.56, 0]), run_time=0.3)
        self.wait(max(0.5, total - 2.6))


class B05_QuoteFoundry(Scene):
    """Quote card — the common cause problem."""
    def construct(self):
        _quote_scene(
            self,
            "What fools the generator is most likely to fool the checker.",
            "— the common cause problem",
            None,
            "fool",
            DUR["B05"],
        )


class B06_SameHole(Scene):
    """THE COMPARE MOVE: holes line up, grain falls through both sieves."""
    def construct(self):
        total = DUR["B06"]
        s1 = _sieve(0, 1.1)
        s2 = _sieve(0, -0.5)
        lbl1 = LabelChip("generator", accent=TEAL, size=22)
        lbl1.next_to(s1, LEFT, buff=0.38)
        lbl2 = LabelChip("checker", accent=TEAL, size=22)
        lbl2.next_to(s2, LEFT, buff=0.38)

        # Dashed alignment line through the shared hole position
        align = DashedLine([0, 2.0, 0], [0, -1.2, 0], color=CRIMSON, stroke_width=2.5)
        align_lbl = SerifLabel("same position", CRIMSON, size=20)
        align_lbl.move_to([2.0, 0.3, 0])

        grain = _grain(0, 2.5)

        self.play(FadeIn(lbl1), FadeIn(lbl2), Create(s1), Create(s2), run_time=1.0)
        self.play(Create(align), FadeIn(align_lbl), run_time=0.7)
        self.play(FadeIn(grain), run_time=0.2)
        self.play(grain.animate.move_to([0, 1.46, 0]), run_time=0.38)
        self.play(grain.animate.move_to([0, 0.74, 0]), run_time=0.33)
        self.play(grain.animate.move_to([0, -0.14, 0]), run_time=0.3)
        self.play(grain.animate.move_to([0, -0.86, 0]), run_time=0.33)
        self.play(grain.animate.move_to([0, -1.8, 0]), run_time=0.38)
        self.wait(max(0.5, total - 3.64))


class B07_SharedFoundation(Scene):
    """Same training data feeds both — correlated blind spots."""
    def construct(self):
        total = DUR["B07"]
        # Training data box at top
        data_rect = Rectangle(width=3.0, height=0.82)
        data_rect.set_fill(SLATE, 0.82).set_stroke(SLATE, 2.0)
        data_rect.move_to([0, 2.8, 0])
        data_lbl = Text("Training Data", font=SANS, color=WHITE, font_size=24)
        data_lbl.move_to(data_rect.get_center())

        # Generator box (left)
        gen_rect = Rectangle(width=2.3, height=0.82)
        gen_rect.set_fill(TEAL, 0.22).set_stroke(TEAL, 2.0)
        gen_rect.move_to([-3.0, 0.8, 0])
        gen_lbl = Text("Generator", font=SANS, color=INK, font_size=24)
        gen_lbl.move_to(gen_rect.get_center())

        # Checker box (right)
        chk_rect = Rectangle(width=2.3, height=0.82)
        chk_rect.set_fill(TEAL, 0.22).set_stroke(TEAL, 2.0)
        chk_rect.move_to([3.0, 0.8, 0])
        chk_lbl = Text("Checker", font=SANS, color=INK, font_size=24)
        chk_lbl.move_to(chk_rect.get_center())

        # Arrows from data box to each model
        arr1 = Arrow(data_rect.get_bottom() + LEFT * 0.5, gen_rect.get_top(),
                     color=SLATE, stroke_width=3, buff=0.1,
                     max_tip_length_to_length_ratio=0.15)
        arr2 = Arrow(data_rect.get_bottom() + RIGHT * 0.5, chk_rect.get_top(),
                     color=SLATE, stroke_width=3, buff=0.1,
                     max_tip_length_to_length_ratio=0.15)

        # Blind spot chip — placed below the data box, not overlapping box border
        bs = LabelChip("blind spot", accent=CRIMSON, size=20)
        bs.next_to(data_rect, DOWN, buff=0.28)

        # Correlated error labels below each model box
        err1 = SerifLabel("same error", CRIMSON, size=22).move_to([-3.0, -0.5, 0])
        err2 = SerifLabel("same error", CRIMSON, size=22).move_to([3.0, -0.5, 0])

        self.play(FadeIn(data_rect), FadeIn(data_lbl), run_time=0.7)
        self.play(Create(arr1), FadeIn(gen_rect), FadeIn(gen_lbl), run_time=0.6)
        self.play(Create(arr2), FadeIn(chk_rect), FadeIn(chk_lbl), run_time=0.6)
        self.play(FadeIn(bs, scale=0.9), run_time=0.5)
        self.play(FadeIn(err1, shift=UP * 0.1), FadeIn(err2, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.0))


class B08_Contrast(Scene):
    """COMPOSITE — same foundation (flaw through) vs independent check (flaw stopped)."""
    def construct(self):
        total = DUR["B08"]
        BAR_W = 1.6
        left_cx, right_cx = -3.3, 3.3

        # Divider
        div = Line([0, 3.2, 0], [0, -2.5, 0], color=INK, stroke_width=1.5)

        # Left panel: two aligned-hole sieves
        left_lbl = LabelChip("same foundation", accent=CRIMSON, size=19)
        left_lbl.move_to([left_cx, 2.6, 0])
        ls1 = _sieve(left_cx, 1.4, bar_w=BAR_W)
        ls2 = _sieve(left_cx, 0.1, bar_w=BAR_W)
        lgrain = _grain(left_cx, 2.2)

        # Right panel: one sieve + solid bar
        right_lbl = LabelChip("independent", accent=TEAL, size=19)
        right_lbl.move_to([right_cx, 2.6, 0])
        rs1 = _sieve(right_cx, 1.4, bar_w=BAR_W)
        rbar = _solid_bar(right_cx, 0.1, bar_w=BAR_W)
        rgrain = _grain(right_cx, 2.2)

        # Outcome labels — positioned well clear of sieve strokes
        l_outcome = SerifLabel("passes through", CRIMSON, size=20).move_to([left_cx, -1.0, 0])
        r_outcome = SerifLabel("stopped", TEAL, size=20).move_to([right_cx, -0.7, 0])

        self.play(FadeIn(left_lbl), FadeIn(right_lbl), Create(div), run_time=0.7)
        self.play(Create(ls1), Create(ls2), Create(rs1), FadeIn(rbar), run_time=0.9)
        # Both grains fall simultaneously
        self.play(lgrain.animate.move_to([left_cx, 1.76, 0]),
                  rgrain.animate.move_to([right_cx, 1.76, 0]), run_time=0.5)
        self.play(lgrain.animate.move_to([left_cx, 0.46, 0]),
                  rgrain.animate.move_to([right_cx, 0.46, 0]), run_time=0.45)
        # Left: falls through ls2 hole; right: stops at rbar
        self.play(lgrain.animate.move_to([left_cx, -0.8, 0]), run_time=0.4)
        self.play(FadeIn(l_outcome), FadeIn(r_outcome), run_time=0.5)
        self.wait(max(0.5, total - 3.45))


class B09_TwoOutcomes(Scene):
    """Two vertical tracks: redundant (grain through) vs independent (grain stopped)."""
    def construct(self):
        total = DUR["B09"]
        BAR_W = 1.6
        left_cx, right_cx = -3.2, 3.2

        # Divider
        div = Line([0, 3.2, 0], [0, -2.6, 0], color=INK, stroke_width=1.5)

        # Left: two aligned sieves (redundant)
        l_lbl = LabelChip("redundant", accent=CRIMSON, size=20).move_to([left_cx, 2.6, 0])
        la1 = _sieve(left_cx, 1.2, bar_w=BAR_W)
        la2 = _sieve(left_cx, -0.2, bar_w=BAR_W)
        lgrain = _grain(left_cx, 2.1)

        # Right: one sieve + solid bar (independent)
        r_lbl = LabelChip("independent", accent=TEAL, size=20).move_to([right_cx, 2.6, 0])
        ra1 = _sieve(right_cx, 1.2, bar_w=BAR_W)
        rbar = _solid_bar(right_cx, -0.2, bar_w=BAR_W)
        rgrain = _grain(right_cx, 2.1)

        # Outcome labels — clear of all strokes
        l_result = SerifLabel("slides through", CRIMSON, size=21).move_to([left_cx, -1.8, 0])
        r_result = SerifLabel("stops here", TEAL, size=21).move_to([right_cx, -1.0, 0])

        self.play(FadeIn(l_lbl), FadeIn(r_lbl), Create(div), run_time=0.6)
        self.play(Create(la1), Create(la2), Create(ra1), FadeIn(rbar), run_time=0.9)
        self.play(lgrain.animate.move_to([left_cx, 0.85, 0]),
                  rgrain.animate.move_to([right_cx, 0.85, 0]), run_time=0.5)
        self.play(lgrain.animate.move_to([left_cx, -0.55, 0]),
                  rgrain.animate.move_to([right_cx, 0.04, 0]), run_time=0.45)
        self.play(lgrain.animate.move_to([left_cx, -1.8, 0]), run_time=0.35)
        self.play(FadeIn(l_result), FadeIn(r_result), run_time=0.5)
        self.wait(max(0.5, total - 3.3))


class B10_Stack(Scene):
    """Three sieves with aligned holes stack up — grain falls through all."""
    def construct(self):
        total = DUR["B10"]
        s1 = _sieve(0, 1.6)
        s2 = _sieve(0, 0.5)
        s3 = _sieve(0, -0.6)
        lbl1 = LabelChip("checker 1", accent=TEAL, size=20).next_to(s1, LEFT, buff=0.3)
        lbl2 = LabelChip("checker 2", accent=TEAL, size=20).next_to(s2, LEFT, buff=0.3)
        lbl3 = LabelChip("checker 3", accent=TEAL, size=20).next_to(s3, LEFT, buff=0.3)

        grain = _grain(0, 3.0)

        coverage = SerifLabel("coverage: unchanged", CRIMSON, size=24)
        coverage.move_to([0, -2.0, 0])

        self.play(Create(s1), FadeIn(lbl1), run_time=0.65)
        self.play(Create(s2), FadeIn(lbl2), run_time=0.55)
        self.play(Create(s3), FadeIn(lbl3), run_time=0.55)
        # Grain falls through all three holes
        self.play(grain.animate.move_to([0, 1.96, 0]), run_time=0.28)
        self.play(grain.animate.move_to([0, 0.86, 0]), run_time=0.28)
        self.play(grain.animate.move_to([0, -0.24, 0]), run_time=0.28)
        self.play(grain.animate.move_to([0, -1.3, 0]), run_time=0.32)
        self.play(FadeIn(coverage, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 3.51))


class B11_ExampleSameNet(Scene):
    """THE EXAMPLE — content moderation: generator+checker same corpus, new pattern missed by both."""
    def construct(self):
        total = DUR["B11"]
        title = Text("Content Moderation — same training corpus", font=DISPLAY, font_size=19, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("Independent check", font=DISPLAY, font_size=16, color=TEAL).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("Same foundation", font=DISPLAY, font_size=16, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.55)

        val_l1 = Text("Checker: different corpus", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + UP * 0.65)
        val_l2 = Text("Different architecture", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.05)
        val_l3 = Text("New pattern: CAUGHT ✓", font=MONO, font_size=13, color=TEAL).move_to(LEFT * 3.2 + DOWN * 0.75)

        val_r1 = Text("Generator: 2021 corpus", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 0.65)
        val_r2 = Text("Checker: same 2021 corpus", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.05)
        val_r3 = Text("New pattern: MISSED ✗", font=MONO, font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + DOWN * 0.75)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)
        note_txt = Text("shared blind spot in training → second model adds nothing (illustrative)",
                        font=MONO, font_size=11, color=CRIMSON).move_to(DOWN * 2.55)

        self.play(Write(title), run_time=0.5)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.6)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(val_l1), Write(val_r1), run_time=0.4)
        self.play(Write(val_l2), Write(val_r2), run_time=0.4)
        self.play(Write(val_l3), Write(val_r3), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.4)
        self.play(Write(note_txt), run_time=0.4)
        self.wait(max(0.5, total - 4.6))
