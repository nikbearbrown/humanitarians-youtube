import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]
    / "vox/aspects/explainer/vox-explainer/manim"))

from vox_graphics import *
from vox_graphics import _quote_scene

DUR = {
    "B01": 4.0,
    "B02": 11.0, "B04": 9.0, "B05": 9.0,
    "B07": 10.0, "B08": 8.0, "B09": 9.0,
    "B10": 8.0,  "B11": 8.0,
    "B12": 18.0,
}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

# ── B01 — Title ───────────────────────────────────────────────────────────────

class B01_Title(Scene):
    def construct(self):
        total = DUR["B01"]
        eye = Text("COMPUTATIONAL SKEPTICISM", font=DISPLAY, color=TEAL, font_size=18)
        t1 = Text("The Model Isn't Broken —", font=DISPLAY, color=INK, font_size=30, weight=BOLD)
        t2 = Text("It's Honest About What It Learned", font=DISPLAY, color=CRIMSON,
                  font_size=30, weight=BOLD)
        block = VGroup(t1, t2).arrange(DOWN, buff=0.18).move_to(UP * 0.15)
        u = Line(t2.get_corner(DL) + DOWN * 0.13, t2.get_corner(DR) + DOWN * 0.13,
                 color=GOLD, stroke_width=2)
        eye.next_to(block, UP, buff=0.55)
        self.play(FadeIn(eye), run_time=0.6)
        self.play(FadeIn(block), Create(u), run_time=1.2)
        self.wait(max(0.3, total - 1.8))


# ── B02 — PandaFlip ───────────────────────────────────────────────────────────

class B02_PandaFlip(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Left: original image
        box_orig = Rectangle(width=4.0, height=3.2, color=SLATE, fill_color=SLATE, fill_opacity=0.10, stroke_width=2).move_to(LEFT * 3.5 + UP * 0.3)
        lbl_orig = Text("[PANDA IMAGE]", font=DISPLAY, font_size=16, color=SLATE).move_to(box_orig)
        conf_orig = LabelChip("PANDA   94%", color=TEAL)
        conf_orig.move_to(LEFT * 3.5 + DOWN * 1.8)

        # Plus perturbation chip
        plus = Text("+ invisible noise", font=DISPLAY, font_size=16, color=INK).move_to(UP * 0.3)

        # Right: perturbed image
        box_pert = Rectangle(width=4.0, height=3.2, color=GOLD, fill_color=GOLD, fill_opacity=0.10, stroke_width=2).move_to(RIGHT * 3.5 + UP * 0.3)
        lbl_pert = Text("[SAME PANDA\n+ perturbation]", font=DISPLAY, font_size=16, color=GOLD).move_to(box_pert)
        conf_pert = LabelChip("GIBBON  99.3%", color=CRIMSON)
        conf_pert.move_to(RIGHT * 3.5 + DOWN * 1.8)

        caption = Text("The panda never moved", font=DISPLAY, font_size=18, color=INK).move_to(DOWN * 2.8)

        self.play(GrowFromCenter(box_orig), run_time=0.5)
        self.play(Write(lbl_orig), run_time=0.4)
        self.play(GrowFromCenter(conf_orig), run_time=0.4)
        self.play(Write(plus), run_time=0.4)
        self.play(GrowFromCenter(box_pert), run_time=0.5)
        self.play(Write(lbl_pert), run_time=0.4)
        self.play(GrowFromCenter(conf_pert), run_time=0.4)
        self.play(Write(caption), run_time=0.5)
        self.wait(DUR["B02"] - 4.5)


# ── B04 — TwoReactions ────────────────────────────────────────────────────────

class B04_TwoReactions(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        hdr_wrong = Rectangle(width=5.5, height=0.6, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.20, stroke_width=1.5).move_to(LEFT * 3.2 + UP * 2.8)
        hdr_right = Rectangle(width=5.5, height=0.6, color=TEAL,   fill_color=TEAL,   fill_opacity=0.20, stroke_width=1.5).move_to(RIGHT * 3.2 + UP * 2.8)
        t_wrong   = Text("NATURAL REACTION", font=DISPLAY, font_size=17, color=CRIMSON).move_to(hdr_wrong)
        t_right   = Text("CORRECT DIAGNOSIS", font=DISPLAY, font_size=17, color=TEAL).move_to(hdr_right)

        body_wrong = Rectangle(width=5.5, height=3.2, color=CRIMSON, fill_opacity=0, stroke_width=1.5).move_to(LEFT * 3.2 + DOWN * 0.4)
        body_right = Rectangle(width=5.5, height=3.2, color=TEAL,   fill_opacity=0, stroke_width=1.5).move_to(RIGHT * 3.2 + DOWN * 0.4)

        w1 = Text("\"The model is brittle\"", font=DISPLAY, font_size=16, color=CRIMSON).move_to(LEFT * 3.2 + UP * 0.9)
        w2 = Text("→ Patch it", font=MONO, font_size=15, color=INK).move_to(LEFT * 3.2 + UP * 0.15)
        w3 = Text("→ Add more training data", font=MONO, font_size=15, color=INK).move_to(LEFT * 3.2 + DOWN * 0.55)
        w4 = Text("→ Smooth the outputs", font=MONO, font_size=15, color=INK).move_to(LEFT * 3.2 + DOWN * 1.25)
        w5 = Text("Attack surface moves.\nProblem stays.", font=DISPLAY, font_size=14, color=CRIMSON).move_to(LEFT * 3.2 + DOWN * 2.1)

        r1 = Text("\"The model learned\nthe wrong thing\"", font=DISPLAY, font_size=16, color=TEAL).move_to(RIGHT * 3.2 + UP * 0.9)
        r2 = Text("→ Interrogate the representation", font=MONO, font_size=15, color=INK).move_to(RIGHT * 3.2 + DOWN * 0.2)
        r3 = Text("→ Ask what it's betting on", font=MONO, font_size=15, color=INK).move_to(RIGHT * 3.2 + DOWN * 0.9)
        r4 = Text("Perturbation = diagnostic.", font=DISPLAY, font_size=14, color=TEAL).move_to(RIGHT * 3.2 + DOWN * 2.1)

        self.play(GrowFromCenter(hdr_wrong), GrowFromCenter(hdr_right), run_time=0.5)
        self.play(Write(t_wrong), Write(t_right), run_time=0.5)
        self.play(GrowFromCenter(body_wrong), GrowFromCenter(body_right), run_time=0.5)
        self.play(Write(w1), Write(r1), run_time=0.4)
        self.play(Write(w2), Write(r2), run_time=0.4)
        self.play(Write(w3), Write(r3), run_time=0.4)
        self.play(Write(w4), run_time=0.3)
        self.play(Write(w5), Write(r4), run_time=0.4)
        self.wait(DUR["B04"] - 4.0)


# ── B05 — TwoChannels ─────────────────────────────────────────────────────────

class B05_TwoChannels(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        # Shape channel (left)
        box_shape = Rectangle(width=4.5, height=3.5, color=SLATE, fill_color=SLATE, fill_opacity=0.10, stroke_width=2).move_to(LEFT * 3.2 + UP * 0.3)
        lbl_shape = Text("SHAPE CHANNEL", font=DISPLAY, font_size=17, color=SLATE).move_to(LEFT * 3.2 + UP * 1.8)
        desc_shape = Text("outlines · pose · color\n[unchanged by perturbation]", font=DISPLAY, font_size=14, color=SLATE).move_to(LEFT * 3.2 + UP * 0.3)
        chip_shape = LabelChip("STABLE", color=SLATE)
        chip_shape.move_to(LEFT * 3.2 + DOWN * 1.6)

        # Texture channel (right)
        box_tex = Rectangle(width=4.5, height=3.5, color=GOLD, fill_color=GOLD, fill_opacity=0.10, stroke_width=2).move_to(RIGHT * 3.2 + UP * 0.3)
        lbl_tex = Text("TEXTURE CHANNEL", font=DISPLAY, font_size=17, color=GOLD).move_to(RIGHT * 3.2 + UP * 1.8)
        desc_tex1 = Text("high-frequency\nstatistical patterns\n[invisible to humans]", font=DISPLAY, font_size=14, color=INK).move_to(RIGHT * 3.2 + UP * 0.4)
        chip_before = LabelChip("panda-signature", color=TEAL)
        arrow_tex = Text("→", font=DISPLAY, font_size=22, color=GOLD).move_to(RIGHT * 3.2 + DOWN * 1.4)
        chip_after = LabelChip("gibbon-signature", color=CRIMSON)

        chip_before.move_to(RIGHT * 1.8 + DOWN * 1.7)
        chip_after.move_to(RIGHT * 4.6 + DOWN * 1.7)

        self.play(GrowFromCenter(box_shape), GrowFromCenter(box_tex), run_time=0.6)
        self.play(Write(lbl_shape), Write(lbl_tex), run_time=0.5)
        self.play(Write(desc_shape), Write(desc_tex1), run_time=0.5)
        self.play(GrowFromCenter(chip_shape), run_time=0.4)
        self.play(GrowFromCenter(chip_before), run_time=0.4)
        self.play(Write(arrow_tex), run_time=0.3)
        self.play(GrowFromCenter(chip_after), run_time=0.4)
        self.wait(DUR["B05"] - 4.1)


# ── B07 — ProxyFeature ────────────────────────────────────────────────────────

class B07_ProxyFeature(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        boxes_data = [
            ("TRAINING",      "model bets on proxy features\n(texture patterns correlated\nwith panda labels)",   INK,     LEFT * 3.8),
            ("DEPLOYMENT",    "adversary pushes texture\ntoward gibbon-signature",                                 GOLD,    ORIGIN),
            ("MODEL FLIPS",   "shape unchanged · texture slid\n→ 99.3% GIBBON",                                   CRIMSON, RIGHT * 3.8),
        ]

        title = Text("Why the Flip Happens", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)
        self.play(Write(title), run_time=0.4)

        prev_box = None
        for label, desc, col, pos in boxes_data:
            box = Rectangle(width=3.4, height=2.5, color=col, fill_color=col, fill_opacity=0.10, stroke_width=2)
            box.move_to(pos + UP * 0.3)
            lbl = Text(label, font=DISPLAY, font_size=16, color=col).move_to(pos + UP * 1.1)
            desc_txt = Text(desc, font=MONO, font_size=13, color=INK).move_to(pos + UP * 0.1)

            self.play(GrowFromCenter(box), run_time=0.4)
            self.play(Write(lbl), run_time=0.3)
            self.play(Write(desc_txt), run_time=0.4)

            if prev_box is not None:
                arr = Line(prev_box.get_right(), box.get_left(), color=INK, stroke_width=2)
                self.play(GrowFromEdge(arr, LEFT), run_time=0.3)
            prev_box = box

        self.wait(DUR["B07"] - 4.5)


# ── B08 — QuoteProxy ─────────────────────────────────────────────────────────

class B08_QuoteProxy(Scene):
    def construct(self):
        _quote_scene(
            self,
            "The model has learned what I will call a proxy — a feature "
            "in the input distribution that correlated reliably with the "
            "right label on the training data. The engineers thought the "
            "model had learned what pandas look like. The model had actually "
            "learned the statistical signature of pixel arrangements that "
            "occurred in panda training images.",
            "Computational Skepticism for AI, Chapter 4",
            None,
            "proxy",
            DUR["B08"],
        )


# ── B09 — WrongDiagnosis ──────────────────────────────────────────────────────

class B09_WrongDiagnosis(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        hdr_frag = Rectangle(width=5.5, height=0.6, color=CRIMSON, fill_color=CRIMSON, fill_opacity=0.20, stroke_width=1.5).move_to(LEFT * 3.2 + UP * 2.8)
        hdr_prox = Rectangle(width=5.5, height=0.6, color=TEAL,   fill_color=TEAL,   fill_opacity=0.20, stroke_width=1.5).move_to(RIGHT * 3.2 + UP * 2.8)
        t_frag   = Text("FRAGILE FRAMING", font=DISPLAY, font_size=17, color=CRIMSON).move_to(hdr_frag)
        t_prox   = Text("PROXY FRAMING", font=DISPLAY, font_size=17, color=TEAL).move_to(hdr_prox)

        body_frag = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_opacity=0, stroke_width=1.5).move_to(LEFT * 3.2 + DOWN * 0.6)
        body_prox = Rectangle(width=5.5, height=3.8, color=TEAL,   fill_opacity=0, stroke_width=1.5).move_to(RIGHT * 3.2 + DOWN * 0.6)

        f1 = Text("→ surface hardening", font=MONO, font_size=15, color=INK).move_to(LEFT * 3.2 + UP * 0.8)
        f2 = Text("→ new attack finds new proxy", font=MONO, font_size=15, color=INK).move_to(LEFT * 3.2 + UP * 0.05)
        f3 = Text("→ attack surface moves", font=MONO, font_size=15, color=INK).move_to(LEFT * 3.2 + DOWN * 0.7)
        f4 = Text("underlying gap: unchanged", font=DISPLAY, font_size=14, color=CRIMSON).move_to(LEFT * 3.2 + DOWN * 1.8)

        p1 = Text("→ ask: what is it betting on?", font=MONO, font_size=15, color=INK).move_to(RIGHT * 3.2 + UP * 0.8)
        p2 = Text("→ interrogate representation", font=MONO, font_size=15, color=INK).move_to(RIGHT * 3.2 + UP * 0.05)
        p3 = Text("→ find the proxy", font=MONO, font_size=15, color=INK).move_to(RIGHT * 3.2 + DOWN * 0.7)
        p4 = Text("engineering problem: addressable", font=DISPLAY, font_size=14, color=TEAL).move_to(RIGHT * 3.2 + DOWN * 1.8)

        self.play(GrowFromCenter(hdr_frag), GrowFromCenter(hdr_prox), run_time=0.5)
        self.play(Write(t_frag), Write(t_prox), run_time=0.5)
        self.play(GrowFromCenter(body_frag), GrowFromCenter(body_prox), run_time=0.5)
        self.play(Write(f1), Write(p1), run_time=0.4)
        self.play(Write(f2), Write(p2), run_time=0.4)
        self.play(Write(f3), Write(p3), run_time=0.4)
        self.play(Write(f4), Write(p4), run_time=0.4)
        self.wait(DUR["B09"] - 4.1)


# ── B10 — QuoteHonest ────────────────────────────────────────────────────────

class B10_QuoteHonest(Scene):
    def construct(self):
        _quote_scene(
            self,
            "Adversarial perturbations are not bugs, they are features — "
            "genuinely predictive, statistically real patterns that happen "
            "to be imperceptible and meaningless to humans. They reveal "
            "what the model actually responds to. They tell you which "
            "features the model has bet on.",
            "Computational Skepticism for AI, Chapter 4",
            None,
            "not bugs",
            DUR["B10"],
        )


# ── B11 — Implication ────────────────────────────────────────────────────────

class B11_Implication(Scene):
    def construct(self):
        DISPLAY = "Montserrat"
        MONO    = "PT Mono"

        title = Text("What 94% accuracy tells you", font=DISPLAY, font_size=22, color=GOLD).move_to(UP * 3.1)

        rows = [
            ("✗  Does NOT mean: robust against unseen inputs",  CRIMSON),
            ("✗  Does NOT mean: model learned intended features", CRIMSON),
            ("✓  DOES mean: its proxies won on training data",   TEAL),
            ("→  Perturbation = the audit that checks the rest", GOLD),
        ]

        self.play(Write(title), run_time=0.4)
        y_start = 1.8
        for i, (text, col) in enumerate(rows):
            y = y_start - i * 1.1
            box = Rectangle(width=9.5, height=0.85, color=col, fill_color=col, fill_opacity=0.10, stroke_width=1.5).move_to(UP * y)
            txt = Text(text, font=MONO, font_size=16, color=col if col != GOLD else GOLD).move_to(UP * y)
            self.play(GrowFromCenter(box), run_time=0.3)
            self.play(Write(txt), run_time=0.3)

        self.wait(DUR["B11"] - 3.8)


# ── B12 — ExampleProxy ───────────────────────────────────────────────────────

class B12_ExampleProxy(Scene):
    """THE EXAMPLE — skin lesion classifier learned 'ruler = cancer' as proxy."""
    def construct(self):
        total = DUR["B12"]
        title = Text("Skin Lesion Classifier — proxy learned", font=DISPLAY,
                     font_size=20, color=GOLD)
        title.move_to(UP * 3.1)

        col_l = Rectangle(width=5.5, height=3.8, color=TEAL, fill_color=TEAL,
                          fill_opacity=0.08, stroke_width=2).move_to(LEFT * 3.2 + DOWN * 0.1)
        col_r = Rectangle(width=5.5, height=3.8, color=CRIMSON, fill_color=CRIMSON,
                          fill_opacity=0.08, stroke_width=2).move_to(RIGHT * 3.2 + DOWN * 0.1)

        lbl_l = Text("Training data", font=DISPLAY, font_size=22, color=TEAL, weight=BOLD)
        lbl_l.move_to(col_l.get_top() + DOWN * 0.45)
        val_l1 = Text("malignant: ruler present 89%", font=MONO, font_size=18, color=TEAL)
        val_l1.move_to(col_l.get_center() + UP * 0.3)
        val_l2 = Text("benign: ruler present 12%", font=MONO, font_size=18, color=TEAL)
        val_l2.move_to(col_l.get_center() + DOWN * 0.4)
        val_l3 = Text("test accuracy: 92%", font=MONO, font_size=18, color=TEAL)
        val_l3.move_to(col_l.get_center() + DOWN * 1.1)

        lbl_r = Text("Proxy learned", font=DISPLAY, font_size=22, color=CRIMSON, weight=BOLD)
        lbl_r.move_to(col_r.get_top() + DOWN * 0.45)
        val_r1 = Text('"ruler = cancer"', font=MONO, font_size=24, color=CRIMSON)
        val_r1.move_to(col_r.get_center() + UP * 0.2)
        val_r2 = Text("without rulers: 62%", font=MONO, font_size=18, color=CRIMSON)
        val_r2.move_to(col_r.get_center() + DOWN * 0.8)

        note_rect = Rectangle(width=9.5, height=0.52, fill_color=CRIMSON, fill_opacity=0.10,
                              stroke_width=1.5, color=CRIMSON).move_to(DOWN * 2.55)
        note_txt = Text("model was honest — it learned what the training data taught it",
                        font=SERIF, font_size=19, color=CRIMSON)
        note_txt.move_to(note_rect.get_center())

        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(col_l), FadeIn(lbl_l), run_time=0.7)
        self.play(FadeIn(val_l1), FadeIn(val_l2), FadeIn(val_l3), run_time=0.6)
        self.play(FadeIn(col_r), FadeIn(lbl_r), run_time=0.7)
        self.play(FadeIn(val_r1), FadeIn(val_r2), run_time=0.6)
        self.play(FadeIn(note_rect), FadeIn(note_txt), run_time=0.7)
        self.wait(max(0.5, total - 4.0))
