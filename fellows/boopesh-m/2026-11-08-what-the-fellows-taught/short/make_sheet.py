# Writes beat_sheet.json (9:16, 2160x3840) for the Short of "What the Fellows Taught" -- Boopesh M.
# A separate native-portrait reel, not a crop. Numbers from ../code/results.json.
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.loads((HERE.parent / "code" / "results.json").read_text())
F, CMP = R["this_week"]["folders"], R["comparison"]
assert F["new_work_folders"] == 74 and F["kinds"]["STEM / explainer video"] == 50
assert list(F["stem_subjects"])[:3] == ["AI for product managers", "testing & metrics", "how AI models work"]
assert (CMP["new_work_folders"]["last_week"], CMP["new_work_folders"]["this_week"]) == (84, 74)
assert (CMP["frictional_logs_added"]["last_week"], CMP["frictional_logs_added"]["this_week"]) == (72, 95)
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
       "Hi, I am Boopesh M., and this video is about what the Humanitarians AI fellows taught this week, "
       "November first to the seventh. Heads up: this is an AI voice reading my script, "
       "and every number comes from the git history.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "ClaudeComposerAsk916", "props": {
            "greeting": "Hi, Boopesh", "topic": "Irreducibly Human", "segment": "What the Fellows Taught",
            "command": "What did the fellows teach in their new folders, Nov 1 to 7?",
            "runningText": "reading the git log…", "folderLabel": HAI,
            "modelLabel": "Claude", "effortLabel": "High",
            "output": ["74 new work folders", "50 teach a topic"]},
            "rendered": {"out": "", "at": ""}}}),
  beat("B10", "SUBJECTS", "50 of 74 folders teach; top three subjects",
       "Seventy-four new work folders landed, and fifty of them teach a topic. "
       "The top subjects: AI for product managers, testing and metrics, and how AI models work.",
       manim("B10_Subjects")),
  beat("B20", "COMPARE", "one comparison with last week",
       "Compared with last week: fewer new folders, seventy-four instead of eighty-four, "
       "but more frictional logs, ninety-five instead of seventy-two.",
       manim("B20_Compare")),
  beat("B30", "MY PART", "Boopesh's two videos last week; delivered for review; PR pending",
       "My part: two videos last week, One Week of Fellows and The Accuracy Trap, each with a Short, "
       "delivered for review. My GitHub pull request is still pending.",
       manim("B30_MyPart")),
  beat("B40", "TAKEAWAY", "teach one idea",
       "The lesson: teach one idea from your week. One worked example, and where it breaks.",
       manim("B40_Takeaway")),
  beat("B90", "OUTRO", "HAI outro + fellow credit",
       "What the fellows taught. With Boopesh M., for Humanitarians AI.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "What the Fellows Taught (Short)",
    "slug": "what-the-fellows-taught-short",
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
    "note": "Native 9:16 Short of 'What the Fellows Taught'. Same facts (../FACTCHECK.md), own layout.",
    "tags": ["Humanitarians AI", "fellows", "STEM explainers", "teaching", "Shorts"],
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
            if (o.get("shot", {}).get("remotion") or {}).get("rendered") and \
                    o["shot"]["remotion"].get("props") == b["shot"]["remotion"].get("props"):
                b["shot"]["remotion"]["rendered"] = o["shot"]["remotion"]["rendered"]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print("wrote", out, len(beats), "beats", sum(len(b["narration_text"].split()) for b in beats), "words")
