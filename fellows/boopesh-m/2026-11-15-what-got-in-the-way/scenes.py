# -*- coding: utf-8 -*-
"""
Manim scenes for "What Got in the Way" (16:9, 3840x2160) -- Boopesh M., week of Nov 8-14 2026.
  B20_Themes      -- the 31 frictional logs with obstacles, sorted into six plain themes (rough keyword sort)
  B30_Examples    -- five short paraphrased examples, obstacle -> fix (fellow folder names only)
  B40_Looked      -- what fixed them: 17 of 31 logs found a problem by looking
  B50_Compare     -- one comparison with last week, same script, recounted today
  B60_MyPart      -- Boopesh's two videos last week; delivered for review; his own obstacle: access
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
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-15-what-got-in-the-way/code")
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
FR = RES["friction"]


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


KERN = 4   # set type large, then scale down: keeps word spacing right at small sizes


def t(s, size=40, color=INK, font=SANS, weight="NORMAL", **kw):
    return Text(s, font=font, font_size=size * KERN, color=color, weight=weight, **kw).scale(1 / KERN)


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
THEME_ORDER = [("layout & picture checks", "Layout and picture checks led"), ("facts & data", "Then facts and data"),
               ("length & time", "Length and time"), ("tools & setup", "Tools and setup"),
               ("timing & pacing", "Timing and pacing"), ("voice & pronunciation", "And the AI voice")]
THEME_LABEL = {"layout & picture checks": "layout & picture checks", "facts & data": "facts & data",
               "length & time": "length & time", "tools & setup": "tools & setup",
               "timing & pacing": "timing & pacing", "voice & pronunciation": "the voice says a word wrong"}


class B20_Themes(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        n_logs, n_obs, n_fel = FR["logs_added"], FR["logs_describing_obstacles"], FR["fellows"]
        hd = header(f"frictional logs added Nov 8–14 · {n_logs} logs · {n_fel} fellows", "What got in the way")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        # strip: one square per log; the one without obstacles stays grey
        sq, step = 0.18, 0.22
        x0, ys = -5.9 + sq / 2, 1.5
        logs = VGroup(*[Square(sq, stroke_width=0, fill_opacity=1, fill_color=TEAL)
                        .move_to([x0 + i * step, ys, 0]) for i in range(n_logs)])
        for i in range(n_obs, n_logs):
            logs[i].set_fill(LINE)
        lghost = VGroup(*[Square(sq, stroke_color=GHOST, stroke_width=2).move_to(c) for c in logs])
        cap = VGroup(t(f"{n_obs}", 34, TEAL, SERIF, weight="BOLD"), t("with obstacles", 22, INK),
                     t(f"· {n_logs - n_obs} without", 20, MUTED)).arrange(RIGHT, buff=0.15)
        cap.next_to(logs, RIGHT, buff=0.3)

        # bars: out of the 31 logs with obstacles (ghost = all 31)
        S, SF = FR["theme_logs"], FR["theme_fellows"]
        L, W = -0.45, 5.0
        rows = VGroup()
        for i, (key, _) in enumerate(THEME_ORDER):
            v = S[key]
            y = 0.62 - i * 0.6
            hot = i == 0
            name = t(THEME_LABEL[key], 26, INK, weight="BOLD" if hot else "NORMAL").move_to([L - 0.3, y, 0],
                                                                                            aligned_edge=RIGHT)
            bar = Rectangle(width=W * v / n_obs, height=0.44, fill_color=ACCENT if hot else TEAL,
                            fill_opacity=1, stroke_width=0).move_to([L, y, 0], aligned_edge=LEFT)
            val = t(str(v), 28, ACCENT if hot else INK, MONO, weight="BOLD").next_to(bar, RIGHT, buff=0.15)
            who = t(f"{SF[key]} fellows", 22, ACCENT if hot else MUTED, weight="BOLD" if hot else "NORMAL")
            who.move_to([L + W + 0.25, y, 0], aligned_edge=LEFT)
            rows.add(VGroup(name, bar, val, who))
        ghosts = VGroup(*[Rectangle(width=W, height=0.44, stroke_color=GHOST, stroke_width=2)
                          .move_to([L, r[1].get_y(), 0], aligned_edge=LEFT) for r in rows])
        scale = t(f"logs, out of {n_obs}", 20, MUTED).move_to([L, 1.0, 0], aligned_edge=LEFT)
        colhead = t("from", 20, MUTED).move_to([L + W + 0.25, 1.0, 0], aligned_edge=LEFT)
        rough = t("my rough sort: keywords · one log can count in several themes · "
                  f"{len(FR['logs_with_no_theme'])} fit none", 20, MUTED)
        rough.next_to(rows, DOWN, buff=0.2).set_x(0)

        clock.play_at(0.4, FadeIn(lghost, lag_ratio=0.01), FadeIn(ghosts), run_time=0.7)
        clock.play_at(cue("B20", "Thirty-two", 0.8), FadeIn(logs, lag_ratio=0.03), run_time=1.0)
        clock.play_at(cue("B20", "thirty-one describe", 4.0), FadeIn(cap, shift=LEFT * 0.1), run_time=0.6)
        clock.play_at(cue("B20", "I sorted them", 7.0), FadeIn(rough), FadeIn(scale), FadeIn(colhead), run_time=0.6)
        for i, (key, phrase) in enumerate(THEME_ORDER):
            at = cue("B20", phrase, 11.0 + 2.5 * i)
            clock.play_at(max(at, clock.t), GrowFromEdge(rows[i][1], LEFT), FadeIn(rows[i][2]), FadeIn(rows[i][3]),
                          FadeIn(rows[i][0]), run_time=0.5)
            if i == 0:
                clock.play_at(max(cue("B20", "things running off", 15.0), clock.t),
                              Indicate(rows[0][1], color=ACCENT, scale_factor=1.04), run_time=0.7)
        clock.finish()


# ======================================================================== B30 =
def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > n:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    lines.append(cur)
    return "\n".join(lines)


class B30_Examples(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("from this week's frictional logs · paraphrased · folder names only", "Obstacle → fix")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        phrases = ["A chart passed", "A working title", "A script ran", "A checking script", "And words on screen"]
        ex = RES["examples"]
        assert len(ex) == 5
        RW, RH = 12.5, 0.92
        rows = VGroup()
        for e in ex:
            c = card(RW, RH)
            th = t(e["theme"], 20, ACCENT, weight="BOLD")
            fo = t(e["fellow"], 18, MUTED, MONO)
            left = VGroup(th, fo).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            fit(left, 2.8)
            ob = fit(t(wrap(e["obstacle"], 38), 23, INK, line_spacing=0.8), 4.55)
            ar = Arrow(LEFT * 0.25, RIGHT * 0.25, color=INK, stroke_width=4, buff=0,
                       max_tip_length_to_length_ratio=0.35)
            fx = fit(t(wrap(e["fix"], 27), 23, TEAL, weight="BOLD", line_spacing=0.8), 3.6)
            c.move_to(ORIGIN)
            left.move_to([-RW / 2 + 0.25, 0, 0], aligned_edge=LEFT)
            ob.move_to([-2.95, 0, 0], aligned_edge=LEFT)
            ar.move_to([1.95, 0, 0])
            fx.move_to([2.35, 0, 0], aligned_edge=LEFT)
            rows.add(VGroup(c, left, ob, ar, fx))
        rows.arrange(DOWN, buff=0.12).move_to([0, -0.55, 0])

        clock.play_at(0.4, FadeIn(VGroup(*[ghost_of(r[0]) for r in rows])), run_time=0.6)
        for i, ph in enumerate(phrases):
            at = cue("B30", ph, 1.5 + 4.0 * i)
            r = rows[i]
            clock.play_at(max(at, clock.t), FadeIn(r[0]), FadeIn(r[1]), FadeIn(r[2], shift=RIGHT * 0.1), run_time=0.45)
            clock.play_at(clock.t + 0.9, GrowArrow(r[3]), FadeIn(r[4], shift=RIGHT * 0.1), run_time=0.45)
        clock.finish()


# ======================================================================== B40 =
class B40_Looked(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        self.camera.background_color = DARK
        stmt = t("Someone looked.", 84, ON_DARK, SERIF, weight="BOLD")
        fit(stmt, 11.4).move_to(UP * 2.35)
        n_look, n_obs = FR["found_by_looking_logs"], FR["logs_describing_obstacles"]
        count = VGroup(t(f"{n_look} of {n_obs}", 64, HOT_DARK, SERIF, weight="BOLD"),
                       t("logs found a problem by looking", 30, ON_DARK)).arrange(RIGHT, buff=0.3)
        count.move_to(UP * 0.95)
        fit(count)

        steps = [("watch", "the cut", "watching the cut"), ("view", "the frames", "viewing the frames"),
                 ("re-read", "the words", "re-reading the words")]
        boxes = VGroup()
        for i, (verb, what, _) in enumerate(steps):
            n = t(verb, 38, ON_DARK, SERIF, weight="BOLD")
            w = t(what, 26, SOFT_DARK)
            g = VGroup(n, w).arrange(DOWN, buff=0.12)
            r = RoundedRectangle(width=3.5, height=1.5, corner_radius=0.14, stroke_color=DIM_DARK, stroke_width=4,
                                 fill_color="#37352F", fill_opacity=1)
            boxes.add(VGroup(r, g.move_to(r)))
        boxes.arrange(RIGHT, buff=0.45).move_to(DOWN * 0.75)
        line = VGroup(t("a passing check: the frame fits", 28, SOFT_DARK),
                      t("·", 28, DIM_DARK),
                      t("looking: it's right", 28, HOT_DARK, weight="BOLD")).arrange(RIGHT, buff=0.3)
        line.next_to(boxes, DOWN, buff=0.6)
        fit(line)
        dim = VGroup(*[b[0] for b in boxes]).copy().set_fill(opacity=0).set_stroke(DIM_DARK)
        clock.play_at(0.2, FadeIn(dim), FadeIn(count.copy().set_color(DIM_DARK)),
                      FadeIn(line.copy().set_color(DIM_DARK)), FadeIn(stmt.copy().set_color(DIM_DARK)), run_time=0.6)
        clock.play_at(cue("B40", "Most often", 1.5), FadeIn(stmt, shift=UP * 0.15), run_time=0.7)
        clock.play_at(max(cue("B40", "In seventeen", 3.0), clock.t), FadeIn(count, shift=UP * 0.1), run_time=0.6)
        for i, (_, _, phrase) in enumerate(steps):
            clock.play_at(max(cue("B40", phrase, 5.0 + 1.2 * i), clock.t), FadeIn(boxes[i], shift=UP * 0.1),
                          run_time=0.45)
        clock.play_at(max(cue("B40", "A passing check", 9.5), clock.t), FadeIn(line, shift=UP * 0.1), run_time=0.6)
        clock.finish()


# ======================================================================== B50 =
class B50_Compare(Scene):
    def construct(self):
        clock = Clock(self, "B50")
        hd = header("same script · Nov 1–7 recounted today vs Nov 8–14", "Last week vs this week")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        specs = [("merged_prs", "pull requests\nmerged", "nineteen, down from"),
                 ("new_work_folders", "new work\nfolders", "fifty-three"),
                 ("fellows_with_new_folders", "fellows with\nnew folders", "seventeen, from"),
                 ("frictional_logs_added", "frictional\nlogs", "thirty-two, from")]
        CW, CH = 2.85, 3.7
        cards = VGroup()
        for key, lab, _ in specs:
            a, b = CMP[key]["last_week"], CMP[key]["this_week"]
            c = card(CW, CH)
            title = t(lab, 24, INK, weight="BOLD", line_spacing=0.9)
            mx = max(a, b)
            H = 1.55
            ba = Rectangle(width=0.7, height=H * a / mx, fill_color=LINE, fill_opacity=1, stroke_width=0)
            bb = Rectangle(width=0.7, height=H * b / mx, fill_color=TEAL, fill_opacity=1, stroke_width=0)
            bars = VGroup(ba, bb).arrange(RIGHT, buff=0.3, aligned_edge=DOWN)
            va = t(str(a), 30, MUTED, MONO, weight="BOLD").next_to(ba, UP, buff=0.1)
            vb = t(str(b), 34, TEAL, MONO, weight="BOLD").next_to(bb, UP, buff=0.1)
            wk = VGroup(t("last", 20, MUTED).next_to(ba, DOWN, buff=0.1),
                        t("this", 20, INK, weight="BOLD").next_to(bb, DOWN, buff=0.1))
            chart = VGroup(bars, va, vb, wk)
            body = VGroup(title, chart).arrange(DOWN, buff=0.3).move_to(c)
            cards.add(VGroup(c, body))
        cards.arrange(RIGHT, buff=0.3).move_to([0, -0.45, 0])
        fit(cards)
        P = RES["last_week_published_vs_recounted"]
        late = P["late_prs"][0]
        pub = P["published_2026_11_08_at_a953b021"]
        note1 = t(f"this week: {TW['merged_prs']['total']} pull requests = {TW['merged_prs']['merge_commits']} merge "
                  f"commits, {TW['merged_prs']['squash_merges']} squash merges", 20, MUTED)
        note2 = t(f"last week's video said {pub[0]} / {pub[1]} / {pub[2]}: PR #{late['pr']} merged late on Sat Nov 7, "
                  "after that count", 20, MUTED)
        notes = VGroup(note1, note2).arrange(DOWN, buff=0.08).next_to(cards, DOWN, buff=0.18)

        clock.play_at(0.4, FadeIn(VGroup(*[ghost_of(c[0]) for c in cards])), run_time=0.6)
        clock.play_at(cue("B50", "recounted today", 1.5), FadeIn(notes[1]), run_time=0.5)
        for i, (_, _, ph) in enumerate(specs):
            c = cards[i]
            title, chart = c[1][0], c[1][1]
            bars, va, vb, wk = chart
            at = cue("B50", ph, 3.5 + 3.0 * i)
            clock.play_at(max(at - 0.3, clock.t), FadeIn(c[0]), FadeIn(title), GrowFromEdge(bars[0], DOWN), FadeIn(va),
                          FadeIn(wk[0]), run_time=0.5)
            clock.play_at(clock.t + 0.2, GrowFromEdge(bars[1], DOWN), FadeIn(vb, scale=1.2), FadeIn(wk[1]),
                          *([FadeIn(notes[0])] if i == 0 else []), run_time=0.5)
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
            im.scale_to_fit_width(4.3)  # ghost below uses the same size
            border = Rectangle(width=im.width, height=im.height, stroke_color=LINE, stroke_width=3).move_to(im)
            tl = VGroup(t(title, 32, INK, SERIF, weight="BOLD"), t(kind, 18, ACCENT, MONO, weight="BOLD"))
            tl.arrange(RIGHT, buff=0.25, aligned_edge=DOWN)
            meta = VGroup(t(f"{D[lk]['mm_ss']} + Short {D[vk]['mm_ss']}", 22, INK, MONO),
                          t(f"{D[lk]['width']}×{D[lk]['height']} + {D[vk]['width']}×{D[vk]['height']}", 20, MUTED, MONO))
            meta.arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            return Group(Group(im, border), tl, meta).arrange(DOWN, aligned_edge=LEFT, buff=0.16)

        a = vcard("lastweek-what-the-fellows-taught.png", "What the Fellows Taught", "PROGRESS",
                  "landscape/WhatTheFellowsTaught_BoopeshM.mp4", "vertical/WhatTheFellowsTaught_BoopeshM.mp4")
        b = vcard("lastweek-backtest-mirage.png", "The Backtest Mirage", "AI IN FINANCE",
                  "landscape/BacktestMirage_BoopeshM.mp4", "vertical/BacktestMirage_BoopeshM.mp4")
        pair = Group(a, b).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        if pair.width > 11.2:
            pair.scale_to_fit_width(11.2)
        pair.move_to([0, 1.84 - pair.height / 2, 0])

        s1 = t("✓ delivered for review", 24, GOOD, weight="BOLD")
        b1 = card(s1.width + 0.6, 0.85).move_to(s1)
        gh = png("github-01.png", 0.5)
        s2 = VGroup(t("pull request", 24, INK, weight="BOLD"), t("pending", 24, ACCENT, weight="BOLD")).arrange(RIGHT, buff=0.2)
        b2 = DashedVMobject(RoundedRectangle(width=s2.width + gh.width + 0.9, height=0.85, corner_radius=0.12,
                                             stroke_color=ACCENT, stroke_width=4), num_dashes=40)
        arrow = Arrow(LEFT, RIGHT, color=INK, stroke_width=5, buff=0).scale(0.5)
        st = Group(VGroup(b1, s1), arrow, Group(b2)).arrange(RIGHT, buff=0.3)
        why = t("my obstacle: access · fork attempt failed · fellows/boopesh-m not on main · not in these counts",
                20, MUTED)
        fit(why, 11.4)
        Group(st, why).arrange(DOWN, buff=0.12).next_to(pair, DOWN, buff=0.22)
        gh.move_to(b2).shift(LEFT * (b2.width / 2 - gh.width / 2 - 0.3))
        s2.next_to(gh, RIGHT, buff=0.2)

        clock.play_at(0.4, FadeIn(ghost_of(Rectangle(width=a[0].width, height=a[0].height).move_to(a[0]))),
                      FadeIn(ghost_of(Rectangle(width=b[0].width, height=b[0].height).move_to(b[0]))),
                      FadeIn(ghost_of(b1)), FadeIn(b2.copy().set_stroke(GHOST)), run_time=0.6)
        clock.play_at(cue("B60", "What the Fellows Taught", 2.5), FadeIn(a, shift=UP * 0.15), run_time=0.7)
        clock.play_at(cue("B60", "The Backtest Mirage", 5.5), FadeIn(b, shift=UP * 0.15), run_time=0.7)
        clock.play_at(cue("B60", "all four are 4K", 9.0),
                      Indicate(Group(a[2], b[2]), color=ACCENT, scale_factor=1.0), run_time=0.7)
        clock.play_at(cue("B60", "delivered for review", 10.5), FadeIn(VGroup(b1, s1)), GrowArrow(arrow), run_time=0.6)
        clock.play_at(cue("B60", "My own obstacle", 12.0), FadeIn(why, shift=UP * 0.1), run_time=0.6)
        clock.play_at(max(cue("B60", "still pending", 14.5), clock.t), Create(b2), FadeIn(gh), FadeIn(s2), run_time=0.7)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = t("What Got in the Way", 92, INK, SERIF)
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
        c3 = t("Data: git history and frictional logs of nikbearbrown/humanitarians-youtube, Nov 8–14, 2026", 22, MUTED)
        c4 = t("Narration: AI voice (Kokoro am_onyx) reading Boopesh's script", 26, MUTED)
        credit = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.2).next_to(rule, DOWN, buff=0.45)
        fit(credit)
        dim = VGroup(rule, credit).copy().set_opacity(0.15)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(max(cue("B90", "With Boopesh", 1.5), clock.t), FadeOut(dim), Create(rule),
                      FadeIn(credit, shift=UP * 0.1), run_time=0.7)
        clock.finish()
