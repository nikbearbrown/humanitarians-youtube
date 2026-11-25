"""scenes.py -- Manim beats for "What a Finished Folder Looks Like" (16:9, 3840x2160).

One Scene per Manim beat; the class prefix before the underscore is the beat id
(run.sh discovers `class B10_*(Scene)` and slots the render into manim/B10.mp4).
Every number on screen is read from code/results.json (code/week_stats.py).
Beat length and cue times come from beat_sheet.json: the measured Kokoro audio
(actual_duration_s) is the clock, and a cue lands where its phrase sits in the
narration (character position x beat length).
House look: cream ground, mono kicker over a serif headline at top-left, PANEL
cards, teal data, ACCENT only for the number that matters, one dark takeaway.
"""
import json
import os
from pathlib import Path

import numpy as np
from manim import *

# ---------------------------------------------------------------- data ------
_CANDIDATES = [Path(__file__).resolve().parent, Path.cwd(),
               Path(os.environ.get("FOLDER_REEL", "/nonexistent")),
               Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/"
                    "2026-11-22-what-a-finished-folder-looks-like")]
REEL = next(p for p in _CANDIDATES if (p / "code" / "results.json").is_file())
RES = json.loads((REEL / "code" / "results.json").read_text())
SHEET = json.loads((REEL / "beat_sheet.json").read_text())
BEATS = {b["beat_id"]: b for b in SHEET["beats"]}
SUM, TW, LW = RES["summary"], RES["this_week"], RES["last_week_recount"]
PUB, LATE = RES["last_week_published"], RES["late_merge_check"]
PC = {lab: n for lab, n in SUM["piece_counts_sorted"]}
NF = TW["new_work_folders"]

# --------------------------------------------------------------- palette ----
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

# piece label -> file name shown on screen
FILE = {"README": "README.md", "FACTCHECK": "FACTCHECK.md", "FRICTIONAL log": "FRICTIONAL.md",
        "PROOF": "PROOF.md", "SHOTLIST": "SHOTLIST.md", "PROMPTS": "PROMPTS.md",
        "beat sheet": "beat_sheet.json", "code": "code/", "description": "description.txt"}
ORDER = ["README", "FACTCHECK", "FRICTIONAL log", "PROOF", "SHOTLIST", "PROMPTS",
         "beat sheet", "code", "description"]


# --------------------------------------------------------------- helpers ----
def T(text, size=30, color=INK, font=SANS, weight="NORMAL"):
    """Text built 2x large then scaled down (clean glyph spacing); size = effective.
    Not 4x: at 4x Pango silently wraps lines wider than ~10 units, which inflates the
    box the layout audit reads. Colour is applied after construction: passing color= to
    Text inflated its bounding box too (1.80 vs 0.64 units for the outro title)."""
    t = Text(text, font=font, font_size=size * 2, weight=weight).scale(0.5)
    return t.set_color(color)


def fit_w(mob, max_w):
    if mob.width > max_w:
        mob.scale_to_fit_width(max_w)
    return mob


def card(w, h, fill=PANEL, r=0.16):
    return RoundedRectangle(width=w, height=h, corner_radius=r, fill_color=fill,
                            fill_opacity=1, stroke_width=0, stroke_opacity=0)


def ghost(w, h, color=GHOST, r=0.16, sw=2.5):
    return RoundedRectangle(width=w, height=h, corner_radius=r, stroke_color=color,
                            stroke_width=sw, fill_opacity=0)


def bar(w, h, color=TEAL):
    return Rectangle(width=max(w, 0.02), height=h, fill_color=color, fill_opacity=1,
                     stroke_width=0, stroke_opacity=0)


def tick(size=0.26, color=TEAL, sw=7):
    return VMobject(stroke_color=color, stroke_width=sw).set_points_as_corners(
        [[-0.5 * size, 0.0, 0], [-0.12 * size, -0.4 * size, 0], [0.55 * size, 0.45 * size, 0]])


def header(kicker, headline, on_dark=False):
    k = T(kicker, 26, SOFT_ON_DARK if on_dark else MUTED, MONO)
    h = T(headline, 54, ON_DARK if on_dark else INK, SERIF)
    g = VGroup(k, h).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
    g.to_corner(UL, buff=0.85)
    return g


class Clock:
    """Beat clock: length = measured narration; cue(phrase) = that phrase's share of the text."""

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


# ----------------------------------------------------------------- beats ----
class B10_TheWeek(Scene):
    def construct(self):
        c = Clock(self, "B10")
        hd = header("GIT LOG · NOV 15–21 · MAIN", "One week on main")
        stats = [(TW["merged_prs"], "merged PRs", TEAL),
                 (NF, "new work folders", ACCENT),
                 (TW["fellows"], "fellows", TEAL)]
        xs = [-4.2, 0.0, 4.2]
        ghosts, fills, nums, labs = [], [], [], []
        for (n, lab, col), x in zip(stats, xs):
            g = ghost(3.9, 3.0).move_to([x, -0.1, 0])
            f = card(3.9, 3.0).move_to([x, -0.1, 0])
            num = T(str(n), 120, col, SERIF).move_to([x, 0.35, 0])
            lb = T(lab, 30, INK).move_to([x, -0.95, 0])
            ghosts.append(g); fills.append(f); nums.append(num); labs.append(lb)
        m1 = T("Window: Sun Nov 15 00:00 to Sat Nov 21 23:59:59, America/New_York", 28, MUTED)
        m2 = T("PR = “Merge pull request #N” on main’s first-parent line, or a squash merge", 28, MUTED)
        meth = VGroup(m1, m2).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        fit_w(meth, 12.4).move_to([0, -2.55, 0]).align_to(hd, LEFT)
        self.add(*ghosts)
        c.play(FadeIn(hd, shift=0.1 * DOWN), FadeIn(meth), rt=0.8)
        for i, phrase in enumerate(["eighteen pull", "fifty-four new", "from nineteen"]):
            c.at(c.cue(phrase, -0.2))
            c.play(FadeIn(fills[i]), FadeIn(nums[i], scale=0.8), FadeIn(labs[i]), rt=0.6)
            self.bring_to_front(nums[i], labs[i])
        c.at(c.cue("Each folder is one piece"))
        c.play(Indicate(nums[1], color=ACCENT, scale_factor=1.08), rt=0.8)
        c.end()


class B20_NinePieces(Scene):
    def construct(self):
        c = Clock(self, "B20")
        hd = header("THE CHECKLIST · 9 PIECES · MATCHED BY FILE NAME", "What a finished folder holds")
        caps = {"README": "what it is", "FACTCHECK": "claims checked",
                "FRICTIONAL log": "what got in the way", "PROOF": "a self-review",
                "SHOTLIST": "every shot planned", "PROMPTS": "the prompts used",
                "beat sheet": "every beat, timed", "code": "behind the numbers",
                "description": "the upload text"}
        cues = {"README": "a README", "FACTCHECK": "a fact-check", "FRICTIONAL log": "a frictional log",
                "PROOF": "a proof self-review", "SHOTLIST": "a shot list", "PROMPTS": "the prompts",
                "beat sheet": "the beat sheet", "code": "the code behind", "description": "an upload description"}
        W, H = 3.95, 1.4
        xs, ys = [-4.2, 0.0, 4.2], [0.95, -0.67, -2.29]
        cells = []
        for i, piece in enumerate(ORDER):
            x, y = xs[i % 3], ys[i // 3]
            g = ghost(W, H).move_to([x, y, 0])
            f = card(W, H).move_to([x, y, 0])
            name = T(FILE[piece], 28, INK, MONO)
            cap = T(caps[piece], 26, MUTED)
            txt = VGroup(name, cap).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
            fit_w(txt, W - 0.5).move_to([x, y, 0]).align_to(f, LEFT).shift(0.28 * RIGHT)
            strip = bar(0.1, H - 0.36, TEAL).move_to([x - W / 2 + 0.13, y, 0])
            cells.append((piece, g, f, txt, strip))
        self.add(*[cl[1] for cl in cells])
        c.play(FadeIn(hd, shift=0.1 * DOWN), rt=0.7)
        for piece, g, f, txt, strip in cells:
            c.at(c.cue(cues[piece], -0.1))
            c.play(FadeIn(f), FadeIn(strip), FadeIn(txt, shift=0.08 * UP), rt=0.45)
        c.at(c.cue("My script checked"))
        c.play(LaggedStart(*[Indicate(cl[4], color=TEAL, scale_factor=1.15) for cl in cells],
                           lag_ratio=0.1), rt=1.4)
        c.end()


class B30_TheCount(Scene):
    def construct(self):
        c = Clock(self, "B30")
        hd = header(f"THE COUNT · {NF} NEW WORK FOLDERS", "Which pieces show up")
        rows = SUM["piece_counts_sorted"]          # sorted most -> least
        x0, full = -2.35, 7.6                       # bar origin, width of 54/54
        top, step = 1.45, 0.555
        labels, tracks, bars, nums = [], [], [], []
        for i, (piece, n) in enumerate(rows):
            y = top - i * step
            col = ACCENT if piece == "PROOF" else TEAL
            lb = T(FILE[piece], 28, INK, MONO)
            lb.move_to([0, y, 0]).align_to(np.array([x0 - 0.3, 0, 0]), RIGHT)
            tr = Rectangle(width=full, height=0.36, fill_color=PANEL, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to([x0 + full / 2, y, 0])
            b = bar(full * n / NF, 0.36, col).move_to([x0, y, 0], aligned_edge=LEFT)
            nm = T(str(n), 30, ACCENT if piece == "PROOF" else INK, SANS, "BOLD")
            nm.move_to([x0 + full * n / NF + 0.38, y, 0])
            labels.append(lb); tracks.append(tr); bars.append(b); nums.append(nm)
        ax = T(f"of {NF}", 28, MUTED).move_to([x0 + full - 0.45, top + 0.55, 0])
        self.add(*tracks)
        c.play(FadeIn(hd, shift=0.1 * DOWN), FadeIn(VGroup(*labels)), FadeIn(ax), rt=0.8)
        c.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.12), rt=2.2)
        c.play(LaggedStart(*[FadeIn(n) for n in nums], lag_ratio=0.08), rt=1.0)
        c.at(c.cue("At the bottom", -0.2))
        c.play(Indicate(nums[-1], color=ACCENT, scale_factor=1.25),
               Indicate(labels[-1], color=ACCENT, scale_factor=1.06), rt=1.0)
        c.end()


class B40_EightOfNine(Scene):
    def construct(self):
        c = Clock(self, "B40")
        hd = header(f"PIECES PER FOLDER · 2 OF THE {SUM['folders_at_max_count']} FOLDERS WITH "
                    f"{SUM['max_pieces']} OF 9", "What eight of nine looks like")
        examples = [("rohan-v/", "2026-11-20-", ["how-auto-tune-works"]),
                    ("likhith-r/", "2026-11-14-", ["word2vec-king-man-", "woman-queen"])]
        pieces = RES["top_folder_pieces"]
        xs = [-3.15, 3.15]
        W, H, cy = 6.1, 4.15, -0.35
        groups = []
        for (fellow, date, slug), x in zip(examples, xs):
            have = set(pieces["fellows/" + fellow + date + "".join(slug)])
            g = ghost(W, H).move_to([x, cy, 0])
            f = card(W, H).move_to([x, cy, 0])
            name = VGroup(T(fellow + date, 28, MUTED, MONO), *[T(part, 28, INK, MONO) for part in slug])
            name.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            fit_w(name, W - 0.6)
            name.align_to(f, LEFT).shift(0.3 * RIGHT).align_to(f, UP).shift(0.22 * DOWN)
            items = []
            for j, piece in enumerate(ORDER):
                ok = piece in have
                lab = T(piece.replace(" log", ""), 26, INK if ok else ACCENT, SANS,
                        "NORMAL" if ok else "BOLD")
                mark = tick(0.26, TEAL) if ok else Square(0.26, stroke_color=ACCENT, stroke_width=5)
                row = VGroup(mark, lab).arrange(RIGHT, buff=0.18)
                col, r = j // 5, j % 5
                row.move_to([0, cy + 0.28 - r * 0.47, 0]).align_to(
                    np.array([x - W / 2 + 0.35 + col * 3.05, 0, 0]), LEFT)
                items.append((row, ok))
            groups.append((g, f, name, items))
        stat = T(f"No folder had all 9  ·  {SUM['folders_at_max_count']} folders had 8  ·  "
                 f"all {SUM['folders_at_max_count']} lack only PROOF.md", 30, INK)
        fit_w(stat, 12.4).move_to([0, -2.95, 0])
        self.add(*[gr[0] for gr in groups])
        c.play(FadeIn(hd, shift=0.1 * DOWN), FadeIn(stat), rt=0.8)
        for i, phrase in enumerate(["like how-auto-tune-works", "word-two-vec"]):
            g, f, name, items = groups[i]
            c.at(c.cue(phrase, -0.2))
            c.play(FadeIn(f), FadeIn(name), rt=0.5)
        c.at(c.cue("Each holds", -0.1))
        for g, f, name, items in groups:
            self.bring_to_front(name)
        c.play(*[FadeIn(row) for _, _, _, items in groups for row, ok in items if ok], rt=1.2)
        c.at(c.cue("The one gap", -0.1))
        c.play(*[FadeIn(row, scale=1.15) for _, _, _, items in groups for row, ok in items if not ok], rt=0.8)
        c.end()


class B50_LastWeek(Scene):
    def construct(self):
        c = Clock(self, "B50")
        hd = header("ONE COMPARISON · SAME CODE, BOTH WEEKS", "The week before, recounted")
        rows = [("merged pull requests", LW["merged_prs"], TW["merged_prs"]),
                ("new work folders", LW["new_work_folders"], NF),
                ("with a frictional log", LW["frictional_logs"], TW["frictional_logs"])]
        xa, xb, xl = 1.35, 4.75, -6.26
        ha = T("Nov 8–14 (recount)", 30, MUTED).move_to([xa, 1.45, 0])
        hb = T("Nov 15–21", 30, MUTED).move_to([xb, 1.45, 0])
        rule = Line([xl, 1.05, 0], [6.26, 1.05, 0], stroke_color=GHOST, stroke_width=2)
        objs = []
        for i, (lab, a, b) in enumerate(rows):
            y = 0.55 - i * 0.85
            last = i == 2
            l = T(lab, 34, INK).move_to([0, y, 0]).align_to(np.array([xl, 0, 0]), LEFT)
            na = T(str(a), 66, INK, SERIF).move_to([xa, y, 0])
            arrow = Arrow([xa + 0.8, y, 0], [xb - 0.8, y, 0], buff=0, stroke_width=5,
                          color=GHOST, max_tip_length_to_length_ratio=0.25)
            nb = T(str(b), 66, ACCENT if last else TEAL, SERIF).move_to([xb, y, 0])
            objs.append((l, na, arrow, nb))
        f1 = T(f"Published last week: {PUB['merged_prs']} PRs · {PUB['new_work_folders']} folders · "
               f"{PUB['frictional_logs']} logs. The recount differs:", 28, MUTED)
        f2 = T(f"PR #{LW['latest_pr']['number']} merged Sat Nov 14, 9:42 pm, after that count;", 28, MUTED)
        f3 = T("this code also skips undated folders (hours, renewals).", 28, MUTED)
        foot = VGroup(f1, f2, f3).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        fit_w(foot, 12.5).move_to([0, -2.5, 0]).align_to(np.array([xl, 0, 0]), LEFT)
        self.add(rule)
        c.play(FadeIn(hd, shift=0.1 * DOWN), FadeIn(ha), FadeIn(hb),
               *[FadeIn(o[0]) for o in objs], *[FadeIn(o[3]) for o in objs], rt=0.8)
        c.at(c.cue("twenty pull", -0.3))
        c.play(*[FadeIn(o[1], shift=0.15 * RIGHT) for o in objs], rt=0.6)
        c.play(*[GrowArrow(o[2]) for o in objs], rt=0.6)
        c.at(c.cue("We published", -0.2))
        c.play(FadeIn(foot), rt=0.8)
        c.at(c.cue("This week:", -0.2))
        c.play(Indicate(objs[2][3], color=ACCENT, scale_factor=1.2), rt=0.9)
        c.end()


class B60_MyWeek(Scene):
    def construct(self):
        c = Clock(self, "B60")
        hd = header("BOOPESH M. · MY WEEK", "Delivered, pending, rebuilt")
        vids = [("What Got in the Way", ["progress video", "2:21  +  Short 0:49  ·  4K"]),
                ("Why Did the AI Say No?", ["AI credit explainability", "2:27  +  Short 0:46  ·  4K"])]
        lw_, lh = 6.0, 2.4
        cards_ = []
        for i, (title, meta) in enumerate(vids):
            y = 0.62 - i * 2.48
            f = card(lw_, lh).move_to([-3.26, y, 0])
            t = T(title, 40, INK, SERIF)
            m = VGroup(*[T(line, 28, MUTED) for line in meta]).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            chip_t = T("delivered for review", 28, ON_DARK, SANS, "BOLD")
            chip = RoundedRectangle(width=chip_t.width + 0.4, height=0.48, corner_radius=0.24,
                                    fill_color=TEAL, fill_opacity=1, stroke_width=0, stroke_opacity=0)
            chip_t.move_to(chip)
            body = VGroup(t, m, VGroup(chip, chip_t)).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
            fit_w(body, lw_ - 0.6).move_to(f).align_to(f, LEFT).shift(0.3 * RIGHT)
            cards_.append(VGroup(f, body))
        logo = ImageMobject(str(_LOGO_GITHUB)).scale_to_fit_height(0.6)
        pr_t = T("Pull request: pending", 34, INK, SANS, "BOLD")
        pr_head = Group(logo, pr_t).arrange(RIGHT, buff=0.25)
        pr_sub = T("the fork attempt failed;\nfellows/boopesh-m is not\non main as of Nov 22", 28, MUTED)
        pr = Group(pr_head, pr_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        pr.move_to([3.3, 0.72, 0]).align_to(np.array([0.55, 0, 0]), LEFT)
        fr_head = T("Friction this week", 34, ACCENT, SANS, "BOLD")
        fr_sub = T("build machine wiped;\ntoolkit rebuilt from\nits own ./setup\nbefore rendering", 28, INK)
        fr = VGroup(fr_head, fr_sub).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        fr.move_to([3.3, -2.05, 0]).align_to(np.array([0.55, 0, 0]), LEFT)
        divider = Line([0.2, 1.75, 0], [0.2, -3.1, 0], stroke_color=GHOST, stroke_width=2)
        g1, g2 = ghost(lw_, lh).move_to(cards_[0][0]), ghost(lw_, lh).move_to(cards_[1][0])
        self.add(g1, g2, divider)
        c.play(FadeIn(hd, shift=0.1 * DOWN), FadeIn(pr_head), FadeIn(fr_head), rt=0.7)
        c.at(c.cue("What Got in the Way", -0.2))
        c.play(FadeIn(cards_[0]), rt=0.6)
        c.at(c.cue("Why Did the AI", -0.2))
        c.play(FadeIn(cards_[1]), rt=0.6)
        c.at(c.cue("My pull request", -0.2))
        c.play(FadeIn(pr_sub), rt=0.7)
        c.at(c.cue("And this week", -0.2))
        c.play(FadeIn(fr_sub), rt=0.7)
        c.end()


class B70_Takeaway(Scene):
    def construct(self):
        c = Clock(self, "B70")
        self.camera.background_color = DARK
        hd = header("TAKEAWAY · A CHECKLIST", "Before you open a pull request", on_dark=True)
        start_here = {"PROOF", "description"}
        xs, ys = [-6.25, -1.98, 2.12], [0.95, -0.2, -1.35]
        boxes, ticks_, labels, chips = [], [], [], []
        for i, piece in enumerate(ORDER):
            x, y = xs[i % 3], ys[i // 3]
            box = Square(0.42, stroke_color=GHOST_DARK, stroke_width=4).move_to([x + 0.21, y, 0])
            tk = tick(0.34, ON_DARK, 8).move_to([x + 0.23, y + 0.02, 0])
            hot = piece in start_here
            lab = T(FILE[piece], 27, DARK if hot else ON_DARK, MONO, "BOLD" if hot else "NORMAL")
            lab.move_to([0, y, 0]).align_to(np.array([x + 0.68, 0, 0]), LEFT)
            chip = None
            if hot:
                chip = RoundedRectangle(width=lab.width + 0.24, height=0.56, corner_radius=0.12,
                                        fill_color=ON_DARK, fill_opacity=1, stroke_width=0,
                                        stroke_opacity=0).move_to(lab)
            boxes.append(box); ticks_.append(tk); labels.append(lab); chips.append(chip)
        bottom = T("A folder with all nine shows the work, the checks and the friction,", 32, ON_DARK)
        bottom2 = T("not just the video.", 32, ON_DARK)
        bl = VGroup(bottom, bottom2).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        fit_w(bl, 12.4).move_to([0, -2.75, 0]).align_to(np.array([-6.25, 0, 0]), LEFT)
        plain = [lab.copy().set_color(ON_DARK) for lab in labels]
        self.add(*boxes)
        c.play(FadeIn(hd, shift=0.1 * DOWN), *[FadeIn(p) for p in plain], rt=0.8)
        c.at(c.cue("check your folder", -0.2))
        c.play(LaggedStart(*[Create(t) for t in ticks_], lag_ratio=0.12), rt=1.6)
        c.at(c.cue("Start with the two", -0.1))
        anims = []
        for p, lab, chip in zip(plain, labels, chips):
            if chip is not None:
                anims += [FadeIn(chip), FadeOut(p), FadeIn(lab)]
        c.play(*anims, rt=0.7)
        c.at(c.cue("A folder with all nine", -0.2))
        c.play(FadeIn(bl, shift=0.1 * UP), rt=0.8)
        c.end()


class B90_Outro(Scene):
    def construct(self):
        c = Clock(self, "B90")
        title = T(SHEET["metadata"]["title"], 64, INK, SERIF).move_to([0, 2.55, 0])
        pill_t = T("SUBSCRIBE", 36, ON_DARK, SANS, "BOLD")
        pill = RoundedRectangle(width=pill_t.width + 0.9, height=0.8, corner_radius=0.4,
                                fill_color=ACCENT, fill_opacity=1, stroke_width=0, stroke_opacity=0)
        pill_t.move_to(pill)
        sub = VGroup(pill, pill_t).move_to([0, 1.35, 0])
        logo = SVGMobject(str(_LOGO_HAI)).set_fill(INK, 1).set_stroke(width=0, opacity=0)
        logo.scale_to_fit_height(1.0)
        handle = T("@HumanitariansAI", 44, INK, SANS, "BOLD")
        brand = VGroup(logo, handle).arrange(RIGHT, buff=0.35).move_to([0, 0.0, 0])
        cr = T("Boopesh M. · Humanitarians AI Fellow · Brutalist team", 32, INK).move_to([0, -1.2, 0])
        nar = T("Narration: AI voice (Kokoro am_onyx)", 28, MUTED).move_to([0, -1.8, 0])
        d1 = T(f"Data: humanitarians-youtube git history, main @ {RES['ref'][:8]}", 28, MUTED)
        d2 = T("Nov 15–21, 2026, America/New_York · code/week_stats.py", 28, MUTED)
        data = VGroup(d1, d2).arrange(DOWN, buff=0.12).move_to([0, -2.75, 0])
        c.play(FadeIn(title, shift=0.1 * DOWN), FadeIn(brand), rt=0.8)
        c.play(FadeIn(sub, scale=0.9), FadeIn(cr), FadeIn(nar), FadeIn(data), rt=0.8)
        c.at(c.cue("please subscribe", -0.3))
        c.play(sub.animate.scale(1.08), rt=0.4)
        c.play(sub.animate.scale(1 / 1.08), rt=0.4)
        c.end()


_TK = Path(os.environ.get("BRUTALIST_HOME", "/home/user/nikbearbrown/brutalist.art"))
_LOGO_GITHUB = _TK / "icons" / "logos" / "github" / "github-01.png"
_LOGO_HAI = _TK / "logos" / "humanitarians" / "humanitarians-logo-1.svg"
