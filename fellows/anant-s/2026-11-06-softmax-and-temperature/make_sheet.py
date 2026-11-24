"""Builds beat_sheet.json for "Softmax and Temperature, Explained".

On-screen numbers are read from demo/evidence.json (produced by demo/softmax_demo.py), never typed.
The narration speaks numbers as words; the CLAIMS block below asserts that every spoken number
still matches the evidence, so a re-run of the demo with different data fails loudly here.
Re-running this OVERWRITES beat_sheet.json (drops measured audio fields) — rerun audio after.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ev = json.loads((HERE / "demo" / "evidence.json").read_text(encoding="utf-8"))
TOK, Z = ev["tokens"], ev["logits"]
W = ev["worked"]
SW = ev["sweep"]
R20 = ev["runs20"]["by_T"]
K10 = ev["draws10k"]
TZ = {g["T"]: g for g in ev["toward_zero"]}
WR = ev["wrong_ranking"]

TITLE = "Softmax and Temperature, Explained"
SLUG = "claude-liam-softmax-temperature"
TOPIC = "LANGUAGE MODELS · SOFTMAX AND TEMPERATURE"
GREETING = "Bonjour, Liam"


def pct(x):
    """51.0 -> '51%', 22.9 -> '22.9%' (one decimal unless whole)."""
    return (f"{x:.0f}" if float(x).is_integer() else f"{x:.1f}") + "%"


def lg(z):
    return f"{z:g}".replace("-", "−")


# ---------------------------------------------------------------- CLAIMS (spoken numbers vs evidence)
mat = TOK.index("mat")
roof = TOK.index("roof")
assert TOK == ["mat", "floor", "couch", "bed", "roof"] and Z[mat] == 3.2 and Z[roof] == 0.3   # B04
assert round(W["exp"][mat], 1) == 24.5 and W["exp"][roof] == 1.35                              # B04 "twenty-four and a half", "one point three five"
assert round(W["sum"]) == 48                                                                   # B04 "about forty-eight"
assert [round(p) for p in W["pct"]] == [51, 23, 14, 9, 3]                                      # B04 spoken shares
assert round(SW["0.2"]["pct"][mat]) == 98 and round(SW["2.0"]["pct"][mat]) == 35               # B05
assert round(SW["2.0"]["pct"][roof]) == 8 and SW["0.2"]["pct"][roof] < 0.05                   # B05 "almost nothing to eight"
assert ev["order_preserved"]                                                                   # B05 "the order never changes"
assert R20["0.2"]["counts"]["mat"] == 20                                                       # B06 "twenty times out of twenty"
assert R20["1.0"]["distinct"] == 4 and R20["2.0"]["distinct"] == 5                             # B06 "four different words", "all five"
assert R20["2.0"]["counts"]["roof"] >= 1                                                       # B06 "even roof"
assert K10["1.0"]["predicted_pct"][mat] == 51.0 and K10["1.0"]["observed_pct"][mat] == 51.3    # B07
assert all(d["max_abs_gap_pct"] < 1.0 for d in K10.values())                                   # B07 "nothing misses by even one point"
assert round(TZ[0.5]["pct_top"]) == 76 and TZ[0.1]["pct_top"] == 99.97                        # B08
wr1, wr02, wr2 = WR["1.0"], WR["0.2"], WR["2.0"]
assert WR["tokens"][0] == "Sydney" and WR["greedy_pick"] == "Sydney"                           # B09 "greedy: wrong every time"
assert abs(wr1["pct_wrong_cities"] - 200 / 3) < 0.5                                            # B09 "two times in three"
assert wr02["pct_wrong_cities"] > 80                                                           # B09 "more than four times in five"
assert wr2["pct_correct"] < wr1["pct_correct"]                                                 # B09 "Canberra actually slips"
assert wr2["pct"][2] > wr1["pct"][2] and wr2["pct"][3] > wr1["pct"][3]                         # B09 "Melbourne and Perth take the extra"


def manim(bid, cls, act, content_type, narration, show, visual_intent, motion_claim, **extra):
    b = {"beat_id": bid, "act": act, "content_type": content_type, "lane": "manim",
         "narration_text": narration,
         "shot": {"type": "GRAPHIC", "source": "own", "motion": "drawon",
                  "manim": {"class": cls, "file": "scenes.py"},
                  "show": show, "visual_intent": visual_intent, "motion_claim": motion_claim}}
    b.update(extra)
    return b


def remotion(bid, act, pattern, props, narration, show, motion, **extra):
    b = {"beat_id": bid, "act": act, "lane": "remotion", "narration_text": narration,
         "shot": {"type": "GRAPHIC", "source": "remotion", "motion": motion, "show": show,
                  "remotion": {"pattern": pattern, "props": props}}}
    b.update(extra)
    return b


beats = []

# ---------------------------------------------------------------- B00 cold open
ask = ("Why does the same prompt give me a different answer every time? "
       "Show me the math underneath, with real numbers.")
beats.append(remotion("B00", "ASK", "ClaudeComposerAsk", {
    "greeting": GREETING, "topic": TOPIC, "segment": TITLE, "command": ask,
    "runningText": "working through the math…",
    "output": ["the model scores every next token; softmax turns the scores into odds",
               f"temperature reshapes the odds: 'mat' is {pct(SW['0.2']['pct'][mat])} at T = 0.2, "
               f"{pct(SW['1.0']['pct'][mat])} at 1, {pct(SW['2.0']['pct'][mat])} at 2",
               "then it rolls weighted dice: same odds, different rolls, different answers"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Bonjour, this is Liam, in for Bear. The ask: why does the same prompt give me a different "
    "answer every time? Show me the math underneath, with real numbers.",
    [{"at": 0.02, "event": "composer card fades in on cream"},
     {"at": 0.10, "event": f"greeting '{GREETING}' types above the composer"},
     {"at": 0.30, "event": "the ask types in"},
     {"at": 0.72, "event": "runningText 'working through the math…' appears"},
     {"at": 0.84, "event": "three result lines cascade in"}],
    "type-on", role_note="COLD OPEN LAW — ask lands answered; Liam introduced in first breath."))

# ---------------------------------------------------------------- B01 BLUF
beats.append(remotion("B01", "BLUF", "BrutalistHesitantWriter", {
    "text": "A language model\npicks the likeliest word.",
    "triggerWords": "picks the likeliest word", "replacementWords": "rolls weighted dice",
    "seed": "claude-liam-softmax-temperature-b01", "face": "serif", "fontSize": 190,
    "lineSpacing": 3.0, "align": "center", "charMs": 28, "jitter": 18,
    "mistakeRate": 0, "hesitateWithin": 0, "hesitateBetween": 0},
    "A language model rolls weighted dice for every word it writes. Softmax sets the weights. "
    "Temperature decides how lopsided they are. That's why the same prompt can come back different.",
    [{"at": 0.0, "event": "cream page holds; caret blinks"},
     {"at": 0.12, "event": "types 'A language model / picks the likeliest word.'"},
     {"at": 0.50, "event": "'picks the likeliest word' turns terracotta, hesitates, backspaces"},
     {"at": 0.65, "event": "types 'rolls weighted dice'"},
     {"at": 0.90, "event": "final lines settle: 'A language model / rolls weighted dice.'"}],
    "hesitant-type", lead_silence_s=0.8,
    role_note="EXECUTIVE-SUMMARY LAW — misconception corrected: a chat model does not simply "
              "pick the single likeliest word; by default it samples from weighted odds."))

# ---------------------------------------------------------------- body
logit_chips = ", ".join(f"{t} {lg(z)}" for t, z in zip(TOK, Z))
beats.append(manim("B02", "B02_Machine", "FRAMEWORK", "structure",
    "Here's the machine. You type a prompt: the cat sat on the. The model doesn't hand back a word. "
    "It hands back a score for every token it knows, called a logit. Here are five of them. "
    "Softmax turns those scores into probabilities. A sampler rolls against those probabilities, "
    "picks one token, appends it, and the loop runs again.",
    [{"at": 0.03, "event": f"prompt chip '{ev['prompt']} ___' draws on at left"},
     {"at": 0.18, "event": "arrow into a 'model' box"},
     {"at": 0.32, "event": f"five logit bars grow out of the box: {logit_chips}; caption 'logits (constructed) — 5 of the whole vocabulary'"},
     {"at": 0.55, "event": "the bars pass through a 'softmax' box and come out as probability bars that sum to 1"},
     {"at": 0.72, "event": "a 'sampler' die rolls; 'mat' lights terracotta and slides into the prompt chip"},
     {"at": 0.88, "event": "a loop arrow draws from the prompt back into the model: 'next token'"}],
    "The next-token loop as a left-to-right machine: prompt → model → logits → softmax → probabilities → sampler → appended token → loop.",
    "Each stage draws on the word that names it; the chosen token physically travels back into the prompt.",
    visual_notes="Node-and-arrow diagram, NOT bars-as-hero; bars here are small. Spread across the full width (±6.0 x)."))

beats.append(manim("B03", "B03_Formula", "FRAMEWORK", "equation",
    "Softmax, written down. Take each token's logit and divide it by the temperature, T. "
    "Raise e to that power, so every score turns positive. Then divide by the same thing summed "
    "over every token, so the shares add up to exactly one. A bigger logit always means a bigger "
    "share. And temperature acts first, before the exponent.",
    [{"at": 0.05, "event": "MathTex typesets large: p_i = e^{z_i/T} / Σ_j e^{z_j/T}"},
     {"at": 0.16, "event": "box spotlight on z_i; label below: 'logit (a score)'"},
     {"at": 0.27, "event": "box spotlight on T; label: 'temperature (you choose it, T > 0)'"},
     {"at": 0.40, "event": "box spotlight on the numerator e^{z_i/T}; label: 'always positive'"},
     {"at": 0.58, "event": "box spotlight on the denominator Σ_j; label: 'same thing, summed over every token'"},
     {"at": 0.72, "event": "chip: 'all p_i add up to 1'"},
     {"at": 0.86, "event": "box spotlight returns to z_i/T: 'temperature acts first'"}],
    "Softmax-with-temperature typeset with MathTex, a box spotlight walking the symbols with a glossary label each.",
    "The spotlight walks the formula in narration order and ends on z_i/T, where temperature enters.",
    visual_notes="Box spotlights only (never underlines). Equation ≥120 pt; labels spread to fill ≥55% of canvas.",
    mathtex=r"p_i = \frac{e^{z_i/T}}{\sum_j e^{z_j/T}}"))

beats.append(manim("B04", "B04_WorkedT1", "WORKED_EXAMPLE", "mechanism",
    "Real numbers, at temperature one. Mat scores three point two; roof, zero point three. "
    "Raise e to each: mat becomes about twenty-four and a half, roof about one point three five. "
    "Add all five and you get about forty-eight. Divide each by forty-eight. Mat gets fifty-one "
    "percent, floor twenty-three, couch fourteen, bed nine, roof three. Those shares are the dice.",
    [{"at": 0.04, "event": "compact formula top-left (from B03) with T = 1 substituted; table header token | z | e^z | p"},
     {"at": 0.12, "event": "logit column fills: " + logit_chips},
     {"at": 0.30, "event": "e^z column fills row by row: " + ", ".join(f"{e:g}" for e in W["exp"])},
     {"at": 0.50, "event": f"the e^z column sums into a terracotta total: {W['sum']:g}"},
     {"at": 0.62, "event": f"each e^z divides by {W['sum']:g}; p column fills: " + ", ".join(pct(x) for x in W["pct"])},
     {"at": 0.88, "event": "the p column tips over into five horizontal probability bars: 'the dice'"}],
    "The B03 formula, visibly applied: an arithmetic table whose columns fill in formula order (exponentiate → sum → divide), executed values only.",
    "Each column fills on its spoken verb; the finished p column becomes the bars B05 will reshape.",
    visual_notes="Column headers z, e^z, p and the compact formula are MathTex, never plain-text carets.",
    mathtex=r"p_i = \frac{e^{z_i}}{\sum_j e^{z_j}} \quad (T = 1)"))

beats.append(manim("B05", "B05_TempSweep", "MECHANISM", "mechanism",
    "Now turn the knob. At zero point two, every logit is divided by zero point two, so every gap "
    "grows five times, and mat takes ninety-eight percent. At two, the gaps shrink by half: mat "
    "falls to thirty-five, and roof climbs from almost nothing to eight. Low temperature sharpens. "
    "High temperature flattens. And watch the order: it never changes.",
    [{"at": 0.03, "event": "five probability bars at T = 1 (from B04); a temperature dial at right reads 1"},
     {"at": 0.12, "event": "dial turns to 0.2; bars morph: " + ", ".join(f"{t} {pct(p)}" for t, p in zip(TOK, SW["0.2"]["pct"]))},
     {"at": 0.28, "event": "mat's bar lights terracotta at " + pct(SW["0.2"]["pct"][mat])},
     {"at": 0.45, "event": "dial turns through 1 to 2; bars flatten: " + ", ".join(f"{t} {pct(p)}" for t, p in zip(TOK, SW["2.0"]["pct"]))},
     {"at": 0.62, "event": f"roof's counter climbs {pct(SW['0.2']['pct'][roof])} → {pct(SW['2.0']['pct'][roof])}"},
     {"at": 0.75, "event": "labels 'sharpens' (T < 1) and 'flattens' (T > 1) land at the dial's ends"},
     {"at": 0.88, "event": "rank numbers 1–5 above the bars stay fixed through a final sweep 0.2 ↔ 2: 'order never changes'"}],
    "One set of five bars morphing live as a temperature dial sweeps 0.2 → 1 → 2, with percentage counters from evidence.json.",
    "The bars ARE the distribution; the dial is the only control; rank badges stay still while heights move."))

u_first = ev["runs20"]["u"][0]
beats.append(manim("B06", "B06_Rolls", "MECHANISM", "mechanism",
    "Here's where the answers start to differ. Lay the probabilities end to end, from zero to one. "
    "A seeded random number lands somewhere on that line, and whichever token owns that stretch wins. "
    "Now the same twenty rolls at each temperature. At zero point two: mat, twenty times out of "
    "twenty. At one: four different words. At two: all five, even roof.",
    [{"at": 0.04, "event": "the T = 1 bars lay end to end into one strip from 0 to 1, segments labelled by token"},
     {"at": 0.22, "event": f"a terracotta tick drops at u = {u_first:g}; the segment it lands in lights: '{R20['1.0']['picks'][0]}'"},
     {"at": 0.42, "event": "three strips stack (T = 0.2, 1, 2); the same 20 ticks drop on all three at once"},
     {"at": 0.58, "event": "row T = 0.2 fills with 20 word chips: all 'mat'"},
     {"at": 0.72, "event": f"row T = 1 fills: {R20['1.0']['distinct']} distinct words — " + ", ".join(f"{k} {v}" for k, v in R20['1.0']['counts'].items() if v)},
     {"at": 0.86, "event": f"row T = 2 fills: {R20['2.0']['distinct']} distinct words — " + ", ".join(f"{k} {v}" for k, v in R20['2.0']['counts'].items() if v) + "; 'roof' chip lights terracotta"}],
    "Inverse-CDF sampling made visible: a probability strip, a seeded tick, and the same 20 rolls producing 1 / 4 / 5 distinct words at T = 0.2 / 1 / 2.",
    "The same ticks fall on three strips simultaneously, so the only thing that differs is the temperature."))

k1 = K10["1.0"]
beats.append(manim("B07", "B07_TenThousand", "FALSIFIABILITY", "data",
    "Twenty rolls prove very little, so test the claim. If softmax really sets the odds, ten thousand "
    "rolls should land on its predicted shares, and they could have missed. At temperature one, it "
    "predicts fifty-one percent mat; the count comes back fifty-one point three. Across all three "
    "temperatures and all five tokens, nothing misses by even one point.",
    [{"at": 0.04, "event": "header: 'prediction: softmax shares · test: 10,000 seeded rolls'"},
     {"at": 0.18, "event": "T = 1: hollow 'predicted' outlines for five bars draw on"},
     {"at": 0.40, "event": f"solid 'counted' bars grow into them; mat counter: predicted {pct(k1['predicted_pct'][mat])} · counted {pct(k1['observed_pct'][mat])}"},
     {"at": 0.62, "event": "two small panels slide in beside it: T = 0.2 and T = 2, outlines and solid bars"},
     {"at": 0.82, "event": "gap chips per temperature: " + " · ".join(f"T = {T}: max gap {d['max_abs_gap_pct']:g} pts" for T, d in K10.items())},
     {"at": 0.92, "event": "terracotta verdict chip: 'prediction survives'"}],
    "A falsifiable prediction tested: predicted outlines vs counted bars over 10,000 executed draws at three temperatures.",
    "Counted bars grow into the predicted outlines, so a miss would be visible as a gap; side-by-side held ≥ 2 s."))

beats.append(manim("B08", "B08_Greedy", "MECHANISM", "mechanism",
    "Now push the knob toward zero. At zero point five, mat holds seventy-six percent. At zero point "
    "one, ninety-nine point nine seven. In the limit there's no roll at all: just take the top token. "
    "That's greedy decoding, and it's what temperature zero means, since the formula itself can't "
    "divide by zero. Same prompt, same answer, at least in principle.",
    [{"at": 0.04, "event": "the 0-to-1 strip from B06; the dial reads 1, mat's segment " + pct(TZ[1.0]['pct_top'])},
     {"at": 0.18, "event": f"dial clicks to 0.5: mat's segment widens to {TZ[0.5]['pct_top']:g}%"},
     {"at": 0.32, "event": f"dial clicks to 0.1: mat fills {TZ[0.1]['pct_top']:g}%; the other four collapse to a hairline"},
     {"at": 0.50, "event": "the strip becomes solid terracotta 'mat'; the random tick disappears: 'argmax — no roll'"},
     {"at": 0.66, "event": "MathTex note: T = 0 is a rule (take the max), not a value plugged into z_i/T"},
     {"at": 0.82, "event": "20 chips fill: 'mat' ×20; caption 'same prompt, same answer (in principle)'"}],
    "The strip from B06 collapsing as T → 0 until one token owns it: greedy decoding as the limit of softmax.",
    "The dial clicks down on each spoken value; the dice tick vanishes on 'no roll at all'.",
    mathtex=r"T \to 0^{+}:\quad p_i \to \begin{cases} 1 & \text{if } i = \arg \max_j z_j \\ 0 & \text{otherwise} \end{cases}"))

wt = WR["tokens"]
beats.append(manim("B09", "B09_WrongRanking", "FALSIFIABILITY", "mechanism",
    "And here's what the knob can't do. Suppose a model ranks Sydney just above Canberra as "
    "Australia's capital. At temperature one, it's wrong two times in three. Turn it down to zero "
    "point two: wrong more than four times in five. Greedy: wrong every time. Turn it up to two, and "
    "Canberra actually slips; Melbourne and Perth take the extra. Temperature changes the spread, "
    "never the ranking.",
    [{"at": 0.03, "event": f"prompt chip '{WR['prompt']} ___'; caption 'hypothetical model · constructed logits'; Canberra marked ✓ correct"},
     {"at": 0.14, "event": "four bars at T = 1: " + ", ".join(f"{t} {pct(p)}" for t, p in zip(wt, wr1["pct"])) + f"; counter 'wrong {pct(wr1['pct_wrong_cities'])}'"},
     {"at": 0.36, "event": "dial to 0.2: " + ", ".join(f"{t} {pct(p)}" for t, p in zip(wt, wr02["pct"])) + f"; counter 'wrong {pct(wr02['pct_wrong_cities'])}'"},
     {"at": 0.50, "event": "greedy: Sydney's bar fills to 100% terracotta; counter 'wrong 100%'"},
     {"at": 0.64, "event": "dial to 2: " + ", ".join(f"{t} {pct(p)}" for t, p in zip(wt, wr2["pct"])) + f"; Canberra's counter slips {pct(wr1['pct_correct'])} → {pct(wr2['pct_correct'])}"},
     {"at": 0.86, "event": "rank badges 1–4 unchanged through the whole sweep: 'spread, not ranking'"}],
    "A constructed wrong-ranking model: lowering T makes it consistently wrong, raising T spreads mass to other wrong cities.",
    "The 'wrong' counter climbs as the dial goes down; the rank badges never move."))

# ---------------------------------------------------------------- closing block
verdict = ["A model scores every token it knows; those scores are logits.",
           "Softmax turns logits into probabilities that add up to one.",
           "Temperature divides the logits first: low sharpens, high flattens.",
           "Sampling rolls those odds, so the same prompt can come back different.",
           "Temperature zero is greedy: always the top token, no dice.",
           "Temperature changes the spread, never the ranking."]
assert len(verdict) in (4, 6)
beats.append(remotion("BVDT", "VERDICT", "ClaudeVerdictArtifact", {
    "artifactTitle": "Verdict", "artifactHeading": "Softmax and temperature, in six lines",
    "artifactLines": verdict},
    "Let's recap with Claude. " + " ".join(verdict),
    [{"at": 0.05, "event": "verdict artifact card in on cream"},
     {"at": 0.15, "event": "heading types"},
     {"at": 0.25, "event": "lines 1–6 land on their spoken cue"}],
    "artifact-in", lead_silence_s=0.5))

prompt = ("Write a short Python script, no ML libraries, that applies softmax with temperature to five "
          "logits: mat 3.2, floor 2.4, couch 1.9, bed 1.5, roof 0.3. Print the probabilities at "
          "temperatures 0.2, 1 and 2. Then draw 1,000 seeded samples at each temperature and compare "
          "the counts with the probabilities. Finally, using only the printed numbers, explain what "
          "temperature can change and what it can't.")
assert [float(x) for x in "3.2 2.4 1.9 1.5 0.3".split()] == Z
spoken_prompt = ("Write a short Python script, no M L libraries, that applies softmax with temperature to "
                 "five logits: mat three point two, floor two point four, couch one point nine, bed one "
                 "point five, roof zero point three. Print the probabilities at temperatures zero point "
                 "two, one and two. Then draw one thousand seeded samples at each temperature and compare "
                 "the counts with the probabilities. Finally, using only the printed numbers, explain what "
                 "temperature can change and what it can't.")
beats.append(remotion("BHTF", "YOUR_TURN", "ClaudeComposerAsk", {
    "greeting": "Your turn.", "topic": "YOUR TURN · SOFTMAX AND TEMPERATURE",
    "segment": "Roll the dice yourself", "command": prompt,
    "runningText": "paste this into Claude…",
    "output": [f"check: at T = 1, mat ≈ {pct(W['pct'][mat])}, floor ≈ {pct(W['pct'][1])}, roof ≈ {pct(W['pct'][roof])}",
               "check: 1,000-draw counts land near the odds, not exactly on them",
               "check: the ranking holds at every T; 'lower T = more accurate' is not claimed"],
    "folderLabel": "@NikBearBrown", "modelLabel": "Claude"},
    "Your turn. Paste this into Claude: " + spoken_prompt + " "
    "Here's what to check. At temperature one, mat should come out at fifty-one percent. The "
    "thousand-draw counts should land near the probabilities, not exactly on them. And the ranking "
    "should hold at every temperature. If Claude says turning the temperature down makes answers more "
    "accurate, ask it to show you that in the numbers.",
    [{"at": 0.02, "event": "composer card in on cream"},
     {"at": 0.08, "event": "greeting 'Your turn.' types"},
     {"at": 0.15, "event": "the prompt types into the composer"},
     {"at": 0.62, "event": "runningText 'paste this into Claude…'"},
     {"at": 0.72, "event": "three check lines cascade in as each is spoken"}],
    "type-on", role_note="HANDOFF LAW — prompt read aloud verbatim (numbers spoken as words), then a 3-point rubric."))

beats.append(remotion("BOUT", "OUTRO", "ClaudeTitleOutro", {"title": TITLE + ".", "handle": "@NikBearBrown", "slug": SLUG},
    f"{TITLE}. At Nik Bear Brown.",
    [{"at": 0.02, "event": "cream page; polarity seeded from slug"},
     {"at": 0.10, "event": "title types"}, {"at": 0.55, "event": "handle @NikBearBrown"},
     {"at": 0.70, "event": "slug-seeded mascot animates under the handle"}],
    "outro-card", kind="outro_voice", tail_silence_s=1.0,
    role_note="OUTRO-LOCK — exact title restate, hardcoded handle, spoken, no music."))

sheet = {"metadata": {
    "title": TITLE, "slug": SLUG, "topic": TOPIC, "skill": "ai-explainer",
    "brand": "claude-liam", "channel": "claude-liam", "audience": "makers and curious learners who use chat models",
    "register": "Teardown", "engine": "kokoro", "voice": "am_onyx", "voice_kokoro": "am_onyx",
    "palette": "claude", "style_preset": "claude", "ground": "#FAF9F5", "aspect_ratio": "16:9",
    "greeting": GREETING, "persona": "Liam (in for Bear)", "in_for_bear": True,
    "folderLabel": "@NikBearBrown", "captions": False, "series_index": 2,
    "evidence": "demo/softmax_demo.py -> demo/evidence.json, demo/RUN-LOG.txt (seed 2)",
    # "a logit" is its own key: cut out alone, a phrase-final "a" is phonemized as the letter /ˈeɪ/
    "pronounce": {"logit": "ˈloʊdʒɪt", "logits": "ˈloʊdʒɪts", "a logit": "ɐ ˈloʊdʒɪt"},
    "tags": ["softmax", "temperature", "sampling", "language models", "greedy decoding",
             "next-token prediction", "probability"]},
    "beats": beats}
(HERE / "beat_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")

for b in beats:
    n = len(b["narration_text"].split())
    print(f"{b['beat_id']:5} {b.get('act',''):15} {n:4} words  ~{n/3.5:5.1f}s")
total = sum(len(b["narration_text"].split()) for b in beats)
print(f"total {total} words  ~{total/3.5/60:.2f} min (3.5 w/s, film-1 Kokoro rate)  ~{total/2.6/60:.2f} min (2.6 w/s planning rate)")
