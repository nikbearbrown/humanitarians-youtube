# -*- coding: utf-8 -*-
"""
Manim scenes for "What the Fellows Taught" (16:9, 3840x2160) -- Boopesh M., week of Nov 1-7 2026.
  B20_Folders     -- the 74 new work folders as squares, coloured by kind; dated this week vs older
  B30_Subjects    -- the 50 topic videos by subject (rough keyword sort), with how many fellows
  B40_Titles      -- six real titles dated this week (folder names only)
  B50_Compare     -- one comparison with last week, same script and definitions
  B60_MyPart      -- Boopesh's two videos last week; delivered for review, GitHub PR pending
  B70_Takeaway    -- dark card: teach one idea (idea, example, where it breaks)
  B90_Outro       -- @HumanitariansAI outro + fellow credit
Every number is read from code/results.json (python3 code/week_stats.py). Each scene lands
exactly on its beat's measured narration length.
"""
import json
from pathlib import Path

from manim import *

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"
CODE = HERE / "code"
if not (CODE / "results.json").exists():   # isolated copies (static pre-flight) fall back to the reel's data
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-08-what-the-fellows-taught/code")
    ASSETS = CODE.parent / "assets"

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"   # terracotta, WCAG 4.5:1+ on cream and panel
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"     # data
TEAL2 = "#4F7A88"
GOOD = "#3F6E4E"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
DIM_DARK = "#5E544C"
HOT_DARK = "#E08A6A"
SOFT_DARK = "#D8D0C0"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

RES = json.loads((CODE / "results.json").read_text())
TW = RES["this_week"]
FD = TW["folders"]
CMP = RES["comparison"]


def _sheet():
    try:
        return {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}
    except Exception:
        return {}


BEATS = _sheet()


def beat_len(bid, default=12.0):
    b = BEATS.get(bid, {})
    return float(b.get("render_duration_s") or b.get("actual_duration_s") or default)


def cue(bid, phrase, default):
    """Seconds into the beat when `phrase` is spoken (share of characters + lead silence)."""
    b = BEATS.get(bid)
    if not b:
        return default
    text = b["narration_text"]
    i = text.find(phrase)
    if i < 0:
        return default
    lead = float(b.get("lead_silence_s") or 0)
    return lead + (beat_len(bid) - lead) * i / len(text)


class Clock:
    """Schedules a scene's animations against narration cues and ends it on the beat length."""

    def __init__(self, scene, bid):
        self.scene, self.bid, self.t = scene, bid, 0.0
        scene.camera.background_color = BG

    def play_at(self, at, *anims, run_time=0.8, **kw):
        if at > self.t:
            self.scene.wait(at - self.t)
            self.t = at
        self.scene.play(*anims, run_time=run_time, **kw)
        self.t += run_time

    def finish(self):
        end = beat_len(self.bid)
        if end - self.t > 1 / 24:
            self.scene.wait(end - self.t)


SAFE_W = 12.6


def t(s, size=40, color=INK, font=SANS, weight="NORMAL", **kw):
    return Text(s, font=font, font_size=size, color=color, weight=weight, **kw)


def fit(m, w=SAFE_W):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def logo(name, height):
    m = SVGMobject(str(ASSETS / name))
    m.scale_to_fit_height(height)
    return m


def png(name, height):
    m = ImageMobject(str(ASSETS / name))
    m.scale_to_fit_height(height)
    return m


def header(kicker, title):
    k = t(kicker.upper(), 22, MUTED, MONO)
    h = t(title, 58, INK, SERIF, weight="BOLD")
    g = VGroup(k, h).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    g.to_corner(UL, buff=0.85)
    return g


def card(w, h, fill=PANEL):
    return RoundedRectangle(width=w, height=h, corner_radius=0.12, fill_color=fill,
                            fill_opacity=1, stroke_width=0)


def ghost_of(m, color=GHOST, width=3):
    return m.copy().set_fill(opacity=0).set_stroke(color, width)


# ======================================================================== B20 =
class B20_Folders(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header(f"new folders under fellows/ · Nov 1–7 · {FD['fellows_with_new_folders']} fellows",
                    f"{FD['new_work_folders']} new work folders")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        K = FD["kinds"]
        n_stem, n_prog, n_hours = K["STEM / explainer video"], K["progress / work video"], K["hours log"]
        total = FD["new_work_folders"]
        assert n_stem + n_prog + n_hours == total
        cols, sq, step = 10, 0.42, 0.52
        rows = -(-total // cols)
        x0, y0 = -6.05 + sq / 2, 1.35 - sq / 2
        cells = VGroup(*[Square(sq, stroke_width=0, fill_opacity=1)
                         .move_to([x0 + (i % cols) * step, y0 - (i // cols) * step, 0]) for i in range(total)])
        colours = [TEAL] * n_stem + [ACCENT] * n_prog + [MUTED] * n_hours
        for c, col in zip(cells, colours):
            c.set_fill(col)
        ghosts = VGroup(*[Square(sq, stroke_color=GHOST, stroke_width=2).move_to(c) for c in cells])
        stem_cells, prog_cells, hours_cells = cells[:n_stem], cells[n_stem:n_stem + n_prog], cells[n_stem + n_prog:]

        # right column: legend with big numbers
        RX = 0.4

        def leg(n, lab, col):
            sw = Square(0.36, fill_color=col, fill_opacity=1, stroke_width=0)
            num = t(str(n), 64, col, SERIF, weight="BOLD")
            lb = t(lab, 28, INK)
            g = VGroup(sw, num, lb).arrange(RIGHT, buff=0.25)
            return g

        legs = VGroup(leg(n_stem, "STEM explainer videos", TEAL), leg(n_prog, "progress videos", ACCENT),
                      leg(n_hours, "hours log", MUTED)).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        fit(legs, 5.3)
        legs.move_to([RX, 1.3 - legs.height / 2, 0], aligned_edge=LEFT).align_to([RX, 0, 0], LEFT)
        rough = t("my rough sort: folder name + README", 20, MUTED).next_to(legs, UP, buff=0.12, aligned_edge=LEFT)

        # dated strip
        parts = [(FD["dated_inside_the_week"], "dated this week", INK),
                 (FD["dated_earlier_added_this_week"], "older work, filed this week", "#8C8578"),
                 (FD["undated_new_folders"], "", LINE)]
        SX, SW, SY = RX, 5.0, -1.45
        strip = VGroup()
        x = SX
        for n, _, col in parts:
            w = SW * n / total
            r = Rectangle(width=w, height=0.5, fill_color=col, fill_opacity=1, stroke_color=BG, stroke_width=3)
            r.move_to([x + w / 2, SY, 0])
            strip.add(r)
            x += w
        def slab(n, lab, col):
            sw = Square(0.26, fill_color=col, fill_opacity=1, stroke_width=0)
            g = VGroup(sw, t(str(n), 38, INK, SERIF, weight="BOLD"), t(lab, 22, INK)).arrange(RIGHT, buff=0.18)
            return g

        lab1 = slab(parts[0][0], parts[0][1], parts[0][2])
        lab2 = slab(parts[1][0], parts[1][1], parts[1][2])
        VGroup(lab1, lab2).arrange(DOWN, aligned_edge=LEFT, buff=0.08).next_to(strip, DOWN, buff=0.18).align_to(strip, LEFT)
        when = t("when is the work from?", 22, MUTED).next_to(strip, UP, buff=0.15, aligned_edge=LEFT)

        clock.play_at(0.4, FadeIn(ghosts, lag_ratio=0.01), FadeIn(VGroup(*[ghost_of(r) for r in strip])),
                      run_time=0.8)
        clock.play_at(cue("B20", "Seventy-four", 2.0), Indicate(hd[1], color=ACCENT, scale_factor=1.04), run_time=0.6)
        clock.play_at(cue("B20", "my rough sort", 5.0), FadeIn(rough), run_time=0.4)
        clock.play_at(cue("B20", "fifty are", 6.5), FadeIn(stem_cells, lag_ratio=0.02), FadeIn(legs[0], shift=UP * 0.1),
                      run_time=0.9)
        clock.play_at(cue("B20", "twenty-three", 9.0), FadeIn(prog_cells, lag_ratio=0.03), FadeIn(legs[1], shift=UP * 0.1),
                      run_time=0.8)
        clock.play_at(cue("B20", "one is an hours", 11.0), FadeIn(hours_cells), FadeIn(legs[2], shift=UP * 0.1),
                      run_time=0.5)
        clock.play_at(cue("B20", "Twenty-eight", 12.5), FadeIn(when), FadeIn(strip[0]), FadeIn(lab1), run_time=0.6)
        clock.play_at(cue("B20", "Forty-five", 14.5), FadeIn(strip[1:]), FadeIn(lab2), run_time=0.6)
        clock.finish()


# ======================================================================== B30 =
SUBJ_ORDER = [("AI for product managers", "Twelve teach"), ("testing & metrics", "Ten are"),
              ("how AI models work", "Nine explain"), ("making videos with AI", "Eight are"),
              ("software & data tools", "Five cover"), ("other topics", "the last six"),
              ("AI in marketing & business", "the last six")]


class B30_Subjects(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        n_stem = FD["kinds"]["STEM / explainer video"]
        hd = header(f"the {n_stem} topic videos · my rough sort by subject", "What did they teach?")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        S, SF = FD["stem_subjects"], FD["stem_subject_fellows"]
        assert sum(S.values()) == n_stem
        mx = max(S.values())
        L, W = -1.5, 4.7
        rows = VGroup()
        for i, (key, _) in enumerate(SUBJ_ORDER):
            v = S[key]
            y = 1.25 - i * 0.6
            hot = key == "testing & metrics"
            name = t(key, 24, INK, weight="BOLD" if i < 2 else "NORMAL").move_to([L - 0.3, y, 0], aligned_edge=RIGHT)
            bar = Rectangle(width=max(W * v / mx, 0.05), height=0.42, fill_color=ACCENT if hot else TEAL,
                            fill_opacity=1, stroke_width=0).move_to([L, y, 0], aligned_edge=LEFT)
            val = t(str(v), 28, ACCENT if hot else INK, MONO, weight="BOLD").next_to(bar, RIGHT, buff=0.18)
            nf = SF[key]
            who = t("1 fellow" if nf == 1 else f"{nf} fellows", 20, ACCENT if hot else MUTED,
                    weight="BOLD" if hot else "NORMAL")
            who.move_to([L + W + 0.95, y, 0], aligned_edge=LEFT)
            rows.add(VGroup(name, bar, val, who))
        ghosts = VGroup(*[Rectangle(width=W, height=0.42, stroke_color=GHOST, stroke_width=2)
                          .move_to([L, r[1].get_y(), 0], aligned_edge=LEFT) for r in rows])
        colhead = t("from", 18, MUTED).move_to([L + W + 0.95, 1.75, 0], aligned_edge=LEFT)

        clock.play_at(0.4, FadeIn(ghosts), run_time=0.6)
        for i, (key, phrase) in enumerate(SUBJ_ORDER):
            at = cue("B30", phrase, 4.0 + 2.2 * i)
            anims = [GrowFromEdge(rows[i][1], LEFT), FadeIn(rows[i][2]), FadeIn(rows[i][3]), FadeIn(rows[i][0])]
            if i == 0:
                anims.append(FadeIn(colhead))
            clock.play_at(max(at, clock.t), *anims, run_time=0.5)
            if i == 1:
                clock.play_at(max(cue("B30", "six different fellows", 9.0), clock.t),
                              Indicate(rows[1][3], color=ACCENT, scale_factor=1.15), run_time=0.6)
        clock.finish()


# ======================================================================== B40 =
def clean_title(s):
    for pre in ("Weekly STEM Video: ", "Weekly Research Report: ", "Explainer — "):
        s = s.removeprefix(pre)
    s = s.split(" — ")[0]
    return s.rstrip(".")


SUBJ_COL = {"how AI models work": TEAL, "testing & metrics": ACCENT, "software & data tools": TEAL2,
            "AI for product managers": GOOD, "AI in marketing & business": "#6B4E71", "making videos with AI": TEAL}


class B40_Titles(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        hd = header("README titles · dated Nov 1–7 · fellow folder names only", "A few of the titles")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        phrases = ["Mixture of Experts", "Goodhart's Law", "Integration Hell", "Likely False", "RAG Explained",
                   "Be the Sentence"]
        ex = RES["examples"]
        assert len(ex) == 6
        CW, CH = 3.85, 2.0
        cards = VGroup()
        for r in ex:
            c = card(CW, CH)
            tt = clean_title(r["title"])
            title = t(tt, 32, INK, SERIF, weight="BOLD")
            if title.width > CW - 0.4:
                w_ = tt.split()
                half = (len(w_) + 1) // 2
                title = t(" ".join(w_[:half]) + "\n" + " ".join(w_[half:]), 31, INK, SERIF, weight="BOLD",
                          line_spacing=0.85)
            fit(title, CW - 0.4)
            who = t(r["folder"].split("/")[0], 20, MUTED, MONO)
            col = SUBJ_COL.get(r["subject"], TEAL)
            chip = t(r["subject"], 20, col, weight="BOLD")
            fit(chip, CW - 0.4)
            g = VGroup(title, chip, who).arrange(DOWN, buff=0.14).move_to(c)
            cards.add(VGroup(c, g))
        cards.arrange_in_grid(rows=2, cols=3, buff=(0.3, 0.3)).move_to([0, -0.75, 0])

        clock.play_at(0.4, FadeIn(VGroup(*[ghost_of(c[0]) for c in cards])), run_time=0.6)
        for i, ph in enumerate(phrases):
            at = cue("B40", ph, 1.5 + 1.6 * i)
            clock.play_at(max(at, clock.t), FadeIn(cards[i], shift=UP * 0.12), run_time=0.45)
        clock.finish()


# ======================================================================== B50 =
class B50_Compare(Scene):
    def construct(self):
        clock = Clock(self, "B50")
        hd = header("same script, same definitions · Oct 25–31 vs Nov 1–7", "Last week vs this week")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        specs = [("merged_prs", "pull requests\nmerged", "thirty to twenty-six"),
                 ("new_work_folders", "new work\nfolders", "eighty-four to"),
                 ("fellows_with_new_folders", "fellows with\nnew folders", "twenty-two to"),
                 ("frictional_logs_added", "frictional\nlogs", "frictional logs went up")]
        CW, CH = 2.85, 4.0
        cards = VGroup()
        for key, lab, _ in specs:
            a, b = CMP[key]["last_week"], CMP[key]["this_week"]
            up = b > a
            c = card(CW, CH)
            title = t(lab, 24, INK, weight="BOLD", line_spacing=0.9)
            mx = max(a, b)
            H = 1.7
            ba = Rectangle(width=0.7, height=H * a / mx, fill_color=LINE, fill_opacity=1, stroke_width=0)
            bb = Rectangle(width=0.7, height=H * b / mx, fill_color=ACCENT if up else TEAL, fill_opacity=1,
                           stroke_width=0)
            bars = VGroup(ba, bb).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
            va = t(str(a), 30, MUTED, MONO, weight="BOLD").next_to(ba, UP, buff=0.1)
            vb = t(str(b), 34, ACCENT if up else TEAL, MONO, weight="BOLD").next_to(bb, UP, buff=0.1)
            wk = VGroup(t("last", 18, MUTED).next_to(ba, DOWN, buff=0.1), t("this", 18, INK, weight="BOLD").next_to(bb, DOWN, buff=0.1))
            chart = VGroup(bars, va, vb, wk)
            body = VGroup(title, chart).arrange(DOWN, buff=0.35).move_to(c)
            cards.add(VGroup(c, body))
        cards.arrange(RIGHT, buff=0.3).move_to([0, -0.7, 0])
        fit(cards)
        note = t(f"{TW['merged_prs']['total']} pull requests = {TW['merged_prs']['merge_commits']} merge commits "
                 f"+ {TW['merged_prs']['squash_merges']} squash merge", 20, MUTED)
        note.next_to(cards, DOWN, buff=0.16)

        clock.play_at(0.4, FadeIn(VGroup(*[ghost_of(c[0]) for c in cards])), run_time=0.6)
        for i, (_, _, ph) in enumerate(specs):
            c = cards[i]
            title, chart = c[1][0], c[1][1]
            bars, va, vb, wk = chart
            at = cue("B50", ph, 3.0 + 3.0 * i)
            clock.play_at(max(at - 0.3, clock.t), FadeIn(c[0]), FadeIn(title), GrowFromEdge(bars[0], DOWN), FadeIn(va),
                          FadeIn(wk[0]), run_time=0.5)
            clock.play_at(clock.t + 0.25, GrowFromEdge(bars[1], DOWN), FadeIn(vb, scale=1.2), FadeIn(wk[1]),
                          *( [FadeIn(note)] if i == 0 else []), run_time=0.5)
        clock.play_at(clock.t + 0.2, Indicate(cards[3][1][1][2], color=ACCENT, scale_factor=1.25), run_time=0.7)
        clock.finish()


# ======================================================================== B60 =
class B60_MyPart(Scene):
    def construct(self):
        clock = Clock(self, "B60")
        hd = header("Boopesh M. · last week's two videos", "My part")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        D = RES["boopesh"]["last_week_deliveries"]

        def vcard(img, title, kind, lk, vk):
            im = ImageMobject(str(ASSETS / img))
            im.scale_to_fit_width(4.3)
            border = Rectangle(width=im.width, height=im.height, stroke_color=LINE, stroke_width=3).move_to(im)
            tl = VGroup(t(title, 32, INK, SERIF, weight="BOLD"), t(kind, 18, ACCENT, MONO, weight="BOLD"))
            tl.arrange(RIGHT, buff=0.25, aligned_edge=DOWN)
            meta = VGroup(t(f"{D[lk]['mm_ss']} + Short {D[vk]['mm_ss']}", 20, INK, MONO),
                          t(f"{D[lk]['width']}×{D[lk]['height']} + {D[vk]['width']}×{D[vk]['height']}", 18, MUTED, MONO))
            meta.arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            return Group(Group(im, border), tl, meta).arrange(DOWN, aligned_edge=LEFT, buff=0.16)

        a = vcard("lastweek-one-week-of-fellows.png", "One Week of Fellows", "PROGRESS",
                  "landscape/OneWeekOfFellows_BoopeshM.mp4", "vertical/OneWeekOfFellows_BoopeshM.mp4")
        b = vcard("lastweek-fraud-accuracy-trap.png", "The 99.9% Accuracy Trap", "STEM",
                  "landscape/FraudAccuracyTrap_BoopeshM.mp4", "vertical/FraudAccuracyTrap_BoopeshM.mp4")
        pair = Group(a, b).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        pair.move_to([0, 1.84 - pair.height / 2, 0])

        s1 = t("✓ delivered for review", 24, GOOD, weight="BOLD")
        b1 = card(s1.width + 0.6, 0.85).move_to(s1)
        gh = png("github-01.png", 0.5)
        s2 = VGroup(t("pull request", 24, INK, weight="BOLD"), t("pending", 24, ACCENT, weight="BOLD")).arrange(RIGHT, buff=0.2)
        b2 = DashedVMobject(RoundedRectangle(width=s2.width + gh.width + 0.9, height=0.85, corner_radius=0.12,
                                             stroke_color=ACCENT, stroke_width=4), num_dashes=40)
        arrow = Arrow(LEFT, RIGHT, color=INK, stroke_width=5, buff=0).scale(0.5)
        st = Group(VGroup(b1, s1), arrow, Group(b2)).arrange(RIGHT, buff=0.3)
        why = t("fork attempt failed · fellows/boopesh-m not on main · not in these counts", 19, MUTED)
        Group(st, why).arrange(DOWN, buff=0.12).next_to(pair, DOWN, buff=0.22)
        gh.move_to(b2).shift(LEFT * (b2.width / 2 - gh.width / 2 - 0.3))
        s2.next_to(gh, RIGHT, buff=0.2)

        clock.play_at(0.4, FadeIn(ghost_of(Rectangle(width=4.3, height=4.3 * 9 / 16).move_to(a[0]))),
                      FadeIn(ghost_of(Rectangle(width=4.3, height=4.3 * 9 / 16).move_to(b[0]))),
                      FadeIn(ghost_of(b1)), FadeIn(b2.copy().set_stroke(GHOST)), run_time=0.6)
        clock.play_at(cue("B60", "One Week of Fellows", 2.5), FadeIn(a, shift=UP * 0.15), run_time=0.7)
        clock.play_at(cue("B60", "The ninety-nine", 6.5), FadeIn(b, shift=UP * 0.15), run_time=0.7)
        clock.play_at(cue("B60", "all four are 4K", 11.0),
                      Indicate(Group(a[2], b[2]), color=ACCENT, scale_factor=1.05), run_time=0.7)
        clock.play_at(cue("B60", "delivered for review", 13.0), FadeIn(VGroup(b1, s1)), GrowArrow(arrow), run_time=0.6)
        clock.play_at(cue("B60", "still pending", 15.5), Create(b2), FadeIn(gh), FadeIn(s2), run_time=0.7)
        clock.play_at(cue("B60", "my fork attempt", 17.0), FadeIn(why, shift=UP * 0.1), run_time=0.6)
        clock.finish()


# ======================================================================== B70 =
class B70_Takeaway(Scene):
    def construct(self):
        clock = Clock(self, "B70")
        self.camera.background_color = DARK
        stmt = t("Teach one idea.", 84, ON_DARK, SERIF, weight="BOLD")
        fit(stmt, 11.4).move_to(UP * 2.3)
        sub = t("turn a week of work into a lesson:", 30, SOFT_DARK).next_to(stmt, DOWN, buff=0.3)

        steps = [("one idea", "from your week", "Take one idea"), ("one example", "worked through", "one worked example"),
                 ("one limit", "where it breaks", "where it breaks")]
        boxes = VGroup()
        for i, (name, what, _) in enumerate(steps):
            n = t(name, 34, ON_DARK, SERIF, weight="BOLD")
            w = t(what, 24, SOFT_DARK)
            num = t(str(i + 1), 26, HOT_DARK, MONO, weight="BOLD")
            g = VGroup(num, n, w).arrange(DOWN, buff=0.14)
            r = RoundedRectangle(width=3.6, height=1.95, corner_radius=0.14, stroke_color=HOT_DARK, stroke_width=5)
            boxes.add(VGroup(r, g.move_to(r)))
        boxes.arrange(RIGHT, buff=0.35).move_to(DOWN * 0.55)
        arrows = VGroup(*[Arrow(boxes[i].get_right(), boxes[i + 1].get_left(), buff=0.04, color=HOT_DARK,
                                stroke_width=5, max_tip_length_to_length_ratio=0.5) for i in range(2)])
        n_stem, total = FD["kinds"]["STEM / explainer video"], FD["new_work_folders"]
        count = VGroup(t(f"{n_stem} of {total}", 60, HOT_DARK, SERIF, weight="BOLD"),
                       t("new folders this week already teach a topic", 28, ON_DARK)).arrange(RIGHT, buff=0.3)
        count.next_to(boxes, DOWN, buff=0.55)
        fit(count)
        dim = VGroup(boxes, arrows).copy().set_color(DIM_DARK)
        clock.play_at(0.2, FadeIn(dim), FadeIn(count.copy().set_color(DIM_DARK)), run_time=0.6)
        clock.play_at(cue("B70", "Your weekly update", 1.5), FadeIn(stmt, shift=UP * 0.15), FadeIn(sub), run_time=0.8)
        for i, (_, _, phrase) in enumerate(steps):
            anims = [FadeIn(boxes[i], shift=UP * 0.1)]
            if i:
                anims.append(GrowArrow(arrows[i - 1]))
            clock.play_at(max(cue("B70", phrase, 4.0 + 1.5 * i), clock.t), *anims, run_time=0.5)
        clock.play_at(max(cue("B70", "That's a lesson", 10.0), clock.t), FadeIn(count, shift=UP * 0.1), run_time=0.7)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = t("What the Fellows Taught", 92, INK, SERIF)
        fit(title, 11.8)
        pill_lab = t("SUBSCRIBE", 32, ON_DARK, SANS, weight="BOLD")
        pill = RoundedRectangle(width=pill_lab.width + 0.8, height=0.74, corner_radius=0.37,
                                fill_color=DARK, fill_opacity=1, stroke_width=0)
        pill_lab.move_to(pill)
        hai = logo("hai-logo.svg", 0.52).set_color(INK)
        handle = t("@HumanitariansAI", 38, INK, SANS, weight="BOLD")
        row = VGroup(VGroup(pill, pill_lab), hai, handle).arrange(RIGHT, buff=0.3)
        main = VGroup(title, row).arrange(DOWN, buff=0.55).move_to(UP * 1.45)
        clock.play_at(0.2, FadeIn(title, shift=UP * 0.15), run_time=0.8)
        clock.play_at(clock.t + 0.1, FadeIn(row, shift=UP * 0.1), run_time=0.6)

        rule = Line(LEFT * 3.4, RIGHT * 3.4, color=LINE, stroke_width=3).next_to(main, DOWN, buff=0.65)
        c1 = t("Boopesh M.", 46, INK, SERIF, weight="BOLD")
        c2 = t("Humanitarians AI Fellow · Brutalist team", 32, MUTED)
        c3 = t("Data: git history of nikbearbrown/humanitarians-youtube, Nov 1–7, 2026", 22, MUTED)
        c4 = t("Narration: AI voice (Kokoro am_onyx) reading Boopesh's script", 26, MUTED)
        credit = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.2).next_to(rule, DOWN, buff=0.45)
        dim = VGroup(rule, credit).copy().set_opacity(0.15)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(max(cue("B90", "With Boopesh", 1.5), clock.t), FadeOut(dim), Create(rule),
                      FadeIn(credit, shift=UP * 0.1), run_time=0.7)
        clock.finish()
