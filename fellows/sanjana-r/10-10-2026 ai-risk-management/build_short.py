# -*- coding: utf-8 -*-
"""Authoring script for "The Risk Register" SHORT (9:16, ~48s).
Dedicated portrait beat sheet (NOT a crop). 4 beats: S00 hook / S01 framework /
S02 handoff / S03 outro. af_bella, @HumanitariansAI, first-person Sanjana.
"""
import json, pathlib
TOPIC, SEG, FOLDER = "Irreducibly Human", "The Risk Register", "@HumanitariansAI"


def composer(greeting, command, runningText, segment, output=None):
    return {"pattern": "ClaudeComposerAsk916",
            "props": {"greeting": greeting, "topic": TOPIC, "segment": segment,
                      "command": command, "runningText": runningText,
                      "folderLabel": FOLDER, "modelLabel": "Claude",
                      "effortLabel": "High", "output": output or []},
            "rendered": {"out": "", "at": ""}}


def beat(bid, act, role, narration, shot, est, extra=None):
    b = {"beat_id": bid, "act": act, "role_note": role, "narration_text": narration,
         "shot": shot, "estimated_duration_s": est, "voice": "af_bella",
         "engine": "kokoro", "voice_kokoro": "af_bella"}
    if extra:
        b.update(extra)
    return b


beats = [
    beat("S00", "INTRO", "COLD OPEN -- ClaudeComposerAsk916",
         "Hi, I'm Sanjana. AI will now build your whole risk register in one prompt. "
         "It's great at the known risks -- but the one that sinks you is usually off the "
         "grid.",
         {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
          "remotion": composer("Hi, Sanjana",
              "AI can auto-build and score my risk register. Can I trust it to catch the "
              "risk that actually matters?",
              "building the register...", "The Risk Register",
              ["AI scores the KNOWN risks fast", "but it only sees template risks",
               "the one that sinks you is project-specific"])},
         10.5, {"qc": {"full_bleed": True}}),
    beat("S01", "CORE", "framework compressed",
         "An AI risk register is a draft of the known risks -- you own the rest. Three "
         "steps. Score: let the AI rate the common risks, fast. Own: add the "
         "project-specific risk it can't see -- your team, your vendor, your timeline. "
         "Watch: give every real risk a trigger and an owner. A register nobody watches "
         "is just a list.",
         {"type": "GRAPHIC", "source": "manim", "motion": "fade",
          "visual_intent": "Portrait: title 'Score. Own. Watch.', three steps SCORE / OWN "
          "/ WATCH each with a one-line test, rule line, punch.",
          "manim": {"scene_class": "S01_ScoreOwnWatch", "file": "scenes_short.py"}},
         21.0),
    beat("S02", "NEXT STEPS", "HANDOFF -- ClaudeComposerAsk916 'Your turn.'",
         "Your turn. Have the AI score the risks it can justify, and separately list what "
         "it could not assess without knowing your project. That second list is your map "
         "of blind spots.",
         {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
          "remotion": composer("Your turn.",
              "Score the risks you can justify from my plan (probability x impact), and "
              "separately list every assumption + what you canNOT assess without my team, "
              "vendors, and timeline.",
              "paste your plan into Claude...", "Run it on your project")},
         12.0),
    beat("S03", "OUTRO", "OUTRO -- custom @HumanitariansAI portrait card",
         "The risk register -- score, own, watch. With Sanjana Rao, at Humanitarians AI.",
         {"type": "GRAPHIC", "source": "manim", "motion": "fade",
          "manim": {"scene_class": "S03_Outro", "file": "scenes_short.py"}},
         5.0),
]

sheet = {
    "metadata": {
        "title": "The Risk Register (Short)", "slug": "ai-risk-management-short",
        "topic": TOPIC, "register": "Plain / Teardown-warm", "audience": "Humanitarians AI",
        "brand": "claude-hai", "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude",
        "style": "claude-explainer", "voice_kokoro": "af_bella",
        "voice_policy": "persistent-fellow-selected", "voice_approval": "APPROVED",
        "approvals": {"voice": {"status": "approved", "reviewer_type": "human",
                                "reviewed_by": "Sanjana Rao", "reviewed_at": "2026-10-11T12:00:00+00:00",
                                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4"}},
        "aspect_ratio": "9:16",
        "note": "9:16 SHORT of The Risk Register (dedicated sheet). af_bella, @HumanitariansAI.",
        "tags": ["Humanitarians AI", "Sanjana Rao", "risk management", "project management", "Shorts", "Claude"],
        "total_estimated_duration_seconds": int(sum(b["estimated_duration_s"] for b in beats)),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2), encoding="utf-8")
print(f"wrote {out} ({len(beats)} beats, est {sheet['metadata']['total_estimated_duration_seconds']}s)")
