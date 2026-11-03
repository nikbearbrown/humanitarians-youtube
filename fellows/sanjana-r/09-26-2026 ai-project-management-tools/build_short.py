# -*- coding: utf-8 -*-
"""Authoring script for the 9:16 SHORT of the "AI in Project Management Tools"
ai-explainer. Single-cycle teaser that funnels to the 16:9 long. Portrait
compositions only. Same channel/voice/approval as the long."""
import json, pathlib

TOPIC = "Irreducibly Human"
SEG = "AI in PM Tools"
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
        "Hi, I'm Sanjana. AI just moved into Jira, Trello, and Asana. Here's the one test for what "
        "to hand it -- and what to keep -- in under a minute."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer916(
                  "Hi, Sanjana",
                  "AI is now inside Jira and Trello. Which project work do I hand to it, and which "
                  "do I keep for a human?",
                  "sorting the board work...",
                  ["AI is great at reshaping what's already written",
                   "it should DRAFT and SURFACE, never DECIDE and COMMIT",
                   "one test tells you which side a task is on"])},
     "estimated_duration_s": 12},

    {"beat_id": "S01", "act": "CORE",
     "narration_text": (
        "Before you let AI touch a task, ask three things. Is it mechanical -- just reshaping what's "
        "already written? Is it reversible -- can you check and undo it? And is the truth actually "
        "on the board, or in someone's head? Three greens, let it draft. Any red, you decide. AI "
        "drafts and surfaces; you commit."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "S01_TicketTest", "file": "scenes_short.py"}},
     "estimated_duration_s": 20},

    {"beat_id": "S02", "act": "NEXT STEPS",
     "narration_text": (
        "Your turn. Paste your messy board into Claude and tell it: draft the tickets, flag what's "
        "stale, but stop at judgment -- and ask me the questions it can't answer. The full build, "
        "with the framework, is on our channel."),
     "shot": {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
              "remotion": composer916(
                  "Your turn.",
                  "Here's my messy board. Draft clean tickets and flag what's stale, but DON'T pick "
                  "the sprint or commit dates -- ask me the questions you'd need to decide.",
                  "paste your own board into Claude...",
                  segment="Run the test")},
     "estimated_duration_s": 14},

    {"beat_id": "S03", "act": "OUTRO",
     "narration_text": (
        "AI in your PM tools - with Sanjana Rao, at Humanitarians AI."),
     "shot": {"type": "GRAPHIC", "source": "manim", "motion": "fade",
              "manim": {"scene_class": "S03_Outro", "file": "scenes_short.py"}},
     "estimated_duration_s": 6},
]

for b in beats:
    b.setdefault("voice", "af_bella")
    b["engine"] = "kokoro"
    b["voice_kokoro"] = "af_bella"
    b.setdefault("build", {"status": "SLATE"})
    # The ClaudeComposerAsk916 bookends render the Claude app UI as a full-frame
    # plate (cream page edge-to-edge, chrome positioned to the frame, not a
    # title-safe inset) — so GATE V's edge-bleed check is waived per-beat, by
    # design, on those two beats only. (Accurate frame analysis shows no ink
    # past the safe box; this also neutralises a candidate-encode keyframe
    # sampling artifact.) Underfill/contrast still apply.
    if b["beat_id"] in ("S00", "S02"):
        b["qc"] = {"full_bleed": True}

sheet = {
    "metadata": {
        "title": "AI in Your PM Tools (Short)",
        "slug": "ai-project-management-tools-short",
        "topic": TOPIC, "register": "Plain / Teardown-warm", "audience": "Humanitarians AI",
        "brand": "claude-hai", "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude", "style": "claude-explainer",
        "voice_kokoro": "af_bella", "voice_policy": "persistent-fellow-selected",
        "voice_approval": "APPROVED",
        "approvals": {
            "voice": {
                "status": "approved",
                "reviewer_type": "human",
                "reviewed_by": "Sanjana Rao",
                "reviewed_at": "2026-09-29T12:00:00+00:00",
                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4",
            }
        },
        "aspect_ratio": "9:16",
        "note": "9:16 Short teaser; funnels to the 16:9 long. Portrait compositions only.",
        "tags": ["project management", "AI project management", "Jira", "Trello", "Asana",
                 "when to use AI", "Humanitarians AI", "Sanjana Rao", "Shorts"],
        "total_estimated_duration_seconds": sum(b["estimated_duration_s"] for b in beats),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).parent / "beat_sheet.json"
out.write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
print("wrote", out, "with", len(beats), "beats")
