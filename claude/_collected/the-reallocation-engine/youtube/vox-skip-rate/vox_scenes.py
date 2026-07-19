"""vox_scenes.py — Reading the Skip Rate: Why a Low Skip Rate Means the Filter Is Failing
(vox-skip-rate, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE beat whose source is 'own'.
No STILL ai beats in this reel.

Color law:
  TEAL   = healthy skip rate / filter working / targeted discipline
  CRIMSON= low skip rate / filter failing / spray-and-pray rebuilt
  GOLD   = fill highlight only, never text
  INK    = body text, neutral labels

Exclusions honored:
  - no per-tier response rate analysis
  - no tracker recipe or analyze-patterns.py implementation
  - no privacy rules around tracker files

Gate B convention: every zero-width stroke is also zero-opacity.
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

_bs = str(pathlib.Path(__file__).with_name("beat_sheet.json"))
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _bar(width, height, color, alpha=1.0):
    r = Rectangle(width=width, height=height)
    r.set_fill(color, alpha).set_stroke(width=0, opacity=0)
    return r


def _section_chip(text, accent, size=22):
    return LabelChip(text, accent=accent, size=size)


# ================================================================ B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("Reading the Skip Rate", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("Why Low Means the Filter Is Failing", font=DISPLAY, color=CRIMSON, font_size=24, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ================================================================ B02 WeeklyTracker

class B02_WeeklyTracker(Scene):
    def construct(self):
        total = DUR["B02"]
        baseline = DOWN * 1.6
        bar_total_w = 9.0
        bar_h = 1.1

        # full bar background (total 30 roles)
        bg = Rectangle(width=bar_total_w, height=bar_h)
        bg.set_fill(SLATE, 0.12).set_stroke(SLATE, 1.0)
        bg.move_to(baseline)

        # applied segment (24/30 = 0.8 of width) — CRIMSON (low skip = bad)
        apply_w = bar_total_w * 0.80
        skip_w  = bar_total_w * 0.20

        apply_bar = Rectangle(width=apply_w, height=bar_h)
        apply_bar.set_fill(CRIMSON, 0.75).set_stroke(width=0, opacity=0)
        apply_bar.move_to(baseline + LEFT * (bar_total_w / 2 - apply_w / 2))

        skip_bar = Rectangle(width=skip_w, height=bar_h)
        skip_bar.set_fill(TEAL, 0.75).set_stroke(width=0, opacity=0)
        skip_bar.move_to(baseline + RIGHT * (bar_total_w / 2 - skip_w / 2))

        # labels above segments
        apply_label = LabelChip("24 applied", accent=CRIMSON, size=20)
        apply_label.next_to(apply_bar, UP, buff=0.28)
        skip_label = LabelChip("6 skipped", accent=TEAL, size=20)
        skip_label.next_to(skip_bar, UP, buff=0.28)

        # "30 roles evaluated" header
        header = Text("30 roles evaluated", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        header.next_to(bg, UP, buff=0.65)

        # skip rate readout
        skip_rate = Text("Skip rate: 20%", font=MONO, color=CRIMSON, font_size=30, weight=BOLD)
        skip_rate.next_to(bg, DOWN, buff=0.38)

        ai_verdict = SerifLabel("AI read: highly productive, covering lots of ground", INK, size=20)
        ai_verdict.next_to(skip_rate, DOWN, buff=0.28)

        self.play(FadeIn(header), FadeIn(bg), run_time=0.7)
        self.play(FadeIn(apply_bar, shift=RIGHT * 0.15), FadeIn(apply_label), run_time=0.7)
        self.play(FadeIn(skip_bar, shift=LEFT * 0.15), FadeIn(skip_label), run_time=0.6)
        self.play(FadeIn(skip_rate), run_time=0.5)
        self.play(FadeIn(ai_verdict), run_time=0.6)
        self.wait(max(0.3, total - 3.1))


# ================================================================ B03 TheQuestion

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        line1 = Text("Applying to more roles should mean more progress.",
                     font=SERIF, color=INK, font_size=25, weight=BOLD)
        line2 = Text("Here is the case where an 80% apply rate",
                     font=SERIF, color=INK, font_size=25)
        line3 = Text("is evidence the engine has failed.", font=SERIF, color=CRIMSON, font_size=25)
        line4 = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=52, weight=BOLD)

        block = VGroup(line1, line2, line3).arrange(DOWN, buff=0.22)
        block.move_to(UP * 0.55)
        line4.next_to(block, DOWN, buff=0.44)

        hl = Rectangle(width=line4.width + 0.4, height=line4.height + 0.18)
        hl.set_fill(GOLD, 0.5).set_stroke(width=0, opacity=0)
        hl.move_to(line4.get_center())

        self.play(FadeIn(line1), run_time=0.7)
        self.play(FadeIn(line2), FadeIn(line3), run_time=0.7)
        self.play(FadeIn(hl), FadeIn(line4, scale=1.06), run_time=0.9)
        self.wait(max(0.3, total - 2.3))


# ================================================================ B04 TheDial

class B04_TheDial(Scene):
    def construct(self):
        total = DUR["B04"]

        # Title
        title = Text("The Skip Rate", font=DISPLAY, color=INK, font_size=28, weight=BOLD)
        title.move_to(UP * 3.0)

        # Build a simple horizontal dial bar
        dial_w = 8.5
        dial_h = 0.55
        dial_bg = Rectangle(width=dial_w, height=dial_h)
        dial_bg.set_fill(SLATE, 0.18).set_stroke(SLATE, 1.2)
        dial_bg.move_to(ORIGIN + DOWN * 0.3)

        # target line at 50%
        target_x = dial_bg.get_left()[0] + dial_w * 0.50
        target_line = Line(
            [target_x, dial_bg.get_top()[1] + 0.15, 0],
            [target_x, dial_bg.get_bottom()[1] - 0.15, 0],
            color=TEAL, stroke_width=3
        )
        target_label = Text("50% target", font=DISPLAY, color=TEAL, font_size=18)
        target_label.next_to(target_line, UP, buff=0.22)

        # Pointer at 20% (CRIMSON zone)
        pointer_x = dial_bg.get_left()[0] + dial_w * 0.20
        pointer = Triangle(fill_opacity=1).set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        pointer.scale(0.25).rotate(PI)
        pointer.move_to([pointer_x, dial_bg.get_bottom()[1] - 0.38, 0])

        # Label below
        pct_label = Text("20%", font=MONO, color=CRIMSON, font_size=26, weight=BOLD)
        pct_label.move_to([pointer_x, dial_bg.get_bottom()[1] - 0.82, 0])

        # Sub-label
        sub = SerifLabel("The pipeline tracker reads the skip rate first.", INK, size=21)
        sub.next_to(dial_bg, DOWN, buff=1.1)

        target_chip = LabelChip("target: 50% or above", accent=TEAL, size=20)
        target_chip.next_to(sub, DOWN, buff=0.28)

        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(dial_bg), run_time=0.6)
        self.play(Create(target_line), FadeIn(target_label), run_time=0.7)
        self.play(FadeIn(pointer, shift=UP * 0.2), FadeIn(pct_label), run_time=0.6)
        self.play(FadeIn(sub), FadeIn(target_chip), run_time=0.6)
        self.wait(max(0.3, total - 3.0))


# ================================================================ B05 DialBands

class B05_DialBands(Scene):
    def construct(self):
        total = DUR["B05"]

        title = Text("The Four Decision Bands", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        title.move_to(UP * 3.2)

        # Horizontal band bar
        dial_w = 9.0
        dial_h = 0.9
        dial_cy = UP * 0.4

        # Four band segments: 0-40%, 40-50%, 50-85%, 85-100%
        seg_widths = [dial_w * 0.40, dial_w * 0.10, dial_w * 0.35, dial_w * 0.15]
        seg_colors = [CRIMSON, "#8B6E44", TEAL, SLATE]
        seg_alphas = [0.65, 0.45, 0.65, 0.35]
        seg_labels = ["below 40%", "40-50%", "50-85%", "above 85%"]
        seg_descs  = ["filter failing", "borderline", "healthy", "starved"]
        seg_desc_colors = [CRIMSON, INK, TEAL, SLATE]

        lx = -dial_w / 2
        segs = []
        chips = []
        descs_text = []
        x_cursor = lx
        for i, (sw, sc, sa, sl, sd, sdc) in enumerate(
                zip(seg_widths, seg_colors, seg_alphas, seg_labels, seg_descs, seg_desc_colors)):
            seg = Rectangle(width=sw, height=dial_h)
            seg.set_fill(sc, sa).set_stroke(width=0, opacity=0)
            seg.move_to(dial_cy + RIGHT * (x_cursor + sw / 2))
            segs.append(seg)

            chip = LabelChip(sl, accent=sdc, size=16)
            chip.next_to(seg, UP, buff=0.2)
            chips.append(chip)

            desc = SerifLabel(sd, sdc, size=18)
            desc.next_to(seg, DOWN, buff=0.28)
            descs_text.append(desc)

            x_cursor += sw

        # Pointer at 20% = far left zone
        ptr_x = -dial_w / 2 + dial_w * 0.20
        pointer = Triangle(fill_opacity=1).set_fill(CRIMSON, 1).set_stroke(width=0, opacity=0)
        pointer.scale(0.22).rotate(PI)
        pointer.move_to([ptr_x, dial_cy[1] - dial_h / 2 - 0.32, 0])

        # Target line at 50%
        tgt_x = -dial_w / 2 + dial_w * 0.50
        tgt_line = Line(
            [tgt_x, dial_cy[1] + dial_h / 2 + 0.12, 0],
            [tgt_x, dial_cy[1] - dial_h / 2 - 0.12, 0],
            color=TEAL, stroke_width=2.5
        )
        tgt_lbl = Text("50%", font=MONO, color=TEAL, font_size=18)
        tgt_lbl.next_to(tgt_line, UP, buff=0.1)

        self.play(FadeIn(title), run_time=0.5)
        # Animate segments one by one scanning left to right
        for i, (seg, chip, desc) in enumerate(zip(segs, chips, descs_text)):
            self.play(FadeIn(seg, shift=UP * 0.1), FadeIn(chip), FadeIn(desc), run_time=0.55)
        self.play(Create(tgt_line), FadeIn(tgt_lbl), run_time=0.5)
        self.play(FadeIn(pointer, shift=UP * 0.15), run_time=0.5)
        self.wait(max(0.3, total - (0.5 + 4 * 0.55 + 1.0)))


# ================================================================ B06 SkipIsAction

class B06_SkipIsAction(Scene):
    def construct(self):
        total = DUR["B06"]

        # Two columns: APPLY log and SKIP log
        col_w = 3.8
        col_h = 4.0
        lx = LEFT * 2.6
        rx = RIGHT * 2.6
        cy = DOWN * 0.15

        lbox = Rectangle(width=col_w, height=col_h)
        lbox.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.5)
        lbox.move_to(lx + cy)

        rbox = Rectangle(width=col_w, height=col_h)
        rbox.set_fill(TEAL, 0.08).set_stroke(TEAL, 1.5)
        rbox.move_to(rx + cy)

        l_chip = LabelChip("apply", accent=CRIMSON, size=22)
        l_chip.next_to(lbox, UP, buff=0.22)
        r_chip = LabelChip("skip", accent=TEAL, size=22)
        r_chip.next_to(rbox, UP, buff=0.22)

        # Apply log entries (inside left box)
        apply_items = VGroup(*[
            SerifLabel(f"Role {chr(65+i)}", CRIMSON, size=18)
            for i in range(5)
        ]).arrange(DOWN, buff=0.36).move_to(lx + cy)

        # Skip log entries (inside right box)
        skip_items = VGroup(*[
            SerifLabel(f"Role {chr(70+i)}", TEAL, size=18)
            for i in range(4)
        ]).arrange(DOWN, buff=0.36).move_to(rx + cy)

        # Bottom label
        label = Text("Skip = decision. Not absence.", font=DISPLAY, color=TEAL,
                     font_size=24, weight=BOLD)
        label.next_to(lbox, DOWN, buff=0.48)
        label.shift(RIGHT * 2.6 - lx)  # center between boxes

        # Actually center label properly
        label.move_to(DOWN * 2.9)

        self.play(FadeIn(lbox), FadeIn(l_chip), FadeIn(rbox), FadeIn(r_chip), run_time=0.7)
        # Build apply items one by one
        for item in apply_items:
            self.play(FadeIn(item, shift=RIGHT * 0.12), run_time=0.25)
        # Build skip items one by one
        for item in skip_items:
            self.play(FadeIn(item, shift=LEFT * 0.12), run_time=0.25)
        self.play(FadeIn(label, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.3, total - (0.7 + 5 * 0.25 + 4 * 0.25 + 0.6)))


# ================================================================ B07 FilterCollapse

class B07_FilterCollapse(Scene):
    def construct(self):
        total = DUR["B07"]

        lx = LEFT * 3.2
        rx = RIGHT * 3.2
        panel_w = 4.8
        panel_h = 4.5

        # Left panel: HEALTHY (high skip)
        lbox = Rectangle(width=panel_w, height=panel_h)
        lbox.set_fill(TEAL, 0.08).set_stroke(TEAL, 1.8)
        lbox.move_to(lx)

        l_chip = LabelChip("60% skip  healthy", accent=TEAL, size=20)
        l_chip.next_to(lbox, UP, buff=0.22)

        l_time = Rectangle(width=3.2, height=0.65)
        l_time.set_fill(TEAL, 0.55).set_stroke(width=0, opacity=0)
        l_time.move_to(lx + UP * 0.6)
        l_time_lbl = SerifLabel("2 hrs targeted", TEAL, size=18)
        l_time_lbl.next_to(l_time, DOWN, buff=0.2)

        l_skips = SerifLabel("18 of 30 roles skipped", TEAL, size=18)
        l_skips.move_to(lx + DOWN * 1.0)
        l_note = SerifLabel("filter doing real work", TEAL, size=18)
        l_note.move_to(lx + DOWN * 1.5)

        # Right panel: COLLAPSED (low skip)
        rbox = Rectangle(width=panel_w, height=panel_h)
        rbox.set_fill(CRIMSON, 0.08).set_stroke(CRIMSON, 1.8)
        rbox.move_to(rx)

        r_chip = LabelChip("20% skip  failing", accent=CRIMSON, size=20)
        r_chip.next_to(rbox, UP, buff=0.22)

        # Block that grows to show time expanding
        r_time_start = Rectangle(width=3.2, height=0.65)
        r_time_start.set_fill(CRIMSON, 0.55).set_stroke(width=0, opacity=0)
        r_time_start.move_to(rx + UP * 0.6)

        r_time_expand = Rectangle(width=4.2, height=0.65)
        r_time_expand.set_fill(CRIMSON, 0.55).set_stroke(width=0, opacity=0)
        r_time_expand.move_to(rx + UP * 0.6)

        r_time_lbl = SerifLabel("2 hrs... then 8 hrs", CRIMSON, size=18)
        r_time_lbl.next_to(r_time_expand, DOWN, buff=0.2)

        r_skips = SerifLabel("6 of 30 roles skipped", CRIMSON, size=18)
        r_skips.move_to(rx + DOWN * 1.0)
        r_note = SerifLabel("filter not filtering", CRIMSON, size=18)
        r_note.move_to(rx + DOWN * 1.5)

        self.play(FadeIn(lbox), FadeIn(l_chip), run_time=0.6)
        self.play(FadeIn(l_time), FadeIn(l_time_lbl), run_time=0.5)
        self.play(FadeIn(l_skips), FadeIn(l_note), run_time=0.5)

        self.play(FadeIn(rbox), FadeIn(r_chip), run_time=0.6)
        self.play(FadeIn(r_time_start), run_time=0.4)
        self.play(Transform(r_time_start, r_time_expand), FadeIn(r_time_lbl), run_time=0.8)
        self.play(FadeIn(r_skips), FadeIn(r_note), run_time=0.5)
        self.wait(max(0.3, total - 3.9))


# ================================================================ B08 VolumeInstinct

class B08_VolumeInstinct(Scene):
    def construct(self):
        total = DUR["B08"]
        baseline = DOWN * 1.8
        bar_w = 1.8
        max_h = 3.6

        # An apply counter rising - single CRIMSON bar growing
        bar = _bar(bar_w, 0.2, CRIMSON, alpha=0.85)
        bar.move_to(baseline + LEFT * 0.5)
        bar.align_to(baseline, DOWN)

        # final tall bar
        bar_final = _bar(bar_w, max_h * 0.85, CRIMSON, alpha=0.85)
        bar_final.move_to(baseline + LEFT * 0.5)
        bar_final.align_to(baseline, DOWN)

        bl = Line(LEFT * 5.0 + baseline, RIGHT * 5.0 + baseline,
                  color=INK, stroke_width=1.5)

        # label on top of bar
        count_label = Text("24 applied", font=MONO, color=CRIMSON, font_size=28, weight=BOLD)
        count_label.next_to(bar_final, UP, buff=0.2)

        chip = LabelChip("apply counter", accent=CRIMSON, size=22)
        chip.next_to(bar_final, DOWN, buff=0.22)

        # Annotation: counter going up is not progress
        ann1 = SerifLabel("counter going up", CRIMSON, size=22)
        ann2 = SerifLabel("is not progress", CRIMSON, size=22)
        anns = VGroup(ann1, ann2).arrange(DOWN, buff=0.22)
        anns.move_to(RIGHT * 3.5 + UP * 0.2)

        ring = HandRing(bar_final, color=CRIMSON)

        # Second label: busy and unfiltered
        bottom_label = SerifLabel("busy and unfiltered -- the state the engine exists to end", INK, size=20)
        bottom_label.to_edge(DOWN, buff=0.5)

        self.play(Create(bl), run_time=0.4)
        self.play(FadeIn(bar), run_time=0.3)
        self.play(Transform(bar, bar_final), FadeIn(count_label), FadeIn(chip), run_time=1.0)
        self.play(Create(ring), run_time=0.8)
        self.play(FadeIn(anns), run_time=0.6)
        self.play(FadeIn(bottom_label), run_time=0.5)
        self.wait(max(0.3, total - 3.6))


# ================================================================ B09 TwoWeeks

class B09_TwoWeeks(Scene):
    def construct(self):
        total = DUR["B09"]

        lx = LEFT * 3.2
        rx = RIGHT * 3.2
        panel_w = 4.6
        panel_h = 5.5

        # Header
        header = Text("Same candidate. Same engine.", font=DISPLAY, color=INK,
                      font_size=24, weight=BOLD)
        header.to_edge(UP, buff=0.5)

        # Week A — CRIMSON (20% skip)
        lbox = Rectangle(width=panel_w, height=panel_h)
        lbox.set_fill(CRIMSON, 0.07).set_stroke(CRIMSON, 1.8)
        lbox.move_to(lx + DOWN * 0.3)

        l_chip = LabelChip("Week A", accent=CRIMSON, size=24)
        l_chip.next_to(lbox, UP, buff=0.22)

        l_eval  = SerifLabel("30 evaluated", INK, size=20)
        l_skip  = SerifLabel("6 skipped  (20%)", CRIMSON, size=20)
        l_apply = SerifLabel("24 applied", CRIMSON, size=20)
        l_refs  = SerifLabel("0 referrals", CRIMSON, size=22)
        l_band  = LabelChip("filter failing band", accent=CRIMSON, size=18)
        l_illus = SerifLabel("illustrative", INK, size=16)

        l_content = VGroup(l_eval, l_skip, l_apply, l_refs, l_band, l_illus).arrange(DOWN, buff=0.28)
        l_content.move_to(lx + DOWN * 0.4)

        # Week B — TEAL (60% skip)
        rbox = Rectangle(width=panel_w, height=panel_h)
        rbox.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.8)
        rbox.move_to(rx + DOWN * 0.3)

        r_chip = LabelChip("Week B", accent=TEAL, size=24)
        r_chip.next_to(rbox, UP, buff=0.22)

        r_eval  = SerifLabel("30 evaluated", INK, size=20)
        r_skip  = SerifLabel("18 skipped  (60%)", TEAL, size=20)
        r_apply = SerifLabel("12 applied", TEAL, size=20)
        r_refs  = SerifLabel("2 referrals", TEAL, size=22)
        r_band  = LabelChip("healthy band", accent=TEAL, size=18)
        r_illus = SerifLabel("illustrative", INK, size=16)

        r_content = VGroup(r_eval, r_skip, r_apply, r_refs, r_band, r_illus).arrange(DOWN, buff=0.28)
        r_content.move_to(rx + DOWN * 0.4)

        self.play(FadeIn(header), run_time=0.5)
        self.play(FadeIn(lbox), FadeIn(l_chip), FadeIn(rbox), FadeIn(r_chip), run_time=0.7)
        self.play(FadeIn(l_content), run_time=0.9)
        self.play(FadeIn(r_content), run_time=0.9)
        self.wait(max(0.3, total - 3.0))


# ================================================================ B10 Endcard

class B10_Endcard(Scene):
    def construct(self):
        total = DUR["B10"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The low skip rate felt more productive.", font=DISPLAY, color=INK,
                  font_size=28, weight=BOLD)
        t2 = Text("The high skip rate was.", font=DISPLAY, color=TEAL, font_size=28, weight=BOLD)
        t3 = Text("Read the dial.", font=DISPLAY, color=CRIMSON, font_size=32, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.4)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        t3.next_to(block, DOWN, buff=0.42)
        sub = Text("from The Reallocation Engine", font=SERIF, color=INK, font_size=20)
        sub.next_to(t3, DOWN, buff=0.38)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.play(FadeIn(t3, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.5))
