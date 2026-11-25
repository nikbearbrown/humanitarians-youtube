#!/usr/bin/env python3
"""Builds beat_sheet.json for claude-liam-cross-entropy (ai-explainer spine, Liam in for Bear)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "beat_sheet.json")
SLUG = "claude-liam-cross-entropy"
TITLE = "Cross-Entropy, One Surprise at a Time"
VOICE = dict(voice="am_onyx", engine="kokoro")
FOLDER = "@NikBearBrown"

def rem(pattern, props, show):
    return {"type": "REMOTION", "source": "own", "show": show,
            "remotion": {"pattern": pattern, "props": props}}

def card(bid, act, narr, est, shot, proof="SHOW", qc=None, **extra):
    b = {"beat_id": bid, "act": act, "proof_gate": proof, "narration_text": narr,
         "estimated_duration_s": est, **VOICE, "shot": shot}
    b.update(extra)
    if qc:
        b["qc"] = {"sparse_by_design": True, "sparse_reason": qc}
    return b

def man(bid, act, narr, est, intent, show, cls, claim):
    return {"beat_id": bid, "act": act, "proof_gate": "SHOW", "narration_text": narr,
            "estimated_duration_s": est, **VOICE,
            "shot": {"type": "GRAPHIC", "source": "own", "visual_intent": intent,
                     "show": show, "manim": {"class": cls}},
            "motion_claim": claim}

beats = []
beats.append(card("B00", "ask",
    "Hi, this is Liam, in for Bear. The ask: how does a classifier turn its scores into a loss, and why do confident mistakes cost so much? Show me with real numbers. Cross-entropy turns the scores into probabilities, then charges the model for how little probability it gave the right answer. A small miss costs little. Sure and wrong costs a lot.",
    26,
    rem("ClaudeComposerAsk", {
        "greeting": "Hi, Liam", "topic": "MACHINE LEARNING · CROSS-ENTROPY",
        "segment": TITLE,
        "command": "How does a classifier turn its scores into a loss? Show me why confident mistakes cost so much, with real numbers.",
        "runningText": "working through the math…", "folderLabel": FOLDER,
        "output": ["Working through the math…",
                   "the trick: loss is minus the log of the share given to the right answer",
                   "worked example: scores 2.0, 1.0, 0.1 give shares 0.66, 0.24, 0.10 and a loss of 0.417",
                   "where it bites: a 1% share costs 4.6, a 50% share costs 0.7"]},
        [{"at": 0.0, "event": "the ask types into the composer"},
         {"at": 0.45, "event": "result lines land one by one"}]),
    qc="Cold-open composer: the ask and its result lines are the motion."))

beats.append(card("B01", "overview",
    "Cross-entropy punishes confident mistakes. Not how many answers the model gets wrong, but how sure it was when it was wrong. That is why a model can be right most of the time and still be charged heavily.",
    14,
    rem("BrutalistHesitantWriter", {
        "text": "Cross-entropy\ncounts the mistakes.",
        "triggerWords": "counts the mistakes",
        "replacementWords": "punishes confident mistakes",
        "fontSize": 140, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1,
        "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive framing"},
         {"at": 0.45, "event": "backspaces 'counts the mistakes' and writes 'punishes confident mistakes'"}]),
    lead_silence_s=0.8,
    motion_claim="The writer types the naive framing and corrects it on the spoken word.",
    qc="Hesitant-writer overview: the correction is the motion."))

beats.append(man("B02", "scores to shares",
    "A model ends with one score per answer. Here, two, one, and point one for cat, dog and fox. Softmax turns them into shares that add up to one: sixty-six percent, twenty-four, ten. Say the right answer is cat. The model gave it sixty-six percent.",
    16, "Scores become shares; the right answer's share is the number that matters.",
    [{"at": 0.1, "event": "three scores appear: 2.0, 1.0, 0.1"},
     {"at": 0.4, "event": "bars grow: 66%, 24%, 10%"},
     {"at": 0.8, "event": "cat marked 'right answer', its bar terracotta"}],
    "B02_Shares", "Scores turning into bars is the claim."))

beats.append(man("B03", "the charge",
    "Now the charge. The loss is minus the natural log of the share given to the right answer. Sixty-six percent gives a loss of point four one seven. Give the right answer more, and the loss shrinks. Give it less, and the loss grows.",
    16, "One line turns the right answer's share into a loss.",
    [{"at": 0.1, "event": "L = −ln p_right writes in"},
     {"at": 0.5, "event": "−ln(0.659) = 0.417 appears beneath"},
     {"at": 0.85, "event": "the p box is highlighted"}],
    "B03_Charge", "The two equations landing in order is the claim."))

beats.append(man("B04", "the curve",
    "Here is that charge for every share. Ninety percent costs point one. Fifty percent, point seven. Ten percent, two point three. One percent, four point six. The curve doesn't flatten as the answer gets worse. It climbs.",
    18, "The cost curve climbs steeply as the right answer's share falls.",
    [{"at": 0.1, "event": "axes and curve draw"},
     {"at": 0.3, "event": "points land at 0.9, 0.5, 0.1, 0.01 on the spoken values"},
     {"at": 0.85, "event": "last point 0.01 turns terracotta"}],
    "B04_Curve", "Points landing higher and higher on the curve is the claim."))

beats.append(man("B05", "two models",
    "Two models, three questions, and both get two right. Same accuracy, sixty-seven percent. Model A is confident: ninety, ninety and ten percent on the true answer. Mean loss, point eight four. Model B hedges: sixty, sixty and forty. Mean loss, point six five. Accuracy can't tell them apart. Cross-entropy can.",
    22, "Equal accuracy, different loss: confidence in the wrong answer is what gets charged.",
    [{"at": 0.1, "event": "Model A bars and Model B bars appear"},
     {"at": 0.45, "event": "accuracy 67% under both"},
     {"at": 0.75, "event": "mean loss 0.84 vs 0.65 land; A's third bar turns terracotta"}],
    "B05_TwoModels", "Same accuracy readout, different loss readout, is the claim."))

beats.append(man("B06", "one step",
    "How does the model learn from it? The slope on each score is just the share minus the answer, where the right one counts as one. Minus point three four one, plus point two four two, plus point oh nine nine. Step against the slope, with step size one. Cat's score rises to two point three four, and the loss drops from point four one seven to point two six four.",
    26, "The slope is share minus answer; one step raises the right score and lowers the loss.",
    [{"at": 0.1, "event": "three bars with slope readouts −0.341, +0.242, +0.099"},
     {"at": 0.55, "event": "bars morph to the post-step shares"},
     {"at": 0.8, "event": "loss readout 0.417 → 0.264"}],
    "B06_Step", "Bars morphing after the step is the claim."))

beats.append(man("B07", "where it bites",
    "Where it bites. If the model gives the right answer a share of zero, the log is infinite. Real code clips the share, say at one in a trillion, and the loss lands at twenty-seven point six. One confident mistake can outweigh a thousand near-perfect answers.",
    19, "One clipped confident mistake outweighs a thousand near-perfect answers.",
    [{"at": 0.1, "event": "p = 0 → loss ∞ readout"},
     {"at": 0.45, "event": "clip at 10⁻¹² → one bar 27.6"},
     {"at": 0.75, "event": "a second bar of 1,000 answers at 99%: total 10.05"}],
    "B07_Bites", "The single tall bar beside the shorter thousand-answer bar is the claim."))

beats.append(card("BVDT", "verdict",
    "Let's recap with Claude. The loss is minus the log of the share given to the right answer. Scores two, one and point one give shares sixty-six, twenty-four and ten, a loss of point four one seven. The cost climbs steeply as that share falls. Accuracy can't separate a confident model from a hedging one, the loss can. The slope on each score is share minus answer. And a share of zero makes the loss infinite, so real code clips it.",
    38,
    rem("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": "Cross-entropy, in six lines",
        "artifactLines": [
            "Loss is minus the log of the share given to the right answer.",
            "Scores 2.0, 1.0, 0.1 become shares 0.66, 0.24, 0.10: loss 0.417.",
            "The cost climbs steeply as the right answer's share falls.",
            "Accuracy can't tell confident from hedged; the loss can.",
            "The slope on each score is share minus answer.",
            "A share of zero makes the loss infinite, so real code clips it."]},
        [{"at": 0.0, "event": "artifact page opens"},
         {"at": 0.2, "event": "six verdict lines land in narration order"}]),
    lead_silence_s=0.5, qc="Mandated ClaudeVerdictArtifact bookend."))

PROMPT = ("Write a short Python script, no ML libraries, that turns the scores 2.0, 1.0 and 0.1 into shares with softmax "
          "and prints the cross-entropy loss when each of the three classes is the right answer. Then take one gradient "
          "step on the scores with step size 1.0, using share minus answer, and print the new loss for class 0. "
          "Before running it, predict which class costs the most.")
beats.append(card("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + PROMPT +
    " Here's what to check. Class zero should cost point four one seven, class one one point four one seven, and class two two point three one seven. After one step the loss for class zero should fall to about point two six four. And see whether Claude explains why the smallest share costs the most, rather than just printing it.",
    58,
    rem("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "CROSS-ENTROPY · YOUR TURN",
        "segment": "Price Every Mistake", "command": PROMPT,
        "runningText": "paste this into Claude…", "folderLabel": FOLDER,
        "modelLabel": "Fable 5", "effortLabel": "High",
        "output": ["Check: class 0 costs 0.417, class 1 costs 1.417, class 2 costs 2.317.",
                   "Check: after one step the class 0 loss falls to about 0.264.",
                   "Check: Claude explains why the smallest share costs the most."]},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.78, "event": "three check lines land"}])))

beats.append(card("BOUT", "outro", TITLE + ". At Nik Bear Brown.", 6,
    rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": FOLDER, "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot; Liam reads the title then 'At Nik Bear Brown'"}]),
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)"))

meta = {
    "slug": SLUG, "title": TITLE, "topic": "MACHINE LEARNING · CROSS-ENTROPY",
    "skill": "ai-explainer", "style_preset": "claude", "brand": "claude-liam", "channel": "claude-liam",
    "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "a smart reader who has met softmax and wants to know why the loss punishes confident mistakes",
    "greeting": "Hi, Liam", "greeting_note": "hello lexicon: Hindi. Wagwan is Bear's.",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "math_route": "MathText SVG (typeset_math.py); Manim MathTex unavailable (no dvisvgm)",
    "note": "Sibling of claude-liam-gradient-descent and claude-liam-backpropagation: same ai-explainer spine, real numbers recomputed in experiment.py.",
    "tags": ["cross-entropy", "softmax", "loss", "machine learning", "Claude", "Nik Bear Brown"],
}

if os.path.exists(OUT):
    old = {b["beat_id"]: b for b in json.load(open(OUT))["beats"]}
    for b in beats:
        for k in ("audio_file", "actual_duration_s"):
            if k in old.get(b["beat_id"], {}):
                b[k] = old[b["beat_id"]][k]
for b in beats:
    act, est = b.get("actual_duration_s"), b["estimated_duration_s"]
    props = (b["shot"].get("remotion") or {}).get("props")
    if act and props is not None and "durationSeconds" in props:
        props["durationSeconds"] = round(act, 2)
json.dump({"metadata": meta, "beats": beats}, open(OUT, "w"), indent=1, ensure_ascii=False)
print("wrote", OUT, {b["beat_id"]: len(b["narration_text"].split()) for b in beats})
