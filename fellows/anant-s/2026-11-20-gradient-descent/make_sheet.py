"""Builds beat_sheet.json for "Gradient Descent, One Step at a Time".

On-screen numbers are read from demo/evidence.json (produced by demo/gd_demo.py), never typed.
Re-running this OVERWRITES beat_sheet.json (drops measured audio fields) — rerun audio after.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ev = json.loads((HERE / "demo" / "evidence.json").read_text(encoding="utf-8"))
W = ev["worked"]["steps"]
SW = ev["sweep"]
NC = ev["nonconvex"]
SC = ev["scale"]

TITLE = "Gradient Descent, One Step at a Time"
SLUG = "claude-liam-gradient-descent"
TOPIC = "MACHINE LEARNING · GRADIENT DESCENT"


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
ask = ("How does a neural network actually learn? Skip the hype. "
       "Show me the one rule underneath, with real numbers.")
beats.append(remotion("B00", "ASK", "ClaudeComposerAsk", {
    "greeting": "Ciao, Liam", "topic": TOPIC, "segment": TITLE, "command": ask,
    "runningText": "working through the math…",
    "output": ["the rule: measure the slope of the error, step the other way",
               f"worked example: from {W[0]['theta']:g} to {W[5]['theta']:g} in five steps",
               "where it breaks: the step size, and valleys that aren't the lowest"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Ciao, this is Liam, in for Bear. The ask: how does a neural network actually learn? "
    "Skip the hype. Show me the one rule underneath, with real numbers.",
    [{"at": 0.02, "event": "composer card fades in on cream"},
     {"at": 0.10, "event": "greeting 'Ciao, Liam' types above the composer"},
     {"at": 0.30, "event": "the ask types in"},
     {"at": 0.72, "event": "runningText 'working through the math…' appears"},
     {"at": 0.84, "event": "three result lines cascade in"}],
    "type-on", role_note="COLD OPEN LAW — ask lands answered; Liam introduced in first breath."))

# ---------------------------------------------------------------- B01 BLUF
beats.append(remotion("B01", "BLUF", "BrutalistHesitantWriter", {
    "text": "Training a model\nfinds the best answer.",
    "triggerWords": "finds the best answer", "replacementWords": "keeps stepping downhill",
    "seed": "claude-liam-gradient-descent-b01", "face": "serif", "fontSize": 160,
    "lineSpacing": 3.1, "align": "center", "charMs": 28, "jitter": 18,
    "mistakeRate": 0, "hesitateWithin": 0, "hesitateBetween": 0},
    "Training a model keeps stepping downhill. It never searches for the best answer. "
    "It measures which way the error rises, takes a small step the other way, and repeats, "
    "step after step.",
    [{"at": 0.0, "event": "cream page holds; caret blinks"},
     {"at": 0.12, "event": "types 'Training a model / finds the best answer.'"},
     {"at": 0.50, "event": "'finds the best answer' turns terracotta, hesitates, backspaces"},
     {"at": 0.65, "event": "types 'keeps stepping downhill'"},
     {"at": 0.90, "event": "final lines settle: 'Training a model / keeps stepping downhill.'"}],
    "hesitant-type", lead_silence_s=0.8,
    role_note="EXECUTIVE-SUMMARY LAW — misconception corrected: training is not a search for "
              "the best answer; it is repeated local steps downhill."))

# ---------------------------------------------------------------- body
beats.append(manim("B02", "B02_Landscape", "FRAMEWORK", "structure",
    "Here is the whole picture. Across the bottom, one setting of the model. Call it theta. "
    "Up the side, the loss: how wrong the model is at that setting. The model sits somewhere "
    "on this curve, and it can't see the bottom. All it can measure is the slope right where "
    "it stands. The slope points uphill. So step the other way.",
    [{"at": 0.05, "event": "axes draw on; x labelled 'setting θ', y labelled 'loss'"},
     {"at": 0.25, "event": "the bowl L(θ)=θ² draws on"},
     {"at": 0.45, "event": "a terracotta ball lands at θ=3"},
     {"at": 0.62, "event": "tangent line draws through the ball: 'slope'"},
     {"at": 0.80, "event": "arrow points uphill, then a second arrow flips to point downhill: 'step'"}],
    "The loss curve as a landscape; the model only sees the local slope.",
    "The tangent at the ball IS the gradient; the downhill arrow is the step."))

beats.append(manim("B03", "B03_UpdateRule", "FRAMEWORK", "equation",
    "Written down, it's one line. The new setting becomes the old setting, minus a step. "
    "The step is two things multiplied: the slope of the loss right here, called the gradient, "
    "and eta, the step size, a number you choose. Steep slope, big step. Flat ground, tiny step. "
    "That minus sign is the whole idea: go against the slope.",
    [{"at": 0.05, "event": "update rule typesets: θ_{t+1} = θ_t − η ∇L(θ_t)"},
     {"at": 0.20, "event": "spotlight on θ_{t+1}; label below: 'new setting'"},
     {"at": 0.32, "event": "spotlight on θ_t; label: 'current setting'"},
     {"at": 0.48, "event": "spotlight on ∇L(θ_t); label: 'slope of the loss here'"},
     {"at": 0.62, "event": "spotlight on η; label: 'step size (you choose it)'"},
     {"at": 0.85, "event": "spotlight on the minus sign: 'against the slope'"}],
    "The update rule with a moving spotlight and a glossary label per symbol.",
    "The spotlight walks the equation in narration order; the minus sign is the final accent."))

beats.append(manim("B04", "B04_FiveSteps", "WORKED_EXAMPLE", "mechanism",
    "Real numbers. Loss is theta squared, so the slope is two theta. Start at three, step size "
    "zero point one. Slope six, step zero point six: we land at two point four. Slope four point "
    "eight: one point nine two. Each step shrinks theta by the same factor, zero point eight. "
    "Five steps in, the loss fell from nine to just under one.",
    [{"at": 0.05, "event": "bowl and ball at θ=3; table header t | θ | slope | loss"},
     {"at": 0.25, "event": f"row t=0: {W[0]['theta']:g} | {W[0]['slope']:g} | {W[0]['loss']:g}"},
     {"at": 0.40, "event": f"ball steps to {W[1]['theta']:g}; row t=1 lands"},
     {"at": 0.55, "event": f"ball steps to {W[2]['theta']:g}; row t=2 lands"},
     {"at": 0.70, "event": "rows t=3..5 land with each step; '×0.8 per step' chip appears"},
     {"at": 0.90, "event": f"loss column highlights {W[0]['loss']:g} → {W[5]['loss']:g}"}],
    "Ball stepping down the bowl in lockstep with a table of executed values (demo/evidence.json).",
    "Each row lands exactly when the ball lands; the shrinking steps are the factor 0.8."))

beats.append(manim("B05", "B05_StepSize", "FALSIFIABILITY", "mechanism",
    "The step size is where this bites. Same bowl, same start, three choices. At zero point zero one, "
    "ten steps later theta has barely moved: two point four five. At zero point one, it's down to "
    "zero point three two. At one point one, every step overshoots the bottom and lands further out; "
    "after ten steps, theta is past eighteen. Too big, and it doesn't slow down. It runs away.",
    [{"at": 0.05, "event": "three bowls side by side, labelled η=0.01, η=0.1, η=1.1"},
     {"at": 0.20, "event": "left ball creeps; counter settles at θ₁₀ = " + str(SW['0.01']['theta'][-1])},
     {"at": 0.40, "event": "middle ball rolls in; counter θ₁₀ = " + str(SW['0.1']['theta'][-1])},
     {"at": 0.60, "event": "right ball zig-zags across the bottom, each bounce wider; terracotta"},
     {"at": 0.80, "event": "right counter climbs to θ₁₀ = " + str(SW['1.1']['theta'][-1])}],
    "Three learning rates on the same bowl, side by side, with θ after 10 executed steps.",
    "Crawl vs converge vs diverge happen simultaneously so the comparison is held, not narrated."))

lm, gm = NC["minima"][1], NC["minima"][0]  # minima sorted by theta: [-1.30 (global), 1.13 (local)]
beats.append(manim("B06", "B06_TwoValleys", "FALSIFIABILITY", "mechanism",
    "The second failure: the slope only knows where you are. This loss has two valleys. Start on "
    "the right, and the ball settles into the shallow one, at a loss of minus one point oh seven, "
    "and stops, because the slope there is zero. The deeper valley, at minus three point five one, "
    "is right next door, and gradient descent never sees it. Where you start decides where you end.",
    [{"at": 0.05, "event": "two-valley curve L(θ)=θ⁴−3θ²+θ draws on"},
     {"at": 0.25, "event": "ball drops at θ=2 and rolls into the right valley"},
     {"at": 0.50, "event": f"label at rest: 'loss {lm['loss']:g}', slope chip '0'"},
     {"at": 0.70, "event": f"left valley lights terracotta: 'loss {gm['loss']:g}'"},
     {"at": 0.88, "event": "ghost ball from θ=−2 rolls into the deep valley: start decides end"}],
    "A non-convex loss where gradient descent stops in the shallower valley (executed).",
    "The ball physically stops in the wrong valley while the deeper one is lit beside it."))

beats.append(manim("B07", "B07_Batches", "MECHANISM", "data",
    "Real models run a version of this same rule on millions, even billions, of settings at once, so the bowl "
    "becomes a landscape you can't draw. Two tricks make that affordable. Backpropagation computes "
    "every slope in one backward pass. And each step looks at a small batch: here, eight points "
    "out of two hundred. The path wobbles, but each step costs a twenty-fifth as much, and the fit "
    "lands within a few percent.",
    [{"at": 0.05, "event": "contour map of the loss over two settings (w, b) fades in"},
     {"at": 0.20, "event": "chip: 'backpropagation: every slope in one backward pass'"},
     {"at": 0.35, "event": "smooth ink path: 'all 200 points per step' draws to the minimum"},
     {"at": 0.55, "event": "wobbly terracotta path: '8 points per step' draws beside it"},
     {"at": 0.85, "event": f"end chips: loss {SC['full_end']['mse']:g} vs {SC['sgd_end']['mse']:g}"}],
    "Full-batch vs mini-batch paths on a real 2-parameter fit (seeded, executed).",
    "The two paths draw simultaneously; the wobble is visible and both reach the valley."))

# ---------------------------------------------------------------- closing block
beats.append(remotion("BVDT", "VERDICT", "ClaudeVerdictArtifact", {
    "artifactTitle": "Verdict", "artifactHeading": "Gradient descent, in six lines",
    "artifactLines": ["Loss measures how wrong the model is; the gradient is its slope.",
                      "Each step: new setting = old setting − step size × slope.",
                      "The step size decides it: too small crawls, too big runs away.",
                      "It finds a valley, not necessarily the lowest one.",
                      "Where you start decides which valley you end in.",
                      "At scale: backpropagation for the slopes, small batches for speed."]},
    "Let's recap with Claude. Loss measures how wrong the model is, and the gradient is its slope. "
    "Each step, the new setting is the old setting minus the step size times the slope. The step "
    "size decides it: too small crawls, too big runs away. It finds a valley, not necessarily the "
    "lowest one. Where you start decides which valley you end in. And at scale: backpropagation for the slopes, small batches for speed.",
    [{"at": 0.05, "event": "verdict artifact card in on cream"},
     {"at": 0.15, "event": "heading types"},
     {"at": 0.25, "event": "lines 1–5 land on their spoken cue"}],
    "artifact-in", lead_silence_s=0.5))

prompt = ("Write a short Python script, no ML libraries, that runs gradient descent on loss = theta "
          "squared, starting at theta = 3, for 10 steps, with step sizes 0.01, 0.1, 0.9 and 1.1. Print "
          "theta after every step. Then, using only the printed numbers, tell me which runs converge, "
          "which oscillate, which blow up, and predict the largest step size that still converges.")
beats.append(remotion("BHTF", "YOUR_TURN", "ClaudeComposerAsk", {
    "greeting": "Your turn.", "topic": "YOUR TURN · GRADIENT DESCENT",
    "segment": "Break gradient descent on purpose", "command": prompt,
    "runningText": "paste this into Claude…",
    "output": ["check: the slope is 2 × theta, and 0.1 goes 3 → 2.4 → 1.92",
               "check: 0.9 flips sign every step but still shrinks",
               "check: the cutoff is derived from the numbers, not asserted"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Your turn. Paste this into Claude: Write a short Python script, no M L libraries, that runs "
    "gradient descent on loss equals theta squared, starting at theta equals three, for ten steps, "
    "with step sizes zero point zero one, zero point one, zero point nine and one point one. Print "
    "theta after every step. Then, using only the printed numbers, tell me which runs converge, which "
    "oscillate, which blow up, and predict the largest step size that still converges. "
    "Here's what to check. Zero point one should go three, two point four, one point nine two. "
    "Zero point nine is the interesting one: it flips sign every step and still lands. And watch "
    "whether Claude derives the cutoff from the numbers, or just asserts it. If it says one, ask it why.",
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
    "greeting": "Ciao, Liam", "persona": "Liam (in for Bear)", "in_for_bear": True,
    "folderLabel": "@NikBearBrown", "captions": False,
    "evidence": "demo/gd_demo.py -> demo/evidence.json, demo/RUN-LOG.txt",
    "pronounce": {"eta": "ˈeɪtə"},
    "tags": ["gradient descent", "machine learning", "optimization", "learning rate",
             "backpropagation", "SGD"]},
    "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")

for b in beats:
    n = len(b["narration_text"].split())
    print(f"{b['beat_id']:5} {b.get('act',''):15} {n:4} words  ~{n/2.6:5.1f}s")
total = sum(len(b["narration_text"].split()) for b in beats)
print(f"total {total} words  ~{total/2.6/60:.1f} min (2.6 w/s)")
