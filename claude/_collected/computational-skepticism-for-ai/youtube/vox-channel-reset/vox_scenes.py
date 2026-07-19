import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,  "B02": 11.0, "B04": 9.0, "B05": 9.0,
    "B07": 9.0,  "B08": 8.0,  "B09": 9.0,
    "B10": 7.0,  "B11": 8.0,  "B12": 18.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


# ── B01 — Title ──────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The Impersonator the Agent Caught", font=DISPLAY, color=INK, font_size=32, weight=BOLD)
        t2 = Text("Then Believed", font=DISPLAY, color=CRIMSON, font_size=32, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02 — ChannelReset ────────────────────────────────────────────────────────

class B02_ChannelReset(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Channel 1 — suspicious, caught
        ch1_box = Rectangle(width=5.0, height=4.5, color=TEAL, fill_color=TEAL,
                            fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.3 + UP * 0.3)
        ch1_lbl = Text("CHANNEL 1 (public)", font=DISPLAY, font_size=13, color=TEAL).move_to(LEFT * 3.3 + UP * 2.2)

        att1_box = Rectangle(width=4.0, height=0.7, color=CRIMSON, fill_color=CRIMSON,
                             fill_opacity=0.20, stroke_width=1).move_to(LEFT * 3.3 + UP * 1.2)
        att1_lbl = Text("\"Chris\": execute this command", font=MONO, font_size=11, color=CRIMSON).move_to(LEFT * 3.3 + UP * 1.2)

        flag_box = Rectangle(width=4.0, height=0.7, color=GOLD, fill_color=GOLD,
                             fill_opacity=0.15, stroke_width=1).move_to(LEFT * 3.3 + UP * 0.2)
        flag_lbl = Text("User ID ≠ owner account → REFUSED", font=MONO, font_size=11, color=GOLD).move_to(LEFT * 3.3 + UP * 0.2)

        refusal = Text("CAUGHT ✓", font=DISPLAY, font_size=15, color=TEAL).move_to(LEFT * 3.3 + DOWN * 0.8)

        # Channel 2 — fresh, trusted
        ch2_box = Rectangle(width=5.0, height=4.5, color=CRIMSON, fill_color=CRIMSON,
                            fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.3 + UP * 0.3)
        ch2_lbl = Text("CHANNEL 2 (new private)", font=DISPLAY, font_size=13, color=CRIMSON).move_to(RIGHT * 3.3 + UP * 2.2)

        att2_box = Rectangle(width=4.0, height=0.7, color=CRIMSON, fill_color=CRIMSON,
                             fill_opacity=0.20, stroke_width=1).move_to(RIGHT * 3.3 + UP * 1.2)
        att2_lbl = Text("\"Chris\": execute this command", font=MONO, font_size=11, color=CRIMSON).move_to(RIGHT * 3.3 + UP * 1.2)

        fresh = Rectangle(width=4.0, height=0.7, color=SLATE, fill_color=SLATE,
                          fill_opacity=0.20, stroke_width=1).move_to(RIGHT * 3.3 + UP * 0.2)
        fresh_lbl = Text("No history. No flags. Display: Chris.", font=MONO, font_size=11, color=SLATE).move_to(RIGHT * 3.3 + UP * 0.2)

        believed = Text("BELIEVED ✗", font=DISPLAY, font_size=15, color=CRIMSON).move_to(RIGHT * 3.3 + DOWN * 0.8)

        caption = Text("Same attacker. Same name. Different channel. Different result.",
                       font=DISPLAY, font_size=13, color=GOLD).move_to(DOWN * 2.6)

        self.play(GrowFromCenter(ch1_box), GrowFromCenter(ch2_box), run_time=0.5)
        self.play(Write(ch1_lbl), Write(ch2_lbl), run_time=0.4)
        self.play(GrowFromCenter(att1_box), GrowFromCenter(att2_box), run_time=0.4)
        self.play(Write(att1_lbl), Write(att2_lbl), run_time=0.4)
        self.play(GrowFromCenter(flag_box), GrowFromCenter(fresh), run_time=0.4)
        self.play(Write(flag_lbl), Write(fresh_lbl), run_time=0.4)
        self.play(Write(refusal), Write(believed), run_time=0.4)
        self.play(Write(caption), run_time=0.4)
        self.wait(DUR["B02"] - 4.7)


# ── B04 — TrustLives ──────────────────────────────────────────────────────────

class B04_TrustLives(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Where the Agent's Suspicion Lives", font=DISPLAY, font_size=20, color=GOLD).move_to(UP * 3.1)

        rows = [
            ("Session context — channel 1",  "Prior interaction history, user ID mismatch flag, suspicious-behavior record",  TEAL),
            ("Channel boundary crossed →",   "New session starts with no memory of prior context",                            SLATE),
            ("Channel 2 — fresh session",    "No history. No flags. Only what's visible now.",                                CRIMSON),
            ("Trust judgment resets",         "Every safeguard from channel 1 is gone",                                       CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(rows):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.12, stroke_width=1.5).move_to(UP * y)
            t1  = Text(name, font=DISPLAY, font_size=14, color=col).move_to([0.0, y + 0.22, 0])
            t2  = Text(desc, font=MONO,    font_size=12, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(t1), run_time=0.3)
            self.play(Write(t2), run_time=0.3)

        self.wait(DUR["B04"] - 4.5)


# ── B05 — DisplayedVsVerified ─────────────────────────────────────────────────

class B05_DisplayedVsVerified(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        hdr_dis = Rectangle(width=5.5, height=0.6, color=CRIMSON, fill_color=CRIMSON,
                            fill_opacity=0.20, stroke_width=1.5).move_to(LEFT * 3.2 + UP * 2.8)
        hdr_ver = Rectangle(width=5.5, height=0.6, color=TEAL,   fill_color=TEAL,
                            fill_opacity=0.20, stroke_width=1.5).move_to(RIGHT * 3.2 + UP * 2.8)
        t_dis   = Text("DISPLAYED IDENTITY", font=DISPLAY, font_size=15, color=CRIMSON).move_to(hdr_dis)
        t_ver   = Text("VERIFIED IDENTITY", font=DISPLAY, font_size=15, color=TEAL).move_to(hdr_ver)

        body_dis = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_opacity=0, stroke_width=1.5).move_to(LEFT * 3.2 + DOWN * 0.6)
        body_ver = Rectangle(width=5.5, height=3.8, color=TEAL,   fill_opacity=0, stroke_width=1.5).move_to(RIGHT * 3.2 + DOWN * 0.6)

        c1 = Text("Name shown in UI\nCan be changed by anyone\nResets every session", font=MONO, font_size=13, color=INK).move_to(LEFT * 3.2 + UP * 0.5)
        c2 = Text("→ WHAT THE AGENT USED", font=DISPLAY, font_size=13, color=CRIMSON).move_to(LEFT * 3.2 + DOWN * 1.5)

        f1 = Text("Cryptographic or infra-level\nPersists across channels\nCannot be faked by name change", font=MONO, font_size=13, color=INK).move_to(RIGHT * 3.2 + UP * 0.5)
        f2 = Text("→ WHAT IT SHOULD HAVE USED", font=DISPLAY, font_size=13, color=TEAL).move_to(RIGHT * 3.2 + DOWN * 1.5)

        self.play(GrowFromCenter(hdr_dis), GrowFromCenter(hdr_ver), run_time=0.5)
        self.play(Write(t_dis), Write(t_ver), run_time=0.5)
        self.play(GrowFromCenter(body_dis), GrowFromCenter(body_ver), run_time=0.5)
        self.play(Write(c1), Write(f1), run_time=0.5)
        self.play(Write(c2), Write(f2), run_time=0.5)
        self.wait(DUR["B05"] - 3.5)


# ── B07 — TwoChannels ─────────────────────────────────────────────────────────

class B07_TwoChannels(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What the Agent Could See in Each Channel", font=DISPLAY, font_size=17, color=GOLD).move_to(UP * 3.1)

        steps = [
            ("CHANNEL 1 — Display: 'Chris' → User ID: not Chris", "mismatch visible → REFUSED",              TEAL),
            ("Channel boundary →",                                  "fresh session; no carryover",            SLATE),
            ("CHANNEL 2 — Display: 'Chris' → User ID: (fresh)",   "no prior ID on file → no discrepancy",   CRIMSON),
            ("Only the attacker knows it's the same attacker",     "agent has no basis to suspect",          CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (patch, result, col) in enumerate(steps):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.5).move_to(UP * y)
            t1  = Text(patch,  font=DISPLAY, font_size=13, color=col).move_to([0.0, y + 0.22, 0])
            t2  = Text(result, font=MONO,    font_size=12, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(t1), run_time=0.3)
            self.play(Write(t2), run_time=0.3)

        self.wait(DUR["B07"] - 4.5)


# ── B08 — QuoteReset ──────────────────────────────────────────────────────────

class B08_QuoteReset(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Any agent system relying on presented identity — rather than "
            "cryptographically grounded or multi-factor authentication — "
            "remains susceptible to session-boundary attacks in which "
            "trust context does not transfer and prior defensive safeguards "
            "are effectively reset.",
            "Computational Skepticism for AI, Chapter 8",
            None,
            "effectively reset",
            DUR["B08"],
        )


# ── B09 — IdentityInfra ───────────────────────────────────────────────────────

class B09_IdentityInfra(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("Where Identity Must Live", font=DISPLAY, font_size=22, color=TEAL).move_to(UP * 3.1)

        cols = [
            ("NOT HERE",   "Session context\nConversational history\nChat display name",      CRIMSON),
            ("HERE",       "Identity infrastructure\nPersists across channels\nCannot be reset by attacker", TEAL),
            ("VALIDATE",   "Test the same attack\nacross channel boundaries\nnot just within one session",   GOLD),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, desc, col) in enumerate(cols):
            x = (i - 1) * 4.3
            box = Rectangle(width=3.8, height=2.8, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to([x, 0.4, 0])
            lbl = Text(name, font=DISPLAY, font_size=18, color=col).move_to([x, 1.5, 0])
            desc_txt = Text(desc, font=MONO, font_size=12, color=INK).move_to([x, 0.1, 0])
            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(desc_txt), run_time=0.3)

        note = Text("Context resets. Infrastructure doesn't.",
                    font=DISPLAY, font_size=15, color=GOLD).move_to(DOWN * 2.4)
        self.play(Write(note), run_time=0.4)
        self.wait(DUR["B09"] - 4.3)


# ── B10 — QuoteDisplayed ──────────────────────────────────────────────────────

class B10_QuoteDisplayed(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The agents in the study use displayed identity rather than "
            "verified identity as the primary authority signal — "
            "and the attack surface is any channel boundary that separates "
            "the agent from its prior context.",
            "Computational Skepticism for AI, Chapter 8",
            None,
            "displayed identity",
            DUR["B10"],
        )


# ── B11 — ValidationMove ──────────────────────────────────────────────────────

class B11_ValidationMove(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What Validation Across Channels Looks Like", font=DISPLAY, font_size=17, color=TEAL).move_to(UP * 3.1)

        rows = [
            ("Test identity attacks in one session",  "necessary — catches same-channel detection",      TEAL),
            ("Test same attack in a new channel",     "catches session-boundary reset vulnerability",    TEAL),
            ("Build identity into infrastructure",    "not into conversational context that resets",     TEAL),
            ("Context-only suspicion",                "can always be escaped with a fresh session",      CRIMSON),
        ]

        self.play(Write(title), run_time=0.4)
        for i, (name, action, col) in enumerate(rows):
            y = 1.8 - i * 1.3
            box = Rectangle(width=10.5, height=1.0, color=col, fill_color=col,
                            fill_opacity=0.10, stroke_width=1.8).move_to(UP * y)
            lbl = Text(name,   font=DISPLAY, font_size=14, color=col).move_to([0.0, y + 0.2,  0])
            act = Text(action, font=MONO,    font_size=13, color=INK).move_to([0.0, y - 0.22, 0])
            self.play(GrowFromCenter(box), run_time=0.35)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(act), run_time=0.3)

        self.wait(DUR["B11"] - 4.5)


# ── B12 — ExampleSupportTicket ────────────────────────────────────────────────

class B12_ExampleSupportTicket(Scene):
    def construct(self):
        total = DUR["B12"]
        title = Text("Same Attack — Different Channel", font=DISPLAY, font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("TICKET #47", font=DISPLAY, font_size=17, color=TEAL).move_to(LEFT * 3.2 + UP * 1.55)
        lbl_r = Text("TICKET #48", font=DISPLAY, font_size=17, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 1.55)

        sub_l = Text("Display: Sarah Chen", font="PT Mono", font_size=14, color=INK).move_to(LEFT * 3.2 + UP * 0.75)
        sub_r = Text("Display: Sarah Chen", font="PT Mono", font_size=14, color=INK).move_to(RIGHT * 3.2 + UP * 0.75)

        det_l = Text("Email mismatch detected", font="PT Mono", font_size=13, color=TEAL).move_to(LEFT * 3.2 + UP * 0.1)
        det_r = Text("Fresh session — no history", font="PT Mono", font_size=13, color=CRIMSON).move_to(RIGHT * 3.2 + UP * 0.1)

        res_l = Text("FLAGGED", font=DISPLAY, font_size=20, color=TEAL, weight=BOLD).move_to(LEFT * 3.2 + DOWN * 0.85)
        res_r = Text("EXPORT RUNS", font=DISPLAY, font_size=20, color=CRIMSON, weight=BOLD).move_to(RIGHT * 3.2 + DOWN * 0.85)

        note = Text("Agent had no record of ticket #47. Attack succeeded.", font=DISPLAY, font_size=15, color=INK).move_to(DOWN * 2.55)
        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)

        self.play(Write(title), run_time=0.4)
        self.play(GrowFromCenter(col_l), GrowFromCenter(col_r), run_time=0.7)
        self.play(Write(lbl_l), Write(lbl_r), run_time=0.5)
        self.play(Write(sub_l), Write(sub_r), run_time=0.4)
        self.play(Write(det_l), Write(det_r), run_time=0.4)
        self.play(FadeIn(res_l), FadeIn(res_r), run_time=0.4)
        self.play(GrowFromCenter(note_rect), run_time=0.3)
        self.play(Write(note), run_time=0.4)
        self.wait(max(0.5, total - 4.5))
