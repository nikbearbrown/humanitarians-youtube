# -*- coding: utf-8 -*-
"""Authoring script for the 9:16 SHORT of the AI Effort Estimation reel.
Single-cycle teaser that funnels to the 16:9 long. Portrait compositions only."""
import json, pathlib

TOPIC = "HUMANITARIANS AI | PROJECT MANAGEMENT"
SEG = "AI Effort Estimation"
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
        "Hi, I'm Sanjana. Your task estimates are probably too optimistic. Here's how to fix "
        "that in about a minute, using AI and your own history."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer916(
                  "Hi, Sanjana",
                  "Don't guess how long each task takes. Match it to similar work we've finished "
                  "and give me an honest range.",
                  "matching tasks to your history...",
                  ["a gut estimate is almost always optimistic",
                   "match each task to work you've actually finished",
                   "report a range, not one number"])},
     "estimated_duration_s": 11},

    {"beat_id": "S01", "act": "OUTPUT",
     "narration_text": (
        "Instead of one gut number per task, match each to similar work you've actually "
        "finished, and read what it really took. Watch what happens: every guess sits on the "
        "optimistic edge, and the honest sprint jumps from ten days to about nineteen."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "S01_ShortRanges", "file": "scenes_short.py"}},
     "estimated_duration_s": 15},

    {"beat_id": "S02", "act": "NEXT STEPS",
     "narration_text": (
        "Your turn. Paste your backlog and your last dozen finished tasks with their real "
        "durations into Claude, and ask for ranges, not numbers. The full build, with the code, "
        "is on our channel."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer916(
                  "Your turn.",
                  "Here's my backlog and my last 15 completed tasks with the days each actually "
                  "took. Group them into classes, match each new task, and give me a P50-P80 range.",
                  "paste this into Claude...",
                  segment="Estimate your own backlog")},
     "estimated_duration_s": 13},

    {"beat_id": "S03", "act": "OUTRO",
     "narration_text": (
        "AI effort estimation - with Sanjana Rao, at Humanitarians AI."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": {"pattern": "ClaudeTitleOutro916",
                           "props": {"title": "AI Effort Estimation.",
                                     "handle": "@HumanitariansAI",
                                     "subline": "with Sanjana Rao | full build on the channel"},
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
        "title": "AI Effort Estimation (Short)",
        "slug": "ai-effort-estimation-short",
        "topic": TOPIC, "register": "Teardown-warm", "audience": "Humanitarians AI",
        "brand": "claude-hai", "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude", "style": "claude-cli",
        "voice_kokoro": "af_bella", "voice_policy": "persistent-fellow-selected",
        "voice_approval": "APPROVED", "aspect_ratio": "9:16",
        "note": "9:16 Short teaser; funnels to the 16:9 long. Portrait compositions only.",
        "tags": ["project management", "effort estimation", "reference-class forecasting",
                 "planning fallacy", "Humanitarians AI", "Sanjana Rao", "Shorts"],
        "total_estimated_duration_seconds": sum(b["estimated_duration_s"] for b in beats),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote", out, "with", len(beats), "beats")
