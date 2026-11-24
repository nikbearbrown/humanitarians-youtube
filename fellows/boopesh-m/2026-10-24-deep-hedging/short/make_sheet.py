# Writes beat_sheet.json (9:16, 2160x3840) for the Short of "Hedging When Trading Isn't Free" -- Boopesh M.
# A separate native-portrait reel, not a crop. Numbers from ../code/results.json.
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
       "Hi, I am Boopesh M., and this video is about Deep Hedging, a 2019 paper from J P Morgan and "
       "E T H Zurich. Heads up: this is an AI voice reading my script, and the numbers are from my own small replication.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "ClaudeComposerAsk916", "props": {
            "greeting": "Hi, Boopesh", "topic": "Irreducibly Human", "segment": "Deep Hedging",
            "command": "Can a neural network hedge an option better than Black–Scholes once trading costs money?",
            "runningText": "running the replication…", "folderLabel": HAI,
            "modelLabel": "Claude", "effortLabel": "High",
            "output": ["Deep Hedging · Quantitative Finance, 2019", "40,000 test paths · 0.5% fee"]},
            "rendered": {"out": "", "at": ""}}}),
  beat("B10", "COST", "the textbook hedge's fees",
       "The textbook Black-Scholes hedge adjusts every day. With a half-percent fee, that costs a dollar eleven "
       "per option. About forty percent of the option's price.",
       manim("B10_Cost")),
  beat("B20", "MOVE", "learned policy with fees in the objective",
       "Deep Hedging trains a neural network to choose the position instead, with the fees inside its objective.",
       manim("B20_Move")),
  beat("B30", "RESULT", "turnover and fees, BS vs deep",
       "On forty thousand test paths, it trades one point three shares instead of two point two, "
       "and pays sixty-five cents in fees instead of a dollar eleven.",
       manim("B30_Result")),
  beat("B40", "LIMITS", "sanity check + honest limit",
       "With zero fees, it lands close to Black-Scholes. The catch: this is a toy world, "
       "and a learned hedge is only as good as its simulator.",
       manim("B40_Limits")),
  beat("B90", "OUTRO", "HAI outro + fellow credit",
       "Hedging when trading isn't free. With Boopesh M., for Humanitarians AI.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "Hedging When Trading Isn't Free (Short)",
    "slug": "deep-hedging-short",
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
    "note": "Native 9:16 Short of 'Hedging When Trading Isn't Free'. Same facts (../FACTCHECK.md), own layout.",
    "tags": ["Humanitarians AI", "deep hedging", "quant finance", "Black-Scholes", "Shorts"],
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
