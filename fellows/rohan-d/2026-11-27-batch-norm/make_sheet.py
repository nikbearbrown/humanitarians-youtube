#!/usr/bin/env python3
"""Builds beat_sheet.json for claude-liam-batch-norm (ai-explainer spine, Liam in for Bear)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "beat_sheet.json")
SLUG = "claude-liam-batch-norm"
TITLE = "Batch Normalization, One Rescale at a Time"
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
    "Hi, this is Liam, in for Bear. The ask: why does normalizing the numbers inside a network make it train faster? Show me with real numbers. Subtract the batch mean, divide by the spread. Every feature lands on one scale. The loss valley stops being a ravine.",
    22,
    rem("ClaudeComposerAsk", {
        "greeting": "Hi, Liam", "topic": "MACHINE LEARNING · BATCH NORMALIZATION",
        "segment": TITLE,
        "command": "Why does normalizing the numbers inside a network make it train faster? Show me with real numbers.",
        "runningText": "working through the math…", "folderLabel": FOLDER,
        "output": ["Working through the math…",
                   "the trick: subtract the batch mean and divide by the spread, so every feature lives on one scale",
                   "worked example: features on scales 5 and 500: condition number 3,182,113 raw, 1.4 normalized",
                   "where it bites: a batch of one has no spread, so every output is zero"]},
        [{"at": 0.0, "event": "the ask types into the composer"},
         {"at": 0.45, "event": "result lines land one by one"}]),
    qc="Cold-open composer: the ask and its result lines are the motion."))

beats.append(card("B01", "overview",
    "Normalization reshapes the landscape. It isn't just tidying. When features live on wildly different scales, the loss is a long narrow ravine. Put them on one scale and the ravine becomes a bowl.",
    14,
    rem("BrutalistHesitantWriter", {
        "text": "Normalization\njust tidies the numbers.",
        "triggerWords": "just tidies the numbers",
        "replacementWords": "reshapes the landscape",
        "fontSize": 140, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1,
        "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive framing"},
         {"at": 0.45, "event": "backspaces 'just tidies the numbers' and writes 'reshapes the landscape'"}]),
    lead_silence_s=0.8,
    motion_claim="The writer types the naive framing and corrects it on the spoken word.",
    qc="Hesitant-writer overview: the correction is the motion."))

beats.append(man("B02", "two scales",
    "Two features, one batch of four. Feature A reads two, four, six, eight. Feature B reads two hundred, four hundred, six hundred, eight hundred. Same shape, a hundred times the scale. Whatever the network does next, B will shout over A.",
    19, "Two rows of identical dots with numbers a hundred times apart.",
    [{"at": 0.1, "event": "row A: 2 4 6 8"},
     {"at": 0.45, "event": "row B: 200 400 600 800"},
     {"at": 0.8, "event": "'100 times' marker between the rows"}],
    "B02_Scales", "Same dot positions, numbers 100x apart, is the claim."))

beats.append(man("B03", "normalize A",
    "Normalize. Take A. The mean is five. The spread, the standard deviation, is two point two four. Subtract the mean: minus three, minus one, one, three. Divide by the spread: minus one point three four, minus point four five, point four five, one point three four.",
    22, "Subtract the mean, then divide by the spread.",
    [{"at": 0.1, "event": "formula writes in"},
     {"at": 0.3, "event": "row 1: 2 4 6 8"},
     {"at": 0.5, "event": "row 2: -3 -1 1 3"},
     {"at": 0.75, "event": "row 3: -1.34 -0.45 0.45 1.34"}],
    "B03_Normalize", "Three rows of numbers appearing in order is the claim."))

beats.append(man("B04", "normalize B",
    "Now B. The mean is five hundred. The spread, two hundred twenty-four. Subtract, divide, and the same four numbers come out. Feature A and feature B now speak at the same volume.",
    16, "Both features normalize to the same four numbers.",
    [{"at": 0.1, "event": "row B raw numbers"},
     {"at": 0.45, "event": "row B becomes -1.34 -0.45 0.45 1.34"},
     {"at": 0.8, "event": "both rows boxed"}],
    "B04_Same", "Two different rows landing on identical numbers is the claim."))

beats.append(man("B05", "the valley",
    "Why does that speed up training? The loss is a valley, like the one in the momentum film. With raw features, its steepest and flattest directions differ by a factor of three million. With normalized features, one point four. Normalized, gradient descent lands within a thousandth of the best loss in four steps. The raw run hasn't arrived after a hundred thousand.",
    27, "Condition number 3,182,113 against 1.4; 4 steps against over 100,000.",
    [{"at": 0.1, "event": "header: condition number"},
     {"at": 0.3, "event": "raw bar long, 3,182,113; normalized bar tiny, 1.4"},
     {"at": 0.65, "event": "steps: raw over 100,000; normalized 4"}],
    "B05_Valley", "A huge bar beside a sliver is the claim."))

beats.append(man("B06", "gamma and beta",
    "One more piece. Forcing every feature to mean zero and spread one might throw away something useful. So batch norm adds two learnable numbers, gamma and beta. Scale by gamma, shift by beta. With gamma two and beta one, those four numbers become minus one point six eight, point one one, one point eight nine, three point six eight.",
    24, "Learnable scale and shift undo the rescale if needed.",
    [{"at": 0.1, "event": "y = gamma x-hat + beta writes in"},
     {"at": 0.4, "event": "input row -1.34 -0.45 0.45 1.34"},
     {"at": 0.7, "event": "output row -1.68 0.11 1.89 3.68"}],
    "B06_GammaBeta", "The output row differing from the input row is the claim."))

beats.append(man("B07", "where it bites",
    "Where it bites. The mean and spread come from the batch. With a batch of one, the batch mean wobbles with a standard deviation of one. At thirty-two, point one eight. And a batch of one has no spread at all: subtract its own mean, and every output is zero.",
    21, "Small batches give noisy statistics; a batch of one gives zeros.",
    [{"at": 0.1, "event": "bars: batch size 1, 2, 8, 32 wobble 1.00, 0.71, 0.35, 0.18"},
     {"at": 0.7, "event": "readout: batch of one, output 0"}],
    "B07_SmallBatch", "Bars shrinking as the batch grows is the claim."))

beats.append(card("BVDT", "verdict",
    "Let's recap with Claude. Normalize each feature: subtract the batch mean, divide by the spread. A and B, a hundred times apart, become the same four numbers. The raw valley has a condition number of three million, the normalized one, one point four. Normalized, gradient descent is near the best loss in four steps. Gamma and beta let the network undo the rescale. And a batch of one has no spread: every output is zero.",
    36,
    rem("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": "Batch normalization, in six lines",
        "artifactLines": [
            "Normalize each feature: subtract the batch mean, divide by the spread.",
            "A [2, 4, 6, 8] and B [200, 400, 600, 800] both become [-1.34, -0.45, 0.45, 1.34].",
            "Condition number: 3,182,113 raw, 1.4 normalized.",
            "Normalized, gradient descent is within 0.001 of the best loss in 4 steps.",
            "Gamma and beta let the network undo the rescale if it needs to.",
            "A batch of one has no spread: every output is zero."]},
        [{"at": 0.0, "event": "artifact page opens"},
         {"at": 0.2, "event": "six verdict lines land in narration order"}]),
    lead_silence_s=0.5, qc="Mandated ClaudeVerdictArtifact bookend."))

PROMPT = ("Write a short Python script, numpy only, that normalizes the batches [2, 4, 6, 8] and [200, 400, 600, 800] "
          "by subtracting the mean and dividing by the standard deviation, and prints both. Then apply gamma = 2 and "
          "beta = 1 to the first result. Finally, normalize a batch containing one number and print it. Predict each "
          "output before you run it.")
beats.append(card("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + PROMPT +
    " Here's what to check. Both batches should print minus one point three four, minus point four five, point four five, one point three four. Gamma two and beta one should give minus one point six eight, point one one, one point eight nine, three point six eight. And the batch of one should print zero. See whether Claude explains why.",
    54,
    rem("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "BATCH NORMALIZATION · YOUR TURN",
        "segment": "Rescale Two Batches", "command": PROMPT,
        "runningText": "paste this into Claude…", "folderLabel": FOLDER,
        "modelLabel": "Fable 5", "effortLabel": "High",
        "output": ["Check: both batches print -1.34, -0.45, 0.45, 1.34.",
                   "Check: gamma 2, beta 1 give -1.68, 0.11, 1.89, 3.68.",
                   "Check: the batch of one prints 0, and Claude explains why."]},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.78, "event": "three check lines land"}])))

beats.append(card("BOUT", "outro", TITLE + ". At Nik Bear Brown.", 6,
    rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": FOLDER, "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot; Liam reads the title then 'At Nik Bear Brown'"}]),
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)"))

meta = {
    "slug": SLUG, "title": TITLE, "topic": "MACHINE LEARNING · BATCH NORMALIZATION",
    "skill": "ai-explainer", "style_preset": "claude", "brand": "claude-liam", "channel": "claude-liam",
    "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "a smart reader who wants to know why normalizing activations speeds up training",
    "greeting": "Hi, Liam", "greeting_note": "hello lexicon: Hindi. Wagwan is Bear's.",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "math_route": "MathText SVG (typeset_math.py); Manim MathTex unavailable (no dvisvgm)",
    "note": "Series film 5 of 6 after claude-liam-cross-entropy: same ai-explainer spine, numbers from experiment.py.",
    "tags": ["batch normalization", "generalization", "machine learning", "Claude", "Nik Bear Brown"],
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
