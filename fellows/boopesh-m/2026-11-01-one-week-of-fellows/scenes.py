# -*- coding: utf-8 -*-
"""
Manim scenes for "One Week of Fellows" (16:9, 3840x2160) -- Boopesh M., week of Oct 25-31 2026.
  B20_PerDay      -- merged pull requests per day, Sun Oct 25 -> Sat Oct 31
  B30_People      -- 37 author names -> 27 people -> 23 who wrote the work
  B40_WorkTypes   -- the 84 new work folders by kind, and when they were dated
  B50_Titles      -- six real titles (folder names only) + topic words
  B60_MyPart      -- Boopesh's two videos last week; Drive submitted, GitHub PR pending
  B70_Takeaway    -- dark card: small weekly evidence adds up; what a good weekly folder holds
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
    CODE = Path("/home/user/nikbearbrown/humanitarians-youtube/fellows/boopesh-m/2026-11-01-one-week-of-fellows/code")
    ASSETS = CODE.parent / "assets"

BG = "#FAF9F5"
INK = "#2B2A26"
ACCENT = "#A64B2A"   # terracotta, WCAG 4.5:1+ on cream and panel
MUTED = "#6F6A5E"
PANEL = "#EEEADF"
LINE = "#D9D3C4"
GHOST = "#A39A88"
TEAL = "#1F4E5F"     # data
GOOD = "#3F6E4E"
DARK = "#2B2A26"
ON_DARK = "#F5F1E8"
DIM_DARK = "#5E544C"
HOT_DARK = "#E08A6A"

SERIF = "EB Garamond"
SANS = "Inter"
MONO = "DejaVu Sans Mono"

RES = json.loads((CODE / "results.json").read_text())
PR = RES["merged_prs"]
PPL = RES["contributors"]
FD = RES["folders"]


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


def words(n):
    return f"{n}"


# ======================================================================== B20 =
class B20_PerDay(Scene):
    def construct(self):
        clock = Clock(self, "B20")
        hd = header(f"git log {RES['base_commit']}..{RES['head_commit']} · Oct 25–31", "Pull requests merged, per day")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        days = list(PR["per_day"].items())
        names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        x0, step, base, top = -5.55, 0.98, -2.55, 1.05
        unit = (top - base) / max(v for _, v in days)
        axis = Line([x0 - 0.6, base, 0], [x0 + step * 6 + 0.6, base, 0], color=INK, stroke_width=4)
        bars, vals, labs = VGroup(), VGroup(), VGroup()
        for i, (d, v) in enumerate(days):
            x = x0 + step * i
            busy = d == PR["busiest_day"]
            h = max(v * unit, 0.02)
            bars.add(Rectangle(width=0.78, height=h, fill_color=ACCENT if busy else TEAL, fill_opacity=1,
                               stroke_width=0).move_to([x, base + h / 2, 0]))
            vals.add(t(str(v), 34 if busy else 28, ACCENT if busy else INK, MONO, weight="BOLD")
                     .move_to([x, base + h + 0.3, 0]))
            labs.add(VGroup(t(names[i], 22, INK, weight="BOLD"), t(d[-2:], 18, MUTED, MONO))
                     .arrange(DOWN, buff=0.08).move_to([x, base - 0.45, 0]))
        ghosts = VGroup(*[Rectangle(width=0.78, height=top - base, stroke_color=GHOST, stroke_width=2)
                          .move_to([x0 + step * i, (top + base) / 2, 0]) for i in range(7)])

        # right column: totals
        big = t(str(PR["total"]), 120, INK, SERIF, weight="BOLD")
        sub = VGroup(t("pull requests merged", 28, INK, weight="BOLD"),
                     t(f"{PR['merge_commits']} merge commits + {PR['squash_merges']} squash merge", 20, MUTED))
        sub.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        gh = png("github-01.png", 0.7)
        tot = Group(Group(gh, big).arrange(RIGHT, buff=0.3), sub).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        c1 = card(4.9, 2.6).move_to([3.75, 0.1, 0])
        fit(tot, 4.4)
        tot.move_to(c1)
        direct = VGroup(t(f"+{RES['direct_commits_to_main']} commits", 30, INK, SERIF, weight="BOLD"),
                        t("straight to main, no pull request", 20, MUTED)).arrange(DOWN, buff=0.1)
        c2 = card(4.9, 1.2).move_to([3.75, -2.2, 0])
        direct.move_to(c2)

        clock.play_at(0.4, FadeIn(ghosts), FadeIn(ghost_of(c1)), FadeIn(ghost_of(c2)), run_time=0.6)
        clock.play_at(1.0, Create(axis), FadeIn(labs, lag_ratio=0.1), run_time=0.8)
        at = cue("B20", "Thirty were merged", 2.0)
        clock.play_at(at, FadeIn(c1), FadeIn(tot, shift=UP * 0.1), run_time=0.7)
        clock.play_at(cue("B20", "Sunday and Monday", 6.0), GrowFromEdge(bars[0], DOWN), GrowFromEdge(bars[1], DOWN),
                      FadeIn(vals[0]), FadeIn(vals[1]), run_time=0.6)
        clock.play_at(clock.t + 0.2, *[GrowFromEdge(bars[i], DOWN) for i in (2, 3, 5)],
                      *[FadeIn(vals[i]) for i in (2, 3, 5)], run_time=0.6)
        clock.play_at(cue("B20", "Thursday", 9.0), GrowFromEdge(bars[4], DOWN), FadeIn(vals[4], scale=1.3), run_time=0.8)
        clock.play_at(clock.t + 0.1, Indicate(labs[4], color=ACCENT, scale_factor=1.15), run_time=0.6)
        clock.play_at(cue("B20", "Saturday had none", 12.0), FadeIn(vals[6]), Indicate(labs[6], color=MUTED), run_time=0.6)
        clock.play_at(cue("B20", "thirty-five more", 14.0), FadeIn(c2), FadeIn(direct, shift=UP * 0.1), run_time=0.7)
        clock.finish()


# ======================================================================== B30 =
class B30_People(Scene):
    def construct(self):
        clock = Clock(self, "B30")
        hd = header("author names in the log, honestly counted", "Who shipped it?")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        specs = [(PPL["distinct_author_names_raw"], "author names", "as git records them", INK, "thirty-seven"),
                 (PPL["distinct_people_after_obvious_dedupe"], "people", "same email or same\nGitHub account = one",
                  TEAL, "twenty-seven people"),
                 (PPL["people_who_authored_non_merge_commits"], "wrote the work", "the rest only\nmerged it",
                  ACCENT, "Twenty-three")]
        cols = VGroup()
        for n, lab, why, col, _ in specs:
            c = card(3.5, 4.1)
            num = t(str(n), 140, col, SERIF, weight="BOLD")
            l1 = t(lab, 30, INK, weight="BOLD")
            l2 = t(why, 22, MUTED, line_spacing=0.9)
            g = VGroup(num, l1, l2).arrange(DOWN, buff=0.22).move_to(c)
            cols.add(VGroup(c, g))
        cols.arrange(RIGHT, buff=0.85).move_to([0, -0.45, 0])
        arrows = VGroup(*[Arrow(cols[i][0].get_right(), cols[i + 1][0].get_left(), buff=0.1, color=INK,
                                stroke_width=6) for i in range(2)])
        # the duplicate-name idea, shown on the first card: one person, two names
        twin = VGroup(t("full name", 20, INK, MONO), t("handle", 20, INK, MONO)).arrange(DOWN, buff=0.08)
        note = t("2 more look-alike pairs left separate (if merged: 25 people, still 23 authors)", 21, MUTED)
        note.next_to(cols, DOWN, buff=0.3)

        clock.play_at(0.4, FadeIn(VGroup(*[ghost_of(c[0]) for c in cols])), FadeIn(arrows.copy().set_color(GHOST)),
                      run_time=0.6)
        clock.play_at(cue("B30", "thirty-seven", 2.0), FadeIn(cols[0], shift=UP * 0.15), run_time=0.7)
        clock.play_at(cue("B30", "a full name", 6.0), Indicate(cols[0][1][1], color=ACCENT, scale_factor=1.1), run_time=0.8)
        clock.play_at(cue("B30", "Merge only", 9.5), GrowArrow(arrows[0]), run_time=0.5)
        clock.play_at(cue("B30", "twenty-seven people", 12.0), FadeIn(cols[1], shift=UP * 0.15), run_time=0.7)
        clock.play_at(cue("B30", "Twenty-three", 14.0), GrowArrow(arrows[1]), FadeIn(cols[2], shift=UP * 0.15), run_time=0.7)
        clock.play_at(cue("B30", "Two more pairs", 17.0), FadeIn(note, shift=UP * 0.1), run_time=0.6)
        clock.finish()


# ======================================================================== B40 =
class B40_WorkTypes(Scene):
    def construct(self):
        clock = Clock(self, "B40")
        hd = header(f"new folders under fellows/ · {FD['fellows_with_new_folders']} fellows",
                    f"{FD['new_work_folders']} new work folders")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        kinds = [("STEM explainer videos", "STEM / explainer video", "forty-two STEM"),
                 ("progress videos", "progress / work video", "thirty progress"),
                 ("renewal requests", "renewal request", "seven renewal"),
                 ("hours logs", "hours log", "three hours"),
                 ("written / code work", "written / code work", "two pieces")]
        mx = max(FD["kinds"].values())
        L, W = -1.6, 6.6
        rows = VGroup()
        for i, (lab, key, _) in enumerate(kinds):
            v = FD["kinds"][key]
            y = 1.05 - i * 0.68
            name = t(lab, 26, INK).move_to([L - 0.3, y, 0], aligned_edge=RIGHT)
            bar = Rectangle(width=max(W * v / mx, 0.05), height=0.46, fill_color=TEAL if i < 2 else "#4F7A88",
                            fill_opacity=1, stroke_width=0)
            bar.move_to([L, y, 0], aligned_edge=LEFT)
            val = t(str(v), 28, INK, MONO, weight="BOLD").next_to(bar, RIGHT, buff=0.18)
            rows.add(VGroup(name, bar, val))
        rough = t("my rough sort: folder name + README", 18, MUTED).move_to([L + W - 1.6, 1.55, 0])
        ghosts = VGroup(*[Rectangle(width=W, height=0.46, stroke_color=GHOST, stroke_width=2)
                          .move_to([L, r[1].get_y(), 0], aligned_edge=LEFT) for r in rows])

        # when the folders are dated
        parts = [(FD["dated_inside_the_week"], "dated this week", ACCENT, "Twenty-seven"),
                 (FD["dated_earlier_added_this_week"], "older work, filed this week", "#8C8578", "Thirty-three"),
                 (FD["undated_new_folders"], "no date in the name", LINE, None)]
        total = sum(p[0] for p in parts)
        SX, SW, SY = -6.0, 12.0, -2.45
        strip, slabs = VGroup(), VGroup()
        x = SX
        for n, lab, col, _ in parts:
            w = SW * n / total
            r = Rectangle(width=w, height=0.5, fill_color=col, fill_opacity=1, stroke_color=BG, stroke_width=4)
            r.move_to([x + w / 2, SY, 0])
            txt = t(f"{n} {lab}", 20, INK).next_to(r, DOWN, buff=0.14)
            if txt.width > w - 0.1:
                fit(txt, w - 0.1)
            strip.add(r)
            slabs.add(txt)
            x += w

        clock.play_at(0.4, FadeIn(ghosts), FadeIn(VGroup(*[ghost_of(r) for r in strip])), run_time=0.6)
        clock.play_at(0.9, FadeIn(VGroup(*[r[0] for r in rows]), lag_ratio=0.1), run_time=0.8)
        clock.play_at(cue("B40", "my rough sort", 4.0), FadeIn(rough), run_time=0.4)
        for i, (_, _, phrase) in enumerate(kinds):
            at = cue("B40", phrase, 5.0 + 1.5 * i)
            clock.play_at(max(at, clock.t), GrowFromEdge(rows[i][1], LEFT), FadeIn(rows[i][2]), run_time=0.5)
        clock.play_at(cue("B40", "Twenty-seven", 13.0), FadeIn(strip[0]), FadeIn(slabs[0]), run_time=0.5)
        clock.play_at(cue("B40", "Thirty-three", 15.0), FadeIn(strip[1:]), FadeIn(slabs[1:]), run_time=0.6)
        clock.finish()


# ======================================================================== B50 =
def clean_title(s):
    for pre in ("Weekly Research Report: ", "Weekly STEM Video: "):
        s = s.removeprefix(pre)
    return s.rstrip(".")


class B50_Titles(Scene):
    def construct(self):
        clock = Clock(self, "B50")
        hd = header("README titles · fellow folder names only", "A few of the titles")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        by = {r["folder"]: r for r in RES["representative_titles"]}
        picks = [("aishwarya-p/2026-10-29-what-is-rlhf", "R L H F"),
                 ("chinnasurya-v/2026-10-28-encrypted-twice", "Encrypted Twice"),
                 ("uday-s/2026-10-30-right-answer-wrong-chain", "Right Answer"),
                 ("yatra-r/2026-10-29-ads-in-the-picture", "Ads in the Picture"),
                 ("anjana-n/2026-10-30-distributed-training-explainer", None),
                 ("satwik-s/2026-10-25-prereq-recall-gap", None)]
        CW, CH = 3.85, 1.8
        cards = VGroup()
        for f, _ in picks:
            r = by[f]
            c = card(CW, CH)
            title = fit(t(clean_title(r["title"]), 30, INK, SERIF, weight="BOLD"), CW - 0.35)
            if title.width > CW - 0.35 or len(clean_title(r["title"])) > 19:
                words_ = clean_title(r["title"]).split()
                half = len(words_) // 2
                title = fit(t(" ".join(words_[:half]) + "\n" + " ".join(words_[half:]), 29, INK, SERIF,
                              weight="BOLD", line_spacing=0.85), CW - 0.35)
            who = t(f.split("/")[0], 21, MUTED, MONO)
            kind = t("progress" if r["kind"].startswith("progress") else "STEM", 20,
                     ACCENT if r["kind"].startswith("progress") else TEAL, MONO, weight="BOLD")
            foot = VGroup(who, kind).arrange(RIGHT, buff=0.3)
            g = VGroup(title, foot).arrange(DOWN, buff=0.16).move_to(c)
            cards.add(VGroup(c, g))
        cards.arrange_in_grid(rows=2, cols=3, buff=(0.3, 0.25)).move_to([0, -0.3, 0])

        top = RES["topic_words_top"]
        cnt = dict(top)
        chips = VGroup()
        for s, hot in ((f"physics ×{cnt['physics']} (one series)", True),
                       (f"agent ×{cnt['agent']}", False), (f"memory ×{cnt['memory']}", False)):
            lab = t(s, 26, ON_DARK if hot else INK, weight="BOLD" if hot else "NORMAL")
            bg = RoundedRectangle(width=lab.width + 0.5, height=0.58, corner_radius=0.29,
                                  fill_color=DARK if hot else PANEL, fill_opacity=1, stroke_width=0)
            chips.add(VGroup(bg, lab.move_to(bg)))
        chips.arrange(RIGHT, buff=0.3)
        cap = t("top topic words:", 26, MUTED)
        row = VGroup(cap, chips).arrange(RIGHT, buff=0.35)
        fit(row, 12.0).next_to(cards, DOWN, buff=0.4).set_x(0)

        clock.play_at(0.4, FadeIn(VGroup(*[ghost_of(c[0]) for c in cards])),
                      FadeIn(VGroup(*[ghost_of(c[0]) for c in chips])), run_time=0.6)
        for i, (_, phrase) in enumerate(picks):
            at = cue("B50", phrase, 2.0 + 1.6 * i) if phrase else clock.t + 0.15
            clock.play_at(max(at, clock.t), FadeIn(cards[i], shift=UP * 0.12), run_time=0.45)
        clock.play_at(cue("B50", "most common topic word", 10.0), FadeIn(cap), FadeIn(chips[0], shift=UP * 0.1),
                      run_time=0.6)
        clock.play_at(cue("B50", "After that", 14.0), FadeIn(chips[1:], lag_ratio=0.3), run_time=0.7)
        clock.finish()


# ======================================================================== B60 =
class B60_MyPart(Scene):
    def construct(self):
        clock = Clock(self, "B60")
        hd = header("Boopesh M. · last week's two videos", "My part")
        clock.play_at(0, FadeIn(hd, shift=DOWN * 0.15), run_time=0.7)

        D = RES["boopesh"]["last_week_deliveries"]

        def mmss(s):
            return f"{int(s // 60)}:{int(s % 60):02d}"

        def vcard(img, title, kind, lk, vk):
            im = ImageMobject(str(ASSETS / img))
            im.scale_to_fit_width(4.3)
            border = Rectangle(width=im.width, height=im.height, stroke_color=LINE, stroke_width=3).move_to(im)
            tl = VGroup(t(title, 32, INK, SERIF, weight="BOLD"), t(kind, 18, ACCENT, MONO, weight="BOLD"))
            tl.arrange(RIGHT, buff=0.25, aligned_edge=DOWN)
            meta = VGroup(t(f"{mmss(D[lk]['duration_s'])} + Short {mmss(D[vk]['duration_s'])}", 18, INK, MONO),
                          t(f"{D[lk]['width']}×{D[lk]['height']} + {D[vk]['width']}×{D[vk]['height']}", 16, MUTED, MONO))
            meta.arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            return Group(Group(im, border), tl, meta).arrange(DOWN, aligned_edge=LEFT, buff=0.16)

        a = vcard("lastweek-brutalist-shared.png", "Brutalist, Shared", "PROGRESS",
                  "landscape/BrutalistShared_BoopeshM.mp4", "vertical/BrutalistShared_BoopeshM.mp4")
        b = vcard("lastweek-deep-hedging.png", "Deep Hedging", "STEM",
                  "landscape/DeepHedging_BoopeshM.mp4", "vertical/DeepHedging_BoopeshM.mp4")
        pair = Group(a, b).arrange(RIGHT, buff=1.0, aligned_edge=UP)
        pair.move_to([0, 1.84 - pair.height / 2, 0])

        drive = logo("google-drive-01.svg", 0.5)
        s1 = VGroup(t("Google Drive", 24, INK, weight="BOLD"), t("✓ submitted", 24, GOOD, weight="BOLD")).arrange(RIGHT, buff=0.2)
        g1 = VGroup(drive, s1).arrange(RIGHT, buff=0.2)
        b1 = card(g1.width + 0.6, 0.85).move_to(g1)
        gh = png("github-01.png", 0.5)
        s2 = VGroup(t("pull request", 24, INK, weight="BOLD"), t("pending", 24, ACCENT, weight="BOLD")).arrange(RIGHT, buff=0.2)
        b2 = DashedVMobject(RoundedRectangle(width=s2.width + gh.width + 0.9, height=0.85, corner_radius=0.12,
                                             stroke_color=ACCENT, stroke_width=4), num_dashes=40)
        st = Group(VGroup(b1, g1), Arrow(LEFT, RIGHT, color=INK, stroke_width=5, buff=0).scale(0.5),
                   Group(b2)).arrange(RIGHT, buff=0.3)
        Group(gh, s2).arrange(RIGHT, buff=0.2).move_to(b2)
        status = Group(st, gh, s2)
        why = t("fork attempt failed · asking the maintainer for access · not in this week's numbers yet", 19, MUTED)
        low = Group(status, why).arrange(DOWN, buff=0.12).next_to(pair, DOWN, buff=0.22)
        gh.move_to(b2).shift(LEFT * (b2.width / 2 - gh.width / 2 - 0.3))
        s2.next_to(gh, RIGHT, buff=0.2)

        clock.play_at(0.4, FadeIn(ghost_of(Rectangle(width=4.3, height=4.3 * 9 / 16).move_to(a[0]))),
                      FadeIn(ghost_of(Rectangle(width=4.3, height=4.3 * 9 / 16).move_to(b[0]))),
                      FadeIn(ghost_of(b1)), FadeIn(b2.copy().set_stroke(GHOST)), run_time=0.6)
        clock.play_at(cue("B60", "a progress update", 2.5), FadeIn(a, shift=UP * 0.15), run_time=0.7)
        clock.play_at(cue("B60", "a STEM explainer", 6.5), FadeIn(b, shift=UP * 0.15), run_time=0.7)
        clock.play_at(cue("B60", "all four are 4K", 10.5),
                      Indicate(Group(a[2], b[2]), color=ACCENT, scale_factor=1.05), run_time=0.7)
        clock.play_at(cue("B60", "submitted to Drive", 13.0), FadeIn(VGroup(b1, g1)), GrowArrow(st[1]), run_time=0.6)
        clock.play_at(cue("B60", "still pending", 15.5), Create(b2), FadeIn(gh), FadeIn(s2), run_time=0.7)
        clock.play_at(cue("B60", "my fork attempt", 17.0), FadeIn(why, shift=UP * 0.1), run_time=0.6)
        clock.finish()


# ======================================================================== B70 =
class B70_Takeaway(Scene):
    def construct(self):
        clock = Clock(self, "B70")
        self.camera.background_color = DARK
        stmt = t("Small weekly evidence adds up.", 76, ON_DARK, SERIF, weight="BOLD")
        fit(stmt, 11.4).move_to(UP * 2.2)
        sub = t("a good weekly folder is small and complete:", 30, "#D8D0C0").next_to(stmt, DOWN, buff=0.35)

        files = [("README.md", "the result", "a README"), ("FACTCHECK.md", "every claim, sourced", "a fact check"),
                 ("FRICTIONAL.md", "what resisted", "a frictional log"), ("source/", "rebuilds the video", "the source")]
        boxes = VGroup()
        for name, what, _ in files:
            n = t(name, 26, ON_DARK, MONO, weight="BOLD")
            w = t(what, 20, "#D8D0C0")
            g = fit(VGroup(n, w).arrange(DOWN, buff=0.18), 2.6)
            r = RoundedRectangle(width=2.8, height=1.6, corner_radius=0.14, stroke_color=HOT_DARK, stroke_width=5)
            boxes.add(VGroup(r, g.move_to(r)))
        boxes.arrange(RIGHT, buff=0.3).move_to(DOWN * 0.75)
        fit(boxes)
        count = VGroup(t(str(FD["frictional_logs_added"]), 64, HOT_DARK, SERIF, weight="BOLD"),
                       t(f"frictional logs landed this week, in {FD['frictional_logs_fellows']} fellow folders",
                         26, ON_DARK)).arrange(RIGHT, buff=0.3)
        count.next_to(boxes, DOWN, buff=0.5)
        fit(count)
        dim = boxes.copy().set_color(DIM_DARK)
        clock.play_at(0.2, FadeIn(dim), FadeIn(count.copy().set_color(DIM_DARK)), run_time=0.6)
        clock.play_at(cue("B70", "Small weekly", 1.5), FadeIn(stmt, shift=UP * 0.15), run_time=0.8)
        clock.play_at(cue("B70", "A good weekly folder", 4.0), FadeIn(sub), run_time=0.5)
        for i, (_, _, phrase) in enumerate(files):
            clock.play_at(max(cue("B70", phrase, 6.0 + 1.5 * i), clock.t), FadeIn(boxes[i], shift=UP * 0.1), run_time=0.5)
        clock.play_at(cue("B70", "Seventy-two", 13.0), FadeIn(count, shift=UP * 0.1),
                      Indicate(boxes[2], color=HOT_DARK, scale_factor=1.06), run_time=0.8)
        clock.finish()


# ======================================================================== B90 =
class B90_Outro(Scene):
    def construct(self):
        clock = Clock(self, "B90")
        title = t("One Week of Fellows", 92, INK, SERIF)
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
        c3 = t("Data: git history of nikbearbrown/humanitarians-youtube, Oct 25–31, 2026", 22, MUTED)
        c4 = t("Narration: AI voice (Kokoro am_onyx) reading Boopesh's script", 26, MUTED)
        credit = VGroup(c1, c2, c3, c4).arrange(DOWN, buff=0.2).next_to(rule, DOWN, buff=0.45)
        dim = VGroup(rule, credit).copy().set_opacity(0.15)
        clock.play_at(clock.t, FadeIn(dim), run_time=0.3)
        clock.play_at(max(cue("B90", "With Boopesh", 1.5), clock.t), FadeOut(dim), Create(rule),
                      FadeIn(credit, shift=UP * 0.1), run_time=0.7)
        clock.finish()
