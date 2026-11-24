# Writes beat_sheet.json (9:16, 2160x3840) for the Short of "Brutalist, Shared" -- Boopesh M.
# A separate native-portrait reel, not a crop of the landscape master.
import json
from pathlib import Path

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
       "Hi, I am Boopesh M., and this video is about the biggest week the Brutalist toolkit has had. "
       "Heads up: this is an AI voice reading my script.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "ClaudeComposerAsk916", "props": {
            "greeting": "Hi, Boopesh", "topic": "Irreducibly Human", "segment": "Brutalist, Shared",
            "command": "What changed in the Brutalist toolkit this week?",
            "runningText": "reading the commit history…", "folderLabel": HAI,
            "modelLabel": "Claude", "effortLabel": "High",
            "output": ["first three pull requests ever merged", "plus three Blender skills"]},
            "rendered": {"out": "", "at": ""}}}),
  beat("B10", "MERGES", "the three merges, timestamps from git",
       "On October twenty-third, Brutalist merged the first three pull requests in its history. "
       "All three within seven seconds.",
       manim("B10_Merges")),
  beat("B20", "WHAT", "one card per pull request; the thumbnail card shows real output",
       "A thumbnail generator, with real 4K output. Setup fixes, so a fresh install just works. "
       "And a speaker-series engine for hour-long talks.",
       manim("B20_ThreePRs")),
  beat("B30", "3D", "Blender skills",
       "Plus three new Blender skills that take the toolkit into 3D.",
       manim("B30_Blender")),
  beat("B40", "TAKEAWAY", "dark statement card",
       "The lesson: you don't need to be the maintainer to improve your tools. "
       "Fix what's in your way, and open a pull request.",
       manim("B40_Takeaway")),
  beat("B90", "OUTRO", "HAI outro + fellow credit",
       "Brutalist, Shared. With Boopesh M., for Humanitarians AI.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "Brutalist, Shared (Short)",
    "slug": "brutalist-shared-short",
    "topic": "Irreducibly Human",
    "register": "Plain / Teardown-warm",
    "audience": "Humanitarians AI",
    "brand": "claude-hai",
    "channel_title": "",   # no burned-in footer text (review checklist); brand is in the composer chip + outro
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
    "note": "Native 9:16 Short of 'Brutalist, Shared'. Same facts (../FACTCHECK.md), own layout.",
    "tags": ["Humanitarians AI", "Brutalist", "open source", "pull requests", "Blender", "Shorts"],
  },
  "beats": beats,
}
out = Path(__file__).with_name("beat_sheet.json")
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
