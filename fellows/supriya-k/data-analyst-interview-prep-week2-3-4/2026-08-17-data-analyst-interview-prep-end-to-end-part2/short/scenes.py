"""scenes.py — portrait (9:16) Manim scenes for hai-sql-window-functions-tie-bug/short.
Full-length short (no beats cut): all 5 Manim beats re-laid-out for portrait —
B01, B02, B05, B08, B09. Not shrunk copies of the landscape scenes: the portrait frame is
narrow in x (frame_width=4.5, Gate B safe ±1.95) and unchanged in y (frame_height=8.0,
safe ±3.4), so every layout is restacked vertically (B02's two columns become two bands).

DATA + TIMING come from the landscape ../scenes.py (imported, not copied): the same rows
parsed from ../sql/*.out at render time, the same measured audio durations, the same
narration-cue placement. Scene classes must be declared as plain Scene subclasses named
B0X_Name — run.sh finds them by regex.
"""
from manim import *
from pathlib import Path
import importlib.util

# `manim -r 2160,3840` does NOT reset the coordinate frame to portrait — without these two
# lines every scene below renders in the 16:9 default space.
config.frame_width = 4.5
config.frame_height = 8.0

_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/data-analyst-interview-prep-week2-3-4/2026-08-17-data-analyst-interview-prep-end-to-end-part2")
_parent = Path(__file__).resolve().parent.parent / "scenes.py"
if not _parent.is_file() or not (_parent.parent / "sql").is_dir():
    _parent = _REEL / "scenes.py"
_spec = importlib.util.spec_from_file_location("landscape_scenes", _parent)
L = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L)

H, SERIF, SANS, MONO = L.H, L.SERIF, L.SANS, L.MONO
TOTALS, COUNTS, RANK101, BUGGY, FIXED, USERS, TIED = L.TOTALS, L.COUNTS, L.RANK101, L.BUGGY, L.FIXED, L.USERS, L.TIED
SAFE_X = 1.95


def handle(scene):
    """Visible author handle, lower-right inside the portrait safe area."""
    h = Text("Supriya", font=SANS, color=H["INK"], font_size=18, weight="BOLD").set_opacity(0.75)
    h.move_to([SAFE_X - 0.05, -3.22, 0], aligned_edge=RIGHT)
    scene.add(h)
    return h


class Clock(L.Clock):
    """The landscape clock (same cues, same DUR) with the portrait handle."""

    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = L.dur(bid)
        scene.camera.background_color = H["CREAM"]
        handle(scene)


def fit(m, w):
    if m.width > w:
        m.scale_to_fit_width(w)
    return m


def pill(text, color, text_color="#FFFFFF", size=22, w=None):
    t = Text(text, font=SANS, font_size=size, color=text_color, weight="BOLD")
    if w:
        fit(t, w - 0.3)
    bg = RoundedRectangle(corner_radius=0.1, width=(w or t.width + 0.4), height=t.height + 0.3,
                          stroke_width=0, fill_color=color, fill_opacity=1)
    return VGroup(bg, t.move_to(bg))


# ── B01 — the tie hiding in the log ───────────────────────────────────────────

class B01_ProblemStakes(Scene):
    def construct(self):
        c = Clock(self, "B01")
        head = VGroup(Text("plays(user_id,", font=MONO, font_size=28, color=H["INK"], weight="BOLD"),
                      Text("track_id, played_at)", font=MONO, font_size=28, color=H["INK"], weight="BOLD")
                      ).arrange(DOWN, buff=0.1)
        fit(head, 3.8).move_to([0, 2.95, 0])
        sub = fit(Text("Loopr — the book's invented streaming service", font=SERIF, font_size=18,
                       color=H["SEC"], slant="ITALIC"), 3.8).next_to(head, DOWN, buff=0.2)
        c.run(FadeIn(head), FadeIn(sub), rt=0.6)

        u101 = [(t, n) for u, t, n in COUNTS if u == TIED[0]]
        top = max(n for _, n in u101)
        groups = VGroup()
        for k, (track, n) in enumerate(u101):
            y = 1.25 - k * 1.25
            lab = Text(f"user {TIED[0]} · {track}", font=MONO, font_size=22, color=H["INK"])
            lab.move_to([-1.85, y + 0.3, 0], aligned_edge=LEFT)
            w = 2.7 * n / top
            bar = Rectangle(width=w, height=0.5, stroke_width=0,
                            fill_color=H["TEAL"] if n == top else H["DIM"], fill_opacity=1)
            bar.move_to([-1.85 + w / 2, y - 0.2, 0])
            num = Text(str(n), font=MONO, font_size=24, color=H["INK"], weight="BOLD").next_to(bar, RIGHT, buff=0.15)
            groups.add(VGroup(lab, bar, num))
        c.until("most people")
        c.run(LaggedStart(*[FadeIn(g, shift=RIGHT * 0.15) for g in groups], lag_ratio=0.25), rt=1.0)
        c.until("tie")
        tie = pill(f"TIE · {top} = {top}", H["CRIMSON"], size=24).move_to([0, -2.55, 0])
        c.run(FadeIn(tie, scale=0.9), rt=0.5)
        c.pad()


# ── B02 — GROUP BY collapses (top band) vs window function keeps rows (bottom) ─

class B02_WindowVsGroupBy(Scene):
    def construct(self):
        c = Clock(self, "B02")
        u = TIED[0]
        mk = lambda s, col=H["INK"], size=20: Text(s, font=MONO, font_size=size, color=col)
        lt = mk("GROUP BY user_id", H["CRIMSON"], 26).move_to([0, 3.1, 0])
        rule = Line([-1.9, 0.0, 0], [1.9, 0.0, 0], color=H["INK"], stroke_width=2).set_opacity(0.35)
        rt = mk("window function", H["TEAL"], 26).move_to([0, -0.45, 0])
        c.run(FadeIn(lt), FadeIn(rule), FadeIn(rt), rt=0.5)

        left_rows = VGroup(*[mk(f"{u} · {t} · {n}") for t, n, _ in RANK101]).arrange(DOWN, buff=0.22).move_to([0, 2.0, 0])
        c.run(FadeIn(left_rows), rt=0.5)
        c.until("collapses")
        collapsed = pill(f"user {u} · {TOTALS[u]} plays", H["CRIMSON"], size=24).move_to([0, 2.05, 0])
        gone = fit(Text("one row left — no track to rank", font=SERIF, font_size=20, color=H["SEC"], slant="ITALIC"),
                   3.8).next_to(collapsed, DOWN, buff=0.3)
        c.run(ReplacementTransform(left_rows, collapsed), rt=0.8)
        c.run(FadeIn(gone), rt=0.4)

        c.until("computes")
        right_rows = VGroup(*[mk(f"{t} · {n} · rank {r}", H["TEAL"] if r == 1 else H["INK"], 22)
                              for t, n, r in RANK101]).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        fit(right_rows, 3.45).move_to([0.2, -1.35, 0])
        c.run(LaggedStart(*[FadeIn(r, shift=LEFT * 0.15) for r in right_rows], lag_ratio=0.25), rt=0.9)
        c.until("partition")
        part = mk("PARTITION BY user_id", H["SLATE"], 20).next_to(right_rows, DOWN, buff=0.35).set_x(0)
        c.run(FadeIn(part), rt=0.4)
        c.until("order by")
        order = mk("ORDER BY plays DESC", H["SLATE"], 20).next_to(part, DOWN, buff=0.15).set_x(0)
        arrow = Arrow(right_rows.get_corner(UL) + LEFT * 0.2 + UP * 0.05,
                      right_rows.get_corner(DL) + LEFT * 0.2 + DOWN * 0.05, color=H["TEAL"], buff=0, stroke_width=5)
        c.run(FadeIn(order), GrowArrow(arrow), rt=0.5)
        c.pad()


# ── B05 / B08 — the rows that come back ───────────────────────────────────────

ROW_Y = [1.55, 0.75, -0.05, -0.85]


def result_row(i, uid, track, plays, color):
    t = VGroup(Text(f"user {uid}", font=MONO, font_size=26, color=color, weight="BOLD"),
               Text(f"{track} · {plays} plays", font=MONO, font_size=22, color=color)).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
    return t.move_to([-0.2, ROW_Y[i], 0])


def counter(n, users, color):
    return VGroup(Text(f"rows returned: {n}", font=MONO, font_size=26, color=color, weight="BOLD"),
                  Text(f"users: {users}", font=MONO, font_size=22, color=color)).arrange(DOWN, buff=0.1).move_to([0, 3.0, 0])


class B05_TopTrackBuggyOutput(Scene):
    def construct(self):
        c = Clock(self, "B05")
        rows = L.order_rows(BUGGY)
        ctr = counter(0, len(USERS), H["INK"])
        tag = Text("top_track_buggy.out", font=MONO, font_size=16, color=H["SEC"]).next_to(ctr, DOWN, buff=0.15)
        c.run(FadeIn(ctr), FadeIn(tag), rt=0.4)
        shown = 0
        c.until("102")
        for i, (u, t, n) in enumerate(rows):
            if u in TIED:
                break
            c.run(FadeIn(result_row(i, u, t, n, H["INK"]), shift=UP * 0.1),
                  Transform(ctr, counter(shown + 1, len(USERS), H["INK"])), rt=0.45)
            shown += 1
        c.until(f"{TIED[0]}")
        objs = [result_row(i, u, t, n, H["CRIMSON"]) for i, (u, t, n) in enumerate(rows) if u in TIED]
        c.run(*[FadeIn(o, shift=UP * 0.1) for o in objs], Transform(ctr, counter(len(rows), len(USERS), H["CRIMSON"])), rt=0.6)
        c.until("rank one")
        box = SurroundingRectangle(VGroup(*objs), color=H["CRIMSON"], buff=0.15, corner_radius=0.1, stroke_width=4)
        both = Text("both rank 1", font=SANS, font_size=22, color=H["CRIMSON"], weight="BOLD").next_to(box, DOWN, buff=0.2)
        c.run(Create(box), FadeIn(both), rt=0.5)
        c.until("three users")
        badge = pill(f"{len(rows)} rows for {len(USERS)} users", H["CRIMSON"], size=24).move_to([0, -2.6, 0])
        c.run(FadeIn(badge, scale=0.9), rt=0.4)
        c.pad()


class B08_TopTrackFixedOutput(Scene):
    def construct(self):
        c = Clock(self, "B08")
        rows = L.order_rows(FIXED)
        ctr = counter(0, len(USERS), H["INK"])
        tag = Text("top_track_fixed.out", font=MONO, font_size=16, color=H["SEC"]).next_to(ctr, DOWN, buff=0.15)
        c.run(FadeIn(ctr), FadeIn(tag), rt=0.4)
        for i, (u, t, n) in enumerate(rows):
            c.until(f"{u}")
            color = H["TEAL"] if u in TIED else H["INK"]
            done = i + 1 == len(rows)
            c.run(FadeIn(result_row(i, u, t, n, color), shift=UP * 0.1),
                  Transform(ctr, counter(i + 1, len(USERS), H["TEAL"] if done else H["INK"])), rt=0.45)
        c.until("tiebreaker")
        lost = [t for u, t, _ in BUGGY if u in TIED and (u, t) not in {(v, s) for v, s, _ in FIXED}][0]
        note = VGroup(Text(f"tie → {rows[-1][1]}", font=SANS, font_size=22, color=H["TEAL"], weight="BOLD"),
                      Text(f"(track_id ASC) · {lost} drops out", font=SANS, font_size=18, color=H["TEAL"])
                      ).arrange(DOWN, buff=0.08)
        fit(note, 3.8).move_to([0, -1.25, 0])
        c.run(FadeIn(note), rt=0.4)
        c.until("three users")
        badge = pill(f"{len(rows)} rows for {len(USERS)} users", H["TEAL"], size=24).move_to([0, -2.6, 0])
        c.run(FadeIn(badge, scale=0.9), rt=0.4)
        c.pad()


# ── B09 — SUMMARY ─────────────────────────────────────────────────────────────

class B09_Lesson(Scene):
    def construct(self):
        c = Clock(self, "B09")
        head = VGroup(Text("Rows returned", font=SERIF, font_size=34, color=H["INK"], weight="BOLD"),
                      Text("≠ correct", font=SERIF, font_size=34, color=H["INK"], weight="BOLD")).arrange(DOWN, buff=0.08)
        head.move_to([0, 2.85, 0])
        rule = Line(head.get_corner(DL) + DOWN * 0.12, head.get_corner(DR) + DOWN * 0.12, color=H["GOLD"], stroke_width=5)
        c.run(FadeIn(head), Create(rule), rt=0.5)
        quote = VGroup(*[Text(s, font=SERIF, font_size=24, color=H["INK"], slant="ITALIC")
                         for s in ["“AI output can pass", "a surface smell test", "and still be subtly wrong.”"]]
                       ).arrange(DOWN, buff=0.1)
        fit(quote, 3.4)
        box = RoundedRectangle(corner_radius=0.12, width=3.85, height=quote.height + 0.5, stroke_color=H["SLATE"],
                               stroke_width=3, fill_color="#FFFFFF", fill_opacity=1).move_to([0, 0.8, 0])
        quote.move_to(box)
        cite = Text("— the book, on AI tools", font=SANS, font_size=16, color=H["SEC"]).next_to(box, DOWN, buff=0.15)
        c.until("smell")
        c.run(FadeIn(box), FadeIn(quote), FadeIn(cite), rt=0.6)
        checks = VGroup()
        for line in ["Read the output.", "Count the rows."]:
            t = Text(line, font=SERIF, font_size=28, color=H["INK"], weight="BOLD")
            mark = Text("✓", font=SANS, font_size=28, color=H["TEAL"], weight="BOLD").next_to(t, LEFT, buff=0.2)
            checks.add(VGroup(mark, t))
        checks.arrange(DOWN, buff=0.45).move_to([0, -1.55, 0])
        boxes = [SurroundingRectangle(k, color=H["TEAL"], buff=0.18, corner_radius=0.1, stroke_width=3) for k in checks]
        c.until("read the output")
        c.run(*[FadeIn(k, shift=UP * 0.1) for k in checks], *[Create(b) for b in boxes], rt=0.5)
        c.pad()
