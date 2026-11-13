# -*- coding: utf-8 -*-
"""Authoring script for "The Critical Path" ai-explainer (16:9).

ai-explainer (claude-explainer) CONCEPT explainer (STEM/AI + project management),
@HumanitariansAI channel, af_bella (female) voice, first-person Sanjana Rao.

Topic: the Critical Path Method. AI can compute the critical path of a project from a
task list + dependencies -- but only if you give it the real dependencies, and the path
moves as the project changes.
Framework taught = MAP / FIND / PROTECT:
  MAP     -- give AI the real tasks, durations, and dependencies (garbage in = wrong path)
  FIND    -- the critical path = the longest chain of dependent tasks; its length is the
             shortest the project can finish; tasks on it have zero slack
  PROTECT -- guard the critical path; slack elsewhere is a buffer, not free time; re-check
             when anything shifts (the path can move)

Worked example network (illustrative, arithmetic is correct):
  A Design 3 -> B Backend 5 -> D Integrate 4 -> E Test 2   = 14 days (CRITICAL)
  A Design 3 -> C UI 2      -> D Integrate 4 -> E Test 2   = 11 days  (C has 3 days slack)
Falsifiability: speeding up C (non-critical) 2->1 day does NOT move the 14-day deadline;
and if C slips +4 (beyond its 3-day slack) the path through C becomes 15 -> the critical
path SHIFTS to A-C-D-E.

Concept explainer -- the network is an illustrative teaching example, not real project
data (FACTCHECK.md). No people named. Rendered prop strings ASCII (Remotion).
NEW graphics vs prior films: an activity-on-node network diagram with durations, the
critical path highlighted terracotta, a slack bar, and a path-shift animation.
"""
import json, pathlib

TOPIC = "Irreducibly Human"            # claude-hai branding kicker is LOCKED
SEG = "The Critical Path"
FOLDER = "@HumanitariansAI"


def composer(greeting, command, runningText, segment, output=None):
    return {"pattern": "ClaudeComposerAsk",
            "props": {"greeting": greeting, "topic": TOPIC, "segment": segment,
                      "command": command, "runningText": runningText,
                      "folderLabel": FOLDER, "modelLabel": "Claude",
                      "effortLabel": "High", "output": output or []},
            "rendered": {"out": "", "at": ""}}


def manim(scene_class):
    return {"scene_class": scene_class, "file": "scenes.py"}


def beat(bid, act, role, narration, shot, est, extra=None):
    b = {"beat_id": bid, "act": act, "role_note": role, "narration_text": narration,
         "shot": shot, "estimated_duration_s": est, "voice": "af_bella",
         "engine": "kokoro", "voice_kokoro": "af_bella"}
    if extra:
        b.update(extra)
    return b


beats = []

beats.append(beat(
    "T00", "INTRO",
    "COLD OPEN LAW -- ClaudeComposerAsk, ask answered; first-person Sanjana",
    "Hi, I'm Sanjana, a project manager at Humanitarians AI. Every project has a deadline, "
    "and when it's slipping, the instinct is to speed everything up. But here's the thing "
    "most schedules get wrong: only some of your tasks actually control the finish date. "
    "The rest have slack. The chain that sets your deadline is called the critical path -- "
    "and AI can find it for you in seconds. The trick is knowing what that actually means.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "Hi, Sanjana",
         "AI can compute my project's critical path from the task list. What is it "
         "actually telling me -- and what should I do with it?",
         "finding the critical path...",
         "The Critical Path",
         ["the longest chain of dependent tasks sets the deadline",
          "tasks on it have zero slack -- a day late = a day late",
          "speeding up the wrong task changes nothing"])},
    28.0))

beats.append(beat(
    "T01", "OVERVIEW",
    "EXECUTIVE-SUMMARY LAW -- hesitant-writer BLUF; corrects the reel's real misconception",
    "Here's the whole idea in one breath. It feels like to finish sooner, you speed up any "
    "task. You don't. Only the longest chain of dependent tasks -- the critical path -- "
    "sets the deadline. Speed up a task that isn't on it, and you've saved nothing. Find "
    "that path, and you know exactly where effort actually counts.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": {
         "pattern": "BrutalistHesitantWriter",
         "props": {
             "text": "To finish sooner, speed up any task.\nEvery task moves the deadline.",
             "face": "serif", "fontSize": 48, "lineSpacing": 1.3, "align": "center",
             "triggerWords": "any task, Every task moves the deadline",
             "replacementWords": "the critical path, Only the longest chain moves it",
             "mistakeRate": 6, "hesitateWithin": 3, "hesitateBetween": 22,
             "charMs": 55, "jitter": 28, "seed": "cpm-bluf-01",
             "showCaret": True, "brandLabel": "@HumanitariansAI",
             "contextTitle": "The whole idea in one breath",
             "contextItems": [
                 {"label": "Critical path", "detail": "the longest chain -- it sets the deadline"},
                 {"label": "Slack", "detail": "everything else can slip a little, for free"},
             ],
         }, "rendered": {"out": "", "at": ""}}},
    16.0, {"lead_silence_s": 0.8}))

beats.append(beat(
    "T02", "PROBLEM",
    "SHOW-DON'T-TELL: a task network; the longest chain sets the end date, not every task",
    "So picture a small project as a network. Design, then two things can happen at once -- "
    "build the backend, build the interface -- then integrate them, then test. The tasks "
    "aren't a straight line; some run in parallel. And that's the catch. The backend takes "
    "five days, the interface takes two. They both start after design and both feed "
    "integration -- so the interface finishing early buys you nothing, because you're still "
    "waiting on the backend. The finish date is set by the longest path through the "
    "network, not by any single task.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "An activity-on-node network: A Design(3) -> B Backend(5) and C "
     "UI(2) in parallel -> D Integrate(4) -> E Test(2). Nodes with durations, arrows for "
     "dependencies. Show the two branches B(5) vs C(2) converging at D; highlight that D "
     "waits for the SLOWER branch. Reframe: the longest path sets the finish, not any one "
     "task. Terracotta on the longest branch.",
     "manim": manim("T02_Network")},
    37.0))

beats.append(beat(
    "T03", "FRAMEWORK",
    "framework-first (PROOF): MAP / FIND / PROTECT, shown BEFORE any example",
    "So to use the critical path well, three steps. One: map. Give the AI the real tasks, "
    "their durations, and -- this is the part people skip -- the real dependencies, what "
    "must finish before what. The path is only as true as the dependencies you feed it. "
    "Two: find. Let the AI compute the critical path -- the longest chain -- and the slack "
    "on every other task. Three: protect. Guard the critical path, spend your attention "
    "there, and re-check after any change, because the critical path can move. Map, find, "
    "protect.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "Three steps stacked: 1 MAP (real tasks + durations + DEPENDENCIES) "
     "2 FIND (AI computes the longest chain + slack on the rest) 3 PROTECT (guard the "
     "critical path; re-check -- it can move). Each with a one-line meaning. Footer: the "
     "path is only as true as the dependencies you feed it. Terracotta on the footer.",
     "manim": manim("T03_MapFindProtect")},
    38.0))

beats.append(beat(
    "T04", "ASK",
    "ASK->RESULT LAW -- composer ask that computes the T05 critical path",
    "Let's do a real one. Here's that five-task project. Watch me ask the AI to find the "
    "critical path and tell me the slack on every task -- not just the answer, the paths it "
    "compared to get there.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "The path,",
         "Here are my tasks, durations, and dependencies. Find the critical path, show me "
         "every path you compared and its length, and give the slack (float) on each task. "
         "Don't just give the answer -- show the paths.",
         "computing the critical path...",
         "Worked example: find the path")},
    15.0))

beats.append(beat(
    "T05", "RESULT",
    "worked example walked through the framework -- compute both paths, slack on the rest",
    "And there it is. Two paths run from start to finish. Design, backend, integrate, test "
    "is fourteen days. Design, interface, integrate, test is only eleven. The longer one "
    "wins -- fourteen days is the critical path, and every task on it has zero slack: a day "
    "late there is a day late for the whole project. The interface branch? It has three "
    "days of slack. It can slip three full days and the deadline never moves. That's not a "
    "problem to fix -- that's a buffer you can use.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "The network with both paths traced: A-B-D-E = 14 (highlighted "
     "terracotta = CRITICAL, zero slack) and A-C-D-E = 11. A slack bar on C shows '3 days "
     "slack'. Numbers add up on screen (3+5+4+2=14, 3+2+4+2=11). Verdict: critical path = "
     "14 days. Terracotta on the critical chain; muted on the slack branch.",
     "manim": manim("T05_FindPath")},
    30.0))

beats.append(beat(
    "T06", "FALSIFIABILITY",
    "falsifiability -- speeding up a non-critical task does nothing; slack overrun shifts the path",
    "Now the mistake almost everyone makes. The deadline's tight, so someone says: crash "
    "the interface, get it done in one day instead of two. Feels productive. But watch the "
    "finish date -- it doesn't move. Still fourteen days, because the interface was never on "
    "the critical path. You spent effort and saved nothing. And here's the twist that "
    "catches people: if that interface branch slips the other way -- say it blows past its "
    "three days of slack and takes six -- now its path is fifteen days, longer than the "
    "backend's. The critical path just moved. So you don't find it once. You watch it.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "Two moves on the network. MOVE 1: shrink C 2->1; the finish stays "
     "14 (a red 'no change' on the deadline) -- speeding a non-critical task does nothing. "
     "MOVE 2: grow C past its slack (to 6); the A-C-D-E path becomes 15 > 14 and the "
     "critical path SHIFTS to the C branch (terracotta jumps to A-C-D-E). Caption: the "
     "critical path moves -- watch it. Terracotta/red on the shift.",
     "manim": manim("T06_PathShift")},
    40.0))

beats.append(beat(
    "T07", "SUMMARY",
    "reusable rubric restated -- AI FINDS the path; you PROTECT it and re-check",
    "So here's the rule for any schedule. Let the AI find the critical path -- it compares "
    "every route faster than you can by hand. But you protect it: put your best people and "
    "your attention on that chain, treat slack elsewhere as a buffer, and re-check the path "
    "every time something changes. The AI finds the longest path. You keep it from getting "
    "longer.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "visual_intent": "A clean router: LEFT 'AI FINDS -- the longest path, fast'. A center "
     "gate = MAP / FIND / PROTECT. RIGHT 'YOU PROTECT -- guard it, re-check'. High negative "
     "space, terracotta accent on the gate.",
     "manim": manim("T07_Router")},
    24.0))

beats.append(beat(
    "T08", "NEXT STEPS",
    "HANDOFF LAW -- ClaudeComposerAsk 'Your turn.'; prompt read aloud + discussed",
    "Your turn. Take your own project's tasks and run this. Give the AI your tasks, "
    "durations, and dependencies, and ask for three things: the critical path, the slack "
    "on every other task, and -- this is the useful part -- what the new critical path "
    "would be if your riskiest task slipped by a week. That last answer tells you which "
    "'safe' task is one bad week away from becoming your problem. A good answer shows its "
    "paths. A bad one gives a single number with no reasoning -- and a critical path with "
    "no paths behind it is just a guess.",
    {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
     "remotion": composer(
         "Your turn.",
         "Here are my tasks, durations, and dependencies.\n[PASTE YOUR TASK LIST]\n\n"
         "1. Find the critical path (show every path you compared + its length).\n"
         "2. Give the slack (float) on every task.\n"
         "3. If [my riskiest task] slips by a week, what becomes the new critical path?\n"
         "Show your reasoning, not just the answer.",
         "paste your task list into Claude...",
         "Run it on your own schedule")},
    37.0))

beats.append(beat(
    "T09", "OUTRO",
    "OUTRO LAW -- title restate; @HumanitariansAI card (house outro is @NikBearBrown-locked)",
    "The critical path -- map, find, protect. With Sanjana Rao, for Humanitarians AI. The "
    "AI finds the longest path. You keep it from getting longer. Thanks for watching.",
    {"type": "GRAPHIC", "source": "manim", "motion": "fade",
     "manim": manim("T09_Outro")},
    12.0))


sheet = {
    "metadata": {
        "title": "The Critical Path",
        "slug": "critical-path",
        "topic": TOPIC, "register": "Plain / Teardown-warm",
        "audience": "Humanitarians AI", "brand": "claude-hai",
        "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude",
        "style": "claude-explainer", "voice_kokoro": "af_bella",
        "voice_policy": "persistent-fellow-selected", "voice_approval": "APPROVED",
        "approvals": {"voice": {"status": "approved", "reviewer_type": "human",
                                "reviewed_by": "Sanjana Rao",
                                "reviewed_at": "2026-10-11T12:00:00+00:00",
                                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4"}},
        "aspect_ratio": "16:9",
        "note": "ai-explainer CONCEPT explainer (AI + Critical Path Method) for "
                "@HumanitariansAI, first-person Sanjana Rao (af_bella). Framework = "
                "MAP / FIND / PROTECT. Example network A-B-D-E=14 (critical) vs A-C-D-E=11 "
                "(C has 3 days slack); non-critical speed-up changes nothing; slack "
                "overrun shifts the path.",
        "tags": ["Humanitarians AI", "Sanjana Rao", "project management",
                 "critical path method", "CPM", "project scheduling", "slack float",
                 "when to use AI", "Claude", "STEM"],
        "total_estimated_duration_seconds": int(sum(b["estimated_duration_s"] for b in beats)),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2), encoding="utf-8")
print(f"wrote {out}  ({len(beats)} beats, est {sheet['metadata']['total_estimated_duration_seconds']}s)")
