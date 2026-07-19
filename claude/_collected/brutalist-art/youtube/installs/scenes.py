"""scenes.py — Manim scenes for 'Installs, .env & Credentials' (installs)

One Scene subclass per GRAPHIC beat with shot.source == 'own'.
Beats: B01, B03, B04, B06, B07, B09, B10, B11 (hero), B12.
Palette: teardown — flat white GROUND, ink INK, red CRIMSON, teal ACCENT_TEAL.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "runtime" / "manim"))
from animated_graphics import *
import numpy as np

ACCENT_TEAL = "#1F6F5C"


# ──────────────────────────────────────────────────────────
# B01 — ONE FILE EVERYTHING (16s)
# .env at center; feature lines plug in from right; two greyed = off
# ──────────────────────────────────────────────────────────
class B01_OneFileEverything(Scene):
    def construct(self):
        section = LabelChip("ONE FILE", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Central .env box
        env_lbl = Text(".env", font=MONO, color=INK, font_size=40, weight=BOLD)
        env_box = surround_box(env_lbl, buff=0.38, fill_color=GROUND,
                               stroke_color=ACCENT_TEAL, stroke_width=3)
        env_grp = VGroup(env_box, env_lbl).move_to(ORIGIN + LEFT * 1.0)
        self.play(FadeIn(env_grp, scale=0.9), run_time=0.7)

        # Feature lines: (name, color, is_greyed)
        features = [
            ("narration",  INK,     False),
            ("ai-video",   SLATE,   True),   # blank = off
            ("publish",    INK,     False),
            ("fal",        SLATE,   True),   # blank = off
        ]
        feature_grps = VGroup()
        for i, (name, color, greyed) in enumerate(features):
            chip_txt = Text(name, font=MONO, color=color, font_size=22)
            chip_box = surround_box(chip_txt, buff=0.18, fill_color=GROUND,
                                    stroke_color=color, stroke_width=1.5)
            chip_grp = VGroup(chip_box, chip_txt)
            y = 0.9 - i * 0.68
            chip_grp.move_to(RIGHT * 3.5 + UP * y)
            line = Line(
                chip_grp.get_left() + LEFT * 0.05,
                env_box.get_right() + RIGHT * 0.05,
                stroke_color=color, stroke_width=1.5,
            )
            if greyed:
                blank = Text("(blank)", font=MONO, color=SLATE, font_size=14)
                blank.next_to(chip_grp, RIGHT, buff=0.15)
                feature_grps.add(chip_grp, line, blank)
            else:
                feature_grps.add(chip_grp, line)

        self.play(LaggedStart(*[
            AnimationGroup(FadeIn(mob, shift=LEFT * 0.2))
            for mob in feature_grps
        ], lag_ratio=0.18), run_time=1.8)
        self.wait(0.4)

        # "blank = off" callout
        note = Text("blank key = feature off", font=SERIF, color=SLATE,
                    font_size=20, slant=ITALIC)
        note.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note), run_time=0.6)

        # "tool loads it for you" subtitle
        loader = SerifLabel("./art loads .env for you", accent=INK, size=20)
        loader.next_to(env_grp, DOWN, buff=0.55)
        self.play(FadeIn(loader), run_time=0.6)
        self.wait(5.0)


# ──────────────────────────────────────────────────────────
# B03 — CREDENTIALS FOLDER (16s)
# Folder tree: youtube/credentials/nikbearbrown/ + three files
# ──────────────────────────────────────────────────────────
class B03_CredentialsFolder(Scene):
    def construct(self):
        section = LabelChip("CREDENTIALS", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Folder header
        folder_lbl = Text("youtube/credentials/nikbearbrown/", font=MONO,
                          color=INK, font_size=22, weight=BOLD)
        folder_box = surround_box(folder_lbl, buff=0.28, fill_color="#FFF8F0",
                                  stroke_color=CRIMSON, stroke_width=2)
        folder_grp = VGroup(folder_box, folder_lbl)
        folder_grp.move_to(UP * 1.8)
        self.play(FadeIn(folder_grp, shift=DOWN * 0.15), run_time=0.6)

        # Three files — build as a single block and reveal at once
        f1 = Text("  client_secret.json          # download from Google Cloud console",
                  font=MONO, color=INK, font_size=17)
        f2 = Text("  youtube_token.json           # created on first auth",
                  font=MONO, color=INK, font_size=17)
        f3 = Text("  youtube_publish_ledger.json  # upload history",
                  font=MONO, color=INK, font_size=17)
        file_block = VGroup(f1, f2, f3).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        file_block.next_to(folder_grp, DOWN, buff=0.35)
        file_block.shift(RIGHT * 0.3)

        self.play(FadeIn(file_block), run_time=0.7)
        self.wait(0.3)

        # Lock stamp
        lock_txt = Text("gitignored", font=DISPLAY, color=CRIMSON,
                        font_size=18, weight=BOLD)
        lock_box = surround_box(lock_txt, buff=0.18, fill_color=GROUND,
                                stroke_color=CRIMSON, stroke_width=2)
        lock_grp = VGroup(lock_box, lock_txt)
        lock_grp.next_to(folder_grp, RIGHT, buff=0.4)
        self.play(FadeIn(lock_grp), run_time=0.5)
        self.wait(0.4)

        # Channel selector line
        channel_line = Text("ART_YOUTUBE_CHANNEL=nikbearbrown",
                            font=MONO, color=ACCENT_TEAL, font_size=20)
        channel_box = surround_box(channel_line, buff=0.22, fill_color=GROUND,
                                   stroke_color=ACCENT_TEAL, stroke_width=2)
        channel_grp = VGroup(channel_box, channel_line)
        channel_grp.to_edge(DOWN, buff=0.65)
        note = Text("one line picks the active channel", font=SERIF, color=SLATE,
                    font_size=18, slant=ITALIC)
        note.next_to(channel_grp, DOWN, buff=0.18)
        self.play(FadeIn(channel_grp), FadeIn(note), run_time=0.7)
        self.wait(4.5)


# ──────────────────────────────────────────────────────────
# B04 — WHAT IS NPX (15s)
# Left: stale global pile. Right: npx transient + pinned version
# ──────────────────────────────────────────────────────────
class B04_WhatIsNpx(Scene):
    def construct(self):
        section = LabelChip("NPX", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        divider = Line(UP * 3, DOWN * 3, stroke_color=SLATE, stroke_width=1)
        divider.move_to(ORIGIN)
        self.play(Create(divider), run_time=0.4)

        # LEFT: messy global install pile
        left_lbl = Text("global install", font=SERIF, color=CRIMSON,
                        font_size=20, slant=ITALIC)
        left_lbl.move_to(LEFT * 3.2 + UP * 2.5)
        self.play(FadeIn(left_lbl), run_time=0.4)

        versions = ["remotion@4.1", "remotion@3.9", "remotion@3.7 ← wrong version"]
        boxes = VGroup()
        for i, v in enumerate(versions):
            vt = Text(v, font=MONO, color=(SLATE if i == 2 else INK), font_size=16)
            vb = auto_box(vt, h_pad=0.15, v_pad=0.12, fill_color="#F5F5F5",
                          stroke_color=(CRIMSON if i == 2 else SLATE), stroke_width=1.5)
            vg = VGroup(vb, vt)
            boxes.add(vg)
        boxes.arrange(DOWN, buff=0.1)
        boxes.move_to(LEFT * 3.2 + UP * 0.3)
        self.play(FadeIn(boxes, shift=DOWN * 0.1), run_time=0.9)
        self.wait(0.3)

        # RIGHT: npx single transient run
        right_lbl = Text("npx — run once", font=SERIF, color=ACCENT_TEAL,
                         font_size=20, slant=ITALIC)
        right_lbl.move_to(RIGHT * 3.2 + UP * 2.5)
        self.play(FadeIn(right_lbl), run_time=0.4)

        npx_txt = Text("npx remotion@4.1", font=MONO, color=INK, font_size=18)
        npx_box = auto_box(npx_txt, h_pad=0.22, v_pad=0.15,
                           fill_color=GROUND, stroke_color=ACCENT_TEAL, stroke_width=2.5)
        npx_grp = VGroup(npx_box, npx_txt)
        npx_grp.move_to(RIGHT * 3.2 + UP * 0.6)

        check = Text("✓ pinned version", font=MONO, color=ACCENT_TEAL, font_size=18)
        check.next_to(npx_grp, DOWN, buff=0.25)

        vanish = Text("leaves nothing behind", font=SERIF, color=SLATE,
                      font_size=16, slant=ITALIC)
        vanish.next_to(check, DOWN, buff=0.18)

        self.play(FadeIn(npx_grp, scale=0.9), run_time=0.5)
        self.play(FadeIn(check), run_time=0.4)
        self.play(FadeIn(vanish), run_time=0.4)
        self.wait(0.4)

        # npx box fades (transient)
        self.play(npx_grp.animate.set_opacity(0.3), run_time=0.6)
        self.wait(3.8)


# ──────────────────────────────────────────────────────────
# B06 — WHAT IS PIP (13s)
# PyPI cloud at top; arrows down to library chips; one install command
# ──────────────────────────────────────────────────────────
class B06_WhatIsPip(Scene):
    def construct(self):
        section = LabelChip("PIP", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # PyPI cloud (represented as a rounded box)
        pypi_txt = Text("PyPI", font=DISPLAY, color=WHITE, font_size=28, weight=BOLD)
        pypi_box = auto_box(pypi_txt, h_pad=0.35, v_pad=0.28, fill_color=INK,
                            stroke_color=INK, stroke_width=0)
        pypi_grp = VGroup(pypi_box, pypi_txt).move_to(UP * 2.8)
        self.play(FadeIn(pypi_grp, scale=0.9), run_time=0.5)

        # Library chips
        libs = ["manim", "librosa", "faster-whisper", "Pillow", "vtracer", "google-api"]
        chip_grps = VGroup()
        for lib in libs:
            lt = Text(lib, font=MONO, color=INK, font_size=17)
            lb = auto_box(lt, h_pad=0.16, v_pad=0.12, fill_color=GROUND,
                          stroke_color=SLATE, stroke_width=1.5)
            chip_grps.add(VGroup(lb, lt))
        chip_grps.arrange_in_grid(rows=2, cols=3, buff=0.22)
        chip_grps.move_to(ORIGIN + DOWN * 0.3)

        # Arrows from PyPI to each chip
        arrows = VGroup()
        for chip in chip_grps:
            arr = Arrow(
                pypi_grp.get_bottom() + DOWN * 0.05,
                chip.get_top() + UP * 0.05,
                stroke_color=SLATE, stroke_width=1.5, tip_length=0.18,
            )
            arrows.add(arr)

        self.play(FadeIn(arrows), run_time=0.7)
        self.play(FadeIn(chip_grps, scale=0.9), run_time=0.8)
        self.wait(0.3)

        # Install command
        cmd_txt = Text("pip install -r requirements.txt", font=MONO,
                       color=ACCENT_TEAL, font_size=18)
        cmd_box = auto_box(cmd_txt, h_pad=0.22, v_pad=0.15, fill_color=GROUND,
                           stroke_color=ACCENT_TEAL, stroke_width=2)
        cmd_grp = VGroup(cmd_box, cmd_txt)
        cmd_grp.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(cmd_grp), run_time=0.5)
        self.wait(3.5)


# ──────────────────────────────────────────────────────────
# B07 — VENV (14s)
# Bubble = .venv; inside: project python + numpy<2; outside: system + numpy 2.x
# ──────────────────────────────────────────────────────────
class B07_Venv(Scene):
    def construct(self):
        section = LabelChip("VENV", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # .venv bubble (ellipse)
        bubble = Ellipse(width=6.4, height=4.4,
                         fill_color=GROUND, fill_opacity=1,
                         stroke_color=ACCENT_TEAL, stroke_width=3)
        bubble.move_to(LEFT * 1.2)
        bubble_lbl = Text(".venv", font=DISPLAY, color=ACCENT_TEAL,
                          font_size=22, weight=BOLD)
        bubble_lbl.move_to(bubble.get_top() + DOWN * 0.35)

        self.play(Create(bubble), FadeIn(bubble_lbl), run_time=0.8)

        # Inside: python interpreter + key chips
        py_in = Text("python3", font=MONO, color=INK, font_size=20)
        py_in_box = surround_box(py_in, buff=0.18, fill_color="#F0F8F0",
                                 stroke_color=ACCENT_TEAL, stroke_width=2)
        py_in_grp = VGroup(py_in_box, py_in).move_to(bubble.get_center() + UP * 0.5 + LEFT * 0.3)

        numpy_pin = Text("numpy < 2", font=MONO, color=ACCENT_TEAL, font_size=17)
        numpy_pin_box = surround_box(numpy_pin, buff=0.15, fill_color=GROUND,
                                     stroke_color=ACCENT_TEAL, stroke_width=1.5)
        numpy_pin_grp = VGroup(numpy_pin_box, numpy_pin)
        numpy_pin_grp.next_to(py_in_grp, DOWN, buff=0.2)

        manim_chip = Text("manim ✓", font=MONO, color=ACCENT_TEAL, font_size=16)
        manim_chip_box = surround_box(manim_chip, buff=0.12, fill_color=GROUND,
                                      stroke_color=ACCENT_TEAL, stroke_width=1.5)
        manim_grp = VGroup(manim_chip_box, manim_chip)
        manim_grp.next_to(numpy_pin_grp, DOWN, buff=0.15)

        inside = VGroup(py_in_grp, numpy_pin_grp, manim_grp)
        self.play(LaggedStart(*[FadeIn(m, scale=0.9) for m in inside],
                              lag_ratio=0.3), run_time=0.9)
        self.wait(0.3)

        # Outside: system python + numpy 2.x
        sys_py = Text("system python3", font=MONO, color=SLATE, font_size=18)
        sys_py_box = surround_box(sys_py, buff=0.16, fill_color="#F5F5F5",
                                  stroke_color=SLATE, stroke_width=1.5)
        sys_py_grp = VGroup(sys_py_box, sys_py).move_to(RIGHT * 4.2 + UP * 0.8)

        numpy_sys = Text("numpy 2.x", font=MONO, color=CRIMSON, font_size=17)
        numpy_sys_box = surround_box(numpy_sys, buff=0.14, fill_color=GROUND,
                                     stroke_color=CRIMSON, stroke_width=1.5)
        numpy_sys_grp = VGroup(numpy_sys_box, numpy_sys)
        numpy_sys_grp.next_to(sys_py_grp, DOWN, buff=0.18)

        outside = VGroup(sys_py_grp, numpy_sys_grp)
        self.play(LaggedStart(*[FadeIn(m) for m in outside], lag_ratio=0.3), run_time=0.6)

        # Caption
        caption = SerifLabel("the pin holds here · nowhere else", accent=INK, size=20)
        caption.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(4.0)


# ──────────────────────────────────────────────────────────
# B09 — CLAUDE USES VENV (17s)
# claude terminal INSIDE .venv; python3 resolves to manim/librosa (green)
# OUTSIDE: same call → ModuleNotFoundError (red)
# ──────────────────────────────────────────────────────────
class B09_ClaudeUsesVenv(Scene):
    def construct(self):
        section = LabelChip("CLAUDE CODE + VENV", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # .venv bubble
        bubble = Ellipse(width=7.0, height=4.2,
                         fill_color=GROUND, fill_opacity=1,
                         stroke_color=ACCENT_TEAL, stroke_width=2.5)
        bubble.move_to(LEFT * 0.8 + DOWN * 0.2)
        bubble_lbl = Text(".venv", font=DISPLAY, color=ACCENT_TEAL, font_size=20, weight=BOLD)
        bubble_lbl.move_to(bubble.get_top() + DOWN * 0.3)
        self.play(Create(bubble), FadeIn(bubble_lbl), run_time=0.7)

        # Claude terminal inside bubble
        claude_txt = Text("claude", font=MONO, color=WHITE, font_size=20)
        claude_box = surround_box(claude_txt, buff=0.22,
                                  fill_color="#111111", stroke_width=0)
        claude_grp = VGroup(claude_box, claude_txt)
        claude_grp.move_to(bubble.get_center() + LEFT * 1.5 + UP * 0.3)
        self.play(FadeIn(claude_grp, scale=0.9), run_time=0.5)

        # python3 → manim/librosa arrows (green)
        resolve_arrow = Arrow(
            claude_grp.get_right() + RIGHT * 0.05,
            claude_grp.get_right() + RIGHT * 1.6,
            stroke_color=ACCENT_TEAL, stroke_width=2, tip_length=0.2,
        )
        manim_ok = Text("manim ✓", font=MONO, color=ACCENT_TEAL, font_size=17)
        librosa_ok = Text("librosa ✓", font=MONO, color=ACCENT_TEAL, font_size=17)
        resolved = VGroup(manim_ok, librosa_ok).arrange(DOWN, buff=0.15)
        resolved.move_to(claude_grp.get_right() + RIGHT * 2.5)

        self.play(GrowArrow(resolve_arrow), run_time=0.4)
        self.play(FadeIn(resolved), run_time=0.5)
        self.wait(0.5)

        # Outside bubble: ModuleNotFoundError
        outside_lbl = Text("outside .venv:", font=SERIF, color=SLATE,
                           font_size=18, slant=ITALIC)
        outside_lbl.move_to(RIGHT * 4.8 + UP * 1.5)
        error_txt = Text("ModuleNotFoundError", font=MONO, color=CRIMSON, font_size=16)
        error_box = surround_box(error_txt, buff=0.18, fill_color=GROUND,
                                 stroke_color=CRIMSON, stroke_width=2)
        error_grp = VGroup(error_box, error_txt)
        error_grp.move_to(RIGHT * 4.8 + UP * 0.6)

        self.play(FadeIn(outside_lbl), FadeIn(error_grp), run_time=0.6)
        self.wait(0.4)

        # Fix note
        fix = SerifLabel("activate → renders just work", accent=ACCENT_TEAL, size=20)
        fix.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(fix), run_time=0.5)
        self.wait(5.5)


# ──────────────────────────────────────────────────────────
# B10 — PAID SERVICES (14s)
# ElevenLabs (highlighted teal), higgsfield, fal, YouTube (apart)
# ──────────────────────────────────────────────────────────
class B10_PaidServices(Scene):
    def construct(self):
        section = LabelChip("PAID SERVICES", accent=CRIMSON, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        def make_card(name, desc, accent_color=SLATE, highlight=False):
            name_txt = Text(name, font=DISPLAY, color=INK, font_size=22, weight=BOLD)
            desc_txt = Text(desc, font=SERIF, color=SLATE, font_size=17)
            stack = VGroup(name_txt, desc_txt).arrange(DOWN, buff=0.16)
            box = surround_box(stack, buff=0.28,
                               fill_color=("#F0FAF6" if highlight else GROUND),
                               stroke_color=accent_color,
                               stroke_width=(3 if highlight else 1.5))
            return VGroup(box, stack)

        el_card = make_card("ElevenLabs", "voice + narration", ACCENT_TEAL, highlight=True)
        hg_card = make_card("higgsfield", "AI image / video", SLATE)
        fal_card = make_card("fal.ai", "optional image path", SLATE)

        paid_row = VGroup(el_card, hg_card, fal_card).arrange(RIGHT, buff=0.38)
        paid_row.move_to(UP * 0.5)

        yt_card = make_card("YouTube", "free — just quota'd", SLATE)
        yt_card.next_to(paid_row, DOWN, buff=0.5)
        yt_card.shift(RIGHT * 0.4)

        self.play(FadeIn(el_card, scale=0.9), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(hg_card), FadeIn(fal_card), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(yt_card), run_time=0.5)

        # "the important one" pointer
        pointer = Text("← start here", font=SERIF, color=ACCENT_TEAL,
                       font_size=18, slant=ITALIC)
        pointer.next_to(el_card, RIGHT, buff=0.2)
        self.play(FadeIn(pointer), run_time=0.4)
        self.wait(4.8)


# ──────────────────────────────────────────────────────────
# B11 — CLONE YOUR VOICE — HERO (21s)
# Split-scale: LEFT = 30 min EVERY session (CRIMSON, wasted stack)
#              RIGHT = 30 min ONCE (teal, clean pipeline)
# Big title in EB Garamond
# ──────────────────────────────────────────────────────────
class B11_CloneYourVoice(Scene):
    def construct(self):
        # Hero title — EB Garamond
        title = Text("CLONE YOUR VOICE", font=SERIF, color=INK,
                     font_size=48, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.8)
        self.wait(0.3)

        # Divider
        divider = Line(UP * 2.0, DOWN * 3.0, stroke_color=SLATE, stroke_width=1.5)
        divider.move_to(ORIGIN)
        self.play(Create(divider), run_time=0.4)

        # ── LEFT: "30 min EVERY session" (the cost, CRIMSON) ──
        left_lbl_top = Text("30 min", font=DISPLAY, color=CRIMSON,
                            font_size=26, weight=BOLD)
        left_lbl_bot = Text("EVERY session", font=DISPLAY, color=CRIMSON,
                            font_size=18)
        left_lbl = VGroup(left_lbl_top, left_lbl_bot).arrange(DOWN, buff=0.1)
        left_lbl.move_to(LEFT * 3.2 + UP * 1.4)
        self.play(FadeIn(left_lbl), run_time=0.5)

        # Wasted-cost stack: mic, levels, retake (repeating)
        waste_items = ["🎙 find mic", "🎚 set levels", "↩ retake", "↩ retake again"]
        waste_grps = VGroup()
        for item in waste_items:
            it = Text(item, font=MONO, color=CRIMSON, font_size=17)
            ib = surround_box(it, buff=0.14, fill_color="#FFF5F5",
                              stroke_color=CRIMSON, stroke_width=1.5)
            waste_grps.add(VGroup(ib, it))
        waste_grps.arrange(DOWN, buff=0.1)
        waste_grps.move_to(LEFT * 3.2 + DOWN * 0.6)

        # Cost summary
        cost_lbl = Text("30 min gone · every video", font=SERIF,
                        color=CRIMSON, font_size=16, slant=ITALIC)
        cost_lbl.next_to(waste_grps, DOWN, buff=0.22)

        self.play(LaggedStart(*[FadeIn(w, shift=DOWN * 0.1) for w in waste_grps],
                              lag_ratio=0.25), run_time=1.0)
        self.play(FadeIn(cost_lbl), run_time=0.4)
        self.wait(0.5)

        # ── RIGHT: "30 min ONCE" (the solution, teal) ──
        right_lbl_top = Text("30 min", font=DISPLAY, color=ACCENT_TEAL,
                             font_size=26, weight=BOLD)
        right_lbl_bot = Text("ONCE", font=DISPLAY, color=ACCENT_TEAL, font_size=18)
        right_lbl = VGroup(right_lbl_top, right_lbl_bot).arrange(DOWN, buff=0.1)
        right_lbl.move_to(RIGHT * 3.2 + UP * 1.4)
        self.play(FadeIn(right_lbl), run_time=0.5)

        # Clean pipeline: record → clone → many videos
        rec_txt = Text("record 30 min", font=MONO, color=INK, font_size=16)
        rec_box = surround_box(rec_txt, buff=0.16, fill_color=GROUND,
                               stroke_color=ACCENT_TEAL, stroke_width=2)
        rec_grp = VGroup(rec_box, rec_txt).move_to(RIGHT * 3.2 + UP * 0.2)

        clone_txt = Text("voice clone", font=MONO, color=WHITE, font_size=16)
        clone_box = surround_box(clone_txt, buff=0.18, fill_color=ACCENT_TEAL,
                                 stroke_width=0)
        clone_grp = VGroup(clone_box, clone_txt).move_to(RIGHT * 3.2 + DOWN * 0.5)

        arr1 = Arrow(rec_grp.get_bottom(), clone_grp.get_top(),
                     stroke_color=ACCENT_TEAL, stroke_width=2, tip_length=0.18)

        videos_txt = Text("every video · instantly", font=SERIF,
                          color=ACCENT_TEAL, font_size=16, slant=ITALIC)
        videos_txt.next_to(clone_grp, DOWN, buff=0.28)

        arr2 = Arrow(clone_grp.get_bottom(), videos_txt.get_top(),
                     stroke_color=ACCENT_TEAL, stroke_width=2, tip_length=0.18)

        self.play(FadeIn(rec_grp), run_time=0.4)
        self.play(GrowArrow(arr1), FadeIn(clone_grp, scale=0.9), run_time=0.5)
        self.play(GrowArrow(arr2), FadeIn(videos_txt), run_time=0.5)
        self.wait(0.5)

        # Summary banner
        summary = SerifLabel("one session · every video · your voice", accent=ACCENT_TEAL, size=22)
        summary.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(summary), run_time=0.6)
        self.wait(4.5)


# ──────────────────────────────────────────────────────────
# B12 — MISPRONOUNCE CAVEAT (12s)
# Speech bubble with wrong pronunciation → red mark → phonetic fix → teal
# ──────────────────────────────────────────────────────────
class B12_MispronounceCaveat(Scene):
    def construct(self):
        section = LabelChip("CAVEAT", accent=SLATE, size=17)
        section.to_corner(UL, buff=0.55)
        self.play(FadeIn(section), run_time=0.5)

        # Heading — light tone
        heading = SerifLabel("it mispronounces some words", accent=INK, size=26)
        heading.move_to(UP * 2.2)
        self.play(FadeIn(heading), run_time=0.6)

        sub = Text("so do you", font=SERIF, color=SLATE, font_size=20, slant=ITALIC)
        sub.next_to(heading, DOWN, buff=0.15)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(0.4)

        # Wrong pronunciation (red)
        wrong_txt = Text('"MAY-nim"', font=MONO, color=CRIMSON, font_size=28)
        wrong_box = surround_box(wrong_txt, buff=0.24, fill_color=GROUND,
                                 stroke_color=CRIMSON, stroke_width=2)
        wrong_grp = VGroup(wrong_box, wrong_txt).move_to(LEFT * 2.2 + DOWN * 0.2)

        label_wrong = Text("✗ mispronounced", font=SERIF, color=CRIMSON,
                           font_size=16, slant=ITALIC)
        label_wrong.next_to(wrong_grp, DOWN, buff=0.18)

        self.play(FadeIn(wrong_grp), FadeIn(label_wrong), run_time=0.5)
        self.wait(0.4)

        # Fix arrow → correct
        fix_arrow = Arrow(wrong_grp.get_right() + RIGHT * 0.1,
                          wrong_grp.get_right() + RIGHT * 1.5,
                          stroke_color=ACCENT_TEAL, stroke_width=2, tip_length=0.2)

        correct_txt = Text('"MAN-im"', font=MONO, color=ACCENT_TEAL, font_size=28)
        correct_box = surround_box(correct_txt, buff=0.24, fill_color=GROUND,
                                   stroke_color=ACCENT_TEAL, stroke_width=2)
        correct_grp = VGroup(correct_box, correct_txt).move_to(RIGHT * 2.2 + DOWN * 0.2)

        label_right = Text("✓ fix the text, move on", font=SERIF, color=ACCENT_TEAL,
                           font_size=16, slant=ITALIC)
        label_right.next_to(correct_grp, DOWN, buff=0.18)

        self.play(GrowArrow(fix_arrow), run_time=0.4)
        self.play(FadeIn(correct_grp), FadeIn(label_right), run_time=0.5)
        self.wait(0.4)

        # Review note chip
        chip = LabelChip("review note", accent=SLATE, size=16)
        chip.next_to(correct_grp, RIGHT, buff=0.3)
        self.play(FadeIn(chip), run_time=0.4)

        # Punchline
        punchline = SerifLabel("a rounding error · never fight a mic again", accent=INK, size=20)
        punchline.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(punchline), run_time=0.5)
        self.wait(2.5)
