"""
Manim scenes for what-is-rlhf
B01_SupervisedFineTuning  — stage 1: labelers write demonstrations, model imitates them
B02_RewardModel           — stage 2: labelers rank answers, a reward model learns one score
B03_PPOOptimization       — stage 3: answer -> score -> PPO update loop, drift penalty, ChatGPT
B04_ConstitutionalAI      — no human data on harmlessness; critique and revise against principles
B04B_RLAIF                — an AI judge replaces the human ranker; comparable results; limits

Sources: Ouyang et al. 2022 (InstructGPT); OpenAI, Introducing ChatGPT (2022);
Bai et al. 2022 (Constitutional AI); Anthropic, Claude's Constitution (2023);
Lee et al. 2023 (RLAIF vs. RLHF). Answer letters in B02 are illustrative,
and no scene shows an invented score or metric.
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


def arrow_between(a, b):
    return Arrow(a.get_right(), b.get_left(), buff=0.1, color=PALETTE["ink"], stroke_width=2)


def stage_strip(active):
    """The three RLHF stages as a small strip, with the current one highlighted."""
    names = ["1  fine-tune", "2  reward model", "3  PPO"]
    cards = VGroup(*[
        card(n, "gold" if i == active else "slate", 2.4, 0.6, font_size=14,
             text_color="ink" if i == active else "slate")
        for i, n in enumerate(names)
    ]).arrange(RIGHT, buff=0.5).move_to([0, 1.6, 0])
    arrows = VGroup(arrow_between(cards[0], cards[1]), arrow_between(cards[1], cards[2]))
    return cards, arrows


class B01_SupervisedFineTuning(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Stage 1:", "Supervised Fine-Tuning")
        self.add(title)

        # State 1 — the three stages, stage 1 highlighted
        stages, stage_arrows = stage_strip(0)
        for i, s in enumerate(stages):
            self.play(Create(s[0]), Write(s[1]), run_time=0.6)
            if i < len(stage_arrows):
                self.play(GrowArrow(stage_arrows[i]), run_time=0.3)
        self.play(Indicate(stages[0], color=PALETTE["gold"]), run_time=0.8)
        self.wait(2.5)

        # State 2 — prompt -> labeler-written answer -> fine-tuned model
        flow = VGroup(
            card("real prompt", "slate", 2.3, 1.0),
            card("labeler writes\nan example answer", "teal", 2.6, 1.0, font_size=14),
            card("fine-tune the\npretrained model", "teal", 2.6, 1.0, font_size=14),
        ).arrange(RIGHT, buff=0.6).move_to([0, -0.4, 0])
        flow_arrows = VGroup(arrow_between(flow[0], flow[1]), arrow_between(flow[1], flow[2]))
        for i, f in enumerate(flow):
            self.play(Create(f[0]), Write(f[1]), run_time=0.8)
            if i < len(flow_arrows):
                self.play(GrowArrow(flow_arrows[i]), run_time=0.4)
            self.wait(3.85)

        bottom = Text(
            "the model starts by imitating the people who wrote the examples",
            color=PALETTE["slate"], font_size=14, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.2)
        self.wait(1.0)


class B02_RewardModel(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Stage 2:", "The Reward Model")
        self.add(title)

        # State 1 — several answers to the same prompt
        prompt = card("same prompt", "slate", 2.6, 0.6, font_size=14).move_to([0, 1.7, 0])
        self.play(Create(prompt[0]), Write(prompt[1]), run_time=0.8)
        answers = VGroup(*[
            card(f"answer {k}", "teal", 1.6, 0.7, font_size=14) for k in "ABCD"
        ]).arrange(RIGHT, buff=0.35).move_to([0, 0.6, 0])
        for a in answers:
            self.play(Create(a[0]), Write(a[1]), run_time=0.5)
        self.wait(3.0)

        # State 2 — labelers rank them; ranking is faster than writing
        ranking = card("labeler ranks:  B  >  D  >  A  >  C", "gold", 7.0, 0.7,
                       text_color="ink").move_to([0, -0.6, 0])
        self.play(Create(ranking[0]), Write(ranking[1]), run_time=1.0)
        self.wait(2.0)
        faster = Text("ranking is much faster than writing",
                      color=PALETTE["slate"], font_size=14, font=BODY_FONT).move_to([0, -1.3, 0])
        self.play(Write(faster), run_time=0.8)
        self.wait(1.4)

        # State 3 — a separate model learns the rankings and outputs one score
        self.play(FadeOut(answers), FadeOut(faster), run_time=0.6)
        rm = VGroup(
            card("reward model", "teal", 3.0, 0.9),
            card("one score per answer\n(predicted preference)", "sage", 3.8, 0.9,
                 font_size=14, text_color="teal"),
        ).arrange(RIGHT, buff=0.8).move_to([0, -2.2, 0])
        rm_arrow = arrow_between(rm[0], rm[1])
        self.play(Create(rm[0][0]), Write(rm[0][1]), run_time=0.9)
        self.play(GrowArrow(rm_arrow), run_time=0.4)
        self.play(Create(rm[1][0]), Write(rm[1][1]), run_time=0.9)
        self.wait(3.8)
        self.play(Indicate(rm[0], color=PALETTE["gold"]), run_time=0.8)
        self.wait(1.0)


class B03_PPOOptimization(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Stage 3:", "Reinforcement Learning with PPO")
        self.add(title)

        # State 1 — the loop: answer -> score -> update
        loop = VGroup(
            card("model answers\na new prompt", "teal", 2.5, 1.0, font_size=14),
            card("reward model\nscores it", "teal", 2.5, 1.0, font_size=14),
            card("PPO nudges it toward\nhigher scores", "gold", 2.8, 1.0, font_size=14,
                 text_color="ink"),
        ).arrange(RIGHT, buff=0.55).move_to([0, 1.1, 0])
        loop_arrows = VGroup(arrow_between(loop[0], loop[1]), arrow_between(loop[1], loop[2]))
        for i, step in enumerate(loop):
            self.play(Create(step[0]), Write(step[1]), run_time=0.8)
            if i < len(loop_arrows):
                self.play(GrowArrow(loop_arrows[i]), run_time=0.4)
            self.wait(2.6)
        repeat = Text("repeat", color=PALETTE["ink"], font_size=14, font=BODY_FONT).move_to([0, 0.2, 0])
        self.play(Write(repeat), run_time=0.5)
        self.wait(1.4)

        # State 2 — the drift penalty
        penalty = card("penalty: don't drift too far from the stage-1 model", "crimson", 7.6, 0.8,
                       font_size=14).move_to([0, -0.8, 0])
        self.play(Create(penalty[0]), Write(penalty[1]), run_time=1.0)
        self.wait(4.2)

        # State 3 — ChatGPT used the same methods
        chatgpt = card("ChatGPT: same methods,\nstarting from a GPT-3.5-series model (OpenAI, 2022)",
                       "slate", 7.8, 1.0, font_size=14).move_to([0, -2.1, 0])
        self.play(Create(chatgpt[0]), Write(chatgpt[1]), run_time=1.2)
        self.wait(4.3)
        self.play(Indicate(chatgpt, color=PALETTE["gold"]), run_time=0.8)
        self.wait(1.0)


class B04_ConstitutionalAI(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("Constitutional AI", "")
        self.add(title)

        # State 1 — the cost problem
        cost = card("human preference labels: slow and expensive", "crimson", 7.0, 0.7,
                    font_size=15).move_to([0, 2.0, 0])
        self.play(Create(cost[0]), Write(cost[1]), run_time=1.0)
        self.wait(1.9)

        # State 2 — Anthropic's harmlessness route
        quote = card("\"no human data on harmlessness\"\n(Anthropic, Claude's Constitution, 2023)",
                     "gold", 7.0, 1.0, font_size=14, text_color="ink").move_to([0, 0.9, 0])
        self.play(Create(quote[0]), Write(quote[1]), run_time=1.2)
        self.play(Indicate(quote, color=PALETTE["gold"]), run_time=0.8)
        self.wait(7.7)

        # State 3 — constitution -> critique -> revise
        flow = VGroup(
            card("constitution:\nwritten principles", "slate", 2.5, 1.0, font_size=14),
            card("model critiques\nits own answer", "teal", 2.5, 1.0, font_size=14),
            card("model revises\nthe answer", "sage", 2.5, 1.0, font_size=14, text_color="teal"),
        ).arrange(RIGHT, buff=0.6).move_to([0, -0.7, 0])
        flow_arrows = VGroup(arrow_between(flow[0], flow[1]), arrow_between(flow[1], flow[2]))
        for i, f in enumerate(flow):
            self.play(Create(f[0]), Write(f[1]), run_time=0.8)
            if i < len(flow_arrows):
                self.play(GrowArrow(flow_arrows[i]), run_time=0.4)
            self.wait(1.2)

        bottom = Text(
            "method: Constitutional AI (Bai et al., 2022)",
            color=PALETTE["slate"], font_size=14, font=BODY_FONT
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(bottom), run_time=1.0)
        self.wait(1.0)


class B04B_RLAIF(Scene):
    def construct(self):
        self.camera.background_color = PALETTE["bg"]
        title = make_title("RLAIF:", "Reinforcement Learning from AI Feedback")
        self.add(title)

        # State 1 — who picks the better answer
        compare = VGroup(
            card("RLHF\na person picks\nthe better answer", "slate", 3.6, 1.4, font_size=14),
            card("RLAIF\nan AI model picks\nthe better answer", "teal", 3.6, 1.4, font_size=14),
        ).arrange(RIGHT, buff=0.6).move_to([0, 1.0, 0])
        self.play(Create(compare[0][0]), Write(compare[0][1]), run_time=0.9)
        self.wait(3.0)
        self.play(Create(compare[1][0]), Write(compare[1][1]), run_time=0.9)
        self.play(Indicate(compare[1], color=PALETTE["gold"]), run_time=0.8)
        self.wait(5.2)

        # State 2 — the 2023 Google result
        result = card("Google, 2023: RLAIF comparable to RLHF\n(Lee et al., RLAIF vs. RLHF)",
                      "sage", 7.8, 1.0, font_size=14, text_color="teal").move_to([0, -0.7, 0])
        self.play(Create(result[0]), Write(result[1]), run_time=1.1)
        self.wait(3.1)

        # State 3 — the limits
        limits = card("humans still write the principles\nfeedback is only as good as the AI judge",
                      "crimson", 7.8, 1.0, font_size=14).move_to([0, -2.1, 0])
        self.play(Create(limits[0]), Write(limits[1]), run_time=1.1)
        self.wait(4.6)
        self.play(Indicate(limits, color=PALETTE["gold"]), run_time=0.8)
        self.wait(1.0)
