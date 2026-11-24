# Writes beat_sheet.json (16:9) for "Why Did the AI Say No?" -- Boopesh M., AI-in-finance explainer.
# Rule anchor: US Equal Credit Opportunity Act / Regulation B, 12 CFR 1002.9 (adverse-action notices),
# and CFPB Circular 2022-03 (complex algorithms; withdrawn May 2025 -- see FACTCHECK.md).
# Every number spoken comes from code/results.json (python code/credit_reasons.py, SYNTHETIC APPLICANTS).
import json
from pathlib import Path

VOICE = "am_onyx"
HAI = "@HumanitariansAI"
TOPIC = "Irreducibly Human"
SEG = "AI in Finance"
RES = json.loads((Path(__file__).with_name("code") / "results.json").read_text())
A = RES["applicant_a"]
R = RES["reasons"]
CF = RES["counterfactual"]

# the spoken words below were written from these values -- stop if a re-run ever changes them
assert RES["setup"]["n_applicants"] == 20_000 and RES["setup"]["cutoff"] == 0.30
assert round(A["risk_scorecard"] * 100) == 53 and round(A["risk_boosted"] * 100) == 34
assert R["scorecard"]["top3"] == ["dti", "util", "missed"]
assert R["boosted"]["top3"] == ["missed", "util", "history"]
assert R["agreement"]["n_shared"] == 2 and R["boosted"]["model_runs"] == 16_000
assert "dti" in R["boosted_vs_approved_background"]["top3"] and "dti" in R["boosted_retrained_other_split"]["top3"]
assert CF["both_approve_paydown"] == 3850 and round(CF["both_approve_util"]) == 34
assert round(RES["models"]["scorecard"]["test_auc"], 2) == round(RES["models"]["boosted"]["test_auc"], 2) == 0.84


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
       "Hi, I am Boopesh M., and this video is about explainable AI in lending. When an AI credit model says no "
       "to a loan, why did it say no? Quick note: this is an AI voice reading my script. And every number comes "
       "from my own small experiment, on synthetic applicants.",
       composer("Hi, Boopesh",
                "When an AI credit model denies a loan, how do you find the specific reasons it said no?",
                ["synthetic applicants: 20,000 made up, 5 plain features",
                 "Applicant A: denied by a scorecard and by a black-box model",
                 "top 3 reasons from each model: they share 2 of 3"],
                "explaining the decision…")),
  beat("B10", "OVERVIEW", "BLUF -- hesitant writer corrects the misconception",
       "Here's the whole idea in one line. The model said no is not a reason. "
       "A lender has to name the facts that drove the no.",
       {"type": "GRAPHIC", "source": "remotion", "motion": "fade",
        "remotion": {"pattern": "BrutalistHesitantWriter", "props": {
            "text": "You were denied because the model said no.",
            "face": "serif", "fontSize": 60, "lineSpacing": 1.3, "align": "center",
            "triggerWords": "the model said no",
            "replacementWords": "your debt is too high for your income",
            "mistakeRate": 4, "hesitateWithin": 2, "hesitateBetween": 14,
            "charMs": 45, "jitter": 20, "seed": "boopesh-reasons-01", "showCaret": True,
            "contextTitle": "The idea in one line",
            "contextItems": [
                {"label": "The rule", "detail": "a denial needs specific reasons"},
                {"label": "The catch", "detail": "a black box has no weights to read"}]},
            "rendered": {"out": "", "at": ""}}},
       lead_silence_s=0.5),
  beat("B20", "THE RULE", "Reg B 1002.9(b)(2): specific principal reasons; 'failed a score' insufficient; "
                          "CFPB Circular 2022-03 (withdrawn May 2025); not legal advice",
       "First, the rule. In the US, Regulation B, under the Equal Credit Opportunity Act, says a denied applicant gets specific reasons: the principal ones. You failed to reach our score is not enough. In twenty twenty-two, a CFPB circular said this holds for complex algorithms too. It was withdrawn in twenty twenty-five, but the regulation's wording remains. That's what the rule asks for, not legal advice.",
       manim("B20_Rule")),
  beat("B30", "THE EXPERIMENT", "20,000 synthetic applicants, 5 features, no protected traits; scorecard vs boosted; "
                                "same AUC",
       "Now my experiment: twenty thousand synthetic applicants, with five plain features: income, debt-to-income, missed payments, credit history length, and card use. No protected traits; fairness is another video. I trained two models: a simple scorecard, and a gradient-boosted black box. On test data, both rank risk equally well.",
       manim("B30_Models")),
  beat("B40", "APPLICANT A", "A's five values; risk 53 % (scorecard) vs 34 % (boosted) vs cutoff 30 %; both deny",
       "Meet Applicant A, also made up. Debt payments take forty-four percent of income. Cards are seventy-two percent used. One missed payment, four years of history. My chosen line is a thirty percent risk of default. The scorecard puts A at fifty-three percent; the black box, at thirty-four. Both say no.",
       manim("B40_ApplicantA")),
  beat("B50", "SCORECARD REASONS", "one formula: push = weight x (A - average); bars; top 3 dti / util / missed",
       "Why? For the scorecard, the answer is exact. Each feature's push toward no is its weight, times how far "
       "A sits from the average applicant. Five multiplications. The top three reasons: debt payments too high "
       "for income, cards near their limits, and a recent missed payment.",
       manim("B50_Scorecard")),
  beat("B60", "BLACK-BOX REASONS", "Shapley values, 16,000 model runs; top 3 missed / util / history; 2 of 3 shared; "
                                   "reasons shift with comparison group / retraining",
       "The black box has no weights to read. So I computed Shapley values: swap A's features in and out, in every "
       "combination, against five hundred other applicants. Sixteen thousand model runs, for one person. "
       "Its top three: the missed payment, card use, and a short credit history. Two of three match the scorecard. "
       "And the list can shift: compare A with approved applicants only, or retrain, and debt-to-income moves back into its top three.",
       manim("B60_BlackBox")),
  beat("B70", "WHAT WOULD CHANGE IT + LIMITS", "counterfactual: pay cards down $3,850 (72 % -> 34 %), both approve; "
                                               "limits",
       "So, what would change the answer? Keep everything else, and pay card balances down by about three thousand "
       "eight hundred dollars, from seventy-two to thirty-four percent of the limit. Both models now say yes. "
       "That's the kind of reason a person can act on. Limits: synthetic applicants, a cutoff I chose, and "
       "Shapley values are one method among several.",
       manim("B70_Change")),
  beat("B80", "YOUR TURN", "HANDOFF -- prompt read aloud",
       "Your turn. Paste this into Claude, with my script attached. Retrain the black box with a different "
       "seed. Does Applicant A keep the same top three reasons?",
       composer("Your turn.",
                "Here's my script (credit_reasons.py). Train a second boosted model with a different seed and data "
                "split. Does Applicant A get the same top 3 reasons? How often do the top 3 change across 20 seeds? "
                "Show the numbers.",
                [], "paste this into Claude…")),
  beat("B90", "OUTRO", "HAI outro + fellow credit card (name, role, team; no invented links)",
       "Why did the AI say no? With Boopesh M., for Humanitarians AI. Thanks for watching.",
       manim("B90_Outro"), lead_silence_s=0.3),
]

sheet = {
  "metadata": {
    "title": "Why Did the AI Say No? Reason codes for AI credit decisions",
    "slug": "why-did-the-ai-say-no",
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
    "pronounce": {"Kokoro": "kˈoʊkəɹoʊ", "Boopesh": "bˈuːpɛʃ", "Shapley": "ʃˈæpli"},
    "brutalist_commit": "a99b5323",
    "sources": {"regulation": "12 CFR 1002.9(a)(2), (b)(2) (Regulation B), text read from a pinned GitHub mirror "
                              "of govinfo eCFR bulk XML (amendment date Sept. 14, 2026)",
                "circular": "CFPB Circular 2022-03 (May 26, 2022; 87 FR 35864) -- not read directly; withdrawn "
                            "May 12, 2025 (90 FR 20084) per search results",
                "method": "Lundberg & Lee, 'A Unified Approach to Interpreting Model Predictions', NeurIPS 2017"},
    "note": "AI-in-finance explainer for Boopesh M. (Humanitarians AI Fellow). Every number from "
            "code/credit_reasons.py (synthetic applicants, results.json). AI narration (Kokoro am_onyx) "
            "disclosed in B00. Not legal advice.",
    "tags": ["Humanitarians AI", "explainable AI", "AI in finance", "credit scoring", "adverse action",
             "reason codes", "Shapley values", "machine learning", "Manim", "Claude"],
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
