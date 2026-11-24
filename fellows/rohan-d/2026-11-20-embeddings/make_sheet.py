#!/usr/bin/env python3
"""Builds beat_sheet.json for claude-liam-embeddings (ai-explainer spine, Liam in for Bear)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "beat_sheet.json")
SLUG = "claude-liam-embeddings"
TITLE = "Embeddings, One Angle at a Time"
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
    "Hi, this is Liam, in for Bear. The ask: how does a model tell that two words mean similar things? Show me with real numbers. Turn each word into a list of numbers, a vector, then compare the angle between them. Length can fool you. Direction doesn't.",
    22,
    rem("ClaudeComposerAsk", {
        "greeting": "Hi, Liam", "topic": "MACHINE LEARNING · EMBEDDINGS",
        "segment": TITLE,
        "command": "How does a model tell that two words mean similar things? Show me with real numbers.",
        "runningText": "working through the math…", "folderLabel": FOLDER,
        "output": ["Working through the math…",
                   "the trick: turn each word into a list of numbers and compare the angle between them",
                   "worked example: cat (4, 1), dog (3, 2), car (1, 4): cat and dog score 0.94, cat and car 0.47",
                   "where it bites: distance is fooled by length, cat times 3 is far from cat but scores 1.00"]},
        [{"at": 0.0, "event": "the ask types into the composer"},
         {"at": 0.45, "event": "result lines land one by one"}]),
    qc="Cold-open composer: the ask and its result lines are the motion."))

beats.append(card("B01", "overview",
    "Similar words have similar directions. Not similar sizes, and not similar spellings. Two vectors that point the same way mean the same kind of thing, however long they are. Then the model can compare any two words by the angle between them.",
    14,
    rem("BrutalistHesitantWriter", {
        "text": "Similar words\nhave similar numbers.",
        "triggerWords": "similar numbers",
        "replacementWords": "similar directions",
        "fontSize": 140, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1,
        "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive framing"},
         {"at": 0.45, "event": "backspaces 'similar numbers' and writes 'similar directions'"}]),
    lead_silence_s=0.8,
    motion_claim="The writer types the naive framing and corrects it on the spoken word.",
    qc="Hesitant-writer overview: the correction is the motion."))

beats.append(man("B02", "words as arrows",
    "Give every word a list of numbers. Here is a toy plane with two numbers per word. Furry along the bottom, vehicle up the side. Cat is four, one. Dog is three, two. Car is one, four. Similar words land near each other.",
    18, "Three words as arrows from the origin.",
    [{"at": 0.1, "event": "axes: furry, vehicle"},
     {"at": 0.35, "event": "cat arrow, then dog, then car, each with its numbers"}],
    "B02_Plane", "Arrows landing in different directions is the claim."))

beats.append(man("B03", "distance fails",
    "The obvious way to compare is distance. Cat to car, four point two. Now say a document uses cat three times as often. Cat times three is twelve, three. Its distance to cat is eight point two, farther than the car. Distance says a cat is less like a cat than a car is.",
    22, "Scaling cat makes it look farther from itself than from car.",
    [{"at": 0.1, "event": "cat, dog, car arrows"},
     {"at": 0.3, "event": "dashed line cat to car: 4.2"},
     {"at": 0.6, "event": "cat x3 arrow; dashed line cat to cat x3: 8.2"}],
    "B03_Distance", "A long dashed line to the scaled cat is the claim."))

beats.append(man("B04", "direction",
    "Compare direction instead. Cat points up at fourteen degrees, dog at thirty-four, car at seventy-six. Cat to dog, twenty degrees. Cat to car, sixty-two. And cat times three points exactly where cat points. Zero degrees.",
    19, "Angles between arrows; the scaled cat shares cat's direction.",
    [{"at": 0.1, "event": "cat, dog, car arrows"},
     {"at": 0.35, "event": "arc cat to dog: 20 degrees"},
     {"at": 0.55, "event": "arc cat to car: 62 degrees"},
     {"at": 0.8, "event": "cat x3 lies on cat: 0 degrees"}],
    "B04_Angle", "Arcs between arrows are the claim."))

beats.append(man("B05", "cosine",
    "The score for that angle is its cosine. Dot product, over the two lengths. Cat dot dog is fourteen. The lengths are four point one two and three point six one. Fourteen over fourteen point nine is point nine four. Same direction scores one.",
    20, "Cosine = dot product over the product of lengths.",
    [{"at": 0.15, "event": "cosine formula writes in"},
     {"at": 0.5, "event": "worked numbers for cat and dog"},
     {"at": 0.85, "event": "the answer 0.94 is boxed"}],
    "B05_Cosine", "The two equations landing in order is the claim."))

beats.append(man("B06", "every pair",
    "Score every pair. Cat and dog, point nine four. Dog and car, point seven four. Cat and car, point four seven. And cat against three cats, one point oh oh. Direction decides. Length doesn't.",
    16, "Cosines for the pairs; the scaled cat scores 1.00.",
    [{"at": 0.15, "event": "four bars grow: 0.94, 0.74, 0.47, 1.00"},
     {"at": 0.85, "event": "the 1.00 bar turns terracotta"}],
    "B06_Pairs", "Four bars of different lengths is the claim."))

beats.append(man("B07", "where it bites",
    "Where it bites. Cosine says near, not same. Cat and dog score point nine four, but they aren't interchangeable. And a vector of zeros has no direction at all. Its cosine is zero divided by zero. Undefined.",
    17, "High cosine is not identity; a zero vector has no cosine.",
    [{"at": 0.15, "event": "rows: cat vs dog 0.94, cat vs 3 cats 1.00"},
     {"at": 0.6, "event": "row: cat vs zeros, an empty dashed bar, undefined"}],
    "B07_Bites", "An empty dashed bar for the zero vector is the claim."))

beats.append(card("BVDT", "verdict",
    "Let's recap with Claude. An embedding turns a word into a list of numbers. Distance is fooled by length: cat to three cats is eight point two, farther than cat to car. Cosine compares direction, dot product over the two lengths. Cat and dog score point nine four, cat and car point four seven, cat and three cats one. Near is not the same. And a zero vector has no direction, so its cosine is undefined.",
    36,
    rem("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": "Embeddings, in six lines",
        "artifactLines": [
            "An embedding turns a word into a list of numbers.",
            "Distance is fooled by length: cat to 3 cats is 8.2, cat to car is 4.2.",
            "Cosine compares direction: dot product over the two lengths.",
            "Cat and dog score 0.94, cat and car 0.47, cat and 3 cats 1.00.",
            "Near is not the same: cat and dog score 0.94 but differ.",
            "A zero vector has no direction, so its cosine is undefined."]},
        [{"at": 0.0, "event": "artifact page opens"},
         {"at": 0.2, "event": "six verdict lines land in narration order"}]),
    lead_silence_s=0.5, qc="Mandated ClaudeVerdictArtifact bookend."))

PROMPT = ("Write a short Python script, no ML libraries, that computes the distance and the cosine between "
          "cat = (4, 1) and each of dog = (3, 2), car = (1, 4) and cat times 3 = (12, 3). Before running it, predict "
          "which of the three each measure ranks closest to cat.")
beats.append(card("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + PROMPT +
    " Here's what to check. Distance should rank dog, then car, then cat times three: one point four one, four point two four, eight point two five. Cosine should rank cat times three, then dog, then car: one, point nine four, point four seven. And see whether Claude explains why the two measures disagree about cat times three.",
    52,
    rem("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "EMBEDDINGS · YOUR TURN",
        "segment": "Compare Two Rulers", "command": PROMPT,
        "runningText": "paste this into Claude…", "folderLabel": FOLDER,
        "modelLabel": "Fable 5", "effortLabel": "High",
        "output": ["Check: distance ranks dog, car, then cat times 3 (1.41, 4.24, 8.25).",
                   "Check: cosine ranks cat times 3, dog, car (1.00, 0.94, 0.47).",
                   "Check: Claude explains why they disagree about cat times 3."]},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.78, "event": "three check lines land"}])))

beats.append(card("BOUT", "outro", TITLE + ". At Nik Bear Brown.", 6,
    rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": FOLDER, "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot; Liam reads the title then 'At Nik Bear Brown'"}]),
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)"))

meta = {
    "slug": SLUG, "title": TITLE, "topic": "MACHINE LEARNING · EMBEDDINGS",
    "skill": "ai-explainer", "style_preset": "claude", "brand": "claude-liam", "channel": "claude-liam",
    "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "a smart reader who wants to know how a model compares two word vectors",
    "greeting": "Hi, Liam", "greeting_note": "hello lexicon: Hindi. Wagwan is Bear's.",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "math_route": "MathText SVG (typeset_math.py); Manim MathTex unavailable (no dvisvgm)",
    "note": "Series film 4 of 6 after claude-liam-cross-entropy: same ai-explainer spine, numbers from experiment.py.",
    "tags": ["embeddings", "generalization", "machine learning", "Claude", "Nik Bear Brown"],
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
