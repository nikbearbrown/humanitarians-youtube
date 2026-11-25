"""short/scenes.py -- native 9:16 Manim beats for the Short (2160x3840).

Its own layouts (not a crop of the landscape film). Frame 4.5 x 8 units; content
kept between y = 3.3 and y = -2.5, centred near x = -0.15. Every number comes from
../code/results.json; beat length and cues come from short/beat_sheet.json.
"""
import json
import os
from pathlib import Path

import numpy as np
from manim import *

config.frame_width = 4.5
config.frame_height = 8.0

_CANDIDATES = [Path(__file__).resolve().parent, Path.cwd(),
               Path(os.environ.get("FOLDER_REEL", "/nonexistent")) / "short",
               Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/"
                    "2026-11-22-what-a-finished-folder-looks-like/short")]
SHORT = next(p for p in _CANDIDATES if (p / "beat_sheet.json").is_file()
             and (p.parent / "code" / "results.json").is_file())
RES = json.loads((SHORT.parent / "code" / "results.json").read_text())
SHEET = json.loads((SHORT / "beat_sheet.json").read_text())
BEATS = {b["beat_id"]: b for b in SHEET["beats"]}
SUM, TW = RES["summary"], RES["this_week"]
NF = TW["new_work_folders"]

BG = "#FAF9F5"
INK = "#2B2A26"
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
SOFT_ON_DARK = "#C9C1B2"
ACCENT = "#A64B2A"
TEAL = "#1F4E5F"
GHOST = "#A39A88"
GHOST_DARK = "#5E544C"
SERIF, SANS, MONO = "EB Garamond", "Inter", "JetBrains Mono"
config.background_color = BG

LEFT_X, RIGHT_X = -1.95, 1.65          # content band, centred near x = -0.15
FILE = {"README": "README.md", "FACTCHECK": "FACTCHECK.md", "FRICTIONAL log": "FRICTIONAL.md",
        "PROOF": "PROOF.md", "SHOTLIST": "SHOTLIST.md", "PROMPTS": "PROMPTS.md",
        "beat sheet": "beat_sheet.json", "code": "code/", "description": "description.txt"}
ORDER = ["README", "FACTCHECK", "FRICTIONAL log", "PROOF", "SHOTLIST", "PROMPTS",
         "beat sheet", "code", "description"]


def T(text, size=40, color=INK, font=SANS, weight="NORMAL"):
    """Portrait text: built 4x large and scaled 1/4 (effective size = size * 0.72).
    Colour is set after construction (color= inflates Text's bounding box)."""
    t = Text(text, font=font, font_size=size * 0.72 * 4, weight=weight).scale(1 / 4)
    return t.set_color(color)


def fit_w(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def tick(size=0.22, color=TEAL, sw=6):
    return VMobject(stroke_color=color, stroke_width=sw).set_points_as_corners(
        [[-0.5 * size, 0.0, 0], [-0.12 * size, -0.4 * size, 0], [0.55 * size, 0.45 * size, 0]])


def at_left(mob, x=LEFT_X):
    return mob.align_to(np.array([x, 0, 0]), LEFT)


def header(kicker, headline, on_dark=False):
    k = T(kicker, 34, SOFT_ON_DARK if on_dark else MUTED, MONO)
    h = T(headline, 62, ON_DARK if on_dark else INK, SERIF)
    fit_w(k, RIGHT_X - LEFT_X)
    fit_w(h, RIGHT_X - LEFT_X)
    g = VGroup(k, h).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
    at_left(g).align_to(np.array([0, 3.3, 0]), UP)
    return g


class Clock:
    def __init__(self, scene, bid):
        self.s, self.bid = scene, bid
        self.T = float(BEATS[bid]["actual_duration_s"])
        self.text = BEATS[bid]["narration_text"]
        self.t = 0.0

    def cue(self, phrase, offset=0.0):
        i = self.text.find(phrase)
        if i < 0:
            raise KeyError(f"{self.bid}: cue phrase not in narration: {phrase!r}")
        return min(self.T - 0.5, self.T * i / len(self.text) + offset)

    def at(self, t):
        if t - self.t >= 1 / 24:
            self.s.wait(t - self.t)
            self.t = t

    def play(self, *anims, rt=0.8):
        self.s.play(*anims, run_time=rt)
        self.t += rt

    def end(self):
        rem = self.T - self.t
        if rem >= 1 / 24:
            self.s.wait(rem)
        self.t = self.T


class B10_TheCount(Scene):
    def construct(self):
        c = Clock(self, "B10")
        hd = header("GIT LOG · NOV 15–21", f"9 pieces, {NF} folders")
        rows = SUM["piece_counts_sorted"]
        top, step, full = 1.85, 0.5, RIGHT_X - LEFT_X
        labels, tracks, bars, nums = [], [], [], []
        for i, (piece, n) in enumerate(rows):
            y = top - i * step
            col = ACCENT if piece == "PROOF" else TEAL
            lb = at_left(T(FILE[piece], 34, INK, MONO).move_to([0, y, 0]))
            nm = T(str(n), 40, ACCENT if piece == "PROOF" else INK, SANS, "BOLD").move_to([0, y, 0])
            nm.align_to(np.array([RIGHT_X, 0, 0]), RIGHT)
            ty = y - 0.235
            tr = Rectangle(width=full, height=0.09, fill_color=PANEL, fill_opacity=1, stroke_width=0,
                           stroke_opacity=0).move_to([(LEFT_X + RIGHT_X) / 2, ty, 0])
            b = Rectangle(width=max(full * n / NF, 0.02), height=0.09, fill_color=col, fill_opacity=1,
                          stroke_width=0, stroke_opacity=0).move_to([LEFT_X, ty, 0], aligned_edge=LEFT)
            labels.append(lb); tracks.append(tr); bars.append(b); nums.append(nm)
        self.add(*tracks)
        c.play(FadeIn(hd, shift=0.1 * DOWN), FadeIn(VGroup(*labels)), rt=0.8)
        c.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.1), rt=1.8)
        c.play(LaggedStart(*[FadeIn(n) for n in nums], lag_ratio=0.06), rt=0.9)
        c.at(c.cue("The beat sheet was in", -0.1))
        c.play(Indicate(nums[0], color=INK, scale_factor=1.2), rt=0.8)
        c.at(c.cue("The proof self-review", -0.1))
        c.play(Indicate(nums[-1], color=ACCENT, scale_factor=1.3),
               Indicate(labels[-1], color=ACCENT, scale_factor=1.08), rt=1.0)
        c.end()


class B20_EightOfNine(Scene):
    def construct(self):
        c = Clock(self, "B20")
        hd = header(f"{SUM['folders_at_max_count']} FOLDERS HAD {SUM['max_pieces']} OF 9", "None had all nine")
        folder = "fellows/rohan-v/2026-11-20-how-auto-tune-works"
        have = set(RES["top_folder_pieces"][folder])
        name = VGroup(T("rohan-v/2026-11-20-", 32, MUTED, MONO), T("how-auto-tune-works", 32, INK, MONO))
        name.arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        fit_w(name, RIGHT_X - LEFT_X)
        at_left(name).move_to([name.get_center()[0], 1.75, 0])
        panel = RoundedRectangle(width=3.7, height=4.1, corner_radius=0.14,
                                 fill_color=PANEL, fill_opacity=1, stroke_width=0, stroke_opacity=0)
        panel.move_to([-0.13, -0.78, 0])      # inside the 5% title-safe band (x >= -2.0)
        rows = []
        for j, piece in enumerate(ORDER):
            ok = piece in have
            y = 1.0 - j * 0.44
            mark = tick(0.22, TEAL) if ok else Square(0.22, stroke_color=ACCENT, stroke_width=5)
            mark.move_to([LEFT_X + 0.25, y, 0])
            lab = T(piece.replace(" log", " log"), 39, INK if ok else ACCENT, SANS,
                    "NORMAL" if ok else "BOLD")
            lab.move_to([0, y, 0]).align_to(np.array([LEFT_X + 0.52, 0, 0]), LEFT)
            rows.append((VGroup(mark, lab), ok))
        self.add(panel)
        c.play(FadeIn(hd, shift=0.1 * DOWN), rt=0.7)
        c.at(c.cue("like how-auto-tune-works", -0.3))
        c.play(FadeIn(name), rt=0.5)
        c.at(c.cue("It has the README", -0.1))
        c.play(LaggedStart(*[FadeIn(r) for r, ok in rows if ok], lag_ratio=0.15), rt=2.4)
        c.at(c.cue("Its one gap", -0.1))
        c.play(*[FadeIn(r, scale=1.2) for r, ok in rows if not ok], rt=0.7)
        c.end()


class B30_Takeaway(Scene):
    def construct(self):
        c = Clock(self, "B30")
        self.camera.background_color = DARK
        hd = header("TAKEAWAY", "Check for nine names", on_dark=True)
        hot = {"PROOF", "description"}
        items = []
        for j, piece in enumerate(ORDER):
            y = 1.75 - j * 0.47
            box = Square(0.3, stroke_color=GHOST_DARK, stroke_width=4).move_to([LEFT_X + 0.17, y, 0])
            tk = tick(0.26, ON_DARK, 7).move_to([LEFT_X + 0.19, y + 0.01, 0])
            is_hot = piece in hot
            lab = T(FILE[piece], 34, DARK if is_hot else ON_DARK, MONO, "BOLD" if is_hot else "NORMAL")
            lab.move_to([0, y, 0]).align_to(np.array([LEFT_X + 0.55, 0, 0]), LEFT)
            plain = lab.copy().set_color(ON_DARK)
            chip = None
            if is_hot:
                chip = RoundedRectangle(width=lab.width + 0.2, height=0.4, corner_radius=0.08,
                                        fill_color=ON_DARK, fill_opacity=1, stroke_width=0,
                                        stroke_opacity=0).move_to(lab)
            items.append((box, tk, lab, plain, chip))
        self.add(*[it[0] for it in items])
        c.play(FadeIn(hd, shift=0.1 * DOWN), *[FadeIn(it[3]) for it in items], rt=0.7)
        c.at(c.cue("check your folder", -0.2))
        c.play(LaggedStart(*[Create(it[1]) for it in items], lag_ratio=0.1), rt=1.4)
        c.at(c.cue("start with the two", -0.1))
        anims = []
        for box, tk, lab, plain, chip in items:
            if chip is not None:
                anims += [FadeIn(chip), FadeOut(plain), FadeIn(lab)]
        c.play(*anims, rt=0.7)
        c.end()


class B90_Outro(Scene):
    def construct(self):
        c = Clock(self, "B90")
        title = VGroup(T("What a Finished", 60, INK, SERIF), T("Folder Looks Like", 60, INK, SERIF))
        title.arrange(DOWN, buff=0.06)
        fit_w(title, RIGHT_X - LEFT_X).move_to([-0.15, 2.75, 0])
        pill_t = T("SUBSCRIBE", 44, ON_DARK, SANS, "BOLD")
        pill = RoundedRectangle(width=pill_t.width + 0.6, height=0.58, corner_radius=0.29,
                                fill_color=ACCENT, fill_opacity=1, stroke_width=0, stroke_opacity=0)
        pill_t.move_to(pill)
        sub = VGroup(pill, pill_t).move_to([-0.15, 1.62, 0])
        logo = SVGMobject(str(_LOGO_HAI)).set_fill(INK, 1).set_stroke(width=0, opacity=0)
        logo.scale_to_fit_height(0.62).move_to([-0.15, 0.82, 0])
        handle = T("@HumanitariansAI", 42, INK, SANS, "BOLD")
        fit_w(handle, RIGHT_X - LEFT_X).move_to([-0.15, 0.17, 0])
        credit = VGroup(*[T(x, 34, INK) for x in ("Boopesh M.", "Humanitarians AI Fellow", "Brutalist team")])
        credit.arrange(DOWN, buff=0.07)
        fit_w(credit, RIGHT_X - LEFT_X).move_to([-0.15, -0.66, 0])
        small = VGroup(*[T(x, 32, MUTED) for x in ("Narration: AI voice", "(Kokoro am_onyx)",
                                                     "Data: git log,", f"main @ {RES['ref'][:8]}")])
        small.arrange(DOWN, buff=0.06)
        fit_w(small, RIGHT_X - LEFT_X).move_to([-0.15, -1.93, 0])
        c.play(FadeIn(title, shift=0.1 * DOWN), FadeIn(logo), FadeIn(handle), rt=0.7)
        c.play(FadeIn(sub, scale=0.9), FadeIn(credit), FadeIn(small), rt=0.7)
        c.at(c.cue("please subscribe", -0.3))
        c.play(sub.animate.scale(1.08), rt=0.35)
        c.play(sub.animate.scale(1 / 1.08), rt=0.35)
        c.end()


_TK = Path(os.environ.get("BRUTALIST_HOME", "/home/user/nikbearbrown/brutalist.art"))
_LOGO_HAI = _TK / "logos" / "humanitarians" / "humanitarians-logo-1.svg"
