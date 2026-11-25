# Writes beat_sheet.json (9:16, 2160x3840) for the Short of "The 99.9% Accuracy Trap" -- Boopesh M.
# A separate native-portrait reel, not a crop. Model numbers from ../code/results.json (synthetic data).
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
       "Hi, I am Boopesh M., and this video is about AI fraud detection, and the ninety-nine point nine percent "
       "accuracy trap. Heads up: this is an AI voice reading my script, and the results come from my own small "
       "experiment, on synthetic data.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "ClaudeComposerAsk916", "props": {
            "greeting": "Hi, Boopesh", "topic": "Irreducibly Human", "segment": "AI Fraud Detection",
            "command": "Can a fraud model be 99.9% accurate and still useless?",
            "runningText": "running the experiment…", "folderLabel": HAI,
            "modelLabel": "Claude", "effortLabel": "High",
            "output": ["fraud: 492 in 284,807 card transactions", "synthetic test · same fraud rate"]},
            "rendered": {"out": "", "at": ""}}}),
  beat("B10", "HOW RARE", "dot grid, 1 red in 580",
       "In a widely used card dataset, fraud is about one transaction in five hundred eighty. "
       "Four hundred ninety-two, out of almost two hundred eighty-five thousand.",
       manim("B10_Rare")),
  beat("B20", "LAZY VS REAL", "lazy model vs boosted model: accuracy alike, frauds caught 0 vs 127",
       "On synthetic data with that fraud rate, a lazy model that always says legit is ninety-nine point eight "
       "percent accurate, and catches zero frauds. A small boosted model is ninety-nine point nine percent accurate, "
       "but it catches a hundred twenty-seven of a hundred forty-eight.",
       manim("B20_LazyVsReal")),
  beat("B30", "TAKEAWAY", "takeaway: recall, precision, cost",
       "Almost the same accuracy, completely different models. For rare events, check recall, precision, "
       "and what each mistake costs.",
       manim("B30_Takeaway")),
  beat("B90", "OUTRO", "HAI outro + fellow credit",
       "The ninety-nine point nine percent accuracy trap. With Boopesh M., for Humanitarians AI.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "The 99.9% Accuracy Trap (Short)",
    "slug": "fraud-accuracy-trap-short",
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
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ", "Boopesh": "bˈuːpɛʃ"},
    "brutalist_commit": "a99b5323",
    "parent": "../beat_sheet.json",
    "note": "Native 9:16 Short of 'The 99.9% Accuracy Trap'. Same facts (../FACTCHECK.md), own layout.",
    "tags": ["Humanitarians AI", "fraud detection", "AI in finance", "precision", "recall", "Shorts"],
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
