# Writes beat_sheet.json (16:9) for "The Backtest Mirage" -- Boopesh M., AI-in-finance explainer.
# Paper anchor: Bailey, Borwein, Lopez de Prado & Zhu, "Pseudo-Mathematics and Financial Charlatanism",
# Notices of the AMS 61(5), 2014 (not readable from the build container -- see FACTCHECK.md).
# Every number spoken comes from code/results.json (python code/backtest_mirage.py, SYNTHETIC NOISE DATA).
import json
from pathlib import Path

VOICE = "am_onyx"
HAI = "@HumanitariansAI"
TOPIC = "Irreducibly Human"
SEG = "AI in Finance"
RES = json.loads((Path(__file__).with_name("code") / "results.json").read_text())
WIN = RES["main_world"]["winner"]


def composer(greeting, command, output, running):
    return {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
            "remotion": {"pattern": "ClaudeComposerAsk", "props": {
                "greeting": greeting, "topic": TOPIC, "segment": SEG,
                "command": command, "runningText": running,
                "folderLabel": HAI, "modelLabel": "Claude", "effortLabel": "High",
                "output": output}, "rendered": {"out": "", "at": ""}}}


def manim(cls):
    return {"type": "GRAPHIC", "source": "manim", "motion": "fade",
            "manim": {"scene_class": cls, "file": "scenes.py"}}


def beat(bid, act, note, text, shot, **kw):
    b = {"beat_id": bid, "act": act, "role_note": note, "narration_text": text,
         "shot": shot, "voice": VOICE, "engine": "kokoro", "voice_kokoro": VOICE}
    b.update(kw)
    return b


beats = [
  beat("B00", "INTRO", "COLD OPEN -- required fellow intro line + AI-voice disclosure; the question",
       "Hi, I am Boopesh M., and this video is about the backtest mirage: why an AI that searches thousands of "
       "trading strategies always finds one that looks brilliant, then fails on new data. Quick note: this is an "
       "AI voice reading my script. And every number comes from my own small experiment, on synthetic noise data.",
       composer("Hi, Boopesh",
                "Why does an AI that tests 10,000 trading strategies always find a brilliant one?",
                ["the market: synthetic noise data, so no real edge exists",
                 f"best backtest Sharpe {WIN['is_sharpe']:.2f} → on new data {WIN['oos_sharpe']:.2f}".replace("-", "−"),
                 "the more you test, the better the luckiest one looks"],
                "searching 10,000 strategies…")),
  beat("B10", "OVERVIEW", "BLUF -- hesitant writer corrects the misconception",
       "Here's the whole idea in one line. Test enough strategies, and your best backtest isn't skill. "
       "It's just the luckiest draw.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "BrutalistHesitantWriter", "props": {
            "text": "My best backtest proves a real edge.",
            "face": "serif", "fontSize": 60, "lineSpacing": 1.3, "align": "center",
            "triggerWords": "proves a real edge",
            "replacementWords": "is just the luckiest try",
            "mistakeRate": 4, "hesitateWithin": 2, "hesitateBetween": 14,
            "charMs": 45, "jitter": 20, "seed": "boopesh-mirage-01", "showCaret": True,
            "contextTitle": "The idea in one line",
            "contextItems": [
                {"label": "Backtest", "detail": "a strategy tested on past data"},
                {"label": "The trap", "detail": "test enough, and one looks brilliant by luck"}]},
            "rendered": {"out": "", "at": ""}}},
       lead_silence_s=0.5),
  beat("B20", "THE NOISE MARKET", "7 years of pure-noise prices; 5 years searched, 2 years locked",
       "First, a market with nothing to find. I generated seven years of daily returns from pure random noise. "
       "Synthetic noise data: no rule can have a real edge. The search may look at the first five years. "
       "The last two stay locked away.",
       manim("B20_Noise")),
  beat("B30", "THE SEARCH", "10,000 rules, histogram of in-sample Sharpe; winner 1.69",
       "Now the search. It tries ten thousand simple rules. Each looks at the last few days, and goes long or "
       "short. Each gets a Sharpe ratio: return per unit of risk. Above one is usually called good. "
       "Most rules land near zero, as they should. But the best of ten thousand scores one point seven. "
       "On pure noise.",
       manim("B30_Search")),
  beat("B40", "UNLOCK", "winner's equity curve: climbs in-sample, turns down out-of-sample",
       "Now unlock the last two years. The winner's line, which climbed for five years, stalls, then slips. "
       "Out of sample, its Sharpe is minus point four. The brilliant backtest was a mirage.",
       manim("B40_Unlock")),
  beat("B50", "THE CLIMB", "best in-sample Sharpe vs number of rules tried, 200 noise markets",
       "Was that one unlucky run? I repeated the whole search on two hundred fresh noise markets. "
       "Best of one rule: a Sharpe near zero. Best of ten: point seven. Best of a hundred: one point one. "
       "Best of ten thousand: one point six. Out of sample, the winners averaged about zero. "
       "The more you test, the better the best looks.",
       manim("B50_Climb")),
  beat("B60", "WHY", "one formula: Sharpe noise ~ 1/sqrt(years); the paper",
       "Why? A Sharpe ratio measured over five years carries noise of about one over the square root of five: "
       "point four five. Test many rules, and the winner is simply the one with the luckiest noise. "
       "Bailey, Borwein, López de Prado and Zhu called this backtest overfitting, in the Notices of the "
       "American Mathematical Society, in 2014. Their warning: with five years of data, about forty-five tries "
       "can already reach a Sharpe near one by luck.",
       manim("B60_Why")),
  beat("B70", "THE FIX + LIMITS", "three rules + the bar to beat; honest limits",
       "So here's the fix. Count your trials, and report them. Hold out data you never touch until the very end. "
       "And demand more as you test more. In my noise markets, one rule beats point eight by luck only one time "
       "in twenty. With ten thousand rules, that bar is one point nine, so our one point seven winner fails. "
       "Correctly. Limits: synthetic noise, no trading costs, and real markets may hide small real edges.",
       manim("B70_Fix")),
  beat("B80", "YOUR TURN", "HANDOFF -- prompt read aloud",
       "Your turn. Paste this into Claude, with my script attached. Give the noise market a small real edge, "
       "and add trading costs. Does the search find the real edge, or a lucky fake? "
       "A good answer shows the numbers.",
       composer("Your turn.",
                "Here's my script (backtest_mirage.py). Give the noise market a small real edge and add a trading "
                "cost. Does the 10,000-rule search find the real edge, or a lucky fake? Show the numbers.",
                [], "paste this into Claude…")),
  beat("B90", "OUTRO", "HAI outro + fellow credit card (name, role, team; no invented links)",
       "The backtest mirage. With Boopesh M., for Humanitarians AI. Thanks for watching.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "The Backtest Mirage: why an AI strategy search always finds a winner",
    "slug": "backtest-mirage",
    "topic": "Irreducibly Human",
    "register": "Plain / Teardown-warm",
    "audience": "Humanitarians AI",
    "brand": "claude-hai",
    "channel_title": "",   # no burned-in footer text (fellow checklist); brand is in the composer chip + outro
    "creator": "Boopesh M.",
    "engine": "kokoro",
    "palette": "claude",
    "style_preset": "claude",
    "style": "claude-explainer",
    "voice_kokoro": VOICE,
    "voice_policy": "persistent-fellow-selected",
    "aspect_ratio": "16:9",
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ", "Boopesh": "bˈuːpɛʃ", "Borwein": "bˈɔːɹwaɪn", "Zhu": "ʤˈuː",
                  "backtest": "bˈæktɛst"},
    "brutalist_commit": "a99b5323",
    "paper": {"authors": "David H. Bailey, Jonathan M. Borwein, Marcos López de Prado, Qiji Jim Zhu",
              "title": "Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on "
                       "Out-of-Sample Performance",
              "venue": "Notices of the AMS 61(5), 458-471, 2014", "doi": "10.1090/noti1105",
              "read_directly": False},
    "note": "AI-in-finance explainer for Boopesh M. (Humanitarians AI Fellow). Every number from "
            "code/backtest_mirage.py (synthetic noise data, results.json). AI narration (Kokoro am_onyx) "
            "disclosed in B00.",
    "tags": ["Humanitarians AI", "backtest overfitting", "AI in finance", "quant", "Sharpe ratio",
             "multiple testing", "machine learning", "Manim", "Claude"],
  },
  "beats": beats,
}
out = Path(__file__).with_name("beat_sheet.json")
if out.exists():   # keep approvals/build stamps written by the pipeline
    old = json.loads(out.read_text())
    for k in ("approvals", "build"):
        if k in old.get("metadata", {}):
            sheet["metadata"][k] = old["metadata"][k]
    prev = {b["beat_id"]: b for b in old.get("beats", [])}
    for b in beats:   # keep audio measurements when the spoken line is unchanged
        o = prev.get(b["beat_id"])
        if o and o.get("narration_text") == b["narration_text"]:
            for k in ("actual_duration_s", "audio_file", "render_duration_s", "build", "shot_rendered"):
                if k in o:
                    b[k] = o[k]
            if (o.get("shot", {}).get("remotion") or {}).get("rendered") and \
                    o["shot"]["remotion"]["props"] == b["shot"]["remotion"]["props"]:
                b["shot"]["remotion"]["rendered"] = o["shot"]["remotion"]["rendered"]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print("wrote", out, len(beats), "beats", sum(len(b["narration_text"].split()) for b in beats), "words")
