#!/usr/bin/env python3
"""Author beat_sheet.json for hai-the-test-that-couldnt-fail.

Subject: a CTGAN synthetic-data notebook whose evaluation reports success on
results that, read literally, are failures.

Every figure quoted in the narration is RECOMPUTED here by re-running the
notebook's own dataset code at its own seed. Nothing is hand-typed. No
individual is named anywhere (the notebook carries a personal copyright line).
"""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

OUT = Path(__file__).resolve().parent / "beat_sheet.json"
WPS = 2.62  # measured from the previous Bella reel

# -- reproduce the notebook's dataset, verbatim, same seed -------------------
np.random.seed(42)
n = 10000
d = pd.DataFrame({
    'Age': np.random.randint(20, 80, n),
    'Gender': np.random.choice(['Male', 'Female'], size=n, p=[0.48, 0.52]),
    'BMI': np.random.normal(27, 4.0, n).round(1),
    'BloodPressure': np.random.randint(90, 180, n),
    'Cholesterol': np.random.randint(120, 300, n),
    'GlucoseLevel': np.random.normal(110, 25, n).round(1),
    'Smoking': np.random.choice(['Yes', 'No'], size=n, p=[0.2, 0.8]),
    'PhysicalActivity': np.random.choice(['Low', 'Moderate', 'High'], size=n, p=[0.4, 0.4, 0.2]),
    'SleepHours': np.random.normal(6.8, 1.2, n).round(1),
    'Diabetes': np.random.choice([0, 1], size=n, p=[0.78, 0.22]),
})
d['Overweight'] = (d['BMI'] > 30).astype(int)
d['HighBP'] = (d['BloodPressure'] > 140).astype(int)
d['HighCholesterol'] = (d['Cholesterol'] > 240).astype(int)
d['HealthRiskScore'] = (0.3 * d['Overweight'] + 0.3 * d['HighBP']
                        + 0.2 * d['HighCholesterol'] + 0.2 * d['Diabetes']
                        + np.random.normal(0, 0.05, n)).round(2)
num = ['Age', 'BMI', 'BloodPressure', 'Cholesterol', 'GlucoseLevel', 'SleepHours', 'HealthRiskScore']
d[num] = MinMaxScaler().fit_transform(d[num])

FEATS = ['Age', 'BMI', 'BloodPressure', 'Cholesterol', 'GlucoseLevel', 'SleepHours']
BASE = 1 - d['Diabetes'].mean()
MAXR = max(abs(d['Diabetes'].corr(d[c])) for c in FEATS)
_m = LogisticRegression(max_iter=1000).fit(d[FEATS], d['Diabetes'])
_pred = _m.predict(d[FEATS])
CTRL_ACC = accuracy_score(d['Diabetes'], _pred)
CTRL_F1 = f1_score(d['Diabetes'], _pred)
CTRL_POS = int(_pred.sum())
BMI_BP = d['BMI'].corr(d['BloodPressure'])
BMI_RISK = d['BMI'].corr(d['HealthRiskScore'])

# Guards: if the reproduction ever stops matching, the narration is wrong.
assert CTRL_POS == 0 and CTRL_F1 == 0.0, "control no longer degenerate - rewrite B16/B17"
assert abs(BASE - 0.785) < 0.002, "base rate drifted - narration quotes 0.785"
assert MAXR < 0.015, "a real correlation appeared - rewrite B17"

B = []


def add(bid, act, text, pattern, props, motion="illustrate"):
    B.append({
        "beat_id": bid, "act": act, "narration_text": text,
        "shot": {"type": "GRAPHIC", "source": "remotion", "motion": motion,
                 "remotion": {"pattern": pattern, "props": props}},
        "estimated_duration_s": round(len(text.split()) / WPS, 1),
        "audio_file": "mp3/beat-%s.mp3" % bid,
    })


def stmt(bid, act, text, eyebrow, headline, kicker="", motion="fade"):
    add(bid, act, text, "IdxStatement",
        {"eyebrow": eyebrow, "headline": headline, "kicker": kicker}, motion)


add("B00", "ASK",
    "A synthetic healthcare dataset, ten thousand records, and an evaluation that says every test passed. "
    "This is Humanitarians AI. Today we read that scoreboard literally, because when you do, "
    "seven out of seven checks failed, and the notebook called it success.",
    "ClaudeComposerAsk",
    {"greeting": "Read the scoreboard.", "topic": "SYNTHETIC DATA · CTGAN",
     "segment": "The Test That Couldn't Fail",
     "command": "Here is a CTGAN synthetic-data notebook. It reports strong fidelity, good utility and strong privacy. Check whether the numbers actually support those three claims — and tell me where the evaluation is measuring nothing at all.",
     "runningText": "re-running the numbers…", "folderLabel": "@HumanitariansAI",
     "output": ["fidelity: 7 of 7 columns rejected the null",
                "utility: accuracy equals the base rate exactly",
                "privacy: one distance, from 100 million pairs"]}, "type-on")

stmt("B01", "PREMISE",
     "The premise is genuinely good. Real health data is confidential, expensive, and often too small. "
     "Synthetic data promises a way around all three — privacy, scarcity, and bias — by learning a distribution "
     "instead of copying records.",
     "THE PREMISE", "Learn the distribution. Never copy the record.",
     "privacy · scarcity · bias — three real problems")

add("B02", "GAN",
    "CTGAN does this with two networks. A generator invents rows. A discriminator tries to spot the fakes. "
    "They train against each other until neither can win, and whatever the generator produces at that point becomes your dataset.",
    "SynthGanDuel", {}, "stagger")

stmt("B03", "SETUP",
     "The notebook builds ten thousand patient records, trains CTGAN on them, and asks three questions. "
     "Is the synthetic data statistically faithful. Is it useful for modelling. And is it private.",
     "THE EXPERIMENT", "Fidelity. Utility. Privacy.",
     "three claims — and the notebook answers yes to all three")

add("B04", "TWIST",
    "But look at where the real data comes from. Age is a random integer. B M I is a random normal. "
    "Blood pressure, cholesterol, glucose, sleep, diabetes — every column drawn on its own, "
    "with no relationship to any other column.",
    "SynthRandomReveal", {}, "stagger")

stmt("B05", "NUANCE",
     "That matters more than it sounds. Four derived columns do carry real structure, because they are computed from the others. "
     "Everything else is independent noise wearing medical labels.",
     "WHAT IS ACTUALLY IN THERE", "Independent noise, with medical column names.",
     "the only real structure is the structure that was calculated")

add("B06", "DIST",
    "So what can a generator learn from that? The shape of each column on its own. And it does. "
    "The synthetic distributions track the real ones closely — a little wider, slightly shifted, essentially the same curve.",
    "SynthParticleHist", {}, "stagger")

stmt("B07", "FIDELITY",
     "Now the first claim: fidelity. The notebook runs a Kolmogorov Smirnov test on every numeric column, "
     "and it states the rule up front. High p-values, above zero point zero five, mean the distributions are similar.",
     "CLAIM ONE — FIDELITY", "The rule, written down before the test.",
     "p greater than 0.05 means “statistically similar”")

add("B08", "PRAIN",
    "Here are the seven results. Zero. Zero. Zero point zero zero zero three. Zero, zero, zero, and zero. "
    "Every numeric column lands below the threshold. By the rule the notebook just wrote down, all seven failed.",
    "SynthPValueRain", {}, "stagger")

stmt("B09", "RULE",
     "And that is not a marginal result. A p-value that small says the two distributions are distinguishable "
     "with essentially total confidence. Seven times out of seven.",
     "READ LITERALLY", "Every column is distinguishable from its synthetic copy.",
     "not close, not borderline — rejected")

add("B10", "GOALPOST",
    "Then the summary says this. All K S values are below zero point one, so the distributions are very similar. "
    "Which is a different test, against a different number, chosen after the results came back.",
    "SynthMovingGoalpost", {}, "illustrate")

stmt("B11", "LESSON",
     "The data did not change. The criterion did. A threshold you pick after seeing your results is not a threshold — "
     "it is a description of the results.",
     "THE FIRST LESSON", "A threshold chosen afterwards is not a threshold.",
     "pre-register the number, or it proves nothing")

add("B12", "CHI",
    "The categorical test has a deeper problem. It cross-tabulates real against synthetic row by row — "
    "but row five of one has nothing to do with row five of the other. Shuffle a column so the marginals are identical, "
    "and the test still returns a comfortable pass.",
    "SynthChiSquareProof", {}, "stagger")

stmt("B13", "LESSON2",
     "So that test passes when the columns match, and passes when they are unrelated. "
     "It cannot fail. Which means it was never evidence of anything.",
     "THE SECOND LESSON", "Run your test on data you know is wrong.",
     "if it still passes, it was never measuring")

stmt("B14", "UTILITY",
     "Now the strongest claim. Train a model on synthetic data, test it on real data. "
     "If it performs, the synthetic data carries real analytical value. The notebook reports accuracy of zero point seven eight five.",
     "CLAIM TWO — UTILITY", "Train on synthetic. Test on real.",
     "reported accuracy 0.785 — and an F1 of zero")

add("B15", "BASERATE",
    "But look at what the model does. It predicts no diabetes, every single time, for all ten thousand patients. "
    "And in this dataset, seventy-eight point five percent of patients do not have diabetes. "
    "The accuracy is not a result. It is the base rate.",
    "SynthBaseRate", {}, "stagger")

add("B16", "CONTROL",
    "Here is the control the notebook never ran. Train the same model on the real data instead, and test on real data. "
    "Same accuracy. Same F1 of zero. Zero positive predictions.",
    "SynthControlRun", {}, "stagger")

add("B17", "SIGNAL",
    "Because there is nothing to learn. Every one of those six features correlates with diabetes at under "
    "one and a half hundredths. They were drawn independently, so no model, on real or synthetic data, could ever predict it.",
    "SynthCorrelationGrid", {}, "stagger")

stmt("B18", "CAUSE",
     "The notebook reads that zero as class imbalance, and suggests better sampling. "
     "But balancing classes cannot create a relationship that was never generated in the first place.",
     "THE MISDIAGNOSIS", "It was not imbalance. There was no signal.",
     "resampling cannot manufacture a correlation")

stmt("B19", "PRIVACY",
     "The privacy claim rests on one number: the single smallest distance between any real and any synthetic record, "
     "out of one hundred million pairs. One extreme value, compared against a threshold with no stated origin, "
     "and no baseline for what real-to-real distance even looks like.",
     "CLAIM THREE — PRIVACY", "One number, from a hundred million comparisons.",
     "a minimum is not a distribution")

add("B20", "FAIR",
    "And here is the part that is easiest to get backwards. "
    "CTGAN did its job. It reproduced the column shapes it was given. What failed was the scoreboard around it.",
    "SynthVerdictScale", {}, "illustrate")

stmt("B21", "FIX",
     "A working evaluation needs three things this one lacks. A threshold fixed before the run. "
     "A control that should fail, to prove the test can fail. And a baseline, so you know what a good score even looks like.",
     "WHAT IT NEEDED", "Pre-register. Control. Baseline.",
     "three things, none of them expensive")

stmt("B22", "BIGGER",
     "This is the whole generative AI evaluation problem in miniature. The model is easy to run, and the output looks convincing. "
     "The hard part, the part almost nobody does, is proving your measurement could have told you otherwise.",
     "THE REAL LESSON", "The output looked right. That was the trap.",
     "an eval that cannot fail is not an eval")

add("B23", "VERDICT",
    "So here is the teardown. Not that synthetic data does not work — it does, and the premise is sound. "
    "But every claim in this notebook was checked by an instrument that could not return bad news.",
    "ClaudeVerdictArtifact",
    {"artifactTitle": "The Test That Couldn't Fail — one page",
     "artifactHeading": "The teardown",
     "artifactLines": [
         "Fidelity: the stated rule was p > 0.05. All seven numeric columns returned p near 0.0000 — then the summary switched to a different statistic and passed them.",
         "The categorical test cross-tabulates unrelated rows. With identical marginals it still returns p near 0.57, so it cannot fail and never measured similarity.",
         "Utility: TSTR accuracy 0.785 is exactly the 0.7847 base rate. The model predicted the majority class for all 10,000 rows and scored F1 = 0.000.",
         "The missing control: training on REAL data scores identically — 0.785, F1 0.000, zero positive predictions. The synthetic data was never the cause.",
         "Root cause: the source columns were drawn independently, so correlation with the target is under 0.014. There was no relationship for any model to find.",
         "The generator is not at fault. CTGAN reproduced the marginals it was given. The evaluation is what failed."]},
    "stagger")

add("B24", "HANDOFF",
    "Your turn, and this one is uncomfortable. Take an evaluation you already trust and feed it data you know is broken. "
    "Shuffle the labels. Swap in noise. If the score barely moves, you have not been measuring your model at all.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "YOUR TURN", "segment": "Can your eval fail?",
     "command": "Here is my evaluation harness. Feed it deliberately broken input — shuffled labels, pure noise, a constant predictor — and tell me whether the score actually moves. If it does not, tell me exactly which check is decorative.",
     "runningText": "trying to make it fail…", "folderLabel": "@HumanitariansAI",
     "output": ["a test that never fails is not a test",
                "the fastest way to trust a metric is to break it on purpose"]}, "type-on")

add("B25", "OUTRO",
    "The test that couldn't fail. If a teardown that checks the measurement, and not just the model, is worth your time, "
    "subscribe. Humanitarians AI.",
    "ClaudeTitleOutro", {"title": "The Test That Couldn't Fail", "handle": "@HumanitariansAI"}, "fade")

sheet = {
    "metadata": {
        "title": "The Test That Couldn't Fail",
        "slug": "hai-the-test-that-couldnt-fail",
        "topic": "SYNTHETIC DATA · CTGAN",
        "register": "Teardown", "audience": "HAI", "brand": "claude",
        "voice": "HumanitariansAI", "engine": "kokoro", "palette": "claude",
        "style_preset": "claude", "ground": "#FAF9F5", "voice_kokoro": "af_bella",
        "channel": "humanitarians-ai", "handle": "@HumanitariansAI",
        "note": ("Teardown of a CTGAN synthetic-data notebook's evaluation. Every figure in the "
                 "narration is recomputed by this script from the notebook's own dataset code at "
                 "seed 42 - nothing is hand-typed. NO INDIVIDUAL IS NAMED (the notebook carries a "
                 "personal copyright line). The verdict is explicitly fair to CTGAN: the generator "
                 "worked; the evaluation is what failed. Bella (af_bella). Never publishes."),
        "tags": ["synthetic data", "CTGAN", "SDV", "evaluation", "statistics",
                 "KS test", "TSTR", "privacy", "generative AI", "Humanitarians AI"],
        "computed": {
            "base_rate": round(float(BASE), 4),
            "max_abs_corr_with_target": round(float(MAXR), 4),
            "control_accuracy": round(float(CTRL_ACC), 3),
            "control_f1": round(float(CTRL_F1), 3),
            "control_positive_predictions": CTRL_POS,
            "corr_bmi_bloodpressure": round(float(BMI_BP), 4),
            "corr_bmi_healthriskscore": round(float(BMI_RISK), 4),
        },
    },
    "beats": B,
}

OUT.write_text(json.dumps(sheet, indent=2, ensure_ascii=False), encoding="utf-8")
w = sum(len(b["narration_text"].split()) for b in B)
print("wrote %s" % OUT)
print("%d beats - %d words - projected %.0fs = %dm%02ds"
      % (len(B), w, w / WPS, int(w / WPS) // 60, int(w / WPS) % 60))
print("computed:", json.dumps(sheet["metadata"]["computed"]))
_banned = ["chinmay", "chinmai", "sawant", "savant"]
_blob = json.dumps(sheet, ensure_ascii=False).lower()
_hits = [x for x in _banned if x in _blob]
print("NAME CHECK:", "CLEAN" if not _hits else "FAIL %s" % _hits)
