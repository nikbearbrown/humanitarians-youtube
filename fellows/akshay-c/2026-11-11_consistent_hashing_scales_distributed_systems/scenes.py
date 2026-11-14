# -*- coding: utf-8 -*-
from manim import *
import numpy as np

# 16:9 Landscape 4K Canvas
config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 24
config.frame_width = 16
config.frame_height = 9

BG = "#111111"
FG = "#F2EEE8"
ACCENT = "#C46F4B"
MUTED = "#777777"
GOOD = "#78A083"
BAD = "#B65C5C"
BLUE = "#5C8BB6"
BORDER = "#5D584F"


class BrutalistScene(Scene):

    def setup(self):
        self.camera.background_color = BG

    def heading(self, text):
        words = text.split()
        lines = []
        current = []
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 36 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))

        title = VGroup(*[
            Text(line, font="Georgia", font_size=34, color=FG, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=0.10)

        if title.width > 12.4:
            title.scale_to_fit_width(12.4)

        title.move_to(UP * 3.55)

        rule = Line(
            LEFT * 6.2,
            RIGHT * 6.2,
            color=ACCENT,
            stroke_width=5
        ).next_to(title, DOWN, buff=0.16)

        return VGroup(title, rule)

    def caption(self, text, color=MUTED):
        t = Text(text, font="Georgia", font_size=30, color=color, weight=BOLD)
        if t.width > 12.4:
            t.scale_to_fit_width(12.4)
        t.move_to(DOWN * 3.45)
        return t

    def box(self, label, width=2.8, height=1.1, color=FG, border_color=BORDER, font_size=26, fill_color=BG, fill_opacity=0.9):
        rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.08,
            stroke_color=border_color,
            stroke_width=3,
            fill_color=fill_color,
            fill_opacity=fill_opacity
        )
        text = Text(label, font="Georgia", font_size=font_size, color=color, weight=BOLD)
        max_text_width = width - 0.35
        if text.width > max_text_width:
            text.scale_to_fit_width(max_text_width)
        text.move_to(rect)
        return VGroup(rect, text)

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=26, width=3.4, height=0.68):
        rect = RoundedRectangle(
            width=width,
            height=height,
            corner_radius=0.06,
            stroke_color=border_color,
            stroke_width=2,
            fill_color=BG,
            fill_opacity=0.9
        )
        text = Text(label, font="Georgia", font_size=font_size, color=color, weight=BOLD)
        if text.width > width - 0.25:
            text.scale_to_fit_width(width - 0.25)
        text.move_to(rect)
        return VGroup(rect, text)


# ============================================================
# Beat B00: Naive Modulo Hashing
# ============================================================
class B00_ModuloHashingChaos(BrutalistScene):
    def construct(self):
        header = self.heading("NAIVE MODULO HASHING: THE REHASHING TRAP")
        cap = self.caption("Adding or losing one node remaps nearly all keys, crashing the database", color=BAD)
        self.add(header, cap)

        # Formula box at top center
        formula_rect = RoundedRectangle(
            width=7.8, height=0.85, corner_radius=0.08,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(UP * 2.5)
        formula_txt = Text("server_index = hash(key) % N_servers", font="Georgia", font_size=28, color=ACCENT, weight=BOLD)
        formula_txt.move_to(formula_rect)
        formula = VGroup(formula_rect, formula_txt)

        # Left panel: Normal Cluster (N = 4)
        left_card = RoundedRectangle(
            width=5.8, height=4.2, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(LEFT * 3.4 + DOWN * 0.4)
        left_title = Text("ORIGINAL: N = 4 SERVERS", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(left_card.get_top(), DOWN, buff=0.25)

        # Grid of nodes N=4
        n0 = self.box("Node 0", width=2.4, height=0.65, color=BLUE, font_size=24).move_to(left_card.get_center() + UP * 0.9 + LEFT * 1.35)
        n1 = self.box("Node 1", width=2.4, height=0.65, color=BLUE, font_size=24).move_to(left_card.get_center() + UP * 0.9 + RIGHT * 1.35)
        n2 = self.box("Node 2", width=2.4, height=0.65, color=BLUE, font_size=24).move_to(left_card.get_center() + UP * 0.15 + LEFT * 1.35)
        n3 = self.box("Node 3", width=2.4, height=0.65, color=BLUE, font_size=24).move_to(left_card.get_center() + UP * 0.15 + RIGHT * 1.35)

        sample_t = Text("Key hashes map: 0..3", font="Georgia", font_size=24, color=MUTED).next_to(n2, DOWN, buff=0.3)
        sample_t.set_x(left_card.get_x())
        hit_badge = self.badge("CACHE HIT RATE: 99.4%", color=GOOD, width=4.8, height=0.65).next_to(sample_t, DOWN, buff=0.2)
        hit_badge.set_x(left_card.get_x())

        # Right panel: Crash or Scale (N = 3)
        right_card = RoundedRectangle(
            width=5.8, height=4.2, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(RIGHT * 3.4 + DOWN * 0.4)
        right_title = Text("NODE CRASH: N = 3 SERVERS", font="Georgia", font_size=26, color=BAD, weight=BOLD).next_to(right_card.get_top(), DOWN, buff=0.25)

        rn0 = self.box("Node 0", width=2.4, height=0.65, color=FG, font_size=24).move_to(right_card.get_center() + UP * 0.9 + LEFT * 1.35)
        rn1 = self.box("Node 1", width=2.4, height=0.65, color=FG, font_size=24).move_to(right_card.get_center() + UP * 0.9 + RIGHT * 1.35)
        rn2 = self.box("Node 2", width=2.4, height=0.65, color=FG, font_size=24).move_to(right_card.get_center() + UP * 0.15 + LEFT * 1.35)
        rn3 = self.box("CRASHED", width=2.4, height=0.65, color=BAD, border_color=BORDER, font_size=24).move_to(right_card.get_center() + UP * 0.15 + RIGHT * 1.35)

        alert_t = Text("hash(k) % 3 SHIFTS ALL KEYS", font="Georgia", font_size=24, color=BAD).next_to(rn2, DOWN, buff=0.3)
        alert_t.set_x(right_card.get_x())
        miss_badge = self.badge("75% KEYS REMAPPED -> MISS", color=BAD, width=4.8, height=0.65).next_to(alert_t, DOWN, buff=0.2)
        miss_badge.set_x(right_card.get_x())

        self.play(FadeIn(formula), FadeIn(left_card), FadeIn(left_title), FadeIn(VGroup(n0, n1, n2, n3)), FadeIn(sample_t), FadeIn(hit_badge))
        self.wait(4.0)
        self.play(FadeIn(right_card), FadeIn(right_title), FadeIn(VGroup(rn0, rn1, rn2, rn3)), FadeIn(alert_t), FadeIn(miss_badge))
        self.wait(10.0)


# ============================================================
# Beat B01: Consistent Hash Ring Concept
# ============================================================
class B01_HashRingConcept(BrutalistScene):
    def construct(self):
        header = self.heading("THE CONSISTENT HASH RING")
        cap = self.caption("Servers and data keys map onto the same circular 360-degree keyspace", color=GOOD)
        self.add(header, cap)

        # Center hash ring
        ring_center = DOWN * 0.3 + LEFT * 1.2
        ring_radius = 2.4
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        # Labels for ring points: 0 and 2^32 - 1 at the top
        zero_label = Text("0", font="Georgia", font_size=26, color=MUTED, weight=BOLD).next_to(ring.get_top(), UP, buff=0.15)
        max_label = Text("2^32 - 1", font="Georgia", font_size=26, color=MUTED, weight=BOLD).next_to(ring.get_top(), DOWN, buff=0.15)

        # Server nodes along the ring
        # Angles: A=45 deg, B=315 deg, C=225 deg, D=135 deg
        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        s_a = self.box("Server A", width=2.1, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(45) + RIGHT * 0.9 + UP * 0.4)
        s_b = self.box("Server B", width=2.1, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(315) + RIGHT * 0.9 + DOWN * 0.4)
        s_c = self.box("Server C", width=2.1, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(225) + LEFT * 0.9 + DOWN * 0.4)
        s_d = self.box("Server D", width=2.1, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(135) + LEFT * 0.9 + UP * 0.4)

        dot_a = Dot(ring_pt(45), radius=0.14, color=BLUE)
        dot_b = Dot(ring_pt(315), radius=0.14, color=BLUE)
        dot_c = Dot(ring_pt(225), radius=0.14, color=BLUE)
        dot_d = Dot(ring_pt(135), radius=0.14, color=BLUE)

        # Right explanatory card
        info_card = RoundedRectangle(
            width=4.6, height=4.6, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(RIGHT * 4.6 + DOWN * 0.3)

        info_h = Text("UNIFORM KEYSPACE", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.3)
        l1 = Text("• Uniform Hash (Murmur3/MD5)", font="Georgia", font_size=22, color=MUTED).next_to(info_h, DOWN, buff=0.35).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• Servers hash to ring points", font="Georgia", font_size=22, color=FG).next_to(l1, DOWN, buff=0.25).align_to(l1, LEFT)
        l3 = Text("• Keys hash to ring points", font="Georgia", font_size=22, color=FG).next_to(l2, DOWN, buff=0.25).align_to(l1, LEFT)
        l4 = Text("• 360-degree wrap-around", font="Georgia", font_size=22, color=MUTED).next_to(l3, DOWN, buff=0.25).align_to(l1, LEFT)

        badge_unif = self.badge("CONTINUOUS 2^32 SPACE", color=GOOD, width=4.0, height=0.65).next_to(l4, DOWN, buff=0.35)
        badge_unif.set_x(info_card.get_x())

        self.play(Create(ring), FadeIn(zero_label), FadeIn(max_label))
        self.wait(3.0)
        self.play(FadeIn(VGroup(dot_a, s_a, dot_b, s_b, dot_c, s_c, dot_d, s_d)))
        self.wait(3.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3, l4)), FadeIn(badge_unif))
        self.wait(8.0)


# ============================================================
# Beat B02: Deterministic Clockwise Routing
# ============================================================
class B02_ClockwiseKeyRouting(BrutalistScene):
    def construct(self):
        header = self.heading("DETERMINISTIC CLOCKWISE KEY ROUTING")
        cap = self.caption("Each data key routes clockwise to the first active server node", color=GOOD)
        self.add(header, cap)

        ring_center = DOWN * 0.3 + LEFT * 1.2
        ring_radius = 2.4
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        # 3 servers: A (90 deg), B (330 deg), C (210 deg)
        s_a = self.box("Server A", width=2.0, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(90) + UP * 0.6)
        s_b = self.box("Server B", width=2.0, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(330) + RIGHT * 0.8 + DOWN * 0.4)
        s_c = self.box("Server C", width=2.0, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(210) + LEFT * 0.8 + DOWN * 0.4)

        dot_a = Dot(ring_pt(90), radius=0.14, color=BLUE)
        dot_b = Dot(ring_pt(330), radius=0.14, color=BLUE)
        dot_c = Dot(ring_pt(210), radius=0.14, color=BLUE)

        # 2 Data keys: K1 at 40 deg (routes clockwise to B at 330 deg / -30 deg)
        # K2 at 280 deg (routes clockwise to C at 210 deg / -150 deg)
        dot_k1 = Dot(ring_pt(40), radius=0.12, color=ACCENT)
        lbl_k1 = Text("Key 1", font="Georgia", font_size=22, color=ACCENT, weight=BOLD).next_to(dot_k1, UR, buff=0.1)

        dot_k2 = Dot(ring_pt(280), radius=0.12, color=ACCENT)
        lbl_k2 = Text("Key 2", font="Georgia", font_size=22, color=ACCENT, weight=BOLD).next_to(dot_k2, DR, buff=0.1)

        # Clockwise routing arrows along the perimeter
        # From 40 deg clockwise (-70 deg) to 330 deg
        arc_arrow1 = CurvedArrow(ring_pt(35), ring_pt(335), color=ACCENT, stroke_width=4, angle=-0.9)
        arc_arrow2 = CurvedArrow(ring_pt(275), ring_pt(215), color=ACCENT, stroke_width=4, angle=-0.9)

        # Right explanatory panel
        info_card = RoundedRectangle(
            width=4.6, height=4.6, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(RIGHT * 4.6 + DOWN * 0.3)

        info_h = Text("ROUTING RULE", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.3)
        l1 = Text("1. Hash key identifier", font="Georgia", font_size=22, color=FG).next_to(info_h, DOWN, buff=0.35).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("2. Walk clockwise on ring", font="Georgia", font_size=22, color=FG).next_to(l1, DOWN, buff=0.25).align_to(l1, LEFT)
        l3 = Text("3. First node stores key", font="Georgia", font_size=22, color=GOOD).next_to(l2, DOWN, buff=0.25).align_to(l1, LEFT)
        l4 = Text("Key 1 -> Server B", font="Georgia", font_size=22, color=ACCENT).next_to(l3, DOWN, buff=0.25).align_to(l1, LEFT)
        l5 = Text("Key 2 -> Server C", font="Georgia", font_size=22, color=ACCENT).next_to(l4, DOWN, buff=0.2).align_to(l1, LEFT)

        badge_det = self.badge("O(log N) BINARY LOOKUP", color=GOOD, width=4.0, height=0.65).next_to(l5, DOWN, buff=0.3)
        badge_det.set_x(info_card.get_x())

        self.play(Create(ring), FadeIn(VGroup(dot_a, s_a, dot_b, s_b, dot_c, s_c)))
        self.wait(3.0)
        self.play(FadeIn(VGroup(dot_k1, lbl_k1, dot_k2, lbl_k2)))
        self.play(Create(arc_arrow1), Create(arc_arrow2))
        self.wait(2.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3, l4, l5)), FadeIn(badge_det))
        self.wait(4.0)


# ============================================================
# Beat B03: Minimal Movement on Node Addition
# ============================================================
class B03_MinimalNodeAddition(BrutalistScene):
    def construct(self):
        header = self.heading("ZERO DOWNTIME: NODE ADDITION")
        cap = self.caption("Adding Server D only remaps keys between Server A and D (only K/N keys move)", color=GOOD)
        self.add(header, cap)

        ring_center = DOWN * 0.3 + LEFT * 1.2
        ring_radius = 2.4
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        s_a = self.box("Server A", width=2.0, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(90) + UP * 0.6)
        s_b = self.box("Server B", width=2.0, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(330) + RIGHT * 0.8 + DOWN * 0.4)
        s_c = self.box("Server C", width=2.0, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(210) + LEFT * 0.8 + DOWN * 0.4)

        dot_a = Dot(ring_pt(90), radius=0.14, color=BLUE)
        dot_b = Dot(ring_pt(330), radius=0.14, color=BLUE)
        dot_c = Dot(ring_pt(210), radius=0.14, color=BLUE)

        # New Node D inserted at 20 degrees
        dot_d = Dot(ring_pt(20), radius=0.16, color=GOOD)
        s_d = self.box("Server D (NEW)", width=2.4, height=0.65, color=GOOD, font_size=22).move_to(ring_pt(20) + RIGHT * 1.0 + UP * 0.3)

        # Highlight affected arc: only from 90 deg to 20 deg
        affected_arc = Arc(radius=ring_radius, start_angle=20 * np.pi / 180.0, angle=70 * np.pi / 180.0, color=GOOD, stroke_width=9).move_to(ring_center).shift(UP * 0.7 + RIGHT * 0.7)

        # Right comparison panel
        info_card = RoundedRectangle(
            width=4.6, height=4.6, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(RIGHT * 4.6 + DOWN * 0.3)

        info_h = Text("TOPOLOGY EXPANSION", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.3)
        l1 = Text("• Server D joins cluster", font="Georgia", font_size=22, color=GOOD).next_to(info_h, DOWN, buff=0.35).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• Takes slice from Server B", font="Georgia", font_size=22, color=FG).next_to(l1, DOWN, buff=0.25).align_to(l1, LEFT)
        l3 = Text("• Server A untouched: 100%", font="Georgia", font_size=22, color=MUTED).next_to(l2, DOWN, buff=0.25).align_to(l1, LEFT)
        l4 = Text("• Server C untouched: 100%", font="Georgia", font_size=22, color=MUTED).next_to(l3, DOWN, buff=0.25).align_to(l1, LEFT)

        b_mod = self.badge("MODULO REHASH: ~75% MOVED", color=BAD, width=4.0, height=0.6).next_to(l4, DOWN, buff=0.3)
        b_mod.set_x(info_card.get_x())
        b_cons = self.badge("CONSISTENT: ONLY K/N MOVED", color=GOOD, width=4.0, height=0.6).next_to(b_mod, DOWN, buff=0.18)
        b_cons.set_x(info_card.get_x())

        self.add(ring, dot_a, s_a, dot_b, s_b, dot_c, s_c)
        self.wait(3.0)
        self.play(FadeIn(dot_d), FadeIn(s_d), Create(affected_arc))
        self.wait(3.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3, l4)), FadeIn(b_mod), FadeIn(b_cons))
        self.wait(6.0)


# ============================================================
# Beat B04: Graceful Node Removal
# ============================================================
class B04_GracefulNodeRemoval(BrutalistScene):
    def construct(self):
        header = self.heading("FAULT TOLERANCE: NODE REMOVAL")
        cap = self.caption("When Server B crashes, its keys spill clockwise to Server C without affecting Server A", color=GOOD)
        self.add(header, cap)

        ring_center = DOWN * 0.3 + LEFT * 1.2
        ring_radius = 2.4
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        s_a = self.box("Server A (UP)", width=2.0, height=0.65, color=BLUE, font_size=22).move_to(ring_pt(90) + UP * 0.6)
        s_b = self.box("Server B (DOWN)", width=2.2, height=0.65, color=BAD, border_color=BORDER, font_size=22).move_to(ring_pt(330) + RIGHT * 0.8 + DOWN * 0.4)
        s_c = self.box("Server C (UP)", width=2.0, height=0.65, color=GOOD, font_size=22).move_to(ring_pt(210) + LEFT * 0.8 + DOWN * 0.4)

        dot_a = Dot(ring_pt(90), radius=0.14, color=BLUE)
        dot_b = Dot(ring_pt(330), radius=0.14, color=BAD)
        dot_c = Dot(ring_pt(210), radius=0.14, color=GOOD)

        # Failover arrow from B's position to C
        spill_arrow = CurvedArrow(ring_pt(325), ring_pt(215), color=GOOD, stroke_width=5, angle=-1.6)

        info_card = RoundedRectangle(
            width=4.6, height=4.6, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(RIGHT * 4.6 + DOWN * 0.3)

        info_h = Text("FAILOVER BEHAVIOR", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.3)
        l1 = Text("• Server B crashes offline", font="Georgia", font_size=22, color=BAD).next_to(info_h, DOWN, buff=0.35).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• B's keys route to Server C", font="Georgia", font_size=22, color=GOOD).next_to(l1, DOWN, buff=0.25).align_to(l1, LEFT)
        l3 = Text("• Server A completely safe", font="Georgia", font_size=22, color=FG).next_to(l2, DOWN, buff=0.25).align_to(l1, LEFT)
        l4 = Text("• Zero global cache cascade", font="Georgia", font_size=22, color=MUTED).next_to(l3, DOWN, buff=0.25).align_to(l1, LEFT)

        badge_resil = self.badge("CONTAINED LOCAL FAILOVER", color=GOOD, width=4.0, height=0.65).next_to(l4, DOWN, buff=0.35)
        badge_resil.set_x(info_card.get_x())

        self.add(ring, dot_a, s_a, dot_b, s_b, dot_c, s_c)
        self.wait(3.0)
        self.play(Create(spill_arrow))
        self.wait(2.5)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3, l4)), FadeIn(badge_resil))
        self.wait(6.0)


# ============================================================
# Beat B05: The Hotspot Dilemma
# ============================================================
class B05_UnevenRingHotspots(BrutalistScene):
    def construct(self):
        header = self.heading("THE HOTSPOT DILEMMA: NON-UNIFORM ARCS")
        cap = self.caption("With few physical nodes, random hashing creates severe load imbalances", color=BAD)
        self.add(header, cap)

        ring_center = DOWN * 0.3 + LEFT * 1.2
        ring_radius = 2.4
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        # Clustered nodes: A at 75 deg, B at 95 deg, C at 280 deg
        s_a = self.box("Node A (12%)", width=2.1, height=0.65, color=MUTED, font_size=20).move_to(ring_pt(75) + RIGHT * 0.8 + UP * 0.4)
        s_b = self.box("Node B (6%)", width=2.1, height=0.65, color=MUTED, font_size=20).move_to(ring_pt(95) + LEFT * 0.8 + UP * 0.4)
        s_c = self.box("Node C (82% HOT)", width=2.3, height=0.65, color=BAD, border_color=BORDER, font_size=20).move_to(ring_pt(280) + DOWN * 0.6)

        dot_a = Dot(ring_pt(75), radius=0.14, color=MUTED)
        dot_b = Dot(ring_pt(95), radius=0.14, color=MUTED)
        dot_c = Dot(ring_pt(280), radius=0.16, color=BAD)

        # Huge arc from 95 deg all the way to 280 deg
        hot_arc = Arc(radius=ring_radius, start_angle=95 * np.pi / 180.0, angle=185 * np.pi / 180.0, color=BAD, stroke_width=9).move_to(ring_center).shift(LEFT * 0.6 + DOWN * 0.2)

        info_card = RoundedRectangle(
            width=4.6, height=4.6, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(RIGHT * 4.6 + DOWN * 0.3)

        info_h = Text("UNEVEN ARC LENGTHS", font="Georgia", font_size=26, color=BAD, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.3)
        l1 = Text("• Random hash clustering", font="Georgia", font_size=22, color=FG).next_to(info_h, DOWN, buff=0.35).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• Node C owns 82% of ring", font="Georgia", font_size=22, color=BAD).next_to(l1, DOWN, buff=0.25).align_to(l1, LEFT)
        l3 = Text("• High CPU & OOM risk", font="Georgia", font_size=22, color=BAD).next_to(l2, DOWN, buff=0.25).align_to(l1, LEFT)
        l4 = Text("• Node A and B underutilized", font="Georgia", font_size=22, color=MUTED).next_to(l3, DOWN, buff=0.25).align_to(l1, LEFT)

        badge_hot = self.badge("CLUSTER OVERLOAD HAZARD", color=BAD, width=4.0, height=0.65).next_to(l4, DOWN, buff=0.35)
        badge_hot.set_x(info_card.get_x())

        self.add(ring, dot_a, s_a, dot_b, s_b, dot_c, s_c)
        self.play(Create(hot_arc))
        self.wait(3.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3, l4)), FadeIn(badge_hot))
        self.wait(5.0)


# ============================================================
# Beat B06: Virtual Nodes Balanced Distribution
# ============================================================
class B06_VirtualNodesBalanced(BrutalistScene):
    def construct(self):
        header = self.heading("VIRTUAL NODES: UNIFORM DISTRIBUTION")
        cap = self.caption("Each physical machine maps to dozens of virtual tokens scattered across the ring", color=GOOD)
        self.add(header, cap)

        ring_center = DOWN * 0.3 + LEFT * 1.2
        ring_radius = 2.4
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        # Interleave 12 virtual nodes: A1, B1, C1, A2, B2, C2, A3, B3, C3, A4, B4, C4
        vnodes = []
        labels = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3", "A4", "B4", "C4"]
        colors = [BLUE, GOOD, ACCENT, BLUE, GOOD, ACCENT, BLUE, GOOD, ACCENT, BLUE, GOOD, ACCENT]

        for i in range(12):
            deg = i * 30
            dot = Dot(ring_pt(deg), radius=0.12, color=colors[i])
            txt = Text(labels[i], font="Georgia", font_size=18, color=colors[i], weight=BOLD)
            txt.next_to(dot, ring_pt(deg) - ring_center, buff=0.12)
            vnodes.append(VGroup(dot, txt))

        vgroup = VGroup(*vnodes)

        info_card = RoundedRectangle(
            width=4.6, height=4.6, corner_radius=0.1,
            stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(RIGHT * 4.6 + DOWN * 0.3)

        info_h = Text("VNODES (TOKENS)", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.3)
        l1 = Text("• 100-256 vnodes per server", font="Georgia", font_size=22, color=FG).next_to(info_h, DOWN, buff=0.35).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• Server A load: 33.2%", font="Georgia", font_size=22, color=BLUE).next_to(l1, DOWN, buff=0.25).align_to(l1, LEFT)
        l3 = Text("• Server B load: 33.5%", font="Georgia", font_size=22, color=GOOD).next_to(l2, DOWN, buff=0.25).align_to(l1, LEFT)
        l4 = Text("• Server C load: 33.3%", font="Georgia", font_size=22, color=ACCENT).next_to(l3, DOWN, buff=0.25).align_to(l1, LEFT)

        badge_bal = self.badge("STATISTICALLY UNIFORM LOAD", color=GOOD, width=4.0, height=0.65).next_to(l4, DOWN, buff=0.35)
        badge_bal.set_x(info_card.get_x())

        self.play(Create(ring))
        self.play(FadeIn(vgroup))
        self.wait(3.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3, l4)), FadeIn(badge_bal))
        self.wait(6.0)


# ============================================================
# Beat B07: Distributed Architecture Payoff
# ============================================================
class B07_DistributedHashArchitecture(BrutalistScene):
    def construct(self):
        header = self.heading("PRODUCTION CONSISTENT HASH ARCHITECTURE")
        cap = self.caption("The foundational routing protocol for modern cloud databases and edge CDNs", color=GOOD)
        self.add(header, cap)

        # 4 architectural cards in a 2x2 grid
        c1 = RoundedRectangle(width=5.8, height=1.9, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(LEFT * 3.4 + UP * 1.3)
        t1_h = Text("1. MINIMAL KEY MOVEMENT", font="Georgia", font_size=24, color=GOOD, weight=BOLD).next_to(c1.get_top(), DOWN, buff=0.25)
        t1_b = Text("Bounds reshuffling to K/N on cluster scale", font="Georgia", font_size=20, color=FG).next_to(t1_h, DOWN, buff=0.2)

        c2 = RoundedRectangle(width=5.8, height=1.9, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(RIGHT * 3.4 + UP * 1.3)
        t2_h = Text("2. VNODE LOAD BALANCING", font="Georgia", font_size=24, color=BLUE, weight=BOLD).next_to(c2.get_top(), DOWN, buff=0.25)
        t2_b = Text("Eliminates hot-spotting via token scatter", font="Georgia", font_size=20, color=FG).next_to(t2_h, DOWN, buff=0.2)

        c3 = RoundedRectangle(width=5.8, height=1.9, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(LEFT * 3.4 + DOWN * 1.0)
        t3_h = Text("3. ZERO-CASCADE FAILOVER", font="Georgia", font_size=24, color=ACCENT, weight=BOLD).next_to(c3.get_top(), DOWN, buff=0.25)
        t3_b = Text("Failed node keys spill to successor only", font="Georgia", font_size=20, color=FG).next_to(t3_h, DOWN, buff=0.2)

        c4 = RoundedRectangle(width=5.8, height=1.9, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(RIGHT * 3.4 + DOWN * 1.0)
        t4_h = Text("4. BATTLE-TESTED SCALE", font="Georgia", font_size=24, color=FG, weight=BOLD).next_to(c4.get_top(), DOWN, buff=0.25)
        t4_b = Text("Powers Amazon DynamoDB, Cassandra, Akamai", font="Georgia", font_size=20, color=MUTED).next_to(t4_h, DOWN, buff=0.2)

        card1 = VGroup(c1, t1_h, t1_b)
        card2 = VGroup(c2, t2_h, t2_b)
        card3 = VGroup(c3, t3_h, t3_b)
        card4 = VGroup(c4, t4_h, t4_b)

        badge_sum = self.badge("FOUNDATION OF HORIZONTAL CLUSTER ELASTICITY", color=GOOD, width=9.2, height=0.68).move_to(DOWN * 2.45)

        self.play(FadeIn(card1), FadeIn(card2))
        self.play(FadeIn(card3), FadeIn(card4))
        self.play(FadeIn(badge_sum))
        self.wait(8.0)
