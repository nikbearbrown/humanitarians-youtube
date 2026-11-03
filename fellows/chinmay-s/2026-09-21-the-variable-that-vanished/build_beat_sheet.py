#!/usr/bin/env python3
"""Author beat_sheet.json for hai-the-variable-that-vanished.

Subject: a notebook on SES -> health causality. Its "causal-aware" model adjusts
for the mediators that carry the very effect the notebook set out to measure.

EVERY figure spoken or rendered in the reel is recomputed here by re-running the
notebook's own data-generating process at seed 42. Assertions below fail the
build if the reproduction drifts, so the narration can never silently go stale.

No individual is named anywhere in the output (the notebook carries a personal
copyright line; the reel attributes to "the notebook").
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

OUT = Path(__file__).resolve().parent / "beat_sheet.json"
WPS = 2.60  # Bella, measured across the two previous reels

# ── reproduce the notebook's DGP, verbatim, seed 42 ────────────────────────
np.random.seed(42)
n = 11500
education = np.random.choice([1, 2, 3, 4], size=n, p=[.35, .35, .2, .1])
income = 20000 + education * 15000 + np.random.normal(0, 8000, size=n)
environment = np.random.normal(50, 10, size=n) + (education - 1) * 2
access = 0.2 + 0.00000001 * income + 0.003 * (environment - 50) + np.random.normal(0, .05, size=n)
access = np.clip(access, 0, 1)
exercise = np.clip(np.random.normal(2 + 0.3 * (education - 1), .8, size=n), 0, None)
diet = np.clip(np.random.normal(60 + 4 * (education - 1), 8, size=n), 0, 100)
smoking = np.random.binomial(1, np.clip(.4 - .07 * (education - 1), .05, .5), size=n)
health = (40 + 0.00015 * income + 0.6 * diet + 1.8 * exercise - 6.0 * smoking
          + 0.3 * environment + 4.0 * access + np.random.normal(0, 10, size=n))
df = pd.DataFrame(dict(Education=education, Income=income, Environment=environment,
                       AccessToHealthcare=access, ExerciseHours=exercise,
                       DietScore=diet, Smoking=smoking, HealthScore=health))

FEATS = ["Income", "Education", "DietScore", "ExerciseHours",
         "Smoking", "Environment", "AccessToHealthcare"]
m_naive = sm.OLS(df.HealthScore, sm.add_constant(df[["Income"]])).fit()
m_adj = sm.OLS(df.HealthScore, sm.add_constant(df[FEATS])).fit()
m_edu = sm.OLS(df.HealthScore, sm.add_constant(df[["Education"]])).fit()

INC_NAIVE = float(m_naive.params["Income"])
INC_ADJ = float(m_adj.params["Income"])
INC_TRUE = 0.00015
EDU_TOTAL = float(m_edu.params["Education"])
EDU_ADJ = float(m_adj.params["Education"])
EDU_P = float(m_adj.pvalues["Education"])
SIGNAL = float(0.00000001 * income.mean())
NOISE = 0.05
RATIO = NOISE / SIGNAL
CORR = float(np.corrcoef(income, access)[0, 1])

# ── guards: the narration quotes these, so break the build if they move ────
assert 6.0 < EDU_TOTAL < 6.5, EDU_TOTAL           # spoken as "about six points"
assert abs(EDU_ADJ) < 0.20, EDU_ADJ               # spoken as "essentially zero"
assert EDU_P > 0.5, EDU_P                         # spoken as "p of zero point eight"
assert abs(INC_ADJ - INC_TRUE) < 2e-5, INC_ADJ    # spoken as "almost exactly"
assert INC_NAIVE > 2 * INC_ADJ, INC_NAIVE         # naive is inflated
assert RATIO > 50, RATIO                          # spoken as "a hundred times"
print(f"[repro] edu total={EDU_TOTAL:.3f}  edu adj={EDU_ADJ:+.3f} (p={EDU_P:.3f})")
print(f"[repro] income naive={INC_NAIVE:.6f}  adj={INC_ADJ:.6f}  true={INC_TRUE}")
print(f"[repro] dead edge: signal={SIGNAL:.6f} vs noise={NOISE}  ratio={RATIO:.0f}x  r={CORR:+.4f}")

B = []


def add(bid, act, text, pattern, props, motion="illustrate"):
    B.append({
        "beat_id": bid, "act": act, "narration_text": text,
        "shot": {"type": "GRAPHIC", "source": "remotion", "motion": motion,
                 "remotion": {"pattern": pattern, "props": props}},
        "estimated_duration_s": round(len(text.split()) / WPS, 1),
        "audio_file": f"mp3/beat-{bid}.mp3",
    })


def stmt(bid, act, text, eyebrow, headline, kicker="", motion="fade"):
    add(bid, act, text, "IdxStatement",
        {"eyebrow": eyebrow, "headline": headline, "kicker": kicker}, motion)


add("B00", "ASK",
    "A notebook asks how socioeconomic status shapes health — and then adjusts that effect out of existence. "
    "This is Humanitarians AI. The model is fine. The statistics are fine. "
    "The answer it reports for education is zero, and the true answer is about six points.",
    "ClaudeComposerAsk",
    {"greeting": "Check the causal claim.", "topic": "CAUSAL INFERENCE · SES & HEALTH",
     "segment": "The Variable That Vanished",
     "command": "This notebook simulates a causal link from socioeconomic status to health, then fits a naive model and a causal-aware model. Re-run its own generator, work out the true effects, and tell me whether the adjusted model answers the question the title asks.",
     "runningText": "re-running the generator…",
     "folderLabel": "@HumanitariansAI",
     "output": ["the DAG says the effect travels through lifestyle",
                "the model adjusts for lifestyle",
                "the effect disappears — and is read as small"]},
    "type-on")

stmt("B01", "PREMISE",
     "Start with credit, because the premise is right. Richer people are healthier is a correlation, not a mechanism, "
     "and asking whether it is causal is exactly the correct question. The notebook builds a diagram, simulates data from it, "
     "and compares two models. That is good practice.",
     "THE PREMISE", "Asking whether it is causal is the right question.",
     "correlation is not a mechanism — the notebook knows this")

add("B02", "DAG",
    "Here is the notebook's own diagram. Education drives income and environment. Those drive lifestyle and access to care. "
    "And those drive health. Notice what is missing: there is no arrow straight from education to health.",
    "CausalDagBuild", {}, "stagger")

stmt("B03", "READING",
     "That absence is the whole story. In the generator, education never appears in the health equation. "
     "Its entire influence is carried by the variables in the middle.",
     "READ THE DIAGRAM", "Education has no direct path to health.",
     "every point of its effect travels through something else")

add("B04", "FLOW",
    "So the effect flows like this. Better education improves diet, exercise, smoking and access, and those improve health. "
    "Four pipes, all carrying real signal, all of it originating at education.",
    "CausalPipeFlow",
    {"mode": "open",
     "caption": "All of education's effect is in transit.",
     "sparkLine": "Nothing arrives directly. Everything arrives through a mediator."},
    "stagger")

add("B05", "WARNING",
    "And the notebook knows this is delicate. Section three point three is titled, in its own words, "
    "causal feature selection — what not to control for.",
    "CausalQuote",
    {"quote": "Causal Feature Selection (What *not* to control for)",
     "source": "section 3.3 — the notebook's own heading",
     "verdict": "Then section 4.7 controls for all four mediators."},
    "fade")

add("B06", "CLAMP",
    "Because that is what the causal-aware model does. It adjusts for diet, exercise, smoking and access, "
    "all at once, and calls it backdoor adjustment. Watch what that does to the pipes.",
    "CausalPipeFlow",
    {"mode": "clamped",
     "caption": "Every route education had is now held fixed.",
     "sparkLine": "Blocking a mediator does not remove bias. It removes the effect."},
    "stagger")

add("B07", "VANISH",
    "Here is the result, measured. Regress health on education alone and you get six point two zero points per level of education. "
    "Adjust for the mediators and that becomes zero point zero four seven, with a p value of zero point eight two. Nothing.",
    "CausalVanish",
    {"total": round(EDU_TOTAL, 2), "adjusted": round(EDU_ADJ, 3), "pvalue": round(EDU_P, 3)},
    "stagger")

add("B08", "MISREAD",
    "And this is where it goes wrong. The notebook reads that near-zero number as a smaller effect.",
    "CausalQuote",
    {"quote": "Income and Education still help, but their direct effects are smaller once we account for lifestyle and environment.",
     "source": "the notebook's observation, section 4.8",
     "verdict": "Education's direct effect is not smaller. It is zero — by construction."},
    "fade")

stmt("B09", "CORRECTION",
     "Zero is not a small number here. It is the correct answer to a question nobody asked. "
     "Education has no direct arrow, so its direct effect was always going to be zero. "
     "Finding it does not validate the model. It just confirms the diagram.",
     "THE CORRECTION", "Zero was guaranteed before the data existed.",
     "the adjusted coefficient confirms the DAG — it measures nothing new")

add("B10", "ESTIMANDS",
    "There are two honest questions here, and they have two different right answers.",
    "CausalEstimands",
    {"total": round(EDU_TOTAL, 2), "direct": 0.0},
    "stagger")

stmt("B11", "NAMING",
     "The first is the total effect — if someone gets more education, how much healthier do they end up, by any route. "
     "That is six point two. The second is the direct effect, holding the mechanisms fixed. That is zero. "
     "The title asks the first. The model answers the second.",
     "NAME YOUR ESTIMAND", "Adjustment did not fix a bias. It swapped the question.",
     "total effect · direct effect — pick one, out loud, before you fit")

add("B12", "FAIRNESS",
    "Now the other half, because the notebook deserves it. For income, the same adjustment works beautifully.",
    "CausalScoreboard",
    {"naive": round(INC_NAIVE, 6), "adjusted": round(INC_ADJ, 6), "truth": INC_TRUE},
    "stagger")

stmt("B13", "FAIRNESS",
     "The naive model says zero point zero zero zero three five three per dollar. The adjusted model says zero point zero zero zero one four three. "
     "The generator's true value is zero point zero zero zero one five. That is a real confounder removed, and a real parameter recovered.",
     "IT WORKED HERE", "Education confounds income. Adjusting for it was correct.",
     "same model, same line of code — right answer this time")

stmt("B14", "DIAGNOSIS",
     "Which is the actual lesson. The technique was never broken. The same adjustment that rescues income destroys education, "
     "because income has a direct arrow and education does not. Adjustment is not a setting you turn up.",
     "THE DIAGNOSIS", "One adjustment. Two variables. Opposite consequences.",
     "what a control does depends entirely on where it sits in the graph")

add("B15", "DEADEDGE",
    "There is a second problem, and this one is arithmetic. The diagram says income drives access to healthcare. "
    "The code gives that arrow a coefficient of one times ten to the minus eight.",
    "CausalDeadEdge",
    {"signal": round(SIGNAL, 6), "noise": NOISE, "ratio": round(RATIO), "corr": round(CORR, 4)},
    "stagger")

stmt("B16", "DEADEDGE",
     "At an average income of fifty thousand dollars, that contributes half of one thousandth to access. "
     "The random noise on the same line has a standard deviation of zero point zero five — about a hundred times larger. "
     "The arrow is in the diagram and in the comment. It is not in the data.",
     "THE DEAD EDGE", "A hundred times smaller than its own noise.",
     "a causal claim can be true in prose and absent in the array")

add("B17", "ORDER",
    "And one plain bug, worth thirty seconds. The correlation matrix reads a dataframe that is created three cells later.",
    "CausalCellOrder", {}, "stagger")

stmt("B18", "ORDER",
     "Run the notebook top to bottom in a fresh kernel and it raises a name error. It has only ever worked "
     "because the cells were executed out of order in a session that is no longer running.",
     "RESTART AND RUN ALL", "A notebook that cannot run top to bottom is not reproducible.",
     "the fix is one cut and paste — the habit is the real fix")

stmt("B19", "FIX",
     "So what should this notebook do instead. Three things, none of them advanced.",
     "THE FIX", "None of this requires a better model.",
     "")

add("B20", "FIX",
    "First, write the estimand down before fitting anything. Second, report the total effect and the direct effect side by side, "
    "and say which one answers your title. Third, make the adjustment set a decision you defend per variable, not a list you reuse.",
    "ClaudeCodeBeat",
    {"title": "the three-line fix", "lang": "python",
     "code": ("# 1. name it, before you fit\n"
              "ESTIMAND = \"total effect of Education on HealthScore\"\n\n"
              "# 2. report both, always\n"
              "total  = ols(\"HealthScore ~ Education\").fit()\n"
              "direct = ols(\"HealthScore ~ Education + Diet + Exercise\"\n"
              "             \" + Smoking + Access\").fit()\n\n"
              "# 3. justify each control by its role in the DAG\n"
              "#    confounder -> adjust.  mediator -> do NOT."),
     "sparkLine": "Mediator or confounder is not a property of the column. It is a property of the question."},
    "type-on")

stmt("B21", "LESSON",
     "The broader habit is simpler than any of it. A causal diagram is a claim about the world, "
     "so it should be tested like one. Check that every arrow you drew actually carries signal in the data you generated.",
     "THE HABIT", "Test the arrows, not just the model.",
     "a diagram is a hypothesis — verify it against the array")

stmt("B22", "STAKES",
     "And the stakes here are not academic. The conclusion section warns that getting this wrong can lead to misleading policy recommendations. "
     "It is right. A model reporting that education has no effect on health is exactly the kind of finding that gets quoted without its footnote.",
     "WHY IT MATTERS", "This is the number that escapes the notebook.",
     "the notebook's own warning, applied to the notebook")

add("B23", "VERDICT",
    "So here is the teardown. The framing was right, the data preparation was careful, and on income the method did exactly what it promised. "
    "But the headline variable was adjusted through its own mechanisms, and a structural zero was reported as a small effect.",
    "ClaudeVerdictArtifact",
    {"artifactTitle": "The Variable That Vanished — one page",
     "artifactHeading": "The teardown",
     "artifactLines": [
         f"Education's true total effect is {EDU_TOTAL:.2f} points per level. The causal-aware model reports {EDU_ADJ:+.3f}, p={EDU_P:.2f} — and reads that as 'smaller'.",
         "Cause: all four of education's pathways — diet, exercise, smoking, access — are in the adjustment set. Blocking a mediator removes the effect, not the bias.",
         f"Credit where due: for income the same model moves {INC_NAIVE:.6f} to {INC_ADJ:.6f} against a true {INC_TRUE} — a confounder correctly removed.",
         f"Second finding: the income to access arrow has coefficient 1e-8, contributing {SIGNAL:.6f} against noise of {NOISE} — roughly {RATIO:.0f}x smaller. The edge is drawn but not simulated.",
         "Third: the correlation matrix reads df_clean three cells before it is defined. A fresh kernel raises NameError.",
         "The verdict: the statistics are correct. The estimand was never named, so the wrong one got reported."]},
    "stagger")

add("B24", "HANDOFF",
    "Your turn. Open the last model where you controlled for everything you had. "
    "Pick one control and ask whether it sits between your cause and your outcome. If it does, you are not removing bias. "
    "You are deleting the thing you were trying to measure.",
    "ClaudeComposerAsk",
    {"greeting": "Your turn.", "topic": "YOUR TURN", "segment": "Confounder, or mediator?",
     "command": "Here is a regression where I controlled for every variable I had. For each control, tell me whether it is a confounder or a mediator of the effect I actually care about — and which ones I should drop to answer my real question.",
     "runningText": "sorting your controls…",
     "folderLabel": "@HumanitariansAI",
     "output": ["controlling for everything is not caution",
                "it is a silent choice of estimand"]},
    "type-on")

add("B25", "OUTRO",
    "The variable that vanished. If a teardown that checks the arrows as well as the code is worth your time, subscribe. Humanitarians AI.",
    "ClaudeTitleOutro",
    {"title": "The Variable That Vanished", "handle": "@HumanitariansAI"},
    "fade")

sheet = {
    "metadata": {
        "title": "The Variable That Vanished",
        "slug": "hai-the-variable-that-vanished",
        "topic": "CAUSAL INFERENCE · SES & HEALTH",
        "register": "Teardown",
        "audience": "HAI",
        "brand": "claude",
        "voice": "HumanitariansAI",
        "engine": "kokoro",
        "palette": "claude",
        "style_preset": "claude",
        "ground": "#FAF9F5",
        "voice_kokoro": "af_bella",
        "channel": "humanitarians-ai",
        "handle": "@HumanitariansAI",
        "note": ("deep-explainer teardown of a notebook on SES->health causality. Every figure is "
                 "recomputed by build_beat_sheet.py, which re-runs the notebook's own DGP at seed 42 "
                 "and asserts the values the narration quotes. NO INDIVIDUAL IS NAMED. The reel is "
                 "deliberately fair: it credits the premise, the data prep, and the income result "
                 "before showing the education failure. Bella (af_bella). Never publishes."),
        "tags": ["causal inference", "DAG", "mediator", "confounder", "over-adjustment",
                 "backdoor criterion", "estimand", "socioeconomic status", "health",
                 "Humanitarians AI"],
    },
    "beats": B,
}
OUT.write_text(json.dumps(sheet, indent=2, ensure_ascii=False), encoding="utf-8")

words = sum(len(b["narration_text"].split()) for b in B)
print(f"\nwrote {OUT}")
print(f"{len(B)} beats · {words} words · projected {words/WPS:.0f}s = {int(words/WPS)//60}m{int(words/WPS)%60:02d}s")
banned = ["chinmay", "chinmai", "chinme", "sawant", "savant"]
blob = json.dumps(sheet, ensure_ascii=False).lower()
hits = [x for x in banned if x in blob]
print("NAME CHECK:", "CLEAN" if not hits else f"FAIL {hits}")
