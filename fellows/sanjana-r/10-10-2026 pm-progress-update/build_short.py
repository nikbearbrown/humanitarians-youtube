# -*- coding: utf-8 -*-
"""Authoring script for "The Last Mile" SHORT (9:16, ~46s).
Dedicated portrait beat sheet (NOT a crop). Emits beat_sheet.json directly (audio +
compile read that name). 4 beats: S00 hook / S01 framework / S02 handoff / S03 outro.
af_bella, @HumanitariansAI, first-person Sanjana. Progress record, week of Oct 4-10.
"""
import json, pathlib
TOPIC, SEG, FOLDER = "Irreducibly Human", "The Last Mile", "@HumanitariansAI"


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
         "Hi, I'm Sanjana. This week I reviewed eighty-five fellow videos for the "
         "Mycroft project -- and only two came back. Not for their content. For the "
         "last mile.",
         {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
          "remotion": composer("Hi, Sanjana",
              "I reviewed 85 fellow videos this week. Almost all passed. So what sends "
              "a finished video back?",
              "reviewing the queue...", "The Last Mile",
              ["code + branding -- automatic now", "what's left is the last mile",
               "2 went back: a footer, a broken 9:16"])},
         10.0, {"qc": {"full_bleed": True}}),
    beat("S01", "CORE", "framework compressed",
         "A finished video isn't a shipped one. Before it goes to the professors, I "
         "check the last mile -- three things. Clean finish: no stray toolkit footer "
         "baked in. Portrait holds: the nine-by-sixteen is its own layout, no "
         "overlapping text. On GitHub: code and assets pushed. Three pass, it ships. "
         "Any fail, it goes back with a mail.",
         {"type": "GRAPHIC", "source": "manim", "motion": "fade",
          "visual_intent": "Portrait: title 'Done isn't shipped.', three checks CLEAN "
          "FINISH / PORTRAIT HOLDS / ON GITHUB each with a one-line test, rule line, punch.",
          "manim": {"scene_class": "S01_LastMile", "file": "scenes_short.py"}},
         20.0),
    beat("S02", "NEXT STEPS", "HANDOFF -- ClaudeComposerAsk916 'Your turn.'",
         "Your turn. Before you submit, run your own last mile -- scan the final "
         "seconds for a stray footer, open the nine-by-sixteen on a phone and read it "
         "for overlapping text, and confirm your code is pushed.",
         {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
          "remotion": composer("Your turn.",
              "Build me a 2-minute pre-submission checklist for my video: scan the last "
              "10s for a stray footer, check the 9:16 on a phone for overlapping text, "
              "confirm code + assets are pushed.",
              "build my checklist...", "Run it before you submit")},
         12.0),
    beat("S03", "OUTRO", "OUTRO -- custom @HumanitariansAI portrait card",
         "The last mile -- the check between finished and shipped. With Sanjana Rao, at "
         "Humanitarians AI.",
         {"type": "GRAPHIC", "source": "manim", "motion": "fade",
          "manim": {"scene_class": "S03_Outro", "file": "scenes_short.py"}},
         5.0),
]

sheet = {
    "metadata": {
        "title": "The Last Mile (Short)", "slug": "the-last-mile-short",
        "topic": TOPIC, "register": "Plain / Teardown-warm", "audience": "Humanitarians AI",
        "brand": "claude-hai", "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude",
        "style": "claude-explainer", "voice_kokoro": "af_bella",
        "voice_policy": "persistent-fellow-selected", "voice_approval": "APPROVED",
        "approvals": {"voice": {"status": "approved", "reviewer_type": "human",
                                "reviewed_by": "Sanjana Rao", "reviewed_at": "2026-10-11T12:00:00+00:00",
                                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4"}},
        "aspect_ratio": "9:16",
        "note": "9:16 SHORT of The Last Mile (dedicated sheet). af_bella, @HumanitariansAI. Progress record, week of Oct 4-10.",
        "tags": ["Humanitarians AI", "Sanjana Rao", "video review", "quality control", "Mycroft", "Shorts", "Claude"],
        "total_estimated_duration_seconds": int(sum(b["estimated_duration_s"] for b in beats)),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).resolve().parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=2), encoding="utf-8")
print(f"wrote {out} ({len(beats)} beats, est {sheet['metadata']['total_estimated_duration_seconds']}s)")
