"""vox_scenes.py — The Resume That Disappeared: Why Your Best-Looking CV Scores Zero
(vox-resume-zero, slate cut, 16:9).

One Scene per GRAPHIC/CARD/COMPOSITE beat whose source is 'own'.
B01 and B09 are STILL (ai media slots) and have no scene here.
Durations read from this reel's beat_sheet.json (actuals after audio lock;
estimates as fallback).

Render everything (on a machine with manim + fonts):
  bash vox/scripts/vox_run.sh the-reallocation-engine/youtube/vox-resume-zero

Color law: TEAL = single-column / parseable / visible to the parser (the safe path);
CRIMSON = two-column / graphic / invisible to the parser (the broken path).
GOLD = the editor-pen highlight in B10 only, fill never text, once per film.
Card exclusions: NO ATS vendor comparisons; NO bullet-content discussion;
NO Playwright/Chromium details.
"""
import sys
import json
import os
import pathlib

# Resolve the shared graphics library wherever this reel lives.
# parents[3] from this file goes up to books/; then into vox/aspects/.../manim.
sys.path.insert(
    0,
    str(pathlib.Path(__file__).resolve().parents[3]
        / "vox/aspects/explainer/vox-explainer/manim")
)
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene  # noqa: F401

_bs = os.path.join(os.path.dirname(__file__), "beat_sheet.json")
try:
    _data = json.load(open(_bs))
    DUR = {b["beat_id"]: b.get("actual_duration_s", b.get("estimated_duration_s", 10.0))
           for b in _data["beats"]}
except Exception:
    DUR = {f"B{i:02d}": 10.0 for i in range(1, 14)}


# ---------------------------------------------------------------- helpers

def _row_bar(w=2.8, h=0.22, color=TEAL):
    r = Rectangle(width=w, height=h)
    r.set_fill(color, 1).set_stroke(width=0, opacity=0)
    return r


def _col_block(n, color, w=2.8, h=0.22, gap=0.12):
    g = VGroup(*[_row_bar(w, h, color) for _ in range(n)])
    g.arrange(DOWN, buff=gap)
    return g


def _panel(center, w, h, fill_opacity=0.25):
    p = Rectangle(width=w, height=h)
    p.set_fill(WHITE, fill_opacity).set_stroke("#C9C2B4", 1.5)
    p.move_to(center)
    return p


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE REALLOCATION ENGINE", font=DISPLAY, color=TEAL, font_size=16)
        t1 = Text("The Resume That Disappeared", font=DISPLAY, color=INK, font_size=28, weight=BOLD)
        t2 = Text("Why Your Best CV Scores Zero", font=DISPLAY, color=CRIMSON, font_size=26, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL)+DOWN*0.13, t2.get_corner(DR)+DOWN*0.13, color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


class B02_ScreeningStat(Scene):
    def construct(self):
        total = DUR["B02"]
        # Section card: screening stat
        stat = Text("82%", font=DISPLAY, color=SLATE, font_size=72, weight=BOLD)
        label = Text("of companies screen resumes", font=SERIF, color=INK, font_size=28)
        label2 = Text("with software first.", font=SERIF, color=INK, font_size=28)
        sub = SerifLabel("~1 in 5 applicants auto-rejected, no human review", CRIMSON, size=22)
        block = VGroup(stat, label, label2, sub).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        self.play(FadeIn(stat, scale=0.85), run_time=0.7)
        self.play(FadeIn(label), FadeIn(label2), run_time=0.8)
        self.play(FadeIn(sub, shift=UP*0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.1))


class B03_TheQuestion(Scene):
    def construct(self):
        total = DUR["B03"]
        q1 = Text("A polished resume should reach human reviewers.", font=SERIF, color=INK, font_size=28)
        q2 = Text("The most polished CV gets auto-rejected.", font=SERIF, color=CRIMSON, font_size=28, weight=BOLD)
        q3 = Text("Why?", font=DISPLAY, color=INK, font_size=44, weight=BOLD)
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.30).move_to(UP * 0.1)
        u = Line(q2.get_corner(DL)+DOWN*0.10, q2.get_corner(DR)+DOWN*0.10, color=CRIMSON, stroke_width=2)
        self.play(FadeIn(q1), run_time=0.7)
        self.play(FadeIn(q2), Create(u), run_time=0.9)
        self.play(FadeIn(q3, scale=0.9), run_time=0.6)
        self.wait(max(0.3, total - 2.2))


class B04_TwoForks(Scene):
    def construct(self):
        total = DUR["B04"]
        # Resume icon (simplified rectangle)
        resume = Rectangle(width=1.0, height=1.3)
        resume.set_fill(WHITE, 0.9).set_stroke(INK, 2)
        resume.move_to(LEFT * 5.2)
        # Lines inside resume to suggest text
        for i in range(4):
            ln = Line(LEFT*0.35, RIGHT*0.35, stroke_width=1.5, color="#C9C2B4")
            ln.move_to(resume.get_center() + UP * (0.35 - i*0.20))
            resume.add(ln)
        resume_label = LabelChip("RESUME", accent=SLATE, size=18)
        resume_label.next_to(resume, DOWN, buff=0.18)

        # Fork node
        fork_dot = Dot(radius=0.12, color=INK)
        fork_dot.move_to(LEFT * 2.8)

        # Parser label
        parser_label = SerifLabel("parser reads first", INK, size=22)
        parser_label.next_to(fork_dot, UP, buff=0.28)

        # TEAL path: clean extraction -> human review -> interview
        teal_path_line = Line(LEFT*2.8, RIGHT*0.6 + UP*1.2, color=TEAL, stroke_width=3)
        teal_arrow = Arrow(RIGHT*0.6+UP*1.2, RIGHT*4.2+UP*1.2, color=TEAL,
                           stroke_width=3, buff=0.0, max_tip_length_to_length_ratio=0.15)
        teal_label = LabelChip("clean text extracted", accent=TEAL, size=20)
        teal_label.move_to(RIGHT*1.8 + UP*1.7)
        # human_label placed above the arrow endpoint, not on it
        human_label = LabelChip("human review", accent=TEAL, size=20)
        human_label.move_to(RIGHT*4.5 + UP*1.65)

        # CRIMSON path: noise -> auto-reject
        crimson_path_line = Line(LEFT*2.8, RIGHT*0.6 + DOWN*1.2, color=CRIMSON, stroke_width=3)
        crimson_arrow = Arrow(RIGHT*0.6+DOWN*1.2, RIGHT*4.2+DOWN*1.2, color=CRIMSON,
                              stroke_width=3, buff=0.0, max_tip_length_to_length_ratio=0.15)
        crimson_label = LabelChip("scrambled noise", accent=CRIMSON, size=20)
        crimson_label.move_to(RIGHT*1.8 + DOWN*1.7)
        # reject_label placed below the arrow endpoint, not on it
        reject_label = LabelChip("auto-reject", accent=CRIMSON, size=20)
        reject_label.move_to(RIGHT*4.5 + DOWN*1.65)

        # connector from resume to fork
        connect = Line(LEFT*4.7, LEFT*2.9, color=INK, stroke_width=2.5)

        self.play(FadeIn(resume), FadeIn(resume_label), run_time=0.7)
        self.play(Create(connect), FadeIn(fork_dot), FadeIn(parser_label), run_time=0.8)
        self.play(Create(teal_path_line), Create(crimson_path_line), run_time=0.7)
        self.play(FadeIn(teal_label), FadeIn(crimson_label), run_time=0.6)
        self.play(GrowArrow(teal_arrow), GrowArrow(crimson_arrow), run_time=0.7)
        self.play(FadeIn(human_label), FadeIn(reject_label), run_time=0.6)
        self.wait(max(0.3, total - 4.1))


class B05_ColumnInterleave(Scene):
    def construct(self):
        total = DUR["B05"]

        # Two-column resume layout
        left_panel = _panel(LEFT*3.0 + UP*0.3, 2.5, 3.2)
        right_panel = _panel(RIGHT*0.4 + UP*0.3, 2.5, 3.2)

        # Column headers
        left_head = LabelChip("LEFT COLUMN", accent=SLATE, size=18)
        left_head.next_to(left_panel, UP, buff=0.18)
        right_head = LabelChip("RIGHT COLUMN", accent=SLATE, size=18)
        right_head.next_to(right_panel, UP, buff=0.18)

        # Rows in each column — alternating to show interleave
        left_rows = [_row_bar(1.8, 0.20, INK) for _ in range(4)]
        right_rows = [_row_bar(1.8, 0.20, INK) for _ in range(4)]
        for i, r in enumerate(left_rows):
            r.move_to(left_panel.get_top() + DOWN*(0.5 + i*0.55))
        for i, r in enumerate(right_rows):
            r.move_to(right_panel.get_top() + DOWN*(0.5 + i*0.55))

        # Extracted text panel (right side)
        extract_panel = _panel(RIGHT*5.2 + UP*0.3, 2.2, 3.2)
        extract_head = LabelChip("PARSER OUTPUT", accent=CRIMSON, size=18)
        extract_head.next_to(extract_panel, UP, buff=0.18)

        # Interleaved output rows (alternating teal/crimson to show mixed columns)
        interleaved = []
        colors = [TEAL, CRIMSON, TEAL, CRIMSON, TEAL, CRIMSON, TEAL, CRIMSON]
        for i in range(8):
            r = _row_bar(1.5, 0.18, colors[i])
            r.move_to(extract_panel.get_top() + DOWN*(0.45 + i*0.32))
            interleaved.append(r)

        # Scanner arrow (sweeping left to right)
        scan_line = Line(LEFT*4.3 + UP*1.5, RIGHT*1.5 + UP*1.5, color=GOLD, stroke_width=2.5)
        scan_line.set_stroke(opacity=0.7)
        scan_line._qc_intentional = True  # scan arrow crosses layout rows intentionally

        self.play(FadeIn(left_panel), FadeIn(right_panel),
                  FadeIn(left_head), FadeIn(right_head), run_time=0.8)
        for r in left_rows:
            self.play(FadeIn(r, scale=0.9), run_time=0.15)
        for r in right_rows:
            self.play(FadeIn(r, scale=0.9), run_time=0.15)
        self.play(FadeIn(extract_panel), FadeIn(extract_head), run_time=0.6)
        # Show scanner sweeping at each row height, producing interleaved output
        for i in range(4):
            scan = Line(LEFT*4.3 + UP*(1.5 - i*0.55), RIGHT*1.5 + UP*(1.5 - i*0.55),
                        color=GOLD, stroke_width=2.5)
            scan.set_stroke(opacity=0.7)
            scan._qc_intentional = True
            self.play(Create(scan), run_time=0.25)
            self.play(FadeIn(interleaved[i*2]), FadeIn(interleaved[i*2+1]), run_time=0.25)
            self.remove(scan)
        self.wait(max(0.3, total - 4.2))


class B06_GraphicBlind(Scene):
    def construct(self):
        total = DUR["B06"]

        # Header banner graphic (name-in-image)
        banner = Rectangle(width=6.0, height=1.0)
        banner.set_fill(SLATE, 0.85).set_stroke(width=0, opacity=0)
        banner.move_to(UP * 2.4)
        banner_text = Text("Ayesha Karimova", font=DISPLAY, color=WHITE, font_size=28)
        banner_text.move_to(banner)
        banner_text._qc_intentional = True  # white on slate banner (not cream): intentional contrast
        banner_label = LabelChip("NAME IN IMAGE", accent=SLATE, size=18)
        banner_label.next_to(banner, LEFT, buff=0.3)

        # Skill bars (graphic elements)
        skill_panel = _panel(LEFT*4.2 + DOWN*0.5, 2.0, 2.2)
        skill_head = SerifLabel("skills sidebar", SLATE, size=20)
        skill_head.next_to(skill_panel, UP, buff=0.18)
        bar_labels = ["Python", "SQL", "Excel"]
        skill_bars = []
        for i, lbl in enumerate(bar_labels):
            barlbl = Text(lbl, font=SERIF, color=INK, font_size=18)
            bar = Rectangle(width=1.2 * (0.9 - i*0.15), height=0.18)
            bar.set_fill(SLATE, 0.6).set_stroke(width=0, opacity=0)
            row = VGroup(barlbl, bar).arrange(RIGHT, buff=0.12)
            row.move_to(skill_panel.get_top() + DOWN*(0.55 + i*0.55))
            skill_bars.append(row)

        # Parser output (blank for both)
        out_panel = _panel(RIGHT*4.0 + UP*0.4, 2.4, 3.2)
        out_head = LabelChip("PARSER OUTPUT", accent=CRIMSON, size=18)
        out_head.next_to(out_panel, UP, buff=0.18)

        name_out = Text("[NAME ABSENT]", font=MONO, color=CRIMSON, font_size=20)
        name_out.move_to(out_panel.get_top() + DOWN*0.7)
        skills_out = Text("[SKILLS: NONE]", font=MONO, color=CRIMSON, font_size=20)
        skills_out.move_to(out_panel.get_center() + DOWN*0.3)

        # Scanner beam
        scan_banner = Line(LEFT*3.5+UP*2.4, RIGHT*2.2+UP*2.4, color=GOLD, stroke_width=2.5)
        scan_banner.set_stroke(opacity=0.7)
        scan_banner._qc_intentional = True
        scan_skills = Line(LEFT*5.4+DOWN*0.5, LEFT*2.2+DOWN*0.5, color=GOLD, stroke_width=2.5)
        scan_skills.set_stroke(opacity=0.7)
        scan_skills._qc_intentional = True

        self.play(FadeIn(banner), FadeIn(banner_text), FadeIn(banner_label), run_time=0.8)
        self.play(FadeIn(skill_panel), FadeIn(skill_head), run_time=0.5)
        for sb in skill_bars:
            self.play(FadeIn(sb), run_time=0.2)
        self.play(FadeIn(out_panel), FadeIn(out_head), run_time=0.5)
        self.play(Create(scan_banner), run_time=0.5)
        self.play(FadeIn(name_out), run_time=0.4)
        self.remove(scan_banner)
        self.play(Create(scan_skills), run_time=0.5)
        self.play(FadeIn(skills_out), run_time=0.4)
        self.remove(scan_skills)
        self.wait(max(0.3, total - 4.0))


class B07_SafeVsDanger(Scene):
    def construct(self):
        total = DUR["B07"]

        # Dividing line
        divider = Line(UP*3.2, DOWN*3.2, color=INK, stroke_width=1.5)
        divider.move_to(ORIGIN)

        # TEAL side (left) — safe structures
        safe_head = LabelChip("SAFE ZONES", accent=TEAL, size=22)
        safe_head.move_to(LEFT*3.2 + UP*2.8)

        safe_items = [
            "Single-column layout",
            "Text headings as plain words",
            "Dates adjacent to roles",
            "Skills as a plain list",
            "Real text throughout",
        ]
        safe_labels = []
        for i, item in enumerate(safe_items):
            dot = Dot(radius=0.08, color=TEAL)
            txt = Text(item, font=SERIF, color=INK, font_size=22)
            row = VGroup(dot, txt).arrange(RIGHT, buff=0.18)
            row.move_to(LEFT*3.0 + UP*(1.8 - i*0.72))
            safe_labels.append(row)

        # CRIMSON side (right) — danger zones
        danger_head = LabelChip("DANGER ZONES", accent=CRIMSON, size=22)
        danger_head.move_to(RIGHT*3.2 + UP*2.8)

        danger_items = [
            "Two-column layout",
            "Name in header graphic",
            "Skill bars as images",
            "Tables for layout",
            "Text inside any image",
        ]
        danger_labels = []
        for i, item in enumerate(danger_items):
            dot = Dot(radius=0.08, color=CRIMSON)
            txt = Text(item, font=SERIF, color=INK, font_size=22)
            row = VGroup(dot, txt).arrange(RIGHT, buff=0.18)
            row.move_to(RIGHT*3.0 + UP*(1.8 - i*0.72))
            danger_labels.append(row)

        self.play(Create(divider), run_time=0.5)
        self.play(FadeIn(safe_head), FadeIn(danger_head), run_time=0.6)
        for s, d in zip(safe_labels, danger_labels):
            self.play(FadeIn(s, shift=RIGHT*0.15), FadeIn(d, shift=LEFT*0.15), run_time=0.35)
        self.wait(max(0.3, total - 0.5 - 0.6 - 5*0.35))


class B08_PasteTest(Scene):
    def construct(self):
        total = DUR["B08"]

        # Left: designed resume (crimson = broken)
        left_panel = _panel(LEFT*3.3 + UP*0.2, 3.2, 4.2)
        left_head = LabelChip("DESIGNED RESUME", accent=SLATE, size=20)
        left_head.next_to(left_panel, UP, buff=0.22)

        # Rows representing the scrambled parser output (explicit sizes for Gate W)
        lr0 = Text("Data Analyst, 2023-2024", font=MONO, color=CRIMSON, font_size=20)
        lr1 = Text("Led data pipeline efforts", font=MONO, color=INK, font_size=19)
        lr2 = Text("Python skills: [NONE]", font=MONO, color=CRIMSON, font_size=20)
        lr3 = Text("Collaborated with teams", font=MONO, color=INK, font_size=19)
        lr4 = Text("[NAME ABSENT]", font=MONO, color=CRIMSON, font_size=20)
        lr5 = Text("Experience in analytics", font=MONO, color=INK, font_size=19)
        left_rows = [lr0, lr1, lr2, lr3, lr4, lr5]
        for i, r in enumerate(left_rows):
            r.move_to(left_panel.get_top() + DOWN*(0.7 + i*0.55))
            if r.width > 2.8:
                r.scale_to_fit_width(2.8)

        # Right: single-column (teal = clean)
        right_panel = _panel(RIGHT*3.3 + UP*0.2, 3.2, 4.2)
        right_head = LabelChip("SINGLE-COLUMN", accent=TEAL, size=20)
        right_head.next_to(right_panel, UP, buff=0.22)

        rr0 = Text("Ayesha Karimova", font=MONO, color=TEAL, font_size=20)
        rr1 = Text("ayesha@email.com", font=MONO, color=INK, font_size=19)
        rr2 = Text("Data Analyst, 2023-2024", font=MONO, color=TEAL, font_size=20)
        rr3 = Text("Led data pipeline efforts", font=MONO, color=INK, font_size=19)
        rr4 = Text("Skills: Python, SQL, Excel", font=MONO, color=TEAL, font_size=20)
        rr5 = Text("Collaborated with teams", font=MONO, color=INK, font_size=19)
        right_rows = [rr0, rr1, rr2, rr3, rr4, rr5]
        for i, r in enumerate(right_rows):
            r.move_to(right_panel.get_top() + DOWN*(0.7 + i*0.55))
            if r.width > 2.8:
                r.scale_to_fit_width(2.8)

        # Build both sides
        self.play(FadeIn(left_panel), FadeIn(left_head), run_time=0.6)
        for r in left_rows:
            self.play(FadeIn(r), run_time=0.18)
        self.play(FadeIn(right_panel), FadeIn(right_head), run_time=0.6)
        for r in right_rows:
            self.play(FadeIn(r), run_time=0.18)
        # Transform effect: the crimson lines resolve to teal on the right
        self.wait(max(0.3, total - 0.6 - 6*0.18 - 0.6 - 6*0.18 - 0.3))


class B10_PasteTestRule(Scene):
    def construct(self):
        total = DUR["B10"]
        # Quote card with paste-test principle
        q1 = Text("Copy all text from the PDF.", font=SERIF, color=INK, font_size=30)
        q2 = Text("Paste it into a plain text editor.", font=SERIF, color=INK, font_size=30)
        q3 = Text("What you see is what the parser sees.", font=SERIF, color=INK, font_size=30, weight=BOLD)
        block = VGroup(q1, q2, q3).arrange(DOWN, buff=0.30).move_to(UP*0.1)
        # Gold highlighter sweep behind q3
        hl = Rectangle(width=q3.width + 0.4, height=q3.height + 0.18)
        hl.set_fill(GOLD, 0.55).set_stroke(width=0, opacity=0)
        hl.move_to(q3.get_center())
        attr = SerifLabel("the paste test", TEAL, size=22)
        attr.next_to(block, DOWN, buff=0.4)
        self.play(FadeIn(q1), FadeIn(q2), run_time=0.8)
        self.play(FadeIn(q3), run_time=0.5)
        self.play(FadeIn(hl), run_time=0.6)
        self.play(FadeIn(attr, shift=UP*0.1), run_time=0.5)
        self.wait(max(0.3, total - 2.4))


class B11_End(Scene):
    def construct(self):
        total = DUR["B11"]
        t1 = Text("Beautiful design disappears.", font=SERIF, color=CRIMSON,
                  font_size=38, weight=BOLD)
        t2 = Text("Parseable layout reaches the human.", font=SERIF, color=TEAL,
                  font_size=38, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.35)
        u = Line(t2.get_corner(DL)+DOWN*0.14, t2.get_corner(DR)+DOWN*0.14,
                 color=TEAL, stroke_width=2)
        s = Text("from The Reallocation Engine -- chapter 13", font=SERIF,
                 color=INK, font_size=22)
        s.next_to(u, DOWN, buff=0.45)
        self.play(FadeIn(t1), run_time=0.7)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP*0.1), run_time=0.6)
        self.wait(max(0.3, total - 2.2))
