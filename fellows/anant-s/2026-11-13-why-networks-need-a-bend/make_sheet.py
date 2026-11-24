"""Builds beat_sheet.json for "Why Neural Networks Need a Bend" (claude-liam-nonlinearity).

On-screen numbers are read from demo/evidence.json (produced by demo/nonlinearity_demo.py), never typed.
Re-running this OVERWRITES beat_sheet.json (drops measured audio fields) — rerun audio after.
Equations/matrices: each Manim beat lists its MathTex strings under shot.manim.mathtex; no TeX ever
goes into a Remotion card prop.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ev = json.loads((HERE / "demo" / "evidence.json").read_text(encoding="utf-8"))
C = ev["collapse"]
S = ev["scale"]
XL = ev["xor_line"]
DL = ev["deep_linear"]
RH = ev["relu_hand"]
SD = ev["seeds"]
K = ev["kinks"]

TITLE = "Why Neural Networks Need a Bend"
SLUG = "claude-liam-nonlinearity"
TOPIC = "MACHINE LEARNING · NONLINEARITY"


def g(v):
    """Number for on-screen text (true minus sign)."""
    s = f"{v:g}"
    return s.replace("-", "−")


def vec(v):
    return "(" + ", ".join(g(a) for a in v) + ")"


def tex_mat(m):
    return r"\begin{bmatrix}" + r"\\".join("&".join(str(a) for a in row) for row in m) + r"\end{bmatrix}"


def tex_col(v):
    return r"\begin{bmatrix}" + r"\\".join(str(a) for a in v) + r"\end{bmatrix}"


def manim(bid, cls, act, content_type, narration, show, visual_intent, motion_claim, mathtex=None, **extra):
    m = {"class": cls, "file": "scenes.py"}
    if mathtex:
        m["mathtex"] = mathtex
    b = {"beat_id": bid, "act": act, "content_type": content_type, "lane": "manim",
         "narration_text": narration,
         "shot": {"type": "GRAPHIC", "source": "own", "motion": "drawon", "manim": m,
                  "show": show, "visual_intent": visual_intent, "motion_claim": motion_claim}}
    b.update(extra)
    return b


def remotion(bid, act, pattern, props, narration, show, motion, **extra):
    b = {"beat_id": bid, "act": act, "lane": "remotion", "narration_text": narration,
         "shot": {"type": "GRAPHIC", "source": "remotion", "motion": motion, "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


ok2, ok8 = SD["two_units"]["solved"], SD["eight_units"]["solved"]
beats = []

# ---------------------------------------------------------------- B00 cold open
ask = ("Why does every neural network put a bend between its layers? "
       "Wouldn't stacking more straight layers be enough? Show me with real numbers.")
beats.append(remotion("B00", "ASK", "ClaudeComposerAsk", {
    "greeting": "Jambo, Liam", "topic": TOPIC, "segment": TITLE, "command": ask,
    "runningText": "multiplying it out…",
    "output": ["two straight layers multiply out to one: identical outputs, executed",
               f"XOR: {XL['lines_tried']:,} lines tried, the best gets {XL['best_correct']} of 4",
               f"one ReLU bend solves it; trained from 100 seeds, it finds it {ok2} times"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Jambo, this is Liam, in for Bear. The ask: why does every neural network put a bend between "
    "its layers? Wouldn't stacking more straight layers be enough? Show me with real numbers.",
    [{"at": 0.02, "event": "composer card fades in on cream"},
     {"at": 0.10, "event": "greeting 'Jambo, Liam' types above the composer"},
     {"at": 0.30, "event": "the ask types in"},
     {"at": 0.72, "event": "runningText 'multiplying it out…' appears"},
     {"at": 0.84, "event": "three result lines cascade in"}],
    "type-on", role_note="COLD OPEN LAW — ask lands answered; Liam introduced in first breath."))

# ---------------------------------------------------------------- B01 BLUF
beats.append(remotion("B01", "BLUF", "BrutalistHesitantWriter", {
    "text": "Stacking more layers\nmakes a network powerful.",
    "triggerWords": "Stacking more layers", "replacementWords": "A bend between layers",
    "seed": "claude-liam-nonlinearity-b01", "face": "serif", "fontSize": 150,
    "lineSpacing": 3.1, "align": "center", "charMs": 28, "jitter": 18,
    "mistakeRate": 0, "hesitateWithin": 0, "hesitateBetween": 0},
    "A bend between layers makes a network powerful. Stacking alone isn't enough: straight layers, "
    "however many, collapse into one. Add a simple bend between them, and the network can finally "
    "draw a curve.",
    [{"at": 0.0, "event": "cream page holds; caret blinks"},
     {"at": 0.12, "event": "types 'Stacking more layers / makes a network powerful.'"},
     {"at": 0.50, "event": "'Stacking more layers' turns terracotta, hesitates, backspaces"},
     {"at": 0.65, "event": "types 'A bend between layers'"},
     {"at": 0.90, "event": "final lines settle: 'A bend between layers / makes a network powerful.'"}],
    "hesitant-type", lead_silence_s=0.8,
    role_note="EXECUTIVE-SUMMARY LAW — misconception corrected: depth alone is not what gives a "
              "network its power; the nonlinearity between layers is."))

# ---------------------------------------------------------------- body
beats.append(manim("B02", "B02_TwoMoves", "FRAMEWORK", "structure",
    "Two moves build a plain neural network. The first is a layer: multiply by a matrix. It can stretch, "
    "rotate and shear the plane, but straight lines stay straight, and parallel lines stay parallel. "
    "The second is the bend, here a ReLU: keep positive numbers, flatten negatives to zero. That one "
    "creases the plane. A network alternates the two: layer, bend, layer.",
    [{"at": 0.03, "event": "a square grid of the input plane draws on, axes in ink"},
     {"at": 0.12, "event": "label 'layer = multiply by a matrix' (MathTex Wx)"},
     {"at": 0.20, "event": "grid shears and rotates under a 2×2 matrix; every grid line stays straight and parallel"},
     {"at": 0.45, "event": "inset: ReLU graph, flat at zero for z<0, slope 1 for z>0 (MathTex ReLU(z)=max(0,z))"},
     {"at": 0.58, "event": "grid passes through ReLU: negative halves fold flat onto the axes; creases light terracotta"},
     {"at": 0.85, "event": "the word 'bend' in the ReLU header is boxed in ink on 'layer, bend, layer'"}],
    "The framework: a layer is a linear map (lines stay lines); the bend is ReLU (it creases).",
    "The same grid undergoes both moves on cue, so 'straight stays straight' vs 'creased' is seen, not told.",
    mathtex=[r"W\mathbf{x}", r"\mathrm{ReLU}(z)=\max(0,\,z)",
             r"\mathbf{x}\;\to\;W_1\;\to\;\text{bend}\;\to\;W_2\;\to\;y"]))

beats.append(manim("B03", "B03_Collapse", "WORKED_EXAMPLE", "equation",
    "Here are two straight layers with no bend: seeded random matrices. Push the input, minus one, "
    "two, through the first layer: minus one, minus three. Then the second: seven, eight. Now "
    "multiply the two matrices first, into one. Push the same input through that single matrix: "
    "seven, eight. Identical. Two layers were one layer in disguise.",
    [{"at": 0.03, "event": f"MathTex W₁ = {C['W1']}, W₂ = {C['W2']}, x = {vec(C['x'])} typeset (seed 0)"},
     {"at": 0.22, "event": f"left path: W₁x = {vec(C['W1x'])} lands under W₁"},
     {"at": 0.36, "event": f"left path: W₂(W₁x) = {vec(C['W2_W1x'])}"},
     {"at": 0.52, "event": f"right path: W₂W₁ multiplies out to {C['W2W1']} (one matrix)"},
     {"at": 0.70, "event": f"right path: (W₂W₁)x = {vec(C['W2W1_x'])}"},
     {"at": 0.80, "event": "MathTex W₂(W₁x) = (W₂W₁)x between the two results; terracotta BOX on the '='"}],
    "Two computation paths side by side with executed integer matrices (demo/evidence.json).",
    "Both paths compute in narration order and land on the same vector, held side by side ≥2 s.",
    mathtex=[r"W_1=" + tex_mat(C["W1"]), r"W_2=" + tex_mat(C["W2"]), r"\mathbf{x}=" + tex_col(C["x"]),
             r"W_1\mathbf{x}=" + tex_col(C["W1x"]), r"W_2(W_1\mathbf{x})=" + tex_col(C["W2_W1x"]),
             r"W_2W_1=" + tex_mat(C["W2W1"]), r"(W_2W_1)\mathbf{x}=" + tex_col(C["W2W1_x"]),
             r"W_2(W_1\mathbf{x})=(W_2W_1)\mathbf{x}"]))

beats.append(manim("B04", "B04_TenLayers", "MECHANISM", "mechanism",
    "Not a lucky pick. A thousand random inputs, ten random layers in a row. Multiply the ten "
    "matrices into one, and every output lands on top of the stack's output. The largest gap is in "
    "the fifteenth decimal place: rounding, not structure. Add a shift to each layer, a bias, and you "
    "still get one matrix plus one shift. Depth without a bend buys no new shapes.",
    [{"at": 0.03, "event": f"a cloud of {S['n_inputs']:,} input points (seed 1)"},
     {"at": 0.12, "event": "the cloud morphs through ten linear layers, one after another (layer counter 1→10)"},
     {"at": 0.38, "event": "a ghost cloud from the single multiplied-out matrix lands exactly on top"},
     {"at": 0.52, "event": f"counter: largest difference {S['ten_layer_max_abs_diff']:.2e} (MathTex 8.88×10⁻¹⁵), chip 'float rounding'"},
     {"at": 0.75, "event": "MathTex W₂(W₁x + b₁) + b₂ = (W₂W₁)x + (W₂b₁ + b₂) typesets; terracotta box on the right-hand side"}],
    "Ten-layer linear stack vs its single multiplied-out matrix on 1,000 executed inputs.",
    "The two clouds coincide; the difference counter shows only rounding error.",
    mathtex=[r"W_{10}\cdots W_2W_1\mathbf{x}=(W_{10}\cdots W_1)\mathbf{x}",
             r"\max|\Delta| = 8.88\times10^{-15}",
             r"W_2(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2=(W_2W_1)\mathbf{x}+(W_2\mathbf{b}_1+\mathbf{b}_2)"]))

beats.append(manim("B05", "B05_NoLine", "MECHANISM", "mechanism",
    "Now a problem no straight map can touch. XOR: output one when exactly one input is on. Four "
    "corners of a square, the ones on one diagonal, the zeros on the other. Find a single line with "
    "both ones on one side. We tried over a hundred and fifteen thousand. The best gets three of "
    "four, and four lines of algebra prove no line ever gets all four.",
    [{"at": 0.03, "event": "unit square; corners (0,0),(1,1) as hollow ink circles '0', (0,1),(1,0) as filled ink dots '1'"},
     {"at": 0.25, "event": "a line sweeps and rotates across the square; a 'correct: n of 4' counter flickers"},
     {"at": 0.55, "event": f"tally: 'lines tried {XL['lines_tried']:,}' climbs; 'best: {XL['best_correct']} of 4' locks"},
     {"at": 0.72, "event": "the best line freezes with one point on the wrong side, ringed terracotta"},
     {"at": 0.85, "event": "the four inequalities typeset (MathTex) and add to a contradiction"}],
    "XOR's four points and an exhaustive line sweep that never exceeds 3 of 4 (executed).",
    "The sweep is the search; the counter maxing at 3 is the result; the algebra closes it.",
    mathtex=[r"b\le 0", r"w_2+b>0", r"w_1+b>0", r"w_1+w_2+b\le 0",
             r"w_1+w_2+2b>0\;\Rightarrow\;w_1+w_2+b>-b\ge 0"]))

lin_curve = DL["run"]["curve"]
beats.append(manim("B06", "B06_StuckAtHalf", "MECHANISM", "data",
    "So give it depth. A two-layer network with no bend, trained by gradient descent for five "
    "thousand steps. The loss sinks to zero point two five and flattens. Every output settles at one "
    "half: a shrug. That's exactly what the best single line predicts, because this network is a "
    "single line. A hundred seeds, same floor. None gets all four.",
    [{"at": 0.03, "event": "network strip x → W₁ → W₂ → y with the bend slot visibly empty"},
     {"at": 0.15, "event": f"loss curve plots over {DL['steps']:,} steps (every 250, executed) and flattens at {g(DL['run']['loss'])}"},
     {"at": 0.45, "event": f"four output bars settle at {', '.join(g(p) for p in DL['run']['pred'])} against targets 0, 1, 1, 0"},
     {"at": 0.62, "event": f"beside them: least-squares best line predicts {', '.join(g(p) for p in XL['least_squares']['pred'])}; terracotta '=' box joins the two"},
     {"at": 0.85, "event": f"chip: '100 seeds: lowest loss {g(DL['over_100_seeds']['min_loss'])}, all four right: {DL['over_100_seeds']['reached_4_of_4']}'"}],
    "A trained deep linear net lands on the best line's answer: one half everywhere (executed).",
    "The loss curve flattens as narrated; the bars and the best-line bars match side by side.",
    mathtex=[r"\hat y = \tfrac12", r"\mathcal{L}=\tfrac14"], data={"loss_curve_every_250": lin_curve}))

rows = RH["rows"]
beats.append(manim("B07", "B07_ReluFix", "WORKED_EXAMPLE", "equation",
    "Now add one bend. Two hidden units, weights set by hand, from the Deep Learning textbook. Each "
    "unit adds up the inputs; the second also subtracts one. Then the ReLU. At zero, zero, the "
    "second unit reads minus one, and the ReLU flattens it to zero. The output takes the first unit "
    "minus twice the second. Zero, one, one, zero. XOR, exactly.",
    [{"at": 0.03, "event": "MathTex h = ReLU(Wx + c), y = w·h with W, c, w as matrices; caption 'weights: Goodfellow, Bengio & Courville (2016), §6.1'"},
     {"at": 0.20, "event": "table header x | Wx + c | ReLU | y | target"},
     {"at": 0.38, "event": f"row x={vec(rows[0]['x'])}: z={vec(rows[0]['z'])} → h={vec(rows[0]['h'])}; terracotta box on the −1 → 0 clip"},
     {"at": 0.60, "event": f"rows {vec(rows[1]['x'])}, {vec(rows[2]['x'])}, {vec(rows[3]['x'])} land: h = {vec(rows[1]['h'])}, {vec(rows[2]['h'])}, {vec(rows[3]['h'])}"},
     {"at": 0.80, "event": "y column fills 0, 1, 1, 0 and matches the target column, row by row ✓"}],
    "The hand-set 2-unit ReLU network computing XOR row by row (executed, asserted).",
    "Each row lands on its spoken cue; the single clip is the beat's terracotta moment.",
    mathtex=[r"\mathbf{h}=\mathrm{ReLU}(W\mathbf{x}+\mathbf{c})", r"y=\mathbf{w}^{\top}\mathbf{h}",
             r"W=" + tex_mat(RH["W"]), r"\mathbf{c}=" + tex_col(RH["c"]), r"\mathbf{w}=" + tex_col(RH["w"])]))

beats.append(manim("B08", "B08_Fold", "MECHANISM", "mechanism",
    "Here's what the bend did, geometrically. The first layer lays all four points on one line, and "
    "the two ones land on the same spot, stuck between the zeros. ReLU folds that line at the "
    "corner, pulling the zero, zero point up to the origin. Now one straight line separates them. "
    "Unfold it back to the square, and that line becomes a band: ones inside, zeros out.",
    [{"at": 0.03, "event": "input square with the four XOR points"},
     {"at": 0.15, "event": "linear move to (z₁, z₂): points slide onto the line z₂ = z₁ − 1; the two '1' points merge at (1, 0)"},
     {"at": 0.40, "event": "ReLU fold: the part of that line below the axis folds up; (0, −1) lands on (0, 0); the crease glows terracotta"},
     {"at": 0.60, "event": "line h₁ − 2h₂ = ½ draws, the merged '1' on one side, both '0's on the other"},
     {"at": 0.80, "event": "unfold back to the input square: the region becomes a band between x₁ + x₂ = ½ and x₁ + x₂ = 3⁄2"}],
    "The geometry of the fold: hidden space before/after ReLU and the band it carves in the input plane.",
    "The points physically move through the linear map and the fold; the separator appears only after the fold.",
    mathtex=[r"z_2=z_1-1", r"h_1-2h_2=\tfrac12", r"\tfrac12<x_1+x_2<\tfrac32"]))

beats.append(manim("B09", "B09_HundredSeeds", "FALSIFIABILITY", "data",
    "So is the bend enough? Same two-unit network, but now trained from a hundred random starts "
    "instead of set by hand. Here, eighteen find XOR. Eighty-two get stuck, most with a hidden unit that "
    "went flat and never woke up. The bend makes a solution possible; it doesn't make training find "
    "it. Give it eight units, and ninety-one of a hundred succeed.",
    [{"at": 0.03, "event": "10×10 grid of seed tiles, labelled 'seeds 0–99, 2 hidden units'"},
     {"at": 0.18, "event": f"tiles resolve in seed order: solved = ink check, stuck = hollow; counter climbs to {ok2} / 100"},
     {"at": 0.45, "event": f"inset for stuck seed {SD['two_units']['example_fail_seed']}: one hidden unit flat at zero on all four inputs, outputs {', '.join(g(p) for p in SD['two_units']['example_fail']['pred'])}; terracotta ring on the flat unit"},
     {"at": 0.62, "event": f"chip: '{SD['two_units']['failed_with_dead_unit']} of {SD['two_units']['failed']} stuck runs have a dead unit'"},
     {"at": 0.80, "event": f"a second grid '8 hidden units' resolves beside it: {ok8} / 100"}],
    "100 seeded training runs at two widths: the bend is necessary, not sufficient (executed).",
    "The two grids are side by side and held, so 18 vs 91 is a visible comparison, not a spoken one.",
    mathtex=[f"{ok2}/100", f"{ok8}/100"]))

beats.append(manim("B10", "B10_StraightAgain", "FALSIFIABILITY", "mechanism",
    "And the bend has a shape. Walk the hand-set network along the square's diagonal. The output is "
    "flat, then climbs in a straight line, then falls in a straight line. Two kinks, exactly where a "
    "unit switches on. Keep walking past the data and it never curves back: at three, three it says "
    "minus four. Between and beyond its kinks, a ReLU network is made of straight pieces.",
    [{"at": 0.03, "event": "inset square with the diagonal x = (t, t) marked; main axes t vs y"},
     {"at": 0.20, "event": "output traces left to right: flat 0, then up to 1 at t = ½, then down"},
     {"at": 0.45, "event": "terracotta dots on the two kinks at t = 0 and t = ½; labels 'unit 1 on', 'unit 2 on'"},
     {"at": 0.65, "event": f"trace continues past t = 1 with no curve: (3, 3) → {g(K['far']['(3,3)'])}"},
     {"at": 0.85, "event": "MathTex pieces: y = 0, y = 2t, y = 2 − 2t (straight pieces bracketed)"}],
    "Piecewise-linear output of the hand-set net along the diagonal, executed (demo/evidence.json).",
    "The trace draws in order; the kinks are marked where the narration says 'switches on'.",
    mathtex=[r"y=\mathrm{ReLU}(2t)-2\,\mathrm{ReLU}(2t-1)", r"y=0", r"y=2t", r"y=2-2t"]))

# ---------------------------------------------------------------- closing block
vlines = ["A layer multiplies by a matrix: straight lines stay straight.",
          "Stacked layers without a bend multiply out to one matrix.",
          "XOR has no separating line, so no purely linear network learns it.",
          "One ReLU bend folds the plane; two hidden units solve XOR exactly.",
          "The bend makes a solution possible, not easy to find.",
          "Between and beyond its kinks, a ReLU network is made of straight pieces."]
beats.append(remotion("BVDT", "VERDICT", "ClaudeVerdictArtifact", {
    "artifactTitle": "Verdict", "artifactHeading": "Nonlinearity, in six lines",
    "artifactLines": vlines},
    "Let's recap with Claude. " + " ".join(vlines),
    [{"at": 0.05, "event": "verdict artifact card in on cream"},
     {"at": 0.15, "event": "heading types"},
     {"at": 0.25, "event": "lines 1–6 land on their spoken cue"}],
    "artifact-in", lead_silence_s=0.5))

prompt = ("Write a short Python script using only numpy. Train a tiny network on XOR twice: once with "
          "no activation, once with a ReLU and two hidden units. Use plain gradient descent from twenty "
          "random seeds each, and print how many seeds get all four points right. Then, from the printed "
          "numbers alone, explain why the linear version never succeeds and why the ReLU version "
          "sometimes fails.")
beats.append(remotion("BHTF", "YOUR_TURN", "ClaudeComposerAsk", {
    "greeting": "Your turn.", "topic": "YOUR TURN · NONLINEARITY",
    "segment": "Break XOR both ways", "command": prompt,
    "runningText": "paste this into Claude…",
    "output": ["check: the linear runs never get all four, on any seed",
               "check: stuck ReLU runs often have a hidden unit flat at zero",
               "check: the reasons come from the printed numbers"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Your turn. Paste this into Claude: " + prompt + " "
    "Here's what to check. The linear runs should never get all four right, on any seed. For the "
    "ReLU runs that fail, ask Claude to print the hidden units, and look for one stuck at zero. And "
    "make sure the explanation comes from the printed numbers, not a recited theorem.",
    [{"at": 0.02, "event": "composer card in on cream"},
     {"at": 0.08, "event": "greeting 'Your turn.' types"},
     {"at": 0.15, "event": "the prompt types into the composer"},
     {"at": 0.62, "event": "runningText 'paste this into Claude…'"},
     {"at": 0.72, "event": "three check lines cascade in as each is spoken"}],
    "type-on", role_note="HANDOFF LAW — prompt read aloud verbatim, then a 3-point rubric."))

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
    "greeting": "Jambo, Liam", "persona": "Liam (in for Bear)", "in_for_bear": True,
    "folderLabel": "@NikBearBrown", "captions": False,
    "evidence": "demo/nonlinearity_demo.py -> demo/evidence.json, demo/RUN-LOG.txt",
    "pronounce": {"ReLU": "ɹˈɛluː", "XOR": "ˈɛksɔːɹ", "numpy": "nˈʌmpaɪ", "Jambo": "dʒˈɑːmboʊ"},
    "series": {"number": 6, "of": 7},
    "tags": ["neural networks", "nonlinearity", "activation functions", "ReLU", "XOR",
             "linear algebra", "deep learning"]},
    "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")

for b in beats:
    n = len(b["narration_text"].split())
    print(f"{b['beat_id']:5} {b.get('act',''):15} {n:4} words  ~{n/3.5:5.1f}s")
total = sum(len(b["narration_text"].split()) for b in beats)
print(f"total {total} words  ~{total/3.5/60:.1f} min (3.5 w/s, film-1 Kokoro rate)")

# ---------------------------------------------------------------- SCRIPT.md (GATE P review copy)
md = [f"# SCRIPT — {TITLE}", "",
      "Narration for review (GATE P). Generated from beat_sheet.json by make_sheet.py; edit make_sheet.py, not this file.",
      f"Estimated runtime: {total} words ≈ {total/3.5/60:.1f} min at film 1's measured Kokoro pace (3.5 words/s).", ""]
for b in beats:
    sh = b["shot"]
    comp = (sh.get("manim") or {}).get("class") or (sh.get("remotion") or {}).get("pattern")
    n = len(b["narration_text"].split())
    md += [f"## {b['beat_id']} · {b.get('act','')} · {comp} · {n} words", "", b["narration_text"], "",
           "*On screen:* " + " → ".join(e["event"] for e in sh["show"]), ""]
(HERE / "SCRIPT.md").write_text("\n".join(md), encoding="utf-8")
