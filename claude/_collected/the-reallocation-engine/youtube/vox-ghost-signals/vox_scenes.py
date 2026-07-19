"""vox_scenes.py — The Ghost Job You Can't See: Five Signals That Read the Posting, Not the Prose
(vox-ghost-signals, slate cut, 16:9)

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat.
B02 is a STILL · ai beat and has no scene class here.

Color law:
  TEAL   = live posting / behavioral signals / real opening / active search
  CRIMSON= ghost posting / frozen / template / stale / dead
  GOLD   = fill highlight only, never text
  INK    = body text, neutral labels

Exclusions honored: no ATS vendor comparisons, no script internals,
false negatives in one sentence only (B10), no equations.

Gate B convention: every zero-width stroke is also zero-opacity.
"""
import sys
import json
import pathlib

# Resolve the shared graphics library wherever this reel lives.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene

_bs = pathlib.Path(__file__).with_name("beat_sheet.json")
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


def _chip(text, accent, size=22):
    return LabelChip(text, accent=accent, size=size)


# ================================================================ B01 Title

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The Ghost Job You Can't See", font=DISPLAY, color=INK, font_size=26, weight=BOLD)
        t2 = Text("Five Signals That Read the Posting", font=DISPLAY, color=CRIMSON, font_size=24, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ================================================================ B03 TheQuestion

class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        line1 = Text("Reading a posting should tell you whether it's real.",
                     font=SERIF, color=INK, font_size=25, weight=BOLD)
        line2 = Text("Here is the case where the most compelling posting is the ghost.",
                     font=SERIF, color=INK, font_size=23)
        line3 = Text("Why?", font=DISPLAY, color=CRIMSON, font_size=52, weight=BOLD)
        block = VGroup(line1, line2, line3).arrange(DOWN, buff=0.28).move_to(ORIGIN)
        hl = Rectangle(width=line3.width + 0.3, height=line3.height + 0.15)
        hl.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        hl.move_to(line3.get_center())
        self.play(FadeIn(line1), run_time=0.7)
        self.play(FadeIn(line2), run_time=0.7)
        self.play(FadeIn(hl), FadeIn(line3, scale=1.05), run_time=0.9)
        self.wait(max(0.3, total - 2.3))


# ================================================================ B04 GhostRate

class B04_GhostRate(Scene):
    def construct(self):
        total = DUR["B04"]
        # Shaded prevalence band: 28-42% of a population icon grid
        # Show as a horizontal band fill on a simple isotype-like bar
        heading = Text("Ghost-Job Prevalence", font=DISPLAY, color=INK,
                       font_size=24, weight=BOLD)
        heading.to_edge(UP, buff=0.6)

        # band label
        band_label = Text("28 - 42%", font=MONO, color=CRIMSON, font_size=42, weight=BOLD)
        band_label.move_to(ORIGIN + UP * 0.4)

        band_sub = Text("of all job postings are ghosts", font=SERIF, color=INK, font_size=26)
        band_sub.next_to(band_label, DOWN, buff=0.22)

        # "held 5 years" chip
        years_chip = _chip("held steady 5 years", CRIMSON, size=20)
        years_chip.next_to(band_sub, DOWN, buff=0.35)

        # structural note
        struct = SerifLabel("a structural feature, not a cycle artifact", INK, size=22)
        struct.next_to(years_chip, DOWN, buff=0.32)

        # Animate
        self.play(FadeIn(heading), run_time=0.5)
        self.play(FadeIn(band_label, scale=0.9), run_time=0.8)
        self.play(FadeIn(band_sub), run_time=0.6)
        self.play(FadeIn(years_chip, shift=UP * 0.2), run_time=0.6)
        self.play(FadeIn(struct, shift=UP * 0.15), run_time=0.6)
        self.wait(max(0.3, total - 2.5))


# ================================================================ B05 WhyGhosts

class B05_WhyGhosts(Scene):
    def construct(self):
        total = DUR["B05"]
        heading = Text("Why Ghost Postings Exist", font=DISPLAY, color=INK,
                       font_size=24, weight=BOLD)
        heading.to_edge(UP, buff=0.6)

        c1 = _chip("pipeline hedge", CRIMSON, size=22)
        c2 = _chip("investor signal", CRIMSON, size=22)
        c3 = _chip("bureaucratic inertia", CRIMSON, size=22)

        causes = VGroup(c1, c2, c3).arrange(DOWN, buff=0.38).move_to(LEFT * 2.5 + DOWN * 0.2)

        divider = Line(UP * 2.0, DOWN * 2.0, color=INK, stroke_width=1.2)
        divider.move_to(ORIGIN)

        note = Text("the description reads perfectly real", font=SERIF, color=INK,
                    font_size=21, slant=ITALIC)
        note.move_to(RIGHT * 3.8 + DOWN * 0.2)
        u_note = Line(note.get_corner(DL) + DOWN * 0.08,
                      note.get_corner(DR) + DOWN * 0.08,
                      color=CRIMSON, stroke_width=1.4)

        self.play(FadeIn(heading), run_time=0.5)
        self.play(FadeIn(causes), Create(divider), run_time=0.9)
        self.play(FadeIn(note), Create(u_note), run_time=0.7)
        self.wait(max(0.3, total - 2.1))


# ================================================================ B06 SpamParallel

class B06_SpamParallel(Scene):
    def construct(self):
        total = DUR["B06"]
        # two-column setup: SPAM FILTER | GHOST DETECTOR
        col_l = LEFT * 3.2
        col_r = RIGHT * 3.2

        heading = Text("The Same Move", font=DISPLAY, color=INK, font_size=24, weight=BOLD)
        heading.to_edge(UP, buff=0.5)

        spam_chip = _chip("spam filter", SLATE, size=22)
        spam_chip.move_to(col_l + UP * 1.4)

        ghost_chip = _chip("ghost detector", CRIMSON, size=22)
        ghost_chip.move_to(col_r + UP * 1.4)

        divider = Line(UP * 1.8, DOWN * 1.5, color=INK, stroke_width=1.2)
        divider.move_to(ORIGIN)

        spam_line = Text("does not read the message", font=SERIF, color=INK, font_size=21)
        spam_line.move_to(col_l + DOWN * 0.1)

        ghost_line = Text("does not read the prose", font=SERIF, color=INK, font_size=21)
        ghost_line.move_to(col_r + DOWN * 0.1)

        spam_act = SerifLabel("scores behavioral fingerprints", SLATE, size=20)
        spam_act.move_to(col_l + DOWN * 1.0)

        ghost_act = SerifLabel("scores behavioral fingerprints", CRIMSON, size=20)
        ghost_act.move_to(col_r + DOWN * 1.0)

        eq_label = SerifLabel("same move", INK, size=22)
        eq_label.move_to(ORIGIN + DOWN * 2.6)

        self.play(FadeIn(heading), run_time=0.5)
        self.play(FadeIn(spam_chip), FadeIn(ghost_chip), Create(divider), run_time=0.8)
        self.play(FadeIn(spam_line), FadeIn(ghost_line), run_time=0.7)
        self.play(FadeIn(spam_act), FadeIn(ghost_act), run_time=0.7)
        self.play(FadeIn(eq_label, shift=UP * 0.15), run_time=0.5)
        self.wait(max(0.3, total - 2.7))


# ================================================================ B07 ThreeFingerprints

class B07_ThreeFingerprints(Scene):
    def construct(self):
        total = DUR["B07"]
        heading = Text("Three Behavioral Fingerprints", font=DISPLAY, color=INK,
                       font_size=24, weight=BOLD)
        heading.to_edge(UP, buff=0.5)

        # three columns
        labels = ["TEMPORAL\nANOMALY", "INTERACTION\nVOID", "TEXTUAL\nHOMOGENEITY"]
        descs = [
            "posting frozen in time\nnever refreshed",
            "no portal activity\nno candidate movement",
            "description is a copy\nreused across listings",
        ]
        positions = [LEFT * 4.1, ORIGIN, RIGHT * 4.1]

        col_groups = VGroup()
        for label, desc, pos in zip(labels, descs, positions):
            chip = _chip(label, CRIMSON, size=19)
            chip.move_to(pos + UP * 0.8)
            d = Text(desc, font=SERIF, color=INK, font_size=20, line_spacing=0.9)
            d.next_to(chip, DOWN, buff=0.35)
            col_groups.add(VGroup(chip, d))

        # vertical dividers
        div1 = Line(UP * 1.5, DOWN * 2.0, color=INK, stroke_width=0.8)
        div1.move_to(LEFT * 2.1)
        div2 = Line(UP * 1.5, DOWN * 2.0, color=INK, stroke_width=0.8)
        div2.move_to(RIGHT * 2.1)

        self.play(FadeIn(heading), run_time=0.5)
        self.play(Create(div1), Create(div2), run_time=0.5)
        for cg in col_groups:
            self.play(FadeIn(cg, shift=UP * 0.2), run_time=0.7)
        self.wait(max(0.3, total - 2.6))


# ================================================================ B08 FiveSignals

class B08_FiveSignals(Scene):
    def construct(self):
        total = DUR["B08"]
        heading = Text("Five Signals", font=DISPLAY, color=INK,
                       font_size=24, weight=BOLD)
        heading.to_edge(UP, buff=0.5)

        signals = [
            ("1  posting age", "prior — weak alone"),
            ("2  last updated", "frozen vs refreshed"),
            ("3  sibling activity", "most diagnostic"),
            ("4  description specificity", "named project vs template"),
            ("5  active search context", "funding + hiring trajectory"),
        ]

        rows = VGroup()
        for num_label, note in signals:
            nl = Text(num_label, font=DISPLAY, color=TEAL, font_size=22, weight=BOLD)
            nt = Text(note, font=SERIF, color=INK, font_size=20, slant=ITALIC)
            row = VGroup(nl, nt).arrange(RIGHT, buff=0.5)
            rows.add(row)

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        rows.move_to(DOWN * 0.3)

        # pin rows left
        for r in rows:
            r.move_to(r.get_center() + LEFT * (r.get_left()[0] + 5.8) * 0)
        rows.to_edge(LEFT, buff=0.9)

        bottom_label = SerifLabel("classify behavior, not prose", TEAL, size=22)
        bottom_label.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(heading), run_time=0.5)
        for i, row in enumerate(rows):
            self.play(FadeIn(row, shift=RIGHT * 0.25), run_time=0.5)
        self.play(FadeIn(bottom_label, shift=UP * 0.15), run_time=0.6)
        self.wait(max(0.3, total - 3.1))


# ================================================================ B09 Classifier

class B09_Classifier(Scene):
    def construct(self):
        total = DUR["B09"]
        heading = Text("Five Signals, One Classification", font=DISPLAY, color=INK,
                       font_size=23, weight=BOLD)
        heading.to_edge(UP, buff=0.5)

        # input box
        input_box = Rectangle(width=3.2, height=1.2)
        input_box.set_fill(SLATE, 0.15).set_stroke(SLATE, 1.4)
        input_box.move_to(LEFT * 3.5 + UP * 0.2)
        input_label = Text("five signals", font=DISPLAY, color=SLATE,
                           font_size=22, weight=BOLD)
        input_label.move_to(input_box)

        # arrow
        arrow = Arrow(input_box.get_right(), input_box.get_right() + RIGHT * 1.4,
                      color=INK, stroke_width=2.5, max_tip_length_to_length_ratio=0.2)

        # classifier box — use LabelChip so white text has a tracked accent box
        clf_chip = LabelChip("classifier", accent=SLATE, size=20)
        clf_chip.next_to(arrow, RIGHT, buff=0.15)

        # output arrows fan
        right_edge = clf_chip.get_right()
        outputs = [("LIVE", TEAL, UP * 1.2), ("GHOST", CRIMSON, ORIGIN), ("INVESTIGATE", SLATE, DOWN * 1.2)]
        out_groups = VGroup()
        for label_txt, color, direction in outputs:
            end_pt = right_edge + RIGHT * 2.0 + direction
            arr = Arrow(right_edge, end_pt, color=color,
                        stroke_width=2.0, max_tip_length_to_length_ratio=0.18)
            chip = _chip(label_txt, color, size=19)
            chip.next_to(arr, RIGHT, buff=0.15)
            out_groups.add(VGroup(arr, chip))

        all_objs = VGroup(input_box, input_label, arrow, clf_chip, out_groups)
        all_objs.move_to(DOWN * 0.3)

        self.play(FadeIn(heading), run_time=0.5)
        self.play(FadeIn(input_box), FadeIn(input_label), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(clf_chip), run_time=0.5)
        for og in out_groups:
            self.play(FadeIn(og, shift=RIGHT * 0.2), run_time=0.5)
        self.wait(max(0.3, total - 2.8))


# ================================================================ B10 TheImplication

class B10_TheImplication(Scene):
    def construct(self):
        total = DUR["B10"]

        t1 = Text("The description is the costume.", font=SERIF, color=CRIMSON,
                  font_size=28, weight=BOLD)
        t2 = Text("The metadata is the evidence.", font=SERIF, color=TEAL,
                  font_size=28, weight=BOLD)
        divider = Line(LEFT * 3.5, RIGHT * 3.5, color=INK, stroke_width=1.2)
        divider.move_to(ORIGIN)

        block = VGroup(t1, divider, t2).arrange(DOWN, buff=0.3).move_to(UP * 0.3)

        fn_label = SerifLabel("one miss: fresh harvest postings designed to look active", CRIMSON, size=19)
        fn_label.to_edge(DOWN, buff=0.55)

        # gold highlight on "metadata is the evidence"
        hl = Rectangle(width=t2.width + 0.25, height=t2.height + 0.12)
        hl.set_fill(GOLD, 0.45).set_stroke(width=0, opacity=0)
        hl.move_to(t2.get_center())

        self.play(FadeIn(t1, shift=DOWN * 0.15), run_time=0.7)
        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(hl), FadeIn(t2, shift=UP * 0.15), run_time=0.7)
        self.play(FadeIn(fn_label, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.4))


# ================================================================ B11 HelixBio

class B11_HelixBio(Scene):
    def construct(self):
        total = DUR["B11"]
        lx = LEFT * 3.2
        rx = RIGHT * 3.2
        panel_w, panel_h = 3.5, 4.6

        # left panel: Posting A (TEAL = live)
        lbox = Rectangle(width=panel_w, height=panel_h)
        lbox.set_fill(TEAL, 0.07).set_stroke(TEAL, 1.8)
        lbox.move_to(lx + UP * 0.05)
        la_chip = _chip("POSTING A", TEAL, size=22)
        la_chip.next_to(lbox, UP, buff=0.2)

        lrows_data = [
            ("age", "9 days", TEAL),
            ("updated", "refreshed twice", TEAL),
            ("siblings", "roles appearing/disappearing", TEAL),
            ("description", "names a specific project", TEAL),
        ]
        lrows = VGroup()
        for field, val, col in lrows_data:
            fl = Text(field + ":", font=SERIF, color=INK, font_size=18, slant=ITALIC)
            vl = Text(val, font=SERIF, color=col, font_size=18)
            row = VGroup(fl, vl).arrange(RIGHT, buff=0.18)
            lrows.add(row)
        lrows.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        lrows.move_to(lx + UP * 0.5)

        l_result = _chip("LIVE", TEAL, size=24)
        l_result.move_to(lx + DOWN * 1.7)

        # right panel: Posting B (CRIMSON = ghost)
        rbox = Rectangle(width=panel_w, height=panel_h)
        rbox.set_fill(CRIMSON, 0.07).set_stroke(CRIMSON, 1.8)
        rbox.move_to(rx + UP * 0.05)
        rb_chip = _chip("POSTING B", CRIMSON, size=22)
        rb_chip.next_to(rbox, UP, buff=0.2)

        rrows_data = [
            ("age", "11 weeks", CRIMSON),
            ("updated", "never refreshed", CRIMSON),
            ("siblings", "all frozen, same age", CRIMSON),
            ("description", "copied from 18 months ago", CRIMSON),
        ]
        rrows = VGroup()
        for field, val, col in rrows_data:
            fl = Text(field + ":", font=SERIF, color=INK, font_size=18, slant=ITALIC)
            vl = Text(val, font=SERIF, color=col, font_size=18)
            row = VGroup(fl, vl).arrange(RIGHT, buff=0.18)
            rrows.add(row)
        rrows.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        rrows.move_to(rx + UP * 0.5)

        r_result = _chip("GHOST", CRIMSON, size=24)
        r_result.move_to(rx + DOWN * 1.7)

        # heading
        heading = Text("Helix Bio  |  Senior Data Scientist  x2  (illustrative)",
                       font=SERIF, color=INK, font_size=18, slant=ITALIC)
        heading.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(lbox), FadeIn(la_chip), FadeIn(rbox), FadeIn(rb_chip),
                  run_time=0.8)
        self.play(FadeIn(lrows), FadeIn(rrows), run_time=1.0)
        self.play(FadeIn(l_result, scale=0.9), FadeIn(r_result, scale=0.9), run_time=0.7)
        self.play(FadeIn(heading), run_time=0.5)
        self.wait(max(0.3, total - 3.0))


# ================================================================ B12 Endcard

class B12_Endcard(Scene):
    def construct(self):
        total = DUR["B12"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The posting looked real.", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("The signals said ghost.", font=DISPLAY, color=CRIMSON, font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=CRIMSON, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        sub = Text("from The Reallocation Engine", font=SERIF, color=INK, font_size=20)
        sub.next_to(u, DOWN, buff=0.4)
        self.play(FadeIn(eye), run_time=0.5)
        self.play(FadeIn(block), Create(u), run_time=1.0)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.0))
