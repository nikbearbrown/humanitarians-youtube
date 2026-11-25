#!/usr/bin/env python3
"""Author beat_sheet.json for hai-static-into-pictures — the kid-friendly cut.

Subject: a from-scratch diffusion notebook (NumPy + Matplotlib only).

Unlike the earlier teardown reels, this one TEACHES. The notebook is careful
work: it ships a numerical gradient check, real baselines beside its results,
and it is honest about its own limits. Nothing here is a critique.

Every figure spoken on screen is PARSED OUT OF THE NOTEBOOK'S OWN recorded
outputs by this script — not transcribed by hand — and the forward-process
figure is additionally recomputed from scratch. Assertions fail the build if
anything drifts. No individual is named.
"""
import json
import re
from pathlib import Path

import numpy as np

NB = Path(r"C:\Users\sawan\OneDrive\Desktop\dumps\diffusion_models_from_scratch.ipynb")
OUT = Path(__file__).resolve().parent / "beat_sheet.json"
WPS = 2.60

# ── pull the notebook's own recorded outputs ──────────────────────────────
nb = json.loads(NB.read_text(encoding="utf-8"))
cells = nb["cells"]


def stream(i):
    return "".join(
        "".join(o.get("text", []))
        for o in cells[i].get("outputs", [])
        if o.get("output_type") == "stream"
    )


# forward process
SIGNAL_LEFT = float(re.search(r"sqrt\(alpha_bar_T\)\s*=\s*([0-9.]+)", stream(10)).group(1))
# gradient check
WORST_ERR = re.search(r"worst relative error:\s*([0-9.e+-]+)", stream(25)).group(1)
# training
N_PARAMS = re.search(r"model has ([\d,]+) parameters", stream(30)).group(1)
FINAL_LOSS = float(re.findall(r"loss ([0-9.]+)", stream(30))[-1])
# determinism
MAX_DIFF = re.search(r"max difference between two runs from the same noise:\s*([0-9.]+)", stream(50)).group(1)
# MMD table
MMD = {}
for line in stream(53).splitlines():
    m = re.match(r"\s*(.+?)\s{2,}(-?[0-9.]+)\s*$", line)
    if m and not m.group(1).startswith("method"):
        MMD[m.group(1).strip()] = float(m.group(2))
# guidance sweep
GUID = []
for line in stream(60).splitlines():
    m = re.match(r"\s*([0-9.]+)\s+([0-9.]+)%\s+([0-9.]+)\s*$", line)
    if m:
        GUID.append((float(m.group(1)), float(m.group(2)), float(m.group(3))))

# ── independent recomputation of the schedule ─────────────────────────────
T = 200
ab = np.cumprod(1 - np.linspace(1e-4, 0.05, T))
RECOMPUTED = float(np.sqrt(ab[-1]))

# ── guards ────────────────────────────────────────────────────────────────
assert abs(RECOMPUTED - SIGNAL_LEFT) < 5e-4, (RECOMPUTED, SIGNAL_LEFT)
assert 0.07 < SIGNAL_LEFT < 0.09, SIGNAL_LEFT
assert float(WORST_ERR) < 1e-5, WORST_ERR
assert 0.30 < FINAL_LOSS < 0.36, FINAL_LOSS
assert MAX_DIFF == "0.0", MAX_DIFF
assert len(MMD) >= 7 and len(GUID) >= 6, (len(MMD), len(GUID))

DDPM = MMD["DDPM, 200 steps"]
D50, D20, D10, D5 = (MMD[f"DDIM, {n} steps"] for n in (50, 20, 10, 5))
REAL = MMD["Fresh real data (best possible)"]
NOISE = MMD["Pure noise N(0, I)"]
assert DDPM < D50 < D20 < D10 < D5, "expected monotonic degradation"
assert D5 > 0.8 * NOISE, "the 5-step claim depends on it being near pure noise"

W0 = next(g for g in GUID if g[0] == 0.0)
W1 = next(g for g in GUID if g[0] == 1.0)
WMAX = GUID[-1]
assert W0[1] < 55 and W1[1] > 99, (W0, W1)

print(f"[nb] signal left at T=200: {SIGNAL_LEFT:.4f}  (recomputed {RECOMPUTED:.4f})")
print(f"[nb] gradient check worst err: {WORST_ERR} · params {N_PARAMS} · final loss {FINAL_LOSS}")
print(f"[nb] MMD  real={REAL}  ddpm={DDPM}  ddim50={D50}  ddim5={D5}  noise={NOISE}")
print(f"[nb] guidance w=0 {W0[1]}%/{W0[2]}  w=1 {W1[1]}%/{W1[2]}  w={WMAX[0]} {WMAX[1]}%/{WMAX[2]}")

B = []


def add(bid, act, text, pattern, props, motion="illustrate"):
    B.append({
        "beat_id": bid, "act": act, "narration_text": text,
        "shot": {"type": "GRAPHIC", "source": "remotion", "motion": motion,
                 "remotion": {"pattern": pattern, "props": props}},
        "estimated_duration_s": round(len(text.split()) / WPS, 1),
        "audio_file": f"mp3/beat-{bid}.mp3",
    })


def stmt(bid, act, text, eyebrow, headline, kicker="", motion="fade"):
    add(bid, act, text, "IdxStatement",
        {"eyebrow": eyebrow, "headline": headline, "kicker": kicker}, motion)


add("B00", "ASK",
    "Every picture you have ever seen made by an AI started life as pure static. Random dots. Nothing. "
    "This is Humanitarians AI, and today we find out how a machine turns a screenful of mess into a picture — "
    "using a real one, built from scratch, that you can watch working.",
    "ClaudeComposerAsk",
    {"greeting": "Show me how it works.", "topic": "HOW PICTURE MACHINES WORK",
     "segment": "Static Into Pictures",
     "command": "Explain how a diffusion model turns random noise into data, using a real from-scratch implementation. Start with the trick that makes it possible, and show me the numbers at every step.",
     "runningText": "opening the notebook…",
     "folderLabel": "@HumanitariansAI",
     "output": ["first: wreck a picture on purpose",
                "then: learn to spot the mess",
                "finally: take the mess back off"]},
    "type-on")

stmt("B01", "PICTURE",
     "We need something to make, so here is our picture. Not a cat, not a face — just a spiral of dots. "
     "Small enough that you can see every single one, which means you can see absolutely everything that happens to it.",
     "OUR PICTURE", "A spiral made of dots.",
     "small enough to watch every step")

add("B02", "SPRINKLE",
    "Now the strange first move. We wreck it. On purpose. "
    "Take the spiral and sprinkle a tiny bit of mess over it. Then sprinkle a tiny bit more. And again. Two hundred times.",
    "KidSprinkle", {}, "stagger")

stmt("B03", "GONE",
     f"By the end, only {SIGNAL_LEFT*100:.0f} percent of the spiral is left. "
     "Everything you could recognise is gone. It is a round fuzzy cloud, and it looks exactly like television static.",
     "ALL GONE", f"Only about {SIGNAL_LEFT*100:.0f}% of the picture survives.",
     "two hundred tiny sprinkles, and no spiral")

stmt("B04", "IDEA",
     "And here is the whole idea, in one sentence. Making a mess is easy — "
     "but we wrote down exactly how much mess we added each time. So the mess is not random to us. We have the recipe.",
     "THE BIG IDEA", "Wrecking it is easy. And we kept the recipe.",
     "if you know how it was broken, you can learn to unbreak it")

add("B05", "QUESTION",
    "So we show the machine a messy picture, and we ask it one question. Not, what is this a picture of. "
    "Just: which bit of this is the mess?",
    "KidMessSpotter", {}, "illustrate")

stmt("B06", "WHY",
     "That is a much easier question, and it is the clever part of the whole thing. "
     "The machine never needs to know it is looking at a spiral. It only needs to point at the sprinkles.",
     "WHY THAT HELPS", "Spot the mess, and you can take a little off.",
     "an easy question, asked two hundred times")

add("B07", "REVERSE",
    "So that is what we do. Start with nothing but static. Ask: where is the mess? Brush a tiny bit of it away. "
    "Then ask again. Two hundred times.",
    "KidUnsprinkle", {}, "stagger")

stmt("B08", "MAGIC",
     "And a spiral appears. Not the one we started with — that one is long gone. A brand new spiral, "
     "built out of random dots by a machine that only ever learned to spot mess.",
     "A SPIRAL NOBODY DREW", "Out of pure static, a new picture.",
     "nothing of the original was left to copy")

add("B09", "HOMEWORK",
    "Now, should we believe any of this? The people who built it asked the same thing. "
    "So they worked out the maths by hand, then had the computer check it a completely different way, by counting.",
    "KidTwoWaysCheck", {"worstErr": WORST_ERR}, "stagger")

stmt("B10", "HONEST",
     f"They were honest about the hard bits too. While learning, the machine's score stops improving at about {FINAL_LOSS:.1f}, "
     "and never reaches zero. That is not a fault. Some of the mess genuinely cannot be guessed, by anyone, ever.",
     "AN HONEST NUMBER", "It never gets a perfect score. It cannot.",
     "some sprinkles are simply unguessable")

add("B11", "JUDGE",
    "Then they brought in a judge — a way of scoring how close the made-up spirals are to real ones. Lower is better.",
    "KidJudgeScore",
    {"rows": [
        {"label": "real dots (best possible)", "score": f"{REAL:+.5f}", "bar": 0.0, "hero": False},
        {"label": "our machine, 200 steps", "score": f"{DDPM:.5f}", "bar": DDPM / NOISE, "hero": True},
        {"label": "our machine, 50 steps", "score": f"{D50:.5f}", "bar": D50 / NOISE, "hero": True},
        {"label": "our machine, 10 steps", "score": f"{D10:.5f}", "bar": D10 / NOISE, "hero": True},
        {"label": "pure static", "score": f"{NOISE:.5f}", "bar": 1.0, "hero": False},
    ]},
    "stagger")

stmt("B12", "READING",
     "Read the bars. Real dots score about zero — that is as good as it gets. "
     "Our machine's two hundred step version is so close to that line you can barely see its bar. Pure static is right off the end.",
     "READING THE SCORES", "The made-up spirals land almost on the real ones.",
     "and pure static is nowhere near")

add("B13", "FASTER",
    "Two hundred steps is slow, though. So can we take bigger steps and get there faster?",
    "KidBigSteps",
    {"rows": [
        {"steps": "200 steps", "score": f"{DDPM:.5f}", "ok": True},
        {"steps": "50 steps", "score": f"{D50:.5f}", "ok": True},
        {"steps": "20 steps", "score": f"{D20:.5f}", "ok": True},
        {"steps": "10 steps", "score": f"{D10:.5f}", "ok": True},
        {"steps": "5 steps", "score": f"{D5:.5f}", "ok": False},
    ]},
    "stagger")

stmt("B14", "LIMIT",
     "Fifty steps is four times faster and still gives a clean spiral. Twenty is ten times faster and still works. "
     "But five steps falls apart completely — and look at its score. It is about the same as pure static. "
     "You went faster and arrived nowhere.",
     "TOO BIG A STEP", "At five steps, you may as well not have bothered.",
     "the same score as the random dots you started from")

add("B15", "STEER",
    "Last trick, and it is the one in every picture app you have used. "
    "Now there are two shapes, and we tell the machine which one we want. There is a dial for how hard to insist.",
    "KidSteerDial",
    {"rows": [
        {"w": f"{w:g}", "acc": f"{a:.1f}%", "spread": f"{s:.3f}",
         "accN": a / 100.0, "spreadN": s / GUID[0][2]}
        for (w, a, s) in GUID
    ]},
    "stagger")

stmt("B16", "TRADEOFF",
     f"With the dial at zero it ignores you completely — {W0[1]:.0f} percent right, which is just a coin flip. "
     f"Turn it to one and it gets the right shape {W1[1]:.1f} percent of the time. Turn it higher and it is perfect, every time.",
     "TURNING IT UP", "From a coin flip to never wrong.",
     "so why not turn it all the way up?")

stmt("B17", "COST",
     f"Because look at the second bar. As obedience goes up, variety goes down — from {GUID[0][2]:.2f} all the way to {WMAX[2]:.2f}. "
     "The shapes get more and more alike. You asked for exactly what you wanted, and you got it, over and over again.",
     "WHAT IT COSTS", "More obedient. Less interesting.",
     "there is no setting that gives you both")

stmt("B18", "SNEAKY",
     "And one sneaky detail that is easy to miss. The machine itself never changed. Not one thing was re-learned. "
     "The dial only changes how you ask — which is why you can move it for every picture, without ever retraining anything.",
     "THE SNEAKY BIT", "The dial is in the asking, not the machine.",
     "nothing was retrained between any of those settings")

stmt("B19", "SCALE",
     "And this toy is not a toy. The same maths, the same mess-spotting, the same dial, "
     "runs the picture tools you already know. The only thing that changes is the size of the machine.",
     "THE SAME MATHS", "Spirals today. Pictures everywhere else.",
     "only the size changes — not one idea")

add("B20", "VERDICT",
    "So here is the whole thing, start to finish.",
    "ClaudeVerdictArtifact",
    {"artifactTitle": "How static becomes a picture",
     "artifactHeading": "The whole idea",
     "artifactLines": [
         f"Wreck it on purpose: add a sprinkle of mess 200 times, until only {SIGNAL_LEFT*100:.0f}% of the picture is left.",
         "Ask one easy question: not 'what is this?' but 'which part is the mess?' — asked over and over.",
         "Undo it: start from pure static, brush a little mess off each time, and a brand new picture appears.",
         f"Check your working: the maths was verified two independent ways, agreeing to {WORST_ERR}.",
         f"Go faster, carefully: 50 steps is 4x quicker and still good; 5 steps scores about the same as pure static.",
         f"Steer it, and pay for it: obedience rises to 100%, variety falls from {GUID[0][2]:.2f} to {WMAX[2]:.2f}."]},
    "stagger")

add("B21", "HANDOFF",
    "Your turn. Next time you use a picture app and see a slider called guidance, you now know exactly what it does. "
    "Try the same prompt at a low setting and a high one, and watch the pictures get more obedient and more boring at the same time.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "YOUR TURN", "segment": "Find the dial",
     "command": "Take one prompt and generate it at a low guidance setting and a high one. Compare how closely each follows the prompt, and how different the images are from each other.",
     "runningText": "turning the dial…",
     "folderLabel": "@HumanitariansAI",
     "output": ["low: varied, loosely follows you",
                "high: obedient, and all rather alike"]},
    "type-on")

add("B22", "OUTRO",
    "Static into pictures. If you like knowing how the magic actually works, subscribe. Humanitarians AI.",
    "ClaudeTitleOutro",
    {"title": "Static Into Pictures", "handle": "@HumanitariansAI"},
    "fade")

sheet = {
    "metadata": {
        "title": "Static Into Pictures",
        "slug": "hai-static-into-pictures",
        "topic": "HOW PICTURE MACHINES WORK",
        "register": "Teardown",
        "audience": "HAI",
        "brand": "claude",
        "voice": "HumanitariansAI",
        "engine": "kokoro",
        "palette": "claude",
        "style_preset": "claude",
        "ground": "#FAF9F5",
        "voice_kokoro": "af_bella",
        "channel": "humanitarians-ai",
        "handle": "@HumanitariansAI",
        "note": ("KID-FRIENDLY explainer of a from-scratch diffusion notebook. This reel TEACHES — "
                 "the source notebook is careful work (numerical gradient check, real baselines, "
                 "honest trade-offs) and the reel says so rather than hunting for faults. Every "
                 "figure is parsed from the notebook's own recorded outputs by build_beat_sheet.py, "
                 "and the forward-process figure is independently recomputed. The sprinkle scenes "
                 "implement the real forward equation. NO INDIVIDUAL IS NAMED. Bella (af_bella)."),
        "tags": ["diffusion models", "explain like I'm ten", "noise", "denoising",
                 "DDPM", "DDIM", "classifier-free guidance", "kids", "Humanitarians AI"],
    },
    "beats": B,
}
OUT.write_text(json.dumps(sheet, indent=2, ensure_ascii=False), encoding="utf-8")

words = sum(len(b["narration_text"].split()) for b in B)
print(f"\nwrote {OUT}")
print(f"{len(B)} beats · {words} words · projected {words/WPS:.0f}s = {int(words/WPS)//60}m{int(words/WPS)%60:02d}s")
banned = ["chinmay", "chinmai", "chinme", "sawant", "savant"]
blob = json.dumps(sheet, ensure_ascii=False).lower()
hits = [x for x in banned if x in blob]
print("NAME CHECK:", "CLEAN" if not hits else f"FAIL {hits}")
print("cartoon/animated scenes:",
      sum(1 for b in B if b["shot"]["remotion"]["pattern"].startswith("Kid")), "of", len(B))
