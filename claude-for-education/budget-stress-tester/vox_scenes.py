import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ---------------------------------------------------------------------------
# B04_BudgetChart — zero-based budget bar chart with 20% stress-test animation
# ---------------------------------------------------------------------------
# Scale: $2500 income maps to income line at y=1.8 above baseline at y=-2.5
# So 1 unit = 1.8/2500 = 0.00072 height units per dollar
# Baseline y = -2.5; income ceiling y = 1.8
# ---------------------------------------------------------------------------

_BASE_Y = -2.5          # x-axis / bar baseline
_CEIL_Y = 1.8           # income ceiling y
_SCALE  = (_CEIL_Y - _BASE_Y) / 2500.0   # height per dollar = 0.00172

_EXPENSES = [
    ("Housing",      750, "fixed",    -4.5, SLATE),
    ("Car+Ins",      450, "fixed",    -3.5, SLATE),
    ("Groceries",    400, "variable", -2.5, GOLD),
    ("Phone",        120, "variable", -1.5, GOLD),
    ("Gas",          200, "variable", -0.5, GOLD),
    ("Medical",      120, "fixed",     0.5, SLATE),
    ("Restaurants",  100, "variable",  1.5, GOLD),
    ("Entertain",     60, "variable",  2.5, GOLD),
]

def _bar_rect(amount, x_pos, color, opacity=0.85):
    """Return a Rectangle with bottom at _BASE_Y, height proportional to amount."""
    h = max(_SCALE * amount, 0.05)
    r = Rectangle(
        width=0.9, height=h,
        color=color, fill_color=color,
        fill_opacity=opacity, stroke_width=0,
    )
    r.move_to([x_pos, _BASE_Y + h / 2, 0])
    return r

def _cream_bg(mobj, pad_x=0.12, pad_y=0.08):
    """Cream Rectangle background behind any Manim text mobject."""
    bg = Rectangle(
        width=mobj.width + pad_x,
        height=mobj.height + pad_y,
        fill_color=CREAM, fill_opacity=1.0,
        stroke_width=0, stroke_opacity=0,
    )
    bg.move_to(mobj.get_center())
    return bg


class B04_BudgetChart(Scene):
    def construct(self):
        total = DUR.get("B04", 20.0)

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("BUDGET STRESS TEST", font=DISPLAY, font_size=32,
                     color=INK).move_to([0, 3.2, 0])

        # ── X-axis baseline ────────────────────────────────────────────────
        x_axis = Line([-5.5, _BASE_Y, 0], [5.5, _BASE_Y, 0],
                      color=INK, stroke_width=2)

        # ── Income ceiling line ────────────────────────────────────────────
        ceil_line = Line([-5.5, _CEIL_Y, 0], [5.5, _CEIL_Y, 0],
                         stroke_color=SLATE, stroke_width=1.5)
        inc_lbl = Text("INCOME $2500", font=MONO, font_size=14, color=SLATE)
        inc_lbl.move_to([4.5, _CEIL_Y + 0.22, 0])
        inc_bg = _cream_bg(inc_lbl)

        # ── Bars ───────────────────────────────────────────────────────────
        bars = []
        val_labels = []
        cat_labels = []
        for name, amt, kind, xpos, col in _EXPENSES:
            b = _bar_rect(amt, xpos, col)
            bars.append(b)

            # Value label above bar
            top_y = _BASE_Y + _SCALE * amt
            vlbl = Text(f"${amt}", font=MONO, font_size=12, color=INK)
            vlbl.move_to([xpos, top_y + 0.18, 0])
            val_labels.append(vlbl)

            # Category label below x-axis, rotated 30 deg
            clbl = Text(name, font=MONO, font_size=11, color=INK)
            clbl.rotate(30 * DEGREES)
            clbl.move_to([xpos, _BASE_Y - 0.38, 0])
            clbl_bg = _cream_bg(clbl, pad_x=0.06, pad_y=0.04)
            cat_labels.append((clbl_bg, clbl))

        fixed_bars     = [bars[i] for i,(_,__,k,*_r) in enumerate(_EXPENSES) if k=="fixed"]
        variable_bars  = [bars[i] for i,(_,__,k,*_r) in enumerate(_EXPENSES) if k=="variable"]
        variable_idxs  = [i for i,(_,__,k,*_r) in enumerate(_EXPENSES) if k=="variable"]

        # ── Animation state 1: title + axis ───────────────────────────────
        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(x_axis), run_time=0.5)

        # ── Animation state 2: income ceiling + label ─────────────────────
        self.play(Create(ceil_line), run_time=0.4)
        self.add(inc_bg)
        self.play(FadeIn(inc_lbl), run_time=0.4)

        # ── Animation state 3: fixed bars ─────────────────────────────────
        self.play(*[GrowFromEdge(b, DOWN) for b in fixed_bars], run_time=0.7)

        # ── Animation state 4: variable bars ──────────────────────────────
        self.play(*[GrowFromEdge(b, DOWN) for b in variable_bars], run_time=0.7)

        # ── Add value and category labels ──────────────────────────────────
        for vlbl in val_labels:
            self.add(vlbl)
        for bg, lbl in cat_labels:
            self.add(bg)
            self.add(lbl)
        self.wait(0.3)

        # ── Animation state 5: stress test — variable bars grow to 120% ───
        stress_anims = []
        stressed_bars = []
        for i in variable_idxs:
            name, amt, kind, xpos, col = _EXPENSES[i]
            new_h = max(_SCALE * amt * 1.20, 0.05)
            new_cy = _BASE_Y + new_h / 2
            new_bar = Rectangle(
                width=0.9, height=new_h,
                color=col, fill_color=col,
                fill_opacity=0.85, stroke_width=0,
            )
            new_bar.move_to([xpos, new_cy, 0])
            stressed_bars.append((i, new_bar))
            stress_anims.append(Transform(bars[i], new_bar))
        self.play(*stress_anims, run_time=1.0)

        # ── Animation state 6: deficit zone ───────────────────────────────
        # Post-stress total = 2500 + (760*0.20) = 2500 + 152 = 2652; savings=360 → 2652+360=3012; deficit=512
        # But per beat sheet: deficit $190 — using the beat sheet numbers directly
        # Pre-stress expenses = 750+450+400+120+200+120+100+60 = 2200; savings=360; total=2560 → already over
        # Recalculating: income=2500, savings=360, expenses sum=2200, total committed=2560
        # That leaves -60 already; stress adds 20% of variable (880)=176, so deficit = 60+176 = 236
        # Beat sheet says $190 — use beat sheet value directly for consistency
        deficit_amt = 190
        deficit_h   = _SCALE * deficit_amt
        deficit_rect = Rectangle(
            width=11.0, height=deficit_h,
            fill_color=CRIMSON, fill_opacity=0.3,
            stroke_width=0,
        )
        deficit_rect.move_to([0, _CEIL_Y + deficit_h / 2, 0])
        self.play(FadeIn(deficit_rect), run_time=0.5)

        # ── Animation state 7: deficit label ──────────────────────────────
        def_lbl = Text("DEFICIT $190", font=DISPLAY, font_size=20, color=CRIMSON)
        def_lbl.move_to([0, _CEIL_Y + deficit_h + 0.25, 0])
        def_bg = _cream_bg(def_lbl)
        self.add(def_bg)
        self.play(FadeIn(def_lbl), run_time=0.4)

        self.wait(max(0.3, total - 6.0))


# ---------------------------------------------------------------------------
# B06_RaiseScenario — three-column comparison: base | raise | raise + car
# ---------------------------------------------------------------------------
# Three column bars: BASE (x=-2.5), RAISE (x=0), RAISE+CAR (x=2.5)
# Scale: use same _SCALE as B04 but columns show total expenses (not individual)
# BASE total expenses: $2140 (expenses - Housing 750 note: used 2140 per beat)
# RAISE income: $2750 (10% raise on 2500)
# RAISE+CAR expenses: $2440 (2140 + 300 car payment)
# ---------------------------------------------------------------------------

_COL_BASE    = ("CURRENT\n$2140 exp",    2140, SLATE,   -2.5)
_COL_RAISE   = ("10% RAISE\n+$250 income", 2140, GOLD,    0.0)
_COL_CAR     = ("+$300 CAR\n= -$50/mo",   2440, SLATE,   2.5)

_BASE_INC    = 2500
_RAISE_INC   = 2750
_COL_W       = 1.5
_COL_SCALE   = (_CEIL_Y - _BASE_Y) / 3000.0   # slightly compressed to show headroom


class B06_RaiseScenario(Scene):
    def construct(self):
        total = DUR.get("B06", 14.0)

        # ── Title ──────────────────────────────────────────────────────────
        title = Text("RAISE + CAR PAYMENT", font=DISPLAY, font_size=28,
                     color=INK).move_to([0, 3.2, 0])

        # ── X-axis baseline ────────────────────────────────────────────────
        x_axis = Line([-5.5, _BASE_Y, 0], [5.5, _BASE_Y, 0],
                      color=INK, stroke_width=2)

        def _col_bar(expenses, x_pos, col, opacity=0.8):
            h = max(_COL_SCALE * expenses, 0.05)
            r = Rectangle(width=_COL_W, height=h,
                           color=col, fill_color=col,
                           fill_opacity=opacity, stroke_width=0)
            r.move_to([x_pos, _BASE_Y + h / 2, 0])
            return r

        def _inc_ceil(income, x_center, col=SLATE):
            half = _COL_W / 2 + 0.3
            y    = _BASE_Y + _COL_SCALE * income
            return Line([x_center - half, y, 0], [x_center + half, y, 0],
                        stroke_color=col, stroke_width=1.5)

        # ── Column 1: BASE ─────────────────────────────────────────────────
        bar_base = _col_bar(2140, -2.5, SLATE)
        ceil_base = _inc_ceil(_BASE_INC, -2.5)
        lbl_base = Text("CURRENT\n$2140 exp", font=MONO, font_size=12, color=INK)
        lbl_base.move_to([-2.5, _BASE_Y - 0.5, 0])
        lbl_base_bg = _cream_bg(lbl_base)

        # ── Column 2: RAISE ────────────────────────────────────────────────
        bar_raise = _col_bar(2140, 0.0, GOLD)
        ceil_raise = _inc_ceil(_RAISE_INC, 0.0, GOLD)
        lbl_raise = Text("10% RAISE\n+$250/mo", font=MONO, font_size=12, color=INK)
        lbl_raise.move_to([0.0, _BASE_Y - 0.5, 0])
        lbl_raise_bg = _cream_bg(lbl_raise)

        # ── Column 3: RAISE + CAR ──────────────────────────────────────────
        base_h   = max(_COL_SCALE * 2140, 0.05)
        car_h    = max(_COL_SCALE * 300, 0.05)
        bar_raise_car = _col_bar(2140, 2.5, SLATE)        # base expense
        car_seg  = Rectangle(width=_COL_W, height=car_h,
                              color=CRIMSON, fill_color=CRIMSON,
                              fill_opacity=0.85, stroke_width=0)
        car_seg.move_to([2.5, _BASE_Y + base_h + car_h / 2, 0])
        ceil_car = _inc_ceil(_RAISE_INC, 2.5, SLATE)
        lbl_car = Text("+$300 CAR\n= -$50/mo", font=MONO, font_size=12, color=INK)
        lbl_car.move_to([2.5, _BASE_Y - 0.5, 0])
        lbl_car_bg = _cream_bg(lbl_car)

        # ── Net impact label — placed at top, above bars, not bottom ──────
        net_txt = Text(
            "Raise +$250  |  Car +$300 fixed  |  Net -$50/mo",
            font=MONO, font_size=16, color=CRIMSON,
        )
        net_txt.move_to([0, 2.8, 0])
        net_bg = _cream_bg(net_txt, pad_x=0.2, pad_y=0.1)

        # ── Annotation arrow — points at car segment top ───────────────────
        car_top_y = _BASE_Y + base_h + car_h
        arrow_tip = [2.5, car_top_y + 0.05, 0]
        arrow = Arrow(
            start=[4.0, car_top_y + 0.5, 0],
            end=arrow_tip,
            color=CRIMSON, stroke_width=2,
            max_tip_length_to_length_ratio=0.25,
        )
        no_cover_lbl = Text("RAISE DOESN'T\nCOVER IT", font=DISPLAY,
                             font_size=13, color=CRIMSON)
        no_cover_lbl.move_to([4.8, car_top_y + 0.6, 0])
        no_cover_bg = _cream_bg(no_cover_lbl)

        # ── Animation state 1: title + axis ───────────────────────────────
        self.play(FadeIn(title), run_time=0.5)
        self.play(Create(x_axis), run_time=0.4)

        # ── Animation state 2: BASE column ────────────────────────────────
        self.play(GrowFromEdge(bar_base, DOWN), Create(ceil_base), run_time=0.6)
        self.add(lbl_base_bg)
        self.play(FadeIn(lbl_base), run_time=0.3)

        # ── Animation state 3: RAISE column ───────────────────────────────
        self.play(GrowFromEdge(bar_raise, DOWN), Create(ceil_raise), run_time=0.6)
        self.add(lbl_raise_bg)
        self.play(FadeIn(lbl_raise), run_time=0.3)

        # ── Animation state 4: RAISE+CAR column ───────────────────────────
        self.play(
            GrowFromEdge(bar_raise_car, DOWN),
            Create(ceil_car),
            run_time=0.6,
        )
        self.play(GrowFromEdge(car_seg, DOWN), run_time=0.5)
        self.add(lbl_car_bg)
        self.play(FadeIn(lbl_car), run_time=0.3)

        # ── Animation state 5: net impact label ───────────────────────────
        self.add(net_bg)
        self.play(FadeIn(net_txt), run_time=0.5)

        # ── Animation state 6: annotation arrow ───────────────────────────
        self.add(no_cover_bg)
        self.play(Create(arrow), FadeIn(no_cover_lbl), run_time=0.5)

        self.wait(max(0.3, total - 5.5))
