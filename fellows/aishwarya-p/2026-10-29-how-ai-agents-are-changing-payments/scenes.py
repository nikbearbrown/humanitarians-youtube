"""
Manim scenes for how-ai-agents-are-changing-payments
B01_KlarnaAssistant        — Klarna's own launch numbers, then the 2025 move back to humans
B02_ReadVsWrite            — read access risks a wrong answer; write access risks a wrong payment
B03_FirstAgenticPayments   — June 2026 pilots: ING (customer approves), then Nordea (end to end)
B04_Accountability         — AP2 mandates give an audit trail; who pays is still open

Every fact on screen is from a cited source:
  Klarna press release, 27 Feb 2024 (2.3M conversations, two-thirds of chats,
  "the equivalent work of 700 full-time agents"); Klarna CEO via Bloomberg,
  reported by Entrepreneur and Computing, 2025; Nordea press release and
  CX Network, June 2026 (ING 2 June, Nordea days later, Mastercard Agent Pay,
  agentic tokens, pilots); Google Cloud AP2 announcement, 16 Sep 2025
  (intent mandate, cart mandate, "non-repudiable audit trail").
"""
from manim import *

PALETTE = {
    "bg":     "#F3EBDD",
    "ink":    "#2F2A26",
    "teal":   "#1F4E5F",
    "crimson": "#E4572E",
    "slate":  "#29335C",
    "gold":   "#F3A712",
    "sage":   "#A8C686",
}

BODY_FONT = "Menlo"


def make_title(line1, line2, font_size=22):
    t1 = Text(line1, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
    if line2:
        t2 = Text(line2, color=PALETTE["ink"], font_size=font_size, font=BODY_FONT)
        title = VGroup(t1, t2).arrange(DOWN, buff=0.15)
    else:
        title = VGroup(t1)
    title.to_edge(UP, buff=0.7)
    title.move_to([0, title.get_y(), 0])
    return title


def card(text, color, width, height=0.8, font_size=15, text_color=None):
    box = RoundedRectangle(
        corner_radius=0.1, width=width, height=height,
        fill_color=PALETTE[color], fill_opacity=0.08,
        stroke_color=PALETTE[color], stroke_width=1.5
    )
    label = Text(text, color=PALETTE[text_color or color], font_size=font_size,
                 font=BODY_FONT, line_spacing=1.2).move_to(box.get_center())
    return VGroup(box, label)


class B01_KlarnaAssistant(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Klarna's AI", "Assistant")
        self.add(title)

        # State 1 — the launch announcement
        launch = card("Klarna AI assistant · February 2024\nbuilt on OpenAI technology",
                      "slate", 7.0, 1.0).move_to([0, 1.5, 0])
        self.play(Create(launch[0]), Write(launch[1]), run_time=1.0)
        self.wait(4.0)

        # State 2 — the three launch numbers
        stats = VGroup(
            card("2.3M\nconversations", "teal", 2.5, 1.2, font_size=16),
            card("2/3\nof chats", "teal", 2.5, 1.2, font_size=16),
            card("700\nfull-time agents\n(equivalent work)", "teal", 2.5, 1.2, font_size=14),
        ).arrange(RIGHT, buff=0.3).move_to([0, 0.0, 0])
        for s in stats:
            self.play(Create(s[0]), Write(s[1]), run_time=0.8)
            self.wait(3.2)
        own = Text("Klarna's own numbers", color=PALETTE["gold"], font_size=15,
                   font=BODY_FONT).next_to(stats, DOWN, buff=0.25)
        self.play(Write(own), run_time=0.8)
        self.play(Indicate(own, color=PALETTE["gold"]), run_time=1.0)
        self.wait(2.5)

        # State 3 — 2025: hiring humans again
        later = card("2025 · CEO: hiring human agents again\ncost drove the decision, quality suffered",
                     "crimson", 7.6, 1.0, font_size=15).move_to([0, -1.9, 0])
        self.play(Create(later[0]), Write(later[1]), run_time=1.1)
        self.wait(9.0)

        bottom = Text("sources: Klarna press release (Feb 2024) · Bloomberg via Entrepreneur (2025)",
                      color=PALETTE["slate"], font_size=13, font=BODY_FONT).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.0)


class B02_ReadVsWrite(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Read Access vs.", "Write Access")
        self.add(title)

        # State 1 — what Klarna's release does and doesn't say
        klarna = card("Klarna's assistant: refunds, returns, payment questions\nrelease doesn't say whether it moves money",
                      "slate", 8.0, 1.0, font_size=14).move_to([0, 1.5, 0])
        self.play(Create(klarna[0]), Write(klarna[1]), run_time=1.1)
        self.wait(5.5)

        # State 2 — the two kinds of access, side by side
        self.play(FadeOut(klarna), run_time=0.5)
        read = card("read access\nanswer questions · check a balance", "teal", 4.0, 1.0, font_size=14).move_to([-2.2, 1.4, 0])
        write = card("write access\npay an invoice · make a purchase", "crimson", 4.0, 1.0, font_size=14).move_to([2.2, 1.4, 0])
        read_risk = card("risk: a wrong answer", "teal", 4.0, 0.7, font_size=15).move_to([-2.2, -0.3, 0])
        write_risk = card("risk: a wrong payment", "crimson", 4.0, 0.7, font_size=15).move_to([2.2, -0.3, 0])
        read_arrow = Arrow(read.get_bottom(), read_risk.get_top(), buff=0.1, color=PALETTE["ink"], stroke_width=2)
        write_arrow = Arrow(write.get_bottom(), write_risk.get_top(), buff=0.1, color=PALETTE["ink"], stroke_width=2)

        self.play(Create(read[0]), Write(read[1]), run_time=0.9)
        self.play(GrowArrow(read_arrow), run_time=0.4)
        self.play(Create(read_risk[0]), Write(read_risk[1]), run_time=0.8)
        self.wait(4.0)
        self.play(Create(write[0]), Write(write[1]), run_time=0.9)
        self.play(GrowArrow(write_arrow), run_time=0.4)
        self.play(Create(write_risk[0]), Write(write_risk[1]), run_time=0.8)
        self.wait(5.5)

        # State 3 — the shift in risk
        shift = card("a bad reply  ->  a bad transaction", "gold", 6.0, 0.8,
                     font_size=16, text_color="ink").move_to([0, -1.8, 0])
        self.play(Create(shift[0]), Write(shift[1]), run_time=1.0)
        self.play(Indicate(write_risk, color=PALETTE["gold"]), run_time=1.0)
        self.wait(1.0)


class B03_FirstAgenticPayments(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("The First Live", "Agentic Payments")
        self.add(title)

        # State 1 — a June 2026 timeline with two pilots
        line = Line([-3.6, 1.5, 0], [3.6, 1.5, 0], color=PALETTE["ink"], stroke_width=2)
        dots = VGroup(
            Dot([-2.1, 1.5, 0], radius=0.09, color=PALETTE["teal"]),
            Dot([2.1, 1.5, 0], radius=0.09, color=PALETTE["crimson"]),
        )
        dates = VGroup(
            Text("2 June 2026", color=PALETTE["teal"], font_size=14, font=BODY_FONT).next_to(dots[0], UP, buff=0.15),
            Text("days later", color=PALETTE["crimson"], font_size=14, font=BODY_FONT).next_to(dots[1], UP, buff=0.15),
        )
        self.play(Create(line), run_time=0.8)
        self.wait(2.5)

        # State 2 — ING: the customer approves the final choice
        ing = card("ING · Netherlands\nconcert tickets\ncustomer approved final choice",
                   "teal", 3.9, 1.4, font_size=14).move_to([-2.1, 0.0, 0])
        self.play(Create(dots[0]), Write(dates[0]), run_time=0.6)
        self.play(Create(ing[0]), Write(ing[1]), run_time=1.1)
        self.wait(7.0)

        # State 3 — Nordea: the agent does purchase and payment end to end
        nordea = card("Nordea · Finland\ncoffee tasting package\nagent: purchase + payment",
                      "crimson", 3.9, 1.4, font_size=14).move_to([2.1, 0.0, 0])
        self.play(Create(dots[1]), Write(dates[1]), run_time=0.6)
        self.play(Create(nordea[0]), Write(nordea[1]), run_time=1.1)
        self.play(Indicate(nordea, color=PALETTE["gold"]), run_time=1.0)
        self.wait(7.2)

        # State 4 — how the card stayed protected, and the caveat
        tokens = card("Mastercard Agent Pay · agentic tokens\nreal card details kept away from the agent",
                      "slate", 7.8, 0.9, font_size=14).move_to([0, -1.5, 0])
        self.play(Create(tokens[0]), Write(tokens[1]), run_time=1.0)
        self.wait(7.5)

        bottom = Text("both pilots: not available to customers yet",
                      color=PALETTE["crimson"], font_size=15, font=BODY_FONT).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.0)


class B04_Accountability(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Who Is", "Responsible?")
        self.add(title)

        # State 1 — the AP2 chain: request, approval, payment
        chain = VGroup(
            card("your request\n-> intent mandate\n(signed)", "teal", 2.6, 1.3, font_size=14),
            card("your approval\nexact items + price\n-> cart mandate", "teal", 2.6, 1.3, font_size=14),
            card("payment", "slate", 2.0, 1.3, font_size=15),
        ).arrange(RIGHT, buff=0.55).move_to([0, 1.1, 0])
        arrows = VGroup(*[
            Arrow(chain[i].get_right(), chain[i + 1].get_left(), buff=0.08,
                  color=PALETTE["ink"], stroke_width=2)
            for i in range(2)
        ])
        label = Text("Google's Agent Payments Protocol (AP2)", color=PALETTE["slate"],
                     font_size=14, font=BODY_FONT).next_to(chain, UP, buff=0.25)
        self.play(Write(label), run_time=0.8)
        self.wait(3.0)
        for i, c in enumerate(chain):
            self.play(Create(c[0]), Write(c[1]), run_time=0.9)
            self.wait(3.0)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.4)

        # State 2 — together: an audit trail
        trail = card('"a non-repudiable audit trail"\nproof of what you asked for and what you approved',
                     "gold", 8.0, 1.0, font_size=14, text_color="ink").move_to([0, -0.4, 0])
        self.play(Create(trail[0]), Write(trail[1]), run_time=1.1)
        self.wait(6.0)

        # State 3 — proof is not liability
        proof = card("proof\nwho asked, who approved", "teal", 3.8, 1.0, font_size=14).move_to([-2.1, -1.9, 0])
        liability = card("liability\nwho pays?  not stated: open", "crimson", 3.8, 1.0, font_size=14).move_to([2.1, -1.9, 0])
        self.play(Create(proof[0]), Write(proof[1]), run_time=0.9)
        self.wait(2.5)
        self.play(Create(liability[0]), Write(liability[1]), run_time=0.9)
        self.wait(1.4)
        self.play(Indicate(liability, color=PALETTE["gold"]), run_time=1.0)
        self.wait(1.0)
