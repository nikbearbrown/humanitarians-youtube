#!/usr/bin/env python3
"""Builds beat_sheet.json for claude-liam-kmeans (ai-explainer spine, Liam in for Bear)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "beat_sheet.json")
SLUG = "claude-liam-kmeans"
TITLE = "K-Means, One Reassignment at a Time"
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
    "Hi, this is Liam, in for Bear. The ask: how does k-means find groups in data that has no labels? Show me with real numbers. Guess two centers. Give every point to its nearest center. Move each center to the mean of its points. Repeat until nothing moves.",
    22,
    rem("ClaudeComposerAsk", {
        "greeting": "Hi, Liam", "topic": "MACHINE LEARNING · K-MEANS",
        "segment": TITLE,
        "command": "How does k-means find groups in data that has no labels? Show me with real numbers.",
        "runningText": "working through the math…", "folderLabel": FOLDER,
        "output": ["Working through the math…",
                   "the trick: guess centers, give each point to the nearest, move each center to the mean, repeat",
                   "worked example: 7 points, centers from (1, 1) and (5, 6) settle in 2 rounds at (1.25, 1.5) and (3.9, 5.1)",
                   "where it bites: a bad start settles on a worse split, inertia 16 instead of 4"]},
        [{"at": 0.0, "event": "the ask types into the composer"},
         {"at": 0.45, "event": "result lines land one by one"}]),
    qc="Cold-open composer: the ask and its result lines are the motion."))

beats.append(card("B01", "overview",
    "K-means settles on a stable guess. It doesn't discover the true groups. It finds a grouping that stops changing, and where it stops depends on where it started. Same data, different start, different answer.",
    14,
    rem("BrutalistHesitantWriter", {
        "text": "K-means\nfinds the true groups.",
        "triggerWords": "finds the true groups",
        "replacementWords": "settles on a stable guess",
        "fontSize": 140, "charMs": 26, "hesitateBetween": 8, "hesitateWithin": 1,
        "mistakeRate": 5, "jitter": 20, "seed": SLUG, "banner": ""},
        [{"at": 0.0, "event": "types the naive framing"},
         {"at": 0.45, "event": "backspaces 'finds the true groups' and writes 'settles on a stable guess'"}]),
    lead_silence_s=0.8,
    motion_claim="The writer types the naive framing and corrects it on the spoken word.",
    qc="Hesitant-writer overview: the correction is the motion."))

beats.append(man("B02", "the start",
    "Seven points on a plane. We want two groups. Pick two starting centers: one, one, and five, six. Nothing about the data told us where to start. Any two spots would do.",
    16, "Seven points and two starting centers.",
    [{"at": 0.1, "event": "seven points appear"},
     {"at": 0.5, "event": "two center squares appear at (1,1) and (5,6)"}],
    "B02_Start", "Seven dots and two squares is the claim."))

beats.append(man("B03", "assign",
    "Assign. Take the point three, four. Distance to the first center: three point six. To the second: two point eight. It joins the second. Do that for every point: two go to the first center, five to the second.",
    18, "Each point joins its nearest center.",
    [{"at": 0.1, "event": "point (3,4) highlighted; two distance lines"},
     {"at": 0.45, "event": "readouts 3.6 and 2.8"},
     {"at": 0.75, "event": "all points joined to their nearest center: 2 and 5"}],
    "B03_Assign", "Lines from points to their nearest square is the claim."))

beats.append(man("B04", "update",
    "Update. Move each center to the mean of its points. The first group, one, one and one point five, two, has its mean at one point two five, one point five. The second group's five points have their mean at three point nine, five point one.",
    19, "Each center moves to the mean of its group.",
    [{"at": 0.15, "event": "center 1 slides to (1.25, 1.5)"},
     {"at": 0.5, "event": "center 2 slides to (3.9, 5.1)"}],
    "B04_Update", "The squares sliding to the group means is the claim."))

beats.append(man("B05", "repeat",
    "Repeat. Assign again from the new centers. Every point stays where it was. Nothing moves, so we're done. Two rounds.",
    11, "A second assignment changes nothing.",
    [{"at": 0.2, "event": "assignment lines redraw from the new centers: identical"},
     {"at": 0.7, "event": "readout: no point changed, 2 rounds"}],
    "B05_Repeat", "The same grouping appearing again is the claim."))

beats.append(man("B06", "inertia",
    "Is it getting better? Add up the squared distances from each point to its center. That's the inertia. At the starting centers, nineteen point two five. After one update, eight point five three. And it can't go up. Each step lowers it or leaves it alone.",
    21, "Inertia falls from 19.25 to 8.53 and never rises.",
    [{"at": 0.15, "event": "bar: start 19.25"},
     {"at": 0.5, "event": "bar: after one update 8.53"},
     {"at": 0.85, "event": "caption: never rises"}],
    "B06_Inertia", "A shorter second bar is the claim."))

beats.append(man("B07", "where it bites",
    "Where it bites. Four points at the corners of a rectangle, four wide and two tall. Start the centers on the middles of the short sides: they split left from right, inertia four. Start them on the middles of the long sides: top from bottom, inertia sixteen. Both are stable. So run it from several starts, and keep the lowest inertia.",
    26, "Two starts settle on two different stable splits.",
    [{"at": 0.15, "event": "rectangle with start 1: vertical split, inertia 4"},
     {"at": 0.55, "event": "rectangle with start 2: horizontal split, inertia 16"},
     {"at": 0.85, "event": "the 16 label turns terracotta"}],
    "B07_BadStart", "Two panels with different splits is the claim."))

beats.append(card("BVDT", "verdict",
    "Let's recap with Claude. K-means guesses centers, assigns each point to the nearest one, moves each center to the mean, and repeats. The point three, four is three point six from one center and two point eight from the other. Starting from one, one and five, six, it settles in two rounds at one point two five, one point five and three point nine, five point one. Inertia falls from nineteen point two five to eight point five three, and never rises. A different start can settle on a worse split, so run it several times.",
    38,
    rem("ClaudeVerdictArtifact", {
        "artifactTitle": "Verdict", "artifactHeading": "K-means, in six lines",
        "artifactLines": [
            "K-means guesses centers, assigns points, moves centers to the mean, repeats.",
            "A point joins its nearest center: (3, 4) is 3.6 from one, 2.8 from the other.",
            "Starting at (1, 1) and (5, 6) it settles in 2 rounds at (1.25, 1.5) and (3.9, 5.1).",
            "Inertia falls from 19.25 to 8.53 and never rises.",
            "A different start can settle on a worse split: inertia 16 instead of 4.",
            "So run it from several starts and keep the lowest inertia."]},
        [{"at": 0.0, "event": "artifact page opens"},
         {"at": 0.2, "event": "six verdict lines land in narration order"}]),
    lead_silence_s=0.5, qc="Mandated ClaudeVerdictArtifact bookend."))

PROMPT = ("Write a short Python script, no ML libraries, that runs k-means with k = 2 on the points (1,1), (1.5,2), "
          "(3,4), (5,7), (3.5,5), (4.5,5) and (3.5,4.5), starting the centers at (1,1) and (5,6). Print the labels, "
          "the centers and the inertia after each round, and stop when nothing changes. Then run it on the rectangle "
          "corners (0,0), (0,2), (4,0) and (4,2) from the starts (0,1),(4,1) and (2,0),(2,2), and print each final inertia.")
beats.append(card("BHTF", "your turn",
    "Your turn. Paste this into Claude: " + PROMPT +
    " Here's what to check. The first run should end at one point two five, one point five and three point nine, five point one, with inertia eight point five three. The rectangle should give inertia four from one start and sixteen from the other. And see whether Claude explains why both answers are stable.",
    62,
    rem("ClaudeComposerAsk", {
        "greeting": "Your turn.", "topic": "K-MEANS · YOUR TURN",
        "segment": "Break The Start", "command": PROMPT,
        "runningText": "paste this into Claude…", "folderLabel": FOLDER,
        "modelLabel": "Fable 5", "effortLabel": "High",
        "output": ["Check: the first run ends at (1.25, 1.5) and (3.9, 5.1), inertia 8.53.",
                   "Check: the rectangle gives inertia 4 from one start and 16 from the other.",
                   "Check: Claude explains why both answers are stable."]},
        [{"at": 0.0, "event": "Composer opens — 'Your turn.'"},
         {"at": 0.1, "event": "the prompt types in full"},
         {"at": 0.78, "event": "three check lines land"}])))

beats.append(card("BOUT", "outro", TITLE + ". At Nik Bear Brown.", 6,
    rem("ClaudeTitleOutro", {"title": TITLE, "slug": SLUG, "handle": FOLDER, "subline": ""},
        [{"at": 0.0, "event": "title restates; handle; slug-seeded mascot; Liam reads the title then 'At Nik Bear Brown'"}]),
    kind="outro_voice", tail_silence_s=1.0,
    hold_note="spoken outro + 1.0 s silent tail (apad); no jingle (OUTRO-LOCK §Voice)"))

meta = {
    "slug": SLUG, "title": TITLE, "topic": "MACHINE LEARNING · K-MEANS",
    "skill": "ai-explainer", "style_preset": "claude", "brand": "claude-liam", "channel": "claude-liam",
    "persona": "Liam (in for Bear)", "voice": "am_onyx", "voice_kokoro": "am_onyx", "engine": "kokoro",
    "clock": "narration", "palette": "claude", "register": "Teardown",
    "fps": 24, "aspect_ratio": "16:9", "width": 3840, "height": 2160, "caption_policy": "none",
    "audience": "a smart reader who wants to know how k-means finds groups and why its start matters",
    "greeting": "Hi, Liam", "greeting_note": "hello lexicon: Hindi. Wagwan is Bear's.",
    "typography": {"serif": "Tiempos/EB Garamond", "ui": "system sans", "mono": "SF Mono"},
    "math_route": "no typeset equations in this film",
    "note": "Series film 6 of 6 after claude-liam-cross-entropy: same ai-explainer spine, numbers from experiment.py.",
    "tags": ["k-means", "generalization", "machine learning", "Claude", "Nik Bear Brown"],
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
