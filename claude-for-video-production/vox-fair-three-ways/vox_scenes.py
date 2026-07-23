"""vox_scenes.py — Why No Algorithm Can Be Fair Three Ways at Once
(vox-fair-three-ways, slate cut, 16:9).

One Scene per GRAPHIC/CARD/DOCUMENT/COMPOSITE-manim beat. Durations read from
this reel's beat_sheet.json (actuals after audio lock; estimates as fallback).
Render everything:
  bash scripts/vox_run.sh reels/vox-fair-three-ways

Numbers verified via Chouldechova's relation (FACTCHECK.md). The calibration
state uses the CORRECTED set (chapter's table B-row was inconsistent).
Color law: blue #5B7B9C = group A, terracotta #D35F43 = group B — GROUP
IDENTITY, morally neutral in this film.
"""
import sys, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve()
                       .parents[2] / "aspects/explainer/vox-explainer/manim"))
from vox_graphics import *   # noqa: F401,F403
from vox_graphics import _quote_scene, MONO
import numpy as np

DUR = {"B01": 10.4, "B03": 7.2, "B04": 7.6, "B05": 8.4, "B06": 9.6,
       "B07": 10.4, "B08": 10.4, "B09": 9.6, "B10": 10.0, "B11": 10.0,
       "B12": 9.2}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s")
                                    or b.get("estimated_duration_s") or 6.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ------------------------------------------------------- the two-row device

def _group_rows(fill_a=0, fill_b=0, y_a=0.9, y_b=-0.9, size=0.42, gap=0.3):
    rows = {}
    for key, color, y in (("a", BLUE, y_a), ("b", TERRA, y_b)):
        row = VGroup()
        for i in range(10):
            sq = Square(size).set_stroke(color, 2.5).set_fill(color, 0.0)
            sq.move_to(np.array([-3.2 + i * (size + gap), y, 0.0]))
            row.add(sq)
        lab = SerifLabel("group A" if key == "a" else "group B",
                         color, size=24)
        lab.next_to(row, LEFT, buff=0.6)
        rows[key] = (row, lab)
    n = {"a": fill_a, "b": fill_b}
    for key in ("a", "b"):
        for sq in rows[key][0][:n[key]]:
            sq.set_fill(BLUE if key == "a" else TERRA, 1.0)
    return rows


# ------------------------------------------------------- the machine device

HONEST = {"tpr": (".83", ".50"), "fpr": (".20", ".04"), "ppv": (".86", ".84")}
EQODDS = {"tpr": (".70", ".70"), "fpr": (".15", ".15"), "ppv": (".88", ".67")}

_PANEL_X0, _PANEL_X1 = -5.5, -0.9
_ROW_Y = {"tpr": 1.55, "fpr": 0.35, "ppv": -0.85}
_COL_X = {"a": 2.85, "b": 4.35}


def _score_x(t):
    return _PANEL_X0 + 0.15 + t * (_PANEL_X1 - _PANEL_X0 - 0.3)


def _bump(base_y, mean, color):
    """A smooth score-distribution bump; same family for both groups —
    the base-rate difference is the ONLY asymmetry (FACTCHECK rule)."""
    v = VMobject(color=color, stroke_width=4)
    xs = np.linspace(0.02, 0.98, 60)
    pts = [np.array([_score_x(t),
                     base_y + 1.15 * np.exp(-((t - mean) ** 2) / 0.045),
                     0.0]) for t in xs]
    v.set_points_smoothly(pts)
    return v


def _panels():
    a_base = Line([_PANEL_X0, 0.85, 0], [_PANEL_X1, 0.85, 0],
                  color=INK, stroke_width=2)
    b_base = Line([_PANEL_X0, -1.95, 0], [_PANEL_X1, -1.95, 0],
                  color=INK, stroke_width=2)
    a_curve = _bump(0.85, 0.62, BLUE)
    b_curve = _bump(-1.95, 0.38, TERRA)
    lab_a = SerifLabel("group A", BLUE, size=22)
    lab_a.move_to(np.array([_PANEL_X0 + 0.8, 2.55, 0]))
    lab_b = SerifLabel("group B", TERRA, size=22)
    lab_b.move_to(np.array([_PANEL_X1 - 0.8, -0.35, 0]))
    return VGroup(a_base, b_base, a_curve, b_curve, lab_a, lab_b)


def _threshold(base_y, t, color=INK):
    x = _score_x(t)
    return Line([x, base_y - 0.12, 0], [x, base_y + 1.45, 0],
                color=color, stroke_width=3)


def _table_static():
    g = VGroup()
    heads = (("A", BLUE, _COL_X["a"]), ("B", TERRA, _COL_X["b"]))
    for txt, color, x in heads:
        h = SerifLabel(txt, color, size=28)
        h.move_to(np.array([x, 2.45, 0]))
        g.add(h)
    names = (("misses caught", "tpr"), ("false alarms", "fpr"),
             ("a ‘yes’ is right", "ppv"))
    for txt, key in names:
        t = Text(txt, font=SERIF, color=INK, font_size=24)
        if t.width > 2.1:
            t.scale_to_fit_width(2.1)
        t.move_to(np.array([1.15, _ROW_Y[key], 0]))
        g.add(t)
    return g


def _table_nums(state):
    g = VGroup()
    for key in ("tpr", "fpr", "ppv"):
        for col, x in (("a", _COL_X["a"]), ("b", _COL_X["b"])):
            v = state[key][0 if col == "a" else 1]
            n = Text(v, font=MONO, color=INK, font_size=34, weight=BOLD)
            n.move_to(np.array([x, _ROW_Y[key], 0]))
            g.add(n)
    return g


# ---------------------------------------------------------------- scenes

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("THE IMPOSSIBILITY THEOREM", font=SERIF, color=BLUE,
                   font_size=24)
        t1 = Text("Why no algorithm can be fair", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        t2 = Text("three ways at once", font=SERIF, color=INK,
                  font_size=50, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.2)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=TERRA, stroke_width=2)
        eye.next_to(block, UP, buff=0.8)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.5, total - 1.8))


class B03_Definition1(Scene):
    def construct(self):
        total = DUR["B03"]
        title = SerifLabel("1 · equal yes-rates", NAVY, size=28)
        title.to_edge(UP, buff=0.6)
        rows = _group_rows(0, 0)
        self.play(FadeIn(title),
                  *[FadeIn(rows[k][0]) for k in ("a", "b")],
                  *[FadeIn(rows[k][1]) for k in ("a", "b")], run_time=0.9)
        fills = []
        for key, color in (("a", BLUE), ("b", TERRA)):
            fills += [sq.animate.set_fill(color, 1.0)
                      for sq in rows[key][0][:4]]
        self.play(LaggedStart(*fills, lag_ratio=0.08, run_time=1.8))
        self.wait(max(0.5, total - 2.7))


class B04_Definition2(Scene):
    def construct(self):
        total = DUR["B04"]
        title = SerifLabel("2 · equal error rates", NAVY, size=28)
        title.to_edge(UP, buff=0.6)
        rows = _group_rows(4, 4)
        self.add(rows["a"][0], rows["a"][1], rows["b"][0], rows["b"][1])
        self.play(FadeIn(title), run_time=0.6)
        c1 = LabelChip("false alarms — equal", accent=SLATE, size=24)
        c1.move_to(UP * 2.0 + RIGHT * 0.4)
        c1.rotate(-0.02 * PI)
        c2 = LabelChip("misses — equal", accent=SLATE, size=24)
        c2.move_to(DOWN * 2.3 + RIGHT * 0.4)
        c2.rotate(0.02 * PI)
        self.play(FadeIn(c1, shift=DOWN * 0.2), run_time=0.8)
        self.play(FadeIn(c2, shift=UP * 0.2), run_time=0.8)
        self.wait(max(0.5, total - 2.2))


class B05_Definition3(Scene):
    def construct(self):
        total = DUR["B05"]
        title = SerifLabel("3 · an honest score", NAVY, size=28)
        title.to_edge(UP, buff=0.6)
        chip = LabelChip("the model says: 70%", accent=SLATE, size=26)
        chip.next_to(title, DOWN, buff=0.45)
        rows = _group_rows(0, 0, y_a=0.55, y_b=-1.25)
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(chip, shift=DOWN * 0.15),
                  *[FadeIn(rows[k][0]) for k in ("a", "b")],
                  *[FadeIn(rows[k][1]) for k in ("a", "b")], run_time=0.9)
        fills = []
        for key, color in (("a", BLUE), ("b", TERRA)):
            fills += [sq.animate.set_fill(color, 1.0)
                      for sq in rows[key][0][:7]]
        self.play(LaggedStart(*fills, lag_ratio=0.06, run_time=2.0))
        self.wait(max(0.5, total - 3.4))


class B06_AnyTwo(Scene):
    def construct(self):
        _quote_scene(self, "You can have any two. Not three.",
                     "— Kleinberg, Mullainathan & Raghavan · "
                     "Chouldechova, 2016", None, "two", DUR["B06"])


class B07_TheMachine(Scene):
    def construct(self):
        total = DUR["B07"]
        panels = _panels()
        thr_a = _threshold(0.85, 0.5)
        thr_b = _threshold(-1.95, 0.5)
        table = _table_static()
        nums = _table_nums(HONEST)
        self.play(Create(panels[2]), Create(panels[3]),
                  FadeIn(panels[0]), FadeIn(panels[1]),
                  FadeIn(panels[4]), FadeIn(panels[5]), run_time=1.6)
        self.play(Create(thr_a), Create(thr_b), run_time=0.8)
        self.play(FadeIn(table), run_time=0.7)
        self.play(FadeIn(nums), run_time=0.9)
        self.wait(max(0.5, total - 4.0))


class B08_EqualizeErrors(Scene):
    def construct(self):
        total = DUR["B08"]
        panels = _panels()
        thr_a = _threshold(0.85, 0.5)
        thr_b = _threshold(-1.95, 0.5)
        table = _table_static()
        nums = _table_nums(HONEST)
        self.add(panels, thr_a, thr_b, table, nums)
        self.play(Transform(thr_b, _threshold(-1.95, 0.6)),
                  Transform(nums, _table_nums(EQODDS)), run_time=1.6)
        e1 = LabelChip("EQUAL", accent=SLATE, size=20)
        e1.move_to(np.array([5.45, _ROW_Y["tpr"], 0]))
        e2 = LabelChip("EQUAL", accent=SLATE, size=20)
        e2.move_to(np.array([5.45, _ROW_Y["fpr"], 0]))
        self.play(FadeIn(e1, scale=0.9), FadeIn(e2, scale=0.9), run_time=0.7)
        self.wait(max(0.5, total - 2.3))


class B09_HonestAgain(Scene):
    def construct(self):
        total = DUR["B09"]
        panels = _panels()
        thr_a = _threshold(0.85, 0.5)
        thr_b = _threshold(-1.95, 0.6)
        table = _table_static()
        nums = _table_nums(EQODDS)
        self.add(panels, thr_a, thr_b, table, nums)
        self.play(Transform(thr_b, _threshold(-1.95, 0.5)),
                  Transform(nums, _table_nums(HONEST)), run_time=1.6)
        zone = Rectangle(width=5.2, height=2.15)
        zone.set_stroke(width=0).set_fill(opacity=0)
        zone.move_to(np.array([2.75, (_ROW_Y["tpr"] + _ROW_Y["fpr"]) / 2, 0]))
        ring = HandRing(zone, color=TERRA)     # the film's single ring
        self.play(Create(ring), run_time=1.0)
        self.wait(max(0.5, total - 2.6))


class B10_TheTriangle(Scene):
    def construct(self):
        total = DUR["B10"]
        pos = {"yes": np.array([0.0, 2.15, 0.0]),
               "err": np.array([-3.6, -1.5, 0.0]),
               "hon": np.array([3.6, -1.5, 0.0])}
        nodes = {}
        for key, txt in (("yes", "equal yeses"), ("err", "equal errors"),
                         ("hon", "honest score")):
            t = Text(txt, font=SERIF, color=INK, font_size=32, weight=BOLD)
            t.move_to(pos[key])
            nodes[key] = t
        def edge(k1, k2):
            d = pos[k2] - pos[k1]
            u = d / np.linalg.norm(d)
            return Line(pos[k1] + u * 1.3, pos[k2] - u * 1.3,
                        color=INK, stroke_width=2)
        edges = VGroup(edge("yes", "err"), edge("yes", "hon"),
                       edge("err", "hon"))
        self.play(*[FadeIn(nodes[k]) for k in nodes], Create(edges),
                  run_time=1.3)

        def bar(node):
            r = Rectangle(width=node.width + 0.3, height=node.height + 0.22)
            r.set_fill(GOLD, 0.55).set_stroke(width=0)
            r.move_to(node)
            r._qc_intentional = True
            return r

        def strike(node):
            g = VGroup(
                Line(node.get_corner(UL) + UL * 0.12,
                     node.get_corner(DR) + DR * 0.12,
                     color=TERRA, stroke_width=6),
                Line(node.get_corner(UR) + UR * 0.12,
                     node.get_corner(DL) + DL * 0.12,
                     color=TERRA, stroke_width=6))
            for m in g:
                m._qc_intentional = True
            return g

        # pick two: yeses + errors -> honest score snaps
        b1, b2 = bar(nodes["yes"]), bar(nodes["err"])
        x1 = strike(nodes["hon"])
        nodes["yes"].set_z_index(1)
        nodes["err"].set_z_index(1)
        nodes["hon"].set_z_index(1)
        self.add(b1, b2)
        self.play(FadeIn(x1), run_time=0.8)
        self.wait(1.2)
        # rotate the pick: errors + honest -> yeses snaps
        b1_new, b2_new = bar(nodes["err"]), bar(nodes["hon"])
        x2 = strike(nodes["yes"])
        self.play(Transform(b1, b1_new), Transform(b2, b2_new),
                  FadeOut(x1), run_time=0.9)
        self.play(FadeIn(x2), run_time=0.7)
        self.wait(max(0.5, total - 4.9))


class B11_WhichWins(Scene):
    def construct(self):
        _quote_scene(self, "Which fairness should win?",
                     "— not a technical question", None,
                     "win", DUR["B11"])


class B12_End(Scene):
    def construct(self):
        total = DUR["B12"]
        t1 = Text("Fairness is a choice.", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        t2 = Text("The theorem just makes it honest.", font=SERIF, color=INK,
                  font_size=48, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.22).move_to(UP * 0.3)
        u = Line(t2.get_corner(DL) + DOWN * 0.16, t2.get_corner(DR) + DOWN * 0.16,
                 color=BLUE, stroke_width=2)
        s = Text("from Computational Skepticism for AI — chapter 7",
                 font=SERIF, color=INK, font_size=26)
        s.next_to(u, DOWN, buff=0.5)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(FadeIn(t2), Create(u), run_time=0.9)
        self.play(FadeIn(s, shift=UP * 0.1), run_time=0.6)
        self.wait(max(0.5, total - 2.3))
