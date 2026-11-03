# -*- coding: utf-8 -*-
"""Authoring script for the 9:16 SHORT of the Two-Week Progress Review reel.
Single-cycle teaser -> funnels to the 16:9 long. SAME Claude intro/outro."""
import json, pathlib

TOPIC = "HUMANITARIANS AI | PROJECT MANAGEMENT"
SEG = "Two-Week Progress Review"
FOLDER = "@HumanitariansAI"

def composer916(greeting, command, runningText, output=None, segment=SEG):
    return {"pattern": "ClaudeComposerAsk916",
            "props": {"greeting": greeting, "topic": TOPIC, "segment": segment,
                      "command": command, "runningText": runningText,
                      "folderLabel": FOLDER, "modelLabel": "Claude",
                      "effortLabel": "High", "output": output or []},
            "rendered": {"out": "", "at": ""}}

beats = [
    {"beat_id": "S00", "act": "INTRO",
     "narration_text": (
        "Hi, I'm Sanjana. Here's my two-week progress at Humanitarians AI, turned into a "
        "dashboard a stakeholder can read in thirty seconds."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer916(
                  "Hi, Sanjana",
                  "Turn my two-week video-review tracker into a clear stakeholder dashboard.",
                  "reading the tracker...",
                  ["172 videos reviewed in two weeks",
                   "119 sent up for the Professors",
                   "one week Mycroft, the next other projects"])},
     "estimated_duration_s": 11},

    {"beat_id": "S01", "act": "OUTPUT",
     "narration_text": (
        "In the past two weeks I reviewed one hundred seventy-two videos from thirty-eight "
        "fellows. One hundred nineteen went up for approval, and fifty came back with specific "
        "changes. And the rhythm held: week one the other projects, eighty-seven videos; week "
        "two Mycroft, eighty-five. Steady and alternating."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "S01_ShortDash", "file": "scenes_short.py"}},
     "estimated_duration_s": 16},

    {"beat_id": "S02", "act": "NEXT STEPS",
     "narration_text": (
        "Your turn. If you keep a review tracker, paste it into Claude and ask for the totals, "
        "the split by week, and three sentences for a stakeholder update. The full build is on "
        "our channel."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer916(
                  "Your turn.",
                  "Here's my review tracker for the last two weeks. Give me total reviewed, "
                  "uploaded, and changes requested, split by week and project.",
                  "paste your tracker into Claude...",
                  segment="Turn your tracker into a dashboard")},
     "estimated_duration_s": 13},

    {"beat_id": "S03", "act": "OUTRO",
     "narration_text": (
        "Two-week progress review - with Sanjana Rao, at Humanitarians AI."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": {"pattern": "ClaudeTitleOutro916",
                           "props": {"title": "Two-Week Progress Review.",
                                     "handle": "@HumanitariansAI",
                                     "subline": "with Sanjana Rao | full report on the channel"},
                           "rendered": {"out": "", "at": ""}}},
     "estimated_duration_s": 6},
]

for b in beats:
    b.setdefault("voice", "af_bella")
    b["engine"] = "kokoro"
    b["voice_kokoro"] = "af_bella"
    b.setdefault("build", {"status": "SLATE"})

sheet = {
    "metadata": {
        "title": "Two-Week Progress Review (Short)",
        "slug": "sept-progress-review-short",
        "topic": TOPIC, "register": "Teardown-warm", "audience": "Humanitarians AI",
        "brand": "claude-hai", "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude", "style": "claude-cli",
        "voice_kokoro": "af_bella", "voice_policy": "persistent-fellow-selected",
        "voice_approval": "APPROVED", "aspect_ratio": "9:16",
        "note": "9:16 Short teaser; funnels to the 16:9 long. SAME Claude intro/outro.",
        "tags": ["project management", "progress report", "video review", "Humanitarians AI",
                 "Mycroft", "dashboard", "Sanjana Rao", "Shorts"],
        "total_estimated_duration_seconds": sum(b["estimated_duration_s"] for b in beats),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote", out, "with", len(beats), "beats")
