# -*- coding: utf-8 -*-
"""Authoring script for "The Review Gate" SHORT (9:16, ~50s).
A dedicated portrait beat sheet (NOT a crop of the 16:9): 4 beats --
  S00 INTRO    ClaudeComposerAsk916  -- first-person Sanjana, the hook
  S01 CORE     Manim portrait        -- the 3-check gate + the two-week numbers
  S02 HANDOFF  ClaudeComposerAsk916  -- 'Your turn.' prompt, read aloud
  S03 OUTRO    Manim portrait        -- custom @HumanitariansAI card
af_bella voice, @HumanitariansAI, Claude skin. All numbers verified from tracker.
"""
import json, pathlib

TOPIC = "Irreducibly Human"
SEG = "The Review Gate"
FOLDER = "@HumanitariansAI"


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
    beat("S00", "INTRO", "COLD OPEN -- ClaudeComposerAsk916, first-person Sanjana",
         "Hi, I'm Sanjana. In the last two weeks of September, I reviewed "
         "eighty-eight fellow videos at Humanitarians AI. Here's the gate I run "
         "on every single one.",
         {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
          "remotion": composer(
              "Hi, Sanjana",
              "Two weeks of fellow-video reviews -- show how I check every one "
              "before it's approved.",
              "opening the gate...", "The Review Gate",
              ["88 reviewed in two weeks", "a 3-check gate on each",
               "78 approved, 10 sent back"])},
         9.5, {"qc": {"full_bleed": True}}),  # composer916 brand rule sits low by design
    beat("S01", "CORE", "the framework + the numbers, compressed",
         "Before any video is approved, it clears three checks. Rendered in true "
         "4K, both cuts? Branding on the Humanitarians AI handle? Code on GitHub? "
         "Three passes, it goes to the professor. Any fail, it goes back with "
         "notes. Two weeks: eighty-eight reviewed, seventy-eight approved, "
         "seventy-one already on GitHub.",
         {"type": "GRAPHIC", "source": "manim", "motion": "fade",
          "visual_intent": "Portrait: eyebrow THE REVIEW GATE, title '3 checks "
          "before approve', three rows 4K ON BOTH CUTS? / RIGHT BRANDING? / CODE "
          "ON GITHUB? each PASS/FAIL, then a numbers block 88 reviewed / 78 "
          "approved / 71 on GitHub, punch line.",
          "manim": {"scene_class": "S01_Gate", "file": "scenes_short.py"}},
         20.0),
    beat("S02", "NEXT STEPS", "HANDOFF -- ClaudeComposerAsk916 'Your turn.'",
         "Your turn. Don't eyeball your reviews -- build a gate. Paste your log "
         "into Claude and have it turn your reasons for sending work back into a "
         "three-check gate you run every time.",
         {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
          "remotion": composer(
              "Your turn.",
              "Here's a log of work I review [PASTE]. Turn the reasons I send "
              "things back into a 3-check gate -- each with a pass test and a "
              "fail action -- that I can run on every item the same way.",
              "paste your log into Claude...", "Build your own gate")},
         13.0),
    beat("S03", "OUTRO", "OUTRO -- custom @HumanitariansAI portrait card",
         "The Review Gate -- two weeks at Humanitarians AI, with Sanjana Rao.",
         {"type": "GRAPHIC", "source": "manim", "motion": "fade",
          "manim": {"scene_class": "S03_Outro", "file": "scenes_short.py"}},
         5.0),
]

sheet = {
    "metadata": {
        "title": "The Review Gate (Short)", "slug": "the-review-gate-short",
        "topic": TOPIC, "register": "Plain / Teardown-warm",
        "audience": "Humanitarians AI", "brand": "claude-hai",
        "channel_title": "@HumanitariansAI", "creator": "Sanjana Rao",
        "engine": "kokoro", "palette": "claude", "style_preset": "claude",
        "style": "claude-explainer", "voice_kokoro": "af_bella",
        "voice_policy": "persistent-fellow-selected", "voice_approval": "APPROVED",
        "approvals": {"voice": {"status": "approved", "reviewer_type": "human",
                                "reviewed_by": "Sanjana Rao",
                                "reviewed_at": "2026-10-08T12:00:00+00:00",
                                "subject_sha256": "d3486a7ac5d092a1899e7d5610728c96d03bf769ed2c423635e04dbd98e04bf4"}},
        "aspect_ratio": "9:16",
        "note": "9:16 SHORT of The Review Gate (dedicated beat sheet, not a crop). "
                "af_bella, @HumanitariansAI, first-person Sanjana. Numbers verified "
                "from the Sep 16-30 review tracker.",
        "tags": ["Humanitarians AI", "Sanjana Rao", "progress", "video review",
                 "quality gate", "Shorts", "Claude"],
        "total_estimated_duration_seconds": int(sum(b["estimated_duration_s"] for b in beats)),
    },
    "beats": beats,
}
out = pathlib.Path(__file__).resolve().parent / "beat_sheet_short.json"
out.write_text(json.dumps(sheet, indent=2), encoding="utf-8")
print(f"wrote {out}  ({len(beats)} beats, est {sheet['metadata']['total_estimated_duration_seconds']}s)")
