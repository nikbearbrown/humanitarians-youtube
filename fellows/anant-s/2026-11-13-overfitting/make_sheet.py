"""Builds beat_sheet.json for "Overfitting, When a Perfect Score Lies".

On-screen numbers are read from demo/evidence.json (produced by demo/overfit_demo.py), never typed.
Narration speaks numbers as words; make_sheet asserts each spoken figure still matches the evidence.
Re-running this OVERWRITES beat_sheet.json (drops measured audio fields) — rerun audio after.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ev = json.loads((HERE / "demo" / "evidence.json").read_text(encoding="utf-8"))
S = ev["setup"]
W = ev["worked"]
SW = ev["sweep"]
BEST = ev["sweep_best"]
MD = {m["n_train"]: m for m in ev["more_data"]}
SEL = ev["selection"]
MX = ev["mse_example"]

TITLE = "Overfitting, When a Perfect Score Lies"
SLUG = "claude-liam-overfitting"
TOPIC = "MACHINE LEARNING · OVERFITTING"
GREETING = "Namaste, Liam"


def f(x, nd=3):
    """On-screen number format: thousands separators, trailing zeros trimmed."""
    if abs(x) >= 1000:
        return f"{x:,.1f}"
    return f"{x:.{nd}f}".rstrip("0").rstrip(".") if x else "0"


# ---- guard the spoken figures against the evidence (numbers-as-words drift check) ----
assert S["n_train"] == 16 and S["n_test"] == 1000 and abs(S["noise_floor_mse"] - 0.04) < 1e-12
assert W["15"]["train_mse"] == 0 and 9500 <= W["15"]["test_mse"] < 10000          # "zero" / "almost ten thousand"
assert round(W["1"]["train_mse"], 2) == 0.28 and round(W["1"]["test_mse"], 2) == 0.27  # "zero point two eight / two seven"
assert round(W["3"]["train_mse"], 2) == 0.06 and round(W["3"]["test_mse"], 3) == 0.047
assert 3 <= BEST["degree"] <= 6 and BEST["test_mse"] < 0.05                         # "around degree three to six"
assert ev["sweep_500"]["best_degree_by_median_test"] == 3
assert round(MD[20]["test_mse"]) == 29 and round(MD[100]["test_mse"], 3) == 0.048 and round(MD[1000]["test_mse"], 3) == 0.041
assert round(MD[1000]["train_mse"], 3) == 0.041
assert round(SEL["peek"]["share_optimistic"], 1) == 0.7                              # "seven times in ten"
assert 0.45 <= SEL["untouched_test"]["share_optimistic"] <= 0.56                     # "about half"
assert round(SEL["untouched_test"]["median_reported"], 3) == round(SEL["untouched_test"]["median_real"], 3)
assert len(ev["data"]["train"]) == 16


def manim(bid, cls, act, content_type, narration, show, visual_intent, motion_claim):
    return {"beat_id": bid, "act": act, "content_type": content_type, "lane": "manim",
            "narration_text": narration,
            "shot": {"type": "GRAPHIC", "source": "own", "motion": "drawon",
                     "manim": {"class": cls, "file": "scenes.py"},
                     "show": show, "visual_intent": visual_intent, "motion_claim": motion_claim}}


def remotion(bid, act, pattern, props, narration, show, motion, **extra):
    b = {"beat_id": bid, "act": act, "lane": "remotion", "narration_text": narration,
         "shot": {"type": "GRAPHIC", "source": "remotion", "motion": motion, "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


beats = []

# ---------------------------------------------------------------- B00 cold open
ask = ("My model scored zero error on its training data. Perfect. "
       "Should I trust it? Show me with real numbers.")
beats.append(remotion("B00", "ASK", "ClaudeComposerAsk", {
    "greeting": GREETING, "topic": TOPIC, "segment": TITLE, "command": ask,
    "runningText": "fitting sixteen noisy points…",
    "output": [f"degree 15: training error {f(W['15']['train_mse'])}, test error {f(W['15']['test_mse'])}",
               f"degree 3: training error {f(W['3']['train_mse'], 4)}, test error {f(W['3']['test_mse'], 4)}",
               "the honest grade comes from data the model never saw"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Namaste, this is Liam, in for Bear. The ask: my model scored zero error on its training data. "
    "Perfect. Should I trust it? Show me with real numbers.",
    [{"at": 0.02, "event": "composer card fades in on cream"},
     {"at": 0.10, "event": "greeting 'Namaste, Liam' types above the composer"},
     {"at": 0.30, "event": "the ask types in"},
     {"at": 0.72, "event": "runningText 'fitting sixteen noisy points…' appears"},
     {"at": 0.84, "event": "three result lines cascade in; '9,882.6' is the one terracotta moment"}],
    "type-on", role_note="COLD OPEN LAW — ask lands answered; Liam introduced in first breath."))

# ---------------------------------------------------------------- B01 BLUF
beats.append(remotion("B01", "BLUF", "BrutalistHesitantWriter", {
    "text": "A perfect training score\nmeans a perfect model.",
    "triggerWords": "means a perfect model", "replacementWords": "can mean memorized noise",
    "seed": "claude-liam-overfitting-b01", "face": "serif", "fontSize": 150,
    "lineSpacing": 3.1, "align": "center", "charMs": 28, "jitter": 18,
    "mistakeRate": 0, "hesitateWithin": 0, "hesitateBetween": 0},
    "A perfect training score can mean memorized noise. A model flexible enough to pass through "
    "every point it was shown has learned the points, not the pattern, and stumbles on the next one.",
    [{"at": 0.0, "event": "cream page holds; caret blinks"},
     {"at": 0.12, "event": "types 'A perfect training score / means a perfect model.'"},
     {"at": 0.50, "event": "'means a perfect model' turns terracotta, hesitates, backspaces"},
     {"at": 0.65, "event": "types 'can mean memorized noise'"},
     {"at": 0.90, "event": "final lines settle: 'A perfect training score / can mean memorized noise.'"}],
    "hesitant-type", lead_silence_s=0.8,
    role_note="EXECUTIVE-SUMMARY LAW — misconception corrected: a perfect score on the data you "
              "trained on is not evidence of a good model; it can be evidence of memorized noise."))

# ---------------------------------------------------------------- body
beats.append(manim("B02", "B02_Setup", "FRAMEWORK", "structure",
    "Here's the setup. A smooth curve, the truth, which the model never gets to see. Sixteen points "
    "drawn from it, each knocked off by random noise: that's the training set. A thousand more, drawn "
    "the same way and locked away: the test set. The model fits the sixteen. We grade it on the "
    "thousand it has never seen.",
    [{"at": 0.03, "event": "axes draw on, x from −1 to 1"},
     {"at": 0.10, "event": "dashed curve y = sin(πx) draws on; tag 'the truth (hidden from the model)'"},
     {"at": 0.30, "event": "16 ink dots drop onto the curve, then each jumps off it by its noise; "
                           "faint tick joins each dot to the curve"},
     {"at": 0.45, "event": "bracket chip: 'training set · 16 points'"},
     {"at": 0.62, "event": "60 faint hollow dots (preview of the 1,000) fade in beside, then slide into "
                           "a box labelled 'test set · 1,000 points · locked'"},
     {"at": 0.82, "event": "the dashed truth curve fades to 40% (the model can't see it); "
                           "labels 'fit on these' under the training dots and 'grade on these' under the test box; 'grade' is terracotta"}],
    "The data-generating picture: hidden true curve, 16 noisy training points, a locked 1,000-point test set.",
    "Each dot visibly leaves the curve by its own noise, so 'noise' is a seen displacement, not a word."))

beats.append(manim("B03", "B03_ErrorMeasure", "FRAMEWORK", "equation",
    "The grade is one number, the mean squared error. For each point, take the gap between the real "
    "value and the model's guess, and square it, so misses above and below both count, and big misses "
    "count most. Then average over every point. On the training points, that's training error. On the "
    "test points, test error. Zero means every point was hit exactly.",
    [{"at": 0.04, "event": "MathTex typesets: MSE = (1/n) Σᵢ₌₁ⁿ (yᵢ − f̂(xᵢ))²"},
     {"at": 0.18, "event": "box spotlight on yᵢ: 'real value'; box spotlight on f̂(xᵢ): 'model's guess'"},
     {"at": 0.28, "event": "box spotlight on the '−' and the square: 'gap, squared'"},
     {"at": 0.42, "event": f"worked term slides in under the equation: one training point, the line's "
                           f"worst miss: gap {f(MX['gap'], 3)}, squared {f(MX['gap_squared'], 3)}"},
     {"at": 0.55, "event": f"box spotlight on (1/n) Σ: 'average over all {MX['n']}': "
                           f"{f(MX['sum_squared'], 3)} ÷ {MX['n']} = {f(MX['mse'], 3)}"},
     {"at": 0.72, "event": "two chips under the equation: 'on training points → training error' | "
                           "'on test points → test error'"},
     {"at": 0.90, "event": "chip 'MSE = 0 · every point hit exactly'; the spotlight box moves onto it"}],
    "The error measure, typeset, with a glossary spotlight per symbol and one real worked term.",
    "Box spotlights walk the formula in narration order; the worked term is a real point from the data."))

beats.append(manim("B04", "B04_ThreeFits", "WORKED_EXAMPLE", "mechanism",
    "Fit three models to the same sixteen points. A straight line, degree one, is too stiff: it "
    "misses the bend, at about zero point two eight in training, zero point two seven on test. "
    "Degree three follows the curve: zero point zero six, and zero point zero four seven. Degree "
    "fifteen has sixteen coefficients for sixteen points, so it threads every one. Training error: "
    "zero. Test error: almost ten thousand.",
    [{"at": 0.03, "event": "three panels side by side, the same 16 dots in each; headers 'degree 1', "
                           "'degree 3', 'degree 15'"},
     {"at": 0.12, "event": f"left: straight line draws through the dots; counters train "
                           f"{f(W['1']['train_mse'])} | test {f(W['1']['test_mse'])}"},
     {"at": 0.42, "event": f"middle: cubic draws, hugging the hidden curve; counters "
                           f"{f(W['3']['train_mse'])} | {f(W['3']['test_mse'])}"},
     {"at": 0.65, "event": "right: degree-15 curve threads every dot, swinging off the panel between "
                           "them (clipped at the frame, arrow marks the exit)"},
     {"at": 0.82, "event": "right counter train → 0"},
     {"at": 0.92, "event": f"right counter test spins up to {f(W['15']['test_mse'])} in terracotta"}],
    "Underfit, good fit, overfit on identical data, with executed train/test errors under each panel.",
    "The three curves draw in narration order; the degree-15 curve visibly passes through every dot "
    "and leaves the frame between them."))

beats.append(manim("B05", "B05_TheU", "MECHANISM", "data",
    "Do that for every degree from zero to fifteen. Training error, in ink, only ever goes down: a "
    "more flexible model can always fit the same points at least as well. Test error falls too, at "
    "first. It bottoms out around degree three to six, just above the dashed line, which is the noise "
    "itself. Then it turns, climbs, and leaves the chart. That U is overfitting.",
    [{"at": 0.03, "event": "axes: x 'degree 0–15', y 'error 0–0.6'; dashed floor line at 0.040: "
                           "'noise floor: even the true curve scores " + f(S["truth_test_mse"], 3) + "'"},
     {"at": 0.12, "event": "ink training-error dots land degree by degree, stepping down to 0 at 15"},
     {"at": 0.40, "event": "test-error dots land degree by degree, falling with the ink ones"},
     {"at": 0.55, "event": f"minimum ringed at degree {BEST['degree']}: {f(BEST['test_mse'], 4)}"},
     {"at": 0.72, "event": "test dots climb, then exit the top from degree 11; terracotta exit chips "
                           + " · ".join(f(s["test_mse"], 1) for s in SW[11:])},
     {"at": 0.90, "event": "label 'overfitting' and chip 'same shape in 500 fresh datasets' land in the empty upper right"}],
    "Training vs test error across all 16 degrees, executed on the film's dataset, with the noise floor.",
    "The two series land degree by degree so the divergence happens on screen; the test curve leaves the chart."))

beats.append(manim("B06", "B06_MoreData", "FALSIFIABILITY", "mechanism",
    "Here's where the simple story bends. Is degree fifteen just too complex? Keep the model, and add "
    "data. At twenty points, test error drops to about twenty-nine. At a hundred, zero point zero four "
    "eight. At a thousand, zero point zero four one, right on the noise floor, and training error has "
    "risen from zero to meet it. Complexity alone isn't the problem. Complexity the data can't pin "
    "down is.",
    [{"at": 0.03, "event": "the degree-15 panel from B04, wild curve over 16 dots; counter n = 16"},
     {"at": 0.22, "event": f"dots multiply to 20; curve refits; test counter {f(MD[20]['test_mse'], 1)}"},
     {"at": 0.42, "event": f"dots multiply to 100; curve calms; test {f(MD[100]['test_mse'], 3)}"},
     {"at": 0.58, "event": f"1,000 dots; curve lies on the hidden truth; test {f(MD[1000]['test_mse'], 3)}"},
     {"at": 0.70, "event": "side ladder: train ↑ and test ↓ counters for n = "
                           + ", ".join(f"{n} ({f(MD[n]['train_mse'], 3)} | {f(MD[n]['test_mse'], 3)})" for n in MD)},
     {"at": 0.82, "event": "both counters meet at the dashed 0.040 floor; terracotta ring on the meeting point"}],
    "One fixed degree-15 model tamed by more data (nested training sets, executed).",
    "The same model refits live as the data grows; train and test errors converge on the floor."))

beats.append(manim("B07", "B07_PeekedScore", "FALSIFIABILITY", "data",
    "One more way a score can lie. Say you try all sixteen degrees and keep whichever scores best on a "
    "held-out validation set. Now that score helped choose the model. Across a thousand repeats, it "
    "came in better than the real error seven times in ten. The fix: choose on validation, then report "
    "on a test set nobody touched. That lands about half and half, as an honest score should.",
    [{"at": 0.03, "event": "data strip splits into three labelled blocks: 'train 30 · validation 20 · test 20'"},
     {"at": 0.18, "event": "sixteen degree chips 0–15 appear; validation's pick (the most-picked degree) gets a box"},
     {"at": 0.40, "event": "left panel 'choose and report on validation': a 10×10 grid of 100 trials "
                           "fills; optimistic trials fill terracotta"},
     {"at": 0.55, "event": f"left counter: {round(SEL['peek']['share_optimistic'] * 100)}% optimistic; "
                           f"median reported {f(SEL['peek']['median_reported'], 4)} vs real "
                           f"{f(SEL['peek']['median_real'], 4)}"},
     {"at": 0.75, "event": "right panel 'choose on validation, report on untouched test' fills the same way"},
     {"at": 0.88, "event": f"right counter: {round(SEL['untouched_test']['share_optimistic'] * 100)}% "
                           f"optimistic; median {f(SEL['untouched_test']['median_reported'], 4)} vs "
                           f"{f(SEL['untouched_test']['median_real'], 4)}; reference chip 'degree fixed in "
                           f"advance: {round(SEL['control_fixed_degree_3']['share_optimistic'] * 100)}%'"}],
    "Selection bias from reusing a held-out score, measured over 1,000 executed repeats, with a control.",
    "The two trial grids fill side by side and are held together, so the 70 vs 55 comparison is seen."))

# ---------------------------------------------------------------- closing block
beats.append(remotion("BVDT", "VERDICT", "ClaudeVerdictArtifact", {
    "artifactTitle": "Verdict", "artifactHeading": "Overfitting, in six lines",
    "artifactLines": ["Training error grades the model on answers it has already seen.",
                      "Test error, on data held back, is the honest grade.",
                      "As flexibility grows, training error falls; test error falls, then climbs.",
                      "A perfect training score can mean the noise was memorized.",
                      "More data lets a flexible model behave.",
                      "A score you chose by is spent; keep one test set untouched."]},
    "Let's recap with Claude. Training error grades the model on answers it has already seen. Test "
    "error, on data held back, is the honest grade. As flexibility grows, training error falls; test "
    "error falls, then climbs. A perfect training score can mean the noise was memorized. More data "
    "lets a flexible model behave. And a score you chose by is spent, so keep one test set untouched.",
    [{"at": 0.05, "event": "verdict artifact card in on cream"},
     {"at": 0.15, "event": "heading types"},
     {"at": 0.25, "event": "lines 1–6 land on their spoken cue"}],
    "artifact-in", lead_silence_s=0.5))

prompt = ("Using only Python and NumPy, draw 16 points from y = sin(pi x) on the interval from -1 to 1, "
          "with Gaussian noise of standard deviation 0.2, plus 1000 more as a test set. Fit polynomials "
          "of degree 0 to 15 and print the training and test error for each. Repeat with 200 training "
          "points. Then, from the printed numbers only, tell me which degree you would ship in each "
          "case, and how you chose it.")
prompt_spoken = ("Using only Python and NumPy, draw sixteen points from y equals sine of pi x on the "
                 "interval from minus one to one, with Gaussian noise of standard deviation zero point "
                 "two, plus a thousand more as a test set. Fit polynomials of degree zero to fifteen and "
                 "print the training and test error for each. Repeat with two hundred training points. "
                 "Then, from the printed numbers only, tell me which degree you would ship in each case, "
                 "and how you chose it.")
beats.append(remotion("BHTF", "YOUR_TURN", "ClaudeComposerAsk", {
    "greeting": "Your turn.", "topic": "YOUR TURN · OVERFITTING",
    "segment": "Catch a model memorizing", "command": prompt,
    "runningText": "paste this into Claude…",
    "output": ["check: training error never rises as the degree goes up",
               "check: 16 points, degree 15 → training error ≈ 0, test error huge",
               "check: the degree is chosen without peeking at the test set"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Your turn. Paste this into Claude: " + prompt_spoken + " "
    "Here's what to check. Training error should never go up as the degree rises. With sixteen "
    "points, degree fifteen should score essentially zero in training and something enormous on test. And watch "
    "how Claude picks the degree. If it picks by the test error, ask it what it should have used instead.",
    [{"at": 0.02, "event": "composer card in on cream"},
     {"at": 0.08, "event": "greeting 'Your turn.' types"},
     {"at": 0.15, "event": "the prompt types into the composer"},
     {"at": 0.62, "event": "runningText 'paste this into Claude…'"},
     {"at": 0.72, "event": "three check lines cascade in as each is spoken"}],
    "type-on", role_note="HANDOFF LAW — prompt read aloud verbatim (numbers spoken as words), "
                         "then a 3-point rubric; the third check tests the B07 lesson."))

beats.append(remotion("BOUT", "OUTRO", "ClaudeTitleOutro", {"title": TITLE + ".", "handle": "@NikBearBrown", "slug": SLUG},
    f"{TITLE}. At Nik Bear Brown.",
    [{"at": 0.02, "event": "cream page; polarity seeded from slug"},
     {"at": 0.10, "event": "title types"}, {"at": 0.55, "event": "handle @NikBearBrown"},
     {"at": 0.70, "event": "slug-seeded mascot animates under the handle"}],
    "outro-card", kind="outro_voice", tail_silence_s=1.0,
    role_note="OUTRO-LOCK — exact title restate, hardcoded handle, spoken, no music."))

sheet = {"metadata": {
    "title": TITLE, "slug": SLUG, "topic": TOPIC, "skill": "ai-explainer",
    "brand": "claude-liam", "channel": "claude-liam", "audience": "makers and curious learners new to ML",
    "register": "Teardown", "engine": "kokoro", "voice": "am_onyx", "voice_kokoro": "am_onyx",
    "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5", "aspect_ratio": "16:9",
    "greeting": GREETING, "persona": "Liam (in for Bear)", "in_for_bear": True,
    "folderLabel": "@NikBearBrown", "captions": False, "series_index": 3,
    "evidence": "demo/overfit_demo.py -> demo/evidence.json, demo/RUN-LOG.txt",
    # espeak gives "Namaste" as /nˈæmæst/ (drops the final syllable); pinned to NUH-muh-stay.
    "pronounce": {"Namaste": "nˈʌməstˌeɪ"},
    "tags": ["overfitting", "machine learning", "generalization", "test set", "validation set",
             "polynomial regression", "bias-variance"]},
    "beats": beats}

# ---- spine / length guards --------------------------------------------------------------
wc = {b["beat_id"]: len(b["narration_text"].split()) for b in beats}
assert 20 <= wc["B01"] <= 35, wc["B01"]
for b in beats:
    if b["beat_id"].startswith("B0") and b["beat_id"] not in ("B00", "B01"):
        assert 45 <= wc[b["beat_id"]] <= 70, (b["beat_id"], wc[b["beat_id"]])
assert len(beats[-3]["shot"]["remotion"]["props"]["artifactLines"]) in (4, 6)
assert beats[0]["narration_text"].startswith("Namaste, this is Liam, in for Bear.")
assert prompt_spoken in beats[-2]["narration_text"]

(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")

for b in beats:
    n = wc[b["beat_id"]]
    print(f"{b['beat_id']:5} {b.get('act',''):15} {n:4} words  ~{n/3.5:5.1f}s @3.5w/s  ~{n/2.6:5.1f}s @2.6w/s")
total = sum(wc.values())
print(f"total {total} words  ~{total/3.5/60:.2f} min (3.5 w/s)  ~{total/2.6/60:.2f} min (2.6 w/s)")
