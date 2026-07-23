import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_FluencyTrap(Scene):
    def construct(self):
        # ---- Title ----
        title = Text(
            "The Fluency Trap: Polished Output Disarms Verification",
            font_size=26, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # ---- Column centers ----
        C1X = -4.65; C2X = -3.35; C3X = -0.55; C4X = 3.65

        # ---- Header row: INK background + CREAM text on it (gate sees on_shape=header_bg) ----
        header_bg = Rectangle(
            width=11.0, height=0.52,
            fill_color=INK, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, 2.3, 0))

        hd1 = Text("DOMAIN",             font_size=19, color=CREAM, weight=BOLD).move_to(header_bg)
        hd2 = Text("YEAR",               font_size=19, color=CREAM, weight=BOLD).move_to(header_bg)
        hd3 = Text("ERROR",              font_size=19, color=CREAM, weight=BOLD).move_to(header_bg)
        hd4 = Text("VERIFICATION CATCH", font_size=19, color=CREAM, weight=BOLD).move_to(header_bg)

        # Reposition each header text to its column center (gate already resolved on_shape above)
        hd1.move_to((C1X, 2.3, 0))
        hd2.move_to((C2X, 2.3, 0))
        hd3.move_to((C3X, 2.3, 0))
        hd4.move_to((C4X, 2.3, 0))

        header_row = VGroup(header_bg, hd1, hd2, hd3, hd4)

        # ---- Data rows ----
        ROW_H = 0.65
        ROW_Y = [1.5, 0.7, -0.1, -0.9, -1.7]
        ROW_BG = [CREAM, GOLD, CREAM, GOLD, CREAM]

        rows_data = [
            ("LEGAL",   "2023", "Mata v. Avianca:", "fabricated citations",      "Westlaw search"),
            ("LEGAL",   "2024", "Colorado atty:",   "hallucinated precedents",    "Pacer/Westlaw"),
            ("MEDICAL", "2020", "IBM Watson:",      "dangerous treatment recs",   "Clinical protocol"),
            ("FINANCE", "2023", "Deloitte AU:",     "hallucinated regulatory refs","Registry search"),
            ("LEGAL",   "2024", "UK Post Office:",  "errors masked as human",     "Audit log review"),
        ]

        row_groups = []
        for i, (dom, yr, err1, err2, catch) in enumerate(rows_data):
            ry = ROW_Y[i]
            rbg = ROW_BG[i]

            row_bg = Rectangle(
                width=11.0, height=ROW_H,
                fill_color=rbg, fill_opacity=1,
                stroke_width=0, stroke_opacity=0
            ).move_to((0, ry, 0))

            dom_t = Text(dom, font_size=18, color=CRIMSON, weight=BOLD).move_to((C1X, ry, 0))
            yr_t  = Text(yr,  font_size=18, color=SLATE).move_to((C2X, ry, 0))

            err_t1 = Text(err1, font_size=18, color=INK).move_to((C3X, ry + 0.15, 0))
            err_t2 = Text(err2, font_size=18, color=INK).move_to((C3X, ry - 0.15, 0))
            err_grp = VGroup(err_t1, err_t2)

            catch_t = Text(catch, font_size=18, color=PASS_CLR, weight=BOLD).move_to((C4X, ry, 0))

            grp = VGroup(row_bg, dom_t, yr_t, err_grp, catch_t)
            row_groups.append(grp)

        # ---- Catch column highlight outlines ----
        catch_outlines = VGroup()
        for ry in ROW_Y:
            outline = Rectangle(
                width=3.7, height=ROW_H,
                fill_opacity=0,
                stroke_color=PASS_CLR, stroke_width=3
            ).move_to((C4X, ry, 0))
            catch_outlines.add(outline)

        # ---- Tally below table ----
        tally_bg = Rectangle(
            width=8.5, height=0.42,
            fill_color=CREAM, fill_opacity=1,
            stroke_width=0, stroke_opacity=0
        ).move_to((0, -2.5, 0))
        tally_t = Text(
            "V CATCH AVAILABLE: 5 of 5 — verification beats fluency every time",
            font_size=19, color=PASS_CLR, weight=BOLD
        ).move_to((0, -2.5, 0))
        tally = VGroup(tally_bg, tally_t)

        # ---- Animate (8 play calls) ----
        self.play(Write(title))
        self.play(FadeIn(header_row))
        self.play(FadeIn(row_groups[0]))
        self.play(FadeIn(row_groups[1]))
        self.play(FadeIn(row_groups[2]))
        self.play(FadeIn(row_groups[3]))
        self.play(FadeIn(row_groups[4]))
        self.play(FadeIn(catch_outlines), FadeIn(tally))
        self.wait(1)
