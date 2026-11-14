# -*- coding: utf-8 -*-
from manim import *
import numpy as np

# 9:16 Portrait 4K Canvas
config.pixel_width = 2160
config.pixel_height = 3840
config.frame_rate = 24
config.frame_width = 9
config.frame_height = 16

BG = "#111111"
FG = "#F2EEE8"
ACCENT = "#C46F4B"
MUTED = "#777777"
GOOD = "#78A083"
BAD = "#B65C5C"
BLUE = "#5C8BB6"
BORDER = "#5D584F"


class BrutalistPortraitScene(Scene):

    def setup(self):
        self.camera.background_color = BG

    def heading(self, text):
        words = text.split()
        lines = []
        current = []
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 20 and current:
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

        if title.width > 6.2:
            title.scale_to_fit_width(6.2)

        title.move_to(UP * 6.2)

        rule = Line(
            LEFT * 3.1,
            RIGHT * 3.1,
            color=ACCENT,
            stroke_width=4
        ).next_to(title, DOWN, buff=0.16)

        return VGroup(title, rule)

    def caption(self, text, color=MUTED):
        words = text.split()
        lines = []
        current = []
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 28 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))

        t = VGroup(*[
            Text(line, font="Georgia", font_size=28, color=color, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=0.08)

        if t.width > 6.2:
            t.scale_to_fit_width(6.2)
        t.move_to(DOWN * 4.9)
        return t

    def box(self, label, width=5.6, height=0.88, color=FG, border_color=BORDER, font_size=28, fill_color=BG, fill_opacity=0.9):
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

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=28, width=5.6, height=0.75):
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
# Beat B00: Naive Modulo Hashing (Portrait)
# ============================================================
class B00_ModuloHashingChaos(BrutalistPortraitScene):
    def construct(self):
        header = self.heading("NAIVE MODULO HASHING")
        cap = self.caption("Adding or losing a node remaps all keys and crashes databases", color=BAD)
        self.add(header, cap)

        f_box = self.box("hash(key) % N_servers", width=6.2, height=0.8, color=ACCENT, font_size=28).move_to(UP * 4.6)

        c1 = RoundedRectangle(width=6.4, height=3.1, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(UP * 2.2)
        c1_t = Text("ORIGINAL: N = 4 SERVERS", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(c1.get_top(), DOWN, buff=0.22)
        nodes4 = VGroup(
            self.box("Node 0", width=2.6, height=0.65, color=BLUE, font_size=26),
            self.box("Node 1", width=2.6, height=0.65, color=BLUE, font_size=26),
            self.box("Node 2", width=2.6, height=0.65, color=BLUE, font_size=26),
            self.box("Node 3", width=2.6, height=0.65, color=BLUE, font_size=26),
        ).arrange_in_grid(rows=2, cols=2, buff=0.3).move_to(c1.get_center() + DOWN * 0.15)
        b1 = self.badge("CACHE HIT RATE: 99.4%", color=GOOD, width=5.6, height=0.6, font_size=26).next_to(nodes4, DOWN, buff=0.2)

        c2 = RoundedRectangle(width=6.4, height=3.3, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(DOWN * 1.8)
        c2_t = Text("NODE CRASH: N = 3 SERVERS", font="Georgia", font_size=26, color=BAD, weight=BOLD).next_to(c2.get_top(), DOWN, buff=0.22)
        nodes3 = VGroup(
            self.box("Node 0", width=2.6, height=0.65, color=FG, font_size=26),
            self.box("Node 1", width=2.6, height=0.65, color=FG, font_size=26),
            self.box("Node 2", width=2.6, height=0.65, color=FG, font_size=26),
            self.box("CRASHED", width=2.6, height=0.65, color=BAD, font_size=26),
        ).arrange_in_grid(rows=2, cols=2, buff=0.3).move_to(c2.get_center() + UP * 0.15)
        alert_txt = Text("hash(k) % 3 SHIFTS ALL KEYS", font="Georgia", font_size=24, color=BAD, weight=BOLD).next_to(nodes3, DOWN, buff=0.2)
        b2 = self.badge("75% KEYS REMAPPED -> MISS", color=BAD, width=5.6, height=0.6, font_size=26).next_to(alert_txt, DOWN, buff=0.18)

        self.play(FadeIn(f_box), FadeIn(c1), FadeIn(c1_t), FadeIn(nodes4), FadeIn(b1))
        self.wait(4.0)
        self.play(FadeIn(c2), FadeIn(c2_t), FadeIn(nodes3), FadeIn(alert_txt), FadeIn(b2))
        self.wait(10.0)


# ============================================================
# Beat B01: Consistent Hash Ring (Portrait)
# ============================================================
class B01_HashRingConcept(BrutalistPortraitScene):
    def construct(self):
        header = self.heading("CONSISTENT HASH RING")
        cap = self.caption("Servers and data keys map onto a circular 360-degree keyspace", color=GOOD)
        self.add(header, cap)

        ring_center = UP * 1.4
        ring_radius = 1.9
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        zero_label = Text("0 (MIN)", font="Georgia", font_size=32, color=MUTED, weight=BOLD).next_to(ring.get_top(), UP, buff=0.15)
        max_label = Text("2^32 (MAX)", font="Georgia", font_size=30, color=MUTED, weight=BOLD).next_to(ring.get_top(), DOWN, buff=0.15)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        s_a = self.box("Server A", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(45) + RIGHT * 0.6 + UP * 0.3)
        s_b = self.box("Server B", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(315) + RIGHT * 0.6 + DOWN * 0.3)
        s_c = self.box("Server C", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(225) + LEFT * 0.6 + DOWN * 0.3)
        s_d = self.box("Server D", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(135) + LEFT * 0.6 + UP * 0.3)

        dot_a = Dot(ring_pt(45), radius=0.16, color=BORDER)
        dot_b = Dot(ring_pt(315), radius=0.16, color=BORDER)
        dot_c = Dot(ring_pt(225), radius=0.16, color=BORDER)
        dot_d = Dot(ring_pt(135), radius=0.16, color=BORDER)

        info_card = RoundedRectangle(width=6.4, height=3.5, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(DOWN * 2.4)
        info_h = Text("UNIFORM KEYSPACE", font="Georgia", font_size=28, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.25)
        l1 = Text("Uniform Hash: Murmur3 / MD5", font="Georgia", font_size=28, color=FG).next_to(info_h, DOWN, buff=0.25).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• Servers hash to perimeter", font="Georgia", font_size=28, color=FG).next_to(l1, DOWN, buff=0.2).align_to(l1, LEFT)
        l3 = Text("• Keys hash to perimeter", font="Georgia", font_size=28, color=FG).next_to(l2, DOWN, buff=0.2).align_to(l1, LEFT)
        b_unif = self.badge("CONTINUOUS 2^32 SPACE", color=GOOD, width=5.8, height=0.65, font_size=28).next_to(l3, DOWN, buff=0.25)
        b_unif.set_x(info_card.get_x())

        self.play(Create(ring), FadeIn(zero_label), FadeIn(max_label))
        self.wait(3.0)
        self.play(FadeIn(VGroup(dot_a, s_a, dot_b, s_b, dot_c, s_c, dot_d, s_d)))
        self.wait(3.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3)), FadeIn(b_unif))
        self.wait(8.0)


# ============================================================
# Beat B02: Deterministic Clockwise Routing (Portrait)
# ============================================================
class B02_ClockwiseKeyRouting(BrutalistPortraitScene):
    def construct(self):
        header = self.heading("CLOCKWISE ROUTING")
        cap = self.caption("Keys travel clockwise along the ring to the nearest server node", color=GOOD)
        self.add(header, cap)

        ring_center = UP * 1.4
        ring_radius = 1.9
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        s_a = self.box("Server A", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(90) + UP * 0.6)
        s_b = self.box("Server B", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(330) + RIGHT * 0.6 + DOWN * 0.3)
        s_c = self.box("Server C", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(210) + LEFT * 0.6 + DOWN * 0.3)

        dot_a = Dot(ring_pt(90), radius=0.16, color=BLUE)
        dot_b = Dot(ring_pt(330), radius=0.16, color=BLUE)
        dot_c = Dot(ring_pt(210), radius=0.16, color=BLUE)

        dot_k1 = Dot(ring_pt(40), radius=0.14, color=ACCENT)
        lbl_k1 = Text("Key 1", font="Georgia", font_size=28, color=ACCENT, weight=BOLD).next_to(dot_k1, UR, buff=0.12)

        dot_k2 = Dot(ring_pt(280), radius=0.14, color=ACCENT)
        lbl_k2 = Text("Key 2", font="Georgia", font_size=28, color=ACCENT, weight=BOLD).next_to(dot_k2, DR, buff=0.12)

        arc_arrow1 = CurvedArrow(ring_pt(35), ring_pt(335), color=ACCENT, stroke_width=5, angle=-0.9)
        arc_arrow2 = CurvedArrow(ring_pt(275), ring_pt(215), color=ACCENT, stroke_width=5, angle=-0.9)

        info_card = RoundedRectangle(width=6.4, height=3.5, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(DOWN * 2.4)
        info_h = Text("ROUTING RULE", font="Georgia", font_size=28, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.25)
        l1 = Text("1. Hash key identifier", font="Georgia", font_size=28, color=FG).next_to(info_h, DOWN, buff=0.25).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("2. Walk clockwise along ring", font="Georgia", font_size=28, color=FG).next_to(l1, DOWN, buff=0.2).align_to(l1, LEFT)
        l3 = Text("Key 1 -> Server B | Key 2 -> Server C", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).next_to(l2, DOWN, buff=0.2).align_to(l1, LEFT)
        b_det = self.badge("O(log N) BINARY LOOKUP", color=GOOD, width=5.8, height=0.65, font_size=28).next_to(l3, DOWN, buff=0.25)
        b_det.set_x(info_card.get_x())

        self.play(Create(ring), FadeIn(VGroup(dot_a, s_a, dot_b, s_b, dot_c, s_c)))
        self.wait(3.0)
        self.play(FadeIn(VGroup(dot_k1, lbl_k1, dot_k2, lbl_k2)))
        self.play(Create(arc_arrow1), Create(arc_arrow2))
        self.wait(2.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3)), FadeIn(b_det))
        self.wait(4.0)


# ============================================================
# Beat B03: Minimal Node Addition (Portrait)
# ============================================================
class B03_MinimalNodeAddition(BrutalistPortraitScene):
    def construct(self):
        header = self.heading("ZERO DOWNTIME ADDITION")
        cap = self.caption("Adding Server D only remaps keys between A and D (only K/N keys move)", color=GOOD)
        self.add(header, cap)

        ring_center = UP * 1.4
        ring_radius = 1.9
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        s_a = self.box("Server A", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(90) + UP * 0.6)
        s_b = self.box("Server B", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(330) + RIGHT * 0.6 + DOWN * 0.3)
        s_c = self.box("Server C", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(210) + LEFT * 0.6 + DOWN * 0.3)

        dot_a = Dot(ring_pt(90), radius=0.16, color=BLUE)
        dot_b = Dot(ring_pt(330), radius=0.16, color=BLUE)
        dot_c = Dot(ring_pt(210), radius=0.16, color=BLUE)

        dot_d = Dot(ring_pt(20), radius=0.18, color=GOOD)
        s_d = self.box("Server D (NEW)", width=2.5, height=0.65, color=GOOD, font_size=26).move_to(ring_pt(20) + RIGHT * 0.6 + UP * 0.2)

        affected_arc = Arc(radius=ring_radius, start_angle=20 * np.pi / 180.0, angle=70 * np.pi / 180.0, color=GOOD, stroke_width=8).move_to(ring_center).shift(UP * 0.6 + RIGHT * 0.6)

        info_card = RoundedRectangle(width=6.4, height=3.5, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(DOWN * 2.4)
        info_h = Text("TOPOLOGY EXPANSION", font="Georgia", font_size=28, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.25)
        l1 = Text("• Server D claims slice from B", font="Georgia", font_size=28, color=GOOD).next_to(info_h, DOWN, buff=0.25).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• Server A & C completely safe", font="Georgia", font_size=28, color=MUTED).next_to(l1, DOWN, buff=0.2).align_to(l1, LEFT)
        b_mod = self.badge("MODULO HASH: ~75% MOVED", color=BAD, width=5.8, height=0.6, font_size=26).next_to(l2, DOWN, buff=0.25)
        b_mod.set_x(info_card.get_x())
        b_cons = self.badge("CONSISTENT: ONLY K/N MOVED", color=GOOD, width=5.8, height=0.6, font_size=26).next_to(b_mod, DOWN, buff=0.18)
        b_cons.set_x(info_card.get_x())

        self.add(ring, dot_a, s_a, dot_b, s_b, dot_c, s_c)
        self.wait(3.0)
        self.play(FadeIn(dot_d), FadeIn(s_d), Create(affected_arc))
        self.wait(3.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2)), FadeIn(b_mod), FadeIn(b_cons))
        self.wait(6.0)


# ============================================================
# Beat B04: Graceful Node Removal (Portrait)
# ============================================================
class B04_GracefulNodeRemoval(BrutalistPortraitScene):
    def construct(self):
        header = self.heading("GRACEFUL NODE REMOVAL")
        cap = self.caption("When Server B crashes, its keys spill clockwise to Server C seamlessly", color=GOOD)
        self.add(header, cap)

        ring_center = UP * 1.4
        ring_radius = 1.9
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        s_a = self.box("Server A (UP)", width=2.4, height=0.65, color=BLUE, font_size=28).move_to(ring_pt(90) + UP * 0.6)
        s_b = self.box("Server B (FAIL)", width=2.4, height=0.65, color=BAD, border_color=BORDER, font_size=26).move_to(ring_pt(330) + RIGHT * 0.6 + DOWN * 0.3)
        s_c = self.box("Server C (UP)", width=2.4, height=0.65, color=GOOD, font_size=28).move_to(ring_pt(210) + LEFT * 0.6 + DOWN * 0.3)

        dot_a = Dot(ring_pt(90), radius=0.16, color=BLUE)
        dot_b = Dot(ring_pt(330), radius=0.16, color=BAD)
        dot_c = Dot(ring_pt(210), radius=0.16, color=GOOD)

        spill_arrow = CurvedArrow(ring_pt(325), ring_pt(215), color=GOOD, stroke_width=5, angle=-1.6)

        info_card = RoundedRectangle(width=6.4, height=3.5, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(DOWN * 2.4)
        info_h = Text("FAILOVER BEHAVIOR", font="Georgia", font_size=28, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.25)
        l1 = Text("• Server B crashes offline", font="Georgia", font_size=28, color=BAD).next_to(info_h, DOWN, buff=0.25).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• B's keys route to Server C", font="Georgia", font_size=28, color=GOOD).next_to(l1, DOWN, buff=0.2).align_to(l1, LEFT)
        l3 = Text("• Server A completely safe", font="Georgia", font_size=28, color=FG).next_to(l2, DOWN, buff=0.2).align_to(l1, LEFT)
        b_resil = self.badge("PREVENTS CACHE COLLAPSE", color=GOOD, width=5.8, height=0.65, font_size=28).next_to(l3, DOWN, buff=0.25)
        b_resil.set_x(info_card.get_x())

        self.add(ring, dot_a, s_a, dot_b, s_b, dot_c, s_c)
        self.wait(3.0)
        self.play(Create(spill_arrow))
        self.wait(2.5)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3)), FadeIn(b_resil))
        self.wait(6.0)


# ============================================================
# Beat B05: The Hotspot Dilemma (Portrait)
# ============================================================
class B05_UnevenRingHotspots(BrutalistPortraitScene):
    def construct(self):
        header = self.heading("THE HOTSPOT DILEMMA")
        cap = self.caption("With few physical nodes, random hashing causes severe load imbalances", color=BAD)
        self.add(header, cap)

        ring_center = UP * 1.4
        ring_radius = 1.9
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        s_a = self.box("Node A (12%)", width=2.4, height=0.65, color=MUTED, font_size=26).move_to(ring_pt(75) + RIGHT * 0.6 + UP * 0.3)
        s_b = self.box("Node B (6%)", width=2.4, height=0.65, color=MUTED, font_size=26).move_to(ring_pt(95) + LEFT * 0.6 + UP * 0.3)
        s_c = self.box("Node C (82% HOT)", width=2.5, height=0.65, color=BAD, border_color=BORDER, font_size=26).move_to(ring_pt(280) + DOWN * 0.5)

        dot_a = Dot(ring_pt(75), radius=0.16, color=MUTED)
        dot_b = Dot(ring_pt(95), radius=0.16, color=MUTED)
        dot_c = Dot(ring_pt(280), radius=0.18, color=BAD)

        hot_arc = Arc(radius=ring_radius, start_angle=95 * np.pi / 180.0, angle=185 * np.pi / 180.0, color=BAD, stroke_width=8).move_to(ring_center).shift(LEFT * 0.5 + DOWN * 0.2)

        info_card = RoundedRectangle(width=6.4, height=3.5, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(DOWN * 2.4)
        info_h = Text("UNEVEN ARC LENGTHS", font="Georgia", font_size=28, color=BAD, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.25)
        l1 = Text("• Random hash clustering", font="Georgia", font_size=28, color=FG).next_to(info_h, DOWN, buff=0.25).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• Node C takes 82% load", font="Georgia", font_size=28, color=BAD).next_to(l1, DOWN, buff=0.2).align_to(l1, LEFT)
        l3 = Text("• High CPU & Out-of-Memory risk", font="Georgia", font_size=28, color=BAD).next_to(l2, DOWN, buff=0.2).align_to(l1, LEFT)
        b_hot = self.badge("CLUSTER OVERLOAD HAZARD", color=BAD, width=5.8, height=0.65, font_size=28).next_to(l3, DOWN, buff=0.25)
        b_hot.set_x(info_card.get_x())

        self.add(ring, dot_a, s_a, dot_b, s_b, dot_c, s_c)
        self.play(Create(hot_arc))
        self.wait(3.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2, l3)), FadeIn(b_hot))
        self.wait(5.0)


# ============================================================
# Beat B06: Virtual Nodes Balanced (Portrait)
# ============================================================
class B06_VirtualNodesBalanced(BrutalistPortraitScene):
    def construct(self):
        header = self.heading("VIRTUAL NODES (VNODES)")
        cap = self.caption("Mapping physical servers to virtual tokens balances load evenly", color=GOOD)
        self.add(header, cap)

        ring_center = UP * 1.4
        ring_radius = 1.9
        ring = Circle(radius=ring_radius, color=BORDER, stroke_width=6).move_to(ring_center)

        def ring_pt(deg):
            rad = deg * np.pi / 180.0
            return ring_center + np.array([np.cos(rad) * ring_radius, np.sin(rad) * ring_radius, 0])

        vnodes = []
        labels = ["A1", "B1", "C1", "A2", "B2", "C2"]
        colors = [BLUE, GOOD, ACCENT, BLUE, GOOD, ACCENT]

        for i in range(6):
            deg = i * 60
            dot = Dot(ring_pt(deg), radius=0.16, color=colors[i])
            txt = Text(labels[i], font="Georgia", font_size=28, color=colors[i], weight=BOLD)
            txt.next_to(dot, ring_pt(deg) - ring_center, buff=0.15)
            vnodes.append(VGroup(dot, txt))

        vgroup = VGroup(*vnodes)

        info_card = RoundedRectangle(width=6.4, height=3.5, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(DOWN * 2.4)
        info_h = Text("UNIFORM DISTRIBUTION", font="Georgia", font_size=28, color=FG, weight=BOLD).next_to(info_card.get_top(), DOWN, buff=0.25)
        l1 = Text("• 100-256 vnodes per server", font="Georgia", font_size=28, color=FG).next_to(info_h, DOWN, buff=0.25).align_to(info_card, LEFT).shift(RIGHT * 0.3)
        l2 = Text("• Load: A: 33% | B: 33% | C: 33%", font="Georgia", font_size=28, color=GOOD, weight=BOLD).next_to(l1, DOWN, buff=0.2).align_to(l1, LEFT)
        b_bal = self.badge("STATISTICALLY UNIFORM LOAD", color=GOOD, width=5.8, height=0.65, font_size=28).next_to(l2, DOWN, buff=0.3)
        b_bal.set_x(info_card.get_x())

        self.play(Create(ring))
        self.play(FadeIn(vgroup))
        self.wait(3.0)
        self.play(FadeIn(info_card), FadeIn(info_h), FadeIn(VGroup(l1, l2)), FadeIn(b_bal))
        self.wait(6.0)


# ============================================================
# Beat B07: Distributed Hash Architecture (Portrait)
# ============================================================
class B07_DistributedHashArchitecture(BrutalistPortraitScene):
    def construct(self):
        header = self.heading("CONSISTENT HASH SCALE")
        cap = self.caption("The foundational routing protocol for cloud storage and edge CDNs", color=GOOD)
        self.add(header, cap)

        cards = []
        data = [
            ("1. MINIMAL KEY MOVEMENT", "Bounds key moves to K/N", GOOD),
            ("2. VNODE LOAD BALANCING", "Vnodes eliminate hotspots", BLUE),
            ("3. ZERO-CASCADE FAILOVER", "Graceful single-node failover", ACCENT),
            ("4. BATTLE-TESTED SCALE", "Powers Dynamo & Cassandra", FG),
        ]

        for i, (title, sub, col) in enumerate(data):
            y_pos = UP * (3.3 - i * 1.45)
            rect = RoundedRectangle(width=6.0, height=1.25, corner_radius=0.1, stroke_color=BORDER, stroke_width=3, fill_color=BG, fill_opacity=0.9).move_to(y_pos)
            t_h = Text(title, font="Georgia", font_size=28, color=col, weight=BOLD)
            if t_h.width > 5.4:
                t_h.scale_to_fit_width(5.4)
            t_h.move_to(rect.get_center() + UP * 0.24)
            t_b = Text(sub, font="Georgia", font_size=26, color=FG)
            if t_b.width > 5.4:
                t_b.scale_to_fit_width(5.4)
            t_b.move_to(rect.get_center() + DOWN * 0.24)
            cards.append(VGroup(rect, t_h, t_b))

        badge_sum = self.badge("HORIZONTAL CLUSTER ELASTICITY", color=GOOD, width=6.0, height=0.65, font_size=28).move_to(DOWN * 3.1)

        for c in cards:
            self.play(FadeIn(c), run_time=0.8)
        self.play(FadeIn(badge_sum))
        self.wait(7.0)
