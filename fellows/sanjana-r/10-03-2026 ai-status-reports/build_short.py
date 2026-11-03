# -*- coding: utf-8 -*-
"""Authoring script for "AI Status Reports" SHORT (9:16, ~48s).
Dedicated portrait beat sheet (NOT a crop). Emits beat_sheet.json directly (audio +
compile read that name). 4 beats: S00 hook / S01 framework / S02 handoff / S03 outro.
af_bella, @HumanitariansAI, first-person Sanjana.
"""
import json, pathlib
TOPIC, SEG, FOLDER = "Irreducibly Human", "AI Status Reports", "@HumanitariansAI"


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
         "Hi, I'm Sanjana. Your project tools will now write your status report for "
         "you. Here's how to know you can trust it before you send it.",
         {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
          "remotion": composer("Hi, Sanjana",
              "The AI can auto-write my project status. How do I trust it before I "
              "send it to a stakeholder?",
              "drafting the status...", "AI Status Reports",
              ["AI drafts the status fast", "but it's only as true as the board",
               "verify 3 things before you sign"])},
         9.5, {"qc": {"full_bleed": True}}),
    beat("S01", "CORE", "framework compressed",
         "The AI drafts the status -- but you sign it. Before it goes to anyone, "
         "check three things. Sourced: does every claim point to a real ticket, not "
         "confident filler? Current: is the board actually up to date? Complete: did "
         "you add the risk the AI can't see? All three, send it. Any gap, fix it "
         "first.",
         {"type": "GRAPHIC", "source": "manim", "motion": "fade",
          "visual_intent": "Portrait: title 'AI drafts it. You sign it.', three "
          "checks SOURCED/CURRENT/COMPLETE with a one-word test each, rule line, punch.",
          "manim": {"scene_class": "S01_SignOff", "file": "scenes_short.py"}},
         20.0),
    beat("S02", "NEXT STEPS", "HANDOFF -- ClaudeComposerAsk916 'Your turn.'",
         "Your turn. Have the AI draft your status, but make it tag every claim with "
         "its source and list what it couldn't verify. That list is your checklist "
         "before you hit send.",
         {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
          "remotion": composer("Your turn.",
              "Draft my status from the board. Tag every claim with its ticket/date, "
              "and separately list what you canNOT verify. Don't declare on-track "
              "yourself.",
              "paste your board into Claude...", "Run it on your status")},
         12.0),
    beat("S03", "OUTRO", "OUTRO -- custom @HumanitariansAI portrait card",
         "AI status reports -- trust, but verify. With Sanjana Rao, at Humanitarians AI.",
         {"type": "GRAPHIC", "source": "manim", "motion": "fade",
          "manim": {"scene_class": "S03_Outro", "file": "scenes_short.py"}},
         5.0),
]

sheet = {
    "metadata": {
        "title": "AI Status Reports (Short)", "slug": "ai-status-reports-short",
        "topic": TOPIC, "register": "Plain / Teardown-warm", "audience": "Humanitarians AI",
        "brand": "claude-hai", "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude",
        "style": "claude-explainer", "voice_kokoro": "af_bella",
        "voice_policy": "persistent-fellow-selected", "voice_approval": "APPROVED",
        "approvals": {"voice": {"status": "approved", "reviewer_type": "human",
                                "reviewed_by": "Sanjana Rao", "reviewed_at": "2026-10-08T12:00:00+00:00",
                                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4"}},
        "aspect_ratio": "9:16",
        "note": "9:16 SHORT of AI Status Reports (dedicated sheet). af_bella, @HumanitariansAI.",
        "tags": ["Humanitarians AI", "Sanjana Rao", "AI status report", "project management", "Shorts", "Claude"],
        "total_estimated_duration_seconds": int(sum(b["estimated_duration_s"] for b in beats)),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2), encoding="utf-8")
print(f"wrote {out} ({len(beats)} beats, est {sheet['metadata']['total_estimated_duration_seconds']}s)")
