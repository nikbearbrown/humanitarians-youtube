# -*- coding: utf-8 -*-
from manim import *

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
            Text(line, font="Georgia", font_size=36, color=FG, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=0.12)

        if title.width > 6.4:
            title.scale_to_fit_width(6.4)

        title.move_to(UP * 6.2)

        rule = Line(
            LEFT * 3.2,
            RIGHT * 3.2,
            color=ACCENT,
            stroke_width=4
        ).next_to(title, DOWN, buff=0.18)

        return VGroup(title, rule)

    def caption(self, text, color=MUTED):
        words = text.split()
        lines = []
        current = []
        for word in words:
            candidate = " ".join(current + [word])
            if len(candidate) > 22 and current:
                lines.append(" ".join(current))
                current = [word]
            else:
                current.append(word)
        if current:
            lines.append(" ".join(current))

        t = VGroup(*[
            Text(line, font="Georgia", font_size=32, color=color, weight=BOLD)
            for line in lines
        ]).arrange(DOWN, buff=0.10)

        if t.width > 6.4:
            t.scale_to_fit_width(6.4)

        t.move_to(DOWN * 5.2)
        return t

    def box(self, label, width=6.2, height=1.1, color=FG, border_color=BORDER, font_size=32, fill_color=BG, fill_opacity=0.9):
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
        max_text_width = width - 0.4
        if text.width > max_text_width:
            text.scale_to_fit_width(max_text_width)
        text.move_to(rect)
        return VGroup(rect, text)

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=32, width=2.0, height=0.75):
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
# B00 - DIRECT COUPLING (PORTRAIT)
# ============================================================

class B00_DirectCouplingChaos(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("DIRECT CLIENT COUPLING FAILS AT SCALE")

        web = self.badge("WEB", color=FG, width=1.9, height=0.75)
        mobile = self.badge("MOBILE", color=FG, width=1.9, height=0.75)
        iot = self.badge("IOT", color=FG, width=1.9, height=0.75)
        clients = VGroup(web, mobile, iot).arrange(RIGHT, buff=0.25).move_to(UP * 4.4)
        cl_tag = Text("CLIENT APPS", font="Georgia", font_size=30, color=MUTED, weight=BOLD).next_to(clients, UP, buff=0.18)

        u_svc = self.badge("USERS", color=BAD, width=1.9, height=0.75)
        o_svc = self.badge("ORDERS", color=BAD, width=1.9, height=0.75)
        p_svc = self.badge("PAYMENTS", color=BAD, width=1.9, height=0.75)
        services = VGroup(u_svc, o_svc, p_svc).arrange(RIGHT, buff=0.25).move_to(DOWN * 3.2)
        svc_tag = Text("MICROSERVICES (OVERLOADED)", font="Georgia", font_size=30, color=BAD, weight=BOLD).next_to(services, DOWN, buff=0.18)

        self.play(FadeIn(title), FadeIn(clients), FadeIn(cl_tag), FadeIn(services), FadeIn(svc_tag), run_time=1.0)

        a1 = Arrow(web.get_bottom(), u_svc.get_top(), buff=0.2, color=BAD, stroke_width=4)
        a2 = Arrow(mobile.get_bottom(), o_svc.get_top(), buff=0.2, color=BAD, stroke_width=4)
        a3 = Arrow(iot.get_bottom(), p_svc.get_top(), buff=0.2, color=BAD, stroke_width=4)
        self.play(Create(a1), Create(a2), Create(a3), run_time=1.2)

        f1 = self.box("DUPLICATED AUTH ON EVERY SERVICE", width=6.2, height=0.75, font_size=30, color=BAD).move_to(UP * 1.5)
        f2 = self.box("NO CENTRAL RATE LIMITING", width=6.2, height=0.75, font_size=30, color=BAD).move_to(ORIGIN)
        f3 = self.box("HARDCODED INTERNAL URLS", width=6.2, height=0.75, font_size=30, color=BAD).move_to(DOWN * 1.5)

        self.play(LaggedStart(FadeIn(f1), FadeIn(f2), FadeIn(f3), lag_ratio=0.2), run_time=1.2)

        alert = Text("CHAOTIC FAILURE MODES", font="Georgia", font_size=32, color=BAD, weight=BOLD).move_to(DOWN * 4.3)
        self.play(FadeIn(alert), run_time=0.6)

        cap = self.caption("DIRECT CALLS FORCE EVERY MICROSERVICE TO DUPLICATE ROUTING AND SECURITY")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(5.0)


# ============================================================
# B01 - THE SOLUTION (PORTRAIT)
# ============================================================

class B01_ApiGatewayEntry(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("API GATEWAY: SINGLE ENTRY POINT")

        web = self.badge("WEB", color=FG, width=1.9, height=0.7)
        mobile = self.badge("MOBILE", color=FG, width=1.9, height=0.7)
        iot = self.badge("IOT", color=FG, width=1.9, height=0.7)
        clients = VGroup(web, mobile, iot).arrange(RIGHT, buff=0.25).move_to(UP * 4.4)

        gw_frame = RoundedRectangle(
            width=6.2, height=3.6, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=4, fill_color=BG, fill_opacity=0.9
        ).move_to(UP * 0.4)
        gw_title = Text("API GATEWAY", font="Georgia", font_size=34, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.45)
        gw_sub = Text("CENTRAL REVERSE PROXY", font="Georgia", font_size=30, color=FG, weight=BOLD).next_to(gw_title, DOWN, buff=0.15)
        r1 = self.badge("INSPECTION", color=BLUE, width=1.8, height=0.6)
        r2 = self.badge("SECURITY", color=GOOD, width=1.8, height=0.6)
        r3 = self.badge("THROTTLING", color=ACCENT, width=1.8, height=0.6)
        roles = VGroup(r1, r2, r3).arrange(RIGHT, buff=0.18).next_to(gw_sub, DOWN, buff=0.25)
        gw = VGroup(gw_frame, gw_title, gw_sub, roles)

        u_svc = self.badge("USERS", color=GOOD, width=1.9, height=0.7)
        o_svc = self.badge("ORDERS", color=GOOD, width=1.9, height=0.7)
        p_svc = self.badge("PAYMENTS", color=GOOD, width=1.9, height=0.7)
        services = VGroup(u_svc, o_svc, p_svc).arrange(RIGHT, buff=0.25).move_to(DOWN * 3.3)

        self.play(FadeIn(title), FadeIn(clients), FadeIn(gw), FadeIn(services), run_time=1.0)

        a_in1 = Arrow(web.get_bottom(), gw_frame.get_top() + LEFT * 2.0, buff=0.15, color=FG, stroke_width=4)
        a_in2 = Arrow(mobile.get_bottom(), gw_frame.get_top(), buff=0.15, color=FG, stroke_width=4)
        a_in3 = Arrow(iot.get_bottom(), gw_frame.get_top() + RIGHT * 2.0, buff=0.15, color=FG, stroke_width=4)

        a_out1 = Arrow(gw_frame.get_bottom() + LEFT * 2.0, u_svc.get_top(), buff=0.15, color=GOOD, stroke_width=4)
        a_out2 = Arrow(gw_frame.get_bottom(), o_svc.get_top(), buff=0.15, color=GOOD, stroke_width=4)
        a_out3 = Arrow(gw_frame.get_bottom() + RIGHT * 2.0, p_svc.get_top(), buff=0.15, color=GOOD, stroke_width=4)

        self.play(Create(a_in1), Create(a_in2), Create(a_in3), run_time=1.0)
        self.play(Create(a_out1), Create(a_out2), Create(a_out3), run_time=1.0)

        tag = self.badge("FULLY DECOUPLED ARCHITECTURE", color=GOOD, width=6.2, height=0.7).move_to(DOWN * 4.3)
        self.play(FadeIn(tag), run_time=0.6)

        cap = self.caption("THE GATEWAY SHIELDS INTERNAL TOPOLOGY FROM EXTERNAL CLIENT TRAFFIC")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(4.0)


# ============================================================
# B02 - PATH ROUTING (PORTRAIT)
# ============================================================

class B02_PathBasedRouting(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("PATH-BASED REQUEST ROUTING")

        client = self.box("CLIENT APP", width=6.2, height=0.85, color=FG, font_size=32).move_to(UP * 4.5)

        gw_frame = RoundedRectangle(
            width=6.2, height=3.6, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=4, fill_color=BG, fill_opacity=0.9
        ).move_to(UP * 0.8)
        gw_hdr = Text("ROUTING ENGINE", font="Georgia", font_size=34, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.4)

        r1 = self.box("/users/*   -> USER SERVICE", width=5.6, height=0.65, font_size=30, color=BLUE).next_to(gw_hdr, DOWN, buff=0.22)
        r2 = self.box("/orders/*  -> ORDER SERVICE", width=5.6, height=0.65, font_size=30, color=GOOD).next_to(r1, DOWN, buff=0.18)
        r3 = self.box("/payment/* -> PAYMENT SERVICE", width=5.6, height=0.65, font_size=30, color=ACCENT).next_to(r2, DOWN, buff=0.18)
        gw = VGroup(gw_frame, gw_hdr, r1, r2, r3)

        u_svc = self.badge("USERS", color=BLUE, width=1.9, height=0.7)
        o_svc = self.badge("ORDERS", color=GOOD, width=1.9, height=0.7)
        p_svc = self.badge("PAYMENTS", color=ACCENT, width=1.9, height=0.7)
        svcs = VGroup(u_svc, o_svc, p_svc).arrange(RIGHT, buff=0.25).move_to(DOWN * 3.0)

        self.play(FadeIn(title), FadeIn(client), FadeIn(gw), FadeIn(svcs), run_time=1.0)

        in_a = Arrow(client.get_bottom(), gw_frame.get_top(), buff=0.15, color=FG, stroke_width=4)
        self.play(Create(in_a), run_time=0.6)

        out1 = Arrow(r1.get_bottom() + LEFT * 1.8, u_svc.get_top(), buff=0.15, color=BLUE, stroke_width=4)
        out2 = Arrow(r2.get_bottom(), o_svc.get_top(), buff=0.15, color=GOOD, stroke_width=4)
        out3 = Arrow(r3.get_bottom() + RIGHT * 1.8, p_svc.get_top(), buff=0.15, color=ACCENT, stroke_width=4)
        self.play(Create(out1), Create(out2), Create(out3), run_time=1.0)

        tag = Text("PATHS · METHODS · HEADERS", font="Georgia", font_size=28, color=FG, weight=BOLD).move_to(DOWN * 4.1)
        self.play(FadeIn(tag), run_time=0.6)

        cap = self.caption("REQUESTS ARE PARSED AT LINE RATE AND ROUTED TO MATCHING UPSTREAM CLUSTERS")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.5)


# ============================================================
# B03 - EDGE AUTHENTICATION (PORTRAIT)
# ============================================================

class B03_EdgeAuthentication(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("CENTRALIZED EDGE AUTH & TLS")

        c_ok = self.badge("VALID CLIENT", color=GOOD, width=2.9, height=0.75)
        c_bad = self.badge("ROGUE CLIENT", color=BAD, width=2.9, height=0.75)
        clients = VGroup(c_ok, c_bad).arrange(RIGHT, buff=0.35).move_to(UP * 4.4)

        gw_frame = RoundedRectangle(
            width=6.2, height=3.6, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=4, fill_color=BG, fill_opacity=0.9
        ).move_to(UP * 0.8)
        gw_title = Text("GATEWAY SECURITY", font="Georgia", font_size=34, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.45)
        s1 = self.badge("TLS TERMINATION", color=BLUE, width=5.4, height=0.6).next_to(gw_title, DOWN, buff=0.22)
        s2 = self.badge("JWT SIGNATURE VERIFIED", color=GOOD, width=5.4, height=0.6).next_to(s1, DOWN, buff=0.18)
        s3 = self.badge("REJECT INVALID TOKENS", color=BAD, width=5.4, height=0.6).next_to(s2, DOWN, buff=0.18)
        gw = VGroup(gw_frame, gw_title, s1, s2, s3)

        svc = self.box("TRUSTED INTERNAL SERVICES", width=6.2, height=1.1, color=GOOD, font_size=32).move_to(DOWN * 2.9)

        self.play(FadeIn(title), FadeIn(clients), FadeIn(gw), FadeIn(svc), run_time=1.0)

        a_ok_in = Arrow(c_ok.get_bottom(), gw_frame.get_top() + LEFT * 1.5, buff=0.15, color=GOOD, stroke_width=4)
        a_ok_out = Arrow(gw_frame.get_bottom(), svc.get_top(), buff=0.15, color=GOOD, stroke_width=4)
        self.play(Create(a_ok_in), run_time=0.6)
        self.play(Create(a_ok_out), run_time=0.6)

        a_bad_in = Arrow(c_bad.get_bottom(), gw_frame.get_top() + RIGHT * 1.5, buff=0.15, color=BAD, stroke_width=4)
        tag_drop = self.badge("401 UNAUTHORIZED (DROPPED AT EDGE)", color=BAD, width=6.2, height=0.7).move_to(DOWN * 4.1)
        self.play(Create(a_bad_in), run_time=0.6)
        self.play(FadeIn(tag_drop), run_time=0.6)

        cap = self.caption("UNTRUSTED REQUESTS ARE REJECTED BEFORE TOUCHING INTERNAL SERVICES")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(4.5)


# ============================================================
# B04 - TOKEN BUCKET (PORTRAIT)
# ============================================================

class B04_TokenBucketRateLimit(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("TOKEN BUCKET RATE LIMITING")

        burst = VGroup(*[
            self.badge(f"REQ {i}", color=FG, font_size=30, width=1.1, height=0.6)
            for i in range(1, 6)
        ]).arrange(RIGHT, buff=0.12).move_to(UP * 4.3)
        tag_b = Text("TRAFFIC BURST", font="Georgia", font_size=30, color=BAD, weight=BOLD).next_to(burst, UP, buff=0.15)

        gw_frame = RoundedRectangle(
            width=6.2, height=3.6, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=4, fill_color=BG, fill_opacity=0.9
        ).move_to(UP * 0.6)
        gw_title = Text("TOKEN BUCKET LIMITER", font="Georgia", font_size=34, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.45)
        b_cap = self.badge("CAPACITY: 1000 REQ/SEC", color=GOOD, width=5.4, height=0.6).next_to(gw_title, DOWN, buff=0.22)
        b_act1 = self.badge("NORMAL -> FORWARDED", color=GOOD, width=5.4, height=0.6).next_to(b_cap, DOWN, buff=0.18)
        b_act2 = self.badge("EXCESS -> 429 TOO MANY REQS", color=BAD, width=5.4, height=0.6).next_to(b_act1, DOWN, buff=0.18)
        gw = VGroup(gw_frame, gw_title, b_cap, b_act1, b_act2)

        svc = self.box("DOWNSTREAM SERVICE\nSTABLE & RESPONSIVE", width=6.2, height=1.2, color=GOOD, font_size=32).move_to(DOWN * 3.0)

        self.play(FadeIn(title), FadeIn(burst), FadeIn(tag_b), FadeIn(gw), FadeIn(svc), run_time=1.0)

        in_a = Arrow(burst.get_bottom(), gw_frame.get_top(), buff=0.15, color=BAD, stroke_width=4)
        out_a = Arrow(gw_frame.get_bottom(), svc.get_top(), buff=0.15, color=GOOD, stroke_width=4)
        self.play(Create(in_a), run_time=0.6)
        self.play(Create(out_a), run_time=0.6)

        shield = Text("PREVENTS CASCADING FAILURES", font="Georgia", font_size=32, color=GOOD, weight=BOLD).move_to(DOWN * 4.3)
        self.play(FadeIn(shield), run_time=0.6)

        cap = self.caption("RATE LIMITING CLAMPS TRAFFIC TO PROTECT DOWNSTREAM SERVICE HEALTH")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(4.0)


# ============================================================
# B05 - LOAD BALANCING (PORTRAIT)
# ============================================================

class B05_LoadBalancingFailover(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("LOAD BALANCING & ACTIVE FAILOVER")

        gw = self.box("API GATEWAY LOAD BALANCER", width=6.2, height=1.0, color=ACCENT, font_size=32).move_to(UP * 4.2)

        inst1 = self.box("ORDER SERVICE #1 · HEALTHY", width=6.2, height=0.85, color=GOOD, font_size=30).move_to(UP * 1.8)
        inst2 = self.box("ORDER SERVICE #2 · FAILED", width=6.2, height=0.85, color=BAD, font_size=30).move_to(UP * 0.4)
        inst3 = self.box("ORDER SERVICE #3 · HEALTHY", width=6.2, height=0.85, color=GOOD, font_size=30).move_to(DOWN * 1.0)
        instances = VGroup(inst1, inst2, inst3)

        self.play(FadeIn(title), FadeIn(gw), FadeIn(instances), run_time=1.0)

        a1 = Arrow(gw.get_bottom() + LEFT * 1.8, inst1.get_top() + LEFT * 1.8, buff=0.15, color=GOOD, stroke_width=4)
        a2_dead = Line(gw.get_bottom(), inst2.get_top(), buff=0.15, color=BAD, stroke_width=2).set_stroke(opacity=0.3)
        cross = Text("X", font="Georgia", font_size=36, color=BAD, weight=BOLD).move_to((gw.get_bottom() + inst2.get_top()) / 2)
        a3 = Arrow(gw.get_bottom() + RIGHT * 1.8, inst3.get_top() + RIGHT * 1.8, buff=0.15, color=GOOD, stroke_width=4)

        self.play(Create(a1), Create(a3), run_time=1.0)
        self.play(Create(a2_dead), FadeIn(cross), run_time=0.7)

        tag = Text("AUTOMATIC TRAFFIC EVACUATION", font="Georgia", font_size=32, color=GOOD, weight=BOLD).move_to(DOWN * 3.3)
        self.play(FadeIn(tag), run_time=0.6)

        cap = self.caption("CONTINUOUS HEALTH CHECKS ENSURE ZERO-DOWNTIME INSTANCE FAILOVER")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.5)


# ============================================================
# B06 - RESPONSE CACHING (PORTRAIT)
# ============================================================

class B06_EdgeResponseCaching(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("EDGE RESPONSE CACHING")

        client = self.box("CLIENT APP", width=6.2, height=0.85, color=FG, font_size=32).move_to(UP * 4.4)

        gw_frame = RoundedRectangle(
            width=6.2, height=2.8, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=4, fill_color=BG, fill_opacity=0.9
        ).move_to(UP * 1.0)
        gw_title = Text("API GATEWAY", font="Georgia", font_size=34, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.4)
        cache_box = self.box("IN-MEMORY CACHE · CACHE HIT!", width=5.6, height=0.95, color=GOOD, font_size=32).next_to(gw_title, DOWN, buff=0.25)
        gw = VGroup(gw_frame, gw_title, cache_box)

        backend = self.box("CATALOG SERVICE & DB\n0 READ QUERIES", width=6.2, height=1.2, color=MUTED, font_size=34).move_to(DOWN * 2.4)

        self.play(FadeIn(title), FadeIn(client), FadeIn(gw), FadeIn(backend), run_time=1.0)

        req_a = Arrow(client.get_bottom() + LEFT * 1.4, gw_frame.get_top() + LEFT * 1.4, buff=0.15, color=FG, stroke_width=4)
        resp_a = Arrow(gw_frame.get_top() + RIGHT * 1.4, client.get_bottom() + RIGHT * 1.4, buff=0.15, color=GOOD, stroke_width=4)
        self.play(Create(req_a), run_time=0.6)
        self.play(Create(resp_a), run_time=0.6)

        tag = self.badge("SUB-MS LATENCY · ZERO DB LOAD", color=GOOD, width=6.2, height=0.8, font_size=30).move_to(DOWN * 4.1)
        self.play(FadeIn(tag), run_time=0.6)

        cap = self.caption("REPEATED READ REQUESTS ARE SERVED DIRECTLY FROM GATEWAY MEMORY")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.5)


# ============================================================
# B07 - ARCHITECTURE PAYOFF (PORTRAIT)
# ============================================================

class B07_ArchitecturePayoff(BrutalistPortraitScene):

    def construct(self):
        title = self.heading("THE 4 PILLARS OF API GATEWAYS")

        p1 = self.box("SMART ROUTING\nPATH & HEADER DISPATCH", width=6.2, height=1.05, color=BLUE, font_size=30).move_to(UP * 3.4)
        p2 = self.box("EDGE SECURITY\nJWT & TLS OFFLOAD", width=6.2, height=1.05, color=GOOD, font_size=30).move_to(UP * 1.8)
        p3 = self.box("RATE LIMITING\nTOKEN BUCKET THROTTLING", width=6.2, height=1.05, color=ACCENT, font_size=30).move_to(UP * 0.2)
        p4 = self.box("EDGE CACHING\nIN-MEMORY READ ACCEL", width=6.2, height=1.05, color=GOOD, font_size=30).move_to(DOWN * 1.4)
        pillars = VGroup(p1, p2, p3, p4)

        self.play(FadeIn(title), run_time=0.8)
        self.play(LaggedStart(FadeIn(p1), FadeIn(p2), FadeIn(p3), FadeIn(p4), lag_ratio=0.18), run_time=1.5)

        summary = self.badge("FAST · RESILIENT · SCALABLE", color=GOOD, width=6.2, height=0.75, font_size=32).move_to(DOWN * 3.3)
        self.play(FadeIn(summary), run_time=0.7)

        cap = self.caption("THE FOUNDATIONAL TRAFFIC CONTROLLER OF MODERN DISTRIBUTED SYSTEMS")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(4.0)
