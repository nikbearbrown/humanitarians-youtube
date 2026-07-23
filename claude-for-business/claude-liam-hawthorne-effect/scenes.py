"""scenes.py — Manim scenes for claude-liam-hawthorne-effect.

Palette: cream #FAF9F5, warm ink #3D3929, terracotta #D97757 (ONE accent/beat).
All figures are qualitative by design — no invented numbers (chapter provides none
for Figures 1–2). Every number on screen (e.g. $45k/$65k, 1890s dates, MBTI claim)
maps to a specific passage in the source chapter.

Source: mba-management/chapters/01-management-and-organizational-behavior.md
"""
from manim import *
import numpy as np

# ── Palette ──────────────────────────────────────────────────────────────────
BG    = ManimColor("#FAF9F5")   # cream page
INK   = ManimColor("#3D3929")   # warm near-black — all body text
ACC   = ManimColor("#D97757")   # terracotta — ONE focal moment per scene
SOFT  = ManimColor("#73705F")   # secondary text / chips
GHOST = ManimColor("#A9A491")   # dimmed / muted elements
CARD  = ManimColor("#FFFFFF")   # white card surface


def _caption(text, font_size=18):
    return Text(text, font_size=font_size, color=SOFT, slant="ITALIC")


def _safe_c2p(ax, x, y):
    """ax.c2p as a numpy array; falls back to an approximate mapping in stub environments."""
    try:
        pt = ax.c2p(x, y)
        _ = pt[0] + 0.0  # arithmetic test — fails in static-check stub
        return np.asarray(pt, dtype=float)
    except (TypeError, AttributeError, RecursionError):
        return np.array([x * 0.75 - 1.5, y * 2.0 - 2.25, 0.0])


# ─────────────────────────────────────────────────────────────────────────────
#  B02_BrokenExperiment
#  A qualitative step chart: three interventions, output rises at every one.
#  Lamp glyph above each; terracotta callout on third; observer eye reveals.
#  Under 30s per spec. No invented numbers on y-axis.
# ─────────────────────────────────────────────────────────────────────────────
class B02_BrokenExperiment(Scene):

    def construct(self):
        self.camera.background_color = BG

        # ── Title ─────────────────────────────────────────────────────────────
        title = Text(
            "Hawthorne Works, 1924",
            font_size=28, color=INK, weight="BOLD",
        ).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.8)

        # ── Axes (qualitative — no numbers on y) ─────────────────────────────
        x_vals = [1.0, 2.5, 4.0]
        y_vals = [0.28, 0.58, 0.88]   # qualitative steps (proportional only)
        labels = ["Brighter", "Dimmer", "Restored"]

        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1.1, 0.5],
            x_length=7.5,
            y_length=3.8,
            axis_config={
                "color": INK, "stroke_width": 1.4, "include_tip": False,
                "include_numbers": False,
            },
            tips=False,
        ).shift(DOWN * 0.35 + LEFT * 0.3)

        y_label = (
            Text("Output", font_size=16, color=SOFT)
            .rotate(PI / 2)
            .next_to(ax, LEFT, buff=0.5)
        )
        source = Text(
            "Source: MBA Management — Bear Brown",
            font_size=11, color=GHOST,
        ).to_corner(DR, buff=0.9)

        self.play(
            Create(ax), FadeIn(y_label), FadeIn(source),
            run_time=1.2,
        )

        # ── X-axis tick labels ────────────────────────────────────────────────
        x_ticks = VGroup(*[
            Text(lbl, font_size=16, color=SOFT)
            .next_to(_safe_c2p(ax,x, 0), DOWN, buff=0.22)
            for x, lbl in zip(x_vals, labels)
        ])
        self.play(FadeIn(x_ticks), run_time=0.6)

        # ── Lamp glyph helper ─────────────────────────────────────────────────
        def make_lamp(pos, dim=False):
            col = GHOST if dim else SOFT
            bulb = Circle(radius=0.18, color=col, stroke_width=2, fill_opacity=0)
            rays = VGroup(*[
                Line(
                    bulb.get_center() + 0.22 * np.array([np.cos(a), np.sin(a), 0]),
                    bulb.get_center() + 0.34 * np.array([np.cos(a), np.sin(a), 0]),
                    stroke_width=1.5, color=col,
                )
                for a in np.linspace(0, 2 * PI, 8, endpoint=False)
            ])
            glyph = VGroup(bulb, rays).move_to(pos)
            return glyph

        lamp_y = _safe_c2p(ax,0, 0)[1] - 0.70   # below the x-axis labels

        # ── Reveal each point with its lamp ──────────────────────────────────
        dots = VGroup()
        for i, (x, y, lbl) in enumerate(zip(x_vals, y_vals, labels)):
            point = _safe_c2p(ax,x, y)
            dot = Dot(point, radius=0.12, color=INK)
            lamp = make_lamp([_safe_c2p(ax,x, 0)[0], lamp_y, 0], dim=(i == 1))
            self.play(FadeIn(lamp), FadeIn(dot), run_time=0.9)
            dots.add(dot)
            self.wait(0.25)

        # ── Connect the dots with a rising line ───────────────────────────────
        line_pts = [_safe_c2p(ax,x, y) for x, y in zip(x_vals, y_vals)]
        rising_line = VMobject(stroke_color=INK, stroke_width=2.4)
        rising_line.set_points_as_corners(line_pts)
        self.play(Create(rising_line), run_time=1.2)

        # ── Terracotta callout on the THIRD rise ──────────────────────────────
        callout_anchor = _safe_c2p(ax,x_vals[2], y_vals[2])
        callout_text = Text(
            "That is not a finding.",
            font_size=18, color=ACC, weight="BOLD",
        ).next_to(callout_anchor, UR, buff=0.18)
        callout_line = Line(
            callout_anchor + RIGHT * 0.12 + UP * 0.12,
            callout_text.get_left() + LEFT * 0.08,
            stroke_width=1.2, color=ACC,
        )
        self.play(
            Create(callout_line), Write(callout_text), run_time=1.4,
        )
        self.wait(0.5)

        # ── Observer eye (the hidden variable) fades in ────────────────────────
        # Simple eye: outer ellipse + inner dot
        eye_pos = _safe_c2p(ax,2.5, 1.05)
        eye_outer = Ellipse(width=1.0, height=0.45, color=ACC, stroke_width=2.0, fill_opacity=0)
        eye_pupil = Dot(radius=0.10, color=ACC)
        eye_group = VGroup(eye_outer, eye_pupil).move_to(eye_pos)
        observer_label = Text(
            "The hidden variable",
            font_size=14, color=ACC,
        ).next_to(eye_group, UP, buff=0.12)

        self.play(
            FadeIn(eye_group, shift=DOWN * 0.15),
            FadeIn(observer_label),
            run_time=1.5,
        )
        self.wait(1.2)


# ─────────────────────────────────────────────────────────────────────────────
#  B04_Reanalysis
#  Qualitative block diagram: Mayo's "OBSERVATION" block fractures into four.
#  No invented percentages — labeled blocks only. Sizes are indicative only.
#  Caption: "Real. Smaller than the story. Still the right lesson."
# ─────────────────────────────────────────────────────────────────────────────
class B04_Reanalysis(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = Text(
            "The Reanalysis — What the Data Actually Showed",
            font_size=24, color=INK, weight="BOLD",
        ).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.8)

        source = Text(
            "Source: MBA Management — Bear Brown",
            font_size=11, color=GHOST,
        ).to_corner(DR, buff=0.9)
        self.add(source)

        # ── Mayo's original single block ──────────────────────────────────────
        mayo_block = Rectangle(width=5.0, height=2.2, color=INK, stroke_width=2)
        mayo_block.shift(UP * 0.3)
        mayo_label = Text("OBSERVATION", font_size=26, color=INK, weight="BOLD")
        mayo_label.move_to(mayo_block)
        mayo_caption = Text(
            "Mayo's explanation: observation was everything",
            font_size=15, color=SOFT,
        ).next_to(mayo_block, DOWN, buff=0.25)

        self.play(Create(mayo_block), Write(mayo_label), run_time=1.2)
        self.play(FadeIn(mayo_caption), run_time=0.5)
        self.wait(0.6)

        # ── Fracture into four blocks ─────────────────────────────────────────
        # Four blocks: worker selection (larger), supervision changes (larger),
        # wage incentives (larger), observation (smaller — the key reveal)
        block_data = [
            ("Worker\nselection",     1.4, 2.0),
            ("Supervision\nchanges",  1.4, 2.0),
            ("Wage\nincentives",      1.4, 2.0),
            ("Observation",           0.9, 2.0),   # visibly smaller
        ]
        total_width = sum(w for _, w, _ in block_data) + 0.15 * (len(block_data) - 1)
        x_start = -total_width / 2

        new_blocks = VGroup()
        x = x_start
        for label_text, width, height in block_data:
            is_observation = "Observation" in label_text
            col = ACC if is_observation else INK
            rect = Rectangle(width=width, height=height, color=col, stroke_width=2)
            rect.move_to([x + width / 2, 0.3, 0])
            lbl = Text(
                label_text, font_size=15, color=col, weight="BOLD",
                line_spacing=0.8,
            ).move_to(rect)
            new_blocks.add(VGroup(rect, lbl))
            x += width + 0.15

        self.play(
            FadeOut(mayo_block), FadeOut(mayo_label), FadeOut(mayo_caption),
            run_time=0.6,
        )
        for blk in new_blocks:
            self.play(FadeIn(blk, shift=UP * 0.12), run_time=0.65)

        # ── Caption below ─────────────────────────────────────────────────────
        verdict = Text(
            "Real.  Smaller than the story.  Still the right lesson.",
            font_size=18, color=SOFT, slant="ITALIC",
        ).next_to(new_blocks, DOWN, buff=0.45)
        self.play(Write(verdict), run_time=1.0)

        # ── Accent note on the observation block ─────────────────────────────
        obs_block_grp = new_blocks[-1]
        note = Text("smaller\nthan claimed", font_size=12, color=ACC)
        note.next_to(obs_block_grp, UP, buff=0.15)
        self.play(FadeIn(note, shift=DOWN * 0.08), run_time=0.8)
        self.wait(1.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B06_FiveFunctions
#  Five cards reveal in sequence with Terkel paraphrases between some.
#  Stat chip: $45k / $65k (from chapter). Raise token diagnostic flip.
#  Terracotta: only Economic card "responds" to the raise.
# ─────────────────────────────────────────────────────────────────────────────
class B06_FiveFunctions(Scene):

    FUNCTIONS = [
        ("Economic",      "Income and material security"),
        ("Social",        "Belonging and daily connection"),
        ("Status",        "Occupation signals social position"),
        ("Identity",      "Evidence of capability — Freud: work binds\na person to reality"),
        ("Actualization", "Genuine challenge and growth — the rarest"),
    ]

    TERKEL = [
        # appears after Social card
        "\"I used to point to a house I'd built — something\nthat proved my labor had landed somewhere real.\"\n— steelworker (Terkel, paraphrased)",
        # appears after Status card
        "\"Dismissed at a party for her job title.\nShe felt worthless.\"\n— receptionist (Terkel, paraphrased)",
    ]

    def construct(self):
        self.camera.background_color = BG

        source = Text(
            "Source: MBA Management — Bear Brown",
            font_size=11, color=GHOST,
        ).to_corner(DR, buff=0.9)
        self.add(source)

        title = Text(
            "The Five Functions of Work",
            font_size=26, color=INK, weight="BOLD",
        ).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        card_w, card_h = 2.6, 1.3
        gap = 0.2
        total_w = 5 * card_w + 4 * gap
        x0 = -total_w / 2 + card_w / 2

        card_positions = [x0 + i * (card_w + gap) for i in range(5)]

        # ── Reveal cards one by one ───────────────────────────────────────────
        cards_group = VGroup()
        for i, (name, desc) in enumerate(self.FUNCTIONS):
            x = card_positions[i]
            rect = RoundedRectangle(
                width=card_w, height=card_h,
                corner_radius=0.12, color=INK, stroke_width=1.6, fill_opacity=0,
            ).move_to([x, 0.1, 0])
            name_lbl = Text(name, font_size=14, color=INK, weight="BOLD").move_to(
                [x, 0.42, 0]
            )
            desc_lbl = Text(
                desc, font_size=10, color=SOFT, line_spacing=0.85,
            ).move_to([x, -0.08, 0])
            card = VGroup(rect, name_lbl, desc_lbl)
            self.play(FadeIn(card, shift=UP * 0.1), run_time=0.65)
            cards_group.add(card)

            # Terkel quote after Social card
            if i == 1:
                quote = Text(
                    self.TERKEL[0], font_size=11, color=SOFT, slant="ITALIC", line_spacing=0.9,
                ).to_edge(DOWN, buff=0.55)
                self.play(FadeIn(quote), run_time=0.6)
                self.wait(0.5)
                self.play(FadeOut(quote), run_time=0.4)

            # Terkel quote after Status card
            if i == 2:
                quote = Text(
                    self.TERKEL[1], font_size=11, color=SOFT, slant="ITALIC", line_spacing=0.9,
                ).to_edge(DOWN, buff=0.55)
                self.play(FadeIn(quote), run_time=0.6)
                self.wait(0.5)
                self.play(FadeOut(quote), run_time=0.4)

        # ── Stat chip ─────────────────────────────────────────────────────────
        stat = Text(
            "$45,000 meaningful  >  $65,000 pointless  (reported satisfaction)",
            font_size=13, color=INK,
        ).next_to(cards_group, DOWN, buff=0.38)
        stat_line = Line(
            stat.get_left() + LEFT * 0.05,
            stat.get_right() + RIGHT * 0.05,
            stroke_width=1.0, color=SOFT,
        ).next_to(stat, UP, buff=0.10)
        self.play(FadeIn(stat), Create(stat_line), run_time=0.8)
        self.wait(0.4)

        # ── Raise token drops onto each card ─────────────────────────────────
        coin = Circle(radius=0.22, color=SOFT, stroke_width=2, fill_opacity=0)
        coin_label = Text("$", font_size=16, color=SOFT, weight="BOLD")
        coin_grp = VGroup(coin, coin_label)

        for i, (name, _) in enumerate(self.FUNCTIONS):
            target = cards_group[i].get_top() + UP * 0.3
            coin_grp.move_to(target + UP * 1.0)

            if i == 0:
                # Economic: repair (terracotta)
                coin_grp_econ = VGroup(
                    Circle(radius=0.22, color=ACC, stroke_width=2.2, fill_opacity=0),
                    Text("$", font_size=16, color=ACC, weight="BOLD"),
                )
                coin_grp_econ.move_to(coin_grp)
                self.play(coin_grp_econ.animate.move_to(target), run_time=0.6)
                self.play(
                    cards_group[0][0].animate.set_stroke(color=ACC),
                    run_time=0.5,
                )
                self.wait(0.2)
                self.play(FadeOut(coin_grp_econ), run_time=0.3)
            else:
                # Other functions: no response (ghost)
                coin_ghost = VGroup(
                    Circle(radius=0.22, color=GHOST, stroke_width=1.2, fill_opacity=0),
                    Text("$", font_size=16, color=GHOST),
                )
                coin_ghost.move_to(target + UP * 1.0)
                self.play(coin_ghost.animate.move_to(target), run_time=0.45)
                self.wait(0.15)
                self.play(FadeOut(coin_ghost), run_time=0.3)

        # ── Final caption ──────────────────────────────────────────────────────
        final = Text(
            "If the identity function is broken — money is not the diagnosis.",
            font_size=14, color=INK, slant="ITALIC",
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(final), run_time=1.0)
        self.wait(1.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B08_ManagementPyramid
#  Three-level pyramid with qualitative time-allocation bands per level.
#  No invented percentages — proportions are indicative only.
# ─────────────────────────────────────────────────────────────────────────────
class B08_ManagementPyramid(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = Text(
            "Management — Four Activities, Three Levels",
            font_size=26, color=INK, weight="BOLD",
        ).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.8)

        source = Text(
            "Source: MBA Management — Bear Brown",
            font_size=11, color=GHOST,
        ).to_corner(DR, buff=0.9)
        self.add(source)

        # ── Pyramid bands (bottom-to-top: first-line, middle, executive) ──────
        # Band heights (indicative — not from chapter numbers)
        band_data = [
            ("First-Line",  2.4, "Mostly Direct"),
            ("Middle",      1.6, "Plan · Organize · Direct · Control"),
            ("Executive",   1.0, "Mostly Plan"),
        ]
        total_h = sum(h for _, h, _ in band_data)
        band_width_base = 7.0   # widest (first-line)
        y_base = -total_h / 2 + 0.2

        y = y_base
        rects = []
        for level, h, activity in band_data:
            # Taper the width: first-line widest, executive narrowest
            fraction = (y - y_base + h / 2) / total_h
            w = band_width_base * (1.0 - 0.6 * fraction)
            col = INK if level != "Middle" else SOFT
            rect = Rectangle(width=w, height=h, color=col, stroke_width=1.6, fill_opacity=0)
            rect.move_to([0.0, y + h / 2, 0])
            level_lbl = Text(level, font_size=15, color=col, weight="BOLD")
            level_lbl.move_to(rect).shift(LEFT * (w / 2 - 0.8))
            activity_lbl = Text(activity, font_size=11, color=GHOST)
            activity_lbl.move_to(rect).shift(RIGHT * 0.4)
            rects.append((rect, level_lbl, activity_lbl))
            y += h

        for rect, lbl, act in rects:
            self.play(FadeIn(rect, shift=UP * 0.08), FadeIn(lbl), run_time=0.7)
            self.play(FadeIn(act), run_time=0.4)

        # ── Activity labels on the right ──────────────────────────────────────
        act_title = Text(
            "Key activities per level (qualitative proportions):",
            font_size=13, color=SOFT,
        ).to_corner(DL, buff=0.35)
        self.play(FadeIn(act_title), run_time=0.5)
        self.wait(1.2)


# ─────────────────────────────────────────────────────────────────────────────
#  B09_SkillsTriangle
#  Skills triangle: Technical, Human, Conceptual — marker climbs.
#  Terracotta rings at the two promotion-trap transition points.
# ─────────────────────────────────────────────────────────────────────────────
class B09_SkillsTriangle(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = Text(
            "The Skills Triangle — and The Promotion Trap",
            font_size=26, color=INK, weight="BOLD",
        ).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.8)

        source = Text(
            "Source: MBA Management — Bear Brown",
            font_size=11, color=GHOST,
        ).to_corner(DR, buff=0.9)
        self.add(source)

        # ── Triangle ──────────────────────────────────────────────────────────
        A = np.array([-3.0, -2.0, 0])   # bottom-left: Technical heavy
        B = np.array([ 3.0, -2.0, 0])   # bottom-right: Conceptual heavy
        C = np.array([ 0.0,  2.0, 0])   # top: Executive — balanced conceptual

        tri = Polygon(A, B, C, stroke_color=INK, stroke_width=2.0, fill_opacity=0)
        self.play(Create(tri), run_time=1.0)

        # Corner labels
        tech_lbl = Text("Technical", font_size=16, color=INK, weight="BOLD").next_to(A, DL, buff=0.15)
        conc_lbl = Text("Conceptual", font_size=16, color=INK, weight="BOLD").next_to(B, DR, buff=0.15)
        hum_lbl = Text("Human", font_size=16, color=INK, weight="BOLD").next_to(C, UP, buff=0.15)

        self.play(
            Write(tech_lbl), Write(conc_lbl), Write(hum_lbl),
            run_time=0.8,
        )

        # Level labels on the left side
        level_positions = [
            (np.array([-0.5, -1.6, 0]), "First-Line"),
            (np.array([-0.25, -0.0, 0]), "Middle"),
            (np.array([ 0.0,  1.5, 0]), "Executive"),
        ]
        for pos, lbl in level_positions:
            t = Text(lbl, font_size=13, color=SOFT)
            t.move_to(pos + LEFT * 3.5)
            arrow = Arrow(t.get_right(), pos + LEFT * 0.5, color=GHOST, buff=0.12, stroke_width=1.2)
            self.play(FadeIn(t), GrowArrow(arrow), run_time=0.55)

        self.wait(0.4)

        # ── Marker climbing from first-line to executive ───────────────────────
        marker = Dot(radius=0.18, color=INK).move_to(A + RIGHT * 0.5 + UP * 0.3)
        self.play(FadeIn(marker), run_time=0.4)

        # Climb path: interpolate from near Technical bottom to near center top
        path_pts = [
            A + RIGHT * 0.5 + UP * 0.3,
            np.array([-0.4, -0.3, 0]),
            C + DOWN * 0.6,
        ]

        # Promotion trap rings at the TWO transitions
        trap_pos1 = path_pts[1]   # first-line → middle
        trap_pos2 = path_pts[2]   # middle → executive

        # Move marker to first transition
        self.play(
            marker.animate.move_to(trap_pos1),
            run_time=1.4, rate_func=linear,
        )
        ring1 = Circle(radius=0.40, color=ACC, stroke_width=2.4)
        ring1.move_to(trap_pos1)
        trap_lbl1 = Text("The promotion\ntrap", font_size=13, color=ACC, line_spacing=0.9)
        trap_lbl1.next_to(ring1, RIGHT, buff=0.15)
        self.play(Create(ring1), Write(trap_lbl1), run_time=0.9)
        self.wait(0.3)

        # Move marker to second transition
        self.play(
            marker.animate.move_to(trap_pos2),
            run_time=1.4, rate_func=linear,
        )
        ring2 = Circle(radius=0.40, color=ACC, stroke_width=2.4)
        ring2.move_to(trap_pos2)
        trap_lbl2 = Text("Again.", font_size=13, color=ACC)
        trap_lbl2.next_to(ring2, RIGHT, buff=0.15)
        self.play(Create(ring2), Write(trap_lbl2), run_time=0.9)

        # ── Caption ───────────────────────────────────────────────────────────
        caption = Text(
            "Each level requires different skills — not more of the same.",
            font_size=14, color=INK, slant="ITALIC",
        ).to_edge(DOWN, buff=0.35)
        self.play(Write(caption), run_time=1.0)
        self.wait(1.5)


# ─────────────────────────────────────────────────────────────────────────────
#  B11_ManagementTimeline
#  Left-to-right timeline: five schools of management, 1890s → present.
#  Each school: two-chip verdict (contribution | limitation).
#  Hawthorne 1924-1932 as terracotta pivot. MBTI vs Big Five end chips.
# ─────────────────────────────────────────────────────────────────────────────
class B11_ManagementTimeline(Scene):

    SCHOOLS = [
        ("Scientific\nManagement", "1890s",
         "Real productivity\ngains", "Human cost;\nwork became mechanical"),
        ("Human\nRelations", "1930s–40s",
         "Satisfaction\nmatters", "Assumed interests\nalign — they don't"),
        ("Systems\nThinking", "1960s",
         "Everything\nconnected", "Limited on\nwhat to DO"),
        ("Contingency\nTheory", "1970s–80s",
         "Context-dependent\ntruth", "True and\nunhelpful"),
        ("Evidence-Based\nMgmt", "2000s–",
         "Aspiration toward\nevidence", "Rarely\npracticed"),
    ]

    def construct(self):
        self.camera.background_color = BG

        title = Text(
            "A Century of Management Thought",
            font_size=26, color=INK, weight="BOLD",
        ).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        source = Text(
            "Source: MBA Management — Bear Brown",
            font_size=11, color=GHOST,
        ).to_corner(DR, buff=0.9)
        self.add(source)

        # ── Timeline spine ────────────────────────────────────────────────────
        spine_y = 0.4
        spine = Line(
            LEFT * 5.8, RIGHT * 5.8, stroke_width=1.6, color=INK,
        ).move_to([0, spine_y, 0])
        self.play(Create(spine), run_time=0.8)

        xs = np.linspace(-5.0, 4.8, len(self.SCHOOLS))

        for i, (name, period, contrib, limit) in enumerate(self.SCHOOLS):
            x = xs[i]
            # Vertical tick
            tick = Line([x, spine_y - 0.12, 0], [x, spine_y + 0.12, 0],
                        stroke_width=1.5, color=INK)

            # School name above the spine
            school_lbl = Text(name, font_size=12, color=INK, weight="BOLD", line_spacing=0.85)
            school_lbl.next_to([x, spine_y, 0], UP, buff=0.22)

            # Period below tick
            period_lbl = Text(period, font_size=10, color=SOFT)
            period_lbl.next_to([x, spine_y, 0], DOWN, buff=0.18)

            self.play(
                Create(tick), FadeIn(school_lbl), FadeIn(period_lbl),
                run_time=0.5,
            )

            # Hawthorne pivot after school 0 (Scientific Management)
            if i == 0:
                pivot_x = (xs[0] + xs[1]) / 2
                pivot = Dot([pivot_x, spine_y, 0], radius=0.14, color=ACC)
                pivot_lbl = Text(
                    "Hawthorne\n1924–1932",
                    font_size=10, color=ACC, weight="BOLD", line_spacing=0.85,
                )
                pivot_lbl.next_to(pivot, UP, buff=0.15)
                self.play(FadeIn(pivot), Write(pivot_lbl), run_time=0.7)

            # Contribution chip (below school name, left)
            contrib_chip = VGroup(
                RoundedRectangle(width=1.55, height=0.55, corner_radius=0.08,
                                 color=SOFT, stroke_width=1.0, fill_opacity=0),
                Text(contrib, font_size=9, color=SOFT, line_spacing=0.85),
            )
            contrib_chip.arrange(ORIGIN)
            contrib_chip[1].move_to(contrib_chip[0])
            contrib_chip.next_to(school_lbl, UP, buff=0.10)

            # Limitation chip (above contrib chip)
            limit_chip = VGroup(
                RoundedRectangle(width=1.55, height=0.55, corner_radius=0.08,
                                 color=GHOST, stroke_width=1.0, fill_opacity=0),
                Text(limit, font_size=9, color=GHOST, line_spacing=0.85),
            )
            limit_chip.arrange(ORIGIN)
            limit_chip[1].move_to(limit_chip[0])
            limit_chip.next_to(contrib_chip, UP, buff=0.08)

            self.play(FadeIn(contrib_chip), FadeIn(limit_chip), run_time=0.5)
            self.wait(0.2)

        # ── MBTI vs Big Five end chips ────────────────────────────────────────
        mbti = VGroup(
            Rectangle(width=2.4, height=0.65, color=GHOST, stroke_width=1.2, fill_opacity=0),
            Text("MBTI — no predictive\nvalidity for job performance",
                 font_size=10, color=GHOST, line_spacing=0.85),
        )
        mbti[1].move_to(mbti[0])
        mbti.to_edge(DOWN, buff=0.6).shift(LEFT * 1.8)

        big5 = VGroup(
            Rectangle(width=2.4, height=0.65, color=ACC, stroke_width=1.5, fill_opacity=0),
            Text("Big Five — predicts\nperformance modestly",
                 font_size=10, color=ACC, line_spacing=0.85),
        )
        big5[1].move_to(big5[0])
        big5.to_edge(DOWN, buff=0.6).shift(RIGHT * 1.0)

        vs = Text("vs", font_size=14, color=INK, weight="BOLD")
        vs.move_to([(mbti.get_right()[0] + big5.get_left()[0]) / 2, mbti.get_center()[1], 0])

        self.play(FadeIn(mbti), FadeIn(vs), FadeIn(big5), run_time=1.0)
        self.wait(1.8)


# ─────────────────────────────────────────────────────────────────────────────
#  B13_FiveBlockDiagnostic
#  Five interlocking blocks → one symptom → five hypotheses → wrong-diagnosis
#  loop → Hawthorne mapping. Terracotta on the loop.
# ─────────────────────────────────────────────────────────────────────────────
class B13_FiveBlockDiagnostic(Scene):

    BLOCKS = [
        ("Individuals\n& Groups",    [-4.5, 1.2, 0]),
        ("Tasks &\nTechnology",      [-1.5, 1.2, 0]),
        ("Organization\nDesign",     [ 1.5, 1.2, 0]),
        ("Processes",                [ 4.5, 1.2, 0]),
        ("Management\n(connective)", [ 0.0, -0.5, 0]),
    ]

    HYPOTHESES = [
        "Person disengaged\nby choice",
        "Task doesn't use\ntheir strengths",
        "Work waits invisibly\non another department",
        "Key conversations\nexclude them",
        "Lacks context,\nfeedback, clarity",
    ]

    def construct(self):
        self.camera.background_color = BG

        source = Text(
            "Source: MBA Management — Bear Brown",
            font_size=11, color=GHOST,
        ).to_corner(DR, buff=0.9)
        self.add(source)

        title = Text(
            "The Five-Block Diagnostic",
            font_size=26, color=INK, weight="BOLD",
        ).to_edge(UP, buff=0.7)
        self.play(Write(title), run_time=0.7)

        # ── Draw five blocks ──────────────────────────────────────────────────
        block_mobs = []
        for i, (label, pos) in enumerate(self.BLOCKS):
            is_mgmt = i == 4
            col = ACC if is_mgmt else INK
            sw = 2.2 if is_mgmt else 1.6
            rect = RoundedRectangle(
                width=2.4 if not is_mgmt else 3.0,
                height=0.90 if not is_mgmt else 0.80,
                corner_radius=0.10, color=col, stroke_width=sw, fill_opacity=0,
            ).move_to(pos)
            lbl = Text(label, font_size=12, color=col, weight="BOLD", line_spacing=0.85)
            lbl.move_to(rect)
            num = Text(str(i + 1) if not is_mgmt else "5", font_size=10, color=col)
            num.next_to(rect, UL, buff=0.05)
            grp = VGroup(rect, lbl, num)
            block_mobs.append(grp)
            self.play(FadeIn(grp, shift=UP * 0.06), run_time=0.45)

        # Connectors between blocks 1-4 and management
        mgmt_pos = np.array(self.BLOCKS[4][1])
        for i in range(4):
            blk_pos = np.array(self.BLOCKS[i][1])
            connector = Line(blk_pos + DOWN * 0.4, mgmt_pos + UP * 0.4,
                             stroke_width=1.0, color=GHOST)
            self.play(Create(connector), run_time=0.3)

        self.wait(0.3)

        # ── Symptom card appears ──────────────────────────────────────────────
        symptom = VGroup(
            Rectangle(width=3.8, height=0.8, color=INK, stroke_width=1.8, fill_opacity=0),
            Text("output down, not responding to feedback",
                 font_size=13, color=INK, weight="BOLD"),
        )
        symptom[1].move_to(symptom[0])
        symptom.to_edge(DOWN, buff=1.2)
        symptom_label = Text("SYMPTOM", font_size=10, color=SOFT).next_to(symptom, LEFT, buff=0.2)
        self.play(FadeIn(symptom), FadeIn(symptom_label), run_time=0.8)

        # ── Hypothesis chips branch from symptom ─────────────────────────────
        hyp_groups = VGroup()
        for i, hyp_text in enumerate(self.HYPOTHESES):
            blk_pos = np.array(self.BLOCKS[i][1])
            hyp = VGroup(
                RoundedRectangle(width=2.1, height=0.70, corner_radius=0.08,
                                 color=SOFT, stroke_width=1.0, fill_opacity=0),
                Text(hyp_text, font_size=9, color=SOFT, line_spacing=0.85),
            )
            hyp[1].move_to(hyp[0])
            hyp.next_to(symptom, UP, buff=0.3).shift(RIGHT * (-2.8 + i * 1.4))
            branch = DashedLine(
                symptom.get_top(), hyp.get_bottom(),
                stroke_width=0.8, color=GHOST, dash_length=0.1,
            )
            hyp_groups.add(hyp)
            self.play(Create(branch), FadeIn(hyp, shift=UP * 0.06), run_time=0.4)

        self.wait(0.3)

        # ── Wrong-diagnosis loop: Block 1 → escalation → termination ─────────
        wrong_path = [
            "Block 1 diagnosed: wrong treatment",
            "→ Escalation",
            "→ Person leaves",
            "→ Same symptom reappears",
        ]
        loop_group = VGroup()
        prev = None
        for j, step in enumerate(wrong_path):
            col = ACC if j > 0 else SOFT
            step_mob = Text(step, font_size=12, color=col)
            if j == 0:
                step_mob.to_edge(RIGHT, buff=0.5).shift(UP * 1.0)
            else:
                step_mob.next_to(prev, DOWN, buff=0.18, aligned_edge=LEFT)
            loop_group.add(step_mob)
            self.play(FadeIn(step_mob, shift=DOWN * 0.06), run_time=0.5)
            prev = step_mob

        # Terracotta rectangle around the loop
        loop_rect = SurroundingRectangle(loop_group, color=ACC, stroke_width=2.0, buff=0.15)
        self.play(Create(loop_rect), run_time=0.7)
        self.wait(0.3)

        # ── Hawthorne mapping ──────────────────────────────────────────────────
        blk2 = block_mobs[1]   # Tasks & Technology (Block 2)
        blk4 = block_mobs[3]   # Processes (Block 4)

        self.play(
            blk2[0].animate.set_stroke(color=SOFT, width=2.4),
            run_time=0.5,
        )
        research_lbl = Text("Researchers\ntested here", font_size=11, color=SOFT)
        research_lbl.next_to(blk2, UP, buff=0.2)

        self.play(
            blk4[0].animate.set_stroke(color=ACC, width=2.4),
            run_time=0.5,
        )
        workers_lbl = Text("Workers responded\nhere", font_size=11, color=ACC, weight="BOLD")
        workers_lbl.next_to(blk4, UP, buff=0.2)

        self.play(FadeIn(research_lbl), FadeIn(workers_lbl), run_time=0.7)
        self.wait(1.8)


# ─────────────────────────────────────────────────────────────────────────────
#  B14_Landing
#  Cream page: the episode's core idea as a typographic poster.
#  No UI chrome (ILLUSTRATE LAW). One text moment; terracotta dash.
# ─────────────────────────────────────────────────────────────────────────────
class B14_Landing(Scene):

    def construct(self):
        self.camera.background_color = BG

        line1 = Text(
            "Management is not a procedure",
            font_size=32, color=INK, weight="BOLD",
        )
        line2 = Text(
            "you apply to people.",
            font_size=32, color=INK, weight="BOLD",
        )
        group = VGroup(line1, line2).arrange(DOWN, buff=0.22).move_to(ORIGIN + UP * 0.5)

        dash = Line(
            LEFT * 1.0, RIGHT * 1.0,
            stroke_width=2.0, color=ACC,
        ).next_to(group, DOWN, buff=0.45)

        sub = Text(
            "It is creating the conditions in which people\n"
            "are able to do their best work — and choose to.",
            font_size=18, color=SOFT, line_spacing=1.2,
        ).next_to(dash, DOWN, buff=0.4)

        source = Text(
            "Source: MBA Management — Bear Brown",
            font_size=11, color=GHOST,
        ).to_corner(DR, buff=0.9)

        self.add(source)
        self.play(Write(group), run_time=1.4)
        self.play(Create(dash), run_time=0.5)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=1.0)
        self.wait(1.5)
