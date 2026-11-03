# -*- coding: utf-8 -*-
from manim import *

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
            if len(candidate) > 34 and current:
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
        t = Text(text, font="Georgia", font_size=32, color=color, weight=BOLD)
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

    def badge(self, label, color=GOOD, border_color=BORDER, font_size=26, width=2.6, height=0.68):
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
# B00 - DIRECT COUPLING CHAOS
# ============================================================

class B00_DirectCouplingChaos(BrutalistScene):

    def construct(self):
        title = self.heading("DIRECT CLIENT-TO-SERVICE COUPLING FAILS AT SCALE")

        web = self.box("WEB CLIENT", width=2.6, height=1.0, color=FG).move_to(LEFT * 4.6 + UP * 1.5)
        mobile = self.box("MOBILE APP", width=2.6, height=1.0, color=FG).move_to(LEFT * 4.6)
        iot = self.box("IOT CLIENT", width=2.6, height=1.0, color=FG).move_to(LEFT * 4.6 + DOWN * 1.5)
        clients = VGroup(web, mobile, iot)

        user_svc = self.box("USER SERVICE", width=2.8, height=1.0, color=BAD).move_to(RIGHT * 4.6 + UP * 1.5)
        order_svc = self.box("ORDER SERVICE", width=2.8, height=1.0, color=BAD).move_to(RIGHT * 4.6)
        pay_svc = self.box("PAYMENT SERVICE", width=2.8, height=1.0, color=BAD).move_to(RIGHT * 4.6 + DOWN * 1.5)
        services = VGroup(user_svc, order_svc, pay_svc)

        self.play(FadeIn(title), FadeIn(clients), FadeIn(services), run_time=1.0)

        a1 = Arrow(web.get_right(), user_svc.get_left(), buff=0.15, color=BAD, stroke_width=4)
        a2 = Arrow(mobile.get_right(), order_svc.get_left(), buff=0.15, color=BAD, stroke_width=4)
        a3 = Arrow(iot.get_right(), pay_svc.get_left(), buff=0.15, color=BAD, stroke_width=4)
        self.play(Create(a1), Create(a2), Create(a3), run_time=1.2)

        b1 = self.badge("NO UNIFIED AUTH", color=BAD, font_size=26, width=3.4, height=0.68).move_to(UP * 1.5)
        b2 = self.badge("NO RATE LIMITING", color=BAD, font_size=26, width=3.4, height=0.68).move_to(ORIGIN)
        b3 = self.badge("HARDCODED ROUTES", color=BAD, font_size=26, width=3.4, height=0.68).move_to(DOWN * 1.5)
        flaws = VGroup(b1, b2, b3)

        self.play(LaggedStart(FadeIn(b1), FadeIn(b2), FadeIn(b3), lag_ratio=0.2), run_time=1.2)

        overload = Text("CHAOTIC FAILURE MODES", font="Georgia", font_size=28, color=BAD, weight=BOLD).move_to(DOWN * 2.5)
        self.play(FadeIn(overload), run_time=0.8)

        cap = self.caption("DIRECT CALLS FORCE EVERY MICROSERVICE TO DUPLICATE ROUTING AND SECURITY")
        self.play(FadeIn(cap), run_time=0.6)
        self.wait(5.0)


# ============================================================
# B01 - THE SOLUTION: API GATEWAY ENTRY POINT
# ============================================================

class B01_ApiGatewayEntry(BrutalistScene):

    def construct(self):
        title = self.heading("API GATEWAY: A SINGLE ENTRY POINT")

        web = self.box("WEB CLIENT", width=2.6, height=1.0, color=FG).move_to(LEFT * 4.4 + UP * 1.5)
        mobile = self.box("MOBILE APP", width=2.6, height=1.0, color=FG).move_to(LEFT * 4.4)
        iot = self.box("IOT CLIENT", width=2.6, height=1.0, color=FG).move_to(LEFT * 4.4 + DOWN * 1.5)
        clients = VGroup(web, mobile, iot)

        gw_frame = RoundedRectangle(
            width=4.2, height=3.8, corner_radius=0.12,
            stroke_color=ACCENT, stroke_width=4, fill_color=BG, fill_opacity=0.9
        ).move_to(ORIGIN)
        gw_title = Text("API GATEWAY", font="Georgia", font_size=28, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.45)
        gw_sub = Text("CENTRAL REVERSE PROXY", font="Georgia", font_size=26, color=FG, weight=BOLD).next_to(gw_title, DOWN, buff=0.18)
        gw_role1 = self.badge("INSPECTION", color=BLUE, font_size=26, width=3.4, height=0.55).next_to(gw_sub, DOWN, buff=0.22)
        gw_role2 = self.badge("AUTHENTICATION", color=GOOD, font_size=26, width=3.4, height=0.55).next_to(gw_role1, DOWN, buff=0.15)
        gw_role3 = self.badge("TRAFFIC SHAPING", color=ACCENT, font_size=26, width=3.4, height=0.55).next_to(gw_role2, DOWN, buff=0.15)
        gateway = VGroup(gw_frame, gw_title, gw_sub, gw_role1, gw_role2, gw_role3)

        u_svc = self.box("USER SERVICE", width=3.0, height=1.0, color=GOOD).move_to(RIGHT * 4.4 + UP * 1.5)
        o_svc = self.box("ORDER SERVICE", width=3.0, height=1.0, color=GOOD).move_to(RIGHT * 4.4)
        p_svc = self.box("PAYMENT SERVICE", width=3.0, height=1.0, color=GOOD).move_to(RIGHT * 4.4 + DOWN * 1.5)
        services = VGroup(u_svc, o_svc, p_svc)

        self.play(FadeIn(title), FadeIn(clients), FadeIn(services), run_time=1.0)
        self.play(FadeIn(gateway), run_time=1.0)

        a_in1 = Arrow(web.get_right(), gw_frame.get_left() + UP * 1.1, buff=0.15, color=FG, stroke_width=4)
        a_in2 = Arrow(mobile.get_right(), gw_frame.get_left(), buff=0.15, color=FG, stroke_width=4)
        a_in3 = Arrow(iot.get_right(), gw_frame.get_left() + DOWN * 1.1, buff=0.15, color=FG, stroke_width=4)

        a_out1 = Arrow(gw_frame.get_right() + UP * 1.1, u_svc.get_left(), buff=0.15, color=GOOD, stroke_width=4)
        a_out2 = Arrow(gw_frame.get_right(), o_svc.get_left(), buff=0.15, color=GOOD, stroke_width=4)
        a_out3 = Arrow(gw_frame.get_right() + DOWN * 1.1, p_svc.get_left(), buff=0.15, color=GOOD, stroke_width=4)

        self.play(Create(a_in1), Create(a_in2), Create(a_in3), run_time=1.0)
        self.play(Create(a_out1), Create(a_out2), Create(a_out3), run_time=1.0)

        badge_decouple = self.badge("FULLY DECOUPLED ARCHITECTURE", color=GOOD, font_size=26, width=5.0, height=0.68).move_to(DOWN * 2.45)
        self.play(FadeIn(badge_decouple), run_time=0.6)

        cap = self.caption("THE GATEWAY SHIELDS INTERNAL TOPOLOGY FROM EXTERNAL CLIENT TRAFFIC")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(4.0)


# ============================================================
# B02 - PATH-BASED ROUTING
# ============================================================

class B02_PathBasedRouting(BrutalistScene):

    def construct(self):
        title = self.heading("PATH-BASED REQUEST ROUTING")

        client = self.box("CLIENT APP", width=2.6, height=1.1, color=FG).move_to(LEFT * 4.6)

        gw_frame = RoundedRectangle(
            width=4.4, height=3.6, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(LEFT * 0.2)
        gw_hdr = Text("ROUTING ENGINE", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.4)

        r1 = self.box("/users/*   -> USERS", width=3.8, height=0.68, font_size=26, color=BLUE).next_to(gw_hdr, DOWN, buff=0.22)
        r2 = self.box("/orders/*  -> ORDERS", width=3.8, height=0.68, font_size=26, color=GOOD).next_to(r1, DOWN, buff=0.18)
        r3 = self.box("/payment/* -> PAYMENTS", width=3.8, height=0.68, font_size=26, color=ACCENT).next_to(r2, DOWN, buff=0.18)
        gw = VGroup(gw_frame, gw_hdr, r1, r2, r3)

        u_svc = self.box("USER SERVICE", width=2.8, height=0.95, color=BLUE).move_to(RIGHT * 4.4 + UP * 1.5)
        o_svc = self.box("ORDER SERVICE", width=2.8, height=0.95, color=GOOD).move_to(RIGHT * 4.4)
        p_svc = self.box("PAYMENT SERVICE", width=2.8, height=0.95, color=ACCENT).move_to(RIGHT * 4.4 + DOWN * 1.5)
        svcs = VGroup(u_svc, o_svc, p_svc)

        self.play(FadeIn(title), FadeIn(client), FadeIn(gw), FadeIn(svcs), run_time=1.0)

        in_arrow = Arrow(client.get_right(), gw_frame.get_left(), buff=0.15, color=FG, stroke_width=4)
        self.play(Create(in_arrow), run_time=0.6)

        out_u = Arrow(r1.get_right(), u_svc.get_left(), buff=0.15, color=BLUE, stroke_width=4)
        out_o = Arrow(r2.get_right(), o_svc.get_left(), buff=0.15, color=GOOD, stroke_width=4)
        out_p = Arrow(r3.get_right(), p_svc.get_left(), buff=0.15, color=ACCENT, stroke_width=4)
        self.play(Create(out_u), Create(out_o), Create(out_p), run_time=1.2)

        tag = Text("URL PATHS  ·  HTTP METHODS  ·  HEADER RULES", font="Georgia", font_size=26, color=FG, weight=BOLD).move_to(DOWN * 2.45)
        self.play(FadeIn(tag), run_time=0.6)

        cap = self.caption("REQUESTS ARE PARSED AT LINE RATE AND ROUTED TO MATCHING UPSTREAM CLUSTERS")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.5)


# ============================================================
# B03 - EDGE AUTHENTICATION & SECURITY
# ============================================================

class B03_EdgeAuthentication(BrutalistScene):

    def construct(self):
        title = self.heading("CENTRALIZED EDGE AUTHENTICATION & TLS")

        client_ok = self.box("VALID CLIENT", width=2.6, height=1.0, color=GOOD).move_to(LEFT * 4.6 + UP * 1.2)
        client_bad = self.box("ROGUE CLIENT", width=2.6, height=1.0, color=BAD).move_to(LEFT * 4.6 + DOWN * 1.2)

        gw_frame = RoundedRectangle(
            width=4.4, height=3.6, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(LEFT * 0.1)
        gw_title = Text("GATEWAY SECURITY", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.45)
        s1 = self.badge("TLS TERMINATION", color=BLUE, font_size=26, width=3.8, height=0.58).next_to(gw_title, DOWN, buff=0.22)
        s2 = self.badge("JWT SIGNATURE VERIFIED", color=GOOD, font_size=26, width=3.8, height=0.58).next_to(s1, DOWN, buff=0.18)
        s3 = self.badge("REJECT INVALID TOKENS", color=BAD, font_size=26, width=3.8, height=0.58).next_to(s2, DOWN, buff=0.18)
        gw = VGroup(gw_frame, gw_title, s1, s2, s3)

        svc = self.box("BACKEND SERVICES", width=3.0, height=1.6, color=GOOD).move_to(RIGHT * 4.4)
        trusted = Text("TRUSTED NETWORK", font="Georgia", font_size=26, color=MUTED, weight=BOLD).next_to(svc, UP, buff=0.18)

        self.play(FadeIn(title), FadeIn(client_ok), FadeIn(client_bad), FadeIn(gw), FadeIn(svc), FadeIn(trusted), run_time=1.0)

        a_ok_in = Arrow(client_ok.get_right(), gw_frame.get_left() + UP * 1.0, buff=0.15, color=GOOD, stroke_width=4)
        a_ok_out = Arrow(gw_frame.get_right(), svc.get_left() + UP * 0.3, buff=0.15, color=GOOD, stroke_width=4)
        self.play(Create(a_ok_in), run_time=0.6)
        self.play(Create(a_ok_out), run_time=0.6)

        a_bad_in = Arrow(client_bad.get_right(), gw_frame.get_left() + DOWN * 1.0, buff=0.15, color=BAD, stroke_width=4)
        blocked_tag = self.badge("401 UNAUTHORIZED (DROPPED)", color=BAD, font_size=26, width=4.6, height=0.65).move_to(DOWN * 2.35)
        self.play(Create(a_bad_in), run_time=0.6)
        self.play(FadeIn(blocked_tag), run_time=0.6)

        cap = self.caption("UNTRUSTED REQUESTS ARE REJECTED BEFORE TOUCHING INTERNAL SERVICES")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(4.5)


# ============================================================
# B04 - TOKEN BUCKET RATE LIMITING
# ============================================================

class B04_TokenBucketRateLimit(BrutalistScene):

    def construct(self):
        title = self.heading("TOKEN BUCKET RATE LIMITING & THROTTLING")

        burst = VGroup(*[
            self.badge(f"REQ {i}", color=FG, font_size=26, width=1.8, height=0.55)
            for i in range(1, 6)
        ]).arrange(DOWN, buff=0.12).move_to(LEFT * 4.6)
        burst_label = Text("TRAFFIC BURST", font="Georgia", font_size=26, color=BAD, weight=BOLD).next_to(burst, UP, buff=0.2)

        gw_frame = RoundedRectangle(
            width=4.4, height=3.6, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(ORIGIN)
        gw_title = Text("TOKEN BUCKET LIMITER", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.45)
        b_cap = self.badge("CAPACITY: 1000 REQ/SEC", color=GOOD, font_size=26, width=3.8, height=0.58).next_to(gw_title, DOWN, buff=0.22)
        b_act1 = self.badge("NORMAL -> FORWARDED", color=GOOD, font_size=26, width=3.8, height=0.55).next_to(b_cap, DOWN, buff=0.18)
        b_act2 = self.badge("EXCESS -> 429 REJECTED", color=BAD, font_size=26, width=3.8, height=0.55).next_to(b_act1, DOWN, buff=0.15)
        gw = VGroup(gw_frame, gw_title, b_cap, b_act1, b_act2)

        svc = self.box("DOWNSTREAM SERVICE", width=3.2, height=1.2, color=GOOD).move_to(RIGHT * 4.4)
        svc_status = Text("STABLE & RESPONSIVE", font="Georgia", font_size=26, color=GOOD, weight=BOLD).next_to(svc, DOWN, buff=0.2)

        self.play(FadeIn(title), FadeIn(burst), FadeIn(burst_label), FadeIn(gw), FadeIn(svc), FadeIn(svc_status), run_time=1.0)

        in_arrow = Arrow(burst.get_right(), gw_frame.get_left(), buff=0.15, color=BAD, stroke_width=4)
        out_arrow = Arrow(gw_frame.get_right(), svc.get_left(), buff=0.15, color=GOOD, stroke_width=4)
        self.play(Create(in_arrow), run_time=0.7)
        self.play(Create(out_arrow), run_time=0.7)

        shield_tag = Text("PREVENTS CASCADING FAILURES AND NOISY NEIGHBORS", font="Georgia", font_size=26, color=GOOD, weight=BOLD).move_to(DOWN * 2.45)
        self.play(FadeIn(shield_tag), run_time=0.6)

        cap = self.caption("RATE LIMITING CLAMPS TRAFFIC TO PROTECT DOWNSTREAM SERVICE HEALTH")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(4.0)


# ============================================================
# B05 - LOAD BALANCING & HEALTH CHECKS
# ============================================================

class B05_LoadBalancingFailover(BrutalistScene):

    def construct(self):
        title = self.heading("LOAD BALANCING & ACTIVE HEALTH MONITORING")

        gw = self.box("API GATEWAY\nLOAD BALANCER", width=3.4, height=1.6, color=ACCENT, font_size=26).move_to(LEFT * 4.3)

        inst1 = self.box("ORDER SERVICE #1\nHEALTH: OK", width=3.4, height=1.0, color=GOOD, font_size=26).move_to(RIGHT * 4.3 + UP * 1.5)
        inst2 = self.box("ORDER SERVICE #2\nHEALTH: FAILED", width=3.4, height=1.0, color=BAD, font_size=26).move_to(RIGHT * 4.3)
        inst3 = self.box("ORDER SERVICE #3\nHEALTH: OK", width=3.4, height=1.0, color=GOOD, font_size=26).move_to(RIGHT * 4.3 + DOWN * 1.5)
        instances = VGroup(inst1, inst2, inst3)

        self.play(FadeIn(title), FadeIn(gw), FadeIn(instances), run_time=1.0)

        a1 = Arrow(gw.get_right(), inst1.get_left(), buff=0.15, color=GOOD, stroke_width=4)
        a2_dead = Line(gw.get_right(), inst2.get_left(), buff=0.15, color=BAD, stroke_width=2).set_stroke(opacity=0.3)
        cross = Text("X", font="Georgia", font_size=36, color=BAD, weight=BOLD).move_to((gw.get_right() + inst2.get_left()) / 2)
        a3 = Arrow(gw.get_right(), inst3.get_left(), buff=0.15, color=GOOD, stroke_width=4)

        self.play(Create(a1), Create(a3), run_time=1.0)
        self.play(Create(a2_dead), FadeIn(cross), run_time=0.8)

        status_tag = Text("AUTOMATIC TRAFFIC EVACUATION AROUND DEGRADED NODES", font="Georgia", font_size=26, color=GOOD, weight=BOLD).move_to(DOWN * 2.45)
        self.play(FadeIn(status_tag), run_time=0.6)

        cap = self.caption("CONTINUOUS HEALTH CHECKS ENSURE ZERO-DOWNTIME INSTANCE FAILOVER")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.5)


# ============================================================
# B06 - RESPONSE CACHING
# ============================================================

class B06_EdgeResponseCaching(BrutalistScene):

    def construct(self):
        title = self.heading("EDGE RESPONSE CACHING FOR SUB-MILLISECOND READS")

        client = self.box("CLIENT APP", width=2.6, height=1.1, color=FG).move_to(LEFT * 4.4)

        gw_frame = RoundedRectangle(
            width=4.2, height=3.2, corner_radius=0.1,
            stroke_color=ACCENT, stroke_width=3, fill_color=BG, fill_opacity=0.9
        ).move_to(ORIGIN)
        gw_title = Text("API GATEWAY", font="Georgia", font_size=26, color=ACCENT, weight=BOLD).move_to(gw_frame.get_top() + DOWN * 0.45)
        cache_box = self.box("IN-MEMORY CACHE\nCACHE HIT!", width=3.6, height=1.2, color=GOOD, font_size=26).next_to(gw_title, DOWN, buff=0.35)
        gw = VGroup(gw_frame, gw_title, cache_box)

        svc = self.box("CATALOG SERVICE\n(UNTOUCHED)", width=3.2, height=1.2, color=MUTED, font_size=26).move_to(RIGHT * 4.4 + UP * 0.8)
        db = self.box("DATABASE\n(0 READ QUERIES)", width=3.2, height=1.2, color=MUTED, font_size=26).move_to(RIGHT * 4.4 + DOWN * 0.8)
        backend = VGroup(svc, db)

        self.play(FadeIn(title), FadeIn(client), FadeIn(gw), FadeIn(backend), run_time=1.0)

        req_arrow = Arrow(client.get_right() + UP * 0.25, gw_frame.get_left() + UP * 0.25, buff=0.15, color=FG, stroke_width=4)
        resp_arrow = Arrow(gw_frame.get_left() + DOWN * 0.25, client.get_right() + DOWN * 0.25, buff=0.15, color=GOOD, stroke_width=4)

        self.play(Create(req_arrow), run_time=0.6)
        self.play(Create(resp_arrow), run_time=0.6)

        latency_tag = self.badge("SUB-MILLISECOND LATENCY  ·  ZERO BACKEND LOAD", color=GOOD, font_size=26, width=6.8, height=0.68).move_to(DOWN * 2.35)
        self.play(FadeIn(latency_tag), run_time=0.6)

        cap = self.caption("REPEATED READ REQUESTS ARE SERVED DIRECTLY FROM GATEWAY MEMORY")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(3.5)


# ============================================================
# B07 - ARCHITECTURE PAYOFF / 4 PILLARS
# ============================================================

class B07_ArchitecturePayoff(BrutalistScene):

    def construct(self):
        title = self.heading("HOW API GATEWAYS MANAGE MILLIONS OF REQUESTS")

        p1 = self.box("SMART ROUTING\nPATH & HEADERS", width=2.8, height=1.8, color=BLUE, font_size=26).move_to(LEFT * 4.2 + UP * 0.3)
        p2 = self.box("EDGE SECURITY\nJWT & TLS OFFLOAD", width=2.8, height=1.8, color=GOOD, font_size=26).move_to(LEFT * 1.4 + UP * 0.3)
        p3 = self.box("RATE LIMITING\nTOKEN BUCKET", width=2.8, height=1.8, color=ACCENT, font_size=26).move_to(RIGHT * 1.4 + UP * 0.3)
        p4 = self.box("RESPONSE CACHE\nIN-MEMORY ACCEL", width=2.8, height=1.8, color=GOOD, font_size=26).move_to(RIGHT * 4.2 + UP * 0.3)
        pillars = VGroup(p1, p2, p3, p4)

        self.play(FadeIn(title), run_time=0.8)
        self.play(
            LaggedStart(
                FadeIn(p1), FadeIn(p2), FadeIn(p3), FadeIn(p4),
                lag_ratio=0.18
            ),
            run_time=1.5
        )

        summary_badge = self.badge(
            "FAST  ·  RESILIENT  ·  SCALABLE UNDER HEAVY LOAD",
            color=GOOD, font_size=26, width=7.4, height=0.72
        ).move_to(DOWN * 2.35)
        self.play(FadeIn(summary_badge), run_time=0.7)

        cap = self.caption("THE FOUNDATIONAL TRAFFIC CONTROLLER OF MODERN DISTRIBUTED SYSTEMS")
        self.play(FadeIn(cap), run_time=0.5)
        self.wait(4.0)
