# -*- coding: utf-8 -*-
"""Authoring script for the Monte Carlo schedule-risk cli-explainer reel.
Emits beat_sheet.json in the required cli-explainer spine, Claude skin,
@HumanitariansAI, af_bella voice, narrated first-person as Sanjana."""
import json, pathlib

TOPIC = "HUMANITARIANS AI · PROJECT MANAGEMENT"
SEG = "Monte Carlo Schedule Risk"
FOLDER = "@HumanitariansAI"

def composer(greeting, command, runningText, output=None, segment=SEG):
    return {
        "pattern": "ClaudeComposerAsk",
        "props": {
            "greeting": greeting,
            "topic": TOPIC,
            "segment": segment,
            "command": command,
            "runningText": runningText,
            "folderLabel": FOLDER,
            "modelLabel": "Claude",
            "effortLabel": "High",
            "output": output or [],
        },
        "rendered": {"out": "", "at": ""},
    }

def code(title, src, spark):
    return {
        "pattern": "ClaudeCodeBeat",
        "props": {"title": title, "code": src, "sparkLine": spark},
        "rendered": {"out": "", "at": ""},
    }

CODE_V1 = '''# schedule_sim.py  --  Monte Carlo schedule risk
import numpy as np

# the chain we THINK is critical -- (optimistic, most_likely, pessimistic) days
TASKS = {
    "design":  (3, 5, 12),
    "backend": (5, 8, 20),
    "test":    (2, 4, 10),
    "release": (1, 2,  5),
}

def sample(o, m, p):
    # triangular: cheap, asymmetric, respects the whole range
    return np.random.triangular(o, m, p)

def one_trial():
    return sum(sample(*rng) for rng in TASKS.values())

trials = np.array([one_trial() for _ in range(10_000)])

print("plan (sum of most-likely):", sum(m for _, m, _ in TASKS.values()))
print("P50:", round(np.percentile(trials, 50), 1))
print("P80:", round(np.percentile(trials, 80), 1))'''

CODE_V2 = '''# schedule_sim.py  --  v2: real dependencies; parallel paths merge at the MAX
TASKS = {  # name: (o, m, p, [predecessors])
    "design":   (3, 5, 12, []),
    "backend":  (5, 8, 20, ["design"]),
    "frontend": (4, 7, 16, ["design"]),   # runs in PARALLEL with backend
    "test":     (2, 4, 10, ["backend", "frontend"]),
    "release":  (1, 2,  5, ["test"]),
}

def one_trial():
    finish = {}
    for name, (o, m, p, preds) in TASKS.items():
        # a task waits for ALL its predecessors -- the merge point
        start = max((finish[d] for d in preds), default=0)
        finish[name] = start + np.random.triangular(o, m, p)
    return finish["release"]          # project ends when the last task ends

trials = np.array([one_trial() for _ in range(10_000)])
print("Commit to the P80 date:", round(np.percentile(trials, 80), 1), "days")'''

HANDOFF_CMD = (
    "Here is my project plan. For every task I have given three estimates: "
    "optimistic, most-likely, pessimistic, plus which tasks must finish before it "
    "can start.\n\n[PASTE YOUR TASKS + DEPENDENCIES]\n\n"
    "1. Run a Monte Carlo simulation: 10,000 trials, triangular sampling per task.\n"
    "2. Respect the dependency graph -- a task starts when ALL predecessors finish.\n"
    "3. Give me P50, P80 and P90 finish dates, and the single-point 'sum of "
    "most-likely' for comparison.\n"
    "4. Tell me which task's uncertainty drives the deadline the most."
)

beats = [
    # B00 INTRO ---------------------------------------------------------------
    {"beat_id": "B00", "act": "INTRO",
     "role_note": "COLD OPEN LAW -- Claude UI, ask lands answered; first-person Sanjana",
     "narration_text": (
        "Hi, I'm Sanjana, a project manager at Humanitarians AI, and this video is about "
        "Monte Carlo schedule risk. It's a way to use AI and a simple simulation to answer "
        "the one question every project lives or dies on: when will this actually finish? "
        "Not when we hope it finishes, when it really will."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "Hi, Sanjana",
                  "Treat my project timeline as a range, not a single date. Run a Monte "
                  "Carlo simulation over my task estimates and tell me the finish date I can "
                  "actually commit to.",
                  "simulating 10,000 schedules…",
                  ["a single-point deadline is almost always optimistic",
                   "give every task a range, then simulate thousands of times",
                   "commit to the P80 date, not the wish"])},
     "estimated_duration_s": 12},

    # B01 PROBLEM -------------------------------------------------------------
    {"beat_id": "B01", "act": "PROBLEM",
     "role_note": "stakes BEFORE the build; SHOW-DON'T-TELL: the single number vs the spread",
     "narration_text": (
        "Here's the problem. When we plan, we give each task one number -- our best guess -- "
        "and we add them up. Design five days, backend eight, test four, release two: nineteen "
        "days, done. But every one of those guesses is really a range, and the ranges are "
        "lopsided. A task can finish a day or two early, or it can blow up by a week. When you "
        "add up ranges like that, the real finish drifts later than the plan almost every time. "
        "The single number isn't just imprecise -- it is systematically optimistic."),
     "visual_intent": (
        "Left: the deterministic plan -- 5 task bars summing to a single marker at 21 days. "
        "Right: the real outcome as a right-skewed histogram whose bulk sits past 21; a "
        "vertical line at 21 labelled 'the plan', most of the distribution to its right, "
        "annotation 'most outcomes land LATER'."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B01_SinglePointLie", "file": "scenes.py"}},
     "estimated_duration_s": 18},

    # B02 FRAMEWORK -----------------------------------------------------------
    {"beat_id": "B02", "act": "FRAMEWORK",
     "role_note": "framework shown BEFORE the worked build (PROOF: framework-first)",
     "narration_text": (
        "So here is the method, before we build anything. Four steps. One: give every task a "
        "range -- optimistic, most-likely, pessimistic -- instead of a single guess. Two: draw "
        "one random duration for each task and add them up along the dependencies. That's one "
        "possible version of your project. Three: do that ten thousand times, and you get a "
        "whole distribution of finish dates. Four: don't report the average. Report the P80 -- "
        "the date you'll hit eighty percent of the time. That's the number you can promise."),
     "visual_intent": (
        "A 4-step horizontal pipeline, each step a labelled card that lights up in turn: "
        "1 RANGE (o/m/p), 2 SAMPLE ONCE (one finish), 3 REPEAT 10,000x (a distribution), "
        "4 COMMIT TO P80. Terracotta accent on the active step; arrows between."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B02_Method", "file": "scenes.py"}},
     "estimated_duration_s": 20},

    # B03 ASK / CLI -----------------------------------------------------------
    {"beat_id": "B03", "act": "ASK",
     "role_note": "ClaudeComposerAsk -- show and discuss the prompt; SPARK 'The ask,'",
     "narration_text": (
        "Let's build it with Claude. The ask is precise: take my tasks, each with three "
        "estimates, sample a triangular distribution for every task, sum them for one trial, "
        "run ten thousand trials, and report the percentiles. Precise in, precise out -- I'm "
        "telling it the sampling method and the output I want, so the code it writes is the "
        "code I can check."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "The ask,",
                  "claude \"Write schedule_sim.py: TASKS as {name: (optimistic, most_likely, "
                  "pessimistic)}. Sample each task with numpy.random.triangular. one_trial() "
                  "sums all task samples. Run 10,000 trials. Print the sum-of-most-likely plan "
                  "and the P50, P80, P90 percentiles.\"",
                  "writing the simulator…")},
     "estimated_duration_s": 15},

    # B04 CODE ----------------------------------------------------------------
    {"beat_id": "B04", "act": "CODE",
     "role_note": "ClaudeCodeBeat -- the ACTUAL code; read the line that teaches",
     "narration_text": (
        "Here's what it wrote. Read the middle. Sample uses a triangular distribution -- cheap, "
        "and it respects the whole range including that long tail on the pessimistic side. "
        "one_trial draws a fresh duration for every task and adds them up: that's a single "
        "imagined run of the project. Then we do it ten thousand times and take percentiles. "
        "Notice the plan number -- the sum of most-likely durations -- is computed right "
        "alongside, so we can see exactly how far off the single guess is."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": code("schedule_sim.py", CODE_V1,
                               "Sample the range, not the guess.")},
     "estimated_duration_s": 18},

    # B05 OUTPUT --------------------------------------------------------------
    {"beat_id": "B05", "act": "OUTPUT",
     "role_note": "moving output -- histogram builds; P50/P80 lines; plan on the optimistic edge",
     "narration_text": (
        "Run it. Watch the ten thousand trials pile up into a distribution. The plan said "
        "twenty-one days -- but look where twenty-one falls: right on the optimistic edge. The "
        "P50, the coin-flip date, is already later. And the P80 -- the date we'd actually "
        "commit to -- is further out still. That gap between the plan and the P80 isn't padding "
        "or pessimism. It is the schedule risk that was invisible in the single number."),
     "visual_intent": (
        "Histogram of finish days accumulating from samples (bars filling in). Vertical lines: "
        "'plan 21' on the left edge, 'P50' near the median, 'P80' further right in terracotta; "
        "shaded gap between plan and P80 labelled 'hidden risk'."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B05_Histogram", "file": "scenes.py"}},
     "estimated_duration_s": 18},

    # B06 CHANGE (revision) ---------------------------------------------------
    {"beat_id": "B06", "act": "CHANGE",
     "role_note": "REVISION -- check & change; SPARK 'The revision,'",
     "narration_text": (
        "But the first version cheated a little: it added the tasks as if they run one after "
        "another. Real projects have parallel work that merges. Backend and frontend both start "
        "after design and run at the same time -- and testing can't begin until both are done. "
        "When paths merge, the project waits for the slowest one. So let's revise the ask: model "
        "the real dependency graph, and make each task start only when all of its predecessors "
        "have finished."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "The revision,",
                  "claude \"Revise it: each task also lists its predecessors. A task starts at "
                  "the MAX finish time of its predecessors, not at the end of the previous line. "
                  "Backend and frontend run in parallel after design; test waits for both. "
                  "Re-run and give me the P80.\"",
                  "adding the dependency graph…")},
     "estimated_duration_s": 18},

    # B07 CODE (revised) ------------------------------------------------------
    {"beat_id": "B07", "act": "CODE",
     "role_note": "revised code -- the one line that matters (the merge)",
     "narration_text": (
        "The whole revision is one line. Each task's start is the max of its predecessors' "
        "finish times. That single max is the merge: the project can't move past a join point "
        "until every path into it is done. It's why adding people to parallel tracks doesn't "
        "always help -- the finish is decided by the slowest path, and the more parallel paths "
        "you have, the more likely at least one of them runs long."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": code("schedule_sim.py · v2", CODE_V2,
                               "Parallel paths merge at the max.")},
     "estimated_duration_s": 18},

    # B08 OUTPUT (revised) ----------------------------------------------------
    {"beat_id": "B08", "act": "OUTPUT",
     "role_note": "the better output -- the shift made visible",
     "narration_text": (
        "Re-run it. The new distribution sits to the right of the old one and spreads wider -- "
        "exactly what the merge predicts. The P80 moves out by several days. And that is not "
        "bad news: it's the truth arriving early, while we can still plan for it. Now I can give "
        "a date with a confidence attached -- eighty percent by this day -- instead of a single "
        "number everyone privately knows we'll miss."),
     "visual_intent": (
        "Two overlaid distributions: v1 (sequential, lighter) and v2 (with merge, terracotta) "
        "shifted right and wider. P80 markers for both, arrow showing the P80 moving out; "
        "caption 'commit to the P80 -- 80% confidence'."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B08_Revised", "file": "scenes.py"}},
     "estimated_duration_s": 17},

    # B09 SUMMARY -------------------------------------------------------------
    {"beat_id": "B09", "act": "SUMMARY",
     "role_note": "the lesson in one beat -- reusable reference",
     "narration_text": (
        "So here's the takeaway you can reuse on any plan. A single-point deadline hides its "
        "risk. Give every task a range, simulate thousands of times, and read three numbers: "
        "P50 is a coin flip, P80 is a commitment, P90 is a promise you'll rarely break. The gap "
        "between your old single-number plan and the P80 is your real risk buffer -- and now "
        "you can see it, size it, and defend it."),
     "visual_intent": (
        "Reference card: three labelled thresholds P50 'coin flip' / P80 'commit' / P90 "
        "'promise' on a mini distribution; below, 'plan number -> P80 = your hidden risk "
        "buffer'. Clean, high negative space."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B09_Summary", "file": "scenes.py"}},
     "estimated_duration_s": 16},

    # B10 NEXT STEPS / HANDOFF ------------------------------------------------
    {"beat_id": "B10", "act": "NEXT STEPS",
     "role_note": "HANDOFF LAW -- prompt READ ALOUD and discussed; greeting 'Your turn.'",
     "narration_text": (
        "Your turn. Take your own project -- the one with the deadline you're not sure about. "
        "List the tasks, give each one three honest estimates, and note what depends on what. "
        "Paste this prompt into Claude. It'll run the simulation, hand you back a P80 date, and "
        "-- this is the useful part -- tell you which task's uncertainty is driving the deadline, "
        "so you know exactly where tightening an estimate would buy you the most confidence."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "Your turn.", HANDOFF_CMD,
                  "paste this into Claude and run it on your own plan…",
                  segment="Simulate your own deadline")},
     "estimated_duration_s": 20},

    # B11 OUTRO ---------------------------------------------------------------
    {"beat_id": "B11", "act": "OUTRO",
     "role_note": "title restate; HAI channel outro",
     "narration_text": (
        "Monte Carlo schedule risk -- with Sanjana Rao, for Humanitarians AI. Give your plan a "
        "range, and let the simulation tell you the truth. Thanks for watching."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": {
                  "pattern": "ClaudeTitleOutro",
                  "props": {"title": "Monte Carlo Schedule Risk.",
                            "handle": "@HumanitariansAI",
                            "subline": "with Sanjana Rao · project management, simulated with AI"},
                  "rendered": {"out": "", "at": ""}}},
     "estimated_duration_s": 8},
]

# Remotion mangles non-ASCII props on this Windows setup (· -> Â·, ... likewise).
# Keep every RENDERED prop string ASCII; narration_text (TTS only) keeps unicode.
_ASCII = {"·": " | ", "…": "...", "—": " - ", "–": "-",
          "’": "'", "‘": "'", "“": '"', "”": '"',
          "×": "x", "−": "-"}
def _san(x):
    if isinstance(x, str):
        for a, b in _ASCII.items():
            x = x.replace(a, b)
        return x
    if isinstance(x, list):
        return [_san(i) for i in x]
    if isinstance(x, dict):
        return {k: _san(v) for k, v in x.items()}
    return x

for b in beats:
    rem = b.get("shot", {}).get("remotion")
    if rem and "props" in rem:
        rem["props"] = _san(rem["props"])
    b.setdefault("voice", "af_bella")
    b["engine"] = "kokoro"
    b["voice_kokoro"] = "af_bella"
    b.setdefault("build", {"status": "SLATE"})

sheet = {
    "metadata": {
        "title": "Monte Carlo Schedule Risk: When Will This Project Really Finish?",
        "slug": "monte-carlo-schedule-risk",
        "topic": TOPIC,
        "register": "Teardown-warm",
        "audience": "Humanitarians AI",
        "brand": "claude-hai",
        "channel_title": "@HumanitariansAI",
        "creator": "Sanjana Rao",
        "engine": "kokoro",
        "palette": "claude",
        "style_preset": "claude",
        "style": "claude-cli",
        "voice_kokoro": "af_bella",
        "voice_policy": "persistent-fellow-selected",
        "voice_approval": "APPROVED",
        "aspect_ratio": "16:9",
        "note": ("cli-explainer for @HumanitariansAI, narrated first-person by Sanjana Rao "
                 "(af_bella). Claude skin bookends; Manim outputs in the humanitarians/claude "
                 "palette. Topic: Monte Carlo schedule risk (project management + simulation)."),
        "tags": ["project management", "Monte Carlo simulation", "schedule risk",
                 "P80", "critical path", "Humanitarians AI", "Sanjana Rao", "Claude"],
        "total_estimated_duration_seconds": sum(b["estimated_duration_s"] for b in beats),
    },
    "beats": beats,
}

out = pathlib.Path(__file__).parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote", out, "with", len(beats), "beats;",
      "est", sheet["metadata"]["total_estimated_duration_seconds"], "s")
