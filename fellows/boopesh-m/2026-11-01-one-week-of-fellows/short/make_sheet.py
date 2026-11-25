# Writes beat_sheet.json (9:16, 2160x3840) for the Short of "One Week of Fellows" -- Boopesh M.
# A separate native-portrait reel, not a crop. Numbers from ../code/results.json.
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.loads((HERE.parent / "code" / "results.json").read_text())
assert R["merged_prs"]["total"] == 30 and R["merged_prs"]["per_day"]["2026-10-29"] == 12
assert R["contributors"]["distinct_people_after_obvious_dedupe"] == 27
assert R["folders"]["new_work_folders"] == 84 and R["folders"]["frictional_logs_added"] == 72
assert R["boopesh"]["folder_on_main"] is False

VOICE = "am_onyx"
HAI = "@HumanitariansAI"


def manim(cls):
    return {"type": "GRAPHIC", "source": "manim", "motion": "fade",
            "manim": {"scene_class": cls, "file": "scenes.py"}}


def beat(bid, act, note, text, shot, **kw):
    b = {"beat_id": bid, "act": act, "role_note": note, "narration_text": text,
         "shot": shot, "voice": VOICE, "engine": "kokoro", "voice_kokoro": VOICE}
    b.update(kw)
    return b


beats = [
  beat("B00", "INTRO", "required fellow intro line + AI-voice disclosure (portrait composer)",
       "Hi, I am Boopesh M., and this video is about one week of Humanitarians AI fellows, "
       "October twenty-fifth to the thirty-first. Heads up: this is an AI voice reading my script, "
       "and every number comes from the git history.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "ClaudeComposerAsk916", "props": {
            "greeting": "Hi, Boopesh", "topic": "Irreducibly Human", "segment": "One Week of Fellows",
            "command": "What did the fellows ship into humanitarians-youtube from Oct 25 to 31?",
            "runningText": "reading the git log…", "folderLabel": HAI,
            "modelLabel": "Claude", "effortLabel": "High",
            "output": ["30 pull requests · 27 people", "84 new work folders"]},
            "rendered": {"out": "", "at": ""}}}),
  beat("B10", "PRS", "merged PRs per day",
       "Thirty pull requests were merged in seven days. Thursday was the busiest, with twelve.",
       manim("B10_PerDay")),
  beat("B20", "NUMBERS", "people, folders, frictional logs",
       "Thirty-seven author names, but only twenty-seven people, once the obvious duplicates are merged. "
       "Together they added eighty-four new work folders, and seventy-two frictional logs.",
       manim("B20_Numbers")),
  beat("B30", "MY PART", "Boopesh's two videos; PR pending",
       "My part: two videos last week, Brutalist, Shared and Deep Hedging, each with a Short. "
       "They're on Drive. My GitHub pull request is still pending.",
       manim("B30_MyPart")),
  beat("B40", "TAKEAWAY", "small weekly evidence adds up",
       "The lesson: small weekly evidence adds up. A README, a fact check, a frictional log, and the source.",
       manim("B40_Takeaway")),
  beat("B90", "OUTRO", "HAI outro + fellow credit",
       "One week of fellows. With Boopesh M., for Humanitarians AI.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "One Week of Fellows (Short)",
    "slug": "one-week-of-fellows-short",
    "topic": "Irreducibly Human",
    "register": "Plain / Teardown-warm",
    "audience": "Humanitarians AI",
    "brand": "claude-hai",
    "channel_title": "",
    "creator": "Boopesh M.",
    "engine": "kokoro",
    "palette": "claude",
    "style_preset": "claude",
    "style": "claude-explainer",
    "voice_kokoro": VOICE,
    "voice_policy": "persistent-fellow-selected",
    "aspect_ratio": "9:16",
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ"},
    "brutalist_commit": "a99b5323",
    "parent": "../beat_sheet.json",
    "note": "Native 9:16 Short of 'One Week of Fellows'. Same facts (../FACTCHECK.md), own layout.",
    "tags": ["Humanitarians AI", "fellows", "git", "pull requests", "Shorts"],
  },
  "beats": beats,
}
out = HERE / "beat_sheet.json"
if out.exists():
    old = json.loads(out.read_text())
    for k in ("approvals", "build"):
        if k in old.get("metadata", {}):
            sheet["metadata"][k] = old["metadata"][k]
    prev = {b["beat_id"]: b for b in old.get("beats", [])}
    for b in beats:
        o = prev.get(b["beat_id"])
        if o and o.get("narration_text") == b["narration_text"]:
            for k in ("actual_duration_s", "audio_file", "render_duration_s", "build"):
                if k in o:
                    b[k] = o[k]
            if (o.get("shot", {}).get("remotion") or {}).get("rendered"):
                b["shot"]["remotion"]["rendered"] = o["shot"]["remotion"]["rendered"]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print("wrote", out, len(beats), "beats", sum(len(b["narration_text"].split()) for b in beats), "words")
