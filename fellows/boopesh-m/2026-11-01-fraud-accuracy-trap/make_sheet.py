# Writes beat_sheet.json (16:9) for "The 99.9% Accuracy Trap" -- Boopesh M., AI-in-finance explainer.
# Real-data facts: Kaggle / ULB Machine Learning Group + Worldline credit-card dataset (492 frauds in 284,807).
# Every model number spoken comes from code/results.json (python code/fraud_trap.py, SYNTHETIC data).
import json
from pathlib import Path

VOICE = "am_onyx"
HAI = "@HumanitariansAI"
TOPIC = "Irreducibly Human"
SEG = "AI Fraud Detection"


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
       "Hi, I am Boopesh M., and this video is about AI fraud detection, and one number that fools a lot of "
       "people: accuracy. Quick note: this is an AI voice reading my script. And every result you'll see "
       "comes from my own small experiment, on synthetic data.",
       composer("Hi, Boopesh",
                "Can a fraud model be 99.9% accurate and still useless?",
                ["fraud is rare: 492 frauds in 284,807 card transactions (ULB + Worldline dataset)",
                 "a model that always says “legit” scores 99.8% and catches nothing",
                 "your experiment: synthetic data with the same fraud rate"],
                "running the experiment…")),
  beat("B10", "OVERVIEW", "BLUF -- hesitant writer corrects the misconception",
       "Here's the whole idea in one line. A high accuracy score sounds great. "
       "But when fraud is this rare, it tells you almost nothing.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "BrutalistHesitantWriter", "props": {
            "text": "99.9% accurate means it works.",
            "face": "serif", "fontSize": 60, "lineSpacing": 1.3, "align": "center",
            "triggerWords": "means it works",
            "replacementWords": "means nothing when fraud is 1 in 580",
            "mistakeRate": 4, "hesitateWithin": 2, "hesitateBetween": 14,
            "charMs": 45, "jitter": 20, "seed": "boopesh-fraud-01", "showCaret": True,
            "contextTitle": "The idea in one line",
            "contextItems": [
                {"label": "Fraud", "detail": "about 1 card transaction in 580"},
                {"label": "Accuracy", "detail": "mostly counts the easy, legit ones"}]},
            "rendered": {"out": "", "at": ""}}},
       lead_silence_s=0.5),
  beat("B20", "HOW RARE", "dot grid: 580 dots, 1 red; real dataset counts",
       "How rare is fraud? In a widely used dataset of real card transactions, there are four hundred "
       "ninety-two frauds out of two hundred eighty-four thousand, eight hundred seven. "
       "About one in every five hundred eighty. Here are five hundred eighty dots. Just one is red.",
       manim("B20_Rare")),
  beat("B30", "THE LAZY MODEL", "accuracy meter 99.8%, 0 of 148 frauds caught",
       "Now meet the laziest fraud model possible. It says legit to every transaction. "
       "On synthetic data with the real fraud rate, its accuracy is ninety-nine point eight percent. "
       "Frauds caught: zero, out of a hundred forty-eight.",
       manim("B30_Lazy")),
  beat("B40", "BETTER SCORECARD", "confusion matrix as 4 boxes; recall and precision in plain words",
       "So use a better scorecard. Sort every test case into four boxes: fraud caught, fraud missed, "
       "false alarm, and legit, correctly let through. "
       "Recall asks: of all the real frauds, how many did we catch? "
       "Precision asks: of all the alarms we raised, how many were really fraud? "
       "For the lazy model, recall is zero.",
       manim("B40_Scorecard")),
  beat("B50", "REAL MODELS", "lazy vs logistic vs boosted: same accuracy, different catch",
       "Now two real models, trained on the same data. A logistic regression: ninety-nine point nine percent "
       "accurate, and it catches sixty-six of the hundred forty-eight frauds. "
       "A small gradient-boosted model: also ninety-nine point nine, but it catches a hundred twenty-seven. "
       "Nearly twice the fraud, and accuracy can't tell them apart. Recall can.",
       manim("B50_Models")),
  beat("B60", "THE THRESHOLD DIAL", "precision-recall curve with a moving threshold; cost rule",
       "Each model gives every transaction a fraud score, and you choose the cutoff. "
       "Lower it, and you catch more fraud, but raise more false alarms. "
       "At point nine, the boosted model catches a hundred twenty-six, with forty-nine false alarms. "
       "At point zero one, a hundred thirty-six, with a hundred eighty-nine. "
       "Which is right? Say a miss costs fifty times a false alarm. Then the cheapest cutoff is a low one.",
       manim("B60_Threshold")),
  beat("B70", "TAKEAWAY + LIMITS", "takeaway card + honest limits",
       "The takeaway: when the thing you're hunting is rare, accuracy is the wrong score. "
       "Look at recall, precision, and the cost of each mistake. "
       "Now the honest limits. My data is synthetic, built to match the real fraud rate, not real transactions. "
       "Real fraud systems use far more signals, and fraudsters change their tricks over time.",
       manim("B70_Takeaway")),
  beat("B80", "YOUR TURN", "HANDOFF -- prompt read aloud",
       "Your turn. Paste this into Claude, with my script attached. Make a missed fraud cost only ten times "
       "a false alarm. Where does the best cutoff move, and how many frauds do you give up? "
       "A good answer shows the numbers, not just a story.",
       composer("Your turn.",
                "Here's my fraud script (fraud_trap.py). Make a missed fraud cost only 10× a false alarm. "
                "Where does the cheapest cutoff move, and how many frauds do I give up? Show the numbers.",
                [], "paste this into Claude…")),
  beat("B90", "OUTRO", "HAI outro + fellow credit card (name, role, team; no invented links)",
       "The ninety-nine point nine percent accuracy trap. With Boopesh M., for Humanitarians AI. Thanks for watching.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "The 99.9% Accuracy Trap: why fraud models need recall and precision",
    "slug": "fraud-accuracy-trap",
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
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ", "Boopesh": "bˈuːpɛʃ"},
    "brutalist_commit": "a99b5323",
    "dataset": {"name": "Credit Card Fraud Detection (Kaggle mlg-ulb/creditcardfraud)",
                "origin": "ULB Machine Learning Group + Worldline", "rows": 284807, "frauds": 492,
                "paper": "Dal Pozzolo, Caelen, Johnson & Bontempi, 'Calibrating Probability with Undersampling "
                         "for Unbalanced Classification', IEEE SSCI 2015"},
    "note": "AI-in-finance explainer for Boopesh M. (Humanitarians AI Fellow). Model numbers from "
            "code/fraud_trap.py (synthetic data, results.json). AI narration (Kokoro am_onyx) disclosed in B00.",
    "tags": ["Humanitarians AI", "fraud detection", "AI in finance", "machine learning", "imbalanced data",
             "precision", "recall", "accuracy", "Manim", "Claude"],
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
