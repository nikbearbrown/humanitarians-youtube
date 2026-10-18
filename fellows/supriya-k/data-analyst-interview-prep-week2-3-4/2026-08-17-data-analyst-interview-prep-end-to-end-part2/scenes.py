"""
Manim scenes for hai-sql-window-functions-tie-bug (cli-explainer) — v2.
5 scenes for the GRAPHIC-lane beats: B01, B02, B05, B08, B09.
Humanitarians palette (matches runtime/remotion/src/tokens/humanitarians.ts).
Scene classes must be declared as plain Scene subclasses named B0X_Name — run.sh finds them by regex.
No LaTeX (Text/Pango only).

THE RECEIPT (ACTUAL-CODE LAW): every row and number on screen is parsed at render time
from the real query output in `sql/*.out` (SQLite runs of `sql/*.sql` against the Loopr
fixture `sql/plays.sql`) — nothing is typed in by hand. Change the data or a query, re-run
it, re-render; the scenes follow.

Every scene carries the "Supriya" corner handle (PM requirement 4 / LOGO LAW) — `handle()`.
v1's output beats drew their rows INK-on-INK (invisible); v2 renders every beat on the
cream stage.

TIMING: DUR is read from beat_sheet.json — `actual_duration_s` once audio exists,
`estimated_duration_s` before. Narration cues are placed by the cue phrase's word position
in that beat's narration_text, scaled to DUR, so regenerated audio re-times the scenes
without hand edits. Never hand-trim an mp4.
"""

from manim import *
from pathlib import Path
import json

# run.sh's Gate A/W pre-flights execute an ISOLATED COPY of scenes.py in a temp dir,
# so fall back to the reel's real location for the data and the timing.
_REEL = Path("/Users/supriyakushwaha/Documents/ai1-cli/brutalist.art/projects/data-analyst-interview-prep-week2-3-4/2026-08-17-data-analyst-interview-prep-end-to-end-part2")
HERE = Path(__file__).resolve().parent
if not (HERE / "sql").is_dir():
    HERE = _REEL

H = {
    "CREAM": "#F3EBDD",
    "INK": "#2F2A26",
    "TEAL": "#1F4E5F",
    "CRIMSON": "#E4572E",
    "SLATE": "#29335C",
    "GOLD": "#F3A712",
    "DIM": "#B9B2A6",
    "SEC": "#6B6357",
}
SERIF = "EB Garamond"
SANS = "Montserrat"
MONO = "PT Mono"

# ── data: the real query output ───────────────────────────────────────────────

def read_out(name):
    """Parse a sqlite3 `-header -column` .out file into a list of dicts."""
    lines = [l for l in (HERE / "sql" / name).read_text().splitlines() if l.strip()]
    rule = lines[1]                                   # the "----  ----" line gives column spans
    spans, i = [], 0
    while i < len(rule):
        if rule[i] == "-":
            j = i
            while j < len(rule) and rule[j] == "-":
                j += 1
            spans.append((i, j)); i = j
        else:
            i += 1
    cut = lambda l: [l[a:(spans[k + 1][0] if k + 1 < len(spans) else None)].strip()
                     for k, (a, _) in enumerate(spans)]
    head = cut(lines[0])
    return [dict(zip(head, cut(l))) for l in lines[2:]]


TOTALS = {int(r["user_id"]): int(r["plays"]) for r in read_out("group_by_collapse.out")}
COUNTS = [(int(r["user_id"]), r["track_id"], int(r["plays"])) for r in read_out("counts_by_track.out")]
RANK101 = [(r["track_id"], int(r["plays"]), int(r["rnk"])) for r in read_out("rank_user_101.out")]
BUGGY = [(int(r["user_id"]), r["track_id"], int(r["plays"])) for r in read_out("top_track_buggy.out")]
FIXED = [(int(r["user_id"]), r["track_id"], int(r["plays"])) for r in read_out("top_track_fixed.out")]
USERS = sorted(TOTALS)
TIED = sorted({u for u, *_ in BUGGY if sum(1 for v, *_ in BUGGY if v == u) > 1})
assert TIED == [101] and len(BUGGY) == 4 and len(FIXED) == 3, "fixture no longer shows the tie"

# ── timing: from the beat sheet ───────────────────────────────────────────────

BEATS = {b["beat_id"]: b for b in json.loads((HERE / "beat_sheet.json").read_text())["beats"]}


def dur(bid):
    b = BEATS[bid]
    return float(b.get("actual_duration_s") or b["estimated_duration_s"])


def _norm(w):
    return w.strip(".,:;!?\"'").lower()


def cue(bid, phrase):
    """Seconds into the beat where `phrase` starts, by word position in the narration."""
    words = BEATS[bid]["narration_text"].split()
    target = phrase.split()
    for i in range(len(words) - len(target) + 1):
        if [_norm(w) for w in words[i:i + len(target)]] == [_norm(t) for t in target]:
            return dur(bid) * i / len(words)
    raise ValueError(f"{bid}: cue phrase not in narration: {phrase!r}")


def handle(scene):
    """Visible author handle, lower-right inside the safe area, on from frame 0."""
    h = Text("Supriya", font=SANS, color=H["INK"], font_size=26, weight="BOLD").set_opacity(0.75)
    h.to_corner(DR, buff=0.9)
    scene.add(h)
    return h


class Clock:
    """A beat's running clock. Scenes stay plain `(Scene)` subclasses and open with
    `c = Clock(self, "B0X")`. `until(phrase)` waits to that cue; `pad()` holds to the
    end of the beat's audio."""

    def __init__(self, scene, bid):
        self.s, self.bid, self.t = scene, bid, 0.0
        self.DUR = dur(bid)
        scene.camera.background_color = H["CREAM"]
        handle(scene)

    def run(self, *anims, rt=0.6):
        self.s.play(*anims, run_time=rt)
        self.t += rt

    def until(self, phrase):
        at = cue(self.bid, phrase)
        if at > self.t:
            self.s.wait(at - self.t)
            self.t = at

    def pad(self):
        self.s.wait(max(0.4, self.DUR - self.t - 0.2))


def title(text, size=40):
    return Text(text, font=SERIF, font_size=size, color=H["INK"], weight="BOLD").to_edge(UP, buff=0.7)


def pill(text, color, text_color="#FFFFFF", size=30, pad=0.6):
    t = Text(text, font=SANS, font_size=size, color=text_color, weight="BOLD")
    bg = RoundedRectangle(corner_radius=0.14, width=t.width + pad, height=t.height + 0.42,
                          stroke_width=0, fill_color=color, fill_opacity=1)
    return VGroup(bg, t.move_to(bg))


# ── B01 — PROBLEM: the tie hiding in the log ──────────────────────────────────

class B01_ProblemStakes(Scene):
    def construct(self):
        c = Clock(self, "B01")
        head = Text("plays(user_id, track_id, played_at)", font=MONO, font_size=36, color=H["INK"],
                    weight="BOLD").to_edge(UP, buff=0.7)
        sub = Text("Loopr — the book's invented streaming service", font=SERIF, font_size=28,
                   color=H["SEC"], slant="ITALIC").next_to(head, DOWN, buff=0.25)
        c.run(FadeIn(head), FadeIn(sub), rt=0.6)

        u101 = [(t, n) for u, t, n in COUNTS if u == TIED[0]]
        top = max(n for _, n in u101)
        rows, bars = VGroup(), VGroup()
        for k, (track, n) in enumerate(u101):
            y = 1.0 - k * 1.25
            lab = Text(f"user {TIED[0]} · {track}", font=MONO, font_size=30, color=H["INK"])
            lab.move_to([-1.6, y, 0], aligned_edge=RIGHT)
            w = 4.2 * n / top
            bar = Rectangle(width=w, height=0.78, stroke_width=0,
                            fill_color=H["TEAL"] if n == top else H["DIM"], fill_opacity=1)
            bar.move_to([-1.3 + w / 2, y, 0])
            num = Text(str(n), font=MONO, font_size=34, color=H["INK"], weight="BOLD").next_to(bar, RIGHT, buff=0.25)
            rows.add(lab); bars.add(VGroup(bar, num))
        c.until("most people")
        c.run(FadeIn(rows), rt=0.5)
        c.run(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.2), rt=1.0)
        c.until("tie")
        brace = Brace(VGroup(bars[0], bars[1]), direction=RIGHT, color=H["CRIMSON"], buff=0.25)
        tie = pill("TIE", H["CRIMSON"], size=34).next_to(brace, RIGHT, buff=0.25)
        c.run(GrowFromCenter(brace), FadeIn(tie, shift=LEFT * 0.2), rt=0.6)
        c.pad()


# ── B02 — PROBLEM: GROUP BY collapses, a window function keeps the rows ───────

class B02_WindowVsGroupBy(Scene):
    def construct(self):
        c = Clock(self, "B02")
        u = TIED[0]
        divider = Line([0, 2.9, 0], [0, -2.9, 0], color=H["INK"], stroke_width=2).set_opacity(0.35)
        lt = Text("GROUP BY user_id", font=MONO, font_size=34, color=H["CRIMSON"], weight="BOLD").move_to([-3.45, 2.85, 0])
        rt = Text("window function", font=MONO, font_size=34, color=H["TEAL"], weight="BOLD").move_to([3.45, 2.85, 0])
        c.run(FadeIn(divider), FadeIn(lt), FadeIn(rt), rt=0.5)

        mk = lambda s, col=H["INK"], size=30: Text(s, font=MONO, font_size=size, color=col)
        left_rows = VGroup(*[mk(f"{u} · {t} · {n}") for t, n, _ in RANK101]).arrange(DOWN, buff=0.45)
        left_rows.move_to([-3.45, 0.9, 0])
        c.run(FadeIn(left_rows), rt=0.5)
        c.until("collapses")
        collapsed = pill(f"user {u} · {TOTALS[u]} plays", H["CRIMSON"], size=32).move_to([-3.45, 0.9, 0])
        gone = Text("one row left — no track to rank", font=SERIF, font_size=28, color=H["SEC"],
                    slant="ITALIC").next_to(collapsed, DOWN, buff=0.45)
        c.run(ReplacementTransform(left_rows, collapsed), rt=0.8)
        c.run(FadeIn(gone), rt=0.4)

        c.until("computes")
        right_rows = VGroup(*[mk(f"{t} · {n} · rank {r}", H["TEAL"] if r == 1 else H["INK"])
                              for t, n, r in RANK101]).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        right_rows.move_to([3.45, 0.9, 0])
        c.run(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in right_rows], lag_ratio=0.25), rt=0.9)
        c.until("partition")
        part = mk("PARTITION BY user_id", H["SLATE"], 26)
        part.next_to(right_rows, DOWN, buff=0.6).set_x(3.45)
        c.run(FadeIn(part), rt=0.4)
        c.until("order by")
        order = mk("ORDER BY plays DESC", H["SLATE"], 26).next_to(part, DOWN, buff=0.3).set_x(3.45)
        arrow = Arrow(right_rows.get_corner(UL) + LEFT * 0.35 + UP * 0.1,
                      right_rows.get_corner(DL) + LEFT * 0.35 + DOWN * 0.1,
                      color=H["TEAL"], buff=0, stroke_width=6)
        c.run(FadeIn(order), GrowArrow(arrow), rt=0.5)
        c.pad()


# ── B05 / B08 — OUTPUT: the rows that come back ───────────────────────────────

ROW_Y = [1.15, 0.2, -0.75, -1.7]


def result_row(i, uid, track, plays, color):
    txt = Text(f"user {uid}   {track}   {plays} plays", font=MONO, font_size=40, color=color, weight="BOLD")
    txt.move_to([-1.0, ROW_Y[i], 0])
    return txt


def counter(n, users, color):
    return Text(f"rows returned: {n}   ·   users: {users}", font=MONO, font_size=34, color=color,
                weight="BOLD").to_edge(UP, buff=0.75)


def order_rows(rows):
    """Clean users first, then the tied user — the order the narration walks them."""
    return sorted(rows, key=lambda r: (r[0] in TIED, r[0], r[1]))


class B05_TopTrackBuggyOutput(Scene):
    def construct(self):
        c = Clock(self, "B05")
        rows = order_rows(BUGGY)
        ctr = counter(0, len(USERS), H["INK"])
        tag = Text("top_track_buggy.out", font=MONO, font_size=24, color=H["SEC"]).next_to(ctr, DOWN, buff=0.2)
        c.run(FadeIn(tag), FadeIn(ctr), rt=0.4)
        shown = 0
        c.until("102")
        for i, (u, t, n) in enumerate(rows):
            if u in TIED:
                break
            new = counter(shown + 1, len(USERS), H["INK"])
            c.run(FadeIn(result_row(i, u, t, n, H["INK"]), shift=UP * 0.15), Transform(ctr, new), rt=0.45)
            shown += 1
        c.until(f"{TIED[0]}")
        tied = [(i, r) for i, r in enumerate(rows) if r[0] in TIED]
        objs = [result_row(i, u, t, n, H["CRIMSON"]) for i, (u, t, n) in tied]
        new = counter(len(rows), len(USERS), H["CRIMSON"])
        c.run(*[FadeIn(o, shift=UP * 0.15) for o in objs], Transform(ctr, new), rt=0.6)
        c.until("rank one")
        box = SurroundingRectangle(VGroup(*objs), color=H["CRIMSON"], buff=0.22, corner_radius=0.12, stroke_width=5)
        both = Text("both rank 1", font=SANS, font_size=28, color=H["CRIMSON"], weight="BOLD").next_to(box, RIGHT, buff=0.2)
        c.run(Create(box), FadeIn(both), rt=0.5)
        c.until("three users")
        badge = pill(f"{len(rows)} rows for {len(USERS)} users", H["CRIMSON"], size=34).move_to([0, -2.85, 0])
        c.run(FadeIn(badge, scale=0.9), rt=0.4)
        c.pad()


class B08_TopTrackFixedOutput(Scene):
    def construct(self):
        c = Clock(self, "B08")
        rows = order_rows(FIXED)
        ctr = counter(0, len(USERS), H["INK"])
        tag = Text("top_track_fixed.out", font=MONO, font_size=24, color=H["SEC"]).next_to(ctr, DOWN, buff=0.2)
        c.run(FadeIn(tag), FadeIn(ctr), rt=0.4)
        for i, (u, t, n) in enumerate(rows):
            c.until(f"{u}")
            color = H["TEAL"] if u in TIED else H["INK"]
            new = counter(i + 1, len(USERS), H["TEAL"] if i + 1 == len(rows) else H["INK"])
            c.run(FadeIn(result_row(i, u, t, n, color), shift=UP * 0.15), Transform(ctr, new), rt=0.45)
        c.until("tiebreaker")
        lost = [t for u, t, _ in BUGGY if u in TIED and (u, t) not in {(v, s) for v, s, _ in FIXED}][0]
        note = Text(f"tie → {rows[-1][1]} (track_id ASC) · {lost} drops out", font=SANS, font_size=30,
                    color=H["TEAL"], weight="BOLD").next_to(ROW_Y[len(rows) - 1] * UP + LEFT * 1.0, DOWN, buff=0.55)
        c.run(FadeIn(note), rt=0.4)
        c.until("three users")
        badge = pill(f"{len(rows)} rows for {len(USERS)} users", H["TEAL"], size=34).move_to([0, -2.85, 0])
        c.run(FadeIn(badge, scale=0.9), rt=0.4)
        c.pad()


# ── B09 — SUMMARY ─────────────────────────────────────────────────────────────

class B09_Lesson(Scene):
    def construct(self):
        c = Clock(self, "B09")
        head = title("Rows returned ≠ correct", size=46)
        rule = Line(head.get_corner(DL) + DOWN * 0.15, head.get_corner(DR) + DOWN * 0.15,
                    color=H["GOLD"], stroke_width=6)
        c.run(FadeIn(head), Create(rule), rt=0.5)
        quote_box = RoundedRectangle(corner_radius=0.16, width=11.6, height=1.7, stroke_color=H["SLATE"],
                                     stroke_width=3, fill_color="#FFFFFF", fill_opacity=1).move_to([0, 0.9, 0])
        quote = VGroup(
            Text("“AI output can pass a surface smell test", font=SERIF, font_size=36, color=H["INK"], slant="ITALIC"),
            Text("and still be subtly wrong.”", font=SERIF, font_size=36, color=H["INK"], slant="ITALIC"),
        ).arrange(DOWN, buff=0.12).move_to(quote_box)
        cite = Text("— the book, on AI tools", font=SANS, font_size=24, color=H["SEC"]).next_to(quote_box, DOWN, buff=0.2)
        c.until("smell")
        c.run(FadeIn(quote_box), FadeIn(quote), FadeIn(cite), rt=0.6)
        checks = VGroup()
        for k, line in enumerate(["Read the output.", "Count the rows."]):
            t = Text(line, font=SERIF, font_size=44, color=H["INK"], weight="BOLD")
            mark = Text("✓", font=SANS, font_size=44, color=H["TEAL"], weight="BOLD").next_to(t, LEFT, buff=0.35)
            checks.add(VGroup(mark, t))
        checks.arrange(RIGHT, buff=1.4).move_to([0, -1.7, 0])
        boxes = [SurroundingRectangle(k, color=H["TEAL"], buff=0.3, corner_radius=0.14, stroke_width=4) for k in checks]
        c.until("read the output")
        c.run(*[FadeIn(k, shift=UP * 0.15) for k in checks], *[Create(b) for b in boxes], rt=0.5)
        c.pad()
