#!/usr/bin/env python3
"""Author beat_sheet.json for hai-practising-in-its-sleep — the kid-friendly cut.

Subject: a from-scratch World Models notebook (NumPy only). A VAE squeezes 16x16
frames to 8 numbers, a memory network predicts the next frame, and a controller is
evolved ENTIRELY inside the model's dream — then plays the real game.

This reel TEACHES. Every figure is parsed from the notebook's recorded outputs
under assertions. No individual is named.

NEW IN THIS BUILD: a dense-scene duration audit. Twice now a dense scene has
shipped with narration too short to read it, so the build itself now fails if a
data-heavy scene is given less than DENSE_MIN_S of projected narration.
"""
import json
import re
from pathlib import Path

NB = Path(r"C:\Users\sawan\OneDrive\Desktop\dumps\world_models_from_scratch.ipynb")
OUT = Path(__file__).resolve().parent / "beat_sheet.json"
WPS = 2.60
DENSE_MIN_S = 12.0
DENSE = {"KidOneFrame", "KidSqueeze", "KidMemoryMatters", "KidPlanAhead",
         "KidLoop", "KidFinalBoard", "ClaudeVerdictArtifact"}

nb = json.loads(NB.read_text(encoding="utf-8"))
cells = nb["cells"]


def stream(i):
    return "".join("".join(o.get("text", []))
                   for o in cells[i].get("outputs", [])
                   if o.get("output_type") == "stream")


def grab(i, pat, g=1):
    m = re.search(pat, stream(i))
    assert m, f"{pat!r} not found in cell {i}"
    return m.group(g)


# ── parse ─────────────────────────────────────────────────────────────────
RANDOM = float(grab(9, r"random\s+catches ([\d.]+)%"))
GREEDY = float(grab(9, r"greedy\s+catches ([\d.]+)%"))
ORACLE = float(grab(9, r"oracle\s+catches ([\d.]+)%"))
PERFECT = grab(16, r"frames rebuilt with zero wrong pixels: ([\d.]+%)")
COMPRESS = grab(16, r"compression: (\d+) pixels -> (\d+) numbers", 0)
PIX = grab(16, r"compression: (\d+) pixels")
NUMS = grab(16, r"-> (\d+) numbers")
RATIO = grab(16, r"\((\d+x) smaller\)")
LIN_R2 = float(grab(18, r"ball x\s+linear R² ([\d.]+)"))
NN_R2 = float(grab(18, r"ball x\s+linear R² [\d.]+\s+nearest-neighbour R² ([\d.]+)"))
REWARD_ACC = grab(23, r"right sign: ([\d.]+)%")
REWARD_BASE = grab(23, r"always guessing 'miss' would get ([\d.]+)%")

MPC = [(a, float(b)) for a, b in
       re.findall(r"MPC with\s+(\d+) imagined plans per step: catch rate ([\d.]+)%", stream(39))]
NEW_DATA = grab(42, r"new data: ([\d.]+)% of episodes end in a catch")
NEW_ACC = grab(42, r"reward head accuracy on random test games: ([\d.]+)%")

# the notebook's own final board (cell 45) is the source of truth for the ranking
BOARD = []
for line in stream(45).splitlines():
    m = re.match(r"^(.+?)\s{2,}([\d.]+)%\s*$", line.rstrip())
    if m and not m.group(1).startswith("agent"):
        BOARD.append((m.group(1).strip(), float(m.group(2))))

Z_ONLY = next(v for k, v in BOARD if "z only" in k)
Z_MEM = next(v for k, v in BOARD if "z + memory" in k)   # NOT the greedy row, which says "no memory"
AFTER_LOOP = next(v for k, v in BOARD if "loop round" in k)

# ── guards ────────────────────────────────────────────────────────────────
assert 20 < RANDOM < 35 and 55 < GREEDY < 70 and ORACLE == 100.0, (RANDOM, GREEDY, ORACLE)
assert float(PERFECT.rstrip('%')) > 95, PERFECT
assert NN_R2 > 0.9 > LIN_R2, (LIN_R2, NN_R2)   # the probe story depends on this gap
assert float(REWARD_ACC) > float(REWARD_BASE), (REWARD_ACC, REWARD_BASE)
assert len(MPC) >= 3 and MPC[-1][1] > MPC[0][1], MPC
assert len(BOARD) >= 6, len(BOARD)
assert Z_MEM > Z_ONLY * 1.5, (Z_ONLY, Z_MEM)   # memory must roughly double it
assert Z_MEM > GREEDY, (Z_MEM, GREEDY)         # the dreamer must beat the cheat
assert AFTER_LOOP > Z_MEM, (AFTER_LOOP, Z_MEM)
print(f"[nb] baselines random {RANDOM}% greedy {GREEDY}% oracle {ORACLE}%")
print(f"[nb] VAE {PIX}->{NUMS} ({RATIO}) · {PERFECT} perfect · probe lin {LIN_R2} vs nn {NN_R2}")
print(f"[nb] dream: z-only {Z_ONLY}% · z+memory {Z_MEM}% · after loop {AFTER_LOOP}%")
print(f"[nb] MPC {MPC} · reward head {REWARD_ACC}% (base {REWARD_BASE}%)")

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
    "A machine learned to play a game by practising in its sleep. "
    "It built a little copy of the world inside its own head, trained there, and then — "
    "having never once touched the real game — went and played it rather well. This is Humanitarians AI.",
    "ClaudeComposerAsk",
    {"greeting": "Show me the dream.", "topic": "LEARNING INSIDE YOUR OWN HEAD",
     "segment": "Practising In Its Sleep",
     "command": "Walk me through a world model: squeezing what it sees into a few numbers, learning to predict what happens next, then training a player entirely inside that prediction. Show me whether the player actually works in the real game.",
     "runningText": "opening the notebook…",
     "folderLabel": "@HumanitariansAI",
     "output": ["squeeze what you see",
                "learn what happens next",
                "then practise somewhere that does not exist"]},
    "type-on")

add("B01", "GAME",
    "Here is the whole game. A ball falls down a little sixteen-by-sixteen grid, "
    "and a paddle at the bottom can go left, go right, or stay put. Catch the ball. That is everything.",
    "KidCatchGame", {}, "stagger")

stmt("B02", "BASELINES",
     f"Before anything clever, how hard is it? Moving at random catches {RANDOM:.0f} percent of balls. "
     f"A simple chaser that always slides towards the ball catches {GREEDY:.0f} percent. "
     f"And something that knows exactly where the ball will land catches every single one. "
     f"So {RANDOM:.0f} is hopeless, {GREEDY:.0f} is decent, and {ORACLE:.0f} is perfect.",
     "HOW HARD IS IT?", f"{RANDOM:.0f}% by luck. {GREEDY:.0f}% by chasing. {ORACLE:.0f}% if you truly know.",
     "those are the marks to beat")

add("B03", "ONEFRAME",
    "Now the problem at the heart of this. Look at one single picture of the game. "
    "The ball is right there, in the middle. So which way is it going? "
    "You cannot tell. It might be drifting left, it might be drifting right, "
    "and those two possibilities end in completely different places. "
    "A photograph shows you where things are. It never shows you where they are heading.",
    "KidOneFrame", {}, "stagger")

add("B04", "SQUEEZE",
    f"So, first job. Take each picture, all {PIX} little squares of it, and squash it down into just {NUMS} numbers. "
    f"That is {RATIO} smaller. It sounds like you would lose almost everything — "
    f"but when you build the picture back out of those {NUMS} numbers, "
    f"{PERFECT} of the time every single square comes back exactly right.",
    "KidSqueeze",
    {"pixels": PIX, "numbers": NUMS, "ratio": RATIO, "perfect": PERFECT},
    "stagger")

stmt("B05", "PROBE",
     f"And the notebook checks something careful here. Is the ball's position really hidden in those {NUMS} numbers, "
     f"or did it get lost? Looked at in a simple straight-line way, you can barely find it. "
     f"But looked at properly, by comparing against similar pictures, you can recover it perfectly. "
     "The information is all there. It is just not written in a tidy order.",
     "IS IT ALL STILL THERE?", "Hidden, but not lost.",
     "scrambled is not the same as missing")

stmt("B06", "MEMORY",
     "Next, the memory. We train a second part whose only job is to watch what has happened so far "
     "and guess what the next picture will be. Not what the game is. Not the rules. "
     "Just: given everything up to now, what comes next.",
     "THE MEMORY", "Watch what happened. Guess what follows.",
     "and it keeps a running sense of what is going on")

add("B07", "DREAM",
    "And once it can guess the next picture, something strange becomes possible. "
    "Feed its own guess back in as if it were real, and it can keep going, and going, "
    "playing a whole game that is not happening anywhere.",
    "KidDreaming", {}, "stagger")

stmt("B08", "TRAIN",
     "So that is where we train the player. Inside the dream. "
     "It tries, it fails, it adjusts, hundreds of times over — and the real game is switched off the entire time. "
     "Then, only at the very end, we let it out to play for real.",
     "TRAINING IN THE DREAM", "The real game stays switched off.",
     "every bit of practice happens inside the model")

add("B09", "MEMORYMATTERS",
    f"And here is the finding the whole notebook is built around. We train the player twice, identically. "
    f"The first one only gets to see the squeezed picture: it catches {Z_ONLY:.0f} percent. "
    f"The second one sees the picture and also gets the memory's running sense of what has been happening: "
    f"{Z_MEM:.0f} percent. Same dream, same practice, same everything else.",
    "KidMemoryMatters",
    {"rows": [
        {"label": "sees only the picture", "pct": f"{Z_ONLY:.1f}%", "val": Z_ONLY / 100,
         "hero": False, "note": "no memory"},
        {"label": "sees the picture and remembers", "pct": f"{Z_MEM:.1f}%", "val": Z_MEM / 100,
         "hero": True, "note": "with memory"},
        {"label": "a cheat that sees the real ball", "pct": f"{GREEDY:.1f}%", "val": GREEDY / 100,
         "hero": False, "note": "but cannot remember"},
    ]},
    "stagger")

stmt("B10", "BEATS",
     f"Look at that bottom bar again, because it is the good bit. The chaser is allowed to cheat — "
     f"it sees the true ball position, perfectly, every turn. It manages {GREEDY:.0f} percent. "
     f"The dreamer, working only from a blurry squeezed picture and its own memory, gets {Z_MEM:.0f}. "
     "Remembering beat seeing.",
     "REMEMBERING BEAT SEEING", "A good memory beat perfect eyesight.",
     "because speed lives in the past, not the present")

add("B11", "PLAN",
    "There is a second way to use a dream, and it is the one you already use yourself. "
    "Instead of training a player at all, just imagine several things you could do, see how each one turns out, and pick the best.",
    "KidPlanAhead",
    {"rows": [{"plans": a, "pct": f"{b:.0f}%", "val": b / 100} for (a, b) in MPC]},
    "stagger")

add("B12", "LOOP",
    f"And then you can go round in a circle. The trained player goes and plays for real, which produces much better experience — "
    f"{NEW_DATA} of those games end in a catch instead of {RANDOM:.0f} percent. "
    f"Feed that back in, the dream gets more accurate, and the player trained in the better dream reaches {AFTER_LOOP:.0f} percent.",
    "KidLoop",
    {"oldData": f"{RANDOM:.1f}%", "newData": NEW_DATA,
     "oldAcc": f"{REWARD_ACC}%", "newAcc": f"{NEW_ACC}%", "finalPct": f"{AFTER_LOOP:.1f}%"},
    "stagger")

add("B13", "BOARD",
    "So here is everybody, lined up by how many balls they actually caught in the real game. "
    "The random flailer at the bottom. The cheat that can see the true ball. "
    "The dreamer with no memory, barely better than flailing. "
    "And then the ones with memory, up near the top, next to something that knows the answer outright.",
    "KidFinalBoard",
    {"rows": [{"name": n, "pct": f"{v:.1f}%", "val": v / 100,
               "hero": ("z + memory" in n or "loop" in n or "MPC" in n)} for (n, v) in BOARD]},
    "stagger")

stmt("B14", "LESSON",
     "And here is the thing worth carrying away. A single snapshot tells you what is there. "
     "It cannot tell you what is happening. For that you need to remember what came a moment ago — "
     "and that is as true for you crossing a road as it is for a machine catching a ball.",
     "THE BIG IDEA", "A snapshot is not a situation.",
     "what is happening only exists across time")

add("B15", "VERDICT",
    "So here is the whole thing. A tiny game. A squeezer that throws away almost everything and keeps what matters. "
    "A memory that guesses what happens next. A dream built out of those guesses. "
    "And a player that got good inside the dream, came out, and beat something that was allowed to cheat.",
    "ClaudeVerdictArtifact",
    {"artifactTitle": "Practising in its sleep",
     "artifactHeading": "The whole idea",
     "artifactLines": [
         f"Squeeze: every {PIX}-square picture becomes {NUMS} numbers, {RATIO} smaller, and {PERFECT} rebuild with every square correct.",
         f"Check: the ball's position is still in there — hard to read in a straight line, perfectly readable when compared against similar frames.",
         "Remember: a second part learns only to guess the next picture, and keeps a running sense of what has been going on.",
         "Dream: feed its own guesses back in, and it plays whole games that are not happening anywhere.",
         f"Train inside the dream: picture only, {Z_ONLY:.0f}%. Picture plus memory, {Z_MEM:.0f}% — beating the {GREEDY:.0f}% cheat that sees the real ball.",
         f"Go round again: better play makes better experience makes a better dream — {AFTER_LOOP:.0f}%, against a perfect score of {ORACLE:.0f}%."]},
    "stagger")

add("B16", "HANDOFF",
    "Your turn. Next time you catch something, notice what your eyes actually gave you: "
    "a stack of snapshots, and no arrows at all. The sense that the thing is moving towards you "
    "is not something you saw. Your brain built it, out of remembering. Same trick, different machine.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "YOUR TURN", "segment": "Notice your own memory",
     "command": "Explain what information a single still frame can and cannot contain about a moving object, and what a brain or a model has to add to recover motion.",
     "runningText": "thinking about motion…",
     "folderLabel": "@HumanitariansAI",
     "output": ["a frame holds positions, never velocities",
                "motion is something you reconstruct"]},
    "type-on")

add("B17", "OUTRO",
    "Practising in its sleep. If you like the ideas that turn out to be about you too, subscribe. Humanitarians AI.",
    "ClaudeTitleOutro",
    {"title": "Practising In Its Sleep", "handle": "@HumanitariansAI"},
    "fade")

# ── the new guard: dense scenes need time to be read ──────────────────────
short = [(b["beat_id"], b["shot"]["remotion"]["pattern"], b["estimated_duration_s"])
         for b in B
         if b["shot"]["remotion"]["pattern"] in DENSE and b["estimated_duration_s"] < DENSE_MIN_S]
assert not short, f"dense scenes with too little narration to read: {short}"
print(f"[audit] all dense scenes >= {DENSE_MIN_S}s projected narration")

sheet = {
    "metadata": {
        "title": "Practising In Its Sleep",
        "slug": "hai-practising-in-its-sleep",
        "topic": "LEARNING INSIDE YOUR OWN HEAD",
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
        "note": ("KID-FRIENDLY explainer of a from-scratch World Models notebook (VAE + memory + "
                 "controller evolved in the dream, on 16x16 Catch). This reel TEACHES. Every figure "
                 "parsed from recorded outputs under 9 assertions, three of which encode the argument "
                 "itself (memory roughly doubles the catch rate; the dreamer beats the sighted cheat; "
                 "the loop improves on it). Build also audits dense scenes for >=12s narration, after "
                 "that pacing bug recurred twice. NO INDIVIDUAL IS NAMED. Bella (af_bella)."),
        "tags": ["world models", "VAE", "latent space", "memory", "dreaming",
                 "model-based RL", "explain like I'm ten", "kids", "Humanitarians AI"],
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
print("animated scenes:", sum(1 for b in B if b["shot"]["remotion"]["pattern"].startswith("Kid")), "of", len(B))
