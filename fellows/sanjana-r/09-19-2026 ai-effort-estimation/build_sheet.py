# -*- coding: utf-8 -*-
"""Authoring script for the AI Effort Estimation cli-explainer reel.
Emits beat_sheet.json in the required cli-explainer spine, Claude skin,
@HumanitariansAI, af_bella voice, narrated first-person as Sanjana Rao.

Topic: AI in project management -- turning a task description into a trustworthy
effort estimate with reference-class forecasting + velocity calibration.
Every number on screen is produced by the reel's own seed-locked estimator
(scenes.py); this file mirrors those numbers in the narration and the CODE beats."""
import json, pathlib

TOPIC = "HUMANITARIANS AI | PROJECT MANAGEMENT"
SEG = "AI Effort Estimation"
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

CODE_V1 = '''# estimate.py  --  v1: one number per task (the gut estimate)
TASKS = {
    "oauth_login":     "add OAuth login (Google + GitHub)",
    "settings_page":   "build the account settings page",
    "export_endpoint": "add an export-report API endpoint",
}

# a single story-point guess, straight from the gut
# (this is also what a one-shot "just estimate it" LLM call returns)
POINTS = {
    "oauth_login":     5,   # "about a week"
    "settings_page":   2,   # "a couple of days"
    "export_endpoint": 3,   # "half a week"
}

def estimate(task):
    return POINTS[task]        # one number. no history, no range.

for t in TASKS:
    print(f"{t:16s} {estimate(t)} days")
print("sprint total:", sum(POINTS.values()), "days")   # -> 10'''

CODE_V2 = '''# estimate.py  --  v2: reference-class forecasting + velocity
import numpy as np

# how similar PAST tasks ACTUALLY took (days), grouped into classes
HISTORY = {
    "integration": [4, 6, 7, 9, 14],   # OAuth-shaped work: fat tail
    "ui_form":     [1, 2, 2, 3],       # a settings page
    "crud":        [2, 3, 3, 4, 6],    # a plain endpoint
}
MATCH = {"oauth_login": "integration",
         "settings_page": "ui_form",
         "export_endpoint": "crud"}

VELOCITY = 1.15   # we ship 15% slower this quarter than that history

def estimate(task):
    actuals = np.array(HISTORY[MATCH[task]], float)
    p50, p80 = np.percentile(actuals, [50, 80]) * VELOCITY
    return round(p50, 1), round(p80, 1)      # a RANGE, not a point

for t in MATCH:
    p50, p80 = estimate(t)
    print(f"{t:16s} {p50}-{p80} days   (P50-P80)")'''

HANDOFF_CMD = (
    "Here is my backlog -- each task is a one-line description.\n"
    "[PASTE YOUR NEW TASKS]\n\n"
    "And here are my last 15 COMPLETED tasks with how many days each ACTUALLY took:\n"
    "[PASTE COMPLETED TASKS + ACTUAL DAYS]\n\n"
    "1. Group my completed tasks into reference classes (similar kinds of work).\n"
    "2. Match each new task to its closest class.\n"
    "3. From that class's ACTUAL times, give me a P50-P80 range, not one number.\n"
    "4. Scale by my current velocity if my recent pace differs from that history.\n"
    "5. Flag any task with NO matching class -- those I should spike before I commit."
)

beats = [
    # B00 INTRO ---------------------------------------------------------------
    {"beat_id": "B00", "act": "INTRO",
     "role_note": "COLD OPEN LAW -- Claude UI, ask lands answered; first-person Sanjana",
     "narration_text": (
        "Hi, I'm Sanjana, a project manager at Humanitarians AI, and this video is about "
        "something every plan quietly depends on: the estimate. How long will this task take? "
        "We usually answer with a gut number. I'll show you how to use AI to turn that guess "
        "into an honest range -- one built from how your team's work has actually gone before, "
        "not from how you hope it'll go this time."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "Hi, Sanjana",
                  "Don't just guess how long each task will take. Match it to similar work we've "
                  "already finished, and give me an honest range I can plan around.",
                  "matching tasks to your history...",
                  ["a gut estimate is almost always optimistic",
                   "match each task to similar work you've actually finished",
                   "report a range, not a single number"])},
     "estimated_duration_s": 15},

    # B01 PROBLEM -------------------------------------------------------------
    {"beat_id": "B01", "act": "PROBLEM",
     "role_note": "stakes BEFORE the build; SHOW-DON'T-TELL: the gut number vs what similar work took",
     "narration_text": (
        "Here's the trouble. When someone asks how long a task will take, we picture it going "
        "well. Add OAuth login? About a week. Build a settings page? A couple of days. So the "
        "sprint gets a confident total -- ten days. But think about the last time you did work "
        "like this. The integration that hit a surprise. The 'quick' page that grew. We "
        "estimate from the best case, and then we're shocked when reality lands later. "
        "Psychologists call it the planning fallacy, and a single gut number walks right into it."),
     "visual_intent": (
        "Left: the gut plan -- three task bars summing to one confident marker at 10 days. "
        "Right: dots of how SIMILAR past tasks actually finished, scattered well to the right of "
        "10, with a soft cloud centered near ~19; annotation 'the same kind of work, last time'."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B01_GutGuess", "file": "scenes.py"}},
     "estimated_duration_s": 19},

    # B02 FRAMEWORK -----------------------------------------------------------
    {"beat_id": "B02", "act": "FRAMEWORK",
     "role_note": "framework shown BEFORE the worked build (PROOF: framework-first)",
     "narration_text": (
        "So here's the method, before we build anything. It's called reference-class forecasting, "
        "and it's four steps. One: describe the task in plain features -- what kind of work is "
        "this, really? Two: match it to its reference class -- the pile of similar tasks you've "
        "actually completed. Three: read that class's real distribution -- not what you hoped "
        "they'd take, what they actually took. Four: calibrate -- nudge for how fast your team is "
        "moving right now, and report a range. Notice what changed: your estimate now comes from "
        "evidence, not optimism."),
     "visual_intent": (
        "A 4-step horizontal pipeline, each a labelled card lighting up in turn: "
        "1 DESCRIBE (task -> features), 2 MATCH (find similar finished work), "
        "3 DISTRIBUTION (what they really took), 4 CALIBRATE (velocity -> a range). "
        "Terracotta accent on the active step; arrows between."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B02_Method", "file": "scenes.py"}},
     "estimated_duration_s": 21},

    # B03 ASK / CLI -----------------------------------------------------------
    {"beat_id": "B03", "act": "ASK",
     "role_note": "ClaudeComposerAsk -- the NAIVE ask, so the revision has somewhere to go; SPARK 'The ask,'",
     "narration_text": (
        "Let's build it with Claude, and let's start the way most people do -- with the simple "
        "ask. Take my three tasks and just estimate each one in days. It's the obvious first "
        "move, and it's worth doing, because seeing where it falls short is exactly what tells "
        "us what to fix."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "The ask,",
                  "claude \"Write estimate.py: TASKS is a dict of {name: description}. POINTS is "
                  "a single-number day estimate per task. estimate(task) returns that number. "
                  "Print each task's estimate and the sprint total.\"",
                  "writing the first estimator...")},
     "estimated_duration_s": 15},

    # B04 CODE ----------------------------------------------------------------
    {"beat_id": "B04", "act": "CODE",
     "role_note": "ClaudeCodeBeat -- the ACTUAL v1 code; read the line that teaches",
     "narration_text": (
        "Here's what it wrote. It's honest about what it is. There's a list of tasks, and then "
        "POINTS -- one number for each, straight from the gut. Five days for OAuth, two for the "
        "settings page, three for the endpoint. The estimate function just looks that number up. "
        "No history, no range -- and that comment says it out loud. This is the same thing you "
        "get if you ask an AI to 'just estimate it' in one shot: a confident number with nothing "
        "underneath it. Add them up and the sprint is ten days."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": code("estimate.py", CODE_V1,
                               "One number, no evidence.")},
     "estimated_duration_s": 19},

    # B05 OUTPUT --------------------------------------------------------------
    {"beat_id": "B05", "act": "OUTPUT",
     "role_note": "moving output -- the three point estimates land; total 10; looks certain",
     "narration_text": (
        "Run it, and here's the plan. Three tasks, three tidy numbers, one clean total: ten days. "
        "And it looks great -- that's the danger. There's no visible uncertainty anywhere on this "
        "screen, so everyone treats ten days like a fact. But nothing here knows how work like "
        "this has actually gone for us before. It's a guess wearing the costume of a measurement."),
     "visual_intent": (
        "Three task rows, each with a single dot/short bar at its estimate (5, 2, 3 days) on a "
        "shared day axis; a bold 'sprint total = 10 days' tag; a faint '...how sure are we?' "
        "question hovering, no error bars anywhere -- the false precision made visible."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B05_PointPlan", "file": "scenes.py"}},
     "estimated_duration_s": 17},

    # B06 CHANGE (revision) ---------------------------------------------------
    {"beat_id": "B06", "act": "CHANGE",
     "role_note": "REVISION -- check & change; the reference-class ask; SPARK 'The revision,'",
     "narration_text": (
        "So let's fix it. The missing ingredient is our own past. We have a stack of completed "
        "tasks and we know how long each really took. Let's revise the ask: don't guess a number "
        "-- match each new task to similar finished work, read what that group actually took, and "
        "hand me back a range from the middle to the eighty-percent mark. And scale it for the "
        "fact that we're running a bit slower this quarter than we used to."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "The revision,",
                  "claude \"Revise estimate.py: add HISTORY = actual completed-task durations "
                  "grouped by class, and MATCH each task to a class. estimate() reads the class's "
                  "P50 and P80 with numpy.percentile, times a VELOCITY factor, and returns the "
                  "range. Re-run for all three tasks.\"",
                  "adding your history + velocity...")},
     "estimated_duration_s": 19},

    # B07 CODE (revised) ------------------------------------------------------
    {"beat_id": "B07", "act": "CODE",
     "role_note": "revised code -- the one line that matters (percentile * velocity -> range)",
     "narration_text": (
        "The whole revision is really one line. We pull the actual times from the matched class, "
        "take the fiftieth and eightieth percentiles, and multiply by velocity. That percentile "
        "call is the heart of it: it lets the real spread of past work set the estimate, instead "
        "of a hopeful guess. The fiftieth is a coin-flip. The eightieth is the number you can "
        "actually commit to. And because we multiply by velocity, the estimate tracks how fast "
        "the team is really moving today -- not how fast we were six months ago."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": code("estimate.py | v2", CODE_V2,
                               "Let the past set the range.")},
     "estimated_duration_s": 19},

    # B08 OUTPUT (revised) ----------------------------------------------------
    {"beat_id": "B08", "act": "OUTPUT",
     "role_note": "the better output -- ranges replace points; total 10->19; the no-class EDGE shown",
     "narration_text": (
        "Re-run it, and the plan grows up. Every task is a range now. OAuth isn't five days -- "
        "it's eight to twelve, because integrations like it really do run long. The settings "
        "page holds near two to three. The endpoint, three to five. Watch the old gut numbers: "
        "each one sits right on the optimistic edge of its range. Add the honest ends up and the "
        "sprint moves from ten days to about nineteen. And here's the honest part of the method: "
        "the new database migration has no similar past work to match -- so we don't fake a "
        "number, we flag it to spike first. When there's no reference class, the right answer is "
        "'I don't know yet,' not a confident guess."),
     "visual_intent": (
        "Four task rows on a shared day axis. Rows 1-3: a P50-P80 band each (8-12, 2-3, 3-5) "
        "with the old gut point marked on the optimistic edge. Totals compared: 'gut 10' (muted) "
        "vs 'honest P80 ~19' (terracotta), held side-by-side. Row 4 'DB migration' has NO band, "
        "just a flag 'no reference class -> spike it' -- the falsifiability case, shown."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B08_Ranges", "file": "scenes.py"}},
     "estimated_duration_s": 22},

    # B09 SUMMARY -------------------------------------------------------------
    {"beat_id": "B09", "act": "SUMMARY",
     "role_note": "the reusable rubric in one beat -- three questions + the honest-unknown rule",
     "narration_text": (
        "So here's the rubric you can run on any estimate, with or without code. Ask three "
        "questions. What's the reference class -- what kind of work is this, really? What did "
        "that class actually take -- read the spread, not the best case? And what's our velocity "
        "-- are we faster or slower than that history right now? Answer those, report a range "
        "instead of a point, and flag anything with no reference class as a spike, not a "
        "promise. That's how a guess becomes an estimate you can defend."),
     "visual_intent": (
        "Reference card: three numbered questions (REFERENCE CLASS / WHAT IT ACTUALLY TOOK / "
        "VELOCITY) stacked, each with a one-line gloss; a footer rule 'no class? spike it, "
        "don't fake it.' Clean, high negative space, terracotta accent on the range idea."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "B09_Summary", "file": "scenes.py"}},
     "estimated_duration_s": 18},

    # B10 NEXT STEPS / HANDOFF ------------------------------------------------
    {"beat_id": "B10", "act": "NEXT STEPS",
     "role_note": "HANDOFF LAW -- prompt READ ALOUD and discussed; greeting 'Your turn.'",
     "narration_text": (
        "Your turn. Grab your backlog and, just as important, your last dozen or so finished "
        "tasks with the days they really took -- that history is the whole trick. Paste this "
        "prompt into Claude. It'll group your finished work into classes, match each new task, "
        "and hand you back honest ranges. And it'll flag the tasks with no match -- the ones to "
        "prototype before you ever put a date on them. A good answer gives you ranges and names "
        "its evidence; a bad one hands you a single confident number, which is exactly what we "
        "just learned not to trust."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer(
                  "Your turn.", HANDOFF_CMD,
                  "paste this into Claude with your own history...",
                  segment="Estimate your own backlog")},
     "estimated_duration_s": 22},

    # B11 OUTRO ---------------------------------------------------------------
    {"beat_id": "B11", "act": "OUTRO",
     "role_note": "title restate; HAI channel outro",
     "narration_text": (
        "AI effort estimation -- with Sanjana Rao, for Humanitarians AI. Estimate from your "
        "history, report a range, and stop being surprised. Thanks for watching."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": {
                  "pattern": "ClaudeTitleOutro",
                  "props": {"title": "AI Effort Estimation.",
                            "handle": "@HumanitariansAI",
                            "subline": "with Sanjana Rao | estimate from history, not hope"},
                  "rendered": {"out": "", "at": ""}}},
     "estimated_duration_s": 9},
]

# Remotion mangles non-ASCII props on this Windows setup (dot -> A-dot, etc.).
# Keep every RENDERED prop string ASCII; narration_text (TTS only) keeps unicode.
_ASCII = {"·": " | ", "…": "...", "—": " - ", "–": "-",
          "’": "'", "‘": "'", "“": '"', "”": '"',
          "×": "x", "−": "-", "→": "->"}
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
        "title": "AI Effort Estimation: Stop Guessing How Long Tasks Take",
        "slug": "ai-effort-estimation",
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
                 "(af_bella). Claude skin bookends; Manim outputs in the Claude palette. "
                 "Topic: AI effort estimation via reference-class forecasting + velocity."),
        "tags": ["project management", "effort estimation", "reference-class forecasting",
                 "story points", "planning fallacy", "velocity", "P80",
                 "Humanitarians AI", "Sanjana Rao", "Claude"],
        "total_estimated_duration_seconds": sum(b["estimated_duration_s"] for b in beats),
    },
    "beats": beats,
}

out = pathlib.Path(__file__).parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote", out, "with", len(beats), "beats;",
      "est", sheet["metadata"]["total_estimated_duration_seconds"], "s")
