"""scenes.py — PORTRAIT (9:16) layouts for 'Installs, .env & Credentials' short.

Kept GENERATED beats: B04, B06, B07, B10, B11, B12.
Dropped:             B01, B03, B09.

Frame: 1080×1920 → Manim units ~4.5 wide × 8.0 tall (x: ±2.25, y: ±4.0).
Strategy: vertical stacks replace left/right splits; font sizes ~0.72× landscape.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "runtime" / "manim"))
from animated_graphics import *
import numpy as np

ACCENT_TEAL = "#1F6F5C"


# ──────────────────────────────────────────────────────────
# B04 — WHAT IS NPX (portrait, 15s)
# Top: global install pile (CRIMSON). Bottom: npx transient (TEAL).
# ──────────────────────────────────────────────────────────
class B04_WhatIsNpx(Scene):
    def construct(self):
        section = LabelChip("NPX", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # TOP: global install pile
        left_lbl = Text("global install", font=SERIF, color=CRIMSON, font_size=18, slant=ITALIC)
        left_lbl.move_to(UP * 2.8)

        versions = ["remotion@4.1", "remotion@3.9", "remotion@3.7 ← wrong"]
        boxes = VGroup()
        for i, v in enumerate(versions):
            vt = Text(v, font=MONO, color=(SLATE if i == 2 else INK), font_size=15)
            vb = auto_box(vt, h_pad=0.14, v_pad=0.10, fill_color="#F5F5F5",
                          stroke_color=(CRIMSON if i == 2 else SLATE), stroke_width=1.5)
            boxes.add(VGroup(vb, vt))
        boxes.arrange(DOWN, buff=0.1).move_to(UP * 1.8)
        if boxes.width > 3.8:
            boxes.scale_to_fit_width(3.8)

        self.play(FadeIn(left_lbl), run_time=0.4)
        self.play(FadeIn(boxes, shift=DOWN * 0.1), run_time=0.8)
        self.wait(0.3)

        # Divider
        divider = Line(LEFT * 2.0, RIGHT * 2.0, stroke_color=SLATE, stroke_width=1)
        divider.move_to(UP * 0.65)
        self.play(Create(divider), run_time=0.3)

        # BOTTOM: npx single run
        right_lbl = Text("npx — run once", font=SERIF, color=ACCENT_TEAL,
                         font_size=18, slant=ITALIC)
        right_lbl.move_to(UP * 0.2)

        npx_txt = Text("npx remotion@4.1", font=MONO, color=INK, font_size=17)
        npx_box = auto_box(npx_txt, h_pad=0.20, v_pad=0.13,
                           fill_color=GROUND, stroke_color=ACCENT_TEAL, stroke_width=2.5)
        npx_grp = VGroup(npx_box, npx_txt).move_to(DOWN * 0.6)
        if npx_grp.width > 3.8:
            npx_grp.scale_to_fit_width(3.8)

        check = Text("✓ pinned version", font=MONO, color=ACCENT_TEAL, font_size=17)
        check.next_to(npx_grp, DOWN, buff=0.22)
        vanish = Text("leaves nothing behind", font=SERIF, color=SLATE, font_size=15, slant=ITALIC)
        vanish.next_to(check, DOWN, buff=0.15)

        self.play(FadeIn(right_lbl), run_time=0.35)
        self.play(FadeIn(npx_grp, scale=0.9), run_time=0.45)
        self.play(FadeIn(check), run_time=0.35)
        self.play(FadeIn(vanish), run_time=0.35)
        self.wait(0.35)
        self.play(npx_grp.animate.set_opacity(0.3), run_time=0.55)
        self.wait(4.2)


# ──────────────────────────────────────────────────────────
# B06 — WHAT IS PIP (portrait, 14s)
# PyPI at top; arrows down; library chips in 2×3 grid; command at bottom.
# ──────────────────────────────────────────────────────────
class B06_WhatIsPip(Scene):
    def construct(self):
        section = LabelChip("PIP", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # PyPI at top
        pypi_txt = Text("PyPI", font=DISPLAY, color=WHITE, font_size=26, weight=BOLD)
        pypi_box = auto_box(pypi_txt, h_pad=0.30, v_pad=0.24,
                            fill_color=INK, stroke_color=INK, stroke_width=0)
        pypi_grp = VGroup(pypi_box, pypi_txt).move_to(UP * 3.0)
        self.play(FadeIn(pypi_grp, scale=0.9), run_time=0.5)

        # Library chips — 2 columns × 3 rows for portrait
        libs = ["manim", "librosa", "faster-whisper", "Pillow", "vtracer", "google-api"]
        chip_grps = VGroup()
        for lib in libs:
            lt = Text(lib, font=MONO, color=INK, font_size=15)
            lb = auto_box(lt, h_pad=0.14, v_pad=0.10, fill_color=GROUND,
                          stroke_color=SLATE, stroke_width=1.5)
            chip_grps.add(VGroup(lb, lt))
        chip_grps.arrange_in_grid(rows=3, cols=2, buff=0.18)
        chip_grps.move_to(UP * 0.8)
        if chip_grps.width > 3.8:
            chip_grps.scale_to_fit_width(3.8)

        # Single arrow from PyPI to grid
        arr = Arrow(pypi_grp.get_bottom() + DOWN * 0.05,
                    chip_grps.get_top() + UP * 0.05,
                    stroke_color=SLATE, stroke_width=1.5, tip_length=0.15)
        self.play(FadeIn(arr), run_time=0.5)
        self.play(FadeIn(chip_grps, scale=0.9), run_time=0.7)
        self.wait(0.3)

        # Install command at bottom
        cmd_txt = Text("pip install -r requirements.txt", font=MONO,
                       color=ACCENT_TEAL, font_size=15)
        cmd_box = auto_box(cmd_txt, h_pad=0.20, v_pad=0.13,
                           fill_color=GROUND, stroke_color=ACCENT_TEAL, stroke_width=2)
        cmd_grp = VGroup(cmd_box, cmd_txt)
        cmd_grp.to_edge(DOWN, buff=0.5)
        if cmd_grp.width > 3.8:
            cmd_grp.scale_to_fit_width(3.8)
        self.play(FadeIn(cmd_grp), run_time=0.5)
        self.wait(4.5)


# ──────────────────────────────────────────────────────────
# B07 — VENV (portrait, 15s)
# Bubble centered; inside content; outside items below the bubble.
# ──────────────────────────────────────────────────────────
class B07_Venv(Scene):
    def construct(self):
        section = LabelChip("VENV", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        # .venv bubble — portrait-sized
        bubble = Ellipse(width=3.8, height=4.2,
                         fill_color=GROUND, fill_opacity=1,
                         stroke_color=ACCENT_TEAL, stroke_width=3)
        bubble.move_to(UP * 0.8)
        bubble_lbl = Text(".venv", font=DISPLAY, color=ACCENT_TEAL, font_size=20, weight=BOLD)
        bubble_lbl.move_to(bubble.get_top() + DOWN * 0.32)
        self.play(Create(bubble), FadeIn(bubble_lbl), run_time=0.7)

        # Inside bubble
        py_in = Text("python3", font=MONO, color=INK, font_size=18)
        py_in_box = surround_box(py_in, buff=0.16, fill_color="#F0F8F0",
                                 stroke_color=ACCENT_TEAL, stroke_width=1.8)
        py_in_grp = VGroup(py_in_box, py_in).move_to(bubble.get_center() + UP * 0.7)

        numpy_pin = Text("numpy < 2", font=MONO, color=ACCENT_TEAL, font_size=15)
        numpy_pin_box = surround_box(numpy_pin, buff=0.13, fill_color=GROUND,
                                     stroke_color=ACCENT_TEAL, stroke_width=1.5)
        numpy_pin_grp = VGroup(numpy_pin_box, numpy_pin)
        numpy_pin_grp.next_to(py_in_grp, DOWN, buff=0.18)

        manim_chip = Text("manim ✓", font=MONO, color=ACCENT_TEAL, font_size=14)
        manim_chip_box = surround_box(manim_chip, buff=0.11, fill_color=GROUND,
                                      stroke_color=ACCENT_TEAL, stroke_width=1.5)
        manim_grp = VGroup(manim_chip_box, manim_chip)
        manim_grp.next_to(numpy_pin_grp, DOWN, buff=0.14)

        inside = VGroup(py_in_grp, numpy_pin_grp, manim_grp)
        self.play(LaggedStart(*[FadeIn(m, scale=0.9) for m in inside], lag_ratio=0.25),
                  run_time=0.8)
        self.wait(0.3)

        # Outside: system python below the bubble
        sys_py = Text("system python3", font=MONO, color=SLATE, font_size=16)
        sys_py_box = surround_box(sys_py, buff=0.14, fill_color="#F5F5F5",
                                  stroke_color=SLATE, stroke_width=1.5)
        numpy_sys = Text("numpy 2.x ✗", font=MONO, color=CRIMSON, font_size=15)
        numpy_sys_box = surround_box(numpy_sys, buff=0.12, fill_color=GROUND,
                                     stroke_color=CRIMSON, stroke_width=1.5)
        outside = VGroup(VGroup(sys_py_box, sys_py), VGroup(numpy_sys_box, numpy_sys))
        outside.arrange(RIGHT, buff=0.22)
        outside.next_to(bubble, DOWN, buff=0.35)
        if outside.width > 3.8:
            outside.scale_to_fit_width(3.8)
        self.play(LaggedStart(*[FadeIn(m) for m in outside], lag_ratio=0.25), run_time=0.6)

        caption = SerifLabel("the pin holds here · nowhere else", accent=INK, size=18)
        caption.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(5.0)


# ──────────────────────────────────────────────────────────
# B10 — PAID SERVICES (portrait, 16s)
# Vertical stack of service cards; ElevenLabs highlighted at top.
# ──────────────────────────────────────────────────────────
class B10_PaidServices(Scene):
    def construct(self):
        section = LabelChip("PAID SERVICES", accent=CRIMSON, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        def make_card(name, desc, accent_color=SLATE, highlight=False):
            name_txt = Text(name, font=DISPLAY, color=INK, font_size=20, weight=BOLD)
            desc_txt = Text(desc, font=SERIF, color=SLATE, font_size=15)
            stack = VGroup(name_txt, desc_txt).arrange(DOWN, buff=0.12)
            box = surround_box(stack, buff=0.24,
                               fill_color=("#F0FAF6" if highlight else GROUND),
                               stroke_color=accent_color,
                               stroke_width=(3 if highlight else 1.5))
            return VGroup(box, stack)

        el_card = make_card("ElevenLabs", "voice + narration", ACCENT_TEAL, highlight=True)
        hg_card = make_card("higgsfield", "AI image / video", SLATE)
        fal_card = make_card("fal.ai", "optional image path", SLATE)
        yt_card = make_card("YouTube", "free — just quota'd", SLATE)

        # Vertical stack for portrait
        cards = VGroup(el_card, hg_card, fal_card, yt_card)
        cards.arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        if cards.width > 3.8:
            cards.scale_to_fit_width(3.8)

        pointer = Text("← start here", font=SERIF, color=ACCENT_TEAL,
                       font_size=16, slant=ITALIC)
        pointer.next_to(el_card, RIGHT, buff=0.15)

        self.play(FadeIn(el_card, scale=0.9), run_time=0.55)
        self.wait(0.2)
        self.play(FadeIn(hg_card), FadeIn(fal_card), run_time=0.55)
        self.wait(0.2)
        self.play(FadeIn(yt_card), run_time=0.45)
        self.play(FadeIn(pointer), run_time=0.35)
        self.wait(6.5)


# ──────────────────────────────────────────────────────────
# B11 — CLONE YOUR VOICE — HERO (portrait, 26s)
# Top section: 30 min EVERY (CRIMSON). Bottom: 30 min ONCE (TEAL).
# ──────────────────────────────────────────────────────────
class B11_CloneYourVoice(Scene):
    def construct(self):
        # Hero title
        title = Text("CLONE YOUR VOICE", font=SERIF, color=INK, font_size=36, weight=BOLD)
        title.to_edge(UP, buff=0.55)
        if title.width > 3.8:
            title.scale_to_fit_width(3.8)
        self.play(FadeIn(title, shift=DOWN * 0.18), run_time=0.7)
        self.wait(0.2)

        # Divider (between title and content sections)
        divider = Line(LEFT * 2.0, RIGHT * 2.0, stroke_color=SLATE, stroke_width=1.5)
        divider.move_to(UP * 2.35)
        self.play(Create(divider), run_time=0.3)

        # TOP: 30 min EVERY session (CRIMSON) — well above the waste_grps
        left_lbl = Text("30 min  EVERY session", font=DISPLAY, color=CRIMSON,
                        font_size=20, weight=BOLD)
        left_lbl.move_to(UP * 1.75)
        if left_lbl.width > 3.8:
            left_lbl.scale_to_fit_width(3.8)
        self.play(FadeIn(left_lbl), run_time=0.4)

        waste_items = ["🎙 find mic", "🎚 set levels", "↩ retake"]
        waste_grps = VGroup()
        for item in waste_items:
            it = Text(item, font=MONO, color=CRIMSON, font_size=15)
            ib = auto_box(it, h_pad=0.12, v_pad=0.10, fill_color="#FFF5F5",
                          stroke_color=CRIMSON, stroke_width=1.5)
            waste_grps.add(VGroup(ib, it))
        waste_grps.arrange(DOWN, buff=0.1).move_to(UP * 0.85)
        if waste_grps.width > 3.8:
            waste_grps.scale_to_fit_width(3.8)
        self.play(LaggedStart(*[FadeIn(w, shift=DOWN * 0.08) for w in waste_grps],
                              lag_ratio=0.2), run_time=0.7)
        self.wait(0.5)

        # Divider 2
        divider2 = Line(LEFT * 2.0, RIGHT * 2.0, stroke_color=SLATE, stroke_width=1.5)
        divider2.move_to(DOWN * 0.3)
        self.play(Create(divider2), run_time=0.3)

        # BOTTOM: 30 min ONCE (TEAL)
        right_lbl = Text("30 min  ONCE", font=DISPLAY, color=ACCENT_TEAL,
                         font_size=20, weight=BOLD)
        right_lbl.move_to(DOWN * 0.75)
        self.play(FadeIn(right_lbl), run_time=0.4)

        rec_txt = Text("record 30 min", font=MONO, color=INK, font_size=15)
        rec_box = surround_box(rec_txt, buff=0.14, fill_color=GROUND,
                               stroke_color=ACCENT_TEAL, stroke_width=1.8)
        rec_grp = VGroup(rec_box, rec_txt).move_to(DOWN * 1.3)

        arr1 = Arrow(rec_grp.get_bottom(), rec_grp.get_bottom() + DOWN * 0.45,
                     stroke_color=ACCENT_TEAL, stroke_width=2, tip_length=0.16, buff=0)

        clone_txt = Text("voice clone", font=MONO, color=WHITE, font_size=15)
        clone_box = surround_box(clone_txt, buff=0.16, fill_color=ACCENT_TEAL, stroke_width=0)
        clone_grp = VGroup(clone_box, clone_txt).move_to(DOWN * 2.05)

        arr2 = Arrow(clone_grp.get_bottom(), clone_grp.get_bottom() + DOWN * 0.45,
                     stroke_color=ACCENT_TEAL, stroke_width=2, tip_length=0.16, buff=0)

        videos_txt = Text("every video · instantly", font=SERIF,
                          color=ACCENT_TEAL, font_size=15, slant=ITALIC)
        videos_txt.move_to(DOWN * 2.8)

        self.play(FadeIn(rec_grp), run_time=0.35)
        self.play(GrowArrow(arr1), FadeIn(clone_grp, scale=0.9), run_time=0.45)
        self.play(GrowArrow(arr2), FadeIn(videos_txt), run_time=0.45)
        self.wait(0.4)

        summary = SerifLabel("one session · every video · your voice", accent=ACCENT_TEAL, size=18)
        summary.to_edge(DOWN, buff=0.45)
        if summary.width > 3.8:
            summary.scale_to_fit_width(3.8)
        self.play(FadeIn(summary), run_time=0.55)
        self.wait(8.5)


# ──────────────────────────────────────────────────────────
# B12 — MISPRONOUNCE CAVEAT (portrait, 13s)
# Heading + wrong/right pronunciation stacked vertically.
# ──────────────────────────────────────────────────────────
class B12_MispronounceCaveat(Scene):
    def construct(self):
        section = LabelChip("CAVEAT", accent=SLATE, size=14)
        section.to_corner(UL, buff=0.45)
        self.play(FadeIn(section), run_time=0.5)

        heading = SerifLabel("it mispronounces some words", accent=INK, size=22)
        heading.move_to(UP * 2.8)
        if heading.width > 3.8:
            heading.scale_to_fit_width(3.8)
        self.play(FadeIn(heading), run_time=0.55)

        sub = Text("so do you", font=SERIF, color=SLATE, font_size=18, slant=ITALIC)
        sub.next_to(heading, DOWN, buff=0.14)
        self.play(FadeIn(sub), run_time=0.35)
        self.wait(0.35)

        # Wrong pronunciation (top)
        wrong_txt = Text('"MAY-nim"', font=MONO, color=CRIMSON, font_size=26)
        wrong_box = surround_box(wrong_txt, buff=0.22, fill_color=GROUND,
                                 stroke_color=CRIMSON, stroke_width=2)
        wrong_grp = VGroup(wrong_box, wrong_txt).move_to(UP * 1.0)
        label_wrong = Text("✗ mispronounced", font=SERIF, color=CRIMSON,
                           font_size=14, slant=ITALIC)
        label_wrong.next_to(wrong_grp, DOWN, buff=0.14)
        self.play(FadeIn(wrong_grp), FadeIn(label_wrong), run_time=0.45)
        self.wait(0.3)

        # Arrow down → correct
        fix_arrow = Arrow(label_wrong.get_bottom() + DOWN * 0.05,
                          label_wrong.get_bottom() + DOWN * 0.55,
                          stroke_color=ACCENT_TEAL, stroke_width=2, tip_length=0.18, buff=0)
        self.play(GrowArrow(fix_arrow), run_time=0.35)

        correct_txt = Text('"MAN-im"', font=MONO, color=ACCENT_TEAL, font_size=26)
        correct_box = surround_box(correct_txt, buff=0.22, fill_color=GROUND,
                                   stroke_color=ACCENT_TEAL, stroke_width=2)
        correct_grp = VGroup(correct_box, correct_txt)
        correct_grp.next_to(fix_arrow, DOWN, buff=0.1)
        label_right = Text("✓ fix the text, move on", font=SERIF, color=ACCENT_TEAL,
                           font_size=14, slant=ITALIC)
        label_right.next_to(correct_grp, DOWN, buff=0.14)
        self.play(FadeIn(correct_grp), FadeIn(label_right), run_time=0.45)
        self.wait(0.3)

        punchline = SerifLabel("a rounding error · never fight a mic again", accent=INK, size=17)
        punchline.to_edge(DOWN, buff=0.45)
        if punchline.width > 3.8:
            punchline.scale_to_fit_width(3.8)
        self.play(FadeIn(punchline), run_time=0.45)
        self.wait(4.0)
