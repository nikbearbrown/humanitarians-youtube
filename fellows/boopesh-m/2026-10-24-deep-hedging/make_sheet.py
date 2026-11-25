# Writes beat_sheet.json (16:9) for "Hedging When Trading Isn't Free" -- Boopesh M., STEM explainer.
# Paper: Buehler, Gonon, Teichmann & Wood, "Deep Hedging", Quantitative Finance 19(8):1271-1291, 2019.
# Every number spoken comes from code/results.json (python code/deep_hedge.py).
import json
from pathlib import Path

VOICE = "am_onyx"
HAI = "@HumanitariansAI"
TOPIC = "Irreducibly Human"
SEG = "Deep Hedging"

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
  beat("B00", "INTRO", "COLD OPEN -- required fellow intro line + AI-voice disclosure; paper named",
       "Hi, I am Boopesh M., and this video is about Deep Hedging, a 2019 paper by Buehler, Gonon, Teichmann "
       "and Wood, from J P Morgan and E T H Zurich. Quick note: this is an AI voice reading my script. "
       "And every number you'll see comes from my own small replication, not from the paper.",
       composer("Hi, Boopesh",
                "What is Deep Hedging (Buehler, Gonon, Teichmann & Wood, 2019), and can I replicate it small?",
                ["Deep Hedging · Quantitative Finance 19(8), 2019 · J.P. Morgan + ETH Zurich",
                 "a neural network learns the hedge, with trading costs in its objective",
                 "your replication: 40,000 simulated test paths, 0.5% fee"],
                "reading the paper and running the code…")),
  beat("B10", "OVERVIEW", "BLUF -- hesitant writer corrects the misconception",
       "Here's the whole idea in one line. The textbook hedge is exact, but only if trading is free. "
       "And in real markets, trading is never free.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "BrutalistHesitantWriter", "props": {
            "text": "Black–Scholes tells you exactly how to hedge.",
            "face": "serif", "fontSize": 60, "lineSpacing": 1.3, "align": "center",
            "triggerWords": "exactly how to hedge",
            "replacementWords": "how to hedge, if trading is free",
            "mistakeRate": 4, "hesitateWithin": 2, "hesitateBetween": 14,
            "charMs": 45, "jitter": 20, "seed": "boopesh-deephedge-01", "showCaret": True,
            "contextTitle": "The idea in one line",
            "contextItems": [
                {"label": "Textbook", "detail": "rebalance all the time, at zero cost"},
                {"label": "Real markets", "detail": "every trade pays a fee"}]},
            "rendered": {"out": "", "at": ""}}},
       lead_silence_s=0.5),
  beat("B20", "BASICS", "hedging basics + typeset Black-Scholes delta",
       "Say you sell a call option on a stock trading at a hundred dollars, expiring in thirty trading days. "
       "To cancel the risk, you hold delta shares of the stock. Black-Scholes gives delta as N of d one: "
       "a number between zero and one that moves with the price. The rule is to adjust it every trading day.",
       manim("B20_Basics")),
  beat("B30", "THE COST", "turnover and fees of the daily delta hedge, from results.json",
       "But in real markets, every trade pays a fee. I set it to half a percent. Over the month, the daily "
       "delta hedge trades about two point two shares per option, and pays a dollar eleven in fees. "
       "The option only sold for two seventy-five. That's about forty percent, gone.",
       manim("B30_Cost")),
  beat("B40", "THE MOVE", "the paper's move: learned policy, objective incl. costs, entropic utility",
       "Deep Hedging's move is simple. Let a small neural network choose the position each day, "
       "from the time left, the price, and what it already holds. Then train it on simulated paths "
       "to maximise a score of the final profit that includes the fees. "
       "For the score, I use the entropic utility from Buehler's own code: big losses count much more than small ones.",
       manim("B40_Move")),
  beat("B50", "RESULTS", "P&L histograms BS vs deep under costs + stats table",
       "Here's the result on forty thousand fresh test paths, with the half-percent fee. "
       "Grey is the Black-Scholes delta, teal is the deep hedge. On average, the seller loses a dollar eleven "
       "with Black-Scholes, and sixty-five cents with the deep hedge. The spread is wider, but the worst "
       "five percent of outcomes improve, and so does the risk score it was trained to maximise.",
       manim("B50_Results")),
  beat("B60", "WHAT IT LEARNED", "one path: positions BS vs deep; turnover and fee bars",
       "So what did it learn? Here's one test path. Black-Scholes nudges its position every single day. "
       "The deep hedge moves more smoothly, and skips the small back-and-forth that the fee would punish. "
       "Across all the test paths, "
       "it trades one point three shares instead of two point two, and pays sixty-five cents in fees "
       "instead of a dollar eleven.",
       manim("B60_Learned")),
  beat("B70", "LIMITS", "gamma = 0 sanity check + honest limits",
       "Is it fooling itself? Sanity check: set the fee to zero, and the network should rediscover "
       "Black-Scholes. It nearly does. Its positions differ by about two hundredths of a share on average, "
       "and its utility is slightly worse. Now the limits. This is a toy world: Black-Scholes prices, one option. "
       "The paper goes further, with S and P five hundred data and the Heston model. And a learned hedge is "
       "only as good as the simulator it trained on. Small network, one fee level.",
       manim("B70_Limits")),
  beat("B80", "YOUR TURN", "HANDOFF -- prompt read aloud",
       "Your turn. Paste this into Claude, with my script attached. Double the fee to one percent and retrain. "
       "Does the network trade even less, and does it still beat the Black-Scholes delta? "
       "A good answer shows the numbers, not just a story.",
       composer("Your turn.",
                "Here's my deep hedging script (deep_hedge.py). Double the fee to 1% and retrain. Does the "
                "network trade even less, and does it still beat the Black–Scholes delta? Show the numbers.",
                [], "paste this into Claude…")),
  beat("B90", "OUTRO", "HAI outro + fellow credit card (name, role, team; no invented links)",
       "Hedging when trading isn't free. With Boopesh M., for Humanitarians AI. Thanks for watching.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "Hedging When Trading Isn't Free: Deep Hedging, replicated",
    "slug": "deep-hedging",
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
    "aspect_ratio": "16:9",
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ", "Buehler": "bjˈuːlɚ", "Buehler's": "bjˈuːlɚz",
                  "Gonon": "ɡoʊnˈɔn", "Teichmann": "tˈaɪkmən"},
    "brutalist_commit": "a99b5323",
    "paper": {"title": "Deep Hedging", "authors": "Hans Buehler, Lukas Gonon, Josef Teichmann, Ben Wood",
              "venue": "Quantitative Finance 19(8):1271-1291, 2019",
              "doi": "10.1080/14697688.2019.1571683", "arxiv": "1802.03042"},
    "note": "STEM explainer for Boopesh M. (Humanitarians AI Fellow). Numbers from code/deep_hedge.py "
            "(results.json). AI narration (Kokoro am_onyx) disclosed in B00.",
    "tags": ["Humanitarians AI", "deep hedging", "quantitative finance", "Black-Scholes", "options",
             "reinforcement learning", "neural networks", "transaction costs", "Manim", "Claude"],
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
            if (o.get("shot", {}).get("remotion") or {}).get("rendered"):
                b["shot"]["remotion"]["rendered"] = o["shot"]["remotion"]["rendered"]
out.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
print("wrote", out, len(beats), "beats", sum(len(b["narration_text"].split()) for b in beats), "words")
