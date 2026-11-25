"""Builds beat_sheet.json for "Backpropagation, One Error at a Time" (film 2 of the series).

On-screen numbers are read from demo/evidence.json (produced by demo/bp_demo.py), never typed.
Re-running this OVERWRITES beat_sheet.json (drops measured audio fields) — rerun audio after.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ev = json.loads((HERE / "demo" / "evidence.json").read_text(encoding="utf-8"))
F, G, S, FD, VA, SAT = ev["forward"], ev["backward"], ev["step"], ev["fd_check"], ev["vanishing"], ev["saturated_w1_5"]

TITLE = "Backpropagation, One Error at a Time"
SLUG = "claude-liam-backpropagation"
TOPIC = "MACHINE LEARNING · BACKPROPAGATION"


def manim(bid, cls, act, content_type, narration, show, visual_intent, motion_claim):
    return {"beat_id": bid, "act": act, "content_type": content_type, "lane": "manim",
            "narration_text": narration,
            "shot": {"type": "GRAPHIC", "source": "own", "motion": "drawon",
                     "manim": {"class": cls, "file": "scenes.py"},
                     "show": show, "visual_intent": visual_intent, "motion_claim": motion_claim}}


def remotion(bid, act, pattern, props, narration, show, motion, **extra):
    b = {"beat_id": bid, "act": act, "lane": "remotion", "narration_text": narration,
         "shot": {"type": "GRAPHIC", "source": "remotion", "motion": motion, "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


beats = []

# ---------------------------------------------------------------- B00 cold open
ask = ("Gradient descent needs a slope for every weight. How does a network get all of them at "
       "once? Show me backpropagation, with real numbers.")
beats.append(remotion("B00", "ASK", "ClaudeComposerAsk", {
    "greeting": "Hola, Liam", "topic": TOPIC, "segment": TITLE, "command": ask,
    "runningText": "running the chain rule backward…",
    "output": ["the trick: the chain rule, run backward from the error",
               f"worked example: one step drops the loss from {S['L_before']} to {S['L_after']}",
               "where it breaks: deep chains where the gradient fades away"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Hola, this is Liam, in for Bear. The ask: gradient descent needs a slope for every weight. "
    "How does a network get all of them at once? Show me backpropagation, with real numbers.",
    [{"at": 0.02, "event": "composer card fades in on cream"},
     {"at": 0.10, "event": "greeting 'Hola, Liam' types above the composer"},
     {"at": 0.30, "event": "the ask types in"},
     {"at": 0.72, "event": "runningText appears"},
     {"at": 0.84, "event": "three result lines cascade in"}],
    "type-on", role_note="COLD OPEN LAW — ask lands answered; Liam introduced in first breath. "
                         "Series link: film 1 (gradient descent) named backprop and moved on."))

# ---------------------------------------------------------------- B01 BLUF
beats.append(remotion("B01", "BLUF", "BrutalistHesitantWriter", {
    "text": "Backpropagation\ntests every weight.",
    "triggerWords": "tests every weight", "replacementWords": "sends the error backward",
    "seed": "claude-liam-backpropagation-b01", "face": "serif", "fontSize": 160,
    "lineSpacing": 3.1, "align": "center", "charMs": 28, "jitter": 18,
    "mistakeRate": 0, "hesitateWithin": 0, "hesitateBetween": 0},
    "Backpropagation sends the error backward once. It doesn't test the weights one by one. It runs "
    "the chain rule from the loss back to the input, and every weight gets its slope.",
    [{"at": 0.0, "event": "cream page holds; caret blinks"},
     {"at": 0.12, "event": "types 'Backpropagation / tests every weight.'"},
     {"at": 0.50, "event": "the wrong phrase turns terracotta, hesitates, backspaces"},
     {"at": 0.65, "event": "types 'sends the error backward'"},
     {"at": 0.90, "event": "final lines settle"}],
    "hesitant-type", lead_silence_s=0.8,
    role_note="EXECUTIVE-SUMMARY LAW — misconception corrected: backprop is not per-weight "
              "trial and error (finite differences); it is one backward pass of the chain rule."))

# ---------------------------------------------------------------- body
beats.append(manim("B02", "B02_Chain", "FRAMEWORK", "structure",
    "Here's the whole network: four small steps in a row. Multiply by the first weight. Squash with "
    "tanh. Multiply by the second weight. Then score it: the loss is how far we land from the target, "
    "squared. Every step is simple, and every step has its own local slope. Backpropagation only ever "
    "needs those.",
    [{"at": 0.05, "event": "node x appears at left"},
     {"at": 0.15, "event": "box '× w₁' → node z draws on"},
     {"at": 0.30, "event": "box 'tanh' → node h draws on"},
     {"at": 0.45, "event": "box '× w₂' → node y draws on"},
     {"at": 0.60, "event": "box '(y − t)²' → node L (loss) draws on"},
     {"at": 0.78, "event": "under each box, a small 'local slope' tag appears, one by one"}],
    "The network as a left-to-right chain of four simple operations, each with a local slope tag.",
    "The chain builds in narration order; the local-slope tags are the framework the film uses."))

beats.append(manim("B03", "B03_ChainRule", "FRAMEWORK", "equation",
    "The chain rule says how a change in the first weight reaches the loss: multiply the local slopes "
    "along the path. How the loss moves with the output. How the output moves with h, which is the "
    "second weight. How tanh bends. And how z moves with the first weight, which is just the input. "
    "Four factors, one product.",
    [{"at": 0.05, "event": "MathTex: ∂L/∂w₁ = ∂L/∂y · ∂y/∂h · ∂h/∂z · ∂z/∂w₁"},
     {"at": 0.30, "event": "box spotlight on ∂L/∂y; label 'how the loss moves with the output'"},
     {"at": 0.45, "event": "box on ∂y/∂h; label 'the second weight, w₂'"},
     {"at": 0.60, "event": "box on ∂h/∂z; label 'how tanh bends: 1 − h²'"},
     {"at": 0.75, "event": "box on ∂z/∂w₁; label 'the input, x'"},
     {"at": 0.90, "event": "all four factors underlined together: 'one product'"}],
    "The chain rule for w₁, factor by factor, each factor tied to a box in the B02 chain.",
    "The spotlight walks the factors right-to-left along the path the error travels."))

beats.append(manim("B04", "B04_Forward", "WORKED_EXAMPLE", "mechanism",
    "Real numbers. Input one, target zero point two, weights zero point five and two. Forward: z is "
    "zero point five. Tanh gives zero point four six. Times two, the output is zero point nine two. "
    "We wanted zero point two, so the loss is about zero point five two. Now run it backward.",
    [{"at": 0.05, "event": "the B02 chain returns; x=1, t=0.2, w₁=0.5, w₂=2 tagged"},
     {"at": 0.25, "event": f"z fills: {F['z']}"},
     {"at": 0.40, "event": f"h fills: {F['h']}"},
     {"at": 0.55, "event": f"y fills: {F['y']}"},
     {"at": 0.75, "event": f"L fills: {F['L']} (terracotta)"}],
    "Forward pass: executed values fill each node left to right (demo/evidence.json).",
    "Each value lands as its node is spoken; the loss is the one accent."))

beats.append(manim("B05", "B05_Backward", "WORKED_EXAMPLE", "mechanism",
    "Backward, the slopes multiply. The loss moves one point four five per unit of output. Times the "
    "second weight: two point nine. Times the tanh slope, zero point seven nine: two point two eight. "
    "That's the first weight's slope. The second weight's is zero point six seven. One step, step size "
    "zero point one, and the loss falls from zero point five two to just under zero point one.",
    [{"at": 0.05, "event": "terracotta arrows run right-to-left under the chain"},
     {"at": 0.15, "event": f"∂L/∂y = {G['dL_dy']} appears at y"},
     {"at": 0.30, "event": f"× w₂ → ∂L/∂h = {G['dL_dh']}"},
     {"at": 0.45, "event": f"× tanh slope {G['dh_dz']} → ∂L/∂z = {G['dL_dz']}"},
     {"at": 0.55, "event": f"× x → ∂L/∂w₁ = {G['dL_dw1']}; ∂L/∂w₂ = {G['dL_dw2']}"},
     {"at": 0.80, "event": f"step: loss counter {S['L_before']} → {S['L_after']}"}],
    "Backward pass: executed gradients flow right to left, then one update step.",
    "The multiplication is visible as the error travels; the loss counter drops on the spoken number."))

beats.append(manim("B06", "B06_Check", "MECHANISM", "data",
    "Is that slope real? Check it the slow way: nudge the first weight up and down by a "
    "hundred-thousandth, and measure how the loss changes. Backprop says two point two seven eight "
    "three. The nudge says the same, to eight decimal places. But nudging costs two passes per weight. "
    "With a million weights, that's two million passes. Backprop needs one.",
    [{"at": 0.05, "event": "w₁ dial nudges ± 0.00001; two loss readings appear"},
     {"at": 0.35, "event": f"side by side: backprop {FD['w1']['backprop']} | nudge {FD['w1']['finite_diff']}"},
     {"at": 0.55, "event": f"difference chip: {FD['w1']['abs_diff']}"},
     {"at": 0.75, "event": "cost bars: '2 passes per weight × 1,000,000' vs 'one backward pass'"}],
    "Finite-difference check against backprop, then the cost comparison that makes backprop matter.",
    "The two numbers sit side by side, digit-aligned; the cost bars grow on the spoken counts."))

beats.append(manim("B07", "B07_Vanishing", "FALSIFIABILITY", "data",
    "Here's where it bites. Stack ten sigmoid layers. A sigmoid's slope is never more than a quarter, "
    "so every layer multiplies the gradient by about zero point two two. By the time the error reaches "
    "the first layer, it's about three and a half ten-millionths. The early layers barely learn. "
    "That's the vanishing gradient, and it's one reason deep networks moved to ReLU.",
    [{"at": 0.05, "event": "ten sigmoid layers stack left to right"},
     {"at": 0.25, "event": "chip: 'sigmoid slope ≤ 0.25'"},
     {"at": 0.40, "event": "gradient bars shrink layer by layer, right to left (log scale)"},
     {"at": 0.70, "event": f"first-layer bar labelled {VA['grad_at_input']} (terracotta)"}],
    "A deep sigmoid chain where the executed gradient shrinks by ~0.22 per layer.",
    "The bars visibly collapse as the error moves back; the tiny first-layer number is the accent."))

# ---------------------------------------------------------------- closing block
lines = ["Backprop runs the chain rule from the loss back to every weight.",
         "Each step only needs its own local slope.",
         "Slopes multiply along the path back to each weight.",
         "One backward pass gives every weight its slope.",
         "A finite-difference check agrees, at far higher cost.",
         "Long chains of small slopes make gradients vanish."]
beats.append(remotion("BVDT", "VERDICT", "ClaudeVerdictArtifact", {
    "artifactTitle": "Verdict", "artifactHeading": "Backpropagation, in six lines",
    "artifactLines": lines},
    "Let's recap with Claude. Backprop runs the chain rule from the loss back to every weight. Each "
    "step only needs its own local slope, and slopes multiply along the path. One backward pass gives "
    "every weight its slope. A finite-difference check agrees, at far higher cost. And long chains of "
    "small slopes make gradients vanish.",
    [{"at": 0.05, "event": "verdict artifact card in on cream"},
     {"at": 0.15, "event": "heading types"},
     {"at": 0.25, "event": "lines 1–6 land on their spoken cue"}],
    "artifact-in", lead_silence_s=0.5))

prompt = ("Write a short Python script, no ML libraries, for y = w2 * tanh(w1 * x) with loss (y - t)^2, "
          "using x = 1, t = 0.2, w1 = 0.5, w2 = 2. Compute dL/dw1 and dL/dw2 with the chain rule, then "
          "check both with central finite differences using a step of 0.00001. Print each pair and their "
          "difference. Then set w1 = 5 and explain, from the numbers, which factor in the chain shrinks dL/dw1.")
beats.append(remotion("BHTF", "YOUR_TURN", "ClaudeComposerAsk", {
    "greeting": "Your turn.", "topic": "YOUR TURN · BACKPROPAGATION",
    "segment": "Check backprop by hand", "command": prompt,
    "runningText": "paste this into Claude…",
    "output": [f"check: dL/dw1 ≈ {round(G['dL_dw1'], 4)} and matches the finite difference",
               f"check: at w1 = 5 the tanh slope is about {SAT['tanh_slope']}",
               "check: it names 1 − tanh² as the factor that shrinks the gradient"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Your turn. Paste this into Claude: Write a short Python script, no M L libraries, for y equals w "
    "two times tanh of w one times x, with loss y minus t, squared. Use x equals one, t equals zero point "
    "two, w one equals zero point five, w two equals two. Compute the slope of the loss for both weights "
    "with the chain rule, then check both with central finite differences, using a step of one "
    "hundred-thousandth. Print each pair and their difference. Then set w one to five, and explain, from "
    "the numbers, which factor in the chain shrinks the first weight's slope. Here's what to check. The "
    "first weight's slope should be about two point two eight, and match the finite difference. At w one "
    "equals five, watch the tanh slope collapse to almost nothing. And see whether Claude names the "
    "culprit: one minus tanh squared.",
    [{"at": 0.02, "event": "composer card in on cream"},
     {"at": 0.08, "event": "greeting 'Your turn.' types"},
     {"at": 0.15, "event": "the prompt types into the composer"},
     {"at": 0.62, "event": "runningText 'paste this into Claude…'"},
     {"at": 0.72, "event": "three check lines cascade in as each is spoken"}],
    "type-on", role_note="HANDOFF LAW — prompt read aloud (spoken form), then a 3-point rubric."))

beats.append(remotion("BOUT", "OUTRO", "ClaudeTitleOutro", {"title": TITLE + ".", "handle": "@NikBearBrown", "slug": SLUG},
    f"{TITLE}. At Nik Bear Brown.",
    [{"at": 0.02, "event": "cream page; polarity seeded from slug"},
     {"at": 0.10, "event": "title types"}, {"at": 0.55, "event": "handle @NikBearBrown"},
     {"at": 0.70, "event": "slug-seeded mascot animates under the handle"}],
    "outro-card", kind="outro_voice", tail_silence_s=1.0,
    role_note="OUTRO-LOCK — exact title restate, hardcoded handle, spoken, no music."))

sheet = {"metadata": {
    "title": TITLE, "slug": SLUG, "topic": TOPIC, "skill": "ai-explainer",
    "brand": "claude-liam", "channel": "claude-liam", "audience": "makers and curious learners new to ML",
    "register": "Teardown", "engine": "kokoro", "voice": "am_onyx", "voice_kokoro": "am_onyx",
    "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5", "aspect_ratio": "16:9",
    "greeting": "Hola, Liam", "persona": "Liam (in for Bear)", "in_for_bear": True,
    "folderLabel": "@NikBearBrown", "captions": False, "series": "STEM films", "series_order": 2,
    "evidence": "demo/bp_demo.py -> demo/evidence.json, demo/RUN-LOG.txt",
    "pronounce": {"tanh": "tˈæntʃ", "backpropagation": "bˌækpɹˌɑːpəɡˈeɪʃən", "Backpropagation": "bˌækpɹˌɑːpəɡˈeɪʃən"},
    "tags": ["backpropagation", "chain rule", "machine learning", "neural networks",
             "gradient", "vanishing gradient"]},
    "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")

for b in beats:
    n = len(b["narration_text"].split())
    print(f"{b['beat_id']:5} {b.get('act',''):15} {n:4} words  ~{n/3.5:5.1f}s")
total = sum(len(b["narration_text"].split()) for b in beats)
print(f"total {total} words  ~{total/3.5/60:.1f} min (3.5 w/s, film-1 Kokoro rate)")
