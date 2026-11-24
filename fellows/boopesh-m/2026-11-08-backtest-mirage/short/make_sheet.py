# Writes beat_sheet.json (9:16, 2160x3840) for the Short of "The Backtest Mirage" -- Boopesh M.
# A separate native-portrait reel, not a crop. Numbers from ../code/results.json (synthetic noise data).
import json
from pathlib import Path

VOICE = "am_onyx"
HAI = "@HumanitariansAI"
RES = json.loads((Path(__file__).resolve().parent.parent / "code" / "results.json").read_text())
WIN = RES["main_world"]["winner"]


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
       "Hi, I am Boopesh M., and this video is about the backtest mirage. Heads up: this is an AI voice reading "
       "my script, and the results come from my own small experiment, on synthetic noise data.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "ClaudeComposerAsk916", "props": {
            "greeting": "Hi, Boopesh", "topic": "Irreducibly Human", "segment": "AI in Finance",
            "command": "Why does an AI that tests 10,000 trading strategies always find a brilliant one?",
            "runningText": "searching 10,000 strategies…", "folderLabel": HAI,
            "modelLabel": "Claude", "effortLabel": "High",
            "output": ["market: synthetic noise, zero real edge",
                       f"best Sharpe {WIN['is_sharpe']:.2f} → new data {WIN['oos_sharpe']:.2f}".replace("-", "−")]},
            "rendered": {"out": "", "at": ""}}}),
  beat("B10", "THE CLIMB", "best in-sample Sharpe for 1 / 100 / 10,000 rules (200 noise markets)",
       "I let a search try trading rules on pure random noise, where no real edge exists. "
       "Best of one rule: a Sharpe near zero. Best of a hundred: one point one. Best of ten thousand: one point six.",
       manim("B10_Climb")),
  beat("B20", "UNLOCK", "the 10,000-rule winner: climbs in-sample, turns down on locked data",
       "Then I tested the best of ten thousand on two years it never saw. Its Sharpe: minus point four. "
       "Across two hundred noise markets, the winners averaged about zero.",
       manim("B20_Unlock")),
  beat("B30", "THE FIX", "count trials, hold out, demand more",
       "The fix: count your trials, hold out data you never touch, and demand more as you test more. "
       "Otherwise, you are just picking the luckiest coin.",
       manim("B30_Fix")),
  beat("B90", "OUTRO", "HAI outro + fellow credit",
       "The backtest mirage. With Boopesh M., for Humanitarians AI.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "The Backtest Mirage (Short)",
    "slug": "backtest-mirage-short",
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
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ", "Boopesh": "bˈuːpɛʃ", "backtest": "bˈæktɛst"},
    "brutalist_commit": "a99b5323",
    "parent": "../beat_sheet.json",
    "note": "Native 9:16 Short of 'The Backtest Mirage'. Same facts (../FACTCHECK.md), own layout.",
    "tags": ["Humanitarians AI", "backtest overfitting", "AI in finance", "Sharpe ratio", "Shorts"],
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
            if (o.get("shot", {}).get("remotion") or {}).get("rendered") and \
                    o["shot"]["remotion"]["props"] == b["shot"]["remotion"]["props"]:
                b["shot"]["remotion"]["rendered"] = o["shot"]["remotion"]["rendered"]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print("wrote", out, len(beats), "beats", sum(len(b["narration_text"].split()) for b in beats), "words")
