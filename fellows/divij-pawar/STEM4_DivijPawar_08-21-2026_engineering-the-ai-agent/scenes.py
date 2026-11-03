"""scenes.py — Manim scenes for engineering-the-ai-agent (claude-divij).

Palette: cream #F2F0E9, ink #3D3929, terracotta #D97757, soft #73705F,
ghost #A9A491 — the Claude fidelity palette per ai-explainer SKILL.md. ONE
accent per beat.

Type: Montserrat (DISPLAY, structural default) / EB Garamond (SERIF,
editorial voice only) / PT Mono (MONO, data only) — see graphics_lib.py.
Boxes are content-fitted via auto_box, never hand-measured.

Doctrine note specific to this reel: the source script called for a real
dashcam photo/video of a pothole (B00 visual notes) and a phone-on-dashboard
shot (Act 2, step 1). Under nopunt, only a genuine archival photograph of a
real person/place/document/event is a legitimate HOLD — a generic stock
pothole photo standing in for the concept is a PUNT. Both are rebuilt here
as drawn diagrams (a line-mark pothole on a road, a GPS tick path) instead.
See SOURCES.md.

Content note: B02 (orchestration patterns) and B08 (the anti-pattern) carry
no equivalent in the source script — they're original synthesis added after
a human-review pass judged the case-study walkthrough alone too thin to be
generalizable. See PEDAGOGY.md / SOURCES.md for the reasoning and the
factual check on those additions.

Timing: self.wait() calls below are sized against estimated_duration_s in
beat_sheet.json (pre-audio). Per BUILD-PROMPT.md Step 3, RETIME every scene
against actual_duration_s once Kokoro has run — do not skip this.
"""
import numpy as np
from graphics_lib import *

# ── Palette (claude-stage retint, per ai-explainer SKILL.md) ──────────────────
BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")
SOFT  = ManimColor("#73705F")
GHOST = ManimColor("#A9A491")

STAGES = ["Perception", "Tool-Use", "Grounding", "Synthesis"]


def strike(mobj, color=None):
    return Line(mobj.get_left() + LEFT * 0.08, mobj.get_right() + RIGHT * 0.08,
                color=color if color is not None else ACC, stroke_width=3.0)


def pipeline_row(active):
    """Four stage chips with connecting arrows. `active` = set of indices
    (0-3) to light in ACC; the rest sit dimmed to ghost opacity."""
    chips = VGroup(*[label_chip(s, SOFT) for s in STAGES])
    chips.arrange(RIGHT, buff=0.55)
    arrows = VGroup(*[
        Arrow(chips[i].get_right(), chips[i + 1].get_left(), color=GHOST,
              stroke_width=2, buff=0.1, max_tip_length_to_length_ratio=0.25)
        for i in range(3)
    ])
    for i, c in enumerate(chips):
        if i in active:
            c[0].set_fill(ACC, opacity=1)
        else:
            c.set_opacity(0.35)
    return chips, arrows


# ─────────────────────────────────────────────────────────────────────────────
#  B01_TwoWaysToWriteCode   (target ~37s)
#  The framework: a tangled if/else tree resolves into a clean hub-and-spoke
#  model, then the truth-table test is named as the deciding question.
# ─────────────────────────────────────────────────────────────────────────────
class B01_TwoWaysToWriteCode(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Two Ways to Write Code", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(0.6)

        divider = Line([0, 2.4, 0], [0, -3.2, 0], color=GHOST, stroke_width=2)
        self.play(Create(divider), run_time=0.5)

        left_lab = label("Traditional", size=28, color=SOFT).move_to([-3.5, 2.0, 0])
        right_lab = label("Agentic", size=28, color=SOFT).move_to([3.5, 2.0, 0])
        self.play(FadeIn(left_lab), FadeIn(right_lab), run_time=0.5)
        self.wait(1.2)

        # Left: a deterministic tangle of if/else branch lines — hand-authored
        # coordinates (not randomised) so the shape is reviewable and stays
        # clear of the divider at x=0.
        branches = VGroup(
            Line([-3.5, 1.2, 0], [-4.6, 0.6, 0], color=SOFT, stroke_width=2),
            Line([-3.5, 1.2, 0], [-2.4, 0.6, 0], color=SOFT, stroke_width=2),
            Line([-4.6, 0.6, 0], [-5.4, 0.0, 0], color=SOFT, stroke_width=2),
            Line([-4.6, 0.6, 0], [-4.0, 0.0, 0], color=SOFT, stroke_width=2),
            Line([-2.4, 0.6, 0], [-3.0, 0.0, 0], color=SOFT, stroke_width=2),
            Line([-2.4, 0.6, 0], [-1.8, 0.0, 0], color=SOFT, stroke_width=2),
            Line([-5.4, 0.0, 0], [-5.7, -0.6, 0], color=SOFT, stroke_width=2),
            Line([-5.4, 0.0, 0], [-5.1, -0.6, 0], color=SOFT, stroke_width=2),
            Line([-4.0, 0.0, 0], [-4.3, -0.6, 0], color=SOFT, stroke_width=2),
            Line([-4.0, 0.0, 0], [-3.7, -0.6, 0], color=SOFT, stroke_width=2),
        )
        self.play(LaggedStart(*[Create(b) for b in branches], lag_ratio=0.08),
                   run_time=1.6)
        edge_note = label("hundreds of if/else branches", size=23, color=SOFT)
        edge_note.move_to([-3.5, -1.3, 0])
        self.play(FadeIn(edge_note), run_time=0.5)
        self.wait(4.3)  # retimed to real audio (31.38s) — was 2.2

        # Right: hub and spoke. Tools/Action sit 1.8 apart from Memory
        # (not the 1.5 tried first) so their chip boxes clear each other —
        # a tighter spacing left corners touching at these font sizes.
        hub = label_chip("Model", INK).move_to([3.5, 0.6, 0])
        sats = VGroup(
            label_chip("Tools", SOFT).move_to([1.7, -1.1, 0]),
            label_chip("Memory", SOFT).move_to([3.5, -1.9, 0]),
            label_chip("Action", SOFT).move_to([5.3, -1.1, 0]),
        )
        spokes = VGroup(*[
            Line(hub.get_bottom(), s.get_top(), color=GHOST, stroke_width=2)
            for s in sats
        ])
        self.play(FadeIn(hub), run_time=0.5)
        self.play(LaggedStart(*[Create(s) for s in spokes], lag_ratio=0.2),
                   LaggedStart(*[FadeIn(s) for s in sats], lag_ratio=0.2),
                   run_time=1.3)
        self.wait(4.3)  # retimed to real audio (31.38s) — was 2.2

        test = label("ask: a truth table —\nor a judgment call?", size=20, color=SOFT,
                     line_spacing=0.85).move_to([3.5, -2.7, 0])
        self.play(FadeIn(test), run_time=0.5)
        self.wait(5.3)  # retimed to real audio (31.38s) — was 3.2

        # Divider extended the full height of the frame — it pierced
        # straight through the landing line once that line fades in
        # (caught in the still-frame QC pass). Fade it out with the left
        # half's scratch content instead of leaving it on screen.
        land = serif("Isolate the fuzzy reasoning.\nKeep everything else deterministic.",
                     size=29, color=INK, line_spacing=0.9).move_to(DOWN * 3.0)
        self.play(FadeOut(branches), FadeOut(edge_note), FadeOut(divider),
                  FadeOut(test), FadeIn(land), run_time=0.7)
        self.wait(8.6)  # retimed to real audio (31.38s) — was 6.5


# ─────────────────────────────────────────────────────────────────────────────
#  B02_OrchestrationPatterns   (target ~45s)
#  A second, independent framework beat — the architecture decision the
#  source script never raised: who decides what happens next?
# ─────────────────────────────────────────────────────────────────────────────
class B02_OrchestrationPatterns(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Who Decides What's Next?", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(0.8)

        divider = Line([0, 2.2, 0], [0, -2.6, 0], color=GHOST, stroke_width=2)
        self.play(Create(divider), run_time=0.5)

        left_lab = label("Agent Loop", size=26, color=SOFT).move_to([-3.5, 1.9, 0])
        right_lab = label("Fixed Pipeline", size=26, color=SOFT).move_to([3.5, 1.9, 0])
        self.play(FadeIn(left_lab), FadeIn(right_lab), run_time=0.5)
        self.wait(4.3)  # retimed to real audio (38.31s) — was 1.4

        # Left: a model deciding what's next, in no fixed order — dashed
        # lines (uncertain) fan out to three tools with no implied sequence.
        model = label_chip("Model", INK).move_to([-3.5, 0.7, 0])
        tools3 = VGroup(
            label("tool A", size=21, color=SOFT).move_to([-5.4, -0.9, 0]),
            label("tool B", size=21, color=SOFT).move_to([-3.5, -1.5, 0]),
            label("tool C", size=21, color=SOFT).move_to([-1.7, -0.9, 0]),
        )
        uncertain = VGroup(*[
            DashedLine(model.get_bottom(), tl.get_top(), color=GHOST, dash_length=0.1)
            for tl in tools3
        ])
        self.play(FadeIn(model), run_time=0.5)
        self.play(FadeIn(tools3), Create(uncertain), run_time=0.7)
        note_l = label("decides the order itself", size=21, color=SOFT)
        note_l.move_to([-3.5, -2.2, 0])
        self.play(FadeIn(note_l), run_time=0.4)
        self.wait(5.9)  # retimed to real audio (38.31s) — was 3.0

        # Right: the same four-stage pipeline, always in this order.
        chips, arrows = pipeline_row(active={0, 1, 2, 3})
        row = VGroup(chips, arrows).scale(0.6).move_to([3.5, 0.5, 0])
        self.play(FadeIn(row), run_time=0.6)
        note_r = label("always in this order", size=21, color=SOFT)
        note_r.move_to([3.5, -0.7, 0])
        self.play(FadeIn(note_r), run_time=0.4)
        self.wait(6.1)  # retimed to real audio (38.31s) — was 3.2

        pick = label("Pothole Reporter picks\nthe boring option, on purpose",
                     size=21, color=INK, line_spacing=0.85).move_to([3.5, -1.9, 0])
        self.play(FadeIn(pick), run_time=0.5)
        self.wait(6.5)  # retimed to real audio (38.31s) — was 3.6

        # Centered on the full frame (ORIGIN), not pinned to the bottom —
        # everything else has cleared by this point, so this is the sole
        # remaining content and reads better as a centered closing thought.
        land = serif("Predictability beats flexibility\nonce real consequences are on the line.",
                     size=27, color=INK, line_spacing=0.9).move_to(ORIGIN)
        self.play(FadeOut(divider), FadeOut(model), FadeOut(tools3),
                  FadeOut(uncertain), FadeOut(note_l), FadeOut(row), FadeOut(note_r),
                  FadeOut(pick), FadeOut(left_lab), FadeOut(right_lab),
                  FadeIn(land), run_time=0.8)
        self.wait(8.9)  # retimed to real audio (38.31s) — was 6.0


# ─────────────────────────────────────────────────────────────────────────────
#  B03_ThePotholeCase   (target ~29s)
#  The worked-example intro: a drawn pothole with an AI bounding box, then the
#  two open questions that make a photo insufficient.
# ─────────────────────────────────────────────────────────────────────────────
class B03_ThePotholeCase(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Pothole Reporter", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(0.8)

        repo = label("github.com/coding-parrot/pothole-reporter", size=22, color=SOFT)
        repo_box = auto_box(repo, h_pad=0.3, v_pad=0.18, color=GHOST)
        repo_grp = VGroup(repo_box, repo).move_to([0, 2.15, 0])
        self.play(FadeIn(repo_grp), run_time=0.5)
        self.wait(4.1)  # retimed to real audio (34.35s) — was 1.6

        # Real documentation photo from the project's own repo (MIT-licensed,
        # docs/example-pothole.jpg) — a genuine archival photo, a legitimate
        # nopunt HOLD, not a drawn stand-in. See SOURCES.md for attribution.
        photo = ImageMobject("assets/example-pothole.jpg")
        photo.height = 3.2
        photo.move_to([-4.3, -0.6, 0])
        self.play(FadeIn(photo), run_time=0.6)
        self.wait(1.0)

        box = DashedVMobject(
            Rectangle(width=1.15, height=0.8).move_to([-4.55, -1.1, 0]),
            num_dashes=16, color=ACC,
        )
        conf = label_chip("probable", ACC, size=20).next_to(box, UP, buff=0.2)
        self.play(Create(box), FadeIn(conf), run_time=0.7)
        self.wait(5.1)  # retimed to real audio (34.35s) — was 2.6

        stat = label("3 report types —\nonly 1 uses AI", size=24, color=SOFT,
                     line_spacing=0.85).move_to([2.3, 1.2, 0])
        self.play(FadeIn(stat), run_time=0.5)
        self.wait(4.7)  # retimed to real audio (34.35s) — was 2.2

        q1 = label("which contractor?", size=24, color=SOFT).move_to([2.3, -0.1, 0])
        q2 = label("which official?", size=24, color=SOFT).move_to([2.3, -0.8, 0])
        self.play(FadeIn(q1), FadeIn(q2), run_time=0.6)
        self.wait(5.5)  # retimed to real audio (34.35s) — was 3.0

        # Centered on the frame — clear of the photo column on the left
        # (photo's right edge sits well past x=-3.35).
        land = serif("A photo isn't an agent.\nAn agent bridges perception and action.",
                     size=28, color=INK, line_spacing=0.9).move_to(ORIGIN)
        self.play(FadeOut(q1), FadeOut(q2), FadeOut(stat), FadeIn(land), run_time=0.7)
        self.wait(9.0)  # retimed to real audio (34.35s) — was 6.5


# ─────────────────────────────────────────────────────────────────────────────
#  B04_TheContextGap   (target ~54s)
#  Step one of agentic engineering: isolate the unstructured piece and name
#  its narrow blast radius (left), then find what it still can't know
#  (right), resolving into two tools.
# ─────────────────────────────────────────────────────────────────────────────
class B04_TheContextGap(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("The Context Gap", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.0)

        vlm_txt = label("Vision-\nLanguage\nModel", size=25, color=INK, line_spacing=0.8)
        vlm_box = auto_box(vlm_txt, h_pad=0.4, v_pad=0.3, color=INK)
        vlm = VGroup(vlm_box, vlm_txt).move_to([-4.2, 1.5, 0])
        self.play(FadeIn(vlm), run_time=0.6)
        self.wait(1.4)

        env = VGroup(*[
            label(w, size=22, color=SOFT) for w in ("rain", "night", "any angle")
        ]).arrange(RIGHT, buff=0.5).move_to([-4.2, 0.3, 0])
        self.play(LaggedStart(*[FadeIn(w) for w in env], lag_ratio=0.25), run_time=0.9)
        self.wait(1.6)

        out = VGroup(
            label("find it", size=23, color=SOFT),
            label("size it", size=23, color=SOFT),
            label("call it: clear,\nprobable, uncertain,\nor absent", size=21,
                  color=SOFT, line_spacing=0.8),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        out_box = auto_box(out, h_pad=0.35, v_pad=0.28, color=SOFT)
        out_grp = VGroup(out_box, out).move_to([-4.2, -1.6, 0])
        # Starts from env's bottom, not vlm's — an arrow spanning the full
        # vlm-to-out_grp distance passed directly through the "night" label
        # in between (same x-center as both endpoints), rendering as a
        # stray vertical mark through the word. Caught in still-frame QC.
        arrow1 = Arrow(env.get_bottom() + DOWN * 0.1, out_grp.get_top(), color=SOFT,
                        stroke_width=2.5, buff=0.1)
        self.play(Create(arrow1), FadeIn(out_grp), run_time=0.7)
        self.wait(2.4)

        scope = label("small blast radius", size=20, color=ACC)
        scope.next_to(out_grp, DOWN, buff=0.3)
        self.play(FadeIn(scope), run_time=0.4)
        self.wait(3.6)

        not_enough = serif("But perception alone isn't enough.", size=27, color=SOFT)
        not_enough.move_to([2.6, 2.2, 0])
        self.play(FadeIn(not_enough), run_time=0.5)
        self.wait(2.6)

        knows = label("knows: what a pothole looks like", size=24, color=SOFT)
        knows.move_to([2.6, 1.0, 0])
        doesnt = label("doesn't know: whose road this is", size=24, color=ACC)
        doesnt.move_to([2.6, 0.3, 0])
        self.play(FadeIn(knows), run_time=0.5)
        self.wait(1.8)
        self.play(FadeIn(doesnt), run_time=0.5)
        self.wait(4.8)  # retimed to real audio (44.33s) — was 2.6

        halluc = label("guess the authority → risk\nnaming the wrong office", size=21,
                       color=ACC, line_spacing=0.8)
        halluc.move_to([2.6, -0.6, 0])
        self.play(FadeIn(halluc), run_time=0.5)
        self.wait(5.4)  # retimed to real audio (44.33s) — was 3.2

        gap_lab = label("the context gap", size=27, color=INK)
        gap_lab.move_to([2.6, -1.7, 0])
        arrow2 = Arrow(halluc.get_bottom(), gap_lab.get_top(), color=INK,
                        stroke_width=2.5, buff=0.12)
        self.play(Create(arrow2), FadeIn(gap_lab), run_time=0.6)
        self.wait(4.4)  # retimed to real audio (44.33s) — was 2.2

        fixes = VGroup(
            label_chip("Tools", ACC),
            label_chip("Retrieval (RAG)", ACC),
        ).arrange(RIGHT, buff=0.5).move_to([2.6, -2.9, 0])
        self.play(FadeIn(fixes), run_time=0.6)
        self.wait(8.7)  # retimed to real audio (44.33s) — was 6.5


# ─────────────────────────────────────────────────────────────────────────────
#  B05_PipelinePerceptionTool   (target ~35s)
#  Stages 1-2 of the four-stage pipeline: the camera trigger, then the GPS
#  coordinate resolved to a street address via a deterministic tool call.
# ─────────────────────────────────────────────────────────────────────────────
class B05_PipelinePerceptionTool(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Look, Then Locate", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(0.8)

        chips, arrows = pipeline_row(active={0, 1})
        row = VGroup(chips, arrows).move_to([0, 2.4, 0])
        self.play(LaggedStart(*[FadeIn(c) for c in chips], lag_ratio=0.15),
                   LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.15),
                   run_time=1.2)
        self.wait(1.6)

        # Perception: a continuous background scan, not a distance-triggered
        # snapshot — no specific trigger interval is documented by the
        # project, so this doesn't claim one (see SOURCES.md).
        scan = DashedLine([-5.6, 0.9, 0], [-1.8, 0.9, 0], color=GHOST, dash_length=0.12)
        scan_lab = label("continuous background scan", size=22, color=SOFT)
        scan_lab.next_to(scan, DOWN, buff=0.3)
        self.play(Create(scan), run_time=0.6)
        self.play(FadeIn(scan_lab), run_time=0.4)
        self.wait(2.4)

        dedupe = label("repeat sightings folded\ninto one report", size=21, color=SOFT,
                       line_spacing=0.85)
        dedupe.next_to(scan_lab, DOWN, buff=0.35)
        self.play(FadeIn(dedupe), run_time=0.4)
        self.wait(5.4)  # retimed to real audio (34.24s) — was 2.8

        confirm = label("frame → vision model →\nclear / probable / uncertain / absent",
                        size=19, color=INK, line_spacing=0.85)
        confirm.next_to(dedupe, DOWN, buff=0.4)
        self.play(FadeIn(confirm), run_time=0.5)
        self.wait(6.2)  # retimed to real audio (34.24s) — was 3.6

        # Tool-use: GPS -> address
        gps = mono("12.9716, 77.5946", size=25, color=SOFT).move_to([2.6, 0.0, 0])
        addr = mono("MG Road, Bengaluru", size=25, color=ACC).move_to([2.6, -1.4, 0])
        osm = label("OpenStreetMap · reverse-geocode", size=21, color=SOFT)
        osm.move_to([2.6, -2.4, 0])
        tool_arrow = Arrow(gps.get_bottom(), addr.get_top(), color=SOFT,
                            stroke_width=2.5, buff=0.15)
        self.play(FadeIn(gps), run_time=0.5)
        self.wait(4.4)  # retimed to real audio (34.24s) — was 1.8
        self.play(Create(tool_arrow), run_time=0.5)
        self.play(FadeIn(addr), FadeIn(osm), run_time=0.6)
        self.wait(8.1)  # retimed to real audio (34.24s) — was 5.5


# ─────────────────────────────────────────────────────────────────────────────
#  B06_PipelineGroundingAction   (target ~35s)
#  Stages 3-4: the database resolves jurisdiction/contractor/tender, then an
#  email draft fills in from that resolution.
# ─────────────────────────────────────────────────────────────────────────────
class B06_PipelineGroundingAction(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Ground It, Then Send It", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(0.8)

        chips, arrows = pipeline_row(active={2, 3})
        row = VGroup(chips, arrows).move_to([0, 2.4, 0])
        self.play(FadeIn(row), run_time=0.6)
        self.wait(1.6)

        db = VGroup(*[
            Rectangle(width=1.6, height=0.28, color=SOFT, stroke_width=2)
            for _ in range(4)
        ]).arrange(DOWN, buff=0.06).move_to([-3.4, 1.0, 0])
        db_lab = label("Karnataka only", size=21, color=SOFT)
        db_lab.next_to(db, DOWN, buff=0.25)
        self.play(FadeIn(db), FadeIn(db_lab), run_time=0.6)
        self.wait(5.6)  # retimed to real audio (43.14s) — was 1.8

        # The real funnel: full procurement snapshot -> indexed pack ->
        # per-point shortlist -> a single probable match (see SOURCES.md).
        funnel = VGroup(
            label("42,283 tenders", size=21, color=SOFT),
            label("13,577 indexed", size=21, color=SOFT),
            label("≤ 25 candidates", size=21, color=SOFT),
            label("1 probable match", size=21, color=ACC),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT).move_to([-3.4, -1.1, 0])
        self.play(LaggedStart(*[FadeIn(f) for f in funnel], lag_ratio=0.25), run_time=1.0)
        self.wait(6.4)  # retimed to real audio (43.14s) — was 2.6

        no_name = label("most: no contractor\nname on file", size=19, color=SOFT,
                        line_spacing=0.8)
        no_name.next_to(funnel, DOWN, buff=0.3)
        self.play(FadeIn(no_name), run_time=0.4)
        self.wait(6.6)  # retimed to real audio (43.14s) — was 2.8

        rows = VGroup(
            label("To: the right recipient", size=21, color=INK),
            label("Subject: road damage —", size=21, color=INK),
            label("probable match, kindly verify", size=20, color=SOFT),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        box = auto_box(rows, h_pad=0.4, v_pad=0.3, color=INK)
        email = VGroup(box, rows).move_to([3.2, -0.3, 0])
        self.play(Create(box), run_time=0.5)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.15), run_time=0.5)
            self.wait(1.3)
        self.wait(5.0)  # retimed to real audio (43.14s) — was 1.2

        never_sent = label("the app never sends it —\nit opens yours, filled in, and stops",
                           size=20, color=ACC, line_spacing=0.85)
        never_sent.next_to(email, DOWN, buff=0.4)
        self.play(FadeIn(never_sent), run_time=0.5)
        self.wait(7.4)  # retimed to real audio (43.14s) — was 3.6


# ─────────────────────────────────────────────────────────────────────────────
#  B07_TheGuardrails   (target ~52s)
#  Three guardrails, each demonstrating its own stopping behaviour: a fork
#  that terminates, a claim that gets hedged, a send control held for review.
#  Narration reframes all three as answers to a general 3-question method.
# ─────────────────────────────────────────────────────────────────────────────
class B07_TheGuardrails(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Guardrails", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.0)

        design_for_failure = serif("Design for failure, not just success.",
                                    size=28, color=SOFT).move_to([0, 2.1, 0])
        self.play(FadeIn(design_for_failure), run_time=0.6)
        self.wait(2.6)
        self.play(FadeOut(design_for_failure), run_time=0.4)

        # 1. Fail-safe routing. Labels are placed under each branch's far
        # ENDPOINT with a fixed offset, not via next_to(fork[i]) — next_to
        # centers under the whole Line's bounding box (its midpoint), which
        # put "national highway" and "local road" only ~1.0 apart and they
        # mashed together in the still-frame QC pass. Widening the branch
        # spread and anchoring off the endpoints fixes it.
        row1_lab = label("Fail-safe routing", size=24, color=INK).move_to([-4.6, 1.1, 0])
        fork = VGroup(
            Line([-4.6, 0.75, 0], [-5.6, -0.05, 0], color=ACC, stroke_width=3),
            Line([-4.6, 0.75, 0], [-3.6, -0.05, 0], color=SOFT, stroke_width=3),
        )
        nh = label("national\nhighway", size=20, color=ACC, line_spacing=0.8)
        nh.move_to([-5.6, -0.75, 0])
        local = label("local road", size=20, color=SOFT).move_to([-3.6, -0.5, 0])
        self.play(FadeIn(row1_lab), run_time=0.4)
        self.play(Create(fork), FadeIn(nh), FadeIn(local), run_time=0.7)
        self.wait(1.8)
        # Real behavior: it doesn't just halt — it hands off to the official
        # highway channel rather than guessing the maintaining authority.
        # Text kept short and narrow ("hands off —\nno guess") — a wider
        # two-line phrase here ran the frame's left edge in still-frame QC.
        term = label("hands off —\nno guess", size=18, color=ACC,
                     line_spacing=0.8).next_to(nh, DOWN, buff=0.25)
        strike1 = strike(nh, color=ACC)
        self.play(Create(strike1), FadeIn(term), run_time=0.5)
        self.wait(3.2)

        # 2. Probabilistic language — the real mechanism: warranty status is
        # inferred only from how old the tender is, never an actual term.
        row2_lab = label("Probabilistic language", size=24, color=INK).move_to([0.6, 1.1, 0])
        claim = label("this IS under warranty", size=20, color=SOFT).move_to([0.6, 0.5, 0])
        hedge = label("possibly within warranty —\nbased on tender age", size=18, color=ACC,
                      line_spacing=0.8).move_to([0.6, -0.3, 0])
        self.play(FadeIn(row2_lab), run_time=0.4)
        self.play(FadeIn(claim), run_time=0.5)
        self.wait(1.6)
        strike2 = strike(claim, color=ACC)
        self.play(Create(strike2), run_time=0.4)
        self.play(FadeIn(hedge), run_time=0.5)
        self.wait(6.6)  # retimed to real audio (54.83s) — was 2.8

        # 3. Human-in-the-loop — the real guarantee is architectural, not
        # just a UI nudge: no complaint-write API exists to call.
        row3_lab = label("Human-in-the-loop", size=24, color=INK).move_to([4.6, 1.1, 0])
        send_txt = label("Send", size=22, color=GHOST)
        send_box = auto_box(send_txt, h_pad=0.4, v_pad=0.22, color=GHOST,
                            fill_color=GHOST, fill_opacity=0.12)
        send = VGroup(send_box, send_txt).move_to([4.6, -0.1, 0])
        hold = label("held for review", size=20, color=SOFT).next_to(send, DOWN, buff=0.25)
        self.play(FadeIn(row3_lab), run_time=0.4)
        self.play(FadeIn(send), FadeIn(hold), run_time=0.6)
        self.wait(6.2)  # retimed to real audio (54.83s) — was 2.4
        # Placed BELOW send, replacing `hold` in the same spot — placing it
        # above (next_to(send, UP)) put it close enough to row3_lab that the
        # two overlapped in the still-frame QC pass.
        press = label("no complaint API,\nno login — it just opens", size=17, color=ACC,
                      line_spacing=0.8).next_to(send, DOWN, buff=0.25)
        self.play(FadeOut(hold), FadeIn(press), run_time=0.5)
        self.play(send_box.animate.set_stroke(ACC, width=3).set_fill(ACC, opacity=0.85),
                  send_txt.animate.set_color(BG), run_time=0.6)
        self.wait(7.4)  # retimed to real audio (54.83s) — was 3.6

        # 4. The general method, named after the three instances
        method = label("same answer, every time: fail closed",
                       size=22, color=SOFT).move_to([0, -2.0, 0])
        self.play(FadeIn(method), run_time=0.5)
        self.wait(6.8)  # retimed to real audio (54.83s) — was 3.0

        land = serif("Autonomy is a liability\nuntil you've defined how it fails.",
                     size=28, color=INK, line_spacing=0.9).move_to(DOWN * 3.4)
        self.play(FadeOut(method), FadeIn(land), run_time=0.6)
        self.wait(9.3)  # retimed to real audio (54.83s) — was 5.5


# ─────────────────────────────────────────────────────────────────────────────
#  B08_TheAntiPattern   (target ~33s)
#  The dedicated falsifiability/stress-test beat — a field of dots, one
#  struck wrong, dramatizes "usually right" as the exact failure mode
#  guardrails exist for.
# ─────────────────────────────────────────────────────────────────────────────
class B08_TheAntiPattern(Scene):

    def construct(self):
        self.camera.background_color = BG

        t = title("Grading Its Own Homework", color=INK)
        self.play(Write(t), run_time=0.6)
        self.wait(1.0)

        tempt = serif("It's tempting to skip the human review —\nthe model is usually right.",
                      size=26, color=SOFT, line_spacing=0.9).move_to([0, 1.9, 0])
        self.play(FadeIn(tempt), run_time=0.6)
        self.wait(2.8)

        # A field of dots, one struck wrong — dramatizes "confidently wrong,
        # once in a hundred" without claiming a real measured error rate.
        dots = VGroup()
        for row in range(6):
            for col in range(16):
                d = Dot(radius=0.06, color=SOFT).move_to(
                    [-5.6 + col * 0.75, 0.4 - row * 0.42, 0])
                dots.add(d)
        bad = dots[47]
        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.01), run_time=1.6)
        self.wait(1.2)
        self.play(bad.animate.set_color(ACC).scale(2.2), run_time=0.5)
        self.wait(1.6)

        callout = label("confidently wrong, once in a hundred", size=22, color=ACC)
        callout.move_to([0, -2.3, 0])
        arrow = Arrow(bad.get_bottom(), callout.get_top(), color=ACC,
                      stroke_width=2, buff=0.15)
        self.play(Create(arrow), FadeIn(callout), run_time=0.6)
        self.wait(2.4)

        dest = label("a real inbox · a real bank account", size=22, color=ACC)
        dest.next_to(callout, DOWN, buff=0.3)
        self.play(FadeIn(dest), run_time=0.5)
        self.wait(2.8)

        self.play(FadeOut(dots), FadeOut(arrow), FadeOut(callout), FadeOut(dest),
                  FadeOut(tempt), run_time=0.6)

        land = serif("If a guardrail only fires when you remember to check it,\n"
                     "it isn't a guardrail — it's a suggestion.",
                     size=25, color=INK, line_spacing=0.9).move_to([0, 0, 0])
        self.play(FadeIn(land), run_time=0.8)
        self.wait(4.75)  # retimed to real audio (22.38s) — was 6.5
