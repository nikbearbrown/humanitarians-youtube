# -*- coding: utf-8 -*-
"""Authoring script for the 9:16 SHORT of the Monte Carlo schedule-risk reel.
Single-cycle teaser that funnels to the 16:9 long. Portrait compositions only."""
import json, pathlib

TOPIC = "HUMANITARIANS AI · PROJECT MANAGEMENT"
SEG = "Monte Carlo Schedule Risk"
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
        "Hi, I'm Sanjana. Your project's deadline is really just a guess. Here's how to find "
        "the honest one in about a minute."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer916(
                  "Hi, Sanjana",
                  "Turn my project plan into a simulated finish date I can actually commit to.",
                  "simulating 10,000 schedules…",
                  ["a single date hides the risk",
                   "give each task a range, then simulate",
                   "commit to the P80"])},
     "estimated_duration_s": 10},

    {"beat_id": "S01", "act": "OUTPUT",
     "narration_text": (
        "Give every task a range instead of one number, and simulate the whole project ten "
        "thousand times. The truth appears. Your plan sits on the optimistic edge — and the "
        "date you can really commit to, the P80, is further out."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "S01_ShortHist", "file": "scenes_short.py"}},
     "estimated_duration_s": 13},

    {"beat_id": "S02", "act": "NEXT STEPS",
     "narration_text": (
        "Your turn. Paste your tasks and their three estimates into Claude, and ask for the "
        "P80. The full build — with the code — is on our channel."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer916(
                  "Your turn.",
                  "Here are my tasks with optimistic / likely / pessimistic estimates and their "
                  "dependencies. Run 10,000 Monte Carlo trials and give me the P80 finish date.",
                  "paste this into Claude…",
                  segment="Simulate your own deadline")},
     "estimated_duration_s": 12},

    {"beat_id": "S03", "act": "OUTRO",
     "narration_text": (
        "Monte Carlo schedule risk — with Sanjana Rao, at Humanitarians AI."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": {"pattern": "ClaudeTitleOutro916",
                           "props": {"title": "Monte Carlo Schedule Risk.",
                                     "handle": "@HumanitariansAI",
                                     "subline": "with Sanjana Rao · full build on the channel"},
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
        "title": "Monte Carlo Schedule Risk (Short)",
        "slug": "monte-carlo-schedule-risk-short",
        "topic": TOPIC, "register": "Teardown-warm", "audience": "Humanitarians AI",
        "brand": "claude-hai", "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude", "style": "claude-cli",
        "voice_kokoro": "af_bella", "voice_policy": "persistent-fellow-selected",
        "voice_approval": "APPROVED", "aspect_ratio": "9:16",
        "note": "9:16 Short teaser; funnels to the 16:9 long. Portrait compositions only.",
        "tags": ["project management", "Monte Carlo", "schedule risk", "P80",
                 "Humanitarians AI", "Sanjana Rao", "Shorts"],
        "total_estimated_duration_seconds": sum(b["estimated_duration_s"] for b in beats),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote", out, "with", len(beats), "beats")
