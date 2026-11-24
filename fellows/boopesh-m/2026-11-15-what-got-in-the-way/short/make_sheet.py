# Writes beat_sheet.json (9:16, 2160x3840) for the Short of "What Got in the Way" -- Boopesh M.
# A separate native-portrait reel, not a crop. Numbers from ../code/results.json.
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.loads((HERE.parent / "code" / "results.json").read_text())
FR = R["friction"]
assert (FR["logs_describing_obstacles"], FR["found_by_looking_logs"]) == (31, 17)
assert list(FR["theme_logs"].items())[:4] == [("layout & picture checks", 19), ("facts & data", 11),
                                              ("length & time", 10), ("tools & setup", 10)]
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
       "Hi, I am Boopesh M., and this video is about what got in the way for the Humanitarians AI fellows this week, "
       "November eighth to the fourteenth. Heads up: this is an AI voice reading my script, "
       "and every number comes from the fellows' own logs.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "ClaudeComposerAsk916", "props": {
            "greeting": "Hi, Boopesh", "topic": "Irreducibly Human", "segment": "What Got in the Way",
            "command": "What got in the way for the fellows, Nov 8 to 14?",
            "runningText": "reading the frictional logs…", "folderLabel": HAI,
            "modelLabel": "Claude", "effortLabel": "High",
            "output": ["31 logs describe obstacles", "top: layout & picture checks"]},
            "rendered": {"out": "", "at": ""}}}),
  beat("B10", "THEMES", "top themes of the 31 logs with obstacles (rough keyword sort)",
       "Thirty-one frictional logs describe obstacles. By my rough sort, layout and picture checks came first, "
       "in nineteen. Then facts and data, eleven, and length and time, and tools and setup, ten each.",
       manim("B10_Themes")),
  beat("B20", "WHAT FIXED IT", "17 of 31 logs found a problem by looking",
       "What fixed them? Most often, someone looked. In seventeen of the thirty-one logs, a problem was found "
       "by watching the cut, viewing the frames, or re-reading the words.",
       manim("B20_Looked")),
  beat("B30", "MY PART", "Boopesh's two videos last week; delivered for review; his obstacle: access, PR pending",
       "My part: two videos last week, What the Fellows Taught and The Backtest Mirage, each with a Short, "
       "delivered for review. My own obstacle is access: my pull request is still pending.",
       manim("B30_MyPart")),
  beat("B90", "OUTRO", "HAI outro + fellow credit",
       "What got in the way. With Boopesh M., for Humanitarians AI.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "What Got in the Way (Short)",
    "slug": "what-got-in-the-way-short",
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
    "note": "Native 9:16 Short of 'What Got in the Way'. Same facts (../FACTCHECK.md), own layout.",
    "tags": ["Humanitarians AI", "fellows", "frictional log", "what got in the way", "Shorts"],
    "approvals": {"voice": {"status": "approved", "reviewer_type": "human", "reviewed_by": "Boopesh M.",
                            "reviewed_at": "2026-10-24T22:00:00+00:00",
                            "subject_sha256": "9fbee75cc6f2e9898f416028987763bde5975fea9179425289a870171991c85e",
                            "note": "Fellow's own words in chat, 2026-10-24: 'I approve am_onyx as my narrator "
                                    "voice.' Same voice subject fingerprint as his approved 2026-10-24, 2026-11-01 "
                                    "and 2026-11-08 reels."}},
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
