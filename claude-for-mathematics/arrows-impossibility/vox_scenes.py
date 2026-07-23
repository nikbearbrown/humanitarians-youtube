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


class B04_VotingMethods(Scene):
    def construct(self):
        # Title
        title = Text(
            "ARROW'S IMPOSSIBILITY — SAME BALLOTS, DIFFERENT WINNERS",
            font_size=24, color=INK, weight=BOLD
        ).move_to((0, 3.2, 0))

        # Ballot summary at bottom
        ballot_bg = Rectangle(width=8.5, height=0.38, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to((0,-2.5,0))
        ballot_txt = Text("Ballot: 35×(A>C>B)  |  33×(B>C>A)  |  32×(C>B>A)",
                          font_size=20, color=SLATE).move_to((0,-2.5,0))
        ballot_summary = VGroup(ballot_bg, ballot_txt)

        # Helper to build one voting box
        def make_box(method, winner, winner_color, violation, cx, cy):
            box = Rectangle(width=4.5, height=1.8,
                            stroke_width=0.5, stroke_color=INK,
                            fill_color=CREAM, fill_opacity=1
                            ).move_to((cx, cy, 0))
            method_txt = Text(method, font_size=20, color=INK, weight=BOLD).move_to((cx, cy+0.55, 0))
            winner_txt = Text(winner, font_size=36, color=winner_color, weight=BOLD).move_to((cx, cy+0.05, 0))
            violation_txt = Text(violation, font_size=14, color=SLATE).move_to((cx, cy-0.55, 0))
            return box, VGroup(method_txt, winner_txt, violation_txt)

        # Box positions (2×2 grid)
        p_box,  p_text  = make_box("PLURALITY",  "A wins", CRIMSON,
                                   "Violates: Condorcet criterion", -2.5, 1.2)
        b_box,  b_text  = make_box("BORDA COUNT","C wins", SLATE,
                                   "Violates: IIA", 2.5, 1.2)
        i_box,  i_text  = make_box("INSTANT RUNOFF","B wins", PASS_CLR,
                                   "Violates: Monotonicity", -2.5, -1.2)
        c_box,  c_text  = make_box("CONDORCET",  "B wins", PASS_CLR,
                                   "No unique winner guaranteed", 2.5, -1.2)

        # Verdict text at y=-3.2
        verdict_bg = Rectangle(width=9.0, height=0.42, fill_color=CREAM, fill_opacity=1,
                                stroke_width=0, stroke_opacity=0).move_to((0,-3.2,0))
        verdict_txt = Text("Every voting method violates at least one fairness criterion",
                           font_size=22, color=CRIMSON, weight=BOLD).move_to((0,-3.2,0))
        verdict_text = VGroup(verdict_bg, verdict_txt)

        # --- Sequence (7 play() calls) ---
        self.play(Write(title))
        self.play(FadeIn(ballot_summary))
        self.play(FadeIn(p_box),  Write(p_text))
        self.play(FadeIn(b_box),  Write(b_text))
        self.play(FadeIn(i_box),  Write(i_text))
        self.play(FadeIn(c_box),  Write(c_text))
        self.play(Write(verdict_text))
        self.wait(1)
